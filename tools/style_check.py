#!/usr/bin/env python3
"""Check lesson prose against STYLE.md (simplified technical English).

Usage:
  python tools/style_check.py NOTEBOOK.ipynb [...]
  python tools/style_check.py --module M26          # every notebook in a module folder
  python tools/style_check.py --module M26 --summary

The checks are heuristics. They report warnings; they do not fail unless --strict is given.
Checked: sentence length, likely passive voice, vague / hype / idiom words, paragraph length.
Only markdown cells are checked. Code blocks, LaTeX, links, tables and headings are ignored.
"""
from __future__ import annotations

import argparse
import glob
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MAX_WORDS = 25
MAX_PARAGRAPH_SENTENCES = 6

VAGUE = ["very", "really", "quite", "basically", "simply", "obviously", "just", "actually", "literally", "kind of", "sort of"]
HYPE = ["magic", "magical", "revolutionary", "game-changer", "game changer", "mind-blowing", "ultimate",
        "incredibly", "insanely", "blazing", "supercharge", "physics of", "the physics"]
IDIOMS = ["under the hood", "piece of cake", "silver bullet", "elephant in the room", "at the end of the day",
          "low-hanging fruit", "out of the box", "rule of thumb", "the bottom line", "in a nutshell",
          "figure out", "get rid of", "kick off", "look into", "come up with", "blow up", "blew up"]
BE = r"(?:is|are|was|were|be|been|being|gets|got)"
IRREGULAR = ("built|done|given|known|made|seen|shown|taken|written|chosen|drawn|driven|found|held|kept|left|lost|"
             "meant|paid|put|read|run|said|sent|set|split|spent|told|thought|understood|won|broken|frozen|hidden|"
             "stored|used|called|trained|computed|defined")
PASSIVE = re.compile(rf"\b{BE}\s+(?:\w+ly\s+)?(?:\w+ed|{IRREGULAR})\b(?!\s+(?:to|that)\b)", re.I)


def clean_markdown(text: str) -> list[str]:
    """Return prose paragraphs from a markdown cell."""
    text = re.sub(r"```.*?```", " ", text, flags=re.S)          # fenced code
    text = re.sub(r"\$\$.*?\$\$", " FORMULA ", text, flags=re.S)  # display math
    text = re.sub(r"\$[^$\n]+\$", "X", text)                    # inline math
    text = re.sub(r"`[^`]+`", "CODE", text)                     # inline code
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)           # images
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)        # links -> text
    text = re.sub(r"<[^>]+>", " ", text)                        # html
    paragraphs = []
    for block in re.split(r"\n\s*\n", text):
        lines = [l for l in block.splitlines()
                 if l.strip() and not l.lstrip().startswith(("#", "|", ">", "---")) and not re.match(r"^\s*-{3,}\s*$", l)]
        if not lines:
            continue
        # every list item is its own paragraph
        items, cur = [], []
        for l in lines:
            if re.match(r"^\s*([-*+]|\d+\.)\s+", l) and cur:
                items.append(" ".join(cur)); cur = []
            cur.append(re.sub(r"^\s*([-*+]|\d+\.)\s+", "", l))
        items.append(" ".join(cur))
        paragraphs += [re.sub(r"[*_]{1,3}", "", p).strip() for p in items if p.strip()]
    return paragraphs


def sentences(paragraph: str) -> list[str]:
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"(])", paragraph)
    return [p.strip() for p in parts if len(p.split()) > 0]


def check_text(text: str, where: str, issues: list[tuple[str, str, str]]):
    for para in clean_markdown(text):
        sents = sentences(para)
        if len(sents) > MAX_PARAGRAPH_SENTENCES:
            issues.append(("long-paragraph", where, f"{len(sents)} sentences: {para[:80]}..."))
        for s in sents:
            n = len(re.findall(r"[A-Za-z0-9][\w'-]*", s))
            if n > MAX_WORDS:
                issues.append(("long-sentence", where, f"{n} words: {s[:110]}{'...' if len(s) > 110 else ''}"))
            low = f" {s.lower()} "
            for w in VAGUE:
                if re.search(rf"\b{re.escape(w)}\b", low):
                    issues.append(("vague-word", where, f"'{w}': {s[:90]}"))
            for w in HYPE:
                if w in low:
                    issues.append(("hype-word", where, f"'{w}': {s[:90]}"))
            for w in IDIOMS:
                if w in low:
                    issues.append(("idiom", where, f"'{w}': {s[:90]}"))
            m = PASSIVE.search(s)
            if m:
                issues.append(("passive?", where, f"'{m.group(0)}': {s[:90]}"))


def check_notebook(path: str) -> list[tuple[str, str, str]]:
    nb = json.load(open(path, encoding="utf-8"))
    issues: list[tuple[str, str, str]] = []
    for i, cell in enumerate(nb["cells"]):
        if cell["cell_type"] == "markdown":
            check_text("".join(cell["source"]), f"cell {i}", issues)
    return issues


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("notebooks", nargs="*")
    ap.add_argument("--module", help="module id, e.g. M26")
    ap.add_argument("--summary", action="store_true", help="only print counts per notebook")
    ap.add_argument("--strict", action="store_true", help="exit 1 if long sentences or hype/idiom words exist")
    a = ap.parse_args()
    paths = list(a.notebooks)
    if a.module:
        paths += sorted(glob.glob(os.path.join(ROOT, f"{a.module}-*", "*.ipynb")))
    if not paths:
        ap.error("give notebooks or --module")
    total = Counter()
    for p in paths:
        issues = check_notebook(p)
        c = Counter(k for k, _, _ in issues)
        total.update(c)
        name = os.path.relpath(p, ROOT)
        print(f"\n{name}: " + (", ".join(f"{k}={v}" for k, v in sorted(c.items())) or "clean"))
        if not a.summary:
            for kind, where, msg in issues:
                print(f"  [{kind}] {where}: {msg}")
    print("\nTOTAL: " + (", ".join(f"{k}={v}" for k, v in sorted(total.items())) or "clean"))
    if a.strict and (total["long-sentence"] or total["hype-word"] or total["idiom"]):
        sys.exit(1)


if __name__ == "__main__":
    main()
