# rv-ref: round-4 review of the reference layer

Scope: README Appendix (0860–0940), Sources (0770–0850), the shared job cards (0, 1, 2a, 3a–3e, 4, 9a, 9b, 12a–12c, 13) and worksheets (baseline, donor, S54 refresh, torque log intro and Phases 3, 9, 12, fluids log, power-up checks, first start, break-in, inspection), the WIRING preamble and power-up checks (0400–0460), and research.md's new round-4 section.

## Checked

- About 150 facts: every torque row in the Appendix against all 31 job cards and the six torque logs (a script compared about 190 card and log rows with the table, and I read every weak match by hand; no value differs); every fluid row against the fluids log and the cards' fluid rows; the Key numbers rows new this round (ride heights, mount spacing, weights, axle ratings, tire pressures, spring heights, damper lengths, brake test values, unit conversions); the glossary's new terms; every open question against the notes' "Still open" lists; the Sources lists against every BMW training document, owner's manual and build the pages cite; card growth (all within 40%), Done-when Reading columns and worksheet table shapes; links, `\$` escapes and table cells in all 65 fragments.
- Leftovers of replaced values: none found on any page for 24 Nm strut tops, 1.9 L or 2.0 US qt gearbox oil, CHF 11S as the fill, "unladen", "loaded ride height", TIS 51 00 or "100 + 10" as the tie-rod value.
- Spot-checked at the source (8): BMW ST040 4wd PDF (NV 124: 0.24 L MTF-LT1 83229408942, plugs 33 Nm, 38:62, 300 Nm); TIS 31 31 1AZ (E46 21 mm-flange nut, replace, 34 Nm; rod nut 64 Nm); TIS 51 71 3AZ and 31 10 8AZ (59 Nm + 90°, +30°, rear screws first); TIS 33 00 M3 rear ride height (587/600 mm, ±10 / ±2 mm) and TIS 32 00 M3 normal position (2 × 68 kg, 14 kg, full tank); TIS 41 00 gap dimensions p.2 (rear door to side wall 4 ± 0.75 mm, etc.); TIS 41 00 rear top view drawing R41 1103 (E–E 440 ahead of the spring seats, F–F 660 behind them); TIS 34 51 (pressure sensors V and H 25 + 5 Nm, pulse generator 8 Nm); 2003 US M3 convertible owner's manual p.153 on archive.org (gearbox 1.9 qt / 1.8 L, coolant 9.8 / 9.3, diff 1.2 / 1.1, reserve 2.1 gal / 8 L).

## Fixed in my fragments

1. **0900 Key numbers:** added BMW's E46 door gaps (TIS 41 00: rear door to side wall 4 ± 0.75 mm, front to rear door 4.5 ± 0.75, front side wall to front door 4.25 ± 0.75, sill 5 ± 1, parallel within 1 mm). The E–E/F–F row now says which pair is which from BMW's drawing, not only from the H–E/H–F distances.
2. **0910 Glossary:** added Code Car, DSC 5.7, NV 124, option code (`$203`, `$7MA`), SP-Daten, type key and VECI label. ALSZ, design and normal position and MK60 were already there.
3. **0920 Open questions:**
   - New gaps: a first-hand NCS refusal of an M3 cluster with a Touring order (the guide's rule rests on coding data; Session 4 step 4 settles it); OE rear damper lengths (the guide uses Bilstein equivalents); the block drain plug's single-owner 24 Nm joins the single-source torque item.
   - The new 325xi group now says what settles each item, as the section's intro promises.
   - Answered list: the M3 MK60's session order and the cluster keeping the donor's order.
   - Applied rv-plan R3 (AW33 on a pre-09/2001 xi), merged with the settle clause.
   - The A/C pulley question was already there (Cooling and A/C); kept as written.
4. **0790 Sources:** listed the BMW documents this round cites that were missing: ST055 fuel management and emissions overview, ST034 engine management, ST054 outputs, ST040 E46 IHKR; the 2003 US sedan manual (the M54's 8.4 L) and the archive.org copy of the 2003 M3 convertible manual (the 420G's 1.8 L).
5. **0780 Start here:** item 5 now says JMCCRNA's thread is a 2003 325xi made rear-drive. **0940:** names the two 325xi notes.
6. **WIRING 0000:** one sentence sends a 325xi owner to the route choice first.
7. **Cards and worksheets:**
   - Fluids log: the A/C oil rule now includes about 60 ml for a new condenser or evaporator, as README's Air conditioning does.
   - Card 3a and the Phase 3 log: US units on the M10 rod-bolt cycle.
   - Inspection day and Card 13: the brake run in metric first, and the red BRAKE lamp out with the parking brake released (540 CMR 4.04(4)).
   - Card 12c and the break-in log: 400 m (440 yd).
   - Baseline record: links the 325xi chapter.
8. **Applied from rv-body:**
   - R1, 0900 plug-weld row: added the arch lip's 6 mm thin-to-thin hole (face 8–10 mm, 3–8 mm tear-out), with BMW TIS 41 00 and I-CAR practice-guide links. The values match `rear_floor_exhaust.md` (I-CAR practice welding guide) and the guide's coupon table.
   - R2, 0920 answered list: split the links. Prices go to Rear arches and doors, the gaps to Rear doors, and the control dimensions to Phase 5 and Key numbers. Checked in the preview: Rear arches and doors holds neither the gaps nor the control dimensions.

## Requests

### R1: research.md (line 177, "Vehicle order and the FSW_PSW.MAN workflow"): the stock-car FA procedure contradicts the build's rule (P1, research-page writer)
- **Change:** insert after
- **Find (exact current text):**
  > finally reset the DME adaptations ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-fa-for-at-mt-swap.1290835/); [50sKid, 26:05](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1565s)).
