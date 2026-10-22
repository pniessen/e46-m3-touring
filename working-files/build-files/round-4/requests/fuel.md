# Requests from the fuel writer

Anchors used below that the fuel writer created: `README.md#choose-the-pump-route`, `#fuel-parts-by-car`, `#filter-regulator-and-vacuum-reference`, `#lines-and-the-pipe-set`, `#filler-and-evap`, `#test-the-fuel-system` (all H4s inside README "Fuel system"), and `WORKSHEETS.md#fuel-system-tests` (new fragment `WORKSHEETS/0196__fuel-system-tests.md`). ST041 Part 2 = `https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf`; ST041 Part 3 = the same path with `Part%203`.

## Conflicts

1. **Where the M3's canister sits (floor notes).** My notes say the canister and leak-test pump sit "under the right rear cargo floor" on both cars (BMW ST041: "under the luggage compartment floor with the DM TL Pump"). The floor notes, from a WDS photo, put the M3's canister crosswise "just behind a finned differential cover". These agree on "under the cargo floor, crosswise on the M3"; I wrote only that, without "right rear" for the M3. Where the M3 holder's four M6 studs are is unconfirmed (floor notes).
2. **When the M3 canister holder goes in (floor notes).** My notes and brief: the M3 holder 16132229735 and cover 51717893604 go in only with the M3 trunk floor (options 1 and 2); with the well kept, the Touring mount stays. The floor notes add: if the Touring canister clashes with the M3 muffler in the mock-up, fit the M3 arrangement. Both say "check the canister against the muffler". If the floor writer's text recommends moving the canister without the M3 floor, make it agree with README "Fuel system" → "Filler and EVAP" (its floor table) and the Parts list "Fuel" row for the holder, or tell me and I'll align mine.
3. **Filler pot position (arches notes).** My notes infer the pot doesn't move at all (the same pot and rigid filler pipe on both bodies). The arches notes say "expect the pot to move out much less than 25–30 mm; trial-fit it". Both drop the "25–30 mm outboard" claim. My text says the pot stays where it is "(our inference)" and asks for a fit check after the graft; R6 below uses the same wording.
4. **Phase 4 step 5 (floor notes, their correction 14).** The floor notes also amend this step (where the canister sits). My R10 only inserts a sentence about the vapour separator after the ETK link; merge the two.
5. **Fuel-gauge job and curve (coding-body notes, passed on by the coordinator).** `TANK_KENNLINIE` is one value with three names (leave it as read), and an M3 (redesign) cluster's Tool32 job is `KOMBI46R.PRG` → `STATUS_AIF_TANKDATEN_LESEN`; `STATUS_TANKINHALT_LESEN` exists only in the older `KOMBI46.PRG`. Applied in my fragments. R13, R14, R24, R27, R28 and R29 carry it to other owners' sections; coding-body's own notes also correct README "Instrument cluster and mileage" and the W&C Session 4 table, so apply R14's curve sentence and R29 only if coding-body hasn't.
6. **`STAT_EKP_CFG_VERBAUT_WERT` (coding-power notes).** Their notes suggest reading it on the donor in Phase 1 and on the swapped car. I put it in W&C "Faults that look like pump faults" and the new fuel worksheet. If coding-power sends its own Phase 1 or open-question request for it, apply one of R8's last clause and theirs, not both.

---

### R1: README 0070__decide-these-before-you-spend-money.md: Fuel decision row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | **Fuel** | Your tank with a tested pump (yours or the M3's with its baffle), or the donor's tank; pump wiring unchanged or the M3 pump module | Your tank with a pump that passes the 5-bar test (yours, or the M3's with its baffle), the M3 filter-regulator and lines; pump wiring unchanged | [Fuel system](#fuel-system), [Fuel-pump control](#fuel-pump-control) |
- **New text:**
  > | **Fuel** | The donor's in-tank set in your tank, the donor's whole tank, or your own pump if it passes the 5-bar delivery test with margin; pump wiring unchanged or the M3 pump module | The donor's in-tank set (pump, baffle, jet pump and left sender) in your tank, with the M3 pipe set, lines and filter-regulator; pump wiring unchanged | [Fuel system](#choose-the-pump-route), [Fuel-pump control](#fuel-pump-control) |
