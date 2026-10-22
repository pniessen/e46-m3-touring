#!/usr/bin/env python3
"""Figure: brake-light switch (two contacts) and clutch chain, after the swap.
Data: wiring-canonical.md §6.1, §6.2; WIRING-AND-CODING.md "Brake-light switch",
"Clutch switch, gear switch and cruise"."""
import sys
from kit import Doc, svg_open, write, width, flush_measurements
from parts import pin, ground, splice, box, swatch_line, swatch_box

W, H = 800, 640
NAME = "21-circuit-brake-clutch.svg"

ARIA = ("Wiring diagram of the brake-light switch and the clutch chain after the swap. "
        "Brake: fuse F9 (5 A, terminal R) feeds switch S29 on plug X78 pin 1 (0.5 VI/GE); pin 2 grounds "
        "at X217 (0.35 BR/SW); the first contact, pin 4, runs 0.35 BL/RT through splice X181 to the light module "
        "and DME plug X60004 pin 24, unchanged; the test contact, pin 3, runs 0.35 BR/GR through splice X1179 and "
        "moves from X60004 pin 28 to pin 34. Clutch: F9 feeds the M3's clutch module 61319122700 on plug X13635 pin 3 "
        "(0.5 VI/GE); pin 1 grounds at X217; pin 4 keeps its 0.35 BL/SW wire to EWS X1659 pin 8, the start interlock, "
        "high with the pedal down; pin 2's 0.35 BL/BR wire moves out of X60004 pin 23 into body X6011 pin 7, where the "
        "M3 engine harness carries it as 0.5 GR to X6053 pin 5 and the gear switch 23142229113 on the 420G, then 0.5 "
        "GR/BL to DME X60002 pin 20. The Touring's module 61319231129 does not work in this chain. Both parts are "
        "electronic, so a meter proves only the wires: STATUS_DIGITAL proves the parts, and EWS3.PRG STATUS_LESEN the "
        "clutch module's signal to the EWS (clutch down, STAT_P_N_EINGANG changes and STAT_ANLASSER_AUS_P_N reads 0). "
        "Test with the key on and the engine off. Brake: STAT_BLS_EIN and STAT_BLTS_EIN must both change with the pedal; "
        "if only one changes the DME stores fault 106 (0x6A) and cruise is off. Clutch, parking brake on: the chain is "
        "high only with the pedal up and a gear in, when STAT_KRAFTSCHLUSS_EIN reads 1 and STAT_KUP_EIN 0; pedal down in "
        "gear, or neutral with either pedal position, reads 0 and 1. A Touring built before 03/2001 (clutch switch S32) "
        "or an SMG donor (no gear-switch wire at X60002 pin 20) needs the text.")


