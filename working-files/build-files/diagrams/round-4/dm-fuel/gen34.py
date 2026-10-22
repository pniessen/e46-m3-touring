#!/usr/bin/env python3
"""Figure 34: the fuel system after the swap (route A), plan view in zones.
README "Fuel system", placeholder <!-- figure: proposed-fuel-layout --> (after "Fuel parts by car").

Data: research_notes/E46 M3 Touring coding, body and chassis/fuel_system_fit.md, "Diagram-ready data"
(zones, lines and joints, test points). Every label follows the fragment text: README 0540 Fuel system,
0210 Fuel parts, 0380 Phase 7, 0470 canister (the merged mock-up rule), 0580 Fuel-pump control; WORKSHEETS 0196. The text names only
TP1 and TP2 of the notes' IDs (Z1-Z6, L1-L5, V1, P1, E1-E3, F1, FS1, RB, VD), so zones, lines and the other
test points carry the text's own names and test numbers (T3, T4).

    python3 gen34.py        (exit 3 = new strings were measured: run it again)
"""
import sys

from kit import Doc, svg_open, write, width, flush_measurements, fmt

W, H = 800, 668
NAME = "34-fuel-layout.svg"

ARIA = (
    "Plan view of the fuel system after the swap, route A, seen from above with the front of the car to the left; "
    "schematic, not to scale. Under the rear seat, your Touring's tank stays and takes the donor's in-tank set: "
    "delivery unit 16142229684 (pump and right sender) in the right half with baffle 16112229656 under it, and the "
    "left sender 16142229683 and jet pump 16142282208 in the left half; the return flow drives the jet pump, whose "
    "transfer pipe goes into the baffle. The M3 pipe set 16112283288 is pushed onto the pump and ends in a "
    "quick-connector for the M3 rear feed; its return hose is clamped to the tank's return nipple. The lines run "
    "along the left floor to the filter-regulator under the left front floor: a new M3 filter on the donor's "
    "regulator housing and 5-bar regulator. The feed path is all quick-connectors, from the pipe set to the rear feed, the "
    "filter and the housing to the front feed; the return is hose and clamps. The housing carries TP1, the threaded "
    "test fitting. The front feed goes to the S54 feed pipe, probably through a quick-connector, and on to the rail, "
    "which has no test port. The vacuum hose, in its metal sleeve, runs from the regulator to the S54's idle-air "
    "pipe, and the M3 front purge line from your rear purge line to the S54 purge valve, whose hose ends in a "
    "quick-connector. Your filler pot, filler pipe, vent pipe, liquid-vapour separator 16136752641, canister and "
    "leak-test pump 16137193479 stay; at the filler only the flap changes, to the M3's 51172695524. The separator "
    "sits in the right rear wheel well, inside the arch-graft zone, and comes out for the arch work. With the spare "
    "well kept the canister stays fore and aft. With an M3 floor, expect the M3 holder 16132229735, crosswise; the "
    "Phase 5 mock-up decides: under 25 mm to the muffler or its right hanger, the M3 holder; 25 mm or more, either "
    "position works. Either way the canister and leak-test pump must keep working. Relay K96 stays behind the glovebox. Test hookups for Phase 7, engine out, with at least 10 L in "
    "the tank: a gauge on TP1 for T1 and T2; the return line off at the housing into a graduated container of 2 L or "
    "more for T3; a switch with a 15 A inline fuse across K96's socket pins 6 and 2 to run the pump; a meter from "
    "the pump connector to the battery posts for T4; and TP2, a gauge on the front feed's capped end before the "
    "engine is in."
)

d = Doc()
DOT = ' stroke-dasharray="0.1 4" stroke-linecap="round"'

# ---------------------------------------------------------------- symbols


def qc(x, y):
    """Quick-connector: a small filled square."""
    d.rect("fill-fg", x - 3.5, y - 3.5, 7, 7)


def clamp(x, y, along="h", half=5):
    """Hose clamp: two short bars across the line (along = the line's direction)."""
    if along == "h":
        d.line("ln", x - 2.5, y - half, x - 2.5, y + half, sw=2)
        d.line("ln", x + 2.5, y - half, x + 2.5, y + half, sw=2)
    else:
        d.line("ln", x - half, y - 2.5, x + half, y - 2.5, sw=2)
        d.line("ln", x - half, y + 2.5, x + half, y + 2.5, sw=2)


