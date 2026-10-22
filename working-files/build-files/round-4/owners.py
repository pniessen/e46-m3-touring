"""Write frags/owners.tsv: page, fragment file, heading, owner. Unlisted sections belong to the integrator."""
import pathlib
O = {
 "README": {
  "Engine and engine bay": "cool", "Fuel": "fuel", "Front axle and steering": "front", "Rear axle": "susp",
  "Brakes and DSC": "front", "Electronics": "coding-power", "Wheels and interior": "susp",
  "Factory documentation and coding kit": "coding-power",
  "Phase 5: Metalwork 1, subframe mounts and floor": "floor", "Phase 6: Metalwork 2, rear arches": "arches",
  "Phase 7: Fit the M3 rear axle and fuel system": "fuel", "Phase 8: Fit the M3 front suspension and steering": "front",
  "Phase 10: Cooling, intake and exhaust": "cool", "Phase 11: Wiring, immobilizer and coding": "coding-power",
  "Rear subframe mount reinforcement": "floor", "Exhaust and the spare-wheel well": "floor",
  "Welding settings and safety": "floor", "Suspension for Touring weight": "susp", "Brakes and bleeding": "front",
  "Fuel system": "fuel", "Cooling and oil cooler": "cool",
  "Deep dive: electronics and coding": "coding-power", "Harness and re-pinning": "coding-power",
  "Fuel-pump control": "fuel", "Immobilizer (EWS)": "coding-power", "Instrument cluster and mileage": "coding-body",
  "DSC, brakes and steering angle": "front", "Inspection readiness": "coding-power",
  "Deep dive: bodywork and fitment": "arches", "Rear arches and doors": "arches",
  "Measure and mock up before you cut": "arches", "Arch graft step by step": "arches", "Rear doors": "arches",
  "Wheels, track and offsets": "susp", "Rear bumper, skirts and trim": "arches", "Wheel alignment": "susp",
 },
 "WIRING-AND-CODING": {
  "Before you start": "coding-power", "Hardware": "coding-power",
  "Software that works and software that doesn't": "coding-power", "Cable and EDIABAS settings": "coding-power",
  "Prove the setup on your Touring": "coding-power", "Back up everything first": "coding-body",
  "Engine harness and DME": "coding-power", "Re-pin or swap harness": "coding-power",
  "Which DME your Touring has": "coding-power", "The five DME plugs": "coding-power",
  "X60004 pin by pin": "coding-power", "Connector views and cavity numbers": "coding-power",
  "MS43 Touring: what to move": "coding-power", "MS45.1 Touring: what to move": "coding-power",
  "DM-TL leak-test pump: test before you swap": "coding-power", "E-box plugs": "coding-power",
  "Power, relays and fuses": "coding-power", "Grounds": "coding-power", "Fans and CAN": "cool",
  "Terminals, tools and repair leads": "coding-power",
  "Body-side wiring": "coding-body", "Sport button and switch center": "coding-body",
  "Brake-light switch": "coding-power", "Clutch switch, gear switch and cruise": "coding-power",
  "Cluster wiring": "coding-body", "Fuel gauge and tank senders": "fuel",
  "CAN, K-bus and the diagnosis socket": "coding-body", "Sensor leads that may not reach": "coding-power",
  "Heater valve and auxiliary water pump": "cool", "A/C with manual or automatic climate control": "cool",
  "Crash fuel cut-off": "coding-power", "Wheel-speed and pad-wear sensors": "front", "Mirrors and headlights": "coding-body",
  "Fuel-pump control": "fuel", "How each car switches the pump": "fuel", "Recommended: keep the relay": "fuel",
  "Checks on the pump circuit": "fuel", "Optional: the M3 pump module (EKP)": "fuel",
  "Faults that look like pump faults": "fuel",
  "Coding step by step": "coding-power", "Session 1: Vehicle order and codings": "coding-body",
  "Session 2: DME VIN, EWS delete and gearbox software": "coding-power", "Session 3: EWS": "coding-power",
  "Session 4: Cluster and light module": "coding-body", "Session 5: DSC coding and VIN": "coding-power",
  "Session 6: First start, adaptations and throttle check": "coding-power",
  "Session 7: Steering angle after the alignment": "coding-power",
  "Session 8: Vehicle-order changes and body modules": "coding-body", "Session 9: Light module and headlights": "coding-body",
  "Readiness and inspection": "coding-power", "What the MSS54 monitors": "coding-power",
  "The DM-TL leak test": "coding-power", "A drive plan for readiness": "coding-power",
  "Checks with Tool32 and a scanner": "coding-power", "What an inspection checks": "coding-power",
  "When a monitor won't complete": "coding-power",
  "Troubleshooting": "coding-power", "Won't start": "coding-power", "Warning lights": "coding-body",
  "DSC, ABS and steering angle": "coding-power", "Driving, emissions and comfort": "coding-power",
  "Tools and coding": "coding-power",
 },
 "JOB-CARDS": {
  "Card 2b: Cut the donor steel": "arches", "Card 3f: Bench work, DME, cluster and fenders": "coding-body",
  "Card 5: Subframe mounts and floor": "floor", "Card 6: Rear arches": "arches", "Card 7a: Fuel system": "fuel",
  "Card 7b: Rear axle in": "susp", "Card 7c: Rear axle at ride height": "susp", "Card 8a: Front suspension": "front",
  "Card 8b: Steering": "front", "Card 8c: Brakes and bleeding": "front", "Card 10a: Cooling and intake": "cool",
  "Card 10b: Exhaust": "floor", "Card 11a: Wiring and checks": "coding-power",
  "Card 11b: Power-up and coding": "coding-power", "Card 12d: Alignment and final coding": "susp",
  "Card 12e: Break-in and readiness": "coding-power",
 },
 "WORKSHEETS": {
  "Touring shell record": "floor", "Shell inspection": "floor", "Electronics baseline": "coding-power",
  "Coding backups log": "coding-power", "Donor DME VIN slots": "coding-power",
  "Donor arch targets": "arches", "Arch targets": "arches", "Floor and welding log": "floor",
  "Panel thickness": "floor", "Test coupons": "floor", "Body diagonals": "floor", "Arches and doors": "arches",
  "Phase 7: rear axle": "susp", "Phase 8: front axle, steering and brakes": "front",
  "Phase 10: cooling and exhaust": "cool", "Re-pin log: MS43 Touring": "coding-power",
  "Re-pin log: MS45.1 Touring": "coding-power", "E-box plug log": "coding-power",
  "X6011, black, 8 pins": "coding-power", "X6053 and X60531, natural, 8 pins": "coding-power",
  "X6021, black, 4 pins": "coding-power", "X6054 or X60541, and the battery feed": "coding-power",
  "Coding sessions log": "coding-power", "Fault log": "coding-power", "Alignment": "susp",
  "Speedometer and fuel gauge": "fuel", "Inspection readiness": "coding-power", "Readiness drives": "coding-power",
  "Hardware checks in Tool32": "coding-power",
 },
}
root = pathlib.Path("frags")
rows, used = ["page\tfile\theading\towner"], set()
for page, m in O.items():
    for f in sorted((root / page).glob("*.md")):
        first = f.read_text(encoding="utf-8").split("\n", 1)[0]
        head = first.lstrip("#").strip() if first.startswith("##") else "(preamble)"
        owner = m.get(head, "integrator")
        if head in m:
            used.add((page, head))
        rows.append(f"{page}\t{f.name}\t{first if first.startswith('##') else '(preamble)'}\t{owner}")
missing = [(p, h) for p, m in O.items() for h in m if (p, h) not in used]
(root / "owners.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print("unmatched map entries:", missing)
from collections import Counter
print(Counter(r.split("\t")[3] for r in rows[1:]))
