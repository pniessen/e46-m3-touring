# Requests from the coding-power writer (DME, EWS, DSC coding, adaptations, steering angle, readiness)

Requests to integrator fragments quote the guide's current text. Requests to other writers' fragments (front, susp, coding-body) quote their text as it stood when I wrote this (22 October 2026, 15:30); if the owner has since reworded the passage, apply the substance.

**Requests from others that I applied myself** (the integrator can skip them): front R27, R28 and R29 (when the INPA bleed is needed), fuel R24 and R27 (`TANK_KENNLINIE` left as read), susp R38 (Session 7 "When"), and cool R28, R29, R30, R31, R33, R34 and R35 (fan plug X82, heater valve, A/C compressor lock, fault 96), applied word for word, with °F added to R35.

## Conflicts

**C1. Rack curve on the Touring's own MK60 (my notes against the front notes).** My notes call `wert_02` the "closest" curve to the M3 rack, from a forum figure of about 13.7:1 for the 330i ZHP. The front notes read BMW USA's 2003 sheets: the 325i Sport Wagon is 13.7:1 too and the M3 15.4:1, so the M3 rack is slower than the Touring's and `wert_02` (the ZHP curve) isn't closer to it. I dropped the "closest" claim. Session 5 now says: leave the rack curve as coded; `touring_s` suits a faster rack, not the M3's. This matches the front writer's README text and their C3.

**C2. Clearing DME adaptations after a vehicle-order change (my notes against the coding-body notes).** My notes say any vehicle-order change means clearing the DME adaptations again. The coding-body notes say: only after an engine-side change (cruise or steering-wheel button wiring, A/C, fuel pump, gearbox), because the DME isn't coded from the vehicle order. I followed the coding-body notes, as the coordinator asked (intro, Session 6, worksheet). Card 12d (susp) and Session 8 (coding-body) need the same rule: R17 and R21.

**C3. Where to read the vehicle order for the DSC session (my notes against the coding-body notes).** My notes' Option B steps read the order "from AKMB", the M3 owners' method. The coding-body notes show that after the cluster swap AKMB can hold the donor's order, and that the EWS holds none on a car built from 09/2001. Session 5 now reads it from ALSZ.

**C4. M Track and `$7MA` (my notes against the coding-body notes).** My notes follow ECUWorx: write `$7MA` into the stored order with `FA_WRITE`, then default-code the cluster and MK60. The coding-body notes say: keep `$7MA` out of the stored order and set the values in coding files. Session 5 now adds `$7MA` to a session order only (no `FA_WRITE`), codes the MK60 with it, then corrects rack, brake and lamp values in the MK60's coding file and sets the cluster's `ANZEIGE_HOCHLADEN` in its own coding file.

**C5. NCS Expert version.** The guide said 3.0.x; the coding-body notes say 4.0.1 with a manipulation profile, and that 3.x doesn't run on 64-bit Windows. Applied in my fragments (Software, Tools and coding, coding kit, Electronics baseline).

**C6. M3 DME hardware numbers (within my notes).** RPM's list of DMEs it can delete runs from 7831815 to 7838802, but NAM3's list parsed from ISTA also has 7842559, 7842975, 7842569 and 7842981. Session 2 gives NAM3's list and tells you to ask the vendor about a later number, instead of calling one outside RPM's range "suspect".

**C7. `STAT_EKP_CFG_VERBAUT_WERT` (fuel).** The fuel writer put it in W&C "Faults that look like pump faults". My Troubleshooting intro and Session 6 mention it, labelled as an inference, and link there. I send no Phase 1 or open-question request for it (fuel note 6).

**C8. `TANK_KENNLINIE` (coding-body notes).** I changed Card 11b and the Coding sessions log to "left as read, checked against a measured fill". Coding-body's Session 4 table and Card 3f should say the same.

## README

