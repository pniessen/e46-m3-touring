# Requests from the xi writer (digit 9)

Fragments I changed or created: README `0050__if-your-car-is-a-325xi.md` (rewritten as a summary; heading kept) and README `0519__325xi-rear-drive-or-all-wheel-drive.md` (new, after "Driveline and rear axle"). New anchors other text can link to: `#325xi-rear-drive-or-all-wheel-drive`, `#how-to-tell-an-xi`, `#rear-drive-or-all-wheel-drive-the-verdict`, `#route-1-convert-to-rear-drive`, `#route-1-swap-the-bosch-dsc-57-for-an-mk60`, `#route-2-the-oil-pan-and-why-a-shared-gasket-proves-nothing`, `#route-2-gearbox-transfer-case-and-differentials`, `#emissions-and-massachusetts-for-an-xi`, `#documented-xi-builds`.

Already done by the integrators, so no request: the Bring a Trailer sale wording ("bid to \$59,250 … reserve not met") in README 0020, 0080 (BaT row), 0120, 0750 and 0810.

## Conflicts

1. **owners.tsv lists README 0050 as `integrator`.** The coordinator assigned it to me and I rewrote it. Please don't overwrite it from another request.
2. **Type key AW33.** The coding-body gap-fill (`gapfill_coding_body.md`, gap 10) gives AW33 as the US 325i Touring's type key for 09/00–08/01, while the xi-rwd notes decode a 2001 VIN with characters 4–7 "AW33" as a 325xi Touring at bmwfans. Pre-09/2001 xi and 325i Tourings may share AW33, with `$203` marking the xi (BMW ST056 says the AWD E46s "do not have their own model identification"). So 0519 tells readers to identify an xi by the bmwfans decode and `$203`, and gives a type-key example only for cars built from 09/2001 (EN33 325i Touring; EP33 on Baca's 2004 xi, our reading of its VIN).
3. **MK60 session order for an xi.** The xi-rwd notes say "code the MK60 against a 325i Touring order". BMW's rules (coding-body gap-fill, `E46SGVT.000`) allow the M3's MK60 index only with `S54B32` and every non-M MK60 index only with `NOT (ALLRAD OR S54B32)`. 0519 therefore says: build the session order as WIRING Session 5 Option B does (donor's type key for the M3 unit) and also delete `$203`; use the 325i Touring key EN33 only for a 325i unit. This matches Session 5 as it stands.
4. **Bosch DSC 5.7 position.** The xi-awd notes' diagram data says the hydraulic unit's position "isn't stated"; the xi-rwd notes read it as the right of the engine bay (BMW ST056 pp.12–13, WDS A65 location page). 0519 says right. The figure 42 maker should draw it on the right.
5. **Headlight-levelling curves.** WIRING Session 9 says the LWR sensor curves "read `wert_01` in every trace seen"; BMW's rules (coding-body gap-fill, `E46CVT.000`) give `ALLRAD` (xi) cars `wert_02`/`wert_01`/`wert_02`/`wert_02` and M3s `wert_03`/`wert_02`/`wert_03`/`wert_03`. 0519 only tells an xi owner with xenons to check them in Session 9; the coding-body writer owns the rest.
6. **Colorado car's diffs.** Its listing says "X3 3.0 3:91" and "factory diffs were 2:94s"; ETK gives the X3 3.0i 3.64, the X3 2.5i 3.91 and a manual 325xi 3.23. 0519 says "X3 3.91 diffs" and leaves out the 2.94.
7. **Minor:** the xi-rwd notes date the xi gearbox exhaust bracket 18207502523 "to 09/2001"; the xi-awd notes list it on all manual xi cars. 0519 gives no date.

---

### R1: README 0080__documented-builds-compared.md: Baca row, AWD details and gearbox
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | 2004 325xi Touring, 5-speed manual, 114,000 mi; kept AWD (330xi oil pan, X3 diffs) | Bought separately: 76,000-mi S54; six-speed (330xi per BimmerLife, 420G per the sale listing) |
- **New text:**
  > | 2004 325xi Touring, 5-speed manual, 114,000 mi; kept AWD: a machined 330xi oil pan (the same part as the 325xi's own, 11137519432: [ETK](https://bmwfans.info/parts-catalog/11137519432/)) with an M50-family oil pump and an S52 windage tray, X3 2.5i 3.91 diffs front and rear, NV 124 transfer case, new GKN front shafts | Bought separately: 76,000-mi S54; 330xi six-speed (BimmerLife; the sale listing says "420G", but BMW made no all-wheel-drive 420G: [ETK](https://bmwfans.info/parts-catalog/23002229721/)) |
- **Why:** the "330xi pan" is the 325xi's own part, both AWD builds used an M50-family pump, and ETK lists the 420G for the M3 only (xi_keep_awd.md, corrections 1 and 7).

### R2: README 0080__documented-builds-compared.md: BaT row, DSC route
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Porsche 996 calipers |
- **New text:**
  > | Porsche 996 calipers; DSC route not stated (a 2001 donor has the MK20; our inference) |
- **Why:** the donor's year means an MK20, not an MK60; nobody says how the xi's Bosch DSC was replaced (xi_convert_rwd.md, correction 10).

### R3: README 0080__documented-builds-compared.md: JMCCRNA row, what "plugged right in" shows
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > M3 DSC module; M3 wheel-speed sensors "plugged right in"
- **New text:**
  > M3 DSC module; the M3 wheel-speed sensors' plugs mated with the xi harness ("plugged right in"), whose Bosch sensors use the same blue housings; wiring not published
- **Why:** the xi's harness is a Bosch DSC 5.7 harness with blue plugs (BMW ST056 p.17), so the case proves the housings mate, not electrical compatibility (xi_convert_rwd.md, correction 9).

### R4: README 0080__documented-builds-compared.md: one row for the Colorado / FCP Euro "M3xi" car
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > | **S54 swap, Touring body kept** | | | | | | | | | | | |
- **New text** (a new row, first in its group because it's the oldest):
  > | A BMW master technician, Colorado (US), by 11/2018; sold through Glen Shelly (03/2019) to FCP Euro's Daniel Sloan, who ran it as the "M3xi" | 2001 325xi Touring, about 278,000 mi; kept AWD: "330Xi Oil Pan w/ Custom Baffles", "M50 Oil Pump w/ Welded Nut", X3 3.91 diffs front and rear. Under FCP the pump chain ground into the pan and wrecked the bottom end: spun bearings, cracked rods and a damaged crank. Rebuilt with a re-made pan, then 1,600 "trouble-free miles" (08/2021). Front CV boots wore when it was lowered | S54 from a 2004 M3 (VANOS failure; head rebuilt, rod bearings done); 330xi six-speed with an OEM 330 clutch kit | Custom tune; EWS route not stated; harness reworked later (FCP) | ECS Tuning CSL brake kit; DSC not stated | M3 fuel pump fitted later (FCP) | Riveted flares | not stated | not stated; strut towers reinforced later (FCP) | Custom high-flow exhaust with high-flow catalytic converters ("passes Colorado emissions", seller) | Asked \$26,500 (11/2018), then \$22,800 (03/2019); FCP's car went "over budget and over time" | [Jalopnik](https://jalopnik.com/does-this-custom-s54-rocking-2001-bmw-325ix-touring-hav-1830305864), [BMWBlog (2018)](https://www.bmwblog.com/2018/11/09/want-this-s54-swapped-e46-3-series-touring/), [German Cars For Sale](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed), [FCP Euro, part 1](https://www.fcpeuro.com/blog/bmw-e46-m3xi-an-m3-powered-bmw-rally-wagon-ready-for-almost-anything), [part 2](https://www.fcpeuro.com/blog/back-on-the-road-off-the-road-bmw-e46-m3xi-part-2) |
- **Why:** FCP Euro's xi and the 2018 BMWBlog "rivet-flare" Touring are one car, listed separately in Sources and missing from the table (xi_keep_awd.md, correction 8 and section 7). 12 cells, as the table's other rows.

### R5: README 0080__documented-builds-compared.md: row for the Buffalo 325xi made rear-drive
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > the whole row that starts `| Bry5on ("Black & Tan 332iT", NAM3), California (US);`
- **New text** (a new row on the next line; oldest-first order puts it after Bry5on's 2022 start):
  > | Seller in Buffalo, New York (US); listed 04/2023 | 2004 325xi Touring, about 200,000 mi on the chassis; made rear-drive with the M3 front and rear subframes and rack | S54 from a 2003 M3 (116,000 mi); 420G with a Sachs clutch and lightweight flywheel; M3 diff (3.64 per the listing) | MSS54HP DME; EWS route not stated | Kept the xi's Bosch DSC 5.7, which the seller lists as a known flaw; Porsche 996 Brembo calipers | not stated | None stated (Touring body) | not stated | not stated | CSL headers | Listed at \$24,000 (04/2023); sold for \$22,000 on Cars & Bids (06/2023, per Engine Swap Depot). The selector-shaft seal was leaking at sale | [Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap), [Engine Swap Depot](https://engineswapdepot.com/?p=101132) |
- **Why:** the second documented xi-to-rear-drive conversion, and one of the three that show the rear-drive front subframe going into an xi (xi_convert_rwd.md, correction 11).

### R6: README 0810__enthusiast-builds-and-sales.md: merge the duplicate car, add the Buffalo xi
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > - All-wheel-drive S54 Touring: [Built for Backroads listing, \$65k](https://www.builtforbackroads.com/listing/2004-bmw-325xit-touring-awd-s54-swap), [BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/)
  > - [FCP Euro's S54 xi Touring](https://www.fcpeuro.com/blog/back-on-the-road-off-the-road-bmw-e46-m3xi-part-2), [BMWBlog: a rivet-flare S54 Touring (2018)](https://www.bmwblog.com/2018/11/09/want-this-s54-swapped-e46-3-series-touring/)
- **New text:**
  > - All-wheel-drive S54 325xi Tourings: Baca's ([Built for Backroads listing, \$65k](https://www.builtforbackroads.com/listing/2004-bmw-325xit-touring-awd-s54-swap), [BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/)); and the Colorado car, later FCP Euro's "M3xi", which is also the "rivet-flare" Touring BMWBlog showed in 2018 ([Jalopnik (2018)](https://jalopnik.com/does-this-custom-s54-rocking-2001-bmw-325ix-touring-hav-1830305864), [BMWBlog (2018)](https://www.bmwblog.com/2018/11/09/want-this-s54-swapped-e46-3-series-touring/), [German Cars For Sale (2019)](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed), [FCP Euro, part 1](https://www.fcpeuro.com/blog/bmw-e46-m3xi-an-m3-powered-bmw-rally-wagon-ready-for-almost-anything), [part 2](https://www.fcpeuro.com/blog/back-on-the-road-off-the-road-bmw-e46-m3xi-part-2))
  > - A 2004 325xi Touring made rear-drive, from Buffalo: [Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap), [Engine Swap Depot](https://engineswapdepot.com/?p=101132)
- **Why:** one car was listed as two (xi_keep_awd.md, correction 8); the Buffalo car is a new documented build (xi_convert_rwd.md, correction 11).

### R7: README 0790__factory-documentation.md: the BMW documents the xi subchapter uses
- **Change:** replace (two places in the "BMW training" line)
- **Find 1 (exact current text):**
  > and [DSC](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/6%20DSC%202010-30-00.pdf);
- **New text 1:**
  > and [DSC](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/6%20DSC%202010-30-00.pdf), plus the [E46 all-wheel-drive system](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf) and [Bosch DSC III 5.7 (text)](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/8%20dsc%20205_djvu.txt);
- **Find 2 (exact current text):**
  > ST051 [EWS](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf).
- **New text 2:**
  > ST051 [EWS](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf); ST034 [E46 models (text)](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/1%20models_djvu.txt); ST045 [E85 driveline](https://archive.org/download/BMWTechnicalTrainingDocuments/ST045%20Z4%20Complete%20Vehicle/05%20E85%20Driveline.pdf); ST601 [E85 M Roadster (text)](https://archive.org/download/BMWTechnicalTrainingDocuments/ST601%20E85%20LCI%20and%20M%20Roadster/E85%20M%20Roadster_djvu.txt); ST406 [vehicle coding information](https://archive.org/download/BMWTechnicalTrainingDocuments/ST406%20Coding%20%26%20Programming/06%20Vehicle%20Coding%20Information.pdf).
- **Why:** 0519 cites these BMW documents; Sources doesn't list them yet (both notes' headers).

### R8: README 0920__open-questions-to-verify.md: a 325xi group
- **Change:** insert before (that is, replace the group heading with the new group plus the heading)
- **Find (exact current text):**
  > **Legal and paperwork:**
- **New text:**
  > **If your car is a 325xi:**
  >
  > - Whether a rear-drive front subframe bolts to an xi's own front frame rails, with all four M12 collar-screw threads and the arm-bracket M10 threads present. Three cars imply it; nobody measured it.
  > - Whether the M3 anti-roll bar's bushing brackets seat on the xi's body brackets (41117161089/032), and whether the xi's strut-tower tops sit at a 325i's height.
  > - Where the M3 gearbox crossmember's four M8 threads would fall on the xi tunnel, and where JMCCRNA's exhaust clashed with its bracket.
  > - The Bosch DSC 5.7's full 42-pin pin table, and the MK60's pins for the brake-light switch, ABS lamp, diagnosis line and wheel-speed outputs.
  > - Whether NCS codes an MK60 from a session order built from an xi's (with `$203` deleted and a rear-drive type key), and the US 325xi Touring's type keys by build date.
  > - Whether the xi's fuel-filter cover (13327500083) clears the M3 filter-regulator.
  > - Keeping all-wheel drive: the xi pan's inside dimensions and how the two builders reworked theirs; the S54's oil pressure on an M50-family pump; the clearance between the S54's headers and the right front shaft; whether the xi's left engine bracket fits the S54; whether the MSS54 and the DSC 5.7 talk cleanly on CAN; how to wire the MSS54's clutch chain with the 330xi gearbox, which has no gear switch; torque ratings for the NV 124, the GS6X37BZ and the diffs behind an S54; and BMW's tolerance, if any, for mismatched front and rear diff ratios.
  > - MassDEP's view of a change from all-wheel to rear-wheel drive under 310 CMR 60.02(12)(d), and what a 2001–05 xi's VECI label prints.
  >
  > **Legal and paperwork:**
- **Why:** the gaps in both xi notes (xi_convert_rwd.md sections 1, 3–5; xi_keep_awd.md sections 1–5).

### R9: README 0120__budget.md: the xi deltas
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > and keep the M54's A/C compressor until the A/C is charged ([Air conditioning](#air-conditioning)).
- **New text** (a new paragraph after that one):
  > **If your car is a 325xi,** converting it to rear drive adds about \$0–\$1,500 in parts with a donor built from 09/2002, or \$1,000–\$3,000 with an earlier one, net of selling the xi's drivetrain and DSC (our estimate). No source costs keeping all-wheel drive. Both routes are in [325xi: rear drive or all-wheel drive](#325xi-rear-drive-or-all-wheel-drive).
- **Why:** xi_convert_rwd.md section 7 and correction 5.

### R10: README 0130__time.md: the xi deltas
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Real builds:
- **New text:**
  > **If your car is a 325xi,** converting it to rear drive adds 4–8 weekends (our estimate): the front-end trial fit and transplant 1–2, a gearbox-crossmember adapter 1–2, anti-roll-bar brackets 0–1, the DSC hardware and pipes 1–2, the DSC loom and coding 1–2 ([325xi: rear drive or all-wheel drive](#325xi-rear-drive-or-all-wheel-drive)).
  >
  > Real builds:
- **Why:** xi_convert_rwd.md section 7.

### R11: README 0310__phase-0-paperwork-and-baseline.md: decode the VIN for an xi
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  >    - **A rear-drive 325i**, not an xi. If it's an xi, read [If your car is a 325xi](#if-your-car-is-a-325xi) first.
- **New text:**
  >    - **A rear-drive 325i**, not an xi. At [bmwfans](https://bmwfans.info/vin/) an xi's VIN decodes as "325xi" (NHTSA's decoder calls it a "325i"), and its vehicle order carries option `$203`, all-wheel drive. If it's an xi, choose a route in [325xi: rear drive or all-wheel drive](#325xi-rear-drive-or-all-wheel-drive) before you buy a donor: it changes which donor you want.
- **Why:** xi_convert_rwd.md, Guide-ready "Changes against the guide's phases", Phase 0; the coordinator asked for the VIN decode with a link.

### R12: README 0730__massachusetts.md: the xi's LEV status in the engine-switch table
- **Change:** insert after, then replace one cell
- **Find (exact current text, for insert after):**
  > | 2001–02, and 2003 cars in test group "LER" | LEV | Same category |
- **New text** (a new row on the next line):
  > | A 325xi, any year 2001–05 (test group "LER", or "M54" for some 2001 cars) | LEV; for 2004–05, California LEV and federal Bin 9 | Same category in every year ([325xi](#emissions-and-massachusetts-for-an-xi)) |
- **Then replace:**
  > | Other 2003–05 cars (test groups "UL2" and "SMG") |
- **with:**
  > | Other 2003–05 325i cars (test groups "UL2" and "SMG") |
- **Why:** EPA certified every 2001–05 325xi Sport Wagon LEV, the S54's category ([EPA certification data](https://www.epa.gov/compliance-and-fuel-economy-data/annual-certification-data-vehicles-engines-and-equipment)); xi_convert_rwd.md, correction 6.

### R13: README 0730__massachusetts.md: ask MassDEP about the drive change
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Does the answer change for a ULEV or SULEV Touring?
- **New text:**
  > Does the answer change for a ULEV or SULEV Touring, or for a 325xi converted from all-wheel to rear-wheel drive?
- **Why:** no source covers a drive-layout change under 310 CMR 60.02(12)(d) (xi_convert_rwd.md, section 5 gaps).

### R14: README 0040__why-your-car-is-a-good-start.md: what keeping AWD took
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Keeping all-wheel drive behind an S54 has needed a modified 330xi oil pan and X3 differentials ([BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/)), and FCP Euro's S54 xi Touring suffered poor oil flow that it put down to the all-wheel-drive refit ([FCP Euro](https://www.fcpeuro.com/blog/back-on-the-road-off-the-road-bmw-e46-m3xi-part-2)). You skip all of that.
- **New text:**
  > Keeping all-wheel drive behind an S54 has needed the xi's own oil pan (the "330xi pan" is the same part, 11137519432) reworked around a single-stage M50-family pump, plus the 330xi six-speed and X3 differentials ([ETK](https://bmwfans.info/parts-catalog/11137519432/), [BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/)). On FCP Euro's S54 xi Touring the pump chain ground into that pan and wrecked the bottom end: "spun bearings, cracked rods, and a damaged crankshaft" ([FCP Euro, part 1](https://www.fcpeuro.com/blog/bmw-e46-m3xi-an-m3-powered-bmw-rally-wagon-ready-for-almost-anything)). Even converting an xi to rear drive adds the M3 front axle, an adapted gearbox crossmember and a complete MK60 ([325xi: rear drive or all-wheel drive](#325xi-rear-drive-or-all-wheel-drive)). You skip all of that.
- **Why:** xi_keep_awd.md, correction 1.

### R15: README 0100__check-your-own-touring-first.md: DME row for a 325xi
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > On a car built in 02 or 03/2003, or a 325xi, check rather than assume ([manual](WIRING-AND-CODING.md#which-dme-your-touring-has)).
- **New text:**
  > On a car built in 02 or 03/2003, check rather than assume; a 325xi should have an MS43 in every year, but read its label too ([manual](WIRING-AND-CODING.md#which-dme-your-touring-has)).
- **Why:** keeps this row in step with R16 (xi_convert_rwd.md, correction 7).

### R16: WIRING-AND-CODING 0090__which-dme-your-touring-has.md: the MS43 note for a 325xi
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > **A 325xi:** never assume. ETK lists the 325xi Touring with MS43 and no end date, yet with the same "from Mar '03" engine harness and secondary-air sensor as the 325i ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/browse/engine_electrical_system/programmed_dme_control_unit/), [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/browse/engine_electrical_system/engine_wiring_harness_engine_module/)). Read the label.
- **New text:**
  > **A 325xi:** expect an MS43 in every year. ETK lists only MS43 units for the 325xi Touring, the latest "from Jul '02", and only the MS43-era air-mass meter (13621432356), where the 325i also lists a later one from 03/2003 ([ETK: DME](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/engine_electrical_system/programmed_dme_control_unit/), [ETK: air-mass meter](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/fuel_preparation_system/hot_film_air_mass_meter/)). EPA certified every 2001–05 325xi Sport Wagon in LEV test groups (LER, and for some 2001 cars M54), never in the ULEV-II group (UL2) the 325i Touring joined from 2003 ([EPA certification data](https://www.epa.gov/compliance-and-fuel-economy-data/annual-certification-data-vehicles-engines-and-equipment)). The 325xi does list the "from Mar '03" engine harness ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/browse/engine_electrical_system/engine_wiring_harness_engine_module/)), so read the label to confirm.
- **Why:** xi_convert_rwd.md, correction 7 (ETK and EPA, both [read]).

### R17: README 0610__dsc-brakes-and-steering-angle.md: the xi sentence at the end
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > If your car turns out to be a 325xi, it has a Bosch DSC 5.7 instead, and Option A doesn't exist ([e46fanatics](https://www.e46fanatics.com/threads/how-to-calibrate-steering-angle-using-tool32.1282261/)).
- **New text:**
  > If your car turns out to be a 325xi, it has a Bosch DSC 5.7 instead ([e46fanatics](https://www.e46fanatics.com/threads/how-to-calibrate-steering-angle-using-tool32.1282261/)). Converted to rear drive, it needs more than Option B's unit: the whole MK60 system, with its sensors, sensor cluster, master cylinder, reservoir, pipes and an adapter loom, because the xi's front sensors don't fit a rear-drive hub and MK60 sensors don't work with the Bosch unit ([BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf)). Kept all-wheel drive, it keeps its own DSC 5.7: there, Option A is the only option. Both are in [325xi: rear drive or all-wheel drive](#325xi-rear-drive-or-all-wheel-drive).
- **Why:** xi_convert_rwd.md correction 8 and xi_keep_awd.md correction 9 (front writer's fragment).

### R18: README 0610__dsc-brakes-and-steering-angle.md: what the xi case shows about sensors
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > A 2003 xi Touring took an M3's sensors without trouble ([e46fanatics](https://www.e46fanatics.com/threads/m3-touring-project.1240087/)).
- **New text:**
  > On a 2003 xi Touring the M3 sensors' plugs mated with the xi's harness ([e46fanatics](https://www.e46fanatics.com/threads/m3-touring-project.1240087/)). The xi's Bosch sensors use the same blue housings, so that proves the plugs fit, not how the sensors read ([BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf)).
- **Why:** "without trouble" isn't in the source; the builder also fitted the M3's DSC module (xi_convert_rwd.md, correction 9; front writer's fragment).

### R19: WIRING-AND-CODING 0320__wheel-speed-and-pad-wear-sensors.md: same correction
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > A 2003 xi Touring took an M3's sensors ([e46fanatics](https://www.e46fanatics.com/threads/m3-touring-project.1240087/)).
- **New text:**
  > On a 2003 xi Touring the M3 sensors' plugs mated with the xi's harness, whose Bosch sensors use the same blue housings ([e46fanatics](https://www.e46fanatics.com/threads/m3-touring-project.1240087/), [BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf)): proof that the plugs fit, not of how the sensors read.
- **Why:** as R18 (front writer's fragment). The other mentions (README 0080 lesson, 0110, 0240, 0330, 0510) use the case only as plug evidence and can stay.

### R20: WIRING-AND-CODING 0540__session-7-steering-angle-after-the-alignment.md: the DSC 5.7 row
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > | Bosch DSC 5.7 | `DSC57.PRG` | `test_lenkwinkel`. For the 325xi and 330xi only |
- **New text** (still three cells):
  > | Bosch DSC 5.7 | `DSC57.PRG` | `TEST_LENKWINKEL`, with argument `LFD_NR`; it returns `STATUS_ABGLEICH` and `ABGL_LWS_ID`. Read the angle with `STATUS_IO_LESEN_ANALOG` → `STAT_LENKWINKEL_WERT` ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC57.md)). Only for a 325xi or 330xi that keeps all-wheel drive: an xi converted to rear drive has an MK60 and uses its job |
- **Why:** xi_keep_awd.md, correction 10; the rear-drive conversion uses the MK60 job (xi_convert_rwd.md, section 3).

### R21: WIRING-AND-CODING 0240__clutch-switch-gear-switch-and-cruise.md: the 330xi six-speed has no gear switch
- **Change:** insert after
- **Find (exact current text, for replace, delete or insert after):**
  > Its state in reverse isn't documented.
- **New text** (same paragraph, after that sentence):
  > A 325xi that keeps all-wheel drive runs the 330xi six-speed, which has no such switch: ETK lists only its reversing-light switch, 23147524811 ([ETK](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/manual_transmission/gs6x37bz_grbx_housing_and_mount_parts/)). Without it the chain stays open and cruise won't work; bridging its plug would make the DME read "in gear" whenever the pedal is up, even in neutral. Neither has been tested (our inference; [325xi](README.md#route-2-gearbox-transfer-case-and-differentials)).
- **Why:** xi_keep_awd.md, correction 11 and section 2.

### R22: README 0870__torque-values.md: NV 124 plugs (AWD route only)
- **Change:** add row (insert after)
- **Find (exact current text, for replace, delete or insert after):**
  > | 420G drain and fill plugs, M24×1.5 | 52 Nm (38 ft-lb) | | Flow p.74 |
- **New text:**
  > | NV 124 transfer-case drain and fill plugs (a 325xi kept all-wheel drive only) | 33 Nm (24 ft-lb) | Lifetime fill; see Fluids | [BMW ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf) |
- **Why:** 0519 gives this torque; the brief keeps torques in step with the Appendix (xi_keep_awd.md, section 2).

### R23: README 0880__fluids-and-capacities.md: NV 124 fill (AWD route only)
- **Change:** add row (insert after)
- **Find (exact current text, for replace, delete or insert after):**
  > the whole row that starts `| Getrag 420G gearbox |`
- **New text** (a new row on the next line):
  > | NV 124 transfer case (a 325xi kept all-wheel drive only) | BMW MTF-LT-1 (83229408942) | 0.24 L (0.25 US qt), a lifetime fill; plugs 33 Nm (24 ft-lb) | [BMW ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf) |
- **Why:** as R22. Worksheets need no change unless the owner takes Route 2.

### R24: README 0190__parts-list.md: point xi owners to their parts
- **Change:** replace
- **Find (exact current text, for replace, delete or insert after):**
  > Single-use fasteners, seals and fluids are under [Consumables and single-use parts](#consumables-and-single-use-parts).
- **New text:**
  > Single-use fasteners, seals and fluids are under [Consumables and single-use parts](#consumables-and-single-use-parts). If your car is a 325xi, its extra and different parts are in [325xi: rear drive or all-wheel drive](#325xi-rear-drive-or-all-wheel-drive).
- **Why:** the brief keeps parts in the Parts list; the xi tables live in 0519, so the list points to them.