def pushon(x, y):
    """Moulded push-on end: a small open circle."""
    d.circle("shape", x, y, 3.6, sw=1.5)


def flow(x, y, direction, cls="donor-f"):
    """A small filled triangle showing which way the fuel or vapour flows."""
    s = 4
    pts = {
        "l": [(x - s, y), (x + s, y - s), (x + s, y + s)],
        "r": [(x + s, y), (x - s, y - s), (x - s, y + s)],
        "u": [(x, y - s), (x - s, y + s), (x + s, y + s)],
        "d": [(x, y + s), (x - s, y - s), (x + s, y - s)],
    }[direction]
    d.path(cls, "M" + " L".join(f"{fmt(px)},{fmt(py)}" for px, py in pts) + " Z")


def gauge(x, y, r=8):
    """A pressure gauge: dial and needle."""
    d.circle("shape", x, y, r, sw=1.4)
    d.line("ln", x, y, x + r * 0.55, y - r * 0.55, sw=1.4)
    d.dot("fill-fg", x, y, 1.6)


def container(x, y, w=16, h=18):
    """A graduated container, open at the top; (x, y) is its top-left corner."""
    d.path("ln", f"M{fmt(x)},{fmt(y)} V{fmt(y + h)} H{fmt(x + w)} V{fmt(y)}", sw=1.4)
    for i in (1, 2, 3):
        d.line("ln-thin", x + 1, y + h * i / 4, x + 6, y + h * i / 4)


def tag(x, y, s, anchor="middle"):
    """A test-point tag: white box, dark outline, bold mono text; (x, y) is the text baseline."""
    w = width("t-xs t-b t-mono", s) + 10
    x0 = x - w / 2 if anchor == "middle" else (x if anchor == "start" else x - w)
    d.rect("ln", x0, y - 11, w, 15, rx=3, sw=1.2)   # outline only: the checker reads a filled box round its own label as a clash
    d.text("t-xs t-b t-mono", x0 + w / 2, y, s, anchor="middle")
    return x0, x0 + w


def hatch(x0, y0, x1, y1, step=7.0, cls="fab-s"):
    """45-degree hatching clipped to a rectangle, drawn as plain line segments."""
    segs = []
    c = x0 - (y1 - y0)
    while c < x1:
        ax, ay, bx, by = c, y1, c + (y1 - y0), y0
        if ax < x0:
            ay -= x0 - ax
            ax = x0
        if bx > x1:
            by += bx - x1
            bx = x1
        if ax < bx:
            segs.append(f"M{fmt(ax)},{fmt(ay)} L{fmt(bx)},{fmt(by)}")
        c += step
    d.path(cls, " ".join(segs), sw=1)


def stack(x, y, rows, lh=12.5, anchor=None):
    for i, (cls, s) in enumerate(rows):
        d.text(cls, x, y + i * lh, s, anchor=anchor)


def dotted(cls, dpath, sw=2):
    d.add(f'<path class="{cls}" d="{dpath}" stroke-width="{fmt(sw)}"{DOT}/>')


def test_lead(dpath, sw=1.2):
    d.path("ln dash", dpath, sw=sw)


def tyre(x, y, w=92, h=26):
    d.rect("ln-thin", x, y, w, h, rx=7)
    for i in (1, 2, 3):
        d.line("ln-faint", x + w * i / 4, y + 4, x + w * i / 4, y + h - 4)


# ---------------------------------------------------------------- key
d.comment("Key: colours, joints, line types")
x = 8
for cls, lab in (("donor", "From donor M3"), ("keep", "Keep yours"), ("new", "Buy new")):
    d.rect(cls, x, 7, 14, 12, rx=2, sw=1)
    d.text("t-sm", x + 20, 17, lab)
    x += 20 + width("t-sm", lab) + 16
d.rect("fab-s", x, 7, 14, 12, rx=1, sw=1)
hatch(x, 7, x + 14, 19, step=4.5)
d.text("t-sm", x + 20, 17, "Arch-graft zone")
x += 20 + width("t-sm", "Arch-graft zone") + 28
qc(x + 4, 13)
d.text("t-sm", x + 14, 17, "Quick-connector")
x += 14 + width("t-sm", "Quick-connector") + 16
d.line("keep-s", x - 3, 13, x + 13, 13, sw=1.6)
clamp(x + 5, 13)
d.text("t-sm", x + 19, 17, "Hose and clamp")
x += 19 + width("t-sm", "Hose and clamp") + 16
pushon(x + 4, 13)
d.text("t-sm", x + 13, 17, "Push-on")