### R1: README 0920__open-questions-to-verify.md: the M3 MK60 in a Touring, narrowed
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - Whether an M3 MK60 can be made to accept a Touring (one never cleared "VIN not initialized"), and its right session vehicle order and `BAUART_MK60` value.
- **New text:**
  > - Whether an M3 MK60, coded from a session vehicle order read from ALSZ and dated #0902 or later (with the donor's type code for that session only) and then initialised in INPA, clears "VIN not initialized" in a Touring. The one Touring that failed had only had a blank coding file and a PA-Soft reset. Neither MK60 has a body type for an M3 Touring: leave the M3 unit at `coupe_m` ([manual, Session 5](WIRING-AND-CODING.md#session-5-dsc-coding-and-vin)).
- **Why:** notes Q4 and correction 8: the failed case skipped the coding and the INPA initialisation (e46fanatics 1260275), and a late session date fixed an M3's MK60 (NAM3 173720).

### R2: README 0920__open-questions-to-verify.md: compensation routines answered
- **Change:** delete
- **Find (exact current text, for replace, delete or insert after):**
  > - The names of the other two MK60 compensation routines, and what the M Track option code `$7MA` stands for.
- **New text:**
  > (none)
- **Why:** answered. The routines are "Pressure Sensors" (`DRUCKSENSOR_DSC_ABGLEICHEN`) and "Lateral Acceleration Sensor" (`QUERBESCHLEUNIGUNG_DSC_ABGLEICHEN`), now in the manual's Session 5 table; `$7MA` is the Competition package's option code (ETK S7MAA), already in Session 5. Notes: correction 3. If coding-body sends a request for the same bullet, apply one.

### R3: README 0920__open-questions-to-verify.md: the US manual ("HS") numbers, narrowed
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - The US manual-gearbox ("HS") data-set numbers for an SMG-to-manual WinKFP flash.
- **New text:**
  > - Which US manual ("HS") assembly number WinKFP should flash to a given M3 DME. The latest in a table parsed from BMW's ISTA discs are about 7842973 for the MSS54 and 7842979 or 7842977 for the MSS54HP; check them against `MSS54.HIS` in your SP-Daten ([manual, Session 2](WIRING-AND-CODING.md#session-2-dme-vin-ews-delete-and-gearbox-software)).
