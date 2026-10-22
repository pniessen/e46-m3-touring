"""diagrams/31-ride-height.svg (portrait), for README 0520 "Suspension for Touring weight",
placeholder proposed-ride-height-points.
BMW's method and figures from TIS 31 00, 33 00 and 32 00 (issue 12/2007), as the coordinator
directed from gapfill_bmw_chassis_body.md: ride height runs from the rim flange (bottom middle) to
the lower edge of the wheel arch, in "normal position", a DIN load (not unladen). M3: 605/587 mm on
18-inch, 619/600 on 19-inch. Touring: the TIS series and sport rows, 15-18 inch. +/-10 mm, left and
right within 10 mm. Plus hub-to-lip, the rim and tyre notes, and the Phase 0 Massachusetts baseline
(jacking points, roof marks, BMW's published roof heights).
The wheel is drawn to scale (0.23 px/mm) for an M3 front on 18-inch wheels: tyre radius 330 mm,
rim-flange radius 246 mm (rim radius + 17.5 mm flange, the notes' assumption), hub to arch 359 mm.
    python3 -I gen31.py"""
import math
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, __import__("os").path.dirname(__file__))
from chkit import Doc, fmt, svg_open, width, wrap, write  # noqa: E402

W = 400
d = Doc()
LH = 13


def para(cls, x, y, s, maxw, lh=LH):
    ls = wrap(cls, s, maxw)
    return d.lines(cls, x, y, ls, lh)


# ================================================================ one wheel, side view
d.comment("One wheel, side view: BMW's ride height and hub-to-lip")
d.text("t-h", 8, 22, "BMW'S RIDE HEIGHT")
d.text("t-xs", 8, 36, "one wheel, side view; the same at all four corners")

S = 0.23
cx, cy = 166, 176
rt, rr, ra = 330 * S, 246 * S, 359 * S          # tyre, rim flange, hub-to-arch
Ay, Cy, Ry = cy - ra, cy, cy + rr
ground = cy + rt
# body side with the arch cut out
pb = cy + 16                                     # panel bottom
dx = math.sqrt(ra * ra - (pb - cy) ** 2)
d.path("panel", f"M{fmt(cx - 100)},52 H{fmt(cx + 96)} V{fmt(pb)} H{fmt(cx + dx)} "
       f"A{fmt(ra)},{fmt(ra)} 0 1 0 {fmt(cx - dx)},{fmt(pb)} H{fmt(cx - 100)} Z", sw=1.5)
d.path("keep-s", f"M{fmt(cx + dx)},{fmt(pb)} A{fmt(ra)},{fmt(ra)} 0 1 0 {fmt(cx - dx)},{fmt(pb)}", sw=2.5)
# ground, tyre, rim, hub
d.line("ln-thin", cx - 84, ground, cx + 84, ground)
d.circle("shape", cx, cy, rt, sw=2.5)
d.circle("ln", cx, cy, rr, sw=1.5)
d.circle("ln-thin", cx, cy, rr - 7)
for k in range(5):
    a = math.radians(-90 + 72 * k + 36)
    d.line("ln-thin", cx + 13 * math.cos(a), cy + 13 * math.sin(a),
           cx + (rr - 9) * math.cos(a), cy + (rr - 9) * math.sin(a))
d.circle("ln", cx, cy, 12)
# the three points
for y in (Ay, Cy, Ry):
    d.circle("fill-fg", cx, y, 3.2)

# dimension lines, right of the wheel
x1 = cx + rt + 12          # hub-to-lip: hub centre to arch edge
x2 = x1 + 20               # BMW's ride height: rim flange to arch edge
d.line("ln-thin", cx + 4, Ay, x2 + 5, Ay)
d.line("ln-thin", cx + 14, Cy, x1 + 5, Cy)
d.line("ln-thin", cx + 4, Ry, x2 + 5, Ry)
d.line("ln", x1, Ay + 1, x1, Cy - 1, end="ah", start="ah")
d.line("ln", x2, Ay + 1, x2, Ry - 1, end="ah", start="ah")