x = 8
for cls, sw, extra, lab in (
    ("donor-s", 3.2, "", "Feed, 5 bar"),
    ("donor-s", 1.6, "", "Return, about 0 bar"),
    ("donor-s dash", 1.6, "", "Vacuum hose"),
    ("donor-s", 2, DOT, "Purge line"),
    ("keep-s dash", 1.6, "", "Vent lines"),
    ("ln dash", 1.2, "", "Test hookup"),
):
    d.add(f'<line class="{cls}" x1="{fmt(x)}" y1="33" x2="{fmt(x + 24)}" y2="33" stroke-width="{fmt(sw)}"{extra}/>')
    d.text("t-sm", x + 30, 37, lab)
    x += 30 + width("t-sm", lab) + 18

d.text("t-h", 8, 64, "AFTER THE SWAP, ROUTE A: SEEN FROM ABOVE")
d.text("t-xs", 8, 80, "Front of the car to the left. Schematic, not to scale: the M3 lines clip to your Touring's own "
       "points, plus two M3 tubing supports.")

# ---------------------------------------------------------------- body outline
CX0, CX1, CY0, CY1 = 16, 784, 106, 482
d.comment("Body outline (faint)")
rf, rr = 56, 28
d.path("ln-faint", f"M{CX0 + rf},{CY0} H{CX1 - rr} Q{CX1},{CY0} {CX1},{CY0 + rr} V{CY1 - rr} Q{CX1},{CY1} {CX1 - rr},{CY1} "
       f"H{CX0 + rf} Q{CX0},{CY1} {CX0},{CY1 - rf} V{CY0 + rf} Q{CX0},{CY0} {CX0 + rf},{CY0} Z", sw=1.5)
d.text("t-xs", 300, 99, "right side (passenger's)", anchor="middle")
d.text("t-xs", 400, 497, "left side (driver's)", anchor="middle")

# ---------------------------------------------------------------- zones
d.comment("Zones")
Z = {
    "bay": (24, 146, 204, 474),      # engine bay
    "glove": (226, 116, 392, 230),   # behind the glovebox
    "floor": (226, 244, 440, 474),   # under the left front floor
    "seat": (448, 116, 592, 474),    # under the rear seat (tank)
    "cargo": (606, 214, 780, 384),   # under the right rear cargo floor
}
for k, (x0, y0, x1, y1) in Z.items():
    d.rect("panel", x0, y0, x1 - x0, y1 - y0, rx=6, sw=1)

# the right rear wheel well: the arch-graft zone, hatched (it stands in for the right rear wheel)
AW = (598, 108, 700, 180)
d.comment("Right rear wheel well: the arch-graft zone, hatched")
hatch(*AW, step=7)
d.rect("fab-s dash", AW[0], AW[1], AW[2] - AW[0], AW[3] - AW[1], rx=4, sw=1.2)

# the other three wheels
for wx, wy in ((106, 111), (106, 452), (602, 452)):
    tyre(wx, wy)

# lanes (y) shared by the engine bay, the left floor and the tank
Y_V, Y_F, Y_R, Y_P = 296, 352, 386, 442

