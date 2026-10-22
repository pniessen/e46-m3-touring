#!/usr/bin/env python3
"""Figure 29 (diagrams/29-floor-exhaust-plan.svg), placeholder proposed-floor-exhaust-plan.

Plan view of the rear floor from below, front at the top (so the car's left is on the right of
the drawing). Positions in mm from datum O (midway between the rear subframe rear-mount bolt
centers), X rearward, Y left (+). Sources:
- research_notes/.../rear_floor_exhaust.md, Diagram-ready data, Figure A (all (E) estimates,
  +-50-100 mm), except as noted below;
- TIS 41 00 control dimensions (gapfill_bmw_chassis_body.md, Gap 6 item 6): rear axle carrier
  mounts E-E 440 and F-F 660. Only the 660 pair can sit beside the rails with a 620 mm well
  between them, so the rear mounts are drawn at Y +-330 (not the notes' +-430 estimate), and
  the rails at about Y +-400..450 so the mounts fall inside CMP's 120 mm strip. That also lets
  the canister fit between the well and the right rail, under the battery box.
- README fragment 0470 for every label and part number.
"""
from floorkit import Fig, build, svg_open, write

S = 0.2            # px per mm
CX = 200           # image x of Y = 0
XTOP = -360        # X at y = Y0
Y0 = 88
DY = Y0 - 74      # margin labels were laid out for Y0 = 74
W = 400


def px(Y):         # car Y (+ = left) -> image x; seen from below, the car's left is on the right
    return CX + S * Y


def py(X):         # car X (+ = rearward) -> image y
    return Y0 + (X - XTOP) * S


def P(X, Y):
    return px(Y), py(X)


# ---- geometry, mm ------------------------------------------------------------------------
RAIL_IN, RAIL_OUT = 400, 450          # rails (rear side members), (E), see docstring
MOUNT_Y = 330                         # rear mounts, TIS F-F 660
SEAM_X = 20
WELL_C, WELL_R = (330, 0), 310        # Touring well, 620 mm (M), centre (E)
MUF = (380, 720, 500)                 # muffler X0, X1, half-width (E)
SHIELD_OFF = 20
REAR_PANEL_X = 730
BUMPER_X = 845
CMP = 120                              # CMP's strip width (P); length drawn generic (100 mm)
CMP_X1 = 140
DIFF = (-270, 60, 130)                # diff body X0, X1, half-width (generic)
M3CAN = (90, 220, 250)                # M3 canister X0, X1, half-width (E)
TCAN = (150, 450, 315, 395)           # Touring canister X0, X1, Y in/out (E, see docstring)
BATT = (120, 420, 320, 480)           # battery box (cargo side) X0, X1, Y in/out (E)
TIPS = (395, 465)                      # tip centres, |Y| (E)
TIP_W = 60
H1 = (410, 440)                        # schematic; real positions are recorded on the donor
H2 = (690, 440)
H3 = (550, -440)
XBOT = 880

ARIA = (
    "Plan view of the Touring's rear floor from below, front at the top, so the car's left is on "
    "the right of the drawing. Positions are approximate, within about 50 to 100 mm, in millimetres "
    "from datum O, the midpoint between the bolt centers of the rear subframe's two rear mounts, with "
    "X rearward and Y left or right; nobody publishes them, so you record the donor's first. The RACP "
    "joins the trunk floor along a seam about 20 mm behind the mounts, and the floor runs back between "
    "the two rails to the rear panel at about X 730; the bumper face is at about X 845. Your Touring's "
    "620 mm spare-wheel well, centred about 330 mm behind O, comes out with the whole floor panel, and "
    "CMP's 120 mm access strip beside each rail, at the front of the well, lies inside it. The new M3 "
    "trunk floor 41127895619 fills the same outline on the same flanges, with reinforcement 51717894229 "
    "along its front edge. The M3 muffler 18107831783, 26.7 kg, spans about X 380 to 720 and nearly the "
    "full width, under its heat shield 51482494848, with its twin inlets at the front left and four tips "
    "at the bumper. It hangs on three stud plates: H1, front left, 41112497585, already on your Touring; "
    "H2, rear left, 41122494844, which replaces your 41118204223; and H3, 41112493931, on the right rail. "
    "The M3 pipes run back from the tunnel, under tunnel shield 51487893366, past the left of the M3 diff. "
    "Your canister and leak-test pump run fore and aft at the right rear, between the battery box and "
    "the well, where the muffler's right end will likely come within 25 mm. With the M3 floor, expect "
    "the M3 holder: if the canister is under 25 mm from the muffler or H3, fit holder 16132229735 and "
    "cover 51717893604 at the donor's position, across the car just behind the diff; at 25 mm or more, "
    "either layout works."
)


