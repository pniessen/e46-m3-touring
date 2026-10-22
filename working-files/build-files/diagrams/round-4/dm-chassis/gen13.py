"""Redraw of diagrams/13-dsc-brake-options.svg (README Figure 12) for the round-4 text in
README 0610 (DSC, brakes and steering angle) and 0530 (Brakes and bleeding).
Fixes: pedal feel (330i master cylinder, ~10% longer and lighter, one firm-pedal report),
booster vacuum (M3 check valve in a new grommet on the shortened S54 hose), wheel-speed
sensors (yours stay; MK20 donors' inductive sensors don't fit), and route B's coding (review
rv-chassis F1: codes only from a session order with the donor's M3 type key and a 09/2002+ date,
then INPA's initialisation; refit your own unit only if "VIN not initialized" stays on).
    python3 -I gen13.py"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, __import__("os").path.dirname(__file__))
from chkit import Doc, key, svg_open, wrap, width, write  # noqa: E402

W = 400
d = Doc()
LH = 13  # t-xs line height

# ---------------------------------------------------------------- key
d.comment("Key")
key(d, 8, 6, [("keep", "Keep"), ("donor", "From donor M3"), ("new", "Buy new")])

# ---------------------------------------------------------------- which unit the donor has
d.comment("Which unit the donor has")
d.rect("donor", 8, 28, 188, 52, rx=5, sw=1.5)
d.text("t-sm t-b", 18, 45, "Donor built before 09/2002")
d.text("t-xs", 18, 59, "MK20, 43-pin plug:")
d.text("t-xs crit-t", 18, 72, "won't plug into your harness")
d.rect("donor", 204, 28, 188, 52, rx=5, sw=1.5)
d.text("t-sm t-b", 214, 45, "Donor built from 09/2002")
d.text("t-xs", 214, 59, "MK60: same 47-pin plug and yaw")
d.text("t-xs", 214, 72, "sensor as your Touring's")
d.line("ln", 102, 80, 102, 99, end="ah")
d.line("ln", 298, 80, 298, 99, end="ah")
d.path("ln", "M240,80 V89 H150 V99", end="ah")

# ---------------------------------------------------------------- the two routes
COLW = 186


def bullets(x, y, items):
    """Paragraphs of t-xs text; returns the y of the last baseline."""
    for i, (cls, s) in enumerate(items):
        if i:
            y += LH + 4
        ls = s if isinstance(s, list) else wrap(cls, s, COLW)
        y = d.lines(cls, x, y, ls, LH)
    return y


d.comment("Route A")
d.text("t-h", 8, 116, "A  KEEP YOURS")
d.text("t-xs t-b", 8, 130, "the default; recommended")
ya = bullets(8, 148, [
    ("t-xs", "No coding: initialise its VIN and steering angle in INPA, then run the compensation routines"),
    ("t-xs", "Stays coded for a 325i: no M Track"),
    ("t-xs", "Your master cylinder is the 330i's: expect a front pedal about 10% longer and lighter "
             "than an M3's (our estimate). One 2004 Touring with M3 brakes reported a firm pedal"),
    ("t-xs", "Check its label first: some US Tourings have an ASC-only unit"),
])

d.comment("Route B")
d.text("t-h", 204, 116, "B  FIT THE M3'S UNIT")
d.text("t-xs t-b", 204, 130, "09/2002-on donors only")
yb = bullets(204, 148, [
    ("t-xs", ["Codes only from a session order with",       # review rv-chassis F1, exact lines
              "the donor's M3 type key and a 09/2002+",
              "date; it then takes the M3's values.",
              "No Touring body type: leave coupe_m"]),
    ("t-xs", "Brings M Track"),
    ("t-xs", "Touring built before 09/2001: also the later yaw-sensor cluster"),
    ("t-xs", ["Then INPA's VIN and steering-angle",          # review rv-chassis F1, exact lines
              "initialisation. \"VIN not initialized\"",
              "still on? Refit your own unit"]),
])

# ---------------------------------------------------------------- hydraulics, pedal to caliper
d.comment("Brake hydraulics, pedal to caliper")
y = max(ya, yb) + 16


def row2(y, h, a, b):
    """One row of two boxes: a and b = (cls, title, note, note_right)."""
    for x, (cls, title, note, right) in ((8, a), (204, b)):
        d.rect(cls, x, y, 188, h, rx=5, sw=1.5)
        if note and not right:
            d.text("t t-b", x + 10, y + h / 2 - 3.3, title)
            d.text("t-xs", x + 10, y + h / 2 + 10.2, note)
        else:
            d.text("t t-b", x + 10, y + h / 2 + 4.6, title)
            if note:
                d.text("t-xs", x + 178, y + h / 2 + 3.7, note, anchor="end")


row2(y, 36, ("keep", "Your booster", "", False), ("keep", "Your booster", "or perhaps the M3's", False))
d.line("ln", 102, y + 36, 102, y + 46)
d.line("ln", 298, y + 36, 298, y + 46)
y += 46
row2(y, 36, ("keep", "Your master cylinder", "the 330i's", False), ("donor", "M3 master cylinder", "", False))
d.line("ln", 102, y + 36, 102, y + 46)
d.line("ln", 298, y + 36, 298, y + 46)
y += 46
row2(y, 26, ("keep", "Your MK60", "DSC unit", True), ("donor", "M3 MK60", "DSC unit", True))
d.line("ln", 102, y + 26, 102, y + 36)
d.line("ln", 298, y + 26, 298, y + 36)
y += 36

d.comment("Same on both routes")
d.rect("keep", 8, y, 384, 38, rx=5, sw=1.5)
d.text("t-sm t-b", 18, y + 15.5, "Your brake pipes stay")
d.text("t-xs", 18, y + 29, "an MK60 M3 uses the same front pipes; the rear pipes and hoses are shared")
d.line("ln", 200, y + 38, 200, y + 48)
y += 48
for cls, title, note in (("new", "M3 front brake hoses", "M3-only, buy new: 34322229723"),
                         ("donor", "M3 calipers", "with the corners and trailing arms"),
                         ("keep", "Your wheel-speed sensors", "the same parts on M3s from 09/2002")):
    d.rect(cls, 8, y, 384, 26, rx=5, sw=1.5)
    d.text("t t-b", 18, y + 17.6, title)
    d.text("t-xs", 382, y + 16.7, note, anchor="end")
    if title == "M3 front brake hoses":
        d.line("ln", 200, y + 26, 200, y + 36)
    y += 36 if title == "M3 front brake hoses" else 34

# ---------------------------------------------------------------- both routes
d.comment("Both routes")
y += 0
items = [
    "Wheel-speed sensors: yours read the M3 hubs and half-shafts. An MK20 donor's inductive sensors "
    "(gray plugs) don't fit your harness: never splice them in.",
    "Booster vacuum: a new grommet 34336765316 and the M3's check valve 34331161300 in your booster, "
    "on the S54's hose shortened to reach it.",
    "Calibrate the steering angle after the wheel alignment.",
    "Keep your MK60, booster, master cylinder and cluster until the car has passed inspection.",
]
lines = [wrap("t-xs", s, 362) for s in items]
h = 32 + sum(len(ls) * LH for ls in lines) + 2 * (len(lines) - 1) - 4
d.rect("panel", 8, y, 384, h, rx=6, sw=1)
d.text("t-sm t-b", 18, y + 17, "Both routes")
yy = y + 32
for ls in lines:
    yy = d.lines("t-xs", 18, yy, ls, LH) + LH + 2
H = int(y + h + 8)

ARIA = (
    "The DSC and brake choice. A donor built before 09/2002 has an MK20 with a 43-pin plug, which won't plug "
    "into your harness, so only route A applies; a donor built from 09/2002 has an MK60 with the same 47-pin "
    "plug and yaw sensor as your Touring, so either route works. Route A, the recommended default, keeps your "
    "MK60, master cylinder and booster: no coding, just initialise its VIN and steering angle in INPA and run "
    "the compensation routines. It stays coded for a 325i with no M Track. Your master cylinder is the 330i's, "
    "so expect a front pedal about 10% longer and lighter than an M3's (our estimate); one 2004 Touring with "
    "M3 brakes reported a firm pedal. Check the unit's label first, as some US Tourings have an ASC-only unit. "
    "Route B fits the M3's MK60 and master cylinder, with your booster or perhaps the M3's. NCS Expert "
    "codes it only from a session-only vehicle order with the donor's M3 type key and a date from 09/2002, and "
    "it then takes the M3's values; its coding has no Touring body type, so it stays coupe_m. It brings M "
    "Track; a Touring built before 09/2001 also needs the later yaw-sensor cluster. Then run INPA's VIN and "
    "steering-angle initialisation; if VIN not initialized still won't clear, refit your own unit. On both routes your brake "
    "pipes stay, since an MK60 M3 uses the same front pipes and the rear pipes and hoses are shared; the "
    "M3-only front brake hoses 34322229723 are bought new; the M3 calipers come with the corners; and your own "
    "wheel-speed sensors stay, the same parts as on M3s from 09/2002. An MK20 donor's inductive sensors with "
    "gray plugs don't fit, so never splice them in. The booster takes a new grommet 34336765316 and the M3's "
    "check valve 34331161300, on the S54's vacuum hose shortened to reach it. Calibrate the steering angle "
    "after the wheel alignment, and keep your MK60, booster, master cylinder and cluster until the car has "
    "passed inspection."
)
p = write("13-dsc-brake-options.svg", svg_open(W, H, ARIA), d.body())
print("wrote", p, "height", H)
