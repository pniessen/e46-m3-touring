"""Figure 26 (WIRING "Warning lights"), redrawn in round 4 from WIRING-AND-CODING fragment 0660 (with 0250, 0520,
0670 and the coordinator's cluster rule): red and yellow BRAKE lamps, the M3 MK60 wording, the ALSZ order rule."""
import sys
sys.dont_write_bytecode = True
import re
import flowkit
from flowkit import *  # noqa: F401,F403

flowkit.LINE_H["t"] = 15.0
flowkit.LINE_H["t-sm"] = 14.0

W = 800
OUT = DIAGRAMS  # writes the published file
NB = " "
EN = "–"
PB = 5.0

ARIA = ("A lookup chart for the warning lights. Expected, not a fault: with the key on and the engine off the red "
        "oil-pressure lamp, the charge lamp and the check-engine lamp are lit, and the red BRAKE lamp while the parking "
        "brake is on; after the start, oil and charge go out within seconds and the check-engine lamp goes out unless a "
        "fault asks for it; the DSC, ABS and yellow BRAKE lamps stay on until Session 5. To tell lamp wiring from a real "
        "fault, read STAT_MIL_EIN: at 0 with the check-engine lamp lit while the engine runs, suspect the cluster or its "
        "coding; at 1, read FS_LESEN. The two BRAKE lamps mean different things (BMW ST056): red is low brake fluid or "
        "the parking brake on, not a DSC fault; yellow is a DSC or ABS fault, lit with the ABS and DSC lamps; have all four "
        "dark before the inspection. Then each lamp with its likely causes, most likely first, and the first check. Check "
        "engine: the leak-test circuit, SMG software in the DME, the O2 sensors or their heaters, secondary air, injector "
        "circuits, throttle or pedal, misfire. No lamp but faults stored: the pump fault 1 (0x01), expected with US "
        "software on K96; possibly 130 (0x82) after an EWS delete; 110 (0x6E) if the Sport LED isn't wired. Oil pressure, "
        "out at key-on: the pin-11 wire or the cluster's CAN setting; on while running: low oil pressure or a grounded "
        "lamp wire. Charge, out at key-on: the pin-1 wire or GENERATOR_UEBER_CAN; on while running: alternator, belt, the "
        "terminal-61 wire, low voltage; with a donor built from 03/2004, if the lamp stays dark with GENERATOR_UEBER_CAN "
        "at nicht_aktiv, code it aktiv. Oil level: the pin-21 wire, TOG_UEBER_CAN, or the sensor, fault 44 (0x2C). EML: "
        "the throttle sensors, pedal, synchronization or actuator, low charging voltage, or the adaptation not done. ABS, "
        "DSC and yellow BRAKE: the VIN not initialized (5E1F; 5EF1 in PA-Soft) until the cluster carries your VIN; wheel-speed faults "
        "5D90 to 5DC5, whose third character names the wheel, and an MK20 donor's sensors don't fit; the steering angle "
        "not calibrated; an M3 MK60 not yet coded from a session order dated 09/2002 (#0902) or later, or reset in "
        "PA-Soft instead of initialised in INPA, so write the VIN, code it, run Shift+F4 then F1, and only if it still "
        "fails refit your Touring's own unit; the yellow BRAKE lamp alone, the brake test-contact wire still on pin 28. "
        "Red BRAKE: low brake fluid, often an unbled system, which also switches DSC off, or the parking brake or its "
        "switch; check the fluid level and STATUS_SCHALTER. Cruise won't engage: not the M3 clutch module, the gear "
        "switch, implausible brake contacts, SMG software, the steering-wheel data line. Airbag: a seat swap or the "
        "slip-ring plugs; never bypass it, since its crash message starts the DME's pump cut-off, unverified with K96. "
        "Gearbox or SMG lamp and tamper dot: SMG software; after a vehicle-order change, the modules it touches not yet "
        "coded; the cluster's VIN or mileage not matching the light module's. The car's order lives in the light module "
        "(ALSZ): read it from there; the M3 cluster keeps the donor's order and is coded only from its own read-out; never "
        "use Code Car. Check filler cap: the cap, or a leak.")

CX0, CX1 = 8, 392       # left grid column
DX0, DX1 = 408, 792     # right grid column


def cell(name, causes, check):
    """A lookup cell: the lamp in bold, its causes, then the first check in t-sm."""
    causes = re.sub(r"(^|\. )([1-7]) ", lambda m: m.group(1) + m.group(2) + NB, causes)  # keep "7 Misfire" together
    blocks = [Block("t", [("t-b", name), ("", " " + causes)])]
    blocks.append(Block("t-sm", [("t-b", "Check:"), ("", " " + check)], gap_before=2))
    return blocks


