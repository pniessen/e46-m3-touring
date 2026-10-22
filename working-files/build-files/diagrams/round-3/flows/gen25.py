"""Figure: the no-start tree (placeholder flow-no-start), from the manual's "Won't start" questions 1 to 8."""
import sys
sys.dont_write_bytecode = True
import flowkit
from flowkit import *  # noqa: F401,F403

flowkit.LINE_H["t"] = 15.0
flowkit.LINE_H["t-sm"] = 14.0

W = 800
OUT = HERE / "out"
NB = " "
EN = "–"
OHM = "Ω"
PB = 5.0

ARIA = ("The no-start tree: work down the questions in order; each one rules out a group of causes. If the engine starts "
        "and then dies, use the next figure instead: an immobilizer mismatch gives crank-no-start. 1: key on, does Tool32 "
        "IDENT or INPA reach the DME? If not, check the cable's pin 7/8 bridge and a COM port matching obd.ini, the DME "
        "relay K6300 and F29, F102, the E-box fuse carrier and X64101/X64102, the grounds, then the E-box plugs pin by pin. "
        "2: clutch fully down, key to start, does the starter crank? If not, the battery (at least about 12.4 volts at rest, "
        "generic, with the charger on), EWS3.PRG STATUS_LESEN for the key, the clutch input and the coding, and terminal 50 "
        "to the starter; never jumper EWS pins. 3: while cranking, does the DME see engine speed? If not, the crankshaft "
        "sensor, its plug and X60003 pins 8 and 21, fault 16 (0x10). 4: is fault 130 (0x82) or 66 (0x42) stored, or does "
        "STAT_EWS3_FREIGABE read 0? If so the DME isn't released: after a delete, confirm it took; with a virgin DME, the "
        "sync failed. If not, or if only a leftover 130 (0x82) is stored after a delete the vendor has confirmed, go on: "
        "a deleted DME can keep 130 stored and still start. 5: did the pump prime at key-on, and is there 5.0 plus or minus "
        "0.2 bar (BMW)? With no prime, the checks on the pump circuit: X60004 pin 10 to K96, the fuses, K96 swapped with "
        "K19, STEUERN_EKP, the E-box plugs; with a prime but low or no pressure, feed and return swapped at the "
        "filter-regulator, the regulator and its vacuum hose, the pump's delivery, old fuel. 6: injector faults 3 to 5 and "
        "31 to 33 or circuit low on all six? Then the injector relay K6327, its fuse, an X6053/X60531 mix, six equal "
        "injector resistances. 7: coil faults 23 to 25 and 50 to 52, or no spark? Then about 0.8 ohms to each coil (BMW), "
        "the X60005 pin 5 ground, the M3 coil harness, plugs and boots. 8: does STATUS_ADAPTIONSBLOCK_06 "
        "STAT_WDK_ADAPT_WERT read 0, do the throttles follow the pedal, is the idle actuator plugged in and are there no "
        "throttle (EML) faults? If not, clear the adaptations and let the throttles relearn on a cold engine, then the "
        "sensors, pedal and actuator; if all is well, the cause is mechanical, not wiring.")

QX0, QX1 = 8, 372           # questions
EX0, EX1 = 402, 792         # exits
QCX = (QX0 + QX1) / 2
GAP = 14
QPAD = 14


def q_blocks(num, text, sub=None, gap=0):
    runs = [("t-b", num + NB + NB), ("", text)] if num else [("", text)]
    out = [Block("t", runs)]
    for i, sl in enumerate([sub] if isinstance(sub, (str, tuple)) or (sub and isinstance(sub[0], tuple)) else (sub or [])):
        out.append(Block("t-sm", sl, gap_before=gap if i == 0 else 0))
    return out


def e_blocks(lead, text):
    """An exit: a bold red lead, then the checks, in one paragraph."""
    return [Block("t", [("t-b crit-t", lead), ("", " " + text)])]