# labels for the points, left of the wheel
LX = 8
d.text("t-xs t-b", LX, Ay + 4, "Arch edge")
d.line("ln-thin", LX + width("t-xs t-b", "Arch edge") + 5, Ay, cx - 5, Ay)
d.text("t-xs t-b", LX, Cy + 4, "Hub centre")
d.line("ln-thin", LX + width("t-xs t-b", "Hub centre") + 5, Cy, cx - 13, Cy)
d.text("t-xs t-b", LX, Ry - 9, "Rim flange,")
d.text("t-xs t-b", LX, Ry + 4, "bottom middle")
d.line("ln-thin", LX + width("t-xs t-b", "bottom middle") + 5, Ry, cx - 5, Ry)

# labels for the dimensions, right of the lines
RX = x2 + 10
RW = W - 8 - RX
yh = Ay + 18
d.line("ln-thin", RX - 3, yh - 4, x1, yh - 4)
d.circle("fill-fg", x1, yh - 4, 2)
d.text("t-xs t-b", RX, yh, "Hub-to-lip")
para("t-xs", RX, yh + LH, "hub centre to the same arch edge: it doesn't depend on the rim", RW)
yH = Cy + 22
d.line("ln-thin", RX - 3, yH - 4, x2, yH - 4)
d.circle("fill-fg", x2, yH - 4, 2)
d.text("t-xs t-b", RX, yH, "BMW's ride height")
para("t-xs", RX, yH + LH, "tape from the rim flange to the arch edge", RW)

# ================================================================ BMW's figures
d.comment("BMW's figures, TIS 31 00 and 33 00 (12/2007), at each car's normal-position load")
y = ground + 34
d.text("t-h", 8, y, "BMW'S FIGURES, MM")
y = para("t-xs", 8, y + 14, "TIS, rim flange to arch edge: ±10 mm (0.4 in), and left and right within 10 mm "
         "of each other. BMW measures each car in normal position, the load under its table.", 384)
y += 10
C1, C2, C3, C4 = 206, 252, 306, 352   # column centres: front, rear (standard), front, rear (sport)
ROW = 19


def load_line(y0, s):
    return para("t-xs", 18, y0, s, 364)


# --- M3 table
t0 = y
rows_m3 = [("18-inch wheels", "605", "587"), ("19-inch wheels", "619", "600")]
load_m3 = ("Normal position: full tank, 68 kg (150 lb) on each front seat, 14 kg (31 lb) in the "
           "middle of the trunk")
nl = len(wrap("t-xs", load_m3, 364))
h_m3 = 24 + ROW * len(rows_m3) + 8 + nl * LH + 4
d.rect("panel", 8, t0, 384, h_m3, rx=6, sw=1)
d.text("t-sm t-b", 18, t0 + 17, "E46 M3")
d.text("t-xs t-b", C1, t0 + 17, "front", anchor="middle")
d.text("t-xs t-b", C2, t0 + 17, "rear", anchor="middle")
for i, (lab, f, r) in enumerate(rows_m3):
    yy = t0 + 24 + ROW * i + 14
    d.line("ln-faint", 18, yy - 14, 382, yy - 14)
    d.text("t-sm", 18, yy, lab)
    d.text("t t-b", C1, yy + 0.5, f, anchor="middle")
    d.text("t t-b", C2, yy + 0.5, r, anchor="middle")
load_line(t0 + 24 + ROW * len(rows_m3) + 14, load_m3)
y = t0 + h_m3 + 10

# --- Touring table
t1 = y
rows_t = [("15-inch", "576", "542", "561", "526"), ("16-inch", "589", "555", "574", "539"),
          ("17-inch", "604", "570", "589", "554"), ("18-inch", "617", "583", "602", "567")]
load_t = ("Normal position: full tank, 68 kg (150 lb) on each front seat, 68 kg in the middle of the "
          "rear seat, 21 kg (46 lb) in the trunk")
nl = len(wrap("t-xs", load_t, 364))
h_t = 38 + ROW * len(rows_t) + 8 + nl * LH + 4
d.rect("panel", 8, t1, 384, h_t, rx=6, sw=1)
d.text("t-sm t-b", 18, t1 + 17, "Your 325i Touring")
d.text("t-xs t-b", (C1 + C2) / 2, t1 + 17, "standard", anchor="middle")
d.text("t-xs t-b", (C3 + C4) / 2, t1 + 17, "sport suspension", anchor="middle")
for c, lab in ((C1, "front"), (C2, "rear"), (C3, "front"), (C4, "rear")):
    d.text("t-xs", c, t1 + 31, lab, anchor="middle")
