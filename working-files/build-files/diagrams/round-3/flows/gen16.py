"""Figure: which DME your Touring has (placeholder flow-which-dme), from the manual's "Which DME your Touring has"."""
import sys
sys.dont_write_bytecode = True
from flowkit import *  # noqa: F401,F403

W = 800
OUT = HERE / "out"
NB = " "
EN = "–"

ARIA = ("How to tell which DME your US 325i Touring with a manual gearbox has, and which move table to use. "
        "The DME changed with March 2003 production: MS43 before, MS45.1 from then on. "
        "First check the engine code: an M56 SULEV also runs an MS45.1, with a CAN-controlled pump module and a "
        "returnless metal tank, and this manual doesn't cover it; a manual gearbox doesn't prove an M54; if the code is "
        "unreadable, stop and don't re-pin until the label or INPA answers. "
        "Then work down the tests, most reliable first, until one answers: 1, the DME label in the E-box, but a car built "
        "in 02 or 03/2003 also needs tests 4 and 5; 2, INPA or NCS Expert; 3, ETK by VIN under Programmed DME control unit: "
        "an MS43 unit means MS43, the manual-gearbox MS45.1 units 12147561526, 12147561528 and 12147562340 mean MS45.1, and "
        "another number can't tell; 4, where the 0.75 SW/RT leak-test heater wire sits, in the body side of X6011 pin 7 on "
        "an MS43 built from 09/2001 or in X60004 pin 2 on an MS45.1; 5, wires in X60004 pins 5 and 15 mean an MS45.1; "
        "6, unverified, the main air-mass meter plug is said to have three wires on an MS43 and five on an MS45.1, and "
        "with neither, stop and don't re-pin until the label or INPA answers. "
        "An MS43 uses the table MS43 Touring: what to move, with Earlier MS43 Tourings below it for cars built before "
        "09/2001; an MS45.1, often written MS45, uses MS45.1 Touring: what to move; both with an M3 donor built from "
        "09/2001. The coils and valve cover are not a test; on a 325xi, never assume, read the label.")

# Geometry
LX0, LX1 = 8, 140            # MS43 result column
RX0, RX1 = 660, 792          # MS45.1 result column
QX0, QX1 = 160, 640          # question ladder
QW = QX1 - QX0
CX = (QX0 + QX1) / 2
SIDE = 72                    # width of the answer zones at each end of a question box
GAP = 22                     # vertical gap between questions (holds the down arrow)


def question(y, num, text, sub=None, left=None, right=None, min_h=40):
    """A decision box: answer zones at the left and right ends, the question in the middle.
    left/right: list of (cls, text) lines shown in the end zone. Returns (svg, height)."""
    runs = [("t-b", num + NB + NB), ("", text)] if num else [("", text)]
    blocks = [Block("t", runs, anchor="middle")]
    for sl in ([sub] if isinstance(sub, str) else (sub or [])):
        blocks.append(Block("t-sm", sl, gap_before=0, anchor="middle"))
    zl = max([line_width(c, t) for c, t in (left or [])] + [0]) + 26
    zr = max([line_width(c, t) for c, t in (right or [])] + [0]) + 26
    z = max(zl, zr, 50)  # symmetric zones keep the question centred on the arrows
    inner_w = QW - 2 * z
    th, _ = measure_box(inner_w, blocks, pad_x=2, pad_top=6, pad_bottom=8)
    h = max(th, min_h)
    tsvg, _, _ = layout_blocks(blocks, QX0 + z, y + (h - th) / 2, inner_w, pad_x=2, pad_top=6, pad_bottom=8)
    out = [f'<rect class="shape" x="{QX0}" y="{fmt(y)}" width="{QW}" height="{fmt(h)}" rx="18" stroke-width="1.5"/>', tsvg]
    for side, lines in (("l", left), ("r", right)):
        if not lines:
            continue
        n = len(lines)
        lh = 14.0
        y0 = y + h / 2 - (n - 1) * lh / 2 + 4.3
        for i, (cls, s) in enumerate(lines):
            if side == "l":
                out.append(text_el(cls, QX0 + 16, y0 + i * lh, s))
            else:
                out.append(text_el(cls, QX1 - 16, y0 + i * lh, s, "end"))
    return "\n".join(out), h