# ---------------------------------------------------------------- engine bay
d.comment("Engine bay: S54, idle-air pipe, rail and feed pipe, purge valve")
x0, y0, x1, y1 = Z["bay"]
d.text("t-sm t-b", x0 + 10, y0 + 17, "Engine bay")
d.rect("donor", 40, 172, 148, 86, rx=6, sw=1.5)
d.text("t t-b", 114, 211, "S54", anchor="middle")
d.text("t-xs", 114, 227, "intake side below", anchor="middle")
# idle-air pipe with the regulator's vacuum nipple (our inference)
d.rect("donor", 36, Y_V - 3, 148, 6, rx=2, sw=1.2)
d.text("t-xs", 36, Y_V + 16, "idle-air pipe (port inferred)")
# rail and feed pipe
d.rect("donor", 36, 336, 124, 8, rx=2, sw=1.2)
d.text("t-xs", 36, 331, "rail: no test port")
d.path("donor-s", f"M160,340 H176 V{Y_F} H192", sw=3.2)
qc(196, Y_F)
stack(36, 368, [("t-xs", "feed pipe; new O-ring"), ("t-xs", "at the rail")])
tag(196, 376, "TP2", anchor="end")
stack(36, 396, [("t-xs", "front-feed joint: probably"), ("t-xs", "a quick-connector (inferred)")])
# purge valve and its hose (quick-connector at the end)
d.rect("donor", 36, Y_P - 9, 50, 18, rx=3, sw=1.2)
d.text("t-xs", 36, Y_P - 14, "purge valve")
dotted("donor-s", f"M86,{Y_P} H192")
qc(196, Y_P)

# ---------------------------------------------------------------- glovebox: K96 and the test bypass
d.comment("Behind the glovebox: K96, F54 supply, pump feed, test bypass")
x0, y0, x1, y1 = Z["glove"]
d.text("t-sm t-b", x0 + 10, y0 + 17, "Behind the glovebox")
d.rect("keep", 236, 146, 54, 58, rx=4, sw=1.5)
d.text("t t-b", 263, 172, "K96", anchor="middle")
d.text("t-xs", 263, 187, "relay", anchor="middle")
for py, pn in ((160, "6"), (190, "2")):
    d.rect("ln", 290, py - 8, 16, 16, rx=2, sw=1.2)
    d.text("t-xs t-mono", 298, py + 3.5, pn, anchor="middle")
d.line("keep-s", 306, 160, 386, 160, sw=1.5)
d.text("t-xs", 340, 154, "F54, 15 A")
d.path("keep-s", "M306,190 H418 V148 H564 V183", sw=1.5)          # pump feed to the pump connector
d.dot("fill-fg", 564, 185, 2.6)
d.text("t-xs", 236, 222, "pump feed, 1.5 mm²")
# test bypass: a switch with a 15 A inline fuse between pin 6 and pin 2
test_lead("M322,160 V167")
d.rect("shape", 318, 167, 8, 9, rx=1, sw=1.2)                     # fuse
test_lead("M322,176 V181")
d.line("ln", 322, 181, 328, 175, sw=1.4)                          # switch blade
test_lead("M322,184 V190")
d.dot("fill-fg", 322, 160, 2.4)
d.dot("fill-fg", 322, 190, 2.4)
tag(334, 180, "bypass", anchor="start")

# ---------------------------------------------------------------- left front floor: filter-regulator
d.comment("Under the left front floor: M3 filter, housing, 5-bar regulator, TP1, T3")
x0, y0, x1, y1 = Z["floor"]
d.text("t-sm t-b", x0 + 10, y0 + 17, "Under the left front floor")
HX0, HX1, FX1 = 300, 328, 380      # housing, filter rear end
# lines first, parts on top
d.path("donor-s dash", f"M308,{Y_F - 29} V{Y_V} H184", sw=1.6)               # vacuum hose
d.text("t-xs", 236, Y_V - 7, "vacuum hose, metal sleeve")
d.path("donor-s", f"M322,{Y_F + 14} V{Y_R} H464", sw=1.6)                    # return
clamp(322, Y_F + 20, along="v")
d.text("t-xs", 392, Y_R - 7, "return")
flow(372, Y_R, "r")
d.path("donor-s", f"M{HX0},{Y_F} H196", sw=3.2)                               # front feed
qc(HX0 - 4, Y_F)
d.text("t-xs", 236, Y_F + 16, "front feed")
flow(256, Y_F, "l")
d.path("donor-s", f"M{FX1},{Y_F} H456", sw=3.2)                               # rear feed
qc(FX1 + 4, Y_F)
d.text("t-xs", 392, Y_F - 7, "rear feed")
flow(446, Y_F, "l")
dotted("donor-s", f"M448,{Y_P} H196")                                         # front purge line
d.text("t-xs", 236, Y_P + 16, "front purge line")
flow(300, Y_P, "l")
# parts
d.rect("donor", HX0, Y_F - 14, HX1 - HX0, 28, rx=3, sw=1.5)                  # the donor's housing
d.rect("new", HX1, Y_F - 10, FX1 - HX1, 20, rx=8, sw=1.5)                    # filter
d.text("t-xs", 360, Y_F + 4, "filter", anchor="middle")
d.line("new-s", 344, Y_F, 334, Y_F, sw=1.2, end="ahn")
d.circle("donor", 308, Y_F - 22, 7, sw=1.5)                                  # the donor's regulator
stack(297, Y_F - 37, [("t-xs", "5-bar"), ("t-xs", "regulator on"), ("t-xs", "its housing")], anchor="end")
# TP1: gauge on the housing's threaded test fitting
d.line("ln", 324, Y_F - 14, 324, Y_F - 26, sw=1.4)
gauge(324, Y_F - 34)
tag(338, Y_F - 30, "TP1", anchor="start")
# T3: the return line off at the housing, into a graduated container
test_lead(f"M318,{Y_F + 24} L298,{Y_R + 10}")
container(286, Y_R + 10)
tag(280, Y_R + 24, "T3", anchor="end")

