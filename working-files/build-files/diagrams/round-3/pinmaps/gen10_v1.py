#!/usr/bin/env python3
"""Redraw diagrams/10-repin-map.svg (portrait, 400 wide): the body-side re-pins on an MS43 and an MS45.1 Touring.
Every row runs from where a wire is now (left) to where it goes (right); orange = a wire you move,
green = a new wire, dashed = optional or only if present. Applies wiring-canonical.md section 10,
"Figure 10", items 1-15. Text in backticks is set in t-mono.
"""
import sys

sys.dont_write_bytecode = True
from pmkit import Canvas, marker, write  # noqa: E402

W = 400
LH_X, RH_X, HW = 4, 298, 98           # housings: left and right, width
LC_X, RC_X, CW, CH = 52, 302, 46, 18  # pin cells
AX0, AX1 = LC_X + CW, RC_X - 1        # arrows run from the left cell to just before the right cell
MID = 200
PITCH = 22                            # row pitch inside one housing
GAP = 8                               # extra space where the right-hand housing changes
NOTE = 13                             # one t-xs note line under an arrow
under, over = Canvas(), Canvas()      # housings below, everything else on top


def segs(s):
    out = []
    for i, part in enumerate(s.split("`")):
        if part:
            out.append((part, "t-mono") if i % 2 else part)
    return out


def housing(side, y0, y1, name, sub=None):
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


def arrow(top, kind="move", dashed=False):
    y = top + CH / 2
    cls = {"move": "fab-s", "add": "new-s"}[kind] + (" dash" if dashed else "")
    mk = {"move": "ahf", "add": "ahn"}[kind]
    over.line(AX0, y, AX1, y, cls, sw=1.5, end=mk)


def text(x, y, s, cls, anchor=None):
    over.text(x, y, segs(s), cls, anchor)


class Block:
    """Rows under one left housing. Each row may open a new right housing (or none)."""

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
            note_cls="t-xs"):
        """right: (name, sub) to open a new right housing at this row; '=' to stay in the open one; None for no right side."""
        if right != "=" and self.y != self.top:
            self.y += GAP if (self.right or right) else 0
        if right != "=":
            self._close_right(self._last_bottom)
            if right:
                self.right = [right[0], right[1], self.y]
        top = self.y
        cell("L", top, lpin, small)
        if right:
            cell("R", top, rpin, small if rsmall is None else rsmall)
            arrow(top, kind, dashed)
        over.text(MID, top + 2, segs(label), "t-sm", "middle")
        for i, n in enumerate(notes):
            over.text(MID, top + CH / 2 + 15 + NOTE * i, segs(n), note_cls, "middle")
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
        over.text(132, y + 3.7, [(code, "t-mono")], "t-xs")
        self._last_bottom = self._content_bottom = top + CH
        self.y = top + PITCH
        return top

    def close(self):
        self._close_right(self._last_bottom)
        housing("L", self.top - 4, self._last_bottom + 4, self.left, self.left_sub)
        return max(self._last_bottom + 4, self._content_bottom + 2)


# ================================================================ MS43
over.comment("MS43 Touring: lamp wires, start feedback and leak-test heater move from X6011 into X60004")
over.text(6, 18, "MS43 TOURING (TO 02/2003)", "t-h")
b = Block(30, "X6011", "E-box")
b.row("3", "11", "Oil-pressure lamp, `0.35 BR/GN`", right=("X60004", "DME"))
b.row("4", "1", "Charge lamp, `0.35 BL`", right="=")
b.row("5", "21", "Oil level, `0.5 WS/GN`", right="=")
b.row("6", "2", "Start feedback (30h), `0.35 SW/GN`", right="=")
b.row("7", "18", "Leak-test heater, `0.75 SW/RT`", right="=")
y = b.close()
text(6, y + 14, "X60004 pin `6` stays empty: older charts put the start feedback there.", "t-xs crit-t")

over.comment("MS43: clutch into X6011 pin 7 once the heater is out; brake test contact 28 to 34; new ground")
b = Block(y + 30, "X60004")
b.row("23", "7", "Clutch, `0.35 BL/BR`", right=("X6011", None),
      notes=("after the heater wire is out of pin `7`;", "via the gear switch to `X60002` pin `20`"))
b.row("28", "34", "Brake test contact, `0.35 BR/GR`", right=("X60004", None))
b.row("5", "X1108", "New ground, `0.35 BR/SW`", right=("ground", None), kind="add", rsmall=True, notes=("recommended",))
y = b.close()

over.comment("MS43: Sport button (optional)")
b = Block(y + 8, "X1869")
b.row("17, 18", "15, 16", "Sport button (optional)", right=("X60004", None), kind="add", dashed=True, small=True,
      notes=("`0.35 SW/RT/GE` and `0.35 SW/GR/GE`",))
y = b.close()

over.line(4, y + 10, 396, y + 10, "ln-faint")