def build():
    parts = []
    k, kx = key_row(8, 7, ["question", "go", "stop", "caution"],
                    labels={"go": "Your move table", "stop": "Stop"})
    parts.append(k)
    parts.append(line(f"M{fmt(kx + 22)},13 H{fmt(kx + 46)}", cls="ln dash"))
    parts.append(text_el("t-sm", kx + 52, 17.5, "Unverified"))

    # Start: the car and the date of the change
    y = 30
    s, h = box(QX0, y, QW, [Block("t t-b", "US 325i Touring with a manual gearbox", anchor="middle"),
                            Block("t", "The DME changed with March 2003 production:", gap_before=0, anchor="middle"),
                            Block("t", "MS43 before, MS45.1 from then on.", gap_before=0, anchor="middle")],
               cls="panel", rx=4)
    parts.append(s)
    start_bottom = y + h

    # Q0: engine code
    y = start_bottom + GAP
    parts.append(arrow(f"M{fmt(CX)},{fmt(start_bottom)} V{fmt(y - 1)}"))
    s, h0 = question(y, "", "Check the engine code: M54 or M56?", sub="A manual gearbox doesn't prove an M54.",
                     left=[("t t-b", "unreadable")], right=[("t t-b", "M56")])
    parts.append(s)
    q0_mid = y + h0 / 2
    q0_bottom = y + h0
    # Stop boxes beside Q0: the M56 (top right) and an unreadable engine code (left)
    stop_blocks = [Block("t t-b crit-t", "Not covered"),
                   Block("t", "The M56 SULEV also runs an MS45.1, with a CAN-controlled pump module and a returnless metal tank.",
                         gap_before=0)]
    STOP_Y = 8
    s, sh = box(RX0, STOP_Y, RX1 - RX0, stop_blocks, cls="crit-s", rx=4)
    parts.append(s)
    parts.append(arrow(f"M{QX1},{fmt(q0_mid)} H{RX0 - 1}"))
    dont = [Block("t t-b crit-t", "Stop"), Block("t", "Don't re-pin until the label or INPA answers.", gap_before=0)]
    dh, _ = measure_box(LX1 - LX0, dont)
    dy0 = max(30, q0_mid + 16 - dh)          # the box's lower part meets the arrow
    s, dh = box(LX0, dy0, LX1 - LX0, dont, cls="crit-s", rx=4)
    parts.append(s)
    parts.append(arrow(f"M{QX0},{fmt(q0_mid)} H{LX1 + 1}"))
    left_stop_bottom = dy0 + dh
    assert dy0 + 10 < q0_mid < left_stop_bottom - 6

    # Ladder
    qs = [
        ("1", "The DME label in the E-box: what does it say?", "Built 02 or 03/2003: confirm with tests 4 and 5.",
         [("t t-b", "MS43")], [("t t-b", "MS45.1")], "unreadable"),
        ("2", "INPA or NCS Expert: which DME does it identify?", None,
         [("t t-b", "MS43")], [("t t-b", "MS45.1")], "can't tell"),
        ("3", "ETK by VIN, under \"Programmed DME control unit\"",
         ["Manual-gearbox MS45.1 units:", "12147561526, 12147561528, 12147562340"],
         [("t-sm t-b", "an MS43"), ("t-sm t-b", "unit")], [("t t-b", "MS45.1")], "another number: can't tell"),
        ("4", "Where is the leak-test heater wire?", "0.75 SW/RT. In X6011 on an MS43 built from 09/2001.",
         [("t-sm t-b", "body X6011"), ("t-sm t-b", f"pin{NB}7")], [("t-sm t-b", "X60004"), ("t-sm t-b", f"pin{NB}2")],
         "can't tell"),
        ("5", "Do X60004 pins 5 and 15 carry wires?",
         "0.5 SW/GE and SW/RT, for the secondary-air air-mass sensor",
         None, [("t t-b", "yes")], "no"),
        ("6", "Main air-mass meter plug: how many wires?", "Unverified: said to be 3 on an MS43 and 5 on an MS45.1.",
         [("t t-b", f"3{NB}wires")], [("t t-b", f"5{NB}wires")], "neither"),
    ]
    y = q0_bottom + GAP
    parts.append(arrow(f"M{fmt(CX)},{fmt(q0_bottom)} V{fmt(y - 1)}"))
    parts.append(text_el("t-sm t-b", CX + 7, q0_bottom + GAP / 2 + 4, "M54"))
    ladder_top = y
    assert ladder_top > max(STOP_Y + sh, left_stop_bottom) + 8 and STOP_Y + 12 < q0_mid < STOP_Y + sh - 12, \
        (ladder_top, sh, left_stop_bottom)
    mids = []
    for i, (num, q, sub, left, right, down) in enumerate(qs):
        s, h = question(y, num, q, sub, left, right)
        parts.append(s)
        mids.append((y + h / 2, left is not None, right is not None, num == "6"))
        ny = y + h + GAP
        parts.append(arrow(f"M{fmt(CX)},{fmt(y + h)} V{fmt(ny - 1)}"))
        parts.append(text_el("t-sm t-b", CX + 7, y + h + GAP / 2 + 4, down))
        last_bottom = y + h
        y = ny
    ladder_bottom = last_bottom
    # Test 6 gives neither: stop
    s, hn = box(QX0, y, QW, [Block("t", [("t-b crit-t", "Stop:"), ("", " don't re-pin until the label or INPA answers.")],
                                   anchor="middle")], cls="crit-s", rx=4)
    parts.append(s)
    neither_bottom = y + hn

    # Result columns
    ms43 = [Block("t t-b", "MS43"),
            Block("t", "Use the table", gap_before=0),
            Block("t-sm", "\"MS43 Touring: what to move\"", gap_before=0),
            Block("t", "for a Touring built from 09/2001 to 02/2003, with an M3 donor built from 09/2001.", gap_before=0),
            Block("t", "Built before 09/2001:", gap_before=10),
            Block("t-sm", "\"Earlier MS43 Tourings\", below that table", gap_before=0)]
    s, _ = box(LX0, ladder_top, LX1 - LX0, ms43, cls="new", rx=4, min_h=ladder_bottom - ladder_top)
    parts.append(s)
    ms45 = [Block("t", [("t-b", "MS45.1"), ("", " (often written MS45)")]),
            Block("t", "Use the table", gap_before=0),
            Block("t-sm", "\"MS45.1 Touring: what to move\"", gap_before=0),
            Block("t", "for a Touring built from 03/2003 with the M54 and a manual gearbox, with an M3 donor built from "
                       "09/2001.", gap_before=0),
            Block("t-sm", "In ETK, by build date:", gap_before=10),
            Block("t-sm", f"12147561526 (03/2003{EN}07/2004)", gap_before=0),
            Block("t-sm", f"12147561528 (07/2004{EN}09/2005)", gap_before=0),
            Block("t-sm", f"12147562340 (from{NB}09/2005)", gap_before=0)]
    s, _ = box(RX0, ladder_top, RX1 - RX0, ms45, cls="new", rx=4, min_h=ladder_bottom - ladder_top)
    parts.append(s)
    for my, l, r, dashed in mids:
        cls = "ln dash" if dashed else "ln"
        if l:
            parts.append(arrow(f"M{QX0},{fmt(my)} H{LX1 + 1}", cls))
        if r:
            parts.append(arrow(f"M{QX1},{fmt(my)} H{RX0 - 1}", cls))

    # Bottom cautions
    y = neither_bottom + 14
    w1 = (W - 16 - 14) / 2
    w2 = W - 16 - 14 - w1
    b1 = [Block("t", [("t-b", "Not a test:"), ("", " the coils and the valve cover. BMW changed those at 09/2002, before the DME.")])]
    b2 = [Block("t", [("t-b", "A 325xi:"), ("", " never assume. ETK lists it with MS43 and no end date, yet with the 325i's "
                                               "\"from Mar '03\" engine harness and secondary-air sensor. Read the label.")])]
    hb = max(measure_box(w1, b1)[0], measure_box(w2, b2)[0])
    s1, _ = box(8, y, w1, b1, cls="warn-f", rx=4, min_h=hb)
    s2, _ = box(8 + w1 + 14, y, w2, b2, cls="warn-f", rx=4, min_h=hb)
    parts += [s1, s2]
    H = int(round(y + hb + 8))
    return svg_doc(W, H, ARIA, "\n".join(parts)), H


if __name__ == "__main__":
    svg, H = build()
    if M.flush():
        svg, H = build()
    p = write("16-flow-which-dme.svg", svg, OUT)
    print(p, "height", H)
