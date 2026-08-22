#!/usr/bin/env python3
"""Bakes contents/*.md into index.html at commit time (B-T2.1).

Why: index.html ships with placeholder text ("Content from home.md
here.") inside each #<section>-md div; static/js/scripts.js replaces it
client-side via fetch + marked.js. That's fine for a real browser, but
anything that doesn't execute JS -- LinkedIn/Slack/WhatsApp link
previews, curl, some crawlers -- sees the placeholder, not the content.

This script renders the same markdown server-side and writes the result
directly into those divs, so `curl https://parzon.github.io` returns
real prose. The client-side fetch still runs for real browsers and
overwrites the same divs on load, so nothing here is user-visible or
changes the editing workflow: contents/*.md stays the only thing a
human edits.

Must be run from the repo root. Section list must match
static/js/scripts.js's `section_names` array.
"""
import re
import sys
from pathlib import Path

import markdown
from bs4 import BeautifulSoup

REPO_ROOT = Path(__file__).resolve().parent.parent
INDEX_HTML = REPO_ROOT / "index.html"
CONTENT_DIR = REPO_ROOT / "contents"

SECTION_NAMES = ["home", "research-interests", "awards", "projects", "experience", "publications"]


def render_markdown(path: Path) -> str:
    text = path.read_text(encoding="utf-8")
    return markdown.markdown(text, extensions=["extra", "sane_lists"])


def main() -> int:
    soup = BeautifulSoup(INDEX_HTML.read_text(encoding="utf-8"), "html.parser")

    for name in SECTION_NAMES:
        md_path = CONTENT_DIR / f"{name}.md"
        if not md_path.exists():
            print(f"warning: {md_path} not found, skipping", file=sys.stderr)
            continue

        target = soup.find(id=f"{name}-md")
        if target is None:
            print(f"warning: no element with id=\"{name}-md\" in index.html, skipping", file=sys.stderr)
            continue

        rendered = render_markdown(md_path)
        fragment = BeautifulSoup(rendered, "html.parser")
        target.clear()
        target.append(fragment)

    # BeautifulSoup's html.parser serializer is fine for this fragment-swap
    # use case, but it lowercases nothing and leaves the rest of the
    # document untouched -- doctype and structure survive as written.
    output = str(soup)
    # BeautifulSoup renders the leading <!DOCTYPE html> as given; make sure
    # it's present even if a parser quirk drops it.
    if not re.match(r"(?is)^\s*<!doctype html>", output):
        output = "<!DOCTYPE html>\n" + output

    INDEX_HTML.write_text(output, encoding="utf-8")
    print(f"Prerendered {len(SECTION_NAMES)} sections into {INDEX_HTML}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