- **New text:**
  > That's the method for a stock car. In this conversion the M3 cluster keeps the donor's order, so write order changes to ALSZ only, code only the modules a change touches, one at a time, and never run Code Car or default-code the cluster (fourth round; [Session 8](WIRING-AND-CODING.md#session-8-vehicle-order-changes-and-body-modules)).
- **Why:** the paragraph tells the reader to `FA_WRITE` into AKMB and run Code Car. The guide now forbids both for this car (WIRING Session 4 steps 4–6 and Session 8; README 0610). `gapfill_coding_body.md` gap 10: an M3 cluster accepts only an M3 order. The same paragraph's last sentence, "Writing an empty `.man` file restores a module's default coding", is the default coding that Session 4 forbids on the M3 cluster; the inserted sentence covers it.

### R2: research.md (line 279, video table, 50sKid row): same contradiction (P3, research-page writer)
- **Change:** replace
- **Find (exact current text):**
  > his ZCS example at [04:45](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=285s) is wrong and is corrected at [30:12](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1812s) |
- **New text:**
  > his ZCS example at [04:45](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=285s) is wrong and is corrected at [30:12](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1812s). A stock car's method: this build writes no order into the M3 cluster and never runs Code Car ([Session 8](WIRING-AND-CODING.md#session-8-vehicle-order-changes-and-body-modules)) |
- **Why:** as R1; the row lists `FA_WRITE` to AKMB and Code Car without a caveat.

### R3: research.md (line 15, round-4 bullet "A 325xi can be done either way"): "lost its S54" overstates (P2, research-page writer)
- **Change:** replace
- **Find (exact current text):**
  > and one of the two documented cars lost its S54 through the oil system
- **New text:**
  > and one of the two documented cars wrecked its S54's bottom end through the oil system
- **Why:** the engine was rebuilt with a re-made pan and ran 1,600 trouble-free miles (`xi_keep_awd.md` section 7; FCP Euro part 2). README 0050 and 0080 say "wrecked the bottom end".

### R4: research.md (line 13, round-4 bullet "The M3 flare is a profile"): ambiguous phrase (P3, research-page writer)
- **Change:** replace
- **Find (exact current text):**
  > so the shell can take no donor steel at all
- **New text:**
  > so the shell can be built without any donor steel
- **Why:** "can take no donor steel" reads as "can't accept donor steel". README 0070 says "so no donor steel goes into your body".

### R5: research.md (line 12, round-4 bullet "BMW measures ride height and alignment loaded"): point at the sections that hold the figures (P3, research-page writer)
- **Change:** replace
- **Find (exact current text):**
  > with tables for the Touring by suspension and wheel size ([Suspension for Touring weight](README.md#suspension-for-touring-weight)).
- **New text:**
  > with tables for the Touring by suspension and wheel size ([Ride height: BMW's method and figures](README.md#ride-height-bmws-method-and-figures), [Wheel alignment](README.md#wheel-alignment)).
- **Why:** both anchors exist in the preview; the bullet covers alignment too.

### R6: research.md (line 97, note under the torque table): out of date since round 4 read TIS (P3, research-page writer)
- **Change:** replace
- **Find (exact current text):**
  > *Only the flywheel, rod-bolt, SI and guibo rows are traced to BMW documents; the rest agree across at least two TIS-citing compilations or vendor procedures, since the TIS mirrors themselves were blocked.*
- **New text:**
  > *Only the flywheel, rod-bolt, SI and guibo rows were traced to BMW documents at first; the rest agree across at least two TIS-citing compilations or vendor procedures. The fourth round read BMW's TIS (issue 12/2007) and confirmed the reinforcement plate: new screws, rear row first, 59 Nm + 90° ([TIS 31 10 8AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/31__front_axle/10__front_axle_suspension/1_azd__front_axle_suspension/page_3534/)); the guide's [Torque values](README.md#torque-values) give TIS sources row by row.*
- **Why:** `gapfill_bmw_chassis_body.md` gaps 3–4; README 0870 now cites TIS 12/2007 throughout.

## Figure fixes (for the diagram makers)

### F1: `24-flow-power-up-2.svg` (WIRING Figure 10): step 33 cites the old Session 6 steps (P2)
- **What's wrong:** the step-33 box reads "Then Session 6 / steps 2–4", and the `aria-label` says "run Session 6 steps 2 to 4". This round changed step 33 to Session 6 steps 2–5, which adds the clutch, brake and Sport bit check (WIRING 0460, WORKSHEETS 0400, README Phase 12, Card 12b).
- **Exact fix:**
  - Visible text: "steps 2–4" → "steps 2–5".
  - `aria-label`: "run Session 6 steps 2 to 4; STATUS_ADAPTIONSBLOCK_06, STAT_WDK_ADAPT_WERT must read 0" → "run Session 6 steps 2 to 5; STATUS_ADAPTIONSBLOCK_06, STAT_WDK_ADAPT_WERT must read 0, and the clutch, brake and Sport bits respond".
- **Optional (P3):** the key-on box "Oil-pressure, charge and check-engine lamps lit" could add "DSC, ABS and BRAKE lamps on until Session 5", matching step 23. Make the same change in the `aria-label` after "check-engine lamps are lit".

## Not verified

- The archived bmwclubmalaysia MK60 parameter list (0840 and WIRING 0520) can't be opened: web.archive.org resets every connection here, and its URL appears in no round-4 note. The note cites the dump without a link. The coding reviewer should confirm the URL or drop the link.
- BMWPartsDeal prices and the BaT result weren't re-checked; rv-plan checked BaT.
