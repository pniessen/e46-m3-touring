"""Figures: checks before first power-up (placeholder flow-power-up: steps 1-19) and the powered checks
(flow-power-up-2: steps 20-33), from the manual's "Checks before first power-up"."""
import re
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
PM = "±"

# Columns
HX0, HX1 = 8, 164          # set-up labels
DX0, DX1 = 176, 574        # gates (questions)
SX0, SX1 = 594, 792        # stop-and-fix exits
DCX = (DX0 + DX1) / 2
GAP = 15
PB = 5.0                   # bottom padding: the same as the top
DPAD = 12                  # side padding inside the gates
IFF = "or that step's \"If it fails\"."

ARIA1 = ("The checks before first power-up, part 1: the meter checks before the battery and the DME are both connected. "
         "Each stage has a gate that must pass before you go on, and a stop-and-fix exit; on a fail, fix what the exit "
         "names or that step's If it fails. In Phase 11, before you join the E-box plugs, compare both halves of X6011, "
         "X6021, X6053/X60531, X6054/X60541 and X64101/X64102: each pair the same circuit or empty on one side; if not, use "
         "the M3's X6053 and X6054 sections together and never an M3 half with a Touring half. Then join the plugs. Steps 1 "
         "to 14, battery disconnected and all five DME plugs off: every terminal locked and every cavity as the move table "
         "says; moved wires open to ground; lamp wires under about 1 ohm (generic); the oil-pressure switch near 0 ohms with "
         "the engine stopped; the brake test contact and the start interlock continuous; across the gear switch near 0 ohms "
         "in gear and open in neutral; the Sport input open with the button released and near 0 ohms pressed (BMW); the "
         "leak-test heater on pin 18 and the pump on 30; pin 10 to K96 pin 4, the M3 harness's X6021 pin 1 open to every K96 "
         "terminal, and the K96 coil about 90 ohms (generic); coils about 0.8 ohms each and all alike (BMW); six equal "
         "injector readings; temperature sensors about 2,500 ohms at 20 degrees C (generic); and the crankshaft sensor a "
         "steady reading, open to ground. Steps 15 to 18, battery connected and the DME still unplugged: battery voltage at "
         "X60001 pin 7 and K6300 terminal 30; terminal 15 at X60004 pin 26 above 9 volts at key position 2 (BMW) and 0 volts "
         "with the key off; grounds near 0 ohms with under 0.1 volt drop (generic). Step 19, battery disconnected again with "
         "the DME and every module plugged in: about 60 ohms between CAN high and low (BMW); 120 ohms, 40 ohms, 0 ohms or "
         "open each point to a different fault. Then steps 20 to 33, in the next figure.")

ARIA2 = ("The checks before first power-up, part 2: from the first key-on to the oil-priming crank. Steps 20 to 29, battery "
         "connected with the charger on, the DME plugged in, key at position 2, engine off: K6300 clicks at key-on and stays "
         "on a few seconds after key-off (BMW); INPA reaches the DME, cluster, light module, EWS and DSC and Tool32 IDENT "
         "returns OKAY; the supplies, temperatures, pedal and throttles, switch bits, EWS and outputs read as steps 21, 24 to "
         "27 and 29 say; the only faults are 1 (0x01), possibly 130 (0x82) after an EWS delete, and the DSC unit's VIN faults "
         "until Session 5; the oil-pressure, charge and check-engine lamps are lit, and the DSC, ABS and yellow BRAKE "
         "lamps stay on until Session 5; and the pump primes once, STEUERN_EKP "
         "clicks K96, and the pressure is 5.0 plus or minus 0.2 bar with under 0.5 bar lost (BMW). Fix anything else before "
         "you crank. Then Sessions 3 to 5. Steps 30 to 32, in Phase 12 with K96 and K6327 pulled and the coils unplugged: "
         "with the clutch up it doesn't crank and with the clutch down it cranks; the DME sees engine speed; and oil pressure "
         "shows and holds on the mechanical gauge while the red lamp goes out. With no oil pressure, stop. Step 33: refit "
         "K96, K6327 and the coils and run Session 6 steps 2 to 5; STATUS_ADAPTIONSBLOCK_06, STAT_WDK_ADAPT_WERT must read 0, "
         "and the clutch, brake and Sport bits respond, "
         "or repeat with the charger on and check the throttle wiring. Then the first start, Session 6 step 6.")


