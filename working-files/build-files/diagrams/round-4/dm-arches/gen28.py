#!/usr/bin/env python3
"""Figure 28 (new, portrait): the order of fitting, tacking, lip plug welds and stitching on one arch.

Placeholder: proposed-arch-weld-sequence (README "Arch graft step by step", before "Weld.", steps 9-11).
Data: notes rear_arches.md Guide-ready A8-A13 and C4; README fragment 0680 steps 8-13 (wins where it
differs); 0480 (coupon pass values); gap-fill gapfill_bmw_chassis_body.md Gap 6 (BMW: backing strips
~60 mm wide, ~30 mm into each side; spots set so close they form a continuous seam, each area left to
cool; 82/18 gas; 8 mm holes >= 25 mm apart as the general rule).
"""
import math
import common as C
from common import w, catmull, poly
import kit

W = 400
NAME = "28-arch-weld-sequence.svg"
LH = 14
BX0, BX1 = 8, 392

ARIA = (
    "How to fit, tack and weld the M3 skin section into one rear quarter, in order, with the check that ends "
    "each step; repeat on the other side between passes. A side view numbers the joints: the top seam first, "
    "then the rear seam, then the front seam, then the lip. The skin seams are butt joints with a 0.8 to 1.0 mm "
    "gap, about one skin thickness, over a backing strip of skin-thickness steel plug-welded or bonded to one "
    "side only; BMW's own strips are about 60 mm wide, about 30 mm into each side. Step 8, fit: clamps or clecos "
    "every 75 to 100 mm; check that every seam is flush within 0.5 mm, the lip is at its target within 3 mm, the "
    "door opens and closes and the bumper corner fits. Step 9, tack: the top seam's center, then its ends, then "
    "halve the gaps down to a 25 to 30 mm pitch, about 30 tacks; then the rear seam, ends then middle; then the "
    "front seam, top, bottom, middle, then halves; check gap, flush, door and templates again and adjust before "
    "any stitching. Step 10, the lip: plug welds through 6 mm holes at the factory spot positions, every second "
    "position first, from the crown outward, alternately forward and back, then the rest; or bond it and plug "
    "every second position. First pass a coupon: each plug 8 to 10 mm across and no more than 3 mm high, tearing "
    "a 3 to 8 mm hole when broken. Step 11, stitch: 10 to 15 mm welds between the tacks, in a skip order: gaps "
    "1, 5, 9 on the top seam, then the rear seam's odd gaps, then the front seam's 1, 5, 9, then the other side "
    "of the car; later passes 3, 7, 11, then 2, 6, 10, then 4, 8, 12, each only when the area is hand-warm, no "
    "more than about 150 mm of weld per seam per pass, until the seam is continuous, as BMW welds its own seams. "
    "Check for penetration on the back of every seam and grind and planish each seam as you finish it. After "
    "dressing, every template fits within 1 mm, the station offsets match side to side within 3 mm, the body "
    "diagonals are within 2 mm of your earlier figures and the door gaps and flush are back.")


def lines(d, cls, x, y, rows, anchor=None, lh=LH):
    for i, s in enumerate(rows):
        c = cls[0] if isinstance(cls, tuple) and i == 0 else (cls[1] if isinstance(cls, tuple) else cls)
        d.text(c, x, y + i * lh, s, anchor=anchor)


def badge(d, x, y, n, cls="ln"):
    """Numbered ring (stroke only, sized to clear the digits)."""
    if cls == "fab":
        d.circle("fab-s", x, y, 9, sw=1.5)
        d.text("t-sm t-b fab-t", x, y + 4, str(n), anchor="middle")
    else:
        d.circle("ln", x, y, 11, sw=1.5)
        d.text("t-sm t-b", x, y + 4, str(n), anchor="middle")


# ---------------------------------------------------------------- seam map (side view, to scale)
MS = 0.29
MXMIN, MXMAX, MYMAX, MYMIN = -760, 470, 560, -60


