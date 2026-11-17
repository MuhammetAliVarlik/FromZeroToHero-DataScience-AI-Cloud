"""Generate the Quarto website ("engineering pad" style, with PDF versions) from curriculum.yml.

    python tools/build_site.py                # write _quarto.yml and site/*.qmd pages
    quarto render                             # render the site into _site/ (notebooks are NOT re-executed)
    quarto preview                            # live preview in the browser

Every lesson is rendered twice: HTML for the site and PDF (Typst, site/book.typ). tools/build_books.py then binds
the lesson PDFs of each module into one book. Only lessons with status "done" are rendered. Notebooks keep their stored outputs (execute: enabled: false).
"""
from __future__ import annotations

import sys
from pathlib import Path
from urllib.parse import quote

import json

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_curriculum as bc  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "site"
REPO_URL = "https://github.com/MuhammetAliVarlik/FromZeroToHero-DataScience-AI-Cloud"
# marker colour per module group ("R G B", used by site/notebook.css as rgb(var(--pad-hl) / alpha))
GROUP_HL = {"Foundations": "255 210 0", "Data": "255 150 40", "Data Science": "110 205 90",
            "Deep Learning & Modalities": "70 190 230", "LLM & AI Applications": "255 120 190",
            "Ops & Systems": "170 140 255", "Responsibility": "255 110 90", "Capstones": "200 220 60",
            "Delivery": "60 210 190"}
LEVEL = {"beginner": "🟢 Beginner", "intermediate": "🟡 Intermediate", "advanced": "🟠 Advanced",
         "expert": "🔴 Expert"}


def rel_from_site(path: str, depth: int) -> str:
    """Link from a page `depth` folders below the repo root to a repo file (URL-encoded)."""
    return "../" * depth + quote(path, safe="/&,()'+")   # Quarto decodes %20 but not %26/%2C


def module_slug(m: dict) -> str:
    return m["id"].lower()


def done_lessons(m: dict) -> list[dict]:
    return [l for l in m["lessons"] if l.get("status") == "done" and l.get("file")]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def module_page(m: dict, mods: dict) -> str:
    done = done_lessons(m)
    rows = []
    for pos, l in enumerate(m["lessons"], start=1):
        if l in done:
            title = f"[{l['title']}]({rel_from_site(l['file'], 2)})"
            state = "✅"
        else:
            title, state = l["title"], "🛠️ in progress"
        rows.append(f"| {pos:02d} | {title} | {LEVEL.get(l.get('level', ''), '')} | {state} | {l.get('description', '')} |")
    assign = ""
    if m.get("assignments"):
        items = []
        for a in m["assignments"]:
            line = f"- [{a['title']}]({rel_from_site(a['file'], 2)})"
            if a.get("solution"):
                line += f" · [solution]({rel_from_site(a['solution'], 2)})"
            items.append(line)
        assign = "## Assignments\n\n" + "\n".join(items)
    book = (f"[⤓ Download this module as a book (PDF)](../../pdf/{module_slug(m)}.pdf){{.book-download}}\n\n"
            if done else "")
    prereq = ", ".join(f"[{p} {mods[p]['name']}]({module_slug(mods[p])}.qmd)" for p in m.get("prereqs", [])) or "none"
    return f"""---
format: html
title: "{m['id']} · {m['name']}"
subtitle: "{m['group']} · {len(done)} of {len(m['lessons'])} lessons ready"
---

{book}**Prerequisites:** {prereq} · **GPU:** {m.get('gpu', 'none')}

| # | Lesson | Level | Status | What you learn |
| :-: | :--- | :--- | :-: | :--- |
{chr(10).join(rows)}

{assign}
"""


def path_page(p: dict, mods: dict) -> str:
    core = []
    rows = []
    for i, mid in enumerate(p["modules"], start=1):
        m = mods[mid]
        rows.append(f"| {i} | [{mid} · {m['name']}](../modules/{module_slug(m)}.qmd) | {len(done_lessons(m))}/{len(m['lessons'])} |")
    return f"""---
format: html
title: "Path: {p['name']}"
---

Take the modules in order; skip lessons you already know.

| Step | Module | Ready |
| :-: | :--- | :-: |
{chr(10).join(rows)}
"""


