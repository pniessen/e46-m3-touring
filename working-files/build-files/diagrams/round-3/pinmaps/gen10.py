#!/usr/bin/env python3
"""Redraw diagrams/10-repin-map.svg (portrait, 400 wide): the body-side re-pins on an MS43 and an MS45.1 Touring.
Every row runs from where a wire is now (left) to where it goes (right); orange = a wire you move,
green = a new wire, dashed = optional or only if present, X = a wire that comes out and is insulated.
Move numbers ("#n") match the manual's tables; the MS45.1 rows follow its work order.
Text in backticks is set in t-mono.
"""
import sys

sys.dont_write_bytecode = True
from pmkit import Canvas, marker, write  # noqa: E402

W = 400
LH_X, RH_X, HW = 4, 298, 98           # housings: left and right, width
LC_X, RC_X, CW, CH = 56, 302, 42, 18  # pin cells
AX0, AX1 = LC_X + CW, RC_X - 1        # arrows run from the left cell to just before the right cell
MID = 200
PITCH = 21                            # row pitch inside one housing
GAP = 9                               # extra space where the right-hand housing changes
NOTE = 13                             # one note line under an arrow
under, over = Canvas(), Canvas()      # housings below, everything else on top
QUAL = "t-sm t-b fab-t"               # order and safety qualifiers: bold orange, as on Figures 17 and 18


def segs(s):
    out = []
    for i, part in enumerate(s.split("`")):
        if part:
            out.append((part, "t-mono") if i % 2 else part)
    return out


def housing(side, y0, y1, name, sub=None):
    if sub and y1 - y0 < 30:            # one row, two-line label: give it room
        y0, y1 = y0 - 3, y1 + 3
    x = LH_X if side == "L" else RH_X
    under.rect(x, y0, HW, y1 - y0, "keep", rx=4, sw=1.5)
    nx = (LH_X + LC_X) / 2 if side == "L" else (RC_X + CW + RH_X + HW) / 2
    cy = (y0 + y1) / 2
    if sub:
        under.text(nx, cy - 2.5, [(name, "t-mono")], "t-xs t-b", "middle")
        under.text(nx, cy + 10.5, sub, "t-xs", "middle")
    else:
        under.text(nx, cy + 3.8, [(name, "t-mono")], "t-xs t-b", "middle")


def cell(side, top, text, small=False):
    x = LC_X if side == "L" else RC_X
    over.rect(x, top, CW, CH, "shape", rx=2)
    cls = "t-xs t-b t-mono" if small else "t t-b t-mono"
    over.text(x + CW / 2, top + (13 if small else 13.5), text, cls, "middle")


def arrow(top, kind="move", dashed=False, back=False):
    y = top + CH / 2
    cls = {"move": "fab-s", "add": "new-s"}[kind] + (" dash" if dashed else "")
    mk = {"move": "ahf", "add": "ahn"}[kind]
    x0, x1 = (AX1, AX0 + 1) if back else (AX0, AX1)
    over.line(x0, y, x1, y, cls, sw=1.5, end=mk)


class Block:
    """Rows under one left housing. Each row may open a new right housing (or have none)."""

    def __init__(self, top, left, left_sub=None):
        self.top, self.y = top, top
        self.left, self.left_sub = left, left_sub
        self.right = None          # [name, sub, y0]
        self._last_bottom = top
        self._content_bottom = top

    def _close_right(self, y_end):
        if self.right:
            name, sub, y0 = self.right
            housing("R", y0 - 4, y_end + 4, name, sub)
            self.right = None

    def row(self, lpin, rpin, label, right=None, kind="move", dashed=False, small=False, notes=(), rsmall=None,
            back=False, extra=0):
        """right: (name, sub) opens a new right housing at this row; '=' stays in the open one; None = no right side.
        notes: lines under the arrow, each a string (gray t-xs) or a list of segments for over.text with its class."""
        if right != "=" and self.y != self.top:
            self.y += (GAP + extra) if (self.right or right) else 0
        if right != "=":
            self._close_right(self._last_bottom)
            if right:
                self.right = [right[0], right[1], self.y]
        top = self.y
        cell("L", top, lpin, small)
        if right:
            cell("R", top, rpin, small if rsmall is None else rsmall)
            arrow(top, kind, dashed, back)
        over.text(MID, top + 2, segs(label), "t-sm", "middle")
        for i, n in enumerate(notes):
            content, cls = (segs(n), "t-xs") if isinstance(n, str) else n
            over.text(MID, top + CH / 2 + 15 + NOTE * i, content, cls, "middle")
        self._last_bottom = top + CH
        self._content_bottom = top + CH / 2 + 15 + NOTE * (len(notes) - 1) + 3 if notes else top + CH
        self.y = top + PITCH + NOTE * len(notes)
        return top

    def xrow(self, lpin, code):
        top = self.y
        if self.right:
            self._close_right(self._last_bottom)
            top = self.y = top + GAP
        cell("L", top, lpin)
        y = top + CH / 2
        over.line(AX0, y, 116, y, "fab-s", sw=1.5)
        over.path(f"M117,{y - 4} l8,8 M117,{y + 4} l8,-8", "fab-s", sw=2)
        over.text(132, y + 3.7, segs(code), "t-xs")
        self._last_bottom = self._content_bottom = top + CH
        self.y = top + PITCH
        return top

    def close(self):
        self._close_right(self._last_bottom)
        housing("L", self.top - 4, self._last_bottom + 4, self.left, self.left_sub)
        return max(self._last_bottom + 4, self._content_bottom + 2)


