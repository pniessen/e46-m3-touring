#!/usr/bin/env python3
"""Generator for diagrams/42-xi-driveline.svg (placeholder proposed-xi-driveline).

Portrait, 400 wide. Panel A: keeping all-wheel drive with the S54, a plan view from above,
front at the top (schematic). Panel B: the rear-drive conversion, a small plan with the
parts that come out, go in and stay.

Run:  python3 -I gen42.py      (re-runs itself once if new text widths had to be measured)
Data: research notes xi_keep_awd.md and xi_convert_rwd.md, and README fragment 0519.
"""
import sys
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.dont_write_bytecode = True
import kit  # noqa: E402  (my copy of the landscape kit; svg_open takes the width)
from kit import Doc, fmt  # noqa: E402

W = 400
WARN = []
LAST_BOX_BOTTOM = [0]

ARIA = (
    "Driveline of a 325xi Touring with the S54, seen from above with the front at the top; schematic, "
    "not to scale. Keeping all-wheel drive: the donor's S54 sits on your xi oil pan 11137519432, which has "
    "the right axle tube welded through its front. That front zone is the hazard: the S54's two-stage pump "
    "has its scavenge pickup there, so both documented builds fitted an M50-family single-stage pump and "
    "machined or re-made the pan, and on one the pump chain ground into the pan and wrecked the bottom end. "
    "Prove every clearance with clay and the oil pressure against the donor's. The front diff, type 174, "
    "bolts to the pan's left side; the right shaft runs through the tube to a support bracket on the pan's "
    "right side; the S54 headers' clearance to that shaft and bracket is unknown: check on the car. Behind "
    "the engine come the 330xi six-speed 23007563053, from 03/2003, on the M3 flywheel with a Z4 M clutch "
    "as in BMW's Z4 M, then the NV 124 transfer case 27107530812, which splits torque 38:62 at the same "
    "speed front and rear and is rated by BMW at 300 Nm, against the US S54's 355 Nm. The front prop shaft "
    "26207525970, 723 mm, runs forward on the left to the front diff; the rear prop shaft runs to the rear "
    "diff, type 188. The front and rear diff ratios must match: both builds used an X3 3.91 pair (the X3 2.5i's ratio), a "
    "325xi/330xi automatic 3.46 pair gives near-M3 gearing, and X3 rear flanges don't fit the xi rear "
    "shafts. Your front axle, knuckles, shafts and rack, the Bosch DSC 5.7 and its four sensors, the "
    "crossmember and the rear prop shaft stay. Converting to rear drive instead: the transfer case, front "
    "diff, front shafts and front prop shaft, the xi front subframe, knuckles and rack, and the Bosch DSC 5.7 "
    "with its sensors come out. In go the M3 front subframe and axle, trial-fitted first; the M3 gearbox "
    "on a custom crossmember bracket; the M3 lower steering joint and coupling; and an MK60 with an "
    "adapter loom, because the xi's plug is 42-pin with CAN on pins 24 and 40 and the MK60's is 47-pin "
    "with CAN on pins 11 and 15, so it is wired signal by signal. Everything behind the front seats is "
    "the same as on a 325i Touring."
)


def tw(cls, s):
    """Widest of the two renderings (site CSS, standalone style block)."""
    return max(kit.width(cls, s), kit.width_std(cls, s))


def check_fit(cls, s, maxw, where):
    w = tw(cls, s)
    if w > maxw:
        WARN.append(f"too wide by {w - maxw:.1f}: [{where}] {s!r} ({cls})")


class D(Doc):
    def lines(self, cls, x, y, rows, lh=14, anchor=None, maxw=None, where=""):
        for i, s in enumerate(rows):
            if maxw:
                check_fit(cls, s, maxw, where)
            self.text(cls, x, y + i * lh, s, anchor)
        return y + (len(rows) - 1) * lh

    def mixed(self, x, y, runs, maxw=None, where=""):
        """One line made of runs of different classes, laid out left to right."""
        cx = x
        for cls, s in runs:
            self.text(cls, cx, y, s)
            cx += tw(cls, s)
        if maxw and cx - x > maxw:
            WARN.append(f"too wide by {cx - x - maxw:.1f}: [{where}] {''.join(s for _, s in runs)!r}")
        return cx

    def runs(self, cls, x, y, parts, maxw=None, where="", anchor=None):
        """One <text> with <tspan> colour runs: parts = [(extra_cls_or_None, str), ...]."""
        full = "".join(t for _, t in parts)
        kit.width(cls, full)
        kit.width_std(cls, full)
        if maxw:
            check_fit(cls, full, maxw, where)
        self.rich(cls, x, y, parts, anchor)

    def xmark(self, x, y, s=7, sw=1.6):
        self.path("crit-s", f"M{fmt(x)},{fmt(y)} l{fmt(s)},{fmt(s)} M{fmt(x)},{fmt(y + s)} l{fmt(s)},{fmt(-s)}", sw=sw)


