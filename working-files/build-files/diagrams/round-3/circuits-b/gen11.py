#!/usr/bin/env python3
"""Generate diagrams/11-fuel-pump-control.svg (portrait): relay K96 (recommended) vs the US M3's EKP module.
Redraw of the earlier generator (../gen11.py) with wiring-canonical.md section 10 "Figure 11" items 1-7 applied,
using section 6.6 and the manual's "Fuel-pump control"."""
import sys
sys.dont_write_bytecode = True
from ckit import (svg_open, marker, t, tm, M, W, tm_width, rect, line, path, dot, write, measure_missing, fmt)

WIDTH = 400


def build():
    out = []
    add = out.append

    def box(cls, x, y, w, h, sw="1.5"):
        add(rect(cls, x, y, w, h, rx=5, sw=sw))

    def cell(cx, cy, label, cls="shape", tcls="t t-mono", w=20, h=18):
        add(rect(cls, cx - w / 2, cy - h / 2, w, h, rx=2, sw="1.2"))
        add(t(tcls, cx, cy + 4.5, label, "middle"))

    def para(x, y, lines, cls="t-xs", step=12.5, anchor=None):
        for i, s in enumerate(lines):
            add(tm(cls, x, y + step * i, M(s), anchor))

    def dme(y0, notes=True):
        """M3 DME with its two pump outputs; returns the y of the pin-10 and pin-11 wires."""
        h = 126 if notes else 104
        box("donor", 8, y0, 144, h)
        add(t("t t-b", 16, y0 + 19, "M3 DME"))
        add(t("t-sm", 16, y0 + 35, "MSS54 / HP"))
        add(t("t-sm t-b t-mono", 16, y0 + 58, "X60004 pin 10"))
        if notes:
            add(t("t-xs", 16, y0 + 71, '"not used" on US drawings'))
            add(t("t-xs", 16, y0 + 83, "(builders report it works)"))
            p11 = y0 + 100
        else:
            add(t("t-xs", 16, y0 + 71, "relay output"))
            p11 = y0 + 82
        add(t("t-sm t-b t-mono", 16, p11 + 4, "X60002 pin 11"))
        add(t("t-xs", 16, p11 + 17, "0–120 Hz PWM"))
        return y0 + 54, p11

    def x6021(x, y, body):
        """X6021 pin 1: the M3-harness half (left) and your body-side half (right)."""
        cell(x + 10, y, "1", cls="donor")
        if body == "empty":
            add(rect("keep dash", x + 20, y - 9, 20, 18, rx=2, sw="1.2"))
        else:
            cell(x + 30, y, "1", cls="new")

    def supply(x, ytop, ycell, lines, side):
        """A supply arriving from above at a top-edge cavity, labelled beside the line."""
        add(line("ln", x, ytop, x, ycell - 10, mk="ah"))
        for i, s in enumerate(lines):
            tx = x - 6 if side == "left" else x + 6
            add(tm("t-xs", tx, ytop + 6 + 12 * i, M(s), "end" if side == "left" else None))

    def pump(cx, y0):
        box("keep", cx - 42, y0, 84, 36)
        add(t("t t-b", cx, y0 + 17, "Pump", "middle"))
        add(t("t-xs", cx, y0 + 30, "in the tank", "middle"))

    # Key
    add("<!-- Key -->")
    for x, cls, label in ((8, "donor", "From donor M3"), (130, "keep", "Keep"), (196, "new", "New")):
        add(rect(cls, x, 6, 12, 12, rx=5, sw="1"))
        add(t("t-sm", x + 17, 16.5, label))

    # ------------------------------------------------------------ recommended: the relay
    add("\n<!-- Recommended: the MSS54's pin-10 output drives your K96 -->")
    add(t("t-h", 8, 44, "RECOMMENDED: KEEP THE RELAY"))
    p10, p11 = dme(100)
    kx0, kx1, ky0, ky1 = 232, 340, 120, 200
    box("keep", kx0, ky0, kx1 - kx0, ky1 - ky0)
    cxk = (kx0 + kx1) / 2 + 6
    add(t("t t-b", cxk, ky0 + 26, "Relay K96", "middle"))
    add(tm("t-xs", cxk, ky0 + 41, M("socket [X10156]"), "middle"))
    add(t("t-xs", cxk, ky0 + 54, "behind the", "middle"))
    add(t("t-xs", cxk, ky0 + 66, "glovebox", "middle"))
    # coil ground from the DME
    cell(kx0, p10, "4")
    add(line("ln", 152, p10, kx0 - 11, p10))
    add(tm("t-xs", (152 + kx0 - 11) / 2, p10 - 6, M("[0.35 SW/VI]"), "middle"))
    # supplies on top
    cell(260, ky0, "8")
    cell(312, ky0, "6")
    supply(260, 62, ky0, ["F3 via [X6021] pin [2]", "[1.5 RT/WS]", "live only while the DME relay is on"], "left")
    supply(312, 62, ky0, ["F54, 15 A", "[2.5 RT/VI]"], "right")
    # out to the pump
    px = 290
    cell(px, ky1, "2")
    add(line("ln", px, ky1 + 9, px, 237, mk="ah"))
    add(tm("t-xs", px + 6, 226, M("[1.5 WS/BL]")))
    pump(px, 238)

    add("\n<!-- Pin 11, the PWM output: ends at X6021 pin 1, never on K96 -->")
    add(line("ln", 152, p11, 166, p11))
    x6021(166, p11, "empty")
    add(line("crit-s dash", 196, p11 - 9.5, 196, p10 + 5, sw="1.5"))
    xm = (p10 + p11) / 2
    add(path("crit-s", f"M191,{xm - 5} l10,10 M191,{xm + 5} l10,-10", sw="2"))
    add(t("t-xs crit-t t-b", 187, xm + 4, "never", "end"))
    add(tm("t-xs", 158, p11 + 22, M("[X6021] pin [1]:")))
    add(t("t-xs", 158, p11 + 34, "your side empty"))

    add("\n<!-- Crash cut-off with the relay: undocumented -->")
    para(8, 256, ["Whether US software drops the pin-10", "output after a crash isn't documented."])

    add("\n<!-- How to prove pin 10 -->")
    para(8, 294, ["Prove pin 10 on the car: one prime at key-on, [STAT_EKP_EIN] = 1 during it, and",
                  "[STEUERN_EKP] makes K96 click. If the job returns OKAY but K96 stays silent,",
                  "go by the prime and [STAT_EKP_EIN]."])

    add("\n<!-- The stored fault -->")
    add(rect("warn-f", 8, 330, 384, 78, rx=5, sw="1.5"))
    add(tm("t-sm t-b", 18, 347, M("Pin 11 connected to nothing: stored fault [1 (0x01)]")))
    para(18, 362, ['"Relais Kraftstoffpumpe" (INPA shows 1): in INPA, ISTA and PA-Soft, not on',
                   "a generic scanner; it doesn't light the check-engine lamp. Not [130 (0x82)],",
                   "the immobilizer fault. Don't flash Euro software to clear it: that drops the",
                   "DM-TL leak test."])

    add("\n<!-- Never -->")
    add(rect("crit-s", 8, 416, 384, 92, rx=5, sw="1.5"))
    add(t("t-sm t-b crit-t", 18, 433, "Never connect the PWM pump output to K96"))
    para(18, 448, ["A relay coil can't follow a 0–120 Hz signal and would likely chatter. The",
                   "wire leaves the M3 harness at [X6021] pin [1] ([0.35 SW/VI], the same color as",
                   "the pin-10 wire: go by the cavity); your side of that pin is empty on a",
                   "manual 325i. Meter: M3 harness [X6021] pin [1] to every K96 socket terminal",
                   "reads open; any continuity → de-pin the M3 wire and insulate it."])

    add('\n<line class="ln-faint" x1="8" y1="522" x2="392" y2="522"/>')

    # ------------------------------------------------------------ optional: the EKP module
    add("\n<!-- Optional: the US M3's pump module, driven by pin 11 -->")
    add(t("t-h", 8, 546, "OPTIONAL: THE M3 PUMP MODULE (EKP)"))
    q10, q11 = dme(560, notes=False)
    add(line("ln", 152, q10, 176, q10))
    add(f'<circle class="shape" cx="180" cy="{q10}" r="3.5"/>')
    add(t("t-xs", 188, q10 + 3.7, "not used"))
    ex0, ex1, ey0, ey1 = 252, 362, 584, 662
    box("donor", ex0, ey0, ex1 - ex0, ey1 - ey0)
    cxe = (ex0 + ex1) / 2 + 6
    add(t("t t-b", cxe, ey0 + 23, "EKP module", "middle"))
    add(tm("t-xs", cxe, ey0 + 37, M("plug [X10157]"), "middle"))
    add(t("t-xs", cxe, ey0 + 50, "slows the pump at", "middle"))
    add(t("t-xs", cxe, ey0 + 62, "idle and part load", "middle"))
    # signal: pin 11 through X6021 pin 1, which needs a new terminal and wire on your side
    add(line("ln", 152, q11, 166, q11))
    x6021(166, q11, "new")
    cell(ex0, q11, "1")
    add(line("new-s", 206, q11, ex0 - 10, q11, sw="2"))
    add(t("t-xs new-t", 158, q11 + 22, "new terminal and"))
    add(t("t-xs new-t", 158, q11 + 34, "wire on your side"))
    # supplies, pump and ground
    cell(280, ey0, "8")
    cell(338, ey0, "6")
    supply(280, 560, ey0, ["F3"], "left")
    supply(338, 560, ey0, ["F54"], "right")
    cell(286, ey1, "2")
    add(line("ln", 286, ey1 + 9, 286, 693, mk="ah"))
    add(tm("t-xs", 277, 689, M("[2.5 RT/WS]"), "end"))
    pump(286, 694)
    cell(342, ey1, "7")
    add(line("ln", 342, ey1 + 9, 342, 692))
    add(path("ln", "M332,692 H352 M336,697 H348 M340,702 H344"))
    add(tm("t-xs", 348, 686, M("[2.5 BR]")))

    add("\n<!-- Crash cut-off: no wire; airbag unit, K-bus, cluster, CAN, DME -->")
    box("keep", 8, 692, 76, 28)
    add(t("t t-b", 46, 710.5, "Cluster", "middle"))
    add(line("ln", 46, 691, 46, 560 + 104 + 1, mk="ah"))
    add(t("t-xs", 52, 684, "CAN"))
    box("keep", 118, 692, 92, 28)
    add(t("t t-b", 164, 710.5, "Airbag unit", "middle"))
    add(line("ln", 117, 706, 85, 706, mk="ah"))
    add(t("t-xs", 101, 697, "K-bus", "middle"))
    para(8, 746, ["No wire: after a crash, the airbag unit's message reaches the DME through",
                  "the cluster, and the DME switches the pump off."])

    add("\n<!-- When to fit it -->")
    para(8, 782, ["Fit it only if your state won't accept the stored fault, or you want the",
                  "slow-running pump and crash cut-off back. It needs five wires to the",
                  "relay's four, and nobody has documented it in a Touring."])
    H = 816

    aria = ("Fuel-pump control, two ways. Recommended: keep the relay. The M3 DME's X60004 pin 10, called not used on "
            "US M3 drawings though builders report it works, grounds the coil of your relay K96 at socket X10156 pin 4 "
            "through the 0.35 SW/VI wire. K96 pin 8 takes the coil supply from F3 through X6021 pin 2 (1.5 RT/WS), live "
            "only while the DME relay is on; pin 6 takes the load supply from F54, 15 A (2.5 RT/VI); pin 2 feeds the pump "
            "in the tank (1.5 WS/BL). The DME's 0–120 Hz PWM output, X60002 pin 11, leaves the M3 harness at X6021 pin 1 "
            "(0.35 SW/VI); on a manual 325i your side of that pin is empty, so it connects to nothing; never put it on "
            "K96; both it and the pin-10 wire are 0.35 SW/VI, so go by the cavity, and a meter from the M3 harness's X6021 "
            "pin 1 to every K96 socket terminal must read open, or de-pin the M3 wire and insulate it. Prove pin 10 with one "
            "prime at key-on, STAT_EKP_EIN at 1 during it, and STEUERN_EKP clicking K96; if the job returns OKAY but K96 "
            "stays silent, go by the prime and STAT_EKP_EIN. Whether US software drops the "
            "pin-10 output after a crash isn't documented. Expect stored fault location 1 (0x01), Relais "
            "Kraftstoffpumpe, which INPA shows as 1; it shows in INPA, ISTA and PA-Soft but not on a generic scanner, "
            "and doesn't light the check-engine lamp; it is not 130 (0x82), the immobilizer fault; don't flash Euro "
            "software to clear it. Optional: the US M3's EKP pump module, plug X10157, takes the pin-11 signal on its "
            "pin 1 through X6021 pin 1, which needs a new terminal and wire on your side, F3 on pin 8, F54 on pin 6, "
            "feeds the pump from pin 2 (2.5 RT/WS) and is grounded on pin 7 (2.5 BR); pin 10 is then not used. There is "
            "no crash wire: the airbag unit's message goes over the K-bus to the cluster and over CAN to the DME, which "
            "switches the pump off. Fit it only if your state won't accept the stored fault or you want the slow-running "
            "pump and crash cut-off back; nobody has documented it in a Touring.")
    return svg_open(WIDTH, H, aria) + "\n".join(o for o in out if o) + "\n</svg>"


if __name__ == "__main__":
    svg = build()
    if measure_missing():
        svg = build()
    print(write("11-fuel-pump-control.svg", svg))
