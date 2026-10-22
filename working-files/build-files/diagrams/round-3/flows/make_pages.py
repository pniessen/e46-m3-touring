#!/usr/bin/env python3
"""Build one test page per SVG, inlined exactly as tools/build_html.py does it (landscape figures).

    python3 make_pages.py OUTDIR path/to/a.svg [path/to/b.svg ...]

Each page loads tools/page.css (inline) and the same Google Fonts the site uses, and wraps the
inlined SVG in <figure class="diagram"><div class="diagram-scroll">...</div><p class="scroll-hint">
...</p><figcaption>...</figcaption></figure>, as build_html.py does for a figure without <!-- portrait -->.
A <main> inside a body grid puts the figure in the same column width as the site at 1440 px.
"""
import pathlib
import sys

sys.dont_write_bytecode = True  # don't leave .pyc files in the project's tools/ folder
ROOT = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion")
sys.path.insert(0, str(ROOT / "tools"))
from build_html import inline_svg  # noqa: E402  (the real function the site uses)

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500'
         '&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap">')


def page(svg_path: pathlib.Path, caption: str = "") -> str:
    css = (ROOT / "tools" / "page.css").read_text(encoding="utf-8")
    svg = inline_svg(svg_path, "d" + svg_path.stem)
    cap = caption or f"Figure N. Test caption for {svg_path.name}."
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{FONTS}
<style>
{css}
</style></head><body>
<nav class="chapters"><ol><li><a href="#">Chapters</a></li></ol></nav>
<main><div class="wrap"><section>
<h3>{svg_path.name}</h3>
<figure class="diagram"><div class="diagram-scroll">{svg}</div><p class="scroll-hint">Swipe sideways to see the whole diagram</p>
<figcaption>{cap}</figcaption></figure>
</section></div></main>
</body></html>
"""


if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    for arg in sys.argv[2:]:
        p = pathlib.Path(arg)
        dest = out / (p.stem + ".html")
        dest.write_text(page(p), encoding="utf-8")
        print("wrote", dest)