CELLS = [
    cell("Check engine:",
         "1 Leak-test circuit: heater 14 (0x0E), valve 27 (0x1B), module 127 (0x7F), after the pin moves or with a "
         "three-wire module. 2 SMG software in the DME (SMG bus faults, \"MIL request from SMG\"). 3 O2 sensors or their "
         f"heaters, faults 37{EN}40 (0x25{EN}0x28): a wrong or mixed O2 harness. 4 Secondary air, faults 19, 63, 170 and "
         "171 (0x13, 0x3F, 0xAA, 0xAB). 5 Injector circuits (an X6053 mix). 6 Throttle or pedal (the EML lamp too). "
         "7 Misfire.",
         "STAT_MIL_EIN; FS_LESEN with its stored values; the leak-test triangle (step 9); START_SYSTEMCHECK_DMTL and "
         "LESEN_SYSTEMCHECK_DMTL; STEUERN_SLS_CHECK"),
    cell("No lamp, but faults stored:",
         "location 1 (0x01), the pump fault, expected with US software on K96; possibly 130 (0x82) after an EWS delete; "
         "110 (0x6E) if the Sport LED isn't wired.",
         "FS_LESEN, and confirm STAT_MIL_EIN = 0"),
    cell("Oil pressure (red), out at key-on:",
         "the pin-11 wire missing or on the wrong cluster pin, or the cluster expects oil pressure over CAN "
         "(CAN_OELDRUCKSCHALTER). "
         "On while running: low oil pressure, or the lamp wire grounded.",
         "the key-on lamp; power-up steps 3 and 4; a\u00a0mechanical\u00a0gauge"),
    cell("Charge, out at key-on:",
         "the pin-1 wire, or GENERATOR_UEBER_CAN; with a donor built from 03/2004, if it stays dark at nicht_aktiv, "
         "code it aktiv. On while running: alternator, belt, the terminal-61 wire to X60003 pin 13, low voltage.",
         "the key-on lamp; STATUS_UBATT running"),
    cell("Oil level (yellow):",
         "the pin-21 wire to cluster pin 17, or TOG_UEBER_CAN; the sensor itself, fault 44 (0x2C).",
         "STATUS_OEL_TEMPERATUR reads plausibly"),
    cell("EML:",
         "throttle sensor 1 or 2, the pedal, throttle synchronization, the actuator; low charging voltage; adaptation "
         "not done.",
         f"faults 118{EN}121 (0x76{EN}0x79), 60 and 61 (0x3C, 0x3D), 111 and 112 (0x6F, 0x70), 228{EN}230 "
         f"(0xE4{EN}0xE6); STAT_WDK_ADAPT_WERT"),
    cell("ABS, DSC, yellow BRAKE:",
         f"1 VIN not initialized (5E1F; 5EF1 in PA-Soft) until the cluster carries your VIN. 2 Wheel-speed faults 5D90{EN}5DC5, "
         "which name the wheel: 5D9x front left, 5DAx front right, 5DBx rear left, 5DCx rear right; an MK20 donor's "
         "sensors don't fit. "
         "3 Steering angle not calibrated. 4 An M3 MK60 not yet coded from a session order dated 09/2002 (#0902) or "
         "later, or reset in PA-Soft instead of initialised in INPA: write the VIN, code it, then Shift+F4 → F1; only if "
         "it still fails, refit your Touring's MK60. 5 The yellow BRAKE lamp alone: the brake test-contact wire still on "
         "pin 28.",
         "INPA's DSC fault memory and wheel speeds"),
    cell("Red BRAKE:",
         "low brake fluid, often an unbled system, which also switches DSC off; or the parking brake on, or its switch. "
         "Not a DSC or ABS fault (BMW ST056).",
         "the fluid level; DSC_MK60.PRG → STATUS_SCHALTER: STAT_HANDBREMSE_SCHALTER_EIN and "
         "STAT_BREMSFLUESSIGKEIT_SCHALTER_EIN follow the lever and the fluid switch"),
    cell("Cruise won't engage:",
         "1 Not the M3 clutch module. 2 Gear switch missing or open. 3 Brake contacts implausible, fault 106 (0x6A). "
         "4 SMG software. 5 Steering-wheel data line, fault 81 (0x51).",
         "STAT_KRAFTSCHLUSS_EIN in gear; STAT_BLS_EIN, STAT_BLTS_EIN; STAT_MFL1_EIN…; faults 80 (0x50), "
         "106 (0x6A), 139 (0x8B), 194 (0xC2)"),
    cell("Airbag:",
         "a seat swap (belt tensioners, occupancy mat), the steering wheel's slip-ring plugs. Never bypass it: its "
         "crash message starts the DME's pump cut-off (unverified with K96).",
         "INPA's airbag fault memory"),
    cell("Gearbox or SMG lamp; tamper dot:",
         "SMG software; after a gearbox-type change in the vehicle order, the modules it touches not yet coded; the "
         "cluster's VIN or mileage not matching the light module's. Read the car's order from ALSZ, the light module; "
         "the M3 cluster keeps the donor's order and is coded only from its own read-out. Never Code Car.",
         "the DME's software; the order in ALSZ; the cluster's VIN"),
    cell("\"Check filler cap\":",
         "the cap not sealing; a leak found after refueling.",
         "LESEN_SYSTEMCHECK_DMTL; fault 181 (0xB5)"),
]

