"""Figure: starts then dies, and fault 1 (0x01): expected or real? (second no-start figure, flow-no-start-2).
From the manual's "Won't start" (the "Starts, then dies" list and the fault-number note under "Troubleshooting")
and "Faults that look like pump faults"."""
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
PB = 5.0

ARIA = ("Two charts for the no-start tree. Left, starts then dies: that isn't the immobilizer's signature, because BMW "
        "describes a mismatch as crank-no-start and a deleted DME ignores the code, so look at the EWS only if 130 (0x82) "
        "or 66 (0x42) is stored, and after a confirmed delete not for a leftover 130 on its own. If it dies within about 3 seconds with the EML lamp on and won't restart, it's a throttle "
        "fault shutdown: read the faults 118 to 121 (0x76 to 0x79) for the throttle sensors, 60 and 61 (0x3C, 0x3D) for the pedal and 228 to 230 (0xE4 to "
        "0xE6) for throttle control. If it dies when the prime would end, the pump isn't being held: the DME needs the "
        "engine-speed signal to keep K96 on, so check STAT_EKP_EIN with the engine running. If it dies at idle with no EML "
        "lamp: the idle actuator, leaks at the idle-air pipe, the adaptation, fuel pressure. If it runs only with the pump "
        "fuse pulled, then floods: an unseated terminal, so tug-test. Right, fault numbers: INPA prints decimal and the job "
        "documentation hex; 130 (0x82) is the immobilizer fault and 1 (0x01) the pump-relay fault that US software stores "
        "when K96 replaces the pump module. The harmless and the real fault 1 carry the same number, so tell them apart by "
        "what the car does: one prime with K96 clicking, 5.0 plus or minus 0.2 bar (BMW), the engine starting and running and STAT_MIL_EIN at 0 "
        "means the expected fault, so record it and do nothing; no prime, no pressure and K96 silent means a real "
        "pump-circuit fault; cranks without starting with all six injectors disabled is usually not the pump: in the 2002 "
        "325iT case it followed an immobilizer problem, "
        "so read 130 (0x82), 66 (0x42) and STAT_EWS3_FREIGABE first.")

LX0, LX1 = 8, 392      # left chart
RX0, RX1 = 408, 792    # right chart
TRUNK_IN = 22          # trunk line inset from the chart's left edge
BR = 18                # branch length from trunk to outcome box


def fanout(x0, x1, y, title_blocks, outcomes, gap=8):
    """A question box, then a trunk down its left side with a branch into each outcome box.
    outcomes: list of (cls, blocks). Returns (svg, bottom)."""
    out = []
    qh, _ = measure_box(x1 - x0, title_blocks, pad_x=14, pad_bottom=PB)
    s, qh = box(x0, y, x1 - x0, title_blocks, cls="shape", rx=18, pad_x=14, min_h=max(qh, 34), valign="middle",
                pad_bottom=PB)
    out.append(s)
    tx = x0 + TRUNK_IN
    bx0 = tx + BR
    yy = y + qh + 14
    mids = []
    for cls, blocks in outcomes:
        s, h = box(bx0, yy, x1 - bx0, blocks, cls=cls, rx=4, pad_bottom=PB)
        out.append(s)
        mids.append(yy + h / 2)
        yy += h + gap
    out.append(line(f"M{tx},{fmt(y + qh)} V{fmt(mids[-1])}"))
    for i, m in enumerate(mids):
        out.append(arrow(f"M{tx},{fmt(m)} H{bx0 - 1}"))
        if i < len(mids) - 1:
            out.append(dot(tx, m))
    return "\n".join(out), yy - gap


def lead(cond, text, cond_cls="t-b crit-t"):
    return [Block("t", [(cond_cls, cond), ("", " " + text)])]