d.line("ln-faint", (C2 + C3) / 2, t1 + 8, (C2 + C3) / 2, t1 + 38 + ROW * len(rows_t))
for i, (lab, a, b, c, e) in enumerate(rows_t):
    yy = t1 + 38 + ROW * i + 14
    d.line("ln-faint", 18, yy - 14, 382, yy - 14)
    d.text("t-sm", 18, yy, lab)
    for col, v in ((C1, a), (C2, b), (C3, c), (C4, e)):
        d.text("t", col, yy + 0.5, v, anchor="middle")
load_line(t1 + 38 + ROW * len(rows_t) + 14, load_t)
y = t1 + h_t + 18

# --- notes
d.comment("Rim size and tyres")
y = para("t-xs", 8, y, "A bigger rim raises BMW's figure about 12.7 mm (0.5 in) per inch with the body where "
         "it was: BMW's rows step 13–15 mm per inch, and hub-to-lip stays the same. M3 tyres also lift the "
         "body itself about 14 mm (0.6 in) at the same suspension position (our arithmetic).", 384)

# ================================================================ Massachusetts baseline
d.comment("Massachusetts baseline: your Touring in Phase 0, before the swap")
y += 34
d.text("t-h", 8, y, "MASSACHUSETTS BASELINE")
d.text("t-xs", 8, y + 14, "your Touring in Phase 0, before the swap, loaded to its normal position")
y += 30
d.text("t-xs t-b", 200, y + 4, "Roof marks, front and rear: measure each from the floor", anchor="middle")
d.text("t-xs", 200, y + 17, "BMW: 1,409 mm (55.5 in); 1,444 mm (56.8 in) with roof rails", anchor="middle")

CS = 0.08                 # px per mm, schematic side view
X0 = 21                   # rear end of the car
roof_y = y + 34
F0 = roof_y + 1409 * CS   # the floor


def P(xm, ym):
    return f"{fmt(X0 + xm * CS)},{fmt(F0 - ym * CS)}"


RA, FA, HUB = 980, 3705, 300          # rear axle, front axle (2,725 mm wheelbase), hub height
ARCH = 370
body = (f"M{P(60, 300)} L{P(18, 380)} L{P(8, 560)} L{P(30, 650)} L{P(60, 770)} L{P(175, 1340)} "
        f"L{P(260, 1400)} L{P(2380, 1409)} L{P(2480, 1385)} L{P(3300, 965)} L{P(4300, 790)} "
        f"L{P(4440, 735)} L{P(4478, 620)} L{P(4470, 380)} L{P(4420, 300)} L{P(FA + ARCH, HUB)} "
        f"A{fmt(ARCH * CS)},{fmt(ARCH * CS)} 0 0 0 {P(FA - ARCH, HUB)} L{P(FA - ARCH - 30, 190)} "
        f"L{P(RA + ARCH + 30, 190)} L{P(RA + ARCH, HUB)} "
        f"A{fmt(ARCH * CS)},{fmt(ARCH * CS)} 0 0 0 {P(RA - ARCH, HUB)} Z")
d.path("shape", body, sw=1.5)
glass = f"M{P(250, 985)} L{P(205, 1330)} L{P(2400, 1345)} L{P(3170, 990)} Z"
d.path("panel", glass, sw=1)
for xm in (1150, 2050):  # C and B pillars
    d.line("ln-thin", X0 + xm * CS, F0 - 985 * CS, X0 + xm * CS, F0 - 1345 * CS)
d.line("ln-thin", X0 - 6, F0, X0 + 4478 * CS + 8, F0)
for xm in (RA, FA):
    d.circle("fill-fg", X0 + xm * CS, F0 - HUB * CS, HUB * CS)
    d.circle("shape", X0 + xm * CS, F0 - HUB * CS, 215 * CS, sw=1)
d.text("t-xs", X0 + 4478 * CS, F0 - 1250 * CS, "front →", anchor="end")
# roof marks
for xm in (700, 2100):
    xp = X0 + xm * CS
    d.path("fill-fg", f"M{fmt(xp - 4)},{fmt(roof_y - 8)} H{fmt(xp + 4)} L{fmt(xp)},{fmt(roof_y - 1)} Z")
