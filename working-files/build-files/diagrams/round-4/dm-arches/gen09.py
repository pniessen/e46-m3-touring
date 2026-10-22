#!/usr/bin/env python3
"""Redraw of figure 09 (README Figure 15), portrait: the section through the right rear arch at the axle.
Also covers placeholder proposed-arch-section-axle (README "Arch graft step by step"), which goes.

Rear view, looking forward; outboard to the right; heights above the hub, widths from the car's center line.
Data: notes rear_arches.md C2 (skin half-widths and move-out by height; wheel geometry; lip channel);
README fragments 0660 (skin 0.7-0.8 mm, lip ~15 mm double skin, tire ~892 vs skin ~890), 0670 (move-out
table: 21/16/12/6/2/0/0), 0680 (fill strip, 6 mm plug welds, sealer, backing strip), 0700 (54.6 / 88.3 mm);
gap-fill Gap 6 (BMW backing strips ~60 mm, ~30 mm into each side; BMW crimps the arch edge and seals it).
The section is to scale (1 px = 1 mm); the lip panel at the bottom is an enlarged schematic.
"""
import common as C
from common import w, catmull, poly
import kit

W = 400
NAME = "09-arch-section.svg"
S = 1.0
H0, H1 = 700, 912          # mm from the center line shown
YT, YB = 562, 148          # mm above the hub shown
X0 = 8
T = 66                     # screen y of YT
LH = 14

ARIA = (
    "Rear view of a section through the right rear arch at the axle line, drawn to scale, with an enlarged "
    "schematic of the arch lip below. Both cars' rear hub faces sit in the same place, about 788 mm from the "
    "car's center line. The 325i's 8J ET47 wheel puts its outer rim edge 54.6 mm outboard of the hub face; the "
    "M3's 9J ET26 wheel puts it 88.3 mm out, with the wheel centerline 21 mm further out. The M3 skin replaces "
    "the Touring's below a top seam 500 to 515 mm above the hub, which is our inference, and stands out by about "
    "21 mm at the lip, 345 mm above the hub, then 16 mm at 385, 12 at 435, 6 at 465, 2 at 500 and 0 from about "
    "525 mm up to the shoulder crease at about 540 mm. The top seam is a butt joint over a backing strip; BMW's "
    "own sectioning joints use strips about 60 mm wide, about 30 mm into each side. The M3 tire's widest point, "
    "about 892 mm from the center line, sits about flush with the M3 skin at about 890 mm, and about 22 mm "
    "outside a stock Touring's skin. The lip is a double skin about 15 mm deep: the skin turns in under the inner "
    "wheelhouse flange, the two are spot-welded at the factory, and the channel above them is sealed. For the "
    "graft, a fill strip extends your flange out by the move-out, about 21 mm at the crown, or you graft the "
    "donor's flange; the lip is plug-welded through 6 mm holes at the factory spot positions, and seam sealer "
    "fills the channel. BMW crimps a new side wall's arch edge over the inner flange and seals it. The skin is "
    "about 0.7 to 0.8 mm thick.")

# notes C2: Touring skin half-width by height above the hub; README 0670: M3 move-out by height
TOURING = [(345, 868), (385, 861), (435, 851), (465, 847), (500, 842), (525, 834), (540, 829), (556, 826)]
MOVE = {345: 21, 385: 16, 435: 12, 465: 6, 500: 2, 525: 0, 540: 0, 556: 0}
SEAM = 507.5


def sx(h):
    return X0 + S * (h - H0)


def sy(y):
    return T + S * (YT - y)


def P(pts):
    return [(sx(h), sy(y)) for h, y in pts]


def lines(d, cls, x, y, rows, anchor=None, lh=LH):
    for i, s in enumerate(rows):
        c = cls[0] if isinstance(cls, tuple) and i == 0 else (cls[1] if isinstance(cls, tuple) else cls)
        d.text(c, x, y + i * lh, s, anchor=anchor)


def skin_at(y, m3=False):
    pts = TOURING
    for (y1, h1), (y2, h2) in zip(pts, pts[1:]):
        if y1 <= y <= y2:
            a = h1 + (h2 - h1) * (y - y1) / (y2 - y1)
            if m3:
                a += MOVE[y1] + (MOVE[y2] - MOVE[y1]) * (y - y1) / (y2 - y1)
            return a
    raise ValueError(y)