def build():
    parts = []
    k, kx = key_row(8, 7, ["question", "go", "stop", "note"],
                    labels={"go": "Expected: record it", "note": "Note"})
    parts.append(k)

    # Left: starts, then dies
    y = 30
    parts.append(text_el("t-h", LX0, y + 12, "STARTS, THEN DIES"))
    y += 22
    s, nh = box(LX0, y, LX1 - LX0, [Block("t", [("t-b", "Not the immobilizer's signature:"),
                                                ("", " BMW describes a mismatch as crank-no-start, and a deleted DME "
                                                     "ignores the code. Look at the EWS only if 130 (0x82) or 66 (0x42) "
                                                     "is stored, and after a confirmed delete not for a leftover 130 on "
                                                     "its own.")])], cls="panel", rx=4, pad_bottom=PB)
    parts.append(s)
    y += nh + 14
    parts.append(arrow(f"M{LX0 + 60},{fmt(y - 14)} V{fmt(y - 1)}"))
    s, lb = fanout(LX0, LX1, y, [Block("t", "How does it die?")], [
        ("crit-s", lead("Within about 3 seconds, EML lamp on, won't restart:",
                        f"a throttle fault shutdown. Read the faults: 118{EN}121 (0x76{EN}0x79) throttle sensors, 60 and 61 "
                        f"(0x3C, 0x3D) pedal, 228{EN}230 (0xE4{EN}0xE6) throttle control. MotoIQ worked through throttle sensor 1, the pedal, throttle "
                        "sensor 2, the synchronization and the actuator, suspecting low charging voltage too.")),
        ("crit-s", lead("When the prime would end:",
                        "the pump isn't being held. The DME needs the engine-speed signal to keep K96 on; check "
                        "STAT_EKP_EIN with the engine running.")),
        ("crit-s", lead("At idle, no EML lamp:",
                        "the idle actuator, leaks at the idle-air pipe, the adaptation, fuel pressure.")),
        ("crit-s", lead("Runs only with the pump fuse pulled, then floods:",
                        "an unseated terminal (in an E36 S54 swap, a ground at X60003 pin 25). Tug-test.")),
    ])
    parts.append(s)

    # Right: fault numbers, and fault 1 expected or real
    y = 30
    parts.append(text_el("t-h", RX0, y + 12, "FAULT 1: EXPECTED OR REAL?"))
    y += 22
    s, nh = box(RX0, y, RX1 - RX0, [Block("t", [("t-b", "Fault numbers:"),
                                                ("", " INPA prints decimal, the job documentation hex. 130 (0x82), "
                                                     "\"EWS-Signalmanipulation\", is the immobilizer fault; 1 (0x01), "
                                                     "\"Relais Kraftstoffpumpe\", the pump fault US software stores when "
                                                     "K96 replaces the pump module.")])], cls="panel", rx=4, pad_bottom=PB)
    parts.append(s)
    y += nh + 14
    parts.append(arrow(f"M{RX0 + 60},{fmt(y - 14)} V{fmt(y - 1)}"))
    s, rb = fanout(RX0, RX1, y, [Block("t", "Fault 1 stored: what does the car do?")], [
        ("new", lead("One prime at key-on (STAT_EKP_EIN = 1, K96 clicks), 5.0 \u00b1 0.2 bar (BMW), it starts and runs, "
                     "STAT_MIL_EIN = 0:",
                     "the expected fault. US software misses its pump module. Record it; nothing to do.", "t-b")),
        ("crit-s", lead("No prime, no pressure, K96 silent:",
                        "a real pump-circuit fault. \"Checks on the pump circuit\" 1–3; fuses F54 and F3; swap K96 "
                        "with K19.")),
        ("crit-s", lead("Cranks, won't start; all six injectors disabled:",
                        "usually not the pump; in the 2002 325iT case it followed an immobilizer problem. Read 130 (0x82), "
                        "66 (0x42) and STAT_EWS3_FREIGABE first (Session 3).")),
    ])
    parts.append(s)
    H = int(round(max(lb, rb) + 8))
    parts.insert(1, line(f"M400,30 V{H - 8}", cls="ln-faint"))
    return svg_doc(W, H, ARIA, "\n".join(parts)), H


if __name__ == "__main__":
    svg, H = build()
    if M.flush():
        svg, H = build()
    p = write("25-flow-no-start-2.svg", svg, OUT)
    print(p, "height", H)
