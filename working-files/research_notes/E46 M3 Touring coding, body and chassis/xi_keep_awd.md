# Keeping all-wheel drive: an S54 in a US 325xi Touring (2001–05), with a 2003–06 US M3 donor

Research date: 22 October 2026. Researcher: `xi-awd`. This covers the **keep-AWD** half of the new "325xi" subchapter. A second researcher covers converting an xi to rear-wheel drive; findings that bear on that half are collected near the end.

It builds on the guide's README "If your car is a 325xi" (lines 68–79), the documented-builds rows for the Baca car (line 122) and the FCP Euro car (line 62 and Sources, line 2057), WIRING-AND-CODING.md's steering-angle table (line 1039) and clutch-chain section (lines 475–505), `coding_powertrain_chassis.md` (the `DSC57.PRG`/`test_lenkwinkel` finding) and `fuel_system_fit.md`, which this note's structure follows.

## Header: sources, blocks and how each was read

**Labels.** [read] = I fetched and read the page or PDF text this session. [snippet] = seen only in a search-result summary. "Inference:" and "Arithmetic:" mark my own reasoning. ETK pages are bmwfans.info mirrors of BMW's parts catalog, read for the US market at the model level (bmwfans shows current, superseding numbers; date splits are as ETK prints them). BMW training documents were read from the archive.org `BMWTechnicalTrainingDocuments` item, as PDF text (`pdftotext`) or archive.org's OCR text.

