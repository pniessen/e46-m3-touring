#!/usr/bin/env python3
"""Redraw of figure 08 (README Figure 14, "Rear quarter cut lines"), portrait.

Fixes: the bulge label points to the flare profile instead of "25-30 mm proud"; the cut follows the
seam lines (top 500-515 above the hub, rear 550-600 behind the axle, front 25-40 behind the shut line)
instead of an arc down to the sill; the bulge ends on the bumper line about 300 mm behind the axle; the
filler pot stays where it is; the step at the door is 11-20 mm. Same geometry as figure 27 (common.py).
Data: notes rear_arches.md C1; README fragments 0660, 0670, 0680, 0690; gap-fill Gap 6 (door gap).
"""
import common as C
from common import w, catmull, poly
import kit

W = 400
NAME = "08-rear-quarter.svg"
S = 0.29
XMIN, XMAX = -760, 470
YMAX, YMIN = 670, -335
HX = 22 + S * 760
TOP = 108
HY = TOP + S * YMAX
RX = HX + S * XMAX
LH = 14

ARIA = (
    "Right side view of the rear quarter and rear door, to scale from BMW drawings. The M3 section to graft is "
    "bounded by three seams, which are our inference from the drawings: a top seam 500 to 515 mm above the hub, "
    "just under the shoulder crease; a rear seam 550 to 600 mm behind the axle, ahead of the tail lamp and down to "
    "about 250 mm above the hub behind the bumper; and a front seam 25 to 40 mm behind the rear door's shut line, "
    "parallel to it, down to the sill flange. The M3 bulge inside it stands about 21 to 23 mm proud over the arch "
    "and more behind it, mostly in the bumper corner; its profile is in the Flare profile section. The bulge ends "
    "on the bumper line about 300 mm behind the axle. The rear door's trailing edge forms the front of the arch, "
    "and with a stock door the M3 surface stands about 11 to 20 mm proud at the shut line: blend the nose in "
    "before the shut line, as BMW did, or reshape the door edge, then restore BMW's 4 plus or minus 0.75 mm gap. "
    "On the right side, take the filler pipe out before welding; your filler pot stays where it is, and the M3 "
    "surround and flap come in with the section.")


def sx(x):
    return HX + S * x


def sy(y):
    return HY - S * y


def P(pts):
    return [(sx(x), sy(y)) for x, y in pts]


def lines(d, cls, x, y, rows, anchor=None, lh=LH):
    for i, s in enumerate(rows):
        c = cls[0] if isinstance(cls, tuple) and i == 0 else (cls[1] if isinstance(cls, tuple) else cls)
        d.text(c, x, y + i * lh, s, anchor=anchor)