def seam_map(d, top):
    hx = 22 + MS * (-MXMIN)
    hy = top + MS * MYMAX

    def sx(x):
        return hx + MS * x

    def sy(y):
        return hy - MS * y

    def P(pts):
        return [(sx(x), sy(y)) for x, y in pts]

    arch = C.ARCH
    i_bump = arch.index((-176, 305))
    upper, rear = arch[: i_bump + 1], arch[i_bump:]
    door_cut = C.door_cut_pts()
    sdx = door_cut[-1][0]
    q = [(C.SHUT_X, MYMAX), (MXMIN, MYMAX), (MXMIN, C.BUMPER_Y)] + list(reversed(upper)) + \
        [(366, C.SILL_Y), (sdx, C.SILL_Y)] + list(reversed(door_cut))
    d.path("keep", poly(P(q), close=True), sw=1)
    d.path("shape", poly(P([(C.SHUT_X, MYMAX), (MXMAX, MYMAX), (MXMAX, C.SILL_Y), (sdx, C.SILL_Y)] +
                           list(reversed(door_cut))), close=True), sw=1)
    d.path("panel", poly(P([(-176, C.BUMPER_Y), (MXMIN, C.BUMPER_Y), (MXMIN, MYMIN), (-381, MYMIN)] +
                           list(reversed(rear))), close=True), sw=1)
    d.line("ln-thin", sx(C.LAMP_X), sy(C.CREASE_Y), sx(MXMAX), sy(C.CREASE_Y))
    fm, rm = C.SHUT_X - sum(C.FRONT_SEAM) / 2, C.R_DOOR - sum(C.FRONT_SEAM) / 2
    ym, xm = sum(C.TOP_SEAM) / 2, sum(C.REAR_SEAM) / 2
    front_c = [(fm, ym), (fm, C.junction_y(rm, fm))] + C.door_cut_pts(rm, fm)[1:]
    sec = [(xm, ym), (xm, C.BUMPER_Y)] + list(reversed(upper)) + [(366, C.SILL_Y)] + list(reversed(front_c))
    d.add(f'<path class="donor" d="{poly(P(sec), close=True)}" stroke-width="0" opacity="0.75"/>')
    # wheel, upper part only
    r = MS * C.TYRE_R
    d.path("ln-thin", f"M{hx - r * math.cos(math.radians(12)):.1f},{hy + r * math.sin(math.radians(12)):.1f} "
                      f"A{r:.1f},{r:.1f} 0 1 1 {hx + r * math.cos(math.radians(12)):.1f},"
                      f"{hy + r * math.sin(math.radians(12)):.1f}")
    d.path("ln", catmull(P(arch)), sw=1.8)
    d.path("ln", poly(P([(364, 0), (366, C.SILL_Y)])), sw=1.8)
    d.path("ln", poly(P([(-379, 0), (-381, MYMIN)])), sw=1.8)
    d.path("ln", poly(P([(C.SHUT_X, MYMAX), (C.SHUT_X, C.junction_y())] + door_cut[1:])), sw=1.2)
    # seams
    d.path("fab-s dash", poly(P([(fm, ym), (xm, ym)])), sw=2.5)
    d.path("fab-s dash", poly(P([(xm, ym), (xm, C.REAR_SEAM_LOW)])), sw=2.5)
    d.path("fab-s dash", poly(P(front_c)), sw=2.5)
    # lip plug welds: round 1 (filled) every second position from the crown outward, round 2 (open) the rest
    pts = []
    for i in range(-15, 16):
        a = 90 + i * 6.2
        x = 369 * math.cos(math.radians(a))
        y = -28 + 369 * math.sin(math.radians(a)) - 6
        if y < 20:
            continue
        pts.append((i, sx(x), sy(y)))
    for i, x, y in pts:
        if i % 2 == 0:
            d.dot("fab-f", x, y, 2.6)
        else:
            d.circle("fab-s", x, y, 2.2, sw=1.2)
    # crown arrows: outward both ways
    d.path("fab-s", f"M{sx(-40):.1f},{sy(382):.1f} H{sx(-150):.1f}", sw=1.2, end="ahf")
    d.path("fab-s", f"M{sx(40):.1f},{sy(382):.1f} H{sx(150):.1f}", sw=1.2, end="ahf")
    # seam order badges
    badge(d, sx(-150), sy(ym) + 16, 1, "fab")
    badge(d, sx(xm) - 14, sy(400), 2, "fab")
    badge(d, sx(fm) + 24, sy(430), 3, "fab")
    badge(d, sx(0), sy(382), 4, "fab")
    d.text("t-xs", sx(MXMAX) - 2, top - 4, "front →", anchor="end")
    bot = sy(MYMIN)
    y = bot + 16
    d.text("t-sm", 8, y, "Joint order: 1 top seam, 2 rear seam, 3 front seam, 4 the lip.")
    y += LH
    x = 8
    for kind, txt in (("dot", "first round: every second spot, from the crown out;"),
                      ("ring", "then the rest.")):
        if kind == "dot":
            d.dot("fab-f", x + 4, y - 4, 2.8)
        else:
            d.circle("fab-s", x + 4, y - 4, 2.4, sw=1.2)
        d.text("t-sm", x + 12, y, txt)
        x += 12 + w("t-sm", txt) + 8
    y += LH
    d.text("t-sm", 8, y, "Seam lines: our inference from BMW drawings.")
    return y + 10


