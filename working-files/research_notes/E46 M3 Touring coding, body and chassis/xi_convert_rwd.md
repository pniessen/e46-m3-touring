# Converting a US 325xi Touring to rear-wheel drive with the M3 running gear (xi-rwd)

Research date: 22 October 2026. Researcher: `xi-rwd`. Scope: making a US 325xi Touring (2001–05, all-wheel drive) rear-drive with a 2001–06 US E46 M3 donor, as a new subchapter of the guide. The other half (keeping all-wheel drive) belongs to another researcher; leads for it are at the end.

This builds on the guide's README "If your car is a 325xi" (lines 68–77), the documented-builds table (JMCCRNA and the Bring a Trailer car), README "DSC, brakes and steering angle", the Massachusetts section (test groups "3BMXV…"), WIRING-AND-CODING.md line 138, and the round-4 notes `front_axle_brakes_abs.md`, `coding_powertrain_chassis.md`, `coding_body_modules.md` and `fuel_system_fit.md`. I don't repeat those unless I correct or extend them.

**How each claim was read**

- **[read]**: I downloaded the page or PDF and read it as text: ETK pages on bmwfans.info (parsed from the HTML tables), BMW training PDFs, WDS schematics (text extracted from the SVG files), EPA spreadsheets, vendor pages.
- **[image]**: my reading of an ETK exploded drawing. It's an interpretation of a picture.
- **[snippet]**: seen only in a search-engine summary.
- **[earlier round]**: a fact in the guide's own documented-builds row, from a page an earlier round read that is now blocked (e46fanatics). Not re-read.
- **Inference** and **estimate** are labelled where they appear.

**Sources read, by block**

