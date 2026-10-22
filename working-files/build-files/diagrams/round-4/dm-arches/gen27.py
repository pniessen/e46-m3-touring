#!/usr/bin/env python3
"""Figure 27 (new, landscape): the M3 flare profile on the Touring's right rear quarter.

Placeholder: proposed-arch-profile (README "Measure and mock up before you cut" > "Flare profile").
Data: notes rear_arches.md, Guide-ready C1 (side-view template) and C3 (plan-view offsets); the README
text's station table, seam lines and door figures (fragments 0660, 0670, 0680, 0690), which win where
they differ; gap-fill notes gapfill_bmw_chassis_body.md Gap 6 (door gap 4 +-0.75 mm; BMW replaces the
whole side wall, so the seam lines are the guide's inference).
Side view and plan strip share one X scale; the plan strip's offsets are drawn 6x larger.
"""
import common as C
from common import w, catmull, poly
import kit

W = 800
NAME = "27-arch-profile.svg"
S = 0.40                    # px per mm, side view
XMIN, XMAX = -760, 470      # mm, view limits (behind .. ahead)
YMAX, YMIN = 670, -335
HX = 446                    # hub screen x
L = HX - S * (-XMIN)        # screen x of XMIN
TOP = 84                    # screen y of YMAX
HY = TOP + S * YMAX         # hub screen y
RX = HX + S * XMAX          # right edge of the side view
SK = 6 * S                  # plan strip: px per mm of offset (6x)
LH = 14                     # label line height (t-sm)

ARIA = (
    "Side view of the Touring's right rear quarter, drawn to scale from BMW drawings with the rear hub center as "
    "datum, and below it a top-view strip of how far the M3 skin stands out at each station along the car. The M3 "
    "flare stands about 21 to 23 mm proud of the Touring's skin from 300 mm ahead of the axle to 100 mm behind it, "
    "about 25 mm at 150 mm behind, 29 to 32 mm from 200 to 350 mm behind, then about 22, 13 and 10 mm at 400, 450 "
    "and 500 mm behind, and 7 mm at 600 mm behind. From about 150 to 220 mm behind the axle, below the bumper's top "
    "line at about 305 mm above the hub, the arch edge is the bumper cover, so the larger figures behind the axle "
    "are mostly the M3 bumper corner, not steel (inferred). The flare starts 380 to 420 mm ahead of the axle. The "
    "rear door meets the arch about 300 to 350 mm ahead of the axle and 150 to 250 mm above the hub, so the first "
    "part of the flare's ramp falls on the door, and with a stock door the M3 surface stands about 11 to 20 mm "
    "proud at the shut line: the M3 nose is beaten in over its last 60 to 100 mm. BMW's gap from rear door to side "
    "wall is 4 plus or minus 0.75 mm. The bulge's edge peaks about 475 mm above the hub over the axle, ends at the "
    "front about 315 mm ahead of the axle and 375 mm above the hub, and meets the bumper line about 300 mm behind "
    "the axle. The bulge blends in 470 to 530 mm "
    "above the hub, under the shoulder crease at about 540 mm; the arch edge is 340 to 350 mm above the hub at the "
    "top. Seam lines, our inference rather than a BMW procedure: top 500 to 515 mm above the hub; rear 550 to 600 "
    "mm behind the axle, down to about 250 mm above the hub behind the bumper; front 25 to 40 mm behind the shut "
    "line, parallel to it, down to the sill flange. The tail lamp starts about 700 mm behind the axle; the filler "
    "flap's position is approximate. Template stations: 400, 300 and 150 mm ahead, the axle, and 150, 300 and 450 "
    "mm behind. Figures are good to about 5 to 10 mm; confirm them with templates on both cars.")


def sx(x):
    return HX + S * x


def sy(y):
    return HY - S * y


def P(pts):
    return [(sx(x), sy(y)) for x, y in pts]


def lines(d, cls, x, y, rows, anchor=None, lh=LH):
    for i, s in enumerate(rows):
        d.text(cls, x, y + i * lh, s, anchor=anchor)


