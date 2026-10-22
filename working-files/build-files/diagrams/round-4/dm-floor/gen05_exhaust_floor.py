#!/usr/bin/env python3
"""Redraw of Figure 6 (diagrams/05-exhaust-floor.svg): side section through the rear floor.

Kept from the original: the two panels (Touring today / after), the clash between the deep well
and the M3 muffler's space, the bumper cut for the tips. Changed: the new floor is led by the new
BMW M3 trunk floor 41127895619 with reinforcement 51717894229 (or the donor's M3 floor), drawn
with its shallow well at the front and flat rear; it is plug-welded at the factory spot-weld
positions (was "tack, stitch"); the M3 heat shield 51482494848 sits between floor and muffler.
X positions follow the research notes' estimates (rear_floor_exhaust.md, Figure A/B: seam about
+20 mm, well 620 mm centred about +330, muffler about +380 to +720, rear panel about +730, bumper
about +845, axle line about -150 mm from the rear mounts); heights are schematic (no depths are
published). Text: README fragment 0470.
"""
from floorkit import Fig, build, svg_open, write

W = 400
S = 0.27


def px(X):                    # X mm from the rear mounts, rearward -> right
    return 22 + (X + 450) * S


AXLE, SEAM, WELL0, WELL1 = -150, 20, 20, 640
MUF0, MUF1, PANEL, BUMPER = 380, 720, 730, 845

ARIA = (
    "Side section through the rear floor, front to the left, schematic: the positions along the car "
    "are roughly to scale but the heights are not, because no depths are published. Today, your "
    "Touring's deep spare-wheel well hangs down into the space the M3 muffler needs behind the rear "
    "axle, so the two clash. After the change, the well is drilled out and a new BMW M3 trunk floor, "
    "41127895619, with its front reinforcement 51717894229, or the donor's M3 floor, is plug-welded in "
    "at the factory spot-weld positions and sealed on both faces. It has a shallow well at the front and "
    "is flat at the rear, so the M3 muffler, 18107831783 at 26.7 kg, fits underneath with the M3 heat "
    "shield 51482494848 between them, and the tips exit through cut-outs in the rear bumper."
)


