"""Helpers for dm-floor's generators, on top of kit.py (house <style> block, Doc, text widths
measured in Chromium with the site's fonts). Portrait figures use svg_open(400, H, ...)."""
import math
import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import kit  # noqa: E402
from kit import Doc, fmt, width, svg_open, write, flush_measurements  # noqa: E402,F401

LH = {"t": 16, "t-sm": 14, "t-xs": 12.5}  # line pitch per size class


def size_of(cls: str) -> str:
    c = cls.split()
    if "t-xs" in c:
        return "t-xs"
    if "t-sm" in c:
        return "t-sm"
    return "t"


def run_width(runs):
    """Width of a rich line given as [(cls, text), ...] (each run measured on its own)."""
    return sum(width(c, s) for c, s in runs)


class Fig(Doc):
    """Doc with label blocks and leaders."""

    def label(self, x, y, lines, anchor="start", leader=None, lead_from=None, gap=3, pitch=None):
        """lines: list of (cls, text) or (cls, [(extra_cls, text), ...]) for a rich line.
        x, y: anchor of the first baseline. leader: (tx, ty) target; drawn from the block's
        nearest side (or lead_from=(lx, ly)). Returns the block's bbox (x0, y0, x1, y1)."""
        x0 = x1 = None
        yy = y
        boxes = []
        for i, (cls, txt) in enumerate(lines):
            if isinstance(txt, list):
                w = sum(width(f"{cls} {c}".strip() if c else cls, s) for c, s in txt)
                runs = [(c, s) for c, s in txt]
                self.rich(cls, x, yy, runs, anchor)
            else:
                w = width(cls, txt)
                self.text(cls, x, yy, txt, anchor)
            if anchor == "end":
                bx0, bx1 = x - w, x
            elif anchor == "middle":
                bx0, bx1 = x - w / 2, x + w / 2
            else:
                bx0, bx1 = x, x + w
            fs = {"t": 13, "t-sm": 11.5, "t-xs": 10.5}[size_of(cls)]
            boxes.append((bx0, yy - 0.72 * fs, bx1, yy + 0.2 * fs))
            x0 = bx0 if x0 is None else min(x0, bx0)
            x1 = bx1 if x1 is None else max(x1, bx1)
            yy += pitch or LH[size_of(cls)]
        bb = (x0, boxes[0][1], x1, boxes[-1][3])
        if leader:
            tx, ty = leader
            if lead_from:
                lx, ly = lead_from
            else:
                # start beside the line of the block whose middle is nearest the target's y
                ly_mid = [((b[1] + b[3]) / 2, b) for b in boxes]
                ly, b = min(ly_mid, key=lambda p: abs(p[0] - ty))
                lx = (b[2] + gap) if tx > b[2] else (b[0] - gap)
            self.line("ln-thin", lx, ly, tx, ty)
        return bb

    def hatch(self, cls, x0, y0, x1, y1, step=5, sw=1, slope=1):
        """45-degree hatch lines clipped to a rectangle: points (x0 + k + s, y1 - s) for
        slope=1 (rising to the right) or (x0 + k + s, y0 + s) for slope=-1."""
        w, h = x1 - x0, y1 - y0
        segs = []
        k = -h + step / 2
        while k < w:
            s0, s1 = max(0, -k), min(h, w - k)
            if s1 - s0 > 0.5:
                ax, bx = x0 + k + s0, x0 + k + s1
                ay, by = ((y1 - s0), (y1 - s1)) if slope == 1 else ((y0 + s0), (y0 + s1))
                segs.append(f"M{fmt(round(ax, 1))},{fmt(round(ay, 1))} L{fmt(round(bx, 1))},{fmt(round(by, 1))}")
            k += step
        if segs:
            self.path(cls, " ".join(segs), sw=sw)

    def capsule(self, cls, x0, y0, x1, y1, sw=None, extra=""):
        r = min(x1 - x0, y1 - y0) / 2
        self.rect(cls, x0, y0, x1 - x0, y1 - y0, rx=r, sw=sw, extra=extra)


_NUM = r"-?\d+(?:\.\d+)?"


def _shift_path(d: str, dx: float, dy: float) -> str:
    """Shift a path's absolute commands (M L H V C Q S T A); relative ones are left alone."""
    import re
    out = []
    for cmd, args in re.findall(r"([MLHVCQSTAZmlhvcqstaz])([^MLHVCQSTAZmlhvcqstaz]*)", d):
        nums = [float(n) for n in re.findall(_NUM, args)]
        if cmd in "ML CQST".replace(" ", ""):
            nums = [n + (dx if i % 2 == 0 else dy) for i, n in enumerate(nums)]
        elif cmd == "H":
            nums = [n + dx for n in nums]
        elif cmd == "V":
            nums = [n + dy for n in nums]
        elif cmd == "A":
            nums = [n + (dx if i % 7 == 5 else dy if i % 7 == 6 else 0) for i, n in enumerate(nums)]
        out.append(cmd + " ".join(fmt(round(n, 2)) if not float(n).is_integer() else str(int(n)) for n in nums))
    return " ".join(out)


def shift_markup(markup: str, dx: float, dy: float) -> str:
    """Flatten a translate(dx, dy): shift x/y/cx/cy/x1/y1/x2/y2 attributes and path data."""
    import re

    def attr(m):
        name, val = m.group(1), float(m.group(2))
        val += dx if name in ("x", "cx", "x1", "x2") else dy
        return f'{name}="{fmt(round(val, 2)) if not val.is_integer() else int(val)}"'

    markup = re.sub(r'(?<![\w-])(x|y|cx|cy|x1|y1|x2|y2)="(' + _NUM + r')"', attr, markup)
    markup = re.sub(r'(?<![\w-])d="([^"]*)"', lambda m: f'd="{_shift_path(m.group(1), dx, dy)}"', markup)
    return markup


def build(fn):
    """Run a generator function until every string it uses has a measured width."""
    for _ in range(4):
        out = fn()
        if not flush_measurements():
            return out
    return fn()
