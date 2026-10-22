# Requests from the susp writer

Requests to integrator fragments quote the guide's current text. Requests to other writers' fragments (front, fuel, arches, floor, coding-power) quote their text as it stood when I wrote this; if the owner has since reworded the passage, apply the substance.

New anchors in my README fragment 0520 that these requests link to: `#weights-and-axle-loads`, `#springs-dampers-and-anti-roll-bars`, `#coilovers-for-the-m3-axles`, `#ride-height-bmws-method-and-figures`, `#targets-for-the-mock-up-and-the-bushed-joints`, `#massachusetts-ride-height-baseline`, `#after-the-build-settle-check-and-align`.

## Conflicts

1. **420G gearbox oil capacity.** BMW's 2003 US M3 owner's manuals (coupe p.147, convertible p.153) print "Manual transmission quarts/liters approx. 1.9/approx. 1.8", i.e. 1.8 L (1.9 US qt). The guide's Fluids table and Fluids log say "1.9 L (2.0 US qt)" from ST041. Both are BMW. R4 and R5 give both figures and say to fill to the plug; R12 adds an open question.
2. **S54 coolant capacity.** The same manuals give 9.3 L (9.8 US qt) "including heater circuit". The cool writer's notes have the same figure, so this isn't a conflict, but apply it once (R3, R5, R12).
3. **Alignment and ride-height load condition (front notes).** `front_axle_brakes_abs.md` (procedure B9, and its correction 17) says to align "at the car's loaded ride height … tell the shop which one you used". My notes, and the brief for this round, say to align to BMW's M3 TIS values unladen with a full tank: BMW ST056 says the E46 M3 is "usually measured without any weight", and ST503 calls that the "normal position". The front writer's current deep-dive step ("Align, then calibrate", README 0500) already drops "loaded", and its Card 8a sends the bar clamps to Card 12d; please keep "unladen, with a full tank" wherever the alignment or the front anti-roll bar clamps are mentioned.
4. **"Normal position" in the rear-arches notes.** `rear_arches.md` (cut-and-weld plan, step 1) reads TIS's "normal position" as loaded ("Unloaded it will read higher … 9 mm"). BMW ST503 defines the normal position as the car "without any weight added", so the M3's 605/587 mm figures apply unladen with a full tank. The arches writer's current fragment 0670 already says "unladen with a full tank", so the guide text agrees; flagging it only in case the 9 mm remark resurfaces.
5. **"Loaded ride height" for the rear bushed joints.** The guide says "at loaded ride height" throughout. The bushed joints should be torqued at the height the finished car sits at, unladen with a full tank (my notes, set-up step F), or with each hub jacked to its target hub-to-lip. "Loaded" now reads as the opposite of "unladen", so R6, R7 and R31–R33 change it to "at ride height", and R34–R37 give the alignment condition as unladen with a full tank. My own fragments (Card 7c, the Phase 7 worksheet) already use "at ride height".

## Key numbers, fluids, torques and open questions

