"""Figure 36: the A/C refrigerant circuit after the swap (portrait, 400 wide).

Data: README 0558 "Air conditioning" (parts table, caution, charge and oil, A/C checks), README
0410 Phase 10 step 4, cooling_ac.md D3. Run: python3 gen36.py (twice if it measured new text).
"""
from coolkit import Doc, svg_open, write, width, flush, report, K

D = Doc()
T = "t-xs"

# ---------------------------------------------------------------- key
D.comment("Key")
x = 8
for cls, label in (("donor", "From donor M3"), ("keep", "Keep yours: same part on both cars"), ("new", "Buy new")):
    D.rect(cls, x, 6, 12, 12, rx=2, sw=1)
    w = D.text("t-sm", x + 17, 16.5, label)
    x += 17 + w + 16
# line key
D.line("ln", 8, 31, 34, 31, end="ah")
w = D.text("t-sm", 40, 35, "High side")
D.line("ln dash", 40 + w + 18, 31, 40 + w + 44, 31, end="ah")
D.text("t-sm", 40 + w + 50, 35, "Low side")

# ---------------------------------------------------------------- recovery first
D.comment("Recovery before any line is opened")
D.rect("crit-s", 8, 46, 384, 54, rx=5, sw=1.5)
D.text("t-sm t-b crit-t", 18, 63, "Never open a line until the refrigerant is recovered", maxw=366)
D.lines(T, 18, 78, ["A shop with Section 609-certified staff recovers it before any line is",
                    "opened. Nobody may vent it (EPA)."], 12.5, maxw=366)

# ---------------------------------------------------------------- the loop
D.comment("Condenser (keep)")
D.rect("keep", 8, 116, 138, 52, rx=5, sw=1.5)
D.text("t t-b", 18, 135, "Condenser")
D.text(T + " t-mono", 18, 150, "64538377614")
D.text(T, 18, 162, "keep yours")

D.comment("Receiver-drier (new)")
D.rect("new", 242, 116, 150, 64, rx=5, sw=1.5)
D.text("t t-b", 252, 135, "Receiver-drier, new")
D.text(T + " t-mono", 252, 150, "64538377330")
D.text(T, 252, 162.5, "fit it on the day of the charge", maxw=136)
D.rich(T, 252, 175, [(None, "keep bracket "), ("t-mono", "64536917658")], maxw=136)

D.comment("Condenser to drier: 64536904013, high side")
D.line("ln", 146, 142, 241, 142, end="ah")
D.text(T + " t-mono", 194, 134, "64536904013", anchor="middle")
D.text(T + " t-b", 194, 157, "high side", anchor="middle")

D.comment("Drier to expansion valve: 64536909448 with the pressure sensor, high side")
XR = 372
D.line("ln", XR, 180, XR, 267, end="ah")
D.circle("keep", XR, 222, 6, sw=1.5)
D.text(T + " t-mono", XR - 10, 199, "64536909448", anchor="end")
D.text("t-sm t-b", XR - 12, 219, "Pressure sensor", anchor="end")
D.text(T + " t-mono", XR - 12, 232, "64539181464", anchor="end")
D.text(T, XR - 12, 244.5, "keep yours", anchor="end")

D.comment("Your heater box: expansion valve and evaporator (keep)")
D.rect("panel", 226, 254, 168, 150, rx=6, sw=1)
D.text(T + " t-b", 234, 268, "In your heater box")
D.rect("keep", 234, 276, 154, 36, rx=5, sw=1.5)
D.text("t-sm t-b", 244, 292, "Expansion valve")
D.text(T + " t-mono", 244, 305, "64503452759")
D.line("ln dash", XR, 312, XR, 329, end="ah")
D.rect("keep", 234, 330, 154, 36, rx=5, sw=1.5)
D.text("t-sm t-b", 244, 346, "Evaporator")
D.text(T + " t-mono", 244, 359, "64119135744")
D.rich(T, 262, 382, [(None, "double pipe "), ("t-mono", "64536908907")], maxw=128)
D.text(T, 262, 395, "carries both lines", maxw=128)