- **Why:** notes Q1 and correction 4 (NAM3 2052 tables; the numbers are the table's last entries, not a tested flash).

### R4: README 0920__open-questions-to-verify.md: the DME VIN and mode 09, narrowed
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - Whether the US MSS54 reports its VIN to generic OBD-II scanners (mode 09).
- **New text:**
  > - Whether every US MSS54 answers a generic scanner's VIN request (mode 09), and from which model year the federal and California rules require it. BMW's SI B12 09 13 says state testers read the VIN stored in an E46 DME, so a DME with the full VIN written should report it.
- **Why:** notes Q3 and correction 6 ("strongly supported", not proven; the CFR and CARB clauses weren't opened).

### R5: README 0920__open-questions-to-verify.md: system checks and readiness, narrowed
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - Whether the MSS54's system-check jobs set a readiness monitor to "ready", or only test the hardware.
- **New text:**
  > - Whether the MSS54's system-check jobs can ever set a readiness monitor. They're BMW function checks that report pass or fail, and the readiness mask is a separate value the monitors set while driving, so we infer they don't; BMW doesn't say ([manual](WIRING-AND-CODING.md#checks-with-tool32-and-a-scanner)).
- **Why:** notes Q3 and correction 5 (inference from the job file and BMW ST041).

### R6: README 0920__open-questions-to-verify.md: the virgin-DME sync
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - A documented sync of a virginized MSS54 to another car's EWS3, and INPA's key path for it.
- **New text:**
  > - A first-hand, start-to-finish sync of a virginized MSS54 to another car's EWS3 (the one solved Tool32 case used a DME whose code had been written in through its programming port), and INPA's key path for it: Kassel's "Shift + F6, F1" clip is an M54 MS43 sync.
- **Why:** notes Q2 gaps and correction 9.

### R7: README 0920__open-questions-to-verify.md: VANOS limits, narrowed
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - BMW's limits for the MSS54 VANOS test jobs (`STEUERN_EVANOS1_VERSTELLZEIT`, `STEUERN_AVANOS1_VERSTELLZEIT`, `STEUERN_EVANOS1_DICHTHEIT` and `STEUERN_AVANOS1_DICHTHEIT`).
- **New text:**
  > - BMW's own limits for the MSS54 VANOS test jobs (`STEUERN_EVANOS1_VERSTELLZEIT`, `STEUERN_AVANOS1_VERSTELLZEIT`, `STEUERN_EVANOS1_DICHTHEIT` and `STEUERN_AVANOS1_DICHTHEIT`). Owners and ISTA give about 180–300 ms adjustment time (ISTA's limit 500 ms) and about ±5 °KW in the leak test ([manual, Session 6](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check)).
- **Why:** notes Q3 and correction 7.

### R8: README 0920__open-questions-to-verify.md: add the Touring MK60's coding index
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > - How a 325i-coded MK60 behaves with the M3's brakes, rack and limited-slip differential.
- **New text:**
  > - Your Touring MK60's coding index (control module 34526765455, hydraulic unit 34516765453), and which values it offers. The manual's list comes from one non-M unit at index C05, a 2002 318i's: no M3 body type, no M3 rack curve, but the M3's brake-pressure models.
- **Why:** notes Q4 gaps (the C05 dump is from a 318i; the Touring unit's index is unchecked).

### R9: README 0430__phase-12-front-end-first-start-and-shakedown.md: VANOS figures and the routines
- **Change:** replace (two sentences)
- **Find (exact current text, for replace, delete or insert after):**
  > 5. Still warm, run the VANOS timing and leak jobs (Session 6, step 7) and compare them with the donor's readings from Phase 1; BMW's limits weren't found.
- **New text:**
  > 5. Still warm, with the coolant at 85 °C (185 °F) or more, run the VANOS timing and leak jobs (Session 6, step 7) and compare them with the donor's readings from Phase 1. BMW publishes no limits; owners and ISTA give about 180–300 ms adjustment time (ISTA's limit 500 ms) and a leak test within about ±5 °KW, with no "weggedriftet" status ([manual](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check)).
- **Find (second):**
  > and run the DSC compensation routines, with the wheel straight, no pressure on the brake and the car level
- **New text (second):**
  > and run the other two DSC compensation routines, pressure sensors and lateral acceleration, with the wheel straight, no pressure on the brake and the car level
- **Why:** notes Q3 (VANOS, owner and ISTA figures, labelled) and Q4 (routine names).

### R10: README 0320__phase-1-buy-and-inspect-the-donor.md: VANOS figures
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - **VANOS:** Tool32's timing and leak tests on a warm engine, to compare with after the refresh ([MSS54 job reference](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).
- **New text:**
  > - **VANOS:** Tool32's timing and leak tests on a warm engine, coolant at 85 °C (185 °F) or more, to compare with after the refresh ([MSS54 job reference](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)). Owners and ISTA, not BMW, put a healthy adjustment time at about 180–300 ms (ISTA's limit 500 ms) and the leak test within about ±5 °KW; a status reading "weggedriftet" means the VANOS leaks ([manual, Session 6](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check)).
- **Why:** notes Q3 and correction 7. Gives the buyer a pass value at the donor.

### R11: README 0900__key-numbers.md: VANOS tests
- **Change:** add row (after the "S54 rod-bearing oil clearance" row, or wherever engine rows sit)
- **New text:**
  > | VANOS tests (Tool32, warm: coolant 85 °C / 185 °F or more) | Adjustment time about 180–300 ms, ISTA's limit 500 ms; leak test within about ±5 °KW of target, no "weggedriftet" status. Owner and ISTA figures, not BMW's. BMW's adjustment ranges: 60° intake, 45° exhaust | [NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/34304-need-help-doing-vanos-test-with-inpa), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/253994-dis-vanos-test-results-leak-help), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/88778-failed-vanos-test-post-beisan), [BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine.pdf) |
- **Why:** notes Q3; same figures as the manual's Session 6.

### R12: README 0630__troubleshooting.md: DSC row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | DSC lamp with "VIN not initialized" | VIN and steering angle not initialised, or an M3 MK60 that won't accept the Touring | [DSC, brakes and steering angle](#dsc-brakes-and-steering-angle) |
- **New text:**
  > | DSC lamp with "VIN not initialized" | VIN and steering angle not initialised; or an M3 MK60 not yet coded from a late enough session vehicle order, or reset in PA-Soft instead of initialised in INPA | [DSC, brakes and steering angle](#dsc-brakes-and-steering-angle), [manual, Session 5](WIRING-AND-CODING.md#session-5-dsc-coding-and-vin) |
- **Why:** correction 8 (e46fanatics 1260275; NAM3 173720).

### R13: README 0910__glossary.md: two coding terms
- **Change:** add row (two rows, in alphabetical place: "HS" after "GM5"; "ZB number" at the end)
- **New text:**
  > | HS | Handschaltung, manual gearbox: the mark of US manual software in BMW's DME data-set names, such as "E46-M3-USA-HS" |
  > | ZB number | The assembly (Zusammenbau) number of a DME software data set, which WinKFP flashes and the DME's VIN slots record |
- **Why:** both terms now appear in the manual's Session 2 (notes Q1).

### R14: README 0790__factory-documentation.md: the DSC sources
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > with every Tool32 job, status bit and fault number the manual uses ([MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).
- **New text:**
  > with every Tool32 job, status bit and fault number the manual uses ([MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md), [DSC_MK60](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC_MK60.md), [EWS3](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/EWS3.md)).
- **Find (second):**
  > ST040 [bus troubleshooting](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/9%20Bus%20System%20Troubleshooting.pdf);
- **New text (second):**
  > ST040 [bus troubleshooting](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/9%20Bus%20System%20Troubleshooting.pdf) and [DSC](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/6%20DSC%202010-30-00.pdf);
- **Why:** the manual now cites these for the MK60 routines and their "when". The susp writer's R39 also edits this fragment; merge.

### R15: README 0840__forum-threads-by-topic.md: coding threads
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > [MK20 to MK60 swap](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap)
- **New text:**
  > [MK20 to MK60 swap](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap), [MK60 VIN issue on an M3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/173720-mk60-vin-issue-m3-track-mode-rabbit-hole) (the session production date), [a non-M MK60's coding options](https://web.archive.org/web/20241209032101/http://www.bmwclubmalaysia.com/forums/threads/ncs-expert-brief-walkthrough-and-available-parameters-2002-e46-318i-ckd.30039/) (a 2002 318i, coding index C05, archived)
- **Second change:** add a new bullet after the "EWS:" bullet:
  > - Engine tests: [VANOS test with Tool32](https://nam3forum.com/forums/forum/special-interests/coding-tuning/34304-need-help-doing-vanos-test-with-inpa), [DIS VANOS results](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/253994-dis-vanos-test-results-leak-help), [failed VANOS test](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/88778-failed-vanos-test-post-beisan)
- **Why:** the manual's Sessions 5 and 6 now rest on these.

## JOB-CARDS

### R16: JOB-CARDS 0020__card-1-buy-and-inspect-the-donor.md: VANOS pass figures
- **Change:** replace (two lines)
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Tool32 VANOS timing and leak tests, warm; fuel pressure through a relay bypass</span>
- **New text:**
  > - [ ] <span>Tool32 VANOS timing and leak tests, coolant 85 °C or more; fuel pressure through a relay bypass</span>
- **Find (second):**
  > | VANOS and fuel | VANOS tests recorded; fuel pressure 5.0 ± 0.2 bar (72.5 ± 2.9 psi) | |
- **New text (second):**
  > | VANOS and fuel | VANOS adjustment about 180–300 ms (ISTA's limit 500 ms), leak within about ±5 °KW, no "weggedriftet" (owner and ISTA figures, not BMW's); fuel pressure 5.0 ± 0.2 bar (72.5 ± 2.9 psi) | |
- **Why:** notes Q3 and correction 7. The fuel writer's R20 edits the same task line; merge.

### R17: JOB-CARDS 0290__card-12d-alignment-and-final-coding.md (susp): the routines and the adaptation rule
- **Change:** replace (two places)
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>DSC compensation routines run; faults cleared and read again</span>
- **New text:**
  > - [ ] <span>Then the other two DSC compensation routines, pressure sensors and lateral acceleration, foot off the brake and the car still (Tool32: `LENKWINKEL_DSC_ABGLEICHEN` and the two others in `DSC_MK60.PRG`); faults cleared and read again</span>
- **Find (second):**
  > If you change the vehicle order, code the other modules one at a time and reset the DME adaptations again.
- **New text (second):**
  > If you change the vehicle order, code only the modules it touches, one at a time, never with Code Car; clear the DME adaptations again only if the change touches the engine side.
- **Why:** notes Q4 (routine names and Tool32 jobs, correction 1); coding-body notes via the coordinator (adaptations only after engine-side changes; never Code Car). See C2.

### R18: JOB-CARDS 0270__card-12b-first-start.md: VANOS pass figures
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Warm VANOS jobs (Session 6, step 7) compared with the donor's Card 1 readings</span>
- **New text:**
  > - [ ] <span>VANOS jobs at 85 °C or more (Session 6, step 7): adjustment about 180–300 ms (ISTA's limit 500 ms), leak within about ±5 °KW, no "weggedriftet"; compared with the donor's Card 1 readings</span>
- **Why:** notes Q3 and correction 7 (owner and ISTA figures; Session 6 labels them).

## WORKSHEETS

### R19: WORKSHEETS 0110__vanos-tests.md: pass figures
- **Change:** replace (the intro sentence and the first table)
- **Find (exact current text, for replace, delete or insert after):**
  > Warm, after `STEUERN_LLS_TESTDREHZAHL` (raised idle), as in [Session 6](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check), step 7. No BMW limits were found: compare after the refresh.
  >
  > | Test | Donor (Phase 1) | After the refresh (Phase 12) |
  > |---|---|---|
  > | Rattle at warm idle | | |
  > | `STEUERN_EVANOS1_VERSTELLZEIT` | | |
  > | `STEUERN_AVANOS1_VERSTELLZEIT` | | |
  > | `STEUERN_EVANOS1_DICHTHEIT` | | |
  > | `STEUERN_AVANOS1_DICHTHEIT` | | |
  > | VANOS faults stored | | |
  > | Exhaust-hub tabs and oil-pump disc, valve cover off, if the seller allows | | — |
- **New text:**
  > Warm, with the coolant at 85 °C (185 °F) or more, after `STEUERN_LLS_TESTDREHZAHL` (raised idle for the test), as in [Session 6](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check), step 7. BMW publishes no limits; the healthy figures are from owners and ISTA. Compare after the refresh.
  >
  > | Test | Healthy (owners and ISTA, not BMW) | Donor (Phase 1) | After the refresh (Phase 12) |
  > |---|---|---|---|
  > | Rattle at warm idle | None | | |
  > | `STEUERN_EVANOS1_VERSTELLZEIT`, advance and retard (ms) | About 180–300 ms; ISTA's limit 500 ms | | |
  > | `STEUERN_AVANOS1_VERSTELLZEIT`, advance and retard (ms) | About 180–300 ms; ISTA's limit 500 ms | | |
  > | `STEUERN_EVANOS1_DICHTHEIT`: target, actual (°KW) and status | Within about ±5 °KW; no "weggedriftet" | | |
  > | `STEUERN_AVANOS1_DICHTHEIT`: target, actual (°KW) and status | Within about ±5 °KW; no "weggedriftet" | | |
  > | VANOS faults stored | None | | |
  > | Exhaust-hub tabs and oil-pump disc, valve cover off, if the seller allows | Tabs intact, disc sound | | — |
- **Why:** notes Q3 and correction 7. The two fillable columns stay last. The fuel writer's R25 edits the fuel-pressure line below this table; no overlap.

## WIRING-AND-CODING (other writers)

### R20: WIRING-AND-CODING 0660__warning-lights.md (coding-body): the M3 MK60 cause
- **Change:** replace (two phrases in the "ABS, DSC, brake" row)
- **Find (exact current text, for replace, delete or insert after):**
  > 4. An M3 MK60 that won't accept the Touring.
- **New text:**
  > 4. An M3 MK60 not yet coded from a late enough session vehicle order, or reset in PA-Soft instead of initialised in INPA.
- **Find (second):**
  > refit your Touring's MK60 ([e46fanatics](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/))
- **New text (second):**
  > an M3 unit that still won't initialise: refit your Touring's MK60 ([e46fanatics](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/))
- **Why:** correction 8. Figure 13 (26-flow-warning-lights.svg) carries the same "won't accept the Touring" wording; reported to the diagram makers.

### R21: WIRING-AND-CODING 0550__session-8-vehicle-order-changes-and-body-modules.md (coding-body): adaptations and Code Car
- **Change:** replace (apply only what your own notes haven't already changed)
- **Find (exact current text, for replace, delete or insert after):**
  > 7. Reset the DME adaptations (Session 6).
- **New text:**
  > 7. Clear the DME adaptations (Session 6) only if the change touches the engine side, such as the cruise buttons or the A/C. A cluster or light option doesn't need it.
- **Why:** coding-body notes takeaway 10, which the manual's intro and Session 6 now follow. Session 8's step 5 (Process Car → Code Car) conflicts with "never Code Car" in Sessions 5 and 6 and in Tools and coding; the coding-body notes drop it.

## README (front)

### R22: README 0610__dsc-brakes-and-steering-angle.md (front): option B's session order, Code Car, M Track and tires
- **Change:** replace (three places)
- **Find (exact current text, for replace, delete or insert after):**
  > An M3 MK60 codes only from a vehicle order whose production date suits its coding index: use 09/2002 or later for the coding session, then run INPA's VIN and steering-angle initialisation.
- **New text:**
  > An M3 MK60 codes only from a vehicle order whose production date suits its coding index: use 09/2002 or later for the coding session, then run INPA's VIN and steering-angle initialisation. Read that order from your light module (ALSZ), not the cluster, whose memory can hold the donor's order after the swap, and don't write the changed order back (no `FA_WRITE`). Once the unit is coded, keep its final coding file and never run Code Car or write a blank coding file to it: either wipes the hand-set M3 values ([manual, Session 5](WIRING-AND-CODING.md#session-5-dsc-coding-and-vin)).
- **Find (second):**
  > - **M Track,** switched on by coding and worked by the existing DSC button. A cluster with the M Track symbol is optional ([ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf)).
- **New text (second):**
  > - **M Track,** switched on by coding and worked by the existing DSC button. A cluster with the M Track symbol is optional ([ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf)). Set it in the MK60's and the cluster's coding files and keep `$7MA`, the Competition package's code, out of your stored vehicle order ([manual, Session 5](WIRING-AND-CODING.md#session-5-dsc-coding-and-vin)).
- **Find (third):**
  > So "M3 values" on your unit means editing its brake and intervention parameters by hand, not changing its body type ([manual, Session 5](WIRING-AND-CODING.md#session-5-dsc-coding-and-vin)).
- **New text (third):**
  > So "M3 values" on your unit means editing its brake and intervention parameters by hand, not changing its body type ([manual, Session 5](WIRING-AND-CODING.md#session-5-dsc-coding-and-vin)). There's no tire-size setting either: after fitting the M3 wheels, set the pressures and reset the flat-tire warning, if it's on (Tool32 `RPA_RESET`).
- **Why:** coding-body notes via the coordinator (ALSZ as the order source; never Code Car; `$7MA` out of the stored order); notes Q4 (no tire-size code; `RPA_RESET` in the MK60 job file).
