# Requests from the front writer (front axle, steering, brakes, ABS/DSC hardware)

## Conflicts

**C1. BMW's loaded position for ride height and alignment (susp owns Wheel alignment; integrator if susp misses it).** My notes now source it: BMW ST056 "Suspension Systems and Alignment Procedures" (01/2003) gives 68 kg in each front seat, 68 kg in the rear seat, 21 kg in the trunk and a full tank "for most vehicles", but says "Usually E39 M5 and E36/E46 M3 are measured without any weight", and sends you to TIS group 32 "Normal Position/Inspection Conditions". Ride height is measured from the lower edge of the rim to the lower edge of the wheel housing (TIS group 31 front, 33 rear). The susp notes agree and add BMW ST503 (03/2006): "Normal Position" means no weight added, "Design Position" the weight added. Status: the susp writer has already put this into Wheel alignment, Card 12d and the Alignment worksheet (align unladen with a full tank, the M3's condition), so no request is needed; I've kept my own text consistent with it. Source URL: https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/01%20Suspension%20Systems%20and%20Alignment%20Procedures%201-20-03_djvu.txt

**C2. Only the front anti-roll-bar clamp nuts wait for ride height.** The control-arm bushing bracket bolts (59 Nm, new bolts) carry no ride-height condition in Flow p.2 ("always replace") or Department 69 (TIS); only the bar clamp nuts (21 Nm) are marked "tighten in normal position to avoid preload" (Flow p.6). I've moved the bracket bolts into Phase 8 on stands in every fragment I own. The susp writer has already fixed Card 12d and the Alignment worksheet. Still to change: Phase 12 step 6 (integrator, R17), Worksheet "Phase 12: at ride height" (integrator, R37), Appendix torque table (integrator, R1, R3, R5). Wording note: BMW's phrase is "normal position", which ST503 (in the susp notes) defines as the car with no weight added; so for these nuts I've written "with the car's weight on its wheels", not "at loaded ride height". Please keep that wording for the front clamp nuts.

**C3. MK60 rack curve on the Touring's own unit (coding-power, Session 5).** The coding notes say a non-M MK60 without the M3 curve `wert_05` "is set to its closest, `wert_02`", and Session 5's optional note says "leave `wert_10`/set `wert_02`". My notes show the M3 steering is slower than the Touring's: 15.4:1 against 13.7:1 for the 2003 US 325i Sport Wagon (BMW USA 2003 spec sheets), about 12%. `wert_02` is the ZHP curve (liam821: "02=ZHP") and `touring_s` is reported as the setting for a faster rack (e46fanatics 1264623), so both move away from the M3 rack, not toward it. My README DSC section says: leave the rack setting as coded (our inference). Status: coding-power's Session 5 already recommends leaving the unit as coded and says `touring_s` doesn't match the slower M3 rack, so this is settled as long as no text calls `wert_02` the "closest" curve.

**C4. Draining the brake fluid in Phase 4 (integrator).** Phase 4 step 2, Card 4 and the Fluids log tell the builder to drain the Touring's brake fluid. My notes (TIS 34 00 050) say that letting the master cylinder, the DSC unit or the pipes between them run dry makes INPA's DSC routine necessary, while keeping the MK60 full (pipe ends capped, reservoir full, pedal depressor) means a conventional bleed is enough, because Option A changes no hard line. Phase 8 and Card 8c now assume the fluid stays in. See R18, R30 and R38.

**C5. Steering ratio figures.** The README rack table (mine) keeps the NAM3 figure "13.7:1 in a 330i" for the ZHP-type rack 32132282296, and the coding notes give "330i ZHP ~13.7:1 (forum)". BMW USA's 2003 sheet gives the standard 325i Sport Wagon 13.7:1 too. So 13.7:1 doesn't distinguish the ZHP rack from the standard one; I've used BMW USA's figure for your Touring and not claimed anything about the ZHP rack against it.

**C6. Front strut-top nut torque.** The susp notes quote "Front top mount 24 Nm" (Flow p.3). My notes show a conflict: 24 Nm in the M3 compilation, 34 Nm in TIS for the non-M E46 (Department 69) and for the E85 Z4 (an owner reading TIS), with new nuts. If any susp text gives 24 Nm alone, it should carry the conflict (see R4).

**C7. Massachusetts lamp wording.** BMW ST056: the red BRAKE lamp means low fluid or the parking brake applied; DSC and ABS faults light the yellow BRAKE lamp, the ABS lamp and the DSC lamp. The Massachusetts table's "A DSC or ABS fault that lights the red lamp fails" is wrong on the lamp colour (R15).

## README

### R1: README 0870__torque-values.md: say which front joint waits for ride height
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > the notes say which joints those are. Ball joints and plain brackets can be torqued in any position.
- **New text:**
  > the notes say which joints those are. At the front that's only the anti-roll-bar clamp nuts; the control-arm bushing brackets carry no ride-height condition in Flow or Department 69. Ball joints and plain brackets can be torqued in any position.
- **Why:** correction 2; only the clamp nuts are marked "tighten in normal position" (Flow p.6). Notes: Q1 torques, Takeaway 2.

### R2: README 0870__torque-values.md: subframe bolts are single-use
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Front axle support (subframe) to body, M12 10.9 | 110 Nm (81 ft-lb) | Tighten the rear bolts first; their dowels center the subframe | [Flow p.2](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing); [FCP Euro – S54 rod bearings (2022), 40:58](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2458s) |
- **New text:**
  > | Front axle support (subframe) to body, M12 10.9 | 110 Nm (81 ft-lb) | New bolts 31116781023 (TIS: replace). Tighten the rear bolts first; their dowels center the subframe | [Flow p.2](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing); Department 69; [FCP Euro – S54 rod bearings (2022), 40:58](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2458s) |
