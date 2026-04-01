#!/usr/bin/env python3
"""Audit the repo tree and history for exposed or unnecessary content."""

from __future__ import annotations

import argparse
import pathlib
import re
import subprocess
import sys
from collections import Counter

CATEGORY_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    (
        "runtime do pack",
        (
            "pack.toml",
            "index.toml",
            "config/",
            "datapacks/",
            "mods/",
            "resourcepacks/",
            "shaderpacks/",
        ),
    ),
    (
        "bootstrap e automacao",
        (
            ".github/",
            ".gitignore",
            ".packwizignore",
            "instance.cfg",
            "instance.dev.cfg",
            "mmc-pack.json",
            "packwiz-installer-bootstrap.jar",
            "scripts/",
        ),
    ),
    (
        "documentacao publica",
        (
            "README.md",
            "CHANGELOG.md",
            "docs/",
        ),
    ),
)

LOCAL_ONLY_PREFIXES = (
    ".agent/",
    ".cursor/",
    ".env",
    ".local/",
    "banned-ips.json",
    "banned-players.json",
    "logs/",
    "ops.json",
    "server.properties",
    "server.properties.template",
    "usercache.json",
    "whitelist.json",
    "world/",
    "world_backup_",
)

SENSITIVE_HISTORY_PATHS = (
    ".env",
    "server.properties",
    "server.properties.template",
    "ops.json",
    "whitelist.json",
    "banned-ips.json",
    "banned-players.json",
    "usercache.json",
    "easyauth.db",
    "auth.db",
)

SENSITIVE_CONTENT_PATTERNS = (
    re.compile(r"rcon\.password=", re.IGNORECASE),
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--repo-root",
        type=pathlib.Path,
        default=pathlib.Path(__file__).resolve().parents[1],
    )
    return parser.parse_args()


def run(
    repo_root: pathlib.Path,
    *args: str,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=repo_root,
        check=check,
        capture_output=True,
        text=True,
    )


def classify_path(path: str) -> str | None:
    for prefix in LOCAL_ONLY_PREFIXES:
        if path == prefix or path.startswith(prefix):
            return "local/host-only"
    for category, rules in CATEGORY_RULES:
        for rule in rules:
            if path == rule or path.startswith(rule):
                return category
    return None


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    tracked = [
        line
        for line in run(
            repo_root,
            "git",
            "ls-files",
            "--cached",
            "--others",
            "--exclude-standard",
        ).stdout.splitlines()
        if line.strip()
    ]

    counts: Counter[str] = Counter()
    errors: list[str] = []
    notes: list[str] = []

    for path in tracked:
        category = classify_path(path)
        if category == "local/host-only":
            errors.append(f"tracked local/host-only path: {path}")
            continue
        if category is None:
            errors.append(f"unclassified tracked path: {path}")
            continue
        counts[category] += 1

    for category, _ in CATEGORY_RULES:
        notes.append(f"{category}: {counts[category]} tracked files")

    history_paths = run(
        repo_root,
        "git",
        "log",
        "--all",
        "--name-only",
        "--pretty=format:",
    ).stdout.splitlines()
    suspicious_history_paths = sorted(
        {
            path
            for path in history_paths
            if any(
                path == fragment
                or path.endswith(f"/{fragment}")
                or path.startswith(f"{fragment}/")
                for fragment in SENSITIVE_HISTORY_PATHS
            )
        }
    )
    if suspicious_history_paths:
        errors.append(
            "sensitive-looking paths found in git history: "
            + ", ".join(suspicious_history_paths)
        )

    revs = [
        line
        for line in run(repo_root, "git", "rev-list", "--all").stdout.splitlines()
        if line.strip()
    ]
    if revs:
        grep = subprocess.run(
            ["git", "grep", "-nEI", "|".join(p.pattern for p in SENSITIVE_CONTENT_PATTERNS), *revs, "--"],
            cwd=repo_root,
            capture_output=True,
            text=True,
        )
        matches = [
            line
            for line in grep.stdout.splitlines()
            if "secrets.GITHUB_TOKEN" not in line
        ]
        if matches:
            errors.append(
                "sensitive-looking content found in git history: " + matches[0]
            )

    for note in notes:
        print(f"NOTE {note}")
    if errors:
        for error in errors:
            print(f"ERROR {error}")
        return 1
    print("OK repo audit found no tracked local-only files or obvious sensitive history")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