def build() -> str:
    d = Doc()
    # ------------------------------------------------------------------ key
    d.comment("Key")
    x = 8
    x = swatch_box(d, x, 17, "donor", "From donor M3") + 18
    x = swatch_box(d, x, 17, "keep", "Keep") + 18
    x = swatch_line(d, x, 17, "fab-s", "Moved wire", sw=2) + 18
    x = swatch_line(d, x, 17, "fab-s", "Where it was", sw=1.5, dashed=True) + 18

    # ------------------------------------------------------------------ titles, divider
    d.text("t-h", 8, 48, "BRAKE-LIGHT SWITCH: TWO CONTACTS")
    d.text("t-h", 364, 48, "CLUTCH CHAIN: MODULE AND GEAR SWITCH")
    d.line("ln-faint", 352, 34, 352, 392)

    # ================================================================== BRAKE
    d.comment("Brake: fuse F9 to X78 pin 1")
    box(d, "keep", 20, 58, 172, 24, [("t", "Fuse F9, 5 A (terminal R)")], first_dy=16.5)
    d.line("keep-s", 56, 82, 56, 105, sw=1.5)
    d.text("t-sm t-mono", 62, 99, "0.5 VI/GE")
    pin(d, 56, 113.5, 1, cls="keep")
    d.text("t-sm t-b", 75, 116.5, "X78")

    d.comment("Brake-light switch S29")
    box(d, "keep", 20, 122, 236, 60, [
        ("t t-b", "Brake-light switch S29"),
        ("t-sm", "61316967601, same on both cars"),
        ("t-sm", "electronic: sends B+ when braking")], first_dy=19)
    for px, n in ((44, 2), (130, 4), (222, 3)):
        pin(d, px, 190.5, n, cls="keep")

    d.comment("Pin 2: ground X217")
    d.line("keep-s", 44, 199.5, 44, 222, sw=1.5)
    ground(d, 44, 222)
    d.text("t-sm t-mono", 50, 214, "0.35 BR/SW")
    d.text("t-sm", 58, 233, "X217")

    d.comment("Pin 4: first contact through splice X181 to the light module and X60004 pin 24 (unchanged)")
    d.line("keep-s", 130, 199.5, 130, 388, sw=1.5)
    d.line("keep-s", 130, 272, 106, 272, sw=1.5)
    splice(d, 130, 272)
    box(d, "keep", 10, 259, 96, 26, [("t", "Light module")], first_dy=17.5, pad=8)
    d.text("t-sm t-mono", 136, 218, "0.35 BL/RT")
    d.text("t-sm", 136, 233, "first contact")
    d.text("t-sm", 138, 276, "splice X181")

    d.comment("Pin 3: test contact through splice X1179, moved from X60004 pin 28 to 34")
    d.line("fab-s", 222, 199.5, 222, 388, sw=2)
    splice(d, 222, 300, cls="fab-f")
    d.text("t-sm t-mono fab-t", 228, 218, "0.35 BR/GR")
    d.text("t-sm", 228, 233, "test contact")
    d.text("t-sm", 230, 304, "splice X1179")
    d.path("fab-s dash", "M222,334 H176 V388", sw=1.5)
    d.text("t-sm fab-t", 230, 338, "was in pin 28")
    d.text("t-sm fab-t t-b", 230, 376, "moved to 34")

    d.comment("DSC reads the switch too")
    d.text("t-sm", 266, 140, "The DSC unit")
    d.text("t-sm", 266, 155, "reads it too")
    d.text("t-sm", 266, 170, "(MK60 pin 41)")

    # ================================================================== CLUTCH
    d.comment("Clutch: fuse F9 to X13635 pin 3")
    box(d, "keep", 376, 58, 172, 24, [("t", "Fuse F9, 5 A (terminal R)")], first_dy=16.5)
    d.text("t-sm", 556, 74.5, "same fuse as the brake switch")
    d.line("keep-s", 404, 82, 404, 105, sw=1.5)
    d.text("t-sm t-mono", 410, 99, "0.5 VI/GE")
    pin(d, 404, 113.5, 3, cls="keep")
    d.text("t-sm t-b", 423, 116.5, "X13635")

    d.comment("M3 clutch module")
    box(d, "donor", 376, 122, 180, 74, [
        ("t t-b", "M3 clutch module"),
        ("t-sm t-b donor-t", "61319122700: required"),
        ("t-sm crit-t", "not the Touring's 61319231129"),
        ("t-sm", "electronic (Hall-effect)")], first_dy=19, lh=16)

    d.comment("Pin 4: start interlock to EWS X1659 pin 8 (keep)")
    pin(d, 569, 140, 4, cls="keep")
    d.line("keep-s", 582.5, 140, 663.5, 140, sw=1.5)
    pin(d, 677, 140, 8, cls="keep")
    box(d, "keep", 690, 122, 102, 56, [
        ("t t-b", "EWS X1659"),
        ("t-sm", "start interlock:"),
        ("t-sm", "keep it")], first_dy=19, lh=15)
    d.text("t-sm t-mono", 589, 134, "0.35 BL/SW")
    d.text("t-sm", 589, 163, "high, pedal down")

    d.comment("Pin 1: ground X217")
    pin(d, 396, 204.5, 1, cls="keep")
    d.line("keep-s", 396, 213.5, 396, 236, sw=1.5)
    ground(d, 396, 236)
    d.text("t-sm t-mono", 402, 228, "0.35 BR/SW")
    d.text("t-sm", 410, 247, "X217")

    d.comment("Pin 2: chain wire, moved from X60004 pin 23 into body X6011 pin 7")
    pin(d, 484, 204.5, 2, cls="keep")
    d.path("fab-s", "M484,213.5 V294 H498.5", sw=2)
    d.text("t-sm t-mono fab-t", 490, 229, "0.35 BL/BR")
    d.text("t-sm fab-t", 490, 244, "out of X60004 23")
    d.text("t-sm", 490, 259, "+12 V with the pedal up")

    d.comment("X6011 pin 7: body half (yours) and engine half (M3)")
    pin(d, 512, 294, 7, cls="keep")
    pin(d, 538, 294, 7, cls="donor")
    d.text("t-sm t-b", 525, 279, "X6011", anchor="middle")
    d.text("t-sm", 512, 317, "body", anchor="middle")
    d.text("t-sm donor-t", 538, 317, "M3", anchor="middle")

    d.comment("M3 engine harness 0.5 GR to X6053 pin 5")
    d.line("donor-s", 551.5, 294, 602.5, 294, sw=1.5)
    d.text("t-sm t-mono", 557, 288, "0.5 GR")
    pin(d, 616, 294, 5, cls="donor")
    pin(d, 642, 294, 5, cls="donor")
    d.text("t-sm t-b", 629, 279, "X6053", anchor="middle")
    d.text("t-sm donor-t", 629, 317, "both M3", anchor="middle")

    d.comment("Gear switch on the 420G")
    d.line("donor-s", 655.5, 294, 663.5, 294, sw=1.5)
    pin(d, 677, 294, 1, cls="donor")
    box(d, "donor", 690, 256, 102, 86, [
        ("t t-b", "Gear switch"),
        ("t-sm", "23142229113"),
        ("t-sm", "on the 420G"),
        ("t-sm", "closed in gear,"),
        ("t-sm", "open in neutral")], first_dy=18, lh=15)
    pin(d, 760, 350.5, 2, cls="donor")
    d.line("donor-s", 760, 359.5, 760, 388, sw=1.5)
    d.text("t-sm t-mono", 752, 382, "0.5 GR/BL", anchor="end")

    d.comment("X6011 pin 7 must be clear first")
    d.rect("warn-f", 364, 325, 262, 76, rx=4)
    d.text("t-sm t-b", 372, 340, "First clear X6011 pin 7:")
    d.text("t-sm", 372, 353.5, "MS43 from 09/2001: move the heater wire")
    d.text("t-sm", 372, 367, "(0.75 SW/RT) to X60004 18 first")
    d.text("t-sm", 372, 380.5, "MS45.1 and earlier MS43: pin 7 is empty")
    d.text("t-sm", 372, 394, "Both: fit a new X6011-type terminal")

    # ================================================================== DME
    d.comment("DME and its plugs")
    d.rect("donor", 8, 406, 784, 28, rx=5, sw=1.5)
    d.text("t t-b", 470, 424.5, "DME: MSS54 or MSS54HP, the M3's", anchor="middle")
    d.text("t-sm t-b", 76, 401, "X60004", anchor="end")
    pin(d, 94, 397, 23, cls="keep", dashed=True)
    pin(d, 130, 397, 24, cls="keep")
    pin(d, 176, 397, 28, cls="keep", dashed=True)
    pin(d, 222, 397, 34, cls="keep")
    d.text("t-sm fab-t", 108, 362, "23: clutch wire", anchor="end")
    d.text("t-sm fab-t", 108, 376, "moved to X6011", anchor="end")
    d.text("t-sm t-b", 741, 401, "X60002", anchor="end")
    pin(d, 760, 397, 20, cls="donor")

    # ================================================================== electronic note
    d.comment("Electronic parts: meter proves wires, status bits prove parts")
    d.rect("warn-f", 8, 442, 784, 38, rx=4)
    d.rich("t-sm", 18, 457, [("t-b", "Both parts are electronic:"), (None, " a meter proves only their wires; "), ("t-mono", "STATUS_DIGITAL"),
                             (None, " proves the brake switch and the clutch module (tables below).")])
    d.rich("t-sm", 18, 472.5, [(None, "The clutch module's EWS signal: "), ("t-mono", "EWS3.PRG"), (None, " \u2192 "), ("t-mono", "STATUS_LESEN"),
                               (None, ", clutch down: "), ("t-mono", "STAT_P_N_EINGANG"), (None, " changes and "),
                               ("t-mono", "STAT_ANLASSER_AUS_P_N"), (None, " = 0.")])

    # ================================================================== tables
    d.comment("Brake logic")
    d.rect("panel", 8, 488, 336, 145, rx=6)
    d.text("t t-b", 18, 505, "Brake: key on, engine off, press the pedal")
    d.text("t-sm", 18, 520, "Both bits change with the pedal.")
    cols = (18, 120, 228)
    for cx, s in zip(cols, ("STAT_BLS_EIN", "STAT_BLTS_EIN")):
        d.text("t-sm t-mono t-b", cx, 538, s)
    d.text("t-sm t-b", cols[2], 538, "Means")
    rows = (("changes", "changes", "OK", "t"), ("changes", "stays", "106 (0x6A), no cruise", "t-sm crit-t"),
            ("stays", "changes", "106 (0x6A), no cruise", "t-sm crit-t"))
    y = 556
    for a, b, c, cc in rows:
        d.line("ln-faint", 16, y - 14, 336, y - 14)
        d.text("t", cols[0], y, a)
        d.text("t", cols[1], y, b)
        d.text(cc, cols[2], y, c)
        y += 18
    d.text("t-sm", 18, y + 1, "Left on 28: yellow brake lamp (one xi Touring, unverified)")

    d.comment("Clutch logic")
    d.rect("panel", 364, 488, 428, 145, rx=6)
    d.text("t t-b", 374, 505, "Clutch: key on, engine off, parking brake on")
    d.text("t-sm", 374, 520, "Chain high = pedal up AND in gear")
    cols = (374, 446, 506, 690)
    for cx, s, c in zip(cols, ("Gearbox", "Pedal", "STAT_KRAFTSCHLUSS_EIN", "STAT_KUP_EIN"),
                        ("t-sm t-b", "t-sm t-b", "t-sm t-mono t-b", "t-sm t-mono t-b")):
        d.text(c, cx, 538, s)
    rows = (("in gear", "up", "1", "0"), ("in gear", "down", "0", "1"), ("neutral", "either", "0", "1"))
    y = 556
    for i, r in enumerate(rows):
        d.line("ln-faint", 372, y - 14, 784, y - 14)
        for cx, s in zip(cols, r):
            d.text("t t-b" if i == 0 else "t", cx, y, s)
        y += 18
    d.text("t-sm", 374, y + 1, "In neutral, 0 and 1 is correct, not a fault. Chain fault: 80 (0x50).")
    d.text("t-sm", 374, y + 15, "Touring before 03/2001 (switch S32) or SMG donor (no pin-20 wire): see text.")

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
