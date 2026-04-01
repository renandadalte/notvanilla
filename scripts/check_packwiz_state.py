#!/usr/bin/env python3
"""Validate packwiz state for the current repository tree."""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
import tomllib

ALLOWED_INDEX_PREFIXES = (
    "config/",
    "datapacks/",
    "mods/",
    "resourcepacks/",
    "shaderpacks/",
)

FORBIDDEN_INDEX_FILES = {
    "CHANGELOG.md",
    "README.md",
    "instance.cfg",
    "instance.dev.cfg",
    "mmc-pack.json",
    "packwiz-installer-bootstrap.jar",
}

FORBIDDEN_INDEX_PREFIXES = (
    ".agent/",
    ".cursor/",
    ".github/",
    ".git/",
    "docs/",
    "logs/",
    "scripts/",
)

REQUIRED_PRESERVE_FILES = {
    "config/bettercombat/client.json5",
    "config/bettercombat/weapon_trails.json",
    "config/entityculling.json",
    "config/fabric/indigo-renderer.properties",
    "config/immediatelyfast.json",
    "config/iris-excluded.json",
    "config/iris.properties",
    "config/leawind_third_person.json",
    "config/modmenu.json",
    "config/notenoughanimations.json",
    "config/observable.json",
    "config/realcamera.json",
    "config/sodium-options.json",
    "config/spark/activity.json",
    "config/yacl.json5",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo-root",
        type=pathlib.Path,
        default=pathlib.Path(__file__).resolve().parents[1],
    )
    return parser.parse_args()


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def read_text(path: pathlib.Path) -> str:
    return path.read_text(encoding="utf-8")


def index_file_entries_from_text(index_text: str) -> list[dict[str, object]]:
    data = tomllib.loads(index_text)
    return [dict(entry) for entry in data.get("files", [])]


def pack_index_hash_from_text(pack_text: str) -> str:
    data = tomllib.loads(pack_text)
    return str(data["index"]["hash"])


def classify_index_file(path: str) -> tuple[bool, str]:
    if path in FORBIDDEN_INDEX_FILES:
        return False, f"forbidden file in index.toml: {path}"
    for prefix in FORBIDDEN_INDEX_PREFIXES:
        if path.startswith(prefix):
            return False, f"forbidden path in index.toml: {path}"
    for prefix in ALLOWED_INDEX_PREFIXES:
        if path.startswith(prefix):
            return True, ""
    return False, f"non-runtime file in index.toml: {path}"


def validate_repo(repo_root: pathlib.Path) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    notes: list[str] = []

    pack_path = repo_root / "pack.toml"
    index_path = repo_root / "index.toml"
    pack_text = read_text(pack_path)
    index_text = read_text(index_path)
    pack_hash = pack_index_hash_from_text(pack_text)
    actual_index_hash = sha256_hex(index_path.read_bytes())
    if pack_hash != actual_index_hash:
        errors.append(
            "pack.toml index hash does not match index.toml "
            f"(pack.toml={pack_hash}, actual={actual_index_hash})"
        )

    file_entries = index_file_entries_from_text(index_text)
    entries = [str(entry["file"]) for entry in file_entries]
    duplicates = sorted({entry for entry in entries if entries.count(entry) > 1})
    if duplicates:
        errors.append(f"duplicate index entries: {', '.join(duplicates)}")

    for entry in entries:
        allowed, message = classify_index_file(entry)
        if not allowed:
            errors.append(message)
            continue
        if not (repo_root / entry).exists():
            errors.append(f"index.toml references a missing file: {entry}")

    preserve_count = 0
    entry_by_path = {str(entry["file"]): entry for entry in file_entries}
    for path in sorted(REQUIRED_PRESERVE_FILES):
        entry = entry_by_path.get(path)
        if entry is None:
            errors.append(f"required preserved config is missing from index.toml: {path}")
            continue
        if entry.get("preserve") is not True:
            errors.append(f"config must set preserve = true: {path}")
            continue
        preserve_count += 1

    spark_activity_path = repo_root / "config/spark/activity.json"
    try:
        spark_activity = json.loads(read_text(spark_activity_path))
    except json.JSONDecodeError as exc:
        errors.append(f"config/spark/activity.json must contain valid JSON: {exc}")
    else:
        if spark_activity != []:
            errors.append(
                "config/spark/activity.json must stay sanitized in git "
                "(expected an empty JSON array)"
            )

    counts = {prefix.rstrip("/"): 0 for prefix in ALLOWED_INDEX_PREFIXES}
    for entry in entries:
        for prefix in ALLOWED_INDEX_PREFIXES:
            if entry.startswith(prefix):
                counts[prefix.rstrip("/")] += 1
                break
    notes.append(
        "index entries by prefix: "
        + ", ".join(f"{name}={count}" for name, count in counts.items())
    )
    notes.append(f"preserved user-local config files: {preserve_count}")
    notes.append(f"pack.toml/index.toml hash: {actual_index_hash}")
    return errors, notes


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    errors, notes = validate_repo(repo_root)
    for note in notes:
        print(f"NOTE {note}")
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print("OK packwiz state is coherent")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
