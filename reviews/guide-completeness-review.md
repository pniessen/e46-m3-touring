# Completeness review: E46 M3 Touring conversion guide

Reviewed 22 October 2026. Scope: `e46-m3-touring-conversion/README.md` (every section) and the nine files in `research_notes/E46 M3 Touring open questions/`. The test applied throughout: could the intended reader finish the car with this guide plus the factory manual it points to?

**The reader:** a hands-on amateur with a day job. They have done brakes, suspension, clutches and some engine work, can MIG-weld sheet steel and do basic bodywork, have a lift or good stands and an engine hoist, and can follow BMW procedures. They have never done an engine swap, BMW coding or panel grafting. Both cars are in their garage: a running US E46 M3 manual donor and a US 325i Touring, 5-speed, rear-wheel drive. The owner called it a "325x"; section 5 says where the guide's advice would break if the car turns out to be an xi.

## Verdict

**No, not yet.** As a planning guide it is strong. It gets the recipe right, names the hard decisions, lists the parts that actually differ, frames the federal and state rules sensibly and links its sources, and the phase order is mostly sound. But this reader can't finish the car from it, for two reasons.

First, four things would stop or seriously endanger the build if followed as written:

- The late S54 rod-bolt procedure gives one tightening cycle where BMW requires three.
- The body-side re-pin table runs in the wrong direction and is incomplete for an MS43 or MS45 Touring.
- The fuel-pump trigger is left as an open question.
- The DSC and brake plan has a documented failure in exactly this kind of car, and the guide never mentions the brake booster or brake hoses that go with it.

Second, the guide lacks the reference data an amateur reaches for at the bench. It gives no fluids or capacities, few torque values beyond the driveline, no alignment figures and no weld settings. It defers to "BMW's repair and wiring documentation" without naming or linking it. Phases 1–13 have no "done when" checks.

**How to get to yes:**

1. Fold in the research notes. They fix the rod-bolt error and the three electrical problems, and most of the coding, fuel, subframe and arch-steel gaps. Of the 55 gaps below, the notes fully cover 17, partly cover 26 and don't touch 12.
2. Add what the notes don't cover: the brake booster, master cylinder and hose decision; alignment before steering-angle calibration; a ride-height and mock-up method for the arches; welding settings and fume and fire safety; A/C recovery for both cars; space, logistics and budget; briefs for the shops; and a verification line for each phase.
3. Add the reference tables in section 6 of this review: fluids, extra torque values and BMW's E46 M3 alignment table.

After that I'd expect this reader to finish. The S54 refresh, the arch graft and the cluster EEPROM work are still where outside help is most likely.

**Counts:** 4 blocking, 29 important, 22 nice-to-have.

**How this was checked:** I read every section of the guide and all nine notes files. To source values I read these myself:

- **BMW ST041 technical data**, fetched from archive.org.
- **The BMW S54 training text.**
- **The "Flow" E46 M3 torque compilation**, a forum PDF built on RealOEM printouts with a BMW TIS alignment printout. I read its pages as images.
- **ETK pages on bmwfans.info**, for the booster, master cylinder, brake hoses, condenser, drier, steering joint and trunk-floor brackets.
- **Fluid and safety pages** from BimmerWorld, Miller, OSHA, EPA and California BAR.

Turner, Pelican and newTIS were behind Cloudflare and were not used. In the tables, "(read)" means I read the page or file, "(snippet)" means I saw only a search summary, and "(notes)" means the value comes from a notes file, which carries its own read or snippet tag.

---

## 1. Blocking gaps

These would stop the build, or put the engine or the brakes at serious risk.

