#!/usr/bin/env python3
"""Figure: the three warning lamps and the start feedback after the swap, with 'before' strips.
Data: wiring-canonical.md §6.3 (and §2 MS43 moves 3-6, MS45.1 moves 7-10); WIRING-AND-CODING.md "Cluster wiring"."""
from kit import Doc, svg_open, write, width, flush_measurements
from parts import pin, splice, box, swatch_line, swatch_box

W, H = 800, 612
NAME = "22-circuit-lamps.svg"

ARIA = ("Wiring diagram of the three warning lamps and the start feedback after the swap, the M3 way: each sensor "
        "feeds the DME and the DME drives the cluster on plug X11175. Oil-pressure switch, closed below about 0.5 bar, "
        "to DME X60003 pin 26; DME X60004 pin 11, 0.35 BR/GN, to cluster pin 13; cluster coding CAN_OELDRUCKSCHALTER = "
        "nicht_aktiv. Alternator terminal 61 to X60003 pin 13; X60004 pin 1, 0.35 BL, to cluster pin 2: the cluster "
        "powers the lamp and the DME grounds it when not charging; GENERATOR_UEBER_CAN = nicht_aktiv. With a donor built "
        "from 03/2004, which WDS draws without X60004 pins 1 and 2, code it aktiv if the charge lamp stays dark at key-on. "
        "Oil-level sensor, a pulse-width signal, to X60003 pin 39; X60004 pin 21, 0.5 WS/GN, to cluster pin 17; "
        "TOG_UEBER_CAN = nicht_aktiv. Starter to X60003 pin 12; X60004 pin 2, 0.35 SW/GN, through splice X276 to "
        "cluster pin 3 and the E-box fan plug, if fitted. Cluster pin 14 is the K-bus, not the oil-pressure lamp; Kassel's chart "
        "is wrong there. Key on, engine off, the red oil-pressure, charge and check-engine lamps are lit, and oil and "
        "charge go out within seconds of the start. Before the swap an MS43 Touring ran these four wires from body "
        "X6011 pins 3, 4, 5 and 6 straight to the cluster, past the DME: you move them into X60004 pins 11, 1, 21 and 2. "
        "An MS45.1 Touring sent the lamps over CAN: you add the three lamp wires new, and move the start feedback from "
        "X6011 pin 6 to X60004 pin 2 only if pin 6 holds a wire, after the heater wire has left pin 2.")

ROWS = [  # sensor lines, X60003 pin, X60004 pin, wire, X11175 pin, lamp, coding switch
    (("Oil-pressure switch", "closed below about", "0.5 bar"), 26, 11, "0.35 BR/GN", 13, "Oil-pressure lamp (red)", "CAN_OELDRUCKSCHALTER"),
    (("Alternator", "terminal 61"), 13, 1, "0.35 BL", 2, "Charge lamp", "GENERATOR_UEBER_CAN"),
    (("Oil-level sensor", "pulse-width signal"), 39, 21, "0.5 WS/GN", 17, "Oil-level lamp (yellow)", "TOG_UEBER_CAN"),
    (("Starter",), 12, 2, "0.35 SW/GN", 3, "Start feedback (terminal 30h)", None),
]


