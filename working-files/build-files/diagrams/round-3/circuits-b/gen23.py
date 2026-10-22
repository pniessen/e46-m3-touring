#!/usr/bin/env python3
"""Generate diagrams/23-can-network.svg: the powertrain CAN after the swap (DME, cluster, DSC unit, steering-angle
sensor on splices X1893/X1894), its two terminators, where to measure and what the readings mean, the diagnosis
socket X19527 (no CAN), the K-bus, and the traffic that crosses the cluster's gateway.
Data: wiring-canonical.md section 6.7 and the manual's "CAN, K-bus and the diagnosis socket", step 19 and
"Crash fuel cut-off"."""
import sys
sys.dont_write_bytecode = True
from ckit import (svg_open, marker, t, tm, M, W, tm_width, rect, line, path, dot, write, measure_missing, fmt)

WIDTH = 800


def build():
    out = []
    add = out.append

    def cell(cx, cy, label, cls="shape", tcls="t t-mono", w=24, h=18):
        if "shape" not in cls:   # an outline-only cell still hides the border it sits on
            add(rect("fill-bg", cx - w / 2, cy - h / 2, w, h, rx=2, sw="0"))
        add(rect(cls, cx - w / 2, cy - h / 2, w, h, rx=2, sw="1.2"))
        add(t(tcls, cx, cy + 4.5, label, "middle"))

    def resistor(x, y0, y1, ym, dashed=False):
        """A terminating resistor inside a node, between its CAN-high and CAN-low cavities, centred on ym."""
        add(line("ln-thin", x, y0, x, ym - 14))
        add(line("ln-thin", x, ym + 14, x, y1))
        add(rect("shape dash" if dashed else "shape", x - 5, ym - 14, 10, 28, rx=1, sw="1.3"))

    def para(x, y, lines, cls="t-sm", step=14, anchor=None):
        for i, s in enumerate(lines):
            add(tm(cls, x, y + step * i, M(s), anchor))

    # ------------------------------------------------------------------ header, key, terminator note
    add(t("t-h", 8, 24, "CAN, K-BUS AND DIAGNOSIS SOCKET"))
    kx = 792
    lab = "120 Ω terminator"
    kx -= W("t-sm", lab)
    add(t("t-sm", kx, 22, lab))
    kx -= 16
    add(rect("shape", kx, 11, 9, 15, rx=1, sw="1.2"))
    kx -= 22
    for cls, label in (("keep", "Keep"), ("donor", "From donor M3")):
        kx -= W("t-sm", label)
        add(t("t-sm", kx, 22, label))
        kx -= 22
        add(rect(cls, kx, 12, 14, 12, rx=2, sw="1"))
        kx -= 16
    add(tm("t-sm", 8, 48, M("Terminators: one 120 Ω in the DSC unit, one in the cluster or the DME "
                            "(which one isn't documented); together 60 Ω.")))

    # ------------------------------------------------------------------ the bus
    yH, yL = 82, 266                   # CAN high bar (splice X1893), CAN low bar (splice X1894)
    top, bot = 108, 240                # node boxes
    yr = 190                           # terminator centre
    ydiag = 216                        # diagnosis-line row
    nodes = {"dme": 60, "clu": 446, "dsc": 516, "sas": 664}   # x of each node's CAN cavities
    add("\n<!-- CAN high and CAN low: every node lands on both splices -->")
    add(line("keep-s", nodes["dme"], yH, nodes["sas"], yH, sw="2.5"))
    add(line("keep-s", nodes["dme"], yL, nodes["sas"], yL, sw="2.5"))
    for x in nodes.values():
        add(line("keep-s", x, yH, x, top - 9, sw="2"))
        add(line("keep-s", x, bot + 9, x, yL, sw="2"))
        add(dot("keep-f", x, yH, 4))
        add(dot("keep-f", x, yL, 4))
    add(tm("t-sm t-b", 92, yH - 8, M("CAN high, [GE/RT]: splice [X1893]")))
    add(tm("t-sm t-b", 92, yL + 18, M("CAN low, [GE/BR]: splice [X1894]")))

    # DME
    add("\n<!-- DME -->")
    add(rect("donor", 40, top, 120, bot - top))
    x = nodes["dme"]
    cell(x, top, "36")
    cell(x, bot, "37")
    resistor(x, top + 9, bot - 9, yr, dashed=True)
    add(t("t t-b", 76, top + 18, "M3 DME"))
    add(t("t-sm", 76, top + 34, "MSS54 / HP"))
    add(t("t-sm t-mono t-b", 76, top + 50, "X60004"))
    add(t("t-sm", 72, yr + 4, "120 Ω ?"))
    cell(160, ydiag, "32")
    add(t("t-sm t-mono", 146, ydiag + 4, "TXD II", "end"))

    # diagnosis socket
    add("\n<!-- Diagnosis socket X19527: no CAN cavities -->")
    ox0, ox1 = 204, 292
    oc = (ox0 + ox1) / 2
    add(rect("keep", ox0, top, ox1 - ox0, bot - top))
    cell(ox0, ydiag, "7")
    cell(ox1, ydiag, "8")
    cell(oc, top, "6", cls="crit-s dash", tcls="t t-mono crit-t")
    cell(oc, bot, "14", cls="crit-s dash", tcls="t t-mono crit-t")
    add(t("t-sm crit-t", oc + 16, top - 12, "no terminal"))
    add(t("t-sm crit-t", oc + 16, bot + 18, "no terminal"))
    add(t("t t-b", oc, top + 30, "Diagnosis", "middle"))
    add(t("t t-b", oc, top + 45, "socket", "middle"))
    add(t("t-sm t-mono t-b", oc, top + 61, "X19527", "middle"))
    add(t("t-sm t-b crit-t", oc, top + 92, "no CAN", "middle"))
    add(line("keep-s", 160 + 12, ydiag, ox0 - 12, ydiag, sw="2"))

    # cluster
    add("\n<!-- Cluster: the gateway -->")
    cx0, cx1 = 336, 470
    add(rect("donor", cx0, top, cx1 - cx0, bot - top))
    x = nodes["clu"]
    cell(x, top, "9")
    cell(x, bot, "10")
    resistor(x, top + 9, bot - 9, yr, dashed=True)
    add(t("t t-b", cx0 + 18, top + 18, "M3 cluster"))
    add(t("t-sm t-mono t-b", cx0 + 18, top + 34, "X11175"))
    add(t("t-sm", cx0 + 18, top + 50, "gateway"))
    add(t("t-sm", x - 12, yr + 4, "120 Ω ?", "end"))
    cell(cx0, ydiag, "25")
    add(t("t-sm", cx0 + 16, ydiag + 4, "D-bus"))
    add(line("keep-s", ox1 + 12, ydiag, cx0 - 12, ydiag, sw="2"))
    kb = cx0 + 74
    cell(kb, bot, "14")
    add(t("t-sm", kb, bot - 15, "K-bus", "middle"))

    # DSC unit
    add("\n<!-- DSC unit (MK60) -->")
    dx0, dx1 = 496, 620
    add(rect("keep", dx0, top, dx1 - dx0, bot - top))
    x = nodes["dsc"]
    cell(x, top, "11")
    cell(x, bot, "15")
    resistor(x, top + 9, bot - 9, yr)
    add(t("t t-b", x + 16, top + 18, "DSC unit"))
    add(tm("t-sm", x + 16, top + 34, M("MK60: [11] / [15]")))
    add(t("t-sm t-b", x + 16, yr + 4, "120 Ω"))

    # steering-angle sensor
    add("\n<!-- Steering-angle sensor -->")
    sx0, sx1 = 644, 792
    add(rect("keep", sx0, top, sx1 - sx0, bot - top))
    x = nodes["sas"]
    cell(x, top, "3")
    cell(x, bot, "4")
    add(t("t t-b", x + 16, top + 18, "Steering-angle"))
    add(t("t t-b", x + 16, top + 33, "sensor"))

    # ------------------------------------------------------------------ where to measure
    add("\n<!-- Where to measure: back-probe at the DME, battery disconnected -->")
    py = 296
    add(rect("panel", 8, py, 324, 252, rx=6, sw="1"))
    mx, my = 40, py + 32
    xs = nodes["dme"]
    add(path("ln-thin", f"M30,{my - 14} V{yH + 8} H{xs - 2}", sw="1.5", mk="ah"))
    add(path("ln-thin", f"M50,{my - 14} V{yL - 10} H{xs - 2}", sw="1.5", mk="ah"))
    add(f'<circle class="shape" cx="{mx}" cy="{my}" r="17"/>')
    add(t("t t-b", mx, my + 5, "Ω", "middle"))
    para(70, py + 20, ["Back-probe [X60004] [36] and [37] at the",
                       "plugged-in DME, or [X11175] [9] and [10] at",
                       "the cluster. Battery disconnected, every",
                       "module plugged in."])
    add(t("t-sm t-b crit-t", 18, py + 88, "Not at the diagnosis socket: no CAN there."))
    add(t("t-sm t-b", 18, py + 110, "Reading"))
    add(t("t-sm t-b", 112, py + 110, "Means"))
    add(line("ln-faint", 18, py + 116, 322, py + 116))
    rows = [("about 60 Ω", "pass: both terminators in place"),
            ("about 120 Ω", "a terminating module unplugged or cut off"),
            ("about 40 Ω", "a third terminator"),
            ("0 Ω", "high and low shorted together"),
            ("open", "both missing, or the probe wire broken")]
    for i, (a, b) in enumerate(rows):
        cls = "t-sm t-b" if i == 0 else "t-sm"
        add(t(cls, 18, py + 132 + 16 * i, a))
        add(t(cls, 112, py + 132 + 16 * i, b))
    add(line("ln-faint", 18, py + 210, 322, py + 210))
    para(18, py + 226, ["Key on: each line about 2.5 V to ground (2.35–2.65 V).",
                        "Unplug one module at a time: about 120 Ω = a terminator."])

    # ------------------------------------------------------------------ K-bus
    add("\n<!-- K-bus: one wire from the cluster to the body modules -->")
    kx0, kx1, ky = 344, 556, 312
    add(path("keep-s", f"M{kb},{bot + 9} V{yL - 6} A6,6 0 0 1 {kb},{yL + 6} V{ky}", sw="2"))
    add(rect("keep", kx0, ky, kx1 - kx0, 138))
    add(t("t t-b", kx0 + 10, ky + 19, "K-bus"))
    add(tm("t-sm", kx0 + 10, ky + 35, M("one wire, [WS/RT/GE], about 12 V")))
    para(kx0 + 10, ky + 56, ["light module, body module, climate",
                             "control, airbag unit, EWS, switch",
                             "center ([X1869] pin [23]), steering-wheel",
                             "audio buttons, park distance control",
                             "and others"])
    para(kx0, ky + 158, ["DME faults for a missing partner:",
                         "[132 (0x84)] DSC, [133 (0x85)]",
                         "steering-angle sensor, [134 (0x86)]",
                         "cluster, [86 (0x56)] its own CAN."])

    # ------------------------------------------------------------------ gateway traffic
    add("\n<!-- What crosses the cluster's gateway in this swap -->")
    gx0, gx1 = 566, 792
    add(rect("keep", gx0, ky, gx1 - gx0, 182))
    add(t("t t-b", gx0 + 10, ky + 19, "Through the cluster's gateway"))
    para(gx0 + 10, ky + 38, ["A/C request (climate control)",
                             "and crash signal (airbag unit):",
                             "K-bus → cluster → CAN → DME",
                             "Tank level: cluster → CAN → DME"])
    para(gx0 + 10, ky + 102, ["If the cluster isn't talking on both",
                              "buses: no A/C, no crash cut-off and",
                              "no leak test"], cls="t-sm t-b")
    para(gx0 + 10, ky + 144, ["(our reading of BMW's descriptions).",
                              "Even with a working cluster, the crash",
                              "cut-off is unverified with the K96 relay."])
    add("\n<!-- Footnotes -->")
    para(344, 534, ["The DSC unit's yaw sensor has a separate CAN of its own, not shown.",
                    "An MK20 DSC unit (not used in this build) has CAN on pins 17 and 16.",
                    "An ex-automatic Touring's gearbox-unit stub stays unplugged."])

    H = 572
    aria = ("Network diagram of the powertrain CAN, the K-bus and the diagnosis socket after the swap. CAN high (GE/RT) "
            "runs along splice X1893 and CAN low (GE/BR) along splice X1894; four nodes land on both: the M3 DME at "
            "X60004 pins 36 and 37, the M3 cluster at X11175 pins 9 and 10, the DSC unit (MK60) at pins 11 and 15, and "
            "the steering-angle sensor at pins 3 and 4. The DSC unit holds one 120 ohm terminator and the cluster or the "
            "DME the other, which one isn't documented, so a healthy bus reads about 60 ohms. Measure with the battery "
            "disconnected and every module plugged in, back-probing X60004 pins 36 and 37 at the DME or X11175 pins 9 "
            "and 10 at the cluster, not at the diagnosis socket. Readings between high and low: about 60 ohms passes; "
            "about 120 ohms means a terminating module is unplugged or cut off; about 40 ohms a third terminator; 0 ohms "
            "high and low shorted together; open means both terminators are missing or the probe wire is broken. Key on, "
            "each line sits at about 2.5 volts to ground (2.35 to 2.65). Unplugging one module at a time shows which ones "
            "terminate. The diagnosis socket X19527 has no terminals at pins 6 and 14, so no CAN; its pin 7 goes to the "
            "DME's TXD II line at X60004 pin 32 and its pin 8 to the cluster's D-bus at X11175 pin 25. The K-bus is one "
            "WS/RT/GE wire at about 12 volts from cluster pin 14 to the light module, body module, climate control, "
            "airbag unit, EWS, switch center (X1869 pin 23), steering-wheel audio buttons, park distance control and "
            "others. The A/C request from the climate control and the crash signal from the airbag unit go over the "
            "K-bus to the cluster and on over CAN to the DME, and so does the cluster's tank level. By the manual's "
            "reading of BMW's descriptions, a cluster that isn't talking on both buses costs the A/C, the crash cut-off "
            "and the leak test; and even with a working cluster, the crash cut-off is unverified with the K96 relay. The "
            "DME logs 132 (0x84) for the DSC unit, 133 (0x85) for the steering-angle sensor, 134 (0x86) for the cluster "
            "and 86 (0x56) for its own CAN. The DSC unit's yaw sensor has a separate CAN, an MK20 DSC unit, not used in "
            "this build, has CAN on pins 17 and 16, and an ex-automatic Touring's gearbox-unit stub stays unplugged.")
    return svg_open(WIDTH, H, aria) + "\n".join(o for o in out if o) + "\n</svg>"


if __name__ == "__main__":
    svg = build()
    if measure_missing():
        svg = build()
    print(write("23-can-network.svg", svg))