def section(d):
    BOT = sy(YB)
    d.text("t-h", 8, 18, "SECTION AT THE AXLE, LOOKING FORWARD")
    d.text("t-sm", 8, 36, "Right side, to scale. Widths: mm from the car's center line.")
    d.text("t-xs", 8, 54, "← inboard")
    d.text("t-xs", 220, 54, "outboard →", anchor="end")

    # ------------------------------------------------------------ height scale (left)
    d.comment("Heights above the hub (the C2 stations)")
    rx = 18
    d.line("ln-thin", rx, sy(540), rx, sy(345))
    for y in (345, 385, 435, 465, 500, 525, 540):
        d.line("ln-thin", rx, sy(y), rx + 5, sy(y))
        d.text("t-xs", rx + 8, sy(y) + 3.5, str(y))
    d.text("t-xs", 8, sy(556) + 3, "mm above the hub")

    # ------------------------------------------------------------ inner wheelhouse (yours)
    d.comment("Inner wheelhouse: your outer half's flange runs down to the lip")
    d.path("keep-s", f"M{sx(H0)},{sy(398)} H{sx(832)} Q{sx(852)},{sy(398)} {sx(852)},{sy(378)} V{sy(349)}", sw=2)
    d.text("t-sm", sx(748), sy(398) - 7, "your wheelhouse")

    # ------------------------------------------------------------ skins
    d.comment("Touring skin: kept above the top seam, cut away below it (dashed), with its old lip")
    above = [(skin_at(y), y) for y in (SEAM, 525, 540, 556)]
    below = [(skin_at(y), y) for y in (345, 385, 435, 465, 500, SEAM)]
    d.path("keep-s", catmull(P(above)), sw=2.5)
    d.path("keep-s dash", catmull(P(below)) + f" M{sx(868)},{sy(345)} V{sy(343)} H{sx(853)}", sw=1.8)
    d.comment("Backing strip behind the top seam (BMW: about 60 mm wide, about 30 mm into each side)")
    strip = [(skin_at(y) - 3, y) for y in (SEAM - 30, 485, 500, SEAM, 515, 525, SEAM + 30)]
    d.path("fab-s", catmull(P(strip)), sw=3.5)
    d.comment("M3 skin (donor) from the top seam down to its lip")
    m3 = [(skin_at(y, True), y) for y in (SEAM, 500, 465, 435, 385, 345)]
    d.path("donor-s", catmull(P(m3)) + f" V{sy(343)} H{sx(874)}", sw=2.5)
    d.comment("Fill strip: extends your flange by the move-out, into the M3 lip")
    d.rect("fab", sx(852), sy(349), sx(888) - sx(852), 4, sw=1)
    d.line("fab-s", sx(skin_at(SEAM)) - 7, sy(SEAM), sx(skin_at(SEAM)) + 7, sy(SEAM), sw=2)
    d.circle("ln-thin dash", sx(880), sy(344), 10)

    # ------------------------------------------------------------ wheels
    d.comment("325i wheel and tire (8J ET47, 225/45R17), dashed")
    d.path("keep-s dash", f"M{sx(H0)},{sy(216)} H{sx(842.6)} V{sy(233)} H{sx(848)}", sw=1.5)
    d.path("keep-s dash", f"M{sx(848)},{sy(233)} C{sx(858)},{sy(248)} {sx(858)},{sy(285)} {sx(852)},{sy(303)} "
                          f"Q{sx(848)},{sy(317)} {sx(834)},{sy(317)} H{sx(H0)}", sw=1.5)
    d.comment("M3 wheel and tire (9J ET26, 255/40R18): rim, disc on the hub face, tire")
    d.path("donor", poly(P([(H0, 222), (882, 222), (882, 246), (876.3, 246), (876.3, 229), (H0, 229)]),
                         close=True), sw=1.2)
    d.rect("donor", sx(788), sy(222), 11, sy(YB) - sy(222), sw=1.2)
    d.path("ln", f"M{sx(882)},{sy(246)} C{sx(894)},{sy(262)} {sx(894)},{sy(300)} {sx(888)},{sy(318)} "
                 f"Q{sx(884)},{sy(331)} {sx(868)},{sy(331)} H{sx(H0)}", sw=2)

    d.comment("Hub face: the same on both cars")
    d.line("ln", sx(788), sy(YB), sx(788), sy(222), sw=2.5)
    d.comment("Wheel centerlines: ET47 -> ET26 moves the wheel 21 mm out")
    d.line("keep-s dash", sx(741), sy(YB), sx(741), sy(212), sw=1.5)
    d.line("donor-s dash", sx(762), sy(YB), sx(762), sy(220), sw=1.5)
    d.line("ln", sx(741), sy(176), sx(762), sy(176), start="ah", end="ah")
    d.text("t-sm", sx(751.5), sy(176) - 8, "21", anchor="middle")
    d.comment("Outer rim edges from the hub face, with extension lines")
    d.line("ln-thin dash", sx(842.6), sy(214), sx(842.6), sy(158))
    d.line("ln-thin dash", sx(876.3), sy(220), sx(876.3), sy(192))
    d.line("keep-s", sx(799), sy(162), sx(842.6), sy(162), sw=1.5, end="ahk")
    d.line("ln", sx(799), sy(196), sx(876.3), sy(196), end="ah")
    d.text("t-sm", sx(842.6) + 8, sy(162) + 4, "325i rim edge: 54.6 mm")
    d.text("t-sm", sx(876.3) + 8, sy(196) + 4, "M3 rim edge: 88.3 mm")

    # ------------------------------------------------------------ move-out figures beside the M3 skin
    d.comment("Move-out at each height (README table)")
    for y in (385, 435, 465, 500):
        d.text("t-sm donor-t", sx(skin_at(y, True)) + 6, sy(y) + 4, str(MOVE[y]))
    d.text("t-sm donor-t", sx(skin_at(525)) + 6, sy(525) + 4, "0")
    d.line("ln", sx(skin_at(362)), sy(362), sx(skin_at(362, True)), sy(362), start="ah", end="ah")
    d.text("t-sm donor-t t-b", sx(skin_at(362, True)) + 6, sy(362) + 4, "21")
    d.comment("Tire flush with the M3 skin")
    d.line("ln-thin dash", sx(891), sy(284), sx(891), sy(341))

    # ------------------------------------------------------------ labels, right column
    cx = 232
    lines(d, "t-sm", cx, sy(556) + 4, ["Shoulder crease ≈540:", "the skins meet"])
    d.path("ln-thin", poly([(cx - 3, sy(556)), (sx(829) + 3, sy(541))]))
    y = sy(522)
    lines(d, ("t-sm fab-t t-b", "t-sm fab-t"), cx, y, ["Top seam, 500–515 above", "the hub (our inference):",
                                                        "butt joint over a backing", "strip; BMW's are ≈60 mm",
                                                        "wide, ≈30 mm each side"])
    d.path("ln-thin", poly([(cx - 3, y - 4), (sx(skin_at(SEAM)) + 8, sy(SEAM))]))
    y = sy(452)
    lines(d, ("t-sm donor-t t-b", "t-sm"), cx, y, ["M3 skin (donor)", "Blue figures: mm it stands",
                                                    "out at each height"])
    d.path("ln-thin", poly([(cx - 3, y - 4), (sx(skin_at(442, True)) + 2, sy(442))]))
    y = sy(394)
    lines(d, "t-sm", cx, y, ["Touring skin below the", "seam: cut away"])
    d.path("ln-thin", poly([(cx - 3, y - 4), (sx(skin_at(402)) + 1, sy(402))]))
    y = sy(340)
    lines(d, ("t-sm fab-t t-b", "t-sm"), cx, y, ["Fill strip", "extends your flange ≈21 mm",
                                                  "into the M3 lip (or graft", "the donor's flange)"])
    d.path("ln-thin", poly([(cx - 3, y - 4), (sx(870), sy(349) + 2)]))
    y = sy(280)
    lines(d, ("t-sm t-b", "t-sm"), cx, y, ["M3 tire: widest ≈892", "About flush with the M3 skin",
                                            "(≈890); ≈22 mm outside a", "stock Touring's skin"])
    d.path("ln-thin", poly([(cx - 3, y - 4), (sx(893) + 2, sy(284))]))

    # ------------------------------------------------------------ under the section
    d.text("t-sm t-b", sx(793), BOT + 15, "hub face ≈788:", anchor="middle")
    d.text("t-sm t-b", sx(793), BOT + 29, "same on both cars", anchor="middle")
    y = BOT + 50
    d.text("t-sm", 8, y, "ET47 → ET26: the M3 wheel sits 21 mm further out.")
    d.line("ln", 8, y + 14, 30, y + 14, sw=2)
    d.text("t-sm", 36, y + 18, "M3 255/40R18 on 9J ET26")
    d.line("keep-s dash", 206, y + 14, 228, y + 14, sw=1.5)
    d.text("t-sm", 234, y + 18, "325i 225/45R17 on 8J ET47")
    return y + 30


