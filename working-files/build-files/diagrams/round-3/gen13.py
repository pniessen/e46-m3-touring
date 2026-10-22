#!/usr/bin/env python3
"""Generate diagrams/13-dsc-brake-options.svg: keep the Touring's MK60 (default) or fit the M3's."""
import sys
sys.dont_write_bytecode = True
from svgkit import svg_open, t, write

out = []
add = out.append
A, B = 8, 204        # column x
CW = 188             # column width
AC, BC = 102, 298    # column centres


def rect(cls, x, y, w, h, sw="1.5", rx=5):
    add(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" stroke-width="{sw}"/>')


def part(cls, x, y, w, h, name, tag=None, sub=None, name_cls="t t-b"):
    rect(cls, x, y, w, h)
    if sub:
        add(t(name_cls, x + 10, y + 15.5, name))
        add(t("t-xs", x + 10, y + 29, sub))
    else:
        add(t(name_cls, x + 10, y + h / 2 + 4.6, name))
    if tag:
        add(t("t-xs", x + w - 10, y + h / 2 + 3.7, tag, "end"))


def pipe(x, y0, y1):
    add(f'<line class="ln" x1="{x}" y1="{y0}" x2="{x}" y2="{y1}"/>')


add("<!-- Key -->")
rect("keep", 8, 6, 12, 12, "1", 2)
add(t("t-sm", 25, 16.5, "Keep"))
rect("donor", 70, 6, 12, 12, "1", 2)
add(t("t-sm", 87, 16.5, "From donor M3"))
rect("new", 186, 6, 12, 12, "1", 2)
add(t("t-sm", 203, 16.5, "Buy new"))

add("\n<!-- Which unit the donor has -->")
rect("donor", A, 28, CW, 52)
add(t("t-sm t-b", A + 10, 45, "Donor built before 09/2002"))
add(t("t-xs", A + 10, 59, "MK20, 43-pin plug:"))
add(t("t-xs crit-t", A + 10, 72, "won't plug into your harness"))
rect("donor", B, 28, CW, 52)
add(t("t-sm t-b", B + 10, 45, "Donor built from 09/2002"))
add(t("t-xs", B + 10, 59, "MK60: same 47-pin plug and yaw"))
add(t("t-xs", B + 10, 72, "sensor as your Touring's"))
add(f'<line class="ln" x1="{AC}" y1="80" x2="{AC}" y2="99" marker-end="url(#ah)"/>')
add(f'<line class="ln" x1="{BC}" y1="80" x2="{BC}" y2="99" marker-end="url(#ah)"/>')
add('<path class="ln" d="M240,80 V89 H150 V99" marker-end="url(#ah)"/>')

add("\n<!-- Route A -->")
add(t("t-h", A, 116, "A  KEEP YOURS"))
add(t("t-xs t-b", A, 130, "the default; recommended"))
add(t("t-xs", A, 148, "No coding tricks: initialise its VIN"))
add(t("t-xs", A, 161, "and steering angle in INPA"))
add(t("t-xs", A, 178, "Stays coded for a 325i: no M Track"))
add(t("t-xs", A, 195, "Pedal feel of M3 calipers on your"))
add(t("t-xs", A, 208, "master cylinder: unreported"))
add(t("t-xs", A, 225, "Check its label first: some US"))
add(t("t-xs", A, 238, "Tourings have an ASC-only unit"))

add("\n<!-- Route B -->")
add(t("t-h", B, 116, "B  FIT THE M3'S UNIT"))
add(t("t-xs t-b", B, 130, "09/2002-on donors only"))
add(t("t-xs", B, 148, "NCS Expert gives it 325i values: set"))
add(t("t-xs", B, 161, "M3 values by hand. Its coding has"))
add(t("t-xs", B, 174, "no Touring body type"))
add(t("t-xs", B, 191, "Brings M Track"))
add(t("t-xs", B, 208, "Touring built before 09/2001: also"))
add(t("t-xs", B, 221, "the later yaw-sensor cluster"))
add(t("t-xs", B, 238, '"VIN not initialized" won\'t clear?'))
add(t("t-xs", B, 251, "Refit your own unit"))

add("\n<!-- Brake hydraulics, pedal to caliper -->")
part("keep", A, 266, CW, 36, "Your booster")
part("keep", B, 266, CW, 36, "Your booster", sub="or perhaps the M3's")
pipe(AC, 302, 312)
pipe(BC, 302, 312)
part("keep", A, 312, CW, 26, "Your master cylinder")
part("donor", B, 312, CW, 26, "M3 master cylinder")
pipe(AC, 338, 348)
pipe(BC, 338, 348)
part("keep", A, 348, CW, 26, "Your MK60", tag="DSC unit")
part("donor", B, 348, CW, 26, "M3 MK60", tag="DSC unit")
pipe(AC, 374, 384)
pipe(BC, 374, 384)

add("\n<!-- Same on both routes -->")
part("keep", 8, 384, 384, 38, "Your brake pipes stay",
     sub="an MK60 M3 uses the same front pipes; the rear pipes and hoses are shared", name_cls="t-sm t-b")
pipe(200, 422, 432)
part("new", 8, 432, 384, 26, "M3 front brake hoses", tag="M3-only, buy new: 34322229723")
pipe(200, 458, 468)
part("donor", 8, 468, 384, 26, "M3 calipers", tag="with the corners and trailing arms")

add("\n<!-- Both routes -->")
rect("panel", 8, 506, 384, 150, "1", 6)
add(t("t-sm t-b", 18, 523, "Both routes"))
add(t("t-xs", 18, 538, "Wheel-speed sensors: the rear sensor changed type at 09/2001 on the"))
add(t("t-xs", 18, 551, "Touring and 09/2002 on the M3, and one build's plugs didn't mate. Check"))
add(t("t-xs", 18, 564, "the plugs on both cars before you order, use sensors whose plugs fit"))
add(t("t-xs", 18, 577, "your harness, and keep the donor's sensors and pigtails until yours are"))
add(t("t-xs", 18, 590, "proven. Read the DSC fault memory after the first slow drive."))
add(t("t-xs", 18, 605, "Booster vacuum hose: the M3's meets the booster from the other side;"))
add(t("t-xs", 18, 618, "check its route at mock-up."))
add(t("t-xs", 18, 633, "Calibrate the steering angle after the wheel alignment."))
add(t("t-xs", 18, 648, "Keep the parts you don't use until the car has passed inspection."))
H = 664

ARIA = ("The DSC and brake choice. A donor built before 09/2002 has an MK20 with a 43-pin plug, which won't plug "
        "into your harness, so only route A applies; a donor built from 09/2002 has an MK60 with the same 47-pin "
        "plug and yaw sensor as your Touring, so either route works. Route A, the recommended default, keeps your "
        "MK60, master cylinder and booster: no coding tricks, just initialise its VIN and steering angle in INPA. "
        "It stays coded for a 325i with no M Track, nobody has reported the pedal feel of M3 calipers on your "
        "master cylinder, and you should check the unit's label first, as some US Tourings have an ASC-only unit. "
        "Route B fits the M3's MK60 and master cylinder, with your booster or perhaps the M3's. NCS Expert gives it "
        "325i values, so you set M3 values by hand, and its coding has no Touring body type. It brings M Track; a "
        "Touring built before 09/2001 also needs the later yaw-sensor cluster; if VIN not initialized won't clear, "
        "refit your own unit. On both routes your brake pipes stay, since an MK60 M3 uses the same front pipes and "
        "the rear pipes and hoses are shared; the M3-only front brake hoses 34322229723 are bought new; and the M3 "
        "calipers come with the corners. Both routes: the rear wheel-speed sensor changed type at 09/2001 on the "
        "Touring and 09/2002 on the M3, and one build's plugs didn't mate, so check the plugs on both cars before "
        "you order, use sensors whose plugs fit your harness, keep the donor's sensors and pigtails until yours are "
        "proven, and read the DSC fault memory after the first slow drive. Check the route of the M3's booster "
        "vacuum hose, which meets the booster from the other side, calibrate the steering angle after the wheel "
        "alignment, and keep the parts you don't use until the car has passed inspection.")
svg = svg_open(H, ARIA) + "\n".join(out) + "\n</svg>"
print(write("13-dsc-brake-options.svg", svg))