def head(steps, state, detail, extra=None):
    out = [Block("t-sm", steps), Block("t t-b", state, gap_before=1), Block("t", detail, gap_before=0)]
    if extra:
        out.append(Block("t-sm", extra, gap_before=4))
    return out


def gate(title, *items):
    """A gate: the question, then items as (text, step) pairs; steps sit in a right-hand column."""
    return dict(title=title, items=[it if isinstance(it, tuple) else (it, "") for it in items])


def stop(title, text):
    return [Block("t t-b crit-t", title), Block("t", text, gap_before=0)]


def gate_svg(g, x, y, w, h=None):
    """Render a gate (rounded question box). Returns (svg or None, height)."""
    inner = w - 2 * DPAD
    out, yy = [], y + 4.5 + 13 * 0.78
    for i, (runs, _) in enumerate(wrap("t t-b", g["title"], inner)):
        if i:
            yy += 15
        out.append(text_el("t t-b", x + DPAD, yy, runs))
    first = True
    for text, step in g["items"]:
        tagw = line_width("t-sm", step) + 14 if step else 0
        lines = wrap("t", text, inner - tagw)
        for i, (runs, _) in enumerate(lines):
            yy += 15 + (1 if first and i == 0 else 0)
            out.append(text_el("t", x + DPAD, yy, runs))
            if step and i == 0:
                out.append(text_el("t-sm", x + w - DPAD, yy, step, "end"))
        first = False
    th = yy - y + 13 * 0.22 + PB
    if h is None:
        return None, th
    dy = (h - th) / 2
    body = "\n".join(out)
    body = re.sub(r'(<text [^>]*?) y="([0-9.]+)"', lambda m: f'{m.group(1)} y="{fmt(float(m.group(2)) + dy)}"', body)
    rect = f'<rect class="shape" x="{fmt(x)}" y="{fmt(y)}" width="{fmt(w)}" height="{fmt(h)}" rx="18" stroke-width="1.5"/>'
    return rect + "\n" + body, h


ROWS1 = [
    dict(
        head=[Block("t-sm", "Phase 11, before you join the E-box plugs")],
        gate=gate("Each pair the same circuit, or empty on one side?",
                  [("", "Both halves of X6011, X6021, X6053/X60531, X6054/X60541 and X64101/X64102 "),
                   ("t-sm", "(E-box plug comparison)")]),
        stop=stop("Stop: fix the pair", "Use the M3's X6053 and X6054 sections together, never an M3 half with a "
                                        "Touring half."),
        down="yes: join the E-box plugs",
    ),
    dict(
        head=head(f"Steps 1{EN}14", "Battery disconnected", "All five DME plugs off, ignition off"),
        gate=gate("Every step passes?",
                  ("Every terminal locked; every cavity as the move table says", "1"),
                  ("Each moved or added wire open to chassis ground", "2"),
                  (f"Lamp wires under about 1{NB}{OHM} (generic)", "3"),
                  (f"Oil-pressure switch near 0{NB}{OHM}, engine stopped", "4"),
                  ("Brake test contact, X60004 pin 34 to X78 pin 3: continuity", "5"),
                  (f"Across the gear switch: near 0{NB}{OHM} in gear, open in neutral", "6"),
                  ("Start interlock, X13635 pin 4 to EWS pin 8: continuity", "7"),
                  (f"Sport: open released, near 0{NB}{OHM} pressed (BMW)", "8"),
                  ("Leak-test triangle: heater on 18, pump (the lowest) on 30", "9"),
                  ("X60004 pin 10 to K96 socket pin 4: continuity", "10"),
                  ("M3 harness X6021 pin 1 to every K96 terminal: open", "10"),
                  (f"K96 coil about 90{NB}{OHM} (generic)", "10"),
                  (f"Coils about 0.8{NB}{OHM} each, all alike (BMW)", "11"),
                  ("Six equal injector readings", "12"),
                  (f"Temperature sensors about 2,500{NB}{OHM} at 20{NB}°C (generic)", "13"),
                  ("Crankshaft sensor: a steady reading, open to ground", "14")),
        stop=stop("Stop: fix, then re-test", "Reseat or replace the terminal; a wrong cavity, such as cluster pin 14 "
                                             f"instead of 13; {IFF}"),
    ),
    dict(
        head=head(f"Steps 15{EN}18", "Battery connected", "DME still unplugged"),
        gate=gate("Every step passes?",
                  ("X60001 pin 7: battery voltage, key on or off", "15"),
                  (f"X60004 pin 26 at key position 2: above 9{NB}V (BMW)", "16"),
                  (f"X60004 pin 26 with the key off: 0{NB}V", "16"),
                  ("K6300 terminal 30: battery voltage, key on or off", "17"),
                  (f"Grounds near 0{NB}{OHM}, under 0.1{NB}V drop (generic)", "18")),
        stop=stop("Stop: fix, then re-test", f"F102 (80 A), F29, X64101/X64102; the ground eyelets and strap; {IFF}"),
    ),
]

