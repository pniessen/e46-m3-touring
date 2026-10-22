#!/usr/bin/env python3
"""Generate diagrams/12-coding-order.svg: the manual's coding sessions in order, their tools,
the two decisions (immobilizer route, DSC unit) and the two non-coding steps in between."""
import sys
sys.dont_write_bytecode = True
from svgkit import svg_open, t, write

out = []
add = out.append
L, R = (8, 188), (204, 188)      # lanes: x, width
LC, RC = 102, 298                # lane centres
GAP = 12                         # vertical gap holding an arrow
SH = 38                          # session box height


def rect(cls, x, y, w, h, sw="1.5", rx=5):
    add(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" stroke-width="{sw}"/>')


def down(x, y0, dashed=False):
    d = " dash" if dashed else ""
    add(f'<line class="ln{d}" x1="{x}" y1="{y0}" x2="{x}" y2="{y0 + GAP - 1}" marker-end="url(#ah)"/>')


def session(y, title, tool, line, x=8, w=384):
    rect("shape", x, y, w, SH)
    add(t("t t-b", x + 10, y + 16, title))
    add(t("t-sm t-mono", x + w - 10, y + 16, tool, "end"))
    add(t("t-xs", x + 10, y + 30, line))
    return y + SH


def option(y, lane, cls, title, lines, h=62):
    x, w = lane
    rect(cls, x, y, w, h)
    add(t("t t-b", x + 10, y + 17, title))
    for i, (s, c) in enumerate(lines):
        add(t(c, x + 10, y + 31 + 13 * i, s))
    return y + h


def other(y, title, line):
    """A step that isn't a coding session."""
    rect("panel", 8, y, 384, 26)
    add(t("t t-b", 18, y + 17.5, title))
    add(t("t-xs", 128, y + 17.5, line))
    return y + 26


def lanes_down(y):
    down(LC, y)
    down(RC, y)
    return y + GAP


add("<!-- Key -->")
rect("donor", 8, 6, 12, 12, "1", 2)
add(t("t-sm", 25, 16.5, "From donor M3"))
rect("keep", 122, 6, 12, 12, "1", 2)
add(t("t-sm", 139, 16.5, "Keep"))
rect("panel", 186, 6, 12, 12, "1", 2)
add(t("t-sm", 203, 16.5, "Not coding"))

add("\n<!-- 1: backups -->")
y = session(26, "1  Back up everything", "NCS Expert, PA-Soft, INPA",
            "Phase 0: vehicle order, codings, cluster and light-module memories")
down(200, y)

add("\n<!-- 2: DME, and the immobilizer decision -->")
y = session(y + GAP, "2  DME VIN and EWS", "Tool32, a vendor", "Read in Phase 1; vendor work in Phase 3")
y = lanes_down(y)
option(y, L, "donor", "EWS delete", [("recommended", "t-xs t-b"), ("bought as a service, with", "t-xs"),
                                       ("your VIN written in", "t-xs")])
y = option(y, R, "donor", "Virginized DME", [("a vendor clears it, then", "t-xs"),
                                               ("you sync it to your EWS", "t-xs"),
                                               ("no documented Touring success", "t-xs crit-t")])
y = lanes_down(y)
y = other(y, "Wire, then check", "Phase 11: re-pin, ohm-check, then power up")
y = lanes_down(y)

add("\n<!-- 3: EWS, depending on the route -->")
session(y, "3  EWS check", "Tool32", "nothing to code after a delete", *L)
y = session(y, "3  EWS sync", "Tool32", "sync the virgin DME to your EWS", *R)
y = lanes_down(y)

add("\n<!-- 4: cluster, then 5: the DSC and its decision -->")
y = session(y, "4  Cluster and light module", "PA-Soft, NCS Expert",
            "Phase 11: the cluster gets your VIN and true mileage from the light module")
down(200, y)
y = session(y + GAP, "5  DSC coding and VIN", "PA-Soft, NCS Expert, INPA",
            "Phase 11, after session 4: the DSC checks its VIN against the cluster's")
y = lanes_down(y)
option(y, L, "keep", "A  Keep your MK60", [("recommended", "t-xs t-b"), ("initialise its VIN and", "t-xs"),
                                             ("steering angle", "t-xs")])
y = option(y, R, "donor", "B  The M3's MK60", [("09/2002-on donors only", "t-xs t-b"),
                                                ("write your VIN, code M3 values", "t-xs"),
                                                ("by hand, then initialise", "t-xs")])
y = lanes_down(y)

add("\n<!-- 6: first start; alignment; 7: steering angle; 8 and 9 -->")
y = session(y, "6  First start, adaptations, throttle check", "Tool32",
            "Phase 12: adaptations cleared, the throttles relearn")
down(200, y)
y = other(y + GAP, "Wheel alignment", "at the car's loaded ride height")
down(200, y)
y = session(y + GAP, "7  Steering angle after the alignment", "INPA or Tool32",
            "Phase 12: wheel straight, car level, no brake pressure")
down(200, y)
y = session(y + GAP, "8  Vehicle-order changes and body modules", "NCS Expert",
            "Phase 12, after session 7, and whenever you change the vehicle order")
down(200, y)
y = session(y + GAP, "9  Light module and headlights", "NCS Expert", "Phase 12, last, with the front end on")
H = y + 8

ARIA = ("The coding sessions in the manual's order, with their tools. 1: back up the vehicle order, every module's "
        "coding and the cluster and light-module memories (NCS Expert, PA-Soft, INPA) in Phase 0. 2: the DME's "
        "VIN and EWS work (Tool32 and a vendor), read in Phase 1 with the vendor work in Phase 3. Decision: an EWS "
        "delete bought as a service, recommended, or a virginized DME that you sync, which no Touring build has "
        "documented working. Then wire and check in Phase 11. 3: the EWS in Tool32, with nothing to code after a "
        "delete, or a sync for a virgin DME. 4: the cluster and light module (PA-Soft, NCS Expert); the cluster gets "
        "your VIN and true mileage from the light module. 5: the DSC (PA-Soft, NCS Expert, INPA), after the cluster "
        "because the DSC checks its VIN against it. Decision: keep your MK60 and initialise it, recommended, or fit "
        "the M3's MK60 from a 09/2002-on donor, code M3 values by hand and initialise it. 6: first start with the "
        "adaptations cleared (Tool32). Then the wheel alignment, then 7: the steering-angle calibration (INPA or "
        "Tool32). 8: vehicle-order changes and body modules, and 9, last: the light module and headlights "
        "(NCS Expert).")
svg = svg_open(H, ARIA) + "\n".join(out) + "\n</svg>"
print(write("12-coding-order.svg", svg), H)
