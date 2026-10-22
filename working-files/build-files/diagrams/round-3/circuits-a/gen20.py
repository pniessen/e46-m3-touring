#!/usr/bin/env python3
"""Figure: Sport button, its LED and the switch center's feeds (optional circuit).
Data: wiring-canonical.md §6.5; WIRING-AND-CODING.md "Sport button and switch center"."""
from kit import Doc, svg_open, write, width, flush_measurements
from parts import pin, ground, splice, box, swatch_line, swatch_box

W, H = 800, 636
NAME = "20-circuit-sport.svg"

ARIA = ("Wiring diagram of the optional Sport button circuit. The M3's switch center (61316925520 coupe, 61316925521 "
        "convertible; your 325i's is 61316925498) takes a new plug, X1869. Pin 17 runs a new 0.35 SW/RT/GE wire to DME "
        "plug X60004 pin 15, the Sport input, which the button grounds when pressed; status STAT_FDYN_EIN. The DME drives "
        "the LED from X60004 pin 16 over a new 0.35 SW/GR/GE wire to X1869 pin 18; without it the DME stores fault 110 "
        "(0x6E). The switch center also needs three feeds a base Touring lacks: pin 7, terminal 30, 4.0 RT/VI from fuse "
        "F42 (30 A); pin 22, terminal R from fuse F12, wire and rating not given; and pin 23, the K-bus, 0.35 WS/RT/GE to "
        "any K-bus point. Your existing DSC-button plug X521 plugs in as it is: pin 1 terminal 15 from F33 (5 A, 0.5 "
        "GN/BL/GE), pin 2 the DSC-off button to the DSC unit's MK60 pin 39, pin 3 panel lighting 58g (0.5 GR/RT) from "
        "the light module, pin 4 ground. Nobody has confirmed the M3 unit's fit in a Touring console. On an MS45.1 the "
        "secondary-air sensor wire (0.5 SW/RT) comes out of X60004 pin 15 on every swap, Sport or not; it is not the "
        "0.75 SW/RT wire in pin 2, so tag both. The tire-pressure reset on pin 2 would go to DSC unit pin 40, needs DSC "
        "and cluster coding and is unproven in a Touring.")


