#!/usr/bin/env python3
"""Query and update the NotVanilla Notion mods database via the public API."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import pathlib
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from difflib import SequenceMatcher
import unicodedata
from typing import Any


ROOT = pathlib.Path(__file__).resolve().parents[1]
DOTENV_PATH = ROOT / ".env"

DEFAULT_API_VERSION = "2022-06-28"
DEFAULT_TITLE_PROPERTY = "Mod"

AUDIT_FIELDS = ("Status", "Ambiente", "Prioridade", "Categoria", "Módulo", "Manifesto")

PRIORITY_MAP = {
    "very high": "5 - Muito Alta",
    "high": "4 - Alta",
    "medium": "3 - Média",
    "low": "2 - Baixa",
    "very low": "1 - Muito Baixa",
}

MODULE_VALUE_MAP = {
    "Interface, inventário e HUD": "Interface e inventário e HUD",
}

TITLE_SUFFIX_PATTERNS = (
    r"\s*-\s*minecraft\s+mods?\s*-\s*curseforge\s*$",
    r"\s*-\s*minecraft\s+mods?\s*$",
    r"\s*-\s*minecraft\s+mod\s*$",
    r"\s*-\s*minecraft\s+data\s+pack\s*$",
    r"\s*-\s*minecraft\s+resource\s+pack\s*$",
    r"\s*-\s*minecraft\s+resourcepacks?\s*$",
    r"\s*-\s*minecraft\s+shader\s*$",
    r"\s*-\s*minecraft\s+shaderpacks?\s*$",
    r"\s*-\s*minecraft\s+plugin\s*$",
    r"\s*\[(fabric|forge)\]\s*$",
)

SELECT_FIELDS = {"Status", "Ambiente", "Prioridade", "Módulo"}
MULTI_SELECT_FIELDS = {"Categoria"}
URL_FIELDS = {"Página"}
RICH_TEXT_FIELDS = {"Manifesto", "Dependências", "Incompatibilidades", "Notas"}
DATE_FIELDS = {"Última revisão"}
TITLE_FIELDS = {DEFAULT_TITLE_PROPERTY}


def load_dotenv(path: pathlib.Path) -> None:
    if not path.exists():
        return
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip("'").strip('"')
        os.environ.setdefault(key, value)


def env(name: str, default: str | None = None) -> str:
    value = os.getenv(name)
    if value is None or value == "":
        if default is not None:
            return default
        raise SystemExit(f"missing required environment variable: {name}")
    return value


def notion_headers() -> dict[str, str]:
    return {
        "Authorization": f"Bearer {env('NOTION_API_KEY')}",
        "Content-Type": "application/json",
        "Notion-Version": env("NOTION_API_VERSION", DEFAULT_API_VERSION),
        "Accept": "application/json",
    }


def notion_request(method: str, path: str, payload: dict[str, Any] | None = None) -> dict[str, Any]:
    data = None if payload is None else json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        f"https://api.notion.com/v1{path}",
        data=data,
        method=method,
        headers=notion_headers(),
    )
    try:
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(
            f"Notion API {method} {path} failed with HTTP {exc.code}: {body}"
        ) from exc
    return json.loads(body)


def database_id() -> str:
    explicit = os.getenv("NOTION_DATABASE_ID") or os.getenv("NOTION_MODS_DATABASE_ID")
    if explicit:
        return explicit.strip().replace("-", "")
    raise SystemExit(
        "missing required environment variable: NOTION_DATABASE_ID"
    )


def fetch_all_rows() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    payload: dict[str, Any] = {"page_size": 100}
    while True:
        data = notion_request("POST", f"/databases/{database_id()}/query", payload)
        rows.extend(data.get("results", []))
        if not data.get("has_more"):
            return rows
        payload["start_cursor"] = data["next_cursor"]


def rich_text_to_plain(value: list[dict[str, Any]] | None) -> str:
    if not value:
        return ""
    return "".join(piece.get("plain_text", "") for piece in value)


def multi_select_to_plain(value: list[dict[str, Any]] | None) -> str:
    if not value:
        return ""
    return ", ".join(piece.get("name", "") for piece in value if piece.get("name"))


def select_name(prop: dict[str, Any] | None) -> str:
    if not prop:
        return ""
    value = prop.get("select")
    if not value:
        return ""
    return str(value.get("name") or "")


def page_title(page: dict[str, Any]) -> str:
    properties = page.get("properties", {})
    title_prop = properties.get(DEFAULT_TITLE_PROPERTY, {})
    return rich_text_to_plain(title_prop.get("title"))


def page_title_link(page: dict[str, Any]) -> str:
    properties = page.get("properties", {})
    title_prop = properties.get(DEFAULT_TITLE_PROPERTY, {})
    for item in title_prop.get("title", []) or []:
        text = item.get("text", {})
        link = text.get("link") or {}
        url = link.get("url")
        if url:
            return url
        href = item.get("href")
        if href:
            return href
    return ""


def is_blank_property(prop: dict[str, Any] | None) -> bool:
    if not prop:
        return True
    prop_type = prop.get("type")
    value = prop.get(prop_type)
    if prop_type == "title":
        return not value
    if prop_type == "select":
        return not value or not value.get("name")
    if prop_type == "multi_select":
        return not value
    if prop_type == "date":
        return not value or not value.get("start")
    if prop_type == "url":
        return not value
    if prop_type == "rich_text":
        return not value
    return value in (None, "", [], {})


def row_field(page: dict[str, Any], field_name: str) -> dict[str, Any] | None:
    return page.get("properties", {}).get(field_name)


def row_summary(page: dict[str, Any]) -> dict[str, Any]:
    props = page.get("properties", {})
    return {
        "id": page.get("id"),
        "title": page_title(page),
        "status": select_name(props.get("Status")),
        "ambiente": select_name(props.get("Ambiente")),
        "prioridade": select_name(props.get("Prioridade")),
        "módulo": select_name(props.get("Módulo")),
        "categoria": multi_select_to_plain((props.get("Categoria", {}) or {}).get("multi_select", [])),
        "manifesto": rich_text_to_plain((props.get("Manifesto", {}) or {}).get("rich_text", [])),
    }


def normalize_name(value: str) -> str:
    text = value.strip()
    for pattern in (
        r"\s*-\s*minecraft\s+mods?\s*-\s*curseforge\s*$",
        r"\s*-\s*minecraft\s+mods?\s*$",
        r"\s*-\s*minecraft\s+mod\s*$",
        r"\s*-\s*minecraft\s+data\s+pack\s*$",
        r"\s*-\s*minecraft\s+resource\s+pack\s*$",
        r"\s*-\s*minecraft\s+resourcepacks?\s*$",
        r"\s*-\s*minecraft\s+shader\s*$",
        r"\s*-\s*minecraft\s+shaderpacks?\s*$",
        r"\s*\[fabric\]\s*$",
        r"\s*\[forge\]\s*$",
    ):
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = text.casefold()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_display_title(value: str) -> str:
    text = value.strip()
    for pattern in TITLE_SUFFIX_PATTERNS:
        text = re.sub(pattern, "", text, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", text).strip()


def parse_markdown_table(section_name: str, text: str) -> list[dict[str, str]]:
    lines = text.splitlines()
    collecting = False
    table_lines: list[str] = []
    for line in lines:
        if line.startswith("## "):
            heading = line[3:].strip()
            if heading == section_name:
                collecting = True
                table_lines = []
                continue
            if collecting:
                break
        if collecting and line.startswith("|"):
            table_lines.append(line)

    if len(table_lines) < 2:
        return []

    headers = [cell.strip() for cell in table_lines[0].strip().strip("|").split("|")]
    rows: list[dict[str, str]] = []
    for line in table_lines[2:]:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) != len(headers):
            continue
        rows.append(dict(zip(headers, cells, strict=True)))
    return rows


def parse_link_url(cell: str) -> str:
    match = re.search(r"\((https?://[^)]+)\)", cell)
    return match.group(1) if match else ""


def parse_pipe_cell(cell: str) -> str:
    value = cell.strip()
    return "" if value == "—" else value


def parse_list_cell(cell: str) -> list[str]:
    value = parse_pipe_cell(cell)
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def parse_priority_label(value: str) -> str:
    normalized = value.strip().casefold()
    return PRIORITY_MAP.get(normalized, value.strip())


def load_markdown(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def load_inventory_rows() -> dict[str, list[dict[str, Any]]]:
    text = load_markdown(ROOT / "docs" / "MODS_INVENTORY.md")
    sections = {
        "active": parse_markdown_table("Active mods", text),
        "listed": parse_markdown_table("Listed mods", text),
        "discarded": parse_markdown_table("Discarded mods", text),
    }
    parsed: dict[str, list[dict[str, Any]]] = {}
    for section, rows in sections.items():
        parsed_rows: list[dict[str, Any]] = []
        for row in rows:
            title = row.get("Mod", "").strip()
            if not title:
                continue
            parsed_rows.append(
                {
                    "title": title,
                    "title_norm": normalize_name(title),
                    "page_url": parse_link_url(row.get("Page", "")),
                    "categories": parse_list_cell(row.get("Categories", "")),
                    "environment": parse_pipe_cell(row.get("Environment", "")),
                    "priority": parse_priority_label(row.get("Priority", "")),
                    "dependencies": parse_pipe_cell(row.get("Dependencies", "")),
                    "dependents": parse_pipe_cell(row.get("Dependents", "")),
                    "incompatibilities": parse_pipe_cell(row.get("Incompatibilities", "")),
                    "notes": parse_pipe_cell(row.get("Notes", "")),
                }
            )
        parsed[section] = parsed_rows
    return parsed


def load_module_map() -> dict[str, str]:
    text = load_markdown(ROOT / "docs" / "MOD_MODULES.md")
    rows = parse_markdown_table("Módulos", text)
    mapping: dict[str, str] = {}
    for row in rows:
        module = MODULE_VALUE_MAP.get(row.get("Módulo", "").strip(), row.get("Módulo", "").strip())
        mods = row.get("Mods principais", "")
        if not module or not mods:
            continue
        for item in mods.split(","):
            candidate = item.strip()
            if not candidate or candidate in {"…", "..."}:
                continue
            mapping.setdefault(normalize_name(candidate), module)
    return mapping


def load_manifest_map() -> dict[str, str]:
    mapping: dict[str, str] = {}
    for relative in ("mods", "shaderpacks", "resourcepacks"):
        for path in sorted((ROOT / relative).glob("*.pw.toml")):
            text = path.read_text(encoding="utf-8")
            name_match = re.search(r'^name\s*=\s*"([^"]+)"', text, re.MULTILINE)
            stem = path.stem.replace(".pw", "")
            for candidate in [name_match.group(1) if name_match else "", stem]:
                norm = normalize_name(candidate)
                if norm and norm not in mapping:
                    mapping[norm] = f"{relative}/{path.name}"
    return mapping


def best_row_match(title: str, rows: list[dict[str, Any]]) -> dict[str, Any] | None:
    target = normalize_name(title)
    if not target:
        return None
    exact_matches = [row for row in rows if row.get("title_norm") == target]
    if len(exact_matches) == 1:
        return exact_matches[0]
    if len(exact_matches) > 1:
        return exact_matches[0]
    best: tuple[float, dict[str, Any]] | None = None
    for row in rows:
        candidate = row.get("title_norm", "")
        if not candidate:
            continue
        score = SequenceMatcher(None, target, candidate).ratio()
        if score < 0.78:
            continue
        if best is None or score > best[0]:
            best = (score, row)
    return best[1] if best else None


def current_text_value(page: dict[str, Any], field_name: str) -> str:
    prop = row_field(page, field_name)
    if not prop:
        return ""
    prop_type = prop.get("type")
    value = prop.get(prop_type)
    if prop_type == "title":
        return rich_text_to_plain(value)
    if prop_type == "select":
        return select_name(prop)
    if prop_type == "multi_select":
        return multi_select_to_plain(value)
    if prop_type == "url":
        return value or ""
    if prop_type == "rich_text":
        return rich_text_to_plain(value)
    if prop_type == "date":
        return (value or {}).get("start", "")
    return "" if value in (None, "", [], {}) else str(value)


def update_page_if_needed(
    page: dict[str, Any],
    updates: dict[str, str],
    title_link_url: str,
    dry_run: bool,
) -> bool:
    needs_title_link = bool(title_link_url and page_title_link(page).strip() != title_link_url)
    if not updates and not needs_title_link:
        return False
    if needs_title_link and DEFAULT_TITLE_PROPERTY not in updates:
        updates = {**updates, DEFAULT_TITLE_PROPERTY: page_title(page).strip() or page_title(page)}
    print(f"UPDATING {page_title(page)} [{page['id']}]: {', '.join(updates)}")
    if dry_run:
        return True
    update_page(page["id"], updates, title_link_url=title_link_url)
    time.sleep(0.35)
    return True


def build_reconciliation_updates(
    page: dict[str, Any],
    source: dict[str, Any],
    module_map: dict[str, str],
    manifest_map: dict[str, str],
    target_status: str,
) -> tuple[dict[str, str], str]:
    updates: dict[str, str] = {}
    canonical_title = source["title"]
    title_link_url = source.get("page_url", "")
    if page_title(page).strip() != canonical_title:
        updates[DEFAULT_TITLE_PROPERTY] = canonical_title

    if current_text_value(page, "Status") != target_status:
        updates["Status"] = target_status

    if source.get("environment") and current_text_value(page, "Ambiente") != source["environment"]:
        updates["Ambiente"] = source["environment"]

    if source.get("priority") and current_text_value(page, "Prioridade") != source["priority"]:
        updates["Prioridade"] = source["priority"]

    if source.get("categories") and is_blank_property(row_field(page, "Categoria")):
        updates["Categoria"] = ", ".join(source["categories"])

    module = module_map.get(source["title_norm"], "")
    if module and current_text_value(page, "Módulo") != module:
        updates["Módulo"] = module

    if source.get("page_url") and current_text_value(page, "Página") != source["page_url"]:
        updates["Página"] = source["page_url"]

    manifest = manifest_map.get(source["title_norm"], "")
    if manifest and current_text_value(page, "Manifesto") != manifest:
        updates["Manifesto"] = manifest

    if source.get("dependencies") and is_blank_property(row_field(page, "Dependências")):
        updates["Dependências"] = source["dependencies"]

    if source.get("incompatibilities") and is_blank_property(row_field(page, "Incompatibilidades")):
        updates["Incompatibilidades"] = source["incompatibilities"]

    if source.get("notes") and is_blank_property(row_field(page, "Notas")):
        updates["Notas"] = source["notes"]

    return updates, title_link_url


def build_title_normalization_updates(page: dict[str, Any]) -> tuple[dict[str, str], str]:
    updates: dict[str, str] = {}
    current_title = page_title(page).strip()
    normalized_title = normalize_display_title(current_title)
    page_url = current_text_value(page, "Página").strip()
    title_link_url = page_title_link(page).strip()

    if normalized_title and normalized_title != current_title:
        updates[DEFAULT_TITLE_PROPERTY] = normalized_title

    if page_url and title_link_url != page_url:
        if DEFAULT_TITLE_PROPERTY not in updates:
            updates[DEFAULT_TITLE_PROPERTY] = normalized_title or current_title
        title_link_url = page_url

    return updates, title_link_url


def build_create_properties(
    source: dict[str, Any],
    module_map: dict[str, str],
    manifest_map: dict[str, str],
    target_status: str,
) -> dict[str, str]:
    properties: dict[str, str] = {
        DEFAULT_TITLE_PROPERTY: source["title"],
        "Status": target_status,
        "Última revisão": dt.date.today().isoformat(),
    }

    if source.get("environment"):
        properties["Ambiente"] = source["environment"]
    if source.get("priority"):
        properties["Prioridade"] = source["priority"]
    if source.get("categories"):
        properties["Categoria"] = ", ".join(source["categories"])

    module = module_map.get(source["title_norm"], "")
    if module:
        properties["Módulo"] = module

    if source.get("page_url"):
        properties["Página"] = source["page_url"]

    manifest = manifest_map.get(source["title_norm"], "")
    if manifest:
        properties["Manifesto"] = manifest

    if source.get("dependencies"):
        properties["Dependências"] = source["dependencies"]
    if source.get("incompatibilities"):
        properties["Incompatibilidades"] = source["incompatibilities"]
    if source.get("notes"):
        properties["Notas"] = source["notes"]

    return properties


def encode_title_value(value: str, title_link_url: str = "") -> dict[str, Any]:
    text: dict[str, Any] = {"content": value}
    if title_link_url:
        text["link"] = {"url": title_link_url}
    return {
        "title": [
            {
                "type": "text",
                "text": text,
            }
        ]
    }


def encode_property(name: str, value: str, title_link_url: str = "") -> dict[str, Any]:
    if name in TITLE_FIELDS:
        return encode_title_value(value, title_link_url)
    if name in SELECT_FIELDS:
        return {"select": {"name": value}}
    if name in MULTI_SELECT_FIELDS:
        entries = [item.strip() for item in value.split(",") if item.strip()]
        return {"multi_select": [{"name": item} for item in entries]}
    if name in URL_FIELDS:
        return {"url": value}
    if name in RICH_TEXT_FIELDS:
        return {
            "rich_text": [
                {
                    "type": "text",
                    "text": {
                        "content": value,
                    },
                }
            ]
        }
    if name in DATE_FIELDS:
        return {"date": {"start": value}}
    raise SystemExit(f"unsupported property for update: {name}")


def update_page(page_id: str, updates: dict[str, str], title_link_url: str = "") -> dict[str, Any]:
    payload = {
        "properties": {
            name: encode_property(name, value, title_link_url=title_link_url if name in TITLE_FIELDS else "")
            for name, value in updates.items()
        }
    }
    return notion_request("PATCH", f"/pages/{page_id}", payload)


def create_page(properties: dict[str, str], title_link_url: str = "") -> dict[str, Any]:
    payload = {
        "parent": {"database_id": database_id()},
        "properties": {
            name: encode_property(name, value, title_link_url=title_link_url if name in TITLE_FIELDS else "")
            for name, value in properties.items()
        },
    }
    return notion_request("POST", "/pages", payload)


def cmd_audit(args: argparse.Namespace) -> int:
    rows = fetch_all_rows()
    fields = args.field or list(AUDIT_FIELDS)
    counters: Counter[str] = Counter()
    blanks: dict[str, list[dict[str, Any]]] = {field: [] for field in fields}

    for page in rows:
        props = page.get("properties", {})
        for field in fields:
            if is_blank_property(props.get(field)):
                counters[field] += 1
                blanks[field].append(row_summary(page))

    print(f"TOTAL {len(rows)}")
    for field in fields:
        print(f"BLANK {field} {counters[field]}")
        for row in blanks[field][: args.limit]:
            print(f"  - {row['title']} [{row['id']}]")
    return 0


def cmd_find(args: argparse.Namespace) -> int:
    query = args.title.casefold()
    rows = fetch_all_rows()
    matches = [row_summary(page) for page in rows if query in page_title(page).casefold()]
    print(f"MATCHES {len(matches)}")
    for row in matches[: args.limit]:
        print(
            f"- {row['title']} [{row['id']}] "
            f"status={row['status'] or '∅'} ambiente={row['ambiente'] or '∅'} "
            f"prioridade={row['prioridade'] or '∅'}"
        )
    return 0


def cmd_bulk_mark_listed(args: argparse.Namespace) -> int:
    rows = fetch_all_rows()
    targets = [page for page in rows if is_blank_property(row_field(page, "Status"))]
    today = dt.date.today().isoformat()
    print(f"TARGETS {len(targets)}")
    for index, page in enumerate(targets, start=1):
        summary = row_summary(page)
        print(f"[{index}/{len(targets)}] {summary['title']}")
        if args.dry_run:
            continue
        update_page(
            page["id"],
            {
                "Status": "Listed",
                "Última revisão": today,
            },
        )
    return 0


def cmd_sync_inventory(args: argparse.Namespace) -> int:
    inventory = load_inventory_rows()
    module_map = load_module_map()
    manifest_map = load_manifest_map()
    rows = fetch_all_rows()

    normalized_rows: list[dict[str, Any]] = []
    for page in rows:
        normalized_rows.append(
            {
                **page,
                "title": page_title(page),
                "title_norm": normalize_name(page_title(page)),
            }
        )

    matched_ids: set[str] = set()
    updated_rows = 0
    missing_inventory_rows: list[str] = []
    created_rows = 0
    created_source_rows: list[str] = []

    for section, target_status in (("active", "Active"), ("listed", "Listed"), ("discarded", "Discarded")):
        for source in inventory[section]:
            page = best_row_match(source["title"], normalized_rows)
            if page is None:
                properties = build_create_properties(source, module_map, manifest_map, target_status)
                print(f"CREATING {source['title']} [{section}]")
                if args.dry_run:
                    missing_inventory_rows.append(f"{section}: {source['title']}")
                    created_rows += 1
                    continue
                else:
                    created = create_page(properties, title_link_url=source.get("page_url", ""))
                    created_rows += 1
                    created_source_rows.append(source["title"])
                    matched_ids.add(created["id"])
                    normalized_rows.append(
                        {
                            **created,
                            "title": page_title(created),
                            "title_norm": normalize_name(page_title(created)),
                        }
                    )
                    time.sleep(0.35)
                continue
            matched_ids.add(page["id"])
            updates, title_link_url = build_reconciliation_updates(page, source, module_map, manifest_map, target_status)
            if updates:
                updates["Última revisão"] = dt.date.today().isoformat()
            if update_page_if_needed(page, updates, title_link_url, args.dry_run):
                updated_rows += 1

    unmatched_rows = [page for page in normalized_rows if page["id"] not in matched_ids]
    blank_status_rows = [page for page in unmatched_rows if is_blank_property(row_field(page, "Status"))]
    today = dt.date.today().isoformat()
    for page in unmatched_rows:
        updates: dict[str, str] = {}
        if is_blank_property(row_field(page, "Status")):
            updates["Status"] = "Listed"
        title_updates, title_link_url = build_title_normalization_updates(page)
        for key, value in title_updates.items():
            updates.setdefault(key, value)
        if updates:
            updates["Última revisão"] = today
            if update_page_if_needed(page, updates, title_link_url, args.dry_run):
                updated_rows += 1

    active_matched = sum(1 for source in inventory["active"] if best_row_match(source["title"], normalized_rows) is not None)
    listed_matched = sum(1 for source in inventory["listed"] if best_row_match(source["title"], normalized_rows) is not None)
    discarded_matched = sum(1 for source in inventory["discarded"] if best_row_match(source["title"], normalized_rows) is not None)

    print(f"ACTIVE_SOURCE_ROWS {len(inventory['active'])}")
    print(f"ACTIVE_MATCHED {active_matched}")
    print(f"LISTED_SOURCE_ROWS {len(inventory['listed'])}")
    print(f"LISTED_MATCHED {listed_matched}")
    print(f"DISCARDED_SOURCE_ROWS {len(inventory['discarded'])}")
    print(f"DISCARDED_MATCHED {discarded_matched}")
    print(f"BLANK_STATUS_LISTED {len(blank_status_rows)}")
    print(f"UPDATED_ROWS {updated_rows}")
    print(f"CREATED_ROWS {created_rows}")
    if created_source_rows:
        print("CREATED_SOURCE_ROWS")
        for item in created_source_rows:
            print(f"  - {item}")
    if missing_inventory_rows:
        print("MISSING_SOURCE_ROWS")
        for item in missing_inventory_rows:
            print(f"  - {item}")
    return 0


def cmd_update(args: argparse.Namespace) -> int:
    updates: dict[str, str] = {}
    for item in args.set:
        if "=" not in item:
            raise SystemExit(f"invalid --set value (expected key=value): {item}")
        key, value = item.split("=", 1)
        updates[key.strip()] = value.strip()
    if args.title is not None:
        updates[DEFAULT_TITLE_PROPERTY] = args.title
    if not updates:
        raise SystemExit("no updates provided")
    print(f"UPDATING {args.page_id}: {', '.join(updates)}")
    if args.dry_run:
        return 0
    update_page(args.page_id, updates, title_link_url=args.title_url or "")
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    audit = sub.add_parser("audit", help="report blank fields across the database")
    audit.add_argument("--field", action="append", help="field name to audit (repeatable)")
    audit.add_argument("--limit", type=int, default=25, help="max rows to print per field")
    audit.set_defaults(func=cmd_audit)

    find = sub.add_parser("find", help="find rows by title substring")
    find.add_argument("--title", required=True, help="title substring to match")
    find.add_argument("--limit", type=int, default=25, help="max rows to print")
    find.set_defaults(func=cmd_find)

    bulk = sub.add_parser("bulk-mark-listed", help="mark all blank Status rows as Listed")
    bulk.add_argument("--dry-run", action="store_true", help="print targets without updating")
    bulk.set_defaults(func=cmd_bulk_mark_listed)

    sync = sub.add_parser(
        "sync-inventory",
        help="reconcile the Notion Mods database with docs/MODS_INVENTORY.md and docs/MOD_MODULES.md",
    )
    sync.add_argument("--dry-run", action="store_true", help="print intended updates without writing")
    sync.set_defaults(func=cmd_sync_inventory)

    update = sub.add_parser("update", help="update a single page by page id")
    update.add_argument("--page-id", required=True, help="Notion page ID")
    update.add_argument(
        "--set",
        action="append",
        default=[],
        metavar="KEY=VALUE",
        help="property update (repeatable)",
    )
    update.add_argument("--title", help="shortcut for updating the title property")
    update.add_argument("--title-url", help="optional URL to link the title to")
    update.add_argument("--dry-run", action="store_true", help="print payload without updating")
    update.set_defaults(func=cmd_update)

    return parser.parse_args()


def main() -> int:
    load_dotenv(DOTENV_PATH)
    args = parse_args()
    return int(args.func(args))


if __name__ == "__main__":
    raise SystemExit(main())
