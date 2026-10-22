"""Layout kit for the landscape flow figures (800 wide).

House style: the <style> block is copied verbatim from diagrams/04-fuel-pressure.svg (as the shared
svgkit.py does), the `ah` marker from 06/12, a `bg` rect, role="img", a full aria-label and
color="#1b2128" on the root. Text widths come from measure_words.js (the site's CSS and fonts, and the
SVG's own style block for a standalone view); the wider of the two is used for wrapping.

Rich text: a "run list" is a list of (cls, text) pairs; cls is added to the line's base class on a
<tspan>. A plain string is one run with no extra class. " " glues words together.
"""
import json
import pathlib
import re
import subprocess
import os
from xml.sax.saxutils import escape

HERE = pathlib.Path(__file__).resolve().parent
DIAGRAMS = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/diagrams")
STYLE = re.search(r"<style>.*?</style>", (DIAGRAMS / "04-fuel-pressure.svg").read_text(encoding="utf-8"), re.S).group(0)
AH = ('  <marker id="ah" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" '
      'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="fill-fg"/></marker>')

FONT_TOKENS = ("t", "t-sm", "t-xs", "t-b", "t-h", "t-mono")
SIZE = {"t": 13.0, "t-sm": 11.5, "t-xs": 10.5, "t-h": 15.0}
LINE_H = {"t": 16.0, "t-sm": 14.5, "t-xs": 13.0, "t-h": 18.0}
CACHE = HERE / "widths.json"
SAFETY = 1.0  # extra multiplier on measured widths


def fmt(v) -> str:
    if isinstance(v, float):
        s = f"{v:.2f}".rstrip("0").rstrip(".")
        return s if s != "-0" else "0"
    return str(v)


def font_key(cls: str) -> str:
    toks = set(cls.split())
    size = "t-h" if "t-h" in toks else "t-sm" if "t-sm" in toks else "t-xs" if "t-xs" in toks else "t"
    key = [size]
    if "t-b" in toks and size != "t-h":
        key.append("t-b")
    if "t-mono" in toks:
        key.append("t-mono")
    return " ".join(key)


def size_of(cls: str) -> float:
    return SIZE[font_key(cls).split()[0]]


class Measurer:
    def __init__(self):
        self.data = json.loads(CACHE.read_text()) if CACHE.exists() else {"page": {}, "solo": {}}
        self.missing = set()

    def width(self, key: str, s: str) -> float:
        k = key + "|" + s
        if k in self.data["page"]:
            return max(self.data["page"][k], self.data["solo"][k]) * SAFETY
        self.missing.add((key, s))
        return len(s) * SIZE[key.split()[0]] * (0.62 if "t-mono" in key else 0.56)

    def space(self, key: str) -> float:
        return self.width(key, "x x") - self.width(key, "xx")

    def flush(self) -> bool:
        """Measure missing words; True if anything was measured (the caller should lay out again)."""
        if not self.missing:
            return False
        need = set(self.missing)
        for key, _ in list(need):
            need.add((key, "x x"))
            need.add((key, "xx"))
        need = sorted(need)
        inp, out = HERE / "_measure_in.json", HERE / "_measure_out.json"
        inp.write_text(json.dumps([[k, s] for k, s in need]))
        env = dict(os.environ)
        env["NODE_PATH"] = subprocess.run(["npm", "root", "-g"], capture_output=True, text=True).stdout.strip()
        subprocess.run(["node", str(HERE / "measure_words.js"), str(inp), str(out)], check=True, env=env)
        res = json.loads(out.read_text())
        for env_name in ("page", "solo"):
            self.data[env_name].update(res[env_name])
        CACHE.write_text(json.dumps(self.data))
        self.missing.clear()
        return True


M = Measurer()


GLUE = [(re.compile(r"(\d) \((0x)"), "\\1\u00a0(\\2"),                      # 130 (0x82) stays together
        (re.compile(r"\b(faults?|location) (\d)"), "\\1\u00a0\\2"),          # fault 106, location 1
        (re.compile(r"\b(Session|Phase|steps?|question) (\d)"), "\\1\u00a0\\2"),  # Session 3, step 12
        (re.compile(r"(\d) and (\d)"), "\\1\u00a0and\u00a0\\2"),              # 60 and 61
        (re.compile(r"([A-Z0-9_]{3,}) = (\d)"), "\\1\u00a0=\u00a0\\2")]       # STAT_MIL_EIN = 0