# ---------------------------------------------------------------- joint section (schematic)
def joint(d, top):
    d.text("t-h", 8, top + 16, "SKIN SEAM: BUTT JOINT OVER A STRIP")
    d.text("t-xs", 392, top + 16, "Section, not to scale", anchor="end")
    y0 = top + 66                      # top face of the skins
    t = 5                              # skin thickness as drawn (0.7-0.8 mm)
    g = 7                              # butt gap as drawn (0.8-1.0 mm)
    cx = 200                           # joint centre
    d.rect("keep", 8, y0, cx - g / 2 - 8, t, sw=1)
    d.rect("donor", cx + g / 2, y0, 392 - (cx + g / 2), t, sw=1)
    d.rect("fab", cx - 60, y0 + t + 1, 120, t, sw=1)                 # backing strip ~60 mm, ~30 each side
    for px in (cx - 44, cx - 22):                                    # plug welds, one side only
        d.rect("fab-f", px - 3, y0 - 1.5, 6, 2 * t + 2.5, rx=1)
    d.path("fab-f", f"M{cx - g / 2 - 1},{y0 - 2} h{g + 2} v{t + 3} h{-(g + 2)} Z")  # stitch in the gap
    d.text("t-sm", 8, y0 - 8, "your Touring")
    d.text("t-sm", 392, y0 - 8, "M3 section", anchor="end")
    lines(d, ("t-sm t-b", "t-sm"), cx, top + 36, ["Gap 0.8–1.0 mm,", "about one skin thickness"], anchor="middle")
    d.line("ln-thin", cx, top + 54, cx, y0 - 4)
    yd = y0 + 2 * t + 10
    d.line("ln-thin", cx - 60, yd - 4, cx - 60, yd + 4)
    d.line("ln-thin", cx + 60, yd - 4, cx + 60, yd + 4)
    d.line("ln", cx - 60, yd, cx + 60, yd, start="ah", end="ah")
    y = yd + 18
    d.text("t-sm fab-t", cx, y, "Backing strip ≈60 mm wide, ≈30 mm into each side (BMW)", anchor="middle")
    d.text("t-sm", cx, y + LH, "Skin-thickness steel, plug-welded or bonded to one side only.", anchor="middle")
    d.text("t-sm", cx, y + 2 * LH, "Skin ≈0.7–0.8 mm; flush within 0.5 mm across the seam.", anchor="middle")
    return y + 2 * LH + 12


# ---------------------------------------------------------------- order of work
def step(d, y, num, title, body, cls="shape"):
    h = 26 + len(body) * LH + 4
    d.rect(cls, BX0, y, BX1 - BX0, h, rx=6, sw=1.5)
    badge(d, BX0 + 19, y + 18, num)
    d.text("t t-b", BX0 + 37, y + 22, title)
    lines(d, "t-sm", BX0 + 37, y + 22 + LH + 2, body)
    return y + h


def check(d, y, body, head="Check"):
    h = 10 + len(body) * LH + 4
    d.rect("crit-s", BX0 + 30, y, BX1 - BX0 - 30, h, rx=4, sw=1.5)
    d.text("t-sm crit-t t-b", BX0 + 40, y + 16, head + ":")
    lines(d, "t-sm", BX0 + 40 + w("t-sm crit-t t-b", head + ":") + 6, y + 16, body)
    return y + h


def flow(d, y0, y1):
    """Down-arrow on the left between two elements."""
    d.line("ln", BX0 + 19, y0, BX0 + 19, y1, end="ah")
    return y1


def tack_strip(d, y):
    """Top seam tack order: centre, ends, midpoints, then halve the gaps to 25-30 mm."""
    x0, x1 = 112, 384
    d.text("t-sm", 44, y + 4, "top seam:")
    d.line("fab-s", x0, y, x1, y, sw=2)
    marks = {0.5: "1", 0.0: "2", 1.0: "3", 0.25: "4", 0.75: "5"}
    for i in range(17):
        f = i / 16
        if f not in marks:
            d.line("fab-s", x0 + f * (x1 - x0), y - 3, x0 + f * (x1 - x0), y + 3, sw=1.5)
    for f, n in marks.items():
        x = x0 + f * (x1 - x0)
        d.dot("fab-f", x, y, 3.6)
        d.text("t-xs t-b", x, y - 8, n, anchor="middle")
    return y + 12


