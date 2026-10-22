"""Figure 35: the S54 coolant circuit in the Touring, with the fill-and-bleed points (portrait).

Data: README 0550 parts table, "Heater valve and its pump", "Fill and bleed the cooling system"
(steps 1-14) and "Cooling checks"; README 0200 and 0410; WIRING-AND-CODING 0290;
cooling_ac.md D1 and BMW ST041 p.13 (circuit topology). Run: python3 gen35.py (twice if it
measured new text).
"""
from coolkit import Doc, svg_open, write, flush, report, width

D = Doc()
T = "t-xs"
HOT = "stroke-width:3"


def pill(x, y, label, anchor="start"):
    """A step number (or several) in a dark pill; (x, y) is the left (or centre) of the pill's
    vertical middle. Returns the pill's width."""
    w = max(width("t-sm t-b fill-bg", label), width("t-sm t-b fill-bg", label, True)) + 12
    w = max(w, 36)
    x0 = x - w / 2 if anchor == "middle" else x
    D.rect("fill-fg", x0, y - 10, w, 20, rx=10)
    D.text("t-sm t-b fill-bg", x0 + w / 2, y + 4, label, anchor="middle")
    return w


# ---------------------------------------------------------------- key
D.comment("Key")
x = 8
for cls, label in (("keep", "Keep"), ("donor", "From donor M3"), ("new", "Buy new")):
    D.rect(cls, x, 6, 12, 12, rx=2, sw=1)
    w = D.text("t-sm", x + 17, 16.5, label)
    x += 17 + w + 16
D.line("ln", 8, 33, 36, 33, end="aht", style=HOT)
w = D.text("t-sm", 42, 37, "Hot: thermostat open")
D.line("ln dash", 42 + w + 20, 33, 42 + w + 48, 33, end="ah")
D.text("t-sm", 42 + w + 54, 37, "Warm-up: thermostat shut")
D.line("ln", 8, 55, 36, 55, end="ah")
w = D.text("t-sm", 42, 59, "Hot and warm-up")
x = 42 + w + 20
D.line("ln-thin", x, 55, x + 28, 55, end="ah")
D.text("t-sm", x + 34, 59, "Tank lines")

# ---------------------------------------------------------------- expansion tank (new) and cap
D.comment("Expansion tank (new) with the 2.0 bar cap: steps 5, 7, 8, 11 and 14 at the neck")
D.rect("new", 110, 98, 180, 44, rx=5, sw=1.5)
D.text("t-sm t-b", 120, 116, "Expansion tank")
D.rich(T, 120, 131, [("t-mono", "17112283344"), (None, ", new")])
D.rect("keep", 124, 90, 22, 8, rx=2, sw=1.5)
D.rich(T, 152, 93, [(None, "cap "), ("t-mono", "17117639022"), (None, ": 2.0 bar")])
pill(72, 89, "5 7 8 10 11 14", anchor="middle")
D.text(T, 72, 113, "tank neck", anchor="middle")

# ---------------------------------------------------------------- radiator (donor)
D.comment("Radiator (donor); the vent line to the tank and the tank's line to the pump")
D.rect("donor", 40, 164, 300, 38, rx=5, sw=1.5)
D.rich("t-sm t-b", 50, 181, [(None, "Radiator "), ("t-mono", "17102228941")])
D.text(T, 50, 195, "the M3's: no drain plug")
D.line("ln-thin", 230, 164, 230, 143, end="ah")
D.path("ln-thin", "M290,120 H384 V300", end=None)
# ---------------------------------------------------------------- thermostat (new), pump (donor), bypass
D.comment("Thermostat 80 °C (new) and water pump (donor); the bypass between them")
D.rect("new", 40, 286, 110, 44, rx=5, sw=1.5)
D.text("t-sm t-b", 50, 304, "80 °C thermostat")
D.rich(T, 50, 318, [("t-mono", "11531318274"), (None, ", new")])
D.rect("donor", 250, 286, 90, 44, rx=5, sw=1.5)
D.text("t-sm t-b", 260, 304, "Water pump")
D.text(T + " t-mono", 260, 318, "11517838118")
D.line("ln dash", 151, 308, 249, 308, end="ah")
D.text(T, 200, 302, "bypass", anchor="middle")