def build() -> str:
    d = Doc()
    d.comment("Key")
    x = 8
    x = swatch_box(d, x, 17, "donor", "From donor M3") + 18
    x = swatch_box(d, x, 17, "keep", "Keep") + 18
    x = swatch_line(d, x, 17, "ln", "Your lamp wire, after the swap", sw=2) + 18
    x = swatch_line(d, x, 17, "fab-s", "Moved wire", sw=2) + 18
    x = swatch_line(d, x, 17, "new-s", "New wire", sw=2) + 18

    d.text("t-h", 8, 48, "AFTER THE SWAP: SENSOR → DME → CLUSTER")

    # columns
    SX0, SX1 = 8, 150          # sensor boxes
    C3 = 189                   # X60003 cells (on the DME's left edge)
    DX0, DX1 = 202, 296        # DME box
    C4 = 309                   # X60004 cells (on the DME's right edge)
    CK = 497                   # X11175 cells
    KX0, KX1 = 510, 792        # cluster box
    rows_y = [100, 168, 236, 304]
    TOP, BOT = 78, 326

    d.text("t-sm t-b", C3, 72, "X60003", anchor="middle")
    d.text("t-sm t-b", C4, 72, "X60004", anchor="middle")
    d.text("t-sm t-b", CK, 72, "X11175", anchor="middle")

    d.comment("DME")
    d.rect("donor", DX0, TOP, DX1 - DX0, BOT - TOP, rx=5, sw=1.5)
    cx = (DX0 + DX1) / 2
    for i, (cls, s) in enumerate((("t t-b", "DME"), ("t-sm", "MSS54 or"), ("t-sm", "MSS54HP,"), ("t-sm", "the M3's"))):
        d.text(cls, cx, 186 + i * 15, s, anchor="middle")

    d.comment("Cluster")
    d.rect("donor", KX0, TOP, KX1 - KX0, BOT - TOP, rx=5, sw=1.5)
    d.text("t t-b", 784, 96, "M3 cluster", anchor="end")

    for (slines, p3, p4, wire, pk, lamp, code), y in zip(ROWS, rows_y):
        d.comment(lamp)
        h = 18 + 15 * len(slines)
        box(d, "donor", SX0, y - h / 2, SX1 - SX0, h,
            [("t t-b", slines[0])] + [("t-sm", s) for s in slines[1:]], pad=8, first_dy=17, lh=15)
        d.line("donor-s", SX1, y, C3 - 13.5, y, sw=1.5)
        pin(d, C3, y, p3, cls="donor")
        pin(d, C4, y, p4, cls="keep")
        pin(d, CK, y, pk, cls="keep")
        d.text("t t-b", KX0 + 10, y - 3, lamp)
        if code:
            d.rich("t-sm t-mono", KX0 + 10, y + 13, [(None, code + " = "), ("t-b", "nicht_aktiv")])
            width("t-sm t-mono", code + " = nicht_aktiv")
        else:
            d.text("t-sm", KX0 + 10, y + 13, "no coding switch")
        if p4 == 1:
            d.rich("t-sm", KX0 + 10, y + 29, [("t-b", "Donor from 03/2004"), (None, " (WDS: no X60004")])
            d.rich("t-sm", KX0 + 10, y + 43, [(None, "pins 1, 2): lamp dark at key-on? Code it "), ("t-mono", "aktiv"), (None, ".")])
        if p4 != 2:
            d.line("ln", C4 + 13.5, y, CK - 13.5, y, sw=2)
            d.text("t-sm t-mono", (C4 + CK) / 2, y - 6, wire, anchor="middle")

    d.comment("Start feedback through splice X276 to cluster pin 3 and the E-box fan plug")
    y = rows_y[3]
    xs = 420
    d.line("ln", C4 + 13.5, y, xs, y, sw=2)
    d.line("keep-s", xs, y, CK - 13.5, y, sw=1.5)
    d.line("keep-s", xs, y, xs, 336, sw=1.5)
    splice(d, xs, y, cls="fill-fg")
    d.text("t-sm t-mono", (C4 + 13.5 + xs) / 2, y - 6, "0.35 SW/GN", anchor="middle")
    d.text("t-sm", xs - 7, y + 17, "splice X276", anchor="end")
    box(d, "keep", xs - 70, 336, 140, 24, [("t-sm", "E-box fan plug (if fitted)")], pad=9, first_dy=16)

    d.comment("Charge lamp: lit by the cluster, grounded by the DME")
    d.text("t-sm", (C4 + CK) / 2, rows_y[1] + 16, "the cluster powers it;", anchor="middle")
    d.text("t-sm", (C4 + CK) / 2, rows_y[1] + 30, "the DME grounds it", anchor="middle")
    d.text("t-sm", (C4 + CK) / 2, rows_y[1] + 44, "when not charging", anchor="middle")

    d.comment("Pin 14 is the K-bus")
    pin(d, CK, rows_y[0] + 17, 14, cls="crit-s", txt_cls="t t-mono crit-t")
    d.text("t-sm crit-t", 478, rows_y[0] + 21, "not 14: that's the K-bus", anchor="end")
    d.text("t-sm crit-t", 478, rows_y[0] + 35, "(Kassel's chart is wrong)", anchor="end")

    d.comment("Key-on expectation")
    d.rect("panel", KX0, 334, KX1 - KX0, 50, rx=5)
    d.rich("t-sm", KX0 + 10, 351, [("t-b", "Key on, engine off:"), (None, " the red oil-pressure, charge")])
    d.text("t-sm", KX0 + 10, 365, "and check-engine lamps are lit. Oil and charge")
    d.text("t-sm", KX0 + 10, 379, "go out within seconds of the start.")
    width("t-sm", "Key on, engine off: the red oil-pressure, charge")

    # ------------------------------------------------------------------ before strips
    y0 = 396
    d.line("ln-faint", 8, y0, 792, y0)

    d.comment("Before: MS43 Touring, X6011 straight to the cluster")
    d.text("t-h", 8, y0 + 26, "BEFORE: MS43 TOURING")
    d.text("t-sm", 8, y0 + 44, "Body X6011 fed the cluster directly, past the DME.")
    rows = [(3, "0.35 BR/GN", "13", 11), (4, "0.35 BL", "2", 1), (5, "0.5 WS/GN", "17", 21), (6, "0.35 SW/GN", "3", 2)]
    ry = [y0 + 72 + i * 23 for i in range(4)]
    CX, CC = 150, 316          # X6011 cells, cluster cells
    d.text("t-sm t-b", CX, y0 + 57, "X6011", anchor="middle")
    d.text("t-sm t-b", CC, y0 + 57, "cluster", anchor="middle")
    for (p6, wire, dest, to), y in zip(rows, ry):
        d.rich("t-sm fab-t", CX - 20, y + 4, [(None, "move to X60004 "), ("t-b", str(to))], anchor="end")
        width("t-sm fab-t", "move to X60004 " + str(to))
        pin(d, CX, y, p6, cls="keep")
        if p6 == 6:
            d.line("fab-s", CX + 13.5, y, 282, y, sw=2)
            splice(d, 282, y, cls="keep-f")
            d.line("keep-s", 282, y, CC - 13.5, y, sw=1.5)
            d.text("t-sm", 282, y + 16, "X276", anchor="middle")
        else:
            d.line("fab-s", CX + 13.5, y, CC - 13.5, y, sw=2)
        d.text("t-sm t-mono", CX + 24, y - 5, wire)
        pin(d, CC, y, dest, cls="keep")

    d.text("t-sm", 8, ry[3] + 40, "Each moved wire gets a new X60004-type terminal, or a repair lead.")

    d.comment("Before: MS45.1 Touring, lamps over CAN")
    x0 = 412
    d.line("ln-faint", x0 - 12, y0 + 10, x0 - 12, H - 8)
    d.text("t-h", x0, y0 + 26, "BEFORE: MS45.1 TOURING")
    d.text("t-sm", x0, y0 + 44, "The MS45.1 read the sensors and sent the lamps over CAN.")
    box(d, "shape", x0, y0 + 56, 96, 30, [("t-sm", "MS45.1 DME")], pad=10, first_dy=19.5)
    box(d, "shape", x0 + 280, y0 + 56, 100, 30, [("t-sm", "cluster")], pad=10, first_dy=19.5)
    d.line("keep-s", x0 + 96, y0 + 71, x0 + 280, y0 + 71, sw=3)
    d.text("t-sm t-b", x0 + 188, y0 + 65, "lamps over CAN", anchor="middle")
    d.text("t-sm", x0 + 380, y0 + 100, "lamp pins 2, 13, 17 (may be empty)", anchor="end")
    adds = [(11, 13, "0.35 BR/GN"), (1, 2, "0.35 BL"), (21, 17, "0.5 WS/GN")]
    for i, (a, b, wire) in enumerate(adds):
        y = y0 + 122 + i * 18
        d.line("new-s", x0, y - 4, x0 + 16, y - 4, sw=2)
        d.rich("t-sm new-t", x0 + 22, y, [(None, "add "), ("t-b", f"X60004 {a} → cluster {b}"), (None, f", new {wire}")])
        width("t-sm new-t", f"add X60004 {a} → cluster {b}, new {wire}")
    y = y0 + 122 + 3 * 18
    d.line("fab-s", x0, y - 4, x0 + 16, y - 4, sw=2)
    d.rich("t-sm fab-t", x0 + 22, y, [(None, "move "), ("t-b", "X6011 6 → X60004 2"), (None, " only if pin 6 holds a wire,")])
    width("t-sm fab-t", "move X6011 6 → X60004 2 only if pin 6 holds a wire,")
    d.text("t-sm fab-t", x0 + 22, y + 14, "after the heater wire has left pin 2")

    return d.body()


def main():
    for _ in range(3):
        body = build()
        if not flush_measurements():
            break
    head = svg_open(W, H, ARIA, markers=("ah",))
    p = write(NAME, head, body)
    print("wrote", p)


if __name__ == "__main__":
    main()