### R1: README 0900__key-numbers.md: weights like for like
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Weight | 325i Touring manual 3,362 lb, 47.7% front and 52.3% rear; M3 coupe 1,495 kg (3,296 lb) DIN | [BMW USA](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437), [BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf) |
- **New text:**
  > | Weight, US curb (full tank), manual gearbox | 325i Touring 1,525 kg (3,362 lb): 727 kg front, 798 kg rear. M3 coupe 1,549 kg (3,415 lb): 779 kg front, 770 kg rear. M3 convertible 1,715 kg (3,781 lb): 856 kg front, 859 kg rear. Your S54 Touring, our estimate: 1,584–1,614 kg (3,490–3,560 lb), 760–772 kg front, 824–842 kg rear. Don't compare these with the M3's 1,495 kg DIN weight in ST041, which leaves out the driver and assumes 90% fuel | [BMW USA: Touring](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437), [BMW USA: M3](https://www.press.bmwgroup.com/usa/article/attachment/T0022150EN_US/41463), [Weights and axle loads](#weights-and-axle-loads) |
  > | Axle ratings, 325i Touring, manual (door-pillar label) | Front 900 kg (1,984 lb), rear 1,210 kg (2,668 lb), GVWR 2,045 kg (4,509 lb). The swap uses about 60–90 kg of the 520 kg payload, and loaded the way BMW loads a car for ride height the front has only about 45–55 kg to spare (our estimates) | [BMW 2004 Sports Wagon owner's manual, p.162](https://manualsnet.com/pdf-content/0945ee845d7bf99b78315dcf/html/162.page.html) |
  > | E46 M3 ride height: rim flange to arch edge, unladen, full tank | 18-inch wheels: 605 mm (23.8 in) front, 587 mm (23.1 in) rear. 19-inch: 619 mm (24.4 in) front, 600 mm (23.6 in) rear. ±10 mm; left and right within 10 mm. BMW's figure for the Touring wasn't found; its published height is 1,409 mm (55.5 in), or 1,444 mm (56.8 in) with roof rails | [BMW TIS screenshots on NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/272922-what-is-oe-e46-m3-stock-ride-height-from-factory), [BMW manual, p.161](https://manualsnet.com/pdf-content/0945ee845d7bf99b78315dcf/html/161.page.html) |
  > | M3 tire pressures, 18- and 19-inch, cold | 230 kPa (33 psi) front, 240 kPa (35 psi) rear with up to four people; 280 kPa (41 psi) front, 330 kPa (48 psi) rear with luggage too | [BMW 2003 M3 coupe owner's manual, p.27](https://manualsnet.com/bmw/m3-coupe-3-series-2003) |
- **Why:** the old row compares a US curb weight with a DIN weight; adds the axle ratings, BMW's M3 ride height and BMW's M3 tire pressures. Notes: corrections 1, 6, 15; Q1, Q4; `rear_arches.md` Q1 (TIS 33 00/31 00).

### R2: README 0900__key-numbers.md: the Touring's wheel offset is now sourced
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > with ET26 wheels on the M3 and ET47 (assumed) on the Touring. Good to a millimetre or two; see [Rear arches and doors](#rear-arches-and-doors) | Worked out from the above and [BMW USA](https://www.press.bmwgroup.com/usa/article/attachment/T0022127EN_US/41385) (M3 rear track 60.0 in, 1,524 mm) |
- **New text:**
  > with ET26 wheels on the M3 and ET47 on the Touring (BMW lists ET47 for its 8J × 17 wheel and ET46 or ET47 for its 7J × 16 wheels). Good to a millimetre or two; see [Rear arches and doors](#rear-arches-and-doors) | Worked out from the above, [BMW USA](https://www.press.bmwgroup.com/usa/article/attachment/T0022127EN_US/41385) (M3 rear track 60.0 in, 1,524 mm) and [BMW's wheel and tire list: Touring](https://myair-bdr.bmwgroup.com/static/manual/RadReif/RadReif/00/mj2003/e46touring3_2003.htm) |
- **Why:** BMW's MY2003 Touring wheel and tire list gives 225/45R17 on 8J × 17 ET47. Notes: correction 14.

### R3: README 0880__fluids-and-capacities.md: S54 coolant capacity
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Coolant | BMW coolant, 50/50 with distilled water (unverified); system pressure 2 bar (29 psi) | **Capacity not found** | Mix: forum posts (unverified); pressure: Flow p.60 |
- **New text:**
  > | Coolant | BMW coolant, 50/50 with distilled water (unverified); system pressure 2 bar (29 psi) | 9.3 L (9.8 US qt), including the heater circuit | Mix: forum posts (unverified); pressure: Flow p.60; capacity: BMW's 2003 US M3 owner's manuals ([coupe, p.147](https://manualsnet.com/bmw/m3-coupe-3-series-2003), [convertible, p.153](https://manualsnet.com/bmw/m3-convertible-3-series-2003)) |
- **Why:** closes "Capacity not found". The cool writer has the same figure; apply once. Notes: "Incidental findings outside this topic".

### R4: README 0880__fluids-and-capacities.md: 420G oil capacity conflict
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | 1.9 L (2.0 US qt); check the label on the gearbox | Fluid: [BimmerWorld](https://www.bimmerworld.com/Genuine-BMW-MTF-LT-2-GL-4-Transmission-Fluid-1-liter.html); capacity: BMW ST041 technical data |
- **New text:**
  > | About 1.8 L (1.9 US qt) in BMW's 2003 US M3 manuals; 1.9 L in ST041. Fill to the fill plug; check the label on the gearbox | Fluid: [BimmerWorld](https://www.bimmerworld.com/Genuine-BMW-MTF-LT-2-GL-4-Transmission-Fluid-1-liter.html); capacity: BMW ST041 technical data and the [2003 M3 coupe owner's manual, p.147](https://manualsnet.com/bmw/m3-coupe-3-series-2003) |
- **Why:** two BMW sources disagree by 0.1 L (see Conflicts 1). Notes: "Incidental findings outside this topic".

### R5: WORKSHEETS 0270__fluids-log.md: coolant and 420G quantities
- **Change:** replace (two rows)
- **Find (exact current text, for replace, delete or insert after):**
  > | 420G gearbox (Phase 9) | Genuine BMW MTF-LT-2, 75W-80 GL-4 (83220309031) | 1.9 L (2.0 US qt); check the label on the gearbox | | |
  > | Coolant (Phase 10) | BMW coolant, 50/50 with distilled water (unverified); system pressure 2 bar (29 psi) | **Capacity not found** | | |
- **New text:**
  > | 420G gearbox (Phase 9) | Genuine BMW MTF-LT-2, 75W-80 GL-4 (83220309031) | About 1.8 L (1.9 US qt) per BMW's US M3 manuals, 1.9 L per ST041: fill to the fill plug; check the label on the gearbox | | |
  > | Coolant (Phase 10) | BMW coolant, 50/50 with distilled water (unverified); system pressure 2 bar (29 psi) | 9.3 L (9.8 US qt), including the heater circuit | | |
- **Why:** keeps the Fluids log in step with R3 and R4.

### R6: README 0870__torque-values.md: ride height for the bushed joints
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Tighten every rubber-bushed joint with the suspension at loaded ride height, so the bushings aren't pre-twisted ([Flow p.16](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing)); the notes say which joints those are.
- **New text:**
  > Tighten every rubber-bushed joint with the suspension at ride height, so the bushings aren't pre-twisted ([Flow p.16](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing)): the height the finished car sits at on its wheels, unladen with a full tank, or each hub jacked to that height ([Targets for the mock-up and the bushed joints](#targets-for-the-mock-up-and-the-bushed-joints)). The notes say which joints those are.
- **Why:** "loaded" now reads as the opposite of the unladen condition the guide uses (Conflicts 5). Notes: set-up step F; correction 9.

### R7: README 0870__torque-values.md: rear-axle rows
- **Change:** replace (five rows)
- **Find (exact current text, for replace, delete or insert after):**
  > | Trailing arm to bracket (through-bolt) | 110 Nm (81 ft-lb) | At loaded ride height | Department 69; [FCP Euro, part 2](https://www.fcpeuro.com/blog/how-to-overhaul-the-bmw-e46-m3-rear-subframe-part-2); Flow p.16 |
  > | Rear control-arm bolts at the subframe, M12 | 77 Nm (57 ft-lb) | At loaded ride height | Flow p.16 |
  > | Rear damper lower bolt, M12 | 100 Nm (74 ft-lb) | At loaded ride height | Flow p.17 |
  > | Rear damper top-mount nuts, M8 (M3 parts) | 28 Nm (21 ft-lb) | New nuts. No value found for the Touring's own top mounts | Flow p.17 |
  > | Rear anti-roll bar, links and brackets | 22 Nm (16 ft-lb) | At loaded ride height (rubber mounts; the diagram doesn't mark it, our recommendation) | Flow p.18 |
- **New text:**
  > | Trailing arm to bracket (through-bolt) | 110 Nm (81 ft-lb) | At ride height | Department 69; [FCP Euro, part 2](https://www.fcpeuro.com/blog/how-to-overhaul-the-bmw-e46-m3-rear-subframe-part-2); Flow p.16 |
  > | Rear control-arm bolts at the subframe, M12 | 77 Nm (57 ft-lb) | At ride height | Flow p.16 |
  > | Rear damper lower bolt, M12 | 100 Nm (74 ft-lb) | At ride height | Flow p.17 |
  > | Rear damper top-mount nuts, M8, on the M3 mounts 33526779670 | 28 Nm (21 ft-lb) | New nuts 07119905374. Your Touring's own mount (33521092362) takes the same nut, so 28 Nm very likely applies to it too (confirm in TIS 33 52) | Flow p.17; [ETK](https://bmwfans.info/parts-catalog/33521092362/) |
  > | Rear anti-roll bar, links and brackets | 22 Nm (16 ft-lb) | At ride height (rubber mounts; the diagram doesn't mark it, our recommendation) | Flow p.18 |
- **Why:** consistent with R6 and with Card 7b, Card 7c and the Phase 7 worksheet; the build fits the M3 mount anyway. Notes: corrections 4 and 9; Q3.

### R8: README 0870__torque-values.md: front control-arm bracket bolts don't need ride height
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts; at ride height | Flow p.2; [FCP Euro (2022), 42:06](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2526s) |
- **New text:**
  > | Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts; on stands (any position) | Flow p.2; [FCP Euro (2022), 42:06](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2526s) |
- **Why:** only the front anti-roll bar clamp nuts (21 Nm) are marked "tighten in normal position". The front writer's notes make the same correction, and its Card 8a and Phase 8 log already say "New bolts; on stands": apply once. Notes: `front_axle_brakes_abs.md` correction 2. I've applied it in Card 12d.

### R9: README 0920__open-questions-to-verify.md: ride height and loading
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - An E46 ride-height specification, and BMW's "normal loaded position" weights for the E46.
- **New text:**
  > - BMW's ride-height figures for the E46 Touring (TIS 31 00 and 33 00, by rim size and suspension). The M3's figures, BMW's method and its loading are in [Ride height: BMW's method and figures](#ride-height-bmws-method-and-figures); a BMW-equipped alignment shop's database may show the Touring's.
- **Why:** method, loading and the M3 figures are answered; the Touring's own numbers aren't. Notes: correction 16; `rear_arches.md` correction 8.

### R10: README 0920__open-questions-to-verify.md: top-mount torque question becomes the spring question
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - Torques for the Touring's own rear damper top mounts.
- **New text:**
  > - BMW's spring-table part numbers for an M3 coupe and an M3 convertible (a dealer looks them up by VIN), and OEM spring rates, which BMW doesn't publish.
  > - The free and compressed lengths of the Touring's own rear dampers and the M3's, which would settle whether the Touring's dampers work on the M3 trailing arms.
  > - Measured corner weights, ride heights and spring choices of any finished S54 Touring.
- **Why:** the build fits the M3 mount, which has a value (28 Nm, same nut as the Touring's); the open items are now the springs and dampers. Notes: correction 4; Q2, Q3 and Q5 gaps.

### R11: README 0920__open-questions-to-verify.md: tire pressures answered, wheel offset sourced
- **Change:** delete the first line; replace in the second
- **Find (exact current text, for replace, delete or insert after):**
  > - BMW tire pressures for the 18- and 19-inch M3 sizes: third-party sites disagree (35/35 psi against 33/35 psi, unverified).
  
  > and the Touring's stock wheel offset (ET47 assumed) isn't sourced.
- **New text:** (delete the first line)
  > and BMW lists the Touring's wheels at ET46 or ET47 depending on the style, ET47 for the 8J × 17.
- **Why:** BMW's 2003 US M3 manuals give 33/35 and 41/48 psi for both sizes; BMW's MY2003 Touring wheel list gives the offsets. Notes: corrections 14 and 15.

### R12: README 0920__open-questions-to-verify.md: coolant capacity answered; 420G capacity added
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - The S54's coolant capacity, and BMW's S54 cooling-system bleed procedure (TIS 17 00).
- **New text:**
  > - BMW's S54 cooling-system bleed procedure (TIS 17 00).
  > - The 420G's oil capacity: about 1.8 L (1.9 US qt) in BMW's 2003 US M3 manuals against 1.9 L in ST041. Fill to the plug either way.
- **Why:** coolant capacity found (9.3 L); the 420G figures disagree (Conflicts 1). Coordinate with the cool writer's request on the same line.

### R13: README 0910__glossary.md: suspension terms
- **Change:** add row (four rows, in alphabetical order)
- **Find (exact current text, for replace, delete or insert after):** insert after `| FA, VO, ZCS | … |`, after `| GM5 | … |`, after `| MVAC | … |` and after `| RACP | … |` respectively
- **New text:**
  > | GAWR, GVWR | Gross axle weight rating and gross vehicle weight rating: the most each axle, and the whole car, may carry. Both are on the door-pillar label |
  
  > | Hub-to-lip | The height from the hub center to the wheel arch's lower edge straight above it. Unlike BMW's ride height, it doesn't change with rim size |
  
  > | Normal position, design position | BMW's conditions for ride height and alignment: the normal position is the car with no weight added, as BMW measures an M3; the design position adds 68 kg in each front seat, 68 kg on the rear seat, 21 kg in the trunk and a full tank |
  
  > | Ride height (BMW) | The height from the rim flange's lower edge, straight below the hub center, to the wheel arch's lower edge straight above it |
- **Why:** the guide now uses these terms. Notes: Q1, Q4; BMW ST056 and ST503.

## Massachusetts, Phase 0 and the baseline

### R14: README 0730__massachusetts.md: how to measure ride height
- **Change:** replace (the "What to do" cell)
- **Find (exact current text, for replace, delete or insert after):**
  > | Record the Touring's ride height in Phase 0 and finish within 2 inches of it |
- **New text:**
  > | In Phase 0, unladen with a full tank and tires at placard pressure, record the roof height at marked points front and rear and the four jacking-point heights. Don't use the arch lips, which get replaced. BMW publishes 1,409 mm (55.5 in) for a 325i Touring, 1,444 mm (56.8 in) with roof rails. Finish within 50.8 mm (2 in) of your readings, ideally 25 mm (our target); the M3's 18-inch tires alone add about 14 mm ([Massachusetts ride-height baseline](#massachusetts-ride-height-baseline)) |
- **Why:** the rule needs a method that survives the arch replacement. Notes: correction 12; Q4.

### R15: README 0730__massachusetts.md: BMW did list staggered Touring sizes
- **Change:** replace (the "What to do" cell)
- **Find (exact current text, for replace, delete or insert after):**
  > | BMW never listed staggered sizes for a Touring, so ask your station about the M3's front and rear sizes before the appointment |
- **New text:**
  > | BMW's MY2003 wheel and tire list gives the 325i Touring staggered 17-inch (225/45ZR17 front, 245/40ZR17 rear) and 18-inch (225/40ZR18 front, 255/35ZR18 rear) sizes, but not the M3's 225/45R18 and 255/40R18, so ask your station about the M3's sizes before the appointment ([BMW wheel and tire list: Touring](https://myair-bdr.bmwgroup.com/static/manual/RadReif/RadReif/00/mj2003/e46touring3_2003.htm), [Wheels, track and offsets](#wheels-track-and-offsets)) |
- **Why:** the guide's statement is wrong. Notes: correction 13.

### R16: README 0310__phase-0-paperwork-and-baseline.md: step 7, the baseline
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 7. **Record the baseline:** on level ground, at normal ride height and placard tire pressures, measure at each corner the heights of the hub center and the arch lip, as you'll measure the donor in Phase 1, and note the fuel level. It's your reference for the arches and for any state rule on ride height ([Massachusetts](#massachusetts)). Then the last alignment printout, and photos of the engine bay, the DME box (E-box), the harness routing and the underside.
- **New text:**
  > 7. **Record the baseline** ([how](#massachusetts-ride-height-baseline)): on level ground, unladen, with a full tank (or 3.2 kg (7 lb) in the cargo area for each US gallon short) and tires at placard pressure, after bouncing each corner and rolling the car a few feet. At each corner measure BMW's ride height (rim flange to arch edge), the heights of the hub center and the arch lip, and the jacking-point height; then the roof height at marked points front and rear. Read the door-pillar label's GVWR and axle ratings (expect 2,045, 900 and 1,210 kg on a manual), and note S226A sport suspension or S338A M Sport II in the option codes. The roof and jacking points are your reference for Massachusetts' ride-height rule, because the arch lips get replaced ([Massachusetts](#massachusetts)); the corner heights are your reference for the arches. Then an alignment printout, asking the shop to include BMW's ride-height figure for your car if its database has one, and photos of the engine bay, the DME box (E-box), the harness routing and the underside.
- **Why:** BMW's method and loading, and a baseline that survives the arch replacement. Notes: set-up step A; corrections 6 and 12.

### R17: README 0310__phase-0-paperwork-and-baseline.md: Done-when row for the baseline
- **Change:** add row (after the "Shell" row)
- **Find (exact current text, for replace, delete or insert after):**
  > | Shell | RACP, arches, sills and jacking points inspected and photographed | Cracks: plan their repair for Phase 5. Torn or rotten floor: get a body-shop quote before you buy the donor |
- **New text:**
  > | Baseline | Corner, jacking-point and roof heights recorded unladen with a full tank; left and right within 10 mm at each axle | A bigger split means a sagging spring or a damaged part: note it, so it isn't copied into your targets |
- **Why:** gives step 7 a pass value. Notes: set-up step A, Pass.

### R18: JOB-CARDS 0010__card-0-paperwork-and-baseline.md: baseline task and check
- **Change:** replace (task line and Done-when row)
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Ride height at four corners; alignment printout; photos of engine bay, E-box, harness and underside</span>
  
  > | Ride height | Hub-center and arch-lip heights at four corners, level ground, placard pressures | |
- **New text:**
  > - [ ] <span>Unladen, tank full: BMW ride height, hub and lip heights and jacking-point height at four corners; roof height front and rear ([how](README.md#massachusetts-ride-height-baseline)); door-pillar label; alignment printout; photos of engine bay, E-box, harness and underside</span>
  
  > | Ride height | Corner, jacking-point and roof heights, unladen, full tank, placard pressures; left and right within 10 mm | |
- **Why:** as R16.

### R19: WORKSHEETS 0010__touring-baseline-record.md: suspension options and the door label
- **Change:** add row (two rows, after "Option codes")
- **Find (exact current text, for replace, delete or insert after):**
  > | Option codes | — | |
- **New text:**
  > | Suspension options | S226A sport suspension (about 15 mm lower) or S338A M Sport II, from the option codes | |
  > | Door-pillar label | GVWR and front and rear axle ratings; expect 2,045 / 900 / 1,210 kg (4,509 / 1,984 / 2,668 lb) on a manual | |
- **Why:** the axle ratings bind the finished car; sport suspension shifts the baseline by about 15 mm. Notes: set-up step A1; Q1, Q4.

### R20: WORKSHEETS 0040__shell-inspection.md (floor): the ride-height table
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > **Ride height,** at normal ride height: the car on its wheels on level ground, unladen, at placard tire pressures, measured up from the floor as you'll measure the donor in Phase 1 ([Phase 0](README.md#phase-0-paperwork-and-baseline), step 7):
  >
  > | Measurement | Front left | Front right | Rear left | Rear right |
  > |---|---|---|---|---|
  > | Hub center (mm) | | | | |
  > | Arch lip, straight above the hub center (mm) | | | | |
  > | Hub to lip: lip minus hub (mm) | | | | |
  >
  > | Condition | Record |
  > |---|---|
  > | Date, fuel level and tire pressures | |
- **New text:**
  > **Ride height:** the car on its wheels on level ground, unladen, tank full (or 3.2 kg (7 lb) in the cargo area for each US gallon short), at placard tire pressures, each corner bounced first ([Phase 0](README.md#phase-0-paperwork-and-baseline), step 7; [how](README.md#massachusetts-ride-height-baseline)). Pass: left and right within 10 mm at each axle.
  >
  > | Measurement | Front left | Front right | Rear left | Rear right |
  > |---|---|---|---|---|
  > | BMW ride height: rim flange's lower edge to the arch's lower edge (mm) | | | | |
  > | Hub center, up from the floor (mm) | | | | |
  > | Arch lip, straight above the hub center (mm) | | | | |
  > | Hub to lip: lip minus hub (mm) | | | | |
  > | Jacking point, up from the floor (mm) | | | | |
  >
  > | Condition | Record |
  > |---|---|
  > | Date, fuel level and tire pressures | |
  > | Wheel and tire size | |
  > | Roof height at the front mark, and where the mark is (mm) | |
  > | Roof height at the rear mark, and where the mark is (mm) | |
- **Why:** the Massachusetts check at the end compares the roof and jacking points with these (my Alignment worksheet has the Phase 12 side). Notes: set-up steps A and I; correction 12.

## Donor, decisions and parts

### R21: README 0320__phase-1-buy-and-inspect-the-donor.md and JOB-CARDS 0020__card-1-buy-and-inspect-the-donor.md: springs and struts
- **Change:** insert after (Phase 1, after the "Arch targets" bullet of step 5); replace (Card 1 task line)
- **Find (exact current text, for replace, delete or insert after):**
  > they give you the M3's stance and where your new arches go in Phase 6 ([Measure and mock up before you cut](#measure-and-mock-up-before-you-cut)).
  
  > - [ ] <span>Tire placard and underhood A/C and emissions labels photographed</span>
- **New text:**
  > (Phase 1, new bullet) `   - **Springs and struts:** photograph the paint marks on each spring and the symbol on each front strut, and note the strut and damper part numbers. They identify the donor's spring-table parts ([Suspension for Touring weight](#suspension-for-touring-weight)).`
  
  > (Card 1) - [ ] <span>Tire placard, underhood A/C and emissions labels, spring paint marks and front-strut symbols photographed</span>
- **Why:** BMW picks springs by VIN; the marks are the only on-car record. The arches writer covers the ride-height measurement itself. Notes: set-up step B; Q2 gaps.

### R22: README 0110__choose-the-donor.md: coupe or convertible, suspension
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > and the convertible's front struts are different parts from the coupe's ([ETK](https://bmwfans.info/parts-catalog/31312283103/)).
- **New text:**
  > and its front struts (31312282265/266) and springs are sized for a heavier nose: about 856 kg against the coupe's 779 kg. Plan on coupe front springs or coilovers with a convertible donor. Its rear dampers (33522282267), on the other hand, suit your Touring's heavier rear better than the coupe's (our inference) ([ETK](https://bmwfans.info/parts-catalog/31312283103/), [Suspension for Touring weight](#springs-dampers-and-anti-roll-bars)).
- **Why:** part numbers and what they mean for the donor choice. Notes: corrections 3 and 10; Q3.

### R23: README 0110__choose-the-donor.md: the donor's measurements
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Measurements | On level ground at normal ride height, at each corner: the heights of the hub center, the arch lip and a body point both cars share, and how far the lip sits outboard of the tire ([Measure and mock up before you cut](#measure-and-mock-up-before-you-cut)). Photograph the B-pillar tire placard and the underhood A/C and emissions labels | Your hub-to-body and hub-to-lip targets for the Phase 6 mock-up, the tire pressures and the A/C charge |
- **New text:**
  > | Measurements | On level ground, unladen with a full tank, on BMW 18- or 19-inch wheels, at each corner: BMW's ride height (rim flange to arch edge), the heights of the hub center, the arch lip and a body point both cars share, and how far the lip sits outboard of the tire ([Measure and mock up before you cut](#measure-and-mock-up-before-you-cut)). Photograph the spring paint marks, the front-strut symbols, the B-pillar tire placard and the underhood A/C and emissions labels | BMW's 605 mm front and 587 mm rear on 18-inch wheels (619 and 600 mm on 19s), ±10 mm with left and right within 10 mm, shows a stock stance. Your hub-to-body and hub-to-lip targets for the Phase 6 mock-up, and the A/C charge |
- **Why:** BMW's method and figures for vetting the donor; BMW's tire pressures are now known. Notes: corrections 6 and 15; `rear_arches.md` Q1.

### R24: README 0070__decide-these-before-you-spend-money.md: springs and dampers
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Coilovers, or springs and dampers rated for the Touring; 18-inch Style 67 or 19-inch wheels |
- **New text:**
  > | M3 coupe struts and springs in front; at the rear, M3 dampers with springs about 7–9% stiffer than an M3 coupe's (our estimate), or M3 coilovers with a stiffer rear spring; 18-inch Style 67 or 19-inch wheels |
- **Why:** says what "rated for the Touring" means. Notes: correction 3; Q2.

### R25: README 0330__phase-2-strip-the-donor.md and JOB-CARDS 0030__card-2a-strip-the-donor.md: keep the M3 rear top mounts
- **Change:** insert after (Phase 2); replace (Card 2a)
- **Find (exact current text, for replace, delete or insert after):**
  > If you'll fit the V-brace, also cut out its body mounting boxes with their reinforcement panels (Phase 5).
  
  > rear axle as one unit with push rod 33312229295 and V-brace 33312229899;
- **New text:**
  > (Phase 2, appended to that bullet) ` Take the rear dampers with their M3 top mounts (33526779670) and bump stops, and photograph each spring's paint marks before it comes out.`
  
  > (Card 2a) rear axle as one unit with push rod 33312229295 and V-brace 33312229899; rear dampers with M3 top mounts 33526779670 and bump stops;
- **Why:** the top mounts bolt to the body, not the axle, so they're easy to leave behind; the build reuses them. Notes: correction 2; Q3.

### R26: README 0340__phase-3-bench-work.md: spring numbers by VIN
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > One S54 Touring on moved-over M3 coupe suspension sat so low that its rear tires rubbed ([Tenza Motorsports – coilovers (2022), 00:40](https://www.youtube.com/watch?v=Sit-SmfU-9k&t=40s)).
- **New text:**
  > ` Before you order springs, ask a dealer for an M3 coupe's and an M3 convertible's spring numbers by VIN: BMW picks springs from a spring table, and your rear wants about 7–9% more rate than a coupe's (our estimate).`
- **Why:** ETK gives no fixed spring numbers. Notes: set-up step C; Q2.

### R27: README 0290__consumables-and-single-use-parts.md: rear damper nuts
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Rear axle fasteners and bushings: subframe collar nuts 33326760374, damper top-mount and rod nuts, RTABs | Buy new | |
- **New text:**
  > | Rear axle fasteners and bushings: subframe collar nuts 33326760374, damper top-mount nuts 07119905374 (four) and rod nuts 33526773882 (two), RTABs | Buy new | |
- **Why:** part numbers now known (ETK; Flow p.17 "always replace"). Notes: Q3.

### R28: README 0230__front-axle-and-steering.md (front): convertible struts and bar
- **Change:** replace (in the front writer's current rows)
- **Find (exact current text, for replace, delete or insert after):**
  > Struts 31312283103/104 (coupe; a convertible's carry other numbers),
  
  > Only the bar and its mounts are M3 parts.
- **New text:**
  > Struts 31312283103/104 (coupe; the convertible's 31312282265/266 are sized for a heavier nose, so prefer the coupe's), upper spring pockets 31331090612, upper pads 31331091233, bump stops 31332229778,
  
  > Only the bar and its mounts are M3 parts. The M3 convertible's 27 mm bar (31352229485) also fits and adds understeer.
- **Why:** the convertible's numbers and the M3-only strut-top parts. Notes: corrections 10 and 11; Q3, Q6.

## Phases 6, 7, 12 and the alignment

### R29: README 0670__measure-and-mock-up-before-you-cut.md (arches): record the bump travel
- **Change:** insert after (end of mock-up step 5, "Full bump")
- **Find (exact current text, for replace, delete or insert after):**
  > That's our suggestion; BMW publishes no rear wheel-travel figure for the M3.
- **New text:**
  > ` Also note how far each hub rose from its target height to full bump: subtracted from the new lip's hub-to-lip, it gives the full-bump figure for the loaded check in Phase 12 ([After the build](#after-the-build-settle-check-and-align)).`
- **Why:** the loaded check needs a full-bump reference taken with the springs out. Notes: set-up steps D and J.

### R30: README 0380__phase-7-fit-the-m3-rear-axle-and-fuel-system.md (fuel): step 5, the rear suspension parts
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 5. Fit springs and dampers rated for the Touring, the M3 sway bar and links,
- **New text:**
  > 5. Fit the M3 rear dampers on M3 top mounts (new M8 nuts at 28 Nm, new rod nuts at 14 Nm) with the M3 bump stops, and rear springs about 7–9% stiffer than an M3 coupe's, or M3 coilovers ([Suspension for Touring weight](#springs-dampers-and-anti-roll-bars)); then the M3 sway bar and links,
- **Why:** says what "rated for the Touring" means. Notes: correction 3; set-up step E.

### R31: README 0380__phase-7-fit-the-m3-rear-axle-and-fuel-system.md (fuel): step 8, how to set ride height
- **Change:** replace (two places)
- **Find (exact current text, for replace, delete or insert after):**
  > 8. **Torque the rubber-bushed joints at loaded ride height**, so
  
  > With the body on stands, jack under the axle until the car just starts to lift off them ([Tracks and Trails – perfecting the Touring's rear end (2025), 40:20](https://www.youtube.com/watch?v=eMJLXbvzckE&t=2420s)). Paint-mark every fastener.
- **New text:**
  > 8. **Torque the rubber-bushed joints at ride height**, so
  
  > With the body on stands, jack each rear hub until hub-to-lip (hub center to the arch's lower edge) matches its target from the mock-up, within 5 mm, and torque there; or torque them once the car is complete on its wheels, unladen with a full tank ([Targets for the mock-up and the bushed joints](#targets-for-the-mock-up-and-the-bushed-joints)). Don't jack until the car lifts off its stands, as one builder did ([Tracks and Trails – perfecting the Touring's rear end (2025), 40:20](https://www.youtube.com/watch?v=eMJLXbvzckE&t=2420s)): without the engine and gearbox the car is lighter than when finished, so that leaves the suspension a little extended. Paint-mark every fastener.
- **Why:** the guide's method sets the wrong height. Notes: correction 9; set-up step F.

### R32: README 0380__phase-7-fit-the-m3-rear-axle-and-fuel-system.md (fuel): Done-when, rear axle
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > the rubber-bushed joints done at loaded height; push rod on its spacers | Re-torque at the right height |
- **New text:**
  > the rubber-bushed joints done with hub-to-lip within 5 mm of target; push rod on its spacers | Re-torque at the right height |
- **Why:** as R31; matches Card 7c.

### R33: README 0510__driveline-and-rear-axle.md: step 7
- **Change:** replace (two places)
- **Find (exact current text, for replace, delete or insert after):**
  > 7. **At loaded ride height** (see [Suspension for Touring weight](#suspension-for-touring-weight)):
  
  > Tracks and Trails approximated ride height by jacking under the axle until the car began to lift off its rear jack point ([Tracks and Trails – Touring rear end (2025), 35:00](https://www.youtube.com/watch?v=eMJLXbvzckE&t=2100s)).
- **New text:**
  > 7. **At ride height** (see [Targets for the mock-up and the bushed joints](#targets-for-the-mock-up-and-the-bushed-joints)):
  
  > Tracks and Trails approximated ride height by jacking under the axle until the car began to lift off its rear jack point ([Tracks and Trails – Touring rear end (2025), 35:00](https://www.youtube.com/watch?v=eMJLXbvzckE&t=2100s)). Without the engine and gearbox that leaves the suspension a little extended, so set each hub to its target hub-to-lip instead, or torque these joints once the car is complete on its wheels, unladen with a full tank.
- **Why:** as R31. Notes: correction 9.

### R34: README 0430__phase-12-front-end-first-start-and-shakedown.md: step 6
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 6. **Alignment:** torque the front rubber-bushed joints with the car's weight on its wheels, then have the car aligned to BMW's E46 M3 figures at its own loaded ride height ([Wheel alignment](#wheel-alignment), [Shop briefs](#shop-briefs)).
- **New text:**
  > 6. **Ride height and alignment:** after 5–10 miles, unladen with a full tank, check the ride height: BMW's 605 mm front and 587 mm rear on 18-inch wheels (619 and 600 mm on 19s), rim flange to arch edge, ±10 mm, left and right within 10 mm; and the roof and jacking points against Phase 0 for Massachusetts ([After the build](#after-the-build-settle-check-and-align)). Torque the front anti-roll bar clamp nuts with the car on its wheels, then have it aligned to BMW's E46 M3 figures in the same unladen, full-tank condition ([Wheel alignment](#wheel-alignment), [Shop briefs](#shop-briefs)).
- **Why:** BMW's M3 test condition; only the bar clamps wait for ride height. Notes: corrections 7 and 8; set-up steps H, I and K; `front_axle_brakes_abs.md` correction 3.

### R35: README 0430__phase-12-front-end-first-start-and-shakedown.md: Done-when, alignment
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Alignment | Printouts before and after, with every value inside BMW's E46 M3 tolerances, set at the car's loaded ride height ([Wheel alignment](#wheel-alignment)) | A value the shop can't reach: a bent part, or a bushed joint torqued at the wrong height |
- **New text:**
  > | Ride height and alignment | BMW's ride height ±10 mm, left and right within 10 mm; roof and jacking points within 50.8 mm (2 in) of Phase 0; printouts before and after, with every value inside BMW's E46 M3 tolerances, set unladen with a full tank ([Wheel alignment](#wheel-alignment)) | Ride height off: springs wrong for the axle load ([After the build](#after-the-build-settle-check-and-align)). A value the shop can't reach: a bent part, a top mount on the wrong side, the wrong ride height, or a bushed joint torqued at the wrong height |
- **Why:** as R34. Notes: set-up steps H, I and K.

### R36: README 0170__shop-briefs.md: wheel alignment
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | **Wheel alignment** | BMW's E46 M3 values, set at the car's loaded ride height, with before and after printouts | The M3 values are a target, since the Touring sits differently ([Wheel alignment](#wheel-alignment)). You'll calibrate the steering-angle sensor afterwards |
- **New text:**
  > | **Wheel alignment** | BMW's E46 M3 values, set unladen with a full tank (BMW's M3 test condition) after a ride-height check, with before and after printouts | Every geometry part is M3, so the M3 values apply. Front camber moves only about ±0.5° in the strut-tower slots (tool 32 3 140) and caster not at all; rear camber is set at an eccentric bolt and rear toe with tool 32 3 030 ([Wheel alignment](#wheel-alignment)). You'll calibrate the steering-angle sensor afterwards |
- **Why:** as R34. Notes: corrections 7 and 8; Q6.

### R37: WORKSHEETS 0260__phase-12-at-ride-height-and-the-oil-pressure-switch.md: only the bar clamps
- **Change:** replace the intro; delete the bracket-bolt row
- **Find (exact current text, for replace, delete or insert after):**
  > Torque the front rubber-bushed joints with the car's weight on its wheels, before the alignment.
  
  > | Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts; at ride height | | |
- **New text:**
  > Torque the front anti-roll bar clamp nuts with the car on its wheels, unladen with a full tank, before the alignment. The control-arm bracket bolts don't need ride height: they're torqued on stands in Phase 8.
  
  > (delete the row: the front writer's Phase 8 log already carries it, "New bolts; on stands")
- **Why:** as R8. Notes: `front_axle_brakes_abs.md` corrections 2 and 3.

### R38: WIRING-AND-CODING 0540__session-7-steering-angle-after-the-alignment.md (coding-power): when
- **Change:** none needed
- **Find (exact current text, for replace, delete or insert after):**
  > (none)
- **New text:**
  > (none: the coding-power writer has already changed the "When" line to "after the wheel alignment, done unladen with a full tank")
- **Why:** listed so the integrator knows the alignment condition is consistent there. Notes: correction 8.

## Sources and other writers' fragments

### R39: README 0790__factory-documentation.md: BMW sources this round used
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > ST051 [EWS](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf).
- **New text:**
  > ` ST041 [running gear](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear.pdf); ST056 [suspension and alignment](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/01%20Suspension%20Systems%20and%20Alignment%20Procedures%201-20-03.pdf) and [level control](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics/05a_Level%20Control%20Systems%201-13-03.pdf); ST503 [wheel alignment](https://archive.org/download/BMWTechnicalTrainingDocuments/ST503%20Undercar%20Technology/03_Wheel%20Alignment%20Procedures.pdf); ST043 [E46 update](https://archive.org/download/BMWTechnicalTrainingDocuments/ST043%202002%20System%20Diagnosis/8%20E46%20Update.pdf).`
  >
  > (new bullet after "BMW training") `- **BMW owner's manuals and wheel lists:** the 2004 US 325i Sports Wagon manual ([manualsnet](https://manualsnet.com/bmw/325i-sports-wagon-3-series-2004)), the 2003 US M3 coupe and convertible manuals ([coupe](https://manualsnet.com/bmw/m3-coupe-3-series-2003), [convertible](https://manualsnet.com/bmw/m3-convertible-3-series-2003)), and BMW's wheel and tire lists for the MY2003 Touring ([BMW](https://myair-bdr.bmwgroup.com/static/manual/RadReif/RadReif/00/mj2003/e46touring3_2003.htm)) and the MY2005 M3 ([BMW](https://myair-bdr.bmwgroup.com/static/manual/RadReif/RadReif/00/M-GmbH/MJ2005/e46m3_2005.htm)).`
- **Why:** the guide now cites these for weights, ratings, ride height, pressures, wheel sizes and capacities. Notes: Q1, Q4, Q6.

### R40: README 0660__rear-arches-and-doors.md (arches): the Touring's wheel offset is sourced
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > and BMW USA gives no offset for the Touring's wheels, so their ET47 is an assumption (unverified).
- **New text:**
  > and BMW's MY2003 wheel and tire list puts the Touring's 8J × 17 wheel at ET47 and its 7J × 16 wheels at ET46 or ET47, depending on the style ([BMW wheel and tire list: Touring](https://myair-bdr.bmwgroup.com/static/manual/RadReif/RadReif/00/mj2003/e46touring3_2003.htm)).
- **Why:** the offset is now sourced. Notes: correction 14.
