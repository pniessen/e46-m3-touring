"""Landscape diagram kit (adapted from ../svgkit.py): the house <style> block copied verbatim
from diagrams/04-fuel-pressure.svg, the root element, markers, background, and a text-width
cache measured in Chromium with the site's own CSS and fonts (see measure_cache.js)."""
import json
import pathlib
import re
import subprocess
import os
from xml.sax.saxutils import escape

HERE = pathlib.Path(__file__).resolve().parent
DIAGRAMS = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/diagrams")
_src = (HERE / "orig" / "04-fuel-pressure.svg").read_text(encoding="utf-8")  # the original house style block, saved before the redraw
STYLE = re.search(r"<style>.*?</style>", _src, re.S).group(0)


def marker(mid: str, cls: str) -> str:
    return (f'  <marker id="{mid}" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="{cls}"/></marker>')


MARKERS = {"ah": "fill-fg", "ahf": "fab-f", "ahn": "new-f", "ahd": "donor-f", "ahk": "keep-f", "ahc": "crit-f"}


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
CACHE = HERE / "widths.json"
_cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
_pending = set()


def _key(cls, s):
    return cls + "|" + s


def width(cls: str, s: str) -> float:
    """Rendered width in SVG user units, measured with the page CSS (falls back to an estimate
    and queues the string for measurement)."""
    k = _key(cls, s)
    if k in _cache:
        return _cache[k]["page"]
    _pending.add(k)
    size = 15 if "t-h" in cls else 13 if " t " in f" {cls} " or cls.split()[0] == "t" else 11.5
    per = 0.62 if "t-mono" in cls else 0.56
    return len(s) * size * per


def width_std(cls: str, s: str) -> float:
    """Width with the SVG's own <style> block (standalone file, Plex/Arial fallback)."""
    k = _key(cls, s)
    if k in _cache:
        return _cache[k]["std"]
    _pending.add(k)
    return width(cls, s)


def flush_measurements() -> bool:
    """Measure any queued strings; returns True if the cache changed (re-run the generator)."""
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


# ---------------------------------------------------------------- drawing helpers
class Doc:
    def __init__(self):
        self.parts = []

    def add(self, s: str):
        self.parts.append(s)

    def comment(self, s: str):
        self.parts.append(f"\n<!-- {s} -->")

    def text(self, cls, x, y, s, anchor=None):
        a = f' text-anchor="{anchor}"' if anchor and anchor != "start" else ""
        width(cls, s)  # queue for measurement
        width_std(cls, s)
        self.parts.append(f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{escape(s)}</text>')

    def rich(self, cls, x, y, runs, anchor=None):
        """One <text> with <tspan> runs: runs = [(extra_cls_or_None, str), ...]."""
        a = f' text-anchor="{anchor}"' if anchor and anchor != "start" else ""
        inner = "".join(f'<tspan class="{c}">{escape(s)}</tspan>' if c else escape(s) for c, s in runs)
        self.parts.append(f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{inner}</text>')

    def rect(self, cls, x, y, w, h, rx=None, sw=None, extra=""):
        r = f' rx="{fmt(rx)}"' if rx is not None else ""
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        self.parts.append(f'<rect class="{cls}" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}"{r}{s}{extra}/>')

    def line(self, cls, x1, y1, x2, y2, sw=None, end=None, start=None):
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        me = f' marker-end="url(#{end})"' if end else ""
        ms = f' marker-start="url(#{start})"' if start else ""
        self.parts.append(f'<line class="{cls}" x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}"{s}{me}{ms}/>')

    def path(self, cls, d, sw=None, end=None, start=None):
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        me = f' marker-end="url(#{end})"' if end else ""
        ms = f' marker-start="url(#{start})"' if start else ""
        self.parts.append(f'<path class="{cls}" d="{d}"{s}{me}{ms}/>')

    def dot(self, cls, x, y, r=3.2):
        self.parts.append(f'<circle class="{cls}" cx="{fmt(x)}" cy="{fmt(y)}" r="{fmt(r)}"/>')

    def circle(self, cls, x, y, r, sw=None):
        s = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
        self.parts.append(f'<circle class="{cls}" cx="{fmt(x)}" cy="{fmt(y)}" r="{fmt(r)}"{s}/>')

    def body(self) -> str:
        return "\n".join(self.parts)


def write(name: str, head: str, body: str) -> pathlib.Path:
    p = DIAGRAMS / name
    txt = head + body + "\n</svg>\n"
    p.write_text(txt, encoding="utf-8")
    return p