# ---------------------------------------------------------------- tank and in-tank set
d.comment("Under the rear seat: your tank, the donor's in-tank set, the M3 pipe set")
x0, y0, x1, y1 = Z["seat"]
d.text("t-sm t-b", x0 + 10, y0 + 17, "Under the rear seat")
TX0, TX1, TY0, TY1 = 456, 584, 140, 430
d.rect("keep", TX0, TY0, TX1 - TX0, TY1 - TY0, rx=14, sw=1.5)
d.text("t-xs t-b", 472, 294, "your tank")
# pipe set: feed hose, push-on at the pump, quick-connector at its end
d.path("donor-s", f"M550,200 H464 V{Y_F} H456", sw=3.2)
pushon(550, 200)
qc(456, Y_F)
# right half: baffle and delivery unit; pump connector
d.rect("donor-s dash", 548, 174, 32, 54, rx=6, sw=1.4)
d.circle("donor", 564, 200, 12, sw=1.5)
tag(548, 170, "T4", anchor="end")
stack(472, 222, [("t-xs", "delivery unit"), ("t-xs t-mono", "16142229684"),
                 ("t-xs", "baffle under it"), ("t-xs t-mono", "16112229656")])
# left half: pipe set label, jet pump with transfer pipe, left sender
stack(472, 312, [("t-xs", "pipe set"), ("t-xs t-mono", "16112283288")])
d.path("donor-s", f"M464,{Y_R} H548", sw=1.6)                      # pipe-set return hose to the return nipple
clamp(460, Y_R)
clamp(538, Y_R)
d.rect("donor", 548, Y_R - 6, 16, 12, rx=2, sw=1.2)                 # jet pump
d.path("donor-s", f"M572,{Y_R} V228", sw=1.6, end="ahd")           # transfer pipe into the baffle
d.line("donor-s", 564, Y_R, 572, Y_R, sw=1.6)
stack(472, 346, [("t-xs", "jet pump"), ("t-xs t-mono", "16142282208"), ("t-xs", "driven by the return")])
d.circle("donor", 552, 412, 9, sw=1.5)                              # left sender
stack(472, 408, [("t-xs", "left sender"), ("t-xs t-mono", "16142229683")])
# filler stub and vent nipple on the right side
d.text("t-xs", 462, 456, "rear purge line: yours, or")
d.text("t-xs", 462, 468, "the M3's if they don't mate")

# ---------------------------------------------------------------- arch zone: filler and separator
d.comment("Right rear wheel well (arch-graft zone): filler pot, flap, filler pipe, separator")
d.path("keep-s", "M624,122 V152 H584", sw=5)                       # filler pipe and hose
clamp(592, 152, half=6)
clamp(608, 152, half=6)
d.rect("keep", 612, 110, 24, 12, rx=2, sw=1.2)                      # filler pot
d.rect("donor", 608, 102, 32, 6, rx=1, sw=1.2)                      # M3 flap
d.text("t-xs", 782, 98, "filler pot and pipe stay; only the flap changes: M3 flap 51172695524", anchor="end")
d.path("keep-s dash", "M584,172 H646 V146 H652", sw=1.6)            # tank vent pipe to the separator
d.rect("keep", 652, 136, 36, 20, rx=3, sw=1.2)                      # separator
d.path("keep-s dash", "M688,146 H776 V268 H712", sw=1.6)            # vent pipes to the canister
stack(598, 192, [("t-xs", "right rear wheel well: separator"), ("t-xs", "16136752641, out for the arch work")])

