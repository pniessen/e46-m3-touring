# Gap-fill: BMW's own data for the chassis and body (agent `bmw-chassis`)

Research date: 22 October 2026. Web searches used: 8 of 30.

**The route that worked.** workshop-manuals.com publishes BMW's TIS for every E46 variant as free HTML pages, with one full-page image per TIS page that carries the drawings. Department 69's E46 torque article links to it, which is how I found it. The TIS issue status is "12/2007"; the pages were printed on 14–17 Feb 2013. I used two manuals:
- the [325i (M54) Touring](https://workshop-manuals.com/bmw/3_Series_E46/325i_M54_TOUR/)
- the [M3 (S54) coupe](https://workshop-manuals.com/bmw/3_Series_E46/M3_S54_COUPE/)

The M3 convertible manual carries the same M3 ride-height and normal-position pages ([example](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_conver/3_technical_data/33__rear_axle/0__general/2_td__rear_axle_ride_height_e46___m3/)). Every page came back as a plain HTTP 200 with no challenge, and nothing was bypassed. The site loads a Cloudflare Turnstile script in the background; I didn't interact with it.

**Tags.**
- [read]: I read the page text.
- [image]: I viewed the TIS drawing or photo.
- [snippet]: a search summary only.
- Our arithmetic and inferences are labelled as such.

## Summary

| # | Status | Answer in one line | Best source |
|---|---|---|---|
| 1 | Closed | BMW ride height, measured rim flange (bottom middle) to the arch's lower edge in normal position, ±10 mm, left/right within 10 mm. 325i Touring, standard suspension, 15/16/17/18 in: front 576/589/604/617, rear 542/555/570/583 mm. Low-slung sports suspension: front 561/574/589/602, rear 526/539/554/567 mm. M3 (18/19 in) confirmed: front 605/619, rear 587/600 mm. All figures are **loaded**: normal position is a DIN load, 2 × 68 kg front seats + 68 kg rear centre + 21 kg luggage + full tank for the Touring, and 2 × 68 kg front seats + 14 kg luggage + full tank for the M3 | TIS 31 00, 33 00 and 32 00 |
| 2 | Closed | Touring, standard suspension: front toe 0°14' ± 8', camber −20' ± 20', caster 5°26' ± 30'; rear toe 0°16' ± 6', camber −1°30' ± 15'. Sport suspension: front camber −43', caster 5°36', rear camber −2°04'. M3 values as in the guide (re-read in the 12/2007 issue). BMW's no-load KDS mode adjusts the targets to the measured ride height, but TIS bars it for M models and for accident-repaired cars: those are aligned in design position (DIN load, then weights until ride height is within ±2 mm) | TIS 32 00 150, 32 00 155, 32 00 TD |
| 3 | Closed | **34 Nm, new nuts**, for the E46's 21 mm-flange strut-mount nuts (the M3 manual's own page). The 24 Nm row is for 18 mm-flange nuts on older models | TIS 31 31 1AZ |
| 4 | Narrowed | The M3 plate has 12 torque-plus-angle screws (6 in the front row, 6 in the rear) plus 6 small edge screws. The Touring plate has 4 front + 4 rear (the rear 4 thread into the body) + 3 small, so the M3 plate has one extra screw per side in each row. TIS says the plate bolts to the "front axle support/engine carrier" but not which holes are in which. Torque: 59 Nm + 90°, new screws, rear screws first | TIS 51 71 374 (both cars), 51 71 3AZ, 31 10 8AZ |
| 5 | Mostly closed | **Bleeding:** E46 TIS 34 00 050 read: max 2 bar; restart the routine at each wheel; 5 pedal strokes. After caliper work TIS points to 34 00 048, which still bleeds the rear circuit with the tester. **Parking brake (34 10 014):** back off **10 notches**; lever 5× at ~400 N; braking starts at the 2nd tooth; bed in at ~40 km/h over ~400 m. **Master cylinder:** BMW's photos suggest the front circuit (sensor V) is on the outlet next to the booster [image, inference]. **Rear pipes:** the single 3,684 mm pipe runs left, the 3,798 + 1,206 mm pair crosses right [image, inference]. **Unions:** no E46 row in TIS (E85/E86 14 Nm, E36 18 Nm) | TIS 34 00, 34 10, 34 31, 34 52; ETK |
| 6 | Closed (BMW data) | **Touring rear side wall (41 35 101):** cut lines at the C-pillar (200 mm below the roof edge), D-pillar and sill cover; ~60 mm backing strips; spots stitched into a continuous seam; arch edge crimped. **Also found:** rear wheel arch (41 14 502/511), luggage floor (41 12 535), gaps (41 00; rear door to side wall 4 ± 0.75 mm). **Body control dimensions** are in TIS 41 00, not 51 00: ±1 mm up to 1 m, ±2 mm above. **Weld rules:** 8 mm plug-weld holes, spots ≥ 25 mm apart, G3Si1/G4Si1 wire, 82/18 Ar/CO2 | TIS 41 00, 41 12, 41 14, 41 35 |
| 7 | Still open | No BMW figure for rear wheel travel or M3 rear bump-stop length (not in TIS, ST041 or BMW's press data) | Measure on the donor |
| 8 | Narrowed | No public safety-inspector manual. The program's inspector training modules cover emissions only; the station page posts 540 CMR 4.00, which is the procedure. Vehicle Check Module 1 (2026) confirms the 15-model-year emissions exemption and the engine-switching rule | mavehiclecheck.com |

---

## Gap 1. Ride height (TIS 31 00, 33 00, 32 00)

### Cited findings

**Touring (rear-wheel-drive E46; TIS heads the table "E46 / REAR END", its translation of rear-wheel drive), front, TIS 31 00** [read]:
- Method: "Ride level in normal position (attach tape measure to rim flange at bottom middle and measure to lower edge of wheel arch)".
- Tolerance: "normal position max. 10 mm; Design position max. 2 mm"; left/right difference "Normal position max. 10 mm; Design position max. 2 mm".
- Source: [TIS 31 00 Touring](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/31__front_axle/0__general/1_td__front_axle_ride_height_e46___rear_end/)

**Touring, rear, TIS 33 00** [read]: same wording and tolerances. Sources: [TIS 33 00 Touring](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/33__rear_axle/0__general/2_td__rear_axle_ride_height_e46___rear_end/), [p.2](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/33__rear_axle/0__general/2_td__rear_axle_ride_height_e46___rear_end/page_3704/).

| TIS row (mm, rim flange to arch) | 15 in | 16 in | 17 in | 18 in |
|---|---|---|---|---|
| Front, Series | 576 | 589 | 604 | 617 |
| Front, Low-slung sports suspension | 561 | 574 | 589 | 602 |
| Front, rough road (all, up to 09/2001; and from 09/2001 E46/4 except 3-litre) | 594 | 606 | 621 | 634 |
| Front, rough road from 09/2001, E46/2/3/C and E46/4 3-litre | 577 | 589 | 604 | 617 |
| Rear, Series | 542 | 555 | 570 | 583 |
| Rear, Low-slung sports suspension | 526 | 539 | 554 | 567 |
| Rear, rough road (all, up to 09/2001; and from 09/2001 E46/4 except 3-litre) | 562 | 575 | 590 | 603 |
| Rear, rough road from 09/2001, E46/2/3/C and E46/4 3-litre | 543 | 555 | 570 | 583 |

**Touring normal position, TIS 32 00 "Chassis/wheel alignment – normal position E46 / M43TU / M47 / M47TU / M52TU / M54 / M56 / M57 / M57TU / N40 / N42 / N45 / N46"** [read]: "Car loaded down to normal position. Vehicle with complete equipment for normal operation with: 2 x 68 kg on front seats (seats in central position) 1 x 68 kg on rear seat (centre) 1 x 21 kg in luggage compartment (centre) and full fuel tank." [TIS 32 00, non-M E46](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/1_td__chassis_wheel_alignment_normal_position_e46___m43tu_m47_m47tu_m52tu_m54_m/)

**M3, front, TIS 31 00 "Front axle – ride height E46 / M3"** [read]: Series, 18 in 605 mm, 19 in 619 mm; same method and tolerances. [TIS 31 00 M3](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/31__front_axle/0__general/1_td__front_axle_ride_height_e46___m3/)

**M3, rear, TIS 33 00 "Rear axle – ride height E46 / M3"** [read]: 18 in 587 mm, 19 in 600 mm. [TIS 33 00 M3](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/33__rear_axle/0__general/2_td__rear_axle_ride_height_e46___m3/)

**M3 normal position, TIS 32 00 "… normal position E46 / M3 / M3 CSL"** [read]: "Car loaded down to normal position. Vehicle with complete equipment for normal operation with: 2 x 68 kg on front seats (seats in central position) 1 x 14 kg in luggage compartment (centre) and full fuel tank." [TIS 32 00 M3](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/1_td__chassis_wheel_alignment_normal_position_e46___m3_m3_csl/)

**How BMW does it** [read]:
- **TIS 32 00 "Moving vehicle into normal position":**
  - "Check vehicle interior and luggage compartment … for load, unload vehicle if necessary".
  - "Introduce DIN load (refer to Technical Data) into vehicle".
  - "Determine vehicle ride height. Note: If the vehicle ride height is not inside the tolerance … the vehicle must be repaired (coil spring/leakage)".
  - [TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/13_ra__moving_vehicle_into_normal_position/)
- **TIS 33 53 "Measuring ride-level height of vehicle"** (M3 manual): "Move vehicle into normal position. Determine actual ride height (A) - to do so, attach tape measure to rim flange (2) at bottom middle and measure to lower edge of wheel arch (1)." [TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/33__rear_axle/53__springs_with_suspension/1_ra__measuring_ride-level_height_of_vehicle/)
- **Which row is your car, TIS 32 00** [read]: "Suspension design can be identified by label (K) on front spring strut".
  - "6Z Serie = 6-cylinder Series"
  - "6Z Sport = 6-cylinder sports suspension, low-slung"
  - "M3/2 = M3 Coupé"; "M3/C = M3 Convertible"
  - The rough-road package is identified by a spacer ring on the support bearing.
  - Without a label, identify the struts by ETK part number.
  - [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/11_ra__identification_on_volume_production_suspension_sports_suspension_etc/)

### What this settles in `rear_arches.md`
- **Source:** the 587/600 and 605/619 mm figures, the method and the tolerances in `rear_arches.md` are word for word the TIS pages above [read]. The NAM3 screenshots were these pages.
- **Loaded or unloaded: loaded.** TIS's normal position for the E46 M3 is a full tank, 68 kg on each front seat and 14 kg in the middle of the trunk.
- **A conflict with the training manuals.** This contradicts BMW NA's training manuals quoted in `suspension_touring_weight.md`:
  - ST056 (2003): M3s are "usually … measured without any weight".
  - ST503 (2006): "Normal Position refers to a vehicle without any weight added".
  - TIS 12/2007 is the repair manual itself and the later document, so follow TIS [inference].
- **The earlier snippet values.** The non-M figures seen as e46fanatics snippets (rear 17/18 in 590/603, front 621/634) are TIS's **rough-road** rows, mixed with the series 15/16 in rows. That explains the 35 mm step the earlier note flagged [read; inference about the mix-up].

### Inferences (ours)
- **Body height is the same for every rim size within a row** once converted to hub-to-arch. We used rim-flange radius = rim diameter/2 + 17.5 mm J-flange height, the same convention as `rear_arches.md` [our arithmetic]:

| Hub centre to arch edge, mm (our arithmetic) | 15 in | 16 in | 17 in | 18 in | 19 in |
|---|---|---|---|---|---|
| Touring front, Series | 368 | 368 | 371 | 371 | — |
| Touring front, Sport | 353 | 353 | 356 | 356 | — |
| Touring rear, Series | 334 | 334 | 337 | 337 | — |
| Touring rear, Sport | 318 | 318 | 321 | 321 | — |
| M3 front | — | — | — | 359 | 360 |
| M3 rear | — | — | — | 341 | 341 |

  If the tape is hooked on the bead seat rather than the flange lip, add 17.5 mm. Measuring the same way every time matters more.
- **The owner's car.** On a 2003 US 325i Touring:
  - Standard car (strut label "6Z Serie", 16 in): BMW's figures are front 589, rear 555 mm.
  - Sport Package car ("6Z Sport", 17 in): front 589, rear 554 mm.
  - Both ±10 mm, at the Touring DIN load.
  - Row choice: our inference from the label key above and BMW USA's 16/17 in fitments in `suspension_touring_weight.md`.
- **Massachusetts.**
  - These TIS numbers are BMW's published "manufacturer's specified height" for the Touring, and the obvious baseline for 540 CMR 4.04(13).
  - But they are measured to the arch edge, which the conversion replaces. So also record body heights (sill at each jacking point, roof) at the same load on the same day.
  - The 2-inch limit is 50.8 mm, five times BMW's ±10 mm tolerance [inference].
- **Arch mock-up.**
  - In normal position the M3 sits at ≈ 341 mm hub-to-arch at the rear and ≈ 359 mm at the front on 18 in wheels [our arithmetic].
  - Vet the donor against 587/605 mm ± 10 at the M3 load before trusting its measured heights.
  - A Touring on M3 springs carries more rear-axle mass than the M3 (see `suspension_touring_weight.md`), so expect it to sit lower than 587 mm at the rear unless the springs are chosen for it [inference].

### Still open
Nothing on BMW's side. Still to do on the cars: measure the owner's Touring and the donor at their DIN loads in Phase 0 and Phase 1.

### Guide impact (writers: **susp** for the specification and loading; **arches** for the mock-up target; **susp** for the Massachusetts row)

1. **README.md:1322** — "We found no E46 ride-height specification, so the target comes from the donor: its hub-to-body heights, measured before teardown in [Phase 1] …"
   Replace the first sentence with:
   > BMW's TIS gives ride height as the distance from the rim flange (bottom middle) to the lower edge of the wheel arch, with the car in "normal position": its DIN load. For an E46 M3 that is a full tank, 68 kg on each front seat and 14 kg in the middle of the trunk. For your Touring it is a full tank, 68 kg on each front seat, 68 kg in the middle of the rear seat and 21 kg in the trunk. E46 M3: front 605 mm and rear 587 mm on 18-inch wheels (619/600 mm on 19s), ±10 mm, left and right within 10 mm ([TIS 31 00](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/31__front_axle/0__general/1_td__front_axle_ride_height_e46___m3/), [TIS 33 00](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/33__rear_axle/0__general/2_td__rear_axle_ride_height_e46___m3/), [normal position](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/1_td__chassis_wheel_alignment_normal_position_e46___m3_m3_csl/)). That is about 359 mm front and 341 mm rear from hub centre to arch edge (our arithmetic). Check the donor against these at its DIN load before you trust it, then take its hub-to-body heights as the target, adjusted for your springs.

2. **README.md:771** — "No BMW ride-height figure was found for this car, so the donor is your reference."
   **README.md:1794** — "We found no BMW ride-height figure, so take the targets from your donor."
   Replace both with:
   > Use the donor's measured heights, after checking them against BMW's M3 figures in [Suspension for Touring weight](#suspension-for-touring-weight) (rear 587 mm, front 605 mm on 18-inch wheels, rim flange to arch edge, ±10 mm, at the M3's DIN load).

3. **README.md:1937** (Massachusetts table, Ride height, "What to do") — "Record the Touring's ride height in Phase 0 and finish within 2 inches of it".
   Replace with:
   > In Phase 0, load the Touring to BMW's normal position (full tank; 68 kg on each front seat, 68 kg in the middle of the rear seat, 21 kg in the trunk) and measure it BMW's way, rim flange to arch edge. Compare with BMW's figure for your suspension, read off the label on the front strut: "6Z Serie" on 16-inch wheels, front 589 / rear 555 mm; "6Z Sport" on 17-inch wheels, front 589 / rear 554 mm; ±10 mm ([TIS front](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/31__front_axle/0__general/1_td__front_axle_ride_height_e46___rear_end/), [TIS rear](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/33__rear_axle/0__general/2_td__rear_axle_ride_height_e46___rear_end/), [strut label](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/11_ra__identification_on_volume_production_suspension_sports_suspension_etc/)). At the same time and load, record the sill height at each jacking point and the roof height, because the arches will change. Finish within 2 inches (51 mm) of those.

4. **README.md:2425** (Open questions) — "An E46 ride-height specification, and BMW's "normal loaded position" weights for the E46."
   Delete it. It is answered by TIS 31 00, 33 00 and 32 00 (above).

5. **For the susp writer folding `suspension_touring_weight.md`:** don't adopt that file's correction that "M3s [are] measured unladen". TIS 32 00 (12/2007) defines the M3's normal position with 2 × 68 kg plus 14 kg plus a full tank.

---

## Gap 2. Alignment (TIS 32 00)

### Cited findings

**Touring, standard suspension, TIS 32 00 "Wheel Alignment E46 / REAR END Standard suspension"** [read], [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/6_td__wheel_alignment_e46___rear_end___standard_suspension/):
- "Observe test conditions."
- Front:
  - total toe 0°14' ± 8'
  - camber −20' ± 20' (left/right difference max 30')
  - toe-angle difference at 20° inner lock −1°34' ± 30'
  - caster 5°26' ± 30' at ±10° lock, 5°37' ± 30' at ±20° (left/right max 30')
  - front wheel displacement (set-back) 0° ± 15'
  - maximum lock about 43.6° inner, 35.6° outer
- Rear:
  - total toe 0°16' ± 6'
  - camber −1°30' ± 15' (left/right max 15')
  - geometrical axis deviation (thrust angle) 0° ± 6'

**Touring, low-slung sports suspension** [read], [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/2_td__wheel_alignment_e46___rear_end___low-slung_sports_suspension/): the same values except:
- front camber −43' ± 20'
- caster 5°36' ± 30' (±10° lock) and 5°47' ± 30' (±20° lock)
- rear camber −2°04' ± 15'

Three rough-road tables also exist (not US).

**E46 M3, TIS 32 00 "Wheel alignment E46 / M3"** [read], [TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/7_td__wheel_alignment_e46___m3/):
- Front:
  - total toe 0°16' ± 7'
  - camber −1° ± 20'
  - toe-angle difference −1°32' ± 30'
  - caster 7°25' ± 30' (±10° lock) and 7°40' ± 30' (±20° lock)
  - set-back 0° ± 10'
  - maximum lock 40.90° inner, 33.81° outer
- Rear:
  - total toe 0°22' ± 6'
  - camber −1°45' ± 15'
  - thrust angle 0° ± 4'

These are identical to the guide's table (from a 01/2005 printout) [read].

**Test conditions, TIS 32 00** [read], [TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/15_ra__test_conditions_for_chassis_wheel_alignment_check/):
- "Correct and identical rim and tyre sizes"
- tread depth may differ left to right "by max. 3-4 mm"
- placard tyre pressures
- wheel-bearing clearance, steering backlash, and suspension and dampers OK

**Two KDS (BMW alignment rig) methods** [read]:
- **TIS 32 00 150 "KDS chassis/wheel alignment check with load up to design position":**
  - "Carry out chassis/wheel alignment check in design position only:
    - if the technical prerequisites for an alignment check with ride-height input are lacking
    - if, in spite of repairs having been carried out, the car's ride height between the left and right sides is still outside the tolerance
    - if the vehicles in question have been involved in an accident
    - if the models are M models"
  - Steps include "Move vehicle into design position".
  - [TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/18_ra__kds_chassis_wheel_alignment_check_with_load_up_to_design_position/)
- **TIS 32 00 155 "KDS chassis/wheel alignment check with ride-height measurement without load":**
  - "Do not carry out chassis/wheel alignment without load" in the same four cases.
  - Otherwise: "Measure and enter vehicle ride height".
  - [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/20_ra__kds_chassis_wheel_alignment_check_with_ride-height_measurement_without_load/)
  - The M3 manual doesn't carry this method at all.
- **"Moving vehicle into design position":**
  - "Move vehicle into normal position".
  - "Add/distribute weights in area of spring struts until the vehicle ride height is within the tolerance (refer to Technical Data)", which is ±2 mm in design position.
  - [TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/12_ra__moving_vehicle_into_design_position/)
- After alignment, TIS 32 00 150 also lists "Carry out steering angle sensor adjustment".

### Inferences (ours)
- **The targets depend on ride height.** BMW's no-load mode takes the measured ride height and corrects the targets. That matches the German forum snippet in `suspension_touring_weight.md` ("calculated dynamically from the ride height entered").
- **This car falls under the design-position rule.** It has M3 axle geometry and major body repair, so TIS's design-position method applies twice over. Tell the shop not to use ride-height input.
- **Which load.** Use the M3's DIN load, because the M3 values were set at it: full tank, 68 kg on each front seat, 14 kg in the middle of the trunk. Then add weight near the struts until each corner is within 2 mm of the M3 TIS height.
- **If the car sits low.** If it sits more than 10 mm *below* the M3 figures at that load, weights can't fix it. BMW's own answer is "the vehicle must be repaired (coil spring …)": choose springs before aligning.
- **Caster proves the parts.** Caster isn't adjustable. A caster inside 7°25' ± 30' rather than the Touring's 5°26' confirms that the M3 top mounts and arms are fitted (as `front_axle_brakes_abs.md` says).

### Still open
None.

### Guide impact (writer: **susp**; Phase 12 and the shop brief also touch **front**)

1. **README.md:2277** — "It says "observe test conditions", meaning BMW's normal loaded position. Forum citations of TIS for other BMWs give that as 68 kg in each front seat, 68 kg in the middle of the rear seat, 21 kg in the luggage area and a full tank (unverified, not confirmed for the E46). Your Touring sits differently from an M3 coupe, so treat these as targets measured at the car's own loaded ride height."
   Replace with:
   > These are BMW's TIS "32 00 Wheel alignment E46 / M3" values ([TIS, issue 12/2007](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/7_td__wheel_alignment_e46___m3/)), the same as the 01/2005 printout on p.96 of the [Flow PDF](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing).
   >
   > "Observe test conditions" means: the same rim and tyre sizes on each axle, tread depths within 3–4 mm side to side, placard pressures, and sound bearings, steering and dampers ([TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/15_ra__test_conditions_for_chassis_wheel_alignment_check/)). The car must also be in BMW's normal position. For an E46 M3 that is a full tank, 68 kg on each front seat (seats in the middle position) and 14 kg in the middle of the trunk ([TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/1_td__chassis_wheel_alignment_normal_position_e46___m3_m3_csl/)). The 68/68/68/21 kg load is the non-M E46's.
   >
   > BMW aligns M models, and any car with accident repairs, only in "design position": the normal-position load, then extra weight near the struts until each ride height is within 2 mm of the TIS figure ([TIS 32 00 150](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/18_ra__kds_chassis_wheel_alignment_check_with_load_up_to_design_position/), [design position](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/12_ra__moving_vehicle_into_design_position/)). Ask the shop not to use the rig's ride-height-input mode, which BMW bars for these cars ([TIS 32 00 155](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/20_ra__kds_chassis_wheel_alignment_check_with_ride-height_measurement_without_load/)). If the car sits more than 10 mm below the M3 heights at that load, fix the springs first. For reference, a stock Touring's own values are front camber −20' (sport suspension −43'), caster 5°26', rear camber −1°30' (sport −2°04') ([TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/32__steering_and_wheel_alignment/0__electronic_chassis_alignment/6_td__wheel_alignment_e46___rear_end___standard_suspension/)).

2. **Phrase used in several places** — "at the car's own loaded ride height" / "set at the car's loaded ride height" / "aligned at loaded ride height". It appears at:
   - README.md:384, 964, 992, 1254, 1324
   - JOB-CARDS.md:930, 940
   - WORKSHEETS.md:801
   - WIRING-AND-CODING.md:1023

   Replace with "in BMW's M3 design position (M3 DIN load, ride height checked; see [Wheel alignment](#wheel-alignment))".

3. **README.md:384** (Shop briefs, Wheel alignment) — "The M3 values are a target, since the Touring sits differently".
   Replace with "Tell the shop: M model, accident-repaired body; design-position method only, no ride-height-input mode (TIS 32 00 150/155)".

---

## Gap 3. Strut-top nuts (TIS 31 31 1AZ)

### Cited findings
- **TIS 31 31 "Spring Struts", in the M3 manual** [read], [TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/31__front_axle/31__spring_strut/1_azd__spring_struts/). Row 1AZ, "Spring strut support bearing / adapter for rough road package to wheel arch":
  - **"E32, E34, E36, E46, E53 — Flanged hexagon nut dia. 21 mm — Replace nuts — 34 Nm"**
  - "E28, E30, E31, E32, E34, E36 / S50 / S52, E38, E39 — Hexagon flange nut dia. 18 mm — Replace nuts — 24 Nm"
  - "E36 / S50 / S52 — Flanged hexagon nut dia. 21 mm — Replace nuts and secure with Loctite 242 — 27 Nm"
  - "E52 … 18 mm … 28 Nm"
  - 2AZ, piston rod nut: E46 "Replace nut 64 Nm".
- **ST041** [read]: "The hole pattern of the front spring strut towers and rear shock absorber mounts is the same as on the standard parts." [ST041 part 1](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle_djvu.txt)
- **Rear top mounts too, TIS 33 52** [read]:
  - E46 rear damper top mount, M8: "Replace nuts 28 Nm".
  - Piston rod on thrust bearing, M10: "Replace nut 14 Nm".
  - Damper to trailing arm, M12: 100 Nm, "tighten in normal position".
  - [TIS 33 52 p.1](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/33__rear_axle/52__shock_absorber/1_azd__shock_absorbers/), [p.2](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/33__rear_axle/52__shock_absorber/1_azd__shock_absorbers/page_3597/)
  - This confirms the 28 Nm that `suspension_touring_weight.md` asked to check.

### Inferences (ours)
- The E46 row has no M3 exception, and it sits in the M3's own manual, so 34 Nm applies to the M3 parts.
- The Flow compilation's 24 Nm is most likely the 18 mm-flange row for older models.
- Both cars use the same nut, 31316769731 (ETK, per `front_axle_brakes_abs.md`). If you want proof, its flange should measure about 21 mm.

### Still open
None.

### Guide impact (writer: **front**)
Rows to change:
- **README.md:2225** — "| Strut top mount to body, M8 collar nuts | 24 Nm (18 ft-lb) | | Flow p.3 |"
- **JOB-CARDS.md:531** — "| Strut top mount to body, M8 collar nuts | 24 Nm (18 ft-lb) | — |"
- **WORKSHEETS.md:469** — "| Strut top mount to body, M8 collar nuts | 24 Nm (18 ft-lb) | — | | |"

Replace each with:
> | Strut top mount to body, M8 collar nuts (21 mm flange) | 34 Nm (25 ft-lb) | New nuts | [TIS 31 31 1AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/31__front_axle/31__spring_strut/1_azd__spring_struts/) (E46; the 24 Nm row is for older models' 18 mm-flange nuts) |

Also update the matching line in the front-axle steps, "Strut tops: three new nuts per side (24 or 34 Nm …)" in `front_axle_brakes_abs.md`, to 34 Nm.

---

## Gap 4. Thrust (reinforcement) plate screws

### Cited findings

**M3, TIS 51 71 374 "Removing and installing / replacing reinforcement plate on front axle support (M3)"** [read; image R51 2687, enlarged] ([TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/51__body_equipment_%28coupe%29/71__gaskets-seals_loose_body_components/4_ra__removing_and_installing___replacing_reinforcement_plate_on_front_axle_support_%28m/)):
- "Vehicles must not be driven without reinforcement plates. Driving without the reinforcement plate may damage the front axle."
- "Release screws (1). Release screws (2) and remove reinforcement plate (3). Installation: Replace screws (2). Install all screws. Tighten screws (2) to torque and then to angle of rotation … Tighten down screws (1)."
- The drawing shows **12 screws (2)**: six along the front edge (a corner screw and two inner screws on each side) and six along the rear edge (the same pattern). It also shows **6 small screws (1)**, three on the front edge and three on the rear.

**Touring, TIS 51 71 374** [read; image R51 2825, enlarged] ([TIS p.1](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/51__body_equipment_%28tour%29/71__gaskets-seals_loose_body_components/5_ra__removing_and_installing_replacing_reinforcement_plate_on_front_axle_support/), [p.2](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/51__body_equipment_%28tour%29/71__gaskets-seals_loose_body_components/5_ra__removing_and_installing_replacing_reinforcement_plate_on_front_axle_support/page_2603/)):
- Which cars have the plate: "Coupés from 11/99, all Convertibles, all E46 models without 4WD from 12/2000".
- Screw layout: "Unfasten screws (3). Release screws (1) and (2) … Replace screws (1) and (2) … Tighten screws (1) and (2) to torque and then to angle … Tighten down screws (3)."
- The rear screws thread into the body: "insert washers at screw-down points (1) between reinforcement plate and body".
- From 02/2001 the plate must have a left/right "impression" to clear the 66 mm control-arm bushings.
- The drawing shows 4 screws (2) across the front, 4 screws (1) across the rear (two per side) and 3 small screws (3).

**Torque** [read]:
- **TIS 51 71 3AZ:** "Reinforcement plate to front axle support/engine carrier — E46 / without AWD … Replace screws — Jointing torque 59 Nm — Torque angle 90°". [TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/51__body_equipment_%28coupe%29/71__gaskets-seals_loose_body_components/1_azd__seals_and_loose_body_parts/)
- **TIS 31 10 8AZ:** "Front end reinforcement on front axle carrier/engine carrier — E46 — Replace screws; first tighten down rear screws — 59 Nm — 90+30°". [TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/31__front_axle/10__front_axle_suspension/1_azd__front_axle_suspension/page_3534/)

**Where the plate bolts, per BMW's training manual** [read]: "The thrust zone is made of aluminum and is bolted to the control arm joints, front axle carrier and the rear control arm mounts." [ST041 Running Gear](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear_djvu.txt)

**Body changes** [read]: ST041's list of M3 body changes from the E46/2 has nine items:
1. floor and luggage floor
2. side frame and wheel arches
3. side panels
4. hood and fuel flap
5. front bumper
6. rear bumper
7. C-pillar
8. strut tower
9. rear axle mounts

The front underbody isn't on the list. [ST041 part 1](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle_djvu.txt)

**M3 control-arm bracket, TIS 31 12 046** [read; image R31 0154] ([TIS](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/31__front_axle/12__struts_w.rubber_mounts/4_ra__replacing_bracket_for_control_arm_%28m3%29/)):
- Preliminary task: "Remove reinforcement plate".
- "Release bolts and remove bracke[t] from engine carrier … Check threads for damage; if necessary, repair with Helicoil thread inserts."
- The bracket is held by two bolts into the engine carrier. The drawing shows no plate threads in the bracket.
- Rubber mount position: "dimension (A) = 299 ± 2 mm on control arm pin".

**ETK drawings** [image]:
- M3 plate 51717893609 (3.4 kg, cast) with 12 × 31106772199.
- The Touring's flat steel plate.
- Neither drawing shows where each screw threads.

### Inferences (ours)
- **The extra screws.** One extra screw per side in each row. The front-row screws most likely go into the front axle support, which is the same part on both cars (31111096902), so its threads should be there.
- **The real risk** is the rear row's extra inboard screws. On the Touring the rear row threads into the body, and nothing BMW publishes says whether a non-M body has the two extra nuts.
- **No body change listed.** ST041 lists no M3 front-underbody change, which slightly favours a common body, but it isn't proof.

### Still open
Which of the 12 holes are body threads. **Settle it at mock-up:** offer up the M3 plate and run every screw in by hand. If any thread is missing, fit the Touring plate (51717028433) with its 8 screws; that is BMW's plate for a non-M E46.

### Guide impact (writer: **front**)

1. **README.md:1252** — "7. **Reinforcement plate** (51717893609): new M10×35 10.9 bolts, 59 Nm + 90° ([SI B11 04 04](…))."
   Replace with:
   > 7. **Reinforcement plate** (51717893609). BMW fixes the M3 plate with 12 M10×35 10.9 screws (six across the front, six across the rear) plus six small edge screws. Your Touring's plate uses 4 + 4 + 3 ([TIS 51 71 374, M3](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/51__body_equipment_%28coupe%29/71__gaskets-seals_loose_body_components/4_ra__removing_and_installing___replacing_reinforcement_plate_on_front_axle_support_%28m/), [Touring](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/51__body_equipment_%28tour%29/71__gaskets-seals_loose_body_components/5_ra__removing_and_installing_replacing_reinforcement_plate_on_front_axle_support/page_2603/)).
   >
   > Offer the plate up and run every screw in by hand before you order new ones. Its extra screw on each side of each row has no counterpart on your plate, and TIS doesn't say whether that thread is in the shared subframe or in the body.
   >
   > Fit new screws, rear ones first, 59 Nm + 90° (BMW allows +30° on the angle), then the small screws ([TIS 31 10 8AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/31__front_axle/10__front_axle_suspension/1_azd__front_axle_suspension/page_3534/), [51 71 3AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/51__body_equipment_%28coupe%29/71__gaskets-seals_loose_body_components/1_azd__seals_and_loose_body_parts/)). If a thread is missing, fit your own plate (51717028433) with its 8 screws. BMW: "Vehicles must not be driven without reinforcement plates."

2. **README.md:2224** — "| Front reinforcement plate, M10×35 10.9 | 59 Nm (44 ft-lb) + 90° | New bolts | BMW SI B11 04 04; Flow p.2 (±30° on the angle) |"
   Change the note to "New screws; rear row first" and add [TIS 51 71 3AZ / 31 10 8AZ] as the source. Make the same change in JOB-CARDS.md:536 and WORKSHEETS.md:468.

---

## Gap 5. E46 brakes (TIS 34)

### Cited findings

**Bleeding after work on the MC, the DSC unit or the pipes between them: TIS 34 00 050 "Bleeding brake system with DSC3"** (Touring manual) [read] ([p.1](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/0__brake_testing_and_bleeding/10_ra__bleeding_brake_system_with_dsc3/), [p.2](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/0__brake_testing_and_bleeding/10_ra__bleeding_brake_system_with_dsc3/page_1743/)):
- When it applies: "observe the filling and bleeding instructions for the following parts: 1. Brake master cylinder 2. Hydraulic unit DSC3 3. and components/connecting lines which are fitted between these assemblies. For all other work on the brake system (e.g. replacing brake calipers), the instructions "Bleeding brake system with ABS/ASC+T" must be observed. 34 00 048".
- Pressure: "(Brake fluid changer connected to max. 2 bar filling pressure) … Charging pressure should not exceed 2 bar."
- "Contrary to the instructions in the DIS, the bleeding routine must be restarted on each wheel."
- Flush: "rear right … until clear, bubble-free brake fluid emerges", then rear left, front right, front left.
- Rear circuit: "Connect bleeder hose … rear right … Close bleeder valve. Run bleeding routine with DIS with bleeder valve open. After completing the routine, press brake pedal 5 times down to floor; clear bubble-free brake fluid must emerge. Close bleed valve. Repeat procedure at rear left."
- Front circuit: the same, front right then front left.
- "Take care of rubber gasket (1) in lid."
- Final check with DIS "Service functions".
- The page also covers older DSC3 systems' "precharging pump", which the MK60 doesn't have.

**After caliper or hose work: TIS 34 00 048 "Bleeding brake system with ABS/ASC+T"** [read] ([p.1](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/0__brake_testing_and_bleeding/9_ra__bleeding_brake_system_with_abs_asc-t/), [p.2](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/0__brake_testing_and_bleeding/9_ra__bleeding_brake_system_with_abs_asc-t/page_1741/)):
- Connect DIS and call up the service function.
- Max 2 bar.
- Flush RR, RL, FR, FL until clear.
- "Bleed rear-axle brake circuit. To bleed the rear wheel brake, follow the procedure specified in the DIS."
- Front: "Open bleed valve. Fully depress brake pedal at least 12 times … Hold down brake pedal in fully depressed position. Close bleeder valve. Release brake pedal." Front right, then front left.

**Keeping air out, TIS 34 32 971** (rear hoses) [read]: "Apply pedal prop and depress brake pedal slightly. This prevents brake fluid from escaping from expansion tank after brake pipes have been disconnected (which would enable air to enter the braking system)." Fit the hose to the caliper first, then to the pipe; "Never twist brake hose". [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/32__brake_lines/3_ra__replacing_both_rear_brake_hoses/)

**BMW's own leak and booster test, TIS 34 00 Technical Data "Testing and bleeding brakes E46"** [read]:
- "Leak test with engine stopped: if applicable discharge vacuum reservoir by operating brake pedal firmly about 10 times. Approx. force on pedal 500 N equals approx. line pressure 36 bar. Max. pressure drop within 2 min. 8 %."
- "Brake booster function test (with engine running): approx. force on pedal 200 N … line pressure 75 … 90 bar."
- [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/34__brakes/0__brake_testing_and_bleeding/1_td__testing_and_bleeding_brakes_e46/)

**Parking brake, TIS 34 10 014 "Adjusting handbrake"** (identical in the Touring and M3 manuals) [read] ([Touring p.1](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/41__parking_brake/2_ra__adjusting_handbrake/), [p.2](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/41__parking_brake/2_ra__adjusting_handbrake/page_1795/), [p.3](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/41__parking_brake/2_ra__adjusting_handbrake/page_1796/), [M3 p.2](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/34__brakes/41__parking_brake/2_ra__adjusting_handbrake/page_1503/)):
- **Inspection:** "When 1st tooth is engaged, no braking effect"; left/right wheel forces on a roller rig within 30 % of the larger; "It should be possible to hold vehicle with handbrake"; readjust "whenever the actuation stroke is greater than 10 teeth".
- **Basic setting needed after** new shoes, new discs, resetting the adjuster, a stroke over 10 teeth, or new cables.
- **Shoes:** slacken the cable nuts fully; remove one wheel bolt per side; "Turn adjusting screw with a screwdriver until the wheel is no longer able to turn. Then unfasten the adjusting screw **10 notches**."
- **Cables:**
  - Hand-tighten the nuts evenly.
  - "the handbrake lever must be tightened 5 times to approx. 400 N hand-lever force with the release button pressed".
  - "Apply 2 teeth of handbrake lever and adjust adjusting nuts until braking action begins. Release handbrake lever; it must be possible to turn wheels easily."
  - Warning lamp: off when the lever is released. "1st tooth: No braking effect; indicator lamp can be lit. 2nd tooth: Braking effect must engage, indicator lamp must be lit."
  - On a roller rig: 0 teeth ≤ 150 N; 4th tooth ≥ 550 N.
- **Bedding in:**
  - On a roller rig: at least 800 N per wheel for about 40 s.
  - "When driving on road … At approx. 40 km/h, apply handbrake lever until braking action can be felt. Pull up handbrake lever into next catch and drive on for approx. 400 m … Repeat braking-in procedure if necessary; allow brake to cool down sufficiently."
- **TIS 34 41 Technical Data** (both manuals) [read]: drum 160 mm; maximum runout 0.1 mm; surface finish Ra 0.5–3.5 µm; minimum lining 1.5 mm. [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/34__brakes/41__parking_brake/1_td__parking_brake_e46/)
- **TIS 34 00 "General information on braking in new brake discs / brake pads"** [read]: test-brake at low speed; "Exaggerated drastic and continuous braking operations for faster braking in are not permitted"; no "wilful drastic braking in the first 200 km". [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/0__brake_testing_and_bleeding/2_ra__general_information_on_braking_in_new_brake_discs___brake_pads/)

**Master cylinder and circuits** [read; image]:
- **TIS 34 31 505 "Removing and installing/replacing brake master cylinder for DSC (MK60)":** "Remove pressure sensor "V" for DSC. Remove pressure sensor "H" for DSC. Detach brake lines (1)". Lines to 34 32 1AZ. "Replace self-locking nuts" to 34 31 1AZ. Replace the O-ring. Keep the booster's and the MC's push rods "on a single plane". [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/31__master_brake_cylinder/3_ra__removing_and_installing_replacing_brake_master_cylinder_for_dsc_%28mk60%29/)
- **TIS 34 52 555 (sensor "H") and 34 52 560 (sensor "V"):** "Detach pipe (1) from intermediate piece (2) and from master brake cylinder (3)". Calibrate with DIS after replacing a sensor, then bleed per 34 00 050. [H](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/52__electronic_components/8_ra__removing_and_installing_replacing_pressure_sensor__h__for_dsc/page_1825/), [V](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/52__electronic_components/9_ra__removing_and_installing_replacing_pressure_sensor__v__for_dsc/page_1827/)
- **What the photos show** [image]: in BMW's photos R34 0183 (V) and R34 0184 (H), the "V" pipe leaves the outlet next to the reservoir grommets, at the booster end. The "H" pipe leaves the outlet further forward. Booster end identified from the MC flange nuts at the left edge, as in R34 0323.

**Torques** [read]:
- **34 51** ([TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/4_tightening_torques/34__brakes/50__slip_control_systems_%28abs_asc%29/1_azd__slip_control_system_%28abs_asc-t_dsc%29/)):
  - pressure sensors "V" and "H" to MC, E46: 25 + 5 Nm
  - MK60 control unit to hydraulic unit, E46: 5 + 1 Nm
  - hydraulic-unit bracket: 8 Nm
  - wheel-speed sensor: 8 Nm
- **34 31** ([TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/4_tightening_torques/34__brakes/31__master_brake_cylinder/1_azd__brake_master_cylinder/)):
  - MC to booster, E46: 26 Nm, "Replace self-locking nut"
  - reservoir to MC: 3.5 Nm
- **34 11 / 34 21 in the M3 manual** ([front](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/34__brakes/11__front_brakes/1_azd__front_brake/), [rear](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/34__brakes/21__rear_brakes/1_azd__rear_brake/)):
  - disc screw: 16 Nm
  - front caliper carrier: 110 Nm
  - guide bolts (7 mm): "30 − 5 Nm"
  - rear carrier, E46: 65 Nm

**Brake-pipe unions, TIS 34 32 1AZ** (same page in both manuals) [read] ([TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/4_tightening_torques/34__brakes/32__brake_lines/1_azd__brake_lines/)):
- "Brake hose couplings": E36/E38/E39, M10×1 and M12×1, 18 Nm.
- E53, E60 … E83, **E85/E86**, M10×1 and M12×1, 14 Nm.
- Brake hose to caliper, E85/E83/E86: 19 Nm.
- **There is no E46 row.**

**Rear pipes, ETK "Rear brake pipe DSC" (Touring)** [read, image] ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/rear_brake_pipe_dsc/)):
- In the drawing the hydraulic unit sits at the front left.
- Item 1, pipe 34326752409 (M10/M12, 3,684 mm), runs straight to the near-side rear hose.
- Item 2, pipe 34326755704 (3,798 mm), runs to the union, item 3 (34326757282, M10×1). From there item 4, pipe 34326766825 (1,206 mm), crosses to the far-side hose.

### Inferences (ours)
- **After caliper and hose work, BMW still bleeds the rear circuit with the tester** (34 00 048, via 34 00 050's cross-reference). This contradicts `front_axle_brakes_abs.md`'s "caliper and hose work gets a conventional bleed".
  - Without DIS, INPA's MK60 routine is the DIY equivalent.
  - Keeping air out of the MC and DSC unit (pedal prop, plugged pipe ends) still avoids the full 34 00 050 procedure.
- **Master-cylinder circuits.** Front circuit (V) is on the push-rod outlet by the booster; rear circuit (H) on the forward, floating outlet. This is our reading of the photos plus ST056's "sensors … below the outlet ports for the front and rear brake circuits". Label both pipes before undoing anything. Option A doesn't open these joints.
- **Rear pipes.** The HU is on the car's left (ST056), so the "near side" in the ETK drawing is the left:
  - left rear: the single 3,684 mm pipe
  - right rear: the 3,798 mm pipe, the union and the 1,206 mm crossover
  - This also fits the lengths.
- **Union torque.** For E46 pipe unions use **14 Nm**, BMW's figure for the E46-derived Z4 (E85/E86) with the same MK60 generation. Treat it as the nearest BMW value, not an E46 one.
- **BMW's leak test at home.** INPA's DSC `STATUS_SENSOREN` reads both circuit pressures in bar (`front_axle_brakes_abs.md`). So BMW's test (~500 N on the pedal ≈ 36 bar, ≤ 8 % drop in 2 min) can be run without a gauge.

### Still open
- An E46 row for brake-pipe union torque (TIS 12/2007 has none).
- Settle it with an older TIS issue, or the Bentley table by VIN.

### Guide impact (writer: **front**)

1. **README.md:1352** (Parking brake, step 1) — "Turn it up on the left side and down on the right side until the rotor won't turn, then back it off 10 clicks. Then take up any slack in the cable at the lever inside the car ([BimmerWorld](…))."
   Replace with:
   > Turn it up on the left side and down on the right side until the rotor won't turn, then back it off **10 notches** (BMW TIS 34 10 014 agrees with BimmerWorld).
   >
   > With the cable nuts slack, pull the lever hard five times (about 400 N, 90 lb) with the button pressed. Then pull it to the 2nd tooth and tighten the cable nuts until braking just begins. Check:
   > - released: both wheels turn freely and the lamp is off
   > - 1st tooth: no braking (the lamp may light)
   > - 2nd tooth: braking starts and the lamp is on
   >
   > Readjust whenever the lever travels more than 10 teeth ([TIS 34 10 014](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/41__parking_brake/2_ra__adjusting_handbrake/page_1795/)).

2. **README.md:1353** (Bed in) — keep ECS, and add before it:
   > BMW's own bedding-in: at about 40 km/h (25 mph), pull the lever until you feel it brake, pull it one more notch and drive about 400 m (440 yd). Let it cool and repeat if needed ([TIS 34 10 014](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/41__parking_brake/2_ra__adjusting_handbrake/page_1796/)). Drum limits: 160 mm, runout under 0.1 mm, lining at least 1.5 mm ([TIS 34 41](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/34__brakes/41__parking_brake/1_td__parking_brake_e46/)).

   Also delete "BMW's own figures are in TIS group 34 41." and the open question at **README.md:2434**.

3. **README.md:1361–1363** (Bleeding, steps 2–4) — "BMW's limit for bleeder pressure is reported as 2 bar ([BMW TIS 34 00 050](…5series.net…), unverified)." / "Bleed right rear, left rear, right front, left front, then the clutch" / "If the DSC unit or master cylinder was replaced or ran dry, follow with INPA's DSC bleed routine".
   Replace with:
   > 2. BMW's limit is 2 bar (29 psi) ([TIS 34 00 050, E46](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/0__brake_testing_and_bleeding/10_ra__bleeding_brake_system_with_dsc3/)).
   > 3. Flush each wheel until the fluid runs clear and bubble-free: right rear, left rear, right front, left front.
   > 4. After caliper or hose work, BMW's procedure (34 00 048) then bleeds the rear circuit with the tester's routine. It bleeds the front by pumping the pedal fully at least 12 times per side and closing the bleeder with the pedal held down ([TIS 34 00 048](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/0__brake_testing_and_bleeding/9_ra__bleeding_brake_system_with_abs_asc-t/page_1741/)).
   > 5. After work on the master cylinder, the DSC unit or the pipes between them (34 00 050), run the tester routine at each wheel in turn, with that bleeder open: right rear, left rear, right front, left front. Restart the routine for every wheel. After each run press the pedal to the floor five times; the fluid must come out clear ([TIS 34 00 050, p.2](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/0__brake_testing_and_bleeding/10_ra__bleeding_brake_system_with_dsc3/page_1743/)). INPA's MK60 routine is the DIY equivalent ([DSC, brakes and steering angle](#dsc-brakes-and-steering-angle)). Then the clutch.

4. **README.md:1348** ("pressure-test any new hard lines with about 20 psi of air") and **README.md:825 / 836** — the earlier notes already advise dropping the air test for Option A.
   Add BMW's check:
   > Whenever you open a pipe, prop the pedal slightly down first so the reservoir can't drain ([TIS 34 32 971](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/34__brakes/32__brake_lines/3_ra__replacing_both_rear_brake_hoses/)). After filling, run BMW's leak test. Engine off, pump the pedal about 10 times, then hold about 500 N (110 lb), roughly 36 bar; the pressure may fall no more than 8 % in 2 minutes. Engine running, about 200 N (45 lb) should give 75–90 bar ([TIS 34 00](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/3_technical_data/34__brakes/0__brake_testing_and_bleeding/1_td__testing_and_bleeding_brakes_e46/)). INPA's DSC sensor status shows both circuits' pressure.

5. **Appendix (brakes torque table)** — add these rows:
   > | Brake-pipe unions, M10×1 / M12×1 | 14 Nm (10 ft-lb) | TIS has no E46 row; 14 Nm is BMW's figure for the E46-based Z4 (E85/E86), 18 Nm for the E36 | [TIS 34 32 1AZ](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/4_tightening_torques/34__brakes/32__brake_lines/1_azd__brake_lines/) |
   > | DSC pressure sensors "V"/"H" to master cylinder | 25 + 5 Nm | Calibrate with INPA/DIS after replacing | [TIS 34 51](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/4_tightening_torques/34__brakes/50__slip_control_systems_%28abs_asc%29/1_azd__slip_control_system_%28abs_asc-t_dsc%29/) |

   Add to `front_axle_brakes_abs.md`'s pipe map, labelled as inference from BMW's photos and the ETK drawing:
   > Front circuit (sensor "V") = master-cylinder outlet nearest the booster; left rear = pipe 34326752409; right rear = 34326755704 + union + 34326766825.

---

## Gap 6. Body repair (TIS 41)

### Cited findings

**1. Touring rear side wall, TIS 41 35 101 "Replacing rear left side wall (part replacement C- and D-pillar, top) (touring)"** (15 pages) [read; images R41 0873, R41 1493, R41 1091] ([p.1](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/35__side_panels/6_ra__replacing_rear_left_side_wall_%28part_replacement_c-_and_d-pillar_top%29_%28touring%29/), [p.2](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/35__side_panels/6_ra__replacing_rear_left_side_wall_%28part_replacement_c-_and_d-pillar_top%29_%28touring%29/page_2206/), [p.8](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/35__side_panels/6_ra__replacing_rear_left_side_wall_%28part_replacement_c-_and_d-pillar_top%29_%28touring%29/page_2212/), [p.11](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/35__side_panels/6_ra__replacing_rear_left_side_wall_%28part_replacement_c-_and_d-pillar_top%29_%28touring%29/page_2215/), [p.15](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/35__side_panels/6_ra__replacing_rear_left_side_wall_%28part_replacement_c-_and_d-pillar_top%29_%28touring%29/page_2219/)):
- **Removed first:** rear bumper, left trunk trims, fuel tank, tailgate, rear door, tail light, part of the rear harness, spare wheel, rear seat, headliner, side window.
- **Permitted cut lines:**
  - C-pillar: "A = 200 mm from roof edge".
  - D-pillar: "(A) = 10 mm from bore for support, ball head, gas-filled strut", and "(A) = 90 mm … (B) = 90 mm from bore for retaining clip, trim strip".
  - Cover for rear side member (outer sill): "(A) = 130 mm from center of bore … dia. 9.5 mm. (B) = 70 mm from center of bore … dia. 9.5 mm", and "(A) = 10 mm from center of bore for finishing strip, entrance … dia. 5.5 mm".
  - The replacement part (R41 0873) is the whole quarter: C- and D-pillar, wheel arch and sill end.
- **Drilled out:** the spot welds at the side window, the door aperture, the side-member cover reinforcement, the D-pillar water drain, the wheel-housing extension, the side panel to tail panel and to water drain, the wheel arch, and the side-member cover. "Heat side wall in area of D-pillar foam and detach from foam."
- **Joints:**
  - "Manufacture reinforcement plate … width = approx. 60 mm".
  - "Drill the holes for the plug welding … in the body", then "Clean connection faces … and coat with zinc dust paint".
  - "Install reinforcement plate … approx. 30 mm" (at the C-pillar, D-pillar and side-member cover).
  - Install the cavity foam parts.
  - "Arrange individual welding spots so close together on connection point for C-pillar that a continuous seam is created. Caution! Locate welding spots in a way which prevents distortion caused by heat elongation. Ensure that welded areas have cooled down sufficiently." The same applies at the D-pillar and the side-member cover.
- **Then:** weld the door aperture, side window, wheel-arch extension and tail panel, wheel arch, side-member cover and floor plate; braze the side panel to the water drain; tin and grind the C/D/sill joints.
- **Finally:** "Cringe [crimp] edge of wheel arch in indicated area (1). Seal connection points." Drawing R41 1091 shows area (1) running along most of the arch lip.

**2. Touring rear wheel arch, TIS 41 14 502** (outer section, side wall removed) **and 41 14 511** (complete arch) [read]:
- The car goes on a straightening bench; the strut/damper comes out.
- The replacement includes "Reinforcement, side section" and "Outer section of rear wheel arch".
- Drill out the welds at the side-panel reinforcement (door opening, outer arch, C-pillar), the outer-to-inner arch joints, the C-pillar, the side-member cover, the seat-belt holder and the D-pillar.
- Zinc-dust paint the faces, then weld.
- Inner arch (41 14 511): "Use straightening attachment … Weld up inner wheel arch section completely"; the side-member closing plate stays on the body.
- [41 14 502](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/14__wheel_wells/6_ra__replacing_rear_left_or_right_wheel_arch_outer_section_%28side_wall_removed%29_%28touri/), [41 14 511](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/14__wheel_wells/7_ra__replacing_complete_rear_left_wheel_arch/)

**3. E46 coupe side panel, TIS 41 35 101 "(partial replacement, C-pillar) (E46 Coupé)"**, in the M3 manual, i.e. the donor's body [read] ([p.1](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/41__body_%28coupe%29/35__side_panels/6_ra__replacing_rear_left_side_panel_%28partial_replacement_c-pillar%29_%28e46_coup%29/), [p.8](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/41__body_%28coupe%29/35__side_panels/6_ra__replacing_rear_left_side_panel_%28partial_replacement_c-pillar%29_%28e46_coup%29/page_1889/), [p.11](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/41__body_%28coupe%29/35__side_panels/6_ra__replacing_rear_left_side_panel_%28partial_replacement_c-pillar%29_%28e46_coup%29/page_1892/)):
- Cut lines: C-pillar 240 mm from the roof edge; a B-pillar "window" 195/265 mm from the roof edge; the sill cover cut referenced to the bores.
- Contact-pattern check: "Perform contact pattern test on adhesive areas … Contact pattern must be uniform. Maximum spacing of adhesive areas 1 mm".
- Backing plates about 40 mm wide (B- and C-pillar) and 60 mm (sill cover), "with 1/2 width into body".
- Bonding: "Coat adhesive areas of outer wheel arch section/side reinforcement and inner frame side member and B-pillar with adhesive 51 0 032".
- Spots set close "to create an enclosed seam".
- Protect the ITS head airbag: heat over 70 °C can stop it working.

**4. Luggage floor, TIS 41 12 535 "Replacing complete rear luggage compartment floor (tail panel removed) (E46)"** [read] ([p.1](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/12__luggage_compartment_floor/1_ra__replacing_complete_rear_luggage_compartment_floor_%28tail_panel_removed%29_%28e46%29/), [p.5](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/12__luggage_compartment_floor/1_ra__replacing_complete_rear_luggage_compartment_floor_%28tail_panel_removed%29_%28e46%29/page_2064/)):
- Set-up: straightening bench; fuel tank and rear axle carrier out.
- Drill off the spot welds along the side walls, the spare-wheel recess and the floor assembly.
- "Roughly cut side member at bore dia. 16 mm"; "Do not damage connecting parts (e.g. cross-members) and underlying metal sheets".
- Fit the new floor "with straightening attachment and clamp".
- Mark and drill plug-weld holes in the spare-wheel recess, the wheel-arch extension and the floor assembly.
- Zinc dust paint; "Clip shaped parts into areas (1) and bond with window adhesive".
- Weld the floor to the floor assembly, the spare-wheel recess and both side members (joint "Measurement (A) = approx. 25 mm"), the underside, and the side walls and wheel arches. Then grind.

**5. Gaps, TIS 41 00 "Gap dimensions on doors / engine hood and trunk lid"** [read] ([p.1](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/13_ra__gap_dimensions_on_doors___engine_hood_and_trunk_lid/), [p.2](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/13_ra__gap_dimensions_on_doors___engine_hood_and_trunk_lid/page_1919/)):
- "Lid seams 3.75 ± 0.75 mm. Permitted parallelism deviation 1 mm. Plane offset to relevant body section joining at back A = max. 1 mm inwards."
- "Door seams: Front side wall / front door = 4.25 ± 0.75 mm. Front door / rear door = 4.5 mm ± 0.75 mm. **Rear door / rear side wall = 4 ± 0.75 mm.** Doors / sill = 5 ± 1 mm. Permitted parallelism deviation 1 mm."
- Rear lid to rear side wall: flush 0 ± 0.5 mm, gap 4.25 ± 1 mm.
- Rear lid to tail panel: protrusion 0.5 ± 0.5 mm, gap 6 ± 1 mm.

**6. Body control dimensions, TIS 41 00 "Frame alignment control dimensions, body … BMW E 46 4-door / 2-door / Touring / Convertible"** [read; images R41 1101, R41 1103] ([side view](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/7_ra__frame_alignment_control_dimensions_body_side_view_bmw_e_46_4-door___2-door___/), [rear side view](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/9_ra__frame_alignment_control_dimensions_body_side_view_rear_end_bmw_e_46_4-door_/), [top view](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/10_ra__frame_alignment_control_dimensions_body_top_view_bmw_e_46_4-door___2-door___t/), [top view, rear](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/12_ra__frame_alignment_control_dimensions_body_top_view_rear_end_bmw_e_46_4-door___/)):
- Tolerance: "dimension over 1000 mm ± 2.0 mm … up to 1000 mm ± 1.0 mm".
- "Only use the indicated values for a rough inspection. Repairs can only be carried out correctly with the approved set of attachments and with straightening bench."
- One set of sheets covers all body styles, drawn on a sedan. There are no heights.
- Top view: B–G (front strut tower to rear damper mount) 3,086; H–E 2,609; H–F 3,011.
- Rear widths [image]:
  - rear damper mounts G–G 1,060
  - spring seats X–X 1,013
  - trailing-arm mounts P–P 1,296 and Q–Q 1,536
  - rear axle carrier mounts E–E 440 and F–F 660
  - R–R and S–S 845
- Side-view stations: A–B 579, B–C 672, C–D 1,238, D–G 876, G–S 661.
- Group number: in this TIS the sheets are under **41 00**, not 51 00.

**7. BMW's weld rules, TIS 41 00 "Welding and soldering steel parts"** [read] ([p.1](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/48_ra__welding_and_soldering_steel_parts/), [p.2](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/48_ra__welding_and_soldering_steel_parts/page_1975/)):
- Processes: MAG and resistance spot welding.
- "Take the number and location of weld spots and MAG weld seams from the separated part. Replace areas inaccessible to spot-welding tongs with MAG plug/spot welds at the same distance. Diameter of bores for plug/spot welds 8 mm."
- Consumables: "Steel welding wire - G3SI1 (SG2) or alternatively G4SI1 (SG3)"; "inert gas (82 % argon, 18 % CO2)".
- Preparation: "Remove the paint coating in an area of approx. 30 mm around the weld seam or spot. The zinc coating underneath must be removed during the MAG welding operation". "Coat all metal overlaps and weld spot flanges with welding primer."
- Welding: "the weld gap must be kept as small as possible"; "Minimum gap between welding spots 25 mm".
- Finishing: don't grind the base metal thin; re-seal every seam that was sealed; replace anti-noise compound.
- Brazing: "The MIG soldering procedure is not used in repairs for strength reasons. MIG soldered/brazed seams used in series production are replaced in repairs by MAG weld seams."
- Filler: up to 2 mm; tin beyond that, on visible outer skin only.
- **"General information about body repair"** [read]: bearing parts with sharp buckling that can't be cold-straightened "must be replaced"; plug welds for inaccessible spots; seal new seams immediately; disconnect the battery; the welder's earth within about 1 m of the weld. [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/15_ra__general_information_about_body_repair/)
- **"Opening weld joints"** [read]: "Set 8 mm dia. weld spot drill bit on punch mark and drill through top metal sheet." [TIS](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/35_ra__opening_weld_joints/)

### Inferences (ours)
- **The arch graft isn't a BMW repair.** BMW sections a Touring's quarter only high on the C- and D-pillars and at the sill, and replaces it whole. So the arch graft is not a BMW sectioning. What carries over is BMW's joint practice:
  - butt joints over a 40–60 mm backing strip, plug-welded through 8 mm holes
  - butt seams stitched with close spots, kept cool
  - zinc-rich primer
  - bonding with 51 0 032 where BMW bonds the outer arch to the side reinforcement (coupe)
  - the arch lip crimped and sealed
- **Plug-hole size.** BMW's 8 mm plug-weld holes are larger than the 6 mm thin-to-thin I-CAR hole quoted in `rear_arches.md`.
- **Wire and gas.** BMW's 82/18 argon/CO2 differs from the guide's 75/25. G3Si1/G4Si1 is the European grade usually cross-referenced to AWS ER70S-6.
- **Door gap.** The guide's "match your original gap" sits inside BMW's 4 ± 0.75 mm, which also gives a pass/fail.
- **Body checks.** The control dimensions give pass/fail checks for the rear after welding. The widths are symmetric about the centre line, so measure each to the centre line on both sides. BMW itself treats them as rough checks without a bench.
- **Floor.** BMW does a floor change on a bench with the axle carrier out and sections the rear side members at the 16 mm hole. A garage graft that keeps the rails whole (the guide's approach) is gentler than BMW's.

### Still open
- None for BMW data.
- Not in TIS: any procedure for welding a different-shaped (M3) arch into a Touring quarter.

### Guide impact (writers: **arches** for side panels, gaps and welding; **floor** for the trunk floor)

1. **README.md:745** — "BMW's body dimensions are in TIS group 51 00 ([newTIS](…))".
   Replace with:
   > BMW's E46 body control dimensions cover the sedan, coupe, Touring and convertible on one set of sheets (TIS 41 00): ±1 mm up to 1 m, ±2 mm above. At the rear: the damper mounts are 1,060 mm apart, the spring seats 1,013 mm, the trailing-arm mounts 1,296 and 1,536 mm, and the rear axle carrier mounts 440 and 660 mm. Front strut tower to rear damper mount is 3,086 mm. BMW calls them a rough check; correct repairs need a straightening bench ([TIS top view](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/10_ra__frame_alignment_control_dimensions_body_top_view_bmw_e_46_4-door___2-door___t/), [rear](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/12_ra__frame_alignment_control_dimensions_body_top_view_rear_end_bmw_e_46_4-door___/)).

   Also delete **README.md:2446** "BMW's E46 Touring body dimensions (TIS 51 00), which our research didn't open."
   In **README.md:319**, "body dimensions (group 51 00)" becomes "(group 41 00)".

2. **README.md:1160** (Wire, gas and settings) — keep Miller, and add:
   > BMW's own body-repair rules ([TIS 41 00](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/48_ra__welding_and_soldering_steel_parts/)):
   > - MAG welding with G3Si1 or G4Si1 wire (sold in the US as ER70S-6) and 82 % argon / 18 % CO2
   > - strip paint about 30 mm around each weld, and the zinc under MAG welds
   > - weld-through primer on every overlap
   > - copy the number and positions of the factory spots, with 8 mm holes for plug welds and spots at least 25 mm apart
   > - keep weld gaps as small as possible
   > - reseal every seam that was sealed
   > - no MIG brazing in repairs

   Same in **README.md:2319** (Key numbers row).

3. **README.md:1826** (Graft step 4) — add after the butt-gap sentence:
   > BMW's own sectioned joints on these bodies are butt joints over a backing strip: about 60 mm wide on the Touring (40 mm at the coupe's pillars), pushed about 30 mm into each side, and plug-welded. The butt seam is spot-stitched "so close together … that a continuous seam is created", with each area left to cool ([TIS 41 35 101, Touring, p.8](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/35__side_panels/6_ra__replacing_rear_left_side_wall_%28part_replacement_c-_and_d-pillar_top%29_%28touring%29/page_2212/), [p.11](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/35__side_panels/6_ra__replacing_rear_left_side_wall_%28part_replacement_c-_and_d-pillar_top%29_%28touring%29/page_2215/)). BMW cuts a Touring quarter only 200 mm below the roof edge on the C-pillar, at the D-pillar and at the sill, and never around the arch, so an arch graft is not a BMW repair.

4. **README.md:1830** (Join the inner wheelhouse), or the lip step — add:
   > On a new side wall BMW crimps the outer skin's arch edge over the inner flange along most of the arch, then seals it ([TIS, p.15](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/35__side_panels/6_ra__replacing_rear_left_side_wall_%28part_replacement_c-_and_d-pillar_top%29_%28touring%29/page_2219/)). On the coupe, which is the donor's body, BMW also bonds the outer arch section to the side reinforcement with adhesive 51 0 032, after a contact-pattern check (gap no more than 1 mm) ([TIS coupe, p.8](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/41__body_%28coupe%29/35__side_panels/6_ra__replacing_rear_left_side_panel_%28partial_replacement_c-pillar%29_%28e46_coup%29/page_1889/), [p.11](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/2_repair_instructions/41__body_%28coupe%29/35__side_panels/6_ra__replacing_rear_left_side_panel_%28partial_replacement_c-pillar%29_%28e46_coup%29/page_1892/)).

5. **README.md:1855** (Restoring the gap) and **README.md:789** ("shut gaps match the originals (feeler gauges)") — add:
   > BMW's E46 gaps: rear door to rear side wall 4 ± 0.75 mm, front door to rear door 4.5 ± 0.75 mm, doors to sill 5 ± 1 mm, each parallel within 1 mm ([TIS 41 00](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/13_ra__gap_dimensions_on_doors___engine_hood_and_trunk_lid/page_1919/)). Your measured gap should fall inside that band.

6. **README.md:1109 / 1122** (trunk floor, writer **floor**) — add:
   > BMW's own floor change ([TIS 41 12 535](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/12__luggage_compartment_floor/1_ra__replacing_complete_rear_luggage_compartment_floor_%28tail_panel_removed%29_%28e46%29/)):
   > - set-up: on a straightening bench, with the tail panel, tank and rear axle carrier out
   > - drill out the spot welds along the side walls, spare-wheel well and floor assembly, and cut the rear side members at their 16 mm hole
   > - clamp the new floor with the bench's attachments
   > - plug-weld it through drilled holes, with zinc-rich primer on every mating face
   > - bond the cavity foam parts in with window adhesive
   >
   > Keeping the rails whole, as this guide does, avoids BMW's rail cut.

---

## Gap 7. M3 rear wheel travel and bump stop

### Cited findings
- **TIS** [read]: none of the M3's 33 52/33 53 pages, the shock-absorber technical data, or the ride-height pages gives wheel travel or the bump-stop (auxiliary damper) length.
  - The rear damper procedure removes "plate (1), spacer, auxiliary damper (2) and protective tube (3)" and says to check them for damage.
  - [TIS 31 32 shock tester limits](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/3_technical_data/31__front_axle/32__shock_absorber/1_td__shock_absorbers_e46/) give tester limits only.
- **ST041** [read]: "The auxiliary cushion on the rear axle shock absorber is new. It differs from the standard auxiliary cushion by an additional groove and the black coloring"; the rear dampers have "piston 32mm, piston rod 15mm". No travel figure. [ST041 Running Gear](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear_djvu.txt)
- **BMW press technical data** (M3 2000–2006; dimensions, weights, suspension type, tyres) [read]: no spring travel. [BMW press PDF](https://press.bmwgroup.com/deutschland/article/attachment/T0082243DE/125133)
- **Search** [snippet]: an m3post post was summarised as "about 2.25 in of compression travel", generation unclear. The site was unreachable (DNS failure), so this is unverified.

### Still open
Yes. **To settle it:** before the donor's rear axle comes apart, measure and record:
- the bump stop's free length
- the gap from the bump stop to the damper body at the donor's ride height (the bump travel)
- the damper's extended and compressed lengths

### Guide impact (writers: **susp**, **arches**)
- **README.md:1815** ("Full bump. Jack the hub until the damper's bump stop is fully compressed…") and **JOB-CARDS.md:397** — add:
  > BMW publishes no wheel-travel or bump-stop figures for the E46 M3. On the donor, before teardown, record the rear bump stop's free length and its gap to the damper body at ride height (Worksheet), so you know how much bump travel the mock-up has to clear.

---

## Gap 8. Massachusetts inspection

### Cited findings
- **mavehiclecheck.com is reachable.** Its [station resources page](https://www.mavehiclecheck.com/stations-resources) posts station paperwork plus [540 CMR 4.00](https://www.mavehiclecheck.com/s/540cmr4.pdf) (MA Reg. #1360, dated 3-9-18) [read].
  - No safety-inspection manual or procedure handbook is posted.
  - The inspector-training modules are emissions only [read]: [Module 1 (2026)](https://www.mavehiclecheck.com/s/Module-1-Vehicle-Inspection-Requirements-v12026.pdf), "Vehicle Inspection Requirements"; Modules 2–4 (2012) cover repair technicians, motorist assistance and OBD inspection/repair ([Module 4](https://www.mavehiclecheck.com/s/MASS-Module_4-2012_Update.pdf)).
- **The safety procedure is the regulation itself** [read], 540 CMR 4.04:
  - **(1)** "Prior to beginning inspection, a visual check of the vehicle shall be made to determine that … the condition of the suspension system will not impede or interfere with the proper aiming of headlamps".
  - **(4)** Brakes, as quoted in `front_axle_brakes_abs.md`:
    - parking-brake hold at 1,200–1,300 rpm in the lowest gear
    - 30 ft / 80 ft stops from 20 mph
    - 125 lb pedal for 10 s with at least 20 % travel left
    - booster check
    - lines and hoses
  - **(5)** Exhaust, and **(12)(d)** "Holes or cracks … in the floor pans or other body panels which would permit the passage of exhaust gases into the passenger or trunk compartments".
  - **(6)(c)–(e):** "The front end (each side) of all vehicles will be raised by jacking and visually examined. Vehicles equipped with ball joints will be raised and checked in accordance with the applicable manufacturer's specifications … Reject a vehicle with excessive wear or play in any part of the steering mechanism, suspension or drive train … Reject a vehicle with broken, bent or missing shock absorbers or suspension springs."
  - **(12)(f)** unibody.
  - **(13)** altered heights: "The original manufacturers specified height … shall not be altered by elevating or lowering the chassis or body by more than two inches".
  - Sources: [540 CMR 4.00 PDF](https://www.mavehiclecheck.com/s/540cmr4.pdf); current text at [LII](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-4-04).
- **Module 1 (v2026)** [read]:
  - Exempt from emissions inspection: "Any light duty non-diesel vehicle with a model year earlier than 1996 or 15 or more model years old (e.g., beginning January 1, 2026, 2011 model year vehicles will be exempt)".
  - Engine switching: "1. The vehicle configuration following the engine switch shall be a certified configuration; 2. … same emissions certification category …; 3. Engine switching between California-certified and federally-certified vehicles is prohibited; 4. Engine switching between vehicle classes is prohibited".
  - Assembled and reconstructed vehicles take the test for "the fuel type, model year, and type of vehicle chassis indicated on the vehicle's certificate of registration".
- **Search** [snippet, 2 searches]: no public inspector manual or bulletin on measuring the height of cars. 540 CMR 6.00 covers 4WD vehicles only (as the guide already says).

### Inferences (ours)
- **Height.** No published method exists for cars. BMW's TIS ride height (Gap 1) is the clearest "manufacturer's specified height" for the Touring.
- **Ball joints.** Inspectors check ball joints against the "manufacturer's specifications", so keep BMW's front ball-joint play check handy (TIS 31 12 "Measuring play of wheel control joints" in the M3 manual; not read in detail).

### Still open
The RMV's internal inspector procedures, if any exist beyond 540 CMR 4.04. Ask the station, or the RMV Vehicle Safety and Compliance Services named in the RMV's 2018 inspector memo.

### Guide impact (writers: **susp** for height and suspension, **front** for brakes, **floor** for exhaust; **coding-power** for the emissions source)

1. **README.md:1931** (IMPORTANT box): "several mass.gov pages blocked automated reading, so confirm anything marked "(unverified)"".
   For the exemption and engine-switch statements, add the program's own current source:
   > [Vehicle Check Module 1 (2026)](https://www.mavehiclecheck.com/s/Module-1-Vehicle-Inspection-Requirements-v12026.pdf): exempt if "15 or more model years old (e.g., beginning January 1, 2026, 2011 model year vehicles will be exempt)"; engine switching "shall be a certified configuration … of the same emissions certification category".

2. **Massachusetts table (README.md:1935–1945)** — add a row:
   > | Suspension and steering | Front end jacked and inspected; ball joints checked "in accordance with the applicable manufacturer's specifications"; rejected for excessive play, or broken, bent or missing shocks or springs; and the suspension must not upset headlamp aim (540 CMR 4.04(1), (6)) | Check the ball joints and dampers before the appointment, and aim the headlights at the final ride height |

3. **The Ride height row** — use the Gap 1 text (BMW TIS baseline plus body heights).

---

## Sources tried and blocked

- **web.archive.org (Wayback pages and the CDX index):**
  - Every attempt (8) ended in a connection reset at the proxy tunnel ("tunnel closed before the exchange completed"), and WebFetch refuses the host.
  - archive.org/wayback/available returned HTTP 429 once.
  - Not worked around. archive.org itself (catalog search, metadata, downloads) worked.
- **archive.org catalog:** no E46 TIS export, Bentley E46 or body-repair item. Found only E36 Bentley excerpts. One item is a licensed electronic Bentley copy, not used.
- **5series.net attachments** (the E46 M3 DSC3 bleeding TIS PDF): Cloudflare error 1005, blocked. The same text is now [read] from the E46 TIS above.
- **princeton.edu/~sdepasqu/bmw/:** the directory page is a Cloudflare challenge (not bypassed). Known PDF URLs download directly (the E38 ride-height PDF returned 200), but no E46 files are known there.
- **m3post.com:** 404, then DNS failure.
- **GitHub eshkurti/multimodal-rag-service-manual** (found by code search):
  - API access is gated for this session.
  - The public raw file is an OCR of an E92/E93 manual, not E46, and was not used for E46 data.
  - It does show TIS's E9x normal position (2 × 68 kg front, 14 kg luggage, full tank).
- **mass.gov:** reachable (my guessed URL returned 404). Not needed, since the program's own site had the documents.
- **newTIS, e46fanatics, Bimmerforums:** not retried (blocked in earlier rounds).
- **WebSearch:** 8 calls.
  - Gap 8: 2 (MA inspector manual, height bulletin)
  - Gap 4: 3 (M3 plate on non-M cars, twice; plate part number)
  - Gap 5: 1 (E46 union torque)
  - Gap 7: 2 (bump stop; German BMW data)
