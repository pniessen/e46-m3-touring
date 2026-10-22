#!/usr/bin/env python3
"""Figure 7 (README "Fuel system"): 04-fuel-pressure.svg, redrawn for round 4.

Before: the 325i's own pump, clamped pipe set and lines, one-piece filter-regulator at 3.5 bar with a vent.
After (route A, recommended): your tank with the donor's in-tank set, the M3 pipe set (push-on at the pump,
quick-connector to the rear feed), the M3 lines, a new M3 filter on the donor's 5-bar housing and regulator with TP1, the return
sample point for T3, the vacuum hose to the S54's idle-air pipe and the M3 front purge line. Route C (your own
pump) is the fallback. Text: README 0540 Fuel system, 0210 Fuel parts, 0380 Phase 7.
Portrait, 400 wide: root and style from svgkit.py (the house kit), drawing helpers from kit.py.

    python3 gen04.py        (exit 3 = new strings were measured: run it again)
"""
import sys

import svgkit
from kit import Doc, width, flush_measurements, fmt, DIAGRAMS

W, H = 400, 468
NAME = "04-fuel-pressure.svg"

ARIA = (
    "Fuel system before and after the swap. Today your 325i's pump feeds a clamped pipe set and plain lines joined "
    "by hoses and clamps, to a one-piece filter-regulator that holds 3.5 bar and whose hose is a vent, not a vacuum "
    "reference. After the swap, route A, recommended: your tank stays and takes the donor's in-tank set (pump, "
    "baffle, jet pump and left sender). The M3 pipe set 16112283288 is pushed onto the pump and ends in a "
    "quick-connector for the M3 rear feed; the feed path to the M3 filter-regulator, a new filter on the donor's "
    "housing and regulator, and on to the S54 rail is "
    "all quick-connectors, and the return is hose and clamps. The regulator holds 5.0 bar and takes a vacuum hose to "
    "the S54's idle-air pipe; the rail has no test port, so the gauge goes on the regulator housing's threaded test "
    "fitting, TP1, and for the delivery test T3 the return line comes off at the housing into a container. The M3 "
    "front purge line runs from your canister's line to the S54 purge valve. Fallback, route C: keep your own pump "
    "only if it delivers 1.3 L or more in 30 s at 5 bar, and accept an adapter nobody has documented, either from "
    "its pipe set to the M3 rear feed or from your rear feed to the M3 filter; route B fits the donor's whole tank."
)

d = Doc()
DOT = ' stroke-dasharray="0.1 4" stroke-linecap="round"'


def qc(x, y):
    d.rect("fill-fg", x - 3.5, y - 3.5, 7, 7)


def clamp(x, y, half=5):
    d.line("ln", x - 2.5, y - half, x - 2.5, y + half, sw=2)
    d.line("ln", x + 2.5, y - half, x + 2.5, y + half, sw=2)


def pushon(x, y):
    d.circle("shape", x, y, 3.6, sw=1.5)


def arrow(x, y, direction, cls="fill-fg", s=4.5):
    """A small filled arrowhead whose tip is at (x, y)."""
    if direction == "r":
        pts = [(x, y), (x - 2 * s, y - s), (x - 2 * s, y + s)]
    else:
        pts = [(x, y), (x + 2 * s, y - s), (x + 2 * s, y + s)]
    d.path(cls, "M" + " L".join(f"{fmt(px)},{fmt(py)}" for px, py in pts) + " Z")


def gauge(x, y, r=8):
    d.circle("shape", x, y, r, sw=1.4)
    d.line("ln", x, y, x + r * 0.55, y - r * 0.55, sw=1.4)
    d.dot("fill-fg", x, y, 1.6)


def container(x, y, w=16, h=18):
    d.path("ln", f"M{fmt(x)},{fmt(y)} V{fmt(y + h)} H{fmt(x + w)} V{fmt(y)}", sw=1.4)
    for i in (1, 2, 3):
        d.line("ln-thin", x + 1, y + h * i / 4, x + 6, y + h * i / 4)


def tag(x, y, s, anchor="middle"):
    w = width("t-xs t-b t-mono", s) + 10
    x0 = x - w / 2 if anchor == "middle" else (x if anchor == "start" else x - w)
    d.rect("ln", x0, y - 11, w, 15, rx=3, sw=1.2)
    d.text("t-xs t-b t-mono", x0 + w / 2, y, s, anchor="middle")
    return x0, x0 + w