# BMW's DIN load for the Touring (positions schematic)
for xm, lab in ((2455, "2 × 68 kg"), (1555, "68 kg"), (505, "21 kg")):
    xp = X0 + xm * CS
    d.rect("fill-fg", xp - 6, F0 - 600 * CS - 6, 12, 7, rx=1)
    d.text("t-xs t-b", xp, F0 - 600 * CS - 11, lab, anchor="middle")
# jacking points
jp = [1600, 3085]
for xm in jp:
    xp = X0 + xm * CS
    d.rect("fill-fg", xp - 4, F0 - 190 * CS, 8, 4)
    d.line("ln-thin", xp, F0 - 190 * CS + 5, xp, F0 + 9)
yb = F0 + 20
d.text("t-xs t-b", 200, yb, "Jacking points, two each side: measure each from the floor", anchor="middle")
y = yb + 22
y = para("t-xs", 8, y, "Record at that load, before anything changes: BMW's ride height and hub-to-lip at each "
         "corner, the four jacking points, the roof marks and the door-pillar label.", 384)
y = para("t-xs", 8, y + LH + 3, "After the build, measure the same points the same way. Pass: the roof and "
         "every jacking point within 50.8 mm (2 in) of Phase 0. Our target: within 25 mm (1 in).", 384)

# ================================================================ how to measure
d.comment("How BMW measures")
y += 16
items = [
    "Level floor; tyres at placard pressure; a metric tape with 1 mm divisions.",
    "Load the car as its table says. Bounce each corner and roll the car a few feet before you read.",
    "Short of a full tank, add 3.2 kg (7 lb) in the cargo area for each US gallon.",
]
wr = [wrap("t-xs", s, 362) for s in items]
h = 30 + sum(len(ls) * LH for ls in wr) + 3 * (len(wr) - 1)
d.rect("warn-f", 8, y, 384, h, rx=5, sw=1.5)
d.text("t-sm t-b", 18, y + 17, "Measure the BMW way")
yy = y + 32
for ls in wr:
    yy = d.lines("t-xs", 18, yy, ls, LH) + LH + 3
H = int(y + h + 8)

ARIA = (
    "BMW's ride height and the Massachusetts baseline. One wheel in side view, the same at every corner: "
    "BMW's ride height is measured with a metric tape from the rim flange, at the bottom middle, to the lower "
    "edge of the wheel arch; hub-to-lip runs from the hub centre to the same arch edge and doesn't depend on "
    "the rim. BMW's figures from TIS, rim flange to arch edge, are plus or minus 10 mm, with left and right "
    "within 10 mm of each other, and are measured in normal position, a load. E46 M3: front 605 mm and rear "
    "587 mm on 18-inch wheels, 619 and 600 mm on 19-inch wheels, with a full tank, 68 kg on each front seat "
    "and 14 kg in the middle of the trunk. 325i Touring, front and rear, standard suspension: 576 and 542 mm "
    "on 15-inch wheels, 589 and 555 on 16-inch, 604 and 570 on 17-inch, 617 and 583 on 18-inch; sport "
    "suspension: 561 and 526, 574 and 539, 589 and 554, 602 and 567 mm; with a full tank, 68 kg on each front "
    "seat, 68 kg in the middle of the rear seat and 21 kg in the trunk. A bigger rim raises BMW's figure by "
    "about 12.7 mm per inch with the body where it was, and BMW's rows step 13–15 mm per inch, while hub-to-lip "
    "doesn't change; M3 tyres lift the body about 14 mm at the same suspension position. Massachusetts "
    "baseline, a side view of your Touring in Phase 0 before the swap, loaded to its normal position: record "
    "BMW's ride height and hub-to-lip at each corner, the height of the four jacking points, two each side, "
    "and the roof at marks front and rear, each from the floor. BMW publishes the roof height as 1,409 mm "
    "(55.5 in), or 1,444 mm (56.8 in) with roof rails. After the build, measure the same points the same "
    "way: the roof and every jacking point must be within 50.8 mm (2 in) of Phase 0, and our target is 25 mm "
    "(1 in). Measure on a level floor with the tyres at placard pressure, bounce each corner and roll the car "
    "first, and add 3.2 kg (7 lb) in the cargo area for each US gallon short of a full tank."
)
p = write("31-ride-height.svg", svg_open(W, H, ARIA), d.body())
print("wrote", p, "height", H)