| Source | What it gave | How read |
|---|---|---|
| BMW ST040 "E46 All-Wheel Drive System" (initial print 10/2000) | Front diff on the left of the oil pan, tube welded into the pan for the right shaft, ratios, diff and transfer-case torque figures, NV 124 construction, chassis changes | [read], PDF text ([PDF](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf)) |
| BMW ST040 "Bosch DSC III 5.7" (same course) | CAN partners, steering-angle sensor, wheel-speed sensors, ADB, coding and workshop hints | [read], OCR text ([text](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/8%20dsc%20205_djvu.txt)) |
| BMW ST034 "E46 Models" | xi manual gearbox named "S5D-280Z" | [read], OCR text ([text](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/1%20models_djvu.txt)) |
| BMW ST041 M3 "DriveLine" and "Complete Vehicle" | S54 two-stage oil pump and pan layout; US S54 355 Nm; 420G ratios | [read], OCR text ([DriveLine](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine_djvu.txt), [Complete Vehicle](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle_djvu.txt)) |
| BMW ST045 "E85 Driveline" | Gearbox designation key; GS6-37BZ ratios; input shaft piloted in the flywheel | [read], PDF text ([PDF](https://archive.org/download/BMWTechnicalTrainingDocuments/ST045%20Z4%20Complete%20Vehicle/05%20E85%20Driveline.pdf)) |
| BMW ST601 "E85 M Roadster" | Z4 M's S54: 262 lb-ft, six-speed manual | [read], OCR text ([text](https://archive.org/download/BMWTechnicalTrainingDocuments/ST601%20E85%20LCI%20and%20M%20Roadster/E85%20M%20Roadster_djvu.txt)) |
| ETK (bmwfans.info) | About 90 group and part-usage pages: 325xi Touring, 330xi sedan, 325i Touring, M3, X3 2.5i/3.0i, Z4 M, 330xd, E36 M3 | [read]; links inline |
| SGBD docs, `DSC57.md` and `MSS54DS0.md` ([GitHub](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC57.md)) | DSC 5.7 coding, CAN status, steering-angle job; MSS54 DSC faults | [read], raw files |
| 2004 325i/325xi Sports Wagon owner's manual, printed pp. 127–128 ([p.127](https://manualsnet.com/pdf-content/0945ee845d7bf99b78315dcf/html/127.page.html), [p.128](https://manualsnet.com/pdf-content/0945ee845d7bf99b78315dcf/html/128.page.html)) | Wheel-tire rule for ABS/DSC/ADB-X; xi snow chains | [read] |
| BimmerLife, 4 Jul 2022 ([link](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/)) | Baca build | [read], fresh fetch |
| Built for Backroads listing ([link](https://www.builtforbackroads.com/listing/2004-bmw-325xit-touring-awd-s54-swap)) | Baca car at sale | [read], fresh fetch |
| FCP Euro, M3xi part 1 ([link](https://www.fcpeuro.com/blog/bmw-e46-m3xi-an-m3-powered-bmw-rally-wagon-ready-for-almost-anything)) and part 2, dated 6 Aug 2021 in page metadata ([link](https://www.fcpeuro.com/blog/back-on-the-road-off-the-road-bmw-e46-m3xi-part-2)) | The Colorado car after purchase: failure, cause, fix | [read], fresh fetch |
| German Cars For Sale Blog, 19 Mar 2019, reprinting the Glen Shelly listing ([link](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed)) | The Colorado car's full build list | [read] |
| Jalopnik, 9 Nov 2018 ([link](https://jalopnik.com/does-this-custom-s54-rocking-2001-bmw-325ix-touring-hav-1830305864)); BMWBlog, 9 Nov 2018 ([link](https://www.bmwblog.com/2018/11/09/want-this-s54-swapped-e46-3-series-touring/)); The Chicago Garage, 12 Mar 2019 ([link](https://www.thechicagogarage.com/threads/2001-bmw-m3-s54-swapped-325xi-sport-wagon-6-speed-awd.168023/)) | Same Colorado car, earlier listing | [read] |
| The Drive, 22 Dec 2023 ([link](https://www.thedrive.com/news/e46-m3-swapped-bmw-x3-with-a-six-speed-is-the-m-suv-you-want)) | An S54 E83 X3 (shares the xi oil pan) | [read] |
| BimmerWorld product pages ([bracket](https://www.bimmerworld.com/Driveline-Shifter/Differentials-Accessories/Genuine-BMW-Supporting-Bracket-31537500850-E46.html), [xi rack](https://www.bimmerworld.com/Suspension-Steering/Steering-Components/Steering-Rack-New-AAE-E46-325xi-330xi-3410N.html)) | Diff support bracket mounting; prices | [read] |
| Achilles Motorsports kit via Turner ([link](https://www.turnermotorsport.com/p-1150774-achilles-motorsports-upgraded-oil-pump-shaft-kit-bmw-s54s50b30b32euro-engine-swap-using-m50-pump-conversion/)) | M50-family pump on an S54 | [snippet]; page refused (403) |
| BMW Group Classic, 330xd ([link](https://www.bmwgroup-classic.com/en/models/bmw-classics/product-description-page.ad-998-1.bmw-330xd-e46.html)) | 330xd torque, 390 then 410 Nm | [snippet]; page returned nothing |

**Blocked or not reached.**
- e46fanatics.com serves a proof-of-work page (checked again today). Not bypassed. This hides the thread "S54 xi Touring swap" (1102352) that WIRING-AND-CODING.md cites, and the M3-brakes-on-a-non-M thread (913537) the README cites.
- archive.org's Wayback API first returned 429 (too many requests). Later it reported a snapshot of thread 1102352 dated 20 Aug 2025 (`web.archive.org/web/20250820032027/…`). But web.archive.org itself reset every connection from this environment (curl and WebFetch), so the thread is still unread. It had no copy of 913537.
- **What would settle it:** open the 20 Aug 2025 snapshot of 1102352 in a normal browser.
- Turner Motorsport (403, then DNS failure in WebFetch), Engine Swap Depot (403), Grassroots Motorsports (403), BMW Group Classic (empty reply). Jalopnik's short link 404s; the full URL worked.
- GitHub's API isn't enabled for this session; raw.githubusercontent.com worked.
- TIS, Bentley and RealOEM weren't tried. There's no S54 oil-pressure specification, no NV 124 or diff fill volume, and no torque table here.

**Web searches used: 17 of 35.** Downloads are in `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/gapfill-dl/xi-awd/`.

---

## Takeaway: what an xi owner who keeps AWD must do

**Verdict: possible, documented twice, and the hardest version of this build.** One of the two documented cars destroyed its S54 through the oil system that keeping AWD forces on you. Keep AWD only if all-wheel drive is the point of the car. Otherwise, converting to rear drive follows a better-trodden path; that's the other researcher's half.

What keeping AWD takes, in order of risk:

1. **An oil system BMW never made.**
   - BMW's xi pan has the front diff bolted to its left side and a tube welded through it for the right shaft ([ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf)).
   - The S54's pump is two-stage. Its scavenge stage draws from the **front** of the pan, which is where the axle tube sits in an xi pan ([ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine_djvu.txt)).
   - Both documented cars used a 330xi pan with a single-stage M50-family pump. ETK lists the "330xi pan" as the same part (11137519432) as your own 325xi pan.
   - On the Colorado car (later FCP Euro's), "the oil pump chain was digging into the pan, and the pickup tube didn't have enough clearance". The result was spun bearings, cracked rods and a damaged crank ([FCP part 1](https://www.fcpeuro.com/blog/bmw-e46-m3xi-an-m3-powered-bmw-rally-wagon-ready-for-almost-anything)).
   - The fix was a re-fabricated pan with baffles ([FCP part 2](https://www.fcpeuro.com/blog/back-on-the-road-off-the-road-bmw-e46-m3xi-part-2)).
   - **Budget for pan machining or fabrication. Prove the clearances with clay against your own M54's figures in the same pan, and prove oil pressure against the donor's own readings before you drive.**
2. **The 330xi six-speed, not your five-speed.**
   - The 325xi's ZF five-speed is "S5D 320Z" in ETK and "S5D-280Z" in BMW's training text. In BMW's older naming that number is torque (Nm), and both values sit below the US S54's 355 Nm.
   - By the builders' own accounts, both builds used the 330xi's six-speed: the ZF GS6X37BZ, built from 03/2003 ([ETK](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/manual_transmission/manual_transmission_gs6x37bz_dz_4_wheel/)). One sale listing says "420G" instead (section 2).
   - BMW itself ran the S54 through the same H-gearbox family in the Z4 M, on the M3's flywheel with a Z4 M clutch ([ETK](https://bmwfans.info/parts-catalog/E85/USA/Z4_M3.2-S54/L-N/browse/manual_transmission/manual_transmission_gs6_37bz_dz/)).
   - Take the six-speed with its 03/2003-on NV 124, adapter shafts, 723 mm front prop shaft and shift parts.
   - The 420G can't be used: ETK has no four-wheel-drive version of it.
3. **A matched pair of diffs.** The NV 124 is an open planetary with "output speeds to the front and rear axle … the same (1:1)" (ST040). Both builds fitted X3 2.5i 3.91s, which give gearing about 11% shorter than the M3's.
   - Arithmetic: the 325xi/330xi **automatic** pair, 3.46/3.46, would put overall gearing within 2% of an M3's, using E46 parts throughout.
4. **Keep the xi front axle, rack and DSC 5.7.**
   - None of the M3 front axle can be used except, with adaptation, the brakes.
   - The DSC 5.7 is the only unit that reads the xi's Bosch wheel-speed sensors and runs four-wheel ADB-X (ST040).
   - Nobody has published whether an MSS54 and a DSC 5.7 talk cleanly on CAN, so it becomes a test, with pass values below.
5. **Torque margins are thin.**
   - BMW's sheet gives the NV 124 "Maximum Torque: 300Nm". Yet BMW also fitted the same NV 124 part numbers to the Euro 330xd, a 390–410 Nm diesel ([ETK](https://bmwfans.info/parts-catalog/27107530812/); torque [snippet]).
   - With 3.91 diffs, first-gear axle torque from an S54 exceeds BMW's 2000 Nm front and 3000 Nm rear diff figures by about 15% and 25%. That's arithmetic, and assumes BMW's figures are output torque.
   - No documented car has reported a transfer case, diff or front-shaft failure, but the mileage behind that is small: roughly 10,000 and 5,000 miles (inference).

**Difficulty and cost, frankly.** It's harder than the RWD route in every dimension except the front axle, which stays.
- **Labour:** the Baca car took 280 hours of mechanical work, plus a separate body shop, and had "over \$70k invested" ([BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/), [Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xit-touring-awd-s54-swap)). The FCP car "has gone over budget and over time", including a full bottom-end rebuild ([FCP part 2](https://www.fcpeuro.com/blog/back-on-the-road-off-the-road-bmw-e46-m3xi-part-2)).
- **Cost:** no source splits out the AWD-only cost. Expect to buy a used 330xi six-speed with its transfer case and prop shafts, a pair of diffs, a second xi pan to machine, pump parts, the Z4 M clutch, front shafts and a custom steering hose.
- **Two benefits:** you keep your own front axle and DSC, and BMW says AWD adds 100 kg (220 lb) and 17 mm of ground clearance (ST040).

---

## 1. Oil pan and pump

### Cited findings

**Part numbers** ([ETK 325xi Touring pan](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/engine/oil_pan_oil_level_indicator/), [325xi pump](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/engine/lubrication_system_oil_pump_with_drive/), [330xi pan](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/engine/oil_pan_oil_level_indicator/), [330xi pump](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/engine/lubrication_system_oil_pump_with_drive/), [M3 pan](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/oil_pan_oil_level_indicator/), [M3 pump](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/lubrication_system_oil_pump_with_drive/), [325i Touring pan](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/oil_pan_oil_level_indicator/), [325i pump](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/lubrication_system_oil_pump_with_drive/)) [read]:

| Item | 325xi and 330xi (M54) | US M3 (S54) | 325i Touring (RWD, reference) |
|---|---|---|---|
| Oil pan | 11137519432 (6.4 kg; old number 11137511600). One piece; ETK lists no upper/lower split | 11137838130 (5.7 kg), one piece plus a "cover" 11137834885 and gasket 11137834886 from 04/2003 (11137832020 / 11137832023 before). On engines built to 04/2003, ETK fits this pan "only in conjunction with" the later suction and return pipes, cover and gasket | 11131432703 (5.0 kg) |
| Pan gasket | 11131437237 (steel) | **11131437237** | 11131437237 |
| Oil pump | 11417501568, single-stage | 11417838123, two-stage (old 11417836993) | 11417501568 |
| Suction pipe (pickup) | **11417502667** | 11417834887 from 04/2003 (11411406405 before) | **11417503258** |
| Return (scavenge) pipe | none | 11417834889 from 04/2003 (11411405215 before) | none |
| Pump drive | Sprocket 11411432737, chain 11417576915 | Sprocket 11411317284, chain 11411401399, chain tensioner 11411317650 | as xi |
| Dipstick / guide tube | 11437506769 / 11437531260 (470 g) | 11437831140 / 11437832140 (260 g) | 11431436293 / 11437531258 |
| Oil-level sensor | 12617508003 | 12617508003 (13617832205 to 03/2001) | 12617508003 |

**Usage** [read, ETK usage pages]:
- **Gasket 11131437237** is listed for essentially every BMW M50, M52, M54, S50, S52 and S54 since 1997: the E46 325i, 325xi, 330xi and M3, the Z4 M, and the E36 M3 ([ETK](https://bmwfans.info/parts-catalog/11131437237/)).
- **The xi pan 11137519432** is listed for the 325xi (sedan and Touring), the 330xi, and the E83 X3 2.5i and 3.0i (M54) ([ETK](https://bmwfans.info/parts-catalog/11137519432/)). The **xi pickup 11417502667** has the same usage ([ETK](https://bmwfans.info/parts-catalog/11417502667/)).
- **The S54 pump and pickup** are shared only with the Z3 M and Z4 M ([ETK](https://bmwfans.info/parts-catalog/11417838123/), [ETK](https://bmwfans.info/parts-catalog/11417834887/)).

**How the xi pan carries the front axle.** BMW, ST040 [read]:
> "The differential for the front axle is bolted to left side of the engine oil pan. … The oil sump has been modified to accommodate the right side axle. A connecting tube is welded into the oil pan. A shaft runs inside of the connecting tube between the front differential and the axle shaft on the right side."

BMW also lists "Modified oil pan and engine mounts to provide access for the front axles" among the xi changes.
- **Diff fixings** ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/front_axle/front_diff_components_all_wheel/)) [read]: four M10×55 bolts (8.8 grade 07119900139 to 09/2003; 10.9 grade 07119905161 from 09/2003). The supporting bracket 31537500850 "May not be replaced" separately from its grooved ball bearing. Gasket sets: 31507500347 (front diff, type 174) and 31507500348 (bracket).
- **The bracket** "mounts the the right side of the oil pan and supports the right front differential output flange. There is a bearing … which is non-serviceable", \$166.73 ([BimmerWorld](https://www.bimmerworld.com/Driveline-Shifter/Differentials-Accessories/Genuine-BMW-Supporting-Bracket-31537500850-E46.html)) [read].

**The S54's pump in the pan.** BMW, ST041 [read]:
> "The S54 oil pump is two stage, supply and scavenge. The pump is driven by the crankshaft with a single row chain. … the scavenge chamber (1) draws oil from the pickup at the front of the oil pan. The oil is transferred from the pump through a small pipe to the main sump at the rear of the oil pan (2). The supply chamber (3) draws oil from the main sump through a large pipe (4)."

BMW tests S54 oil pressure at the oil-filter housing with special tool 90 88 6 114 390, which replaces the housing's cover bolt.

**What the builds did:**

| Car | Pan | Pump, pickup, windage | Outcome | Source |
|---|---|---|---|---|
| Colorado 2001 325xi Touring (built by "a BMW master tech"; Glen Shelly 2019; then FCP Euro's "M3baru") | "330Xi Oil Pan w/ Custom Baffles" | "M50 Oil Pump w/ Welded Nut"; Mishimoto oil cooler, braided lines | After purchase: "The oil pump chain was digging into the pan, and the pickup tube didn't have enough clearance to supply oil properly … spun bearings, cracked rods, and a damaged crankshaft". Mechanic Chris Rhom: "the actual oil pump gear and chain were grinding through the front of the oil pan. It filled the engine up with really fine aluminum dust. … What failed was the very last rod bearing". On the road the filter "looked clean". Fix: "cutting up the all-wheel drive oil pan to fabricate a new one with correct clearances, as well as putting in baffles"; part 1 adds "If necessary, a custom oil pickup tube will be fabricated." Then 1,600 "trouble-free miles" | [German Cars For Sale](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed), [FCP 1](https://www.fcpeuro.com/blog/bmw-e46-m3xi-an-m3-powered-bmw-rally-wagon-ready-for-almost-anything), [FCP 2](https://www.fcpeuro.com/blog/back-on-the-road-off-the-road-bmw-e46-m3xi-part-2) [read] |
| Baca 2004 325xi Touring | "A 330xi oil pan" ([BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/)); "330Xi Oil Pan (Custom Machined)" ([Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xit-touring-awd-s54-swap)) | "used in conjunction with an S52 windage tray and M50 oil pump" | No failure reported, from 2019 to the 2025 sale | [read] |
| E83 X3 with S54 (RWD-converted, "can be switched back to X-drive") | "a custom oil pump and pan" | — | Daily-driven about a year and 15,000 miles; catless exhaust (an emissions caution, not a model) | [The Drive](https://www.thedrive.com/news/e46-m3-swapped-bmw-x3-with-a-six-speed-is-the-m-suv-you-want) [read] |

**The M50-family parts.** ETK lists the US M50/M52/S52 pump 11411740154 (E36 320i/325i/325is M50, 323i/328i M52, M3 S50 and S52, Z3 M S52; old number 11411730475) ([ETK](https://bmwfans.info/parts-catalog/11411740154/)). The same family's oil deflector, the "windage tray", is 11131433060 (E36 M50/M52/S52, E34 525i M50, E39 528i, Z3 M S52) ([ETK](https://bmwfans.info/parts-catalog/11131433060/)). The S52 pump's sprocket is 11411719935; its chain, 11417576915, is the same part as the M54's ([ETK](https://bmwfans.info/parts-catalog/E36-Coupe/USA/M3_3.2-S52/L-M/browse/engine/lubrication_system_oil_pump_with_drive/)) [read].
- A vendor kit, Achilles Motorsports' "upgraded oil pump shaft kit … S54 … engine swap using M50 pump conversion", is described as "a typical conversion when retrofitting an S54 engine into a chassis such as an E30 or E34 that requires the use of a front sump oil pan" [snippet; Turner refused].

### Inferences (labelled)

- **The shared gasket proves only the flange.** It's common to every M5x/S5x six since 1997, including the RWD 325i, so it says nothing about the pump, pickup, sprocket or tube positions inside. The owner's preliminary finding is right, and that is why "clearly more changes are needed".
- **"330xi oil pan" means your own pan.** ETK gives the 325xi and 330xi one pan part number, so a 325xi owner already has the pan both builds bought. Buy a second one anyway, to machine while yours stays a spare.
- **Why the S54 pump doesn't drop in.** ETK shows the RWD and xi M54 using the same pump with different pickups (11417503258 against 11417502667), so the xi pan's sump is shaped differently. The S54's pump adds a scavenge pickup at the pan's front, where ST040 puts the axle tube, and a chain-driven sprocket with its own tensioner. Both of the S54's pickups are drawn for the M3 pan, not for an xi pan.
- **Why builders chose the M50-family pump.** It's single-stage, so there's no front scavenge pickup to fight the tube. It's a relative of the M54's (the M54 shares the S52's chain), and per the vendor snippet it bolts to the S54. Neither build says which pickup it used.
- **The single-stage pump has known failure modes.** The Colorado car's pump chain still ground the pan, so the M50 pump is not a bolt-in either. Its sprocket nut (M10×1 left-hand, 07119905857 on all three engines) is the reason for the "welded nut" and the Achilles shaft kit.
- **No oil-pressure figure exists for an S54 on an M50 pump.** The S54 revs to 8,000 rpm against the M50's 6,500 rpm.
- **The dipstick and level sensor.** With the xi pan, use the xi guide tube and dipstick, since the pan's bore sets the tube. Whether the xi tube clears the S54's intake side is unchecked. The oil-level sensor is the same part in both pans, but its warning point follows the xi pan's geometry, so check the dipstick marks with a measured fill.
- **Windage.** ETK lists no windage tray for the S54; the block's mounting parts are a covering plate and oil spray nozzles ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/engine_block_mounting_parts/)). The S52 tray Baca used is an addition, not a replacement.
- **A clean filter proves nothing.** On the FCP car, aluminium dust built up over "hundreds or even thousands of miles" and the paper filter "looked clean" as the engine failed. Use oil analysis for aluminium, not filter inspection, as the early-warning test.

### Gaps
- No published dimensions for the xi pan's tube, sump or front-wall clearance, and no account of exactly how either builder machined the pan, or which pickup it ran.
- No BMW oil-pressure specification for the S54 here (TIS not reached). The guide's ≥ 0.7 bar at hot idle is a compilation figure.
- Whether the xi dipstick tube clears the S54. *Settle by:* trial fit on the stand.
- The e46fanatics "S54 xi Touring swap" thread (1102352) may answer some of this. The live page is behind a proof-of-work check; a 20 Aug 2025 Wayback snapshot exists but was unreachable from here.

---

## 2. Gearbox and transfer case

### Cited findings

**Manual gearboxes in ETK** [read]:

| Car | Gearbox | Part number and code | Dates |
|---|---|---|---|
| 325xi (sedan, Touring) | 5-speed "S5D 320Z", 4-wheel | 23007502658 THCG; 23007527111 THCN; 23007531644 THCR | to 03/2003; 03–09/2003; from 09/2003 ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/manual_transmission/manual_transmission_s5d_z_4_wheel/)) |
| 330xi | 5-speed S5D 320Z THCG | 23007502658 | to 03/2003 |
| 330xi | **6-speed GS6X37BZ, 4-wheel** | **23007563053 THEW** | **from 03/2003** ([ETK](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/manual_transmission/manual_transmission_gs6x37bz_dz_4_wheel/)) |
| X3 3.0i (M54) | 6-speed GS6X37BZ, 4-wheel | 23007562732 THET | ([ETK](https://bmwfans.info/parts-catalog/E83/USA/X3_3.0i-M54/L-N/browse/manual_transmission/manual_transmission_gs6x37bz_dz_4_wheel/)); its transfer case is the ATC 400, with a control unit, not the NV 124 ([ETK](https://bmwfans.info/parts-catalog/E83/USA/X3_3.0i-M54/L-N/browse/transfer_box_electric_gearbox/transfer_case_atc_400/)) |
| Z4 M Roadster (S54) | 6-speed GS6-37BZ, rear-drive | 23007837983 TJEE | ([ETK](https://bmwfans.info/parts-catalog/E85/USA/Z4_M3.2-S54/L-N/browse/manual_transmission/manual_transmission_gs6_37bz_dz/)) |
| M3 | 6-speed S6S 420G | 23002229721 TBAI; ETK usage lists **only the E46 M3** (coupe, convertible) ([ETK](https://bmwfans.info/parts-catalog/23002229721/)) | — |

**BMW's training text and naming:**
- ST040 and ST034 call the xi manual "the S5D-280Z direct gear transmission. The extension housing is modified to accept the transfer case" (initial print 10/2000) [read].
- BMW's key for the newer names: in "GS6-37BZ", "37" is the **gearbox type "H"** (39 = "F", 53 = "G", 20 = "B"), "B = Petrol gear ratio", "Z = ZF". Among manual gearboxes, "X = All-wheel drive with manual gearshift" and "W = All-wheel drive with SMG". The key's automatic-gearbox example describes the same number position as "Alternatively: gearbox type/size/torque (Nm)". It also equates GS5-20BG with the E46's "S5D-250G" ([ST045](https://archive.org/download/BMWTechnicalTrainingDocuments/ST045%20Z4%20Complete%20Vehicle/05%20E85%20Driveline.pdf), pp. 3–5) [read].
- GS6-37BZ ratios: 4.350, 2.496, 1.665, 1.234, 1:1, 0.851, reverse 3.926. It's "designed by … ZF and built and supplied by ZF and Getrag". Its changes include "Input shaft mounting in dual-mass flywheel" and "Involute input shaft teeth" (ST045) [read].
- 420G ratios: 4.227, 2.528, 1.669, 1.226, 1.00, 0.828 ([ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle_djvu.txt)) [read].
- S54 torque: US M3 "355 Nm of Torque at 4900 rpm" ([ST041 DriveLine](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine_djvu.txt)). Z4 M: "maximum torque is 262 lb-ft at 4900 rpm" with "a 6-speed manual gearbox … standard" ([ST601](https://archive.org/download/BMWTechnicalTrainingDocuments/ST601%20E85%20LCI%20and%20M%20Roadster/E85%20M%20Roadster_djvu.txt)) [read].

**Transfer case NV 124** (ST040) [read]:
- Made by New Venture. "Torque Distribution: 38%: 62%. Maximum Torque: 300Nm".
- "only one speed and does not use any viscous coupler. The transmission ratio of the planetary gear set provides a fixed torque transfer of 38:62 (front:Rear). The output speeds to the front and rear axle are the same (1:1)."
- It uses gears, not the X5's chain, to fit the tunnel.
- Lifetime fill MTF-LT1 (83 22 9 408 942), 0.24 litre; drain and fill plugs 33 Nm.
- "The only repairs possible are the replacement of the three oil seals and the hydraulic mount."

**NV 124 part numbers** ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/transfer_box_electric_gearbox/transfer_case_nv_124/), [single parts](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/transfer_box_electric_gearbox/single_parts_f_transfer_case_nv_124/), [fixings](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/transfer_box_electric_gearbox/gearbox_mounting_parts/)) [read]:
- 27107509763 to 03/2003; 27107530812 from 03/2003.
- Adapter shaft 27107525789 "for vehicles with manual transmission", with O-ring 27107536962.
- Fixings to 03/2003: 2 × M10×75 23001434691 and 4 × M10×45 27101229717. From 03/2003: 2 × M10×65 07129904681 and 4 × M10×35 23001434694.
- **Both numbers are also listed for the Euro E46 330xd (M57 and M57N)** ([ETK](https://bmwfans.info/parts-catalog/27107530812/), [ETK](https://bmwfans.info/parts-catalog/27107509763/)). The 330xd M57N Touring has a ZF GS6X53DZ gearbox (23007531347) and 2.93 front diff ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/Europe/330xd-M57N/L-N/browse/manual_transmission/manual_transmission_gs6x53dz_4_wheel/)).
- BMW Group Classic gives the 330xd 184 hp / 390 Nm, later 204 hp / 410 Nm [snippet].

**330xi six-speed specifics** ([housing](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/manual_transmission/gs6x37bz_grbx_housing_and_mount_parts/), [fixings](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/manual_transmission/gearbox_mounting_parts/), [prop shafts](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/drive_shaft/drive_shaft_4_wheel/), [shift parts](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/gearshift/gear_shift_parts_manual_transm_4_wheel/), [crossmember](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/engine_and_gearbox_suspension/gearbox_suspension_4_wheel_drive/)) [read]:
- Gearbox-side adapter shaft 23117551424, protection cap 23117551425, M10×95 bolt 23117551426.
- Guide tube 23117531354 and input seal 23117531353: the same parts as the Z4 M's GS6-37BZ ([ETK](https://bmwfans.info/parts-catalog/E85/USA/Z4_M3.2-S54/L-N/browse/manual_transmission/gs6_37bz_dz_sealing_and_mount_parts/)).
- Backup-light switch 23147524811 is the only switch listed on either box. The M3's 420G also carries a gear-recognition switch, 23142229113 (WIRING-AND-CODING.md).
- Bellhousing fixings: 2 × M12×50 23001222891, 2 × M12×90 23001222894, 3 × M8×50 23001222887, 1 × M6×12, 2 × M10×65, dowels 11117524470.
- Prop shafts for every manual xi from 03/2003, 325xi and 330xi alike: front 26207525970 (L = 723 mm; the 718 mm 26207525969 before 03/2003), rear 26117502959 (L = 1,244 mm, "NV-124").
- Crossmember 22316750856 and transfer-case mount 22316773125 are the same as the 325xi's ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/engine_and_gearbox_suspension/gearbox_suspension_4_wheel_drive/)). BMW: "Both manual and automatic transmissions utilize the same part" for the crossmember (ST040).
- Six-speed shift parts, all from 03/2003: shifting arm 25117521280, bearing sleeves 25117528407, shift lever 25117543189, boot 25117522149, selector rod 25117524347, rod joint 25117522384. The five-speed's are 25111434658, 25117519670, 25117527252, 25117501638, 25111434673.

**Flywheel and clutch** [read, ETK]:
- **M3** ([flywheel](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/flywheel_twin_mass_flywheel/), [clutch](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/clutch/clutch/)): dual-mass flywheel 21212229900 (240 mm, 8 × M12×1.5×50 bolts 11222243051, pilot bearing 11211720310); clutch set 21212282667 with disc 21212282666; release bearing 21511223582. The M3 disc is shared only with the M3 CSL, E39 M5 and E38 740i ([ETK](https://bmwfans.info/parts-catalog/21212282666/)).
- **Z4 M** ([clutch](https://bmwfans.info/parts-catalog/E85/USA/Z4_M3.2-S54/L-N/browse/clutch/clutch/), [flywheel](https://bmwfans.info/parts-catalog/E85/USA/Z4_M3.2-S54/L-N/browse/engine/flywheel_twin_mass_flywheel/)): the **same flywheel 21212229900**, but its own clutch set **21217837984** with disc **21217837095** (both Z4 M only). Release bearing 21511223582 and pressure-plate screws 21207548052 are as on the M3.
- **330xi** ([clutch](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/clutch/clutch/)): from 03/2003, clutch set 21217528211, disc 21217526600, release bearing 21517521360. Disc 21217526600 also serves the 325xi, 330i/330Ci, X3 and E53 X5 3.0i ([ETK](https://bmwfans.info/parts-catalog/21217526600/)).

**What the builds ran:**
- **Colorado car:** "A six-speed transmission from a 60,000-mile 330Xi was installed with a fresh OEM 330 clutch kit" ([German Cars For Sale](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed)); Jalopnik called it a "six speed Getrag manual out of a 330i" ([Jalopnik](https://jalopnik.com/does-this-custom-s54-rocking-2001-bmw-325ix-touring-hav-1830305864)) [read]. No gearbox or transfer-case trouble reported through FCP part 2.
- **Baca car:** BimmerLife, quoting the owner: "a 64,000-mile 330xi six-speed manual transmission", and "This is the only touring chassis that will accommodate the 330xi six-speed manual transmission", meaning a manual 325xi Touring. The 2025 sale listing says "420G 6-Speed Transmission" and "330i Transfer Case" [read]. Clutch: "Kyle didn't like the clutch chatter from the lightweight flywheel, so he took it to RRT, who installed an OEM LUK clutch kit" [read].

### Inferences (labelled)
- **The five-speed is under-rated for an S54.** Read with BMW's key, "S5D 320Z" means 320 Nm and the training text's "S5D-280Z" 280 Nm. Either is below the S54's 355 Nm (US) or 365 Nm (Euro). No build used it.
- **The 330xi six-speed is the right box.** Its gearset is the H-gearbox BMW put behind a 262 lb-ft S54 in the Z4 M, and its input side (guide tube, seal) is common with the Z4 M's. So the M3 flywheel plus the Z4 M clutch set is BMW's own S54-to-H-gearbox pairing. Assumption: the X version shares the petrol ratio set; ETK doesn't print ratios.
- **The Colorado car's 330 clutch kit** also fits the spline, since 21217526600 serves the H-box cars. It's built for M54 torque, though.
- **The listing's "420G" is probably a mislabel.** ETK has no four-wheel-drive 420G, no adapter, and no 420G rear housing for the NV 124. BimmerLife's "330xi six-speed" fits everything else known; the Getrag build credit on the ZF box explains the name.
- **Buy the 330xi gearbox as a set.** It exists only from 03/2003. A 325xi built before 03/2003 has the earlier NV 124 and 718 mm front shaft, so take the donor's NV 124 (27107530812), front prop shaft (26207525970), adapter shafts and shift parts with the box. A 03/2003-on 325xi already has the later NV 124 and shaft, and ETK lists the same crossmember either way.
- **The NV 124's 300 Nm.** ST040's figure equals the US 330xi's M54B30 torque (300 Nm, ST045). BMW's own use of the same NV 124 behind 390–410 Nm diesels says 300 Nm isn't the case's hard limit, but there is no BMW rating for an S54 behind it.
- **The clutch chain needs a substitute for the 420G's gear switch.** The MSS54 chain expects the 420G's gear-recognition switch in series with the clutch module (WIRING-AND-CODING.md), and the 330xi box has no such switch. Bridging the switch's two pins at X6053 would make the DME see "in gear" whenever the pedal is up, even in neutral. Undocumented; for the coding-power writer.

### Gaps
- No torque rating for the GS6X37BZ, the NV 124 with an S54, or the S5D 320Z beyond the designations.
- No published account of either build's clutch-chain wiring with the 330xi box.
- No mileage on either build's gearbox beyond about 10,000 (Colorado) and 5,000 (Baca) miles (inference below).

---

## 3. Differential ratios

### Cited findings

| Car | Front diff (type 174) | Rear diff (HAG 188N) | Source [read] |
|---|---|---|---|
| 325xi manual | 3.23 (42:13): 31507500797 to 03/2003, 31507526216 from 03/2003 | 3.23: 33107500783 | [ETK front](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/front_axle/front_diff_components_all_wheel/), [ETK rear](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/rear_axle/final_drive_input_output_4_wheel/) |
| 330xi manual | 3.07 (43:14): 31507500793 / 31507526252 | 3.07: 33107500785 | [ETK front](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/front_axle/front_diff_components_all_wheel/), [ETK rear](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/rear_axle/final_drive_input_output_4_wheel/) |
| 325xi and 330xi automatic | **3.46 (45:13): 31507500799** | **3.46: 33107531623 (also 33107531622)** | same pages |
| X3 2.5i (M54) | **3.91 (43:11): 31507523651**, also listed for the US X3 3.0i with the N52 | **3.91: 33107537722 manual**, 33107533140 automatic | [ETK front](https://bmwfans.info/parts-catalog/E83/USA/X3_2.5i-M54/L-N/browse/front_axle/front_diff_components_all_wheel/), [ETK rear](https://bmwfans.info/parts-catalog/E83/USA/X3_2.5i-M54/L-N/browse/rear_axle/differential_drive_output/), [usage](https://bmwfans.info/parts-catalog/31507523651/) |
| X3 3.0i (M54) | 3.64 (40:11): 31507523653 | 3.64: 33107523667 manual, 33107523669 automatic | [ETK front](https://bmwfans.info/parts-catalog/E83/USA/X3_3.0i-M54/L-N/browse/front_axle/front_diff_components_all_wheel/), [ETK rear](https://bmwfans.info/parts-catalog/E83/USA/X3_3.0i-M54/L-N/browse/rear_axle/differential_drive_output/) |
| M3 | — | 3.62: 33102282480 (45 kg, M differential) | [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/rear_axle/differential_drive_output/). BMW's ST041 table prints 3.64 for the E46 M3; ETK and the guide say 3.62 |

**BMW's ratings and design** (ST040) [read]:
- Front "Type: VAG 174 … Max torque: 2000Nm … Lifetime fluid fill: SAF-XO". Rear "Type: HAG 188N … Max torque: 3000Nm".
- "The complete rear axle and the rear differential are the same as the 2wd version of the 325i and 330i."
- "It uses two open differentials and a single speed transfer case."

**X3 diffs against xi parts** (ETK) [read]:
- **Front:** the X3 diff shares the xi's shaft seals (33107505601, 31521428678), O-rings, type-174 gasket sets, M10×55 10.9 bolt size and the oil pan. Its supporting bracket differs: 31507516064 against the xi's 31537500850.
- **Rear:** the X3's output flanges have an **86 mm bolt circle** (manual) against the E46 xi's **94 mm**. Seals (33107505604) and lock rings (33131214961) are common. Until 01/2007 the X3's rear mount used a longer M14×138 bolt with a 5 mm shim, where the E46 has M14×133.

**What the builds did** [read]:
- **Baca:** "X3 differentials to change the gear ratio to 3.91" (BimmerLife); "3.91 X3 Differentials" (Built for Backroads).
- **Colorado:** "X3 3.0 3:91 ratio (the factory diffs were 2:94s) front and rear differentials … from a low mileage X3" (German Cars For Sale). The 2.94 claim conflicts with ETK's 3.23 for a manual 325xi.
- **FCP:** "After trying two different final drive differential ratios, he settled on 3.91 gearing to prioritize acceleration and responsiveness over loose surfaces"; "a new Wavetrac LSD provides traction", axle not stated (FCP part 1). Part 2: "the 3.91 differential ratio improved the total experience and made the M3baru more drivable in more gears."

**Tires** (2004 Sports Wagon owner's manual, printed p. 127) [read]: "The correct wheel-tire combination affects different systems such as ABS, DSC and ADB-X/DBC. The function of these systems is impaired if improper wheel-tire combinations are used. For this reason, use only tires of the same manufacture and tread configuration." On the xi, chains go on the rear pair only, but "in an extreme emergency … a chain may also be mounted on just one tire for the limited period needed" (p. 128).

### Arithmetic and inferences (labelled)

**Overall gearing.** Arithmetic, using GS6-37BZ "B" ratios for the 330xi box (an assumption), against an M3's 4.227 × 3.62 = 15.30 in first and 0.828 × 3.62 = 3.00 in sixth. The rpm column assumes a 661 mm tyre, about a 255/40R18:

| 330xi six-speed with | First, overall | Against M3 | Sixth, overall | rpm at 70 mph in sixth |
|---|---|---|---|---|
| 3.07 (330xi manual) | 13.35 | 12.7% taller | 2.61 | 2,360 (M3: 2,710) |
| 3.23 (325xi manual) | 14.05 | 8.2% taller | 2.75 | 2,490 |
| **3.46 (xi automatic)** | **15.05** | **1.6% taller** | 2.94 | 2,660 |
| 3.64 (X3 3.0i, M54) | 15.83 | 3.5% shorter | 3.10 | 2,800 |
| 3.91 (X3 2.5i; builds' choice) | 17.01 | 11.2% shorter | 3.33 | 3,010 |

- **The 3.46 automatic pair is the closest match to M3 gearing**, and it's an E46 xi part on both axles: same mountings, same 94 mm rear flanges, same support bracket. The builders' 3.91s deliberately shorten the gearing, which FCP liked for gravel.
- **The X3 rear diff needs work.** Its flanges don't match the xi rear shafts. Moving your E46 output flanges into it should work, given the common seal and lock ring, but neither build mentions it. With an X3 front diff, keep the E46 support bracket and right-hand shaft.
- **The matching rule and its tolerance.** BMW never sold mismatched ratios and publishes no tolerance; every build changed both diffs as a pair. Because the NV 124's centre is an open planetary, a small mismatch would not bind the driveline as it would with a viscous or clutch centre. Instead the planetary would turn continuously: about 0.6% of prop-shaft speed for 3.62 against 3.64, roughly 16 rpm at 100 km/h. The wheels themselves still all roll at road speed. Nobody has tested that for wear, so treat any mismatch as untested.
- **Tyres matter more to DSC than diff ratios.** The DSC compares wheel speeds, and a staggered set changes them. Arithmetic on nominal sizes: an M3's 225/45R18 front is 659.7 mm and its 255/40R18 rear 661.2 mm, 0.2% apart. BMW never approved staggered sizes on an xi.
- **The M3's limited-slip rear isn't a practical option.**
  - Its 3.62 has no front partner; the nearest is the X3 3.0i's 3.64.
  - It's a different, larger diff (45 kg) with different mounting hardware (M14×65 plus 2 × M12×50, against the 188's 2 × M12×80 plus M14×133), which points to the M3 rear subframe and shafts.
  - The xi's Bosch rear wheel-speed sensors would then have to work in M3 trailing arms.
  - No build has tried it. FCP's route, an aftermarket limited-slip unit (Wavetrac) in a matched-ratio diff, is the documented way.

### Gaps
- No BMW tolerance for front-to-rear ratio or rolling-circumference mismatch.
- Whether the X3 front diff's input flange suits the xi front prop shaft; both builds imply it does, without saying.
- Which axle FCP's Wavetrac went into.

---

## 4. Front axle, mounts, shafts, brakes and rack

### Cited findings

**BMW's xi front end** (ST040) [read]:
- "The front axle has been completely re-designed over the standard drive E46. All components are constructed of steel."
- The lower arms are steel, "smaller than the aluminum arms used on the 2wd model", with "a separate ball joint bolted to the axle carrier … to provide clearance for the front axle shafts".
- "The hydraulic engine mounts are different from the 2wd version and have also been relocated to provide front axle clearance."
- Sway bar 23.5 mm. Struts shorter, with reinforcement plates at the strut bearings.
- "The spring travel of the E46/16 is approximately 20mm less … due to the limited angle of deflection of the front axle shafts."
- Rack "constructed with a larger diameter piston"; "The lower steering spindle … connects to the steering rack via a double cardan joint". Turning radius 35.8 ft.
- "Two drive shafts of equal length". "The steering knuckle is modified to accept the CV joint". The front bearings "incorporate the wheel speed sensor pulse wheel into the bearing seal".
- "Standard wheel size is 17x 7.0 to ensure there is enough room for the front axles and brakes."

**ETK** [read]:
- **Axle carrier** 31101096954 (13.9 kg), with left and right adaptors (31106768293/294 from 12/2000) ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/front_axle/front_axle_support_4_wheel/)).
- **Front shafts:** left 31607505199 (L = 605 mm), right 31607505200 (L = 926 mm), inner and outer boot kits 31607565315 and 31607507402, outer CV joint 31607597894, M27×1.5 collar nut 33411133785 ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/front_axle/final_drive_frnt_axle_output_shaft_4whl/)).
- **Knuckles:** 31216756541/542 to 03/2002, 31216759311/312 from 03/2002. Drive flange 31201096423, bearing 31221095702 (45×85×41), "Pulse generator, ABS" 34526756382 ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/front_axle/spring_strut_front_carrier_4_wheel/)).
- **Engine mounts** ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/engine_and_gearbox_suspension/engine_suspension/), [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine_and_gearbox_suspension/engine_suspension/), [ETK 325i](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_and_gearbox_suspension/engine_suspension/)):

| Part | 325xi / 330xi | M3 | 325i Touring |
|---|---|---|---|
| Supporting bracket, left | 22116750853 | 22112229898 | 22111094697 |
| Supporting bracket, right | 22116750852 | 22111094694 | 22111094694 |
| Engine mounts | 11812283798 (**the M3's mount**) + 22116750862 | 11812283798 × 2 | 22116771361 × 2 |
| Bracket-to-block bolts | M8×34 × 7 | M8×26 × 6 + M8×35 × 2 | M8×34 × 8 |
| Right-side heat shield | 22116754500 (180 g) | 22111094624 + 22111094623 | 22111094624 + 22111094623 |

**Rack and steering** ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/steering/power_steering/), [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/power_steering/), [joints xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/steering/steer_col_lower_joint_assy/), [joints M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/steer_col_lower_joint_assy/), [hoses xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/steering/hydro_steering_oil_pipes/), [hoses M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/hydro_steering_oil_pipes/)) [read]:
- **xi:** ZF rack 32136759815 (6.6 kg), fixed with M10×60 bolts 07119902696; lower joint 32306750815 (to 11/2003) or 32306764009, plus double joint 32306754165; pressure hose 32416751242, return 32416796391.
- **M3:** rack 32132229397 (32132282642 with the Competition package), fixed with M10×67 bolts 32106781639; lower joint 32301094700 or 32306764006, with flexible coupling 32301094703. The M3's own hoses and cooler loop: 32412283893, 32412282354, 32412282353.
- A new xi rack costs \$532.99 ([BimmerWorld](https://www.bimmerworld.com/Suspension-Steering/Steering-Components/Steering-Rack-New-AAE-E46-325xi-330xi-3410N.html)) [read].

**Front brakes** ([ETK 325xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/brakes/front_brake_pad_wear_sensor/), [325xi disc](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/brakes/front_brake_brake_disc/), [330xi](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/brakes/front_brake_pad_wear_sensor/), [330xi disc](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/brakes/front_brake_brake_disc/), [330xi knuckle](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/front_axle/spring_strut_front_carrier_4_wheel/), [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/front_brake_pad_wear_sensor/), [M3 disc](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/front_brake_brake_disc/)) [read]:

| | 325xi | 330xi | M3 |
|---|---|---|---|
| Disc | 300 × 22, 34116864058 | 325 × 25, 34116864047 | 325 × 28, 34112229529/530 |
| Caliper | 34116758113/114 | 34116765881/882 | 34112282617/618 |
| Carrier | 34106758120 | 34106765880 | 34112282177 (Competition 34112282619) |
| Carrier bolts | M12×1.5×32, 34116772428 | M12×1.5×32, 34116772428 | **M12×1.5×41**, 34116767217 |
| Dust shields | 34116759595/596 | **34116759595/596** | 34112282109/110 |
| Knuckle | 31216759311/312 | **31216759311/312** | (rear-drive, not used) |

**Builds** [read]:
- **Baca:** "The steering was modified and updated to adapt the factory E46 M3's steering system to the xi platform. … The front driveshafts were replaced with new GKN units. The front control arms received stronger ball joints." Brakes: M3 front calipers and floating rotors, 330i rear calipers (Built for Backroads).
- **Colorado:** "ECS Tuning M3 CSL Brake Kit". "The front CV axles are at an angle that causes to the boots wear prematurely depending on ride height. We have adjusted it as high as possible to help mitigate this. I will include a replacement front axle". Power-steering pump and lines were renewed.
- **FCP:** "The steering isn't as communicative or quick as a 'real' M3 because it has the 325xi steering rack"; "it's a completely different subframe … different control arms, different pickup points, the strut towers are a little different, the steering rack—everything's designed around the all-wheel drive" (part 2). Rhom raised the suspension, and a "custom skid plate protects the front undercarriage" (part 1).

**Front axle torque.** Arithmetic: US S54 355 Nm × 4.350 (first) = 1,544 Nm into the NV 124; 38% = 587 Nm to the front diff and 62% = 957 Nm to the rear. Axle torque (both shafts) by ratio, against BMW's 2,000 Nm front and 3,000 Nm rear figures. BMW doesn't say where its figures apply; this table assumes diff output:

| Ratio | Front axle | Rear axle |
|---|---|---|
| 3.07 | 1,802 Nm (10% under) | 2,939 Nm (2% under) |
| 3.23 | 1,895 (5% under) | 3,093 (3% over) |
| 3.46 | 2,030 (2% over) | 3,313 (10% over) |
| 3.64 | 2,136 (7% over) | 3,485 (16% over) |
| 3.91 | 2,294 (15% over) | 3,744 (25% over) |
| Stock 330xi (300 Nm, 3.07) | 1,522 | 2,484 |

With the Euro 365 Nm, add about 3%.

### Inferences (labelled)
- **Keep the whole xi front axle**: carrier, steel arms, struts, knuckles, hubs, shafts and the xi rack. The M3's rear-drive front axle can't carry drive shafts. Only its brakes transfer, with adaptation.
- **The 330xi brake upgrade bolts on.** The 330xi's 325 × 25 front brake mounts to the same knuckle and shields as the 325xi's. The M3's 325 × 28 needs longer carrier bolts and M3 shields, and per the guide one builder milled the brackets (not re-read; e46fanatics blocked).
- **Engine brackets.**
  - The right-hand M54 and S54 patterns are the same (the 325i and M3 share 22111094694), so the xi's right bracket should bolt to the S54.
  - The left differs between the 325i and M3, so offer up the xi's left bracket and check.
  - Use bolt lengths that suit the S54's iron block: the M3 uses M8×26 where the M54 aluminium block uses M8×34.
  - The xi's left mount is already the M3's part.
- **Power steering.** The S54's pump and the xi rack have no common hose. A custom pressure line from the M3 pump to the xi rack is the likely meaning of Baca's "adapted … steering" and the Colorado car's new "Power Steering Lines".
- **Ride height.** Don't lower an xi beyond stock: BMW cut its spring travel to protect the shafts, and the Colorado car wore boots when lowered.
- **Shaft margins with the S54** are below BMW's own: arithmetic above. Fit new shafts and keep a spare, as Baca and the Colorado car did.

### Gaps
- No measured S54-header-to-right-shaft or sump-to-diff clearance has been published.
- Whether the M3 rack fits the xi carrier: Baca's wording is vague; no part-level account.
- Whether the xi's left engine bracket bolts to the S54 block. *Settle by:* trial fit.

---

## 5. DSC and coding

### Cited findings

**The Bosch DSC III 5.7** (ST040) [read]:
- It is "used in the E46/16 in place of the DSC III MK 60 used on 2wd vehicles. The DSC system is the same as used in the E53."
- Its xi-specific functions are a modified ABS (front wheels may lock up to about 20 km/h on loose surfaces), "ASC+T (All-Wheel Drive version)" and "Four wheel ADB function". ADB brakes a slipping wheel or axle to move torque, "much like a limited slip differential", including a "Longitudinal differential-lock function".
- **CAN:** it "is connected to the CAN bus for communication with the AGS, DME control module, Steering Angle Sensor and the Instrument Cluster … DME - The DME sends current engine torque. DSC commands the DME to reduce (ASC/DSC) or raise (MSR) engine torque. … LEW - The DSC receives steering angle information. KOMBI - The DSC commands the instrument cluster to activate or deactivate the warning lamps."
- **Wheel-speed sensors:** Hall-effect, two-wire, 8 V. "The front sensors of the 2wd and 4wd versions of E46 are physically different and will not fit in the wheel hub. The rear sensors can be confused with the Teves MK 60 sensors and will fit in the rear axle of the 4wd car however they are not compatible with the Bosch system."
- **Steering-angle sensor (LEW):** "mounted towards the lower end of the steering column, above the flexible coupling". It sends angle over CAN, "requires initialization", and then "sends an ID number to the DSC control unit".
- **The DSC button** leaves "Brake intervention … active for the ADB function"; only ASC engine and DSC yaw intervention switch off.
- **Coding:** "Coding must be performed after replacement of the DSC III control module or the steering angle sensor. ZCS coding … Follow on-screen instructions for initialization." The steering-angle offset is needed "after the sensor has been replaced, coded or after repairs to the steering or suspension system".
- **No separate model:** "The all-wheel drive models of the E46 series do not have their own model identification"; DIS asks "Yes for All-Wheel".

**SGBD `DSC57.prg`** ("Robert Bosch DSC57 E38/E39/E52/E53/E46-16") ([DSC57.md](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC57.md)) [read]:
- `COD_LESEN` returns `COD_VARIANTE`, `COD_DBC` and `COD_ACC` and two coding bytes. `COD_SCHREIBEN` writes "2 Codierbytes".
- `STATUS_IO_LESEN_CAN` returns `STAT_MOTORDREHZAHL_WERT` (engine speed) and `STAT_NORM_FUELLUNG_SOLL_WERT` / `_FAHRER_WERT` (normalised fill, %).
- `STATUS_IO_LESEN_ANALOG` returns `STAT_LENKWINKEL_WERT` (degrees), yaw rate and lateral acceleration.
- `TEST_LENKWINKEL`, "Lenkwinkel Initialisierung DSC57", takes `LFD_NR` and returns `STATUS_ABGLEICH` and `ABGL_LWS_ID`.
- `TEST_QUERBESCHLEUNIGUNG`, `TEST_DREHRATE` and `TEST_DRUCK` reset offsets "only on sensor replacement".

**SGBD `MSS54DS0`** ([MSS54DS0.md](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)) [read]:
- Fault locations 0x83 "DSC-Eingriff unplausibel", 0x84 "Timeout DSC-Botschaft", 0x85 "Timeout LWS-Botschaft" (the steering-angle sensor's message) and 0x86 "Timeout KOMBI-Botschaft".
- Fault type "DSC meldet V-Fehler" (0xE9 in the fault-type table).
- `STATUS_V_CAN`, "Fahrzeuggeschwindigkeit v_asc (CAN)": the DME takes road speed from the DSC.

**No transfer-case control.** ETK's xi transfer-box group lists only the NV 124, its single parts and fixings; the X3's group adds "control_unit_transfer_box" for its ATC 400 ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/transfer_box_electric_gearbox/transfer_case_nv_124/)). ST040: single speed, no viscous coupler.

**Builds.** None published its DSC outcome. The Colorado listing says "everything functions as if came from the factory this way (air conditioning, AWD, emissions controls, etc)" ([German Cars For Sale](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed)) [read]. Baca's is not stated.

### Inferences (labelled)
- **Keep the xi's own DSC 5.7, sensors, yaw sensor and steering-angle sensor.** An MK60 can't run the xi: its front sensors won't fit the xi hubs, and it has no four-wheel ADB. For the AWD route, "Option A, keep your own unit", is the only option.
- **The CAN link should work, but nobody has shown it.** The DSC 5.7 and the M3's MK20/MK60 both talk to their DMEs over the same E46 CAN. The DSC 5.7 reads engine speed and normalised fill rather than an engine-specific number, so it may tolerate the MSS54.
- **The MSS54 listens for two messages here.** It needs the DSC's road-speed message, or it logs 0x84 and loses cruise. It also monitors the steering-angle sensor's message (0x85). Whether the xi's DSC 5.7-era sensor sends the message the MSS54 expects is unknown, and a stored 0x85 would be the sign.
- **Coding stays as it is.** The DSC 5.7's two coding bytes come from the car's own ZCS or vehicle order, so there's no reason to recode for an engine change. Re-initialise the steering angle after alignment.
- **The cluster.** An M3 cluster takes the DSC and yellow brake lamps over CAN, while the ABS lamp is hard-wired from the DSC 5.7 (ST040). Check all three at key-on.

### Gaps
- The first documented MSS54 + DSC 5.7 result will be yours. Neither build published its fault memory.
- The e46fanatics thread 1102352 may hold the answer. The guide notes its owner moved the brake-switch wire to clear a yellow brake lamp. A 20 Aug 2025 Wayback snapshot exists, but this environment couldn't reach web.archive.org.

---

## 6. Exhaust, heat shields, cooling and fuel on the xi

### Cited findings

**Exhaust** ([ETK 325xi manifolds](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/engine/exhaust_manifold_with_catalyst/), [325xi front section](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/exhaust_system/catalytic_converter_front_silencer/), [325xi hangers](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/exhaust_system/suspension_parts_exhaust/), [325i hangers](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/exhaust_system/suspension_parts_exhaust/), [330xi hangers](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/exhaust_system/suspension_parts_exhaust/)) [read]:
- The 325xi uses **the same catalyst-manifolds as the 325i**, 18407514502 and 18407514503.
- Its front muffler section differs: 18107504169 against the 325i's 18107504168.
- The exhaust bracket at the gearbox is 18207502523 on manual xi cars, five- and six-speed, against the 325i's 18311728547 ("GETRAG").
- The exhaust support 18301436331, clamps and joint sleeves are common.
- BMW: the xi body has "a widened transmission tunnel and modifications on the driver's side to accept the transfer case" (ST040).

**Heat shields** ([ETK 325xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/vehicle_trim/insulation_2/), [325i](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_trim/insulation_2/), [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_trim/insulation/)) [read]:

| Shield | 325xi | 325i Touring | M3 |
|---|---|---|---|
| Tunnel heat insulator | **51488253953** | 51488193807 | 51487893366 |
| Heat insulation (right front) | 51488253954 | 51488253954 | 51487893370 |
| Rear silencer insulator | 51487037885 | 51487037885 | 51482494848 |
| Engine-support heat plate | 51488177000 | 51488177000 | 51487893363 |
| Front-wall plate | 51488202979 | 51488202979 | 51487893670 |
| Underbody screens | front 51718265977, **centre 51718265927** | — | front 51717895091 |

**Fuel** ([ETK 325xi tank](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/fuel_supply/fuel_tank_attaching_parts/), [325xi lines](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/fuel_supply/fuel_pipe_and_mounting_parts/), [325xi pump](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/), [325i tank](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/fuel_supply/fuel_tank_attaching_parts/)) [read]:
- The 325xi Touring has **the same tank** (16116766940), straps, filler parts and vent pipe as the 325i Touring.
- It has the same delivery unit (16146766942), left sender (16116768788) and jet pump (16146755880).
- It has the same feed, return and front lines (16126752180, 16126752186, 16126752183), the same pipe set (16117175998) and the same clips.
- **The xi adds only a "Protective plate for fuel tank" 16111183924**, with three spring nuts 51418229585.

**Builds** [read]:
- **Colorado:** "custom high-flow exhaust with high-flow catalytic convertors … passes Colorado emissions"; "M3 Radiator … expansion tank was relocated to the right of the engine bay (the washer reservoir was removed …)"; Mishimoto oil cooler.
- **Baca:** "3" Custom Mandrel Bent Stainless Steel Exhaust", "Super Sprint Mid Pipes", "T-304 Billy Boat Exhaust"; "M3 5-bar Fuel System"; "Fuel Tank Baffles"; "factory E46 M3" cooling.
- **FCP:** "An M3 fuel pump replaced the 325 unit".

### Inferences (labelled)
- **Fuel:** `fuel_system_fit.md`'s plan applies to a 325xi Touring unchanged. Keep the xi's tank protective plate.
- **Heat shields:** keep the xi's tunnel heat insulator, its right engine-mount heat shield and its centre screen. They're shaped around the xi tunnel and mounts.
- **Exhaust:** the M54's manifolds clear the xi's right shaft, but nobody has published whether the S54 headers do, or whether the M3's front pipes clear the NV 124 on the driver's side of the tunnel. Both builds ran custom or aftermarket pipes from the headers back.
- **Oil cooler:** the Colorado car's aftermarket cooler hints, but doesn't prove, that the M3 cooler lines were awkward with the xi front diff.

### Gaps
- Header-to-shaft and pipe-to-NV 124 clearances. *Settle by:* trial fit, at full droop and at full bump.

---

## 7. Documented AWD S54 E46 builds

| Car | What they did | What broke | Cost and time | Sources |
|---|---|---|---|---|
| **Colorado 2001 325xi Touring** (VIN WBAAW33421EN80596, Orient Blue, about 278,000–280,000 chassis miles). Built by "a BMW master tech" (FCP: "a BMW master technician"; listing: "BMW Master Tech and Shop Owner") | S54 from a 2004 M3 (VANOS failure, head rebuilt, rod bearings) at about 80,000 engine miles; 330xi six-speed with "OEM 330 clutch kit"; "330Xi Oil Pan w/ Custom Baffles"; "M50 Oil Pump w/ Welded Nut"; Mishimoto cooler; "X3 3.0 3:91" diffs; custom tune; M3 radiator; CSL brake kit; KW V1; riveted flares. Later, under Daniel Sloan and Rhom Innovations: raised suspension, reinforced strut towers, skid plate, Wavetrac LSD, 3.91 after trying two ratios, M3 fuel pump, harness rework | Front CV boots wore when lowered. Then oil starvation: "spun bearings, cracked rods, and a damaged crankshaft"; the pump chain and gear ground the pan front. Crank straightened, heat-treated, re-nitrided; new pistons and rods; pan re-fabricated with baffles; then 1,600 trouble-free miles in a summer heatwave (part 2, dated Aug 2021) | Asked \$26,500 (Nov 2018); \$22,800 (Mar 2019); "over budget and over time" | [Jalopnik](https://jalopnik.com/does-this-custom-s54-rocking-2001-bmw-325ix-touring-hav-1830305864), [BMWBlog 2018](https://www.bmwblog.com/2018/11/09/want-this-s54-swapped-e46-3-series-touring/), [Chicago Garage](https://www.thechicagogarage.com/threads/2001-bmw-m3-s54-swapped-325xi-sport-wagon-6-speed-awd.168023/), [German Cars For Sale](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed), [FCP 1](https://www.fcpeuro.com/blog/bmw-e46-m3xi-an-m3-powered-bmw-rally-wagon-ready-for-almost-anything), [FCP 2](https://www.fcpeuro.com/blog/back-on-the-road-off-the-road-bmw-e46-m3xi-part-2) [read] |
| **Baca 2004 325xi Touring** (VIN WBAEP33484PE91920), Virginia, 2018–22; inspired by the Colorado car, which BimmerLife says they saw "listed by a specialty dealer, Glen Shelly" | 76,000-mile S54 (ACL rod bearings, VANOS); 330xi six-speed (BimmerLife) or "420G" (listing); "330i" transfer case; X3 3.91 diffs; 330xi pan "custom machined" with an S52 windage tray and M50 pump; new GKN front shafts; stronger ball joints; M3 steering "adapted"; M3 front brakes; M3 cooling and fuel; Kassel tune (~370 crank hp claimed); rear subframe "custom-built with reinforced rear sway-bar mounts"; body by Mid-Atlantic Customs | Clutch chatter with a lightweight flywheel, replaced by an OEM LuK kit. Nothing else reported | 280 h mechanical; "over \$70k invested"; sold, listed at \$65,000. 114,000 mi at purchase, 119,019 at sale: about 5,000 miles in six years (inference) | [BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/), [Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xit-touring-awd-s54-swap) [read] |
| **Austin Sera's** AWD S54 build, Virginia | BimmerLife calls Sera "the only other person I could find that had taken on the challenge of building an all-wheel-drive S54 drivetrain"; he supplied Baca's parts list | Not documented (one search found nothing) | — | [BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/) [read] |
| **E83 X3 with S54** (context: same oil pan family) | Six-speed manual, RWD "but can be switched back to X-drive", "custom oil pump and pan" | — | \$19,840 asking; 15,000 miles since the swap | [The Drive](https://www.thedrive.com/news/e46-m3-swapped-bmw-x3-with-a-six-speed-is-the-m-suv-you-want) [read] |

**Inference: the Colorado car is the FCP car.** It's the same 2001 325xi Touring bought in Denver in March 2019, built by a BMW master tech. Engine mileage since the swap: about 8,000 by November 2018, plus 1,600 to Portland, plus local use and the failed trip; roughly 10,000–12,000 miles before the bearing failure.

---

## Guide-ready section

### Parts table

"Use" is for the keep-AWD route. ETK numbers are as printed; check every one against your VIN.

| System | Item | 325xi (yours) | US M3 (donor) | 330xi / X3 / other | Use |
|---|---|---|---|---|---|
| Oil | Pan | 11137519432 | 11137838130 | 330xi and X3 M54: **11137519432** (same) | Your pan, or a second 11137519432, machined (two builds) or re-fabricated (FCP) |
| Oil | Pan gasket | 11131437237 | 11131437237 | same | New |
| Oil | Pump | 11417501568 | 11417838123 (two-stage) | M50/M52/S52: 11411740154 | M50-family pump (both builds); secure the left-hand nut (welded, or Achilles kit [snippet]) |
| Oil | Pickup | 11417502667 | 11417834887 + return 11417834889 | — | Not documented; prove clearance |
| Oil | Windage | — | — | S52 family oil deflector 11131433060 | As Baca |
| Oil | Dipstick / tube | 11437506769 / 11437531260 | 11437831140 / 11437832140 | — | xi parts with the xi pan; check fit |
| Oil | Level sensor | 12617508003 | 12617508003 | — | Either |
| Front diff | Diff (type 174) | 3.23: 31507526216 | — | 3.46 auto 31507500799; X3 3.64 31507523653; X3 3.91 31507523651 | Pair with the rear |
| Front diff | Fixings | 4 × M10×55 10.9 (07119905161), gasket set 31507500347 | — | X3 31517547750 | — |
| Front diff | Right support bracket with bearing | 31537500850 (\$166.73, BimmerWorld) | — | X3 31507516064 | Keep the E46 part |
| Front axle | Shafts | L 31607505199 (605 mm), R 31607505200 (926 mm) | — | — | New, as Baca (GKN) |
| Front axle | Carrier | 31101096954 | — | — | Keep |
| Mounts | Engine brackets | L 22116750853, R 22116750852 | L 22112229898, R 22111094694 | — | xi brackets; check the left fits the S54 |
| Mounts | Engine mounts | 11812283798 + 22116750862 | 11812283798 × 2 | — | xi set |
| Mounts | Right heat shield | 22116754500 | 22111094624 | — | xi |
| Gearbox | Gearbox | S5D 320Z (THCG/THCN/THCR) | 420G 23002229721 (rear-drive only) | **330xi GS6X37BZ 23007563053 (from 03/2003)** | 330xi six-speed |
| Gearbox | Gearbox-side adapter | — | — | 23117551424 + cap 23117551425 + M10×95 23117551426 | With the box |
| Gearbox | Bellhousing fixings | — | — | 23001222891 ×2, 23001222894 ×2, 23001222887 ×3, 07119905524, 07129904681 ×2, dowels 11117524470 | Per ETK for the box |
| Clutch | Flywheel | M54 DMF | **21212229900** | Z4 M: same | M3 flywheel, 8 new bolts 11222243051 |
| Clutch | Clutch set / disc | — | 21212282667 / 21212282666 (420G spline) | **Z4 M 21217837984 / 21217837095**; 330xi 21217528211 / 21217526600 | Z4 M set (BMW's S54 + H-box pairing); the Colorado car used the 330 set |
| Clutch | Release bearing | 21517521360 (6-speed) | 21511223582 | Z4 M: 21511223582 | 21511223582 |
| Transfer case | NV 124 | 27107509763 (to 03/2003) or 27107530812 | — | 330xi six-speed: 27107530812 | From 03/2003 unit |
| Transfer case | Adapter shaft, O-ring | 27107525789, 27107536962 | — | same | — |
| Transfer case | Fixings | to 03/2003: 23001434691 ×2, 27101229717 ×4 | — | from 03/2003: 07129904681 ×2, 23001434694 ×4 | Match the NV 124 |
| Transfer case | Fluid | MTF-LT1, 0.24 L, plugs 33 Nm (ST040) | — | — | — |
| Prop shafts | Front | 26207525969 (718 mm, to 03/2003) | — | **26207525970 (723 mm, manual from 03/2003)**, Torx 26117571956 ×4, 26117525945 ×3 | 723 mm with the late NV 124 |
| Prop shafts | Rear | 26117502959 (1,244 mm) | — | same | Keep |
| Crossmember | Support / mount | 22316750856 / 22316773125 | — | same | Keep |
| Shifter | Six-speed parts | five-speed set | — | 25117521280, 25117528407 ×2, 25117543189, 25117522149, 25117524347, 25117522384 | From the 330xi |
| Rear diff | Diff (HAG 188N) | 3.23: 33107500783 (94 mm flanges) | 3.62 33102282480 (not used) | 3.46 auto 33107531623; X3 3.91 33107537722 (86 mm flanges); X3 3.64 33107523667 | Same ratio as the front; with X3, move your 94 mm flanges (inference) |
| Steering | Rack | 32136759815 (M10×60 bolts) | 32132229397 | — | Keep the xi rack (FCP) |
| Steering | Lower joint | 32306764009 + double joint 32306754165 | 32306764006 + flex coupling 32301094703 | — | xi |
| Steering | Pressure hose | 32416751242 | 32412283893 (+ cooler loop) | — | Custom line, S54 pump to xi rack (inference) |
| Brakes | Front | 300 × 22 | 325 × 28 | **330xi 325 × 25: discs 34116864047, calipers 34116765881/882, carriers 34106765880** | 330xi set bolts on; M3 set needs M12×41 bolts, M3 shields and possibly machining |
| DSC | Unit, sensors, steering-angle sensor | Bosch DSC 5.7 | MK20/MK60 (not used) | — | Keep all xi parts |
| Exhaust | Gearbox bracket | 18207502523 | — | 330xi: same | Keep |
| Heat | Tunnel insulator | 51488253953 | 51487893366 | 325i 51488193807 | Keep the xi part |
| Heat | Underbody screens | 51718265977, 51718265927 | — | — | Keep |
| Fuel | Tank, pump, lines | as the 325i Touring | — | — | Per `fuel_system_fit.md`; keep the protective plate 16111183924 |
| Wiring | Gear-recognition switch | none | 23142229113 (on the 420G) | 330xi box: none | Bridge in the MSS54 chain (inference; coding-power writer) |

### Order of work, with checks and pass values

Use the guide's phases for everything not listed here. Where BMW publishes no value, the pass value is a measurement you take first, from the donor or your own M54 in the same pan. That makes the build its own reference.

**Phase 0: decide and baseline**

1. **Decode the VIN.** Confirm 325xi, manual, and the build month (03/2003 changes the NV 124, front prop shaft and shift parts; 09/2003 the gearbox and diff bolts).
   - Pass: a manual 325xi.
   - An automatic xi needs the manual pedals, clutch hydraulics and xi manual crossmember work as well; out of scope here.
2. **Read your xi's DSC fault memory** with Tool32: `DSC57.PRG` `FS_LESEN`. Also `STATUS_IO_LESEN_ANALOG` with the wheel straight.
   - Pass: no stored faults; `STAT_LENKWINKEL_WERT` near 0°.
   - This is your known-good DSC baseline before anything changes.
3. **On the running donor M3**, fit the guide's mechanical gauge at the oil-pressure switch port. Record oil pressure at hot idle, 3,000 rpm and 6,000 rpm, with the oil temperature.
   - These numbers become the AWD engine's pass values in step 17.
   - Inference: matching the donor's pressures is the best available test without a TIS specification.

**Phase 1: parts**

4. **Buy the 330xi six-speed as a set:** box 23007563053, with its NV 124 27107530812, both adapter shafts, the 723 mm front prop shaft and the six-speed shift parts.
   - Check: the gearbox label reads GS6X37BZ and the transfer case NV 124.
   - Pass: the part numbers match the parts table.
5. **Buy a matched diff pair:** 3.46 xi automatic, 3.64 X3 3.0i M54, or 3.91 X3 2.5i.
   - Check the ratio tag on each.
   - Bench check: tie both output flanges together and count input-flange turns for one output turn. Pass: equal to the stated ratio within a tenth of a turn, front and rear alike.
6. **Clutch and oil parts:** Z4 M clutch set 21217837984, release bearing 21511223582 and M3 flywheel bolts. A second xi pan, an M50-family pump 11411740154 with a secured nut, and oil deflector 11131433060.

**Phase 2: oil system, engine on the stand**

7. **Before the M54 leaves the xi**, or on the stand with its own pan, take reference measurements with modelling clay:
   - pump sprocket and chain to the pan's front wall;
   - pickup mouth to the pan floor.
   - Record both. They're the pass values for step 9.
8. **Fit the M50-family pump, a pickup and the deflector** to the S54. Turn the crank two full turns by hand with the pan trial-fitted on clay.
   - Pass: no contact anywhere, and no clay thinner than the M54's references from step 7.
   - Where it fails, machine or fabricate the pan (as both cars ended up doing) and repeat.
9. **Fit baffles** (both cars did) and re-check step 8.
10. **Check the dipstick** against a measured fill. Check the xi dipstick tube clears the S54's intake side.

**Phase 3: gearbox and transfer case**

11. **Fit the M3 flywheel** with eight new bolts: 105 Nm, threads oiled, per the guide. Then the Z4 M clutch, the 330xi box, the adapter shafts, and the NV 124 with its fixings for its date.
    - Fill the NV 124 with MTF-LT1, 0.24 L; plugs 33 Nm (ST040).

**Phase 4: install**

12. **Fit the xi engine brackets.** Offer up the left bracket first.
    - Pass: every hole lines up without force, and the bolts give full thread engagement in the iron block (M3 lengths for reference).
13. **Fit the front diff** to the pan (4 × M10×55 10.9) with the E46 support bracket, then the right intermediate shaft through the tube, the shafts, prop shafts, crossmember and mounts.
14. **Clearance checks at full droop and full bump, with the steering at both locks:**
    - S54 headers to the right shaft and support bracket;
    - front prop shaft to the starter and oil-cooler lines;
    - exhaust to the NV 124 and the tunnel insulator.
    - Pass: no contact, and every heat shield refitted. BMW gives no figure; any rub mark later means fail.
15. **Ride height:** stock xi height or higher.
    - Pass: CV boots not stretched or kinked at full droop. The Colorado car wore its boots out when lowered.

**Phase 5: steering, brakes, wiring**

16. **Steering, brakes and clutch wiring:**
    - Keep the xi rack and joint; make the custom pressure line. Bleed. Pass: no leaks at full lock with the engine running.
    - Fit the 330xi front brakes, or the M3's with their bolts and shields. Pass: caliper clears the wheel by hand-spin at lock.
    - Fit the clutch chain with a gear-switch bridge (inference). Pass, per the guide's test: `STAT_KRAFTSCHLUSS_EIN` follows the pedal, with no fault 0x50.

**Phase 6: first start and the oil proof**

17. **First start** per the guide.
    - Pass: hot-idle oil pressure at least 0.7 bar (the guide's figure) **and** at least the donor's step-3 reading at the same rpm and oil temperature.
    - Repeat at 3,000 and 6,000 rpm. Pass: at least the donor's readings.
    - Any shortfall: stop.
18. **Oil analysis** at the first change (about 500 miles) and again at 1,000–1,500 miles.
    - Pass: aluminium not rising between samples.
    - Inference: FCP's clean filter hid aluminium dust, so a filter check alone isn't enough.

**Phase 7: DSC 5.7 and CAN**

19. **Ignition on.**
    - Pass: the DSC, yellow brake and ABS lamps light, then go out after the engine starts and the car rolls a few metres.
    - MSS54 fault memory: none of 0x83, 0x84, 0x85 or 0x86, and no fault of type "DSC meldet V-Fehler".
    - `DSC57.PRG` `FS_LESEN`: empty after clearing and a drive.
20. **`STATUS_IO_LESEN_CAN` at idle and at 3,000 rpm.**
    - Pass: `STAT_MOTORDREHZAHL_WERT` matches the tachometer, and the normalised fill rises with throttle.
    - On a drive, MSS54 `STATUS_V_CAN` matches the speedometer.
21. **After the alignment, run `TEST_LENKWINKEL`.**
    - Pass: job OK and `ABGL_LWS_ID` returned; `STAT_LENKWINKEL_WERT` about 0° with the wheel straight; DSC lamp off.
22. **Traction test** on a loose surface at low speed.
    - Pass: the DSC lamp flashes and engine power drops during wheelspin. With DSC switched off, ADB still brakes a spinning wheel (ST040).
23. **Driveline check at 500 miles:** NV 124, diff and gearbox seals dry; CV boots intact; no rub marks.

### Decision: keep AWD or convert to rear drive

| Question | Keep AWD (this note) | Convert to RWD (other researcher; guide text) |
|---|---|---|
| Front axle | Keep the xi's: carrier, arms, knuckles, shafts, rack | Fit the M3's rear-drive front axle (carrier 31111096902) |
| Oil system | No BMW part fits. xi pan with a single-stage pump, machined or fabricated; one documented engine failure | The S54's own pan and pump |
| Gearbox | 330xi six-speed (03/2003+) with its NV 124, shafts and shift parts; Z4 M clutch | The donor's 420G and M3 parts |
| Diffs | Matched pair: 3.46 xi auto, 3.64 or 3.91 X3. M3 limited-slip diff impractical | M3 3.62 limited-slip diff |
| DSC | Keep the DSC 5.7; MSS54 CAN undocumented, test it | Fit an MK60 (guide), with its own open questions |
| Torque margins | NV 124 rated "300Nm" by BMW (but used behind 390–410 Nm diesels); diffs over BMW's figures at 3.91 (arithmetic) | M3 parts, rated by BMW for the S54 |
| Builds | Two in the US (one engine failure), plus an unpublished one | BaT car and JMCCRNA (guide) |
| What you gain | Winter traction; 17 mm more clearance; 38:62 split with ADB-X | M3 handling and parts; about 100 kg lighter (BMW's xi figure) |
| Difficulty | Very hard: fabrication plus one-off integration | Hard: more M3 parts, fewer unknowns |

---

## Diagram-ready data: xi driveline layout

**View:** plan from above, front at the top. US left-hand drive, so the driver's side is the left of the drawing. A side-view inset shows the pan, tube and diff heights.

| ID | Component | Position | Connects to | Data |
|---|---|---|---|---|
| E | S54 engine | Centre line, longitudinal | G (bellhousing), P | 355 Nm at 4,900 rpm (US); 8,000 rpm limit |
| P | Oil pan 11137519432 (xi; same on 330xi and X3) | Under E | FD bolted to its **left** side; tube T through its **front** section; SB on its **right** side | Gasket 11131437237 (common); pump inside: M50-family single-stage on both builds; S54's own pump has a front scavenge pickup that conflicts with T |
| T | Tube welded through P | Across the front of P, left to right | Carries IS | BMW: "A connecting tube is welded into the oil pan" |
| FD | Front diff, type VAG 174 | Left of P, at the front axle line | FP (input, from the rear), FL (left), IS (right) | Ratio = RD's; xi 3.23 / 3.07 manual, 3.46 auto; X3 3.64 / 3.91. BMW max 2,000 Nm |
| IS | Intermediate shaft | Inside T | FD to SB to FR | Part of shaft 31607505200 |
| SB | Support bracket with bearing 31537500850 | Right side of P | Holds IS | Non-serviceable bearing |
| FL / FR | Front shafts | FD to left hub; SB to right hub | Knuckles 31216759311/312 | L 605 mm 31607505199; R 926 mm 31607505200; spring travel limited by shaft angle |
| G | Gearbox, 330xi GS6X37BZ 23007563053 | Behind E | TC | 4.350 / 2.496 / 1.665 / 1.234 / 1.000 / 0.851 (petrol "B" set; assumption for the X version) |
| TC | Transfer case NV 124 27107530812 | Bolted to G's rear housing; front output on the **left** | Input from G via adapter shafts 23117551424 and 27107525789; ring gear to RP; sun and transfer gear to FP | 38:62 torque, 1:1 speed, open planetary; BMW "Maximum Torque 300Nm"; MTF-LT1 0.24 L |
| FP | Front prop shaft 26207525970 | From TC's left output, forward along the left of G and E | FD input | 723 mm, 40 mm single piece, U-joints at both ends |
| RP | Rear prop shaft 26117502959 | Centre tunnel | RD | 1,244 mm |
| RD | Rear diff, HAG 188N | Rear axle carrier (as on the 325i) | Rear shafts | Same ratio as FD; BMW max 3,000 Nm |
| H | S54 headers | Right side of E, down and back | Exhaust | **Check zone:** H against FR and SB |
| X | Exhaust pipes | Under the tunnel | Hanger 18207502523 on G | **Check zone:** X against TC and the tunnel insulator 51488253953 |
| D | Bosch DSC 5.7 | Engine bay. BMW puts its pre-charge pump below the master cylinder on the left; the hydraulic unit's position isn't stated | CAN to E's MSS54, KOMBI, LEW | ADB-X on all four wheels |
| L | Steering-angle sensor (LEW) | Lower steering column | CAN | Initialised with `TEST_LENKWINKEL` |

**Torque path (first gear, US S54, 3.91 pair), as arrow labels.** E 355 Nm → G ×4.350 = 1,544 Nm → TC: 587 Nm to FP (38%), 957 Nm to RP (62%) → FD ×3.91 = 2,294 Nm at the front axle; RD ×3.91 = 3,744 Nm at the rear axle. Mark BMW's figures beside them: NV 124 300 Nm, VAG 174 2,000 Nm, HAG 188N 3,000 Nm. Footnote: arithmetic; BMW doesn't say where its diff figures apply.

**Before and after panels:**
- **Before:** M54 (300 Nm on the 330xi; the 325xi's M54B25 less), S5D 320Z five-speed, matched 3.23 / 3.23.
- **After:** S54 with the GS6X37BZ, a matched 3.46 / 3.64 / 3.91 pair, and the pan re-made inside.

---

## Guide corrections

1. **README line 62** (Why your car is a good start): "Keeping all-wheel drive behind an S54 has needed a modified 330xi oil pan and X3 differentials ([BimmerLife]), and FCP Euro's S54 xi Touring suffered poor oil flow that it put down to the all-wheel-drive refit ([FCP Euro])."
   - **Correction:** the "330xi oil pan" is the 325xi's own part, 11137519432, also used by the X3 M54 ([ETK](https://bmwfans.info/parts-catalog/11137519432/)).
   - Both documented cars also replaced the S54's two-stage pump with an M50-family single-stage pump ([BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/), [German Cars For Sale](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed)).
   - FCP Euro's car is the Colorado car built that way. Its failure was specific: "The oil pump chain was digging into the pan, and the pickup tube didn't have enough clearance to supply oil properly … spun bearings, cracked rods, and a damaged crankshaft" ([FCP Euro, part 1](https://www.fcpeuro.com/blog/bmw-e46-m3xi-an-m3-powered-bmw-rally-wagon-ready-for-almost-anything)).
2. **README line 73:** "Keeping all-wheel drive needs the oil-pan and differential work described above."
   - **Correction:** it also needs the 330xi six-speed, built from 03/2003, with that era's NV 124, 723 mm front prop shaft and six-speed shift parts. The 325xi's own five-speed is "S5D 320Z" (ETK) or "S5D-280Z" (BMW training), rated below the S54.
   - It needs an S54-compatible clutch (BMW's Z4 M set on the M3 flywheel), a custom power-steering pressure line, and a matched diff pair ([ETK](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/manual_transmission/manual_transmission_gs6x37bz_dz_4_wheel/), [ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf)).
3. **README line 72:** "You need the donor's rear-drive subframe (31111096902) with the whole M3 front axle".
   - **Correction:** true only when converting to rear drive. Keeping AWD, you keep the xi carrier, arms, knuckles, shafts and rack; only the M3 front brakes transfer, with adaptation.
   - The 330xi's 325 × 25 front brake bolts to the xi knuckle unchanged ([ETK](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/brakes/front_brake_pad_wear_sensor/)).
4. **README line 74 (DSC):** "this guide's default of keeping your own DSC unit doesn't exist. You'd fit an MK60 … and adapt the DSC wiring".
   - **Correction:** for the keep-AWD route the reverse is true: keep your own DSC 5.7. BMW: the xi's front wheel-speed sensors "are physically different and will not fit in the wheel hub" of a 2wd car, and four-wheel ADB is a DSC 5.7 function ([ST040, DSC 5.7](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/8%20dsc%20205_djvu.txt)).
   - The MK60 sentence applies only to a rear-drive conversion.
5. **README line 75:** "Not checked for the xi: the fuel tank, tunnel heat shields and exhaust hangers."
   - **Replace with:** the 325xi Touring uses the 325i Touring's tank, pump, senders, lines and pipe set, plus a tank protective plate 16111183924.
   - Its tunnel heat insulator (51488253953) and the gearbox-mounted exhaust bracket (18207502523) are xi parts; the catalyst-manifolds are the 325i's ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/fuel_supply/fuel_tank_attaching_parts/), [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/vehicle_trim/insulation_2/)).
6. **README line 77:** "budget for the second front axle and the DSC work".
   - **Correction:** that's the rear-drive budget. Keeping AWD needs no second front axle; budget instead for the gearbox set, diff pair, oil-system fabrication and the CAN test.
7. **README line 122 (Baca row):** "kept AWD (330xi oil pan, X3 diffs)".
   - **Add:** "with an M50 oil pump and S52 windage tray; X3 diffs at 3.91 (X3 2.5i ratio); NV 124 transfer case; new GKN front shafts" ([BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/)).
   - On "six-speed (330xi per BimmerLife, 420G per the sale listing)": ETK lists the 420G only on the M3, with no four-wheel-drive version ([ETK](https://bmwfans.info/parts-catalog/23002229721/)), so BimmerLife's 330xi six-speed is the consistent reading.
8. **README Sources, line 2057:** "[FCP Euro's S54 xi Touring] … [BMWBlog: a rivet-flare S54 Touring (2018)]".
   - **Correction:** these are the same car: a 2001 325iX Touring, AWD, listed in Denver in November 2018 and sold through Glen Shelly in March 2019 to FCP's Daniel Sloan ([BMWBlog](https://www.bmwblog.com/2018/11/09/want-this-s54-swapped-e46-3-series-touring/), [Jalopnik](https://jalopnik.com/does-this-custom-s54-rocking-2001-bmw-325ix-touring-hav-1830305864), [German Cars For Sale](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed), [FCP part 1](https://www.fcpeuro.com/blog/bmw-e46-m3xi-an-m3-powered-bmw-rally-wagon-ready-for-almost-anything)).
   - It deserves a builds-table row (section 7).
9. **README line 1661:** "If your car turns out to be a 325xi, it has a Bosch DSC 5.7 instead, and Option A doesn't exist."
   - **Correction:** keeping AWD, Option A (your own unit) is the only option.
10. **WIRING-AND-CODING.md line 1039 (steering-angle table), Bosch DSC 5.7 row.**
    - **Add:** `TEST_LENKWINKEL` takes argument `LFD_NR` and returns `STATUS_ABGLEICH` and `ABGL_LWS_ID`. `STATUS_IO_LESEN_ANALOG` reads the angle ([DSC57.md](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC57.md)).
11. **WIRING-AND-CODING.md, "Clutch switch, gear switch and cruise":** "the 420G's gear-recognition switch in series".
    - **Add:** an xi keeping AWD runs the 330xi six-speed, which has no such switch; ETK lists only the backup-light switch 23147524811 ([ETK](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/L-N/browse/manual_transmission/gs6x37bz_grbx_housing_and_mount_parts/)).
    - The chain needs a bridge where the switch would be; inference, untested.

---

## Findings that bear on the rear-drive half

- **Rear wheel-speed sensors.** BMW: MK60 rear sensors "will fit in the rear axle of the 4wd car however they are not compatible with the Bosch system". The reverse matters for a conversion that fits an MK60: the xi's Bosch rear sensors (Hall-effect, two-wire, 8 V) shouldn't be assumed to work with an MK60 ([ST040 DSC 5.7](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/8%20dsc%20205_djvu.txt)).
- **The rear axle.** The xi's rear axle carrier and diff type are the 325i's (ST040), so a conversion can keep them or fit the M3's.
- **The tunnel and crossmember.** The xi gearbox crossmember (22316750856) is xi-specific, and the xi tunnel is widened on the driver's side (ST040). The guide's JMCCRNA row needed a custom gearbox bracket.
- **More RWD examples**, not read: an Engine Swap Depot 2004 325xi Touring, five-speed, converted to RWD with a 2003 M3's S54 [snippet; site 403], and a Built for Backroads "2004 BMW 325xi Touring S54 swap" listing.
- **Fuel and heat shields:** as in section 6; they apply to either route.