def box(cls, x0, y0, x1, y1, rows, sw=1.5):
    """A part box with centred rows [(class, text, baseline offset from y0)]."""
    d.rect(cls, x0, y0, x1 - x0, y1 - y0, rx=5, sw=sw)
    for c, s, dy in rows:
        d.text(c, (x0 + x1) / 2, y0 + dy, s, anchor="middle")


# columns: tank, filter-regulator, engine
TA0, TA1 = 8, 92
FR0, FR1 = 170, 258
EN0, EN1 = 316, 392

# ---------------------------------------------------------------- key
d.comment("Key")
x = 8
for cls, lab in (("donor", "From donor M3"), ("keep", "Keep yours"), ("new", "Buy new")):
    d.rect(cls, x, 6, 12, 12, rx=5, sw=1)
    d.text("t-sm", x + 17, 16.5, lab)
    x += 17 + width("t-sm", lab) + 18
x = 8
qc(x + 4, 31)
d.text("t-sm", x + 14, 35, "Quick-connector")
x += 14 + width("t-sm", "Quick-connector") + 16
d.line("keep-s", x - 3, 31, x + 13, 31, sw=1.6)
clamp(x + 5, 31)
d.text("t-sm", x + 19, 35, "Hose and clamp")
x += 19 + width("t-sm", "Hose and clamp") + 16
pushon(x + 4, 31)
d.text("t-sm", x + 13, 35, "Push-on")

# ---------------------------------------------------------------- before
d.comment("325i today (M54)")
d.text("t-h", 8, 64, "325i TODAY (M54)")
YF, YR = 100, 128
box("keep", TA0, 88, TA1, 140, [("t t-b", "Tank +", 23), ("t", "your pump", 40)])
box("keep", FR0, 88, FR1, 140, [("t t-b", "Filter-", 19), ("t t-b", "regulator", 34), ("t-xs", "one piece", 47)])
box("keep", EN0, 88, EN1, 140, [("t", "M54", 30), ("t", "fuel rail", 46)])
# feed: pipe set (clamped both ends) and rear feed
d.line("ln", TA1, YF, FR0 - 8, YF)
arrow(FR0, YF, "r")
for cx in (98, 130, 156):
    clamp(cx, YF)
d.text("t-xs", 114, YF - 10, "pipe set", anchor="middle")
d.text("t-xs", 146, YF + 16, "rear feed", anchor="middle")
# return
d.line("ln", FR0, YR, TA1 + 8, YR)
arrow(TA1, YR, "l")
for cx in (106, 162):
    clamp(cx, YR)
d.text("t-xs", 134, YR + 16, "return", anchor="middle")
# front feed
d.line("ln", FR1, YF, EN0 - 8, YF)
arrow(EN0, YF, "r")
for cx in (266, 300):
    clamp(cx, YF)
d.text("t-xs", 283, YF - 10, "front feed", anchor="middle")
# vent
d.line("ln-thin", 214, 88, 214, 72)
d.text("t-xs", 220, 76, "vent, not a vacuum reference")
d.text("t t-b t-mono", 214, 158, "3.5 bar", anchor="middle")
d.text("t-xs", 8, 158, "Pipe set 16117175998: clamped")
d.text("t-xs", 316, 158, "test fitting,")
d.text("t-xs", 316, 170, "if yours has one")

d.line("ln-faint", 8, 184, 392, 184)

# ---------------------------------------------------------------- after
d.comment("After the swap: route A")
d.text("t-h", 8, 208, "AFTER: ROUTE A (RECOMMENDED)")
YF, YR = 246, 278
# tank with the donor's in-tank set
d.rect("keep", TA0, 232, TA1 - TA0, 104, rx=5, sw=1.5)
d.text("t t-b", 50, 251, "Your tank", anchor="middle")
box("donor", 14, 260, 86, 330, [("t-xs t-b", "Donor's", 14), ("t-xs t-b", "in-tank set:", 26.5),
                                 ("t-xs", "pump, baffle,", 39), ("t-xs", "jet pump,", 51.5), ("t-xs", "left sender", 64)],
    sw=1.2)
