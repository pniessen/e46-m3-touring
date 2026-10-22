"""diagrams/32-brake-hydraulics.svg (portrait), for README 0530 "Brakes and bleeding",
placeholder proposed-brake-hydraulics; its lower panel also covers proposed-booster-vacuum.
Option A hydraulics: your booster, master cylinder, MK60 and every hard line stay; the M3 front
hoses 34322229723 and the M3 calipers are the changes; rear hoses are common. Unknowns (which
master-cylinder outlet is the front circuit, which rear pipe serves which side, the MK60's port
layout) are drawn generically and labelled "check on the car".
    python3 -I gen32.py"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, __import__("os").path.dirname(__file__))
from chkit import Doc, fmt, key, svg_open, wrap, write  # noqa: E402

W = 400
d = Doc()
LH = 13


def box(cls, x, y, w, h, title, subs=(), tcls="t-sm t-b", center=True):
    """A part box: title plus sub-lines [(cls, text), ...], centred vertically."""
    d.rect(cls, x, y, w, h, rx=5, sw=1.5)
    n = 1 + len(subs)
    first = y + h / 2 - (n - 1) * 6.5 + 4
    cx = x + w / 2 if center else x + 9
    anchor = "middle" if center else None
    d.text(tcls, cx, first, title, anchor)
    for i, (c, s) in enumerate(subs):
        d.text(c, cx, first + 13 * (i + 1), s, anchor)


def hose(cls, x1, x2, y, sw=3):
    """A wavy hose between x1 and x2 at height y."""
    n = 4
    step = (x2 - x1) / n
    p = f"M{fmt(x1)},{fmt(y)}"
    for i in range(n):
        dy = -5 if i % 2 == 0 else 5
        p += f" q{fmt(step / 2)},{dy} {fmt(step)},0"
    d.path(cls, p, sw=sw)


def bleed(x, y, n):
    """Bleed-order badge (unfilled, so the number isn't drawn over a filled shape)."""
    d.circle("ln", x, y, 9, sw=1.5)
    d.text("t-xs t-b", x, y + 3.8, str(n), anchor="middle")


def para(cls, x, y, s, maxw):
    ls = wrap(cls, s, maxw)
    return d.lines(cls, x, y, ls, LH)


# ---------------------------------------------------------------- key
d.comment("Key")
key(d, 8, 6, [("keep", "Keep"), ("donor", "From donor M3"), ("new", "Buy new"),
              ("fab", "Modify"), ("remove", "Remove")], gap=11)

# ---------------------------------------------------------------- the hydraulics
d.comment("Hydraulics: schematic, front at the top, the car's left side on the left")
d.text("t-h", 8, 46, "HYDRAULICS")
d.text("t-xs", 8, 60, "schematic, front at the top")

d.comment("Booster, master cylinder and reservoir: all yours")
MX, MY, MW, MH = 150, 78, 112, 48        # master cylinder
BX, BY, BW, BH = 58, 82, 92, 40          # booster, bolted to the master cylinder
box("keep", BX, BY, BW, BH, "Your booster", [("t-xs t-mono", "34336779682")])
box("keep", MX, MY, MW, MH, "Master cylinder", [("t-xs", "yours: the 330i's"), ("t-xs t-mono", "34336785666")])
d.text("t-xs", BX + BW / 2, BY + BH + 14, "vacuum: see below", anchor="middle")
RX, RY, RW, RH = 170, 54, 72, 24
box("keep", RX, RY, RW, RH, "Reservoir", tcls="t-xs t-b")
d.comment("Clutch feed from the reservoir")
d.path("keep-s", f"M{RX + RW},{RY + 12} H{299}", sw=2)
bleed(310, RY + 12, 5)
d.text("t-xs t-b", 325, RY + 16, "Clutch")
d.text("t-xs", 325, RY + 29, "bleed it last,")
d.text("t-xs", 325, RY + 42, "at the slave")

d.comment("MK60: ports drawn generic")
KX, KY, KW, KH = 156, 182, 100, 62
box("keep", KX, KY, KW, KH, "Your MK60", [("t-xs t-mono", "34516765453"), ("t-xs crit-t", "ports: check"),
                                         ("t-xs crit-t", "on the car")])
for x in (190, 222):  # master cylinder to MK60: two pipes, one per circuit
    d.line("keep-s", x, MY + MH, x, KY, sw=2.5)
d.text("t-xs t-b", 185, 152, "front", anchor="end")
d.text("t-xs t-b", 227, 152, "rear")
d.text("t-xs", 185, 165, "(sensor V)", anchor="end")
d.text("t-xs", 227, 165, "(sensor H)")
d.text("t-xs", 286, 152, "outlets inferred")
d.text("t-xs", 286, 165, "from BMW's photos")

d.comment("Front corners: new M3 hoses on your pipes, M3 calipers")
FY = 213
CW, CH = 64, 34
for side, cx_, br, mk in (("L", 8, 108, KX), ("R", W - 8 - CW, W - 108, KX + KW)):
    box("donor", cx_, FY - CH / 2, CW, CH, "M3 caliper", tcls="t-xs t-b")
    if side == "L":
        hose("new-s", cx_ + CW, br, FY)
        d.line("keep-s", br, FY, mk, FY, sw=2.5)
    else:
        hose("new-s", br, cx_, FY)
        d.line("keep-s", mk, FY, br, FY, sw=2.5)
    d.circle("shape", br, FY, 3.2, sw=1.5)
d.text("t-xs t-b", 8, FY - CH / 2 - 9, "Left front")
bleed(72, FY - CH / 2 - 13, 4)
d.text("t-xs t-b", W - 8, FY - CH / 2 - 9, "Right front", anchor="end")
bleed(W - 81, FY - CH / 2 - 13, 3)
for x in (92, W - 92):
    d.text("t-xs new-t t-b", x, FY + CH / 2 + 15, "M3 hose, new", anchor="middle")
    d.text("t-xs t-mono", x, FY + CH / 2 + 28, "34322229723", anchor="middle")

d.comment("Rear: two pipes along the floor to your hoses (common) and the M3 calipers")
RYc = 424
for x, br in ((198, 108), (214, W - 108)):
    d.path("keep-s", f"M{x},{KY + KH} V{RYc} H{br}", sw=2.5)
d.rect("shape", 210, RYc - 4, 8, 8, sw=1.5)  # the union on the right-hand pipe
d.text("t-xs", 153, RYc - 7, "3,684 mm", anchor="middle")
d.text("t-xs", 224, RYc - 7, "3,798 + 1,206 mm")
d.text("t-xs", 222, RYc + 15, "union")
for side, cx_, br in (("L", 8, 108), ("R", W - 8 - CW, W - 108)):
    box("donor", cx_, RYc - CH / 2, CW, CH, "M3 caliper", tcls="t-xs t-b")
    if side == "L":
        hose("keep-s", cx_ + CW, br, RYc)
    else:
        hose("keep-s", br, cx_, RYc)
    d.circle("shape", br, RYc, 3.2, sw=1.5)
d.text("t-xs t-b", 8, RYc + CH / 2 + 17, "Left rear")
bleed(70, RYc + CH / 2 + 13, 2)
d.text("t-xs t-b", W - 8, RYc + CH / 2 + 17, "Right rear", anchor="end")
bleed(W - 79, RYc + CH / 2 + 13, 1)
for x in (92, W - 92):
    d.text("t-xs", x, RYc - CH / 2 - 19, "your hose", anchor="middle")
    d.text("t-xs t-mono", x, RYc - CH / 2 - 6, "34301165174", anchor="middle")
d.text("t-xs", 200, RYc + 33, "rear pipe sides and lengths inferred", anchor="middle")
d.text("t-xs", 200, RYc + 46, "from BMW's ETK drawing", anchor="middle")

d.comment("Notes between the rear pipes' runs")
para("t-xs", 8, 290, "Every pipe stays: an MK60 M3 uses the same four front pipes, 34326759218, "
     "34326755801, 34326752405 and 34326752407, and the same rear pipes.", 178)
para("t-xs", 226, 290, "Front hoses: 19 Nm (14 ft-lb) at the caliper. Yours, 34326766966, come off.", 166)
para("t-xs", 226, 342, "Option B (the M3's MK60) also brings the M3's master cylinder, 34317838638.", 166)

# ---------------------------------------------------------------- filling and bleeding
d.comment("Filling and bleeding")
y = RYc + CH / 2 + 44
items = [
    ("t-xs", "Fluid: DOT 4 low-viscosity, BMW 81220142156, about 1.5 L (1.6 US qt)."),
    ("t-xs t-b", "Pressure bleeder: no more than 2 bar (29 psi), on an airtight cap."),
    ("t-xs", "Flush each wheel until the fluid runs clear and bubble-free: 1\u00a0right\u00a0rear, "
             "2\u00a0left\u00a0rear, 3\u00a0right\u00a0front, 4\u00a0left\u00a0front. "
             "The clutch is last\u00a0(5)."),
    ("t-xs", "After caliper or hose work (TIS 34 00 048): bleed the rear circuit with the tester's "
             "routine (INPA's MK60 bleed). At each front, pump the pedal fully at least 12 times and "
             "close the bleeder with the pedal held down."),
    ("t-xs", "After work on the master cylinder, the MK60 or the pipes between them (TIS 34 00 050): "
             "run the routine at each wheel in the same order, restarting it for every wheel, with "
             "5 full pedal strokes after each run."),
]
wrapped = [(c, wrap(c, s, 364)) for c, s in items]
h = 30 + sum(len(ls) * LH for _, ls in wrapped) + 3 * (len(wrapped) - 1) + 2
d.rect("panel", 8, y, 384, h, rx=6, sw=1)
d.text("t-sm t-b", 18, y + 17, "Fill and bleed")
yy = y + 32
for c, ls in wrapped:
    yy = d.lines(c, 18, yy, ls, LH) + LH + 3
y += h + 26

# ---------------------------------------------------------------- booster vacuum
d.comment("Booster vacuum: the S54's jet pump to your booster")
d.text("t-h", 8, y + 6, "BOOSTER VACUUM")
d.text("t-xs", 8, y + 20, "arrows: the way air flows, from the booster to the engine")
y += 34
CHX, CHW, BHh, GAP = 8, 150, 34, 16
chain = [
    ("donor", "Air shut-off valve", [("t-xs t-mono", "11617833212")]),
    ("donor", "Suction jet pump", [("t-xs", "on the S54")]),
    ("fab", "Donor's hose", [("t-xs", "shortened or re-routed")]),
    ("new", "Clamp", [("t-xs t-mono", "11151726340")]),
    ("donor", "M3 check valve", [("t-xs t-mono", "34331161300")]),
    ("new", "New grommet", [("t-xs t-mono", "34336765316")]),
    ("keep", "Your booster", [("t-xs t-mono", "34336779682")]),
]
tops = []
for i, (cls, title, subs) in enumerate(chain):
    top = y + i * (BHh + GAP)
    tops.append(top)
    box(cls, CHX, top, CHW, BHh, title, subs, center=False)
    if i == 1:   # the valve switches the pump: no air-flow arrow here
        d.line("ln", CHX + CHW - 30, top - GAP, CHX + CHW - 30, top)
    elif i > 1:  # air flows up the chain, booster to engine
        d.line("ln", CHX + CHW - 30, top, CHX + CHW - 30, top - GAP + 1, end="ah")
NX = CHX + CHW + 14
NW = W - 8 - NX
notes = {
    0: "The DME switches it to add vacuum: A/C on, in gear with the clutch up, or below 70 °C (158 °F). "
       "It clicks in the DME's valve test at first key-on.",
    1: "The S54's own vacuum supply: keep it, the valve and their wiring working.",
    2: "It meets the M3's booster from the other side: shorten or re-route it to reach yours.",
    4: "Blow through it first: air must pass only from the booster toward the engine.",
}
for i, s in notes.items():
    ls = wrap("t-xs", s, NW)
    first = tops[i] + BHh / 2 - (len(ls) - 1) * LH / 2 + 3.7
    d.lines("t-xs", NX, first, ls, LH)
d.comment("Removed: your own non-return valve and elbow")
rt = tops[5] - 1
rh = 2 * BHh + GAP + 2
d.rect("keep dash", NX, rt, NW, rh, rx=5, sw=1.5)
d.path("crit-s", f"M{NX + 10},{rt + 10} l11,11 M{NX + 10},{rt + 21} l11,-11", sw=2)
d.text("t-xs t-b crit-t", NX + 29, rt + 19.5, "Remove")
rl = wrap("t-xs", "Your non-return valve 34331160183 and its elbow 34336751108: the M3 check valve "
          "goes in their place.", NW - 20)
d.lines("t-xs", NX + 10, rt + 37, rl, LH)
y = tops[-1] + BHh + 20
y = para("t-xs", 8, y, "Check once the engine runs: engine off, pump the pedal until it's hard, hold it with "
         "about 110 N (25 lb) and start the engine. The pedal must drop slightly.", 384)
H = int(y + 10)

ARIA = (
    "Brake hydraulics and booster vacuum, schematic, front at the top. Your booster 34336779682, your "
    "master cylinder 34336785666 (the 330i's) with its reservoir, and your MK60 DSC unit 34516765453 all "
    "stay; the reservoir also feeds the clutch. Two pipes run from the master cylinder to the MK60, one per "
    "circuit: the outlet next to the booster feeds the front circuit (pressure sensor V) and the other the "
    "rear (sensor H), as inferred from BMW's photos. From the MK60 one pipe runs to each front corner and two "
    "run along the floor to the rear: a single 3,684 mm pipe to the left rear, and a 3,798 mm pipe to a union "
    "and a 1,206 mm crossover to the right rear, as inferred from BMW's ETK drawing. The MK60's port layout "
    "isn't in the sources: check it on the car. Every pipe stays, since an MK60 M3 uses the same four front "
    "pipes, 34326759218, 34326755801, 34326752405 and 34326752407, and the same rear pipes. At the front, new "
    "M3-only hoses 34322229723 replace your 34326766966 and feed the M3 calipers, 19 Nm at the caliper; at the "
    "rear your hoses 34301165174, the same part as the M3's, feed the M3 calipers. Option B, the M3's MK60, "
    "also brings the M3 master cylinder 34317838638. Fill with DOT 4 low-viscosity fluid, BMW 81220142156, "
    "about 1.5 litres; a pressure bleeder must not exceed 2 bar (29 psi). Flush each wheel until the fluid "
    "runs clear and bubble-free in the order right rear, left rear, right front, left front, and bleed the "
    "clutch last. After caliper or hose work BMW bleeds the rear circuit with the tester's routine, INPA's "
    "MK60 bleed, and each front by pumping the pedal fully at least 12 times and closing the bleeder with the "
    "pedal held down. After work on the master cylinder, the MK60 or the pipes between them, the routine runs "
    "at each wheel in the same order, restarted for every wheel, with 5 full pedal strokes after each run. "
    "Booster vacuum, with air flowing from the booster toward the engine: the S54's air shut-off valve "
    "11617833212, which the DME switches to add vacuum with the A/C on, in gear with the clutch up or below "
    "70 °C, controls the suction jet pump; the donor's hose, shortened or re-routed because it meets the M3's "
    "booster from the other side, runs through clamp 11151726340 to the M3 check valve 34331161300, in a new "
    "grommet 34336765316 in your booster 34336779682. Your own non-return valve 34331160183 and its elbow "
    "34336751108 come out, and the check valve goes in their place. Air must pass the check valve only from "
    "the booster toward the engine. To check once the engine runs, pump the pedal hard with the engine off, "
    "hold about 110 N (25 lb) and start the engine: the pedal must drop slightly."
)
p = write("32-brake-hydraulics.svg", svg_open(W, H, ARIA), d.body())
print("wrote", p, "height", H)