def build():
    d = kit.Doc()
    BOT = sy(YMIN)                 # bottom of the side view
    AX = BOT + 16                  # station axis line
    BASE = AX + 40                 # plan strip: the Touring's skin line
    VAL = BASE + SK * 32 + 22      # value row
    ZONE = VAL + 26                # zone brackets
    FOOT = ZONE + 50
    H = int(FOOT + 2 * 13 + 10)

    # ------------------------------------------------------------ heading and key
    d.text("t-h", 8, 20, "RIGHT REAR QUARTER, SIDE VIEW")
    d.text("t-xs", 776, 20, "front", anchor="end")
    d.line("ln", 780, 16, 794, 16, end="ah")
    d.text("t-sm", 8, 38, "Datum: the rear hub center. Sizes in mm, scaled from BMW drawings, ±5–10 mm: "
                          "confirm with templates on both cars.")
    x, y = 8, 60
    for cls, label in (("keep", "Your Touring"), ("donor", "M3 section and flare (donor)"),
                       ("panel", "Bumper, lamp, glass")):
        d.rect(cls, x, y - 10, 14, 12, rx=2, sw=1)
        d.text("t-sm", x + 20, y, label)
        x += 20 + w("t-sm", label) + 16
    d.rect("fab-f", x, y - 8.5, 22, 7, extra=' opacity="0.35"')
    d.line("fab-s dash", x, y - 5, x + 22, y - 5, sw=1.5)
    s = "Seam band (our inference)"
    d.text("t-sm", x + 28, y, s)
    x += 28 + w("t-sm", s) + 16
    d.line("crit-s", x, y - 4, x + 16, y - 4, sw=3)
    d.text("t-sm", x + 22, y, "Step at a stock door")

    # ------------------------------------------------------------ body panels (right side, mm)
    d.comment("Glass above the beltline")
    d.rect("panel", sx(XMIN), sy(YMAX), S * (XMAX - XMIN), S * (YMAX - C.BELT_Y))

    jy = C.junction_y()
    door_cut = C.door_cut_pts()                      # junction -> sill, round the arch
    sill_door_x = door_cut[-1][0]
    arch = C.ARCH
    i_bump = arch.index((-176, 305))
    upper_arch = arch[: i_bump + 1]                   # front (+364, 0) .. (-176, 305)
    rear_flank = arch[i_bump:]                        # (-176, 305) .. (-379, 0)

    d.comment("Quarter panel (yours): shut line, beltline, bumper line, arch, lip band in front of the arch")
    q = [(C.SHUT_X, C.BELT_Y), (XMIN, C.BELT_Y), (XMIN, C.BUMPER_Y)]
    q += list(reversed(upper_arch))
    q += [(366, C.SILL_Y), (sill_door_x, C.SILL_Y)]
    q += list(reversed(door_cut))
    d.path("keep", poly(P(q), close=True), sw=1.2)

    d.comment("Rear door (stock)")
    door = [(C.SHUT_X, C.BELT_Y), (XMAX, C.BELT_Y), (XMAX, C.SILL_Y), (sill_door_x, C.SILL_Y)]
    door += list(reversed(door_cut))
    d.path("shape", poly(P(door), close=True), sw=1.2)

    d.comment("Side skirt and rear bumper cover")
    d.path("panel", poly(P([(367, C.SILL_Y), (XMAX, C.SILL_Y), (XMAX, -130), (369, -130)]), close=True), sw=1)
    bump = [(-176, C.BUMPER_Y), (XMIN, C.BUMPER_Y), (XMIN, -130), (-383, -130)] + list(reversed(rear_flank))
    d.path("panel", poly(P(bump), close=True), sw=1.2)

    d.comment("Tail lamp: starts about 700 mm behind the axle")
    lx, l0, l1 = sx(C.LAMP_X), sy(C.LAMP_LOW), sy(548)
    d.path("panel", f"M{sx(XMIN):.1f},{l0:.1f} H{lx - 5:.1f} Q{lx:.1f},{l0:.1f} {lx:.1f},{l0 - 5:.1f} "
                    f"V{l1 + 5:.1f} Q{lx:.1f},{l1:.1f} {lx - 5:.1f},{l1:.1f} H{sx(XMIN):.1f} Z", sw=1.2)

    d.comment("Shoulder crease, about 540 mm above the hub")
    d.line("ln-thin", sx(C.LAMP_X), sy(C.CREASE_Y), sx(XMAX), sy(C.CREASE_Y))

    # ------------------------------------------------------------ M3 bulge (donor section)
    d.comment("M3 section: inside the seam centre lines, above the bumper line (tinted)")
    fm0, rm0 = C.SHUT_X - sum(C.FRONT_SEAM) / 2, C.R_DOOR - sum(C.FRONT_SEAM) / 2
    ym0, xm0 = sum(C.TOP_SEAM) / 2, sum(C.REAR_SEAM) / 2
    front_c0 = [(fm0, ym0), (fm0, C.junction_y(rm0, fm0))] + C.door_cut_pts(rm0, fm0)[1:]
    sec = [(xm0, ym0), (xm0, C.BUMPER_Y)] + list(reversed(upper_arch)) + \
        [(366, C.SILL_Y)] + list(reversed(front_c0))
    d.add(f'<path class="donor" d="{poly(P(sec), close=True)}" stroke-width="0" opacity="0.75"/>')

    d.comment("M3 bulge: between the arch edge and its styling line (notes C1); ends on the bumper line")
    edge = arch[2:i_bump + 1]                          # (307,177) .. (-176,305), front -> rear
    path = catmull(P(C.BULGE)) + " L" + catmull(P(list(reversed(edge))))[1:] + " Z"
    d.path("donor", path, sw=0)
    d.path("donor-s dash", catmull(P(C.BULGE)), sw=1.5)

    # ------------------------------------------------------------ filler flap (right side, generic position)
    fx0, fx1, fy0, fy1 = C.FLAP
    d.rect("donor", sx(fx0), sy(fy1), S * (fx1 - fx0), S * (fy1 - fy0), rx=6, sw=1.2)

    # ------------------------------------------------------------ arch edge, wheel, hub datum
    d.comment("Arch edge (both cars), wheel and hub datum")
    d.path("ln", catmull(P(arch)), sw=2)
    d.path("ln", poly(P([(364, 0), (366, C.SILL_Y), (369, -130)])), sw=2)
    d.path("ln", poly(P([(-379, 0), (-383, -130)])), sw=2)
    d.circle("ln", HX, HY, S * C.TYRE_R, sw=1.5)
    d.circle("ln-thin", HX, HY, S * C.RIM_R)
    d.line("ln-thin", HX - 12, HY, HX + 12, HY)
    d.line("ln-thin", HX, HY - 12, HX, HY + 12)
    d.dot("fill-fg", HX, HY, 3)
    d.text("t-sm t-b", HX, HY + 26, "datum: hub center", anchor="middle")

    # ------------------------------------------------------------ seams (our inference)
    d.comment("Seams: top 500-515 above the hub; rear 550-600 behind; front 25-40 behind the shut line")
    fs_out, fs_in = C.SHUT_X - C.FRONT_SEAM[0], C.SHUT_X - C.FRONT_SEAM[1]
    xr0, xr1 = C.REAR_SEAM
    y0, y1 = C.TOP_SEAM
    d.rect("fab-f", sx(xr1), sy(y1), sx(fs_in) - sx(xr1), S * (y1 - y0), extra=' opacity="0.35"')
    d.rect("fab-f", sx(xr0), sy(y1), S * (xr1 - xr0), S * (y1 - C.BUMPER_Y), extra=' opacity="0.35"')
    d.rect("fab-f", sx(xr0), sy(C.BUMPER_Y), S * (xr1 - xr0), S * (C.BUMPER_Y - C.REAR_SEAM_LOW),
           extra=' opacity="0.15"')
    rin, rout = C.R_DOOR - C.FRONT_SEAM[1], C.R_DOOR - C.FRONT_SEAM[0]
    seam_out, seam_in = C.door_cut_pts(rout, fs_out), C.door_cut_pts(rin, fs_in)
    fband = [(fs_out, y1), (fs_out, C.junction_y(rout, fs_out))] + seam_out[1:] + \
        list(reversed(seam_in[1:])) + [(fs_in, C.junction_y(rin, fs_in)), (fs_in, y1)]
    d.add(f'<path class="fab-f" d="{poly(P(fband), close=True)}" opacity="0.35"/>')
    ym, xm = (y0 + y1) / 2, (xr0 + xr1) / 2
    fm, rm = C.SHUT_X - sum(C.FRONT_SEAM) / 2, C.R_DOOR - sum(C.FRONT_SEAM) / 2
    d.path("fab-s dash", poly(P([(fm, ym), (xm, ym), (xm, C.BUMPER_Y)])), sw=2)
    d.path("fab-s dash", poly(P([(xm, C.BUMPER_Y), (xm, C.REAR_SEAM_LOW)])), sw=1.2)
    d.path("fab-s dash", poly(P([(fm, ym), (fm, C.junction_y(rm, fm))] + C.door_cut_pts(rm, fm)[1:])), sw=2)

    # ------------------------------------------------------------ shut line and the step at a stock door
    d.comment("Door shut line: vertical, then round the arch (door's cut edge, drawn generically)")
    d.path("ln", poly(P([(C.SHUT_X, C.BELT_Y), (C.SHUT_X, jy)] + door_cut[1:])), sw=1.5)
    d.path("crit-s", poly(P([(C.SHUT_X, jy + 4), (C.SHUT_X, 380)])), sw=3)
    # nose blend: the last 60-100 mm before the shut line
    yb = 452
    d.line("crit-s", sx(C.SHUT_X - 100), sy(yb), sx(C.SHUT_X), sy(yb), sw=1.5)
    d.line("crit-s", sx(C.SHUT_X - 100), sy(yb) - 4, sx(C.SHUT_X - 100), sy(yb) + 4, sw=1.5)
    d.line("crit-s", sx(C.SHUT_X - 60), sy(yb) - 4, sx(C.SHUT_X - 60), sy(yb) + 4, sw=1.5)
    d.circle("ln-thin dash", sx(C.SHUT_X), sy(jy), 7)

    # ------------------------------------------------------------ height ruler (right)
    d.comment("Heights above the hub")
    rx = RX + 12
    d.line("ln-thin", rx, sy(0), rx, sy(600))
    d.text("t-xs", rx - 2, sy(600) - 8, "mm above the hub")
    for t in (0, 305, 345, 540):
        d.line("ln-thin", rx - 5, sy(t), rx, sy(t))
    d.rect("fab-f", rx - 3, sy(515), 6, S * 15, extra=' opacity="0.7"')
    d.line("donor-s", rx + 5, sy(470), rx + 5, sy(530), sw=3)
    ruler = [(540, 554, "540  shoulder crease"), (507.5, 519, "500–515  top seam"),
             (500, 484, "470–530  bulge blends in"), (345, 352, "340–350  arch edge, top"),
             (305, 304, "305  bumper top line")]
    for ty, ly, s in ruler:
        yy = sy(ly) + 4
        d.line("ln-thin", rx + 7, sy(ty), rx + 14, yy - 4)
        d.text("t-sm", rx + 17, yy, s)

    # ------------------------------------------------------------ door labels (right column)
    cx = rx + 6
    d.comment("Door labels")
    d.text("t-xs", (sx(C.SHUT_X) + RX) / 2, sy(600), "rear door", anchor="middle")
    y = sy(305) + 26
    lines(d, "t-sm crit-t t-b", cx, y, ["Stock door: M3 surface"])
    lines(d, "t-sm crit-t", cx, y + LH, ["≈11–20 mm proud at the", "shut line; beat the nose in",
                                          "over its last 60–100 mm"])
    d.path("ln-thin", poly([(cx - 3, y - 4), (sx(C.SHUT_X) + 3, sy(300))]))
    y2 = y + 4 * LH + 6
    lines(d, "t-sm", cx, y2, ["Door meets the arch", "≈300–350 ahead, 150–250", "up (±50 mm: measure)"])
    d.path("ln-thin", poly([(cx - 3, y2 - 4), (sx(C.SHUT_X) + 7, sy(jy) + 2)]))
    y3 = y2 + 3 * LH + 6
    lines(d, "t-sm", cx, y3, ["Shut line: BMW gap", "4 ± 0.75 mm, parallel", "within 1 mm"])
    gx = (C.R_DOOR ** 2 - (120 - C.ARC_C[1]) ** 2) ** 0.5
    d.path("ln-thin", poly([(cx - 3, y3 - 4), (sx(gx) + 2, sy(120))]))
    y4 = y3 + 3 * LH + 6
    lines(d, "t-sm fab-t", cx, y4, ["Front seam: 25–40 mm", "behind the shut line and", "parallel to it, down to",
                                    "the sill flange"])
    fx = (rm ** 2 - (0 - C.ARC_C[1]) ** 2) ** 0.5
    d.path("ln-thin", poly([(cx - 3, y4 - 4), (sx(fx) + 3, sy(0))]))

    # ------------------------------------------------------------ rear labels (left column and bumper)
    d.comment("Rear labels")
    lines(d, "t-sm", 8, sy(620) + 4, ["Tail lamp starts", "≈700 mm behind"])
    d.path("ln-thin", poly([(100, sy(620) + 10), (sx(C.LAMP_X) - 3, sy(520))]))
    yr = sy(470)
    lines(d, "t-sm fab-t", 8, yr, ["Rear seam: 550–600", "behind the axle, to", "≈250 above the hub"])
    d.path("ln-thin", poly([(122, yr - 4), (sx(xm) - 3, sy(440))]))
    yb2 = yr + 3 * LH + 12
    lines(d, "t-sm", 8, yb2, ["Bulge meets the", "bumper line ≈300", "mm behind the axle"])
    d.path("ln-thin", poly([(114, yb2 - 4), (sx(-306) - 3, sy(306) - 1)]))
    yb3 = yb2 + 3 * LH + 12
    lines(d, "t-sm", 8, yb3, ["Bumper cover forms", "the arch edge from", "≈150–220 mm behind",
                              "the axle (inferred)"])
    d.path("ln-thin", poly([(122, yb3 - 4), (sx(C.arch_x_at(170)) - 3, sy(170))]))
    yf = sy(612) + 2
    lines(d, "t-sm", sx(-560), yf, ["Filler flap, right side: position approx. Where the top seam would",
                                    "cross its surround, step the seam up round it."])
    d.path("ln-thin", poly([(sx(-380), yf + LH + 5), (sx(-380), sy(fy1) - 1)]))
    lines(d, "t-sm donor-t", sx(20), HY - 162, ["M3 bulge, edge ≈475", "(front end ≈375 up, 315 ahead)"],
          anchor="middle")

    # ------------------------------------------------------------ station axis
    d.comment("Stations along the car")
    d.line("ln-thin", sx(-700), AX, sx(400), AX)
    for xs in range(-700, 401, 100):
        d.line("ln-thin", sx(xs), AX, sx(xs), AX + 4)
    for xs in (-700, -600, -500, -400, -300, -200, -100, 100, 200, 300, 400):
        d.text("t-xs", sx(xs), AX + 15, str(abs(xs)), anchor="middle")
    d.text("t-xs t-b", sx(0), AX + 15, "axle", anchor="middle")
    d.text("t-xs", sx(-700) - 14, AX + 15, "← behind", anchor="end")
    d.text("t-xs", sx(400) + 14, AX + 15, "ahead →")
    for xs in (400, 300, 150, 0, -150, -300, -450):
        d.path("fill-fg", f"M{sx(xs):.1f},{AX - 1} l-3.5,-6 h7 Z")
    d.path("fill-fg", f"M{12:.1f},{AX - 1} l-3.5,-6 h7 Z")
    d.text("t-xs", 20, AX - 1, "template station")

    # ------------------------------------------------------------ plan strip
    d.comment("Plan view: M3 skin proud of the Touring's, offsets drawn 6x")
    lines(d, "t-sm t-b", 8, BASE + 16, ["Seen from above:"])
    lines(d, "t-sm", 8, BASE + 16 + LH, ["M3 skin proud of the", "Touring's, mm", "(offsets drawn 6×)"])
    d.line("keep-s", sx(-700), BASE, sx(XMAX), BASE, sw=2)
    d.text("t-xs", sx(XMAX), BASE - 5, "Touring skin, stock door", anchor="end")
    split = -185
    steel = [(C.SHUT_X, C.offset_at(C.SHUT_X))] + [(x, o) for x, o in C.OFFSETS if split <= x < C.SHUT_X] + \
        [(split, C.offset_at(split))]
    bumpz = [(split, C.offset_at(split))] + [(x, o) for x, o in C.OFFSETS if x < split]
    door_part = [(x, o) for x, o in C.OFFSETS if x > C.SHUT_X] + [(C.SHUT_X, C.offset_at(C.SHUT_X))]
    d.path("donor", poly([(sx(C.SHUT_X), BASE)] + [(sx(x), BASE + SK * o) for x, o in steel] +
                         [(sx(split), BASE)], close=True), sw=0)
    d.path("panel", poly([(sx(split), BASE)] + [(sx(x), BASE + SK * o) for x, o in bumpz] +
                         [(sx(bumpz[-1][0]), BASE)], close=True), sw=0)
    d.path("donor-s", poly([(sx(x), BASE + SK * o) for x, o in steel]), sw=2)
    d.path("donor-s dash", poly([(sx(x), BASE + SK * o) for x, o in bumpz]), sw=2)
    d.path("donor-s dash", poly([(sx(x), BASE + SK * o) for x, o in door_part]), sw=1.2)
    for x, o in C.OFFSETS[1:]:
        d.dot("donor-f", sx(x), BASE + SK * o, 2.2)
    so = C.offset_at(C.SHUT_X)
    d.line("crit-s", sx(C.SHUT_X), BASE, sx(C.SHUT_X), BASE + SK * so, sw=3)
    # flare start and step labels, right of the strip
    lines(d, "t-sm", RX + 8, BASE + 16, ["Flare starts 380–420", "ahead: its first", "50–100 mm is on", "the door"])
    d.path("ln-thin", poly([(RX + 5, BASE + 12), (sx(420) + 3, BASE + 2)]))
    lines(d, "t-sm crit-t", RX + 8, BASE + 16 + 4 * LH + 6, ["Step ≈11–20 mm"])
    d.path("ln-thin", poly([(RX + 5, BASE + 16 + 4 * LH + 2), (sx(C.SHUT_X) + 3, BASE + SK * so - 8)]))

    vals = [(350, "16"), (-150, "25"), (-400, "22"), (-450, "13"), (-500, "10"), (-600, "7")]
    for x, s in vals:
        d.text("t-sm", sx(x), VAL, s, anchor="middle")
    d.text("t-sm", sx(400) + 4, VAL, "0–9", anchor="middle")
    d.text("t-sm t-b", sx(100), VAL, "21–23", anchor="middle")
    d.text("t-sm t-b", sx(-275), VAL, "29–32", anchor="middle")
    d.text("t-xs", 8, VAL, "mm proud:")

    def bracket(x0, x1, cls, label, tcls="t-sm"):
        a, b = sx(x0), sx(x1)
        d.path(cls, f"M{a:.1f},{ZONE - 9} V{ZONE - 5} H{b:.1f} V{ZONE - 9}", sw=1.2)
        lines(d, tcls, (a + b) / 2, ZONE + 9, label, anchor="middle")

    bracket(C.SHUT_X, split + 3, "donor-s", ["M3 steel flare: over the axle", "the lip moves out ≈21 mm"])
    bracket(split - 3, -600, "ln-thin", ["Mostly the M3 bumper corner,", "not steel (inferred)"])

    # ------------------------------------------------------------ footer
    lines(d, "t-xs", 8, FOOT, [
        "BMW has no arch section: it replaces a Touring's whole side wall (TIS 41 35 101). These seam lines are our "
        "inference from the drawings: move one where the",
        "two cars' templates disagree by more than 1 mm. The door/arch junction (±50 mm) and the filler flap's "
        "position are estimates: measure them on the car.",
        "The front seam's path round the arch is drawn generically."], lh=13)
    return kit.svg_open(W, H, ARIA), d.body()


if __name__ == "__main__":
    print(C.run(build, NAME))