ROWS = [
    # (question blocks, [(exit blocks, arrow label)], down label)
    (q_blocks("1", f"Key on: does Tool32 IDENT (or INPA) reach the{NB}DME?"),
     [(e_blocks("Link, power, grounds:",
                "the cable's pin 7/8 bridge and a COM port matching obd.ini; K6300 and F29; F102, the E-box fuse "
                "carrier and X64101/X64102; the grounds; then the E-box plugs pin by pin."), "no")], "yes"),
    (q_blocks("2", "Clutch fully down, key to start: does the starter crank?"),
     [(e_blocks("Battery and EWS:",
                f"at least about 12.4{NB}V at rest (generic), charger on; EWS3.PRG → STATUS_LESEN: key, clutch input, "
                "coding; terminal 50 to the starter. Never jumper EWS pins."), "no")], "yes"),
    (q_blocks("3", "While cranking, does the DME see engine speed?",
              "STATUS_MOTORDREHZAHL above 0, the tachometer moving"),
     [(e_blocks("Engine speed:", "the crankshaft sensor, its plug and X60003 pins 8 and 21; fault 16 (0x10)."), "no")], "yes"),
    (q_blocks("4", "Is fault 130 (0x82) or 66 (0x42) stored, or does STAT_EWS3_FREIGABE read 0?",
              "130 (0x82) is the immobilizer fault, not the pump fault 1 (0x01).", gap=2),
     [(e_blocks("The DME isn't released:",
                "after a delete, confirm it took (re-read the DME; ask the vendor); with a virgin DME, the sync failed "
                "(Session 3)."), "yes")],
     [[("t-sm t-b", "no,"), ("t-sm", " or only a leftover 130 (0x82) after a delete the vendor has confirmed: that "
                                     "alone isn't the cause. A deleted DME can keep 130 stored and still start (step 22; "
                                     "Session 2).")]]),
    (q_blocks("5", f"Did the pump prime at key-on, and is there 5.0{NB}±{NB}0.2{NB}bar (BMW)?",
              ["Listen at K96 and the tank at key-on: one prime.", "STEUERN_EKP clicks K96 and runs the pump (step 28).",
               "Fault 1 (0x01) stored? The next figure tells the", "expected one from a real pump fault."], gap=4),
     [([Block("t", [("t-b crit-t", "No prime:"), ("", " \"Checks on the pump circuit\": X60004 pin 10 to K96, the fuses, "
                                                      "K96 swapped with K19, STEUERN_EKP, the E-box plugs.")]),
        Block("t", [("t-b crit-t", "Primes, but low or no pressure:"), ("", " feed and return swapped at the "
                    "filter-regulator; the regulator and its vacuum hose; the pump's delivery; old fuel.")], gap_before=5)],
       "no")], "yes"),
    (q_blocks("6", f"Injector faults 3{EN}5 and 31{EN}33 (0x03{EN}0x05, 0x1F{EN}0x21), or \"circuit low\" on all six?"),
     [(e_blocks("Injectors:", "the injector relay K6327, its E-box fuse, an X6053/X60531 mix; six equal injector "
                              "resistances (step 12)."), "yes")], "no"),
    (q_blocks("7", f"Coil faults 23{EN}25 and 50{EN}52 (0x17{EN}0x19, 0x32{EN}0x34), or no spark?"),
     [(e_blocks("Coils:", f"about 0.8{NB}{OHM} from terminal 15 to each coil's pin (BMW, step 11); the X60005 pin 5 "
                          "ground; the M3 harness's coil harness only; plugs and boots."), "yes")], "no"),
    (q_blocks("8", "Air and throttle: STATUS_ADAPTIONSBLOCK_06 → STAT_WDK_ADAPT_WERT = 0, the throttles following "
                   "the pedal, the idle actuator "
                   "plugged in (X60003 pins 46 and 47), no throttle (EML) faults?"),
     [(e_blocks("Relearn:", "clear the adaptations and let the throttles relearn on a cold engine (Session 6). Then the "
                            "throttle sensors, pedal and actuator."), "no")], "yes"),
]


LABEL_W = EX1 - QCX - 12   # a long "down" label may run under the exits


def label_lines(down):
    if isinstance(down, str):
        return [[("t-sm t-b", down)]]
    out = []
    for runs in down:
        out += [r for r, _ in wrap("t-sm", runs, LABEL_W)]
    return out