def qual(s):
    return (segs(s), QUAL)


def text(x, y, s, cls, anchor=None):
    over.text(x, y, segs(s), cls, anchor)


RULE = "Each wire crossing `X6011` ↔ `X60004` gets a new terminal of the target's type."

# ================================================================ MS43
over.comment("MS43 Touring: lamp wires, start feedback and leak-test heater move from X6011 into X60004")
over.text(6, 18, "MS43 TOURING (09/2001 TO 02/2003)", "t-h")
text(6, 33, "M3 donor built from 09/2001; earlier cars: see “Earlier MS43 Tourings”.", "t-xs")
b = Block(46, "X6011", "body side")
b.row("7", "18", "#1 Leak-test heater, `0.75 SW/RT`", right=("X60004", "DME"))
b.row("3", "11", "#3 Oil-pressure lamp, `0.35 BR/GN`", right="=")
b.row("4", "1", "#4 Charge lamp, `0.35 BL`", right="=")
b.row("5", "21", "#5 Oil level, `0.5 WS/GN`", right="=")
b.row("6", "2", "#6 Start feedback, `0.35 SW/GN`", right="=")
y = b.close()

over.comment("MS43: clutch into X6011 pin 7 once the heater is out; brake test contact 28 to 34; new ground")
b = Block(y + 12, "X60004", "DME")
b.row("23", "7", "#2 Clutch, `0.35 BL/BR`", right=("X6011", "body side"),
      notes=(qual("after the heater wire is out of pin `7`"),))
b.row("28", "34", "#7 Brake test contact, `0.35 BR/GR`", right=("X60004", None))
b.row("5", "X1108", "#8 New ground, recommended", right=("ground", None), kind="add", rsmall=True,
      notes=("`0.35 BR/SW` to ground point `X1108`",))
y = b.close()

over.comment("MS43: Sport button and LED (optional); the LED wire runs from X60004 16 to X1869 18")
b = Block(y + 10, "X1869", "optional")
b.row("17", "15", "#9 Sport button, `0.35 SW/RT/GE`", right=("X60004", None), kind="add", dashed=True)
b.row("18", "16", "#9 Sport LED, `0.35 SW/GR/GE`", right="=", kind="add", dashed=True, back=True)
y = b.close()
text(6, y + 15, RULE, "t-xs")
y += 21
over.line(4, y + 6, 396, y + 6, "ln-faint")

# ================================================================ MS45.1, in the manual's work order
over.comment("MS45.1 Touring, in the manual's work order: tag, wires out, then the moves and new wires")
y += 27
over.text(6, y, "MS45.1 TOURING (M54, FROM 03/2003)", "t-h")
text(6, y + 15, "Manual gearbox; M3 donor built from 09/2001.", "t-xs")
text(6, y + 30, "Tag `2` and `15` first: both are SW/RT (0.75 mm² in `2`, 0.5 mm² in `15`).", "t-xs t-b crit-t")
b = Block(y + 43, "X60004", "DME")
t5 = b.xrow("5", "#2: `0.5 SW/GE`")
b.xrow("15", "#3: `0.5 SW/RT`")
t19 = b.xrow("19", "#4: `0.5 BR/OR`")
over.path(f"M206,{t5 + 1} H210 V{t19 + 17} H206", "ln-thin")
text(218, t5 + 12, "Out first; insulate.", "t-xs")
text(218, t5 + 26, "#2, #3: secondary-air sensor", "t-xs")
text(218, t5 + 40, "#4: E-box fan, if fitted", "t-xs")
b.row("2", "18", "#1 Leak-test heater, `0.75 SW/RT`", right=("X60004", None))
b.row("28", "34", "#5 Brake test contact, `0.35 BR/GR`", right="=")
b.row("23", "7", "#6 Clutch, `0.35 BL/BR`", right=("X6011", "body side"), extra=3)
b.row("11", "13", "#7 Oil-pressure lamp, `0.35 BR/GN`", right=("X11175", "cluster"), kind="add", extra=3)
b.row("1", "2", "#8 Charge lamp, `0.35 BL`", right="=", kind="add")
b.row("21", "17", "#9 Oil level, `0.5 WS/GN`", right="=", kind="add")
y = b.close()

