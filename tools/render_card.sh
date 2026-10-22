#!/bin/bash
# Render tools/assets/social-card.html to tools/assets/og-image.png (1200 x 630) with headless Chromium.
# Usage: tools/render_card.sh [path-to-chrome-or-headless_shell]
# Prefer chrome-headless-shell: the new headless mode trims the viewport below --window-size.
set -euo pipefail
cd "$(dirname "$0")/assets"
CHROME="${1:-${CHROME:-chromium}}"
PROXY_ARGS=()
HEADLESS_ARGS=(--headless=new)
case "$CHROME" in *headless_shell*) HEADLESS_ARGS=() ;; esac
if [ -n "${HTTPS_PROXY:-}" ]; then PROXY_ARGS=(--proxy-server="$HTTPS_PROXY"); fi
"$CHROME" "${HEADLESS_ARGS[@]}" --no-sandbox --disable-gpu --hide-scrollbars "${PROXY_ARGS[@]}" \
  --window-size=1200,630 --virtual-time-budget=8000 --allow-file-access-from-files \
  --screenshot="$PWD/og-image.png" "file://$PWD/social-card.html" >/dev/null 2>&1
echo "wrote $PWD/og-image.png"
