# rv-fluids: round-4 review of fuel, cooling, fans and A/C

## Summary

- **Facts checked against the notes:** about 160: every part number in the fuel, cooling and A/C tables (README 0200, 0210, 0540, 0550, 0558; WIRING 0190–0390; Cards 7a and 10a; WS 0196, 0250, 0460, 0468), pressures, capacities, torques, fault codes (decimal and hex), job names, pin numbers, unit conversions, step numbers and cross-references, plus a grep of all pages and research.md for each value and the old value it replaced.
- **Spot-checked at their URLs (15 sources, about 40 claims), BMW first.** WebFetch failed with "getaddrinfo ENOTFOUND" on every host (archive.org, wds.psjr.org, bmwfans.info), so I fetched the same URLs with curl through the session proxy and read them as text:
  - BMW ST041 Part 2 (archive.org PDF): p.24 baffle and syphon jet; p.25 regulator "influenced by engine vacuum via a hose connected to the idle air distribution pipe", left front floor, return on the filter-regulator; p.26 "5.0 Bar (+/- 0.2)", 3.8 bar; p.33 "high output fuel pump"; p.39 "DO NOT OPERATE THE FUEL PUMP unless … submersed"; p.40 access plates under the rear seat; p.41 "Remove the fuel pump relay/module (… E46 M3 located in the trunk, above right wheel well …). Connect the Relay Bypass Switch to pin 87b and 30 of the relay socket", bleed-off 0.5 bar; p.42 volume test purpose; p.46 threaded fitting, adapter 13 5 220. All confirmed.
  - WDS pin tables E46_PK96A (X10156) and E46_PK96B (X10157), drawings SP0000014336 and SP0000014408: see Decision 1. Confirmed.
  - BMW ST054 "07 AC Service and Diagnosis": ≥30 min evacuation, more than 2" change in 5 min = leak, drier after 24 h open, old oil + 10 g, 1 oz drier / 2 oz condenser or evaporator, run-in at ≥75% blower for 2 min, evaporator ≤15 °C in 3–4 min, 1–2 / 10–15 bar, 40–68 °F, 20 °F below ambient. Confirmed.
  - BMW US M3 owner's manual MY2003 (archive.org djvu text): "Cooling system including heater circuit … 9.8/9.3"; fuel 16.6 gal / 63 L, reserve 2.1 gal / 8 L. Confirmed.
  - ETK (bmwfans): M3 pressure hose 64536902681; drier 64538377330 with "Bracket drying container" 64536917658; M3 belt 11287830946 "5PK X 829"; compressor 64526910458 "to Sep '02", 64526916232 "from Sep '02"; Touring "Fan housing with fan" 17117561757 "390W", plain shroud 17111436259 only for automatics; 82141467704 "1 GALLON". Confirmed.
  - spareto: DCP05039 (OE 64526916232) 7SBU16C, ND-8, 160 ml, 4 grooves; DCP05014 (OE 64526910458) the same but 5 grooves. Confirmed.
  - SGBD (GitHub raw): KOMBI46R has `STATUS_AIF_TANKDATEN_LESEN` (HEBEL1/HEBEL2, `STAT_RESERVE`) and no `STATUS_TANKINHALT_LESEN`, which is in KOMBI46. MSS54DS0: 0x01 Relais Kraftstoffpumpe, 0x2B, 0x30, 0x35, 0x42, 0x4E, 0x60, 0x82 as the guide names them; `STAT_EKP_CFG_VERBAUT_WERT`. The FARTMATRIX row for 0x60 includes fault type 0x50 "T-Erhöhung zu gering oder Kühler wärmer als Motor", so README 0550's "among this fault's types" is right (the cooling notes' "without saying which fault uses it" missed the matrix). Confirmed.
  - EPA MVAC servicing page: no venting; Section 609 for paid work; certified equipment removes refrigerant before servicing. Confirmed.
- **WebSearch:** none used.
- **Hard limits:** refrigerant is never vented on any page; the EVAP move keeps every part working; fuel, vapour and fire warnings intact. Nothing weakened.

## Decisions on the open items

