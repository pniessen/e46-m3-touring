#!/usr/bin/env python3
"""Generate diagrams/19-circuit-dmtl.svg: the leak-test (DM-TL) module circuit with the M3 DME as BMW draws it
(the "pump on 30" case), the heater wire's move, the label and color conflicts, and the test that decides
pins 20 and 30. Data: wiring-canonical.md section 6.4 and the manual's "DM-TL leak-test pump: test before you
swap", "X60004 pin by pin" and "Earlier MS43 Tourings"."""
import sys
sys.dont_write_bytecode = True
from ckit import (svg_open, marker, t, tm, M, W, tm_width, rect, line, path, dot, write, measure_missing, fmt)

WIDTH = 800


def build():
    out = []
    add = out.append

    def cell(cx, cy, label, cls="shape", w=22, h=18):
        add(rect(cls, cx - w / 2, cy - h / 2, w, h, rx=2, sw="1.2"))
        add(t("t t-mono", cx, cy + 4.5, label, "middle"))

    def badge(x, y, n):
        add(f'<circle class="fill-fg" cx="{fmt(x)}" cy="{fmt(y)}" r="9"/>')
        add(t("t t-b fill-bg", x, y + 4.5, n, "middle"))

    def ref_box(x, cy, parts, cls="keep", pad=7, h=20):
        """A connector-and-pin reference in a small box, e.g. [X60004] pin [18]; returns its right edge."""
        w = tm_width("t-sm", parts) + 2 * pad
        add(rect(cls, x, cy - h / 2, w, h, rx=3, sw="1.2"))
        add(tm("t-sm", x + pad, cy + 4, parts))
        return x + w

    def para(x, y, lines, cls="t-sm", step=14):
        for i, s in enumerate(lines):
            add(tm(cls, x, y + step * i, M(s)))

    # ------------------------------------------------------------------ header, key, assumptions
    add(t("t-h", 8, 24, "WITH THE M3 DME, AS BMW DRAWS IT"))
    kx = 792
    for kind, cls, label in [("swatch", "new-s", "New wire"), ("swatch", "fab-s", "Moved wire"),
                             ("box", "keep", "Keep"), ("box", "donor", "From donor M3")]:
        kx -= W("t-sm", label)
        add(t("t-sm", kx, 22, label))
        kx -= 22
        if kind == "box":
            add(rect(cls, kx, 12, 14, 12, rx=2, sw="1"))
        else:
            add(line(cls, kx - 6, 18, kx + 14, 18, sw="2.5"))
            kx -= 6
        kx -= 16
    add(t("t-sm", 8, 44, 'Touring and donor built from 09/2001; drawn for the "pump on 30" result of the test below.'))

    # ------------------------------------------------------------------ schematic
    yS, y18, y20, y30 = 108, 148, 188, 228         # rows: supply, heater, pin 20, pin 30
    dme_x1 = 128
    stripL = (128, 162)                            # X60004 cavities
    stripR = (344, 380)                            # module plug
    mod_x1 = 516
    cL = sum(stripL) / 2
    cR = sum(stripR) / 2

    add("\n<!-- Supply: DME relay, F3, X6021 pin 2, splice X11212, module pin 4 -->")
    add(rect("shape", 8, yS - 18, 120, 36))
    add(t("t t-b", 16, yS - 3, "Fuse F3, 20 A"))
    add(t("t-sm", 16, yS + 12, "after the DME relay"))
    add(line("donor-s", 128, yS, 146, yS, sw="2"))
    add(rect("donor", 146, yS - 9, 20, 18, rx=2, sw="1.2"))
    add(rect("keep", 166, yS - 9, 20, 18, rx=2, sw="1.2"))
    add(t("t t-mono", 156, yS + 4.5, "2", "middle"))
    add(t("t t-mono", 176, yS + 4.5, "2", "middle"))
    add(t("t-sm t-mono t-b", 166, yS - 15, "X6021", "middle"))
    xs = 262
    add(line("keep-s", 186, yS, cR - 11, yS, sw="2"))
    add(tm("t-sm", (186 + xs - 4) / 2, yS - 6, M("[1.5 RT/WS]"), "middle"))
    add(tm("t-sm", (xs + 4 + cR - 11) / 2, yS - 6, M("[0.75 RT/WS]"), "middle"))
    add(dot("keep-f", xs, yS, 4))
    add(line("keep-s", xs, yS - 4, xs, yS - 34, sw="2", mk="ahk"))
    add(t("t-sm", xs, yS - 44, "also feeds the K96 and K19 relay coils", "middle"))
    add(tm("t-sm t-b", xs + 8, yS - 26, M("splice [X11212]")))

    add("\n<!-- DME and its X60004 cavities -->")
    add(rect("donor", 8, 136, dme_x1 - 8, 110))
    add(t("t t-b", 16, 155, "M3 DME"))
    add(t("t-sm", 16, 171, "MSS54 / HP"))
    add(rect("keep", stripL[0], 138, stripL[1] - stripL[0], 104, rx=3, sw="1.2"))
    for y, n in ((y18, "18"), (y20, "20"), (y30, "30")):
        cell(cL, y, n, w=24)
    add(t("t-sm t-mono t-b", cL, 258, "X60004", "middle"))

    add("\n<!-- Module and its plug -->")
    add(rect("keep", stripR[1], 56, mod_x1 - stripR[1], 190))
    add(t("t t-b", stripR[1] + 8, 74, "Leak-test module"))
    add(tm("t-sm", stripR[1] + 8, 90, M("[16137193479], heated")))
    add(rect("keep", stripR[0], 94, stripR[1] - stripR[0], 148, rx=3, sw="1.2"))
    for y, n in ((yS, "4"), (y18, "2"), (y20, "1"), (y30, "3")):
        cell(cR, y, n)
    add(tm("t-sm t-b", cR, 258, M("plug [X1714] (MS43) or [X17141] (MS45.1)"), "middle"))
    # inside: a common +12 V rail from pin 4, one element per pin (the "pump on 30" case)
    rail = 502
    add(line("keep-s", cR + 11, yS, rail, yS, sw="1.5"))
    add(line("keep-s", rail, yS, rail, y30, sw="1.5"))
    add(t("t-sm", (cR + 11 + rail) / 2, yS - 6, "+12 V", "middle"))
    ex0, ex1 = 414, 462
    for y, name in ((y18, "heater"), (y20, "valve"), (y30, "pump")):
        add(line("keep-s", cR + 11, y, ex0, y, sw="1.5"))
        add(rect("shape", ex0, y - 6, ex1 - ex0, 12, rx=1, sw="1.2"))
        add(line("keep-s", ex1, y, rail, y, sw="1.5"))
        if y != y30:
            add(dot("keep-f", rail, y, 2.6))
        add(t("t-sm", (ex0 + ex1) / 2, y - 10, name, "middle"))

    add("\n<!-- The three DME wires -->")
    x0, x1 = stripL[1], stripR[0]
    xm = (x0 + x1) / 2
    add(line("fab-s", cL + 12, y18, cR - 11, y18, sw="2.5"))
    add(tm("t-sm fab-t", xm, y18 - 7, M("[0.75 SW/RT], moved here"), "middle"))
    add(line("keep-s", cL + 12, y20, cR - 11, y20, sw="2"))
    add(tm("t-sm", xm, y20 - 7, M("[0.75 BR/BL]*"), "middle"))
    add(line("keep-s", cL + 12, y30, cR - 11, y30, sw="2"))
    add(tm("t-sm", xm, y30 - 7, M("[0.5 SW/GN]*"), "middle"))
    for y, name in ((y18, "MSS54: heater"), (y20, "MSS54: valve (DMTL)"), (y30, "MSS54: pump (DMTLP)")):
        add(t("t-sm", x0 + 8, y + 16, name))

    # ------------------------------------------------------------------ heater move (below the schematic)
    add("\n<!-- The heater wire's move, and cars built before 09/2001 -->")
    hy = 270
    add(rect("panel", 8, hy, mod_x1 - 8, 112, rx=6, sw="1"))
    add(tm("t t-b", 18, hy + 20, M("Move the heater wire first: [0.75 SW/RT] into [X60004] pin [18]")))
    for x, car, src, note in ((18, "MS43 Touring, built from 09/2001", M("body [X6011] pin [7]"),
                               "then the clutch wire takes X6011 pin 7"),
                              (282, "MS45.1 Touring", M("[X60004] pin [2]"), "pins 2 and 15 are both SW/RT: tag them")):
        add(t("t-sm t-b", x, hy + 39, car))
        r = ref_box(x, hy + 53, src, cls="keep")
        add(line("fab-s", r, hy + 53, r + 22, hy + 53, sw="2", mk="ahf"))
        ref_box(r + 24, hy + 53, M("[X60004] pin [18]"), cls="keep")
        add(t("t-sm", x, hy + 74, note))
    para(18, hy + 94, ["Built before 09/2001: a three-wire module and no heater wire. Fit [16137193479]",
                       "and run a new [0.75] mm² wire from [X60004] pin [18] to module pin [2]."], cls="t-sm new-t")

    # ------------------------------------------------------------------ right column: label and color conflict
    add("\n<!-- The labels and colors disagree: go by the cavity -->")
    rx0, rx1 = 532, 792
    add(rect("warn-f", rx0, 40, rx1 - rx0, 234, rx=6, sw="1.5"))
    add(t("t t-b", rx0 + 10, 58, "Names and colors disagree"))
    c1, c2, c3 = rx0 + 10, rx0 + 136, rx0 + 196
    add(tm("t-sm t-b", c2, 78, M("pin [20]")))
    add(tm("t-sm t-b", c3, 78, M("pin [30]")))
    rows = [("MS43 table", "valve", "pump"), ("MS45.1 table", "pump", "valve"),
            ("MSS54 table", "valve", "pump"), ("Every heated drawing", "module 1", "module 3")]
    for i, (a, b, c) in enumerate(rows):
        y = 96 + 16 * i
        cls = "t-sm t-b" if i == 3 else "t-sm"
        add(t(cls, c1, y, a))
        add(t(cls, c2, y, b))
        add(t(cls, c3, y, c))
    add(line("ln-faint", c1, 152, rx1 - 10, 152))
    para(c1, 170, ["Every heated drawing wires 20 to module",
                   "pin 1 and 30 to pin 3; only the tables'",
                   "names differ.",
                   "* MS45.1 and MSS54 drawings: 20 = BR/BL,",
                   "30 = SW/GN. The US MS43 drawing has them",
                   "the other way round, as did one MS43 car."])
    add(t("t-sm t-b", c1, 262, "Go by the cavity, not color or name."))

    # ------------------------------------------------------------------ right column: after the engine swap
    add("\n<!-- After the engine swap: the MSS54's own checks -->")
    ay = 284
    add(rect("keep", rx0, ay, rx1 - rx0, 100, rx=6, sw="1.5"))
    add(t("t t-b", rx0 + 10, ay + 19, "After the engine swap (MSS54)"))
    para(rx0 + 10, ay + 37, ["[STEUERN_DMTL_HEIZUNG] switches the",
                             "heater. Run [START_SYSTEMCHECK_DMTL],",
                             "then [LESEN_SYSTEMCHECK_DMTL].",
                             "Faults: [14 (0x0E)] heater, [27 (0x1B)]",
                             "valve, [127 (0x7F)] module."])

    # ------------------------------------------------------------------ bottom band: the test
    add("\n<!-- The test that decides pins 20 and 30 -->")
    by = 398
    add(t("t-h", 8, by + 8, "TEST BEFORE YOU SWAP 20 AND 30"))
    top = by + 20
    arrow_y = top + 62

    # step 1: before the Touring's DME comes out
    b1 = (8, 192)
    add(rect("keep", b1[0], top, b1[1] - b1[0], 196, rx=6, sw="1.5"))
    badge(b1[0] + 18, top + 16, "1")
    add(t("t t-b", b1[0] + 32, top + 20.5, "Touring DME still in"))
    para(b1[0] + 9, top + 40, ["Run its leak-test jobs. A test", "lamp at the back of the plug",
                               "shows which X60004 wire", "switches; tag each one. The",
                               "MSS54 has no pump or valve", "job of its own."])
    para(b1[0] + 9, top + 130, ["MS45.1 ([MS450DS0.PRG]):"], cls="t-sm t-b")
    para(b1[0] + 9, top + 144, ["[STEUERN_DMTL_P], [_V], [_H]"])
    para(b1[0] + 9, top + 162, ["MS43 ([MS430DS0.PRG]):"], cls="t-sm t-b")
    para(b1[0] + 9, top + 176, ["[STEUERN_DMTL_MOTOR],", "[_VENTIL], [_HEIZUNG]"])

    # step 2: the triangle, once the heater is in pin 18
    b2 = (208, 428)
    add(line("ln", b1[1], arrow_y, b2[0] - 1, arrow_y, mk="ah"))
    add(rect("keep", b2[0], top, b2[1] - b2[0], 238, rx=6, sw="1.5"))
    badge(b2[0] + 18, top + 16, "2")
    add(t("t t-b", b2[0] + 32, top + 20.5, "Measure the triangle"))
    para(b2[0] + 9, top + 38, ["at X60004, DME unplugged, module in,", "heater in pin 18 (power-up step 9)"])
    tx, ty = (b2[0] + b2[1]) / 2 - 12, top + 72     # apex (pin 18)
    p18, p20, p30 = (tx, ty), (tx - 56, ty + 56), (tx + 56, ty + 56)

    def clip(a, b, hw=13, hh=10):
        """The point where the segment a->b leaves a cell of half-size hw x hh centred on a."""
        dx, dy = b[0] - a[0], b[1] - a[1]
        k = min(hw / abs(dx) if dx else 9e9, hh / abs(dy) if dy else 9e9)
        return a[0] + dx * k, a[1] + dy * k
    for a, b in ((p18, p20), (p18, p30), (p20, p30)):
        (xa, ya), (xb, yb) = clip(a, b), clip(b, a)
        add(line("ln-thin", round(xa, 1), round(ya, 1), round(xb, 1), round(yb, 1), sw="1.5"))
    for (x, y), n in ((p18, "18"), (p20, "20"), (p30, "30")):
        cell(x, y, n, w=24)
    add(t("t-sm t-b", (p18[0] + p20[0]) / 2 - 12, (p18[1] + p20[1]) / 2 + 2, "68 Ω", "end"))
    add(t("t-sm t-b", (p18[0] + p30[0]) / 2 + 12, (p18[1] + p30[1]) / 2 + 2, "52 Ω"))
    add(t("t-sm t-b", tx, p20[1] - 6, "44 Ω", "middle"))
    add(t("t-sm", p18[0] + 18, p18[1] + 4, "heater ≈ 38 Ω"))
    add(t("t-sm", p20[0], p20[1] + 22, "valve ≈ 30 Ω", "middle"))
    add(t("t-sm t-b", p30[0], p30[1] + 22, "pump ≈ 14 Ω", "middle"))
    para(b2[0] + 9, top + 168, ["Each element = (the two readings that",
                                "include its pin, added, minus the",
                                "third) ÷ 2."])
    add(t("t-sm t-b", b2[0] + 9 + W("t-sm", "third) ÷ 2.") + 4, top + 196, "The lowest is the pump."))
    para(b2[0] + 9, top + 214, ["Values from a new Bosch module (E93):", "generic, not BMW limits."])

    # step 3: bench check
    b3 = (444, 596)
    add(line("ln", b2[1], arrow_y, b3[0] - 1, arrow_y, mk="ah"))
    add(rect("keep", b3[0], top, b3[1] - b3[0], 160, rx=6, sw="1.5"))
    badge(b3[0] + 18, top + 16, "3")
    add(t("t t-b", b3[0] + 32, top + 20.5, "Still unsure?"))
    para(b3[0] + 9, top + 40, ["Unplug the module, feed", "+12 V through a fused lead", "to its pin 4, then briefly",
                               "ground pin 1, then pin 3.", "The pump runs on one, the", "valve clicks on the other",
                               "(our inference from the", "drawings)."])

    # decision
    dc = (701, arrow_y)
    hw, hh = 88, 34
    add(t("t-sm", dc[0], top + 12, "The MSS54 wants the pump on 30.", "middle"))
    add(line("ln", b3[1], dc[1], dc[0] - hw - 1, dc[1], mk="ah"))
    add(path("shape", f"M{dc[0] - hw},{dc[1]} L{dc[0]},{dc[1] - hh} L{dc[0] + hw},{dc[1]} L{dc[0]},{dc[1] + hh} Z"))
    add(t("t-sm t-b", dc[0], dc[1] - 3, "Which X60004 pin", "middle"))
    add(t("t-sm t-b", dc[0], dc[1] + 11, "runs the pump?", "middle"))
    fy = dc[1] + hh + 10
    ax, bx = 655, 747
    add(line("ln", dc[0], dc[1] + hh, dc[0], fy))
    add(line("ln", ax, fy, bx, fy))
    oy = fy + 18
    add(line("ln", ax, fy, ax, oy - 1, mk="ah"))
    add(line("ln", bx, fy, bx, oy - 1, mk="ah"))
    add(rect("keep", 610, oy, 90, 40, rx=5, sw="1.5"))
    add(t("t-sm t-b", ax, oy + 16, "Pump on 30", "middle"))
    add(t("t-sm", ax, oy + 32, "change nothing", "middle"))
    add(rect("fab", 702, oy, 90, 40, rx=5, sw="1.5"))
    add(t("t-sm t-b fab-t", 747, oy + 16, "Pump on 20", "middle"))
    add(t("t-sm fab-t", 747, oy + 32, "swap 20 and 30", "middle"))

    H = top + 246
    aria = ("Wiring diagram of the leak-test (DM-TL) module with the M3 DME as BMW draws it, for a Touring and donor "
            "built from 09/2001, showing the pump-on-30 result of the test, and the test that decides pins 20 and 30. "
            "Fuse F3 (20 A, after the DME relay) feeds X6021 pin 2, 1.5 RT/WS, from the M3 harness to splice X11212, "
            "which also feeds the K96 and K19 relay coils, and on by a 0.75 RT/WS wire to module pin 4, +12 V. Inside "
            "the module the heater, valve and pump each run from pin 4 to their own pin. The M3 DME's X60004 pin 18 "
            "takes the 0.75 SW/RT heater wire to module pin 2; this wire is moved first: from body X6011 pin 7 on an "
            "MS43 Touring built from 09/2001, after which the clutch wire takes X6011 pin 7, or from X60004 pin 2 on an "
            "MS45.1, where pins 2 and 15 are both SW/RT and need tags. A Touring built before 09/2001 has a three-wire "
            "module and no heater wire: fit 16137193479 and run a new 0.75 mm2 wire from X60004 pin 18 to module pin 2. "
            "X60004 pin 20 (MSS54 name: valve, DMTL) goes to module pin 1 and pin 30 (pump, DMTLP) to module pin 3. "
            "The MS43 and MSS54 tables call pin 20 the valve and pin 30 the pump, the MS45.1 table the reverse, and "
            "every heated-module drawing wires 20 to module pin 1 and 30 to pin 3. MS45.1 and MSS54 drawings show 20 as "
            "0.75 BR/BL and 30 as 0.5 SW/GN; the US MS43 drawing has the colors the other way round, as did one MS43 "
            "car, so go by the cavity, not the color or the name. After the "
            "engine swap, STEUERN_DMTL_HEIZUNG switches the heater, START_SYSTEMCHECK_DMTL then LESEN_SYSTEMCHECK_DMTL "
            "run the check, and the faults are 14 (0x0E) heater, 27 (0x1B) valve and 127 (0x7F) module. The test "
            "before you swap 20 and 30: first, with the Touring's DME still in, run its leak-test jobs (MS45.1, "
            "MS450DS0.PRG: STEUERN_DMTL_P, _V and _H; MS43, MS430DS0.PRG: STEUERN_DMTL_MOTOR, _VENTIL and _HEIZUNG) "
            "and tag the X60004 wire that switches for each, using a test lamp at the back of the plug; the MSS54 has "
            "no pump or valve job of its own. Second, with the heater in pin 18, DME unplugged and module plugged in "
            "(power-up step 9), measure X60004 pins 18 to 20, 18 to 30 and 20 to 30: each element is the two readings "
            "that include its pin, added, minus the third, divided by two, and the lowest is the pump; a new Bosch "
            "module (E93) read about 68, 52 and 44 ohms, giving heater 38, valve 30 and pump 14 ohms, generic values "
            "rather than BMW limits. Third, if still unsure, bench-check the module with 12 volts through a fused lead "
            "on its pin 4, grounding pin 1 and then pin 3; the pump should run on one and the valve click on the other, "
            "the manual's inference from the drawings. The MSS54 wants the pump on 30: pump on 30, change nothing; "
            "pump on 20, swap 20 and 30.")
    mk = [marker("ahf", "fab-f"), marker("ahk", "keep-f")]
    return svg_open(WIDTH, H, aria, mk) + "\n".join(o for o in out if o) + "\n</svg>"


if __name__ == "__main__":
    svg = build()
    if measure_missing():
        svg = build()
    print(write("19-circuit-dmtl.svg", svg))
