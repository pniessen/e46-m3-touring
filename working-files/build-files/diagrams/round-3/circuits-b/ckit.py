"""Circuit-diagram kit for the wiring figures (circuits-b).

Based on ../svgkit.py: the house <style> block is copied verbatim from diagrams/04-fuel-pressure.svg,
the `ah` marker as in 06-electronics.svg, coloured markers as in 10-repin-map.svg. Adds a viewBox
width parameter (landscape figures are 800 wide), a measured-width cache (site CSS and fonts, via
measure_json.js) and a few drawing helpers. Colour comes only from the house classes.
"""
import json
import os
import pathlib
import re
import subprocess
from xml.sax.saxutils import escape

HERE = pathlib.Path(__file__).resolve().parent
DIAGRAMS = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/diagrams")
_src = (DIAGRAMS / "04-fuel-pressure.svg").read_text(encoding="utf-8")
STYLE = re.search(r"<style>.*?</style>", _src, re.S).group(0)

AH = ('  <marker id="ah" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" '
      'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="fill-fg"/></marker>')


def marker(mid, cls):
    return (f'  <marker id="{mid}" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="{cls}"/></marker>')


def svg_open(width, height, aria, extra_markers=()):
    defs = "\n".join([AH, *extra_markers])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" '
            f'aria-label="{escape(aria, {chr(34): "&quot;"})}" color="#1b2128">\n{STYLE}\n<defs>\n{defs}\n</defs>\n'
            f'<rect class="bg" x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>\n')


def fmt(v):
    if isinstance(v, float):
        s = f"{v:.1f}"
        return s[:-2] if s.endswith(".0") else s
    return str(v)


# ------------------------------------------------------------------ measured widths
CACHE = HERE / "widths.json"
_w = json.loads(CACHE.read_text()) if CACHE.exists() else {}
_missing = []


def W(cls, s):
    """Width of s in class cls as the site renders it; 0 and queued if not yet measured."""
    k = f"{cls}|{s}"
    if k in _w:
        return _w[k]
    if [cls, s] not in _missing:
        _missing.append([cls, s])
    return 7.0 * len(s)  # rough until measured


def measure_missing():
    """Measure queued strings; returns True if anything was measured (caller should re-run)."""
    global _w
    if not _missing:
        return False
    tmp = HERE / "pending.json"
    tmp.write_text(json.dumps(_missing))
    env = dict(os.environ)
    env["NODE_PATH"] = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
    subprocess.run(["node", str(HERE / "measure_json.js"), str(tmp), str(CACHE)], check=True, env=env)
    _w = json.loads(CACHE.read_text())
    _missing.clear()
    return True


# ------------------------------------------------------------------ text
def t(cls, x, y, s, anchor=None, extra=""):
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}{extra}>{escape(s)}</text>'


def tm(cls, x, y, parts, anchor=None):
    """Mixed text: parts is a list of (text, is_mono). Mono parts become <tspan class="t-mono">."""
    a = f' text-anchor="{anchor}"' if anchor else ""
    inner = "".join(f'<tspan class="t-mono">{escape(s)}</tspan>' if m else escape(s) for s, m in parts)
    return f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{inner}</text>'


def tm_width(cls, parts):
    # SVG drops a text element's leading and trailing spaces, so measure segment spaces as no-break spaces
    return sum(W(cls + (" t-mono" if m else ""), s.replace(" ", "\u00a0")) for s, m in parts)


def M(s):
    """Parse 'plain [mono] plain' into parts: text in square brackets is mono."""
    parts = []
    for i, chunk in enumerate(re.split(r"\[|\]", s)):
        if chunk:
            parts.append((chunk, i % 2 == 1))
    return parts


# ------------------------------------------------------------------ shapes
def rect(cls, x, y, w, h, rx=5, sw="1.5", extra=""):
    return (f'<rect class="{cls}" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" '
            f'rx="{rx}" stroke-width="{sw}"{extra}/>')


def line(cls, x1, y1, x2, y2, sw=None, mk=None, extra=""):
    s = f' stroke-width="{sw}"' if sw else ""
    m = f' marker-end="url(#{mk})"' if mk else ""
    return f'<line class="{cls}" x1="{fmt(x1)}" y1="{fmt(y1)}" x2="{fmt(x2)}" y2="{fmt(y2)}"{s}{m}{extra}/>'


def path(cls, d, sw=None, mk=None, extra=""):
    s = f' stroke-width="{sw}"' if sw else ""
    m = f' marker-end="url(#{mk})"' if mk else ""
    return f'<path class="{cls}" d="{d}"{s}{m}{extra}/>'


def dot(cls, x, y, r=3.2):
    """A splice: a filled dot (cls is a fill class such as fill-fg or keep-f)."""
    return f'<circle class="{cls}" cx="{fmt(x)}" cy="{fmt(y)}" r="{r}"/>'


def ring(x, y, r=3.5):
    """An open end: a hollow circle."""
    return f'<circle class="shape" cx="{fmt(x)}" cy="{fmt(y)}" r="{r}"/>'


def pin_cell(x, y, label, w=24, h=18, cls="t-sm t-mono t-b"):
    """A small pin-number cell (white box with the cavity number) centred on (x, y)."""
    return (rect("shape", x - w / 2, y - h / 2, w, h, rx=2, sw="1.2") + "\n"
            + t(cls, x, y + 4.1, label, "middle"))


def write(name, body):
    p = DIAGRAMS / name
    p.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    return p