1. **K96 pin 2 is BMW's 87b, not terminal 87.** WDS's pin table for X10156 names pin 6 "Terminal 30" (F54), pin 2 "Fuel pump via relay", pin 4 the DME signal, and pin 8 "Voltage supply … Terminal 87" (the coil feed from F3; the drawing's "87" bus sits over F3). The US M3's module socket X10157 has the same pin 6 and pin 2 (plus 1 signal, 7 ground, 8 "Terminal 87"). BMW's ST041 tells you to bridge "pin 87b and 30" of exactly that E46 M3 socket, so 87b = pin 2. The fuel notes' "terminal 87" was the researcher's own mapping and would send a reader to pin 8. The text already said 87b; I made the evidence explicit and added "leave pin 8 alone" (README 0540, WIRING 0370, 0380). Figure 11 (`11-fuel-pump-control.svg`, README Figure 21) names pins by number and function only: no fix needed (optional F5 below). research.md still says "terminals 30 and 87": R1.
2. **Filter new; the donor's housing and regulator.** The fuel notes (parts table "M3 (new filter, O-rings, copper ring)", Phase 2 "the regulator housing and regulator, as cores", Phase 1 "proves the donor's pump, regulator and check valve") and the guide's own Phase 1, Phase 2 and Card 2a (which take the donor's filter-regulator) all point one way; no gap-fill says otherwise. Only the Parts list ("Buy new"), the Budget row, Card 7a's bare list and figures 04 and 34 disagreed. Rule now: a new filter 13327831089; the donor's housing 13537830368 and regulator 13531404089, proven by the donor's Phase 1 test; new copper ring, O-rings and lock ring; a new regulator only if the donor couldn't be tested or T2 traces a bleed-down to it. Applied in README 0210, 0540, 0380, Card 7a, WS 0196, caption 34; R2 (Budget), F1/F2 (figures).
3. **Tank job name.** `KOMBI46R.PRG` → `STATUS_AIF_TANKDATEN_LESEN` everywhere (README 0430, 0540, 0600; WIRING 0260, Session 4, troubleshooting; WS 0460); `STATUS_TANKINHALT_LESEN` appears only as "belongs to KOMBI46". Consistent; no change.
4. **Compressor pulley.** README 0558 states it correctly (ETK: 64526916232 from 09/2002 and only the 5PK × 829 belt for the M3; Denso via spareto: 4 grooves), and the action, count the donor's grooves before buying a belt, is right. README 0920 already carries it as an open question ("How many grooves the compressor pulleys have…"), so no request. I aligned WIRING 0300, which said "the donor's … belt", with "a new belt to suit its pulley's grooves".
5. **Views.** Figure 34's caption and drawing say "seen from above, front of the car to the left", with the car's right side at the top; figure 29's say "from below, front at the top, so the car's left is on the right". Both correct and consistent (canister and battery at the car's right rear in both). Canister wording differs slightly: F2, F5.

## Fixed directly in my fragments

| Priority | Fragment | What was wrong | Fix |
|---|---|---|---|
| P1 | README 0210 | Parts list said "Buy new" for the M3 housing and regulator, against Phase 1/2, Card 2a and the notes | Split: filter "Buy new"; housing and regulator "Donor M3", proven by the Phase 1 test, new seals, new regulator only if untested or T2 blames it |
| P1 | README 0200 | Expansion-tank holder 17112229108 listed "Buy new" (\$175), while Phase 10 fits it from the donor | Holder moved out of the "Buy new" row: "on the donor's holder 17112229108" |
| P2 | README 0540 | Filter-regulator paragraph and steps didn't say whose housing and regulator; parts-table action said only "new filter, O-rings and copper ring" | "a new M3 filter with the donor's regulator housing and regulator", the Phase 1 pass values, when to buy a new regulator; steps 2 and 3 say "the donor's" |
| P2 | README 0540 | K96 bypass: 87b mapping hedged without the evidence; no warning about pin 8 | WDS pin names quoted (pin 6 "Terminal 30", pin 8 "Terminal 87" = coil supply, leave it alone), X10157 has the same pins, so 87b = pin 2 (our reading); WDS pin-table links added |
| P2 | README 0540 | Donor test: "terminals 30 and 87b" with no pins; pass value lacked BMW's 0.5 bar bleed-off | "pins 6 and 2 of plug X10157, through the same fused switch"; "no more than 0.5 bar lost and still 4.5 bar or more" (as T2) |
| P2 | README 0380 | Phase 7 never refitted the vapour separator, the filler hose, the canister, the leak-test pump or the EVAP lines (Phase 4 removes them; Card 7a assumed the separator was back; Phase 10 checks the exhaust against them) | Step 1: separator refitted, filler hose 16117176011 on two new L42-48 clamps 07129952119. New step 9 after the axle: canister and leak-test pump in the layout chosen at the mock-up, vent and purge lines, pump plugged in. Done-when row "EVAP" |
| P2 | README 0380 | Step 2 didn't say the housing and regulator are the donor's | "the donor's regulator housing … the donor's 5-bar regulator …; a new regulator only if the donor's failed its Phase 1 test or couldn't be tested" |
| P2 | README 0410 | Done-when "Exhaust leaks: none at a cold start": the engine can't run until Phase 12 | "Checked at the first start, in Phase 12, while the joints are cold"; R6 adds it to Phase 12 |
| P2 | README 0410 | Step 1 put the tank "on the donor brackets from Phase 2", but no phase welds them to your body | Names the holder (donor's) and the brackets 41147894115/116 "you welded or riveted to the front of the right strut tower at the donor's positions"; R5 adds the welding step |
| P2 | WIRING 0300 | "Fit the donor's compressor, bracket and belt": the A/C section and figure 36 say a new belt, chosen by the pulley's grooves | "the donor's compressor and bracket …, a new belt to suit its pulley's grooves" |
| P2 | WIRING 0370 | Check 4: the 87b-to-pin mapping without WDS's names; no pin-8 warning | Same evidence as README 0540, with links to both WDS pin tables |
| P2 | WIRING 0380 | "bridge terminals 30 and 87b of the module's socket" gave no pins or fuse | "pins 6 (F54) and 2 (out to the pump) of plug X10157, through a switch with a 15 A inline fuse. Leave pin 8 … alone" |
| P2 | Card 7a | Parts list didn't say which filter-regulator parts are new; no filler-hose clamps; separator refit only a precondition | "new filter; the donor's housing and regulator (a new regulator only if it failed its Phase 1 test)"; L42-48 clamps ×2; checklist line now "separator refitted; … filler hose on two new L42-48 clamps". Card at about +28% of its original size |
| P3 | README 0540 | Canister rule omitted the muffler's right hanger (README 0210, 0470, WS and figure 29 include it) | "under 25 mm (1 in) from the muffler or its right hanger" |
| P3 | README 0550 | "plan to extend or re-route its lead", though the same section (and gapfill_builds_forums) says one manual-Touring swap plugged X82 straight in | "compare the plugs, check that the lead reaches, and extend or re-route it if it doesn't" |
| P3 | README 0558 | Header-shield studs to be welded at Phase 10, with the engine in | "Weld the studs while the engine bay is empty (Phases 4 to 8), or fit rivnut studs later" |
| P3 | WS 0196 | No record of whose regulator went in | Row "Regulator: the donor's, proven in its Phase 1 test, or new" |
| P3 | Caption 37 (proposed-fan-layout) | "X82 has to be extended or re-routed" | "may need extending or re-routing" |
| P3 | Caption 34 (proposed-fuel-layout) | "to the new filter-regulator" | "to the M3 filter-regulator, a new filter on the donor's housing and regulator" |

Checked and left alone: README 0550's fault 96 (0x60) sentence (the SGBD's FARTMATRIX supports it; I briefly edited it on the notes' reading and reverted it), every fluid against the Appendix fluids table and the worksheet fluids log (9.3 L, 82141467704, R-134a 715–765 g, about 0.74 kg, PAG about 150 ml, Denso 7SBU16C with ND-8, 160 ml), every torque against the Appendix torque table, bleed steps 1–8 / 9–10 / 11–14 against Phase 10, Phase 12, Cards 10a and 12a and figure 35, and the canister rule against README 0470, Card 5 and WS 0184. All edited fragments re-checked: headings unchanged, tables even, `$` escaped, anchors present in the preview.

## Requests to other owners

### R1: research.md (no fragment; coordinator): BMW's bypass named on the wrong terminal (P1)
- **Change:** replace
- **Find (exact current text):**
  > Run BMW's own test: bridge the K96 socket (terminals 30 and 87), confirm 5.0 ± 0.2 bar through the M3 regulator with less than 0.5 bar bleed-off, measure at least 1.12 litres in 30 seconds, and fit the M3 delivery unit and baffle if the car will see a track.
- **New text:**
  > Run BMW's own test: pull K96 and bridge its socket's pins 6 and 2 through a fused switch, BMW's "pin 87b and 30" ([BMW ST041, part 2, p.41](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)); WDS gives "Terminal 87" to pin 8, the coil supply, which must not be bridged ([WDS](https://wds.psjr.org/en/e46/zinfo/E46_PK96A.htm)). Confirm 5.0 ± 0.2 bar through the M3 regulator with no more than 0.5 bar bleed-off, and measure at least 1.12 litres in 30 seconds. The fourth round made the donor's whole in-tank set the default rather than a track-only upgrade ([Fuel system](README.md#choose-the-pump-route)).
- **Why:** "terminals 30 and 87" points a reader at pin 8 (WDS E46_PK96A/PK96B; BMW ST041 p.41 says 87b); the track-only advice contradicts the guide's route A (fuel_system_fit.md, Takeaway 1).

### R2: README 0120__budget.md: fuel row still buys the housing and regulator new (P1, rv-plan)
- **Change:** replace
- **Find (exact current text):**
  > | Fuel: new M3 filter, regulator housing, regulator, seals and clamps; the donor's in-tank set, pipe set and lines | \$250–\$900 |
- **New text:**
  > | Fuel: a new M3 filter, seals and clamps; the donor's in-tank set, pipe set, lines, regulator housing and regulator (a new regulator only if the donor's fails its Phase 1 test) | \$250–\$900 |
- **Why:** the Parts list (README 0210), Phase 1/2/7, Card 2a and the fuel notes (Guide-ready parts table and Phase 2 strip list) reuse the donor's housing and regulator; the rest of the row is unchanged.

### R3: README 0110__choose-the-donor.md and 0320__phase-1-buy-and-inspect-the-donor.md: donor fuel test lacks BMW's bleed-off limit and the pins (P2, rv-plan)
- **Change:** replace (two places)
- **Find (exact current text, 0110):**
  > pump run through a bypass at its module's socket, terminals 30 and 87b, BMW's method ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)) | 5.0 ± 0.2 bar, and 4.5 bar or more after 20 minutes
- **New text:**
  > pump run through a bypass at its module's socket, terminals 30 and 87b (pins 6 and 2 of plug X10157, through a switch with a 15 A inline fuse), BMW's method ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)) | 5.0 ± 0.2 bar; 20 minutes later no more than 0.5 bar (7 psi) lost and still 4.5 bar or more