def key(d, y):
    """Two rows of swatches."""
    rows = [
        [("keep", "Keep"), ("donor", "From donor M3"), ("new", "Buy, used or new")],
        [("fab", "Modify"), ("crit", "Hazard, or check on the car"), ("out", "Comes out")],
    ]
    for r, items in enumerate(rows):
        x = 8
        yy = y + r * 20
        for cls, label in items:
            if cls == "crit":
                d.rect("crit-s dash", x, yy, 12, 12, rx=2, sw=1.5)
            elif cls == "out":
                d.rect("keep dash", x, yy, 12, 12, rx=2, sw=1)
                d.xmark(x + 2.5, yy + 2.5)
            else:
                d.rect(cls, x, yy, 12, 12, rx=2, sw=1)
            d.text("t-sm", x + 17, yy + 10.5, label)
            x += 17 + tw("t-sm", label) + 14
        if x - 14 > W - 8:
            WARN.append(f"key row {r} too wide: ends at {x - 14:.1f}")


def panel_a(d, y0):
    """Keep AWD: plan view. Returns the y where the panel ends."""
    d.comment("Panel A: keep all-wheel drive")
    d.text("t-h", 8, y0, "KEEP ALL-WHEEL DRIVE")
    d.text("t-sm", 8, y0 + 17, "Seen from above, front at the top. Schematic, not to scale.")

    # ---- hazard note in front of the car
    hy = y0 + 30
    rows = [
        "Your xi pan 11137519432 has the right axle tube welded",
        "through its front, the zone where the S54's two-stage pump",
        "has its scavenge pickup. Both builds fitted an M50-family",
        "single-stage pump instead. On one, the pump chain ground",
        "into the pan and wrecked the bottom end. Prove every",
        "clearance with clay, and oil pressure against the donor's.",
    ]
    hh = 26 + 14 * len(rows)
    FA = hy + hh + 52          # front axle line
    d.rect("warn-f", 8, hy, W - 16, hh, rx=5, sw=1.5)
    d.text("t t-b crit-t", 18, hy + 19, "Hazard: the front of the oil pan")
    d.lines("t-sm", 18, hy + 36, rows, maxw=W - 16 - 20, where="hazard")

    # ---- plan geometry
    ex0, ex1 = 168, 232        # engine block, plan
    ey0, ey1 = FA - 40, FA + 140
    gy1 = ey1 + 100            # gearbox rear face
    ty1 = gy1 + 30             # transfer case rear face
    RA = ty1 + 212             # rear axle line

    d.text("t-xs", 8, FA - 36, "left (driver's side)")
    d.text("t-xs", W - 8, FA - 36, "right", anchor="end")

    # wheels (yours)
    for x in (14, W - 34):
        d.rect("keep", x, FA - 26, 20, 52, rx=4, sw=1.5)
        d.rect("keep", x, RA - 26, 20, 52, rx=4, sw=1.5)

    # engine (donor) and the xi pan beneath it (modify)
    d.rect("donor", ex0, ey0, ex1 - ex0, ey1 - ey0, rx=6, sw=1.5)
    d.rect("fab", ex0 + 6, ey0 + 18, ex1 - ex0 - 12, ey1 - ey0 - 44, rx=4, sw=1.5)
    d.text("t-sm t-b donor-t", 200, ey1 - 9, "S54", anchor="middle")
    d.text("t-sm t-b fab-t", 200, FA + 72, "xi pan", anchor="middle")

    # S54 headers on the right of the engine (donor), schematic; the front one passes the bracket
    for yy in (FA - 14, FA + 10, FA + 34):
        d.path("donor-s", f"M{ex1},{yy} c12,0 18,6 18,24", sw=1.5)

    # front axle: shafts (yours), tube welded in the pan (yours), front diff (buy), bracket (yours)
    fdx0, fdx1 = 122, 158
    bx0 = ex1 + 6                                                          # support bracket
    d.line("keep-s", 34, FA, fdx0, FA, sw=3)
    d.rect("keep", fdx1, FA - 5, bx0 - fdx1, 10, rx=2, sw=1.2)            # welded tube
    d.line("keep-s", fdx1, FA, W - 34, FA, sw=3)                          # right shaft, through the tube
    d.rect("keep", bx0, FA - 8, 12, 16, rx=2, sw=1.5)
    d.rect("new", fdx0, FA - 14, fdx1 - fdx0, 28, rx=4, sw=2)             # front diff

    # hazard zone: the front of the engine and pan (pump, its chain, the pickups, the tube)
    d.rect("crit-s dash", ex0 - 3, ey0 - 3, ex1 - ex0 + 6, (FA + 22) - (ey0 - 3), rx=8, sw=2)
    d.line("crit-s", 200, hy + hh, 200, ey0 - 3, sw=1.5)
    # check zone: headers against the right shaft and its bracket
    hcx = bx0 + 14
    d.add(f'<ellipse class="crit-s dash" cx="{hcx}" cy="{FA + 4}" rx="14" ry="21" stroke-width="1.5"/>')

    # gearbox (buy), transfer case (buy, with the gearbox)
    gx0, gx1 = 172, 228
    d.path("new", f"M{gx0},{ey1} L{gx1},{ey1} L{gx1 - 6},{ey1 + 24} L{gx1 - 6},{gy1} L{gx0 + 6},{gy1} "
                  f"L{gx0 + 6},{ey1 + 24} Z", sw=2)
    tx0 = 128
    d.rect("new", tx0, gy1, (gx1 - 6) - tx0, ty1 - gy1, rx=4, sw=2)

    # prop shafts: front (buy, with the gearbox), rear (yours)
    fpx = (fdx0 + fdx1) / 2
    d.line("new-s", fpx, gy1, fpx, FA + 16, sw=3, end="ahn")
    d.line("keep-s", 200, ty1, 200, RA - 18, sw=3, end="ahk")

    # rear axle: diff (buy, matched to the front), shafts and wheels (yours)
    d.line("keep-s", 34, RA, 182, RA, sw=3)
    d.line("keep-s", 218, RA, W - 34, RA, sw=3)
    d.rect("new", 182, RA - 16, 36, 32, rx=4, sw=2)

    # ---- labels, left
    lx = 8
    lw = fpx - 8 - lx
    d.lines("t-sm t-b", lx, FA + 42, ["Front diff, type 174"], maxw=lw, where="FD")
    d.lines("t-sm", lx, FA + 56, ["bolted to the pan's", "left side"], maxw=lw, where="FD")
    d.line("ln-thin", 92, FA + 31, fdx0 + 6, FA + 15)
    yy = FA + 122
    d.lines("t-sm t-b", lx, yy, ["Front prop shaft"], maxw=lw, where="FP")
    d.lines("t-xs t-mono", lx, yy + 14, ["26207525970"], maxw=lw, where="FP")
    d.lines("t-sm", lx, yy + 28, ["723 mm, from", "03/2003"], maxw=lw, where="FP")

    # ---- labels, right
    rx = 258
    mw = W - 8 - rx
    yy = FA + 46
    d.lines("t-sm crit-t", rx, yy, ["Headers to the right", "shaft and bracket:", "check on the car"],
            maxw=mw, where="headers")
    d.line("crit-s", rx - 2, yy - 11, hcx + 5, FA + 23, sw=1)
    yy = FA + 104
    d.lines("t-sm", rx, yy, ["Pan machined or", "re-made on both builds"], maxw=mw, where="pan")
    d.line("ln-thin", rx - 4, yy - 4, ex1 - 6, yy - 4)
    yy = ey1 + 18
    d.lines("t-sm t-b", rx, yy, ["330xi six-speed"], maxw=mw, where="gbx")
    d.lines("t-xs t-mono", rx, yy + 14, ["23007563053"], maxw=mw, where="gbx")
    d.lines("t-sm", rx, yy + 28, ["from 03/2003, on the M3", "flywheel with a Z4 M", "clutch, as in BMW's Z4 M"],
            maxw=mw, where="gbx")
    d.line("ln-thin", rx - 4, yy - 4, gx1 - 5, yy - 4)
    yy = gy1 + 6
    d.lines("t-sm t-b", rx, yy, ["NV 124 transfer case"], maxw=mw, where="tc")
    d.lines("t-xs t-mono", rx, yy + 14, ["27107530812"], maxw=mw, where="tc")
    d.lines("t-sm", rx, yy + 28, ["38:62 torque, 1:1 speed"], maxw=mw, where="tc")
    d.lines("t-sm crit-t", rx, yy + 42, ["BMW: 300 Nm max;", "US S54: 355 Nm"], maxw=mw, where="tc")
    d.line("ln-thin", rx - 4, yy - 4, gx1 - 6, yy - 4)

    # ---- ratio rule and what stays, either side of the rear prop shaft
    by = ty1 + 50
    bw = 184
    rows = [
        "Both prop shafts turn at the",
        "same speed. Both builds used",
        "an X3 3.91 pair; the",
        "325xi/330xi automatic 3.46",
        "pair gives near-M3 gearing.",
        "X3 rear flanges don't fit",
        "the xi rear shafts.",
    ]
    bh = 26 + 14 * len(rows)
    LAST_BOX_BOTTOM[0] = by + bh
    d.rect("panel", 8, by, bw, bh, rx=5, sw=1)
    d.text("t-sm t-b", 16, by + 18, "Diff ratios must match")
    d.lines("t-sm", 16, by + 34, rows, maxw=bw - 16, where="ratio")

    rows = [
        "Your front axle, knuckles,",
        "shafts and rack; your",
        "Bosch DSC 5.7 and its four",
        "sensors; the crossmember",
        "and rear prop shaft.",
    ]
    d.rect("panel", W - 8 - bw, by, bw, 26 + 14 * len(rows), rx=5, sw=1)
    d.text("t-sm t-b", W - bw, by + 18, "Stays")
    d.lines("t-sm", W - bw, by + 34, rows, maxw=bw - 16, where="stays")

    d.text("t-sm", 200, RA + 40, "Rear diff, type 188: same ratio as the front", anchor="middle")
    return RA + 52, RA