def stitch_rows(d, y):
    """Skip order on the top seam: four passes put a stitch in every gap; then fill until continuous."""
    x0, pitch, n = 84, 25, 12
    passes = [("1st", (1, 5, 9)), ("2nd", (3, 7, 11)), ("3rd", (2, 6, 10)), ("4th", (4, 8, 12))]
    d.text("t-xs", 44, y, "gap")
    for g in range(1, n + 1):
        d.text("t-xs", x0 + (g - 0.5) * pitch, y, str(g), anchor="middle")
    y += 13
    done = []
    for name, gaps in passes:
        d.line("ln-thin", x0, y, x0 + n * pitch, y)
        for g in done:
            d.rect("fab", x0 + (g - 0.5) * pitch - 6, y - 3, 12, 6, rx=1.5, sw=1)
        for g in gaps:
            d.rect("fab-f", x0 + (g - 0.5) * pitch - 6, y - 3, 12, 6, rx=1.5)
        for g in range(n + 1):
            d.dot("fill-fg", x0 + g * pitch, y, 2.2)
        d.text("t-sm t-b", 44, y + 4, name)
        done += gaps
        y += 17
    d.line("fab-s", x0, y, x0 + n * pitch, y, sw=5)
    for g in range(n + 1):
        d.dot("fill-fg", x0 + g * pitch, y, 2.2)
    d.text("t-sm t-b", 44, y + 4, "fill")
    return y + 8


def build():
    d = kit.Doc()
    d.text("t-h", 8, 20, "ARCH SKIN: FIT, TACK, WELD")
    d.text("t-sm", 8, 38, "One side shown. Weld the other side between passes.")
    y = seam_map(d, 58)
    d.line("ln-faint", 8, y, 392, y)
    y = joint(d, y + 4)
    d.line("ln-faint", 8, y, 392, y)
    y += 22
    d.text("t-h", 8, y, "ORDER OF WORK")
    d.text("t-xs", 392, y, "Graft steps 8–11", anchor="end")
    y += 10
    G = 12

    y = step(d, y, 8, "Fit the skin", ["Trim to the butt gap; fit the backing strips.",
                                         "Clamps or clecos every 75–100 mm."])
    y = check(d, flow(d, y, y + G), ["every seam flush within 0.5 mm; lip at its",
                                    "target within 3 mm; door shuts; bumper fits"])
    y = step(d, flow(d, y, y + G), 9, "Tack, top seam first",
             ["Center, ends, then halve the gaps to a 25–30 mm",
              "pitch (≈30 tacks). Then the rear seam (ends,",
              "middle), then the front (top, bottom, middle, halves)."])
    y2 = tack_strip(d, y + 22)
    y = check(d, flow(d, y, y2 + 8), ["gap, flush, door and templates again.",
                                     "Adjust now, before any stitching."])
    y = step(d, flow(d, y, y + G), 10, "Plug-weld the lip",
             ["6 mm holes at the factory spot positions (your",
              "count from step 5), or bond and plug every second.",
              "Every second hole first, from the crown outward,",
              "alternately forward and back; then the rest.",
              "Pass a coupon first: plug 8–10 mm across, ≤3 mm",
              "high; broken apart, it tears a 3–8 mm hole."])
    y = step(d, flow(d, y, y + G), 11, "Stitch, skip, cool",
             ["10–15 mm welds between the tacks, never a long",
              "bead; at most ≈150 mm per seam per pass (our",
              "suggestion). Each pass: top seam, rear seam (odd",
              "gaps first), front seam, then the other side of",
              "the car. Weld beside a stitch only when hand-warm."])
    y2 = stitch_rows(d, y + 22)
    lines(d, "t-sm", 44, y2 + 14, ["Fill until the seam is continuous, as BMW", "welds its own seams."])
    y = check(d, flow(d, y, y2 + 2 * LH + 10), ["penetration visible on the back of every",
                                               "seam; grind and planish each one as it's done"])
    y = check(d, flow(d, y, y + G), ["every template within 1 mm; offsets left to", "right within 3 mm; "
                                     "body diagonals within", "±2 mm; door gaps and flush back"],
              head="After dressing")
    y += 14
    hb = 3 * LH + 12
    d.rect("warn-f", 8, y, 384, hb, rx=4, sw=1.2)
    lines(d, ("t-sm t-b", "t-sm"), 18, y + 18, ["Heat: overhead, turn the settings down 10–15%.",
                                                 "Gas: 75/25 argon/CO2 (BMW uses 82/18), never",
                                                 "pure argon."])
    y += hb + 8
    return kit.svg_open(W, int(y), ARIA, markers=("ah", "ahf")), d.body()


if __name__ == "__main__":
    print(C.run(build, NAME))
