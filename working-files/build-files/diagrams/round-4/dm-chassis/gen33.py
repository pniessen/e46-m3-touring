"""diagrams/33-power-steering.svg (portrait), for README 0500 "Front axle and steering",
placeholder proposed-power-steering-circuit.
Circuit (0500): reservoir -> suction hose -> pump -> pressure hose -> rack -> return pipe -> cooling
coil in front of the radiator -> return line -> reservoir. M3 parts: pump, pressure hose, suction
hose, return pipe, cooling coil, return line (and the rack). Shared: reservoir with lid and bracket,
column, lower joint, flexible coupling, steering-angle sensor. Torques (0500 step 10): M16 hollow
bolts 40 Nm, M14 rack banjo with check valve 35 Nm, new rings; pump mounting bolts M8x80 21 Nm,
pulley bolts 27 Nm. Fluid (0530): ATF (Dexron III type), not CHF 11S, don't mix; capacity not found.
Part numbers only where the text gives them (reservoir, label, rack, lower joint, angle sensor).
    python3 -I gen33.py"""
import sys
sys.dont_write_bytecode = True
sys.path.insert(0, __import__("os").path.dirname(__file__))
from chkit import Doc, key, svg_open, wrap, write  # noqa: E402

W = 400
d = Doc()
LH = 13


def box(cls, x, y, w, h, title, subs=(), tcls="t-sm t-b", center=True):
    d.rect(cls, x, y, w, h, rx=5, sw=1.5)
    n = 1 + len(subs)
    first = y + h / 2 - (n - 1) * 6.5 + 4
    cx = x + w / 2 if center else x + 10
    anchor = "middle" if center else None
    d.text(tcls, cx, first, title, anchor)
    for i, (c, s) in enumerate(subs):
        d.text(c, cx, first + 13 * (i + 1), s, anchor)


def para(cls, x, y, s, maxw, anchor=None):
    ls = wrap(cls, s, maxw)
    return d.lines(cls, x, y, ls, LH, anchor)


def ring(x, y):
    """A new sealing ring pair at a hollow bolt or banjo."""
    d.rect("new", x - 7, y - 3.5, 14, 7, rx=2, sw=1.5)


# ---------------------------------------------------------------- key
d.comment("Key")
key(d, 8, 6, [("keep", "Shared: keep yours"), ("donor", "From donor M3"), ("new", "New sealing rings")], gap=12)

d.text("t-h", 8, 42, "POWER-STEERING CIRCUIT")
d.text("t-xs", 8, 56, "schematic; arrows show the flow")

# ---------------------------------------------------------------- parts
XL, XR = 74, 330          # supply branch (left), return branch (right)
d.comment("Reservoir: the same part on both cars")
RX, RY, RW, RH = 152, 70, 124, 50
box("keep", RX, RY, RW, RH, "Reservoir", [("t-xs t-mono", "32416851217"), ("t-xs", "lid and bracket too")])
RM = RY + RH / 2

d.comment("M3 pump")
PX, PY, PW, PH = 16, 152, 118, 50
box("donor", PX, PY, PW, PH, "M3 pump, ZF", [("t-xs", "up to 120 bar,"), ("t-xs", "11 L/min")])

d.comment("Cooling coil, in front of the radiator")
CX, CY, CW, CH = 272, 214, 120, 40
box("donor", CX, CY, CW, CH, "Cooling coil", [("t-xs", "in front of the radiator")])

d.comment("M3 rack")
KY, KH = 338, 44
box("donor", 16, KY, 368, KH, "M3 rack 32132229397",
    [("t-xs", "15.4:1, no hydraulic end stops: don't hold the wheel at full lock")])

d.comment("Lines: M3 parts, arrows in the direction of flow")
d.path("donor-s", f"M{RX},{RM} H{XL} V{PY - 1}", sw=2.5, end="ahd")                 # suction hose
d.line("donor-s", XL, PY + PH, XL, KY - 1, sw=2.5, end="ahd")                       # pressure hose
d.line("donor-s", XR, KY, XR, CY + CH + 1, sw=2.5, end="ahd")                       # return pipe
d.path("donor-s", f"M{XR},{CY} V{RM} H{RX + RW + 1}", sw=2.5, end="ahd")             # return line
d.text("t-xs donor-t t-b", XL + 8, RM - 7, "suction hose")
d.text("t-xs donor-t t-b", XL + 9, 268, "pressure hose")
d.text("t-xs donor-t t-b", XR - 9, 296, "return pipe", anchor="end")
d.text("t-xs donor-t t-b", XR + 9, 150, "return line")

