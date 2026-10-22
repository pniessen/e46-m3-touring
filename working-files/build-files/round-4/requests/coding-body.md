# Requests from the coding-body writer (vehicle order, cluster, light module, switch centre, body modules)

Requests to integrator fragments quote the guide's current text. Requests to coding-power's and susp's fragments quote their text as it stood at 15:45 on 22 October 2026; if the owner has since reworded the passage, apply the substance.

**Requests from others that I applied myself** (the integrator can skip them):

- coding-power R20 (Warning lights, the M3 MK60 cause) and R21 (Session 8, adaptations and Code Car): applied; Code Car is gone from Session 8 and has a warning instead.
- cool R36 (Session 8, the compressor transport lock): applied word for word as a paragraph under Session 8's body-module table, with the job files written `IHKR46.PRG` and `IHKA46.PRG`.
- front R26 (Warning lights, brake-lamp colours): applied, with the 5D90–5DC5 wording; the red BRAKE lamp now has its own row and an intro paragraph.
- fuel R14 (README cluster section, tank senders and job name): applied, with "(62.8 L)" and a link to [Choose the pump route](#choose-the-pump-route); the curve bullet now says leave `TANK_KENNLINIE` as read.
- fuel R28 (Warning lights, fuel-gauge row): applied word for word.
- fuel R29 (Session 4, tank curve row): my own rewrite already says "As read", with the same reasoning.

**New sections I created** (link targets other requests use): `WIRING-AND-CODING/0471__ncs-expert-basics.md` ("NCS Expert basics", anchor `#ncs-expert-basics`: setup, screen map, the coding-file rules and the full message table) and `WIRING-AND-CODING/0241__steering-wheel-buttons-mfl.md` ("Steering-wheel buttons (MFL)", anchor `#steering-wheel-buttons-mfl`). coding-power's Tools and coding table already links to the first.

## Conflicts

**C1. Vehicle-order source, Code Car, `$7MA`, NCS Expert version and adaptations (coding-power notes against mine).** coding-power's notes follow the M3 owners: read the order from AKMB (or EWS), write `$7MA` with `FA_WRITE`, default-code AKMB, Code Car after an order change, NCS Expert 3.0.x, and clear DME adaptations after any order change. My notes show AKMB holds the donor's order after a chip route, the EWS holds none from 09/2001, the M3 cluster must never be default-coded, 3.x doesn't run on 64-bit Windows, and adaptations need clearing only after engine-side changes. coding-power has already applied all of this in its fragments (its C2–C5); my sessions match.

**C2. The switch centre's job file (my notes against the job file itself).** My notes say `SZM46.PRG` has "only `IDENT`, `FS_LESEN`, `IS_LESEN` and `CODIERUNG_LESEN`". The job-file documentation also lists `STATUS_IO` and `STEUERN_IO`, so the manual's existing `STATUS_IO` test stands. Either way there's no job that writes its coding, which is what the "no coding" statement rests on.

**C3. Massachusetts brakes row (README 0730, integrator).** "A DSC or ABS fault that lights the red lamp fails" contradicts BMW ST056: DSC and ABS faults light the yellow lamp; red means low fluid or the parking brake. front R15 corrects it; my Warning lights section now follows ST056.

---

## coding-power fragments

### R1: README 0260__electronics.md (coding-power): the cluster brings the donor's vehicle order; the switch unit needs no coding
- **Change:** replace (two places)
- **Find (exact current text, for replace, delete or insert after):**
  > Or use a cluster service ([Shop briefs](#shop-briefs)) |
- **New text:**
  > The new chip brings back the donor's vehicle order as well; the manual's Session 4 copies yours from the light module ([manual](WIRING-AND-CODING.md#session-4-cluster-and-light-module)). Or use a cluster service ([Shop briefs](#shop-briefs)) |
- **Find (second):**
  > Optional, for the Sport button; your 325i's (61316925498) has none ([ETK: convertible](https://bmwfans.info/parts-catalog/61316925521/)).
- **New text (second):**
  > Optional, for the Sport button; a 325i Touring's switch unit has none (61316925498 without DSC; the number with DSC wasn't found) ([ETK: convertible](https://bmwfans.info/parts-catalog/61316925521/), [ETK: Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_electrical_system/switch_unit_center_console/)). It needs no coding: NCS Expert has no entry for it ([manual](WIRING-AND-CODING.md#sport-button-and-switch-center)).
- **Why:** notes Takeaway 1 (the cluster's EEPROM carries the FA; "the VO is brought back onto the new Chip", NAM3 154645) and §4 (SZM46 has no coding-write job; the ETK 325iT page is filtered to "DSC: No").

### R2: README 0560__deep-dive-electronics-and-coding.md (coding-power): the yellow BRAKE lamp, and the order check in Session 4
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > In one 330Ci the DSC and parking-brake lamps went out only once the M3 cluster carried the car's VIN
- **New text:**
  > In one 330Ci the DSC and yellow BRAKE lamps went out only once the M3 cluster carried the car's VIN
- **Find (second), end of the same step 5:**
  > "complained that the vin was not a match" with the cluster ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/173720-mk60-vin-issue-m3-track-mode-rabbit-hole)).
- **New text (second):**
  > "complained that the vin was not a match" with the cluster ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/173720-mk60-vin-issue-m3-track-mode-rabbit-hole)). Session 4 also checks which vehicle order the cluster holds: a chip-route cluster brings the donor's, so read the order from the light module until yours is back in the cluster ([manual](WIRING-AND-CODING.md#session-4-cluster-and-light-module)).
- **Why:** BMW ST056 via the front notes (DSC faults light the yellow BRAKE lamp; red is fluid or the parking brake); my notes Takeaway 1.

### R3: README 0420__phase-11-wiring-immobilizer-and-coding.md (coding-power): step 11, the vehicle order in the cluster
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > On a pre-09/2001 (ZCS) car the LCM may not pass the mileage across, so check ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)).
- **New text:**
  > On a pre-09/2001 (ZCS) car the LCM may not pass the mileage across, so check ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)). Then check which vehicle order the cluster holds: after a chip route it's the donor M3's order, so copy yours from the LCM into it, or keep the LCM as your only source, and code the cluster only from its own coding file ([Session 4](WIRING-AND-CODING.md#session-4-cluster-and-light-module)).
- **Why:** notes Takeaway 1 and 3.

### R4: WIRING-AND-CODING 0240__clutch-switch-gear-switch-and-cruise.md (coding-power): pointer to the MFL retrofit
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - the steering-wheel buttons' data line, X60004 pin 27 (0.35 BL/SW), unchanged: the right-hand buttons reach the DME on one serial wire through the clock spring ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf));
- **New text:**
  > - the steering-wheel buttons' data line, X60004 pin 27 (0.35 BL/SW), unchanged: the right-hand buttons reach the DME on one serial wire through the clock spring ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)). A Touring without steering-wheel buttons gets this wire from BMW's three-wire retrofit, with no coding ([Steering-wheel buttons (MFL)](#steering-wheel-buttons-mfl));
- **Why:** notes §5 and G7 (BMW EBA 01 29 0 023 076: X10170 pin 8 → X60004 pin 27; "Coding of the vehicle must not be carried out").

### R5: WIRING-AND-CODING 0110__x60004-pin-by-pin.md (coding-power): pin 27 row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | 27 | Cruise buttons: serial data from the steering wheel (0.35 BL/SW) |
- **New text:**
  > | 27 | Cruise buttons: serial data from the steering wheel (0.35 BL/SW). A Touring without steering-wheel buttons gets this wire from BMW's retrofit ([Steering-wheel buttons (MFL)](#steering-wheel-buttons-mfl)) |
- **Why:** as R4; the wiring line for X60004 that the MFL retrofit adds. Skip if R4 is enough for you.

### R6: WIRING-AND-CODING 0470__coding-step-by-step.md (coding-power): point to NCS Expert basics
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Keep the charger on for every session, and run one program at a time.
- **New text:**
  > Keep the charger on for every session, and run one program at a time. Set NCS Expert up before Session 1: the version, a manipulation profile, the coding file, the data files and what each error message means are in [NCS Expert basics](#ncs-expert-basics), the next section.
- **Why:** the new section sits between this one and Session 1 (my fragment 0471).

### R7: JOB-CARDS 0250__card-11b-power-up-and-coding.md (coding-power): the vehicle order after the cluster swap
- **Change:** insert after, and add row
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Cluster coded from its own edited file, never default-coded: its three lamp switches `nicht_aktiv`; `TANK_KENNLINIE` left as read, checked later with a measured fill</span>
- **New text:**
  > - [ ] <span>Vehicle order: AKMB reads the same as ALSZ after `FA_WRITE`, or the ALSZ-only rule written on your coding sheet ([Session 4](WIRING-AND-CODING.md#session-4-cluster-and-light-module))</span>
- **Find (second, insert after this Done-when row):**
  > | Cluster | Shows your car's true mileage (compare with your Card 0 photo), with no tamper dot | |
- **New text (second):**
  > | Vehicle order | NCS Expert reads the same order from ALSZ and AKMB, or the ALSZ-only rule is noted | |
- **Why:** notes Takeaway 1, G4 step 6.

### R8: WORKSHEETS 0410__coding-sessions-log.md (coding-power): Sessions 4 and 9
- **Change:** replace (two rows)
- **Find (exact current text, for replace, delete or insert after):**
  > | 4. Cluster and light module | Options edited, not default-coded: `CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN` and `TOG_UEBER_CAN` = `nicht_aktiv`, with the three lamp wires in place; `TANK_KENNLINIE` left as read and checked against a measured fill. No tamper dot; your true mileage, matching the Phase 0 photo | | |
- **New text:**
  > | 4. Cluster and light module | Coded from its own complete coding file, never default-coded: `CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN` and `TOG_UEBER_CAN` = `nicht_aktiv`, with the three lamp wires in place; `TANK_KENNLINIE` left as read and checked against a measured fill; the re-read matches the coding file. No tamper dot; your true mileage, matching the Phase 0 photo. The order in AKMB matches ALSZ, or the ALSZ-only rule is on your coding sheet | | |
- **Find (second):**
  > | 9. Light module and headlights | Lights work as fitted; headlights aimed at ride height | | |
- **New text (second):**
  > | 9. Light module and headlights | Halogen: no lamp faults in `LSZ_2.PRG` → `FS_LESEN`. Xenon: `XENON_VORHANDEN` and `LWR_VORHANDEN` report present; both level-sensor voltages between 0 and 5 V and changing with load; the lamps re-level within about 15 s of loading each end. Headlights aimed at ride height | | |
- **Why:** notes G4 steps 5–6 and G6 steps 7–8 (BMW EBA load test, "delay approx. 15 seconds").

### R9: WORKSHEETS 0060__coding-backups-log.md (coding-power): both order copies, NETTODAT, the other modules
- **Change:** replace (three rows) and add row (two rows)
- **Find (exact current text, for replace, delete or insert after):**
  > | FA or ZCS screenshots: VIN, options, production date, type code (NCS Expert) | | | | | |
- **New text:**
  > | FA or ZCS screenshots from ALSZ and AKMB: VIN, options, production date, type code (NCS Expert) | | | | | |
- **Find (second):**
  > | Cluster coding, KMB or AKMB, `FSW_PSW.TRC` (NCS Expert) | | | | | |
- **New text (second):**
  > | Cluster coding, KMB or AKMB, `FSW_PSW.TRC` and `NETTODAT.TRC` (NCS Expert) | | | | | |
- **Insert after:**
  > | Climate-control coding, IHKA or IHKR (NCS Expert) | | | | | |
- **New row:**
  > | Airbag (MRS), steering-angle sensor (LWS) and park distance control (PDC) coding, if fitted (NCS Expert) | | | | | |
- **Find (third):**
  > | Donor vehicle order: type code and production date, for an M3 DSC (option B) only (NCS Expert) | | | | | |
- **New text (third):**
  > | Donor vehicle order (FA) screenshots from AKMB and ALSZ: type code, production date and options, for a session-only order in Session 4 or an M3 DSC (option B) (NCS Expert) | | | | | |
- **Insert after:**
  > | Cluster before and after Session 4: EEPROM, VIN and mileage screenshots (PA-Soft) | | | | | |
- **New row:**
  > | Vehicle order after Session 4: screenshots from ALSZ and AKMB, and whether `FA_WRITE` to AKMB worked (NCS Expert) | | | | | |
- **Why:** notes correction 3 (every module NCS lists, NETTODAT too) and G3/G4 (both order copies; the donor's order for a session-only cluster session).

### R10: WORKSHEETS 0050__electronics-baseline.md (coding-power): the coding file and data files
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] NCS Expert reads the vehicle order (FA) from ALSZ and from AKMB, and the two match; or the ZCS on a car built before 09/2001
- **New text:**
  > - [ ] `FSW_PSW.MAN` in `C:\NCSEXPER\WORK\`, named exactly that; `KMBE46M3.C23` or `C24` and `LSZ.C35` to `LSZ.C37` in the E46 data ([NCS Expert basics](WIRING-AND-CODING.md#ncs-expert-basics))
- **Why:** notes G1 (the MAN saved as `.MAN.txt` gives COAPI-1020; the M3 cluster and light-module files must be in the data).

## integrator fragments

### R11: README 0920__open-questions-to-verify.md: the body-coding questions
- **Change:** replace (three items), delete (one item), add (four items, in the "Wiring and coding" list after the lamp-switch item)
- **Find (exact current text, for replace, delete or insert after):**
  > - Which cluster coding indexes have the three lamp switches (`CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN`, `TOG_UEBER_CAN`); one snippet says 07, 08, 23 and 24.
- **New text:**
  > - The factory values of the cluster's three lamp switches (`CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN`, `TOG_UEBER_CAN`) on a US M3 cluster at coding index 23 against 24. The switches are confirmed on index 24 and absent from a pre-2003 non-M cluster and a 2002 M3's list; index 23 almost certainly has them ([manual](WIRING-AND-CODING.md#cluster-wiring)).
  > - Whether NCS Expert accepts an index-24 M3 cluster, for coding and for `FA_WRITE`, with a 325i Touring's vehicle order in the session. The manual codes the cluster with the donor's order loaded and has a fallback if `FA_WRITE` is refused ([Session 4](WIRING-AND-CODING.md#session-4-cluster-and-light-module)).
  > - Whether front fog lights on a Touring that lacks them need option `$520` in the vehicle order as well as the fog version of the light module (61319133024 to 61319133027).
  > - Whether US M3s have headlight washers as standard, and their option code (`S502A` is unverified).
  > - Which US passenger-seat occupancy system, OC3 or SBE, each model year has, and whether an OC3 seat works with an earlier airbag module. It matters only if the seats change.
- **Find (second):**
  > - Whether the M3 console switch unit fits a Touring's console.
- **New text (second):**
  > - Whether the M3 console switch unit fits a Touring's console (it needs no coding), and the part number of a US 325i Touring's switch unit with DSC: the catalog page read shows only the unit without DSC, 61316925498.
- **Find (third):**
  > - The light-module parameters and levelling-sensor wiring for M3 headlights that differ from the Touring's.
- **New text (third):**
  > - For xenon M3 headlights on a Touring: the level-sensor curves (`KENNLINIE_LWR_SENSOR_VO`, `KENNLINIE_LWR_SENSOR_HI`) to use with the M3 front link, and whether a US halogen light module can run levelling after coding alone (BMW's retrofit replaces the module). The wiring and the parameter names are answered ([manual](WIRING-AND-CODING.md#session-9-light-module-and-headlights)).
- **Delete:**
  > - How to add multifunction steering-wheel buttons if your car doesn't have them.
- **Why:** notes correction 8 (lamp switches) and 22 (answered items); the four new items are the notes' open questions (§2, §3, §5 gaps). Two related items are handled elsewhere: coding-power R2 deletes the "`$7MA`" line (answered: the Competition package), and fuel R19 item 4 keeps "whether an M3 cluster shows the tailgate and rear-window warnings", which covers my tailgate and rear-glass question.

### R12: README 0110__choose-the-donor.md: cluster row, the 09/2002 rule
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Prefer a redesign cluster: it properly supports the M Track light and brake-force display. The backlight wire changed at 09/2002,
- **New text:**
  > | Prefer a redesign cluster: it properly supports the M Track light and brake-force display. For a Touring built from 09/2002, use a cluster from 09/2002 or later: ECUswap calls it compulsory ("zwangsweise") ([ECUswap](https://ecuswap.de/technikinfo-kombiinstrument-austausch-e46/)); a 2003–06 donor gives index 23 or 24. The backlight wire changed at 09/2002,
- **Why:** notes correction 21.

### R13: README 0170__shop-briefs.md: cluster service row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | **Cluster service** | Your Touring's VIN in the M3 cluster, with the odometer set so it takes your true mileage from the light module; the M3 coding index kept; rear-door warning lights added if offered |
- **New text:**
  > | **Cluster service** | Your Touring's VIN in the M3 cluster, with the odometer set so it takes your true mileage from the light module; the M3 coding index and coding kept, not re-coded "from the factory vehicle order"; your vehicle order written into the cluster if they can, or a note that it wasn't; rear-door warning lights added if offered |
- **Why:** notes Inference 3 in §2 (a service's standard coding "from the factory vehicle order", ECUswap, default-codes an M3 cluster from a 325iT order) and Takeaway 1.

### R14: README 0430__phase-12-front-end-first-start-and-shakedown.md: steps 8 and 9
- **Change:** replace (two items)
- **Find (exact current text, for replace, delete or insert after):**
  > 8. **Vehicle-order changes and body modules** ([Session 8](WIRING-AND-CODING.md#session-8-vehicle-order-changes-and-body-modules)): none need swap coding if you kept your Touring's vehicle order. If you change it, for example for M Track with an M3 MK60, code the other modules one at a time and reset the DME adaptations again.
- **New text:**
  > 8. **Vehicle-order changes and body modules** ([Session 8](WIRING-AND-CODING.md#session-8-vehicle-order-changes-and-body-modules)): none need swap coding if you kept your Touring's vehicle order. M Track doesn't need a stored change either: keep `$7MA` out of the stored order. If you do change the order, code only the modules it touches, one at a time and never with Code Car, and reset the DME adaptations again only after an engine-side change.
- **Find (second):**
  > 9. **Headlights** ([Session 9](WIRING-AND-CODING.md#session-9-light-module-and-headlights)): if the M3 headlights differ from your Touring's, code the light module for them. Then aim them, at ride height.
- **New text (second):**
  > 9. **Headlights** ([Session 9](WIRING-AND-CODING.md#session-9-light-module-and-headlights)): halogen M3 lamps in a halogen Touring need no coding; check the bulbs and that the light module stores no lamp faults. Xenon lamps need BMW's xenon light module, fitted new or virginized, and two level sensors. Then aim them, at ride height.
- **Why:** notes corrections 10–14 and 18–19.

### R15: README 0120__budget.md: cluster row, Huggins prices
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Cluster: new EEPROM done yourself, or a service | \$50–\$400 | Estimate. One Touring build paid Kassel
- **New text:**
  > | Cluster: new EEPROM done yourself, or a service | \$50–\$400 | Estimate. Huggins Racing lists a used-cluster VIN and mileage correction at \$125 and its rear-door LED mod at \$100 (October 2026) ([Huggins](https://racehuggins.com/product/e46-cluster-mileage-vin-correction/), [Huggins](https://racehuggins.com/product/e46-m3-cluster-mod-for-non-m/)). One Touring build paid Kassel
- **Why:** the README cluster section now quotes both prices (notes §2, Huggins [read]).

### R16: README 0910__glossary.md: the cluster's copy of the order, and the two coding files
- **Change:** replace (two rows) and add row (after "TIS, newTIS")
- **Find (exact current text, for replace, delete or insert after):**
  > | KOMBI (KMB, AKMB) | The instrument cluster; NCS Expert calls it KMB on ZCS cars and AKMB on FA cars |
- **New text:**
  > | KOMBI (KMB, AKMB) | The instrument cluster; NCS Expert calls it KMB on ZCS cars and AKMB on FA cars, where it holds one of the two copies of the vehicle order |
- **Find (second):**
  > | M35080 | The cluster's EEPROM chip, which stores its VIN and mileage |
- **New text (second):**
  > | M35080 | The cluster's EEPROM chip, which stores its VIN, mileage and coding, and its copy of the vehicle order |
- **Insert after:**
  > | TIS, newTIS | BMW's repair information system, and the online copy of it |
- **New row:**
  > | Trace, coding file (TRC, MAN) | NCS Expert's read-out of a module's coding (`FSW_PSW.TRC`), and the edited copy it writes back (`FSW_PSW.MAN`) |
- **Why:** notes Takeaway 1 (KOMBI46R stores the FA; "the VO is brought back onto the new Chip"); the manual's sessions now use both file names throughout.

### R17: README 0270__body.md: headlights in the front-end row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Tourings built from 09/2001 don't have them, so buy a pair ([Garagistic](https://www.garagistic.com/products/e46-m3-style-front-bumper-aftermarket-replacement)) |
- **New text:**
  > Tourings built from 09/2001 don't have them, so buy a pair ([Garagistic](https://www.garagistic.com/products/e46-m3-style-front-bumper-aftermarket-replacement)). Halogen M3 headlights plug into a halogen Touring with no coding. Xenon ones also need BMW's xenon light module (61319133026, or 61319133027 with a rain/light sensor), new or virginized (RPM Motorsport programs used ones for \$300, October 2026), and front and rear level sensors ([manual](WIRING-AND-CODING.md#session-9-light-module-and-headlights)) |
- **Why:** notes correction 19 and §3 (BMW EBA 01 29 9 416 445 replaces the light module; RPM [read]).

### R18: README 0100__check-your-own-touring-first.md: options that pick the light module
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Options | Climate control (automatic IHKA or manual IHKR), console switch center, xenon lights, mirror harness on facelift doors, cruise |
- **New text:**
  > | Options | Climate control (automatic IHKA or manual IHKR), console switch center, xenon lights, front fogs and a rain/light sensor (together they set your light module's part number), steering-wheel buttons, mirror harness on facelift doors, cruise |
- **Why:** notes §3: ETK lists different light modules with and without fogs, rain/light sensor and xenon; §5: the MFL retrofit only applies to a car without buttons.

### R19: README 0310__phase-0-paperwork-and-baseline.md: step 5, both order copies and every module
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > the FA or ZCS, with screenshots of the option list, production date and type code ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-fa-for-at-mt-swap.1290835/)); each module's coding file (`FSW_PSW.TRC`) for the cluster, light module (LCM), GM5, DSC, EWS and climate control ([ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf));
- **New text:**
  > the FA or ZCS, read from both the light module (ALSZ) and the cluster (AKMB), with screenshots of the option list, production date and type code ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-fa-for-at-mt-swap.1290835/)); each module's coding files (`FSW_PSW.TRC` and `NETTODAT.TRC`) for the cluster, light module (LCM), GM5, DSC, EWS, climate control, and the airbag, steering-angle and park-distance modules if fitted ([ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf));
- **Why:** notes correction 3 and G3 step 1.

### R20: JOB-CARDS 0010__card-0-paperwork-and-baseline.md: backup line
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>FA or ZCS, every module's coding, cluster and LCM EEPROMs and fault lists saved ([Session 1](WIRING-AND-CODING.md#session-1-vehicle-order-and-codings))</span>
- **New text:**
  > - [ ] <span>FA or ZCS read from both ALSZ and AKMB; every module's coding (trace and NETTODAT), cluster and LCM EEPROMs and fault lists saved ([Session 1](WIRING-AND-CODING.md#session-1-vehicle-order-and-codings))</span>
- **Why:** as R19.

### R21: WIRING-AND-CODING 0450__first-key-on-what-to-expect.md: step 23, the brake lamps at key-on
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | 23 | Lamps at key-on | Red oil-pressure lamp, charge lamp and check-engine lamp lit. The check-engine bulb check is also an inspection item |
- **New text:**
  > | 23 | Lamps at key-on | Red oil-pressure lamp, charge lamp and check-engine lamp lit, and the red BRAKE lamp with the parking brake on; the DSC, ABS and yellow BRAKE lamps stay on until Session 5. The check-engine bulb check is also an inspection item |
- **Why:** BMW ST056 lamp meanings (front notes Q4/Q5), matching the manual's Warning lights section.

## susp fragments

### R22: JOB-CARDS 0290__card-12d-alignment-and-final-coding.md (susp): the last two coding tasks
- **Change:** replace (two task lines)
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Vehicle-order changes and body modules, if any ([Session 8](WIRING-AND-CODING.md#session-8-vehicle-order-changes-and-body-modules))</span>
- **New text:**
  > - [ ] <span>Vehicle-order changes and body modules, if any: only the modules a change touches, never Code Car ([Session 8](WIRING-AND-CODING.md#session-8-vehicle-order-changes-and-body-modules))</span>
- **Find (second):**
  > - [ ] <span>Light module coded for the M3 headlights if they differ, then aimed at ride height ([Session 9](WIRING-AND-CODING.md#session-9-light-module-and-headlights))</span>
- **New text (second):**
  > - [ ] <span>Headlights: halogen M3 lamps with no lamp faults in the light module, or xenon with BMW's xenon light module and level sensors and the load test passed; then aimed at ride height ([Session 9](WIRING-AND-CODING.md#session-9-light-module-and-headlights))</span>
- **Why:** notes corrections 12, 18 and 19. coding-power R17 changes the same card's "Stop and ask" sentence on vehicle-order changes; both can apply.
