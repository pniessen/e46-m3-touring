#!/usr/bin/env python3
"""Build one test page per SVG, inlined exactly as tools/build_html.py does it (adapted from make_pages.py).

    python3 make_pages_b.py OUTDIR [--portrait] a.svg [--portrait] b.svg ...

--portrait applies to the SVG that follows it: only those get the `portrait` class on .diagram-scroll,
as build_html.py does for images marked <!-- portrait -->. Each page also carries the scroll hint the
site adds after landscape figures.
"""
import pathlib
import sys

sys.dont_write_bytecode = True  # don't leave .pyc files in the project's tools/ folder
ROOT = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion")
sys.path.insert(0, str(ROOT / "tools"))
from build_html import inline_svg  # noqa: E402  (the real function the site uses)

FONTS = ('<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500'
         '&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap">')


def page(svg_path: pathlib.Path, portrait: bool) -> str:
    css = (ROOT / "tools" / "page.css").read_text(encoding="utf-8")
    svg = inline_svg(svg_path, "d" + svg_path.stem)
    cls = "diagram-scroll portrait" if portrait else "diagram-scroll"
    hint = "" if portrait else '<p class="scroll-hint">Swipe sideways to see the whole diagram</p>'
    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
{FONTS}
<style>
{css}
</style></head><body>
<main><div class="wrap"><section>
<h3>{svg_path.name}</h3>
<p>Some body text before the figure, as on the page, so the figure sits in the reading column.</p>
<figure class="diagram"><div class="{cls}">{svg}</div>{hint}
<figcaption>Figure N. Test caption for {svg_path.name}.</figcaption></figure>
</section></div></main>
</body></html>
"""


if __name__ == "__main__":
    out = pathlib.Path(sys.argv[1])
    out.mkdir(parents=True, exist_ok=True)
    portrait = False
    for arg in sys.argv[2:]:
        if arg == "--portrait":
            portrait = True
            continue
        p = pathlib.Path(arg)
        dest = out / (p.stem + ".html")
        dest.write_text(page(p, portrait), encoding="utf-8")
        print("wrote", dest, "(portrait)" if portrait else "")
        portrait = False