def build():
    d = kit.Doc()
    BOT = sy(YMIN)
    H = int(BOT + 112)

    # ------------------------------------------------------------ labels above the drawing
    lines(d, ("t t-b crit-t", "t-sm"), 8, 18, ["Fuel filler, right side", "Take the filler pipe out before",
                                               "you weld. Your pot, 51718208646,", "stays where it is; the M3",
                                               "surround and flap come with", "the section."])
    lines(d, ("t t-b fab-t", "t-sm"), 212, 18, ["Seams (our inference)", "Top: 500–515 mm above the hub",
                                                "Rear: 550–600 mm behind the axle",
                                                "Front: 25–40 mm behind the", "shut line, down to the sill"])
    d.text("t-xs", 376, TOP - 4, "front", anchor="end")
    d.line("ln", 379, TOP - 8, 393, TOP - 8, end="ah")

    # ------------------------------------------------------------ panels
    d.comment("Glass above the beltline")
    d.rect("panel", sx(XMIN), sy(YMAX), S * (XMAX - XMIN), S * (YMAX - C.BELT_Y))
    jy = C.junction_y()
    door_cut = C.door_cut_pts()
    sill_door_x = door_cut[-1][0]
    arch = C.ARCH
    i_bump = arch.index((-176, 305))
    upper_arch, rear_flank = arch[: i_bump + 1], arch[i_bump:]

    d.comment("Quarter panel (yours)")
    q = [(C.SHUT_X, C.BELT_Y), (XMIN, C.BELT_Y), (XMIN, C.BUMPER_Y)] + list(reversed(upper_arch)) + \
        [(366, C.SILL_Y), (sill_door_x, C.SILL_Y)] + list(reversed(door_cut))
    d.path("keep", poly(P(q), close=True), sw=1.2)
    d.comment("Rear door (yours)")
    door = [(C.SHUT_X, C.BELT_Y), (XMAX, C.BELT_Y), (XMAX, C.SILL_Y), (sill_door_x, C.SILL_Y)] + \
        list(reversed(door_cut))
    d.path("shape", poly(P(door), close=True), sw=1.2)
    d.text("t-sm", (sx(C.SHUT_X) + RX) / 2, sy(480), "rear", anchor="middle")
    d.text("t-sm", (sx(C.SHUT_X) + RX) / 2, sy(480) + 13, "door", anchor="middle")
    d.comment("Side skirt, bumper cover, tail lamp")
    d.path("panel", poly(P([(367, C.SILL_Y), (XMAX, C.SILL_Y), (XMAX, -130), (369, -130)]), close=True), sw=1)
    bump = [(-176, C.BUMPER_Y), (XMIN, C.BUMPER_Y), (XMIN, -130), (-383, -130)] + list(reversed(rear_flank))
    d.path("panel", poly(P(bump), close=True), sw=1.2)
    d.text("t-xs", sx(-560), sy(150), "bumper", anchor="middle")
    lx, l0, l1 = sx(C.LAMP_X), sy(C.LAMP_LOW), sy(548)
    d.path("panel", f"M{sx(XMIN):.1f},{l0:.1f} H{lx - 4:.1f} Q{lx:.1f},{l0:.1f} {lx:.1f},{l0 - 4:.1f} "
                    f"V{l1 + 4:.1f} Q{lx:.1f},{l1:.1f} {lx - 4:.1f},{l1:.1f} H{sx(XMIN):.1f} Z", sw=1.2)
    d.line("ln-thin", sx(C.LAMP_X), sy(C.CREASE_Y), sx(XMAX), sy(C.CREASE_Y))

    # ------------------------------------------------------------ M3 section and bulge
    fm, rm = C.SHUT_X - sum(C.FRONT_SEAM) / 2, C.R_DOOR - sum(C.FRONT_SEAM) / 2
    ym, xm = sum(C.TOP_SEAM) / 2, sum(C.REAR_SEAM) / 2
    front_c = [(fm, ym), (fm, C.junction_y(rm, fm))] + C.door_cut_pts(rm, fm)[1:]
    sec = [(xm, ym), (xm, C.BUMPER_Y)] + list(reversed(upper_arch)) + [(366, C.SILL_Y)] + list(reversed(front_c))
    d.add(f'<path class="donor" d="{poly(P(sec), close=True)}" stroke-width="0" opacity="0.75"/>')
    edge = arch[2:i_bump + 1]
    d.path("donor", catmull(P(C.BULGE)) + " L" + catmull(P(list(reversed(edge))))[1:] + " Z", sw=0)
    d.path("donor-s dash", catmull(P(C.BULGE)), sw=1.5)
    fx0, fx1, fy0, fy1 = C.FLAP
    d.rect("donor", sx(fx0), sy(fy1), S * (fx1 - fx0), S * (fy1 - fy0), rx=4, sw=1.2)

    # ------------------------------------------------------------ arch, wheel
    d.path("ln", catmull(P(arch)), sw=2)
    d.path("ln", poly(P([(364, 0), (366, C.SILL_Y), (369, -130)])), sw=2)
    d.path("ln", poly(P([(-379, 0), (-383, -130)])), sw=2)
    d.circle("ln", HX, HY, S * C.TYRE_R, sw=1.5)
    d.circle("ln-thin", HX, HY, S * C.RIM_R)
    d.dot("fill-fg", HX, HY, 3)

    # ------------------------------------------------------------ seams, shut line, step
    d.comment("Seams (our inference): cut and weld here")
    d.path("fab-s dash", poly(P([(fm, ym), (xm, ym), (xm, C.BUMPER_Y)])), sw=2.5)
    d.path("fab-s dash", poly(P([(xm, C.BUMPER_Y), (xm, C.REAR_SEAM_LOW)])), sw=1.2)
    d.path("fab-s dash", poly(P(front_c)), sw=2.5)
    d.comment("Shut line; the step where the M3 nose meets a stock door")
    d.path("ln", poly(P([(C.SHUT_X, C.BELT_Y), (C.SHUT_X, jy)] + door_cut[1:])), sw=1.5)
    d.path("crit-s", poly(P([(C.SHUT_X, jy + 4), (C.SHUT_X, 380)])), sw=3)

    # ------------------------------------------------------------ leaders from the top labels
    d.path("ln-thin", poly([(60, 18 + 5 * LH + 6), (sx(-380), sy(C.FLAP[3]) - 1)]))
    d.path("ln-thin", poly([(300, 18 + 4 * LH + 6), (sx(-150), sy(ym) - 2)]))

    # ------------------------------------------------------------ labels below the drawing
    yb = BOT + 18
    lines(d, ("t t-b donor-t", "t-sm"), 8, yb, ["M3 bulge", "≈21–23 mm proud over the arch,",
                                                 "more behind it, mostly in the", "bumper corner: see Flare profile.",
                                                 "Ends on the bumper line ≈300", "mm behind the axle."])
    d.path("ln-thin", poly([(80, yb - 13), (sx(-306) - 1, sy(306) + 3)]))
    lines(d, ("t t-b crit-t", "t-sm"), 212, yb, ["Bulge meets the door", "≈11–20 mm step at the shut line",
                                                  "with a stock door: blend the", "nose in before it (BMW) or reshape",
                                                  "the door edge, then restore", "the 4 ± 0.75 mm gap."])
    d.path("ln-thin", poly([(374, yb - 13), (sx(C.SHUT_X) + 2, sy(320))]))
    return kit.svg_open(W, H, ARIA), d.body()


if __name__ == "__main__":
    print(C.run(build, NAME))