def role_page(r: dict, paths: dict, mods: dict) -> str:
    plinks = ", ".join(f"[{paths[pid]['name']}](../paths/{pid}.qmd)" for pid in r.get("paths", []))
    extra = ", ".join(f"[{mid} · {mods[mid]['name']}](../modules/{module_slug(mods[mid])}.qmd)" for mid in r.get("extra_modules", []))
    return f"""---
format: html
title: "Role: {r['name']}"
---

{r.get('summary', '')}

**Paths:** {plinks or '—'}

**Extra modules:** {extra or '—'}
"""


def home_page(doc: dict) -> str:
    mods = doc["modules"]
    total = sum(len(m["lessons"]) for m in mods)
    done = sum(len(done_lessons(m)) for m in mods)
    groups: dict[str, list] = {}
    for m in mods:
        groups.setdefault(m["group"], []).append(m)
    cards = []
    for g, ms in groups.items():
        items = "\n".join(f"- [{m['id']} · {m['name']}](site/modules/{module_slug(m)}.qmd) "
                          f"<span class='ready'>{len(done_lessons(m))}/{len(m['lessons'])}</span>" for m in ms)
        cards.append((GROUP_HL.get(g, "255 210 0"), f"### {g}\n\n{items}"))
    paths = "\n".join(f"- [{p['name']}](site/paths/{p['id']}.qmd)" for p in doc["paths"])
    roles = "\n".join(f"- [{r['name']}](site/roles/{r['id']}.qmd)" for r in doc["roles"])
    return f"""---
format: html
title: "From Zero to Hero"
subtitle: "Data Science · AI · Data Engineering · MLOps · GPU — a free notebook course"
page-layout: full
toc: false
---

::: {{.lead}}
Every lesson is a Jupyter notebook that was **executed on a real machine** (a laptop GPU with 4 GB and Docker),
with real public data wherever it matters. **{done} of {total} lessons** are ready; the rest are in progress.
:::

*Insight: Pick a path for a skill, or a role for a job; each module page lists its lessons, and every lesson page shows the code and its real output.*

:::: {{.columns}}
::: {{.column width="50%"}}
## Learning paths
{paths}
:::
::: {{.column width="50%"}}
## Job roles
{roles}
:::
::::

## Modules

:::: {{.module-grid}}
{chr(10).join(f'::: {{.module-card style="--card-hl: {hl}"}}{chr(10)}{c}{chr(10)}:::' for hl, c in cards)}
::::

<small>Lesson content is AI-assisted and reviewed; outputs come from real runs. MIT licence. [Source on GitHub]({REPO_URL}).</small>
"""


def book_script(doc: dict) -> str:
    """Per-page touches that need the curriculum: marker colour of the module group, chapter label, PDF button."""
    mods = {m["id"]: {"name": m["name"], "hl": GROUP_HL.get(m["group"], "255 210 0")} for m in doc["modules"]}
    return """<script>
(function () {
  const MODS = %s;
  const path = decodeURIComponent(location.pathname);
  const lesson = path.match(/\\/(M\\d\\d)-[^\\/]+\\/(assignments\\/)?([^\\/]+)$/);
  const modpage = path.match(/\\/site\\/modules\\/m(\\d\\d)\\.html$/);
  const mod = lesson ? lesson[1] : (modpage ? "M" + modpage[1] : null);
  if (!mod || !MODS[mod]) return;
  document.documentElement.style.setProperty("--pad-hl", MODS[mod].hl);
  if (!lesson) return;
  const num = (lesson[3].match(/^(\\d\\d)-/) || [])[1];
  const h1 = document.querySelector("h1.title");
  if (!num || !h1) return;
  const eyebrow = document.createElement("div");
  eyebrow.className = "pad-eyebrow";
  const chapter = document.createElement("span");
  chapter.className = "pad-chapter";
  chapter.textContent = lesson[2] ? "Mission " + num + (/-solution\\.html$/.test(lesson[3]) ? " · solution" : "")
                                  : "Chapter " + num;
  const where = document.createElement("span");
  where.textContent = mod + " · " + MODS[mod].name;
  eyebrow.append(chapter, where);
  const pdf = document.querySelector('.quarto-alternate-formats a[href$=".pdf"]');
  if (pdf) {
    const a = document.createElement("a");
    a.className = "pad-pdf"; a.href = pdf.getAttribute("href"); a.textContent = "⤓ PDF";
    eyebrow.append(a);
  }
  h1.parentElement.insertBefore(eyebrow, h1);
})();
</script>""" % json.dumps(mods, ensure_ascii=False)


