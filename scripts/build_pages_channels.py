#!/usr/bin/env python3
"""Build a minimal GitHub Pages artifact for the main/dev packwiz channels."""

from __future__ import annotations

import argparse
import json
import pathlib
import subprocess
import tomllib

from check_packwiz_state import classify_index_file, index_entries_from_text, pack_index_hash_from_text, sha256_hex


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output-dir",
        type=pathlib.Path,
        required=True,
    )
    parser.add_argument(
        "--repo-root",
        type=pathlib.Path,
        default=pathlib.Path(__file__).resolve().parents[1],
    )
    parser.add_argument(
        "--branches",
        nargs="+",
        default=["main", "dev"],
    )
    parser.add_argument(
        "--ref-prefix",
        default="origin/",
    )
    parser.add_argument(
        "--strict-branches",
        nargs="*",
        default=[],
    )
    return parser.parse_args()


def git_show(repo_root: pathlib.Path, ref: str, path: str) -> bytes:
    return subprocess.check_output(["git", "show", f"{ref}:{path}"], cwd=repo_root)


def write_file(base: pathlib.Path, relative_path: str, data: bytes) -> None:
    target = base / relative_path
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_bytes(data)


def build_channel(
    repo_root: pathlib.Path,
    output_dir: pathlib.Path,
    branch: str,
    ref_prefix: str,
    strict: bool,
) -> dict[str, str]:
    ref = f"{ref_prefix}{branch}"
    pack_bytes = git_show(repo_root, ref, "pack.toml")
    index_bytes = git_show(repo_root, ref, "index.toml")
    pack_text = pack_bytes.decode("utf-8")
    index_text = index_bytes.decode("utf-8")

    expected_hash = pack_index_hash_from_text(pack_text)
    actual_hash = sha256_hex(index_bytes)
    if expected_hash != actual_hash:
        raise SystemExit(
            f"{ref}: pack.toml hash does not match index.toml ({expected_hash} != {actual_hash})"
        )

    channel_dir = output_dir / branch
    channel_dir.mkdir(parents=True, exist_ok=True)
    write_file(channel_dir, "pack.toml", pack_bytes)
    write_file(channel_dir, "index.toml", index_bytes)

    for relative_path in index_entries_from_text(index_text):
        if strict:
            allowed, message = classify_index_file(relative_path)
            if not allowed:
                raise SystemExit(f"{ref}: {message}")
        write_file(channel_dir, relative_path, git_show(repo_root, ref, relative_path))

    pack_data = tomllib.loads(pack_text)
    return {
        "branch": branch,
        "pack_url": f"/notvanilla/{branch}/pack.toml",
        "version": str(pack_data["version"]),
        "minecraft": str(pack_data["versions"]["minecraft"]),
        "fabric": str(pack_data["versions"]["fabric"]),
        "index_hash": actual_hash,
    }


def main() -> int:
    args = parse_args()
    repo_root = args.repo_root.resolve()
    output_dir = args.output_dir.resolve()
    output_dir.mkdir(parents=True, exist_ok=True)

    strict_branches = set(args.strict_branches)
    channels = [
        build_channel(
            repo_root,
            output_dir,
            branch,
            args.ref_prefix,
            branch in strict_branches,
        )
        for branch in args.branches
    ]

    (output_dir / ".nojekyll").write_text("", encoding="utf-8")
    (output_dir / "channels.json").write_text(
        json.dumps(channels, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )

    html_lines = [
        "<!doctype html>",
        "<html lang=\"pt-BR\">",
        "<head>",
        "  <meta charset=\"utf-8\">",
        "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">",
        "  <title>NotVanilla — canais packwiz</title>",
        "  <style>",
        "    body { font-family: sans-serif; margin: 2rem auto; max-width: 52rem; line-height: 1.6; padding: 0 1rem; }",
        "    code { background: #f4f4f4; padding: 0.1rem 0.3rem; border-radius: 0.25rem; }",
        "  </style>",
        "</head>",
        "<body>",
        "  <h1>NotVanilla — canais packwiz</h1>",
        "  <p>Manifestos publicados atomicamente para os canais <code>main</code> e <code>dev</code>.</p>",
        "  <ul>",
    ]
    for channel in channels:
        html_lines.append(
            "    <li>"
            f"<strong>{channel['branch']}</strong>: "
            f"<a href=\"./{channel['branch']}/pack.toml\">{channel['pack_url']}</a> "
            f"(pack {channel['version']}, Minecraft {channel['minecraft']}, Fabric {channel['fabric']})"
            "</li>"
        )
    html_lines.extend(["  </ul>", "</body>", "</html>"])
    (output_dir / "index.html").write_text("\n".join(html_lines) + "\n", encoding="utf-8")
    print(f"Built Pages artifact in {output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
