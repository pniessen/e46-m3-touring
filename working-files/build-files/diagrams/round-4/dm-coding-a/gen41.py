#!/usr/bin/env python3
"""Generate diagrams/41-identity-storage.svg (WIRING-AND-CODING, Session 4; replaces the placeholder
proposed-identity-storage). Portrait, 400 wide.

Top: where the car's identity lives. The light module (ALSZ) holds your VIN (last 7 characters), your true
mileage (steps of 100 km, only ever up) and your Touring's vehicle order, the car's true order. The M3 cluster
(AKMB) holds your VIN and your true mileage (taken from the light module) and keeps the donor M3's order for good
(coordinator's correction from BMW's coding data: an M3 cluster is accepted only with an M3 order). The DME and
the DSC unit hold a VIN and no order; the EWS holds your VIN but no order on a car built from 09/2001.
Bottom: which copy Sessions 1, 4, 5, 8 and 9 read and write. No FA_WRITE into the cluster.
Run:  python3 -I gen41.py
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(__file__))
from ckit import Doc, run, width  # noqa: E402

X0, X1 = 8, 392
PAD = 10


def wrap(cls, s, maxw):
    words, lines, cur = s.split(" "), [], ""
    for w in words:
        cand = (cur + " " + w) if cur else w
        if cur and width(cls, cand, queue=False) > maxw:
            lines.append(cur)
            cur = w
        else:
            cur = cand
    if cur:
        lines.append(cur)
    for ln in lines:
        width(cls, ln)
    return lines


def build(d: Doc):
    d.markers = ("ah",)
    over = []

    def chk(cls, s, x, right, anchor=None):
        w = width(cls, s)
        x0 = x - w if anchor == "end" else (x - w / 2 if anchor == "middle" else x)
        if x0 + w > right + 0.01 or x0 < 2:
            over.append(f"{s!r}: {x0:.1f}..{x0 + w:.1f} (limit {right})")

    # ------------------------------------------------------------------ key
    d.comment("Key")
    kx = 8
    for cls, label in [("keep", "Keep"), ("donor", "From donor M3"), ("new", "Buy new"),
                       ("shape", "NCS Expert session")]:
        d.rect(cls, kx, 6, 12, 12, rx=2, sw=1)
        d.text("t-sm", kx + 17, 16.5, label)
        kx += 17 + width("t-sm", label) + 14
    if kx > X1 + 14:
        over.append("key too wide")

    # ------------------------------------------------------------------ module cards
    def card(y, cls, title, right, right_cls, rows, footer=None):
        """Full-width card: title (and a right-hand note), then label/value rows; values wrap."""
        vx = X0 + PAD + 82
        body = []
        for label, value in rows:
            lines = wrap("t-xs", value, X1 - 3 - vx)
            body.append((label, lines))
        n = sum(len(v) for _, v in body)
        h = 22 + 13 * n + (13 if footer else 0) + 6
        d.rect(cls, X0, y, X1 - X0, h, rx=5, sw=1.5)
        d.text("t t-b", X0 + PAD, y + 17, title)
        d.text(right_cls, X1 - PAD, y + 17, right, "end")
        if width("t t-b", title) + 12 + width(right_cls, right) > X1 - X0 - 2 * PAD:
            over.append(f"card title {title!r}")
        yy = y + 22 + 10
        for label, lines in body:
            d.text("t-xs t-b", X0 + PAD, yy, label)
            for ln in lines:
                d.text("t-xs", vx, yy, ln)
                chk("t-xs", ln, vx, X1 - 3)
                yy += 13
        if footer:
            d.text("t-xs crit-t", X0 + PAD, yy, footer)
            chk("t-xs crit-t", footer, X0 + PAD, X1 - 3)
        return y + h

    d.text("t-xs t-b", X0, 40, "WHERE THE CAR'S IDENTITY LIVES")
    y = 48
    d.comment("The light module: the car's own record")
    y = card(y, "keep", "Light module (ALSZ)", "your Touring's: the master record", "t-xs t-b",
             [("VIN", "the last 7 characters of yours"),
              ("Mileage", "your true mileage, in steps of 100 km; it can only go up"),
              ("Vehicle order", "your Touring's: the car's true order, and the source for every other module")],
             footer="Never write a VIN or mileage into it to match a cluster.")
    alsz_bot = y

    d.comment("Between the two: the key-on compare, and the one-way mileage transfer")
    gap_top = y
    col = [(X0, 196), (204, X1)]
    labels = [["Compared at every key-on: a", "mismatch lights the tamper dot"],
              ["Your true mileage passes to the", "cluster only once the VINs", "match and the cluster reads zero"]]
    n = max(len(l) for l in labels)
    gap_h = 12 + 13 * n + 4
    akmb_top = gap_top + gap_h
    # left: double-headed compare arrow
    ax = X0 + 14
    d.line("ln", ax, gap_top + 1, ax, akmb_top - 1, end="ah", start="ah")
    for i, s in enumerate(labels[0]):
        d.text("t-xs", ax + 10, gap_top + 16 + 13 * i, s)
        chk("t-xs", s, ax + 10, col[0][1])
    # right: mileage, light module down to the cluster
    bx = col[1][0] + 10
    d.line("ln", bx, gap_top + 1, bx, akmb_top - 1, end="ah")
    for i, s in enumerate(labels[1]):
        d.text("t-xs", bx + 10, gap_top + 16 + 13 * i, s)
        chk("t-xs", s, bx + 10, X1)

    d.comment("The M3 cluster: your VIN and true mileage, the donor's vehicle order")
    y = card(akmb_top, "donor", "M3 cluster (AKMB)", "KMBE46M3.C23 or C24", "t-xs t-mono",
             [("VIN", "yours, set by a service or on a new chip"),
              ("Mileage", "your car's true mileage only, from the light module"),
              ("Vehicle order", "the donor M3's after the chip route, left there for good: NCS accepts an M3 "
                                "cluster only with an M3 order"),
              ("Coding", "only from a complete coding file made from its own read-out")])
    akmb_bot = y

    d.comment("The other modules: a VIN, but no vehicle order")
    small = [("donor", "DME", "MSS54 or HP", ["VIN: yours, in a free AIF slot (Session 2).",
                                              "No vehicle order: it isn't coded from one."]),
             ("keep", "DSC unit", "MK60", ["VIN: initialised, or written into an M3 unit (Session 5).",
                                          "No vehicle order."]),
             ("keep", "EWS", "yours", ["Holds your VIN, but no vehicle order (from 09/2001): not a backup copy."])]
    sw_, sg = 120, 12
    top = akmb_bot + 26
    wrapped = []
    for cls, t1, t2, paras in small:
        lines = []
        for p in paras:
            lines += wrap("t-xs", p, sw_ - 2 * PAD)
        wrapped.append(lines)
    sh = 22 + 13 * max(len(l) for l in wrapped) + 6
    for i, ((cls, t1, t2, paras), lines) in enumerate(zip(small, wrapped)):
        x = X0 + i * (sw_ + sg)
        d.rect(cls, x, top, sw_, sh, rx=5, sw=1.5)
        d.rich("t", x + PAD, top + 17, [("t-b", t1), ("t-xs", "  " + t2)])
        if width("t t-b", t1) + width("t t-xs", "  " + t2) > sw_ - 2 * PAD:
            over.append(f"small title {t1}")
        for j, ln in enumerate(lines):
            d.text("t-xs", x + PAD, top + 32 + 13 * j, ln)
            chk("t-xs", ln, x + PAD, x + sw_ - 3)
    # the DSC unit checks its VIN against the cluster's
    mx = X0 + sw_ + sg + sw_ / 2
    d.line("ln", mx, top - 1, mx, akmb_bot + 1, end="ah")
    d.text("t-xs", mx + 8, akmb_bot + 17, "checks its VIN against the cluster's")
    chk("t-xs", "checks its VIN against the cluster's", mx + 8, X1)
    y = top + sh

    # ------------------------------------------------------------------ sessions
    y += 24
    d.text("t-xs t-b", X0, y, "WHICH COPY EACH SESSION READS AND WRITES")
    y += 8
    L, M, R = (X0, 76), (156, 88), (316, 76)          # chip x, width: 72 px gaps hold the arrow labels

    def chip(c, y0, cls, lines):
        x, w = c
        h = 26 if len(lines) == 1 else 36
        d.rect(cls, x, y0, w, h, rx=4, sw=1.5)
        for i, s in enumerate(lines):
            yy = y0 + (17.5 if len(lines) == 1 else 15 + 12 * i)
            d.text("t-sm t-b" if i == 0 else "t-xs", x + w / 2, yy, s, "middle")
            chk("t-sm t-b" if i == 0 else "t-xs", s, x + w / 2, x + w - 3, "middle")
        return h

    def harrow(xa, xb, ya, label, lcls="t-xs", below=False):
        d.line("ln", xa, ya, xb, ya, end="ah")
        lx = (xa + xb) / 2
        d.text(lcls, lx, ya + 15 if below else ya - 5, label, "middle")
        w = width(lcls, label)
        if w > abs(xb - xa) - 4:
            over.append(f"arrow label {label!r} {w:.1f} > {abs(xb - xa) - 4}")

    rows = [
        dict(head="Session 1, Phase 0: your Touring's own cluster still fitted",
             chips=[("keep", ["ALSZ"]), ("shape", ["NCS session"]), ("keep", ["AKMB"])],
             arrows=[("LM", "read", 0), ("RM", "read", 0)],
             note="Both copies hold your order and should match; if not, trust ALSZ. Screenshot the donor's "
                  "order too, in the donor (Phase 1)."),
        dict(head="Session 4: the M3 cluster fitted",
             chips=[("keep", ["ALSZ"]), ("shape", ["NCS session"]), ("donor", ["AKMB"])],
             arrows=[("LM", "read", 0), ("RM", "read", -6), ("MR", "code", 6)],
             note="ALSZ must still match your Session 1 screenshot. Code the cluster with its own (the donor's) "
                  "order loaded, from its own read-out. Write no order into it."),
        dict(head="Session 5, option B only: the M3's MK60",
             chips=[("keep", ["ALSZ"]), ("shape", ["NCS session"]), ("donor", ["M3 MK60"])],
             arrows=[("LM", "read", 0), ("MR", "code", 0)],
             note="For this session only: a date of #0902 or later and the donor's M3 type code. No FA_WRITE."),
        dict(head="Session 8: a vehicle-order change",
             chips=[("keep", ["ALSZ"]), ("shape", ["NCS session"]), ("keep", ["Modules it", "touches"])],
             arrows=[("LM", "read", -6), ("ML", "FA_WRITE", 6), ("MR", "code", 0)],
             note="Change it in the session and write it back to ALSZ only. The cluster keeps the donor's order. "
                  "Never run Code Car."),
        dict(head="Session 9, xenon only: a new light module",
             chips=[("new", ["New ALSZ"]), ("shape", ["NCS session"]), ("donor", ["AKMB"])],
             arrows=[("ML", "FA_WRITE", 0), ("RL", "true mileage", None)],
             note="It holds no order yet: type yours from your Session 1 screenshot and add $522. Once it has "
                  "your VIN, it takes the cluster's true mileage, so fit only a new or virginized module."),
    ]
    pos = {"L": L, "M": M, "R": R}
    for r in rows:
        d.comment(r["head"])
        d.text("t-xs t-b", X0, y + 11, r["head"])
        chk("t-xs t-b", r["head"], X0, X1)
        cy = y + 22
        hs = [chip(pos[k], cy, cls, lines) for k, (cls, lines) in zip("LMR", r["chips"])]
        ch = max(hs)
        mid = cy + ch / 2
        extra_below = 0
        for spec, label, off in r["arrows"]:
            a, b = pos[spec[0]], pos[spec[1]]
            lcls = "t-xs t-mono" if label == "FA_WRITE" else "t-xs"
            if off is None:      # routed under the chips (AKMB to the new light module)
                ya = cy + ch + 8
                xa, xb = a[0] + a[1] / 2, b[0] + b[1] / 2
                d.path("ln", f"M{xa},{cy + hs['LMR'.index(spec[0])]} V{ya} H{xb} V{cy + hs['LMR'.index(spec[1])] + 1}",
                       end="ah")
                d.text(lcls, (M[0] + M[1] / 2), ya + 12, label, "middle")
                extra_below = max(extra_below, 22)
                continue
            if b[0] > a[0]:
                xa, xb = a[0] + a[1], b[0] - 1
            else:
                xa, xb = a[0], b[0] + b[1] + 1
            below = off > 0
            harrow(xa, xb, mid + off, label, lcls, below=below)
            if below:
                extra_below = max(extra_below, mid + off + 17 - (cy + ch))
        ny = cy + ch + max(extra_below, 0) + 14
        lines = wrap("t-xs", r["note"], X1 - X0)
        for i, ln in enumerate(lines):
            d.text("t-xs", X0, ny + 13 * i, ln)
            chk("t-xs", ln, X0, X1)
        y = ny + 13 * (len(lines) - 1) + 14

    height = y + 4
    if over:
        print("DOES NOT FIT:", *over, sep="\n  ", flush=True)

    aria = (
        "Where the car's identity lives after the swap, and which copy each coding session reads and writes. "
        "The light module (ALSZ), your Touring's own, is the master record: it holds the last 7 characters of "
        "your VIN, your true mileage in steps of 100 km, which can only go up, and your Touring's vehicle order, "
        "the car's true order and the source for every other module; never write a VIN or mileage into it to "
        "match a cluster. At every key-on it and the cluster compare VIN and mileage, and a mismatch lights the "
        "tamper dot; your true mileage passes to the cluster only once the VINs match and the cluster reads "
        "zero. The M3 cluster (AKMB, coding file KMBE46M3.C23 or C24) holds your VIN, set by a service or on a "
        "new chip, and your car's true mileage only, taken from the light module; after the chip route it holds "
        "the donor M3's vehicle order, which stays there for good, because NCS accepts an M3 cluster only with "
        "an M3 order, and it is coded only "
        "from a complete coding file made from its own read-out. The DME (MSS54 or HP) holds your VIN in a free "
        "AIF slot (Session 2) and no vehicle order. The DSC unit (MK60) holds a VIN, initialised or written into "
        "an M3 unit in Session 5, checks it against the cluster's, and holds no vehicle order. Your EWS holds your "
        "VIN but no vehicle order on a car built from 09/2001, so it is no backup copy. Session 1, with your own cluster "
        "still fitted: NCS Expert reads the order from ALSZ and from AKMB; they should match, and if not, trust "
        "ALSZ; the donor's order is screenshot in the donor in Phase 1. Session 4, with the M3 cluster fitted: "
        "read ALSZ, which must still match the Session 1 screenshot, and read AKMB, which holds the donor's "
        "order; code the cluster with that order loaded, from its own read-out, and write no order into it. "
        "Session 5, option B only: read ALSZ, give the session a date of #0902 or later and the donor's M3 type "
        "code for this session only, and code the M3 MK60, with no FA_WRITE. Session 8, a vehicle-order change: "
        "read ALSZ, change the order in the session, FA_WRITE it back to ALSZ only, and code only the modules "
        "the change touches; the cluster keeps the donor's order, and Code Car is never run. Session 9, xenon only, with a new light "
        "module: it holds no order yet, so type yours from the Session 1 screenshot, add $522 and FA_WRITE it "
        "to the new module; once it has your VIN it takes the cluster's true mileage, so fit only a new or "
        "virginized module.")
    return height, aria


if __name__ == "__main__":
    run(build, "41-identity-storage.svg")