def make():
    d = Fig()

    # ---------------- header ----------------
    d.text("t-h", 8, 20, "REAR FLOOR, SEEN FROM BELOW")
    d.text("t-xs", 380, 20, "front", "end")
    d.line("ln", 388, 22, 388, 9, end="ah")
    d.text("t-xs", 8, 37, "Front at the top, so the car's left is on your right.")
    d.text("t-xs t-b", 8, 51, "All positions approximate (±50–100 mm), in mm from datum O.")
    d.text("t-xs t-b", 8, 74, "RIGHT SIDE")
    d.text("t-xs t-b", 392, 74, "LEFT SIDE", "end")

    xtop_px = py(-400)

    # ---------------- floor and body ----------------
    d.comment("Underbody and floor, seen from below")
    d.rect("panel", px(-520), xtop_px, px(520) - px(-520), py(REAR_PANEL_X) - xtop_px)
    # the new M3 floor fills the panel between the flanges: RACP seam, both rails, rear panel
    d.rect("new", px(-RAIL_IN), py(SEAM_X), px(RAIL_IN) - px(-RAIL_IN), py(REAR_PANEL_X) - py(SEAM_X), sw=1.5)

    # battery box, in the cargo area (above the floor): dashed
    bx0, bx1, by_in, by_out = BATT
    d.rect("keep-s dash", px(-by_out), py(bx0), px(-by_in) - px(-by_out), py(bx1) - py(bx0), sw=1.2)

    # CMP's access strips: 120 mm from each rail's inner edge, at the front of the well
    for sgn in (-1, 1):
        xa, xb = sorted((px(sgn * (RAIL_IN - CMP)), px(sgn * RAIL_IN)))
        d.rect("fab-f", xa, py(SEAM_X), xb - xa, py(CMP_X1) - py(SEAM_X), extra=' opacity="0.16"')
        d.hatch("fab-s", xa, py(SEAM_X), xb, py(CMP_X1), step=4.5, sw=0.9)

    # Touring well, visible part (the muffler hides its rear half)
    wcx, wcy = P(*WELL_C)
    r = WELL_R * S
    ycut = py(MUF[0])
    dx = (r * r - (ycut - wcy) ** 2) ** 0.5
    d.path("fab-s dash", f"M{wcx - dx:.1f},{ycut:.1f} A{r:.1f},{r:.1f} 0 1 1 {wcx + dx:.1f},{ycut:.1f}", sw=1.6)

    # rails
    for sgn in (-1, 1):
        xa, xb = sorted((px(sgn * RAIL_IN), px(sgn * RAIL_OUT)))
        d.rect("keep", xa, xtop_px, xb - xa, py(REAR_PANEL_X) - xtop_px, sw=1)

    # RACP seam, front reinforcement, rear panel
    d.line("ln", px(-RAIL_IN), py(SEAM_X), px(RAIL_IN), py(SEAM_X), sw=1.5)
    d.rect("new-f", px(-320), py(SEAM_X), px(320) - px(-320), 30 * S)
    d.rect("keep", px(-500), py(REAR_PANEL_X), px(500) - px(-500), 4, sw=1)

    # rear subframe rear mounts
    for sgn in (-1, 1):
        d.circle("shape", px(sgn * MOUNT_Y), py(0), 7)
        d.dot("fill-fg", px(sgn * MOUNT_Y), py(0), 1.6)

    # ---------------- things that hang below ----------------
    # tunnel shield (in the tunnel, over the pipes) and the twin pipes
    d.rect("donor", px(-110), xtop_px, px(110) - px(-110), py(-310) - xtop_px, sw=1.2)
    d.comment("twin M3 pipes: tunnel -> past the left of the diff -> muffler's front-left inlets")
    xa_, xb_ = px(-60), px(60)
    xa2, xb2 = px(180), px(225)
    yb0, yb1 = py(-380), py(-300)
    for x0, x2 in ((xa_, xa2), (xb_, xb2)):
        d.path("donor-s", f"M{x0:.1f},{xtop_px:.1f} V{yb0:.1f} C{x0:.1f},{yb0 + 9:.1f} {x2:.1f},{yb1 - 9:.1f} "
               f"{x2:.1f},{yb1:.1f} V{py(MUF[0]):.1f}", sw=2)

    # M3 diff
    d.rect("donor", px(-DIFF[2]), py(DIFF[0]), px(DIFF[2]) - px(-DIFF[2]), py(DIFF[1]) - py(DIFF[0]), rx=8, sw=1.5)

    # datum: line through the rear-mount bolts, and O
    d.line("ln-thin dash", px(-MOUNT_Y) + 7, py(0), px(MOUNT_Y) - 7, py(0))
    ox, oy = P(0, 0)
    d.line("ln", ox - 5, oy, ox + 5, oy, sw=1.3)
    d.line("ln", ox, oy - 5, ox, oy + 5, sw=1.3)

    # M3 canister position (an option): across the car, just behind the diff
    d.capsule("donor dash", px(-M3CAN[2]), py(M3CAN[0]), px(M3CAN[2]), py(M3CAN[1]), sw=1.4)

    # your canister + leak-test pump, fore and aft at the right rear (runs under the muffler's end)
    c0, c1, cin, cout = TCAN
    d.capsule("keep", px(-cout), py(c0), px(-cin), py(c1), sw=1.4)

    # heat shield outline, then the muffler on top
    m0, m1, mh = MUF
    d.rect("donor-s dash", px(-mh - SHIELD_OFF), py(m0 - SHIELD_OFF), px(mh + SHIELD_OFF) - px(-mh - SHIELD_OFF),
           py(m1 + SHIELD_OFF) - py(m0 - SHIELD_OFF), rx=9, sw=1.2)
    d.rect("donor", px(-mh), py(m0), px(mh) - px(-mh), py(m1) - py(m0), rx=8, sw=1.5)

    # tips and bumper face
    for yc in TIPS:
        for sgn in (-1, 1):
            d.rect("donor", px(sgn * yc) - TIP_W * S / 2, py(m1), TIP_W * S, py(860) - py(m1), rx=2, sw=1)
    d.line("ln", px(-520), py(BUMPER_X), px(520), py(BUMPER_X), sw=2.5)

    # hangers: stud plate with two M8 studs
    for (hx, hy), cls in ((H1, "keep"), (H2, "new"), (H3, "new")):
        x, y = P(hx, hy)
        d.rect(cls, x - 6, y - 4.5, 12, 9, rx=1.5, sw=1.2)
        d.dot("fill-fg", x - 2.8, y, 1.3)
        d.dot("fill-fg", x + 2.8, y, 1.3)

    # likely clash: your canister's rear end against the muffler's right end
    clx, cly = px(-(cin + cout) / 2), py(m0) + 3
    d.circle("crit-s dash", clx, cly, 8.5, sw=1.6)

    # ---------------- labels in the drawing ----------------
    d.text("t-xs donor-t", px(0), py(-150), "M3 diff", "middle")
    d.text("t-xs t-b", ox + 4, oy - 4, "O")
    d.text("t-xs donor-t", px(-40), py(155) + 3.5, "M3 canister", "middle")
    d.label(px(-60), py(M3CAN[1]) + 12, [("t-xs fab-t", "your well, Ø 620:"), ("t-xs fab-t", "comes out")], "middle")
    d.label(px(0), py(m0) + 19, [("t-xs donor-t", [(None, "M3 muffler "), ("t-mono", "18107831783")]),
                                 ("t-xs donor-t", "26.7 kg, X ≈ +380 to +720"),
                                 ("t-xs donor-t", [(None, "shield "), ("t-mono", "51482494848"), (None, " above it")])],
            "middle", pitch=13.5)
    d.text("t-xs", px(0), py(REAR_PANEL_X) + 15, "rear panel, X ≈ +730", "middle")
    d.text("t-xs", px(0), py(BUMPER_X) + 13, "bumper face, X ≈ +845", "middle")

    # ---------------- margin labels, car's right (left of the drawing) ----------------
    LX = 90
    d.label(LX, 79 + DY, [("t-xs donor-t", "tunnel shield"), ("t-xs donor-t t-mono", "51487893366")], "end",
            leader=(px(-110), 80 + DY))
    d.label(LX, 128 + DY, [("t-xs", "rear mount")], "end", leader=(px(-MOUNT_Y) - 7, py(0) - 2))
    d.label(LX, 152 + DY, [("t-xs fab-t", "CMP's 120 mm"), ("t-xs fab-t", "access strip")], "end",
            leader=(px(-(RAIL_IN - 40)), py(60)))
    d.label(LX, 190 + DY, [("t-xs", "battery box"), ("t-xs", "(cargo side)")], "end", leader=(px(-470), py(200)))
    d.label(LX, 226 + DY, [("t-xs", "your canister"), ("t-xs", "+ leak-test pump")], "end",
            leader=(px(-cout) + 1, py(300)))
    d.label(LX, 262 + DY, [("t-xs crit-t", "likely clash:"), ("t-xs crit-t", "check 25 mm")], "end",
            leader=(clx - 8.5, cly + 2))
    d.label(LX, 296 + DY, [("t-xs t-b new-t", "H3, right rail"), ("t-xs new-t t-mono", "41112493931")], "end",
            leader=(px(H3[1]) - 6, py(H3[0])))
    d.label(LX, 322 + DY, [("t-xs donor-t", "4 tips, in the"), ("t-xs donor-t", "bumper cut-outs")], "end",
            leader=(px(-TIPS[1]) - 4, py(800)))

    # ---------------- margin labels, car's left (right of the drawing) ----------------
    RX = 310
    d.label(RX, 84 + DY, [("t-xs donor-t", "twin M3 pipes")], leader=(px(225) + 1, py(-250)))
    d.label(RX, 128 + DY, [("t-xs", "rear mount")], leader=(px(MOUNT_Y) + 7, py(0) - 2))
    d.label(RX, 152 + DY, [("t-xs", "RACP seam,"), ("t-xs", "X ≈ +20")], leader=(px(260), py(SEAM_X)))
    d.label(RX, 186 + DY, [("t-xs new-t", "reinforcement"), ("t-xs new-t t-mono", "51717894229")],
            leader=(px(300), py(SEAM_X) + 4))
    d.label(RX, 220 + DY, [("t-xs new-t", "M3 floor"), ("t-xs new-t t-mono", "41127895619")],
            leader=(px(380), py(215)))
    d.label(RX, 254 + DY, [("t-xs t-b", "H1, front-left"), ("t-xs t-mono", "41112497585"), ("t-xs", "already fitted")],
            leader=(px(H1[1]) + 6, py(H1[0])))
    d.label(RX, 290 + DY, [("t-xs t-b new-t", "H2, rear-left"), ("t-xs new-t t-mono", "41122494844"),
                      ("t-xs", "replaces your"), ("t-xs t-mono", "41118204223")],
            leader=(px(H2[1]) + 6, py(H2[0])))

    # ---------------- key and notes ----------------
    ky = 372 + DY - 14
    d.line("ln-faint", 8, ky - 12, 392, ky - 12)
    d.rect("keep", 8, ky, 12, 12, rx=2)
    d.text("t-sm", 26, ky + 10.5, "Your Touring's, kept")
    d.rect("new", 206, ky, 12, 12, rx=2)
    d.text("t-sm", 224, ky + 10.5, "Buy new (BMW)")
    ky += 18
    d.rect("donor", 8, ky, 12, 12, rx=2)
    d.text("t-sm", 26, ky + 10.5, "M3 part, from the donor")
    d.rect("fab-s dash", 206, ky, 12, 12, rx=2, sw=1.6)
    d.text("t-sm", 224, ky + 10.5, "Comes out")
    ky += 18
    d.rect("fab-f", 8, ky, 12, 12, extra=' opacity="0.16"')
    d.hatch("fab-s", 8, ky, 20, ky + 12, step=4.5, sw=0.9)
    d.text("t-sm", 26, ky + 10.5, "CMP's access strip")
    d.circle("crit-s dash", 212, ky + 6, 6, sw=1.6)
    d.text("t-sm", 224, ky + 10.5, "Check at the mock-up")

    ny = ky + 26
    lines = [
        "Datum O: midway between the rear-mount bolt centers. X runs",
        "rearward, Y left (+) or right (−). Nobody publishes these positions:",
        "record your donor's, then set each hanger stud within ±3 mm of its",
        "X and Y. Which BMW plate is which isn't confirmed, so go by position.",
    ]
    d.rect("warn-f", 8, ny, 384, 12 + 14 * 7 + 2, rx=5)
    yy = ny + 17
    for s in lines[:4]:
        d.text("t-sm fill-fg", 18, yy, s)
        yy += 14
    # canister rule, worded as in figure 34 and README 0470/0540 (review F4)
    d.text("t-sm fill-fg", 18, yy, "M3 floor: expect the M3 holder. Canister under 25 mm from the")
    yy += 14
    d.rich("t-sm fill-fg", 18, yy, [(None, "muffler or H3: fit holder "), ("t-mono", "16132229735"), (None, " and cover "),
                                    ("t-mono", "51717893604")])
    yy += 14
    d.text("t-sm fill-fg", 18, yy, "at the donor's position; 25 mm or more: either layout works.")
    H = int(ny + 12 + 14 * 7 + 2 + 8)
    return d, H


def main():
    d, H = build(make)
    head = svg_open(W, H, ARIA)
    p = write("29-floor-exhaust-plan.svg", head, d.body())
    print("wrote", p, "height", H)


if __name__ == "__main__":
    main()
