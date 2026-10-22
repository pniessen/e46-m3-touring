"""Figure 39 (portrait), placeholder proposed-dsc-coding-path: Session 5, DSC coding and VIN.
Data: WIRING-AND-CODING fragment 0520 (Session 5: before you start, Option A steps 1-4, the three compensation
routines with their conditions and checks, what the C05 unit offers, wheels and tires, Option B steps 1-7, Expect,
and the M3 unit that never clears 5EF1), with 0670 (the DSC lamp row) and the coordinator's ALSZ rule.

Layout: two lanes, A (your MK60, grey) and B (the M3's, blue), merge into the shared initialisation; then the
question with its "no" exit indented below and "yes" down a spine at the left edge, as in figure 40."""
import sys
sys.dont_write_bytecode = True
import flowkit
from flowkit import *  # noqa: F401,F403

flowkit.LINE_H["t"] = 15.0
flowkit.LINE_H["t-sm"] = 14.0

W = 400
NAME = "39-flow-dsc-coding.svg"
NB = " "
EN = "–"
PB = 5.0
X0, X1 = 8, 392
AX0, AX1 = 8, 195          # lane A
BX0, BX1 = 205, 392        # lane B
IN = 6                     # inset of the boxes inside a lane
SPX = 22                   # the "yes" spine at the bottom
EXX = 52
NOX = 140

ARIA = ("Flowchart of Session 5, DSC coding and VIN. Before you start, the cluster carries your VIN (Session 4), the "
        "charger is on, and your DSC unit's part number and coding index are saved (Session 1). Option A, recommended: "
        "your Touring's own MK60, left coded as it is, a 325i Touring's, with the M54 engine, 325i brakes and rack and an "
        "open differential. A panel shows what one non-M unit offers, a 2002 318i's at coding index C05: no M3 body "
        "type (coupe_m) and no M3 rack curve (wert_05, only wert_10 and wert_02), but the M3's brake-pressure models, "
        "front typ_0 and rear typ_2; no MK60 has a tire-size code, so with the flat-tire warning on, set the pressures "
        "after fitting the M3 wheels and run RPA_RESET. Still set for the Touring's quicker rack, your unit may step "
        "in early, which is our inference. Option B, the M3's MK60, from an M3 built from 09/2002: 1, write your VIN "
        "(PA-Soft Write FGSTNR with the 14 characters after WBA, or Tool32 IDENT_VIN_SCHREIBEN, read back with "
        "IDENT_VIN); 2, set up a session-only vehicle order read from ALSZ, the light module, with the production date "
        "#0902 or later and the donor's type code, so it says S54B32, and no FA_WRITE; 3, code only the MK60 with "
        "SG_CODIEREN, never Process Car or Code Car; 4, if NCS doesn't list the MK60 or says Codierindex nicht "
        "zulaessig, the date is too early or the type key isn't the donor's M3 one, so fix both and retry; 5, check the values, set the rack curve "
        "and brake models for your parts in FSW_PSW.MAN and write it, leaving the body type at coupe_m; 6, save the "
        "final coding file and trace, and never write a blank coding file or run Code Car on it again. Both options "
        "then initialise in INPA (A steps 1 to 4, B step 7): read the DSC fault memory, where 5E1F (5EF1 in some "
        "tools), VIN not initialized, is expected after a cluster change; run the three compensation routines with Shift+F4 in this "
        "order: 1, steering angle and VIN, F1, LENKWINKEL_DSC_ABGLEICHEN, with the wheel dead straight and the car "
        "level, a fault being flagged more than 30 degrees off center, checked by 0 degrees in INPA's status page or "
        "STAT_LENKWINKEL_WERT about 0; 2, pressure sensors, DRUCKSENSOR_DSC_ABGLEICHEN, foot off the brake, checked "
        "in STATUS_SENSOREN by both pressures near 0 bar with the pedal released and never over 5 bar with the "
        "brake-light switch off; 3, lateral acceleration, QUERBESCHLEUNIGUNG_DSC_ABGLEICHEN, car level and stationary, "
        "checked by lateral acceleration near 0 g. With option A only the first is strictly due; option B needs all "
        "three. Then clear and re-read the faults in every module. If 5E1F (5EF1 in some tools) is gone, expect the DSC and "
        "yellow BRAKE lamps out and about 0 degrees with the wheel straight, provisional until Session 7 after the "
        "alignment. If not: with option A, the cluster must carry your VIN; with option B, redo steps 1 to 7 in order, "
        "and if the M3 unit still won't initialise, refit your Touring's own MK60, the documented cure, and follow "
        "option A.")