# ---------------------------------------------------------------- cargo floor: EVAP
d.comment("Under the right rear floor: canister, DM-TL, battery")
x0, y0, x1, y1 = Z["cargo"]
d.text("t-sm t-b", x0 + 10, y0 + 17, "Under the right rear floor")
d.rect("keep", 700, 238, 52, 16, rx=3, sw=1.2)
d.text("t-xs", 726, 249.5, "battery", anchor="middle")
d.rect("keep", 632, 260, 80, 16, rx=6, sw=1.2)
d.text("t-xs", 672, 272, "canister", anchor="middle")
d.path("keep-s dash", "M656,276 V284", sw=1.6)
d.rect("keep", 632, 284, 48, 16, rx=3, sw=1.2)
d.text("t-xs", 656, 296, "DM-TL", anchor="middle")
d.path("keep-s dash", "M680,292 H690", sw=1.6)
d.rect("keep", 690, 286, 12, 12, rx=2, sw=1.2)
d.line("keep-s", 702, 292, 716, 292, sw=1.4, end="ahk")
d.text("t-xs", 720, 296, "air")
# the merged rule (README 0540 / 0470): the Phase 5 mock-up decides the canister's mounting with an M3 floor
stack(616, 316, [("t-xs", "leak-test pump 16137193479"), ("t-xs", "M3 floor: expect the M3 holder,"),
                 ("t-xs", "crosswise; the mock-up decides"), ("t-xs", "(under 25 mm to the muffler or"),
                 ("t-xs", "its right hanger: M3 holder;"), ("t-xs", "25 mm or more: either).")])
# rear purge line (yours) from the canister to the front purge line
dotted("keep-s", f"M632,268 H596 V{Y_P} H448")

# ---------------------------------------------------------------- lines list
d.comment("The M3 lines")
d.text("t-xs t-b", 612, 398, "M3 lines, from the donor:")
stack(612, 410.5, [("t-xs", "rear feed 16122229409"), ("t-xs", "front feed 16122229410"), ("t-xs", "return 16122229411"),
                   ("t-xs", "front purge line 16132229652")])

# ---------------------------------------------------------------- test hookups strip
d.comment("Test hookups, Phase 7, engine out")
d.text("t-h", 8, 528, "TEST HOOKUPS, PHASE 7 (ENGINE OUT)")
cells = [
    ("TP1", ["Gauge on the housing's threaded test fitting", "(adapter 13 5 220), filter cover off: T1 static",
             "and T2 hold; T6 and T7 at the first start."]),
    ("T3", ["Return line off at the housing, through a fuel", "hose into a graduated container of 2 L or",
            "more: 30 s, with TP1 near 5 bar throughout."]),
    ("bypass", ["Pull K96. A switch with a 15 A inline fuse", "across socket pins 6 (F54) and 2 (to the",
                "pump). Battery alone, no charger."]),
    ("T4", ["Meter from the pump connector, under the right", "rear seat, to the battery posts: within 0.5 V;",
            "0.5 V or less on the ground side."]),
    ("TP2", ["Before the engine is in: a gauge on the front", "feed's capped engine end (quick-connect",
             "adapter), or a plug rated for 5 bar."]),
]
for i, (tg, rows) in enumerate(cells):
    cx = 8 + (i % 3) * 264
    cy = 556 + (i // 3) * 54
    tag(cx, cy, tg, anchor="start")
    tx = cx + width("t-xs t-b t-mono", tg) + 18
    stack(tx, cy, [("t-xs", r) for r in rows])
# safety
d.rect("crit-s", 536, 600, 256, 56, rx=5, sw=1.5)
d.text("t-xs t-b crit-t", 546, 616, "Fuel: outdoors, extinguisher at hand.")
stack(546, 629, [("t-xs", "At least 10 L in the tank first; never run the"), ("t-xs", "pump dry or with the front feed open.")])

head = svg_open(W, H, ARIA, markers=("ah", "ahd", "ahk", "ahn"))
p = write(NAME, head, d.body())
if flush_measurements():
    print("measured new strings: run again")
    sys.exit(3)
print("wrote", p)
