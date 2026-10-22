"""Schematic parts shared by the three circuit figures, drawn with house classes only."""
from ckit import Doc, width, fmt

PIN_W, PIN_H = 26, 17


def pin(d: Doc, cx, cy, num, cls="shape", dashed=False, w=PIN_W, h=PIN_H, txt_cls="t t-mono"):
    """A connector cavity: small box centred on (cx, cy) with its number."""
    d.rect(cls + (" dash" if dashed else ""), cx - w / 2, cy - h / 2, w, h, rx=2)
    d.text(txt_cls, cx, cy + 4.5, str(num), anchor="middle")


def ground(d: Doc, x, y, cls="keep-s"):
    """Ground symbol with its top at (x, y)."""
    d.line(cls, x - 10, y, x + 10, y, sw=1.5)
    d.line(cls, x - 6.5, y + 4, x + 6.5, y + 4, sw=1.5)
    d.line(cls, x - 3, y + 8, x + 3, y + 8, sw=1.5)


def splice(d: Doc, x, y, cls="keep-f", r=3.6):
    d.dot(cls, x, y, r)


def box(d: Doc, cls, x, y, w, h, lines, pad=10, first_dy=None, lh=16, rx=5, sw=1.5):
    """A component box with lines = [(text_cls, text), ...] left-aligned."""
    d.rect(cls, x, y, w, h, rx=rx, sw=sw)
    yy = y + (first_dy if first_dy is not None else 18)
    for tc, s in lines:
        if s:
            d.text(tc, x + pad, yy, s)
        yy += lh


def swatch_line(d: Doc, x, y, cls, label, sw=2, dashed=False, length=22):
    c = cls + (" dash" if dashed else "")
    d.line(c, x, y - 4, x + length, y - 4, sw=sw)
    d.text("t-sm", x + length + 6, y, label)
    return x + length + 6 + width("t-sm", label)


def swatch_box(d: Doc, x, y, cls, label):
    d.rect(cls, x, y - 10, 14, 12, rx=2, sw=1)
    d.text("t-sm", x + 22, y, label)
    return x + 22 + width("t-sm", label)