| # | Where in the guide | What's missing or wrong | Why it matters for this reader | Covered by the new research notes? | Suggestion |
|---|---|---|---|---|---|
| B1 | Phase 3; "S54 refresh on the stand" → Rod bearings steps 2–3; Appendix torque rows | **The late (M10) rod-bolt procedure is wrong.** BMW's SI B11 04 04 calls for new M10 E-Torx bolts tightened three times. Each cycle is 5 Nm, 30 Nm, then 105° in one pull, with the bolt backed off about one turn between cycles; the third cycle is final. The guide gives one cycle. It also gives the change-over as 02/2003 (BMW says 12/12–13/2002 production), never says how to tell the bolts apart, and doesn't say to do Plastigauge checks with the old bolts. It gives no rod-bearing oil-clearance figure to compare the Plastigauge reading against. | BMW warns that not following the M10 procedure "will result in serious engine damage". The rod-bearing job exists to save the engine. A Plastigauge reading with no target figure tells the reader nothing. | **Yes for the bolts:** `torque_specs.md` Q2 (SI B11 04 04, read) and Q3 (ARP's own procedure: stretch measurement, rods re-sized). **No for the clearance target:** neither the notes nor I found a BMW figure. A tuning-shop page quotes about 0.001 in (snippet). | Replace both rows with the SI procedure. **M11, 12-point head (12 mm socket):** reuse each bolt in its own hole, 5 Nm, 30 Nm, 70° in one pull. **M10, E-Torx head (E12):** new bolts, three cycles of 5/30/105° with about one turn of release between. Identify the bolts by their heads, not the build date. Plastigauge with the old bolts and fit new ones only for final assembly. Add the BMW clearance figure from TIS 11 24 before the reader buys bearings. Note that ARP bolts follow ARP's sheet and the rods should be re-sized. |
| B2 | Phase 11 step 2; "Harness and re-pinning" → pin table; Troubleshooting | **The re-pin table is wrong for this car.** Its first row (four wires from X60004 to X6011) is one poster's from-memory description of his earlier MS42-to-MS43 M54 swap in a 1998 323i, not an S54 swap. For an S54 going into an MS43 Touring the moves run the other way. These moves are missing: brake-light test signal 28→34; DM-TL heater into 18 (MS43: from X6011-7; MS45: from pin 2); MS45 pins 5, 15 and 19 to be removed (a leftover wire on pin 5 would land on an MSS54 ground); clearing pin 23; and the cluster lamps. On MS45 cars the oil-pressure lamp needs a wire from X60004-11 to cluster X11175 pin 13, with "oil pressure via CAN" coded off. The charge lamp (1→2) and oil level (21→17) are wired or coded. The guide does mention the gear-switch path to X60002-20. It doesn't cover the E-box sub-connectors: the mini fuse box, the 3-pin plug with the heavy DME-relay feed, and the X6053/X60531 pair whose mismatch gave injector-circuit-low codes in one swap. | Phase 12 primes the oil "until oil pressure shows". Without the lamp wired, a freshly rebuilt S54 is cranked and started with no oil-pressure signal. A wrong DM-TL connection stops the EVAP monitor, which fails plug-in inspection. Brake-switch pins affect cruise and plausibility checks. This reader can't work this out without good data. | **Yes:** `harness_engine_side.md` Q1–Q2 (X60004 table and move lists for MS43 and MS45 Tourings), Q4 (pin 5 ground, E-box housing), Q6 (verify with an ohmmeter, load the right VIN). Also `harness_body_functions.md` §1, §4, §5, §8. | Replace the table with the two move lists (MS43 Touring to 02/2003, MS45 from 02/2003). Add an E-box sub-connector checklist. Add a pre-power step: ohm-check each moved circuit end to end, and read diagrams with the Touring's VIN loaded for the body side. Mark the pin data as coming from Kassel, forum posts and a community WDS copy. For first start, also fit a mechanical oil-pressure gauge (see I19). |
| B3 | "Fuel system" step 4; Phase 11; Phase 12 step 4; Troubleshooting; "Open questions" | **The fuel-pump trigger is unresolved.** The guide says to "work out the pump trigger before the first start" and leaves it as an open question. Its description of the US M3's PWM pump module invites wiring that PWM output to the Touring's mechanical relay. | First start depends on it. A 0–120 Hz PWM signal on a relay coil is the likely cause of chatter or relay failure. The reader has no way to settle it from the guide. | **Yes:** `fuel_pump_control.md` §1–§2. The US MSS54 also drives a non-US relay output on X60004 pin 10, which is the pin the MS43 (and the MS45.1) uses for the pump relay, K96 on the Touring. On an MS45 car, confirm the pin. Documented swaps change nothing in the pump wiring and get a stored EKP/pump-relay fault that doesn't light the check-engine lamp. Never put X60002-11 (PWM) on a relay. | Replace step 4 and the open question with that answer. Add a check: with a meter and the Touring's WDS, confirm X60004-10 reaches the K96 relay's SW/VI wire. Say that a stored fault is expected. For strict states, add the options: fit the M3 EKP module, or have the vendor code the fault out. |
| B4 | Parts list → Electronics (DSC, brake master cylinder); Phase 2 step 6; Phase 8; Phase 11 step 3; "DSC and steering angle" | **The DSC and brake plan is unproven and incomplete.** The guide says to transplant the donor's DSC unit with its master cylinder. In one documented S54 Touring, an M3 MK60 never cleared "VIN not initialized" and the DSC light stayed on; refitting the Touring's own 325i MK60 fixed it. A second S54 wagon ran on both. The guide doesn't consider MK20 donors (built before about 09/2002). It never mentions the **brake booster**: in ETK the M3's booster (34332282193 to 09/2002, 34332282622 from 09/2002) and master cylinder (34312282343 / 34317838638) appear only on S54 cars, and the Touring has its own (booster 34336779682, master cylinder 34316752541). The M3's **front brake hose** (34322229723) and front pipes (34322282275/277) are M3-only too. | These are safety systems. Following the guide, a reader can finish with ABS and DSC lights on and no documented fix. Or they can end up mixing a master cylinder and booster that may not belong together, and discover missing hoses only at assembly. | **Partly:** `coding_body_chassis.md` §5 and `harness_body_functions.md` §7 cover choosing a unit, the coding parameters (C12 rules key on `S54B32`/`TOUR`), VIN and steering-angle initialization, and INPA pump bleeding. **Not covered:** the booster, master cylinder and hose part numbers. I checked those in ETK for this review. | Present two options. **A:** keep the Touring's MK60, booster and master cylinder, fit M3 front hoses, and code toward M3 values with care. **B:** M3 MK60 plus M3 master cylinder, adding the M3 booster if the M3 cylinder doesn't suit the Touring booster (not verified by anyone), coded by the FA or FSW_PSW route in the notes. With an MK20 donor, use A. Keep the Touring's DSC, booster and master cylinder until the car passes inspection. Add an ABS test (careful hard stop on a quiet road) and a re-bleed after the first drives. |

---

## 2. Important gaps

These would trip up this reader, cost time or money, or risk an inspection failure. They are in roughly build order.

| # | Where in the guide | What's missing | Why it matters for this reader | Covered by the new research notes? | Suggestion |
|---|---|---|---|---|---|
| I1 | Intro; "Tools, space and software"; whole guide | **No factory documentation is named or linked.** There is no newTIS/TIS, no WDS link and no Bentley. The guide says only "BMW's repair and wiring documentation". | The guide sends every standard procedure and most torques to "the factory manual". The reader needs to know which source covers the S54 and the 325iT, and how to get wiring diagrams for an exact VIN. One Touring swapper found the diagrams changed once his VIN was loaded. | **Partly:** `harness_engine_side.md` Q6 (wrong-VIN diagrams and a misleading Bentley page). The notes' researchers couldn't open newTIS because of Cloudflare, but it works in a normal browser. | Add a "Documentation" box: newTIS (newtis.info) for repair instructions, torque tables and WDS by VIN (load the Touring's VIN for the body side and the donor's for the engine side). Add the Bentley E46 manual; a seller listing says it covers the 2000–05 M3 (snippet). Add the Flow E46 M3 torque PDF as a cross-check. |
| I2 | Phase 0 steps 3–4; Tools → Electrical | **No setup steps for the coding kit, and the order is wrong.** Phase 0 asks for scans and backups before the reader has a working laptop, cable and software, and never says how to back up. | Most failures to read the cluster, LCM or DSC come from pins 7/8 not bridged on the cable, the wrong COM port, or an INPA build without MK60 steering-angle calibration. PA-Soft needs its own interface, and its driver is the step most likely to fail on Windows 10/11. The software circulates unofficially. | **Yes:** `coding_body_chassis.md` §1 (install steps, pins 7/8, COM1 and `obd.ini`, latency, PA-Soft interface, INPA versions, Tool32 OCX fix) and §2 (read and save FA/ZCS and `FSW_PSW.TRC` for every module before changing anything). | Add a first Phase 0 step: build and prove the coding laptop on the unmodified Touring. List the hardware, then the backups: cluster and LCM EEPROMs with PA-Soft; FA or ZCS (with screenshots of options, production date and type code); `FSW_PSW.TRC` for KMB/AKMB, LSZ/ALSZ, GM5, DSC, EWS and IHKA. Say plainly that the software comes from forums, not BMW. |
| I3 | Phase 0 | **The reader's own shell isn't checked:** no look at the RACP (cracks above and below the mounts), rust at the arches, sills and jacking points, or whether the car has an M54 rather than an M56 SULEV. | A badly cracked RACP changes the plan; BMW's 21 kg repair panel 41117000246 is reported discontinued (snippet). An M56 car has a pump controller, a metal tank and no return line, so the M3 filter-regulator plan wouldn't apply. | **Partly:** `touring_subframe_reinforcement.md` §1, §6; `fuel_pump_control.md` §3 (BMW's bulletin put the M56 only in automatics, so a 5-speed should be an M54; confirm anyway). | Add to Phase 0: inspect the RACP using CMP's criteria, check rust, confirm engine code M54B25 and a plastic tank. |
| I4 | Phase 1 step 5; Phase 2 | **No list of tests and measurements to do while the donor still runs.** | Once the donor is cut up there's no way to prove the A/C, DSC, gearbox synchros, diff, fuel pressure, VANOS or pump module. You also lose the best reference for Phase 6: where the M3's arch and fender lips sit relative to the hub at M3 ride height. | **Partly:** `coding_dme_ews.md` §1 (save DME faults, hardware number and AIF before shipping the DME); `coding_body_chassis.md` §3 (read the M3 cluster EEPROM); `fuel_pump_control.md` §4 (pressure spec). | Add a "before teardown" list: INPA module IDs and faults; DME IDENT and AIF; cluster EEPROM; Tool32 VANOS jobs; fuel pressure; A/C operation; road-test notes; photos of the B-pillar tire placard and the underhood A/C and emissions labels; **hub-centre-to-arch-lip height and lip position outboard of the tire at all four corners**. Book A/C recovery while the donor can still be moved. |
| I5 | Phase 2 (strip the donor) | **Harvest items are missing.** The step list never removes the front axle and steering parts (they appear only in the "drop the subframe with the engine" option). Also missing: M3 front brake hoses and pipes (B4); the M3 trunk-floor muffler brackets and front reinforcement; the M3 push rod and V-brace; rear wheel-arch liners; the M3 clutch-switch module and the gearbox gear-identification switch; the E-box mini fuse box and 3-pin plug; the M3 fuel lines; and the booster (if option B). | Missing parts turn up months later, after the donor shell is gone. | **Partly:** `touring_subframe_reinforcement.md` §4–§5 (41122494844, 41112493931, 51717894229, push rod 33312229295, V-brace 33312229899); `harness_engine_side.md` Q1 (fuse box, 3-pin plug); `harness_body_functions.md` §5 (clutch module 61319122700, gear switch 23142229113); `fuel_pump_control.md` §5 (M3 lines). | Turn Phase 2 into a checklist that follows the parts list, add the items above, and add draining and disposing of fluids. |
| I6 | Phase 3 (clutch, flywheel); Phase 9; Appendix; Parts list → Engine | **Flywheel torque is missing** ("use BMW's S54 figure", with an incorrect remark that 105 Nm is only the M54 value). Pressure-plate screws aren't identified as the M3's 10.9 grade. The front reinforcement plate has no torque. The parts list has no pilot bearing or fastener kits. | Phase 9 can't be finished without them, and all of these are single-use fasteners. | **Yes:** `torque_specs.md` Q1 (TIS: 105 Nm, eight new M12×1.5×50 bolts 11222243051, threads oiled, no thread locker), Q4 (M3 pressure-plate screws are M8 10.9 micro-encapsulated: 34 Nm, new screws), Q2 (reinforcement plate: new M10 screws, 59 Nm + 90°, from the SI). | Add the rows; add pilot bearing 11211720310, flywheel bolts and pressure-plate screws 21207548052 to the parts list. |
| I7 | Phase 12 step 6 | **Break-in advice contradicts BMW.** The guide says to drive gently for 300–500 miles. BMW's rod-bearing SI says 1,200 miles below 5,500 rpm after new bearings. | The rod bearings are the reason the engine was opened. | **Yes:** `torque_specs.md` Q2 (SI B11 04 04). | Use the SI figure. Suggest an oil change at the end of break-in (a recommendation, not a BMW source). |
| I8 | Parts list; Phases 3, 7, 9, 10, 12 | **No fluids or capacities anywhere:** engine oil grade and quantity, 420G oil, M-differential oil (a friction-modified LSD oil), power-steering fluid, coolant, brake and clutch fluid, refrigerant. | Ordinary gear oil in the M variable diff or the wrong gearbox oil risks damage, and the reader needs quantities to buy fluids. | **Partly:** `torque_specs.md` Q2 (10W-60; 6.5 L after the rod-bearing job, 5.5 L for a normal service, from the SI). Nothing else is covered. | Add the fluids table in section 6.1. |
| I9 | Appendix → Torque values; Phases 7–10 | **The torque table covers only the driveline and rear subframe.** Missing: wheel bolts; hub collar nuts; the front axle (subframe, control arms, brackets, ball joints, strut clamp bolts, top mounts); steering (rack, tie rods, lower joint); brakes (carriers, guide bolts, lines, master cylinder); rear arms, dampers and anti-roll bars; engine and gearbox mounts; bellhousing; starter; slave cylinder; oil drain, filter and cooler; the fan clutch (left-hand thread); exhaust and O2 sensors. The guide also doesn't say that front bushing joints are tightened at loaded ride height too. | These are safety-critical, many fasteners are single-use, and the reverse-thread fan clutch is a classic trap. | **Partly:** `torque_specs.md` Q2 and Q4 (SI and driveline values); `touring_subframe_reinforcement.md` §5 (V-brace 59 Nm + 90°, push-rod cradle 25 Nm, from PS Designs/Redish). | Add the extended table in section 6.2 (Flow compilation, read; mark it as compilation-sourced and to be confirmed in TIS). |
| I10 | Phase 5; "Exhaust and the spare-wheel well"; "Rear subframe mount reinforcement" | **The well cut and the reinforcement are separate steps.** The guide doesn't warn against cutting through the rail-to-RACP flanges within about 120 mm of the rails. It doesn't use the well opening to reach the rosette welds. It closes the floor before the M3 axle and muffler are mocked up, even though the flat-panel option sets the floor "at the height the muffler needs". | Mistakes here weaken the very structure being reinforced, and a floor at the wrong height means the exhaust won't fit. | **Mostly:** `touring_subframe_reinforcement.md` §2, §4 (cut plan, topside welds through the opening, M3 floor as first choice, flat-panel rules, hang the muffler from the outer underbody). **No** on the muffler mock-up order. | Make Phase 5 one sequence: open the well → topside welds and rail plates → test-fit the M3 axle and muffler (or close the floor during the Phase 6 mock-up) → close and seal the floor. |
| I11 | "Rear subframe mount reinforcement" → kits table and step 9 | **Cargo-side work on a Touring is under-specified.** No Touring-specific cargo-side plates or instructions exist. CMP's Stage 1, 1.5 and 2 kits list the Touring; CMP's front beam and the Rogue and Turner top-side braces don't. The guide also says the Touring floor is "slightly different", which ETK contradicts. | Step 9 tells the reader to "dry-fit any cargo-side plates", which don't exist for the Touring. | **Yes:** `touring_subframe_reinforcement.md` §1–§3, §6 (same RACP and trunk floor as the sedan; seam reference; BMW foam fix and its limits). | Fold in; correct the floor claim. |
| I12 | Parts list → Rear axle; Phase 7 | **The M3 push rod and V-brace are absent.** The tubular push rod (front crossmember, 33312229295) isn't mentioned, nor the M3-only V-brace (33312229899), nor the reinforcement kit's spacer plates under the push rod. Nobody knows whether a Touring body has the V-brace mounting points. | The M3 subframe goes in with its push rod, and the V-brace is part of rear-axle bracing the Touring body lacks. | **Yes:** `touring_subframe_reinforcement.md` §5. | Add both parts. Check the rails for threaded M10 points before planning on the V-brace, and keep the kit's spacer plates. |
| I13 | Phases 5–6; Tools → Body; Tools → Safety | **No welding parameters or welding safety.** No wire, gas or settings for 0.8–1.2 mm skins against 1.5–2.5 mm plates. No fume protection, though the plates are zinc-coated and weld-through primer is zinc-rich. No fire watch. No mention of fuel-vapour parts near the right-rear arch: ETK lists a fuel expansion-tank bracket among the rear wheelhouse parts. | This reader has MIG'd sheet but never plug-welded 1.5–2.5 mm plate to a thin double-skin floor overhead. Zinc fume causes metal fume fever, and undercoating and seam sealer smoulder. | **Partly:** `touring_subframe_reinforcement.md` §2 (CMP rail plates are 2.5 mm zinc-coated steel), `convertible_arch_steel.md` §5 (LBL arch sections 1.2 mm, snippet). No settings or safety. | Add Miller's guidance: 0.023–0.024 in wire for body panels up to 1/16 in; 0.030 in for 20 gauge to 1/8 in (likely better for the plates); 75/25 argon/CO2; start from the welder's door chart; spot and stitch on panels (read). Measure the real panel gauge at a cut edge. Weld test coupons of the same thicknesses and break one. Use local fume extraction or a respirator (OSHA fact sheet: zinc fume, metal fume fever, local exhaust; read). Keep a fire watch. Remove every fuel and EVAP component near the right-rear arch before welding there. |
| I14 | Phase 6 steps 1–2; "Suspension for Touring weight" | **No ride-height target, no way to load a stripped shell, no bump-clearance method, no spring or damper choice.** The guide says to "set the target ride height with the suspension loaded" and to leave "clearance for bump travel", but not how or to what. Spring and damper choice is left to "ask the vendor". | The arches are cut and welded permanently around this mock-up. Final springs, dampers, wheels and tires must be bought before Phase 6. | **No.** | Make choosing springs and dampers a Phase 1–3 decision. Use the donor's measured hub-to-lip heights (I4) as the target. Set each corner by jacking the hub to that height with the spring out, then check full bump with the bump stop compressed and the tire fitted. Check left/right symmetry from the centre line. List the documented choices (KW, Bilstein PSS10) and ask vendors for Touring rear rates. |
| I15 | "Rear arches and doors" → steel sources; "Open questions" | **The steel-source picture is incomplete.** The guide says BMW lists new M3 quarters only for the coupe and CSL. BMW also lists M3 convertible quarters (41357894541/542), and the arch region is very likely the same pressing. A convertible donor yields the whole outer skin back to the tail-light (no C-pillar, which a Touring doesn't need) but takes more spot-weld drilling. Generic coupe/convertible arch repair panels exclude the M3; LBL Panels makes M3 arch sections (snippet). | Many cheap donors are convertibles, and the open question leaves the reader unsure whether that steel is usable. | **Yes:** `convertible_arch_steel.md` §1–§5. | Fold in. Add the cheap check before cutting: a profile gauge or cardboard template at 3–4 stations across both flares. |
| I16 | Phase 7 step 1; Parts list → Fuel; "Fuel system" | **The fuel line fittings differ.** The M3 filter-regulator uses quick-disconnect high-pressure lines; the Touring's are barb-and-clamp. The M3 chassis lines (16122229410 front feed, 16122229409 rear feed, 16122229411 return) or adapters aren't listed. Feed and return swapped caused one swap's no-start. The guide says a donor pump "isn't a confirmed fit", but the M3 pump and M3 baffle have been fitted to sedan tanks, and the sedan tank is the same part as the Touring's. No test numbers are given. | Phase 7 stalls without the right lines, and the cautious wording pushes the reader toward keeping a possibly weak pump. | **Yes:** `fuel_pump_control.md` §4–§5 (no confirmed adapter exists). | Add the M3 lines or a fitting plan, a feed/return check, and the test: 5.0 ± 0.2 bar static, above 4.5 bar after 20 minutes, at least 1.12 L in 30 s at 12 V (Bentley, quoted in the notes). Add the tools: gauge, adapter, relay bypass. |
| I17 | "Instrument cluster and mileage"; Parts list → Electronics | **The cluster procedure is too thin.** PA-Soft can't write VIN or mileage to a used cluster over OBD. The documented route is a new M35080 chip carrying an image with the odometer zeroed and the Touring's VIN, with the gauge needles removed and re-zeroed. The rear-door LEDs have to be added (M3 clusters lack them). The backlight wire depends on 09/2002. The speedo remark is wrong: the M3 cluster over-reads about 8.9% by design, not because of a non-M diff. Pre-09/2001 (ZCS) Tourings may not push mileage from the light module. The tools needed (hot air, a programmer like the R270) aren't listed. | This is how the car shows its legal mileage (49 U.S.C. §32704) and clears the tamper dot and DSC lights. | **Yes:** `coding_body_chassis.md` §3–§4 (procedure, coding index, parameters, services, ZCS caveat). | Fold in, and offer the service route: send the cluster to a vendor named in the notes with the Touring's VIN and the light module's mileage. Keep before/after screenshots and photos. |
| I18 | "Immobilizer (EWS)"; Phase 3 step 3; Phase 11 step 4; Budget | **The EWS section is out of date and misleading in places.** RPM's delete is now $300 (Kassel: delete $109, VIN $20, swap coding $349). The guide implies a used donor DME can be synced; BMW burns the rolling-code table into the DME, so only a virgin (BDM-cleared) DME syncs. The Tool32 AIF procedure for writing the Touring's VIN into the DME is missing. So is the fact that an SMG donor's DME needs manual-gearbox software. | Phase 11 step 4 sends the reader down a route that can't work with a used DME. Inspection reads the DME's VIN. | **Yes:** `coding_dme_ews.md` §1–§5. | Fold in. Reword step 4 as "sync only a virgin DME". Add the AIF write procedure and the SMG-to-manual options. |
| I19 | Phase 12 steps 2–4 | **The first-start procedure is skeletal.** There's no adaptation reset or throttle self-test. Oil priming relies on the cluster lamp, which depends on B2; there's no mechanical gauge and no disabling of ignition and injection while cranking. There's no check of the clutch and gear-switch chain, and no fuel-pressure gauge in the tool list. | A rebuilt S54 deserves proven oil pressure before it fires. The MSS54 needs `ADAPT_LOESCHEN` and its throttle learn. A wrong clutch chain causes rev and idle problems. | **Mostly:** `coding_dme_ews.md` §5–§6 (first-start sequence with Tool32 jobs, throttle pre- and post-drive checks, VANOS tests, crank-wheel adaptation); `fuel_pump_control.md` §4. **No** on the gauge. | Add the sequence. Prime with the pump fuse out and injection and ignition disabled, and watch a mechanical gauge at the pressure-switch port (an adapter is needed; the switch is M12×1.5, 27 Nm). Limit cranking bursts and keep the battery on a charger. |
| I20 | Phase 12 step 5; "DSC and steering angle" | **Alignment comes in the wrong order and without numbers.** No alignment specs, no loading condition, and the steering-angle sensor is calibrated before the alignment; BMW requires the adjustment after any steering or suspension work. | Expect a crooked wheel and DSC faults or false interventions. | **Partly:** `coding_body_chassis.md` §5 (BMW DSC III training on when the sensor must be adjusted). No specs. | Align first, then calibrate the sensor and run the compensation routines. Add BMW's E46 M3 alignment table (section 6.3) and the loaded condition; brief the shop to align at the car's actual loaded ride height. |
| I21 | Phase 12 step 6; "Inspection readiness" | **The readiness advice is generic.** The MSS54's DM-TL leak test runs with the engine off, after at least 20 minutes of driving that followed a 5-hour cold soak, with 15–85% fuel, −7 to 35 °C ambient and 11.5–14.5 V, and only every second time those conditions are met. EVAP is the monitor reported not ready on MSS54 swaps. | Plug-in tests depend on readiness; New York fails a MY2001+ car with more than one monitor not ready. | **Yes:** `coding_dme_ews.md` §7 (MSS54 plan and Tool32 system checks). | Fold in the MSS54-specific plan. |
| I22 | Phase 4; Phase 10; Phase 12 | **A/C on the Touring isn't covered.** The Touring's refrigerant must be recovered before its compressor and lines are opened (the guide covers only the donor). There's no plan for capping open lines, replacing the drier and O-rings, or evacuating and charging at the end, and no charge amount. | Venting refrigerant from a car A/C system is prohibited (EPA, read). A system left open for two years needs a new drier. | **No.** | Have a shop recover both cars before teardown. Cap all openings. Replace the drier (64538377330 / 64536917658; the same parts on both cars, as is condenser 64538377614 (ETK, read)) and O-rings. Have a shop vacuum-test and charge by weight from the underhood label after first start. |
| I23 | Phases 1–13 | **Only Phase 0 has a "Done when".** No phase gives checks, expected readings or a "what if it fails" step, apart from the electronics troubleshooting table. | An amateur needs to know a phase worked before burying it under the next: welds before sealer and paint, wiring before first start. | **Partly:** the notes supply many checks (fuel pressure, INPA status jobs, a generic CAN resistance, readiness). | Add the "Done when" lines from section 4. |
| I24 | Plan and budget → Time, Tools/space, Budget | **No space or logistics plan.** Two cars, a stripped shell, an engine on a stand, two axle assemblies and panels must be stored for 18–30 months. Nothing covers getting rid of the donor shell and its title, or insurance and registration for a Touring off the road. The budget leaves out tools and equipment, laptop, cables and programmer, shop services (A/C twice, alignment, exhaust, inspection referee), M3 fuel lines, a cluster service, topside reinforcement plates and a contingency. | These decide whether a home-garage amateur can start and finish. | **No.** | Add a "Space and logistics" box: strip the donor fast, then scrap or sell the shell with its title, using dollies, a stand and wall racks. Add the missing budget rows as estimates. |
| I25 | Paint, A/C, alignment, DME flash, exhaust, welding (throughout) | **No briefs for the shops it suggests using.** | The guide recommends shops for paint and reinforcement and mentions A/C, alignment and flashing, but doesn't say what to ask for. | **Partly:** `coding_dme_ews.md` §1 (what to order and decline from a DME vendor), `coding_body_chassis.md` §3 (cluster services). | Add a short brief per shop. **Paint:** what you've prepped, colour, jambs and engine bay. **A/C:** recover now, charge by label later. **Alignment:** M3 table at loaded height; you'll calibrate the steering-angle sensor afterwards. **Exhaust:** keep the M3 cats and O2 sensors; hangers from the M3 brackets; clearance to floor, tank and tires. **DME:** EWS delete plus VIN only, manual software, no emissions deletes. **Cluster:** VIN and mileage from the light module. **Welding:** Touring cargo side, fuel lines removed. |
| I26 | Phase 9 step 5; Phase 12 step 2 | **No bleeding methods.** E46 clutches are notoriously hard to bleed after a dry install, and the guide gives no method or tool. A dry or used DSC unit needs INPA's pump routine. | A spongy clutch or air trapped in the DSC unit stops the shakedown. | **Partly:** `coding_body_chassis.md` §5 (INPA bleed for MK60, about 1.25 L of fluid, re-bleed after driving). Clutch: no. | Add a pressure bleeder, and bench-bleeding the slave cylinder with the bleeder up while pushing the piston (forum method, snippet), or a slave-bleed tool. Point to TIS group 21 52. |
| I27 | Phase 3 (gearbox) | **The 420G gets no inspection or service while it's out.** Missing: oil (MTF-LT-2, 1.9 L); seals (input 35×52×7, 23121228493; selector 15×21×6.5, 23127501582; output 52×68×8, 23121222769); the gear-identification switch needed for cruise; and a clutch alignment tool in the tool list. | Cheap now, a gearbox-out job later. | **Partly:** `harness_body_functions.md` §5 (gear switch 23142229113). | Add a gearbox line to Phase 3 and the seals to the parts list (ETK via Flow p.74, read). |
| I28 | "Cooling and oil cooler"; Phases 10, 12 | **No coolant specification or procedures:** no spec or capacity, no bleeding procedure, no pressure test, and no warning that the fan clutch has a left-hand thread. | Air pockets can overheat a fresh engine, and the fan nut defeats people who don't know. | **Partly:** `harness_body_functions.md` §2, §8 (fan pins unchanged; radiator-outlet sensor, coolant-level and washer sensor leads may need extending). No coolant spec. | Add BMW coolant mixed 50/50 with distilled water and bled at the expansion-tank bleed screw with the heater on full (forum, snippet). Pressure-test to the 2 bar system pressure (Flow p.60, read). Note the fan clutch: 40 Nm, left-hand thread (Flow p.61, read). Get the capacity from TIS; I couldn't source it. |
| I29 | Registration and legal (US); "Immobilizer"; "Inspection readiness" | **California is missing**, and it's the strictest and largest market. Every engine change there needs an initial BAR Referee inspection and a Referee label; bringing the donor's VIN helps, and the test follows the donor vehicle's requirements. Since 19 July 2021 Smog Check has failed "Modified Software" that doesn't match an OEM or CARB-approved configuration, which bears on the guide's "simplest" EWS-delete flash. | A California reader could build the car around a DME flash that blocks registration. | **Partly:** `coding_dme_ews.md` §4 (California reads the DME's VIN; mentions Cal ID/CVN); `fuel_pump_control.md` §2 (a reported California failure for a detected tune). | Add a California paragraph (BAR pages, read). Tell readers in any state that checks software to ask whether a VIN-matched EWS-delete flash passes before choosing between delete, virgin-DME sync and donor EWS. |

---

## 3. Nice-to-have

| # | Where in the guide | What's missing | Why it matters for this reader | Covered by the new research notes? | Suggestion |
|---|---|---|---|---|---|
| N1 | Phase 0 step 1 | It says "confirm it's not an xi" but not what breaks if it is (the owner called the car a "325x"). | Avoids a wrong plan from day one. | **Partly:** `coding_body_chassis.md` §5 (xi cars use Bosch DSC 5.7). | Add the short box in section 5. |
| N2 | "Choose the donor" → Check before you pay | No compression or leak-down figures, and no tools for those tests in the list. | The reader can't judge the results. | **No.** No S54 figure found; an M54 figure of 10–11 bar minimum and 0.5 bar maximum spread was seen for a different engine (snippet). | Add the testers; judge evenness across cylinders; get the S54 figure from TIS. |
| N3 | Phase 2 step 9; Phase 4 step 4 | It doesn't say what to sell or when. | Selling the Touring's DSC, booster, master cylinder, cluster or clutch switch too early removes the documented fallbacks (B4, I17). | **No.** | List what's safe to sell early: M54, 5-speed, MS43/45 DME and harness, 325i axle parts, Touring front panels, donor interior and glass, convertible top. Hold the fallback parts until inspection is passed. |
| N4 | Phase 4 step 2 | It doesn't say how to drain the Touring's saddle tank before dropping it. | Fuel handling is a fire hazard. | **No.** | Run the pump through a relay bypass into approved cans, or pump it out; store the fuel safely. |
| N5 | Phase 6 step 3 (right-side filler) | The M3 filler flap and pot move about 25–30 mm outboard; nothing checks that the Touring's filler neck still reaches and seals. | An EVAP leak fails the DM-TL test. | **Partly:** `convertible_arch_steel.md` §1 (filler pot 51718208646 is the same on both M3s; flap hinge differs between coupe and convertible). | Add the check. |
| N6 | Parts list → Body | No rear wheel-arch liners for the widened arches. | Liners keep spray off the new seams. | **Partly:** `convertible_arch_steel.md` §1 and gaps (the M3-only "coverings" 51712695667/51717895936 may be the rear liners; unconfirmed). | Add, as to be confirmed. |
| N7 | Phase 12 step 1 | Headlight wiring and coding aren't covered when the cars differ (halogen vs xenon, levelling sensors, light-module coding), and neither is headlight aim. | Lights and aim are inspection items. | **No.** | Add a check, and aim the headlights after the front end goes on. |
| N8 | Phase 7 step 3 | No parking-brake shoe adjustment or bedding-in for the M3 drum-in-hat brakes. | Inspection item. | **No.** | Point to TIS or Bentley group 34 41. |
| N9 | Parts list → Electronics (Sport button) | Sport button wiring and the M Track coding aren't explained. | Optional, but the guide raises it. | **Yes:** `harness_body_functions.md` §3 (X60004 15/16 to switch-centre X1869 17/18; M3 switch unit 61316925520; M Track via MK60 coding). | Fold in. |
| N10 | Phase 11 | Cruise control needs the M3 clutch-switch module and the gear-switch chain. | Otherwise cruise doesn't work, as one Touring found. | **Yes:** `harness_body_functions.md` §5; `coding_dme_ews.md` §5. | Fold in. |
| N11 | Troubleshooting → A/C | A/C with manual climate control (IHKR) is unconfirmed with the MSS54. | Know early. | **Partly:** `harness_body_functions.md` §6. | Test A/C early on IHKR cars. |
| N12 | Phase 11 | No bus or continuity checks before first power-up. | Catches pinning errors safely. | **Partly:** `harness_body_functions.md` §7 (about 60 Ω across CAN at OBD pins 6/14; a generic figure). | Add. |
| N13 | Tools → Electrical | Depinning keys and terminals aren't specified. | The wrong terminal family damages factory housings. | **Partly:** `harness_engine_side.md` Q6 (ETK terminal part numbers; buy pre-crimped repair leads). | Add. |
| N14 | Phase 11 | Some sensor leads (coolant level, washer level, radiator outlet) may not reach the M3 parts. | Small but stalls first start. | **Partly:** `harness_body_functions.md` §2, §8. | Add. |
| N15 | S54 refresh → rod bolts | ARP bolts are mentioned without ARP's stretch values or the rod re-sizing step. | Readers often choose ARP. | **Yes:** `torque_specs.md` Q3. | Fold in. |
| N16 | Phase 5 | No body measurements before and after welding. | Plates welded to a thin floor can pull. | **No.** | Tape the diagonals between the four rear subframe mounts (and the front subframe points) before and after; BMW body dimensions are in TIS group 51 00. |
| N17 | Phase 10 step 3 | No heat shielding is mentioned for the muffler at the new floor or near the tank, cargo area and battery. | Heat damage, smell, or a fire risk. | **Partly:** `touring_subframe_reinforcement.md` §4 (hang the muffler from the outer underbody). | Fit the M3 floor heat shields or make shields. |
| N18 | Phase 12 | The fuel gauge with an M3 cluster reading the Touring's senders isn't checked. | A wrong gauge strands you. | **No** (no source either way). | Check the gauge and range against a known fill. |
| N19 | Phase 13 step 4 | No pre-inspection safety checklist. | Avoids a failed first inspection. | **No.** | Lights and aim, horn, wipers, ABS, DSC and airbag lamps out, tires, exhaust leaks, rear reflectors kept on the modified bumper. |
| N20 | Tools → Lifting | No warning that the centre of gravity shifts when the engine or rear axle comes out. | A car can tip off a two-post lift. | **No.** | Strap or support the car, and move the arms when mass comes out. |
| N21 | Figures and photos | No openly licensed underbody or subframe photos exist. | The reader relies on diagrams and vendor photos. | **Yes (a negative finding):** `photos_openly_licensed.md` Q7. | Keep linking vendor photo instructions (Garagistic, BimmerWorld, CMP). |
| N22 | Several sentences | Statements the notes contradict (see section 7). | Accuracy. | **Yes:** each notes file. | Fix while folding in. |

---

## 4. Phase-by-phase readiness

"Ready" means this reader could do the phase with the guide plus the factory manual. The last column is a proposed "Done when" line for each phase (gap I23).

| Phase | Status | Reason | Proposed "Done when" |
|---|---|---|---|
| 0 Paperwork and baseline | Needs work | Asks for scans and backups before the coding kit exists, never says how to back up, skips the own-shell inspection and doesn't name the factory manual (I1–I3). | The coding laptop reads every module on the Touring; FA/ZCS, module codings and the cluster and LCM EEPROMs are saved; RACP and rust inspected; the state's answer is in writing. |
| 1 Buy and inspect the donor | Ready, with small additions | The checklist is sound; it lacks a compression spec and test tools, and a before-teardown test and measurement list (I4, N2). | Compression/leak-down, VANOS, faults and module IDs recorded; hub-to-lip heights measured; placard and labels photographed; title in hand. |
| 2 Strip the donor | Needs work | The front axle and steering aren't in the steps; several M3-only parts aren't harvested; no fluid or A/C timing; no shell or title disposal (I5, I22). | Every parts-list line removed, tagged and stored; shell and title disposed of. |
| 3 Bench work | **Blocked** | Wrong M10 rod-bolt procedure; no bearing-clearance target; no flywheel torque (B1, I6). The notes fix the bolts and the flywheel. | Clearances recorded and within the TIS figure; bolts tightened per the SI; Beisan VANOS checks passed; 420G resealed and filled; DME back from the vendor and the flash verified by re-reading. |
| 4 Strip your Touring | Needs work | No Touring A/C recovery and no fuel draining; "sell the M54 parts" should hold back the fallback parts (I22, N3, N4). | Shell stripped, A/C recovered, fuel and tank out and stored safely. |
| 5 Metalwork 1 | Needs work | No weld settings or fume safety; the Touring cargo side and the well-cut sequence need the notes; the floor is closed before the muffler mock-up (I10, I11, I13). | Test coupons pass; topside welds and plates done; floor closed after the axle and muffler fit check; diagonals unchanged; all seams sealed and waxed. |
| 6 Metalwork 2 | Needs work | No ride-height target, loading method, bump check or spring choice; the steel-source questions need the notes (I14, I15). | Arch lips symmetric left and right; tire clears at full bump; doors open, close and gap correctly; inner lips sealed double-skin. |
| 7 Rear axle and fuel | Needs work | Fuel-line fittings, pump test spec, push rod and V-brace, torques and diff oil missing (I9, I12, I16). | Pump passes 5 bar, hold and flow; no leaks; bushings torqued at loaded height; diff filled. |
| 8 Front suspension and steering | Needs work | No torques beyond the plate; the booster, master cylinder and hose decision is missing; no power-steering fluid (B4, I8, I9). | Every fastener torqued and paint-marked; rack centred; brake lines pressure-tested; no leaks. |
| 9 S54 and 420G | Needs work | Flywheel, pressure-plate, mount and bellhousing torques; clutch alignment tool; clutch bleeding; gearbox oil (I6, I9, I26, I27). | Oil-pan clearance confirmed; clutch pedal firm; driveshaft centre bearing preloaded; gearbox and diff filled. |
| 10 Cooling, intake, exhaust | Needs work | Coolant spec and bleeding; fan-clutch thread; A/C charge plan; exhaust brief and heat shields (I22, I25, I28, N17). | Cooling system holds 2 bar; exhaust clears floor, tank and tires at bump; heat shields fitted. |
| 11 Wiring, immobilizer, coding | **Blocked** | Wrong re-pin table, unanswered pump trigger, unproven DSC plan, thin cluster procedure (B2–B4, I17–I18). The notes fix most of it. | Moved circuits ohm-checked; all modules talk; warning lamps test at key-on; cluster shows true mileage with no tamper dot; DSC coded; only the expected EKP and 0x82 faults stored. |
| 12 Front end, first start, shakedown | Needs work | First-start sequence, oil priming, alignment figures and order, break-in, tire pressures, readiness (I7, I19–I21, I29). | Oil pressure proven on a gauge; 5 bar fuel; idle stable; DSC/ABS tested; aligned, then steering angle calibrated; monitors ready; 1,200-mile break-in done. |
| 13 Paint, trim, paperwork | Needs work | No paint brief, no pre-inspection checklist, no California Referee or software-check path (I25, I29, N19). | Inspection passed; registration and title updated as your state requires; agreed-value policy in place. |

---

## 5. If the car turns out to be a 325xi

The owner called the car a "325x". The guide is written for the rear-drive 325i, and Phase 0 only says to confirm the car isn't an xi. If the VIN decodes as a 325xi Touring, this is where the guide's advice breaks (sources: the guide itself and `coding_body_chassis.md` §5):

- **Front subframe.** The guide's "keep your front subframe" doesn't apply. The xi has its own front axle support, so you need the donor's rear-drive one (31111096902). The Bring a Trailer car shows an xi can be converted to rear-wheel drive.
- **DSC.** The xi uses a Bosch DSC 5.7, not the MK60, so the notes' fallback of keeping the Touring's own unit doesn't exist. You would have to run an MK60 (the M3's or a 325i's) and adapt the DSC wiring. Nobody has documented that in a Touring. The steering-angle job also differs (`DSC57.PRG` → `test_lenkwinkel`).
- **Other xi-only parts** come out: transfer case, front driveshaft and front axle parts. The fuel tank, tunnel heat shields and exhaust hangers were not checked for the xi.

---

## 6. Add to the guide: consolidated lists

Values appear only where I found a source. "Flow" means the "E46 M3 Fasteners Torque Specifications" PDF, a forum compilation built on RealOEM printouts and updated 12 Feb 2024. It is linked from the NAM3 torque thread ([Google Drive](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing), [NAM3 thread](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/414-e46-m3-torque-spec-thread-every-bolt-on-the-car-on-diagrams)). I read its pages as rendered images, and page numbers below are the PDF's. It isn't BMW, so mark these values "compilation; confirm in TIS".

### 6.1 Fluids and capacities

| System | Specification | Quantity | Source |
|---|---|---|---|
| S54 engine oil | BMW-recommended Castrol TWS Motorsport SAE 10W-60 or Castrol Formula RS 10W-60, BMW PN 07 51 0 009 420 | 5.5 L oil change with filter. About 6.5 L after a rod-bearing job (cooler and passages drained). | BMW S54 training text in ST041 "2 M3 DriveLine" (read; same text as the guide's billswebspace module); capacity from BMW ST041 "1 M3 Complete Vehicle" technical data ([archive.org](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle_djvu.txt), read); 6.5 L from SI B11 04 04 (notes: `torque_specs.md` Q2) |
| Getrag 420G gearbox | Genuine BMW MTF-LT-2, 75W-80 GL-4 (83 22 0 309 031); the vendor's fitment list includes the E46 M3 | 1.9 L | Fluid: [BimmerWorld](https://www.bimmerworld.com/Genuine-BMW-MTF-LT-2-GL-4-Transmission-Fluid-1-liter.html) (read); supersession to 83220309031: Turner listing (snippet). Capacity: BMW ST041 (read). Check the label on the gearbox. |
| M variable differential | Genuine BMW SAF-XJ+FM 75W-140 GL-5 with the friction modifier for the M variable LSD (83 22 2 282 583, 500 ml bottles) | 1.1 L oil change; buy three bottles (Turner says 1.2 L) | Fluid: [BimmerWorld](https://www.bimmerworld.com/Fluids/Driveline-Fluids/Genuine-BMW-Differential-Gear-Oil-SAF-XJFM-500ml-bottle-E46-M3-E9X-M3-F8X-M3-M4.html) (read). Capacity: BMW ST041 (read); Turner's 1.2 L (snippet). |
| Power steering | **Not sourced.** Read the cap on the donor's M3 reservoir (ATF or CHF 11S) and don't mix the two. BimmerWorld lists CHF 11S for no E46 model. | Not found | [BimmerWorld CHF 11S page](https://www.bimmerworld.com/Suspension-Steering/Pentosin-CHF11S-Hydraulic-Fluid-BMW-82111468041.html) (read; fitment list and do-not-mix warning) |
| Coolant | BMW coolant, 50/50 with distilled water; system pressure 2 bar | **Capacity not found** | 50/50: forum posts (snippet). 2 bar: Flow p.60 (read). |
| Brake and clutch fluid | **Spec not sourced in this review.** Check the reservoir cap and TIS. | About 1.25 L was used for one INPA DSC bleed (Z4 M MK60) | `coding_body_chassis.md` §5 (notes) |
| A/C refrigerant | Per the underhood label; **charge amount not found** | Charge by weight, from the label | none found |
| Fuel | Premium unleaded | Touring tank stays | BMW ST041 (read) |

### 6.2 Extra torque values

The guide's existing rows still stand, with the corrections in `torque_specs.md` Q4. "New" means fit a new fastener. Tighten every rubber-bushed joint at loaded ride height (Flow p.1 warning; BMW practice).

**Front axle and steering**

| Fastener | Value | Notes | Source |
|---|---|---|---|
| Front axle support (subframe) to body, M12 10.9 | 110 Nm | | Flow p.2 |
| Control arm to subframe, M14 self-locking nut | 90 Nm | New nut | Flow p.2 |
| Control-arm bushing bracket to body, M10 | 59 Nm | New bolts; at ride height | Flow p.2 |
| Ball joint to knuckle, M12 self-locking collar nut | 65 Nm | New nut; no impact wrench | Flow p.2 |
| Front reinforcement plate, M10×35 10.9 | 59 Nm + 90° (±30°) | New bolts | Flow p.2; the same figure from SI B11 04 04 (notes, `torque_specs.md` Q2) |
| Strut top mount to body, M8 collar nuts | 24 Nm | | Flow p.3 |
| Damper rod top nut, M14 | 64 Nm | New nut | Flow p.3 |
| Strut to knuckle clamp bolt, M12×1.5×55 10.9 | 81 Nm | New bolt | Flow p.4 |
| Front wheel-speed sensor bolt | 8 Nm | | Flow p.4 |
| Front anti-roll bar link nuts, M10 | 65 Nm | New nuts | Flow p.6 |
| Front anti-roll bar bracket nuts, M8 | 21 Nm | At ride height | Flow p.6 |
| Steering rack to subframe, M10 | 42 Nm | | Flow p.7 |
| Inner tie rod to rack | 100 + 10 Nm | | Flow p.9 |
| Outer tie-rod lock nut, M14 | 45 Nm | | Flow p.9 |
| Tie-rod end to knuckle, M12 self-locking | 65 Nm | No impact wrench | Flow p.9 |
| Steering lower joint Torx bolts, M8×33 | 22 Nm | New bolts (SI) | Flow p.12; SI (notes) |
| Front hub collar nut (only if hubs are replaced) | 290 Nm | New nut | Flow p.14 |

**Rear axle**

| Fastener | Value | Notes | Source |
|---|---|---|---|
| Rear control-arm bolts at the subframe, M12 | 77 Nm | Loaded ride height | Flow p.16 |
| M12 10.9 bolts at the trailing arm (upper-arm ball joint, eccentric bolt) | 110 Nm | Loaded ride height | Flow p.16 |
| Rear damper lower bolt, M12 | 100 Nm | Loaded ride height | Flow p.17 |
| Rear damper top-mount nuts, M8 | 28 Nm | New nuts. M3 parts; Touring damper mounts not checked. | Flow p.17 |
| Rear damper rod nut, M10×1 | 14 Nm | New nut | Flow p.17 |
| Rear anti-roll bar, links and brackets | 22 Nm | | Flow p.18 |
| Rear drive-flange collar nut, M27×1.5 | 300 Nm | New nut; lightly oil the contact face | Flow p.19 |
| Diff drain and fill plugs | 60 Nm with O-ring; 65 Nm with sealing washer | If the diff's output flanges come out, mark the flange bolt first and reassemble to the mark (bearing preload) | Flow pp.80–81 |
| M3 V-brace bolts (×3) | 59 Nm + 90° | | PS Designs/Redish instructions (notes, `touring_subframe_reinforcement.md` §5) |
| Subframe front support cradle (push rod) bolts (×4) | 25 Nm | Keep the kit's spacer plates | same |

**Brakes and wheels**

| Fastener | Value | Notes | Source |
|---|---|---|---|
| Wheel bolts, M12×1.5 | 120 ± 10 Nm | | Flow p.28 |
| Front caliper carrier, M12×1.5 | 110 Nm | | Flow p.25 |
| Caliper guide bolts, front and rear | 30 Nm | | Flow pp.24–25 |
| Rear caliper carrier, M10 | 65 Nm | Micro-encapsulated screws | Flow p.24 |
| Brake line to caliper | 19 Nm | | Flow pp.24–25 |
| Bleed screws | 7 mm: 3.5–5 Nm; 11 mm: 12–16 Nm | | Flow pp.24–25 |
| Rotor retaining screw | 16 Nm | | Flow p.23 |
| Master cylinder to booster, M8 | 26 Nm | New nuts | Flow pp.26–27 |
| Booster to pedal bracket | 25 Nm | | Flow p.26 |
| DSC pressure sensor in master cylinder | 25 + 5 Nm | | Flow p.27 |

**Engine, gearbox, cooling, exhaust**

| Fastener | Value | Notes | Source |
|---|---|---|---|
| Flywheel to crank | 105 Nm | Eight new M12×1.5×50 bolts; threads oiled; no thread locker | TIS screenshot (notes, `torque_specs.md` Q1) |
| Pressure plate, M8 10.9 | 34 Nm | New screws | notes, `torque_specs.md` Q4 |
| Engine mount nuts, M10 | 45 Nm | | Flow p.54 |
| Engine support arm to block, M8 | 21 Nm | | Flow p.54 |
| Bellhousing Torx bolts | M8: 28 Nm; M10: 52 Nm; M12: 98 Nm | Confirm M12 in TIS: Flow's own general table gives 82 Nm for M12 8.8 | Flow p.72 |
| Gearbox crossmember to body, and gearbox mounts, M8 | 21 Nm | | Flow p.78 |
| Starter, M10 Torx | 45 Nm | Leads: M5 5 Nm, M6 7 Nm, M8 13 Nm | Flow p.77 |
| Clutch slave cylinder nuts | 22 Nm | Line unions 14–20 Nm | Flow p.70 |
| 420G drain and fill plugs, M24×1.5 | 52 Nm | Reverse-light switch 20 Nm | Flow p.74 |
| Oil drain plug | 25 Nm | New sealing ring | Flow p.53 |
| Oil pan bolts, M6 | 10 Nm (8.8) / 12 Nm (10.9) | Sealant at the joints: Flow says Drei Bond 1209; the SI (notes) says Hylomar | Flow p.53; SI (notes) |
| Oil filter cover | 33 Nm | Oil-pressure switch 27 Nm; filter housing bolts 22 Nm | Flow p.58 |
| Oil-cooler pipes | 25 Nm | | Flow p.57 |
| Oil-pump sprocket nut | 25 Nm | Left-hand thread | SI (notes, `torque_specs.md` Q2) |
| Fan clutch to water pump | 40 Nm | **Left-hand thread** | Flow p.61 |
| Exhaust manifold to front pipe (S54 US) | 24 Nm | New nuts and gaskets | Flow p.86 |
| O2 sensors | 50 Nm | Anti-seize on the threads only | Flow p.86 |
| Exhaust flange, M8 | 22 ± 2 Nm | | Flow p.86 |

### 6.3 Wheel alignment (BMW TIS)

This is a BMW TIS printout, "32 00 Wheel alignment E46 / M3", issue status 01/2005, reproduced as p.96 of the Flow PDF (read as an image). It says "observe test conditions", meaning BMW's normal loaded position. Forum citations of TIS for other BMWs give that as 68 kg in each front seat, 68 kg in the middle of the rear seat, 21 kg in the luggage area and a full tank (snippet; not confirmed for the E46). The Touring sits differently from an M3 coupe, so treat these as targets measured at the car's own loaded ride height.

| Axle | Item | Value |
|---|---|---|
| Front | Total toe | 0°16' ± 7' |
| Front | Camber | −1°00' ± 20' (left/right difference max 30') |
| Front | Caster at ±10° lock / ±20° lock | 7°25' ± 30' / 7°40' ± 30' (left/right difference max 30') |
| Front | Toe-out on turns (20° inner lock) | −1°32' ± 30' |
| Front | Set-back | 0° ± 10' |
| Front | Maximum lock (approx.) | 40.90° inner, 33.81° outer |
| Rear | Total toe | 0°22' ± 6' |
| Rear | Camber | −1°45' ± 15' (left/right difference max 15') |
| Rear | Thrust angle (geometric axis) | 0° ± 4' |

### 6.4 Other numbers worth printing in the guide

| Item | Value | Source |
|---|---|---|
| S54 fuel pressure, static | 5.0 ± 0.2 bar; residual above 4.5 bar after 20 minutes | Bentley, quoted on e46fanatics (notes, `fuel_pump_control.md` §4) |
| Pump delivery minimum | 1.12 L in 30 s at 12 V | same |
| Oil-pressure switch closes at | 0.5 bar | NAM3 post (notes, `harness_engine_side.md` Q2) |
| Crankshaft end play | 0.141–0.253 mm | Flow p.43 |
| Coolant system pressure | 2 bar | Flow p.60 |
| Fan clutch switch-on | about 92 °C | Flow p.61 |
| Break-in after new rod bearings | 1,200 miles below 5,500 rpm | SI B11 04 04 (notes) |
| DM-TL leak test enabling conditions | Engine off after at least 20 minutes of driving that followed a 5-hour soak; fuel 15–85%; −7 to 35 °C; 11.5–14.5 V; every second qualifying time | BMW ST041 Part 3 (notes, `coding_dme_ews.md` §7) |
| MIG wire and gas | 0.023–0.024 in for body panels up to 1/16 in; 0.030 in for 20 gauge to 1/8 in; 75/25 argon/CO2; voltage and wire speed from the welder's door chart | [Miller](https://www.millerwelds.com/en-US/resources/knowledge-hub/mig-welding/how-to/mig-basics-for-automotive-welding-repair) (read) |
| Sheet and plate thickness | Properparts plates 1.5 mm (guide); CMP rail plates 2.5 mm zinc-coated (notes); LBL arch sections 1.2 mm (notes, snippet); body panels not measured, so measure yours | as stated |

### 6.5 Consumables and single-use parts the parts list implies but doesn't list

Part numbers come from the notes (ETK) or from the ETK pages in the Flow PDF. Confirm each by VIN.

- **Engine:**
  - Rod bearings, plus 12 new M10 bolts 11247834310 on late engines.
  - Beisan VANOS seals and oil-pump disc.
  - CPV O-ring; valve-cover gasket and spark-plug-tube seals; oil-pan gasket and sealant; rear main seal; water pump and thermostat gaskets.
  - Oil filter set 11427833769; drain-plug sealing ring 07119963151.
  - Exhaust manifold gaskets and new nuts; O2 anti-seize; coolant hoses and clamps; new expansion tank (already listed).
- **Clutch:** clutch set, dual-mass flywheel, release bearing, pilot bearing 11211720310, eight flywheel bolts 11222243051, six pressure-plate screws 21207548052, clutch-line O-rings.
- **Gearbox:** 2 L of MTF-LT-2; seals 23121228493, 23127501582 and 23121222769; shifter bushings (already listed); gear-identification switch 23142229113 if missing or worn.
- **Driveline:**
  - Flex disc (guibo) 26112226527, with bolts 26117635643 and self-locking nuts 26127536563.
  - Centre mount 26122282495.
  - Half-shaft bolts 33211227664 (×12; Flow: always replace).
  - Three bottles of SAF-XJ+FM; diff front bolt 33177840535 if disturbed.
  - Rear collar nuts 33411133785 if hubs are disturbed.
- **Front axle:**
  - Self-locking nuts for the control arms (31106774714), ball joints (31106777806) and tie-rod ends (32216769539).
  - Strut clamp bolts 31306779487; top-mount nuts (M14 31106774714, M8 31316769731).
  - Anti-roll bar link nuts.
  - Reinforcement-plate bolts 31106772199 (ETK quantity 12).
  - Steering lower joint bolts 32306778609.
- **Rear axle:** M3 subframe and diff mounts (already listed), subframe collar nuts 33326760374, rear damper top and rod nuts, RTABs.
- **Brakes:** pads and rotors (already listed), M3 front brake hoses 34322229723 (B4), master-cylinder nuts 07129906196, brake fluid (at least 1.5 L for fill and bleed).
- **Fuel:** M3 filter and regulator parts (already listed), M3 chassis lines 16122229409/410/411 or fittings, M3 vacuum hoses; if you fit the M3 pump, its baffle 16112229656 and a new lock ring and seal.
- **Cooling and A/C:** BMW coolant and distilled water; drier 64538377330/64536917658; A/C O-rings; PAG oil, which the shop supplies.
- **Body:**
  - Weld-through primer, epoxy primer, seam sealer, cavity wax, underbody coating, filler, test coupons.
  - M3 rocker clips; body hole plugs; expanding nuts 51127046911 (×4) only if you fit a new Touring trunk-floor panel.
  - Leave out structural foam until all welding is finished.
- **Electrical:** a blank M35080 EEPROM for the cluster (notes: "080D0WQ"), BMW pre-crimped repair leads matched to each housing's terminal family, heat-shrink and harness tape.

### 6.6 Tools, test equipment and software missing from the guide's list

- **Measuring and testing:**
  - Two torque wrenches: one covering about 5–60 Nm, and one reaching 300 Nm for the 290 and 300 Nm hub nuts.
  - Compression tester and leak-down tester.
  - Fuel-pressure gauge with an adapter and a relay bypass jumper.
  - Mechanical oil-pressure gauge with an M12×1.5 adapter.
  - Cooling-system pressure tester.
  - Vernier caliper to measure panel gauge; profile gauge for comparing arch shapes.
  - Tape measure and plumb bob for ride height and body diagonals.
  - Optional toe plates and a camber gauge.
- **Engine and driveline:**
  - Clutch alignment tool; flywheel lock.
  - E-Torx sockets E10, E12 and E14; 12-point 12 mm socket for M11 rod bolts.
  - 32 mm fan-clutch wrench and pulley holder (left-hand thread).
  - O2-sensor socket; spring compressor for the front struts; slave-cylinder bleed tool or pressure bleeder.
- **Body:**
  - Spot-weld drill bits; hole punch for plug-weld holes; butt-weld clamps; copper or aluminium backing paddles.
  - 0.023 in and 0.030 in ER70S-6 wire; 75/25 gas.
  - Respirator rated for metal fume plus local extraction; fire blanket and a second extinguisher.
- **Electrical and coding:**
  - Dedicated Windows 10/11 laptop running natively (not a VM).
  - K+DCAN cable with genuine FTDI chip and a pins 7/8 switch.
  - Separate PA-Soft (BMW Scanner 1.4) interface.
  - Battery charger or power supply of at least 10 A.
  - Software: NCS Dummy and an NCS profile that allows editing (Revtor or FISTER). BMWFlash, licensed, only for a DIY delete.
  - EEPROM programmer (R270-type) and a hot-air rework station, or use a cluster service.
  - BMW-style depinning keys and a crimper suited to the terminal families.

### 6.7 Values I could not source

Ask TIS, Bentley or the parts on the cars for these. I found no reliable source and haven't guessed:

- power-steering fluid type;
- coolant capacity;
- brake-fluid specification;
- A/C refrigerant charge;
- BMW tire pressures for the 18- and 19-inch M3 sizes (third-party sites disagree: 35/35 psi on tirepressure.com versus 33/35 psi on wheel-sizes.com, both snippets), so photograph the donor's placard and have a tire shop adjust for the Touring's rear weight;
- S54 compression figures;
- S54 rod-bearing oil clearance;
- E46 ride-height specification;
- the E46-specific "normal loaded position" weights;
- RACP and floor sheet thickness;
- MIG voltage and wire speed (these depend on the machine);
- Touring rear damper top-mount torques.

---

## 7. Corrections the notes make to the guide's text

Fix these while folding the notes in, so the guide doesn't contradict its own new sections.

1. **Late rod bolts:** three cycles, not one; change-over 12/2002; identify by bolt head (`torque_specs.md` Q2).
2. **Flywheel:** "the often-quoted 105 Nm is the M54 value" is wrong. TIS gives 105 Nm for the S54 (Q1).
3. **Pressure plate:** the M3 uses 10.9 screws, so 34 Nm (Q4). The guibo's 115 Nm is now confirmed by a TIS printout (Q4).
4. **Four-wire X60004/X6011 move:** it is a from-memory description of an earlier MS42-to-MS43 M54 swap (e34m5freak199's 1998 323i), and for this car it runs the other way (`harness_body_functions.md` §1, `harness_engine_side.md` Q2).
5. **"Not found: pin data for the electric fan, Sport button and brake-light switch, or the DME power and grounds":** the notes now have all four (`harness_body_functions.md` §2–§4, `harness_engine_side.md` Q3–Q4).
6. **The 8.9% speedometer error** isn't caused by a non-M diff. The M3 cluster over-reads by design (`coding_body_chassis.md` §3).
7. **"The wagon's floor is slightly different":** ETK lists the same RACP and trunk floor as the sedan (`touring_subframe_reinforcement.md` §1).
8. **"A donor pump isn't a confirmed fit":** the M3 delivery unit and baffle have been fitted to sedan tanks, which are the same part as the Touring tank. The outlet fitting differs (`fuel_pump_control.md` §3–§5).
9. **"BMW lists its new M3 quarter panels for the coupe and CSL only":** M3 convertible quarters 41357894541/542 exist (`convertible_arch_steel.md` §1).
10. **RPM's EWS delete** is now $300 (`coding_dme_ews.md` §1).
11. **"Sync it to your EWS":** a used DME can't be synced; only a virgin one can (`coding_dme_ews.md` §2). The ZCS-versus-FA explanation for the 325xi failure is probably not the cause (same section).
12. **"Write your VIN with PA-Soft":** this doesn't work on a used cluster without the EEPROM route (`coding_body_chassis.md` §3).
13. **"Transplant the donor's DSC unit":** present it as a choice, because of the documented Touring failure (`coding_body_chassis.md` §5).
14. **"Drive gently for the first 300–500 miles":** BMW's SI says 1,200 miles below 5,500 rpm (`torque_specs.md` Q2).

---

## 8. Sources consulted for this review (beyond the guide and the notes)

- **BMW ST041 "1 M3 Complete Vehicle", technical data** (capacities, fuel grade). [archive.org text](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle_djvu.txt) (read).
- **BMW S54 training text** (oil recommendation), in ST041 "2 M3 DriveLine", the same text as the guide's [billswebspace module](https://www.billswebspace.com/MS54B32TrainingModule.pdf) (read, from a local copy).
- **"Flow" E46 M3 torque compilation, updated Feb 2024**, including the BMW TIS alignment printout on p.96. [Google Drive](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing), via the [NAM3 thread](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/414-e46-m3-torque-spec-thread-every-bolt-on-the-car-on-diagrams) (read, pages as images).
- **ETK on bmwfans.info** (read):
  - booster: M3 [34332282193](https://bmwfans.info/parts-catalog/34332282193/), [34332282622](https://bmwfans.info/parts-catalog/34332282622/); Touring [34336779682](https://bmwfans.info/parts-catalog/34336779682/)
  - master cylinder: M3 [34312282343](https://bmwfans.info/parts-catalog/34312282343/); Touring [34316752541](https://bmwfans.info/parts-catalog/34316752541/)
  - M3 front brake hose [34322229723](https://bmwfans.info/parts-catalog/34322229723/) and pipes [34322282275](https://bmwfans.info/parts-catalog/34322282275/)
  - front ABS sensors, shared: [34526792896](https://bmwfans.info/parts-catalog/34526792896/)
  - steering lower joint, shared: [32301094700](https://bmwfans.info/parts-catalog/32301094700/)
  - A/C condenser and drier diagrams: [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/condenser_air_conditioning/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/condenser_air_conditioning/)
  - trunk-floor mounting parts: [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/mounting_parts_for_trunk_floor_panel/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/mounting_parts_for_trunk_floor_panel/)
- **Fluid pages** (read): [BimmerWorld MTF-LT-2](https://www.bimmerworld.com/Genuine-BMW-MTF-LT-2-GL-4-Transmission-Fluid-1-liter.html), [BimmerWorld SAF-XJ+FM](https://www.bimmerworld.com/Fluids/Driveline-Fluids/Genuine-BMW-Differential-Gear-Oil-SAF-XJFM-500ml-bottle-E46-M3-E9X-M3-F8X-M3-M4.html), [BimmerWorld CHF 11S](https://www.bimmerworld.com/Suspension-Steering/Pentosin-CHF11S-Hydraulic-Fluid-BMW-82111468041.html).
- **Welding and safety** (read): [Miller, MIG basics for automotive repair](https://www.millerwelds.com/en-US/resources/knowledge-hub/mig-welding/how-to/mig-basics-for-automotive-welding-repair); [OSHA fact sheet FS-3647, welding fume](https://www.osha.gov/sites/default/files/publications/OSHA_FS-3647_WELDING.pdf).
- **Legal** (read): [EPA, MVAC servicing requirements (venting prohibition)](https://www.epa.gov/mvac/regulatory-requirements-mvac-system-servicing); [California BAR, engine changes](https://www.bar.ca.gov/engine-changes); [BAR, modified-software implementation, July 2021](https://www.bar.ca.gov/pdf/bag/202107/bar-ois-modified-software.pdf).
- **BMW wheel/tire list, E46 M3 MY2005** (read; has no pressures): [myair-bdr.bmwgroup.com](https://myair-bdr.bmwgroup.com/static/manual/RadReif/RadReif/00/M-GmbH/MJ2005/e46m3_2005.htm).
- **Search snippets only** (not verified):
  - Turner fluid listings: MTF-LT-2 supersession; diff 1.2 L. Turner blocks with Cloudflare.
  - [tirepressure.com](https://tirepressure.com/2004-bmw-m3-tire-pressure) and [wheel-sizes.com](https://wheel-sizes.com/tire-pressure/bmw/m3/) tire pressures.
  - The M54 compression figure on [bmwfaq.org](https://bmwfaq.org/threads/compresion-n46.977278/).
  - The 0.001 in rod-bearing clearance on [bmwtuning.co](https://bmwtuning.co/bmw-rod-bearing-failure/).
  - Coolant 50/50 and bleed-screw method (M3Post, zhpmafia).
  - "Normal loaded position" weights (xoutpost, z4-forum).
  - Clutch bleeding methods (m3post).
  - Bentley E46 coverage including the M3 (seller listing).