def lip_panel(d, top):
    """Enlarged schematic of the lip (circled in the section): skin flange, fill strip, plug welds, sealer."""
    d.line("ln-faint", 8, top, 392, top)
    d.text("t-h", 8, top + 22, "THE LIP, ENLARGED")
    d.text("t-xs", 392, top + 22, "Schematic, not to scale", anchor="end")
    oy = top + 44                    # top of the drawing
    xw, xs = 46, 150                 # wheelhouse wall (inboard), skin wall (outboard)
    yb = oy + 92                     # underside of the lip
    t = 4                            # sheet thickness as drawn
    d.comment("Seam sealer fills the channel between skin and wheelhouse")
    d.path("panel", f"M{xw + 22 + t},{yb - 2 * t - 18} H{xs - t} V{yb - 2 * t} H{xw + 22 + t} Z", sw=1)
    d.comment("Your wheelhouse wall and old flange (keep), fill strip (fab), M3 skin (donor)")
    d.path("keep", f"M{xw},{oy} H{xw + t} V{yb - 2 * t} H{xw + 30} V{yb - t} H{xw} Z", sw=1)
    d.path("fab", f"M{xw + 22},{yb - 2 * t} H{xs - t} V{yb - t} H{xw + 22} Z", sw=1)
    d.path("donor", f"M{xs - t},{oy} H{xs} V{yb} H{xs - 64} Q{xs - 72},{yb} {xs - 72},{yb - t - 4} "
                    f"Q{xs - 72},{yb - 2 * t - 2} {xs - 66},{yb - 2 * t - 2} H{xs - 62} V{yb - 2 * t} "
                    f"Q{xs - 68},{yb - 2 * t} {xs - 68},{yb - t - 4} Q{xs - 68},{yb - t} {xs - 64},{yb - t} "
                    f"H{xs - t} Z", sw=1)
    d.comment("6 mm plug welds through the double skin")
    for px in (xs - 50, xs - 30, xs - 12):
        d.rect("fab-f", px - 3, yb - 2 * t - 1, 6, 2 * t + 2, rx=1)
    d.comment("Depth of the double skin")
    d.line("ln-thin", xs - 72, yb + 6, xs - 72, yb + 14)
    d.line("ln-thin", xs, yb + 6, xs, yb + 14)
    d.line("ln", xs - 72, yb + 10, xs, yb + 10, start="ah", end="ah")
    d.text("t-sm", (2 * xs - 72) / 2, yb + 27, "≈15 mm", anchor="middle")
    d.text("t-xs", xw + 2, oy - 6, "wheelhouse")
    d.text("t-xs", xs + 4, oy - 6, "skin")

    cx = 182
    rows = [
        (("t-sm donor-t t-b", "t-sm"), ["M3 skin, ≈0.7–0.8 mm", "turns in under the flange"], (xs + 1, oy + 30)),
        (("t-sm t-b", "t-sm"), ["Seam sealer", "brushed in to fill the channel"], (xs - 24, yb - 2 * t - 14)),
        (("t-sm fab-t t-b", "t-sm"), ["Fill strip on your flange", "≈21 mm out at the crown"], (xs - 40, yb - 2 * t)),
        (("t-sm fab-t t-b", "t-sm"), ["6 mm plug welds", "at the factory spot positions"], (xs - 12, yb + 1)),
    ]
    y = oy + 4
    for cls, txt, (tx, ty) in rows:
        lines(d, cls, cx, y, txt)
        d.path("ln-thin", poly([(cx - 3, y - 4), (tx, ty)]))
        y += 2 * LH + 10
    lines(d, "t-xs", 8, y + 4, ["Double skin ≈15 mm deep. BMW crimps a new side wall's edge over",
                                "the flange, then seals it."], lh=13)
    return y + 29


def build():
    d = kit.Doc()
    top = section(d)
    h = lip_panel(d, top + 6)
    return kit.svg_open(W, int(h), ARIA, markers=("ah", "ahk")), d.body()


if __name__ == "__main__":
    print(C.run(build, NAME))
