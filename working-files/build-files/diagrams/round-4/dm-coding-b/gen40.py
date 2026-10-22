"""Figure 40 (portrait), placeholder proposed-ews-recovery: what to do when the engine won't start after EWS work.
Data: WIRING-AND-CODING fragment 0500 (Session 3: the after-delete checks, the sync, the fault-type table, the donor EWS
and the "If it won't start after EWS work" list) and 0650 (Won't start, questions 2, 4 and 5). Procedures only.

Layout: questions span the width; each "no" drops into an indented exit box below it, and "yes" runs down a spine
at the left edge to the next question."""
import sys
sys.dont_write_bytecode = True
import flowkit
from flowkit import *  # noqa: F401,F403

flowkit.LINE_H["t"] = 15.0
flowkit.LINE_H["t-sm"] = 14.0

W = 400
NAME = "40-flow-ews-recovery.svg"
NB = " "
PB = 5.0
X0, X1 = 8, 392
SPX = 22                 # the "yes" spine
EXX = 52                 # exits are indented to clear the spine and its label
NOX = 140                # the "no" arrow into an exit
DROP = 22                # question bottom -> exit top
GAP = 24                 # exit bottom -> next item (the spine runs past the exit)

ARIA = ("Flowchart: what to do when the engine won't start after EWS work. Question 1, clutch down and key to start: "
        "does the starter crank? If not, the cause is on the EWS side, and a delete in the DME changes none of it. In "
        "EWS3.prg, STATUS_LESEN, the key should be sending and not barred, the key-check bits STAT_SCHLUESSEL_NIO_ID, "
        "STAT_SCHLUESSEL_NIO_PW and STAT_SCHLUESSEL_NIO_WC (ID, password and rolling code not OK) should read 0, and with "
        "the clutch down STAT_ANLASSER_AUS_P_N should read 0; the EWS coding keeps PARK/NEUTRAL_EINGANG at aktiv. Then "
        "check the battery, the clutch input at EWS pin 8 and the starter feed (Won't start, question 2), and never "
        "jumper EWS pins. Question 2, it cranks, perhaps firing once or twice: is fault 130 (0x82) or 66 (0x42) stored, or does STAT_EWS3_FREIGABE "
        "read 0? If not, or if only a leftover 130 remains after a delete the vendor has confirmed, the immobilizer "
        "isn't what stops the engine: go on with Won't start, question 5. If so, read the fault's type and act on it. "
        "Start value empty (Startwert leer), a virgin DME that hasn't received the code table: run the sync. Rolling "
        "code lost (Wechselcode verloren), an ordinary loss of sync: re-run the alignment, which BMW allows any number "
        "of times. Manipulation, the DME married to another EWS: delete, virginize, or use the donor EWS. Fault 66, the "
        "EWS interface, meaning the EWS-to-DME line or a module unplugged with the key on: check the wire in X60004 pin "
        "33, the EWS data line, and re-run the alignment. After a delete, re-read the DME or ask the vendor to confirm "
        "the delete took. Question 3: released, with 130 gone and STAT_EWS3_FREIGABE showing the release? If not, fit "
        "the donor's EWS and key and re-align, or send the DME away for a delete; if so, key off for at least 10 "
        "seconds, then start. A panel lists the alignment in Tool32, with the charger on and the ignition at position "
        "2: WECHSELCODE_SYNC_DME in EWS3.prg, then EWS3_INITIALISIEREN with 0x01 in the Arguments box, EWS3_SYNC and "
        "EWS3_GET_STATUS in MSS54DS0.PRG, the first three returning OKAY, then FS_LESEN with 130 gone and STAT_EWS3_FREIGABE "
        "showing the release, and the key off for 10 seconds. It worked once, on one owner's CSL-clone MSS54; no "
        "Touring build has confirmed it.")


def q_blocks(num, text, sub=None):
    out = [Block("t", [("t-b", num + NB + NB), ("", text)])]
    if sub:
        out.append(Block("t-sm", sub, gap_before=2))
    return out


def question(parts, y, blocks):
    s, h = box(X0, y, X1 - X0, blocks, cls="shape", rx=18, pad_x=16, pad_bottom=PB, min_h=36, valign="middle")
    parts.append(s)
    return y + h


