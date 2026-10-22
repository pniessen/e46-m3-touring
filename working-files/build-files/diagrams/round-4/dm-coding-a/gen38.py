#!/usr/bin/env python3
"""Generate diagrams/38-flow-coding-sessions.svg (WIRING-AND-CODING, "Coding step by step";
replaces the placeholder proposed-coding-sessions-flow). Portrait, 400 wide.

Sessions 1-9 and the wheel alignment, in the manual's order, with the decisions that change them:
the donor DME (MSS54 or MSS54HP: no change; SMG: manual software in Session 2), the immobilizer route
(EWS delete, or a used DME matched to your EWS by a vendor or virginized and synced by you: lanes through
Sessions 2 and 3; review fix F6), the Touring's DME family (MS43 or MS45.1:
wiring only) and the DSC unit (A or B: lanes at Session 5). Dashed back-edges from Session 8 go only to the
sessions that code what a change touches: the cluster (Session 4), an M3 DSC unit (Session 5) and, only after
an engine-side change, the adaptations (Session 6).

Rules from the coordinator's corrections (22 Oct): the M3 cluster keeps the donor's vehicle order for good and is
coded only from its own read-out; ALSZ holds the car's order and is the source for every other module; no Code
Car; the alignment is done in BMW's design position at the M3 load.
Run:  python3 -I gen38.py
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(__file__))
from ckit import Doc, run, width  # noqa: E402

X0, X1 = 8, 366            # main column (the right margin carries the back-edges)
W = X1 - X0
LL, LW = 8, 174            # left lane x, width
RL, RW = 192, 174          # right lane x, width
LC, RC = LL + LW / 2, RL + RW / 2   # lane centres; LC is the spine
CH = 384                   # back-edge channel
PAD = 10
GAP = 12


def wrap2(cls, s, first_w, rest_w):
    """Greedy wrap with a narrower (or wider) first line."""
    words, lines, cur = s.split(" "), [], ""
    for w in words:
        lim = first_w if not lines else rest_w
        cand = (cur + " " + w) if cur else w
        if cur and width(cls, cand, queue=False) > lim:
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
    over = []

    def chk(cls, s, x, right, anchor=None):
        w = width(cls, s)
        x0 = x - w if anchor == "end" else x
        if x0 + w > right + 0.01:
            over.append(f"{s!r}: right edge {x0 + w:.1f} > {right}")

    def down(x, y0, y1):
        d.line("ln", x, y0, x, y1 - 1, end="ah")

    def session(y, title, tool, detail, x=X0, w=W):
        """White box: title (and tool, right) then wrapped detail lines. Returns the bottom."""
        inner = w - 2 * PAD
        tw, kw = width("t t-b", title), width("t-sm t-mono", tool)
        tool_on_title = tw + 12 + kw <= inner
        first = inner if tool_on_title else inner - kw - 12
        lines = wrap2("t-xs", detail, first, inner)
        h = 30 + 13 * (len(lines) - 1) + 8
        d.rect("shape", x, y, w, h, rx=5, sw=1.5)
        d.text("t t-b", x + PAD, y + 16, title)
        chk("t t-b", title, x + PAD, x + w - 3)
        d.text("t-sm t-mono", x + w - PAD, y + (16 if tool_on_title else 30), tool, "end")
        for i, s in enumerate(lines):
            d.text("t-xs", x + PAD, y + 30 + 13 * i, s)
            chk("t-xs", s, x + PAD, x + w - 3 - (0 if (tool_on_title or i) else kw + 12))
        return y + h

    def opt_lines(w, rows):
        lines = []
        for s, c in rows:
            for ln in wrap2(c, s, w - 2 * PAD, w - 2 * PAD):
                lines.append((ln, c))
        return lines

    def opt_need(w, rows):
        return 31 + 13 * (len(opt_lines(w, rows)) - 1) + 8

    def option(y, x, w, cls, title, rows, h):
        """A lane box: bold title, then rows of (text, class); long rows wrap."""
        lines = opt_lines(w, rows)
        d.rect(cls, x, y, w, h, rx=5, sw=1.5)
        d.text("t t-b", x + PAD, y + 17, title)
        chk("t t-b", title, x + PAD, x + w - 3)
        for i, (s, c) in enumerate(lines):
            d.text(c, x + PAD, y + 31 + 13 * i, s)
            chk(c, s, x + PAD, x + w - 3)
        return y + h

    def lane_pair(y, left, right):
        """left/right = (cls, title, rows): two lane boxes of equal height."""
        h = max(opt_need(LW, left[2]), opt_need(RW, right[2]))
        option(y, LL, LW, *left, h)
        option(y, RL, RW, *right, h)
        return y + h

    def pill(y, x, w, s):
        d.rect("shape", x, y, w, 26, rx=13, sw=1.5)
        d.text("t", x + w / 2, y + 17.5, s, "middle")
        chk("t", s, x + 10, x + w - 10)
        return y + 26

    def lead_w(cls, lead):
        """Width of a bold lead such as "yes: " (a trailing space isn't measured, so add one)."""
        return width(cls, lead.rstrip()) + (3.4 if lead.endswith(" ") else 0)

    def outcome(y, rows, x=RL + 6):
        """Answers to the right of a pill: a short arrow from the pill, then rows of (bold lead, text)."""
        d.line("ln", LL + LW, y + 13, x - 4, y + 13, end="ah")
        n = sum(len(wrap2("t-xs", t, X1 - 3 - x - lead_w("t-xs t-b", lead), X1 - 3 - x - lead_w("t-xs t-b", lead)))
                for lead, t in rows)
        yy = y + 13 + 3.5 - 6.5 * (n - 1)          # centre the block on the arrow
        yy = max(yy, y + 9)
        for lead, t in rows:
            lw = lead_w("t-xs t-b", lead)
            lines = wrap2("t-xs", t, X1 - 3 - x - lw, X1 - 3 - x - lw)
            for i, ln in enumerate(lines):
                if i == 0 and lead:
                    d.rich("t-xs", x, yy, [("t-b", lead), (None, ln)])
                else:
                    d.text("t-xs", x + lw, yy, ln)
                chk("t-xs", ln, x + lw, X1 - 3)
                yy += 13
        return max(y + 26, yy - 13 + 5)

    # ------------------------------------------------------------------ key
    d.comment("Key")
    kx, ky = 8, 6
    items = [("pill", "Choice"), ("keep", "Keep"), ("donor", "From donor M3"), ("panel", "Not coding")]
    for kind, label in items:
        if kind == "pill":
            d.rect("shape", kx, ky, 20, 12, rx=6, sw=1.2)
            kx += 26
        else:
            d.rect(kind, kx, ky, 12, 12, rx=2, sw=1)
            kx += 17
        d.text("t-sm", kx, ky + 10.5, label)
        kx += width("t-sm", label) + 16
    ky2 = 24
    d.path("ln dash", f"M8,{ky2 + 6} H36", end="ah")
    d.text("t-sm", 42, ky2 + 10.5, "Loops back after Session 8, only for what a change touches")
    chk("t-sm", "Loops back after Session 8, only for what a change touches", 42, 392)

    y = 44
    # ------------------------------------------------------------------ Session 1
    d.comment("Session 1")
    y = session(y, "1  Vehicle order and codings", "NCS Expert",
                "Phase 0, before you change anything; the donor in Phase 1. Screenshot the order from ALSZ "
                "and AKMB, and save every module's coding.")
    down(LC, y, y + GAP)
    y += GAP

    # ------------------------------------------------------------------ the donor DME: two choices
    d.comment("Choices about the donor DME: neither changes the order of the sessions")
    p = pill(y, LL, LW, "MSS54 or MSS54HP?")
    yb = outcome(y, [("either: ", "the same sessions")])
    y = max(p, yb)
    down(LC, y, y + GAP)
    y += GAP
    p = pill(y, LL, LW, "SMG donor?")
    yb = outcome(y, [("yes: ", "Session 2 adds manual (“HS”) software"),
                     ("no: ", "its US software, as it is")])
    y = max(p, yb)
    down(LC, y, y + GAP)
    y += GAP

    # ------------------------------------------------------------------ immobilizer route: two lanes
    d.comment("Immobilizer route: the lanes run through Sessions 2 and 3")
    p = pill(y, LL, LW, "Immobilizer route?")
    d.path("ln", f"M{LL + LW},{y + 13} H{RC} V{p + GAP - 1}", end="ah")
    down(LC, p, p + GAP)
    y = p + GAP
    y = lane_pair(y, ("donor", "EWS delete", [("recommended", "t-xs t-b"), ("your VIN written in", "t-xs")]),
                  ("donor", "Matched used DME", [("matched to your EWS by a vendor, or virginized and synced "
                                                  "by you", "t-xs"),
                                                 ("no documented Touring success", "t-xs crit-t")]))
    down(LC, y, y + GAP)
    down(RC, y, y + GAP)
    y += GAP

    d.comment("Session 2")
    y = session(y, "2  DME VIN, EWS delete and gearbox software", "Tool32, a vendor",
                "Read in Phase 1; vendor work in Phase 3, before the first key-on")
    down(LC, y, y + GAP)
    down(RC, y, y + GAP)
    y += GAP

    # ------------------------------------------------------------------ wiring, with the DME-family choice
    d.comment("Wire, then check; the Touring's DME family changes the wiring only")
    top = y
    mark = len(d.parts)          # the panel goes in here once its height is known
    d.text("t t-b", X0 + PAD, top + 17.5, "Wire, then check")
    s = "Phase 11: re-pin, ohm-check, then power up"
    sx = X0 + PAD + width("t t-b", "Wire, then check") + 8
    d.text("t-xs", sx, top + 17.5, s)
    chk("t-xs", s, sx, X1 - 3)
    pill_y = top + 28
    pill(pill_y, LL + PAD, LW - PAD, "MS43 or MS45.1?")
    ob = outcome(pill_y, [("", "changes only the wiring, not the sessions")])
    pan_h = max(pill_y + 26, ob) - top + 9
    d.parts.insert(mark, f'<rect class="panel" x="{X0}" y="{top}" width="{W}" height="{pan_h}" rx="5" '
                         f'stroke-width="1.5"/>')
    y = top + pan_h
    down(LC, y, y + GAP)
    down(RC, y, y + GAP)
    y += GAP

    # ------------------------------------------------------------------ Session 3, per route
    d.comment("Session 3, by immobilizer route")
    yl = session(y, "3  EWS check", "Tool32", "nothing to code after a delete", LL, LW)
    yr = session(y, "3  Check or sync", "Tool32", "after a vendor's match, a check; with a virgin DME, the sync, "
                 "or the donor's EWS fitted and re-aligned", RL, RW)
    y = max(yl, yr)
    down(LC, yl, y + GAP)
    down(RC, yr, y + GAP)
    y += GAP

    # ------------------------------------------------------------------ Session 4 and 5
    d.comment("Session 4: the M3 cluster keeps the donor's vehicle order")
    s4_top = y
    y = session(y, "4  Cluster and light module", "PA-Soft, NCS Expert",
                "Phase 11: your VIN and true mileage in the M3 cluster, by a service or new chip. It keeps the "
                "donor's vehicle order: code it only from its own read-out.")
    s4_bot = y
    down(LC, y, y + 16)
    y += 16
    d.comment("Session 5 and the DSC choice")
    y = session(y, "5  DSC coding and VIN", "PA-Soft, NCS Expert, INPA",
                "Phase 11, after Session 4: the DSC checks its VIN against the cluster's")
    s5_bot = y
    down(LC, y, y + 16)
    y += 16
    p = pill(y, LL, LW, "DSC unit?")
    d.path("ln", f"M{LL + LW},{y + 13} H{RC} V{p + GAP - 1}", end="ah")
    d.text("t-xs", (LL + LW + RC) / 2 + 22, y + 9, "chosen before Session 2", "middle")
    down(LC, p, p + GAP)
    y = p + GAP
    y = lane_pair(y, ("keep", "A  Keep your MK60", [("recommended", "t-xs t-b"), ("the initialisation only: in INPA, Shift+F4, its three compensation routines", "t-xs")]),
                  ("donor", "B  The M3's MK60",
                   [("09/2002-on donors only", "t-xs t-b"),
                    ("a VIN write, coding from a late session order read from ALSZ, M3 values in its coding "
                     "file, then the initialisation", "t-xs")]))
    down(LC, y, y + GAP)
    down(RC, y, y + GAP)
    y += GAP

    # ------------------------------------------------------------------ Sessions 6 to 9
    d.comment("Session 6, the alignment, Sessions 7, 8 and 9")
    y = session(y, "6  First start, adaptations and throttle check", "Tool32",
                "Phase 12: adaptations cleared, the throttles relearn")
    s6_bot = y
    down(LC, y, y + 16)
    y += 16
    d.rect("panel", X0, y, W, 26, rx=5, sw=1.5)
    d.text("t t-b", X0 + PAD, y + 17.5, "Wheel alignment")
    s = "in BMW's design position, at the M3 load"
    d.text("t-xs", X0 + PAD + width("t t-b", "Wheel alignment") + 8, y + 17.5, s)
    chk("t-xs", s, X0 + PAD + width("t t-b", "Wheel alignment") + 8, X1 - 3)
    y += 26
    down(LC, y, y + GAP)
    y += GAP
    y = session(y, "7  Steering angle after the alignment", "INPA or Tool32",
                "Phase 12: the alignment moves the wheel's straight-ahead position, so Session 5's zero "
                "was provisional")
    down(LC, y, y + 18)
    lab = "a change loops back only to the modules it touches"
    d.text("t-xs", CH - 6, y + 13, lab, "end")
    chk("t-xs", lab, CH - 6 - width("t-xs", lab), CH - 6)
    y += 18
    s8_top = y
    y = session(y, "8  Vehicle-order changes and body modules", "NCS Expert",
                "Phase 12, after Session 7, and whenever you change the order: read it from ALSZ, change it "
                "and write it back there, then code only the modules the change touches, one at a time")
    down(LC, y, y + GAP)
    y += GAP
    y = session(y, "9  Light module and headlights", "NCS Expert", "Phase 12, last, with the front end on")

    # ------------------------------------------------------------------ back-edges from Session 8
    d.comment("Back-edges from Session 8: only to the sessions that code what a change touches")
    ex = s8_top + 10
    targets = [(s6_bot - 9, "clear the adaptations only after an engine-side change"), (s5_bot - 9, "an M3 DSC unit"),
               (s4_bot - 9, "the cluster, from its own coding file")]
    for ty, label in targets:
        d.path("ln dash", f"M{X1},{ex} H{CH} V{ty} H{X1 + 1}", end="ah")
        d.text("t-xs", CH - 6, ty + 9 + 12, label, "end")

    # ------------------------------------------------------------------ rules
    y += 14
    d.comment("Rules for every session")
    rules = [
        ("panel", [("t-b", "Vehicle order: "), (None, "read your car's from ALSZ, the light module, never "
                                                     "from the swapped cluster, which keeps the donor's.")]),
        ("crit-s", [("t-b crit-t", "Never on this car: "), (None, "Code Car or Process Car, or default-coding "
                                                                  "the M3 cluster or an M3 DSC unit. Code those "
                                                                  "two only from complete coding files made from "
                                                                  "their own read-outs.")]),
    ]
    for cls, runs in rules:
        # first run bold, then the rest wrapped after it
        lead_c, lead = runs[0]
        rest = runs[1][1]
        lw = lead_w(f"t {lead_c}", lead)
        lines = wrap2("t", rest, W - 2 * PAD - lw, W - 2 * PAD)
        h = 18 + 16 * (len(lines) - 1) + 9
        d.rect(cls, X0, y, W, h, rx=5, sw=1.5)
        d.rich("t", X0 + PAD, y + 17, [(lead_c, lead), (None, lines[0])])
        chk("t", lines[0], X0 + PAD + lw, X1 - 3)
        for i, ln in enumerate(lines[1:], 1):
            d.text("t", X0 + PAD, y + 17 + 16 * i, ln)
            chk("t", ln, X0 + PAD, X1 - 3)
        y += h + 8
    height = y

    if over:
        print("DOES NOT FIT:", *over, sep="\n  ", flush=True)

    aria = (
        "Flowchart of the nine coding sessions and the wheel alignment, in order, with the choices that change "
        "them. 1, vehicle order and codings (NCS Expert): in Phase 0, before you change anything, and on the "
        "donor in Phase 1, screenshot the order from the light module (ALSZ) and the cluster (AKMB) and save "
        "every module's coding. Then the donor DME: MSS54 or MSS54HP makes no difference to the sessions; an "
        "SMG donor adds manual (HS) software to Session 2, and a manual donor keeps its US software as it is. "
        "Immobilizer route: an EWS delete with your VIN written in, recommended, or a used DME matched to your EWS "
        "by a vendor (once, in a 330i) or virginized and synced yourself (no Touring success). 2, DME VIN, EWS delete and gearbox software (Tool32, a vendor): read in "
        "Phase 1, vendor work in Phase 3, before the first key-on. Then wire and check in Phase 11; whether your "
        "Touring has an MS43 or an MS45.1 changes only the wiring, not the sessions. 3, EWS (Tool32): after a "
        "delete or a vendor's match, a check "
        "with nothing to code; with a virgin DME, the sync, or the donor's EWS fitted and re-aligned. 4, cluster "
        "and light module (PA-Soft, NCS Expert): the M3 cluster gets your VIN and true mileage by a service or a "
        "new chip, keeps the donor's vehicle order and is coded only from its own read-out. 5, DSC coding and VIN "
        "(PA-Soft, NCS Expert, INPA), after Session 4 because the DSC checks its VIN against the cluster's. DSC "
        "unit, chosen before Session 2: A, keep your MK60, recommended, which needs only the initialisation, "
        "INPA's three compensation routines under Shift+F4; or B, "
        "the M3's MK60 from a 09/2002-on donor: a VIN write, coding from a late session order read from ALSZ, M3 "
        "values in its coding file, then the initialisation. 6, first start, adaptations and throttle check "
        "(Tool32). Wheel alignment in BMW's design position at the M3 load. 7, steering angle after the "
        "alignment (INPA or Tool32), because the alignment moves the straight-ahead position. 8, vehicle-order "
        "changes and body modules (NCS Expert), after Session 7 and whenever you change the order: read it from "
        "ALSZ, change it and write it back there, then code only the modules the change touches, one at a time. "
        "Dashed back-edges from Session 8 go only to Session 4 for the cluster, from its own coding file, to "
        "Session 5 for an M3 DSC unit, and to Session 6 to clear the adaptations only after an engine-side "
        "change. 9, light module and headlights (NCS Expert), last, with the front end on. Rules: read your car's "
        "vehicle order from ALSZ, never from the swapped cluster, which keeps the donor's; never use Code Car or "
        "Process Car, and never default-code the M3 cluster or an M3 DSC unit: code them only from complete "
        "coding files made from their own read-outs.")
    return height, aria


if __name__ == "__main__":
    run(build, "38-flow-coding-sessions.svg")
