# Round-4 fold-in log (for later phases)

## Agent IDs
- Writers: arches aeaa3d53ded88d109, floor ad6f4f622a29dbef1, susp a30112f911fd3c0bc, fuel add10541deab4d8ca (DONE),
  front a892b5f82b56153de, coding-power aac9cb591d4540684, cool adb5e4b183691f9a1, coding-body abb987e20b0bc227f
- Gap-fillers: bmw-chassis aa23d336dde28078f, bmw-powertrain ac4d45749aa9345ef, parts a37c0c6953244873b,
  builds a50d99e676cb2a4d9, coding-body-gaps a940cd36ee717256c
- xi: xi-awd abeb8c29b1fdfb98a, xi-rwd acd875fefd3025b66

## Figures to fix or draw (diagram phase)
- 04-fuel-pressure.svg (README Figure 7): "after" panel wrong (labels own pump "test at 5 bar first"); lacks pipe set, TP1,
  return sample point, purge line. New caption suggested by fuel writer: "The donor's in-tank set moves into your tank;
  the M3 pipe set, lines and filter-regulator take it to 5 bar, with a vacuum hose to the idle-air pipe. Test at the
  regulator's threaded fitting (TP1)."
- 11-fuel-pump-control.svg: OK; could add fused bypass across K96 pins 6->2 and soften "which stores fault 1".
- NEW proposed-fuel-layout (README, after fuel parts table in "Fuel system"): plan view zones Z1-Z6, tank + M3 in-tank set,
  pipe set, feed/return L1-L5, vacuum V1, purge P1, vents E1-E3, filler F1, filter-regulator TP1, rail, canister, DM-TL,
  separator (graft zone hatched), test hookups TP2/FS1/RB/VD, quick-connector vs clamp, M3 vs Touring colours.
  Data: fuel_system_fit.md diagram section.

## research.md items (research-page writer)
- line ~56: barb vs quick-disconnect statement is outdated (pipe set finding).

## Conflicts flagged by writers (integrators decide)
- fuel: M3 canister position / M3 holder without M3 floor (vs floor notes); filler pot "moves much less" vs "doesn't move"
  (arches notes); overlapping edits Phase 4 step 5; gauge curve corrections; EKP_CFG lead.

## susp writer (DONE): 40 requests
- Figure: 12-coding-order.svg (README Figure 9) says "Wheel alignment at the car's loaded ride height" -> unladen, full tank.
- NEW proposed-ride-height-points (README 0520): wheel side view (hub centre, rim flange lower edge, arch edge; BMW ride
  height = rim flange to arch edge; hub-to-lip), M3 targets 605/587 (18 in), 619/600 (19 in), ±10 mm; 16->18 in rim
  adds ~25 mm with body unchanged; M3 tyres lift ~14 mm; car side view with four jacking points + roof marks
  (1,409 mm, 1,444 mm with rails) as the Massachusetts baseline.
- Conflicts: 420G oil 1.8 L (2003 US M3 manuals) vs 1.9 L (ST041); alignment load (front notes "loaded ride height" vs
  susp: unladen + full tank per BMW M3); "normal position" reading (arches notes loaded vs ST503 no added weight).

## front writer (DONE): 41 requests (39 open)
- Figure 13-dsc-brake-options.svg (README Figure 12) WRONG: "pedal feel unreported", booster-hose footer, wheel-speed footer
  ("keep the donor's pigtails"), B-route fallback (recode from VO dated 09/2002+ first); caption's "sensor plugs need checking".
- 12-coding-order.svg: "loaded ride height" -> unladen, full tank (same as susp).
- 26-flow-warning-lights.svg (WIRING): could add MK60 fault ranges 5D90-5DC5 and red BRAKE lamp meaning.
- NEW proposed-brake-hydraulics (MC/booster, MK60, unchanged hard lines, M3 front hoses + calipers highlighted; missing: MC
  outlet->front circuit, rear pipe sides, MK60 port layout; 590 mm pipe to LF inferred).
- NEW proposed-booster-vacuum (S54 air shut-off valve -> jet pump -> shortened hose -> clamp -> M3 check valve 34331161300 ->
  new grommet 34336765316 -> booster; Touring valve+elbow removed).
- NEW proposed-power-steering-circuit (pump -> pressure hose -> rack -> return pipe -> cooling coil -> reservoir; ATF;
  40/35/21/27 Nm; missing capacity, coil connection).
- Conflicts: Phase 4 brake-fluid drain vs keep MK60 full (R18/R30/R38); rack curve wert_02/touring_s for quicker racks ->
  leave unit as coded; 13.7:1 also ZHP; strut-top 24 vs 34 Nm flagged; new safety line about brake pipes near welding (R24,
  our recommendation).

