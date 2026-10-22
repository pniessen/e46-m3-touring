#!/usr/bin/env python3
"""Generate diagrams/10-repin-map.svg (body-side re-pins, MS43 and MS45 Tourings).
Every row runs from where a wire is now (left) to where it goes (right)."""
import sys
sys.dont_write_bytecode = True
from svgkit import svg_open, marker, t, write

LH_X, RH_X, HW = 8, 298, 94          # housings: left and right, width
LC_X, RC_X, CW, CH = 56, 302, 42, 20  # pin cells
AX0, AX1 = LC_X + CW, RC_X - 1        # arrow from left cell edge to just before right cell
MID = 200
out = []
add = out.append


def housing(side, y0, y1, name, sub=None):
    x = LH_X if side == "L" else RH_X
    add(f'<rect class="keep" x="{x}" y="{y0}" width="{HW}" height="{y1 - y0}" rx="4" stroke-width="1.5"/>')
    nx = (LH_X + LC_X) / 2 if side == "L" else (RC_X + CW + RH_X + HW) / 2
    cy = (y0 + y1) / 2
    if sub:
        add(t("t-xs t-b", nx, cy - 2.5, name, "middle"))
        add(t("t-xs", nx, cy + 10.5, sub, "middle"))
    else:
        add(t("t-xs t-b", nx, cy + 3.8, name, "middle"))


def cell(side, top, label, small=False):
    x = LC_X if side == "L" else RC_X
    add(f'<rect class="shape" x="{x}" y="{top}" width="{CW}" height="{CH}" rx="2"/>')
    cls = "t-sm t-b" if small else "t t-b"
    add(t(cls, x + CW / 2, top + (14 if small else 14.5), label, "middle"))


def arrow(top, kind="move", dashed=False):
    y = top + CH // 2
    cls = {"move": "fab-s", "add": "new-s"}[kind]
    mk = {"move": "ahf", "add": "ahn"}[kind]
    d = " dash" if dashed else ""
    add(f'<line class="{cls}{d}" x1="{AX0}" y1="{y}" x2="{AX1}" y2="{y}" stroke-width="1.5" marker-end="url(#{mk})"/>')


def label(top, s, cls="t-sm"):
    add(t(cls, MID, top + 3, s, "middle"))


