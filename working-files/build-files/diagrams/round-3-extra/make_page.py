#!/usr/bin/env python3
"""Wrap one diagram SVG the way tools/build_html.py does, for previewing.

    python3 make_page.py path/to/NN-name.svg out.html "Caption text"
"""
import pathlib
import sys

ROOT = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion")
sys.path.insert(0, str(ROOT / "tools"))
from build_html import inline_svg  # the real function the site uses

svg_path = pathlib.Path(sys.argv[1])
out = pathlib.Path(sys.argv[2])
caption = sys.argv[3] if len(sys.argv) > 3 else ""
css = (ROOT / "tools" / "page.css").read_text(encoding="utf-8")
svg = inline_svg(svg_path, "d" + svg_path.stem)
here = pathlib.Path(__file__).resolve().parent
page = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<link rel="stylesheet" href="{here / 'fonts' / 'fonts.css'}">
<style>
{css}
</style>
</head>
<body>
<main data-page="guide"><div class="wrap"><section id="test">
<p>Paragraph before the figure, for context.</p>
<figure class="diagram"><div class="diagram-scroll portrait">{svg}</div><figcaption>{caption}</figcaption></figure>
<p>Paragraph after the figure.</p>
</section></div></main>
</body>
</html>
"""
out.write_text(page, encoding="utf-8")
print("wrote", out)