## cool writer (DONE): 57 requests; new fragments README/0558__air-conditioning.md, WORKSHEETS/0468__a-c-after-the-charge.md
- NEW proposed-coolant-circuit (README "Fill and bleed the cooling system"): pump, block/head, 80 °C thermostat, radiator,
  vent screw in hose 11537830716, tank + 2.0 bar cap, heater valve (with pump or plain), heater core, outlet sensor, drains, arrows.
- NEW proposed-ac-circuit (README "Air conditioning"): compressor -> M3 hose 64536902681 -> condenser -> new drier -> sensor ->
  expansion valve -> evaporator; high side solid, low side dashed; M3 vs Touring parts.
- NEW proposed-fan-layout (README Cooling): Touring as built (shroud fan, X82 on shroud) vs swapped (viscous fan + shroud,
  pusher in front of condenser, X82 extended); DME pin 4, F37, ground.
- Overlaps for integrators: susp R3/R5/R12 vs cool R1/R54/R23 (apply cool's coolant lines, keep susp's 420G part);
  coding-body Session 8 climate bullet + cool R36 appended; front R23/R32 still match (Card 10a ~43% with R32).

## floor writer (DONE): 25 requests; new WORKSHEETS/0184__plug-welds-and-sealing.md; floor options swapped (1 = new BMW floor)
- Figure 14-cargo-floor-plates.svg (README Figure 5) WRONG: "no flame-cutting within about 120 mm of the rails" labels,
  aria-label and caption (correction 4) -> the rail and rear-floor flanges must survive; drill spot welds.
- Figure 05-exhaust-floor.svg (README Figure 6) WRONG: lead with new BMW floor (not "donor coupe floor section or flat panel");
  "tack, stitch" -> plug welds at factory spot-weld positions.
- Figure 01-swap-map.svg aria-label calls the floor "fabricated" -> fix.
- 03-subframe-mount.svg OK.
- NEW proposed-floor-exhaust-plan (in README 0470): plan from below: rear-mount datum, rails, RACP seam, removed Touring well,
  CMP 120 mm strip, M3 floor outline, muffler box, hangers H1 41112497585 / H2 41122494844 / H3 41112493931, heat shields
  51482494848 / 51487893366, canister on Touring vs M3; coordinates from notes' Figure A, "approximate".
- NEW proposed-floor-seams: drill-out rows along flanges, well drops out downward, joint inset (8 mm plug, 10-13 mm face,
  >=25 mm pitch, sealer both faces), flangeless-lap inset.
- Overlaps: arches Key numbers row dup of floor R17 (apply one); Massachusetts title sentence after arches' version;
  Phase 4 step 5: apply fuel R10 and floor's; canister wording (floor: within 25 mm of muffler fit M3 holder; if clear either).

## coding-power writer (DONE): 22 requests; changed 32 fragments, none created
- Already applied by coding-power (integrators skip): front R27-R29, fuel R24 + R27, susp R38, cool R28-R31 + R33-R35;
  coordinator's six body-module points.
- coding-power R17 -> susp's Card 12d (routine names, adaptation rule); R20-R21 -> coding-body (Warning lights MK60 cause,
  Session 8 adaptation step); R22 -> front (session order from ALSZ, no Code Car, M Track, RPA reset).
