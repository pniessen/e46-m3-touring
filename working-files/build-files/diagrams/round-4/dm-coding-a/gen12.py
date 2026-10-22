#!/usr/bin/env python3
"""Redraw diagrams/12-coding-order.svg (README Figure 9): the manual's coding sessions in order, their tools,
the two decisions (immobilizer route, DSC unit) and the two non-coding steps in between.

Round-4 changes against last round's gen12.py (same layout otherwise):
- Session 4: the M3 cluster keeps the donor's vehicle order and is coded only from its own read-out
  (coordinator's correction from BMW's coding data: no FA_WRITE of the Touring's order into the cluster).
- Session 8: the order is read from ALSZ; only the modules a change touches are coded; never Code Car.
- The alignment is done in BMW's design position at the M3 load (TIS 32 00; README Phase 12 wording).
- Review fix F5: Session 1 tools add Tool32; Session 2's alternative is a used DME matched to your EWS by a vendor,
  or virginized and synced by you (Session 3 is a check after a vendor's match); option B codes from a session
  order (donor's type key, #0902 or later), then sets values for your parts.
Run:  python3 -I gen12.py   (from this folder; measures new labels in Chromium, then writes the SVG)
"""
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, __import__("os").path.dirname(__file__))
from ckit import Doc, run, width  # noqa: E402

L, R = (8, 188), (204, 188)      # lanes: x, width
LC, RC = 102, 298                # lane centres
GAP = 12                         # vertical gap holding an arrow
PAD = 10


