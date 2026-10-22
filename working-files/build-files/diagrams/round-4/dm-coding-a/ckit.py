"""Portrait (400-wide) kit for dm-coding-a.

Combines ../../tools/svgkit.py (the 400-wide root element and the house <style> block, copied
verbatim) with the text-width cache from last round's landscape kit (measure_cache.js measures
each label in Chromium, with the site's page.css and fonts and with the SVG's own style block).
The style block is read from orig/12-coding-order.svg, a saved copy of a house diagram, so the
generators don't depend on files other makers may be rewriting.

Usage in a generator:
    from ckit import Doc, svg_open, write, run
    def build(d: Doc) -> (height, aria): ...
    run(build, "NN-name.svg")      # measures any new strings in Chromium and rebuilds until stable
"""
import json
import os
import pathlib
import re
import subprocess
from xml.sax.saxutils import escape

HERE = pathlib.Path(__file__).resolve().parent
DIAGRAMS = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/diagrams")
STYLE = re.search(r"<style>.*?</style>", (HERE / "orig" / "12-coding-order.svg").read_text(encoding="utf-8"),
                  re.S).group(0)
W = 400

MARKERS = {"ah": "fill-fg", "ahf": "fab-f", "ahn": "new-f", "ahd": "donor-f", "ahk": "keep-f", "ahc": "crit-f"}


def marker(mid: str, cls: str) -> str:
    return (f'  <marker id="{mid}" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="{cls}"/></marker>')


def svg_open(height, aria: str, markers=("ah",)) -> str:
    defs = "\n".join(marker(m, MARKERS[m]) for m in markers)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {fmt(height)}" role="img" '
            f'aria-label="{escape(aria, {chr(34): "&quot;"})}" color="#1b2128">\n{STYLE}\n<defs>\n{defs}\n</defs>\n'
            f'<rect class="bg" x="0" y="0" width="{W}" height="{fmt(height)}" fill="#ffffff"/>\n')


def fmt(v) -> str:
    if isinstance(v, float):
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        return s if s not in ("-0", "") else "0"
    return str(v)


# ---------------------------------------------------------------- text widths
CACHE = HERE / "widths.json"
_cache = json.loads(CACHE.read_text()) if CACHE.exists() else {}
_pending = set()


def _size(cls: str) -> float:
    c = cls.split()
    if "t-h" in c:
        return 15.0
    if "t-xs" in c:
        return 10.5
    if "t-sm" in c:
        return 11.5
    return 13.0


def _exact(cls: str, s: str):
    v = _cache.get(cls + "|" + s)
    return None if v is None else max(v["page"], v["std"])


def _space(cls: str):
    a, b = _exact(cls, "x x"), _exact(cls, "xx")
    return None if a is None or b is None else a - b


def width(cls: str, s: str, queue: bool = True) -> float:
    """Rendered width in user units: the larger of the site rendering (page.css, Plex fonts) and
    the standalone file (the SVG's own style block). An unmeasured string is estimated from its
    measured words (exact to a pixel or so) and, if queue is set, queued for exact measurement."""
    e = _exact(cls, s)
    if e is not None:
        return e
    if queue:
        _pending.add(cls + "|" + s)
    words = s.split(" ")
    ws = [_exact(cls, w) for w in words]
    sp = _space(cls)
    if sp is not None and all(v is not None for v in ws):
        return sum(ws) + sp * (len(words) - 1)
    for w in words:
        if w and _exact(cls, w) is None:
            _pending.add(cls + "|" + w)
    _pending.update({cls + "|x x", cls + "|xx"})
    per = 0.62 if "t-mono" in cls.split() else 0.58
    if "t-b" in cls.split():
        per += 0.03
    return len(s) * _size(cls) * per


def runs_width(cls: str, runs) -> float:
    """Width of a <text> made of tspan runs [(extra_cls_or_None, str)], measured run by run."""
    return sum(width(f"{cls} {c}".strip() if c else cls, s) for c, s in runs)


def wrap(cls: str, s: str, maxw: float):
    """Greedy word wrap to maxw user units (measured widths)."""
    words, lines, cur = s.split(" "), [], ""
    for w in words:
        cand = (cur + " " + w) if cur else w
        if cur and width(cls, cand, queue=False) > maxw:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    for ln in lines:
        width(cls, ln)
    return lines


def flush_measurements() -> bool:
    """Measure queued strings in Chromium; True if the cache changed (so rebuild)."""
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
        width(cls, s)
        self.parts.append(f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{escape(s)}</text>')

    def rich(self, cls, x, y, runs, anchor=None):
        """One <text> with <tspan> runs: runs = [(extra_cls_or_None, str), ...]."""
        a = f' text-anchor="{anchor}"' if anchor and anchor != "start" else ""
        runs_width(cls, runs)
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

    def body(self) -> str:
        return "\n".join(self.parts)


def write(name: str, head: str, body: str) -> pathlib.Path:
    p = DIAGRAMS / name
    p.write_text(head + body + "\n</svg>\n", encoding="utf-8")
    return p


def _pending_after_dry_run(build) -> bool:
    """Build once silently to see whether any label still needs measuring."""
    import builtins
    real_print = builtins.print
    builtins.print = lambda *a, **k: None
    try:
        build(Doc())
    finally:
        builtins.print = real_print
    return bool(_pending)


def run(build, name: str, rounds: int = 15):
    """build(doc) -> (height, aria). Re-run until every string on the figure has been measured."""
    import builtins
    real_print = builtins.print
    for i in range(rounds):
        d = Doc()
        # only the final pass (every label measured) may report layout problems
        builtins.print = real_print if not _pending_after_dry_run(build) else (lambda *a, **k: None)
        height, aria = build(d)
        builtins.print = real_print
        if not flush_measurements():
            break
    else:
        print("WARNING: labels still unmeasured after", rounds, "rounds", flush=True)
    p = write(name, svg_open(height, aria, getattr(d, "markers", ("ah",))), d.body())
    print("wrote", p, "height", fmt(height), flush=True)
    return p