def glue(text: str) -> str:
    for rx, rep in GLUE:
        text = rx.sub(rep, text)
    return text


def runs_of(content):
    if isinstance(content, str):
        return [("", glue(content))]
    return [("", glue(r)) if isinstance(r, str) else (r[0], glue(r[1])) for r in content]


IDENT_RE = re.compile(r"^([(\"']*)([A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+|[A-Z0-9_]+\.(?:PRG|prg)|IDENT|nicht_aktiv|aktiv|obd\.ini)((?:\u00a0=\u00a0\d+)?[)\"'.,;:…]*)$")
AUTO_MONO = True
NBSP = " "


class Word:
    """One space-separated word: segments of (extra_cls, text) with no space between them."""

    def __init__(self, base, segs):
        self.segs = [list(sg) for sg in segs if sg[1]]
        self.width = sum(M.width(font_key(base + " " + c), t.replace(NBSP, " ")) for c, t in self.segs)
        self.first, self.last = self.segs[0][0], self.segs[-1][0]


def words_of(base: str, content):
    """Words of a run list. Job, status and coding names (and .PRG files) are set in t-mono, as the manual sets
    them in code; brackets and punctuation around them stay in the surrounding font."""
    out = []
    for extra, text in runs_of(content):
        for w in text.split(" "):
            if w == "":
                continue
            m = IDENT_RE.match(w) if AUTO_MONO and "t-mono" not in (base + " " + extra) else None
            if m:
                mono = (extra + " t-mono").strip()
                out.append(Word(base, [(extra, m.group(1)), (mono, m.group(2)), (extra, m.group(3))]))
            else:
                out.append(Word(base, [(extra, w)]))
    return out


def _gap(base, a, b):
    """The space between two words: in their font when they meet in the same class, else in the base font."""
    return M.space(font_key(base + " " + a.last)) if a.last == b.first else M.space(font_key(base))


def wrap(base: str, content, maxw: float):
    """Greedy wrap. Returns a list of lines; each line is a list of (extra_cls, text) runs, and its width."""
    words = words_of(base, content)
    lines, cur, curw = [], [], 0.0
    for wd in words:
        add = wd.width if not cur else _gap(base, cur[-1], wd) + wd.width
        if cur and curw + add > maxw:
            lines.append((cur, curw))
            cur, curw = [], 0.0
            add = wd.width
        cur.append(wd)
        curw += add
    if cur:
        lines.append((cur, curw))
    return [(_merge(ws), lw) for ws, lw in lines]


def _merge(ws):
    """Join words into runs; a space between two classes sits outside both, in the base font."""
    runs = []

    def put(cls, text):
        if runs and runs[-1][0] == cls:
            runs[-1][1] += text
        else:
            runs.append([cls, text])

    for i, w in enumerate(ws):
        if i:
            put(w.first if ws[i - 1].last == w.first else "", " ")
        for cls, text in w.segs:
            put(cls, text)
    return [(e, t) for e, t in runs]


def text_el(base: str, x, y, runs, anchor=None) -> str:
    a = f' text-anchor="{anchor}"' if anchor else ""
    if isinstance(runs, str):
        runs = [("", runs)]
    inner = ""
    for extra, t in runs:
        t = escape(t.replace(" ", " "))
        inner += f'<tspan class="{extra}">{t}</tspan>' if extra else t
    return f'<text class="{base}" x="{fmt(x)}" y="{fmt(y)}"{a}>{inner}</text>'


def line_width(base: str, content) -> float:
    ws = words_of(base, content)
    return sum(w.width for w in ws) + sum(_gap(base, a, b) for a, b in zip(ws, ws[1:]))


class Block:
    """A paragraph inside a box: base class, content, wrap width, alignment."""

    def __init__(self, base, content, gap_before=0.0, anchor="start", lh=None):
        self.base, self.content, self.gap_before, self.anchor = base, content, gap_before, anchor
        self.lh = lh or LINE_H[font_key(base).split()[0]]