def gap_for(down):
    n = len(label_lines(down))
    return GAP if n == 1 else 14 * n + 7


def down_label(down, top):
    return [text_el("t-sm", QCX + 7, top + 10.5 + 14 * i, runs) for i, runs in enumerate(label_lines(down))]


def build():
    parts = []
    # Entry: starts then dies?
    y = 8
    eq = q_blocks("", "Does it start, then die?")
    ptr = [Block("t", [("t-b", "Starts, then dies:"), ("", " see the next figure. An immobilizer mismatch gives "
                                                          "crank-no-start instead (question 4).")])]
    qh, _ = measure_box(QX1 - QX0, eq, pad_x=QPAD, pad_bottom=PB)
    ph, _ = measure_box(EX1 - EX0, ptr, pad_bottom=PB)
    h = max(qh, ph, 34)
    s, _ = box(QX0, y, QX1 - QX0, eq, cls="shape", rx=18, pad_x=QPAD, min_h=h, valign="middle", pad_bottom=PB)
    parts.append(s)
    s, _ = box(EX0, y, EX1 - EX0, ptr, cls="panel", rx=4, min_h=h, valign="middle", pad_bottom=PB)
    parts.append(s)
    parts.append(arrow(f"M{QX1},{fmt(y + h / 2)} H{EX0 - 1}"))
    parts.append(text_el("t-sm t-b", (QX1 + EX0) / 2, y + h / 2 - 8, "yes", "middle"))
    prev_bottom, down = y + h, "no"
    y = y + h + GAP

    for qb, exits, down_next in ROWS:
        qh, _ = measure_box(QX1 - QX0, qb, pad_x=QPAD, pad_bottom=PB)
        ehs = [measure_box(EX1 - EX0, eb, pad_bottom=PB)[0] for eb, _ in exits]
        eh_total = sum(ehs) + 6 * (len(ehs) - 1)
        h = max(qh, eh_total)
        parts.append(arrow(f"M{fmt(QCX)},{fmt(prev_bottom)} V{fmt(y - 1)}"))
        parts += down_label(down, prev_bottom)
        s, _ = box(QX0, y, QX1 - QX0, qb, cls="shape", rx=18, pad_x=QPAD, min_h=h, valign="middle", pad_bottom=PB)
        parts.append(s)
        ey = y + (h - eh_total) / 2 if len(exits) == 1 else y
        for (eb, lab), eh in zip(exits, ehs):
            hh = eh if len(exits) > 1 else h
            yy = ey if len(exits) > 1 else y
            s, _ = box(EX0, yy, EX1 - EX0, eb, cls="crit-s", rx=4, min_h=hh, valign="middle", pad_bottom=PB)
            parts.append(s)
            mid = yy + hh / 2
            parts.append(arrow(f"M{QX1},{fmt(mid)} H{EX0 - 1}"))
            if lab:
                parts.append(text_el("t-sm t-b", (QX1 + EX0) / 2, mid - 8, lab, "middle"))
            ey += eh + 6
        prev_bottom, down = y + h, down_next
        y = y + h + gap_for(down_next)

    # End: mechanical
    parts.append(arrow(f"M{fmt(QCX)},{fmt(prev_bottom)} V{fmt(y - 1)}"))
    parts.append(text_el("t-sm t-b", QCX + 7, prev_bottom + GAP / 2 + 3.5, down))
    s, he = box(QX0, y, QX1 - QX0, [Block("t", [("t-b", "Mechanical"), ("", " (timing, compression), not wiring")])],
                cls="panel", rx=4, pad_bottom=PB)
    parts.append(s)
    # Fault-number note beside the end
    k, kx = key_row(EX0 + 2, y + (he - 12) / 2, ["question", "stop", "note"],
                    labels={"stop": "Stop: fix before going on", "note": "Elsewhere"}, gap=16)
    parts.append(k)
    nh = 0
    H = int(round(y + max(he, nh) + 5))
    return svg_doc(W, H, ARIA, "\n".join(parts)), H


if __name__ == "__main__":
    svg, H = build()
    if M.flush():
        svg, H = build()
    p = write("25-flow-no-start.svg", svg, OUT)
    print(p, "height", H)