def quarto_yml(doc: dict) -> dict:
    mods = doc["modules"]
    render = ["index.qmd", "site/**/*.qmd"]
    sidebar_sections = []
    groups: dict[str, list] = {}
    for m in mods:
        groups.setdefault(m["group"], []).append(m)
    for g, ms in groups.items():
        contents = []
        for m in ms:
            lessons = done_lessons(m)
            entry = {"section": f"{m['id']} · {m['name']}", "href": f"site/modules/{module_slug(m)}.qmd", "contents": []}
            for l in lessons:
                render.append(l["file"])
                entry["contents"].append({"href": l["file"], "text": l["title"]})
            for a in m.get("assignments") or []:
                if lessons and a.get("file"):
                    render.append(a["file"])
                    entry["contents"].append({"href": a["file"], "text": f"✍️ {a['title']}"})
                    if a.get("solution"):
                        render.append(a["solution"])
            if not lessons:
                entry.pop("contents")
                entry = {"href": f"site/modules/{module_slug(m)}.qmd", "text": f"{m['id']} · {m['name']} 🛠️"}
            contents.append(entry)
        sidebar_sections.append({"section": g, "contents": contents})
    return {
        "project": {"type": "website", "output-dir": "_site", "render": render},
        "execute": {"enabled": False},
        "website": {
            "title": "From Zero to Hero",
            "site-url": "https://muhammetalivarlik.github.io/FromZeroToHero-DataScience-AI-Cloud/",
            "repo-url": REPO_URL,
            "repo-actions": ["source", "issue"],
            "page-navigation": True,
            "search": {"location": "navbar", "type": "overlay"},
            "navbar": {"left": [{"href": "index.qmd", "text": "Home"},
                                {"text": "Paths", "menu": [{"href": f"site/paths/{p['id']}.qmd", "text": p["name"]} for p in doc["paths"]]},
                                {"text": "Roles", "menu": [{"href": f"site/roles/{r['id']}.qmd", "text": r["name"]} for r in doc["roles"]]}],
                       "right": [{"icon": "github", "href": REPO_URL}]},
            "sidebar": {"style": "floating", "collapse-level": 2, "contents": sidebar_sections},
            "page-footer": {"center": "Free and open (MIT). Notebooks rendered with their stored outputs."},
        },
        "format": {"html": {
            "theme": {"light": ["cosmo", "site/theme-light.scss"], "dark": ["darkly", "site/theme-dark.scss"]},
            "css": "site/notebook.css",
            "toc": True, "toc-depth": 2,
            # Quarto adds its default links ("Typst") unless the list has a plain format name; "none" matches no format
            "format-links": [{"format": "typst", "text": "PDF", "icon": "file-pdf"}, "none"],
            "code-copy": True, "code-overflow": "wrap",
            "highlight-style": {"light": "github", "dark": "nord"},
            "filters": ["site/insight.lua"],
            "include-after-body": "site/book-script.html",
            "fig-responsive": True,
            "smooth-scroll": True,
        }, "typst": {
            "include-in-header": "site/book.typ",
            "include-before-body": "site/book-body.typ",
            "font-paths": ["site/fonts"],
            "mainfont": "Atkinson Hyperlegible",
            "fontsize": "10.5pt",
            "papersize": "a4",
            "margin": {"left": "27mm", "right": "17mm", "top": "18mm", "bottom": "20mm"},
            "filters": ["site/insight.lua"],
            "toc": False,
            "fig-format": "png",
        }},
    }


def main() -> None:
    doc = bc.load()
    mods = bc.by_id(doc)
    paths = {p["id"]: p for p in doc["paths"]}
    for m in doc["modules"]:
        write(SITE / "modules" / f"{module_slug(m)}.qmd", module_page(m, mods))
    for p in doc["paths"]:
        write(SITE / "paths" / f"{p['id']}.qmd", path_page(p, mods))
    for r in doc["roles"]:
        write(SITE / "roles" / f"{r['id']}.qmd", role_page(r, paths, mods))
    write(ROOT / "index.qmd", home_page(doc))
    write(SITE / "book-script.html", book_script(doc))
    cfg = quarto_yml(doc)
    header = "# Generated by tools/build_site.py from curriculum.yml. Do not edit by hand.\n"
    (ROOT / "_quarto.yml").write_text(header + yaml.safe_dump(cfg, sort_keys=False, allow_unicode=True, width=120), encoding="utf-8")
    n = len([f for f in cfg["project"]["render"] if f.endswith(".ipynb")])
    print(f"site: {n} notebooks, {len(doc['modules'])} module pages, {len(doc['paths'])} paths, {len(doc['roles'])} roles")


if __name__ == "__main__":
    main()
