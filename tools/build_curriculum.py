#!/usr/bin/env python3
"""Build tooling for the course structure.

`curriculum.yml` is the single source of truth. This script:

  --check     validates the YAML against the files on disk and the prerequisite graph
  --generate  writes the generated README sections, module READMEs, paths/*.md and roles/*.md
  --sync      renames lesson files/folders (git mv) to match the YAML order and names,
              then rewrites the `file:` fields in curriculum.yml

Usage:
  python tools/build_curriculum.py --check
  python tools/build_curriculum.py --sync --generate --check
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import urllib.parse
from collections import Counter, OrderedDict

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
YML = os.path.join(ROOT, "curriculum.yml")

STATUS_ICON = OrderedDict([
    ("done", "✅"), ("review", "🔍"), ("deepen", "📈"), ("realise", "⚙️"),
    ("merge", "🔀"), ("rewrite", "✏️"), ("planned", "🆕"),
])
LEVEL_ICON = {"beginner": "🟢 Beginner", "intermediate": "🟡 Intermediate",
              "advanced": "🟠 Advanced", "expert": "🔴 Expert"}
GPU_ICON = {"none": "—", "optional": "optional", "required": "required"}
# service name in curriculum.yml -> docker/compose.yml profile (None = not a compose service)
SERVICE_PROFILE = {"postgres": "db", "mongodb": "db", "redis": "db", "kafka": "streaming", "rustfs": "streaming",
                   "localstack": "cloud", "prometheus": "observability", "grafana": "observability",
                   "neo4j": "graph", "qdrant": "vector", "ollama": "ollama",
                   "airflow": "orchestration", "superset": "bi", "connect": "cdc", "flink": "flink",
                   "schema-registry": "streaming", "iceberg-rest": "lakehouse", "marquez": "lineage"}
SERVICE_NOTE = {"ollama": "or native Ollama on http://localhost:11434", "kind": "kind CLI (local Kubernetes in Docker)",
                "docker": "Docker Engine"}


def services_md(services):
    profiles = sorted({SERVICE_PROFILE[s] for s in services if SERVICE_PROFILE.get(s)})
    notes = [f"{s}: {SERVICE_NOTE[s]}" for s in services if s in SERVICE_NOTE]
    out = ", ".join(services)
    if profiles:
        out += " · start with `docker compose -f docker/compose.yml " + " ".join(f"--profile {p}" for p in profiles) + " up -d`"
    if notes:
        out += " (" + "; ".join(notes) + ")"
    return out
GROUP_ICON = {"Foundations": "🧱", "Data": "🗄️", "Data Science": "🔬", "Deep Learning & Modalities": "🧠",
              "LLM & AI Applications": "🤖", "Ops & Systems": "⚙️", "Responsibility": "🛡️",
              "Capstones": "🏁", "Delivery": "🤝"}


# --------------------------------------------------------------------------- helpers
def load() -> dict:
    with open(YML, encoding="utf-8") as f:
        return yaml.safe_load(f)


class _Dumper(yaml.SafeDumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)


def save(doc: dict) -> None:
    with open(YML, "w", encoding="utf-8") as f:
        f.write("# Single source of truth for the course structure.\n"
                "# Edit this file, then run: python tools/build_curriculum.py --check --generate\n")
        yaml.dump(doc, f, Dumper=_Dumper, sort_keys=False, allow_unicode=True, width=120)


def module_dir(m: dict) -> str:
    return f"{m['id']}-{safe_title(m['name'])}"


def safe_title(t: str) -> str:
    """Make a title usable as a cross-platform file name."""
    t = t.replace("／", "-").replace("/", "-").replace(":", " -").replace("—", "-")
    t = re.sub(r'[<>"\\|?*]', "", t)
    return re.sub(r"\s+", " ", t).strip().rstrip(".")


def lesson_filename(pos: int, title: str) -> str:
    return f"{pos:02d}-{safe_title(title)}.ipynb"


def link(path: str) -> str:
    return "/" + urllib.parse.quote(path, safe="/&,()-")


def rel_link(path: str, from_dir: str) -> str:
    return urllib.parse.quote(os.path.relpath(path, from_dir), safe="/&,()-.")


def by_id(doc):
    return {m["id"]: m for m in doc["modules"]}


def role_modules(doc, role) -> list[str]:
    paths = {p["id"]: p for p in doc["paths"]}
    seen = []
    for pid in role["paths"]:
        for mid in paths[pid]["modules"]:
            if mid not in seen:
                seen.append(mid)
    for mid in role.get("extra_modules", []):
        if mid not in seen:
            seen.append(mid)
    return seen


def counts(m):
    c = Counter(l["status"] for l in m["lessons"])
    existing = sum(v for k, v in c.items() if k != "planned")
    return existing, c.get("planned", 0), c.get("done", 0)


# --------------------------------------------------------------------------- check
def check(doc) -> int:
    errors, warnings = [], []
    mods = by_id(doc)
    ids = [m["id"] for m in doc["modules"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate module ids")
    listed = set()
    for m in doc["modules"]:
        for key in ("prereqs", "recommended"):
            for p in m.get(key, []):
                if p not in mods:
                    errors.append(f"{m['id']}: unknown {key} {p}")
        for l in m["lessons"]:
            if l["status"] not in STATUS_ICON:
                errors.append(f"{m['id']} '{l['title']}': unknown status {l['status']}")
            f = l.get("file")
            if l["status"] == "planned":
                if f:
                    errors.append(f"{m['id']} '{l['title']}': planned lesson has a file")
                continue
            if not f:
                errors.append(f"{m['id']} '{l['title']}': missing file")
            elif not os.path.exists(os.path.join(ROOT, f)):
                errors.append(f"{m['id']}: file not found: {f}")
            else:
                listed.add(os.path.normpath(f))
        for a in m.get("assignments", []):
            for k in ("file", "solution"):
                if a.get(k):
                    if not os.path.exists(os.path.join(ROOT, a[k])):
                        errors.append(f"{m['id']}: assignment file not found: {a[k]}")
                    listed.add(os.path.normpath(a[k]))

    # notebooks on disk that the YAML does not know about
    for d in sorted(os.listdir(ROOT)):
        if not (re.match(r"M\d\d-", d) or d.startswith("Section ")) or not os.path.isdir(os.path.join(ROOT, d)):
            continue
        for dp, _, fs in os.walk(os.path.join(ROOT, d)):
            if ".ipynb_checkpoints" in dp:
                continue
            for fn in fs:
                if fn.endswith(".ipynb"):
                    rel = os.path.normpath(os.path.relpath(os.path.join(dp, fn), ROOT))
                    if rel not in listed:
                        errors.append(f"notebook not in curriculum.yml: {rel}")

    # prerequisite graph must be acyclic
    state = {}
    def visit(mid, stack):
        if state.get(mid) == 1:
            errors.append("prerequisite cycle: " + " -> ".join(stack + [mid]))
            return
        if state.get(mid) == 2:
            return
        state[mid] = 1
        for p in mods[mid].get("prereqs", []):
            if p in mods:
                visit(p, stack + [mid])
        state[mid] = 2
    for mid in mods:
        visit(mid, [])

    # paths: hard prerequisites must come earlier in the same path
    for p in doc["paths"]:
        for i, mid in enumerate(p["modules"]):
            if mid not in mods:
                errors.append(f"path {p['id']}: unknown module {mid}")
                continue
            for pre in mods[mid].get("prereqs", []):
                if pre not in p["modules"][:i]:
                    errors.append(f"path {p['id']}: {mid} needs {pre} earlier in the path")
    for r in doc["roles"]:
        for pid in r["paths"]:
            if pid not in {p["id"] for p in doc["paths"]}:
                errors.append(f"role {r['id']}: unknown path {pid}")
        order = role_modules(doc, r)
        for i, mid in enumerate(order):
            for pre in mods[mid].get("prereqs", []):
                if pre not in order[:i]:
                    warnings.append(f"role {r['id']}: {mid} needs {pre}, which is not earlier in the role order")
    # modules not reachable from any path
    in_paths = {mid for p in doc["paths"] for mid in p["modules"]} | {mid for r in doc["roles"] for mid in r.get("extra_modules", [])}
    for mid in mods:
        if mid not in in_paths and mid != "M42":
            warnings.append(f"module {mid} is not part of any path or role")

    for w in warnings:
        print("WARN ", w)
    for e in errors:
        print("ERROR", e)
    total = sum(len(m["lessons"]) for m in doc["modules"])
    print(f"check: {len(doc['modules'])} modules, {total} lessons, {len(doc['paths'])} paths, "
          f"{len(doc['roles'])} roles -> {len(errors)} errors, {len(warnings)} warnings")
    return 1 if errors else 0


# --------------------------------------------------------------------------- sync (renames)
def git_mv(src, dst):
    os.makedirs(os.path.dirname(os.path.join(ROOT, dst)), exist_ok=True)
    tracked = subprocess.run(["git", "ls-files", "--error-unmatch", src], cwd=ROOT,
                             capture_output=True).returncode == 0
    if tracked:
        subprocess.run(["git", "mv", src, dst], cwd=ROOT, check=True)
    else:
        os.rename(os.path.join(ROOT, src), os.path.join(ROOT, dst))


def sync(doc) -> dict:
    moves = {}
    for m in doc["modules"]:
        folder = module_dir(m)
        for pos, l in enumerate(m["lessons"], start=1):
            if l["status"] == "planned" or not l.get("file"):
                continue
            target = f"{folder}/{lesson_filename(pos, l['title'])}"
            if os.path.normpath(l["file"]) != os.path.normpath(target):
                moves[l["file"]] = target
                l["file"] = target
        for a in m.get("assignments", []):
            for k in ("file", "solution"):
                if a.get(k):
                    target = f"{folder}/assignments/{os.path.basename(a[k])}"
                    if os.path.normpath(a[k]) != os.path.normpath(target):
                        moves[a[k]] = target
                        a[k] = target
    # two-phase move avoids collisions when files swap names inside one folder
    temp = {}
    for i, (src, dst) in enumerate(moves.items()):
        tmp = f"{os.path.dirname(dst)}/__tmp_{i}.ipynb"
        git_mv(src, tmp)
        temp[tmp] = dst
    for tmp, dst in temp.items():
        git_mv(tmp, dst)
    save(doc)
    print(f"sync: moved {len(moves)} files")
    return moves


# --------------------------------------------------------------------------- generate
def gen_module_readme(doc, m) -> str:
    mods = by_id(doc)
    folder = module_dir(m)
    paths_in = [p for p in doc["paths"] if m["id"] in p["modules"]]
    ex, planned, done = counts(m)
    out = [f"# {m['id']} · {m['name']}", "",
           "> Generated from `curriculum.yml` by `tools/build_curriculum.py`. Do not edit by hand.", "",
           f"**Group:** {m['group']} · **Lessons:** {ex} existing + {planned} planned ({done} verified) · "
           f"**GPU:** {GPU_ICON[m['gpu']]}"
           , ""]
    if m.get("services"):
        out += [f"**Services:** {services_md(m['services'])}", ""]
    pre = ", ".join(f"[{p} {mods[p]['name']}](../{urllib.parse.quote(module_dir(mods[p]))}/README.md)" for p in m.get("prereqs", []))
    rec = ", ".join(f"[{p} {mods[p]['name']}](../{urllib.parse.quote(module_dir(mods[p]))}/README.md)" for p in m.get("recommended", []))
    out.append(f"**Prerequisites:** {pre or 'none'}" + (f" · **Recommended:** {rec}" if rec else ""))
    if paths_in:
        out += ["", "**Part of paths:** " + ", ".join(f"[{p['name']}](../paths/{p['id']}.md)" for p in paths_in)]
    out += ["", "| # | Lesson | Level | Status | Description |", "| :-: | :--- | :--- | :-: | :--- |"]
    for pos, l in enumerate(m["lessons"], start=1):
        name = (f"[{l['title']}]({rel_link(os.path.join(ROOT, l['file']), os.path.join(ROOT, folder))})"
                if l.get("file") else l["title"])
        desc = l.get("description", "")
        if l.get("notes"):
            desc = (desc + " " if desc else "") + f"*({l['notes']})*"
        out.append(f"| {pos:02d} | {name} | {LEVEL_ICON.get(l.get('level'), '')} | "
                   f"{STATUS_ICON[l['status']]} | {desc} |")
    if m.get("assignments"):
        out += ["", "## Assignments", "", "| Assignment | Solution |", "| :--- | :--- |"]
        for a in m["assignments"]:
            sol = (f"[solution]({rel_link(os.path.join(ROOT, a['solution']), os.path.join(ROOT, folder))})"
                   if a.get("solution") else "not written yet")
            out.append(f"| [{a['title']}]({rel_link(os.path.join(ROOT, a['file']), os.path.join(ROOT, folder))}) | {sol} |")
    out += ["", "Status legend: " + " · ".join(f"{v} {k}" for k, v in STATUS_ICON.items()), ""]
    return "\n".join(out)


def gen_path_page(doc, p) -> str:
    mods = by_id(doc)
    roles = [r for r in doc["roles"] if p["id"] in r["paths"]]
    total_ex = total_pl = 0
    rows = []
    for i, mid in enumerate(p["modules"], start=1):
        m = mods[mid]
        ex, pl, done = counts(m)
        total_ex += ex; total_pl += pl
        rows.append(f"| {i} | [{mid} · {m['name']}](../{urllib.parse.quote(module_dir(m))}/README.md) | "
                    f"{ex + pl} | {done}/{ex + pl} | {GPU_ICON[m['gpu']]} |")
    out = [f"# Path: {p['name']}", "",
           "> Generated from `curriculum.yml`. Do not edit by hand.", "",
           f"Take the modules in order. Each module lists its lessons; skip lessons you already know.", "",
           "| Step | Module | Lessons | Verified | GPU |", "| :-: | :--- | :-: | :-: | :-: |"] + rows
    out += ["", f"**Total:** {total_ex + total_pl} lessons ({total_pl} still planned). "
                f"**Capstone:** {p['capstone']} (module M42).", ""]
    if roles:
        out += ["**Used by roles:** " + ", ".join(f"[{r['name']}](../roles/{r['id']}.md)" for r in roles), ""]
    return "\n".join(out)


def gen_role_page(doc, r) -> str:
    mods = by_id(doc)
    paths = {p["id"]: p for p in doc["paths"]}
    order = role_modules(doc, r)
    out = [f"# Role: {r['name']}", "", "> Generated from `curriculum.yml`. Do not edit by hand.", "",
           r["summary"], "",
           "**Paths:** " + " + ".join(f"[{paths[pid]['name']}](../paths/{pid}.md)" for pid in r["paths"])
           + (" · **Extra modules:** " + ", ".join(r["extra_modules"]) if r.get("extra_modules") else ""), "",
           "## Module order", "", "| Step | Module | Lessons |", "| :-: | :--- | :-: |"]
    for i, mid in enumerate(order, start=1):
        m = mods[mid]
        out.append(f"| {i} | [{mid} · {m['name']}](../{urllib.parse.quote(module_dir(m))}/README.md) | {len(m['lessons'])} |")
    # overlap with other roles helps people plan hybrid profiles
    mine = set(order)
    sims = []
    for o in doc["roles"]:
        if o["id"] == r["id"]:
            continue
        theirs = set(role_modules(doc, o))
        sims.append((len(mine & theirs) / len(mine | theirs), o))
    sims.sort(key=lambda t: -t[0])
    out += ["", "## Closest roles (shared modules)", ""]
    for s, o in sims[:3]:
        extra = [mid for mid in role_modules(doc, o) if mid not in mine]
        out.append(f"- [{o['name']}]({o['id']}.md): {s:.0%} overlap; to add it, also take "
                   + (", ".join(extra) if extra else "nothing new"))
    out.append("")
    return "\n".join(out)


def gen_readme_paths(doc) -> str:
    paths = {p["id"]: p for p in doc["paths"]}
    mods = by_id(doc)
    def n_lessons(mids):
        return sum(len(mods[x]["lessons"]) for x in mids)
    out = ["## 🧭 Choose Your Path", "",
           "The course is a catalogue of **modules**. A **path** is an ordered list of modules for one skill area. "
           "A **role** combines paths to match a real job. Every path starts with the Core modules "
           "(M01 Python, M03 Git, M04 Linux). Hybrid profiles are common, so you can combine roles. "
           "Each role page shows its closest roles and what extra modules you need.", "",
           "### Roles (job market, 2025–26)", "", "| Role | Combines | Modules | Lessons |", "| :--- | :--- | :-: | :-: |"]
    for r in doc["roles"]:
        order = role_modules(doc, r)
        comb = " + ".join(paths[p]["name"] for p in r["paths"]) + (" + " + ", ".join(r["extra_modules"]) if r.get("extra_modules") else "")
        out.append(f"| [{r['name']}](roles/{r['id']}.md) | {comb} | {len(order)} | {n_lessons(order)} |")
    out += ["", "### Atomic paths", "", "| Path | Module order | Lessons |", "| :--- | :--- | :-: |"]
    for p in doc["paths"]:
        out.append(f"| [{p['name']}](paths/{p['id']}.md) | {' → '.join(p['modules'])} | {n_lessons(p['modules'])} |")
    out.append("")
    return "\n".join(out)


def gen_readme_catalogue(doc) -> str:
    total = sum(len(m["lessons"]) for m in doc["modules"])
    c = Counter(l["status"] for m in doc["modules"] for l in m["lessons"])
    out = ["## 🛣️ Module Catalogue", "",
           f"**{len(doc['modules'])} modules · {total} lessons** "
           f"({total - c.get('planned', 0)} written, {c.get('planned', 0)} planned, {c.get('done', 0)} fully verified). "
           "Each module folder has its own README with the lesson list. Status per lesson: "
           + " · ".join(f"{v} {k}" for k, v in STATUS_ICON.items()) + ".", ""]
    groups = OrderedDict()
    for m in doc["modules"]:
        groups.setdefault(m["group"], []).append(m)
    for g, ms in groups.items():
        out += [f"### {GROUP_ICON.get(g, '')} {g}", "", "| Module | Lessons | Verified | Prerequisites | GPU |",
                "| :--- | :-: | :-: | :--- | :-: |"]
        for m in ms:
            ex, pl, done = counts(m)
            out.append(f"| [{m['id']} · {m['name']}]({urllib.parse.quote(module_dir(m))}/README.md) | "
                       f"{ex} + {pl} planned | {done} | {', '.join(m.get('prereqs', [])) or '—'} | {GPU_ICON[m['gpu']]} |")
        out.append("")
    return "\n".join(out)


def replace_block(text, name, content, fallback_start=None, fallback_end=None):
    b, e = f"<!-- BEGIN GENERATED:{name} -->", f"<!-- END GENERATED:{name} -->"
    block = f"{b}\n{content}\n{e}"
    if b in text:
        return re.sub(re.escape(b) + r".*?" + re.escape(e), lambda _: block, text, flags=re.S)
    i = text.index(fallback_start)
    j = text.index(fallback_end, i)
    return text[:i] + block + "\n\n" + text[j:]


def generate(doc):
    for m in doc["modules"]:
        d = os.path.join(ROOT, module_dir(m))
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
            f.write(gen_module_readme(doc, m))
    for sub, items, fn in (("paths", doc["paths"], gen_path_page), ("roles", doc["roles"], gen_role_page)):
        d = os.path.join(ROOT, sub)
        os.makedirs(d, exist_ok=True)
        keep = set()
        for it in items:
            keep.add(f"{it['id']}.md")
            with open(os.path.join(d, f"{it['id']}.md"), "w", encoding="utf-8") as f:
                f.write(fn(doc, it))
        for old in os.listdir(d):
            if old.endswith(".md") and old not in keep:
                os.remove(os.path.join(d, old))
    readme_path = os.path.join(ROOT, "README.md")
    text = open(readme_path, encoding="utf-8").read()
    text = replace_block(text, "paths", gen_readme_paths(doc), "## 🧭 Choose Your Path", "## 🚀 Getting Started")
    text = replace_block(text, "catalogue", gen_readme_catalogue(doc), "## 🛣️ Roadmap Plan", "### Notes on Supporting Material")
    text = re.sub(r"!\[(Sections|Modules)\]\(https://img\.shields\.io/badge/[^)]*\)",
                  f"![Modules](https://img.shields.io/badge/modules-{len(doc['modules'])}-blue)", text)
    open(readme_path, "w", encoding="utf-8").write(text)
    print(f"generate: README + {len(doc['modules'])} module READMEs + {len(doc['paths'])} paths + {len(doc['roles'])} roles")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--generate", action="store_true")
    ap.add_argument("--sync", action="store_true")
    ap.add_argument("--moves-out", help="write the {old: new} file mapping of --sync to this JSON file")
    a = ap.parse_args()
    if not (a.check or a.generate or a.sync):
        ap.error("choose at least one of --check, --generate, --sync")
    doc = load()
    if a.sync:
        moves = sync(doc)
        if a.moves_out:
            json.dump(moves, open(a.moves_out, "w"), indent=1, ensure_ascii=False)
    if a.generate:
        generate(doc)
    if a.check:
        sys.exit(check(doc))


if __name__ == "__main__":
    main()