def build() -> str:
    d = Doc()
    d.comment("Key")
    x = 8
    x = swatch_box(d, x, 17, "donor", "From donor M3") + 18
    x = swatch_box(d, x, 17, "keep", "Keep") + 18
    x = swatch_box(d, x, 17, "new", "New wire or plug") + 18
    d.text("t-sm fab-t t-b", x, 17, "Orange text: an MS45.1 step")

    d.text("t-h", 8, 48, "SPORT BUTTON AND SWITCH CENTER: OPTIONAL")
    d.text("t-sm", 8, 66, "The button switches the DME's throttle map. Skip the circuit and the DME stores fault 110 (0x6E), with no warning lamp.")

    LX1 = 176            # right edge of the left-hand boxes
    CL = 318             # X1869 / X521 cells on the switch center's left edge
    SX0, SX1 = 331, 505  # switch center
    CR = 518             # X1869 cells on its right edge
    C4 = 662             # X60004 cells on the DME's left edge
    DX0, DX1 = 675, 792  # DME
    TOP, BOT = 84, 470

    # ------------------------------------------------------------------ switch center
    d.comment("M3 switch center")
    d.rect("donor", SX0, TOP, SX1 - SX0, BOT - TOP, rx=5, sw=1.5)
    for i, (c, s) in enumerate((("t t-b", "M3 switch center"), ("t-sm", "61316925520 coupe,"),
                                ("t-sm", "61316925521 convertible"), ("t-sm", "(your 325i's: 61316925498)"),
                                ("t-sm", "fit in a Touring console"), ("t-sm", "unconfirmed"))):
        d.text(c, SX0 + 12, TOP + 20 + i * 15, s)
    d.line("ln-faint", SX0 + 1, TOP + 104, SX1 - 1, TOP + 104)

    # ------------------------------------------------------------------ new feeds (left, top)
    d.comment("Feeds a base Touring lacks: new X1869 pins 7, 22, 23")
    d.text("t-sm t-b new-t", 8, 180, "NEW: feeds a base Touring lacks")
    feeds = [
        (210, 7, "4.0 RT/VI", [("t", "Fuse F42, 30 A"), ("t-sm", "terminal 30")]),
        (254, 22, "wire not given", [("t", "Fuse F12"), ("t-sm", "terminal R; rating not given")]),
        (298, 23, "0.35 WS/RT/GE", [("t", "K-bus, any point"), ("t-sm", "such as cluster pin 14's wire")]),
    ]
    for y, p, wire, lines in feeds:
        box(d, "keep", 8, y - 18, LX1 - 8, 36, lines, pad=8, first_dy=15, lh=15)
        d.line("new-s", LX1, y, CL - 13.5, y, sw=2)
        if p == 23:
            splice(d, LX1, y, cls="new-f")
        pin(d, CL, y, p, cls="new")
        d.text("t-sm t-mono", (LX1 + CL - 13.5) / 2, y - 6, wire, anchor="middle")
    d.text("t-sm t-b", SX0 + 8, 214, "X1869")
    d.text("t-sm", SX0 + 8, 228, "new plug")

    # ------------------------------------------------------------------ X521 (already there)
    d.comment("X521: your DSC-button plug, already there")
    d.text("t-sm t-b", 8, 332, "ALREADY THERE: your DSC-button plug")
    x521 = [
        (352, 1, "0.5 GN/BL/GE", [("t", "Fuse F33, 5 A"), ("t-sm", "terminal 15")]),
        (386, 2, "blue/violet (TIS)", [("t", "DSC unit"), ("t-sm", "MK60 pin 39: DSC off")]),
        (420, 3, "0.5 GR/RT", [("t", "Light module"), ("t-sm", "panel lighting 58g")]),
    ]
    for y, p, wire, lines in x521:
        box(d, "keep", 8, y - 15.5, LX1 - 8, 31, lines, pad=8, first_dy=13.5, lh=13.5)
        d.line("keep-s", LX1, y, CL - 13.5, y, sw=1.5)
        pin(d, CL, y, p, cls="keep")
        d.text("t-sm t-mono", (LX1 + CL - 13.5) / 2, y - 5, wire, anchor="middle")
    y = 452
    d.line("keep-s", 150, y, CL - 13.5, y, sw=1.5)
    pin(d, CL, y, 4, cls="keep")
    d.line("keep-s", 150, y, 150, y + 4, sw=1.5)
    ground(d, 150, y + 4)
    d.text("t", 136, y + 4, "ground", anchor="end")
    d.text("t-sm t-mono", (150 + CL - 13.5) / 2, y - 5, "0.75 BR or 0.5 BR/SW", anchor="middle")
    d.text("t-sm t-b", SX0 + 8, 356, "X521")
    d.text("t-sm", SX0 + 8, 370, "plugs in as it is")

    # ------------------------------------------------------------------ Sport button and LED to the DME
    d.comment("Sport input X1869 17 to X60004 15; LED X60004 16 to X1869 18")
    yS, yL = 226, 290
    pin(d, CR, yS, 17, cls="new")
    pin(d, CR, yL, 18, cls="new")
    pin(d, C4, yS, 15, cls="keep")
    pin(d, C4, yL, 16, cls="keep")
    d.line("new-s", CR + 13.5, yS, C4 - 13.5, yS, sw=2, end="ahn")
    d.line("new-s", C4 - 13.5, yL, CR + 13.5, yL, sw=2, end="ahn")
    # labels sit clear of the arrowheads (about 13 px long at this stroke width)
    d.text("t-sm t-mono", 583, yS - 6, "0.35 SW/RT/GE", anchor="middle")
    d.text("t-sm t-mono", 597, yL - 6, "0.35 SW/GR/GE", anchor="middle")
    d.text("t-sm", 583, yS + 19, "pressed, the button", anchor="middle")
    d.text("t-sm", 583, yS + 33, "grounds the input", anchor="middle")
    d.text("t-sm t-b", SX1 - 8, yS - 22, "X1869 (same plug)", anchor="end")
    d.text("t", SX1 - 8, yS + 4, "Sport button", anchor="end")
    d.text("t", SX1 - 8, yL + 4, "Sport LED", anchor="end")

    d.comment("DME")
    d.rect("donor", DX0, TOP, DX1 - DX0, 254, rx=5, sw=1.5)
    d.text("t t-b", DX0 + 9, TOP + 20, "DME, the M3's")
    d.text("t-sm", DX0 + 9, TOP + 35, "MSS54 or MSS54HP")
    d.text("t-sm t-b", DX0 + 9, yS - 22, "X60004")
    d.text("t-sm", DX0 + 9, yS + 4, "Sport in")
    d.text("t-sm t-mono", DX0 + 9, yS + 22, "STAT_FDYN_EIN")
    d.text("t-sm", DX0 + 9, yS + 36, "follows the button")
    d.text("t-sm", DX0 + 9, yL + 4, "LED out")
    d.text("t-sm", DX0 + 9, yL + 22, "no LED wire:")
    d.text("t-sm crit-t", DX0 + 9, yL + 36, "fault 110 (0x6E)")

    d.comment("MS45.1: the secondary-air sensor wire leaves pin 15 on every swap")
    d.rect("fab", 520, 352, 272, 72, rx=4, sw=1.5)
    d.text("t-sm t-b fab-t", 530, 369, "MS45.1, every swap, Sport or not:")
    d.text("t-sm", 530, 384, "the secondary-air sensor wire (0.5 SW/RT)")
    d.text("t-sm", 530, 399, "comes out of X60004 pin 15; insulate it.")
    d.text("t-sm", 530, 414, "It's not the 0.75 SW/RT wire in pin 2: tag both.")

    # ------------------------------------------------------------------ notes
    d.comment("Notes")
    y0 = 482
    d.rect("warn-f", 8, y0, 784, 36, rx=4)
    d.rich("t-sm", 18, y0 + 15, [("t-b", "Wire pins 7, 22 and 23 too:"),
                                 (None, " without 7 the switch center logs “terminal 30 missing”; without 22 nothing on the")])
    width("t-sm", "Wire pins 7, 22 and 23 too: without 7 the switch center logs “terminal 30 missing”; without 22 nothing on the")
    d.text("t-sm", 18, y0 + 29, "panel works, the DSC button included. Check that F42 and F12 are wired on their load side: unused positions often aren't.")

    y1 = y0 + 46
    d.rect("panel", 8, y1, 452, 100, rx=6)
    d.text("t-sm t-b", 18, y1 + 17, "Test")
    d.rich("t-sm", 18, y1 + 33, [("t-mono", "SZM46.PRG"), (None, " → "), ("t-mono", "STATUS_IO"), (None, ": terminals R, 15 and 50 on, terminal-30 voltage present.")])
    d.rich("t-sm", 18, y1 + 48, [("t-mono", "MSS54DS0.PRG"), (None, " → "), ("t-mono", "STATUS_DIGITAL"), (None, ": "), ("t-mono", "STAT_FDYN_EIN"), (None, " changes when you")])
    d.text("t-sm", 18, y1 + 62, "press the button, and the LED follows. Meter, at power-up step 8 (battery")
    d.text("t-sm", 18, y1 + 76, "disconnected, DME unplugged, switch unit in): X60004 pin 15 to ground is")
    d.text("t-sm", 18, y1 + 90, "open with the button released, near 0 Ω pressed.")

    d.rect("panel", 470, y1, 322, 100, rx=6)
    d.text("t-sm t-b", 480, y1 + 17, "Leave out unless fitted")
    d.text("t-sm", 480, y1 + 33, "X1869 pins 1, 13, 20, 21: seat heating; pins")
    d.text("t-sm", 480, y1 + 47, "14, 15, 19: sunshade and HiFi.")
    d.text("t-sm", 480, y1 + 62, "Optional: pin 2, tire-pressure reset (0.5 GE/SW),")
    d.text("t-sm", 480, y1 + 76, "to DSC unit pin 40; needs DSC and cluster coding;")
    d.text("t-sm", 480, y1 + 90, "unproven in a Touring.")

    return d.body()


def main():
    for _ in range(3):
        body = build()
        if not flush_measurements():
            break
    head = svg_open(W, H, ARIA, markers=("ah", "ahn"))
    p = write(NAME, head, body)
    print("wrote", p)


if __name__ == "__main__":
    main()