- Figures: 13-dsc-brake-options says "refit your own unit" with no coding step first (WRONG, same as front's note);
  26-flow-warning-lights still says "M3 MK60 that won't accept the Touring" (WRONG). 12-coding-order, 25-flow-no-start(-2),
  24-flow-power-up(-2) still correct (but 12 has "loaded ride height" per susp/front).
- NEW proposed-coding-sessions-flow (WIRING 0470): sessions 1-9 + alignment; decisions SMG donor, MSS54/HP, MS43/MS45.1
  (wiring only), immobilizer route, DSC option; back-edge Session 8 -> touched modules; Session 6 only after engine change.
- NEW proposed-dsc-coding-path (Session 5): A = three routines + checks; B = VIN write -> session order (#0902+) -> coding ->
  save final coding file -> routines -> refit own unit if fails; panel with C05 unit settings.
- NEW proposed-ews-recovery (Session 3): cranks? no -> EWS status bits; yes -> fault 130/66 types + actions; lone 130 after
  delete -> "Won't start" Q5.
- Conflicts: wert_02 "closest" dropped; ALSZ over AKMB; NCS 4.0.1; HW numbers RPM vs NAM3 (ask vendor);
  TANK_KENNLINIE "left as read" (coding-body Session 4 should match).

## arches writer (DONE): 37 requests; 12 fragments; new H4s in 0670 (Flare profile; Datum, stations and templates;
## Measure both cars, then mock up)
- Already applied by arches (skip): fuel R16, floor R21, susp R29, susp R40. Apply arches R16 (MA title) instead of floor R15(c).
  arches R12 carries floor R11's change to the same row.
- readme-main: check README 0520 for stale "We found no E46 ride-height specification" (susp fragment) -> M3 TIS figures now known.
- Figure 08-rear-quarter.svg (README Figure 14) WRONG: "about 25-30 mm proud" -> profile; cut line should follow seams
  (top 500-515 mm above hub, rear 550-600 mm behind axle, front 25-40 mm behind shut line), not an arc to the sill;
  bulge ends at bumper line ~300 mm behind axle; filler label: pot stays put; caption: 11-20 mm step at the door.
- Figure 09-arch-section.svg (README Figure 15) WRONG: offset ~21 mm at the axle (not ~29); tire about flush (not 15 mm
  inside); lip = double skin ~15 mm deep; caption + aria-label "25-30 mm".
- NEW proposed-arch-profile (notes rear_arches.md Guide-ready C1, C3): side-view cut template, offsets at stations, seam lines.
- NEW proposed-arch-section-axle (C2) -> probably fold into the 09 redraw.
- NEW proposed-arch-weld-sequence (C4): tacks, stitches, lip plug welds order.
- Decisions: coupon tear-out 3-8 mm (I-CAR thin-to-thin); 6 mm holes on arch lip, 8 mm on floor; normal position = unladen,
  full tank; filler pot stays; lap joint floor, butt joint over backing strip for the arch skin.

## Diagram makers (launched, DIAGRAM-BRIEF.md)
- dm-arches a93be5ba79755a66b: 27-arch-profile (new), 28-arch-weld-sequence (new), redraw 08, redraw 09 (= section at axle;
  REMOVE placeholder proposed-arch-section-axle at integration).
- dm-floor ab512928784f83539: 29-floor-exhaust-plan, 30-floor-seams, redraw 14, redraw 05, fix 01 aria.
- dm-chassis ab612caf06268028b: 31-ride-height, 32-brake-hydraulics (+ booster panel; REMOVE placeholder proposed-booster-vacuum),
  33-power-steering, redraw 13.
- dm-fuel a610efd964cfcd139: 34-fuel-layout, redraw 04, optional 11.
- dm-cool adeb94c09be9954ec: 35-coolant-circuit, 36-ac-circuit, 37-fan-layout.
- PENDING dm-coding (after coding-body writer): 38-flow-coding-sessions, 39-flow-dsc-coding, 40-flow-ews-recovery,
  41-identity-storage, redraw 12-coding-order ("loaded ride height" -> unladen, full tank), redraw 26-flow-warning-lights.
  DROP placeholders proposed-ncs-error-triage and proposed-xenon-path (tables suffice).
- PENDING xi: 42-xi-driveline.

## coding-body writer (DONE): 22 requests; new WIRING fragments 0471__ncs-expert-basics.md, 0241__steering-wheel-buttons-mfl.md
- Already applied by coding-body (skip): coding-power R20 + R21, cool R36, front R26, fuel R14 + R28 + R29.
- Conflict: README Massachusetts brakes row says DSC/ABS faults light the red lamp (contradicts BMW ST056) -> front R15 fixes it.
- Figures WRONG: 26-flow-warning-lights.svg (WIRING Figure 13): add red BRAKE row (low fluid or parking brake, not a DSC fault),
  rename "brake" -> "yellow BRAKE", add yellow BRAKE to key-on box, update "re-code AKMB and ALSZ" wording; also coding-power:
  "M3 MK60 that won't accept the Touring" wording; optionally MK60 fault ranges 5D90-5DC5.
  12-coding-order.svg (README Figure 9): Session 4 add FA_WRITE of the vehicle order back into the cluster; Session 8 = only the
  modules a change touches, never Code Car; plus "loaded ride height" -> unladen, full tank.
  06-electronics.svg (README Figure 8): light module also holds the vehicle order; cluster box mentions the donor's order.
  20-circuit-sport.svg (WIRING Figure 5): 61316925498 is the no-DSC Touring's switch unit (DSC-equipped part number open).
- Proposed figures: identity-storage (KEEP -> 41), ncs-error-triage (DROP), xenon-path (DROP).

## Integrators (launched): readme-plan a78bd50845da5f696, readme-build aad5f31431613186b, readme-back a39331ad9f8ed7627,
## others a00e5ea313d64a48e. dm-coding-a aa355834804067cac, dm-coding-b a561916327d47b53d.

## Gap-fill results (to send to integrators in one batch when all are in)
- bmw-powertrain DONE -> gapfill_bmw_powertrain_coding.md: closed brake fluid DOT 4 (owner's manuals), 420G ~1.8 L (1.9 US qt;
  ST041 1.9 L = quart figure), coolant 9.3 L (325i 8.4 L), reserve ~8 L (2.1 gal) of 63 L, mode-09 VIN required only from
  MY2005 (13 CCR 1968.2(g)(4.8.1)); narrowed A/C (Denso 7SBU16C, ND-8 PAG, 160 ml new unit), PS (same reservoir, ATF label;
  capacity unknown), fan logic (16 A/C stages, 60% fallback), IHKR release, readiness, EWS (RPM-matched used DME success).
  Open: TIS 13 31, TIS 17 00, VANOS limits, mode 09 answer on 2003 MSS54, MK60 CI.
- parts DONE -> gapfill_parts_prices.md: BMWPartsDeal 22 Oct 2026 (ships 1-3 days): conv side panel 41357894541/542 $2,105.60 ea;
  inner trim panel 41217894553/554 $127.54/$118.80; coupe interior side frame 41217890677/678 $1,311.70 ea; M3 coupe side panel
  41217890689/690 $6,932.63 ea; floor $763.61 + reinforcement $88.22 (eStore-Central EUR 717.97 / 81.79); conv steel both arches
  + floor ~ $5,309. SIDE FINDING: RACP insert 41117000246 "discontinued" (check guide's subframe reinforcement text + parts).
  Springs: OE numbers (FCP Euro VIN fitment) for 2003 manual 325iT std/sport and US M3 coupe/conv; no Touring kit for M3 axle.
  Damper lengths (Bilstein equiv.): non-M rear 370-618 mm, M3 rear 377-597 mm, same mounts. Expansion-tank holder 17112229108
  also carries the SAP; M3-only welded brackets 41147894115/116. Narrowed: inner-panel flange M3-only number at arch position;
  fuel "sleeve" probably the M3 baffle; manual 325iT has no pusher fan (forum snippet) and X82 probably matches; canister holder
  on 4 M6 studs; rear heat shield nuts on body studs; thrust plate broader at front.
- coding-body-gaps DONE -> gapfill_coding_body.md (SP-Daten V32 decode): CLUSTER ACCEPTANCE = NO (M3 cluster idx 22/23/24 only
  with PU01 AND S54B32; EN33 fails; FA_WRITE very likely refused) -> cluster keeps donor order, ALSZ = true order, never Code Car.
  TANK_KENNLINIE = 60_l_literskala per BMW rule (original guide right; metalltank only M56B25). Lamp switches idx 07/08/23/24;
  LWR curves M3 wert_03/02/03/03 vs non-M wert_01; fogs need fog-variant LM + button + K47 ($520 nothing); washers opt 502 SWA
  (optional US M3); DSC 325iT switch = separate 61316901592 (61316925498 = non-DSC console; 61316925512 = US sedan DSC console);
  type keys EN33 (AW33 pre-09/01), BL93, BR93. Open: rear-glass LED (Tool32 test), OC3 year, first SP-Daten with C23/C24.
- SENT batch 1 (powertrain, parts, coding-body gaps) to all four integrators; corrected dm-coding-a and dm-coding-b (cluster rule,
  DSC switch). Remaining gap-fillers: bmw-chassis aa23d336dde28078f, builds a50d99e676cb2a4d9.
- builds DONE -> gapfill_builds_forums.md; bmw-chassis DONE -> gapfill_bmw_chassis_body.md (TIS 12/2007 via workshop-manuals.com):
  RIDE HEIGHT + ALIGNMENT LOADED (M3: full tank, 2x68 kg front, 14 kg trunk; Touring adds 68 kg rear centre, 21 kg trunk);
  Touring TIS ride heights std 15/16/17/18 F 576/589/604/617 R 542/555/570/583, sport F 561/574/589/602 R 526/539/554/567;
  M3 design position for alignment; strut-top 34 Nm new nuts; thrust plate 6+6 vs 4+4, 59 Nm + 90 deg rear row first;
  bleed: rear circuit with tester even after caliper work (34 00 048); parking brake 10 notches; MC front circuit next to
  booster (inferred); rear pipes: 3,684 mm left, 3,798+1,206 mm right (inferred); body: graft not a BMW repair; joint practice
  (60 mm backing strips, stitched continuous seam, crimped arch edge); gaps 4 +-0.75 rear door/side wall; 82/18 Ar/CO2, G3Si1.
  Builds: BaT car bid $59,250 reserve not met; Bry5on S54 Touring weights; E36 M3 muffler with well kept (3 swaps); carbon floor;
  manual Touring no pusher fan (owners); "crank and brief fire" = EWS (George Hill).
- SENT batch 2 to all four integrators; corrected dm-chassis, dm-arches, dm-floor, dm-coding-a.

## xi research
- xi-rwd DONE -> xi_convert_rwd.md: verdict hard but feasible; +$0-1,500 parts (donor from 09/2002) or $1,000-3,000 (earlier),
  +4-8 weekends. Body: rear of front seats same as 325i (axle mounts, trunk floor, tank, fuel lines, parking-brake cables, exhaust
  hangers); forward: xi-only frame rails, strut towers, anti-roll-bar brackets, widened tunnel. Subframe: three xi Tourings run
  M3/RWD front subframes, no mount fab reported -> trial fit is the gate. M3 gearbox crossmember doesn't fit xi tunnel (custom
  bracket, JMCCRNA); xi lower steering joint must change. DSC: full MK60 system needed (xi Bosch 5.7 front sensors don't fit RWD
  hubs; MK60 sensors incompatible with Bosch unit); plugs 42-pin vs 47-pin; CAN pins 24/40 vs 11/15 -> adapter loom signal by
  signal (pin table in notes). Coding: xi order has $203 (AWD) + own type key; code MK60 against a 325iT order in that session only.
  Emissions: every 2001-05 325xi Sport Wagon LEV = S54's category (MA best case). Open: subframe threads, M3 ARB brackets, Bosch
  pinout, NCS + MK60 on xi order, BaT sale (Top Gear "sold" vs not sold at $59,250).
- xi-awd DONE -> xi_keep_awd.md: very hard; 2 US cars; one wrecked S54 (Colorado/FCP car: pump chain ground into pan -> spun
  bearings, cracked rods, crank damage; fix re-made pan). xi pan 11137519432 (= "330xi pan", also X3 M54); gasket shared by every
  M5x/S5x six since 1997 -> proves nothing; axle tube welded at pan front where S54 two-stage pump draws; builds fitted M50-family
  pump. Gearbox: 325xi 5-spd below S54 torque; both builds 330xi 6-spd (from 03/2003); Z4 M S54 used that family, M3 flywheel +
  Z4 M clutch; no AWD 420G. Transfer case NV 124 300 Nm quoted, fitted to 390-410 Nm 330xd. Diffs: X3 2.5i 3.91 pairs; 325xi/330xi
  auto 3.46 pair ~ M3 gearing; X3 rear flanges don't match. Keep xi DSC 5.7/front axle/rack. Fuel = 325iT's. Guide correction:
  FCP car = BMWBlog 2018 rivet-flare Touring (listed twice).
- xi writer ac1ce2663bf620a80 (owns README 0050 + new 0519; requests -> requests/xi.md, I apply after integrators).
- dm-xi a93bd6907e538d696: 42-xi-driveline.svg.

## dm-chassis DONE: 31-ride-height, 32-brake-hydraulics, 33-power-steering, redraw 13 (0 issues). VERIFY after integrators:
  README 0520 no longer says "unladen, full tank" (Which load, M3 figures, mock-up step 1, rear bushed joints, MA baseline, settle
  check) nor "BMW's figure for the E46 Touring is still missing"; README 0530 bleeding step 3 no longer allows conventional bleed
  after caliper/hose work (rear circuit with tester per TIS 34 00 048); "about 25 mm" 16->18 in vs TIS 28 mm rows.
  Fig 31 omits the strut-label hint (6Z Serie / 6Z Sport) -> text should carry it.

## dm-coding-b DONE: 39-flow-dsc-coding (400x1395), 40-flow-ews-recovery (400x1197), redraw 26 (landscape 800x825), 20 label.
  VERIFY after integrators: WIRING 0510 step 6, 0550 step 3, 0660 check column no FA_WRITE to AKMB; WIRING 0220 step 1 + README
  0260 parts row: DSC button 61316901592 (61316925498 non-DSC); WIRING 0520 "yellow BRAKE"; WIRING 0500 fault table "X60004 pin 33
  (EWS data line)". (Sent 0520/0500 items to others.)

## dm-cool DONE: 35-coolant-circuit, 36-ac-circuit, 37-fan-layout (portrait, 0 issues).
  VERIFY: README 0550 step 8 no "oil-cooler joints" in coolant test; 0430 Phase 12 links to Fill and bleed steps 9-14;
  0920 coolant capacity no longer open (9.3 L). (Sent 0550/0430 to readme-build.)

## USAGE LIMIT HIT ~18:00 UTC; nine agents stopped mid-work, resumed after reset.
## dm-floor DONE: 29-floor-exhaust-plan (400x540), 30-floor-seams (400x1002), redraws 14 + 05, fix 01 (label "fit M3 floor").
  Rear subframe mounts drawn 660 mm apart = TIS 41 00 F-F. CONFIRMED (inference): TIS top view H-E 2,609 < H-F 3,011, so E is the
  front pair (440 mm) and F the rear pair (660 mm); matches 0460 "rear mounts ... beside each chassis rail".
  Text asks: README 0470 hanger table name H1/H2/H3 (readme-build); worksheet "rear-mount bolt spacing" row 660 mm (others).

## dm-arches DONE: 27-arch-profile (800x752), 28-arch-weld-sequence (400x1324), redraws 08 + 09 (0 issues). 09 caption replaces
  placeholder proposed-arch-section-axle (apply_redraws drops it). Sent text fixes to readme-build: 0670 "unladen" x2 -> loaded;
  0660 "10 o'clock" left only (2 o'clock right); 0680 front seam along shut line to sill flange; step 8 backing strip ~60 mm;
  step 11 "until continuous"; arch graft not a BMW repair; door gap 4 +-0.75.

## dm-fuel DONE: 34-fuel-layout (800x668), redraw 04 (400x468), tweak 11 (bypass K96 6->2, softer fault wording; 11 is in README
  "Fuel-pump control"). Sent canister rule merge to readme-build (0540 vs 0470). FOR REVIEW (rv-fluids): K96 pin 2 = terminal 87
  (notes) vs 87b (text) -> verify on WDS; filter/housing/regulator buy new (text) vs donor cores (notes); T9 job name text
  STATUS_AIF_TANKDATEN_LESEN (KOMBI46R) vs notes STATUS_TANKINHALT_LESEN (KOMBI46) -> text consistent with coding-body notes;
  fig 34 view from above front-left vs fig 29 from below front-top (each states its view).

## readme-plan DONE: 48 writer requests + both gap batches. Budget ~$26k-$73k ($23,455 x 1.10; $63,784 x 1.15); optional new arch
  steel ~$4,460 outside total. Decisions: TIS loaded wins; cluster keeps donor order; canister: move only with M3 floor, expect to,
  mock-up 25 mm rule; filler pot stays; BaT bid $59,250 not sold; builds Bry5on, Kaiv added. Not applied: "keep M3 hubs with M3
  DSC" (contradicts default); Westminster row (all "not stated"). Forwarded its 3 cross-set requests: WIRING 0540 "unladen"
  (others), README 0470 "unladen" + 0480 "TIS 51 00" -> 41 00 (readme-build). research.md not checked (do at review).

## dm-coding-a DONE: 38-flow-coding-sessions, 41-identity-storage (new), redraws 12 + 06 (0 issues). Cluster keeps donor order;
  FA_WRITE only into ALSZ in fig 41; alignment "in BMW's design position, at the M3 load". EWS drawn as holding no vehicle order
  (README 0590 says EWS carries a VIN). Sent README 0600 stale sentences to readme-build. WIRING 0540 "unladen" already sent to others.

## readme-back DONE: 78 writer requests + both gap batches + late additions; torque table one row per fastener (New/Reuse/
  Conflict); open questions grouped, "Answered in October 2026" list; MA rows (floor pans, suspension/steering, brakes per ST056,
  ride height per TIS). 420G ~1.8 L. Cross-set R3 (README 0510 420G wording) -> readme-build; R4 (WIRING 0530 cam-range citation)
  -> others. Backups: scratchpad/rb-backup/. Not applied: two more BAR-certified S54 Tourings; BaT "true mileage unknown".
## dm-xi DONE: 42-xi-driveline (400x1214, 0 issues), drawn from notes before 0519 existed -> CHECK caption/labels vs 0519.
  US S54 = 355 Nm (ST041), not 365 (told xi writer); "wrecked the bottom end"; "M3 lower steering joint and coupling".
## research.md updated by me: new H2 "A fourth round in October 2026 read BMW's own repair manual and coding data" (7 bullets)
  + inline fixes (fuel pipe set; DSC row 13 ALSZ/leave as coded; M Track $7MA; 318i NCS path note; light module/cluster).
  TODO: NAV_TEXT_LABELS entry ("A fourth round", "Round 4: what changed").

## readme-build DONE: 64 requests (55 applied, 9 already in place), merges in Phase 0/1/2/4/12, all "unladen" -> TIS normal
  position (M3 load for donor/mock-up/bushed joints/alignment design position; Touring load for Phase 0 baseline + MA check),
  bleed per TIS 34 00 048/050, parking brake 2nd tooth, TANK_KENNLINIE 60_l_literskala, canister merged rule, filler pot stays,
  "TIS 51 00" -> 41 00 (0360/0480/0670), RACP note (discontinued). Backup: scratchpad/readme-build-backup/.
  -> Fig 34 canister label unconditional: resumed dm-fuel to fix.
  -> Fig 12 (13-dsc) caption "sensor plugs need checking" is replaced at assembly by redraw-13 caption (OK).
  -> 0558: Denso 4-groove pulley for compressor 64526916232 vs ETK 5-rib belt for M3: flagged in text; consider open question (rv-fluids/rv-ref).

## xi writer DONE: README 0050 rewritten (short summary + link), new README 0519 "### 325xi: rear drive or all-wheel drive"
  (13 H4s, ~70 KB). 24 requests in requests/xi.md (none applied). Conflicts: AW33 type key (325iT vs 325xi); MK60 coding
  Option B ($203 deleted, EN33 only for 325i unit); DSC 5.7 on RIGHT of engine bay (fig 42 must match); Session 9 levelling
  curves vs BMW ALLRAD; Colorado car diff ratios listing vs ETK. Placeholder proposed-xi-driveline in Route 2.
  Not applied: "plugged right in" wording kept; no permanent 325i-order fallback (ALSZ rule kept).
## coordinator: applied xi R1-R15, R17, R18, R22-R24 (README; all OK, tables/$ clean). Held WIRING R16, R19, R20, R21 until
  "others" integrator finishes. Verified 7 archive.org BMW doc file names (R7). Fig 42 checked vs 0519: part numbers, 38:62,
  300/355 Nm, 3.46/3.91, flanges, DSC 5.7 right / MK60 left, adapter loom: all consistent. Backups: scratchpad/r4fold/xi-backup/.
## rv-plan LAUNCHED (README framing/plan/legal + xi 0050/0519 + fig 42). Others wait for 'others' integrator.

## others integrator DONE: all writer requests + gap batches + xi R16/R19/R20/R21 + readme-plan R1 + readme-back R4 + coding-body
  R4-R6 (deleted duplicate "No buttons on your steering wheel?" para in 0240; new fragment 0241 covers it). Merges: coding-power
  R16+fuel R20 (Card 1); cool R38+front R36 (Card 2a); fuel R22+floor R22 (Card 4); coding-power R17+coding-body R22 (Card 12d);
  front R37+susp R37 (WS 0260). Overruled by gap-fill: TANK_KENNLINIE 60_l_literskala everywhere; all "unladen" gone; parking
  brake 2nd tooth (TIS 34 10 014); front R27 -> TIS 34 00 048; no FA_WRITE to AKMB anywhere. Decided: strut-top 34 Nm; 420G
  ~1.8 L; 660 mm mount spacing +-1 mm (TIS 41 00: +-1 mm to 1 m). WS 0230 torque rows aligned with 0870. Cards grow 0-41%.
  No cross-set requests. 0241 not in owners.tsv.
## REVIEWERS LAUNCHED (18:5x): rv-plan ad9c01890fa406aab; rv-chassis acee9d3179c30d7f8; rv-fluids a3c1457c0e7fda896;
  rv-body ac4cc39790d23a236; rv-coding a4c2c15a5c3cd467c; rv-ref ae38a4f6cf2f9f24b. Requests -> review-requests/<rv>.md.
  Fixed owners.tsv: README 0050 -> xi; added WIRING 0241 (coding-body). Preview rebuilt after "others" finished: links OK.
## rv-plan DONE: ~140 facts, 14 spot-checks. P1 fixed in 0519: 540 CMR 4.04(13) exempts 4WD from the 2-inch rule; 6.00 limits
  apply (level within 2 in, no spacers, <=4 in more track). P2/P3 fixed in 0000, 0070, 0080, 0110, 0130, 0330, 0510, 0519, 0730:
  sensor-cluster quote; weekends 4-8 (ARB brackets folded into front end); xi row in "Decide these"; "Choose the donor" bullet;
  "plugged right in" -> plugs fit; Phase 11 order VIN/coding/routines. AW33: go by VIN decode + $203. Colorado diffs "X3 3.91
  pairs (the X3 2.5i's ratio)". Requests: R1 rv-coding (Session 5 delete $203), R2 rv-chassis (README 0240 anecdote), R3 rv-ref
  (AW33 open question). Fig 42 F1/F2 sent to dm-xi. Backup: scratchpad/rvplan-backup/.
## dm-xi: fig 42 F1 (X3 3.91 pair) + F2 (rack comes out) applied, 0 issues.
## rv-body DONE: no P1; 9 P2 + 11 P3 fixed in own frags (E36-muffler "quiet" claims; 0670 "490 mm" is a radius -> front end
  ~375 up/315 ahead; seams = inference in Phase 6/Card 6/WS 0190; welding: brake-pipe rule + combustible foam; filler 2 mm pass;
  H1/H2/H3 hangers in 0470/Phase 5/WS 0184; 660 mm in 0470 datum step). Requests: R1, R2 -> rv-ref (forwarded); R3 research.md
  (26.7 kg muffler; R44 GBP 4,420; BMWPartsDeal $2,105.60) APPLIED by me. Fig 27 F1 -> dm-arches (sent).
## rv-coding DONE: ~150 facts, 9 spot-checks. P1 fixed: bleed wording BMW-first in WIRING 0520/0670 + README 0420 step 13;
  Session 9 rear sensor on the fitted (M3) axle; headlight washers = option 502. Levelling: added ALLRAD curves to Session 9 +
  WS 0410. EWS holds VIN, no order (README 0590, WIRING 0471, fig 41 caption). AIF_KM = true reading. 5E1F leads (5EF1 in
  PA-Soft). rv-plan R1 applied in substance. Requests: R1 -> rv-chassis (forwarded); R2 research.md MK60 x3 APPLIED by me.
  Figure fixes sent: dm-coding-a (41, 12, 38, 06), dm-coding-b (39, 40, 26, 25, 25-2).
## rv-ref DONE (+ rv-body R1/R2 applied; rv-plan R3 applied): ~150 facts, 8 spot-checks; ~190 torque rows vs Appendix: no
  mismatch; no stale values. P2 fixed: door gaps in Key numbers; glossary +7 terms; open questions (+NCS cluster refusal, OE
  damper lengths, xi "what settles it"); Sources +5 BMW docs +2 owner's manuals; WIRING preamble xi pointer. research.md R1-R6
  APPLIED by me (R1 P1: stock-car FA_WRITE/Code Car caveat -> Session 8; R3 "wrecked its S54's bottom end"; R5 ride-height/
  alignment anchors; R6 TIS 12/2007 note). Fig 24-2 step 33 "Session 6 steps 2-5" -> dm-coding-b (queued).
  bmwclubmalaysia archived link (README 0840, WIRING 0520): notes mark the C05 dump [read] but give no URL; web.archive.org and
  the live forum unreachable here (reset/429). KEPT; not re-verified.
## dm-arches: fig 27 label "(front end ~375 up, 315 ahead)" + aria fixed, 0 issues.
## dm-coding-a: figs 41 (EWS holds VIN), 12 (option B session order; matched used DME; Tool32), 38, 06 fixed, 0 issues.
## rv-fluids DONE: ~160 facts, 15 sources via curl (WebFetch ENOTFOUND). K96 pin 2 = 87b (ST041 "87b and 30"; WDS pin 8 =
  "Terminal 87" coil supply). Filter-regulator: new filter on donor housing + regulator (new regulator only if test fails).
  P1 fixed: README 0210/0540/0380, Card 7a, WS 0196, fig 34 caption; README 0200 expansion-tank holder donor's. P2: Phase 7
  EVAP refit + Done-when; WIRING 0300 new belt; Phase 10 exhaust check relabelled. Requests APPLIED by me: R1 research.md;
  R2 0120; R3 0110+0320 (0.5 bar bleed-off, pins 6/2 X10157); R4 Card 1 + WS 0110; R5 0360 (+hedge "most likely ... our
  inference") + Card 5; R6 0430 + Card 12b; R8 0330; R9 0570; R10 0920. R7 Card 7b -> rv-chassis (queued). Backups:
  r4fold/rvfluids-apply-backup/. Figure fixes sent: dm-fuel (04, 34, 11 opt), dm-cool (37), dm-floor (29).
## rv-chassis DONE: ~190 facts, ~55 TIS/ETK pages via curl. P1: inner tie rod "100 + 10 Nm" (TIS 32 21 2AZ, every E46; 110 = Z4 M)
  -> value 110 kept, notes fixed (0390, 0500, Card 8b, WS 0230); 0610 Option B (M3 unit refuses Touring order) fixed; WIRING 0520
  bleed already fixed by rv-coding. Applied coordinator items (0240 xi sensors; 0610 5E1F; Card 7b canister R7). Requests APPLIED
  by me: R1 R3 (0870 tie rod + 4 "replace" rows), R2 (0920), R5 (0510, 0380 new nuts), R6 (0290), R7 (0070), R8 (0120), R9
  (research.md bleed row). R4 DECIDED: push rod 21 Nm (TIS 33 32 17AZ) over PS Designs 25 Nm (kept as note): applied 0870, 0460,
  0510; rv-chassis to apply Card 7b + WS 0220. Figs 13 (F1 P1) + 31 (F2) -> dm-chassis. Backups: r4fold/rvchassis-apply-backup/.
## rv-chassis R4 rows applied (Card 7b, WS 0220 = 21 Nm); no push-rod 25 Nm left except PS Designs notes (0460, 0870).
## dm-floor fig 29 canister rule (400x554); dm-cool fig 37 pusher "almost certainly not" (caption already "may need" X82: OK);
  dm-coding-b figs 39, 40, 26, 25, 25-2, 24-2 (steps 2-5; key-on adds DSC/ABS/yellow BRAKE; part 1 byte-identical). 0 issues.
## Stale scan after reviews: clean except research.md "M3 unit ... receives 325i values" -> FIXED by me (C06 PU02 AND S54B32,
  NCS refuses; link Session 5). "unladen" in 0519 = 540 CMR 6.03 measurement method (OK).
## dm-fuel: figs 04 (new filter on donor housing+regulator), 34 (donor housing/regulator; 'or its right hanger'), 11 (not pin 8). Done. ALL REVIEW FIXES IN -> final assembly.
## coordinator: 0120 cluster mileage correction -> 'sets a used cluster to your car's true mileage'. Final assembly into $G done; 28 captions verified; hard-limit grep clean.
## PUBLISHED: archeyon 501bded; public repo main ffe9818 (Pages run 3 success); artifact v7. Tasks 21/22/24 done.