# hot hose up to the radiator, with the vent screw
D.comment("Hose 11537830716 with the vent screw: steps 4, 6, 10 and 13")
D.line("ln", 95, 285, 95, 204, end="aht", style=HOT)
D.circle("new", 95, 246, 5, sw=1.5)
pill(50, 246, "4 6 10 13", anchor="middle")
D.rich(T + " t-b", 106, 230, [(None, "Vent screw "), ("t-mono", "17111712788")])
D.rich(T, 106, 243, [(None, "in hose "), ("t-mono", "11537830716")])
D.text(T, 106, 255.5, "under the intake ducting;")
D.text(T, 106, 268, "plastic: 2.5 Nm")

# lower hose down to the pump, with the outlet sensor
D.comment("Lower hose to the pump with the radiator-outlet sensor: steps 1 and 12")
D.line("ln", 295, 203, 295, 285, end="aht", style=HOT)
D.circle("keep", 295, 222, 5, sw=1.5)
D.text(T + " t-b", 305, 220, "outlet sensor")
D.text(T + " t-mono", 305, 232.5, "13621433077")
pw = pill(303, 249, "12")
D.text(T, 303 + pw + 4, 253, "Tool32")
pw = pill(303, 272, "1")
D.text(T, 303 + pw + 4, 276, "hose on")

# tank line and heater return join, then into the pump
D.circle("fill-fg", 384, 300, 2.5)
D.line("ln-thin", 384, 300, 341, 300, end="ah")

# ---------------------------------------------------------------- engine (donor)
D.comment("Block and cross-flow head (donor); the return pipe up to the thermostat")
D.rect("donor", 40, 372, 110, 44, rx=5, sw=1.5)
D.text("t-sm t-b", 50, 390, "Cylinder head")
D.text(T, 50, 404, "S54")
D.rect("donor", 250, 372, 90, 44, rx=5, sw=1.5)
D.text("t-sm t-b", 260, 390, "Block")
D.text(T, 260, 404, "S54")
D.line("ln", 295, 330, 295, 371, end="ah")
D.text(T, 303, 354, "into the block")
D.line("ln", 250, 394, 151, 394, end="ah")
D.text(T, 200, 388, "into the head", anchor="middle")
D.line("ln", 95, 372, 95, 331, end="ah")
D.text(T, 103, 360, "return pipe")
# block drain plug
D.comment("Block drain plug: step 1")
pill(206, 437, "1")
D.lines(T, 250, 434, ["block drain plug in: 24 Nm", "(one owner's figure), with a",
                      "new 14 mm washer"], 12.5, maxw=130)

# ---------------------------------------------------------------- heater loop
D.comment("Heater: from the return pipe through the valve and your heater core, back to the pump")
D.circle("fill-fg", 95, 350, 2.5)
D.path("ln", "M95,350 H20 V488 H39", end="ah")
D.rect("shape", 40, 466, 110, 44, rx=5, sw=1.5)
D.text("t-sm t-b", 50, 484, "Heater valve")
D.text(T, 50, 498, "two options: below")
D.line("ln", 151, 488, 249, 488, end="ah")
D.rect("keep", 250, 466, 90, 44, rx=5, sw=1.5)
D.text("t-sm t-b", 260, 484, "Heater core")
D.text(T, 260, 498, "yours, kept")
D.path("ln", "M341,488 H384 V302")
pw = pill(40, 528, "9")
D.text(T, 40 + pw + 6, 532, "ignition on, blower low, heat at maximum:")
D.text(T, 40 + pw + 6, 544.5, "the valve opens fully; the M3 valve's pump runs.")
D.text(T, 40 + pw + 6, 557, "IHKR: blower at 1, not 0, and the dial fully right.")
D.text(T, 40 + pw + 6, 569.5, "In Phase 10, ignition off, it rests open.")

# ---------------------------------------------------------------- phases
D.comment("The steps by phase")
D.text("t-sm t-b", 8, 596, "Numbered points: the steps below, by phase")
y = 614
for label, txt in (("1–8", "Phase 10: engine cold, ignition off"),
                   ("9–10", "Phase 12, before the first start: ignition on, engine off"),
                   ("11–14", "First start and heat cycles: repeat 11–13 until no hiss")):
    pw = pill(8, y, label)
    D.text(T, 8 + pw + 6, y + 4, txt)
    y += 22