def wrap2(cls, s, first_w, rest_w):
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

    def fits(cls, s, x, right):
        if x + width(cls, s) > right - 3:
            over.append(f"{s!r} ends at {x + width(cls, s):.1f} > {right - 3}")

    def rect(cls, x, y, w, h, sw="1.5", rx=5):
        d.add(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" stroke-width="{sw}"/>')

    def down(x, y0):
        d.add(f'<line class="ln" x1="{x}" y1="{y0}" x2="{x}" y2="{y0 + GAP - 1}" marker-end="url(#ah)"/>')

    def session(y, title, tool, lines, x=8, w=384, h=None):
        """White box: title, tool (right of the title, or right of the first detail line when it doesn't fit
        there), then detail lines. A string is wrapped to fit; h pads the box to match its lane partner."""
        inner = w - 2 * PAD
        kw = width("t-sm t-mono", tool)
        on_title = width("t t-b", title) + kw + 12 <= inner
        first = inner if on_title else inner - kw - 12
        if isinstance(lines, str):
            lines = wrap2("t-xs", lines, first, inner)
        h = max(h or 0, 24 + 14 * len(lines))
        rect("shape", x, y, w, h)
        d.text("t t-b", x + PAD, y + 16, title)
        d.text("t-sm t-mono", x + w - PAD, y + (16 if on_title else 30), tool, "end")
        for i, s in enumerate(lines):
            d.text("t-xs", x + PAD, y + 30 + 14 * i, s)
            fits("t-xs", s, x + PAD, x + w - (0 if (on_title or i) else kw + 12))
        return y + h

    def option(y, lane, cls, title, lines, h=62):
        x, w = lane
        rect(cls, x, y, w, h)
        d.text("t t-b", x + PAD, y + 17, title)
        for i, (s, c) in enumerate(lines):
            d.text(c, x + PAD, y + 31 + 13 * i, s)
            fits(c, s, x + PAD, x + w)
        return y + h

    def other(y, title, line):
        """A step that isn't a coding session."""
        rect("panel", 8, y, 384, 26)
        d.text("t t-b", 18, y + 17.5, title)
        d.text("t-xs", 128, y + 17.5, line)
        fits("t-xs", line, 128, 392)
        return y + 26

    def lanes_down(y):
        down(LC, y)
        down(RC, y)
        return y + GAP

    d.comment("Key")
    rect("donor", 8, 6, 12, 12, "1", 2)
    d.text("t-sm", 25, 16.5, "From donor M3")
    rect("keep", 122, 6, 12, 12, "1", 2)
    d.text("t-sm", 139, 16.5, "Keep")
    rect("panel", 186, 6, 12, 12, "1", 2)
    d.text("t-sm", 203, 16.5, "Not coding")

    d.comment("1: backups")
    y = session(26, "1  Back up everything", "NCS Expert, PA-Soft, INPA, Tool32",
                "Phase 0: vehicle order, codings, cluster and light-module memories")
    down(200, y)

    d.comment("2: DME, and the immobilizer decision")
    y = session(y + GAP, "2  DME VIN and EWS", "Tool32, a vendor", ["Read in Phase 1; vendor work in Phase 3"])
    y = lanes_down(y)
    option(y, L, "donor", "EWS delete", [("recommended", "t-xs t-b"), ("bought as a service, with", "t-xs"),
                                           ("your VIN written in", "t-xs")])
    y = option(y, R, "donor", "Matched used DME", [("matched to your EWS by a vendor,", "t-xs"),
                                                     ("or virginized and synced by you", "t-xs"),
                                                     ("no documented Touring success", "t-xs crit-t")])
    y = lanes_down(y)
    y = other(y, "Wire, then check", "Phase 11: re-pin, ohm-check, then power up")
    y = lanes_down(y)

    d.comment("3: EWS, depending on the route")
    s3 = ["a check after a vendor's match;", "sync a DME you virginized"]
    session(y, "3  EWS check", "Tool32", ["nothing to code after a delete"], *L, h=24 + 14 * len(s3))
    y = session(y, "3  Check or sync", "Tool32", s3, *R)
    y = lanes_down(y)

    d.comment("4: cluster (it keeps the donor's vehicle order), then 5: the DSC and its decision")
    y = session(y, "4  Cluster and light module", "PA-Soft, NCS Expert",
                ["Phase 11: your VIN and true mileage, by a service or new chip;",
                 "the cluster keeps the donor's vehicle order: code it from its own read-out"])
    down(200, y)
    y = session(y + GAP, "5  DSC coding and VIN", "PA-Soft, NCS Expert, INPA",
                ["Phase 11, after session 4: the DSC checks its VIN against the cluster's"])
    y = lanes_down(y)
    b_rows = [("09/2002-on donors only", "t-xs t-b")] + [
        (ln, "t-xs") for ln in wrap2("t-xs", "write your VIN, code from a session order (donor's type key, #0902+), "
                                     "set values for your parts, then initialise", R[1] - 2 * PAD, R[1] - 2 * PAD)]
    hb = 31 + 13 * (len(b_rows) - 1) + 9
    option(y, L, "keep", "A  Keep your MK60", [("recommended", "t-xs t-b"), ("initialise its VIN and", "t-xs"),
                                                 ("steering angle", "t-xs")], h=hb)
    y = option(y, R, "donor", "B  The M3's MK60", b_rows, h=hb)
    y = lanes_down(y)

    d.comment("6: first start; alignment; 7: steering angle; 8 and 9")
    y = session(y, "6  First start, adaptations, throttle check", "Tool32",
                ["Phase 12: adaptations cleared, the throttles relearn"])
    down(200, y)
    y = other(y + GAP, "Wheel alignment", "in BMW's design position, at the M3 load")
    down(200, y)
    y = session(y + GAP, "7  Steering angle after the alignment", "INPA or Tool32",
                ["Phase 12: wheel straight, car level, no brake pressure"])
    down(200, y)
    y = session(y + GAP, "8  Vehicle-order changes and body modules", "NCS Expert",
                ["Phase 12, after session 7, whenever you change the order: read it from ALSZ;",
                 "code only the modules a change touches, one at a time; never Code Car"])
    down(200, y)
    y = session(y + GAP, "9  Light module and headlights", "NCS Expert", ["Phase 12, last, with the front end on"])
    if over:
        print("DOES NOT FIT:", *over, sep="\n  ", flush=True)
    height = y + 8

    aria = ("The coding sessions in the manual's order, with their tools. 1: back up the vehicle order, every "
            "module's coding and the cluster and light-module memories (NCS Expert, PA-Soft, INPA, Tool32) in Phase 0. 2: "
            "the DME's VIN and EWS work (Tool32 and a vendor), read in Phase 1 with the vendor work in Phase 3. "
            "Decision: an EWS delete bought as a service, recommended, or a used DME matched to your EWS by a vendor, "
            "or virginized and synced by you, which no Touring build has documented working. Then wire and check "
            "in Phase 11. 3: the EWS in Tool32: a check, with nothing to code, after a delete or a vendor's match, "
            "or a sync for a DME you virginized. 4: the cluster and light module (PA-Soft, "
            "NCS Expert): the M3 cluster gets your VIN and true mileage through a service or a new chip, keeps the "
            "donor's vehicle order, and is coded only from its own read-out. 5: the DSC (PA-Soft, NCS Expert, INPA), "
            "after the cluster because the DSC checks its VIN against it. Decision: keep your MK60 and initialise "
            "it, recommended, or fit the M3's MK60 from a 09/2002-on donor: write your VIN, code it from a session "
            "order with the donor's type key and #0902 or later, set values for your parts, then initialise it. 6: first start with the adaptations cleared (Tool32). Then the wheel alignment, in BMW's design "
            "position at the M3 load, then 7: the steering-angle calibration "
            "(INPA or Tool32). 8: vehicle-order changes and body modules (NCS Expert): read the order from the "
            "light module (ALSZ), code only the modules a change touches, one at a time, and never use Code Car. "
            "9, last: the light module and headlights (NCS Expert).")
    return height, aria


if __name__ == "__main__":
    run(build, "12-coding-order.svg")
