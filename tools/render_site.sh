#!/usr/bin/env bash
# Render the Quarto site (HTML + one PDF per lesson) and bind the module books. On WSL with the repo on a Windows drive (/mnt/*), Quarto's project cache (a database with
# WAL files) hangs, so the site is rendered in a mirror on the Linux filesystem and _site/ is copied back.
#   tools/render_site.sh            # render everything listed in _quarto.yml
#   tools/render_site.sh FILE...    # render only these files (paths relative to the repo root)
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
export PATH="$HOME/.local/bin:$PATH"
"$ROOT/.venv/bin/python" "$ROOT/tools/build_site.py"
if [[ "$ROOT" == /mnt/* ]]; then
  MIRROR="${SITE_MIRROR:-$HOME/.cache/fzth-site}"
  mkdir -p "$MIRROR"
  rsync -a --delete --exclude='/_site/' --exclude='.quarto/' --exclude='.venv/' --exclude='/data/' \
        --exclude='_legacy_untracked/' --include='*/' --include='*.ipynb' --include='*.qmd' --include='*.yml' \
        --include='*.scss' --include='*.css' --include='*.lua' --include='site/*.typ' \
        --include='site/*.html' --include='site/fonts/*' \
        --exclude='*' --prune-empty-dirs "$ROOT/" "$MIRROR/"
  cd "$MIRROR"
else
  cd "$ROOT"
fi
if [[ $# -eq 0 ]]; then
  quarto render
else
  for f in "$@"; do quarto render "$f"; done   # quarto render takes ONE input; extra args go to pandoc
fi
# bind the lesson PDFs of each module into a book (_site/pdf/mNN.pdf, linked from the module pages)
"$ROOT/.venv/bin/python" "$ROOT/tools/build_books.py" "$PWD/_site"
if [[ "$ROOT" == /mnt/* ]]; then
  rsync -a --delete "$MIRROR/_site/" "$ROOT/_site/"
fi
echo "site ready: $ROOT/_site/index.html"
