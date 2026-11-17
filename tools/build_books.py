"""Bind the rendered lesson PDFs of each module into one book: cover + contents + lessons + assignments.

    python tools/build_books.py SITE_DIR            # all modules with rendered PDFs
    python tools/build_books.py SITE_DIR M07 M11    # only these modules

SITE_DIR is the rendered site (tools/render_site.sh renders lessons to HTML and PDF). Books are written to
SITE_DIR/pdf/<module>.pdf and linked from the module pages. The cover and contents are typeset with Typst
(`quarto typst`) in the same "engineering pad" style as the lessons (site/book.typ); PDF bookmarks list every lesson.
"""
from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_curriculum as bc  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
GROUP_HL = {"Foundations": (255, 210, 0), "Data": (255, 150, 40), "Data Science": (110, 205, 90),
            "Deep Learning & Modalities": (70, 190, 230), "LLM & AI Applications": (255, 120, 190),
            "Ops & Systems": (170, 140, 255), "Responsibility": (255, 110, 90), "Capstones": (200, 220, 60),
            "Delivery": (60, 210, 190)}


def typst_str(s: str) -> str:
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def front_matter(m: dict, entries: list[tuple[str, str, int]], hl: tuple[int, int, int]) -> str:
    """Typst source for the cover and the contents page. entries: (label, title, first page in the book)."""
    rows = ",\n    ".join(f"({typst_str(lbl)}, {typst_str(t)}, {p})" for lbl, t, p in entries)
    r, g, b = hl
    n_ch = sum(1 for lbl, _, _ in entries if lbl.startswith("Chapter"))
    n_mi = len(entries) - n_ch
    counts = f"{n_ch} chapters" + (f" · {n_mi} missions" if n_mi else "")
    return f"""
#import "book.typ": *
#set page(paper: "a4", margin: (left: 27mm, right: 17mm, top: 22mm, bottom: 20mm), footer: none,
          fill: pad-paper, background: pad-background)
#set text(font: "Atkinson Hyperlegible", size: 11pt, fill: pad-ink)
#show heading: set text(font: "Shantell Sans", weight: 600, size: 20pt)

// cover
#v(28mm)
#text(font: "Kalam", size: 15pt, fill: pad-red)[From Zero to Hero · {m['group']}]
#v(4mm)
#block(text(font: "Shantell Sans", weight: 700, size: 34pt)[
  #box(fill: rgb({r}, {g}, {b}, 120), inset: (x: 6pt, y: 2pt), radius: 3pt)[{m['id']}]
  {m['name']}
])
#v(2mm)
#curve(stroke: 1.6pt + pad-red.transparentize(25%),
  curve.move((0pt, 6pt)), curve.quad((30pt, -2pt), (60pt, 6pt)), curve.quad((90pt, 14pt), (120pt, 6pt)),
  curve.quad((150pt, -2pt), (180pt, 6pt)), curve.quad((210pt, 14pt), (240pt, 6pt)))
#v(10mm)
#text(font: "Kalam", size: 14pt)[{counts} · every notebook executed on a real machine]
#v(1fr)
#insight[This book is the PDF edition of one module of a free notebook course. Code, numbers and plots come from
real runs; the online version links every chapter to its notebook.]
#text(size: 9pt, fill: pad-ink.transparentize(30%))[MIT licence · github.com/MuhammetAliVarlik/FromZeroToHero-DataScience-AI-Cloud]
#pagebreak()

// contents
#heading(level: 1, outlined: false)[Contents]
#v(4mm)
#let entries = (
    {rows},
)
#for (label, title, page) in entries [
  #grid(columns: (24mm, 1fr, auto), column-gutter: 3mm, row-gutter: 0mm,
    text(font: "Kalam", fill: pad-red, label),
    [#title #box(width: 1fr, repeat[#h(2pt).#h(2pt)])],
    str(page))
  #v(1.2mm)
]
"""


def lesson_pdf(site: Path, file: str) -> Path:
    return site / Path(file).with_suffix(".pdf")


def build_module(m: dict, site: Path, out_dir: Path) -> Path | None:
    items = []                                     # (label, title, pdf)
    for pos, l in enumerate(m["lessons"], start=1):
        if l.get("status") == "done" and l.get("file") and lesson_pdf(site, l["file"]).exists():
            items.append((f"Chapter {pos:02d}", l["title"], lesson_pdf(site, l["file"])))
    for i, a in enumerate(m.get("assignments") or [], start=1):
        if a.get("file") and lesson_pdf(site, a["file"]).exists():
            items.append((f"Mission {i:02d}", a["title"], lesson_pdf(site, a["file"])))
    if not items:
        return None
    readers = [PdfReader(p) for _, _, p in items]
    hl = GROUP_HL.get(m["group"], (255, 210, 0))

    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        (tmp / "book.typ").write_text((ROOT / "site" / "book.typ").read_text(encoding="utf-8")
                                      .split("// the title block uses")[0], encoding="utf-8")   # no Quarto `article` here

        def compile_front(entries) -> PdfReader:
            (tmp / "front.typ").write_text(front_matter(m, entries, hl), encoding="utf-8")
            subprocess.run(["quarto", "typst", "compile", "--font-path", str(ROOT / "site" / "fonts"),
                            str(tmp / "front.typ"), str(tmp / "front.pdf")], check=True)
            return PdfReader(tmp / "front.pdf")

        # the contents page lists page numbers, which depend on the length of the front matter: compile twice
        front = compile_front([(lbl, t, 0) for lbl, t, _ in items])
        start, entries = len(front.pages) + 1, []
        for (lbl, t, _), r in zip(items, readers):
            entries.append((lbl, t, start))
            start += len(r.pages)
        front = compile_front(entries)

        w = PdfWriter()
        w.append(front)
        for (lbl, t, _), r, (_, _, first) in zip(items, readers, entries):
            w.append(r, import_outline=False)
            parent = w.add_outline_item(title=f"{lbl} · {t}", page_number=first - 1)
            for o in r.outline:                    # the lesson's own top-level headings, nested under its chapter
                if not isinstance(o, list):
                    w.add_outline_item(title=o.title, page_number=first - 1 + r.get_destination_page_number(o), parent=parent)
        w.add_metadata({"/Title": f"{m['id']} · {m['name']}", "/Author": "From Zero to Hero"})
        out = out_dir / f"{m['id'].lower()}.pdf"
        out_dir.mkdir(parents=True, exist_ok=True)
        with open(out, "wb") as f:
            w.write(f)
    return out


def main() -> None:
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    site = Path(sys.argv[1]).resolve()
    only = {a.upper() for a in sys.argv[2:]}
    doc = bc.load()
    for m in doc["modules"]:
        if only and m["id"] not in only:
            continue
        out = build_module(m, site, site / "pdf")
        if out:
            print(f"{m['id']}: {out.relative_to(site)} ({len(PdfReader(out).pages)} pages)")


if __name__ == "__main__":
    main()