def panel_b(d, y0):
    """Rear-drive conversion: what comes out (dashed box), then a small plan of the converted car
    beside what goes in. The front-seats line runs across the panel: behind it, nothing changes."""
    d.comment("Panel B: convert to rear drive")
    d.line("ln-faint", 8, y0, W - 8, y0)
    d.text("t-h", 8, y0 + 26, "OR CONVERT TO REAR DRIVE")
    d.text("t-sm", 8, y0 + 43, "The same view, smaller: the car after the conversion.")

    # ---- what comes out
    by = y0 + 56
    rows = [
        "Transfer case, front diff, front shafts and front prop shaft;",
        "the xi front subframe, knuckles and rack; the Bosch DSC 5.7",
        "with its sensors.",
    ]
    bh = 30 + 14 * len(rows)
    d.rect("keep dash", 8, by, W - 16, bh, rx=5, sw=1.5)
    d.xmark(18, by + 9, s=10, sw=2)
    d.text("t-sm t-b crit-t", 36, by + 18.5, "Comes out")
    d.lines("t-sm", 18, by + 36, rows, maxw=W - 16 - 20, where="out")

    # ---- what goes in, right column (sets the front-seats line)
    lx = 136
    mw = W - 8 - lx
    my0 = by + bh + 14
    y = my0 + 10
    d.rect("donor", lx, y - 10, 12, 12, rx=2, sw=1)
    d.text("t-sm t-b", lx + 18, y, "Goes in")
    y += 16
    d.runs("t-sm", lx, y, [(None, "M3 front subframe and axle:")], maxw=mw, where="in1")
    d.runs("t-sm", lx, y + 14, [("crit-t", "trial-fit it first")], maxw=mw, where="in1")
    y += 32
    d.runs("t-sm", lx, y, [(None, "M3 gearbox on a "), ("fab-t", "custom")], maxw=mw, where="in2")
    d.runs("t-sm", lx, y + 14, [("fab-t", "crossmember bracket")], maxw=mw, where="in2")
    y += 32
    d.text("t-sm", lx, y, "M3 lower steering joint and coupling")
    y += 18
    d.runs("t-sm", lx, y, [(None, "MK60 with an "), ("fab-t", "adapter loom")], maxw=mw, where="in4")
    y = d.lines("t-sm", lx, y + 14, [
        "xi: 42-pin plug, CAN pins 24/40",
        "MK60: 47-pin plug, CAN pins 11/15",
        "Wire it signal by signal",
    ], maxw=mw, where="in4")
    seat = y + 16
    d.line("ln dash", 8, seat, W - 8, seat, sw=1.5)
    d.text("t-xs", W - 8, seat + 14, "front seats", anchor="end")
    y = seat + 24
    d.rect("keep", lx, y - 10, 12, 12, rx=2, sw=1)
    d.text("t-sm t-b", lx + 18, y, "Stays")
    y = d.lines("t-sm", lx, y + 16, [
        "Everything behind the front seats",
        "is the same as on a 325i Touring",
    ], maxw=mw, where="stays")

    # ---- mini plan, left column
    cx = 68
    fy = my0 + 30
    ry = seat + 62
    gb1 = seat - 12                # gearbox rear
    gb0 = gb1 - 40                 # gearbox front = engine rear
    d.rect("keep", 10, seat, 116, ry + 26 - seat, rx=10, sw=1)        # behind the seats: as a 325i
    d.rect("ln-faint", 10, my0, 116, ry + 26 - my0, rx=18)
    for y_ in (fy, ry):
        d.rect("keep", 12, y_ - 14, 10, 28, rx=3, sw=1.2)
        d.rect("keep", 114, y_ - 14, 10, 28, rx=3, sw=1.2)
    # M3 front subframe and axle (donor), trial-fit first (red dashed)
    d.rect("donor", 28, fy - 5, 80, 10, rx=2, sw=1.5)
    d.rect("crit-s dash", 25, fy - 9, 86, 18, rx=4, sw=1.5)
    # S54 and 420G (donor) on a custom crossmember bracket (modify)
    d.rect("donor", cx - 13, fy - 22, 26, gb0 - (fy - 22), rx=4, sw=1.5)
    d.text("t-xs", cx, gb0 - 10, "S54", anchor="middle")
    d.path("donor", f"M{cx - 10},{gb0} L{cx + 10},{gb0} L{cx + 7},{gb0 + 10} L{cx + 7},{gb1} "
                    f"L{cx - 7},{gb1} L{cx - 7},{gb0 + 10} Z", sw=1.5)
    d.text("t-xs", cx - 12, gb0 + 22, "420G", anchor="end")
    d.rect("fab", cx - 18, gb1 - 8, 36, 7, rx=2, sw=1.5)
    # prop shaft and rear axle (donor, as in the main plan)
    d.line("donor-s", cx, gb1, cx, ry - 8, sw=2.5)
    d.rect("donor", cx - 8, ry - 8, 16, 16, rx=3, sw=1.5)
    d.line("donor-s", 22, ry, cx - 8, ry, sw=2)
    d.line("donor-s", cx + 8, ry, 114, ry, sw=2)
    # DSC: the MK60 goes in on the left (donor); the Bosch DSC 5.7 on the right comes out
    dy = fy + 30
    d.rect("donor", 26, dy, 20, 14, rx=2, sw=1.5)
    d.text("t-xs", 36, dy - 5, "MK60", anchor="middle")
    d.rect("keep dash", 94, dy, 20, 14, rx=2, sw=1.2)
    d.xmark(100.5, dy + 3.5)
    d.text("t-xs", 122, dy - 5, "DSC 5.7", anchor="end")
    return max(y, ry + 26) + 8


def build():
    d = D()
    key(d, 6)
    y, ra = panel_a(d, 66)
    assert ra - 26 > LAST_BOX_BOTTOM[0] + 8, "rear wheels hit the ratio box"
    y = panel_b(d, y + 10)
    H = int(y + 8)
    aria = ARIA
    head = kit.svg_open(W, H, aria, markers=("ah", "ahn", "ahk", "ahd", "ahc"))
    return head, d.body()


def main():
    for _ in range(3):
        WARN.clear()
        head, body = build()
        if not kit.flush_measurements():
            break
    p = kit.write("42-xi-driveline.svg", head, body)
    print("wrote", p)
    for w in WARN:
        print("WARN", w)


if __name__ == "__main__":
    main()