- **Why:** correction 6; Department 69 (TIS): "M12 grade 10.9. Replace bolts". Notes: Q1 torques.

### R3: README 0870__torque-values.md: bracket bolts have no ride-height condition
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts; at ride height | Flow p.2; [FCP Euro (2022), 42:06](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2526s) |
- **New text:**
  > | Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts (33306760652); any position, so on stands in Phase 8 | Flow p.2; Department 69; [FCP Euro (2022), 42:06](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2526s) |
- **Why:** correction 2. Notes: Q1 torques, Takeaway 2.

### R4: README 0870__torque-values.md: strut-top nut torque conflict
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Strut top mount to body, M8 collar nuts | 24 Nm (18 ft-lb) | | Flow p.3 |
- **New text:**
  > | Strut top mount to body, M8 collar nuts | **The sources conflict:** 24 Nm (18 ft-lb) in the M3 compilation; 34 Nm (25 ft-lb) in TIS for the non-M E46 and the E85 Z4 | New nuts 31316769731. Check TIS for the M3 top mount | Flow p.3; Department 69; [Z4-forum](https://z4-forum.com/threads/replacement-front-struts-torque-specs.113285/) |
- **Why:** correction 5. Notes: Q1 torques and gaps.

### R5: README 0870__torque-values.md: front clamp nuts wording
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Front anti-roll bar bracket nuts, M8 | 21 Nm (15 ft-lb) | At ride height | Flow p.6 |
- **New text:**
  > | Front anti-roll bar bracket nuts, M8 | 21 Nm (15 ft-lb) | With the car's weight on its wheels (Phase 12): "tighten in normal position to avoid preload". The only front joint so marked | Flow p.6 |
- **Why:** corrections 1–3. Notes: Q1 torques.

### R6: README 0870__torque-values.md: M3 inner tie rod is 110 Nm
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Inner tie rod to rack | 100 + 10 Nm, as the compilation prints it | Check TIS for what the "+ 10" means | Flow p.9 |
- **New text:**
  > | Inner tie rod to rack, M3 | 110 Nm (81 ft-lb) | TIS gives 110 Nm for the M3; the compilation's "100 + 10 Nm" is TIS's figure for other E46s | Department 69; Flow p.9 |
- **Why:** correction 4; Department 69 cites TIS: "All except M3: 100 Nm +10 Nm… M3: 110 Nm (81 ft-lb)". Notes: Q2 torques.

### R7: README 0870__torque-values.md: add the power-steering line torques
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Steering shaft lower joint Torx bolt, M8×33 | 22 Nm (16 ft-lb) | New bolt | BMW SI B11 04 04; Flow p.12 |
- **New text:**
  > | Power-steering hollow bolts, M16 (pump outlet and rack) | 40 Nm (30 ft-lb) | New A16×22 sealing rings 32411093597 | Flow p.8 |
  > | Rack banjo bolt with check valve, M14 | 35 Nm (26 ft-lb) | New A14×20 sealing rings 32411093596 | Flow p.8 |
- **Why:** correction 7. Notes: Q2 torques (Flow p.8, image).

### R8: README 0870__torque-values.md: power-steering pump bolts (Engine table)
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Crank pulley bolts; power-steering pump bolts | 23 Nm (17 ft-lb) | One video only | [FCP Euro – S54 rod bearings (2022), 38:07](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2287s), [39:18](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2358s) |
- **New text:**
  > | Crank pulley bolts | 23 Nm (17 ft-lb) | One video only | [FCP Euro – S54 rod bearings (2022), 38:07](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2287s) |
  > | Power-steering pump: mounting bolts M8×80; pulley bolts M8×14 | Mounting bolts 21 Nm (15 ft-lb); pulley bolts 27 Nm (20 ft-lb) | The M3 compilation's figures; FCP's video gives 23 Nm ([39:18](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2358s)) | [Flow p.11](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) |
- **Why:** correction 7. Notes: Q2 torques (Flow p.11, image).

### R9: README 0870__torque-values.md: brake rows
- **Change:** replace (three rows, then insert one)
- **Find (exact current text, for replace, delete or insert after):**
  > | Front caliper carrier, M12×1.5 | 110 Nm (81 ft-lb) | | Flow p.25 |
- **New text:**
  > | Front caliper carrier, M12×1.5 | 110 Nm (81 ft-lb) | The M3's M12×1.5×41 bolts (34111156989 or 34116767217) | Flow p.25; Department 69 |
- **Find:**
  > | Caliper guide bolts, front and rear | 30 Nm (22 ft-lb) | | Flow pp.24–25 |
- **New text:**
  > | Caliper guide bolts, front and rear | 30 Nm (22 ft-lb) | Department 69 gives 25–30 Nm | Flow pp.24–25; Department 69 |
- **Find:**
  > | Rear caliper carrier, M10 | 65 Nm (48 ft-lb) | Micro-encapsulated screws | Flow p.24 |
- **New text:**
  > | Rear caliper carrier, M10 | 65 Nm (48 ft-lb) | New micro-encapsulated screws 34203414763 | Flow p.24; Department 69 |
- **Insert after:**
  > | Rotor retaining screw | 16 Nm (142 in-lb) | | Flow p.23 |
- **New text:**
  > | Brake dust-shield screws, M6 | 9 Nm (80 in-lb) | | Flow p.23 |
- **Why:** notes, Guide-ready torque table "Brakes" (Flow pp.23–25; Department 69).

### R10: README 0880__fluids-and-capacities.md: power-steering fluid is ATF
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Power steering | **Not found.** Read the cap on the donor's M3 reservoir (ATF or CHF 11S) and don't mix the two; BimmerWorld lists CHF 11S for no E46 | Not found | [BimmerWorld CHF 11S](https://www.bimmerworld.com/Suspension-Steering/Pentosin-CHF11S-Hydraulic-Fluid-BMW-82111468041.html) |
- **New text:**
  > | Power steering | ATF (Dexron III type), not CHF 11S; don't mix the two. ETK pairs the reservoir on both cars with the "ATF" label 71246798132, and BMW's original fill for cars without active steering was ATF Dexron III. A new reservoir cap may say CHF 11S whatever the car | **Capacity not found;** fill to the mark on the lid | [ETK: label](https://bmwfans.info/parts-catalog/71246798132/), [FCP Euro](https://www.fcpeuro.com/blog/heres-how-to-pick-the-right-power-steering-fluid-for-your-car-), [M346 Projects – Pt 13 first start (2024), 08:00](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=480s) |
- **Why:** correction 8. Notes: Q2 reservoir and fluid evidence, inference "Fluid: ATF".

### R11: README 0880__fluids-and-capacities.md: brake fluid is DOT 4 low-viscosity
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Brake and clutch fluid | **Not found.** Check the reservoir cap and TIS | Allow about 1.5 L (1.6 US qt) for filling and bleeding; one INPA DSC bleed on a Z4 M's MK60 used about 1.25 L | Z4 M bleed: [z4-forum](https://z4-forum.com/threads/bleed-the-abs-dsc-system-using-inpa.146558/) |
- **New text:**
  > | Brake and clutch fluid | DOT 4 low-viscosity, BMW 81220142156. BMW's bleeding instructions require it for DSC cars without a pre-charge pump, which the MK60 is (unverified: seen only in a summary). Pressure bleeder at no more than 2 bar (29 psi) | Allow about 1.5 L (1.6 US qt) for filling and bleeding; one INPA DSC bleed on a Z4 M's MK60 used about 1.25 L | [BMW TIS (2005)](https://5series.net/forums/attachments/diy-do-yourself-14/5580-brake-fluid-flush-ra__bleeding_brake_system_with_dsc.pdf), [BimmerWorld](https://www.bimmerworld.com/Brakes/Genuine-BMW-DOT4-ESL-Low-Viscosity-Brake-Fluid-81220142156.html), [BMW TIS 34 00 050](https://xoutpost.com/attachments/x5-e53-forum/83406-low-speed-braking-34-00-050-bleeding-brake-system-dsc.pdf); Z4 M bleed: [z4-forum](https://z4-forum.com/threads/bleed-the-abs-dsc-system-using-inpa.146558/) |
- **Why:** corrections 9 and 10. Notes: Q3 brake fluid and bleeding.

### R12: README 0920__open-questions-to-verify.md: answered and new chassis questions
- **Change:** replace (the Chassis and brakes items below), then one Engine item
- **Find (exact current text, for replace, delete or insert after):**
  > - An E46 ride-height specification, and BMW's "normal loaded position" weights for the E46.
- **New text:**
  > - BMW's E46 ride-height values (TIS groups 31 and 33). The loading is now sourced: BMW ST056 gives 68 kg in each front seat, 68 kg in the rear seat, 21 kg in the trunk and a full tank for most cars, and says M3s are usually measured without weight.
- **Find:**
  > - What the Flow compilation's "100 + 10 Nm" (inner tie rod) and "25 + 5 Nm" (DSC pressure sensor) mean.
- **New text:**
  > - What the Flow compilation's "25 + 5 Nm" (DSC pressure sensor) means. (Its "100 + 10 Nm" for the inner tie rod is TIS's non-M figure; the M3's is 110 Nm.)
  > - The front strut-top nut torque: 24 Nm in the M3 compilation, 34 Nm in TIS for the non-M E46 and the E85 Z4.
  > - Where the M3 reinforcement plate's four extra screws (12 against the Touring's 8) thread in.
- **Find:**
  > - The power-steering fluid for the M3 rack (the reservoir's ATF label against CHF 11S), and the brake-fluid specification.
- **New text:**
  > - The power-steering system's capacity. (The fluid is ATF and the brake fluid DOT 4 low-viscosity: see [Fluids and capacities](#fluids-and-capacities).)
- **Find:**
  > - Whether the M3 master cylinder suits the Touring's booster, and how M3 calipers feel on the Touring's master cylinder.
- **New text:**
  > - Whether the M3 master cylinder suits the Touring's booster; BMW's bore sizes for both master cylinders and the calipers, and which master-cylinder outlet feeds the front circuit. Forum sizes suggest a front pedal about 10% longer and lighter than an M3's on the Touring's master cylinder (our estimate).
- **Find:**
  > - How the S54's brake-booster vacuum hose reaches the Touring's booster port; on the M3 it connects from the other side.
- **New text (delete the item; answered):**
  > (nothing)
- **Find:**
  > - BMW's limit for pressure-bleeder pressure (2 bar per TIS 34 00 050, a source we couldn't open).
- **New text (delete the item; answered):**
  > (nothing)
- **Find:**
  > - BMW's own parking-brake adjustment and bedding figures (TIS 34 41).
- **New text:**
  > - BMW's E46 parking-brake text (TIS 34 41): the E46 workshop manual and BimmerWorld back the adjuster off 10 notches, a TIS printout of unidentified model 8.
  > - How many teeth the M3 front hub's pulse wheel has (the rear gives 48 pulses per turn on every rear-drive E46). A steady-speed comparison of the four wheel speeds proves it on the car.
- **Find:**
  > - Why one 2004 Touring's own wheel-speed sensors gave an ABS light in M3 hubs; it was never diagnosed.
- **New text (delete the item; answered as far as the sources allow — see DSC, brakes and steering angle):**
  > (nothing)
- **Find (Engine and driveline):**
  > - The VANOS fasteners, crank pulley and power-steering pump bolts: one video each.
- **New text:**
  > - The VANOS fasteners and crank pulley bolts: one video each.
- **Why:** correction 22, plus the gaps in Q1–Q4 of my notes.

### R13: README 0290__consumables-and-single-use-parts.md: front axle, steering and brake consumables
- **Change:** replace two rows, add three rows
- **Find (exact current text, for replace, delete or insert after):**
  > | Front axle fasteners: M14 self-locking nuts 31106774714 (control arms and strut tops), ball-joint nuts 31106777806, tie-rod-end nuts 32216769539, strut clamp bolts 31306779487, top-mount nuts 31316769731, reinforcement-plate bolts 31106772199 (12), steering-joint bolts 32306778609 | Buy new | Self-locking or stretch fasteners |
- **New text:**
  > | Front axle fasteners: subframe bolts 31116781023 (4), control-arm bracket bolts 33306760652 (4), M14 self-locking nuts 31106774714 (control arms and strut tops), ball-joint nuts 31106777806, tie-rod-end nuts 32216769539, strut clamp bolts 31306779487, top-mount nuts 31316769731 (6), reinforcement-plate bolts 31106772199 (12), anti-roll-bar link nuts 33306760587 (4) and clamp nuts 07119905374 (4), steering-joint bolts 32306778609; front hub collar nuts 31211128336 only if a hub comes off | Buy new | Self-locking or stretch fasteners; TIS says to replace the subframe bolts ([Department 69](https://www.department69.com/articles/bmw-e46-torque-specs-complete-reference-all-engines)) |
- **Insert after:**
  > | Brake pads and rotors, front and rear | Buy new | |
- **New text:**
  > | Rear caliper carrier screws 34203414763 (4) | Buy new | Micro-encapsulated M10×26.5 |
  > | Power-steering sealing rings: A16×22 32411093597 (4), A14×20 32411093596 (2) | Buy new | For the hollow bolts and the rack banjo |
  > | Brake-booster port grommet 34336765316 | Buy new | Takes the M3's check valve in your booster ([Brakes and bleeding](#brakes-and-bleeding)) |
- **Find:**
  > | Fluids: BMW 10W-60 engine oil, MTF-LT-2 gearbox oil, SAF-XJ+FM diff oil with friction modifier, power-steering fluid as marked on the M3 reservoir cap, BMW coolant and distilled water, brake fluid | Buy new | Specifications and quantities: [Fluids and capacities](#fluids-and-capacities) |
- **New text:**
  > | Fluids: BMW 10W-60 engine oil, MTF-LT-2 gearbox oil, SAF-XJ+FM diff oil with friction modifier, ATF (Dexron III type) for the power steering, BMW coolant and distilled water, DOT 4 low-viscosity brake fluid (BMW 81220142156) | Buy new | Specifications and quantities: [Fluids and capacities](#fluids-and-capacities) |
- **Why:** notes, Guide-ready parts tables (front axle "Buy new" rows; steering rings; brakes); corrections 6, 8, 9, 12.

### R14: README 0630__troubleshooting.md: ABS lamp row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | ABS lamp after the first drive | An MK20 donor's wheel-speed sensors, or a sensor not seated | [DSC, brakes and steering angle](#dsc-brakes-and-steering-angle) |
- **New text:**
  > | ABS lamp after the first drive | Faults stored while parts were unplugged (clear them and drive), a sensor not seated, a damaged pulse wheel, mixed tire sizes, or an MK20 donor's sensors. The DSC's wheel-speed faults are 5D90–5DC5, one block per wheel; the last digit: 0 wiring, 1 or 3 seating, 2 pulse wheel, 4 or 5 tooth count or tire size | [Wheel-speed and pad-wear sensors](WIRING-AND-CODING.md#wheel-speed-and-pad-wear-sensors), [DSC, brakes and steering angle](#dsc-brakes-and-steering-angle) |
- **Why:** correction 15; fault list from the DSC_MK60 SGBD. Notes: Q4 cited findings and inferences.

### R15: README 0730__massachusetts.md: Brakes row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Brakes | The red brake warning lamp stays off, and the car stops from 20 mph within 30 ft (540 CMR 4.04(4)) | A DSC or ABS fault that lights the red lamp fails; see [DSC, brakes and steering angle](#dsc-brakes-and-steering-angle) |
- **New text:**
  > | Brakes | The inspector tests the service brake at 4–8 mph for pull, the parking brake against the engine in the lowest gear at 1,200–1,300 rpm, and a stop from 20 mph within 30 ft on the foot brake or 80 ft on the parking brake. With the car stopped, about 125 lb on the pedal for 10 s must hold, with at least 20% of the travel left and the brake warning lamp off; the booster must assist when the engine starts; and lines and hoses must be free of leaks and chafing (540 CMR 4.04(4)) | Run the same tests first: [Brakes and bleeding](#brakes-and-bleeding). BMW's red brake lamp means low fluid or the parking brake on; DSC and ABS faults light the yellow brake, ABS and DSC lamps ([BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf)). Get them all dark |
- **Why:** correction 16; 540 CMR 4.04(4) read in full (LII). Notes: Q3 Massachusetts, Q4 ST056 lamps.

### R16: README 0510__driveline-and-rear-axle.md: Tenza's ABS light
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > One S54 Touring, a 2004 car with a 2002 donor, had an ABS light at first start with its own sensors in the M3 hubs that was never diagnosed; its builder's fallback of splicing in the donor's sensor leads would have put MK20 sensors on an MK60, so don't ([Tenza – 5 things, part 2 (2021), 03:15](https://www.youtube.com/watch?v=mDBiRn30fEs&t=195s)).
- **New text:**
  > One S54 Touring, a 2004 car with a 2002 donor, showed an ABS light at its first start with its own sensors in the M3 hubs, but the car was standing and its brakes not yet bled, and three months later the builder reported no problems; it isn't evidence that the sensors don't suit ([DSC, brakes and steering angle](#dsc-brakes-and-steering-angle)). His fallback of splicing in the donor's sensor leads would have put MK20 sensors on an MK60, so don't ([Tenza – 5 things, part 2 (2021), 03:15](https://www.youtube.com/watch?v=mDBiRn30fEs&t=195s), [04:00](https://www.youtube.com/watch?v=mDBiRn30fEs&t=240s)).
- **Why:** correction 14. Notes: Q4, Tenza in order.

### R17: README 0430__phase-12-front-end-first-start-and-shakedown.md: ATF, Tenza, and the front joints
- **Change:** replace (three places)
- **Find (exact current text, for replace, delete or insert after):**
  > and the power-steering system with the fluid marked on the M3 reservoir's cap ([Fluids and capacities](#fluids-and-capacities)).
- **New text:**
  > and the power-steering reservoir with ATF, to about 25 mm below its edge with the engine off; then bleed it after the start as [Brakes and bleeding](#brakes-and-bleeding) describes. One build's pump rattled dry at its first start until the ATF went in ([M346 Projects – Pt 13 first start (2024), 08:00](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=480s)).
- **Find:**
  > An M3 built before 09/2002 has sensors that don't suit your harness, and one S54 Touring got an ABS light, never diagnosed, with non-M sensors in its M3 hubs ([Tenza Motorsports – first start (2021), 07:18](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=438s)), so check this before you go further ([DSC, brakes and steering angle](#dsc-brakes-and-steering-angle)).
- **New text:**
  > An M3 built before 09/2002 has sensors that don't suit your harness. If a speed is missing or the ABS lamp stays on, read the DSC fault memory before you go further: 5D90–5DC5 are the wheel-speed faults, and the last digit points to wiring, seating, the pulse wheel or tire size ([manual](WIRING-AND-CODING.md#wheel-speed-and-pad-wear-sensors)).
- **Find:**
  > 6. **Alignment:** torque the front rubber-bushed joints with the car's weight on its wheels, then have the car aligned to BMW's E46 M3 figures at its own loaded ride height ([Wheel alignment](#wheel-alignment), [Shop briefs](#shop-briefs)).
- **New text:**
  > 6. **Alignment:** torque the front anti-roll-bar clamp nuts, 21 Nm (15 ft-lb), with the car's weight on its wheels; everything else at the front was torqued on stands in Phase 8. Then have the car aligned to BMW's E46 M3 figures, unladen with a full tank, BMW's test condition for the M3 ([Wheel alignment](#wheel-alignment), [Shop briefs](#shop-briefs)).
- **Why:** corrections 3, 8 and 14. Notes: Q1 torques, Q2 fluid, Q4 Tenza.

### R18: README 0350__phase-4-strip-your-touring.md: keep the brake fluid in
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > 2. Disconnect the battery. Drain the oil, coolant, power-steering fluid and brake fluid.
- **New text:**
  > 2. Disconnect the battery. Drain the oil, coolant and power-steering fluid. **Leave the brake fluid in:** your brake pipes stay, so cap each pipe end as you open it (the front hoses at the strut brackets, the rear hoses at their brackets, the clutch line), keep the reservoir full, and leave a pedal depressor holding the pedal slightly down. If the DSC unit doesn't run dry, a conventional bleed is all it needs later; if it does, it needs INPA's routine ([Brakes and bleeding](#brakes-and-bleeding)).
- **Why:** correction 11 and conflict C4: BMW TIS 34 00 050 requires the tester routine only after work on the master cylinder, the hydraulic unit or the pipes between them. Notes: Q3 bleeding, procedure A step 1.

### R19: README 0080__documented-builds-compared.md: Tenza row and item 6
- **Change:** replace (two places)
- **Find (exact current text, for replace, delete or insert after):**
  > | M3 front brakes; M3 and non-M wheel-speed sensor plugs didn't mate, so non-M sensors went in the M3 hubs and the ABS light came on |
- **New text:**
  > | M3 front brakes; M3 and non-M wheel-speed sensor plugs didn't mate (an MK20 donor), so non-M sensors went in the M3 hubs. An ABS light at the first start, before the brakes were bled; no problem reported three months later |
- **Find:**
  > it fitted non-M sensors in the M3 hubs and got an ABS light ([Tenza Motorsports – 5 things they don't tell you, part 2 (2021), 03:20](https://www.youtube.com/watch?v=mDBiRn30fEs&t=200s), [Tenza Motorsports – M3 touring build finally runs! (2021), 07:20](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=440s)),
- **New text:**
  > it fitted non-M sensors in the M3 hubs and saw an ABS light at the first start, standing and before the brakes were bled; three months later the builder reported no problems ([Tenza Motorsports – 5 things they don't tell you, part 2 (2021), 03:20](https://www.youtube.com/watch?v=mDBiRn30fEs&t=200s), [04:00](https://www.youtube.com/watch?v=mDBiRn30fEs&t=240s), [Tenza Motorsports – M3 touring build finally runs! (2021), 07:20](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=440s)),
- **Why:** correction 14. Notes: Q4, Tenza in order.

### R20: README 0900__key-numbers.md: steering against the Touring's, and brake numbers
- **Change:** replace (one row becomes two)
- **Find (exact current text, for replace, delete or insert after):**
  > | Steering | M3 rack 47 mm per turn (15.4:1); ZCP and CSL 50 mm per turn (about 14.5:1) | [NAM3 steering thread](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189-comprehensive-steering-information-thread) |
- **New text:**
  > | Steering | M3: 15.4:1 overall, 3.0 turns lock to lock, turning circle 11.0 m (36.1 ft); 2003 US 325i Touring: 13.7:1, 3.0 turns, 10.5 m (34.4 ft). So the M3 rack makes your steering about 12% slower. M3 rack 47 mm per turn; ZCP and CSL 50 mm per turn (about 14.5:1) | BMW USA [M3](https://www.press.bmwgroup.com/usa/article/attachment/T0022150EN_US/41463) and [325i Sport Wagon](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437) (2003); [NAM3 steering thread](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189-comprehensive-steering-information-thread) |
  > | Brakes and DSC | Pressure bleeder no more than 2 bar (29 psi); DSC brake-pressure sensors under 5 bar (73 psi) with the pedal released; ABS works above 12 km/h (7 mph); wheel-speed sensors switch 7 mA and 14 mA on a 12 V supply | [BMW TIS 34 00 050](https://xoutpost.com/attachments/x5-e53-forum/83406-low-speed-braking-34-00-050-bleeding-brake-system-dsc.pdf), [BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) |
- **Why:** correction 21; Takeaway 7 and 13. Notes: Q2 BMW USA, Q3 bleeding, Q4 ST056.

### R21: README 0120__budget.md: brakes line covers the new small parts
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Brakes: pads, rotors, M3 front hoses | \$600–\$1,500 | Estimate |
- **New text:**
  > | Brakes: pads, rotors, pad-wear sensors, M3 front hoses, booster grommet, DOT 4 low-viscosity fluid; parking-brake shoes if worn | \$600–\$1,500 | Estimate |
- **Why:** parts added to the Parts list this round; no new prices in my notes.

### R22: README 0330__phase-2-strip-the-donor.md: keep the booster check valve
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > and the DSC unit with its lines and the master cylinder, plus the brake booster if you plan DSC option B.
- **New text:**
  > and the DSC unit with its lines and the master cylinder, plus the brake booster if you plan DSC option B. Keep the booster's check valve (34331161300) with the S54's booster hose: it goes into your booster ([Brakes and bleeding](#brakes-and-bleeding)).
- **Why:** correction 12. Notes: Q3 booster vacuum.

### R23: README 0410__phase-10-cooling-intake-and-exhaust.md (cool): booster hose
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > The M3's brake-booster vacuum hose connects on the opposite side ([Tenza Motorsports – 5 things (2021), 07:40](https://www.youtube.com/watch?v=-TXzg2Z8d7w&t=460s)).
- **New text:**
  > Connect the S54's brake-booster hose to the M3 check valve you fitted in your booster in Phase 8. On the M3 the hose meets the booster from the other side, so shorten or re-route it to reach and clamp it with 11151726340, as Tenza and two other builds did ([Tenza Motorsports – 5 things (2021), 07:40](https://www.youtube.com/watch?v=-TXzg2Z8d7w&t=460s), [Brakes and bleeding](#brakes-and-bleeding)).
- **Why:** correction 12. Notes: Q3 booster vacuum, procedure C step 4.

### R24: README 0180__safety.md: brake pipes near welding
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - **Brakes.** Don't drive until the pedal is firm, then prove the ABS with a careful hard stop on a quiet road ([DSC, brakes and steering angle](#dsc-brakes-and-steering-angle)).
- **New text:**
  > - **Brakes.** The brake fluid stays in the system through the build (Phase 4), so keep weld heat and spatter off the brake pipes along the floor: unclip and move a pipe clear of a weld, or shield it, and keep every opened end capped (our recommendation). Don't drive until the pedal is firm, then prove the ABS with a careful hard stop on a quiet road ([DSC, brakes and steering angle](#dsc-brakes-and-steering-angle)).
- **Why:** follows from R18 (fluid kept in to protect the MK60); a safety addition, not from a source.

### R25: README 0380__phase-7-fit-the-m3-rear-axle-and-fuel-system.md (fuel): parking-brake check
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Parking brake | Rear wheels turn freely with the lever down and lock with it up | Re-adjust the shoes |
- **New text:**
  > | Parking brake | Rear wheels turn freely with the lever down; no braking at the 1st tooth; the wheels lock with the lever up | Re-adjust the shoes, then the cables ([Brakes and bleeding](#brakes-and-bleeding)) |
- **Why:** correction 18 (E46 workshop manual checks). Notes: Q3 parking brake, procedure E.

## WIRING-AND-CODING

### R26: WIRING-AND-CODING 0660__warning-lights.md (coding-body): what the brake lamp colours mean
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | ABS, DSC, brake | 1. VIN not initialized (5EF1, 5E1F) until the cluster carries your VIN. 2. Wheel-speed sensors: an MK20 donor's don't fit. 3. Steering angle not calibrated. 4. An M3 MK60 that won't accept the Touring. 5. The yellow brake lamp: the brake test-contact wire still on pin 28 |
- **New text:**
  > | ABS, DSC, brake | 1. VIN not initialized (5EF1, 5E1F) until the cluster carries your VIN. 2. Wheel-speed faults (5D90–5DC5): see [Wheel-speed and pad-wear sensors](#wheel-speed-and-pad-wear-sensors); an MK20 donor's sensors don't fit. 3. Steering angle not calibrated. 4. An M3 MK60 that won't accept the Touring. 5. The yellow brake lamp: the brake test-contact wire still on pin 28. The red brake lamp means low fluid or the parking brake on, not a DSC fault ([BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf)) |
- **Why:** corrections 15–16. Notes: Q4 ST056 lamps.

### R27: WIRING-AND-CODING 0520__session-5-dsc-coding-and-vin.md (coding-power): when the INPA bleed is needed
- **Change:** insert after (append one sentence to the paragraph's first sentence)
- **Find (exact current text, for replace, delete or insert after):**
  > **Bleeding with INPA.** INPA → E46 → Chassis → DSC MK60 → Activate (F6) → Control hydraulic (F1) → F2 for front left and rear left, F3 for front right and rear right.
- **New text:**
  > BMW asks for the routine only after work on the master cylinder, the DSC unit or the pipes between them, or if the unit ran dry; caliper and hose work gets a conventional bleed, with a pressure bleeder at no more than 2 bar (29 psi) ([BMW TIS 34 00 050](https://xoutpost.com/attachments/x5-e53-forum/83406-low-speed-braking-34-00-050-bleeding-brake-system-dsc.pdf)).
- **Why:** correction 10 and Takeaway 7. Notes: Q3 bleeding.

### R28: README 0420__phase-11-wiring-immobilizer-and-coding.md (coding-power): when the INPA bleed applies
- **Status:** already applied by coding-power (step 13 now names the master cylinder and the pipes between it and the DSC unit). Nothing to do.

### R29: JOB-CARDS 0250__card-11b-power-up-and-coding.md (coding-power): when the INPA bleed applies
- **Status:** already applied by coding-power. Nothing to do.

## JOB-CARDS

### R30: JOB-CARDS 0110__card-4-strip-your-touring.md: keep the brake fluid in
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Battery disconnected; oil, coolant, power-steering fluid and brake fluid drained</span>
- **New text:**
  > - [ ] <span>Battery disconnected; oil, coolant and power-steering fluid drained. Brake fluid left in: each opened pipe capped, reservoir full, pedal held down ([why](README.md#phase-4-strip-your-touring))</span>
- **Why:** conflict C4; correction 11. Notes: Q3 bleeding, procedure A step 1.

### R31: JOB-CARDS 0260__card-12a-front-end-and-oil-prime.md: power-steering fluid
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Power steering | **Not found.** Read the cap on the donor's M3 reservoir (ATF or CHF 11S) and don't mix the two | Not found |
- **New text:**
  > | Power steering | ATF (Dexron III type), not CHF 11S; don't mix them. Fill before the first start | **Capacity not found;** fill to about 25 mm below the reservoir's edge, then bleed ([how](README.md#brakes-and-bleeding)) |
- **Why:** correction 8. Notes: Q2 fluid.

### R32: JOB-CARDS 0220__card-10a-cooling-and-intake.md (cool): booster hose and the pump-end hollow bolt
- **Change:** replace one task line, add one table row
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Brake-booster vacuum hose: on the M3 it connects on the opposite side</span>
- **New text:**
  > - [ ] <span>S54 booster hose to the M3 check valve in your booster, shortened or re-routed to reach; clamp 11151726340 ([how](README.md#brakes-and-bleeding))</span>
- **Insert after:**
  > | Fan clutch to water pump | 40 Nm (30 ft-lb) | Left-hand thread: loosen it clockwise |
- **New text:**
  > | Power-steering hollow bolt at the pump, M16 | 40 Nm (30 ft-lb) | New A16×22 rings |
- **Why:** correction 12; Flow p.8. Notes: Q3 booster vacuum, Q2 torques.

### R33: JOB-CARDS 0160__card-7c-rear-axle-at-ride-height.md (susp): parking-brake set-up
- **Change:** replace two task lines and one Done-when row
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] <span>Shoes adjusted before the cable: up on the left, down on the right to lock, back 10 clicks ([how](README.md#brakes-and-bleeding))</span>
- **New text:**
  > - [ ] <span>Cable nuts slackened; shoes adjusted before the cable: up on the left, down on the right to lock, back 10 notches ([how](README.md#brakes-and-bleeding))</span>
- **Find:**
  > - [ ] <span>Cable slack taken up at the lever</span>
- **New text:**
  > - [ ] <span>Cables set at the 4th tooth, with the wheels still just turning by hand</span>
- **Find:**
  > | Parking brake | Rear wheels turn freely with the lever down and lock with it up | |
- **New text:**
  > | Parking brake | Released: both wheels free. 1st tooth: no braking. Lever up: wheels locked. Lamp off when released and on at the 2nd tooth (check at power-up) | |
- **Why:** correction 18 (E46 workshop manual: 10 notches, cable at 4 teeth, lamp and tooth checks). Notes: Q3 parking brake, procedure E.

### R34: JOB-CARDS 0280__card-12c-shakedown.md: ABS light, read the fault
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > An ABS light, or wheel speeds that disagree: check the sensor plugs before you go further.
- **New text:**
  > An ABS light, or wheel speeds that disagree: read the DSC fault memory before you go further. 5D90–5DC5 are the wheel-speed faults; the last digit points to wiring, seating, the pulse wheel or tire size ([manual](WIRING-AND-CODING.md#wheel-speed-and-pad-wear-sensors)).
- **Why:** correction 15. Notes: Q4 fault list.

### R35: JOB-CARDS 0090__card-3e-bench-work-axles.md: rear carrier screws are single-use
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Rear caliper carrier, M10 | 65 Nm (48 ft-lb) | Micro-encapsulated screws |
- **New text:**
  > | Rear caliper carrier, M10 | 65 Nm (48 ft-lb) | New micro-encapsulated screws 34203414763 |
- **Why:** notes, Guide-ready torque table (Flow p.24, Department 69: new screws).

### R36: JOB-CARDS 0030__card-2a-strip-the-donor.md: keep the booster check valve
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > DSC unit, its lines and the master cylinder (booster too for option B) |
- **New text:**
  > DSC unit, its lines and the master cylinder (booster too for option B); the booster's check valve 34331161300 with the S54's booster hose |
- **Why:** correction 12. Notes: Q3 booster vacuum.

## WORKSHEETS

### R37: WORKSHEETS 0260__phase-12-at-ride-height-and-the-oil-pressure-switch.md: only the clamp nuts wait
- **Change:** replace the intro line, delete one row
- **Find (exact current text, for replace, delete or insert after):**
  > Torque the front rubber-bushed joints with the car's weight on its wheels, before the alignment.
- **New text:**
  > Torque the front anti-roll-bar clamp nuts with the car's weight on its wheels, before the alignment. Everything else at the front was torqued on stands in Phase 8.
- **Find (delete):**
  > | Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts; at ride height | | |
- **Find (replace):**
  > | Front anti-roll bar bracket nuts, M8 | 21 Nm (15 ft-lb) | At ride height | | |
- **New text:**
  > | Front anti-roll bar bracket nuts, M8 | 21 Nm (15 ft-lb) | With the car's weight on its wheels | | |
- **Why:** corrections 1–3; the bracket-bolt row is now in my Phase 8 worksheet. Notes: Q1 torques.

### R38: WORKSHEETS 0270__fluids-log.md: brake fluid, power-steering fluid, Phase 4
- **Change:** replace three places
- **Find (exact current text, for replace, delete or insert after):**
  > | Brakes, fill and bleed (Phase 8) | **Not found.** Check the reservoir cap and TIS | Allow about 1.5 L (1.6 US qt) for filling and bleeding | | |
- **New text:**
  > | Brakes, fill and bleed (Phase 8) | DOT 4 low-viscosity (BMW 81220142156); bleeder at no more than 2 bar (29 psi) | Allow about 1.5 L (1.6 US qt) for filling and bleeding | | |
- **Find:**
  > | Power steering (Phase 12) | **Not found.** Read the cap on the donor's M3 reservoir (ATF or CHF 11S) and don't mix the two | Not found | | |
- **New text:**
  > | Power steering (Phase 12) | ATF (Dexron III type), not CHF 11S; don't mix them | **Capacity not found;** fill to the mark on the lid | | |
- **Find:**
  > - [ ] Your Touring drained (Phase 4): oil, coolant, power steering, brakes, both halves of the tank
- **New text:**
  > - [ ] Your Touring drained (Phase 4): oil, coolant, power steering, both halves of the tank. Brake fluid left in, pipe ends capped and the reservoir full
- **Why:** corrections 8, 9 and 11; conflict C4.

### R39: WORKSHEETS 0210__phase-3-on-the-bench.md: power-steering pump bolts
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Crank pulley bolts; power-steering pump bolts | 23 Nm (17 ft-lb) | One video only | | |
- **New text:**
  > | Crank pulley bolts | 23 Nm (17 ft-lb) | One video only | | |
  > | Power-steering pump, only if it came off: mounting bolts M8×80; pulley bolts M8×14 | Mounting bolts 21 Nm (15 ft-lb); pulley bolts 27 Nm (20 ft-lb) | The M3 compilation's figures | | |
- **Why:** correction 7. Notes: Q2 torques (Flow p.11).

### R40: WORKSHEETS 0450__alignment.md (susp): the full-lock reading
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | Steering angle after calibration | INPA reads 0° with the wheel straight | — | |
- **New text:**
  > | Steering angle at full lock, each way | About 540° either side of zero (3.0 turns lock to lock; our arithmetic) | — | |
- **Why:** notes Q5, suggested pass values (the clamp-nut wording is already fixed by susp).

### R41: WORKSHEETS 0510__inspection-day.md: the brake run
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > - [ ] Horn, wipers and washers; brakes, parking brake and tires
- **New text:**
  > - [ ] Brake run done beforehand ([how](README.md#brakes-and-bleeding)): no pull at 4–8 mph; 20 mph stop within 30 ft; parking brake holds in first at 1,200–1,300 rpm and stops from 20 mph within 80 ft; 125 lb on the pedal for 10 s with at least 20% travel left; booster drop test passes
- **Why:** correction 16; 540 CMR 4.04(4). Notes: Q3 Massachusetts, procedure G.