1. **ETK (bmwfans.info), a full comparison of the US 325xi Touring against the US 325i Touring** (both `L-N`, all build dates). About 300 catalogue pages in these groups: front axle, steering, engine and gearbox suspension, drive shaft, transfer box, manual gearbox, gearshift, rear axle, brakes, fuel supply, fuel preparation, exhaust, pedals, clutch, 12 bodywork subgroups, 11 vehicle-trim subgroups (insulation, underfloor, floor covering and others), the vehicle electrical groups (EWS, main harness), instruments, and programmed DMEs. Plus the matching US M3 coupe groups, 28 part-usage pages, a VIN decode, and eight exploded drawings (1le7, dnz4, 1nu0, 1v9j, 2egi, fey, 1kgn, 2qi9) [read], [image].
2. **BMW ST040 "E46 All-Wheel Drive System"** (initial print 10/03/2000) [read]: [PDF](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf).
3. **BMW ST056 "E46 Dynamic Stability Control Systems"** (01/2003), its Bosch DSC III 5.7 sections [read]: [PDF](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf).
4. **BMW ST406 "Vehicle Coding Information"** [read]: [PDF](https://archive.org/download/BMWTechnicalTrainingDocuments/ST406%20Coding%20%26%20Programming/06%20Vehicle%20Coding%20Information.pdf).
5. **WDS (wds.psjr.org): the E46 DSC 5.7 and MK60 schematics** (overviews SP0000017263 and SP0000017266; supply SP0000016593 and SP0000015072; steering-angle sensor SP0000016594, SP0000017308 and SP0000015078; CAN bus SP0000017172; MK60 wheel-speed SP0000015073 and SP0000015074; sensor cluster SP0000017311; pressure sensors SP0000015080 and SP0000015081; handbrake SP0000015085; DSC button SP0000015075; fluid level SP0000015086). Also the X18303 connector pages and the A65 location pages. Text was extracted from the SVGs [read].
6. **EPA certification data**: the light-duty "models archive (1999–2008)" and "test results report archive (1999–2008)" spreadsheets, which an earlier round downloaded from [EPA](https://www.epa.gov/compliance-and-fuel-economy-data/annual-certification-data-vehicles-engines-and-equipment). I read them with Python [read].
7. **Builds**: [Top Gear (21 Aug 2024)](https://www.topgear.com/car-news/used-cars/modified-bmw-e46-m3-touring-just-sold-nearly-60000) [read]; [vmax.si (Dec 2024)](https://en.vmax.si/2024/12/21/this-is-a-near-perfect-m3-and-it-was-for-sale/) [read]; [Engine Swap Depot (6 Jun 2023)](https://engineswapdepot.com/?p=101132) [read]; [Built for Backroads, 2004 325xi listing (Apr 2023)](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap) [read]; [German Cars For Sale Blog (19 Mar 2019)](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed), an AWD car [read].
8. **Coding**: [bmwfaq.org "Avería Pérdida FA/VO e46"](https://bmwfaq.org/threads/perdida-fa-vo-e46.1068598/) [read]; [ncsx data-format notes](https://github.com/emdzej/ncsx/blob/main/docs/daten-format.md) [read]; the [bmwfans VIN decoder](https://bmwfans.info/vin/) and [NHTSA vPIC](https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/WBAAW33421EN80596?format=json) on the 2001 325xi Touring VIN WBAAW33421EN80596 [read].
9. **Massachusetts**: 540 CMR 6.01–6.04 on LII ([6.03](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-6-03), [6.04](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-6-04)) [read].

**Blocked or not reached** (details at the end): e46fanatics (proof-of-work challenge), including JMCCRNA's thread and seven xi-to-RWD threads; bimmerfest (challenge); f30.bimmerpost (403); BMWBlog and Motor1 (403 to curl, DNS failure in the fetch tool); Cars & Bids and classic.com (Cloudflare); the Bring a Trailer listing itself (URL not found). web.archive.org was unusable: the proxy reset its connections and the availability API returned 429. Snapshots of Motor1 (2025) and the Cars & Bids auction (2023) exist but couldn't be downloaded. **WebSearch: 16 calls**, one of them rejected because it named a blocked domain.

---

## Takeaway: what an xi owner must do to go rear-drive

1. **The xi shell is not a 325i shell from the front seats forward, tunnel included.**
   - BMW lists the xi body as "a specially designed body pan with a widened transmission tunnel and modifications on the driver's side to accept the transfer case". It adds "a completely new front engine carrier", "re-reinforcements for the front strut bearings" and a "new transmission cross-member" ([BMW ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf)) [read].
   - ETK gives the xi its own front frame rails, inner (41007037635/636) and outer (41117029237/238), its own front wheelhouses (strut towers, 41007037637/638), its own anti-roll-bar body brackets (41117161089/032) and its own driver's seat console. The M3 uses the 325i's parts (41118234033/034, 41117029239/240, 41148234035/036, 41118239195/196) [read].
   - Behind the front seats the shell is common. That covers the rear-axle-carrier insert 41117000246, the rear wheelhouses, the trunk floor and partition, the tank, the fuel lines, the parking-brake cables and almost all the exhaust hangers [read]. So Phases 5–7 of the guide (floor, arches, rear axle, fuel) apply unchanged.
2. **Front axle: fit the donor's complete rear-drive front end.**
   - That means the subframe 31111096902, the M3 arms and their brackets (FCABs), struts, knuckles, rack, the lower steering joint, the anti-roll bar and the reinforcement plate.
   - **Will the subframe bolt in?** Probably. Three xi Tourings carry M3 or rear-drive front subframes, and none of the sources reports work at the subframe mounts: the BaT car, a 2004 xi from Buffalo NY, and JMCCRNA's 2003 xi.
   - It's not proven, though. The xi frame rails are different parts, and the xi subframe fastens differently (adaptors and M10 bolts at the rear, longer M12 screws at the front). **Trial-fit it before you commit** (Phase 0 gate below).
3. **Two fabrication jobs to expect.**
   - **Gearbox crossmember.** The xi's cast all-wheel-drive crossmember (22316750856) bolts to the xi tunnel. The M3's (22312229198) needs four M8 threads at the rear-drive positions. JMCCRNA needed a custom bracket, and it then clashed with a Euro exhaust [earlier round].
   - **Front anti-roll-bar brackets.** These are xi-specific body parts. The M3 bar's bushing brackets are made for the 325i/M3 body brackets, so check at mock-up and be ready to weld on the rear-drive brackets (about €8 each, list price).
4. **DSC: the whole MK60 system replaces the Bosch DSC 5.7.** That means:
   - an MK60, the donor's from 09/2002 or a 325i's from 09/2001
   - its CAN sensor cluster
   - four MK60 wheel-speed sensors
   - the MK60 master cylinder with two pressure sensors
   - the rear-drive reservoir and cap
   - the rear-drive/M3 brake pipes (the xi's unit and pipes are on the right; the MK60 sits on the left)
   - an adapter loom built signal by signal

   The xi's own DSC can't serve: its front sensors don't fit a rear-drive hub, and the rear-drive sensors aren't compatible with it ([BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf)) [read]. The Buffalo car kept its "Bosch 5.7 DSC from Xi" and lists that as a known flaw ([Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap)) [read].
5. **Coding.**
   - The xi's vehicle order carries an xi type key and option `$203` (all-wheel drive). Code the MK60 against a rear-drive Touring order: in that coding session only, remove `$203` and use a 325i Touring type key. Or set its values by hand.
   - Keep the stored order's body type a Touring.
   - Your own xi VIN goes into the MSS54, the cluster and the MK60 as usual.
6. **Emissions: an xi is the best case for Massachusetts.**
   - EPA certified every 2001–05 325xi Sport Wagon in an LEV test group (LER; for 2001 also M54). For 2004–05 that was California LEV and federal Bin 9, exactly as the S54 was.
   - A 2003–05 rear-drive 325i Touring may be ULEV or SULEV instead [read, EPA].
   - Once the car can't drive all four wheels, Massachusetts' four-wheel-drive height rules (540 CMR 6.00) no longer apply to it (our reading).
7. **Verdict: hard but feasible; a 325i is still simpler.**
   - **Parts:** our estimate is an extra \$0–\$1,500 with a donor built from 09/2002, which brings its own MK60, sensors, pipes and master cylinder. It's \$1,000–\$3,000 with an earlier donor. Selling the xi drivetrain recovers part of it.
   - **Time:** add 4–8 weekends (our estimate), mostly the DSC loom, the crossmember adapter and the front-end trial fit.
   - **Difficulty:** "DSC and brakes" goes from Moderate to Hard, and the front-axle transplant from Moderate to Moderate-to-hard.
   - **Recommendation:** if you haven't bought a car yet, a rear-drive 325i Touring is less work. If you're in Massachusetts and the 325i on offer is a 2003–05 ULEV car, though, an xi's LEV certificate is worth something.

---

## 1. Body: how an xi Touring shell differs from a rear-drive Touring shell

### Cited findings

**What BMW changed** ([BMW ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf), pp.3–11) [read]:
- "Changes from the standard drive version are: A specially designed body pan with a widened transmission tunnel and modifications on the driver's side to accept the transfer case. Modified oil pan and engine mounts to provide access for the front axles. A completely new front engine carrier. Re-reinforcements for the front strut bearings. A compact new transfer case (NV 124). New transmission cross-member. Bosch DSC III 5.7."
- Front axle carrier: "two square frame sections welded to two tubes to form a box structure… bolted to the vehicle frame at both the front and rear attachment points". The steel lower arms "attach at the rear to the axle carrier", and the ball joint at the arm's apex is "bolted to the axle carrier".
- "The struts are shorter than the 2wd and there are reinforcement plates between the strut bearing and the sheet metal of the strut towers"; spring travel is "approximately 20mm less".
- "The lower steering spindle is different than the 2wd and connects to the steering rack via a double cardan joint." The xi's turning circle is 35.8 ft, "1.4 ft greater than the 2wd".
- Cross-member: "the cast aluminum transmission cross-member is a low profile design… Both manual and automatic transmissions utilize the same part."
- "The complete rear axle and the rear differential are the same as the 2wd version of the 325i and 330i."
- The xi adds about 100 kg (220 lb) and "17mm ground clearance".

**ETK, front-end body parts** ([ETK xi front body parts](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/bodywork/front_body_parts/), [ETK 325i](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/front_body_parts/)) [read]. The usage pages give who uses each part [read].

| Body part | 325xi Touring | 325i Touring and M3 | Usage of the xi part |
|---|---|---|---|
| Front engine support (inner frame rail), L/R | 41007037635/636 | 41118234033/034 | 325xi, 330xi, 330xd only ([ETK](https://bmwfans.info/parts-catalog/41007037635/)); the rear-drive part covers every rear-drive E46, M3 and CSL included ([ETK](https://bmwfans.info/parts-catalog/41118234033/)) |
| Exterior engine support (outer rail), L/R | 41117029237/238 | 41117029239/240 | xi only ([ETK](https://bmwfans.info/parts-catalog/41117029237/)); rear-drive part on all rear-drive cars including M3 ([ETK](https://bmwfans.info/parts-catalog/41117029239/)) |
| Front wheelhouse (strut tower), L/R | 41007037637/638 | 41148234035/036 | xi only ([ETK](https://bmwfans.info/parts-catalog/41007037637/)); rear-drive part on M3 too ([ETK](https://bmwfans.info/parts-catalog/41148234035/)) |
| Front anti-roll-bar body bracket ("stabilizer support"), L/R | 41117161089/032 | 41118239195/196 | xi only ([ETK](https://bmwfans.info/parts-catalog/41117161089/)); rear-drive part on M3 too ([ETK](https://bmwfans.info/parts-catalog/41118239195/)) |
| Left front seat console | 41117037741 | 41118239493 | 325xi, 330xi, 330xd, 330d ([ETK](https://bmwfans.info/parts-catalog/41117037741/)) |
| Covering plate left (side frame) | 41117037743 | 41117037745 | — |
| Section of engine support, rear engine support, front-wall struts, engine-support reinforcement, front panel | Common | Common | Same part numbers on both cars |
| Body bracket for the ABS hydraulic unit (left) | 41148201492 | 41148201492 | Common to every E46, xi and M3 included ([ETK](https://bmwfans.info/parts-catalog/41148201492/)) |
| Strut-tower reinforcement plate (under the top mount) | 51717036781 with blind rivet | 51717036781 with blind rivet | Common ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/bodywork/front_body_bracket_left/)) |
| Rear-axle-carrier insert (RACP) | 41117000246 | 41117000246 | Common to 325xi, 325i and M3 ([ETK](https://bmwfans.info/parts-catalog/41117000246/)) |
| Rear wheelhouse/floor parts, trunk-floor mounting parts, trunk partition, side frames, splash wall | Common | Common | No differences in these ETK groups |

**Front subframe mounting.**
- The xi front axle support 31101096954 is used only on the 325xi, 330xi and 330xd ([ETK](https://bmwfans.info/parts-catalog/31101096954/)) [read]. It is held by:
  - two collar screws M12×1.5×140 (31101095617)
  - adaptors left and right (31106768293/294 from 12/2000; earlier 31101097117/118), fixed by four M10×50 12.9 bolts (07119902899)
  - two M12×1.5×50 bolts (07149112451) ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/front_axle/front_axle_support_4_wheel/)) [read]
- The rear-drive and M3 support 31111096902 is held by four M12×1.5×100 collar screws (31116781023) ([ETK 325i](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/front_axle_support_wishbone_2/), [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/front_axle_support_wishbone/)) [read].
- In ETK's drawing the xi's rear tube ends in a flat tab. The M12×1.5×50 bolt goes up through the tab into the adaptor, and the adaptor is bolted to the body with the M10 bolts ([drawing 1le7](https://ills.bmwfans.info/1le7.png)) [image]. The rear-drive subframe has four vertical collar-screw bosses ([drawing 1nu0](https://ills.bmwfans.info/1nu0.png)) [image].
- On the rear-drive car the arm's rear bracket (FCAB) bolts to the body with M10×35 10.9 screws (31106772199). The M3 lists 12 of these, the 325i 8, the difference being the reinforcement plate. The xi has no FCAB: its arm's rear mount and ball joint bolt to the subframe [read, ETK and ST040].
- Forum summaries conflict, and I couldn't read the threads (e46fanatics blocked):
  - "The body of the car is basically the same (mounting points for subframe, suspension, etc.)" against "The AWD FCAB attaches to subframe, while the RWD attaches to the chassis" ([e46fanatics: RWD vs AWD chassis differences (for swap purposes)](https://www.e46fanatics.com/threads/rwd-vs-awd-chassis-differences-for-swap-purposes.1108800/)) [snippet].
  - "Steering racks from all of the RWD cars won't fit because of the modifications done to the xi's front subframe" ([e46fanatics: XI vs RWD front suspension different?](https://www.e46fanatics.com/threads/xi-vs-rwd-front-supension-different.1302844/)) [snippet].
- **Builds that fitted a rear-drive or M3 front subframe to an xi body:**
  - **Buffalo NY, 2004 325xi Touring:** "E46 M3 Front / Rear Subframe", "converted to rear wheel drive" ([Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap)) [read]; "E46 M3 steering rack and rear subframe" ([Engine Swap Depot](https://engineswapdepot.com/?p=101132)) [read].
  - **BaT car, 2001 325xi:** "subframes" from the donor (guide's BMWBlog citation); "The six-speed manual transmission and axles come from the donor M3" ([vmax.si](https://en.vmax.si/2024/12/21/this-is-a-near-perfect-m3-and-it-was-for-sale/)) [read].
  - **JMCCRNA's 2003 xi:** "made rear-drive" [earlier round].
  - None of these sources mentions work on the front subframe mounts.

**Gearbox crossmember and tunnel.**
- **xi:** gearbox support 22316750856 (325xi/330xi/330xd only), transmission bearing set 22316773125, rubber buffer 22316788586, one M12×1.5×115 through-bolt, two M8×22 body bolts (22326760945) and two M8×60 body bolts (22316779982) ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/engine_and_gearbox_suspension/gearbox_suspension_4_wheel_drive/), [usage](https://bmwfans.info/parts-catalog/22316750856/)) [read].
  - The drawing shows an asymmetric cast beam. Its left end carries a cylindrical rubber bushing on a horizontal bolt, under the NV124's "hole for rubber mounting" (ST040) ([drawing 1kgn](https://ills.bmwfans.info/1kgn.png)) [image].
- **M3:** support 22312229198 (M3 and CSL only) with two mounts 22322282340 and four M8×22 body bolts (22326760945) ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine_and_gearbox_suspension/gearbox_mounting/)) [read].
- **325i:** support 22316769911 with four of the same M8×22 bolts [read].
- **JMCCRNA's 2003 xi Touring:** "the xi gearbox mount needed a custom bracket"; "Euro exhaust and the custom gearbox brace clashed" (guide's builds table, [e46fanatics](https://www.e46fanatics.com/threads/m3-touring-project.1240087/)) [earlier round].
- **Driveshaft centre mount:**
  - xi: 26121229317, which ETK also uses on rear-drive four-cylinder E46s ([ETK](https://bmwfans.info/parts-catalog/26121229317/)) [read].
  - 325i: aluminium mount 26127501257.
  - M3: 26122282495.
  - All three are fastened with two M8 flange nuts (26117574872) [read].

**Floor, heat shields and exhaust hangers** ([ETK vehicle trim](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/vehicle_trim/), [exhaust](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/exhaust_system/)) [read]:

| Part | 325xi Touring | 325i Touring |
|---|---|---|
| Tunnel heat insulator | 51488253953 (325xi and 330xi only, [ETK](https://bmwfans.info/parts-catalog/51488253953/)) | 51488193807 (not M3, [ETK](https://bmwfans.info/parts-catalog/51488193807/)) |
| Engine-compartment screening | Front 51718265977 and centre 51718265927 | 51718268344, plus heat plate 51717023073 |
| Tunnel exterior sound insulation | 51488266570 | 51488193827 |
| Underfloor panel, centre | 51718265985, bracket 51717042799 | Bracket 51718205875, engine-support trim panels 51718244305/51718218118, connecting support 18217039780 |
| Front and rear carpets | xi-specific (e.g. 51478265878) | 51478213974 and others |
| Exhaust suspension parts | Common, except xi bracket 18207502523 (to 09/2001) | Common, except bracket 18311728547 ("GETRAG") |
| Mufflers | Front 18107504169, centre 18107506018, rear 18107504172, and an exhaust-flap vacuum system | 18107504168, 18107504170, 18107504171/18107516921 |

**Fuel tank and lines** ([ETK fuel supply](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/fuel_supply/)) [read]:
- 57 of the xi's 59 fuel-supply part numbers are the 325i Touring's. That includes the tank, pump, senders, pipes, vent and EVAP parts.
- The xi adds a "protective plate for fuel tank" 16111183924 with three spring nuts. Rear-drive four-cylinder and diesel E46s use it too ([ETK](https://bmwfans.info/parts-catalog/16111183924/)).
- Under the floor, the filter-regulator group differs only in the **filter cover**: xi 13327500083 against 325i 13328230397. The bracket 13321435583, the screws and the cage nuts are common ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/fuel_preparation_system/fuel_filter_pressure_regulator/), [ETK 325i](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/fuel_preparation_system/fuel_filter_pressure_regulator/)).

**Parking brake.**
- The handbrake lever and the cables 34411165020/021 are common [read].
- The xi's shoes, springs and adjusters differ: 34416761292 against 325i 34416761291 ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/brakes/parking_brake_brake_shoes/)) [read].

**Rear axle carrier.**
- xi 33316770787 (also 320d, 330xi, 330xd) against 325i 33316770865 ([ETK](https://bmwfans.info/parts-catalog/33316770787/)) [read].
- The trailing arms (33326774779/780) and output flanges are xi-specific too, with larger bearings and flanges.
- The body insert the subframe bolts to is common (above).

**Brake lines, steering column and rack** [read]:
- **Brake pipes.**
  - The xi has its own front and rear runs, because its hydraulic unit sits on the right.
  - Its rear pipes share most pieces with the pre-09/2002 M3 (MK20, also on the right): 34326754861, 34326754950, 34326755684, 34326766825 and the 5-fold brackets ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/brakes/brake_pipe_rear_4_wheel/), [ETK M3 to 09/2002](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/rear_brake_pipe_dsc/)).
  - The 325i (MK60 from 09/2001) and the M3 from 09/2002 share the left-side set: front 34326759218, 34326755801, 34326752405, 34326752407; rear 34326752409, 34326755704, 34326766825 ([ETK M3 from 09/2002](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/rear_brake_pipe_dsc_2/)).
- **Steering column and steering-angle sensor.** The column (32303450159, manual) and the sensor 32306793632 are common to xi, 325i and M3 ([ETK](https://bmwfans.info/parts-catalog/32306793632/)).
- **Lower steering joint.** The xi has 32306750815 (to 11/2003) or 32306764009 (from 11/2003) plus a double joint 32306754165. The 325i and M3 have 32301094700 (to 11/2003) or 32306764006 (from 11/2003) plus flexible coupling 32301094703 ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/steer_col_lower_joint_assy/)).
- **Rack.** xi 32136759815, on two M10×60 screws; 325i 32136755065 from 09/2001, on M10×67 screws.

**Engine mounts.**
- The xi's engine supporting brackets (22116750853/852) and its mounts sit on the xi subframe ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/engine_and_gearbox_suspension/engine_suspension/)) [read].
- The M3 uses its own brackets (left 22112229898, right 22111094694) and mounts 11812283798 on the rear-drive subframe ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine_and_gearbox_suspension/engine_suspension/)) [read].
- No engine-mount bracket is part of the body.

**Strut towers.** The towers are different body parts, but the hardware is common: the top-mount kit (31352241445 to 11/2003, 31352241448 from 11/2003), the three M8 collar nuts (31316769731), the spring pocket, the pads and the reinforcement plate 51717036781 ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/front_axle/guide_support_spring_pad_attaching_parts/)) [read].

### Inferences (labelled)

- **The rear-drive subframe probably bolts in (inference).** Three xi Tourings carry one with no reported mount work, and BMW says the xi carrier bolts to "the vehicle frame at both the front and rear attachment points".
  - The xi's front collar screws use the same thread (M12×1.5) as the rear-drive ones, only longer.
  - The xi's rear adaptors use M10 bolts into the body, as the rear-drive FCAB brackets do. My reading is that the xi body keeps the rear-drive threads and uses some of them differently.
  - Not proven: ETK gives the xi frame rails their own numbers, and nobody has published a trial fit.
- **The anti-roll bar is the most likely front-end surprise (inference).** The M3 bar's bushing brackets 31351094552 clamp onto the body bracket's studs with M8 collar nuts. The xi has different body brackets (41117161089/032) for a bar routed round the front differential and axles. Plan to weld on 41118239195/196, at €7.85 and €7.81 list ([bmwfans](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/front_body_bracket_left/)), set from BMW's body dimensions or measured off the donor.
- **The strut tower should take M3 top mounts (inference from common hardware).** The tower panel number differs, perhaps for the right-side DSC unit's or the pre-charge pump's mountings. Whether the tower top sits at the same height isn't documented, so check ride height at mock-up.
- **Crossmember (inference).** The xi tunnel has threads where the xi's cast crossmember bolts, not necessarily where the M3's does. The 420G's mount also sits at a different station from the NV124's rubber mount. Hence JMCCRNA's bracket.
- **Driveshaft centre mount (inference).** It probably sits on the same tunnel studs: the xi's mount is a part rear-drive four-cylinder cars use, fastened the same way. Check that the M3 shaft's centre bearing lines up.
- **Heat shields and hangers (inference).** The M3 exhaust should have more room, not less, in the widened tunnel. The tunnel shields won't match the donor's, so fit and trim at Phase 10.

### Gaps

- **Subframe threads.** Whether all four rear-drive M12 subframe threads and the FCAB M10 threads exist on the xi rails. Settle it by trial-fitting a rear-drive subframe, or by measuring and thread-gauging on the car.
- **Anti-roll-bar brackets.** Whether the M3 bushing brackets bolt to the xi body brackets.
- **Crossmember positions.** The exact positions of the xi's and the M3's crossmember bolts. Measure the donor before stripping it (Phase 1 below).
- **Strut tower height.** Whether the xi tower top sits higher than a 325i's. Measure.
- **Exhaust.** Where JMCCRNA's exhaust clash was.

---

## 2. Parts to convert: what the xi gains and loses

### Cited findings

**What leaves the car** [read, ETK and ST040]:

| Item | Part numbers |
|---|---|
| NV124 transfer case, 38:62 split, 0.24 L MTF-LT-1 (ST040) | 27107509763 to 03/2003; 27107530812 from 03/2003 |
| Front driveshaft | 26207525969 (718 mm) to 03/2003; 26207525970 (723 mm) from 03/2003 |
| Front differential (VAG 174, bolted to the left of the oil pan) | 31507500797 (3.23, manual) or 31507526216 |
| Front output shafts | 31607505199 (605 mm), 31607505200 (926 mm; the right side, which BMW says runs through a tube in the oil pan) |
| xi front subframe and its fixings | 31101096954 with adaptors, ball joints 31126756695/696, arms 31126758533/534, brackets 31121139791/792 |
| Struts and carriers (knuckles) | Struts 31316751131/132 or 31316759647/648; carriers 31216756541/542 or 31216759311/312 |
| Rack and lower steering joint | 32136759815; 32306750815 or 32306764009 with 32306754165 |
| Anti-roll bars | Front 31351097261 (23.5 mm), rear 33556751267 (20 mm) |
| Gearbox, crossmember, rear driveshaft | S5D 320Z (e.g. 23007502658); 22316750856; 26117502959 (1,244 mm) |
| Rear axle | Carrier 33316770787, arms 33326774779/780, diff 33107500783 (3.23) or 33107531623 (3.46) |
| DSC 5.7 system | Hydraulic unit 34516762114 (right side, bracket 34516750966); pre-charge pump 34511166087 with bracket 34516751719; yaw/lateral sensor 34526753694; master cylinder 34316751442; reservoir 34326751589; xi brake pipes; wheel-speed sensors front 34526756382 and rear 34526756383 (xi-only parts, [ETK](https://bmwfans.info/parts-catalog/34526756382/)) |
| Separate RPA (flat-tyre warning) unit, where fitted | 36236753289 |
| M54 with its xi oil pan and engine brackets; MS43 xi DME | Goes with the engine swap |

**What comes in, and where it comes from:**
- **Front end:** the M3 front axle as the guide lists it (subframe, arms and brackets, struts, knuckles, hubs, rack and tie rods, reinforcement plate 51717893609, brakes), plus:
  - the M3 lower steering joint 32301094700 or 32306764006, with flexible coupling 32301094703
  - the M3 front anti-roll bar 31352229755 (26 mm) with bushing brackets 31351094552 and links 31356780847
  - possibly the rear-drive body brackets 41118239195/196 [read, ETK M3]
- **Driveline:**
  - the M3 gearbox support 22312229198 with mounts 22322282340, plus an adapter (fabricated)
  - the M3 driveshaft 26112229240 (1,404 mm, per the guide) with centre mount 26122282495
- **Engine mounts:** the M3 brackets and mounts (above).
- **DSC (section 3):** MK60, sensor cluster, sensors, master cylinder with pressure sensors, reservoir and cap, brake pipes, 47-pin plug housing 61136954574.
- **Fuel:** the donor's filter cover 13328230397 (the fuel notes add the M3 sealing element 13327830949), if the xi's 13327500083 doesn't fit the M3 filter-regulator.
- **Tunnel shields:** the donor's, or adapt the xi's.

**Builds show the same pattern.**
- Buffalo car: "E46 M3 Front / Rear Subframe", a 420G, an M3 3.64 diff and the M3 rack ([Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap), [Engine Swap Depot](https://engineswapdepot.com/?p=101132)) [read].
- BaT car: transmission, axles and subframes from the donor ([vmax.si](https://en.vmax.si/2024/12/21/this-is-a-near-perfect-m3-and-it-was-for-sale/)) [read]; the all-wheel-drive system "ditched for a rear-wheel drive configuration" ([Top Gear](https://www.topgear.com/car-news/used-cars/modified-bmw-e46-m3-touring-just-sold-nearly-60000)) [read].

**Weight.**
- BMW says the all-wheel-drive system adds 100 kg (220 lb) (ST040) [read].
- In EPA's test data the 325xi Sport Wagon (automatic) weighs 3,693 lb (1,675 kg) at the curb, against 3,494 lb (1,585 kg) for the 325i Sport Wagon (automatic, M56) [read, EPA test-results archive].

**List prices** (BMW list shown by bmwfans in EUR, October 2026) [read]:
- xi front subframe €784.75, rear-drive €356.70
- lower joint 32301094700 €125.95; flexible coupling €35.41
- M3 gearbox support €22.49; its mounts €14.48 each; M3 centre mount €84.77
- tunnel heat insulator 51488193807 €128.57

### Inferences (labelled)

- **The donor's front subframe replaces your own (inference).** In the guide's 325i plan the Touring's subframe stays; for an xi there's none to keep. The donor's subframe carries the M3's engine-mount pedestals, so crack-check it (M3 subframes crack, per the guide's BimmerWorld kit row) and treat it as the part you can't easily replace: a new one is €356.70 list.
- **Driveshaft length (inference).** The xi's longer gearbox-plus-transfer-case left a 1,244 mm rear shaft. The 420G with the M3 shaft (1,404 mm) gives an M3 layout, so the length should be right if the centre-bearing studs are where the rear-drive cars have them.
- **What to sell (estimate).** The xi's AWD parts (transfer case, front differential, axles, xi subframe, Bosch DSC unit) are wanted by xi owners. Selling them should recover a few hundred to perhaps \$1,500. No price source was read.

### Gaps

- Used-market prices for the xi parts you sell and for a used MK60 and sensor cluster.
- Whether the xi filter cover clears the M3 filter-regulator assembly.

---

## 3. DSC: replacing the Bosch DSC 5.7 with an MK60

### Cited findings

**Which units** ([BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf), pp.1–5) [read]:
- "Bosch DSC III 5.7 01- Present 330Xi, 325Xi"; "Teves MK 60 - Used from 01 production until present. (not used on iX and M3)".
- "The Bosch DSC III 5.7 is used in the E46/16 in place of the DSC III MK 60 used on 2wd vehicles. The DSC system is the same as used in the E53. HDC is not a feature on 2001 Xi models."

**Where they sit and what surrounds them** [read]:

| Component | Bosch DSC 5.7 (xi) | Teves MK60 (325i from 09/2001; M3 from 09/2002) | Source |
|---|---|---|---|
| Control and hydraulic unit | "in the engine compartment on the right hand side"; WDS: "in water box right"; 34516762114 on bracket 34516750966, the same bracket and rubber mounts as the pre-09/2002 M3's MK20 | "on the left side under the brake master cylinder"; 34516765453 (325i) or 34512282558 (M3) on bracket 34516752664. The left body bracket "Bracket ABS hydraulic unit" 41148201492 is listed for the xi body too; that the MK60 bracket bolts to it is our inference | ST056 pp.12–13; [WDS A65](https://wds.psjr.org/en/e46/zinfo/E46_EA65B.htm), [WDS A65 MK60](https://wds.psjr.org/en/e46/zinfo/E46_EA65D.htm); ETK |
| Connector X18303 | 42-pin, blue | 47-pin, black (housing 61136954574) | [WDS X18303 page](https://wds.psjr.org/en/e46/Component%20and%20signal%20information/Plug-in%2C%20comb-type%20and%20solder%20connectors/Connectors%20from%20X1.../X18303%20Adapter%20345240~-50%2C%20storage%20location%20M204~-N205) |
| Pre-charge pump | Below the master cylinder on the left; feeds 10–15 bar to the front circuit; 34511166087 | None ("no longer required") | ST056 p.15; ETK |
| Master cylinder | 34316751442, with a pre-charge inlet | 325i 34336785666; M3 34317838638; two pressure sensors 34521164458 on the cylinder | ST056 p.16; ETK |
| Brake-pressure sensors | One, on the hydraulic unit, front circuit (34511165467) | Two, on the master cylinder | ST056 pp.26–27 |
| Fluid reservoir | 34326751589, level switch in the tank, extra outlet for the pre-charge pump | 34326750798 with cap switch 34326752698 | ST056 p.16; ETK |
| Yaw/lateral sensor | Combined analogue sensor under the driver's seat (34526753694; label 0 265 005 215 / 34 52 1 165 292), 2.5 V reference | CAN "sensor cluster" 34526764018 on bracket 34526750817, "installed in the same position" | ST056 pp.6, 25; ETK |
| Wheel-speed sensors | Hall effect, two-wire, 8 V supply; front pulse wheel in the bearing seal; xi-only parts 34526756382 (front) and 34526756383 (rear) | Magnetoresistive, 12 V; current front 34526792896/897, rear 34526752683 | ST056 pp.17–21; ETK |
| DSC button | Turns off engine and yaw intervention only; ADB braking stays active | Short and long press functions | ST056 p.28 |

**Wheel-speed sensors, in BMW's words** (ST056 pp.17–18) [read]:
- "The color of the sensor connector is blue, just as the Magnetoresistive sensors of the Teves MK 60 used on 2wd vehicles. The front sensors of the 2wd and 4wd versions of E46 are physically different and will not fit in the wheel hub."
- "The rear sensors can be confused with the Teves MK 60 sensors and will fit in the rear axle of the 4wd car however they are not compatible with the Bosch system."
- So with M3 knuckles the xi's front sensors can't be used, and MK60 sensors can't work with the Bosch unit.
- The 2004 Buffalo xi that kept its Bosch unit lists "Still using Bosch 5.7 DSC from Xi" under known flaws ([Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap)) [read].

**Connector X18303 pin by pin: what WDS shows.**
- **DSC 5.7, 42-pin blue** ([supply SP0000016593](https://wds.psjr.org/en/e46/svg/SP0000016593.svg), [CAN SP0000017172](https://wds.psjr.org/en/e46/svg/SP0000017172.svg), [steering-angle sensor SP0000016594](https://wds.psjr.org/en/e46/svg/SP0000016594.svg)) [read]:
  - pin 2: terminal 30 via F35, 50 A (4.0 mm², red)
  - pin 6: terminal 30 via F53, 30 A (2.5 mm², red/green)
  - pin 23: `U_HR`, terminal 87 via F3 (20 A, 0.75 mm², red/white)
  - pin 11: diagnosis TxD
  - pins 1 and 5: ground to X170
  - pins 24 and 40: PT-CAN high and low
  - WDS gives no detailed SVGs for its other pins. The overview drawing names their signals: four two-wire wheel-speed sensors, a six-wire analogue sensor (`DRSM`, `AY`, `DRST`, `DRSU`, `DRSS`, `DRSR`), a three-wire pressure sensor, pre-charge pump `VLP+`/`VLP–`, `HDC` and `HDC_KL` from 09/2001, an `LCM` line, the handbrake, fluid level, button, brake-light switch and ABS lamp ([overview SP0000017263](https://wds.psjr.org/en/e46/svg/SP0000017263.svg)).
- **MK60, 47-pin black** ([supply SP0000015072](https://wds.psjr.org/en/e46/svg/SP0000015072.svg), [front sensors SP0000015073](https://wds.psjr.org/en/e46/svg/SP0000015073.svg), [rear sensors SP0000015074](https://wds.psjr.org/en/e46/svg/SP0000015074.svg), [sensor cluster SP0000017311](https://wds.psjr.org/en/e46/svg/SP0000017311.svg), [pressure sensor 1 SP0000015080](https://wds.psjr.org/en/e46/svg/SP0000015080.svg), [pressure sensor 2 SP0000015081](https://wds.psjr.org/en/e46/svg/SP0000015081.svg), [handbrake SP0000015085](https://wds.psjr.org/en/e46/svg/SP0000015085.svg), [button SP0000015075](https://wds.psjr.org/en/e46/svg/SP0000015075.svg), [fluid level SP0000015086](https://wds.psjr.org/en/e46/svg/SP0000015086.svg), [CAN SP0000017172](https://wds.psjr.org/en/e46/svg/SP0000017172.svg)) [read]. The full table is under Guide-ready below.
- **The trap: the CAN pins.** The CAN-bus drawing lists the three units side by side: "ABS/ASC unit" on X18303 pins 11/15, "ABS/DSC unit" (MK60) on 11/15, and "DSC all-wheel drive" on pins 24/40 (SP0000017172) [read]. On the MK60, pin 24 is the sensor cluster's ground and pin 6 its supply.
  - So moving the xi's wires into a 47-pin housing by pin number would put PT-CAN high on a ground pin and a 30 A battery feed on the sensor supply (inference from the tables).
  - One WDS page for the steering-angle sensor "with DSC MK60 as of 2001_09" also shows pins 24/40 (SP0000017308). The CAN-bus page and the pre-09/2001 sensor page (SP0000015078, pins 11/15) contradict it, so I treat SP0000017308 as a drawing error.
- **Steering-angle sensor X1658** [read], same pins on both systems:
  - pin 1: terminal 30 via F40, 5 A
  - pin 2: switched supply. On the xi that's `U_HR` from F3; on MK60 cars, terminal 15 via F33, 5 A.
  - pins 3/4: CAN
  - pin 5: ground
  - pin 6: TxD
- **Sensor cluster and yaw-sensor plug housing.** The MK60 sensor cluster's plug housing is the same 6-pole part (61138383300) as the xi's yaw-sensor plug housing ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/brakes/dsc_compressor_senors_mounting_parts/), [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/hydro_unit_dsc_fastening_sensors/)) [read]. The functions behind the pins differ: the cluster uses its pins 1, 2, 3 and 5 for CAN low, CAN high, supply and ground (SP0000017311).

**What the documented conversions did:**
- **JMCCRNA (2003 xi Touring):** "M3 DSC module; M3 wheel-speed sensors 'plugged right in'" (guide's builds table) [earlier round]. No wiring details.
- **BaT car (2001 325xi):** the donor was a 2001 M3, so it had an MK20, not an MK60 (inference from its year). Its DSC route isn't stated in anything I could read.
- **Buffalo car (2004 325xi):** kept the Bosch DSC 5.7, listed as a known flaw [read].
- No source publishes an xi-to-MK60 adapter harness or pin map. Forum threads titled "converting a XI to RWD" and "2001 330xi RWD conversion" exist but are blocked. A summary of one quotes a member: swapping in a rear-drive Bosch 5.7 from an E39 "will hopefully do it", and another replies that the E39 module is a different version, so it's "not plug-and-go" ([e46fanatics](https://www.e46fanatics.com/threads/xi-to-rwd-conversion.776142/)) [snippet].

### Inferences (labelled)

- **Use a donor built from 09/2002 (inference).** It brings everything left-side: the MK60, its bracket and mounts, the sensor cluster with its bracket, all four sensors, the master cylinder with both pressure sensors, reservoir and cap, every brake pipe front and rear, and, most usefully, its DSC harness branch. A 325i built from 09/2001 is the second source, using its master cylinder 34336785666 and your M3 front hoses.
- **The MK20 isn't a sensible fallback (inference).** A pre-09/2002 donor's MK20 sits on the right like the xi's unit (same bracket 34516750966, similar pipe run) [read, ETK]. But it uses inductive sensors with grey plugs, a 43-pin plug and its own charge pump, and its coding has no Touring body type (guide). Not recommended; nobody has documented it.
- **Build the adapter loom by signal, not by pin number (inference).** Cut the donor's DSC branch out long before you strip the donor: the 47-pin plug with every lead back to the next joint. Then join it to the xi harness at the battery feeds (two 30 A, per MK60 practice), terminal 15 (5 A), grounds, PT-CAN, button, handbrake, brake-light switch, ABS lamp, diagnosis line and the four wheel-speed leads. Use the donor's leads for the sensor cluster, both pressure sensors and the reservoir cap.
- **Fuse ratings (inference).** Fuse each MK60 battery feed at 30 A, as on the 325i (F56 and F61). The xi's 50 A F35 feed is rated for the Bosch unit.
- **What becomes redundant (inference from ST056 and WDS).** The xi's pre-charge-pump circuit, the HDC circuit, the analogue sensor leads and the separate RPA unit go dead. The MK60 from MY2002 "incorporates the RDW function" (ST056 p.12). Insulate and tie back the unused leads.
- **The steering-angle sensor stays (inference).** Same part and pinout. After the swap, calibrate it with the MK60's job (`DSC_MK60.PRG`, `lenkwinkel_dsc_abgleichen`, as the guide's manual says), not the xi's `test_lenkwinkel`.

### Gaps

- The DSC 5.7's full 42-pin pin table. WDS only gives the supply, CAN and diagnosis pins. Read the rest off the plug, or from ISTA wiring for your VIN.
- The MK60 pins for the brake-light switch, ABS lamp, diagnosis TxD and the conditioned wheel-speed outputs (not on the WDS pages read).
- How JMCCRNA's shop wired the M3 unit, and whether its lights went out.

---

## 4. Coding: the vehicle order, the type key and which modules care

### Cited findings

- **The xi is an option code.** "All-wheel drive will be an option (SA 203), available on E46 sedans and Sport Wagons beginning 2001M.Y." ([BMW ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/7%20E46%204wd%202010-24-00.pdf), p.3) [read].
- **And the type key says so too.** A Spanish owner's 330d Touring carried a wrong order, `E46_#0902&N6SW%0354|7526441|7789420*EV91 $203$205$210…`. "EV91 belongs to a 330xd sedan, which is why the rear lights didn't work properly"; the right key was EX91 ([bmwfaq.org](https://bmwfaq.org/threads/perdida-fa-vo-e46.1068598/)) [read, my translation]. His summary: the `*` code tells "the body (sedan, touring, coupé/cabrio or compact), the engine and the drive (rear or xDrive)", and "`$203` means the car is four-wheel drive, `$205` automatic" [read].
- **A 2001 US 325xi Touring VIN** (WBAAW33421EN80596) decodes at bmwfans as "BMW 325xi, E46 Touring, M54, USA, production date May 2001" ([bmwfans](https://bmwfans.info/vin/)) [read]. So its type key is AW33 (VIN characters 4–7) (inference from BMW's VIN layout).
  - NHTSA's decoder reads the same VIN as a 2001 "325i" wagon, "PASSENGER CAR", GVWR class 1, with no drive type ([vPIC](https://vpic.nhtsa.dot.gov/api/vehicles/DecodeVinValues/WBAAW33421EN80596?format=json)) [read].
- **BMW's coding structure** ([BMW ST406](https://archive.org/download/BMWTechnicalTrainingDocuments/ST406%20Coding%20%26%20Programming/06%20Vehicle%20Coding%20Information.pdf)) [read]:
  - The ZCS's GM segment holds "vehicle type… body style… country… unique equipment".
  - ZCS digits "should never be changed manually unless it is necessary for special recoding functions… the BMW Technical Hotline should be contacted… requesting a modified ZCS code".
  - The vehicle order's model code "indicates the vehicle and engine type plus… the country".
  - The E46 moved to the vehicle order at 09/2001 production.
- **What DIS does with an xi:** "The all-wheel drive models of the E46 series do not have their own model identification and all-wheel drive specific equipment (i.e. DSC III 5.7) is not detected automatically" (ST056 p.44) [read].
- **The MK60 rules key off order keywords:** `S54B32`, `TOUR`, `M54B25` and others, from liam821's dump, as `coding_powertrain_chassis.md` reports [earlier round].
- **The same move on a later car.** An F30 335xi converted to a rear-drive manual "FA coded all of the modules to type key 3A93 (RWD) and deleted the $205" ([f30.bimmerpost](https://f30.bimmerpost.com/forums/showthread.php?p=32755911)) [snippet; not an E46].
- **Modules that are the same hardware on xi and 325i Touring** (ETK) [read]: the instrument cluster (all 8 instrument parts common), the EWS, the steering-angle sensor and the booster. The main wiring harness is xi-specific in every period, for example xi 61116920910 against 325i 61116920909 (09/2001–03/2002).
- **DME.** The xi Touring lists MS43 units only (latest 12147571604, "from Jul '02"), with no MS45.1 group. It lists only the MS43-era air-mass meter 13621432356; the 325i also lists 13627566984 from 03/2003 ([ETK xi](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/engine_electrical_system/programmed_dme_control_unit/), [ETK 325i HFM](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/fuel_preparation_system/hot_film_air_mass_meter/)) [read].

### Inferences (labelled)

- **DSC.** An MK60 coded from an order that says xi type plus `$203` may be refused ("not allowed for this coding job") or get 325i Touring values. MK60 rules were never written for an xi. Code it in a session with a virtual order that has `$203` deleted and a 325i Touring type key of the same market and era, without `FA_WRITE`. Or code it from the donor's file and set `BAUART_MK60` = `touring` and the M3 values by hand in NCS Dummy, as the guide's Option B describes.
- **Cluster.** No sign that it codes anything from `$203`. The hardware is common, and the M3 cluster gets your order as the guide already plans. Keep the xi order.
- **DME.** The MSS54 isn't coded from the order (guide, SGBD documentation), so `$203` doesn't matter to it.
  - **Can the xi VIN stay in the MSS54?** Yes. The vendor writes your 17-character xi VIN with the EWS delete, as for a 325i; nothing in the MSS54 checks the VIN against the model.
- **Light module and GM5.** They code from the type key's body, as the bmwfaq case shows. An xi Touring and a 325i Touring are both Touring, so writing a 325i Touring type key permanently should be safe for the lights. Do it only if the MK60 won't code otherwise; then recode every module and check the rear lights and tailgate.
- **EWS.** Same part, and no all-wheel-drive role found. Nothing changes beyond the guide's EWS plan.
- **Pre-09/2001 xi Tourings.** They carry a ZCS (GM/SA/VN) instead of an order. ST406 says a modified ZCS should come from BMW, and the MK60 from 09/2001 expects an order-era car. That is the hard case the guide's coding notes already describe (convert the car to an order with a later LCM), so prefer an xi built from 09/2001.

### Gaps

- The US 325i Touring's and 325xi Touring's type keys for 2002–05. Read your own order's `*` field; a dealer or ISTA can give the 325i equivalent.
- Whether NCS refuses an MK60 against an xi order. Untested anywhere I could read.
- Whether `$203` changes any cluster or LCM coding value.

---

## 5. Emissions and legal

### Cited findings

**EPA test groups for the US 325xi Sport Wagon** [read, EPA models archive and test-results archive (1999–2008), from the [EPA certification data page](https://www.epa.gov/compliance-and-fuel-economy-data/annual-certification-data-vehicles-engines-and-equipment)]:

| Model year | 325xi Sport Wagon test group | Certified level | Sales area (test data) | M3 (S54), same year |
|---|---|---|---|---|
| 2001 | 1BMXV02.5M54 and 1BMXV03.0LER | LEV | "Clean fuel veh + NLEV (ASTR) + CA" | 1BMXV03.2S54, LEV |
| 2002 | 2BMXV03.0LER | LEV | same | 2BMXV03.2S54, LEV |
| 2003 | 3BMXV03.0LER | LEV | California; NLEV all states; clean-fuel | 3BMXV03.2S54, LEV |
| 2004 | 4BMXV03.0LER | LEV (California), Bin 9 (federal) | California; federal all altitude | 4BMXV03.2S54, LEV and Bin 9 |
| 2005 | 5BMXV03.0LER | LEV (California), Bin 9 (federal) | same | 5BMXV03.2S54, LEV and Bin 9 |

- In every one of those years, the LER group's represented test vehicle was the 325xi Sport Wagon itself (automatic, curb 3,693 lb, GVWR 4,729 lb, axle 3.46) [read].
- The rear-drive 325i Sport Wagon was in LER (LEV) only up to 2003. It was also in UL2 (LEV-II ULEV) and M56 (SULEV) for 2003, and in UL2, SMG (ULEV) and M56 for 2004–05. The 2004–05 LER groups list only the 325xi, 325xi Sport Wagon and 330xi [read].
- Certificate numbers for the 2001–03 groups read "120LDV…" (light-duty vehicle), for 2004–05 "120INT…". NHTSA classes the xi wagon as a passenger car, GVWR class 1 [read].

**Massachusetts four-wheel-drive rule** [read]:
- 540 CMR 6.00 "regulate[s] alterations to the height of four wheel drive vehicles". It defines them as "Any vehicle that is capable of providing torque to all four wheels" ([6.02](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-6-02), [6.03](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-6-03)).
- It covers raising or lowering "more than two inches above or below the original manufacturer's height" ([6.01](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-6-01)).
- It bans wheel spacers and limits a track increase by tyres and rims to four inches ([6.04](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-6-04)).

### Inferences (labelled)

- **The "same certification category" test.** An xi passes it for every model year. LEV car, LEV engine; for 2004–05, both California LEV and federal Bin 9; same vehicle class (light-duty vehicle).
  - That's better than the guide's 325i case, where a 2003 car in UL2 or any 2004–05 Touring would drop from ULEV to LEV.
  - EPA's "same or newer model year" test still applies: a 2004 xi wants a 2004–06 donor, a 2005 xi a 2005–06 donor.
- **The VECI label.** It should name an LER test group (for example "3BMXV03.0LER"). If it doesn't, go by the label.
- **540 CMR 6.00 and the xi.** A stock xi is a "four wheel drive motor vehicle" under it. Lowered by more than two inches, or on spacers, it would fall foul of 6.00 while still all-wheel drive. Once converted it can't send torque to all four wheels, so 6.00 no longer applies (our reading; put it in the letter to the RMV).
- **Drive layout and the title.**
  - No rule found ties emissions certification or the title to the drive layout.
  - Massachusetts titles record cylinders, transmission type, fuel, colour and odometer (guide), not drive.
  - The VIN will still decode as a 325xi at BMW-data decoders, and as a "325i" wagon at NHTSA. Tell your insurer the car is now rear-drive, and keep the conversion receipts with the build file.

### Gaps

- MassDEP's view of a drive-layout change under 310 CMR 60.02(12)(d). No source; add it to the guide's questions for MassDEP.
- What a 2001–05 xi VECI label prints (photograph yours).

---

## 6. Documented xi-to-rear-drive conversions

| Build | Base | What was done | What went wrong | Time, cost and sale | Sources |
|---|---|---|---|---|---|
| JMCCRNA (e46fanatics), 2018 | 2003 xi Touring, blown engine | Made rear-drive; M3 DSC module; M3 wheel-speed sensors "plugged right in" | The xi gearbox mount needed a custom bracket; Euro exhaust and the custom brace clashed | Started 10/2018; to paint 11/2018 | [earlier round], [e46fanatics](https://www.e46fanatics.com/threads/m3-touring-project.1240087/) |
| BaT car, Laguna Hills, California | 2001 325xi Sport Wagon | Donor 2001 M3: rebuilt S54 with CSL-style carbon airbox, six-speed, axles, subframes, diff. Bilstein PSS10 coilovers, H&R anti-roll bars, poly bushings, "track plates", carbon strut brace. Genuine M3 bonnet, sills, skirts, mirrors, fenders. Porsche 996 brakes. Kassel tune [snippet] | DSC route not stated; the donor's year means an MK20 (inference) | Top Gear: "just sold for nearly \$60,000" (21 Aug 2024). vmax.si quotes a mid-auction high bid "just over 35,000 dollars". An aggregator shows "highest bid \$59,250… Not Sold", 20 Aug 2024 [snippet] | [Top Gear](https://www.topgear.com/car-news/used-cars/modified-bmw-e46-m3-touring-just-sold-nearly-60000), [vmax.si](https://en.vmax.si/2024/12/21/this-is-a-near-perfect-m3-and-it-was-for-sale/), [classic.com](https://www.classic.com/m/bmw/3-series/e46/325xi/year-2001) [snippet] |
| Buffalo NY | 2004 325xi Touring, Jet Black; 200,000 mi chassis, S54 at 116k | "Converted to rear wheel drive to reduce weight"; S54 from a 2003 M3; 420G with Sachs clutch and lightweight flywheel; M3 3.64 diff; "E46 M3 Front / Rear Subframe"; M3 rack; Fortune Auto 500 coilovers; AKG bushings; 996 Brembo brakes; CSL headers; MSS54HP DME upgrade | "Still using Bosch 5.7 DSC from Xi"; selector-shaft seal leaking | Listed at \$24,000 on Built for Backroads (04/2023, "Sold"); sold for \$22,000 on Cars & Bids (Engine Swap Depot, 06/2023) | [Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap), [Engine Swap Depot](https://engineswapdepot.com/?p=101132) |

Forum threads on xi-to-rear-drive conversions exist but couldn't be read: "converting a XI to RWD" (1284904), "XI to RWD conversion?" (776142, five or more pages), "2001 330xi RWD conversion" (1042163), "XI RWD conversion" (1319419) and "Coding 330xd automatic to RWD manual conversion" (1314623). One summary gives the core list: "a new oil pan, rwd front subframe, all the front suspension parts, transmission and drive shaft all from the rwd vehicle" ([e46fanatics](https://www.e46fanatics.com/threads/converting-a-xi-to-rwd.1284904/)) [snippet].

---

## 7. Cost and time compared with the guide's rear-drive plan (estimates)

| Item | 325i Touring (guide's plan) | 325xi Touring, donor from 09/2002 | 325xi Touring, donor before 09/2002 |
|---|---|---|---|
| Front subframe | Keep yours | Donor's (\$0); new €356.70 list | Same |
| Lower steering joint and coupling | Keep yours | Donor's (\$0); new €125.95 + €35.41 list | Same |
| Anti-roll-bar body brackets | — | 41118239195/196, €7.85/€7.81 list, plus welding, if needed | Same |
| Gearbox crossmember adapter | — | \$50–\$300 in steel and hardware, or \$300–\$800 at a fabricator (estimate) | Same |
| MK60, sensor cluster, sensors, master cylinder and sensors, reservoir and cap, brake pipes | Keep yours | All from the donor (\$0) | A used 325i MK60 and cluster, or new parts: sensor cluster €360.48, four sensors €84.69 and €91.46 each, master cylinder €328.81, pressure sensors €93.64 each, reservoir and cap €79.02, six pipes about €120 (list). Our estimate \$800–\$2,500 depending on used or new |
| DSC adapter loom | — | \$50–\$150 in terminals, wire and a 47-pin housing (€5.29 list) (estimate) | Same |
| Tunnel heat shields | — | Donor's, or adapt the xi's (\$0–\$150) | Same |
| Sell the xi drivetrain and DSC | — | Recover perhaps \$300–\$1,500 (estimate) | Same |
| **Net extra parts** | — | **About \$0–\$1,500** | **About \$1,000–\$3,000** |
| **Extra time** | — | **4–8 weekends**: front-end trial fit and transplant (1–2), crossmember adapter (1–2), anti-roll-bar brackets (0–1), DSC hardware and pipes (1–2), loom and coding (1–2) | Same, plus sourcing |

Against the guide's \$27k–\$75k total and roughly two years, an xi adds a few per cent in money and perhaps 10–15% in time (our estimate). The risk is concentrated in two undocumented jobs, the DSC loom and coding, and the crossmember adapter.

---

## Guide-ready

### Parts table: 325xi Touring, 325i Touring and M3

| Item | 325xi Touring (yours) | 325i Touring (rear-drive) | US M3 (donor) | Action for an xi |
|---|---|---|---|---|
| Front axle support | 31101096954, adaptors 31106768293/294, screws 31101095617 ×2, 07149112451 ×2, 07119902899 ×4 | 31111096902, collar screws 31116781023 ×4 | 31111096902, 31116781023 ×4, plate 51717893609 | Donor's, trial-fit first |
| Lower arms; rear brackets | 31126758533/534; ball joints 31126756695/696; brackets 31121139791/792 on the subframe | 31122282121/122; 31126783376 to body | 31122229453/454; 31122229623/624 to body (M10×35 31106772199) | Donor's |
| Struts; knuckles | 31316751131/132 (to 03/2002), 31316759647/648; carriers 31216756541/542 or 31216759311/312 | 31316750789/790 and others; king pins 31211096429/430 | M3 (see guide) | Donor's |
| Top-mount hardware | 31352241445/448, nuts 31316769731, plate 51717036781 | Common | Common | Keep or renew |
| Front anti-roll bar; bushing brackets; links | 31351097261 (23.5 mm); 31356754336; 31356751079/080 | 31351097178 (23 mm); 31351094552; 31356780847 | 31352229755 (26 mm); 31351094552; 31356780847 | Donor's |
| Anti-roll-bar body brackets | 41117161089/032 | 41118239195/196 | 41118239195/196 | Check; weld rear-drive brackets if needed |
| Rack | 32136759815 | 32136755065 (from 09/2001) | 32132229397 (32132282642 ZCP) | Donor's |
| Lower steering joint | 32306750815 (to 11/2003) or 32306764009, plus 32306754165 | 32301094700 (to 11/2003) or 32306764006, plus coupling 32301094703 | Same as 325i | Donor's |
| Steering column; steering-angle sensor | 32303450159; 32306793632 | Common | Common | Keep; recalibrate |
| Gearbox crossmember | 22316750856, bearing 22316773125, buffer 22316788586, M8×22 ×2 and M8×60 ×2 | 22316769911, adapter 22316760532, mounts 22316799331 ×2, M8×22 ×4 | 22312229198, mounts 22322282340 ×2, M8×22 22326760945 ×4 | Donor's on a fabricated adapter |
| Transfer case; front driveshaft; front diff; front shafts | 27107509763/27107530812; 26207525969/970; 31507500797 or 31507526216; 31607505199/200 | — | — | Remove and sell |
| Rear driveshaft; centre mount | 26117502959 (1,244 mm); 26121229317 | 26111229557 (1,585 mm); 26127501257 | 26112229240 (1,404 mm); 26122282495 | Donor's |
| Rear axle carrier (body insert) | 33316770787 (41117000246) | 33316770865 (41117000246) | 33312282490 (41117000246) | Donor's; same body points |
| Parking-brake cables; lever | 34411165020/021; common | Common | (guide: fit M3 arms) | Keep |
| DSC hydraulic unit; bracket | 34516762114 (Bosch 5.7, right); 34516750966 | 34516765453 (MK60 from 09/2001); 34516752664 on body bracket 41148201492 | 34512282558 (from 09/2002); 34516752664 | MK60 on the left |
| Pre-charge pump | 34511166087, bracket 34516751719 | — | — (MK20 cars have a charge pump) | Remove |
| Yaw/lateral sensor | 34526753694 on 34511166016 | 34526764018 on 34526750817 | Same as 325i | Fit the sensor cluster |
| Master cylinder; pressure sensors | 34316751442; one sensor on the unit (34511165467) | 34336785666; 34521164458 ×2 | 34317838638; 34521164458 ×2 | Donor's or 325i's |
| Reservoir | 34326751589 (switch in tank) | 34326750798, cap 34326752698 | Same as 325i | Donor's |
| Booster | 34336779682 | 34336779682 | 34332282622 (from 09/2002) | Keep yours, or the M3's with its master cylinder (see guide) |
| Front brake pipes | 34326754837, 34326761171, 34326754840, 34326761169, 34326754847, 34326754849; pre-charge hose 34536754892 | 34326759218, 34326755801, 34326752405, 34326752407 | Same as 325i from 09/2002 | Donor's |
| Rear brake pipes | 34326754853, 34326754861, 34326754950, 34326755684, 34326766825 | 34326752409, 34326755704, 34326766825 | Same as 325i from 09/2002 | Donor's (34326766825 is common) |
| Front brake hoses | 34306752400 | 34326766966 | 34322229723 | M3 new (guide) |
| Wheel-speed sensors | Front 34526756382 ×2, rear 34526756383 ×2 (Bosch Hall) | Front 34526792896/897, rear 34526752683 (from 09/2001) | Same from 09/2002 | Donor's or new |
| DSC plug X18303 | 42-pin, blue | 47-pin, black, housing 61136954574 | Same as 325i | Donor's branch |
| Fuel filter cover | 13327500083 | 13328230397 | 13328230397 (plus seal 13327830949, fuel notes) | Donor's |
| Tank, pump, senders, lines, EVAP | Same as 325i (plus plate 16111183924) | — | (see fuel notes) | Guide's fuel plan applies |
| Tunnel heat insulator | 51488253953 | 51488193807 | M3 shields (guide) | Fit and trim |
| Clutch hard line | 21526753015, support 21526774229 | 21526774230, 21526774227 | 21522229675, bracket 21522229699 | Donor's (guide); check the route on the xi tunnel |

### Changes against the guide's phases

**Phase 0, paperwork and baseline**
- Decode the VIN at bmwfans: it should say "325xi", as 2001 xi VIN WBAAW33421EN80596 does.
- Save the vehicle order. Note the `*` type key and `$203`.
- Note the build month. Before 09/2001 means a ZCS: plan the order conversion or choose another car.
- Photograph the VECI label. It should name an LER group, which means LEV, the best emissions case.
- Photograph from below the xi crossmember and its four bolts, the tunnel, the anti-roll-bar brackets and the right-side DSC unit with its blue plug.
- **Gate: buy a donor built from 09/2002**, and for EPA's model-year test, of the same model year as your xi or newer.

**Phase 1, donor**
- Before teardown, record the donor's MK60 coding file and its order.
- Measure where the donor's gearbox crossmember bolts sit relative to the driveshaft centre-bearing studs and the front subframe's rear screws. That gives you the template for the adapter.
- Measure where the anti-roll-bar body brackets sit relative to the front subframe screws.

**Phase 2, strip the donor.** In addition to the guide's list, take:
- the complete front subframe with all its fixings and the FCAB screws
- the lower steering joint and coupling
- the front anti-roll bar with its bushing brackets. Consider cutting the donor's body brackets out with margin, as templates or as parts.
- the whole MK60 system: unit, bracket and mounts, sensor cluster and bracket, master cylinder with both pressure sensors, reservoir and cap, every brake pipe and clip front and rear, and all four wheel-speed sensors
- **the DSC harness branch, cut long and labelled at both ends**
- the tunnel heat shields and the fuel filter cover

**Phase 3, bench**
- Build the DSC adapter loom on the bench from both WDS sets (table below). Check every lead end to end.
- Sell the xi drivetrain parts.

**Phase 4, strip your Touring.** Also remove:
- the front axle complete (subframe with differential, shafts, rack)
- the transfer case and front driveshaft, the gearbox with its cast crossmember, and the rear driveshaft
- the Bosch unit with its bracket, the pre-charge pump, the yaw sensor, the master cylinder and reservoir, and all brake pipes

Keep the booster, the steering column and the steering-angle sensor. Chase or gauge the subframe and FCAB threads; don't recut good threads.

**Phase 5, metalwork 1.** Add:
- **front-end trial fit:** donor subframe, FCAB brackets and reinforcement plate on loose screws; anti-roll bar on its brackets
- anti-roll-bar body brackets, if they're needed
- the gearbox crossmember adapter, or weld nuts at the rear-drive positions
- measure the front-subframe diagonals before and after, as the guide does for the rear. The xi rails are their own parts.

**Phase 6, arches.** Unchanged: the rear quarters are the same part.

**Phase 7, rear axle and fuel.** Unchanged. The body points, tank, lines and parking-brake cables are common. Fit the donor's fuel filter cover if the xi's doesn't clear the M3 filter-regulator.

**Phase 8, front suspension and steering.**
- Fit the donor's front axle as the guide describes (subframe 110 Nm; FCAB 59 Nm; plate 59 Nm + 90°; steering-coupler Torx 22 Nm; all guide values).
- Brakes are Option B only: MK60 on the left, M3 master cylinder or 325i master cylinder with both pressure sensors, reservoir and cap, the donor's pipes, and new M3 front hoses.
- Air-test, fill and bleed with INPA's routine.

**Phase 9, engine and gearbox.**
- M3 crossmember on the adapter, M8 bolts at 21 Nm (guide).
- Driveshaft: the centre-bearing bolts start by hand with the shaft fully home; preload 4–6 mm forward (guide).
- Check the clutch line's route along the xi tunnel.

**Phase 10, exhaust.** Hang the M3 exhaust: the hanger parts are the 325i Touring's in ETK. Check clearance at the crossmember adapter, where JMCCRNA's clashed, and fit and trim the tunnel shields.

**Phase 11, wiring and coding.**
- Fit the DSC adapter loom (by signal; CAN to pins 11/15). Insulate the dead xi circuits.
- Code the MK60 with a session order without `$203` and with a 325i Touring type key, or by hand.
- Write your VIN to the MK60; initialise and calibrate. RPA coding is up to you.

**Phase 12, first start and shakedown.** Use the DSC checks below.

**Phase 13, paperwork.**
- The xi is LEV: same category as the S54.
- Note that 540 CMR 6.00 no longer applies to a rear-drive car (our reading).
- Tell your insurer; keep the receipts.

### DSC adapter-loom table: MK60 47-pin X18303, with what the xi provides

Source: WDS drawings named in section 3 [read]. "Move" means use the xi's existing lead, re-terminated by signal (inference).

| MK60 pin | Signal | MK60 wire (WDS) | xi source | Action |
|---|---|---|---|---|
| 1 | Terminal 30, F61 30 A | 2.5 RT/GE | xi pin 2 feed (F35, 50 A, 4.0 RT) or pin 6 (F53, 30 A) | Use a 30 A fused feed per pin (inference) |
| 32 | Terminal 30, F56 30 A | 2.5 RT/BL | The other xi feed | As above |
| 4 | Terminal 15, F33 5 A | 0.5 GN/BL/GE | xi pin 23 is `U_HR` (terminal 87, F3 20 A) | New terminal-15 feed from F33, or re-fuse at 5 A (inference) |
| 16, 47 | Ground to X170 | 2.5 BR | xi pins 1 and 5 | Move |
| 11, 15 | PT-CAN high, low | (twisted pair) | xi pins 24, 40 | **Move to 11/15. Never leave them on 24/40** |
| 6, 24, 29, 25 | Sensor-cluster supply, ground, CAN2-H, CAN2-L | SW/RT/WS, BL/WS/GE, GE, BL/GE (cluster plug X61035 pins 3, 5, 2, 1) | xi analogue yaw-sensor leads (6 wires, same 6-pole housing) | Donor's leads, or rewire by signal |
| 22, 23, 21 | Pressure sensor 1 supply, signal, ground | BL/SW/GE, SW/VI/GE, WS/BL/GE (X1747) | xi sensor on the unit (3 wires) | Donor's leads to the master cylinder |
| 18, 20, 19 | Pressure sensor 2 supply, signal, ground | BL/SW, SW/VI, WS/BL (X1748) | none | Donor's leads |
| 46, 45 | Front left wheel speed `DFVL`, `DFVL+` | BR, BR/RT | xi front-left lead (blue plug) | Move |
| 33, 34 | Front right `DFVR`, `DFVR+` | BR, GE | xi front-right lead | Move |
| 37, 36 | Rear left `DFHL`, `DFHL+` | BR, BL | xi rear-left lead | Move |
| 42, 43 | Rear right `DFHR`, `DFHR+` | GE/BR, GE/SW | xi rear-right lead | Move |
| 9 | Brake-fluid level `BRFN` (also cluster X11175 pin 20) | 0.35 BR/GN/GE | xi tank-switch lead | Donor's cap-switch lead |
| 27 | Handbrake `FSB` (also cluster X11175 pin 23) | 0.5 BL/BR/GE | xi lead | Move |
| 39 | DSC button `S_ASCPAS` | 0.5 BL/VI | xi lead | Move |
| not found | Brake-light switch, ABS lamp, diagnosis TxD, conditioned wheel-speed outputs | — | xi leads (TxD on xi pin 11) | Read the pins off the donor's plug |
| — | Pre-charge pump, HDC, LCM line | — | xi only | Insulate and tie back |

### Checks with pass values

| Check | Pass | If it fails |
|---|---|---|
| VIN and order (Phase 0) | bmwfans decode reads 325xi; order shows the xi `*` type key and `$203`; build month recorded | Before 09/2001 (ZCS): plan the order conversion first |
| VECI label (Phase 0) | Test group …LER (LEV) | Different group: go by the label |
| Subframe trial fit (Phase 5) | All four M12×1.5 collar screws (31116781023) start by hand and run to full depth; rear dowels engage; no gap at any mount face before torque (our check) | Stop. Measure against BMW's body dimensions; get a body shop |
| FCAB and plate threads | M10×35 screws (31106772199) start by hand at every bracket and plate hole (our check) | Thread inserts only where BMW's dimensions confirm the position |
| Anti-roll bar | Both bushing brackets seat on studs on each side; the bar clears the pan, rack and lines through full lock and full bump (our check) | Weld on 41118239195/196 at the rear-drive position |
| Crossmember (Phase 9) | 420G mounts sit square; four M8 bolts at 21 Nm (guide); centre-bearing bolts start by hand with the shaft home; preload 4–6 mm forward (guide) | Rework the adapter before the driveshaft goes in |
| Exhaust | No contact with the crossmember adapter or tunnel with the engine rocked by hand (our check) | Re-hang or trim |
| Brake pipes | Air test at about 20 psi holds (guide); no weeps after bleeding | Re-make the union |
| DSC identification | INPA identifies the MK60; fault memory clear after the compensation routines | Re-check CAN pins 11/15 and the terminal-15 feed |
| Pressure sensors | About 0 bar with the pedal released; the brake-light switch changes state before either sensor reads 5 bar ("must not detect more than 5 bar when the BLS is not actuated", ST056) | Swap leads 1 and 2; check the supply |
| Steering-angle sensor | Reads 0 with the wheel straight after calibration; 2–3° means not calibrated (guide) | Recalibrate after the alignment |
| Wheel speeds | All four the same while rolling straight at a steady 20 km/h (12 mph), within about 1 km/h (our check) | Swapped sensor leads, or an xi Hall sensor left in |
| Lamps | ABS, DSC and yellow BRAKE lamps out after the self-test; red BRAKE lamp off with the handbrake down and the reservoir full (ST056 colours) | Read the faults; check `BRFN` and `FSB` |

---

## Diagram-ready data

**Figure A, "What's different on an xi shell"** (underside plan; front of car at the left):

| Zone | Where | xi | Rear-drive and M3 | Status |
|---|---|---|---|---|
| A1 | Front frame rails, inner and outer | 41007037635/636, 41117029237/238 | 41118234033/034, 41117029239/240 | Different parts; subframe threads probably present (unproven) |
| A2 | Strut towers | 41007037637/638 | 41148234035/036 | Different panels; top-mount hardware common |
| A3 | Front anti-roll-bar body brackets | 41117161089/032 | 41118239195/196 | Different; check, possibly weld |
| A4 | Front subframe mounts | 2 × M12×1.5×140 front; adaptors with 4 × M10×50 and 2 × M12×1.5×50 rear | 4 × M12×1.5×100 | Trial-fit gate |
| A5 | DSC unit | Right, "water box" (bracket 34516750966) | Left under the master cylinder (34516752664 on 41148201492) | Body bracket for the left position exists on the xi |
| A6 | Tunnel and crossmember | Widened tunnel; cast crossmember 22316750856 | 22312229198 at rear-drive positions | Adapter needed (JMCCRNA) |
| A7 | Driver's seat console and sensor | 41117037741; yaw sensor under the seat | 41118239493; sensor cluster in "the same position" | Check the bracket holes |
| A8 | Fuel filter cover | 13327500083 | 13328230397 | Bracket common |
| A9 | Tunnel heat shield | 51488253953 | 51488193807 | Fit and trim |
| A10 | Rear floor, RACP, trunk floor, tank, lines, parking-brake cables, exhaust hangers | Common | Common | Guide's plan applies |

**Figure B, "Drivetrain before and after":**
- **Before:** M54 with the xi oil pan and its axle tube → S5D 320Z → NV124 transfer case (38:62) → front driveshaft (718 or 723 mm) to the front differential on the left of the oil pan, then shafts of 605 and 926 mm; rear driveshaft (1,244 mm, centre mount 26121229317) to the rear differential (3.23 manual, 3.46 automatic).
- **After:** S54 → 420G on the M3 crossmember (on an adapter) → M3 driveshaft (1,404 mm, centre mount 26122282495) → M3 differential (3.62 or 3.64:1, guide).
- **Mass:** BMW says the all-wheel-drive system adds 100 kg (ST040); EPA's test weights differ by 199 lb (90 kg).

**Figure C, "DSC swap":**
- **Left panel (xi):** Bosch unit on the right with its 42-pin blue plug; pre-charge pump under the master cylinder (left); one pressure sensor on the unit; analogue yaw sensor under the driver's seat; Hall sensors (two-wire, 8 V); reservoir with the switch in the tank; CAN on pins 24/40.
- **Right panel (after):** MK60 under the master cylinder with its 47-pin black plug; two pressure sensors on the master cylinder; CAN sensor cluster under the driver's seat (CAN2 on pins 29/25); MR sensors (12 V); reservoir cap switch; PT-CAN on pins 11/15.
- **Unchanged:** the steering-angle sensor on the column (X1658 pins 3/4 to the CAN), the booster and the parking-brake switch.

---

## Guide statements this research corrects

1. **README "If your car is a 325xi", Front axle:** "The xi has its own front subframe (31101096954) and knuckles, so "keep your front subframe" doesn't apply. You need the donor's rear-drive subframe (31111096902) with the whole M3 front axle…"
   - Add that the shell differs too. The xi's front frame rails (41007037635/636, 41117029237/238), strut towers (41007037637/638) and anti-roll-bar body brackets (41117161089/032) are xi-only parts; the M3 uses the 325i's ([ETK](https://bmwfans.info/parts-catalog/41007037635/), [ETK](https://bmwfans.info/parts-catalog/41118234033/)).
   - The xi's lower steering joint is a double-cardan part (32306750815 or 32306764009 with 32306754165). Fit the M3's 32301094700 or 32306764006 with coupling 32301094703.
   - The rear-drive subframe has gone into three xi Tourings without reported mount work, but trial-fit it before you commit.
2. **README, same section, Drivetrain:** "Converting to rear drive removes the transfer case, front driveshaft and front axle drive; the Bring a Trailer car is a 325xi converted this way."
   - Add the xi gearbox, its cast crossmember 22316750856 and the 1,244 mm rear driveshaft.
   - The M3 crossmember doesn't bolt to the xi tunnel: JMCCRNA needed a custom bracket, which then clashed with the exhaust.
   - Cite the second converted car, the 2004 Buffalo xi ([Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap)).
3. **README, same section, DSC:** "You'd fit an MK60 (the donor's, if it was built from 09/2002, or a late 325i's) and adapt the DSC wiring; nobody has documented that in a Touring. The steering-angle job differs too."
   - JMCCRNA's 2003 xi Touring used the M3's DSC module, though no wiring was published. A 2004 xi that kept its Bosch unit lists it as a known flaw.
   - Say what the swap needs: the MK60 and its left-side bracket; the CAN sensor cluster 34526764018; four MK60 wheel-speed sensors (the xi's Bosch Hall sensors are incompatible, and its front ones don't fit a rear-drive hub, [BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) pp.17–18); an MK60 master cylinder with two pressure sensors; reservoir and cap; the rear-drive/M3 brake pipes; and a loom built by signal, because the 42-pin and 47-pin plugs put CAN on different pins (24/40 against 11/15, [WDS](https://wds.psjr.org/en/e46/svg/SP0000017172.svg)).
   - The steering-angle sensor itself (32306793632) is common to all three cars. After the swap, use the MK60 job.
4. **README, same section:** "**Not checked for the xi:** the fuel tank, tunnel heat shields and exhaust hangers."
   - Now checked. The tank, pump, senders, lines and EVAP parts are the 325i Touring's. The xi adds a tank protective plate (16111183924) that rear-drive four-cylinder cars use too ([ETK](https://bmwfans.info/parts-catalog/16111183924/)).
   - The fuel-filter cover differs: 13327500083 against 13328230397, with a common bracket.
   - The tunnel heat insulator (51488253953 against 51488193807), the tunnel's outer insulation and the centre underfloor panel differ.
   - The exhaust hanger parts are common except one xi bracket ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/exhaust_system/)).
5. **README, same section:** "If the VIN says xi, budget for the second front axle and the DSC work, or look for a rear-drive 325i Touring."
   - Add the estimate: about \$0–\$1,500 extra in parts with a donor built from 09/2002, \$1,000–\$3,000 with an earlier one, and 4–8 more weekends.
   - Add the emissions point: every 2001–05 325xi Sport Wagon is LEV (test group LER), the same category as the S54, so in Massachusetts an xi is the better start than a 2003–05 325i Touring in UL2, SMG or M56.
6. **README Massachusetts, engine-switch table:**

   | Your Touring | Category | Against the S54 (LEV; federal Bin 9 from 2004) |
   |---|---|---|
   | 2001–02, and 2003 cars in test group "LER" | LEV | Same category |

   Add a row: "325xi (all 2001–05; 2001 test groups 1BMXV02.5M54 or 1BMXV03.0LER, 2002–05 LER) | LEV; 2004–05 California LEV and federal Bin 9 | Same category in every year" ([EPA certification data](https://www.epa.gov/compliance-and-fuel-economy-data/annual-certification-data-vehicles-engines-and-equipment)). And change the next row to "Other 2003–05 **325i** cars".
7. **WIRING-AND-CODING.md line 138:** "**A 325xi:** never assume. ETK lists the 325xi Touring with MS43 and no end date, yet with the same "from Mar '03" engine harness and secondary-air sensor as the 325i… Read the label."
   - Replace with: "A 325xi: expect an MS43 in every year. ETK lists only MS43 units for the 325xi Touring and only the MS43-era air-mass meter (13621432356). EPA certified every 2001–05 325xi Sport Wagon in the LEV test groups (LER), never in the ULEV-II group (UL2) that came with the MS45.1 on the 325i. The 325xi does list the "from Mar '03" engine harness. Read the label to confirm."
   - Sources: [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/L-N/browse/fuel_preparation_system/hot_film_air_mass_meter/), [EPA](https://www.epa.gov/compliance-and-fuel-economy-data/annual-certification-data-vehicles-engines-and-equipment).
8. **README "DSC, brakes and steering angle":** "If your car turns out to be a 325xi, it has a Bosch DSC 5.7 instead, and Option A doesn't exist."
   - Add: "Option B is the only route, and it needs more than the unit: see [If your car is a 325xi](#if-your-car-is-a-325xi) for the sensors, pipes, master cylinder, reservoir and wiring."
9. **README lines 164, 207, 477, 662, 1295 and 1649, and WIRING-AND-CODING line 638:** "…while a 2003 xi Touring took an M3's sensors…" / "on a 2003 xi Touring the M3 sensors 'plugged right in'."
   - That car's harness was a Bosch DSC 5.7 harness, with Hall sensors in the same blue plugs as the MK60's ([BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) p.17), and its builder also fitted the M3 DSC module.
   - So it shows only that the blue plug housings mate, not that MK60 sensors read correctly on a 325i harness. Keep the plug-check advice, but drop it as evidence of electrical compatibility, or say "the plugs mated".
10. **README line 39 and the BaT row (line 130):** "Finished conversions have sold for nearly \$60,000 ([Bring a Trailer, Aug 2024, via Top Gear]…)" / "Sold for nearly \$60,000."
    - Top Gear reported it "just sold for nearly \$60,000". An auction aggregator lists the 20 Aug 2024 result as "highest bid \$59,250 … Not Sold" [snippet], and vmax.si quoted a mid-auction high bid of "just over 35,000 dollars".
    - Suggest "bid to about \$59,250 on Bring a Trailer in 08/2024 (Top Gear reported it sold)" until the BaT page is read.
    - Add to the row: "donor a 2001 M3, so an MK20 (DSC route not stated)".
11. **README documented-builds table:** add a row for the 2004 Buffalo xi:
    - 325xi Touring made rear-drive; 2003 M3 S54 and 420G; M3 front and rear subframes, rack and 3.64 diff; MSS54HP DME; "Still using Bosch 5.7 DSC from Xi" (a known flaw); listed at \$24,000 (04/2023), sold for \$22,000 on Cars & Bids (06/2023)
    - Sources: [Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xi-touring-s54-swap), [Engine Swap Depot](https://engineswapdepot.com/?p=101132).

---

## Leads for the all-wheel-drive researcher (not my half)

- **540 CMR 6.00 applies to an xi kept all-wheel drive.** It covers "Any vehicle that is capable of providing torque to all four wheels": no spacers, at most four inches of track increase by tyres and rims, and the two-inch height rule ([6.03](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-6-03), [6.04](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-6-04)) [read]. M3 width and offsets on an AWD xi need checking against it.
- **A third AWD S54 xi Touring:** 2001, Denver, by a BMW master tech. 330xi oil pan with custom baffles, M50 oil pump with a welded nut, X3 3.0 3.91 front and rear differentials, a six-speed from a 330xi, and "the CV boot issue" mentioned in comments ([German Cars For Sale Blog](https://germancarsforsaleblog.com/superb-swap-2001-bmw-325xi-touring-s54-6-speed)) [read]. Also listed on a Chicago forum ([thechicagogarage](https://www.thechicagogarage.com/threads/2001-bmw-m3-s54-swapped-325xi-sport-wagon-6-speed-awd.168023/)) [snippet].
- **ETK facts:**
  - The xi transfer case changed at 03/2003 (27107509763 to 27107530812).
  - The front driveshaft changed from 718 to 723 mm at 03/2003.
  - The xi uses a 240 mm clutch (325i 228 mm) and its own clutch pipe 21526753015.
  - The xi front axle carries the "VAG 174" front differential bolted to the oil pan's left side (ST040) [read].
- **EPA:** the xi stays LEV in every year, which helps an AWD build in Massachusetts too.

## Other leads (outside this topic)

- **A California sleeper.** Built for Backroads lists a 2001 325i Touring with "BMW S54 Engine (BAR Legal)", a 420G and a custom driveshaft ([Built for Backroads](https://www.builtforbackroads.com/listing/2001-bmw-m3-touring-s54-swap)) [read]. That's a documented California referee case for the legal section, if the seller's claim holds.
- **ZCS storage.** ST406's table puts the E46 ZCS in the "Instrument Cluster/LSZ", while the Bali DIY used by the coding notes says cluster and EWS for ZCS cars ([BMW ST406](https://archive.org/download/BMWTechnicalTrainingDocuments/ST406%20Coding%20%26%20Programming/06%20Vehicle%20Coding%20Information.pdf)) [read]. Worth a line in the coding notes.

---

## Sources tried and blocked

| Source | What happened | What would settle it |
|---|---|---|
| e46fanatics: JMCCRNA "M3 Touring project" (1240087); "converting a XI to RWD" (1284904); "XI to RWD conversion?" (776142); "2001 330xi RWD conversion" (1042163); "XI RWD conversion" (1319419); "$200 rwd conversion" (1127234); "Coding 330xd automatic to RWD manual conversion" (1314623); "RWD vs AWD chassis differences" (1108800); "XI vs RWD front suspension different?" (1302844) | Challenge page (HTTP 202 with a "challenge" script); Wayback has no snapshots of 1240087, 1302844, 1065607 or 1108800 | A logged-in browser read of 1284904, 1042163 and 1314623 |
| bimmerfest (t-392088; 1324515, which is probably an E60) | Challenge page | Browser read |
| f30.bimmerpost (F30 xDrive-to-RWD coding) | 403 | Browser read; not an E46 anyway |
| BMWBlog (BaT article), Motor1 | 403 to curl; DNS failure in the fetch tool | The guide's earlier [read]; Wayback Motor1 snapshot 2025-07-23 exists |
| Bring a Trailer listing | URL not found by search; guessed URLs redirect to login | The listing URL from BMWBlog |
| Cars & Bids auction (36qE0ZYZ) | Cloudflare | Wayback snapshot 2023-05-25 exists |
| classic.com | Cloudflare | — |
| web.archive.org | The proxy reset every connection; the availability API returned 429 for most of the session | Retry later |
| archive.org (download) | Worked: ST040, ST056, ST406 | — |
| WebSearch | 16 calls, one rejected for naming a blocked domain | — |