def key(parts, y):
    items = [("keep", 1.5, "Your Touring's MK60"), ("donor", 1.5, "The M3's MK60"), ("crit-s", 1.5, "If it fails")]
    x = X0
    for cls, rx, label in items:
        parts.append(f'<rect class="{cls}" x="{fmt(x)}" y="{fmt(y)}" width="20" height="12" rx="{fmt(rx)}" '
                     f'stroke-width="1.2"/>')
        parts.append(text_el("t-sm", x + 26, y + 10.5, label))
        x += 26 + line_width("t-sm", label) + 16
    return x - 16


def lane(x0, x1, y, title, sub, items, arrows=True):
    """A lane: a tinted container with its title, then white boxes, joined by short arrows when they are steps.
    items = [(blocks, cls)]. Returns (svg parts for the inside, height of the content)."""
    out = []
    t = [Block("t", [("t-b", title)]), Block("t-sm", [("t-b", sub)], gap_before=0)]
    tsvg, th, _ = layout_blocks(t, x0, y, x1 - x0, pad_x=10, pad_top=6, pad_bottom=2)
    out.append(tsvg)
    yy = y + th + 4
    cx = (x0 + x1) / 2
    for i, (blocks, cls) in enumerate(items):
        if i and arrows:
            out.append(arrow(f"M{fmt(cx)},{fmt(yy)} V{fmt(yy + 9)}"))
            yy += 10
        elif i:
            yy += 6
        s, h = box(x0 + IN, yy, x1 - x0 - 2 * IN, blocks, cls=cls, rx=4, pad_x=8, pad_bottom=PB)
        out.append(s)
        yy += h
    return out, yy - y