ROWS2 = [
    dict(
        head=head("Step 19: CAN bus", "Battery disconnected", "DME and every module plugged in, ignition off"),
        gate=gate(f"About 60{NB}{OHM} from CAN high to low (BMW)?",
                  "Back-probe X60004 pins 36 and 37, or cluster X11175 pins 9 and 10. Not at the diagnosis socket."),
        stop=stop("Stop: find the fault", f"About 120{NB}{OHM}: a terminator off the bus. About 40{NB}{OHM}: a third "
                                          f"one. 0{NB}{OHM}: shorted. Open: both missing, or a broken wire."),
    ),
    dict(
        head=head(f"Steps 20{EN}29: first key-on", "Battery connected", "Charger on, DME plugged in, key at position 2, "
                  "engine off", extra="BMW: run the pump only in the tank, in fuel"),
        gate=gate("Every step passes?",
                  ("K6300 clicks; stays on a few seconds after key-off (BMW)", "20"),
                  ("INPA reaches the DME, cluster, light module, EWS, DSC", "20"),
                  ("Tool32 IDENT returns OKAY", "20"),
                  ("Supplies, temperatures, pedal and throttles, switch bits, EWS, outputs",
                   f"21, 24{EN}27, 29"),
                  ("Faults: only 1 (0x01); possibly 130 (0x82) after an EWS delete; the DSC unit's VIN faults until "
                   "Session 5", "22"),
                  ("Oil-pressure, charge and check-engine lamps lit; DSC, ABS and yellow BRAKE lamps on until "
                   "Session 5", "23"),
                  ("One prime; STEUERN_EKP clicks K96", "28"),
                  (f"5.0 {PM} 0.2{NB}bar, under 0.5{NB}bar lost (BMW)", "28")),
        stop=stop("Stop: fix before you crank", f"Plug and unplug the DME only with the ignition off; {IFF}"),
        down="yes: Sessions 3–5, then",
    ),
    dict(
        head=head(f"Steps 30{EN}32: oil-priming crank", "Phase 12", "K96 and K6327 pulled, the six coils unplugged"),
        gate=gate("Every step passes?",
                  ("Clutch up: no crank; clutch down: cranks", "30"),
                  ("Engine speed above 0; the tachometer moves", "31"),
                  ("Oil pressure shows and holds on the mechanical gauge", "32"),
                  ("The red lamp goes out", "32")),
        stop=stop("Stop", "No oil pressure: oil level, pickup O-ring, pump. Clutch interlock: EWS pin 8 input, EWS "
                          "coding. No engine speed: crankshaft sensor. Or that step's \"If it fails\"."),
    ),
    dict(
        head=head("Step 33: reset", "Refit K96, K6327 and the coils", "Then Session 6 steps 2–5"),
        gate=gate("STAT_WDK_ADAPT_WERT = 0 after the reset, and the clutch, brake and Sport bits respond?",
                  "ADAPT_LOESCHEN and FS_LOESCHEN, key off at least 15\u00a0s, key\u00a0on; then STATUS_ADAPTIONSBLOCK_06 → "
                  "STAT_WDK_ADAPT_WERT; STATUS_DIGITAL for the bits"),
        stop=stop("Stop: fix, then re-test", "Repeat with the charger on; the throttle wiring."),
    ),
]


