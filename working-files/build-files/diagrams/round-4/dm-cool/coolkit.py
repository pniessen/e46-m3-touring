"""dm-cool helpers on top of svgkit.py (the portrait kit, copied from r4fold/tools).

Adds drawing helpers and a text-width cache measured in Chromium with the site's page.css and
fonts (measure_cache.js, copied from last round's landscape kit). Generators call width() to
place text, then flush(); if flush() measured new strings, run the generator again.
"""
import json
import os
import pathlib
import subprocess
import sys
from xml.sax.saxutils import escape

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import svgkit as K  # noqa: E402

STYLE = K.STYLE
fmt = K.fmt
MARKERS = {"ah": "fill-fg", "ahd": "donor-f", "ahn": "new-f", "ahf": "fab-f", "ahk": "keep-f", "ahc": "crit-f"}

# ---------------------------------------------------------------- text widths
CACHE = HERE / "widths.json"
_cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
_pending = set()
WARN = []


def _size(cls):
    c = f" {cls} "
    if " t-h " in c:
        return 15.0
    if " t-xs " in c:
        return 10.5
    if " t-sm " in c:
        return 11.5
    return 13.0


def width(cls: str, s: str, std=False) -> float:
    """Rendered width in user units with the site CSS (std=True: the SVG's own style block)."""
    k = cls + "|" + s
    if k in _cache:
        return _cache[k]["std" if std else "page"]
    _pending.add(k)
    per = 0.62 if "t-mono" in cls else 0.56
    return len(s) * _size(cls) * per


def rwidth(cls: str, runs) -> float:
    """Width of a rich text: runs = [(extra_cls_or_None, str), ...]."""
    return sum(max(width(f"{cls} {c}" if c else cls, s), width(f"{cls} {c}" if c else cls, s, True))
               for c, s in runs)


def flush() -> bool:
    global _cache
    if not _pending:
        return False
    req = HERE / "measure_req.txt"
    req.write_text("\n".join(sorted(_pending)), encoding="utf-8")
    env = dict(os.environ)
    env["NODE_PATH"] = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    subprocess.run(["node", str(HERE / "measure_cache.js"), str(req), str(CACHE)], check=True, env=env)
    _cache = json.loads(CACHE.read_text())
    _pending.clear()
    return True


# ---------------------------------------------------------------- document
class Doc:
    def __init__(self):
        self.parts = []

    def add(self, s):
        self.parts.append(s)

    def comment(self, s):
        self.parts.append(f"\n<!-- {s} -->")

    def text(self, cls, x, y, s, anchor=None, maxw=None):
        a = f' text-anchor="{anchor}"' if anchor and anchor != "start" else ""
        w = max(width(cls, s), width(cls, s, True))
        if maxw is not None and w > maxw:
            WARN.append(f"too wide ({w:.0f} > {maxw:.0f}): {s}")
        self.parts.append(f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{escape(s)}</text>')
        return w

    def rich(self, cls, x, y, runs, anchor=None, maxw=None):
        a = f' text-anchor="{anchor}"' if anchor and anchor != "start" else ""
        w = rwidth(cls, runs)
        if maxw is not None and w > maxw:
            WARN.append(f"too wide ({w:.0f} > {maxw:.0f}): {''.join(s for _, s in runs)}")
        inner = "".join(f'<tspan class="{c}">{escape(s)}</tspan>' if c else escape(s) for c, s in runs)
        self.parts.append(f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{inner}</text>')
        return w

    def lines(self, cls, x, y, rows, lh, anchor=None, maxw=None):
        """Several lines; a row is a str or a list of runs. Returns the y after the last line."""
        for r in rows:
            if isinstance(r, str):
                self.text(cls, x, y, r, anchor, maxw)
            else:
                self.rich(cls, x, y, r, anchor, maxw)
            y += lh
        return y

    def rect(self, cls, x, y, w, h, rx=None, sw=None, style=None):
        r = f' rx="{fmt(rx)}"' if rx is not None else ""
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        st = f' style="{style}"' if style else ""
        self.parts.append(f'<rect class="{cls}" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}"{r}{s}{st}/>')

    def line(self, cls, x1, y1, x2, y2, sw=None, end=None, start=None, style=None):
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        me = f' marker-end="url(#{end})"' if end else ""
        ms = f' marker-start="url(#{start})"' if start else ""
        st = f' style="{style}"' if style else ""
        self.parts.append(f'<line class="{cls}" x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}"{s}{st}{me}{ms}/>')

    def path(self, cls, d, sw=None, end=None, start=None, style=None):
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        me = f' marker-end="url(#{end})"' if end else ""
        ms = f' marker-start="url(#{start})"' if start else ""
        st = f' style="{style}"' if style else ""
        self.parts.append(f'<path class="{cls}" d="{d}"{s}{st}{me}{ms}/>')

    def circle(self, cls, cx, cy, r, sw=None, style=None):
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        st = f' style="{style}"' if style else ""
        self.parts.append(f'<circle class="{cls}" cx="{fmt(cx)}" cy="{fmt(cy)}" r="{fmt(r)}"{s}{st}/>')

    def badge(self, cx, cy, label, r=7.5):
        """A step number in a filled circle (white text on the foreground colour)."""
        self.circle("fill-fg", cx, cy, r)
        self.parts.append(f'<text class="t-xs t-b" x="{fmt(cx)}" y="{fmt(cy + 3.7)}" text-anchor="middle" '
                          f'style="fill:var(--surface,#fff)">{escape(label)}</text>')

    def ground(self, x, y, cls="ln"):
        """Ground symbol hanging from (x, y)."""
        self.path(cls, f"M{fmt(x - 9)},{fmt(y)} H{fmt(x + 9)} M{fmt(x - 5.5)},{fmt(y + 4.5)} H{fmt(x + 5.5)} "
                       f"M{fmt(x - 2)},{fmt(y + 9)} H{fmt(x + 2)}")

    def body(self):
        return "\n".join(self.parts)


def svg_open(height, aria, markers=("ah",)):
    defs = "\n".join(K.marker(m, MARKERS[m]) for m in markers)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 {height}" role="img" '
            f'aria-label="{escape(aria, {chr(34): "&quot;"})}" color="#1b2128">\n{STYLE}\n<defs>\n{defs}\n</defs>\n'
            f'<rect class="bg" x="0" y="0" width="400" height="{height}" fill="#ffffff"/>\n')


def write(name, head, body):
    p = K.DIAGRAMS / name
    p.write_text(head + body + "\n</svg>\n", encoding="utf-8")
    return p


def report():
    for w in WARN:
        print("WARN", w)