def exit_below(parts, qb, blocks, cls, label="no"):
    """The question's 'no': an arrow from its bottom into an indented box. Returns the box's bottom."""
    top = qb + DROP
    parts.append(arrow(f"M{NOX},{fmt(qb)} V{fmt(top - 1)}"))
    parts.append(text_el("t-sm t-b", NOX + 7, qb + 14.5, label))
    s, h = box(EXX, top, X1 - EXX, blocks, cls=cls, rx=4, pad_bottom=PB)
    parts.append(s)
    return top + h


def spine(parts, y0, y1, label=None):
    """The 'yes' path down the left edge; its label sits just under the question it leaves."""
    parts.append(arrow(f"M{SPX},{fmt(y0)} V{fmt(y1 - 1)}"))
    if label:
        parts.append(text_el("t-sm t-b", SPX + 7, y0 + 14.5, label) if isinstance(label, str)
                     else text_el("t-sm", SPX + 7, y0 + 14.5, label))


def key(parts, y):
    items = [("shape", 6, "Question"), ("crit-s", 1.5, "Fix, then retry"), ("panel", 1.5, "Elsewhere"),
             ("new", 1.5, "Released")]
    x = X0
    for cls, rx, label in items:
        parts.append(f'<rect class="{cls}" x="{fmt(x)}" y="{fmt(y)}" width="20" height="12" rx="{fmt(rx)}" '
                     f'stroke-width="1.2"/>')
        parts.append(text_el("t-sm", x + 26, y + 10.5, label))
        x += 26 + line_width("t-sm", label) + 16
    return x - 16