D.comment("Suction: evaporator to compressor, low side")
D.path("ln dash", "M250,366 V412 H83 V387", end="ah")
D.text(T + " t-b", 166, 406, "low side", anchor="middle")
D.rich(T, 166, 427, [(None, "suction pipe "), ("t-mono", "64536923956"), (None, ", keep yours")], anchor="middle")

D.comment("Compressor (donor, on the S54)")
D.rect("donor", 8, 330, 150, 56, rx=5, sw=1.5)
D.text("t t-b", 18, 349, "Compressor")
D.text(T, 18, 364, "the donor's, on the S54,")
D.text(T, 18, 376.5, "with its bracket; a new belt")

D.comment("Compressor to condenser: the M3 pressure hose, the only M3-only line, high side")
D.line("donor-s", 40, 329, 40, 170, sw=2.5, end="ahd")
D.text("t-sm t-b donor-t", 50, 196, "M3 pressure hose")
D.text(T + " t-mono donor-t", 50, 210, "64536902681")
D.lines(T, 50, 224, ["the only line that changes:",
                     [(None, "your Touring's "), ("t-mono", "64536984883")],
                     "comes out",
                     "new O-rings at both ends;",
                     "flange screws 20 Nm"], 12.5, maxw=170)

# ---------------------------------------------------------------- charge and checks
D.comment("Charge and oil")
D.rect("panel", 8, 442, 384, 82, rx=6, sw=1)
D.text("t-sm t-b", 18, 459, "Charge and oil")
D.lines(T, 18, 474, ["R-134a by weight, to your Touring's underhood label: the label decides.",
                     "Expect about 0.74 kg (26 oz). MAHLE, a vendor source, lists 715–765 g",
                     "for every E46 petrol engine, the S54 included.",
                     "Oil: PAG, about 150 ml (5.1 US fl oz) for the whole system (MAHLE)."], 12.5, maxw=366)

D.comment("Pass checks")
D.rect("panel", 8, 532, 384, 70, rx=6, sw=1)
D.text("t-sm t-b", 18, 549, "Pass checks (BMW)")
D.lines(T, 18, 564, ["Evaporator, in BMW's efficiency test: 15 °C (59 °F) or less in 3–4 minutes",
                     "Low side: 1–2 bar (15–30 psi); up to about 3 bar (45 psi) on a hot day",
                     "High side: 10–15 bar (150–225 psi), engine at 1,500–2,000 rpm"], 12.5, maxw=366)

H = 610
ARIA = ("The A/C refrigerant circuit after the swap, high side solid and low side dashed. The donor's "
        "compressor, on the S54, pumps refrigerant through the M3 pressure hose 64536902681, the only line "
        "that changes (your Touring's 64536984883 comes out), to the condenser 64538377614, through hose "
        "64536904013 to a new receiver-drier 64538377330 in your bracket 64536917658, then through hose "
        "64536909448 past the pressure sensor 64539181464 to the expansion valve 64503452759 and the "
        "evaporator 64119135744 in your heater box, and back through the double pipe 64536908907 and the "
        "suction pipe 64536923956 to the compressor. Every other part has the same part number on the US M3 "
        "and the US 325i Touring, so your Touring's stay, apart from the drier. A shop with Section "
        "609-certified staff recovers the refrigerant before any line is opened, and nobody may vent it. "
        "Charge R-134a by weight to your Touring's underhood label, about 0.74 kg; MAHLE, a vendor source, "
        "lists 715 to 765 g for every E46 petrol engine, with about 150 ml of PAG oil for the whole system. "
        "BMW's pass values: the evaporator at 15 °C or less within 3 to 4 minutes, the low side at 1 to 2 bar "
        "and the high side at 10 to 15 bar with the engine at 1,500 to 2,000 rpm.")

ahd = ('  <marker id="ahd" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="4.2" markerHeight="4.2" '
       'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="donor-f"/></marker>')
head = svg_open(H, ARIA, markers=("ah",)).replace("</defs>", ahd + "\n</defs>")
p = write("36-ac-circuit.svg", head, D.body())
print("wrote", p)
report()
if flush():
    print("measured new strings: run again")
