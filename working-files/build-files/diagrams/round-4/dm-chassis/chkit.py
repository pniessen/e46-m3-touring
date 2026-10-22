"""dm-chassis kit, built from the round's portrait kit (svgkit_portrait_orig.py) and the
landscape kit's Doc class (kit_landscape_orig.py): the house <style> block copied verbatim
from diagrams/04-fuel-pressure.svg, the root element, coloured arrowheads, a background, and
text widths estimated from a per-character table measured in Chromium (measure_chars.js), both
with the site's page.css and fonts ("page") and with the SVG's own style block ("std").
Layout uses the wider of the two, so the figure fits on the site and as a standalone file."""
import json
import pathlib
import re
from xml.sax.saxutils import escape

HERE = pathlib.Path(__file__).resolve().parent
DIAGRAMS = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/diagrams")
_src = (DIAGRAMS / "04-fuel-pressure.svg").read_text(encoding="utf-8")
STYLE = re.search(r"<style>.*?</style>", _src, re.S).group(0)

MARKERS = {"ah": "fill-fg", "ahf": "fab-f", "ahn": "new-f", "ahd": "donor-f", "ahk": "keep-f", "ahc": "crit-f"}


def marker(mid: str, cls: str) -> str:
    return (f'  <marker id="{mid}" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="{cls}"/></marker>')


def svg_open(width: int, height: int, aria: str, markers=("ah",)) -> str:
    defs = "\n".join(marker(m, MARKERS[m]) for m in markers)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" '
            f'aria-label="{escape(aria, {chr(34): "&quot;"})}" color="#1b2128">\n{STYLE}\n<defs>\n{defs}\n</defs>\n'
            f'<rect class="bg" x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>\n')


def fmt(v) -> str:
    if isinstance(v, float):
        s = f"{v:.1f}"
        return s[:-2] if s.endswith(".0") else s
    return str(v)


# ---------------------------------------------------------------- text widths
_CH = json.loads((HERE / "chars.json").read_text())
SIZE = {"t": 13, "t-sm": 11.5, "t-xs": 10.5, "t-h": 13}


def _norm(cls: str) -> str:
    """Map any class string to one measured in chars.json."""
    c = set(cls.split())
    size = "t-h" if "t-h" in c else "t-xs" if "t-xs" in c else "t-sm" if "t-sm" in c else "t"
    if size == "t-h":
        return "t-h"
    key = size + (" t-b" if "t-b" in c else "") + (" t-mono" if "t-mono" in c else "")
    return key


def width_mode(cls: str, s: str, mode: str) -> float:
    tab = _CH[mode][_norm(cls)]
    if "t-h" in cls.split() and mode == "page":
        s = s.upper()
    default = SIZE[_norm(cls).split()[0]] * 0.62
    return sum(tab.get(ch, default) for ch in s)


def width(cls: str, s: str) -> float:
    """Wider of the site rendering and the standalone rendering, plus 2% for kerning slop."""
    return max(width_mode(cls, s, "page"), width_mode(cls, s, "std")) * 1.02


def runs_width(cls: str, runs) -> float:
    """Width of a <text> made of runs [(extra_cls_or_None, str), ...]."""
    tot = 0.0
    for extra, s in runs:
        c = cls + (" " + extra if extra else "")
        # a tspan's own size class wins over the parent's
        if extra and any(k in extra.split() for k in ("t", "t-sm", "t-xs")):
            c = " ".join(k for k in cls.split() if k not in ("t", "t-sm", "t-xs")) + " " + extra
        tot += width(c, s)
    return tot


_UNITS = r"(mm|Nm|bar|psi|L|lb|N|in|ft-lb|in-lb|kg|°C|°F|°|qt|US|%|mph|km/h|L/min|teeth|turns)"