d.comment("Joints: new sealing rings and torques")
ring(XL, PY + PH + 13)
d.text("t-xs t-b", XL + 12, PY + PH + 17, "M16 hollow bolt, 40 Nm (30 ft-lb)")
ring(XL, KY - 11)
d.text("t-xs t-b", XL + 12, KY - 7, "M16 hollow bolt, 40 Nm")
ring(XR, KY - 11)
d.text("t-xs t-b", XR - 12, KY - 20, "M14 banjo with check valve,", anchor="end")
d.text("t-xs t-b", XR - 12, KY - 7, "35 Nm (26 ft-lb)", anchor="end")
para("t-xs", 146, 162, "If the pump comes off: mounting bolts M8×80 21 Nm (15 ft-lb), pulley bolts "
     "27 Nm (20 ft-lb).", 118)

d.comment("Steering column parts: the same on both cars")
SY = KY + KH + 12
d.line("ln", 100, KY + KH, 100, SY)
lines = wrap("t-xs", "The same parts on both cars, so keep yours; the angle sensor is 32306793632. The "
             "lower joint changed from 32301094700 to 32306764006 at 11/2003 on both: keep whichever "
             "you have.", 344)
SH = 22 + len(lines) * LH + 8
d.rect("keep", 16, SY, 368, SH, rx=5, sw=1.5)
d.text("t-sm t-b", 26, SY + 17, "Column, lower joint, coupling, steering-angle sensor")
d.lines("t-xs", 26, SY + 32, lines, LH)
y = SY + SH + 14

d.comment("Fluid")
fl = [
    ("t-sm t-b", "ATF (Dexron III type), not Pentosin CHF 11S"),
    ("t-xs", "Don't mix the two. BMW's catalog pairs the reservoir with label 71246798132, listed for ATF. "
             "Green fluid in the donor's reservoir means it was converted: flush the whole system to one fluid."),
    ("t-xs crit-t", "Capacity: not found. Fill to the mark on the lid."),
]
wr = [(c, wrap(c, s, 362) if c != "t-sm t-b" else [s]) for c, s in fl]
h = 14 + sum(len(ls) * LH for _, ls in wr) + 3 * (len(wr) - 1) + 2
d.rect("warn-f", 8, y, 384, h, rx=5, sw=1.5)
yy = y + 18
for c, ls in wr:
    yy = d.lines(c, 18, yy, ls, LH) + LH + 3
y += h + 18

d.comment("Fill and bleed")
y = para("t-xs", 8, y, "Keep the lines clear of the anti-roll bar and the oil pan.", 384)
y = para("t-xs", 8, y + LH + 3, "Fill before the first start: a dry pump rattles. Engine off, fill to about 25 mm (1 in) "
         "below the edge; start and top up; turn to full lock each way twice, without holding it there; "
         "switch off and top up to the mark.", 384)
y = para("t-xs", 8, y + LH + 3, "Check: no foaming or groaning after a short run, no weeps at the hollow bolts "
         "or the rack banjo, and the level steady after a drive.", 384)
H = int(y + 10)

ARIA = (
    "The power-steering circuit, schematic, with arrows in the direction of flow: from the reservoir "
    "through the suction hose to the pump, through the pressure hose to the rack, then through the return "
    "pipe to the cooling coil in front of the radiator, and through the return line back to the reservoir. "
    "The pump, the suction and pressure hoses, the rack (32132229397, 15.4:1), the return pipe, the cooling "
    "coil and its return line are M3 parts from the donor. The M3's ZF pump makes up to 120 bar and 11 litres "
    "a minute, and the M3 rack has no hydraulic end stops, so don't hold the wheel at full lock. The reservoir "
    "32416851217 with its lid and bracket, the steering column, the lower joint, the flexible coupling and "
    "the steering-angle sensor 32306793632 are the same parts on both cars, so they stay; the lower joint "
    "changed from 32301094700 to 32306764006 at 11/2003 on both cars. Torques, each with new sealing rings: "
    "the M16 hollow bolts at the pump outlet and at the rack, 40 Nm (30 ft-lb); the M14 banjo with its check "
    "valve at the rack, 35 Nm (26 ft-lb). If the pump comes off, its M8 by 80 mounting bolts take 21 Nm "
    "(15 ft-lb) and its pulley bolts 27 Nm (20 ft-lb). Keep the lines clear of the anti-roll bar and oil "
    "pan. The fluid is ATF of the Dexron III type, not Pentosin CHF 11S, and the two must not be mixed; BMW's "
    "catalog pairs the reservoir with label 71246798132, listed for ATF, and green fluid in the donor's reservoir means the system must be "
    "flushed to one fluid. The capacity wasn't found: fill to the mark on the lid. Fill before the first "
    "start; with the engine off fill to about 25 mm below the edge, start and top up, turn to full lock each "
    "way twice without holding it there, then switch off and top up to the mark. Check for no foaming or "
    "groaning, no weeps at the hollow bolts or the banjo, and a steady level after a drive."
)
p = write("33-power-steering.svg", svg_open(W, H, ARIA, markers=("ah", "ahd")), d.body())
print("wrote", p, "height", H)