PADX = 10
CELL_GAP = 0


def build():
    parts = []
    # Top strip: what's expected, and the check-engine fork
    y = 8
    exp = [Block("t", [("t-b", "Expected, not a fault."), ("", " Key on, engine off: the red oil-pressure lamp, the charge "
                                                             "lamp and the check-engine lamp lit, and the red BRAKE lamp "
                                                             "while the parking brake is on. After the start, oil and "
                                                             "charge go out within seconds, and check engine unless a fault "
                                                             "asks for it. The DSC, ABS and yellow BRAKE lamps stay on "
                                                             "until Session 5.")])]
    TX1, QX0 = 344, 360    # top strip: expected states | the check-engine question
    eh, _ = measure_box(TX1 - CX0, exp, pad_bottom=PB)
    s, eh = box(CX0, y, TX1 - CX0, exp, cls="new", rx=4, pad_bottom=PB)
    parts.append(s)

    q = [Block("t", "Check-engine lamp lit with the engine running: wiring or a real fault? Read STAT_MIL_EIN.")]
    qh, _ = measure_box(DX1 - QX0, q, pad_x=14, pad_bottom=PB)
    s, qh = box(QX0, y, DX1 - QX0, q, cls="shape", rx=18, pad_x=14, valign="middle", pad_bottom=PB, min_h=max(qh, 30))
    parts.append(s)
    oy = y + qh + 16
    half = (DX1 - QX0 - 12) / 2
    o0 = [Block("t", [("t-b crit-t", "0"), ("", " with the lamp lit: suspect the cluster or its coding.")])]
    o1 = [Block("t", [("t-b", "1:"), ("", " read FS_LESEN, then see Check engine below.")])]
    h0, _ = measure_box(half, o0, pad_bottom=PB)
    h1, _ = measure_box(half, o1, pad_bottom=PB)
    hh = max(h0, h1)
    s, _ = box(QX0, oy, half, o0, cls="crit-s", rx=4, min_h=hh, pad_bottom=PB)
    parts.append(s)
    s, _ = box(QX0 + half + 12, oy, half, o1, cls="shape", rx=4, min_h=hh, pad_bottom=PB)
    parts.append(s)
    for cx, lab in ((QX0 + half / 2, "0"), (QX0 + half + 12 + half / 2, "1")):
        parts.append(arrow(f"M{fmt(cx)},{fmt(y + qh)} V{fmt(oy - 1)}"))
        parts.append(text_el("t-sm t-b", cx + 6, y + qh + 12, lab))
    by = oy + hh + 10
    brake = [Block("t-sm", [("t-b", "Two BRAKE lamps (BMW ST056):"),
                            ("", " red is low brake fluid or the parking brake on, not a DSC fault; yellow is a DSC or "
                                 "ABS fault, lit with the ABS and DSC lamps. Have all four dark before the inspection.")])]
    s, bh = box(QX0, by, DX1 - QX0, brake, cls="warn-f", rx=4, pad_bottom=PB)
    parts.append(s)
    top_bottom = max(y + eh, by + bh)

    # Grid: balance the cells over two columns, keeping the manual's order
    hs = [measure_box(CX1 - CX0, c, pad_x=PADX, pad_bottom=PB)[0] for c in CELLS]
    best = None
    for k in range(1, len(CELLS)):
        lh, rh = sum(hs[:k]), sum(hs[k:])
        cand = (max(lh, rh), k)
        best = min(best, cand) if best else cand
    k = best[1]
    gy = top_bottom + 10
    parts.append(text_el("t-h", CX0, gy + 13, "LAMPS AND SYMPTOMS: LIKELY CAUSES, MOST LIKELY FIRST, AND THE FIRST CHECK"))
    gy += 20
    parts.append(line(f"M{CX0},{fmt(gy)} H{CX1}", cls="ln-thin"))
    parts.append(line(f"M{DX0},{fmt(gy)} H{DX1}", cls="ln-thin"))
    bottoms = []
    for col, (x0, x1, cells, chs) in enumerate(((CX0, CX1, CELLS[:k], hs[:k]), (DX0, DX1, CELLS[k:], hs[k:]))):
        yy = gy
        for c, h in zip(cells, chs):
            tsvg, _, _ = layout_blocks(c, x0, yy, x1 - x0, pad_x=PADX, pad_bottom=PB)
            parts.append(tsvg)
            yy += h
            parts.append(line(f"M{x0},{fmt(yy)} H{x1}", cls="ln-faint"))
        bottoms.append(yy)
    H = int(round(max(bottoms) + 8))
    return svg_doc(W, H, ARIA, "\n".join(parts)), H


if __name__ == "__main__":
    svg, H = build()
    if M.flush():
        svg, H = build()
    p = write("26-flow-warning-lights.svg", svg, OUT)
    print(p, "height", H)