over.comment("MS45.1: start feedback only if body X6011 pin 6 holds a wire, once 2 is clear")
b = Block(y + 13, "X6011", "body side")
b.row("6", "2", "#10 Start feedback, `0.35 SW/GN`", right=("X60004", None), dashed=True,
      notes=(qual("only if body `X6011` pin `6` has a wire,"), qual("once `2` is clear")))
y = b.close()
b = Block(y + 10, "X60004", None)
b.row("5", "X1108", "#11 New ground, recommended", right=("ground", None), kind="add", rsmall=True,
      notes=(([("once ", "t-b fab-t"), ("5", "t-b fab-t t-mono"), (" is clear", "t-b fab-t"), ": "]
              + segs("`0.35 BR/SW` to `X1108`"), "t-xs"),))
y = b.close()
b = Block(y + 10, "X1869", "optional")
b.row("17", "15", "#12 Sport button, `0.35 SW/RT/GE`", right=("X60004", None), kind="add", dashed=True,
      notes=(qual("once `15` is clear"),))
b.row("18", "16", "#12 Sport LED, `0.35 SW/GR/GE`", right="=", kind="add", dashed=True, back=True)
y = b.close()
text(6, y + 15, RULE, "t-xs")
y += 21

over.comment("Both cars")
over.line(4, y + 6, 396, y + 6, "ln-faint")
text(6, y + 23, "Both cars: M3 clutch module `61319122700` replaces `61319231129` (#10, #13).", "t-xs")
text(6, y + 36, "Code the cluster's `CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN` and", "t-xs")
text(6, y + 49, "`TOG_UEBER_CAN` to `nicht_aktiv`.", "t-xs")
text(6, y + 63, "X60004 pin `6` stays empty: a forum mapping put the start feedback there.", "t-xs t-b crit-t")
text(6, y + 77, "Pins `20` and `30` (leak-test pump) stay: test before your Touring's DME comes out.", "t-xs")
text(6, y + 90, "Fuel pump: `K96` stays on `X60004` pin `10`; prove it with `STEUERN_EKP`.", "t-xs")
H = int(y + 98)

ARIA = ("Re-pin map for the body-side plugs, drawn from where each wire is now to where it goes and numbered as in the "
        "manual's tables: orange for a wire you move, green for a new wire, dashed for an optional wire or one that may not "
        "be there, and an X for a wire that comes out and is insulated. MS43 Touring built 09/2001 to 02/2003, with an M3 "
        "donor built from 09/2001: the leak-test heater moves from body X6011 pin 7 to X60004 pin 18 (#1), and only then "
        "the clutch wire from X60004 pin 23 into X6011 pin 7 (#2); the oil-pressure lamp moves from 3 to 11, the charge "
        "lamp from 4 to 1, the oil level from 5 to 21 and the start feedback from 6 to 2 (#3 to #6); the brake test contact "
        "moves from 28 to 34 (#7); a new ground runs from X60004 pin 5 to ground point X1108 (#8, recommended); and the "
        "optional Sport button runs from switch-center pin 17 to X60004 pin 15, its LED from X60004 pin 16 to pin 18 (#9). "
        "MS45.1 Touring with the M54, from 03/2003, with an M3 donor built from 09/2001, in work order: tag pins 2 and 15 "
        "first, because both are black with red; take out and insulate the wires in 5 and 15 and, if fitted, 19 (#2 to #4); "
        "then the heater moves from 2 to 18 (#1), the brake test contact from 28 to 34 (#5) and the clutch wire from 23 "
        "into X6011 pin 7 (#6); new wires run from 11, 1 and 21 to cluster pins 13, 2 and 17 (#7 to #9); the start "
        "feedback moves from X6011 pin 6 to X60004 pin 2 only if pin 6 has a wire, once 2 is clear (#10); a new ground goes "
        "into 5 once it is clear (#11, recommended); and the optional Sport wires go into 15 and 16 once 15 is clear (#12). "
        "On both cars every wire that crosses between X6011 and X60004 gets a new terminal of the target's type, the M3 "
        "clutch module replaces the Touring's, the cluster's three lamp switches are coded to nicht_aktiv, X60004 pin 6 "
        "stays empty, pins 20 and 30 stay until tested, and the fuel-pump relay K96 stays on pin 10.")
c = Canvas()
c.parts = under.parts + over.parts
svg = c.svg(W, H, ARIA, [marker("ahf", "fab-f"), marker("ahn", "new-f")])
print(write("10-repin-map.svg", svg), H)
