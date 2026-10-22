"""Shared helpers for dm-arches generators (figures 27, 28 and redraws 08, 09).

Builds on kit.py (copied from last round's landscape kit): the house <style> block, markers and
a Chromium-measured text-width cache. All four figures use it; portrait figures simply pass width 400.
"""
import math
import kit
from kit import Doc, fmt  # noqa: F401  (re-exported)


def w(cls: str, s: str) -> float:
    """Widest of the page (site fonts) and standalone widths, so labels fit in both."""
    return max(kit.width(cls, s), kit.width_std(cls, s))


def run(build, name: str):
    """Build once to queue every label for measurement, measure, then build again and write."""
    build()
    if kit.flush_measurements():
        build()
    head, body, = build()
    return kit.write(name, head, body)


# ---------------------------------------------------------------- geometry helpers
def catmull(pts, closed=False, tension=0.5):
    """Smooth SVG path data through screen points (Catmull-Rom as cubic Beziers)."""
    if len(pts) < 3:
        return "M" + " L".join(f"{fmt(round(x, 1))},{fmt(round(y, 1))}" for x, y in pts)
    p = list(pts)
    d = [f"M{fmt(round(p[0][0], 1))},{fmt(round(p[0][1], 1))}"]
    n = len(p)
    for i in range(n - 1):
        p0 = p[i - 1] if i > 0 else p[i]
        p1, p2 = p[i], p[i + 1]
        p3 = p[i + 2] if i + 2 < n else p[i + 1]
        c1 = (p1[0] + (p2[0] - p0[0]) * tension / 3, p1[1] + (p2[1] - p0[1]) * tension / 3)
        c2 = (p2[0] - (p3[0] - p1[0]) * tension / 3, p2[1] - (p3[1] - p1[1]) * tension / 3)
        d.append("C" + " ".join(f"{fmt(round(a, 1))},{fmt(round(b, 1))}" for a, b in (c1, c2, p2)))
    return " ".join(d)


def poly(pts, close=False):
    s = "M" + " L".join(f"{fmt(round(x, 1))},{fmt(round(y, 1))}" for x, y in pts)
    return s + (" Z" if close else "")


def arc_pts(cx, cy, r, a0, a1, n=24):
    """Points on a circle (mm space, angles in degrees, 0 = +X forward, 90 = +Y up)."""
    return [(cx + r * math.cos(math.radians(a0 + (a1 - a0) * i / n)),
             cy + r * math.sin(math.radians(a0 + (a1 - a0) * i / n))) for i in range(n + 1)]


# ---------------------------------------------------------------- right-side view, mm
# Rear hub centre = (0, 0); X + forward (ahead of the axle), Y + up. Sources: notes rear_arches.md,
# Guide-ready C1 (arch edge, M3 bulge boundary, reference lines) and the README text
# ("Flare profile", "Rear arches and doors"). [E] = scaled from drawings, +-5-10 mm.
ARCH = [(364, 0), (334, 122), (307, 177), (274, 230), (228, 272), (175, 303), (120, 329), (61, 344),
        (0, 348), (-61, 344), (-119, 327), (-176, 305), (-227, 271), (-273, 229), (-308, 178),
        (-339, 123), (-362, 64), (-379, 0)]
BULGE = [(315, 376), (244, 422), (165, 454), (83, 473), (0, 475), (-82, 463), (-158, 435),
         (-227, 393), (-285, 339), (-306, 306)]
BUMPER_Y = 305          # bumper top line (text: about 305 above the hub)
CREASE_Y = 540          # shoulder crease
BELT_Y = 640            # beltline, where the door's trailing edge ends (notes C1)
LAMP_X = -700           # tail lamp starts (text: about 700 behind)
LAMP_LOW = 360          # tail-lamp lower edge (notes C1/B2, +-20)
SILL_Y = -40            # sill flange (notes C1, measure)
TOP_SEAM = (500, 515)   # text: 500-515 above the hub
REAR_SEAM = (-600, -550)  # text: 550-600 behind the axle
REAR_SEAM_LOW = 250     # text: down to about 250 above the hub, hidden by the bumper
SHUT_X = 335            # door trailing edge (text: door meets the arch 300-350 ahead, 150-250 up)
FRONT_SEAM = (25, 40)   # text: 25-40 mm behind the shut line
ARC_C = (0, -28)        # arch circle-fit centre (notes: Touring R ~369, 28 below the hub)
R_ARCH = 369
R_DOOR = 415            # door's cut edge round the arch: drawn generically (measure)
TYRE_R = 330            # M3 255/40R18, unloaded radius ~330.6 (orientation only)
RIM_R = 229             # 18-inch rim
FLAP = (-430, -330, 370, 470)  # filler flap: generic position (not measurable from the drawings)


def junction_y(r=R_DOOR, x=SHUT_X):
    return ARC_C[1] + math.sqrt(r * r - x * x)


def door_cut_pts(r=R_DOOR, x_top=SHUT_X, y_bottom=SILL_Y, n=16):
    """Door's cut edge: from the junction with the vertical shut line round the arch to the sill."""
    a_top = math.degrees(math.atan2(junction_y(r, x_top) - ARC_C[1], x_top))
    a_bot = math.degrees(math.asin((y_bottom - ARC_C[1]) / r))
    return arc_pts(ARC_C[0], ARC_C[1], r, a_top, a_bot, n)


def arch_y_at(x):
    """Arch-edge height at a given X on the upper arch (linear between C1 points)."""
    pts = ARCH
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        if min(x1, x2) <= x <= max(x1, x2) and x1 != x2:
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    raise ValueError(x)


def arch_x_at(y, rear=True):
    """Arch-edge X at height y on the rear (or front) flank."""
    pts = ARCH[ARCH.index((0, 348)):] if rear else ARCH[: ARCH.index((0, 348)) + 1]
    for (x1, y1), (x2, y2) in zip(pts, pts[1:]):
        if min(y1, y2) <= y <= max(y1, y2) and y1 != y2:
            return x1 + (x2 - x1) * (y - y1) / (y2 - y1)
    raise ValueError(y)


# Plan-view offsets, M3 skin proud of the Touring's (mm) at stations along the car (X).
# Curve: notes C3 values; the ramp starts at about +420 (C1). Labels use the README text's table.
OFFSETS = [(420, 0), (350, 16), (300, 22), (200, 21), (100, 21), (0, 23), (-100, 23), (-150, 25),
           (-200, 29), (-250, 29), (-300, 31), (-350, 32), (-400, 22), (-450, 13), (-500, 10), (-600, 7)]


def offset_at(x):
    for (x1, y1), (x2, y2) in zip(OFFSETS, OFFSETS[1:]):
        if x2 <= x <= x1:
            return y1 + (y2 - y1) * (x - x1) / (x2 - x1)
    return 0.0