# filter-regulator: the donor's housing and 5-bar regulator, with a new filter at the inlet end; the engine (donor)
box("donor", FR0, 232, FR1, 308, [("t-sm t-b", "housing +", 39), ("t-sm t-b", "regulator", 53),
                                   ("t-sm t-b t-mono donor-t", "5.0 bar", 68)], sw=1.5)
FI0 = FR0 - 4                                                   # the filter capsule sticks out at the inlet end
d.rect("new", FI0, 238, 60, 16, rx=8, sw=1.5)
d.text("t-xs new-t", FI0 + 30, 249.5, "new filter", anchor="middle")
box("donor", EN0, 232, EN1, 270, [("t t-b", "S54 rail", 17), ("t-xs", "no test port", 31)])
box("donor", EN0, 282, EN1, 318, [("t", "S54 idle-", 15), ("t", "air pipe", 30)])
box("donor", EN0, 336, EN1, 372, [("t", "S54 purge", 15), ("t", "valve", 30)])
# feed: push-on at the pump, pipe set, quick-connector, M3 rear feed, quick-connector at the filter
d.line("donor-s", TA1, YF, FI0 - 8, YF, sw=3)
arrow(FI0, YF, "r", "donor-f")
pushon(TA1 + 4, YF)
qc(130, YF)
qc(FR0 - 16, YF)
d.text("t-xs", 112, YF - 10, "pipe set", anchor="middle")
d.text("t-xs", 144, YF + 16, "rear feed", anchor="middle")
# front feed
d.line("donor-s", FR1, YF, EN0 - 8, YF, sw=3)
arrow(EN0, YF, "r", "donor-f")
qc(FR1 + 6, YF)
qc(EN0 - 16, YF)
d.text("t-xs", 283, YF - 10, "front feed", anchor="middle")
# return: hose and clamps
d.line("donor-s", FR0, YR, TA1 + 8, YR, sw=1.6)
arrow(TA1, YR, "l", "donor-f")
for cx in (106, 162):
    clamp(cx, YR)
d.text("t-xs", 118, YR + 16, "return", anchor="middle")
# vacuum hose to the idle-air pipe
d.line("donor-s dash", FR1, 290, EN0 - 1, 290, sw=1.8)
d.text("t-xs", 287, 272, "vacuum", anchor="middle")
d.text("t-xs", 287, 284, "hose", anchor="middle")
# TP1: gauge on the housing's threaded test fitting
d.line("ln", 190, 308, 190, 314, sw=1.4)
gauge(190, 322)
tag(202, 326, "TP1", anchor="start")
d.text("t-xs", 234, 326, "threaded fitting")
# T3: return line off at the housing, into a container
d.path("ln dash", f"M162,{YR + 6} L146,306", sw=1.2)
container(132, 306)
tag(126, 320, "T3", anchor="end")
# purge: your canister's line, then the M3 front purge line
box("keep", TA0, 342, TA1, 366, [("t-sm", "canister", 16)], sw=1.2)
d.add(f'<path class="keep-s" d="M{TA1},354 H120" stroke-width="2"{DOT}/>')
d.add(f'<path class="donor-s" d="M120,354 H{EN0 - 9}" stroke-width="2"{DOT}/>')
arrow(EN0, 354, "r", "donor-f")
d.text("t-xs", 214, 348, "M3 front purge line", anchor="middle")

# ---------------------------------------------------------------- fallback
d.comment("Fallback: route C")
d.rect("warn-f", 8, 384, 384, 76, rx=5, sw=1.5)
d.text("t-sm t-b", 18, 400, "Route C, the fallback: your own pump")
d.text("t-xs", 18, 414, "Only if it delivers 1.3 L or more in 30 s at 5 bar (T3, our margin),")
d.text("t-xs", 18, 426.5, "and with an adapter nobody has documented: your pipe set to the M3")
d.text("t-xs", 18, 439, "rear feed, or your rear feed to the M3 filter. Route B fits the donor's")
d.text("t-xs", 18, 451.5, "whole tank instead, with the same pipe set and lines.")

svgkit_open = svgkit.svg_open(H, ARIA, extra_markers=(svgkit.marker("ahd", "donor-f"),))
p = DIAGRAMS / NAME
p.write_text(svgkit_open + d.body() + "\n</svg>\n", encoding="utf-8")
if flush_measurements():
    print("measured new strings: run again")
    sys.exit(3)
print("wrote", p)
