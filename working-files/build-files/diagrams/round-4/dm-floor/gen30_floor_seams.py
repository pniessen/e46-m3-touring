#!/usr/bin/env python3
"""Figure 30 (diagrams/30-floor-seams.svg), placeholder proposed-floor-seams. Portrait.

1  plan from the cargo side: drill-out rows along the RACP seam, both rails and the rear panel;
2  two sections: drill and split so the well drops out downward; the new floor goes up from
   below and is plug-welded down-hand through the same holes;
3  inset: one flange joint (8 mm hole, 10-13 mm face, no more than 3 mm high, at least 25 mm
   apart at the factory spot-weld positions, gap 1 mm or less, weld-through primer kept out of
   the weld spot, paint off about 30 mm round each weld, sealer on both faces);
4  inset: the flangeless lap (joggle, 12-15 mm overlap, 8 mm plugs in the top layer at
   25-40 mm pitch, short stitches, sealed both faces).
Every value is from README fragments 0470 and 0480 (the text wins over the notes).
"""
from floorkit import Fig, build, svg_open, write

W = 400

ARIA = (
    "How the Touring's floor comes out and the M3 floor goes in, in four parts. One: seen from the "
    "cargo side, the floor panel and its spare-wheel well are spot-welded under three sets of body "
    "flanges, the RACP seam across the front, both rails and the rear panel; you drill every spot "
    "weld from above with an 8 mm (5/16 in) cutter through the flange only, after counting each row "
    "and measuring its pitch, and you never cut or grind through a flange. Two: you split the layers "
    "from below with a spot-weld chisel and the well drops out downward; the new floor goes up from "
    "below, clamped or clecoed at every hole, and you plug-weld it down-hand from above through the "
    "same holes. Three: at each flange joint the 8 mm hole in the Touring's flange is filled with a "
    "plug weld whose face is 10 to 13 mm across and no more than 3 mm high, at the factory spot-weld "
    "positions and at least 25 mm (1 in) apart; the layers touch, with a gap of 1 mm or less; paint "
    "comes off about 30 mm round each weld on both faces, weld-through primer goes between the layers "
    "but not in the weld spot, and seam sealer goes on both faces. Four: where a joint has no flange, "
    "on a partial graft or a flat panel, one edge is joggled and the panels lap by about 12 to 15 mm, "
    "with 8 mm plug welds through the top layer at 25 to 40 mm pitch plus short stitches, sealed on "
    "both faces."
)


def head(d, y, num, text, sub=None):
    d.text("t-h", 8, y, f"{num}  {text}")
    if sub:
        d.text("t-xs", 392, y, sub, "end")