def note(top, s, line=0):
    add(t("t-xs", MID, top + CH // 2 + 15 + 13 * line, s, "middle"))


def row(top, lpin, rpin, text, kind="move", dashed=False, small=False):
    cell("L", top, lpin, small)
    cell("R", top, rpin, small)
    arrow(top, kind, dashed)
    label(top, text)


# ---------------------------------------------------------------- MS43
add("\n<!-- MS43 Touring: lamp wires and DM-TL heater move from X6011 into X60004 -->")
add(t("t-h", 8, 18, "MS43 TOURING (TO 02/2003)"))
g1 = [(34, "3", "11", "Oil-pressure lamp, BR/GN", False),
      (60, "4", "1", "Charge lamp", False),
      (86, "5", "21", "Oil level", False),
      (112, "6", "6", "Start signal to the cluster (optional)", True),
      (138, "7", "18", "DM-TL heater, BK/RT", False)]
housing("L", 30, 162, "X6011", "E-box")
housing("R", 30, 162, "X60004", "DME")
for top, lp, rp, s, dashed in g1:
    row(top, lp, rp, s, dashed=dashed)

add("\n<!-- MS43: clutch wire out of X60004 into the gear-switch path; brake wire 28 to 34 -->")
housing("L", 168, 240, "X60004")
housing("R", 168, 196, "X6011")
housing("R", 212, 240, "X60004")
row(172, "23", "7?", "Clutch signal, BL/BR")
note(172, "via the gear switch to X60002 pin 20")
row(216, "28", "34", "Brake-light switch, BR/GN")

add("\n<!-- MS43: Sport button (optional) -->")
housing("L", 246, 274, "X1869")
housing("R", 246, 274, "X60004")
row(250, "17, 18", "15, 16", "Sport button (optional)", dashed=True, small=True)

add('\n<line class="ln-faint" x1="8" y1="286" x2="392" y2="286"/>')

# ---------------------------------------------------------------- MS45
add("\n<!-- MS45 Touring: moves inside X60004, leftover wires out, new lamp wires to the cluster -->")
add(t("t-h", 8, 310, "MS45 TOURING (FROM 02/2003)"))
housing("L", 322, 608, "X60004", "DME")
housing("R", 322, 376, "X60004")
row(326, "28", "34", "Brake-light switch, BR/GN")
row(352, "2", "18", "DM-TL heater, BK/RT")

add("\n<!-- MS45: leftover wires come out -->")
for top, pin, colour in [(382, "5", "BK/GE"), (408, "15", "BK/RT"), (434, "19", "BR/OR")]:
    cell("L", top, pin)
    y = top + CH // 2
    add(f'<line class="fab-s" x1="{AX0}" y1="{y}" x2="116" y2="{y}" stroke-width="1.5"/>')
    add(f'<path class="fab-s" d="M117,{y - 4} l8,8 M117,{y + 4} l8,-8" stroke-width="2"/>')
    add(t("t-xs", 132, y + 3.7, colour))
add('<path class="ln-thin" d="M168,385 H172 V451 H168"/>')
add(t("t-sm", 180, 401, "Remove if populated;"))
add(t("t-sm", 180, 415, "insulate and tie back"))
add(t("t-xs crit-t", 180, 431, "Pin 5 is a ground on the MSS54,"))
add(t("t-xs crit-t", 180, 444, "so a wire left there would be grounded"))

add("\n<!-- MS45: clutch wire, then new lamp wires to the M3 cluster -->")
housing("R", 458, 486, "X6011")
row(462, "23", "7?", "Clutch signal, if populated")
note(462, "into the gear-switch path")
housing("R", 500, 608, "X11175", "cluster")
row(504, "11", "13", "Oil-pressure lamp: add a wire", kind="add")
note(504, "then code the cluster not to expect")
note(504, "oil pressure over CAN", 1)
row(558, "1", "2", "Charge lamp: add, or leave on CAN", kind="add", dashed=True)
row(584, "21", "17", "Oil level: add, or leave on CAN", kind="add", dashed=True)

add("\n<!-- MS45: Sport button (optional), once pin 15 is clear -->")
housing("L", 614, 642, "X1869")
housing("R", 614, 642, "X60004")
row(618, "17, 18", "15, 16", "Sport button (optional)", dashed=True, small=True)

add("\n<!-- Notes -->")
add(t("t-xs", 8, 662, "7? Probably X6011 pin 7, the cavity facing the M3 harness's gear-switch"))
add(t("t-xs", 8, 675, "wire. Confirm on the donor."))
add(t("t-xs", 8, 692, "Fuel pump: X60004 pin 10 should reach relay K96. No move on an MS43;"))
add(t("t-xs", 8, 705, "on an MS45, confirm which pin drives K96."))

H = 714
ARIA = ("Re-pin map for the body-side plugs, drawn from where each wire is now to where it goes. "
        "On an MS43 Touring five wires move from the E-box plug X6011 into X60004, the plug at the DME: "
        "oil-pressure lamp from pin 3 to 11, charge lamp from 4 to 1, oil level from 5 to 21, the optional "
        "start signal from 6 to 6, and the DM-TL heater from 7 to 18. The clutch wire leaves X60004 pin 23 for "
        "the gear-switch path, probably X6011 pin 7, and the brake-light wire moves from pin 28 to 34. "
        "On an MS45 Touring the brake-light wire moves from 28 to 34 and the DM-TL heater from 2 to 18, "
        "leftover wires at pins 5, 15 and 19 come out (pin 5 is a ground on the MSS54), the clutch wire leaves "
        "pin 23, and new wires run from X60004 pins 11, 1 and 21 to cluster pins 13, 2 and 17; the last two can "
        "stay on CAN instead. On both, the optional Sport button takes switch-centre pins 17 and 18 to X60004 "
        "pins 15 and 16, and X60004 pin 10 should reach fuel-pump relay K96.")
svg = svg_open(H, ARIA, [marker("ahf", "fab-f"), marker("ahn", "new-f")]) + "\n".join(out) + "\n</svg>"
print(write("10-repin-map.svg", svg))