def wrap(cls: str, s: str, maxw: float):
    """Greedy word wrap to maxw user units. A number and its unit ("110 N", "70 °C",
    "1.6 US qt") never split across lines."""
    nb = " "
    s = re.sub(r"(\d) (?=" + _UNITS + r"\b|°)", "\\1" + nb, s)
    s = s.replace("US qt", "US" + nb + "qt")
    words = s.split(" ")
    lines, cur = [], ""
    for w in words:
        cand = (cur + " " + w).strip()
        if cur and width(cls, cand.replace(nb, " ")) > maxw:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    return [ln.replace(nb, " ") for ln in lines]


# ---------------------------------------------------------------- drawing helpers
class Doc:
    def __init__(self):
        self.parts = []
        self.texts = []  # (cls, x, y, string, anchor) for self-checks

    def add(self, s: str):
        self.parts.append(s)

    def comment(self, s: str):
        self.parts.append(f"\n<!-- {s} -->")

    def text(self, cls, x, y, s, anchor=None):
        a = f' text-anchor="{anchor}"' if anchor and anchor != "start" else ""
        self.texts.append((cls, x, y, s, anchor))
        self.parts.append(f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{escape(s)}</text>')

    def rich(self, cls, x, y, runs, anchor=None):
        """One <text> with <tspan> runs: runs = [(extra_cls_or_None, str), ...]."""
        a = f' text-anchor="{anchor}"' if anchor and anchor != "start" else ""
        inner = "".join(f'<tspan class="{c}">{escape(s)}</tspan>' if c else escape(s) for c, s in runs)
        self.texts.append((cls, x, y, "".join(s for _, s in runs), anchor))
        self.parts.append(f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{inner}</text>')

    def lines(self, cls, x, y, lines, lh, anchor=None):
        """Several lines of one class; returns the y of the last baseline."""
        for i, s in enumerate(lines):
            self.text(cls, x, y + i * lh, s, anchor)
        return y + (len(lines) - 1) * lh

    def para(self, cls, x, y, s, maxw, lh, anchor=None):
        ls = wrap(cls, s, maxw)
        return self.lines(cls, x, y, ls, lh, anchor), len(ls)

    def rect(self, cls, x, y, w, h, rx=None, sw=None, extra=""):
        r = f' rx="{fmt(rx)}"' if rx is not None else ""
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        self.parts.append(f'<rect class="{cls}" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}"{r}{s}{extra}/>')

    def line(self, cls, x1, y1, x2, y2, sw=None, end=None, start=None):
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        me = f' marker-end="url(#{end})"' if end else ""
        ms = f' marker-start="url(#{start})"' if start else ""
        self.parts.append(f'<line class="{cls}" x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}"{s}{me}{ms}/>')

    def path(self, cls, d, sw=None, end=None, start=None, extra=""):
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        me = f' marker-end="url(#{end})"' if end else ""
        ms = f' marker-start="url(#{start})"' if start else ""
        self.parts.append(f'<path class="{cls}" d="{d}"{s}{me}{ms}{extra}/>')

    def circle(self, cls, x, y, r, sw=None, extra=""):
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        self.parts.append(f'<circle class="{cls}" cx="{fmt(x)}" cy="{fmt(y)}" r="{fmt(r)}"{s}{extra}/>')

    def body(self) -> str:
        return "\n".join(self.parts)


def key(d: Doc, x, y, items, gap=14):
    """A row of key swatches: items = [(swatch_cls, label), ...]; returns the end x.
    A swatch class of 'remove' draws a dashed grey box with a red cross."""
    for cls, label in items:
        if cls == "remove":
            d.rect("keep dash", x, y, 12, 12, rx=2, sw=1)
            d.path("crit-s", f"M{fmt(x + 2.5)},{fmt(y + 2.5)} l7,7 M{fmt(x + 2.5)},{fmt(y + 9.5)} l7,-7", sw=1.6)
        else:
            d.rect(cls, x, y, 12, 12, rx=2, sw=1)
        d.text("t-sm", x + 17, y + 10.5, label)
        x += 17 + width("t-sm", label) + gap
    return x


def write(name: str, head: str, body: str) -> pathlib.Path:
    p = DIAGRAMS / name
    txt = head + body + "\n</svg>\n"
    p.write_text(txt, encoding="utf-8")
    return p