# ---------------------------------------------------------------- heater valve options
D.comment("Heater valve: two options")
Y = 688
D.rect("panel", 8, Y, 188, 154, rx=6, sw=1)
D.rect("panel", 204, Y, 188, 154, rx=6, sw=1)
D.text("t-sm t-b", 18, Y + 18, "1  Your plain valve")
D.text(T + " t-b", 18, Y + 31, "recommended")
D.rect("keep", 18, Y + 39, 10, 10, rx=2, sw=1)
D.rich(T, 33, Y + 48, [(None, "valve "), ("t-mono", "64118369805"), (None, ", yours")], maxw=158)
D.rect("new", 18, Y + 55, 10, 10, rx=2, sw=1)
D.rich(T, 33, Y + 64, [(None, "to the core: CSL hose")], maxw=158)
D.text(T + " t-mono", 33, Y + 76.5, "64212282548", maxw=158)
D.lines(T, 18, Y + 94, ["No wiring, no coding. The engine's",
                        "own pump vents the heater circuit",
                        "(our inference): allow two heat",
                        "cycles."], 12.5, maxw=172)
D.text("t-sm t-b", 214, Y + 18, "2  The M3 valve and its pump")
D.rect("donor", 214, Y + 39, 10, 10, rx=2, sw=1)
D.rich(T, 229, Y + 48, [(None, "valve "), ("t-mono", "64118369807")], maxw=158)
D.rect("donor", 214, Y + 55, 10, 10, rx=2, sw=1)
D.rich(T, 229, Y + 64, [(None, "to the core: hose "), ("t-mono", "64216902679")], maxw=158)
D.lines(T, 214, Y + 94, ["Two wires, and the coding",
                         [("t-mono", "ZUSATZWASSERPUMPE"), (None, " = "), ("t-mono", "aktiv"), (None, ".")],
                         "Wire it before you fill: BMW's fill",
                         "runs the pump to vent the heater",
                         "circuit."], 12.5, maxw=172)
D.rich(T, 8, Y + 172, [(None, "Both options: the donor's hoses "), ("t-mono", "64216902678"),
                       (None, ", engine to valve,")], maxw=384)
D.rich(T, 8, Y + 184.5, [(None, "and "), ("t-mono", "64216902680"),
                         (None, ", heater core to engine. Schematic, not to scale.")], maxw=384)

H = Y + 194
ARIA = ("The S54 coolant circuit in your Touring, as a schematic with the radiator at the top, and the points "
        "used to fill and bleed it, numbered as in the steps of Fill and bleed the cooling system. The water "
        "pump, 11517838118, pushes coolant into the block, through the cylinder head and back "
        "through the return pipe to the 80 °C thermostat, 11531318274, which is new. While the thermostat is "
        "shut during warm-up, the coolant goes straight back to the pump through the bypass. Once it opens at "
        "80 °C, the coolant runs through hose 11537830716 to the M3 radiator, 17102228941, which has no drain "
        "plug, and back through the lower hose, past the radiator-outlet sensor 13621433077, to the pump. The "
        "heater circuit takes coolant from the return pipe through the heater valve to your Touring's heater "
        "core and back to the pump: either your plain valve 64118369805 with the CSL hose "
        "64212282548, the recommended option, with no wiring or coding, or the M3 valve with its pump, "
        "64118369807, with hose 64216902679, two wires and coding; both use the donor's hoses 64216902678 and "
        "64216902680. A line from the radiator vents to the new expansion tank, 17112283344, with its 2.0 bar "
        "cap 17117639022, and a line from the tank feeds the pump. Step 1 is the block drain plug, 24 Nm by "
        "one owner's figure, with a new 14 mm washer, and the lower hose. Steps 4, 6, 10 and 13 are at the vent screw 17111712788 in hose "
        "11537830716, under the intake ducting, plastic, 2.5 Nm. Steps 5, 7, 8, 10, 11 and 14 are at the tank neck. "
        "Step 9 is at the heater valve: with the ignition on, the blower low and the heat at maximum it opens "
        "fully and the M3 valve's pump runs (with manual climate control, blower at 1, "
        "not 0, and the dial fully right); with the ignition off in Phase 10 it rests open. Step 12 reads the "
        "radiator-outlet temperature in Tool32. Steps 1 to 8 are in Phase 10 with the engine cold and the "
        "ignition off, 9 and 10 in Phase 12 before the first start with the ignition on, and 11 to 14 at the "
        "first start and heat cycles, repeating 11 to 13 until no air hisses out.")

aht = ('  <marker id="aht" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="3.6" markerHeight="3.6" '
       'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="fill-fg"/></marker>')
head = svg_open(H, ARIA).replace("</defs>", aht + "\n</defs>")
p = write("35-coolant-circuit.svg", head, D.body())
print("wrote", p)
report()
if flush():
    print("measured new strings: run again")