def make():
    d = Fig()

    # ================= 1  plan from the cargo side =================
    head(d, 20, "1", "DRILL OUT FROM ABOVE")
    d.text("t-xs", 8, 36, "Cargo side, front at the top")
    d.text("t-xs", 380, 20, "front", "end")
    d.line("ln", 388, 22, 388, 9, end="ah")

    S = 0.19
    cx, ytop = 98, 50            # plan centre x; y of X = -120

    def px(Y):
        return cx + S * Y

    def py(X):
        return ytop + (X + 120) * S

    # RACP (ahead of the seam) and the floor panel that comes out
    d.rect("panel", px(-400), py(-120), px(400) - px(-400), py(20) - py(-120))
    d.text("t-xs", cx, py(-50) + 4, "RACP", "middle")
    d.rect("fab dash", px(-400), py(20), px(400) - px(-400), py(730) - py(20), sw=1.5)
    d.circle("fab-s dash", px(0), py(330), 310 * S, sw=1.4)
    d.text("t-xs fab-t", cx, py(300) + 1, "floor and", "middle")
    d.text("t-xs fab-t", cx, py(300) + 13.5, "well come out,", "middle")
    d.text("t-xs fab-t", cx, py(300) + 26, "downward", "middle")
    d.line("fab-s", cx, py(300) + 32, cx, py(300) + 52, sw=1.5, end="ahf")

    # rails and rear panel (kept)
    for sgn in (-1, 1):
        xa, xb = sorted((px(sgn * 400), px(sgn * 450)))
        d.rect("keep", xa, py(-120), xb - xa, py(760) - py(-120), sw=1)
    d.rect("keep", px(-450), py(730), px(450) - px(-450), py(760) - py(730), sw=1)
    d.line("ln", px(-400), py(20), px(400), py(20), sw=1.5)

    # spot-weld rows to drill: RACP seam, both rails (inner flanges), rear panel
    pitch = 8.0
    xs = []
    x = px(-385)
    while x <= px(385) + 0.1:
        xs.append(x)
        x += pitch
    for x in xs:
        d.dot("fab-f", x, py(20), 1.7)
        d.dot("fab-f", x, py(738), 1.7)
    y = py(40)
    while y <= py(715) + 0.1:
        d.dot("fab-f", px(-408), y, 1.7)
        d.dot("fab-f", px(408), y, 1.7)
        y += pitch

    # labels, right
    LX = 210
    d.label(LX, 62, [("t-sm t-b", "Spot-weld rows along every"), ("t-sm t-b", "flange: the RACP seam, both"),
                     ("t-sm t-b", "rails and the rear panel")], leader=(px(392) + 4, py(20) - 2))
    d.label(LX, 116, [("t-sm fab-t", "Drill each one from above with"),
                      ("t-sm fab-t", "an 8 mm (5/16 in) spot-weld"),
                      ("t-sm fab-t", "cutter, through the flange only")], leader=(px(408) + 3, py(250)))
    d.label(LX, 170, [("t-sm", "Count each row and measure"), ("t-sm", "its pitch before you drill")])
    d.label(LX, 210, [("t-sm crit-t", "Keep every flange whole: never"), ("t-sm crit-t", "torch-cut, and never cut or"),
                      ("t-sm crit-t", "grind through a flange")], leader=(px(450) + 2, py(745)))

    # ================= 2  sections =================
    y2 = 268
    d.line("ln-faint", 8, y2 - 18, 392, y2 - 18)
    head(d, y2, "2", "OUT DOWNWARD, IN FROM BELOW")
    d.text("t-xs", 8, y2 + 16, "Section across one rail, schematic")

    def rail(ox, oy, hole=False):
        # rail box (kept) with its flange running inboard over the floor edge
        d.rect("keep", ox, oy, 30, 44, sw=1.2)
        if hole:
            d.rect("keep", ox + 30, oy, 22, 4, sw=1)
            d.rect("keep", ox + 60, oy, 26, 4, sw=1)
        else:
            d.rect("keep", ox + 30, oy, 56, 4, sw=1)

    # a: drill, split, drop
    ax, ay = 14, y2 + 62
    d.text("t-sm t-b", 8, y2 + 40, "a")
    rail(ax, ay, hole=True)
    # old floor (comes out), drawn dashed and dropping
    d.path("fab-s dash", f"M{ax + 32},{ay + 6} H{ax + 98} C{ax + 112},{ay + 6} {ax + 112},{ay + 40} {ax + 126},{ay + 40} H{ax + 176}",
           sw=2.5)
    # drill from above, through the flange only
    d.line("fab-s", ax + 56, ay - 26, ax + 56, ay - 3, sw=2, end="ahf")
    # chisel from below, into the joint
    d.line("fab-s", ax + 104, ay + 30, ax + 89, ay + 8, sw=2, end="ahf")
    # drops out
    d.line("ln", ax + 150, ay + 46, ax + 150, ay + 70, sw=1.5, end="ah")
    d.label(ax + 64, ay - 26, [("t-xs fab-t", "8 mm cutter,"), ("t-xs fab-t", "flange only")])
    d.label(ax + 86, ay + 24, [("t-xs fab-t", "chisel"), ("t-xs fab-t", "from below")], "end")
    d.text("t-xs", ax + 156, ay + 66, "drops out")

    # b: new floor up, plug-weld down-hand
    bx, by = 214, y2 + 62
    d.text("t-sm t-b", 204, y2 + 40, "b")
    rail(bx, by, hole=True)
    d.path("new-s", f"M{bx + 32},{by + 6} H{bx + 176}", sw=3)
    # plug weld filling the drilled hole, from above
    d.path("fab", f"M{bx + 51},{by + 4.5} V{by} Q{bx + 56},{by - 6} {bx + 61},{by} V{by + 4.5} Z", sw=1)
    d.line("fab-s", bx + 56, by - 26, bx + 56, by - 9, sw=2, end="ahf")
    d.line("new-s", bx + 140, by + 40, bx + 140, by + 12, sw=2, end="ahn")
    d.label(bx + 64, by - 26, [("t-xs fab-t", "plug-weld down-"), ("t-xs fab-t", "hand from above")])
    d.label(bx + 146, by + 32, [("t-xs new-t", "up from"), ("t-xs new-t", "below")])

    # captions under the two sections
    cy = y2 + 148
    d.label(8, cy, [("t-xs", "Drill every weld from above, split the"),
                    ("t-xs", "layers from below with a spot-weld"),
                    ("t-xs", "chisel, and the well drops out.")])
    d.label(204, cy, [("t-xs", "Offer the new floor up, cleco or clamp"),
                      ("t-xs", "it at every hole, then plug-weld through"),
                      ("t-xs", "the same holes into the floor beneath.")])

    # ================= 3  one flange joint =================
    y3 = cy + 60
    d.line("ln-faint", 8, y3 - 18, 392, y3 - 18)
    head(d, y3, "3", "EACH FLANGE JOINT")
    d.text("t-xs", 8, y3 + 16, "Enlarged section; sheet thickness: measure yours")

    k = 4.0                      # px per mm in the inset
    jy = y3 + 78                 # top surface of the top layer
    t = 5                        # drawn sheet thickness (not to scale)
    hx = 196                     # hole centre
    x_wall, x_fl_edge, x_floor_edge = 40, 300, 88
    # top layer: Touring flange (kept), with an 8 mm hole
    d.rect("keep", x_wall, jy, hx - 4 * k - x_wall, t, sw=1)
    d.rect("keep", hx + 4 * k, jy, x_fl_edge - (hx + 4 * k), t, sw=1)
    # bottom layer: new floor edge
    d.rect("new", x_floor_edge, jy + t + 1.5, 392 - x_floor_edge - 4, t, sw=1)
    # weld-through primer between the layers, kept out of the weld spot
    d.line("ln dash", x_floor_edge + 2, jy + t + 0.75, hx - 7 * k, jy + t + 0.75, sw=1)
    d.line("ln dash", hx + 7 * k, jy + t + 0.75, x_fl_edge - 2, jy + t + 0.75, sw=1)
    # plug weld: fills the hole, face 10-13 mm across, no more than 3 mm high; melt-through below
    fx0, fx1 = hx - 6 * k, hx + 6 * k
    d.path("fab", f"M{fx0},{jy} Q{hx},{jy - 3 * k * 1.6} {fx1},{jy} L{hx + 4 * k},{jy} L{hx + 4 * k},{jy + 2 * t + 1.5} "
                  f"Q{hx},{jy + 2 * t + 1.5 + 6} {hx - 4 * k},{jy + 2 * t + 1.5} L{hx - 4 * k},{jy} Z", sw=1.2)
    # seam sealer on both faces
    d.path("fill-fg", f"M{x_fl_edge},{jy} Q{x_fl_edge + 9},{jy + t + 1} {x_fl_edge + 13},{jy + t + 1.5} L{x_fl_edge},{jy + t + 1.5} Z")
    d.path("fill-fg", f"M{x_floor_edge},{jy + t + 1.5} L{x_floor_edge},{jy + 2 * t + 1.5} Q{x_floor_edge - 9},{jy + t + 1.5} {x_floor_edge - 13},{jy + t + 1.5} Z")

    # dimensions and labels
    d.line("ln", fx0, jy - 16, fx1, jy - 16, sw=1, end="ah", start="ah")
    d.label(hx, jy - 40, [("t-xs t-b", "face 10–13 mm,"), ("t-xs t-b", "no more than 3 mm high")], "middle")
    d.line("ln", hx - 4 * k, jy + 2 * t + 22, hx + 4 * k, jy + 2 * t + 22, sw=1, end="ah", start="ah")
    d.line("ln-thin", hx - 4 * k, jy + 2 * t + 4, hx - 4 * k, jy + 2 * t + 26)
    d.line("ln-thin", hx + 4 * k, jy + 2 * t + 4, hx + 4 * k, jy + 2 * t + 26)
    d.text("t-xs t-b", hx, jy + 2 * t + 36, "8 mm (5/16 in) hole", "middle")

    d.label(8, jy - 40, [("t-xs", "Touring flange: rail,"), ("t-xs", "RACP or rear panel")],
            leader=(x_wall + 24, jy - 1), lead_from=(60, jy - 24))
    d.label(392, jy + 34, [("t-xs new-t", "new floor edge")], "end",
            leader=(352, jy + t + 2), lead_from=(352, jy + 24))
    d.label(8, jy + 34, [("t-xs", "seam sealer,"), ("t-xs", "underside")],
            leader=(x_floor_edge - 7, jy + 2 * t + 2), lead_from=(36, jy + 24))
    d.label(392, jy - 40, [("t-xs", "seam sealer,"), ("t-xs", "cargo side")], "end",
            leader=(x_fl_edge + 6, jy + 2), lead_from=(340, jy - 24))

    # notes under the joint
    ny = jy + 2 * t + 58
    d.text("t-xs", 8, ny, "Dashed: weld-through primer on the mating faces, kept out of the weld spot.")
    d.text("t-xs", 8, ny + 12.5, "Layers touching at every hole: gap 1 mm or less. Paint off about 30 mm")
    d.text("t-xs", 8, ny + 25, "round each weld, both faces; grind off the zinc where you weld.")

    # a strip of the flange from above: plug welds at the factory positions, at least 25 mm apart
    sy = ny + 38
    d.rect("keep", 40, sy, 320, 18, sw=1)
    for i, xx in enumerate((70, 150, 230, 310)):
        d.circle("fab", xx, sy + 9, 6, sw=1.2)
    d.line("ln", 150, sy + 28, 230, sy + 28, sw=1, end="ah", start="ah")
    d.text("t-xs t-b", 190, sy + 42, "at least 25 mm (1 in) apart", "middle")
    d.label(8, sy + 56, [("t-xs", "Same count and positions as the factory spot welds; skip round the four")], )
    d.text("t-xs", 8, sy + 68.5, "edges so no area gets hot.")

    # ================= 4  flangeless lap =================
    y4 = sy + 98
    d.line("ln-faint", 8, y4 - 18, 392, y4 - 18)
    head(d, y4, "4", "NO FLANGE: A JOGGLED LAP")
    d.text("t-xs", 8, y4 + 16, "Partial graft or flat panel; enlarged section")

    ly = y4 + 58
    lap0, lap1 = 160, 214          # overlap 12-15 mm at about 4 px per mm
    # top layer: the panel you keep (Touring floor), plug holes through it
    d.rect("keep", 20, ly, lap1 - 20, t, sw=1)
    # joggled lower panel: steps down one thickness under the lap, flush beyond it
    d.path("fab", f"M{lap0},{ly + t + 1.5} H{lap1 + 10} L{lap1 + 16},{ly} H380 V{ly + t} H{lap1 + 18} "
                  f"L{lap1 + 12},{ly + 2 * t + 1.5} H{lap0} Z", sw=1)
    # plug weld through the top layer
    d.path("fab", f"M{lap0 + 12},{ly} Q{(lap0 + lap1) / 2 - 2},{ly - 9} {lap0 + 34},{ly} L{lap0 + 29},{ly} L{lap0 + 29},{ly + t} "
                  f"L{lap0 + 17},{ly + t} L{lap0 + 17},{ly} Z", sw=1)
    # sealer on both faces
    d.path("fill-fg", f"M{lap1},{ly} Q{lap1 + 4},{ly - 1} {lap1 + 7},{ly - 4} L{lap1 + 9},{ly} Z")
    d.path("fill-fg", f"M{lap0},{ly + t + 1.5} L{lap0},{ly + 2 * t + 1.5} Q{lap0 - 6},{ly + 2 * t + 1.5} {lap0 - 10},{ly + 2 * t + 5} Z")

    d.line("ln", lap0, ly + 2 * t + 16, lap1, ly + 2 * t + 16, sw=1, end="ah", start="ah")
    d.line("ln-thin", lap0, ly + 2 * t + 4, lap0, ly + 2 * t + 20)
    d.line("ln-thin", lap1, ly + t + 2, lap1, ly + 2 * t + 20)
    d.text("t-xs t-b", (lap0 + lap1) / 2, ly + 2 * t + 30, "lap about 12–15 mm", "middle")
    d.label(8, ly - 24, [("t-xs", "panel you keep")], leader=(70, ly - 1), lead_from=(50, ly - 20))
    d.label(250, ly - 26, [("t-xs fab-t", "joggled edge: steps")], leader=(lap1 + 14, ly + 4))
    d.text("t-xs fab-t", 250, ly - 13.5, "down one thickness")
    d.label(8, ly - 12 + 52, [("t-xs fab-t", "8 mm plug welds"), ("t-xs fab-t", "in the top layer")],
            leader=(lap0 + 20, ly - 2), lead_from=(92, ly + 34))

    # strip from above: plugs at 25-40 mm pitch plus short stitches
    ty = ly + 66
    d.rect("keep", 40, ty, 320, 16, sw=1)
    for xx in (70, 150, 230, 310):
        d.circle("fab", xx, ty + 8, 5, sw=1.2)
    for xx in (98, 178, 258):
        d.line("fab-s", xx, ty + 16, xx + 26, ty + 16, sw=3)
    d.line("ln", 70, ty + 26, 150, ty + 26, sw=1, end="ah", start="ah")
    d.text("t-xs t-b", 110, ty + 40, "25–40 mm pitch", "middle")
    d.label(392, ty + 40, [("t-xs fab-t", "short stitches")], "end", leader=(286, ty + 17), lead_from=(318, ty + 30))
    d.text("t-xs", 8, ty + 60, "Seal the lap on both faces: laps trap water.")

    # ================= key =================
    ky = ty + 80
    d.line("ln-faint", 8, ky - 12, 392, ky - 12)
    d.rect("keep", 8, ky, 12, 12, rx=2)
    d.text("t-sm", 26, ky + 10.5, "Your Touring's body, kept")
    d.rect("new", 206, ky, 12, 12, rx=2)
    d.text("t-sm", 224, ky + 10.5, "New M3 floor")
    ky += 18
    d.rect("fab", 8, ky, 12, 12, rx=2)
    d.text("t-sm", 26, ky + 10.5, "Drill, weld or modify")
    d.rect("fab-s dash", 206, ky, 12, 12, rx=2, sw=1.6)
    d.text("t-sm", 224, ky + 10.5, "Comes out")
    H = int(ky + 22)
    return d, H


def main():
    d, H = build(make)
    head_ = svg_open(W, H, ARIA, markers=("ah", "ahf", "ahn"))
    p = write("30-floor-seams.svg", head_, d.body())
    print("wrote", p, "height", H)


if __name__ == "__main__":
    main()