# ================================================================ MS45.1
over.comment("MS45.1 Touring: moves inside X60004, sensor wires out, new ground, clutch to X6011, lamp wires to the cluster")
y += 30
over.text(6, y, "MS45.1 TOURING (FROM 03/2003)", "t-h")
b = Block(y + 12, "X60004", "DME")
b.row("28", "34", "Brake test contact, `0.35 BR/GR`", right=("X60004", None))
b.row("2", "18", "Leak-test heater, `0.75 SW/RT`", right="=")
t5 = b.xrow("5", "0.5 SW/GE")
b.xrow("15", "0.5 SW/RT")
t19 = b.xrow("19", "0.5 BR/OR")
over.path(f"M200,{t5 + 1} H204 V{t19 + 15} H200", "ln-thin")
text(212, t5 + 6, "Out first; insulate.", "t-xs")
text(212, t5 + 19, "`5`, `15`: secondary-air sensor", "t-xs")
text(212, t5 + 32, "`19`: E-box fan, if fitted", "t-xs")
text(212, t5 + 47, "Tag `2` and `15` first:", "t-xs t-b crit-t")
text(212, t5 + 59, "both are SW/RT", "t-xs t-b crit-t")
b.row("5", "X1108", "New ground, `0.35 BR/SW`", right=("ground", None), kind="add", rsmall=True,
      notes=("once `5` is clear; recommended",))
b.row("23", "7", "Clutch, `0.35 BL/BR`: new terminal", right=("X6011", None))
b.row("11", "13", "Oil-pressure lamp, `0.35 BR/GN`", right=("X11175", "cluster"), kind="add")
b.row("1", "2", "Charge lamp, `0.35 BL`", right="=", kind="add")
b.row("21", "17", "Oil level, `0.5 WS/GN`", right="=", kind="add")
y = b.close()
text(6, y + 14, "Code `CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN` and `TOG_UEBER_CAN`", "t-xs")
text(6, y + 27, "to `nicht_aktiv`: then the lamps work with any MSS54 software.", "t-xs")

over.comment("MS45.1: start feedback only if your X6011 pin 6 holds a wire; Sport once 15 is clear")
b = Block(y + 44, "X6011")
b.row("6", "2", "Start feedback, `0.35 SW/GN`", right=("X60004", None), dashed=True,
      notes=("only if your `X6011` pin `6` holds a wire",))
y = b.close()
b = Block(y + 8, "X1869")
b.row("17, 18", "15, 16", "Sport (optional), once `15` is clear", right=("X60004", None), kind="add", dashed=True,
      small=True, notes=("`0.35 SW/RT/GE` and `0.35 SW/GR/GE`",))
y = b.close()

over.comment("Both cars")
over.line(4, y + 10, 396, y + 10, "ln-faint")
text(6, y + 25, "Both cars: fit the M3 clutch module `61319122700` in place of `61319231129`.", "t-xs")
text(6, y + 38, "Pins `20` and `30` (leak-test pump) don't move on the drawings: test first.", "t-xs")
text(6, y + 51, "Fuel pump: `K96` stays on `X60004` pin `10` on both; prove it with `STEUERN_EKP`.", "t-xs")
H = int(y + 59)

ARIA = ("Re-pin map for the body-side plugs, drawn from where each wire is now to where it goes, with new wires in green. "
        "On an MS43 Touring the oil-pressure lamp moves from E-box plug X6011 pin 3 to X60004 pin 11, the charge lamp from "
        "4 to 1, the oil level from 5 to 21, the start feedback from 6 to 2 and the leak-test heater from 7 to 18, and "
        "X60004 pin 6 stays empty. Once the heater wire is out, the clutch wire moves from X60004 pin 23 into X6011 pin 7, "
        "the brake test contact moves from 28 to 34, a new ground runs from X60004 pin 5 to ground point X1108, and the "
        "optional Sport button takes switch-center pins 17 and 18 to X60004 pins 15 and 16. On an MS45.1 Touring the brake "
        "test contact moves from 28 to 34 and the heater from 2 to 18; the wires in 5, 15 and 19 come out first and are "
        "insulated, with 2 and 15 tagged first because both are black with red; a new ground goes into 5; the clutch wire "
        "moves from 23 into X6011 pin 7 with a new terminal; new wires run from X60004 pins 11, 1 and 21 to cluster pins 13, "
        "2 and 17, with the cluster's three lamp switches coded to nicht_aktiv; the start feedback moves from X6011 pin 6 to "
        "X60004 pin 2 only if pin 6 holds a wire; and the optional Sport wires go into 15 and 16 once 15 is clear. Both cars "
        "take the M3 clutch module, leave pins 20 and 30 alone until tested, and keep the fuel-pump relay on pin 10.")
c = Canvas()
c.parts = under.parts + over.parts
svg = c.svg(W, H, ARIA, [marker("ahf", "fab-f"), marker("ahn", "new-f")])
print(write("10-repin-map.svg", svg), H)
