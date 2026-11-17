#!/usr/bin/env bash
# Render the Quarto site. On WSL with the repo on a Windows drive (/mnt/*), Quarto's project cache (a database with
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
  rsync -a --delete --include='*/' --include='*.ipynb' --include='*.qmd' --include='*.yml' \
        --include='*.scss' --include='*.css' --include='*.lua' \
        --exclude='_site/***' --exclude='.quarto/***' --exclude='.venv/***' --exclude='data/***' \
        --exclude='_legacy_untracked/***' --exclude='*' --prune-empty-dirs "$ROOT/" "$MIRROR/"
  cd "$MIRROR"
else
  cd "$ROOT"
fi
if [[ $# -eq 0 ]]; then
  quarto render
else
  for f in "$@"; do quarto render "$f"; done   # quarto render takes ONE input; extra args go to pandoc
fi
if [[ "$ROOT" == /mnt/* ]]; then
  rsync -a --delete "$MIRROR/_site/" "$ROOT/_site/"
fi
echo "site ready: $ROOT/_site/index.html"