def build():
    parts = []
    key(parts, 6)
    y = 28

    before = [Block("t-sm", [("t-b", "Before you start:"), ("", " the cluster carries your VIN (Session 4); the charger is "
                                                              "on; your DSC unit's part number and coding index are "
                                                              "saved (Session 1).")])]
    s, h = box(X0, y, X1 - X0, before, cls="panel", rx=4, pad_bottom=PB)
    parts.append(s)
    y += h + 12
    s, qh = box(X0, y, X1 - X0, [Block("t", "Which MK60 is in the car?")], cls="shape", rx=18, pad_x=16,
                pad_bottom=PB, min_h=34, valign="middle")
    parts.append(s)
    qb = y + qh
    ly = qb + 22
    acx, bcx = (AX0 + AX1) / 2, (BX0 + BX1) / 2
    parts.append(arrow(f"M{fmt(acx)},{fmt(qb)} V{fmt(ly - 1)}"))
    parts.append(text_el("t-sm t-b", acx + 7, qb + 14.5, "yours"))
    parts.append(arrow(f"M{fmt(bcx)},{fmt(qb)} V{fmt(ly - 1)}"))
    parts.append(text_el("t-sm t-b", bcx + 7, qb + 14.5, "the M3's"))

    # Lane A: your MK60, and what a non-M unit offers
    a_items = [
        ([Block("t-sm", [("t-b", "Leave it coded as it is:"), ("", " a 325i Touring's, with the M54 engine, 325i brakes "
                                                                    "and rack, open differential. It's a safety system, "
                                                                    "and nobody has documented hand-set values in a "
                                                                    "Touring with M3 brakes and rack.")])], "shape"),
        ([Block("t-sm", [("t-b", "What a non-M unit offers")]),
          Block("t-sm", "read from a 2002 318i's unit, coding index C05; check your own unit's coding file in "
                        "NCS Dummy"),
          Block("t-sm", [("t-b", "No"), ("", " M3 body type: no coupe_m")], gap_before=5),
          Block("t-sm", [("t-b", "No"), ("", " M3 rack curve: wert_10 or wert_02, not wert_05")], gap_before=3),
          Block("t-sm", [("t-b", "Yes:"), ("", " the M3's brake-pressure models, front typ_0, rear typ_2")],
                gap_before=3),
          Block("t-sm", [("t-b", "No"), ("", " tire-size code on any MK60. With its flat-tire warning on, set the "
                                             "pressures on the M3 wheels, then RPA_RESET (Tool32)")], gap_before=3)],
         "shape"),
        ([Block("t-sm", "Still set for the Touring's quicker rack, it may step in early: watch for it on the "
                        "shakedown (our inference).")], "shape"),
    ]

    # Lane B: the M3's MK60, steps 1 to 6 as the text numbers them
    b_items = [
        ([Block("t-sm", [("t-b", "1" + NB + NB + "Write your VIN."), ("", " PA-Soft → Write FGSTNR, the 14 characters "
                                                                        "after \"WBA\"; or Tool32 IDENT_VIN_SCHREIBEN, "
                                                                        "read back with IDENT_VIN.")])], "shape"),
        ([Block("t-sm", [("t-b", "2" + NB + NB + "A session order from ALSZ."),
                         ("", " Enter FA: date #0902 or later, not earlier than the unit; the donor's type code, so it "
                              "says S54B32. No FA_WRITE.")])], "shape"),
        ([Block("t-sm", [("t-b", "3" + NB + NB + "Code the MK60 only."),
                         ("", " Process ECU → MK60 → SG_CODIEREN. Never Process Car or Code Car.")]),
          Block("t-sm", [("t-b crit-t", "4" + NB + NB + "Not listed, or \"Codierindex … nicht zulässig\"?"),
                         ("", " The date is too early, or the type key isn't the donor's M3 one (BL93, BR93): fix "
                              "both in 2 and retry.")], gap_before=4)], "shape"),
        ([Block("t-sm", [("t-b", "5" + NB + NB + "Check the values."),
                         ("", " CODIERDATEN_LESEN; set the rack curve and brake models for your parts in FSW_PSW.MAN; "
                              "SG_CODIEREN. Body type stays coupe_m.")])], "shape"),
        ([Block("t-sm", [("t-b", "6" + NB + NB + "Keep the final coding."),
                         ("", " Re-read: only your lines differ. Save the trace and FSW_PSW.MAN. Never a blank coding "
                              "file or Code Car again.")])], "shape"),
    ]

    a_in, a_h = lane(AX0, AX1, ly, "A" + NB + NB + "Your Touring's MK60", "recommended", a_items, arrows=False)
    b_in, b_h = lane(BX0, BX1, ly, "B" + NB + NB + "The M3's MK60", "an M3 from 09/2002", b_items)
    lh = max(a_h, b_h) + IN
    parts.append(f'<rect class="keep" x="{AX0}" y="{fmt(ly)}" width="{AX1 - AX0}" height="{fmt(lh)}" rx="6" '
                 f'stroke-width="1.5"/>')
    parts.append(f'<rect class="donor" x="{BX0}" y="{fmt(ly)}" width="{BX1 - BX0}" height="{fmt(lh)}" rx="6" '
                 f'stroke-width="1.5"/>')
    parts += a_in + b_in
    lb = ly + lh

    # Merge into the shared initialisation (A: steps 1-4; B: step 7)
    y = lb + 26
    parts.append(arrow(f"M{fmt(acx)},{fmt(lb)} V{fmt(y - 1)}"))
    parts.append(text_el("t-sm t-b", acx + 7, lb + 16, "A: steps 1–4"))
    parts.append(arrow(f"M{fmt(bcx)},{fmt(lb)} V{fmt(y - 1)}"))
    parts.append(text_el("t-sm t-b", bcx + 7, lb + 16, "B: step 7"))

    PADX = 10
    sections = []   # (blocks, extra right-aligned label or None)
    sections.append(([Block("t-sm", [("t-b", "INPA → E46 (F3) → Chassis → DSC MK60."),
                                      ("", " First read the fault memory, F4 → F1: after a cluster change, expect "
                                           "5E1F (5EF1 in some tools), \"VIN not initialized\".")])], None))
    sections.append(([Block("t-sm", [("t-b", "Then the three compensation routines, in this order:"),
                                      ("", " Shift+F4. In Tool32, DSC_MK60.PRG and the job named.")])], None))
    routines = [
        ("1" + NB + NB + "Steering angle and VIN", "INPA F1", "LENKWINKEL_DSC_ABGLEICHEN",
         [("t-b", "When:"), ("", " wheel dead straight, car level; a fault is flagged if it's more than 30° off "
                                 "center.")],
         [("t-b", "Check:"), ("", " 0° in INPA status (F5) → analog → DSC sensor (F2), or STATUS_CAN_LWS_1_LESEN → "
                                  "STAT_LENKWINKEL_WERT about 0.")]),
        ("2" + NB + NB + "Pressure sensors", "\"Pressure Sensors\"", "DRUCKSENSOR_DSC_ABGLEICHEN",
         [("t-b", "When:"), ("", " foot off the brake.")],
         [("t-b", "Check:"), ("", " STATUS_SENSOREN: both pressures near 0 bar with the pedal released. BMW: never "
                                  "over 5 bar while the brake-light switch is off.")]),
        ("3" + NB + NB + "Lateral acceleration", "\"Lateral Acceleration Sensor\"", "QUERBESCHLEUNIGUNG_DSC_ABGLEICHEN",
         [("t-b", "When:"), ("", " car level and stationary.")],
         [("t-b", "Check:"), ("", " STATUS_SENSOREN: lateral acceleration near 0 g (our check).")]),
    ]
    for name, inpa, job, when, check in routines:
        sections.append(([Block("t-sm", [("t-b", name)]), Block("t-sm", [("", job)]), Block("t-sm", when),
                          Block("t-sm", check)], inpa))
    sections.append(([Block("t-sm", [("t-b", "Last, clear and read again:"),
                                      ("", " F4 → F2, then F1: no faults. Clear the faults in every module, cycle the "
                                           "ignition, read again.")])], None))
    sections.append(([Block("t-sm", [("t-b", "A:"), ("", " only the first routine is strictly due, since your unit and "
                                                         "its sensors stay; all three take a minute. "),
                                      ("t-b", "B:"), ("", " all three, as the unit is new to the car.")])], None))
    body, yy = [], y
    for i, (blocks, right) in enumerate(sections):
        if i:
            body.append(line(f"M{X0 + 1},{fmt(yy)} H{X1 - 1}", cls="ln-faint"))
        tsvg, th, _ = layout_blocks(blocks, X0, yy, X1 - X0, pad_x=PADX, pad_top=4, pad_bottom=4)
        body.append(tsvg)
        if right:
            body.append(text_el("t-sm", X1 - PADX, yy + 4 + 11.5 * 0.78, right, "end"))
        yy += th
    yy += 2
    parts.append(f'<rect class="shape" x="{X0}" y="{fmt(y)}" width="{X1 - X0}" height="{fmt(yy - y)}" rx="4" '
                 f'stroke-width="1.5"/>')
    parts += body
    y = yy + 12
    parts.append(arrow(f"M200,{fmt(yy)} V{fmt(y - 1)}"))

    # Pass or fail
    s, qh = box(X0, y, X1 - X0, [Block("t", "5E1F (or 5EF1) gone?")], cls="shape", rx=18, pad_x=16, pad_bottom=PB,
                min_h=34, valign="middle")
    parts.append(s)
    qb = y + qh
    fail = [Block("t-sm", [("t-b crit-t", "Still \"VIN not initialized\"."), ("", " A: the cluster must carry your VIN "
                                                                                "(Session 4); then initialise again.")]),
            Block("t-sm", [("t-b", "B:"), ("", " do 1–7 in order: the VIN, a late session order with an M3 type key, "
                                               "set up from ALSZ, the coding, then Shift+F4 → F1. The failed Touring had "
                                               "only a blank coding file and a PA-Soft reset.")], gap_before=4),
            Block("t-sm", [("t-b crit-t", "Still failing:"), ("", " refit your Touring's own MK60, the cure in that "
                                                                  "Touring, and follow A.")], gap_before=4)]
    top = qb + 22
    parts.append(arrow(f"M{NOX},{fmt(qb)} V{fmt(top - 1)}"))
    parts.append(text_el("t-sm t-b", NOX + 7, qb + 14.5, "no"))
    s, fh2 = box(EXX, top, X1 - EXX, fail, cls="crit-s", rx=4, pad_bottom=PB)
    parts.append(s)
    y = top + fh2 + 24
    parts.append(arrow(f"M{SPX},{fmt(qb)} V{fmt(y - 1)}"))
    parts.append(text_el("t-sm t-b", SPX + 7, qb + 14.5, "yes"))
    ok = [Block("t-sm", [("t-b", "Expect:"), ("", " the DSC and yellow BRAKE lamps out; no 5EF1 or 5E1F; about 0° with "
                                                  "the wheel straight, provisional until Session 7, after the "
                                                  "alignment.")])]
    s, h = box(X0, y, X1 - X0, ok, cls="new", rx=4, pad_bottom=PB)
    parts.append(s)
    H = int(round(y + h + 8))
    return svg_doc(W, H, ARIA, "\n".join(parts)), H


if __name__ == "__main__":
    svg, H = build()
    if M.flush():
        svg, H = build()
    p = write(NAME, svg, DIAGRAMS)
    print(p, "height", H)