def make():
    d = Fig()

    # ================= TOURING TODAY =================
    d.text("t-h", 8, 20, "TOURING TODAY")
    d.text("t-xs", 392, 20, "front ← → rear", "end")
    fy = 58                                   # floor level
    # M3 rear axle and pipe (where they will sit)
    d.circle("donor", px(AXLE), 100, 11, sw=1.5)
    d.text("t-xs", px(AXLE), 80, "rear axle", "middle")
    d.line("donor-s", 20, 117, px(WELL0) + 4, 117, sw=2.5)
    # the M3 muffler's space
    d.rect("donor dash", px(MUF0), 96, px(MUF1) - px(MUF0), 38, rx=6, sw=1.5, extra=' opacity="0.85"')
    # your floor with its deep well
    w0, w1 = px(WELL0), px(WELL1)
    d.path("ln", f"M20,{fy} H{w0:.1f} C{w0 + 10:.1f},{fy} {w0 + 14:.1f},{fy + 6} {w0 + 17:.1f},{fy + 16} "
                 f"L{w0 + 26:.1f},{fy + 62} Q{w0 + 30:.1f},{fy + 72} {w0 + 42:.1f},{fy + 72} "
                 f"H{w1 - 42:.1f} Q{w1 - 30:.1f},{fy + 72} {w1 - 26:.1f},{fy + 62} L{w1 - 17:.1f},{fy + 16} "
                 f"C{w1 - 14:.1f},{fy + 6} {w1 - 10:.1f},{fy} {w1:.1f},{fy} H{px(PANEL):.1f}", sw=2.5)
    # the clash: the well's bottom inside the muffler's space
    d.path("crit-s", f"M{px(MUF0):.1f},{fy + 72} H{w1 - 42:.1f} Q{w1 - 30:.1f},{fy + 72} {w1 - 26:.1f},{fy + 62} "
                     f"L{w1 - 22.5:.1f},{fy + 44}", sw=4)
    # rear panel and bumper
    d.path("ln", f"M{px(PANEL):.1f},{fy} V{fy - 8}", sw=2.5)
    d.path("ln", f"M{px(BUMPER):.1f},52 V140", sw=3)
    d.text("t-xs", px(BUMPER), 44, "bumper", "middle")
    # labels
    d.text("t-sm", (w0 + w1) / 2 - 12, 38, "spare-wheel well", "middle")
    d.text("t-xs", (w0 + w1) / 2 - 12, 51, "(depth not published)", "middle")
    d.line("ln-thin", 112, 152, px(MUF0) + 8, 134)
    d.text("t-sm donor-t", 8, 164, "M3 muffler space")
    d.line("ln-thin", w1 - 40, 147, w1 - 44, fy + 76)
    d.text("t-sm crit-t", 392, 164, "Clash: the well hangs into it", "end")

    d.line("ln-faint", 8, 182, 392, 182)

    # ================= AFTER =================
    oy = 196
    d.text("t-h", 8, oy + 10, "AFTER")
    fy = oy + 76                               # floor level
    ay = fy + 46
    d.circle("donor", px(AXLE), ay - 4, 11, sw=1.5)
    # pipe into the muffler's front
    d.line("donor-s", 20, ay + 13, px(MUF0), ay + 13, sw=2.5)
    # floor ahead of the seam (yours)
    d.path("ln", f"M20,{fy} H{px(SEAM):.1f}", sw=2.5)
    # new M3 floor: shallow well at the front, flat at the rear over the muffler
    s0, s1 = px(SEAM), px(PANEL)
    sw0, sw1 = s0 + 10, px(330)
    d.path("new-s", f"M{s0:.1f},{fy} H{sw0:.1f} C{sw0 + 8:.1f},{fy} {sw0 + 8:.1f},{fy + 13} {sw0 + 18:.1f},{fy + 13} "
                    f"H{sw1 - 18:.1f} C{sw1 - 8:.1f},{fy + 13} {sw1 - 8:.1f},{fy} {sw1:.1f},{fy} H{s1:.1f}", sw=3)
    # front reinforcement under the front edge
    d.rect("new", s0 + 1, fy + 2, 13, 6, rx=1, sw=1.2)
    # rear panel
    d.path("ln", f"M{s1:.1f},{fy} V{fy - 8}", sw=2.5)
    # plug welds at the factory spot-weld positions: front seam and rear panel
    d.circle("fab-f", s0, fy, 3.5)
    d.circle("fab-f", s1, fy, 3.5)
    # heat shield between floor and muffler
    d.path("donor-s dash", f"M{px(MUF0 - 20):.1f},{fy + 9} H{px(MUF1 + 10):.1f}", sw=2)
    # muffler
    m0, m1 = px(MUF0), px(MUF1)
    d.rect("donor", m0, fy + 20, m1 - m0, 40, rx=6, sw=1.5)
    d.text("t-sm donor-t", (m0 + m1) / 2, fy + 37, "M3 muffler", "middle")
    d.text("t-xs donor-t", (m0 + m1) / 2, fy + 51, "26.7 kg", "middle")
    # tips through the cut bumper
    d.rect("donor", m1 - 6, fy + 47, px(BUMPER + 45) - (m1 - 6), 8, rx=2, sw=1.5)
    bx = px(BUMPER)
    d.path("ln", f"M{bx:.1f},{fy - 6} V{fy + 42} M{bx:.1f},{fy + 60} V{fy + 66}", sw=3)
    d.path("fab-s", f"M{bx - 4:.1f},{fy + 42} H{bx + 4:.1f} M{bx - 4:.1f},{fy + 60} H{bx + 4:.1f}", sw=2.5)

    # labels above the floor
    bb = d.label(8, oy + 30, [("t-sm new-t t-b", "New BMW M3 trunk floor 41127895619"),
                              ("t-xs", [(None, "with reinforcement "), ("t-mono", "51717894229"), (None, ", or the donor's")]),
                              ("t-xs", "shallow well at the front, flat over the muffler")])
    d.line("ln-thin", bb[2] + 4, oy + 54, px(560), fy - 3)
    d.label(392, oy + 10, [("t-xs donor-t", [(None, "heat shield "), ("t-mono", "51482494848")])], "end",
            leader=(px(MUF1 - 10), fy + 7), lead_from=(px(MUF1 - 10), oy + 14))
    # labels below
    by = fy + 84
    d.label(8, by, [("t-sm fab-t", "Plug welds at the factory spot-weld"), ("t-sm fab-t", "positions; seal both faces")],
            leader=(s0 + 1, fy + 5), lead_from=(s0 + 18, by - 11))
    d.label(392, by, [("t-sm fab-t", "Cut the bumper"), ("t-sm fab-t", "for the tips")], "end",
            leader=(bx, fy + 68), lead_from=(bx, by - 11))

    # key
    ky = by + 34
    d.line("ln-faint", 8, ky - 10, 392, ky - 10)
    d.rect("new", 8, ky, 12, 12, rx=2)
    d.text("t-sm", 26, ky + 10.5, "New BMW part")
    d.rect("donor", 132, ky, 12, 12, rx=2)
    d.text("t-sm", 150, ky + 10.5, "From the donor M3")
    d.rect("fab", 284, ky, 12, 12, rx=2)
    d.text("t-sm", 302, ky + 10.5, "Weld or cut")
    H = int(ky + 20)
    return d, H


def main():
    d, H = build(make)
    p = write("05-exhaust-floor.svg", svg_open(W, H, ARIA), d.body())
    print("wrote", p, "height", H)


if __name__ == "__main__":
    main()