def build():
    parts = []
    key(parts, 6)
    y = 28

    # 1: does it crank?
    q1b = question(parts, y, q_blocks("1", "Clutch down, key to start: does the starter crank?"))
    e1 = [Block("t-sm", [("t-b crit-t", "No crank: the EWS side."), ("", " A delete in the DME changes none of it.")]),
          Block("t-sm", "EWS3.prg → STATUS_LESEN: the key sending and not barred; STAT_SCHLUESSEL_NIO_ID, "
                        "STAT_SCHLUESSEL_NIO_PW and STAT_SCHLUESSEL_NIO_WC (ID, password, rolling code not OK) at 0; "
                        "with the clutch down, STAT_ANLASSER_AUS_P_N at 0.", gap_before=4),
          Block("t-sm", f"EWS coding: PARK/NEUTRAL_EINGANG{NB}={NB}aktiv.", gap_before=4),
          Block("t-sm", "Then the battery, the clutch input at EWS pin 8 and the starter feed (Won't start, "
                        "question 2).", gap_before=4),
          Block("t-sm", [("t-b crit-t", "Never jumper EWS pins.")], gap_before=4)]
    e1b = exit_below(parts, q1b, e1, "crit-s")
    y = e1b + GAP
    spine(parts, q1b, y, "yes")

    # 2: is 130 or 66 stored?
    q2b = question(parts, y, q_blocks("2", "It cranks, perhaps firing once or twice: is fault 130 (0x82) or 66 "
                                           "(0x42) stored, or does STAT_EWS3_FREIGABE read 0?",
                                      "MSS54DS0.PRG → FS_LESEN and STATUS_DIGITAL"))
    e2 = [Block("t-sm", [("t-b", "No, or only a leftover 130 (0x82) after a delete the vendor has confirmed:"),
                         ("", " the immobilizer isn't what stops the engine. Go on with Won't start, question 5.")])]
    e2b = exit_below(parts, q2b, e2, "panel")
    y = e2b + GAP + 14
    spine(parts, q2b, y, "yes")
    parts.append(text_el("t-sm t-b", SPX + 12, y - 6, "Read the fault's type, and do what it says:"))

    # The fault's type, and what to do
    LX0, LX1, RX0, RX1 = X0, 184, 204, X1
    rows = [
        ([("t-b", "130 (0x82), \"Startwert leer\""), ("", " (start value empty): a virgin DME that hasn't received the "
                                                         "code table")],
         "Run the sync (panel below)."),
        ([("t-b", "130 (0x82), \"Wechselcode verloren\""), ("", " (rolling code lost): an ordinary loss of sync")],
         "Re-run the alignment (panel below); BMW allows it any number of times."),
        ([("t-b", "130 (0x82), \"Manipulation\":"), ("", " the DME is married to another EWS")],
         "Delete, virginize, or use the donor EWS (under question 3)."),
        ([("t-b", "66 (0x42), EWS interface:"), ("", " the EWS–DME line, or the key was on with a module unplugged")],
         "Check the wire in X60004 pin 33, the EWS data line; re-run the alignment."),
    ]
    for left, right in rows:
        lb = [Block("t-sm", left)]
        rb = [Block("t-sm", right)]
        lh, _ = measure_box(LX1 - LX0, lb, pad_bottom=PB)
        rh, _ = measure_box(RX1 - RX0, rb, pad_bottom=PB)
        h = max(lh, rh)
        s, _ = box(LX0, y, LX1 - LX0, lb, cls="shape", rx=4, min_h=h, valign="middle", pad_bottom=PB)
        parts.append(s)
        s, _ = box(RX0, y, RX1 - RX0, rb, cls="crit-s", rx=4, min_h=h, valign="middle", pad_bottom=PB)
        parts.append(s)
        parts.append(arrow(f"M{LX1},{fmt(y + h / 2)} H{RX0 - 1}"))
        y += h + 6
    note = [Block("t-sm", [("t-b", "After a delete:"), ("", " re-read the DME, or ask the vendor, to confirm the delete "
                                                            "took. With a virginized DME, run the alignment again.")])]
    s, nh = box(X0, y, X1 - X0, note, cls="warn-f", rx=4, pad_bottom=PB)
    parts.append(s)
    nb = y + nh

    # 3: released?
    y = nb + 18
    spine(parts, nb, y)
    q3b = question(parts, y, q_blocks("3", "Released: 130 (0x82) gone, and STAT_EWS3_FREIGABE showing the release?"))
    e3 = [Block("t-sm", [("t-b crit-t", "Still not released:"), ("", " fit the donor's EWS and key and re-align, or send "
                                                                      "the DME away for a delete.")]),
          Block("t-sm", [("t-b", "Donor EWS:"), ("", " save your own EWS's coding file first. Fit the donor's EWS with "
                                                    "its DME, and put the donor key's transponder near the ring antenna. "
                                                    "Code it to match your file "
                                                    f"(PARK/NEUTRAL_EINGANG{NB}={NB}aktiv), re-align it, and check "
                                                    "STATUS_LESEN.")], gap_before=4)]
    e3b = exit_below(parts, q3b, e3, "crit-s")
    y = e3b + GAP
    spine(parts, q3b, y, "yes")
    done = [Block("t-sm", [("t-b", "Released:"), ("", " key off for at least 10 seconds, then start.")])]
    s, dh = box(X0, y, X1 - X0, done, cls="new", rx=4, pad_bottom=PB)
    parts.append(s)
    y += dh + 14

    # The alignment (sync) in Tool32
    sync = [Block("t-sm", [("t-b", "The sync, or alignment, in Tool32:"),
                           ("", " charger on, ignition at position 2, engine off. Jobs 1 to 3 should each "
                                "return OKAY.")]),
            Block("t-sm", [("t-b", "1"), ("", " EWS3.prg → WECHSELCODE_SYNC_DME")], gap_before=4),
            Block("t-sm", [("t-b", "2"), ("", " MSS54DS0.PRG → EWS3_INITIALISIEREN, with 0x01 in the Arguments box")]),
            Block("t-sm", [("t-b", "3"), ("", " EWS3_SYNC")]),
            Block("t-sm", [("t-b", "4"), ("", " EWS3_GET_STATUS: the failed Touring showed EWS3_STATUS = Invalid and "
                                              "EWS3_STATUS_WERT = 3")]),
            Block("t-sm", [("t-b", "5"), ("", " FS_LESEN: 130 (0x82) gone; STATUS_DIGITAL → STAT_EWS3_FREIGABE shows "
                                              "the release")]),
            Block("t-sm", [("t-b", "6"), ("", " Key off for at least 10 seconds, then start")]),
            Block("t-sm", "It worked once, on one owner's CSL-clone MSS54. No Touring build has confirmed it.",
                  gap_before=4)]
    s, sh = box(X0, y, X1 - X0, sync, cls="panel", rx=6, pad_bottom=PB)
    parts.append(s)
    H = int(round(y + sh + 8))
    return svg_doc(W, H, ARIA, "\n".join(parts)), H


if __name__ == "__main__":
    svg, H = build()
    if M.flush():
        svg, H = build()
    p = write(NAME, svg, DIAGRAMS)
    print(p, "height", H)