def rows_svg(rows, y, parts, first_down=None):
    """Lay out swimlane rows from y; returns the bottom of the last row and its 'down' label."""
    prev_bottom, down = None, first_down
    for r in rows:
        hh, _ = measure_box(HX1 - HX0, r["head"], pad_bottom=PB)
        _, dh = gate_svg(r["gate"], DX0, 0, DX1 - DX0)
        sh, _ = measure_box(SX1 - SX0, r["stop"], pad_bottom=PB)
        h = max(hh, dh, sh)
        if prev_bottom is not None:
            parts.append(arrow(f"M{fmt(DCX)},{fmt(prev_bottom)} V{fmt(y - 1)}"))
            parts.append(text_el("t-sm t-b", DCX + 7, prev_bottom + GAP / 2 + 3.5, down))
        s, _ = box(HX0, y, HX1 - HX0, r["head"], cls="panel", rx=4, min_h=h, sw=1.5, pad_bottom=PB)
        parts.append(s)
        s, _ = gate_svg(r["gate"], DX0, y, DX1 - DX0, h)
        parts.append(s)
        s, _ = box(SX0, y, SX1 - SX0, r["stop"], cls="crit-s", rx=4, min_h=h, valign="middle", pad_bottom=PB)
        parts.append(s)
        mid = y + h / 2
        parts.append(arrow(f"M{DX1},{fmt(mid)} H{SX0 - 1}"))
        parts.append(text_el("t-sm t-b", (DX1 + SX0) / 2, mid - 8, "no", "middle"))
        prev_bottom, down = y + h, r.get("down", "yes")
        y = y + h + GAP
    return prev_bottom, down, y


def key(parts, items, labels):
    k, kx = key_row(8, 7, items, labels=labels, gap=18)
    parts.append(k)
    parts.append(f'<rect class="panel" x="{fmt(kx + 18)}" y="7" width="20" height="12" rx="1.5" stroke-width="1.2"/>')
    parts.append(text_el("t-sm", kx + 44, 17.5, "Set-up"))
    note = [("t-b", "BMW:"), ("", " BMW's pass value.  "), ("t-b", "Generic:"), ("", " a guide, not a limit.")]
    parts.append(text_el("t-sm", W - 8, 17.5, note, "end"))


def build1():
    parts = []
    key(parts, ["question", "stop"], {})
    bottom, down, y = rows_svg(ROWS1, 28, parts)
    parts.append(arrow(f"M{fmt(DCX)},{fmt(bottom)} V{fmt(y - 1)}"))
    parts.append(text_el("t-sm t-b", DCX + 7, bottom + GAP / 2 + 3.5, down))
    s, he = box(DX0, y, DX1 - DX0, [Block("t", [("t-b", f"Steps 19{EN}33,"), ("", " with the DME plugged in: the next figure")],
                                          anchor="middle")], cls="panel", rx=4, pad_bottom=PB)
    parts.append(s)
    H = int(round(y + he + 6))
    return svg_doc(W, H, ARIA1, "\n".join(parts)), H


def build2():
    parts = []
    key(parts, ["question", "go", "stop"], {"go": "Go on"})
    y = 28
    s, hs = box(DX0, y, DX1 - DX0, [Block("t", [("t-b", f"Steps 1{EN}18 passed"), ("", " (the previous figure)")],
                                          anchor="middle")], cls="panel", rx=4, pad_bottom=PB)
    parts.append(s)
    top = y + hs
    y = top + GAP
    parts.append(arrow(f"M{fmt(DCX)},{fmt(top)} V{fmt(y - 1)}"))
    bottom, down, y = rows_svg(ROWS2, y, parts)
    parts.append(arrow(f"M{fmt(DCX)},{fmt(bottom)} V{fmt(y - 1)}"))
    parts.append(text_el("t-sm t-b", DCX + 7, bottom + GAP / 2 + 3.5, down))
    s, he = box(DX0, y, DX1 - DX0, [Block("t t-b", "First start: Session 6 step 6", anchor="middle")], cls="new", rx=4,
                pad_bottom=PB)
    parts.append(s)
    H = int(round(y + he + 6))
    return svg_doc(W, H, ARIA2, "\n".join(parts)), H


if __name__ == "__main__":
    for name, fn in (("24-flow-power-up.svg", build1), ("24-flow-power-up-2.svg", build2)):
        svg, H = fn()
        if M.flush():
            svg, H = fn()
        p = write(name, svg, OUT)
        print(p, "height", H)
