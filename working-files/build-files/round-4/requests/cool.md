# Requests from the cool writer (cooling, fans, heater valve, A/C)

How to read these: the **Find** and **New text** blocks quote exact text, one line per `> ` line; strip the leading `  > ` to get it. **Insert after** means: add the new text as new line(s) directly below the line that ends the Find text. Every Find was checked to occur exactly once in its fragment as it stood when this file was written.

## Conflicts

- **No factual conflicts found.**
- **Overlap in WIRING-AND-CODING Session 8 (coding-body):** `coding_body_modules.md` (its correction 15) replaces the bullet "**Climate control:** no swap coding found." with the IHK coding parameters (`ZYLINDER_ZAHL`, `MOTOR_ART`, `GEREGELTER_KOMPRESSOR`, `ZUSATZWASSERPUMPE`; keep the Touring's coding). My R36 adds the compressor-lock sentences to that same bullet: apply coding-body's text first, then append R36's new sentences (everything after "no swap coding found.") to it.
- **Same lines, other writers' requests (apply as follows):**
  - README Fluids and capacities, coolant row: my R1 and susp R3 replace the same row with the same 9.3 L figure. Apply my R1, which also corrects the antifreeze, cap, thermostat and mix source, and skip susp R3. Susp's manualsnet links to the 2003 coupe (p.147) and convertible (p.153) manuals can be added to R1's Source cell.
  - WORKSHEETS Fluids log: susp R5 replaces the 420G and coolant rows in one go. Apply susp R5's 420G row and my R54 for the coolant row.
  - README Open questions: susp R12 and my R23 both rewrite the line "The S54's coolant capacity, and BMW's S54 cooling-system bleed procedure (TIS 17 00)." Apply my R23, then add susp R12's 420G line after it.
  - README Consumables, Fluids row: front R13 rewrites this row. My R4's Find ("BMW coolant and distilled water") survives front's new text, so the two apply in either order.
  - My fragments: front R23 (Phase 10, booster hose) and front R32 (Card 10a, booster hose and a power-steering torque row) still match my edited fragments exactly; I left those lines alone. With front R32 applied, Card 10a grows about 43% in all, against my 35% alone.
- **Small difference, no change needed:** `coding_body_modules.md` lists 64526936883 as an M3 compressor from 09/2002; my notes list it as a remanufactured part. Both agree the M3 uses 64526916232 from 09/2002, and that ETK doesn't list 64526916232 for the US 325i Touring. My fragments use only 64526910458 and 64526916232.
- **Shared fragment, exhaust lines untouched:** README Phase 10 and the WORKSHEETS Phase 10 torque table are mine, but their exhaust steps (5–7), the Exhaust Done-when row and the three exhaust torque rows are byte-identical to the original, so the floor writer's Find texts still match.

### R1: README 0880__fluids-and-capacities.md: Coolant capacity, antifreeze and cap
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Coolant | BMW coolant, 50/50 with distilled water (unverified); system pressure 2 bar (29 psi) | **Capacity not found** | Mix: forum posts (unverified); pressure: Flow p.60 |
- **New text:**
  > | Coolant | BMW antifreeze 82141467704, 50/50 with distilled water; the cap and system are rated 2.0 bar (29 psi), and the M3 thermostat opens at 80 °C (176 °F) | About 9.3 L (9.8 US qt) including the heater. Fill to the level mark, checked with the coolant at 30 °C (86 °F) or below | Capacity: BMW's US owner's manuals for the [2002](https://archive.org/details/manualzilla-id-7335091) and [2003](https://archive.org/details/manualzilla-id-7342203) M3; mix: [BMW ST054, engine cooling](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control/03_Engine%20Cooling-Heating%20System.pdf); cap: [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/radiator/expansion_tank_tubing/); distilled water is DIY practice ([Blankowski](https://blankowski.com/Cars/m3_coolant_change/)) |
- **Why:** Capacity found (9.3 L, 2002 and 2003 US M3 owner's manuals); BMW antifreeze at 50%; cap 2.0 bar; thermostat 80 °C. cooling_ac.md, correction 1 (Q2).

### R2: README 0880__fluids-and-capacities.md: A/C refrigerant charge and oil
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | A/C refrigerant | Per the underhood label | **Charge not found;** charge by weight from the label | — |
- **New text:**
  > | A/C refrigerant | R-134a, by weight, to the underhood label; PAG oil, about 150 ml (5.1 US fl oz) for the whole system | Expect about 0.74 kg (26 oz): MAHLE lists 715–765 g for every E46 petrol engine, the S54 included, and one M3 owner reports 710–765 g (25–27 oz). The label decides | [MAHLE](https://www.mahle-aftermarket.com/media/homepage/facelift/media-center/klima/thermokampagne/2021/2-2-handbuch-fuellmengen-pkw-&-nkw-210112-en-screen.pdf) (a vendor source), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/30199-diy-a-c-system-service-charging); oil rules: [Air conditioning](#air-conditioning) |
- **Why:** An E46 charge range now exists (MAHLE 715–765 g, PAG, 150 ml); the label still decides. cooling_ac.md, correction 2 (Q3).

### R3: README 0290__consumables-and-single-use-parts.md: Drier part number; 64536917658 is its bracket
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | A/C drier 64538377330 or 64536917658, and O-rings | Buy new | The same parts on both cars ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/condenser_air_conditioning/)); the shop supplies the compressor oil |
- **New text:**
  > | A/C receiver-drier 64538377330, and O-rings for every joint you open (64508374959, 64508375741, 64508363041, 64538375742) | Buy new | The same parts on both cars. 64536917658 is the drier's bracket, which you keep ([ETK: drier](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/drying_container/), [ETK: lines](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/coolant_lines/)). The shop supplies the PAG oil ([Air conditioning](#air-conditioning)) |
- **Why:** 64536917658 is the drier's bracket, not an alternative drier; O-rings listed by number. cooling_ac.md, correction 3 (Q3).

### R4: README 0290__consumables-and-single-use-parts.md: Coolant by part number
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > BMW coolant and distilled water
- **New text:**
  > BMW antifreeze 82141467704 (two 1 US gal jugs) and distilled water
- **Why:** BMW antifreeze part number; about 4.7 L of concentrate per 9.3 L fill, so two jugs cover a fill and top-ups. cooling_ac.md, Guide-ready parts table and correction 1.

### R5: README 0170__shop-briefs.md: A/C before teardown: record the oil
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | **A/C, before teardown** | Recover the refrigerant from both cars | The donor's compressor and lines are coming out; you'll cap every opening |
- **New text:**
  > | **A/C, before teardown** | Recover the refrigerant from both cars, and write down how much refrigerant and how much oil came out of each | The donor's compressor and pressure hose are coming out; you'll cap every opening. BMW puts the recovered oil back in at the charge ([Air conditioning](#air-conditioning)) |
- **Why:** BMW measures and replaces the oil extracted with the refrigerant, so the shop must record it per car. cooling_ac.md, correction 14 (Q3, P1).

### R6: README 0170__shop-briefs.md: A/C after first start: drier fix and BMW's service numbers
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | **A/C, after first start** | A new drier (64538377330 or 64536917658) and O-rings, a vacuum test, and a charge by weight to the underhood label | The system has been open for months; the drier and condenser are the same parts on both cars ([ETK: M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/condenser_air_conditioning/), [ETK: Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/condenser_air_conditioning/)). Bring your photo of the label |
- **New text:**
  > | **A/C, after first start** | Fit a new receiver-drier, 64538377330. Set the oil by BMW's rules: drain the donor's compressor and refill it with the amount drained from the Touring's old compressor plus 10 g, add back the oil recovered from the Touring, and add about 30 ml (1 oz) for the new drier: about 150 ml (5.1 US fl oz) of PAG in all. Evacuate for at least 30 minutes, with no more than 7 kPa (2 inHg) of change in a 5-minute hold. Charge R-134a by weight to the underhood label, then run the compressor in | The system has been open for months. Only the compressor-to-condenser hose (64536902681) is an M3 part; the condenser, the other lines and the drier's bracket are the same parts on both cars ([ETK: M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/coolant_lines/), [ETK: Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/coolant_lines/)). Bring your photo of the label, the Touring's old compressor and the recovery figures. BMW's targets: low side 1–2 bar, high side 10–15 bar, centre vent 4–20 °C (40–68 °F) ([Air conditioning](#air-conditioning)) |
- **Why:** Drier number corrected; BMW's evacuation, oil and run-in rules; only the pressure hose is M3-specific. cooling_ac.md, corrections 3, 4 and 12 (Q3, P5).

### R7: README 0180__safety.md: Refrigerant and hot coolant
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > - **Fuel.** Drain and remove the tank, filler neck and EVAP parts before you weld or grind anywhere near the rear of the car, and cap every line. Store fuel in approved cans away from the work.
- **New text:**
  > - **Refrigerant and coolant.** Never open an A/C line before a shop has recovered the refrigerant: nobody may vent it ([EPA](https://www.epa.gov/mvac/regulatory-requirements-mvac-system-servicing)). The cooling system runs at up to 2.0 bar (29 psi): open the expansion-tank cap only with the coolant cold. BMW checks the level only at 30 °C (86 °F) or below ([Cooling and oil cooler](#cooling-and-oil-cooler)).
- **Why:** Adds the refrigerant rule and the cold-cap rule to Safety; strengthens, doesn't weaken. cooling_ac.md, Takeaway 9 and Q2 (BMW fill rules).

### R8: README 0750__a-c-odometer-title-and-insurance.md: A/C refrigerant: small cans, 608/609, recovery
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > **A/C refrigerant.** Under the Clean Air Act, refrigerant may not be vented. Anyone who services a car's A/C for pay must be certified under section 609 and use approved equipment; certified equipment must remove the refrigerant before the system is opened; and recovered refrigerant must be recycled or reclaimed before it goes back into a car ([EPA](https://www.epa.gov/mvac/regulatory-requirements-mvac-system-servicing)). In practice, have a certified shop recover the refrigerant from both cars before you open any A/C line, cap every open fitting, and after the first start have a shop vacuum-test the system and charge it by weight from the underhood label. The shop brief is in [Shop briefs](#shop-briefs).
- **New text:**
  > **A/C refrigerant.** Under the Clean Air Act, nobody may vent refrigerant. Anyone who services a car's A/C for pay must be certified under Section 609 and use approved equipment; certified equipment must remove the refrigerant before the system is opened; and recovered refrigerant must be recycled or reclaimed before it goes back into a car ([EPA](https://www.epa.gov/mvac/regulatory-requirements-mvac-system-servicing)). Refrigerant in containers over 0.9 kg (2 lb) is sold only to technicians certified under Section 608 or 609. Small cans of R-134a, 0.9 kg (2 lb) or less with a self-sealing valve, can still be sold for DIY use ([EPA](https://www.epa.gov/section608/refrigerant-sales-restriction), [EPA](https://www.epa.gov/section608/section-608-and-section-609-overlap)). EPA's approved Section 609 programs include ASE, ESCO Institute and MACS ([EPA](https://www.epa.gov/mvac/section-609-technician-training-and-certification-programs)). In practice, have a certified shop recover the refrigerant from both cars before you open any A/C line, cap every open fitting, and after the first start have a shop evacuate the system and charge it by weight to the underhood label. The shop brief is in [Shop briefs](#shop-briefs), and the job in [Air conditioning](#air-conditioning).
- **Why:** EPA pages (2026): small DIY cans still legal; larger containers need 608/609 certification; no venting; 609 for paid service. cooling_ac.md, Takeaway 9 (Q3, Law).

### R9: README 0310__phase-0-paperwork-and-baseline.md: Step 7: A/C quick check, label and fan layout
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Check that the A/C blows cold, and book a shop to recover its refrigerant before teardown (Phase 4).
- **New text:**
  > Run BMW's A/C quick check: windows and doors shut, engine at 1,500–2,000 rpm, blower on medium, maximum cold, A/C on for more than 3 minutes. The centre vent should blow at least 11 °C (20 °F) below the outside air ([BMW ST054, A/C service](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control/07_AC%20Service%20and%20Diagnosis.pdf)). Photograph the underhood A/C label, which gives the refrigerant charge and oil. Note the fan layout: a manual Touring should have an electric fan in its radiator shroud, with plug X82 on the shroud; look in front of the condenser for a second fan ([Cooling and oil cooler](#cooling-and-oil-cooler)). Book a shop to recover the refrigerant before teardown (Phase 4).
- **Why:** Baseline values for the A/C, the label for the charge, and the manual Touring's fan layout, which the swap changes. cooling_ac.md, P1 and correction 5 (Q1, Q5).

### R10: README 0330__phase-2-strip-the-donor.md: Step 1: where to drain the S54's coolant
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > and the fuel tank, into approved containers, and dispose of them properly ([Safety](#safety)).
- **New text:**
  > and the fuel tank, into approved containers, and dispose of them properly ([Safety](#safety)). The M3 radiator has no drain plug: drain the coolant at the lower radiator hose and at the block's drain plug (13 mm) ([Blankowski](https://blankowski.com/Cars/m3_coolant_change/)).
- **Why:** The M3 radiator has no drain plug. cooling_ac.md, Q1 (radiator) and P1 step 5.

### R11: README 0330__phase-2-strip-the-donor.md: Engine bay list: only the A/C pressure hose
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > radiator, both fans, oil cooler and lines; power-steering reservoir, lines and cooler; A/C lines; and the DSC unit
- **New text:**
  > radiator, shroud, both fans, oil cooler and lines; the heater hoses, and the heater valve if you'll use the M3's; power-steering reservoir, lines and cooler; the A/C pressure hose 64536902681, compressor to condenser (the other A/C lines match your Touring's); and the DSC unit
- **Why:** Only the compressor-to-condenser hose is M3-specific; the S54's heater hoses replace the Touring's. cooling_ac.md, corrections 4 and 7 (Q1, Q3).

### R12: README 0350__phase-4-strip-your-touring.md: Step 1: record refrigerant and oil
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 1. Have a shop recover the Touring's A/C refrigerant before you open any line ([EPA](https://www.epa.gov/mvac/regulatory-requirements-mvac-system-servicing)), and cap every opening.
- **New text:**
  > 1. Have a shop recover the Touring's A/C refrigerant before you open any line ([EPA](https://www.epa.gov/mvac/regulatory-requirements-mvac-system-servicing)), and cap every opening. Ask the shop to write down how much refrigerant and how much oil came out: BMW puts the recovered oil back in at the charge ([Air conditioning](#air-conditioning)).
- **Why:** The oil figure sets the refill. cooling_ac.md, correction 14 (Q3).

### R13: README 0350__phase-4-strip-your-touring.md: Step 8: keep the M54's A/C compressor
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 8. Sell the M54, 5-speed, MS43 or MS45.1 DME and engine harness, the 325i axle parts and the Touring's front panels.
- **New text:**
  > 8. Sell the M54, 5-speed, MS43 or MS45.1 DME and engine harness, the 325i axle parts and the Touring's front panels. Before the M54 goes, unbolt its A/C compressor, cap its ports and keep it until the A/C is charged: BMW sets the oil in a replacement compressor by what the old one held ([Air conditioning](#air-conditioning)).
- **Why:** BMW's compressor-swap rule: old compressor's oil + 10 g. cooling_ac.md, Takeaway 6 (Q3, P5 step 3).

### R14: README 0430__phase-12-front-end-first-start-and-shakedown.md: Before the first start: coolant with the ignition on
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > 5. Ignition on, engine off: in Tool32 load `MSS54DS0.PRG`, run `IDENT` and `FS_LESEN`, and save both results. This is step 1 of the manual's [Session 6](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check), which the rest of this phase follows ([MSS54 job reference](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).
- **New text:**
  > 6. **Coolant, with the ignition on** (steps 9 and 10 of [Fill and bleed the cooling system](#fill-and-bleed-the-cooling-system)). Engine off. With IHKA: heat at maximum, blower low, A/C off. With IHKR: blower at 1 and the temperature dial fully right, since at 0 the valve is energized shut. That holds the heater valve open and runs the M3 valve's pump, if you fitted it. After a few minutes, top up to the cold mark and crack the vent screw until coolant runs without bubbles; refit it at 2.5 Nm (22 in-lb) ([BMW ST054, engine cooling](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control/03_Engine%20Cooling-Heating%20System.pdf), [BMW ST054, IHKR](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/13%20IHKR%20E46.pdf)).
- **Why:** BMW's fill rule needs the ignition on (valve open, pump running), which can't happen before the Phase 11 power-up. cooling_ac.md, correction 8 (Q2, P4).

### R15: README 0430__phase-12-front-end-first-start-and-shakedown.md: Start it, step 3: bleed with Tool32 readings
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 3. Bleed the cooling system as it warms ([Cooling and oil cooler](#cooling-and-oil-cooler)), and check that the electric fan runs.
- **New text:**
  > 3. **Bleed the cooling system as it warms** (steps 11 and 12 of [Fill and bleed the cooling system](#fill-and-bleed-the-cooling-system)). Idle about one minute with the cap off, top up and fit the cap. Then watch the coolant in Tool32, not the gauge, which shows oil temperature: `STATUS_MOTORTEMPERATUR` for the engine and `STATUS_KUEHLW_AUSL_TEMPERATUR` for the radiator outlet. The outlet should climb steadily once the engine passes about 80 °C (176 °F). Run `STEUERN_E_LUEFTER` to check that the electric fan runs.
- **Why:** Names the tools and pass value; the M3 gauge reads oil. cooling_ac.md, corrections 8 and 11 (Q2, Q5).

### R16: README 0430__phase-12-front-end-first-start-and-shakedown.md: Step 7: cool to 30 °C and check for air
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 7. Switch off, let it cool, top up the coolant and check the oil.
- **New text:**
  > 7. Switch off and let the coolant cool to 30 °C (86 °F) or below. Crack the vent screw: a hiss of air means another heat cycle, and two are usual (step 13 of [Fill and bleed the cooling system](#fill-and-bleed-the-cooling-system)). Top up to the cold mark and check the oil.
- **Why:** BMW checks the level at 30 °C or below; the DIY's heat-cycle check. cooling_ac.md, correction 8 (Q2, P4 step 10).

### R17: README 0430__phase-12-front-end-first-start-and-shakedown.md: Step 10: A/C service and BMW's pass values
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 10. **A/C:** have a shop vacuum-test the system and charge it by weight from the underhood label, then check it blows cold.
- **New text:**
  > 10. **A/C:** have a shop fit the new drier, set the oil, evacuate the system for at least 30 minutes, with no more than 7 kPa (2 inHg) of change in a 5-minute hold, and charge it by weight to the underhood label; then run the compressor in ([Shop briefs](#shop-briefs)). Then run BMW's checks: the compressor engages (`STAT_AC_EIN` and `STAT_KO_EIN` read 1); in BMW's efficiency test the evaporator reaches 15 °C (59 °F) or less within 3–4 minutes; the low side reads 1–2 bar (15–30 psi) and the high side 10–15 bar (150–225 psi); the centre vent blows 4–20 °C (40–68 °F), at least 11 °C (20 °F) below the outside air ([A/C checks and pass values](#ac-checks-and-pass-values), [worksheet](WORKSHEETS.md#ac-after-the-charge)). If the compressor never engages, start with the climate control's coded compressor lock ([manual](WIRING-AND-CODING.md#ac-with-manual-or-automatic-climate-control)).
- **Why:** BMW's evacuation rule, run-in and pass values; the coded compressor lock. cooling_ac.md, corrections 12 and 13 (Q3, Q4, Q5).

### R18: README 0430__phase-12-front-end-first-start-and-shakedown.md: Done when: cooling row with tools, plus an A/C row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Cooling | Temperature steady, no air in the system, fan cycles | Bleed again; with the M3 heater valve, check its pump's wiring and coding |
- **New text:**
  > | Cooling | In Tool32 (the M3 gauge shows oil), the radiator-outlet temperature rises once the engine passes about 80 °C; no fault 96 (0x60); no hiss at the vent screw when cold, usually after two heat cycles; the electric fan runs on `STEUERN_E_LUEFTER` and with the A/C on at idle | Bleed again; with the M3 heater valve, check its pump's wiring and coding. Fault 96 (0x60): the radiator-outlet sensor's plug and hose, then the thermostat ([Cooling checks and pass values](#cooling-checks-and-pass-values)) |
  > | A/C | The compressor engages; the evaporator reaches 15 °C (59 °F) or less within 3–4 minutes in BMW's test; low side 1–2 bar, high side 10–15 bar; centre vent 4–20 °C (40–68 °F), at least 11 °C (20 °F) below the outside air | Never engages: the coded compressor lock, then the cluster's gateway and relay K19 ([manual](WIRING-AND-CODING.md#ac-with-manual-or-automatic-climate-control)). Cools poorly: have the shop recover and weigh the charge |
- **Why:** Names the tools (the M3 gauge reads oil) and adds BMW's A/C pass values. cooling_ac.md, corrections 11 and 12 (Q4, Q5).

### R19: README 0630__troubleshooting.md: A/C won't engage: the coded lock; new row for fault 96
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | A/C won't engage | The cluster not passing the request, then the chain from the DME's pin 29 to relay K19 and the compressor clutch | [Manual](WIRING-AND-CODING.md#driving-emissions-and-comfort) |
- **New text:**
  > | A/C won't engage | The cluster not passing the request; the climate control's coded compressor lock (`KOMPRESSOR_SPERRE`); the refrigerant pressure; then the chain from the DME's pin 29 to relay K19 and the compressor clutch | [Manual](WIRING-AND-CODING.md#ac-with-manual-or-automatic-climate-control) |
  > | Fault 96 (0x60), radiator-outlet temperature plausibility, or a slow warm-up | The radiator-outlet sensor unplugged or in the wrong hose; we infer that a thermostat stuck open sets it too | [Cooling checks and pass values](#cooling-checks-and-pass-values) |
- **Why:** Both climate controls carry a coded compressor lock; fault 0x60 is the MSS54's radiator-outlet plausibility check (stuck-open thermostat is an inference). cooling_ac.md, correction 13 and Q4.

### R20: README 0870__torque-values.md: Engine table: oil-cooler screws and thermostat housing
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Oil-cooler pipes | 25 Nm (18 ft-lb) | | Flow p.57 |
- **New text:**
  > | Oil-cooler flange screws, M8 (17227833189) | 20 Nm (15 ft-lb) | New O-rings 17222245358 | Flow p.57 |
  > | Oil-cooler bracket bolt, M6 | 6 Nm (53 in-lb) | | Flow p.57 |
  > | Thermostat housing and water-pump bolts | 10 Nm (89 in-lb) | New 80 °C thermostat 11531318274 and O-ring 11531318402; new pump gasket 11517831099 | Flow p.59 |
- **Why:** Flow call-outs for the oil cooler and thermostat housing (Phase 3 and 10). cooling_ac.md, Q1 (oil cooler, thermostat) and P2.

### R21: README 0870__torque-values.md: Cooling table: fan, vent screw, drain plug, A/C flanges
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Fan clutch to water pump | 40 Nm (30 ft-lb) | **Left-hand thread:** loosen it clockwise, with a 32 mm fan wrench and a pulley holder | [Flow p.61](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing); [FCP Euro – S54 rod bearings (2022), 07:13](https://www.youtube.com/watch?v=Emjw22o_V8c&t=433s) |
- **New text:**
  > | Fan to coupling | 10 Nm (89 in-lb) | | Flow p.61 |
  > | Coolant vent screw 17111712788, in hose 11537830716 | 2.5 Nm (22 in-lb) | Plastic: don't overtighten. Tightened in Phase 10 and again at the first start | Flow p.60 |
  > | S54 block drain plug (13 mm) | 24 Nm (18 ft-lb) | New 14 mm washer; one owner's figure | [Blankowski](https://blankowski.com/Cars/m3_coolant_change/) |
  > | A/C line flanges, M8 (07119905720) | 20 Nm (15 ft-lb) | New O-rings at every joint you open | Flow p.63 |
- **Why:** Torques used in Card 10a and the Phase 10 worksheet. cooling_ac.md, Q1–Q3 call-outs and P2.

### R22: README 0900__key-numbers.md: Cooling system, fan clutch and A/C pass values
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Cooling system pressure | 2 bar (29 psi) | Flow p.60 |
  > | Fan clutch switch-on | About 92 °C (198 °F) | Flow p.61 |
- **New text:**
  > | Cooling system | Cap and system 2.0 bar (29 psi): pressure-test at 2.0 bar, never above, and hold 15 minutes. Thermostat opens at 80 °C (176 °F); overheat lamp at 120 °C (248 °F). Capacity about 9.3 L (9.8 US qt) with the heater | [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/radiator/expansion_tank_tubing/), Flow p.60, [BMW SI B17 03 16](https://static.nhtsa.gov/odi/tsbs/2016/MC-10146885-9999.pdf) (hold time, on a later model), [BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine.pdf), [BMW ST054, IHKA](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/12%20IHKA%20E46.pdf), [2003 owner's manual](https://archive.org/details/manualzilla-id-7342203) |
  > | Fan clutch switch-on and switch-off | About 92 °C (198 °F) on, 60 °C (140 °F) off | Flow p.61 |
  > | A/C pass values | Evaporator 15 °C (59 °F) or less within 3–4 minutes in BMW's efficiency test; low side 1–2 bar (15–30 psi), high side 10–15 bar (150–225 psi); vents 4–20 °C (40–68 °F), at least 11 °C (20 °F) below outside; vacuum: at least 30 minutes, then no more than 7 kPa (2 inHg) of change in 5 minutes | [BMW ST054, A/C service](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control/07_AC%20Service%20and%20Diagnosis.pdf) |
- **Why:** Cap rating, 15-minute hold, thermostat, overheat lamp, capacity, fan switch-off and BMW's A/C numbers. cooling_ac.md, corrections 1, 9 and 12 (Q5).

### R23: README 0920__open-questions-to-verify.md: Replace the capacity and charge questions
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - The S54's coolant capacity, and BMW's S54 cooling-system bleed procedure (TIS 17 00).
  > - The A/C refrigerant charge (read it from the underhood label).
- **New text:**
  > - BMW's own S54 fill-and-bleed text (TIS 17 00), and an E46 cooling-system test pressure from TIS. The capacity is settled at about 9.3 L (9.8 US qt), and the guide's bleed follows BMW's general rules.
  > - BMW's own E46 refrigerant charge and oil quantity (TIS 64), and the compressor's make and oil grade. MAHLE gives 715–765 g and 150 ml of PAG for E46 petrol engines; the underhood label decides.
  > - The MSS54's electric-fan switch points against coolant temperature.
  > - Whether a US manual 325i Touring has a pusher fan as well as its shroud fan, and whether its plug X82 reaches the M3's pusher fan.
  > - Which welded body bracket carries the M3 expansion-tank holder 17112229108.
  > - Whether the Touring's own valve-to-heater-core hose 64218363198 fits the plain valve with the S54's heater hoses.
  > - Whether the post-09/2002 Touring's A/C compressor pulley has 4 or 5 grooves (it matters only if you keep that compressor).
- **Why:** Capacity settled; bleed partly settled; charge has an E46 range; new gaps. cooling_ac.md, correction 10 and the Q1–Q5 gaps.

### R24: README 0920__open-questions-to-verify.md: IHKR: what allows the compressor
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > - Whether A/C with manual climate control (IHKR) works with the MSS54 in practice; BMW's description says it should.
- **New text:**
  > - What the IHKR's `STAT_KLIMABEREITSCHAFT_EIN` ("A/C ready after the compressor run-in") needs before it allows the compressor.
- **Why:** New gap from the IHKR46 SGBD. cooling_ac.md, Q4 gaps.

### R25: README 0910__glossary.md: PAG and pusher fan
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | PA-Soft | The tool that reads and writes the cluster and LCM memory (BMW Scanner 1.4) |
- **New text:**
  > | PAG | Polyalkylene glycol, the compressor oil in R-134a A/C systems |
  > | Pusher fan | An electric fan in front of the A/C condenser that pushes air through it and the radiator; on the M3 it's the fan the DME controls |
- **Why:** Terms the new cooling and A/C sections use. cooling_ac.md, Q1 and Q3.

### R26: README 0910__glossary.md: Receiver-drier
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | RACP | Rear axle carrier panel, the floor area the rear subframe bolts to |
- **New text:**
  > | Receiver-drier | The A/C part that holds a little refrigerant and absorbs moisture; BMW replaces it whenever a system has stood open for more than 24 hours |
- **Why:** Term the new A/C section uses. cooling_ac.md, Q3 (BMW ST054 service rules).

### R27: README 0910__glossary.md: Viscous fan
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | VANOS | BMW's variable cam timing |
- **New text:**
  > | Viscous fan (fan clutch) | An engine-driven fan with a temperature-controlled coupling. The M3 has one; a manual 325i Touring doesn't |
- **Why:** Term the new cooling section uses. cooling_ac.md, Q1 (fans).

### R28: README 0570__harness-and-re-pinning.md: Fans: X82 has to reach the pusher fan
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > The electric fan's wiring doesn't change; the M3's fan and shroud are their own parts, so fit them with its radiator ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/pusher_fan/)).
- **New text:**
  > The electric fan's DME wire doesn't move (X60004 pin 4). But on a manual Touring the fan the DME drives sits in the radiator shroud, with its plug X82 on the shroud, while the M3's electric fan is a pusher in front of the condenser: compare the plugs, then extend or re-route X82's lead to reach it ([Cooling and oil cooler](#cooling-and-oil-cooler), [manual](WIRING-AND-CODING.md#fans-and-can)).
- **Why:** A manual Touring's DME fan is the 390 W shroud fan with X82 on the shroud. cooling_ac.md, correction 5 (Q1).

### R29: README 0570__harness-and-re-pinning.md: Sensor leads: add X82
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > and the radiator-outlet sensor ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/), [Tracks and Trails – Attempting to drive my E46 M3 Touring (2026), 22:40](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=1360s)).
- **New text:**
  > and the radiator-outlet sensor ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/), [Tracks and Trails – Attempting to drive my E46 M3 Touring (2026), 22:40](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=1360s)). Add the electric fan's plug X82, which has to reach the M3's pusher fan ([manual](WIRING-AND-CODING.md#fans-and-can)).
- **Why:** X82 sits on a manual Touring's shroud, the M3 fan sits in front of the condenser. cooling_ac.md, correction 5 (Q1 inference).

### R30: README 0570__harness-and-re-pinning.md: Heater valve: every M3 except the CSL; the CSL hose
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - **Heater valve.** The US M3's valve carries a small electric pump that your Touring's plain valve lacks. Either fit your plain valve (64118369805) on the S54, with no wiring or coding, or keep the M3 valve and wire and code its pump.
- **New text:**
  > - **Heater valve.** Every E46 M3 except the CSL has a valve with a small electric pump (64118369807) that your Touring's plain valve lacks. Either fit your plain valve (64118369805) on the S54 with the CSL's valve-to-heater-core hose 64212282548, with no wiring or coding (recommended), or keep the M3 valve and wire and code its pump.
- **Why:** ETK fits the pump valve to every E46 M3 except the CSL; the CSL's hose pairs with the plain valve. cooling_ac.md, correction 7 (Q1).

### R31: README 0570__harness-and-re-pinning.md: A/C: keep the coding; the compressor lock
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Nobody has reported first-hand on manual climate control (IHKR), but BMW describes the same messages, so it should work; test it early ([manual](WIRING-AND-CODING.md#ac-with-manual-or-automatic-climate-control), [e46fanatics](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)).
- **New text:**
  > Nobody has reported first-hand on manual climate control (IHKR), but BMW describes the same messages, so it should work; test it early ([manual](WIRING-AND-CODING.md#ac-with-manual-or-automatic-climate-control), [e46fanatics](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)). Keep your Touring's climate-control coding, which carries engine and compressor settings. If the compressor never engages, check the climate control's coded compressor lock first (same manual section).
- **Why:** Both IHKs have a coded compressor lock; the IHK coding carries engine parameters (coding_body_modules.md). cooling_ac.md, correction 13 (Q4).

### R32: README 0080__documented-builds-compared.md: UNRIVALED row: one pump, on the heater valve
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > The S54's second auxiliary water pump needs its own wiring, or the cooling system is hard to bleed.
- **New text:**
  > The M3 heater valve's auxiliary water pump needs its own wiring, or the cooling system is hard to bleed.
- **Why:** The M3 has one auxiliary pump, built into its heater valve; non-M E46s have none (ETK). cooling_ac.md, Q1 (heater valve).

### R33: WIRING-AND-CODING 0280__sensor-leads-that-may-not-reach.md: Add plug X82 for the pusher fan
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Radiator-outlet temperature (X60004 pins 38 and 39) | The M3 radiator and hoses move it | Your 325i already reads this sensor, so check that its lead reaches the M3 radiator's. The one build that extended it was a Euro 318d diesel Touring ([M3projekts – E46 M3 Touring build, episode 6 (2023), 07:31](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=451s)) |
- **New text:**
  > | Electric fan, plug X82 (pin 2 from X60004 pin 4; pin 4 the F37 feed; pin 1 ground) | On a manual Touring X82 sits on the radiator shroud; the M3's electric fan is a pusher in front of the condenser | No build has reported it. Compare the plugs, then extend pins 1 and 4 in 6.0 mm² and pin 2 in 0.5 mm² ([Fans and CAN](#fans-and-can)) |
- **Why:** WDS puts X82 on a manual Touring's radiator shroud. cooling_ac.md, correction 5 and Q1 inferences.

### R34: WIRING-AND-CODING 0680__driving-emissions-and-comfort.md: A/C won't engage: add the lock and the pressure
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | A/C won't engage | The cluster not passing the request, then the chain from the climate control through the DME (X60004 pin 29) to relay K19 and 12 V at the compressor clutch | `STAT_AC_EIN`, `STAT_KO_EIN`, `STEUERN_KO`. A dead compressor clutch was the cause in one E46 (an N42 318i) ([e46fanatics](https://www.e46fanatics.com/threads/a-c-compressor-not-engaging.1278940/)) |
- **New text:**
  > | A/C won't engage | The cluster not passing the request; the climate control's coded compressor lock; the refrigerant pressure; then the chain through the DME (X60004 pin 29) to relay K19 and 12 V at the compressor clutch | `STAT_AC_EIN`; `CODIERUNG_LESEN` in IHKR46 (`KOMPRESSOR_SPERRE` = 0) or IHKA46 (`ALLGEMEIN_2` blank); `STAT_DRUCKSENSOR_WERT`; `STAT_KO_EIN`, `STEUERN_KO` ([A/C with manual or automatic climate control](#ac-with-manual-or-automatic-climate-control)). A dead compressor clutch was the cause in one E46 (an N42 318i) ([e46fanatics](https://www.e46fanatics.com/threads/a-c-compressor-not-engaging.1278940/)) |
- **Why:** Both IHKs carry a coded compressor transport lock. cooling_ac.md, correction 13 (Q4, SGBD IHKR46/IHKA46).

### R35: WIRING-AND-CODING 0680__driving-emissions-and-comfort.md: New row: fault 96 (0x60)
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Cooling system hard to bleed; heater odd | The M3 valve's pump isn't wired | [Heater valve and auxiliary water pump](#heater-valve-and-auxiliary-water-pump) |
- **New text:**
  > | Fault 96 (0x60), radiator-outlet temperature plausibility; slow warm-up | The radiator-outlet sensor unplugged or in the wrong hose; we infer that a thermostat stuck open sets it too | `STATUS_MOTORTEMPERATUR` against `STATUS_KUEHLW_AUSL_TEMPERATUR` while warming: the outlet should rise once the engine passes about 80 °C ([Cooling checks and pass values](README.md#cooling-checks-and-pass-values)) |
- **Why:** MSS54 fault 0x60 "Plausibilisierung Kühleraustrittstemp." cooling_ac.md, Q4 (SGBD) and correction 11.

### R36: WIRING-AND-CODING 0550__session-8-vehicle-order-changes-and-body-modules.md: Climate control: the compressor lock
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - **Climate control:** no swap coding found.
- **New text:**
  > - **Climate control:** no swap coding found. If the A/C never engages, read the coded compressor transport lock: Tool32 `CODIERUNG_LESEN` should show `KOMPRESSOR_SPERRE` = 0 in IHKR46, or a blank `ALLGEMEIN_2` in IHKA46. Both SGBDs have a `KOMPRESSOR_SPERRE` job (argument `SPERRE`: `EIN` or `AUS`) that sets or clears it; BMW's dealer tool calls clearing it "Deactivate transport-lock function" ([IHKR46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKR46.md), [IHKA46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKA46.md), [BMW ST054, IHKR](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/13%20IHKR%20E46.pdf)).
- **Why:** The A/C section links here for climate-module coding. cooling_ac.md, correction 13 (Q4). See Conflicts: coding-body also rewrites this bullet; append this to their text.

### R37: JOB-CARDS 0010__card-0-paperwork-and-baseline.md: A/C quick check, label and fan layout
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>A/C blows cold; refrigerant recovery booked for [Card 4](#card-4-strip-your-touring)</span>
- **New text:**
  > - [ ] <span>A/C quick check: centre vent at least 11 °C (20 °F) below the outside air; underhood A/C label photographed; recovery booked for [Card 4](#card-4-strip-your-touring)</span>
  > - [ ] <span>Fan layout noted: a fan in the radiator shroud with plug X82 on it, and whether there's one in front of the condenser ([fans](README.md#cooling-and-oil-cooler))</span>
- **Why:** Matches the Phase 0 request. cooling_ac.md, P1 and correction 5.

### R38: JOB-CARDS 0030__card-2a-strip-the-donor.md: Engine bay: the A/C pressure hose and heater hoses
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > radiator, both fans, oil cooler and lines; power-steering reservoir, lines and cooler; A/C lines; DSC unit
- **New text:**
  > radiator, shroud, both fans, oil cooler and lines; heater hoses (and the heater valve if you'll use the M3's); power-steering reservoir, lines and cooler; A/C pressure hose 64536902681; DSC unit
- **Why:** Only the compressor-to-condenser hose is M3-specific. cooling_ac.md, correction 4.

### R39: JOB-CARDS 0070__card-3c-bench-work-valves-and-seals.md: Thermostat and pump part numbers
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > CPV O-ring; rear main seal; water pump, thermostat and their gaskets.
- **New text:**
  > CPV O-ring; rear main seal; water pump and gasket 11517831099; 80 °C thermostat 11531318274 and O-ring 11531318402.
- **Why:** S54 thermostat (80 °C) and pump parts. cooling_ac.md, Q1 (thermostat, water pump).

### R40: JOB-CARDS 0070__card-3c-bench-work-valves-and-seals.md: Thermostat housing and pump torque
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Crankcase-vent return banjo (17 mm) | 19 Nm (14 ft-lb) | New washers; one video only |
- **New text:**
  > | Thermostat housing and water-pump bolts | 10 Nm (89 in-lb) | — |
- **Why:** Flow p.59; matches the torque-table and Phase 3 worksheet requests. cooling_ac.md, Q1.

### R41: JOB-CARDS 0110__card-4-strip-your-touring.md: Recovery: record the oil
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>A shop recovers the refrigerant; every opening capped ([Shop briefs](README.md#shop-briefs))</span>
- **New text:**
  > - [ ] <span>A shop recovers the refrigerant and writes down the refrigerant and oil recovered; every opening capped ([Shop briefs](README.md#shop-briefs))</span>
- **Why:** The oil figure sets the refill. cooling_ac.md, correction 14.

### R42: JOB-CARDS 0110__card-4-strip-your-touring.md: Keep the M54's A/C compressor
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>DME wires tagged first ([worksheet](WORKSHEETS.md#electronics-baseline)); M54 harness and DME out for resale; the body harness stays</span>
- **New text:**
  > - [ ] <span>The M54's A/C compressor unbolted, ports capped, and kept until the A/C is charged ([A/C](README.md#air-conditioning))</span>
- **Why:** BMW sets the replacement compressor's oil by the old one's. cooling_ac.md, Takeaway 6 (Q3).

### R43: JOB-CARDS 0260__card-12a-front-end-and-oil-prime.md: Coolant with the ignition on
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Engine oil and power-steering fluid in; no drips under the car</span>
- **New text:**
  > - [ ] <span>Ignition on, engine off: heat at maximum, blower low (IHKR: blower 1, dial fully right); after a few minutes, coolant topped up to the cold mark and the vent screw bubble-free, 2.5 Nm ([steps 9–10](README.md#fill-and-bleed-the-cooling-system))</span>
- **Why:** BMW's fill rule needs the ignition on, so the valve opens and the M3 valve's pump runs. cooling_ac.md, correction 8 (P4).

### R44: JOB-CARDS 0260__card-12a-front-end-and-oil-prime.md: Done when: coolant
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Start interlock | The starter turns only with the clutch down | |
- **New text:**
  > | Coolant | At the cold mark after the ignition-on circulation; vent screw bubble-free | |
- **Why:** Pass value for the ignition-on step. cooling_ac.md, P4.

### R45: JOB-CARDS 0270__card-12b-first-start.md: Cooling bleed with Tool32
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Cooling bled as it warms; the electric fan runs ([cooling](README.md#cooling-and-oil-cooler))</span>
- **New text:**
  > - [ ] <span>Idled one minute with the cap off; topped up; cap on ([bleed](README.md#fill-and-bleed-the-cooling-system))</span>
  > - [ ] <span>Warmed up watching Tool32, not the gauge (it shows oil): the radiator outlet (`STATUS_KUEHLW_AUSL_TEMPERATUR`) climbs once the engine (`STATUS_MOTORTEMPERATUR`) passes about 80 °C; `STEUERN_E_LUEFTER` runs the fan</span>
- **Why:** Names the tools and the pass value. cooling_ac.md, corrections 8 and 11.

### R46: JOB-CARDS 0270__card-12b-first-start.md: Cool-down check at the vent screw
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Faults read in every module; then switched off, cooled, coolant topped up and oil checked</span>
- **New text:**
  > - [ ] <span>Faults read in every module; then switched off and cooled to 30 °C or below; vent screw cracked: no hiss, or another heat cycle; coolant topped up; oil checked</span>
- **Why:** BMW checks the level at 30 °C or below; DIY heat-cycle check. cooling_ac.md, P4 step 10.

### R47: JOB-CARDS 0270__card-12b-first-start.md: Done when: cooling row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Cooling | Temperature steady, no air in the system, fan cycles | |
- **New text:**
  > | Cooling | The outlet rises once the engine passes about 80 °C; no fault 96 (0x60); no hiss at the vent screw when cold; the fan runs on command | |
- **Why:** Pass values with tools. cooling_ac.md, correction 11.

### R48: JOB-CARDS 0280__card-12c-shakedown.md: A/C service and checks
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>A/C vacuum-tested and charged by weight from the underhood label by a shop; it blows cold</span>
- **New text:**
  > - [ ] <span>A/C by a shop: new drier, oil set, 30 minutes' vacuum and a 5-minute hold, charge by weight, compressor run-in ([A/C](README.md#air-conditioning)); then BMW's checks on the [worksheet](WORKSHEETS.md#ac-after-the-charge)</span>
- **Why:** BMW's service rules and pass values. cooling_ac.md, correction 12 (Q3, Q5).

### R49: JOB-CARDS 0280__card-12c-shakedown.md: Done when: A/C
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Brakes and ABS | Firm pedal; ABS pulses in a hard stop; the car stops straight | |
- **New text:**
  > | A/C | The compressor engages; centre vent 4–20 °C (40–68 °F), at least 11 °C (20 °F) below the outside air | |
- **Why:** BMW's pass values. cooling_ac.md, Q5.

### R50: JOB-CARDS 0280__card-12c-shakedown.md: Stop and ask: A/C never engages
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Your brake lights don't come on when you slow with the parking brake.
- **New text:**
  > Your brake lights don't come on when you slow with the parking brake. The A/C never engages: check the climate control's coded compressor lock first ([manual](WIRING-AND-CODING.md#ac-with-manual-or-automatic-climate-control)).
- **Why:** KOMPRESSOR_SPERRE. cooling_ac.md, correction 13.

### R51: WORKSHEETS 0010__touring-baseline-record.md: A/C quick check, label and fan layout
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | A/C | Blows cold, before recovery in Phase 4 | |
- **New text:**
  > | A/C quick check (BMW): 1,500–2,000 rpm, blower medium, maximum cold, more than 3 minutes | Centre vent at least 11 °C (20 °F) below the outside air; record both temperatures | |
  > | Underhood A/C label | Refrigerant charge and oil, photographed | |
  > | Fan layout | A fan in the radiator shroud with plug X82 on it (manual car); any fan in front of the condenser; distance from X82 to the front of the condenser ([fans](README.md#cooling-and-oil-cooler)) | |
- **Why:** Baseline values and the fan check. cooling_ac.md, P1 and correction 5.

### R52: WORKSHEETS 0210__phase-3-on-the-bench.md: Thermostat housing and pump bolts
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Crankcase-vent return banjo (17 mm) | 19 Nm (14 ft-lb) | New washers; one video only | | |
- **New text:**
  > | Thermostat housing and water-pump bolts | 10 Nm (89 in-lb) | New 80 °C thermostat 11531318274 and O-ring 11531318402; new pump gasket 11517831099 | | |
- **Why:** Flow p.59; matches the torque table and Card 3c. cooling_ac.md, Q1.

### R53: WORKSHEETS 0270__fluids-log.md: A/C recovery: record refrigerant and oil
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | A/C recovered, donor (Phase 2) | Recovered by a shop; venting it is prohibited | — | | |
  > | A/C recovered, Touring (Phase 4) | Recovered by a shop; venting it is prohibited | — | | |
- **New text:**
  > | A/C recovered, donor (Phase 2) | Recovered by a shop; venting it is prohibited. Record the refrigerant and oil recovered | — | | |
  > | A/C recovered, Touring (Phase 4) | Recovered by a shop; venting it is prohibited. Record the refrigerant and oil recovered, and later the oil drained from the M54's compressor: both set the refill | — | | |
- **Why:** The oil figures set the refill. cooling_ac.md, correction 14.

### R54: WORKSHEETS 0270__fluids-log.md: Coolant row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Coolant (Phase 10) | BMW coolant, 50/50 with distilled water (unverified); system pressure 2 bar (29 psi) | **Capacity not found** | | |
- **New text:**
  > | Coolant (Phase 10) | BMW antifreeze 82141467704, 50/50 with distilled water; cap and system 2.0 bar (29 psi) | About 9.3 L (9.8 US qt) including the heater; fill to the level mark | | |
- **Why:** Matches the Fluids table request. cooling_ac.md, correction 1.

### R55: WORKSHEETS 0270__fluids-log.md: A/C charge row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | A/C charge, by a shop (Phase 12) | Per the underhood label | **Charge not found;** charge by weight from the label | | |
- **New text:**
  > | A/C charge, by a shop (Phase 12) | R-134a by weight to the underhood label. PAG oil: the old compressor's amount + 10 g in the donor's compressor, the recovered oil, and about 30 ml (1 oz) for the new drier | Expect about 0.74 kg (MAHLE: 715–765 g); about 150 ml of oil in all | | |
- **Why:** Matches the Fluids table request. cooling_ac.md, correction 2 and Q3.

### R56: WORKSHEETS 0430__first-start.md: Pressure test 15 minutes; ignition-on coolant step
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Cooling, pressure tester (Phase 10) | Holds 2 bar (29 psi), no drop, no leaks | |
- **New text:**
  > | Cooling, pressure tester (Phase 10) | Holds 2.0 bar (29 psi) for 15 minutes, no drop, no seepage; the cap holds and relieves at 2.0 bar | |
  > | Coolant, ignition on (IHKA: heat maximum, blower low; IHKR: blower 1, dial fully right) | Topped up to the cold mark; vent screw bubble-free | |
- **Why:** Cap rating, 15-minute hold, cap test; BMW's ignition-on fill step. cooling_ac.md, corrections 8 and 9.

### R57: WORKSHEETS 0430__first-start.md: Cooling readings with tools
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Cooling | Temperature steady, no air, fan cycles | |
- **New text:**
  > | Radiator outlet against engine temperature, Tool32, warming up | The outlet rises once the engine passes about 80 °C (176 °F); no fault 96 (0x60) | |
  > | Electric fan, `STEUERN_E_LUEFTER` | Runs on command | |
  > | Vent screw cracked, coolant at 30 °C (86 °F) or below | No hiss; otherwise another heat cycle (two are usual) | |
- **Why:** Names the tools and pass values; the M3 gauge reads oil. cooling_ac.md, correction 11.