- **Find (exact current text, 0320):**
  > with the pump on a bypass: 5.0 ± 0.2 bar (72.5 ± 2.9 psi), and 4.5 bar (65 psi) or more 20 minutes later
- **New text:**
  > with the pump on a bypass (pins 6 and 2 of the module's plug X10157): 5.0 ± 0.2 bar (72.5 ± 2.9 psi); 20 minutes later no more than 0.5 bar (7 psi) lost and still 4.5 bar (65 psi) or more. It decides whether the donor's regulator goes back in ([Filter-regulator and vacuum reference](#filter-regulator-and-vacuum-reference))
- **Why:** this test now qualifies the donor's regulator for reuse, and BMW's own fail is "bleed off … more than 0.5 bar" (ST041 p.41), as in T2; WDS E46_PK96B gives pins 6 and 2.

### R4: JOB-CARDS 0020__card-1-buy-and-inspect-the-donor.md and WORKSHEETS 0110__vanos-tests.md: the same bleed-off limit (P2, rv-ref)
- **Change:** replace
- **Find (Card 1):**
  > fuel pressure 5.0 ± 0.2 bar (72.5 ± 2.9 psi), and 4.5 bar (65 psi) or more 20 minutes later | |
- **New text:**
  > fuel pressure 5.0 ± 0.2 bar (72.5 ± 2.9 psi); 20 minutes later no more than 0.5 bar (7 psi) lost and still 4.5 bar (65 psi) or more | |
- **Find (WS 0110):**
  > | 20 minutes later | Still above 4.5 bar | |
- **New text:**
  > | 20 minutes later | No more than 0.5 bar (7 psi) lost, and still above 4.5 bar. A pass lets the donor's regulator go back in | |
- **Why:** as R3; matches T2 on Card 7a and WS 0196.

### R5: README 0360__phase-5-metalwork-1-subframe-mounts-and-floor.md and JOB-CARDS 0120__card-5-subframe-mounts-and-floor.md: no phase welds the expansion-tank brackets (P2, rv-body)
- **Change:** insert after (keeps the step numbers; WS cites "Phase 5, step 10")
- **Find (exact current text, end of Phase 5 step 7):**
  > Weld them in now, with the rest of the underside work.
- **New text (appended to step 7):**
  > While the welder is out and the engine bay is empty, also weld the donor's secondary-air-pump brackets 41147894115 (front) and 41147894116 (rear), or new ones, to the front of the right strut tower at the positions you measured on the donor; the M3 expansion-tank holder bolts to them in Phase 10. Copies on rivnuts work too ([Cooling and oil cooler](#cooling-and-oil-cooler)).
- **Find (Card 5):**
  > - [ ] <span>V-brace mounting boxes welded in, if you'll fit the V-brace</span>
- **New text:**
  > - [ ] <span>V-brace mounting boxes welded in, if you'll fit the V-brace; expansion-tank brackets 41147894115/116 on the right strut tower, at the donor's positions</span>
- **Why:** Phase 2 cuts the brackets off the donor and Card 10a says "Before you start: the expansion-tank brackets welded in", but no phase or card says when (gapfill_parts_prices.md Gap 7; README 0550 "weld copies or the new parts in").

### R6: README 0430__phase-12-front-end-first-start-and-shakedown.md and JOB-CARDS 0270__card-12b-first-start.md: the exhaust-leak check belongs at the first start (P2, rv-plan; card rv-ref)
- **Change:** replace
- **Find (0430):**
  > Look for fuel, oil, coolant and power-steering leaks, and listen for knocking or VANOS rattle.
- **New text:**
  > Look for fuel, oil, coolant and power-steering leaks, and for exhaust leaks at each joint while they're still cold (listen, or spray soapy water on them), and listen for knocking or VANOS rattle.
- **Find (Card 12b):**
  > - [ ] <span>Idling: no fuel, oil, coolant or power-steering leaks; no knocking or VANOS rattle</span>
- **New text:**
  > - [ ] <span>Idling: no fuel, oil, coolant, power-steering or exhaust leaks; no knocking or VANOS rattle</span>
- **Why:** Phase 10's Done-when carried a cold-start exhaust-leak check before the engine can run; I re-labelled it there as a Phase 12 check.

### R7: JOB-CARDS 0150__card-7b-rear-axle-in.md: refit the canister after the axle (P2, rv-chassis)
- **Change:** insert after
- **Find (exact current text):**
  > - [ ] <span>Your own wheel-speed sensors, or an MK60 donor's; never an MK20 donor's ([sensors](README.md#dsc-brakes-and-steering-angle))</span>
- **New text:**
  > - [ ] <span>Canister and leak-test pump back in the layout chosen at the mock-up (your mount, or the M3 holder 16132229735 and cover 51717893604); vent and purge hoses on without kinks; the pump plugged in ([Phase 7](README.md#phase-7-fit-the-m3-rear-axle-and-fuel-system), step 9)</span>
- **Why:** Phase 4 removes them and no phase or card put them back; README 0380 now has step 9 and an "EVAP" Done-when row. The M3 holder sits just behind the diff, so after the axle is up.

### R8: README 0330__phase-2-strip-the-donor.md: measure the brackets before they come off (P3, rv-plan)
- **Change:** replace
- **Find (exact current text):**
  > Also the brackets for the expansion tank and secondary-air pump, which a non-M body doesn't have
- **New text:**
  > Also the brackets for the expansion tank and secondary-air pump (41147894115 and 41147894116, on the front of the right strut tower), which a non-M body doesn't have: measure and photograph their positions before you cut them off
- **Why:** README 0550 tells you to measure them on the donor; Phase 2 is where you meet them (gapfill_parts_prices.md Gap 7).

### R9: README 0570__harness-and-re-pinning.md: X82 may already reach (P3, rv-coding)
- **Change:** replace
- **Find (exact current text):**
  > compare the plugs, then extend or re-route X82's lead to reach it
- **New text:**
  > compare the plugs, then extend or re-route X82's lead if it doesn't reach (one manual-Touring swap plugged it straight in)
- **Why:** gapfill_builds_forums.md Gap 3 ("plugged right in"); matches README 0200, 0550, WIRING 0190 and 0280.

### R10: README 0920__open-questions-to-verify.md: the pusher-fan item isn't "unverified" (P3, rv-ref)
- **Change:** replace
- **Find (exact current text):**
  > (owners say it doesn't, unverified)
- **New text:**
  > (owners say it doesn't: [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/246516-non-m-electric-fan-fitment))
- **Why:** the posts were read, not seen in a snippet (gapfill_builds_forums.md Gap 3), so the style rule's "(unverified)" doesn't apply.

## Figure fixes

### F1: `04-fuel-pressure.svg` (README Figure 13, redraw 04): the filter-regulator is drawn "Buy new" (P1)
- **Wrong:** the "AFTER" panel's `<rect class="new" x="170" y="232" width="88" height="66" …>` ("M3 filter- / regulator / 5.0 bar", text class `new-t`) shows the whole unit as bought new. The guide now fits a new filter on the donor's housing and regulator.
- **Fix:** split the box: the filter at the inlet end in class `new` (Buy new) with a `t-xs new-t` label "new filter", the housing and regulator in class `donor` with "5.0 bar" in `donor-t`. In the aria-label, replace "the feed path to the new M3 filter-regulator" with "the feed path to the M3 filter-regulator, a new filter on the donor's housing and regulator,".

### F2: `34-fuel-layout.svg` (README Figure 14): housing and regulator "bought new"; canister rule omits the hanger (P1, P3)
- **Wrong:** `<rect class="new" x="300" y="338" width="28" height="28" …>` (housing) and `<circle class="new" cx="308" cy="330" r="7" …>` (regulator) are green, and the aria-label says "the M3 filter, regulator housing and 5-bar regulator, bought new". The canister note reads "(under 25 mm to the muffler: M3 holder; 25 mm or more: either)".
- **Fix:** change those two elements to class `donor`; keep the filter rect (x=328) `new`. Aria-label: "a new M3 filter on the donor's regulator housing and 5-bar regulator". Canister note and aria-label: "under 25 mm to the muffler or its right hanger: M3 holder; 25 mm or more: either", as README 0470 and 0540 state the rule.

### F3: `37-fan-layout.svg` (README Figure 15): pusher fan "not settled" (P3)
- **Wrong:** the "?" box says "A pusher fan here too? Not settled: see below", and the note and aria-label say it "isn't settled", while README 0200, 0550, WIRING 0190 and gapfill_builds_forums.md say a manual Touring almost certainly has none. The orange-lead note reads as if X82 must always be extended.
- **Fix:** box: "A pusher fan here too? Almost certainly not: see below". Note: "A manual Touring almost certainly has no pusher fan: ETK lists one (64546988913) with no gearbox note, but the DME has only one fan output and owners call it the automatic's part. Check your car in Phase 0." Lead note: "The orange lead: extend or re-route X82 only if it doesn't reach the pusher (one manual-Touring swap plugged straight in), keeping the pins; …". Same wording in the aria-label.

### F4: `29-floor-exhaust-plan.svg` (README Figure 7, in 0470): canister rule worded differently from figure 34 (P3)
- **Wrong:** "Canister within 25 mm of the muffler or H3? Fit the M3 holder 16132229735 and cover 51717893604 at the donor's position." It doesn't say to expect the M3 holder with an M3 floor, or that at 25 mm or more either layout works.
- **Fix:** "M3 floor: expect the M3 holder. Canister under 25 mm from the muffler or H3: fit holder 16132229735 and cover 51717893604 at the donor's position; 25 mm or more: either layout works." Same rule in the aria-label. (Its "seen from below, front at the top" wording is correct.)

### F5: `11-fuel-pump-control.svg` (README Figure 21): optional pin-8 warning (P3)
- **Wrong:** nothing wrong: the bypass row names pins 6 and 2 by function. But WDS calls pin 8 "Terminal 87", which a reader of BMW's "87b and 30" could bridge by mistake.
- **Fix (optional):** in the "Fuel tests: the bypass" box, add a line "Not pin 8: WDS's 'Terminal 87' is the coil supply."

## Not verified

- Whether the M3 canister holder can go in before the rear axle (I put the refit after it, to be safe).
- The pulley grooves on a given donor: still a count on the car (README 0920 has it).
- BMW's own refrigerant charge and TIS 17 00 bleed text: still open, as README 0920 says.