- **Why:** the donor's in-tank set is now the recommended route and your own pump the fallback (notes: Takeaway 1, correction 11).

### R2: README 0030__the-recipe.md: step 4, fuel
- **Change:** replace
- **Find:**
  > The S54 runs at 5 bar through the M3 filter-regulator and the M3's high-pressure lines. Keep your tank with a pump that passes the 5-bar test: your own, or the donor's M3 pump and baffle, which owners have fitted to the sedan tank, the same part as yours ([e46fanatics](https://www.e46fanatics.com/threads/will-an-m3-fuel-pump-fit-a-non-m-is-there-any-point-in-doing-this.903381/page-2)).
- **New text:**
  > The S54 runs at 5 bar through the M3 filter-regulator, the M3 lines and the short M3 pipe set that joins them to the pump. Move the donor's whole in-tank set into your tank: pump, baffle, jet pump and left sender, BMW's own combination, which owners have fitted to non-M tanks, the same part as yours ([e46fanatics](https://www.e46fanatics.com/threads/will-an-m3-fuel-pump-fit-a-non-m-is-there-any-point-in-doing-this.903381/page-2)). Keeping your own pump is the fallback, and it needs an adapter nobody has documented.
- **Why:** notes Takeaway 1 and correction 11. The rest of step 4 ("Or fit the donor's whole tank…") stays.

### R3: README 0110__choose-the-donor.md: "Fuel pressure" row of the test-while-it-runs table
- **Change:** replace
- **Find:**
  > | Fuel pressure | Gauge on the feed, pump run through a relay bypass, BMW's method ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)) | 5.0 ± 0.2 bar, still above 4.5 bar after 20 minutes ([Bentley, quoted on e46fanatics](https://www.e46fanatics.com/threads/fuel-pressure-info.1116777/)) |
- **New text:**
  > | Fuel pressure | Gauge on the threaded test fitting at the regulator, beside the filter under the left front floor (filter cover off); pump run through a bypass at its module's socket, terminals 30 and 87b, BMW's method ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)) | 5.0 ± 0.2 bar, and 4.5 bar or more after 20 minutes ([Bentley, quoted on e46fanatics](https://www.e46fanatics.com/threads/fuel-pressure-info.1116777/)). It proves the pump, regulator and check valve you'll move |
- **Why:** BMW's S54 test point is "a threaded fitting… at the fuel pressure regulator" (ST041 Part 2, p.46); the M3 rail has no port (notes: correction 9, procedure step 3).

### R4: README 0150__tools-and-test-equipment.md: fuel test kit
- **Change:** replace
- **Find:**
  > a fuel-pressure gauge with an adapter and a relay bypass jumper,
- **New text:**
  > a fuel-pressure gauge with an adapter for BMW's threaded test fitting (BMW names adapter 13 5 220 for the S54 regulator's fitting and for later non-M rails; [BMW ST041 Part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf), [BMW ST055](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics/04_Fuel%20Management.pdf)), a relay-bypass switch with a 15 A inline fuse, a graduated container of 2 L or more and a quick-connect cap rated for 5 bar for the fuel tests ([Test the fuel system](#test-the-fuel-system)),
- **Why:** the new Phase 7 test procedure needs these (notes: section 2, test points table).

### R5: README 0180__safety.md: Fuel bullet
- **Change:** replace
- **Find:**
  > - **Fuel.** Drain and remove the tank, filler neck and EVAP parts before you weld or grind anywhere near the rear of the car, and cap every line. Store fuel in approved cans away from the work.
- **New text:**
  > - **Fuel.** Drain and remove the tank, filler neck and EVAP parts, including the vapour separator in the right rear wheel well, before you weld or grind anywhere near the rear of the car, and cap every line. Store fuel in approved cans away from the work. When you run the pump for a test, work outdoors or with the doors open, away from flames, sparks, heaters and grinding, with an extinguisher at hand, eye protection and fuel-resistant gloves. Relieve the pressure before you open a joint, since "residual fuel pressure may be present" ([BMW ST041 Part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)), and never run the pump dry or with a line open ([Test the fuel system](#test-the-fuel-system)).
- **Why:** the brief asks for fuel-vapour and fire safety with the new pump bypass test; the separator sits inside the arch graft (ST041 Part 3, p.63).

### R6: README 0270__body.md: filler flap row
- **Change:** replace
- **Find:**
  > | M3 fuel filler flap 51172695524 and surround | Donor M3 | Shaped to the M3 quarter; graft it with the right-side arch. The hinge differs by donor body (coupe 51172695527, convertible 51178151955) ([ETK](https://bmwfans.info/parts-catalog/51172695524/)). With the flap moved outboard, check that your filler neck still reaches it and seals |
- **New text:**
  > | M3 fuel filler flap 51172695524 and surround | Donor M3 | Shaped to the M3 quarter; graft it with the right-side arch. Only the flap changes: the filler pot 51718208646, filler pipe 16117177490, pipe seal 16116755071 and cap pin 16111184156 are your Touring's own parts, so the pot stays where it is (our inference from the shared parts) ([ETK: Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/bodywork/side_panel_tail_trim/), [ETK: M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/side_panel_tail_trim/)). Take a coupe donor's hinge (51172695527) with its surround; a convertible donor's hinge (51178151955) is your Touring's part. The flap actuator (67116988090 to 03/2003, 67116987637 from 03/2003) stays with your car. After the graft, check that the pot seats in the M3 opening and the flap closes flush and locks ([Filler and EVAP](#filler-and-evap)) |
- **Why:** ETK lists the same pot, filler pipe, seal and cap pin for the US 325i Touring and the US M3; "the flap moved outboard… filler neck still reaches" is wrong (notes: Takeaway 5, corrections 4–6).

### R7: README 0290__consumables-and-single-use-parts.md: fuel row
- **Change:** replace
- **Find:**
  > | Fuel: regulator O-rings 13531720251 and 13531720252 and regulator lock ring 13531736234; pump lock ring and seal; hose clamps | Buy new | Regulator parts per the M3's filter-regulator diagram ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_preparation_system/fuel_filter_pressure_regulator/)).
- **New text:**
  > | Fuel: regulator O-rings 13531720251 and 13531720252, regulator lock ring 13531736234 and housing copper ring 07119963129; pump-flange seals 16111184084 (×2) and O-ring 16141183543; the S54 feed pipe's O-ring 13641730767 at the rail; hose clamps, including L12-15 07129952104 for the pipe set's return hose and L42-48 07129952119 (×2) for the filler hose | Buy new | Regulator parts per the M3's filter-regulator diagram ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_preparation_system/fuel_filter_pressure_regulator/)); BMW replaces fuel-system sealing rings "with new COPPER rings only" ([BMW ST055](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics/04_Fuel%20Management.pdf)). Pump seals per the M3's pump diagram ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/)).
- **Why:** single-use parts for moving the in-tank set and fitting the M3 regulator housing (notes: parts table; correction 3). The rest of the row's notes (M346 links) stays.

### R8: README 0320__phase-1-buy-and-inspect-the-donor.md: Fuel pressure bullet
- **Change:** replace
- **Find:**
  >    - **Fuel pressure:** 5.0 ± 0.2 bar (72.5 ± 2.9 psi) ([Bentley, quoted on e46fanatics](https://www.e46fanatics.com/threads/fuel-pressure-info.1116777/)).
- **New text:**
  >    - **Fuel pressure,** at the threaded test fitting on the regulator beside the filter, with the pump on a bypass: 5.0 ± 0.2 bar (72.5 ± 2.9 psi), and 4.5 bar (65 psi) or more 20 minutes later ([BMW ST041, part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf), [Bentley, quoted on e46fanatics](https://www.e46fanatics.com/threads/fuel-pressure-info.1116777/)). If you want the untested pump-control lead, also note Tool32's `STAT_EKP_CFG_VERBAUT_WERT` ([manual](WIRING-AND-CODING.md#faults-that-look-like-pump-faults)).
- **Why:** test point per ST041 (correction 9); the EKP_CFG read on the donor is the comparison the lead needs (see Conflict 6).

### R9: README 0330__phase-2-strip-the-donor.md: Underside bullet
- **Change:** replace
- **Find:**
  >    - **Underside:** the fuel filter-regulator with its vacuum hoses, and the M3 fuel lines (16122229409, 16122229410, 16122229411, [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pipe_and_mounting_parts/));
- **New text:**
  >    - **Underside:** label every fuel-line end (feed, return, purge) and photograph the clip positions first. Take the fuel filter-regulator with its vacuum-hose set and metal sleeve and the filter cover's sealing element (13327830949); the M3 fuel lines (16122229409, 16122229410, 16122229411) with their tubing supports (16122282049, 16131177494); the fuel pipes set (16112283288); and the front purge line (16132229652) ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pipe_and_mounting_parts/)). From the tank, take the in-tank set (delivery unit 16142229684, left sender 16142229683, jet pump 16142282208 and baffle 16112229656), or the whole tank with every hose off before you lower it ([Fuel system](#choose-the-pump-route)). For an M3 trunk floor, also take the canister holder (16132229735) with its nuts, its cover (51717893604), the vent pipes (16132283286, 16132229415) and the rear purge line (16132229417);
- **Why:** these parts were missing from the strip list (notes: procedure step 4; corrections 3 and 8).

### R10: README 0350__phase-4-strip-your-touring.md: step 5, vapour separator
- **Change:** insert after
- **Find:**
  > a fuel expansion-tank bracket sits among the rear wheelhouse parts ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/)).
- **New text:**
  >  That bracket (41148196386) carries the liquid-vapour separator (16136752641), which sits in the right rear wheel well behind the trim, inside the arch graft ([BMW ST041 Part 3](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)). Take it out with its vent hoses, keep the bracket (or transfer it if you graft the donor's inner tub), and refit both before the tank goes back in.
- **Why:** ST041 Part 3, p.63; brief item 6 (see Conflict 4).

### R11: README 0430__phase-12-front-end-first-start-and-shakedown.md: where the fuel gauge goes
- **Change:** replace
- **Find:**
  > 4. Fit the fuel-pressure gauge at the fuel-pressure fitting that TIS 13 31 shows ([BMW ST041, part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)).
- **New text:**
  > 4. Fit the fuel-pressure gauge at the S54's test point, the threaded fitting on the regulator housing under the left front floor (filter cover off; BMW adapter 13 5 220), and tie it where you can read it. The rail has no port ([BMW ST041, part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf), [Test the fuel system](#test-the-fuel-system)).
- **Why:** ST041 Part 2, p.46; TIS 13 31's text wasn't read (correction 9).

### R12: README 0430__phase-12-front-end-first-start-and-shakedown.md: hot-idle fuel check
- **Change:** replace
- **Find:**
  >    - fuel pressure below 5 bar with the vacuum hose connected; BMW's diagram shows 3.8 bar with part-throttle vacuum ([BMW ST041, part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf));
- **New text:**
  >    - fuel pressure below 5 bar with the vacuum hose connected; BMW's diagram shows 3.8 bar with part-throttle vacuum ([BMW ST041, part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)). Pull the hose: the pressure returns to 5.0 ± 0.2 bar, and the hose is dry inside; fuel in it means a leaking regulator diaphragm (our check);
- **Why:** test T7 in the notes' procedure (step 23).

### R13: README 0430__phase-12-front-end-first-start-and-shakedown.md: shakedown step 4, fuel gauge
- **Change:** replace
- **Find:**
  > 4. **Fuel gauge:** starting near empty, add a measured amount and check that the gauge, the range and Tool32's `STATUS_TANKINHALT_LESEN` follow it. Nobody has reported an M3 cluster on the Touring's tank senders, and the leak test relies on the reading ([manual](WIRING-AND-CODING.md#fuel-gauge-and-tank-senders)).
- **New text:**
  > 4. **Fuel gauge:** starting near empty, add a measured amount and check that the gauge, the range and Tool32's `KOMBI46R.PRG` → `STATUS_AIF_TANKDATEN_LESEN` follow it (`STATUS_TANKINHALT_LESEN` belongs to the older cluster's `KOMBI46.PRG`). With the M3 delivery unit and left sender in your tank, the cluster reads BMW's own M3 sender pair in a tank of the same 16.6 US gal; with your Touring's senders, nobody has reported the reading. The reserve lamp should come on with about 8 L left, and the leak test relies on the reading ([manual](WIRING-AND-CODING.md#fuel-gauge-and-tank-senders)).
- **Why:** notes correction 14 and section 4 (capacity, 8 L reserve); coding-body notes (job name), see Conflict 5.

### R14: README 0600__instrument-cluster-and-mileage.md (coding-body): tank senders and job name
- **Change:** replace
- **Find:**
  > - Nobody has reported an M3 cluster on a Touring's tank senders. Check the gauge, the range and Tool32's `STATUS_TANKINHALT_LESEN` against a measured fill before you rely on them.
- **New text:**
  > - Move the M3 left sender with the M3 delivery unit, as the fuel plan recommends, and the cluster reads BMW's own M3 sender pair in a tank of the same 16.6 US gal; with your Touring's senders, nobody has reported the reading. Either way, check the gauge, the range and Tool32's `KOMBI46R.PRG` → `STATUS_AIF_TANKDATEN_LESEN` against a measured fill before you rely on them.
- **Why:** notes correction 14; job name per coding-body notes. The same fragment's "Fuel-gauge curve" bullet (`TANK_KENNLINIE` at `60_l_literskala`) should become "leave `TANK_KENNLINIE` as read: it's one stored value with three names"; coding-body's notes carry that correction, so use theirs if sent.

### R15: README 0630__troubleshooting.md: EVAP monitor row
- **Change:** replace
- **Find:**
  > | EVAP monitor never ready | The heater not on pin 18, the pump and valve wiring not proven, a hose or the filler cap, the fuel gauge, or the test conditions |
- **New text:**
  > | EVAP monitor never ready | The heater not on pin 18, the pump and valve wiring not proven, a hose, the vapour separator in the right rear wheel well or the filler cap after the arch work, the fuel gauge, or the test conditions |
- **Why:** the separator and its hoses are disturbed by the arch graft (notes: section 4, leak-test plumbing).

### R16: README 0680__arch-graft-step-by-step.md (arches): name the vapour separator
- **Change:** insert after
- **Find:**
  > keep the bracket, or move it to a new inner tub ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/), [Fuel system](#fuel-system)).
- **New text:**
  >  The bracket carries the liquid-vapour separator (16136752641), which sits "in the right rear wheel well behind the trim" ([BMW ST041 Part 3](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)). Take it out with its vent hoses before you cut, refit both before the tank goes back in, and let the leak test prove them ([Filler and EVAP](#filler-and-evap)).
- **Why:** brief item 6; ST041 Part 3, p.63. The arches writer already added "keep the bracket, or move it"; this names the part on it.

### R17: README 0880__fluids-and-capacities.md: fuel capacity
- **Change:** replace
- **Find:**
  > | Fuel | Premium unleaded | Your Touring's tank | BMW ST041 [technical data](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle_djvu.txt) |
- **New text:**
  > | Fuel | Premium unleaded | 63 L (16.6 US gal), the same in your Touring's tank and the M3's | BMW ST041 [technical data](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle_djvu.txt); BMW USA spec sheets, [2003 325](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437) and [2002 M3](https://www.press.bmwgroup.com/usa/article/attachment/T0022127EN_US/41385) |
- **Why:** both BMW USA sheets give 16.6 US gal; ST041 gives the M3 63 L (notes: section 4; correction 12).

### R18: README 0900__key-numbers.md: delivery row and the test point
- **Change:** replace
- **Find:**
  > | Fuel residual pressure and pump delivery | Above 4.5 bar (65 psi) after 20 minutes; at least 1.12 L (1.2 US qt) in 30 s at 12 V | Bentley, quoted on [e46fanatics](https://www.e46fanatics.com/threads/fuel-pressure-info.1116777/) |
- **New text:**
  > | S54 fuel-pressure test point | The threaded fitting on the regulator housing under the left front floor, BMW adapter 13 5 220; the rail has no port | [BMW ST041 Part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf) |
  > | Fuel residual pressure and pump delivery | Above 4.5 bar (65 psi) after 20 minutes; at least 1.12 L (1.2 US qt) in 30 s at 12 V, the floor for every E46 engine. This guide collects the delivery from the return line at the regulator, so the pump works against 5 bar, and keeps a non-M pump only at 1.3 L (1.4 US qt) or more (both our method) | Bentley, quoted on [e46fanatics](https://www.e46fanatics.com/threads/fuel-pressure-info.1116777/); [Test the fuel system](#test-the-fuel-system) |
- **Why:** test point (correction 9); our method and margin labelled (correction 10; brief item 3).

### R19: README 0920__open-questions-to-verify.md: Fuel list and the gauge item
- **Change:** replace (three items) and add (four items)
- **Find (1):**
  > - Whether the M3 rear feed line's quick-disconnect mates with the Touring pump's outlet, and whether the M3 lines route unmodified under a Touring.
- **New text (1):**
  > - Whether the M3 fuel pipes set (16112283288) fits the Touring pump's outlet, which matters only if you keep your pump, and the size of the M3 quick-connectors. The M3 lines themselves route unmodified: four Touring builds fitted them ([Fuel system](#lines-and-the-pipe-set)).
- **Find (2), delete:**
  > - Whether the M3 tank and pump fit every model year of Touring: the builds that fitted them didn't compare part numbers.
- **Why (2):** answered: ETK lists identical mounting and interface parts for Jan 2001, Feb and Mar 2003 and May 2005 Tourings and the 2003–06 M3, and builds on 2002–2004 Tourings fitted them (notes correction 15).
- **Find (3):**
  > - Where TIS 13 31 connects the fuel-pressure gauge and collects the flow sample on an S54.
- **New text (3):**
  > - Where TIS 13 31 collects the delivery sample on an S54, and at what pressure. The gauge goes on the regulator's threaded fitting (BMW ST041); this guide collects from the return line at 5 bar (our method).
  > - A flow rating (L/h at 5 bar) for either car's delivery unit, and a 5-bar delivery figure or a pressure under load from any S54 swap.
  > - Sender resistance curves for either car, and why BMW gave the M3 its own left sender and jet pump.
  > - Whether the M3 front purge line (16132229652) mates with the Touring's rear purge line (16136751175).
  > - Whether the MSS54's learned `STAT_EKP_CFG_VERBAUT_WERT` follows the pump control fitted, and whether it has anything to do with the stored fault 1 (0x01).
- **Find (4), in the electronics list:**
  > - How accurately an M3 cluster's fuel gauge reads the Touring's tank senders, and whether it shows the tailgate and rear-window warnings.
- **New text (4):**
  > - Whether an M3 cluster shows the tailgate and rear-window warnings, and how its fuel gauge reads Touring tank senders if you keep them (moot with the M3 senders).
- **Why:** notes correction 15 and gaps in sections 2–4. Item 4 is shared with coding-body (tailgate warnings); merge with theirs if they changed it.

### R20: JOB-CARDS 0020__card-1-buy-and-inspect-the-donor.md: donor fuel test line
- **Change:** replace
- **Find:**
  > - [ ] <span>Tool32 VANOS timing and leak tests, warm; fuel pressure through a relay bypass</span>
- **New text:**
  > - [ ] <span>Tool32 VANOS timing and leak tests, warm; fuel pressure at the regulator's test fitting by the filter, pump on a bypass</span>
- **Why:** the S54 test point (correction 9).

### R21: JOB-CARDS 0030__card-2a-strip-the-donor.md: Underside row
- **Change:** replace
- **Find:**
  > | Underside | Fuel filter-regulator with its vacuum hoses; fuel lines 16122229409, 16122229410, 16122229411;
- **New text:**
  > | Underside | Fuel-line ends labelled first; filter-regulator with its vacuum-hose set and cover seal 13327830949; fuel lines 16122229409, 16122229410, 16122229411 with supports 16122282049, 16131177494; pipe set 16112283288; front purge line 16132229652; in-tank set (16142229684, 16142229683, 16142282208, 16112229656) or the whole tank, hoses off first; for an M3 floor, canister holder 16132229735, cover 51717893604 and their lines;
- **Why:** strip list for the recommended fuel route (procedure step 4). The rest of the row stays.

### R22: JOB-CARDS 0110__card-4-strip-your-touring.md: separator
- **Change:** replace
- **Find:**
  > - [ ] <span>Tank and filler neck out; EVAP parts near the right-rear arch out; every line capped</span>
- **New text:**
  > - [ ] <span>Tank and filler neck out; EVAP parts near the right-rear arch out, including the vapour separator in the wheel well; every line capped</span>
- **Why:** ST041 Part 3, p.63 (brief item 6).

### R23: JOB-CARDS 0260__card-12a-front-end-and-oil-prime.md: fuel gauge position
- **Change:** replace
- **Find:**
  > - [ ] <span>Oil gauge on a tee at the oil-pressure switch port; fuel gauge at the TIS 13 31 fitting</span>
- **New text:**
  > - [ ] <span>Oil gauge on a tee at the oil-pressure switch port; fuel gauge on the regulator's test fitting under the left front floor</span>
- **Why:** correction 9.

### R24: JOB-CARDS 0250__card-11b-power-up-and-coding.md (coding-power): tank curve
- **Change:** replace
- **Find:**
  > `TANK_KENNLINIE` = `60_l_literskala`</span>
- **New text:**
  > `TANK_KENNLINIE` left as read</span>
- **Why:** it's one stored value with three names, so there's nothing to choose (coding-body notes, via the coordinator; Conflict 5).

### R25: WORKSHEETS 0110__vanos-tests.md: donor fuel-pressure line
- **Change:** replace
- **Find:**
  > **Fuel pressure,** gauge on the feed, pump run through a relay bypass as BMW's test does:
- **New text:**
  > **Fuel pressure,** gauge on the threaded test fitting at the regulator beside the filter (filter cover off), pump run through a bypass at its module's socket as BMW's test does:
- **Why:** correction 9.

### R26: WORKSHEETS 0430__first-start.md: point the fuel rows at the new record; add the hose-pulled check
- **Change:** replace, then add row
- **Find (1):**
  > | Fuel, static, pump on a relay bypass (Phase 7) | 5.0 ± 0.2 bar (72.5 ± 2.9 psi) | |
  > | Fuel, 20 minutes after switch-off | Above 4.5 bar (65 psi); no more than 0.5 bar lost | |
  > | Fuel delivery at 12 V (TIS 13 31) | At least 1.12 L in 30 s | |
  > | Fuel leaks; feed and return confirmed | None | |
- **New text (1):**
  > | Fuel system tests T1–T5 (Phase 7): [Fuel system tests](#fuel-system-tests) | All passed | |
- **Add row (2), after** `| Fuel pressure at hot idle, vacuum hose on | Below 5 bar; BMW's diagram: 3.8 bar at part-throttle vacuum | |`:
  > | Fuel pressure at hot idle, vacuum hose pulled | Back to 5.0 ± 0.2 bar; the hose dry inside (our check) | |
- **Why:** the Phase 7 record now lives in the new fragment `0196__fuel-system-tests.md` (one place to write the results, no "TIS 13 31" label); T7 from the notes' procedure.

### R27: WORKSHEETS 0410__coding-sessions-log.md (coding-power): tank curve
- **Change:** replace
- **Find:**
  > `TANK_KENNLINIE` = `60_l_literskala`.
- **New text:**
  > `TANK_KENNLINIE` left as read.
- **Why:** as R24.

### R28: WIRING-AND-CODING 0660__warning-lights.md (coding-body): fuel-gauge row
- **Change:** replace
- **Find:**
  > | Fuel gauge or range wrong | The tank curve or a sender | `STATUS_TANKINHALT_LESEN` against a measured fill ([Fuel gauge and tank senders](#fuel-gauge-and-tank-senders)) |
- **New text:**
  > | Fuel gauge or range wrong | A sender or its plug pins, or senders mixed between the two cars | `KOMBI46R.PRG` → `STATUS_AIF_TANKDATEN_LESEN` against a measured fill ([Fuel gauge and tank senders](#fuel-gauge-and-tank-senders)) |
- **Why:** the curve isn't a choice, and `STATUS_TANKINHALT_LESEN` doesn't run on the M3's cluster (Conflict 5).

### R29: WIRING-AND-CODING 0510__session-4-cluster-and-light-module.md (coding-body): tank curve row
- **Change:** replace (skip if coding-body already applied its own correction)
- **Find:**
  > | `TANK_KENNLINIE` (fuel-gauge curve) | `60_l_literskala` | A plastic tank, the Touring's or the M3's; `metalltank` only for an ex-M56 SULEV metal tank. Check against a measured fill ([Fuel gauge and tank senders](#fuel-gauge-and-tank-senders)) |
- **New text:**
  > | `TANK_KENNLINIE` (fuel-gauge curve) | As read | One stored value with three names (`60_l_literskala`, `dad_tank_diesel`, `metalltank`), so there's nothing to choose. Check the gauge against a measured fill ([Fuel gauge and tank senders](#fuel-gauge-and-tank-senders)) |
- **Why:** Conflict 5.