def layout_blocks(blocks, x, y_top, w, pad_x=10, pad_top=None, pad_bottom=7.0):
    """Lay out blocks in a column [x+pad_x, x+w-pad_x]. Returns (svg, total_height, line_widths)."""
    inner_w = w - 2 * pad_x
    svg, y, widths = [], y_top, []
    first = True
    for b in blocks:
        fs = size_of(b.base)
        lines = wrap(b.base, b.content, inner_w)
        for i, (runs, lw) in enumerate(lines):
            if first:
                y += (pad_top if pad_top is not None else 4.5) + fs * 0.78
                first = False
            elif i == 0:
                y += b.gap_before + b.lh
            else:
                y += b.lh
            if b.anchor == "middle":
                svg.append(text_el(b.base, x + w / 2, y, runs, "middle"))
            elif b.anchor == "end":
                svg.append(text_el(b.base, x + w - pad_x, y, runs, "end"))
            else:
                svg.append(text_el(b.base, x + pad_x, y, runs))
            widths.append(lw)
            last_fs = fs
    h = (y - y_top) + last_fs * 0.22 + pad_bottom
    return "\n".join(svg), h, widths


def box(x, y, w, blocks, cls="shape", rx=4, pad_x=10, pad_top=None, pad_bottom=7.0, min_h=0, sw=1.5,
        valign="top"):
    """A rect with wrapped text. Returns (svg, height)."""
    tsvg, th, _ = layout_blocks(blocks, x, y, w, pad_x, pad_top, pad_bottom)
    h = max(th, min_h)
    if valign == "middle" and h > th:
        tsvg, _, _ = layout_blocks(blocks, x, y + (h - th) / 2, w, pad_x, pad_top, pad_bottom)
    stroke = f' stroke-width="{fmt(sw)}"' if sw is not None else ""
    r = f'<rect class="{cls}" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" rx="{fmt(rx)}"{stroke}/>'
    return r + "\n" + tsvg, h


def measure_box(w, blocks, pad_x=10, pad_top=None, pad_bottom=7.0):
    _, h, widths = layout_blocks(blocks, 0, 0, w, pad_x, pad_top, pad_bottom)
    return h, (max(widths) if widths else 0)


def arrow(d: str, cls="ln") -> str:
    return f'<path class="{cls}" d="{d}" marker-end="url(#ah)"/>'


def line(d: str, cls="ln") -> str:
    return f'<path class="{cls}" d="{d}"/>'


def dot(x, y, r=2.6) -> str:
    return f'<circle class="fill-fg" cx="{fmt(x)}" cy="{fmt(y)}" r="{fmt(r)}"/>'


def svg_doc(width: int, height: int, aria: str, body: str) -> str:
    aria_esc = escape(aria, {'"': "&quot;"})
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" '
            f'aria-label="{aria_esc}" color="#1b2128">\n{STYLE}\n<defs>\n{AH}\n</defs>\n'
            f'<rect class="bg" x="0" y="0" width="{width}" height="{height}" fill="#ffffff"/>\n{body}\n</svg>\n')


KEY_ITEMS = {
    "question": ("shape", 6, "Question"),
    "action": ("shape", 1.5, "Check or action"),
    "go": ("new", 1.5, "Pass: go on"),
    "stop": ("crit-s", 1.5, "Stop: fix before going on"),
    "caution": ("warn-f", 1.5, "Caution"),
    "note": ("panel", 1.5, "Note"),
}


def key_row(x, y, items, labels=None, gap=22):
    """A legend row like figures 06 and 12: 18x12 swatches with t-sm labels. Returns (svg, right_x)."""
    out = []
    labels = labels or {}
    for it in items:
        cls, rx, label = KEY_ITEMS[it]
        label = labels.get(it, label)
        out.append(f'<rect class="{cls}" x="{fmt(x)}" y="{fmt(y)}" width="20" height="12" rx="{fmt(rx)}" stroke-width="1.2"/>')
        out.append(text_el("t-sm", x + 26, y + 10.5, label))
        x += 26 + line_width("t-sm", label) + gap
    return "\n".join(out), x - gap


def write(name: str, svg: str, outdir: pathlib.Path) -> pathlib.Path:
    p = outdir / name
    p.write_text(svg, encoding="utf-8")
    return p
