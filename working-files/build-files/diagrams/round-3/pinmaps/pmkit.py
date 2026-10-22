"""Drawing kit for the pin-map figures (adapted from ../svgkit.py).

The <style> block is copied verbatim from diagrams/04-fuel-pressure.svg, so the standalone SVG
looks like the others; on the site, build_html.inline_svg() drops it and page.css styles the classes.
Only classes carry color: no hard-coded fill or stroke outside the style block.
"""
import pathlib
import re
from xml.sax.saxutils import escape

DIAGRAMS = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/diagrams")
OUT = pathlib.Path(__file__).resolve().parent / "out"
_src = (DIAGRAMS / "04-fuel-pressure.svg").read_text(encoding="utf-8")
STYLE = re.search(r"<style>.*?</style>", _src, re.S).group(0)


def fmt(v) -> str:
    if isinstance(v, float):
        s = f"{v:.1f}"
        return s[:-2] if s.endswith(".0") else s
    return str(v)


def marker(mid: str, cls: str, size: float = 7) -> str:
    return (f'  <marker id="{mid}" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="{fmt(size)}" '
            f'markerHeight="{fmt(size)}" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="{cls}"/></marker>')


AH = marker("ah", "fill-fg")
# Dotted stroke for "only if present": a dash pattern, not a color, so it may sit on the element.
DOTS = ' stroke-dasharray="0.1 3.4" stroke-linecap="round"'


def svg_open(width: int, height: int, aria: str, extra_markers=()) -> str:
    defs = "\n".join([AH, *extra_markers])
    a = escape(aria, {'"': "&quot;"})
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" '
            f'aria-label="{a}" color="#1b2128">\n{STYLE}\n<defs>\n{defs}\n</defs>\n'
            f'<rect class="bg" x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>\n')


class Canvas:
    def __init__(self):
        self.parts = []

    def add(self, s: str):
        self.parts.append(s)

    def comment(self, s: str):
        self.parts.append(f"\n<!-- {s} -->")

    def rect(self, x, y, w, h, cls, rx=3, sw=None, dots=False):
        swa = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        swa += DOTS if dots else ""
        self.add(f'<rect class="{cls}" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" rx="{fmt(rx)}"{swa}/>')

    def circle(self, cx, cy, r, cls):
        self.add(f'<circle class="{cls}" cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}"/>')

    def path(self, pts_or_d, cls, end=None, start=None, sw=None, dots=False):
        if isinstance(pts_or_d, str):
            d = pts_or_d
        else:
            d = "M" + " L".join(f"{fmt(x)},{fmt(y)}" for x, y in pts_or_d)
        m = ""
        if end:
            m += f' marker-end="url(#{end})"'
        if start:
            m += f' marker-start="url(#{start})"'
        swa = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        swa += DOTS if dots else ""
        self.add(f'<path class="{cls}" d="{d}"{swa}{m}/>')

    def line(self, x1, y1, x2, y2, cls, sw=None, end=None):
        self.path([(x1, y1), (x2, y2)], cls, end=end, sw=sw)

    def text(self, x, y, content, cls, anchor=None):
        """content: a string, or a list of strings / (string, class) tuples rendered as tspans."""
        a = f' text-anchor="{anchor}"' if anchor else ""
        if isinstance(content, str):
            inner = escape(content)
        else:
            bits = []
            for seg in content:
                if isinstance(seg, str):
                    bits.append(escape(seg))
                else:
                    s, c = seg
                    bits.append(f'<tspan class="{c}">{escape(s)}</tspan>')
            inner = "".join(bits)
        self.add(f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{inner}</text>')

    def svg(self, width, height, aria, markers=()) -> str:
        return svg_open(width, height, aria, markers) + "\n".join(self.parts) + "\n</svg>\n"


def write(name: str, body: str) -> pathlib.Path:
    OUT.mkdir(exist_ok=True)
    p = OUT / name
    p.write_text(body, encoding="utf-8")
    return p
