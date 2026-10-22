# Front axle, steering, brakes and ABS/DSC hardware: M3 parts in a 2003 US 325i Touring (Teves MK60)

Research date: 22 October 2026. Scope: a 2003 US E46 325i Touring (M54, 5-speed manual, RWD, Teves MK60 DSC from 09/2001 production, Massachusetts registration) receiving the front axle, steering, brakes and rear brake parts of a 2003–06 US E46 M3 (S54, MK60 from 09/2002). Default route (the guide's Option A): keep the Touring's own MK60 hydraulic unit/control unit, booster and master cylinder. DSC coding and calibration belong to another researcher; where a hardware fact affects coding it is flagged as a cross-reference only.

How each finding was read:
- **[read]** I read the page or document itself (HTML, PDF text, or a parts-catalog page).
- **[image]** I looked at the parts-catalog or compilation diagram image.
- **[captions]** I read the video's caption text (auto-generated unless stated) with timestamps.
- **[snippet]** I saw only a search engine's summary of the page; the page itself was blocked or not opened.
- **[earlier note]** taken from an earlier research note in this project, which marked it as read.

Blocked or unavailable this round (not retried, nothing worked around): e46fanatics.com and bimmerfest.com (proof-of-work bot challenge), workshop-manuals.com, bolidenforum.de, leebmann24.com, m3cutters.co.uk, turnermotorsport.com, pelicanparts.com (403/Cloudflare), princeton.edu (Cloudflare challenge), 5series.net (Cloudflare, per earlier notes), tis.spaghetticoder.org (dead). The shared web-search budget ran out near the end of this round, so a few leads below could not be followed (listed under Gaps).

"ETK" below means BMW's parts catalog as published on bmwfans.info for the **US E46 M3 coupe (M3-S54, L-N)** and the **US E46 325i Touring (325i-M54, L-N)**; I read every group page cited and, where shown, the diagram image.

---

## Takeaway (what changes in the guide)

1. **Front axle bolts straight on.** ETK lists the same front axle support (31111096902), the same four M12×1.5×100 subframe bolts (31116781023), the same control-arm-bracket bolts (33306760652, two per side), the same strut-top nuts (31316769731, three per side) and the same anti-roll-bar supports and end links (31351094552, 31356780847) for both cars. BMW's training manual says the E46's strut tower is slotted for camber on all E46s, and that the M3's top mount differs by an offset centre for more caster. One documented 2004 Touring (Tenza) fitted the whole M3 front subframe and the M3's aluminium thrust plate as a "direct bolt-on"; a UK 330i Touring fitted M3 knuckles/hubs and new M3 lower arms. Only open item: the M3 thrust plate uses 12 M10 screws where the Touring's uses 8, so confirm all 12 threads at mock-up.
2. **Only the anti-roll-bar clamps need ride height at the front.** BMW-derived annotations mark "tighten in normal position" only on the front anti-roll-bar clamp nuts (21 Nm). The control-arm bracket bolts (59 Nm), ball joints, strut, tie rods and plate carry no ride-height condition. The guide's "bracket bolts at ride height" (README, Appendix, Cards 8a/12d) should be dropped.
3. **Torque fixes:** M3 inner tie rods **110 Nm** (TIS via Department 69; "100 + 10 Nm" is the non-M figure and tolerance); subframe bolts **replace** (TIS via Department 69); strut-top nuts **conflict** (24 Nm in the M3 compilation, 34 Nm in TIS for the non-M E46 and the E85 Z4); PS pump mounting bolts 21 Nm and pulley bolts 27 Nm; PS hollow bolts M16 40 Nm, rack banjo M14 35 Nm.
4. **Steering:** M3 rack 32132229397 (ZF), 15.4:1 overall, 3.0 turns lock-to-lock, 36.1 ft turning circle (BMW USA 2003 and ST041); the 2003 325i Touring is 13.7:1, 3.0 turns, 34.4 ft. The M3 steering is about 12% slower than the Touring's. Pump, pressure hose, suction hose, return pipe, cooler coil and return line are all M3 parts; reservoir, bracket, lower joint, flexible coupling, column and steering-angle sensor are the **same part numbers** on both cars.
5. **Power-steering fluid: ATF.** ETK lists the reservoir and lid (32416851217/32416851332, same part on both cars) as the CHF 11S variant but "only in conjunction with" label 71246798132, whose supplement is "ATF". FCP Euro says BMW filled pre-2006 cars without active steering or hydraulic suspension with ATF Dexron III. M346 Projects filled its 2004 Touring/2003 M3 build with ATF. Don't mix with CHF 11S.
6. **Brake fluid: DOT 4, low-viscosity** for an MK60 car (BMW TIS bleeding instructions, 2005 issue: "all vehicles with DSC without precharging pumps must be filled with the new DOT4 low-viscosity brake fluid" [snippet]; BimmerWorld: DSC cars use low-viscosity, BMW 81220142156).
7. **Pressure-bleeder limit settled: 2 bar (29 psi)**, from BMW TIS 34 00 050 [read, E70 printout of the same procedure; E46 M3 DSC3 version agrees per snippet]. BMW requires the tester's bleed routine only after work on the master cylinder, the hydraulic unit or the lines between them; caliper and hose work gets a conventional bleed.
8. **Don't push air through a filled MK60.** In Option A no hard line changes (ETK: same front and rear pipes on the Touring and a 09/2002-on M3), so skip the guide's 20 psi air test, plug open lines, keep the reservoir full (a pedal depressor helps), and prove the system with a pedal-held static test instead (NAM3: overnight with the pedal wedged; Massachusetts: 125 lb for 10 s, at least 20% travel left).
9. **Booster vacuum hose: use the M3 check valve in your booster.** The Touring booster's port grommet (34336765316) is the same part on a 09/2002-on M3; the M3's check valve (34331161300) is the part BMW fitted to M52 E46s, including the 323i Touring, which use **your booster part (34336779682)**. Fit the M3 check valve in your booster, then shorten or re-route the M3 jet-pump hose: two S54 swaps (Tenza 2004 Touring; Import Modify 328Ci) had to cut and re-terminate it, and heinzboehmer's M3 MK20→MK60 conversion shortened the same kind of line.
10. **Master cylinder and calipers:** your 2003 MC (34336785666) is the same part as the 330i's. Reported bores: 330i MC 23.8/22 mm, M3 25/20 or 25/22 mm (forum); M3 front piston 60 mm (seal kit shared with E36 M3/E39; MaXgear listing [snippet]); 330i 57 mm, 325i 54 mm (BMW repair set description). Expect about 10% longer, lighter pedal travel than a real M3 on the front circuit; one documented 2004 Touring build with M3 brakes reported a "nice and firm" pedal after a manual plus INPA bleed (MC origin not stated).
11. **Wheel-speed sensors: same part numbers.** ETK lists front 34526792896/897 and rear 34526752683 for both the US 325i Touring and the US M3 from 09/2002, together with the same yaw/lateral sensor cluster (34526764018) and steering-angle sensor (32306793632). BMW: 2WD E46 rear pulse wheel sits on the outboard CV joint (comes with the M3 half-shafts) and gives 48 pulses per revolution. The Touring's own sensors plug in and read the M3 hubs.
12. **The 2004 Touring's ABS light (Tenza) is weak evidence of a problem:** it was seen at the first start, stationary, before the brakes were bled; three months later the builder said he'd had "not had any issues with this yet" after a 0.3–0.4 mile drive, and a later video mentions only body damage. Most likely causes are faults stored during the build, a sensor not seated, or a damaged pulse wheel. The DSC_MK60 fault list (below) tells them apart.
13. **Checks with pass values:** BMW's active sensors switch 7 mA/14 mA on a 12 V supply (not testable with an ohmmeter); MK60 pressure sensors must read under 5 bar with the brake light switch off; ABS works above 12 km/h (7 mph). Massachusetts' full brake test (540 CMR 4.04(4)) adds a parking-brake hold in the lowest gear at 1,200–1,300 rpm, a parking-brake stop from 20 mph within 80 ft, a 125 lb/10 s pedal hold with ≥20% travel left, the booster drop test and a no-pull check. The 30 ft service stop needs about 0.45 g average, the 80 ft parking-brake stop about 0.17 g (our arithmetic).
14. **BMW's loaded position is now sourced:** ST056 (2003) gives 68 kg per front seat, 68 kg in the rear seat, 21 kg in the trunk and a full tank for most models, but says the E36/E46 M3 is "usually measured without any weight"; ride height is measured rim edge to arch edge, with specs in TIS groups 31 and 33.

---

## Q1. Front axle: subframe, control arms, bushings, struts, hubs, anti-roll bar

### Cited findings

**ETK, US M3 vs US 325i Touring (both read; diagrams viewed [image]):**
- Front axle support: **31111096902 on both cars**; four "Hex screw with collar M12X1,5X100" 31116781023 on both. M3: "only in conjunction with Reinforcement plate 51717893609"; Touring from 02/2001: "only in conjunction with Reinforcement plate 51717028433" (Touring to 02/2001: "Reinforcement 31111096431"). [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/front_axle_support_wishbone/), [Touring from 02/01](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/front_axle_support_wishbone_2/), [Touring to 02/01](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/front_axle_support_wishbone/) [read]
- Reinforcement (thrust) plate fasteners: **M3: 12 × "Hexagon screw with flange M10X35-10.9ZNS3" 31106772199**, plus a jack fixture 51717894027 and blind rivet 07119903402. **Touring (from 02/01): 8 × 31106772199.** [read]
- Control arms ("Wishbone"): M3 31122229453/454 ("Required for repair"); Touring 31122282121/122 (from 03/01; earlier 31126777851/852). Arm fasteners on both: M14×1.5 self-locking nut 31106774714 (arm-to-subframe ball pin); M3 ball-joint nut "Self-locking collar nut M12X1,5" 31106777806; Touring uses 32216769539 "Self-locking hex nut M12X1.5". [read]
- Rear bushing brackets: M3 "Wishbone bracket with rubber mount" 31122229623 (L)/624 (R) with separate "Rubber Mounting" 31122229857 (×2); Touring "Set of brackets with rubber mounting" 31126783376 (D=66 mm). **Bracket-to-body bolts on both: "Hex bolt with washer M10X35-Z1-10.9" 33306760652, two per side.** [read]
- Struts: M3 31312283103/104 (coupe); Touring 31312282101/102 (from 11/2000) or 31316750789/790 and 31316750791/792. Strut-to-knuckle clamp bolt 31306779487 (M12×1.5×55-10.9) on both. Knuckles ("King pin"): M3 31212229855/856; Touring 31211096429/430. ABS/hose bracket on the strut 34526780591/592 and ABS sensor "ISA screw" 07129905386 (M6×30) on both. [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/front_spring_strut_shock_absorber/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/front_spring_strut_shock_absorber/) [read]
- Top mounts: M3 "Left/Right guide support" 31332229165/166 (handed), plate 31332229427, protection cap 31312229458 (to 04/02), upper spring pocket 31331090612, bump stop 31332229778. **Strut-top nuts on both: "Self-locking collar nut M8-8 ZNS3" 31316769731 (×6); rod nut 31106774714 (×2) on both.** [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/guide_support_spring_pad_attaching_parts/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/guide_support_spring_pad_attaching_parts/) [read]
- Hubs: M3 "Wheel hub with bearing, front" 31222229501; Touring "Wheel hub, front, symmetric" 31226757024. Same collar nut 31211128336, dust collar 31206777788 (D=69 mm) and cap 31206777789. [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/wheel_bearing/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/wheel_bearing/) [read]
- Anti-roll bar: M3 31352229755 (D=26 mm) with mounts 31352229756; Touring 31351097178 (23 mm) or 31351094542 (24 mm, sport/M Sport II). **Same supports 31351094552, collar nuts 07119905374, end links ("Front swing support") 31356780847 and link nuts 33306760587 on both.** [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/stabilizer_front/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/stabilizer_front/) [read]
- Brake dust shields: M3 34112282109/110; Touring 34116750129/130 (screw 34103451068 on both). [read]

**BMW ST041 "E46 M3 Running Gear" (production 01/2001):** M3-specific: "Front axle mount; Aluminum control arm frame; Aluminum thrust zone; Larger track width (1508 mm); Stabilizer bar; Steering (track rod length changed); Steering knuckle; Wheel bearings; Front axle carrier; Modified elastokinematics (rubber mounts and joints)". "The geometric layout (offset center) of the front axle mount makes it possible to increase the caster angle." "A locating bolt (arrow) can be removed and the upper mount bolt holes in the strut tower are slotted to allow the mount to be re-positioned for minimum camber adjustment." "The thrust zone is made of aluminum and is bolted to the control arm joints, front axle carrier and the rear control arm mounts." "The front stabilizer bar is 26 mm in diameter. The stabilizer links have been adopted from the E46/2." "The mount for the brake caliper has been modified compared to the E46/2. The wheel bearings have been modified for higher loads. A drive pin for the brake disc is located on the wheel hub." [text](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear_djvu.txt), [PDF](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear.pdf) [read]. Note: ST041 lists "Front axle carrier" as M3-specific, while the US ETK lists one part number (31111096902) for both cars.

**BMW ST056 "Suspension Systems and Alignment Procedures" (01/2003):** E46: front caster "No Adjustment", front camber "Yes, Tool #323 140", front toe yes, rear camber "Yes (Eccentric)", rear toe "Yes, Tool #323 030". "Camber is adjustable on the E46 and E85. There is a slot in the upper strut tower which will allow small Camber changes. A pin must be driven down… up to .5 degrees… Drive out the pin in the upper strut mount. Loosen all 3 upper strut mounting bolts… tighten upper strut mounting bolts to specification." E46 front: "Hydraulic bushings are used for the rear lower control arm support"; "The steering knuckles are press fit into the strut tubes". Loading: "68 kg. in each front passenger seat, 68 kg in the rear seat, 21 kg in the trunk, Fuel tank full. Not all vehicle need to be weighed down. Usually E39 M5 and E36/E46 M3 are measured without any weight. Always check TIS under Technical Data Group 32… 'Normal Position/Inspection Conditions'." "Ride height is measured from the lower edge of the wheel rim to the lower edge of the wheel housing… front axle ride height is in Group 31 and the rear… Group 33." Fuel compensation: about 3.2 kg per US gallon missing. [text](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/01%20Suspension%20Systems%20and%20Alignment%20Procedures%201-20-03_djvu.txt) [read]

**BMW USA 2003 spec sheets:** 325i Sport Wagon manual 3,362 lb, 47.7/52.3% front/rear, track 57.9/58.4 in. M3 coupe 3,415 lb, 50.3/49.7%, track 59.4/60.0 in. [325 sheet](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437), [M3 sheet](https://www.press.bmwgroup.com/usa/article/attachment/T0022150EN_US/41463) [read]

**Torques (compilations of BMW data):**
- Flow PDF (RealOEM printouts of the **EUR M3** annotated with TIS values) [read text, pages 2 and 8/11/27 viewed as images]: p.2 subframe M12 10.9 **110 Nm**; arm ball pin to subframe **90 Nm "Always replace"**; bracket bolts **59 Nm "(always replace)"** (no ride-height note); ball joint to knuckle **65 Nm "(always replace) (No impact wrench!)"**; plate screws **"Initial torque 59 Nm + Angle Torque: 90° (±30°) Always replace"**. p.3 strut-top nuts **24 Nm**; rod nut **64 Nm "Replace nut"**. p.4 strut clamp bolt **81 Nm "Replace screw"**; ABS sensor screw **8 Nm**. p.6 end-link nuts **65 Nm "(Always replace)"**; bar clamp nuts **21 Nm "Tighten in normal position to avoid preload"**. p.14 hub collar nut **290 Nm**. General note p.1: "When torquing down suspension bushings, car must be in 'loaded' position". [Flow](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) (local copy from an earlier round)
- Department 69 (each row linked to TIS for the E46 330i sedan) [read]: strut top nut 64 Nm, replace; **strut top mount to body 34 Nm, replace nuts**; strut clamp 81 Nm, replace; ball joint to knuckle 65 Nm, no impact gun; arm ball joint to subframe 90 Nm, replace nuts; rear bushing bracket to body 59 Nm (no condition); sway-bar end link 65 Nm; clamp 21 Nm; **front subframe bolts 110 Nm, "M12 grade 10.9. Replace bolts"**; hub nut 290 Nm. [Department 69](https://www.department69.com/articles/bmw-e46-torque-specs-complete-reference-all-engines)
- Z4-forum (E85, owner reading TIS): strut clamp 81 Nm, rod nut 64 Nm, "the three nuts connecting the strut mount (34Nm?)" — reply: "All those torques are correct." [Z4-forum](https://z4-forum.com/threads/replacement-front-struts-torque-specs.113285/) [read]. E85 shares the E46-type front axle (flag: not E46).

**Documented builds with results:**
- **Tenza Motorsports (2004 US 325i Touring + 2002 M3 donor):** "I am using an entire M3 front and rear subframe" — [Tenza – 5 things they don't tell you, part 2 (2021-07-19), 03:20](https://www.youtube.com/watch?v=mDBiRn30fEs&t=200s) [captions]. Front end reassembly: "it looks like everything should be a direct bolt-on"; "the actual metal skid plate is going to be the M3 skid plate and that's the metal one with the access door on it" (the M3's aluminium thrust plate) — [Tenza – S54 wagon front end reassembly using M3 parts (2021-02-20), 00:40](https://www.youtube.com/watch?v=k2YMcy9TdJk&t=40s), [06:00](https://www.youtube.com/watch?v=k2YMcy9TdJk&t=360s) [captions]. (An earlier plan video had said he would keep the Touring's subframe — [Tenza (2020-12-06), 01:40](https://www.youtube.com/watch?v=roTBxPmyhEY&t=100s) — superseded by the 2021 statement.)
- **Autoalex v2 (UK, supercharged 330i Touring):** to fit a big-brake kit, "we need these E46 M3 hubs because the spacing between these bolts is actually different to what's on the 330i"; fitted "brand new M3 lower arms… slightly longer, which gives you a slightly different caster and potentially camber angle" — [Autoalex v2 – We fitted expensive mods to our fast Tourings (2026-07-04), 15:40](https://www.youtube.com/watch?v=c_2bnLbABCc&t=940s), [21:40](https://www.youtube.com/watch?v=c_2bnLbABCc&t=1300s) [captions]. No alignment figures given.
- **Bimmersport NZ "332i" (330i sedan to M3 running gear):** "For the front, new CSL kingpins and wheel bearings were used" — [bimmersport](https://bimmersport.co.nz/topic/61203-project-332i-e46-m3-sedan/) [read]. Sedan, not Touring.

### Inferences
- **Body mounting points are the same.** Every fastener that meets the body or the shared subframe (subframe bolts, bracket bolts, strut-top nuts, bar supports) has the same part number and count on both cars, and BMW describes the strut-tower camber slot for all E46s. The M3's differences are in the parts themselves (arms, brackets/bushings, knuckles, hubs, struts, top mounts, bar), not in the body. Our inference from ETK + ST041/ST056, supported by Tenza's bolt-on report.
- **The thrust plate is the one item to prove at mock-up.** The M3 plate takes 12 screws, the Touring's 8. ST041 says the M3 plate bolts to "the control arm joints, front axle carrier and the rear control arm mounts"; if the 4 extra points are on the M3 brackets or the shared subframe they come with the swap. Tenza's report suggests it fitted; confirm all 12 threads before relying on it. If any is missing, fit your Touring's plate (51717028433) with its 8 screws and note it.
- **Ride-height condition.** Only the anti-roll-bar clamps clamp a rubber bush whose twist depends on the suspension position at tightening. The rear bushing of the front arm is pressed into its bracket and is not clamped by the bracket bolts, so tightening those bolts on stands doesn't preload it. The general "loaded" note in Flow is the compiler's; the BMW-annotated items don't carry it. So: torque everything at the front on stands except the bar clamp nuts.
- **Front axle loads match the M3's.** 325i Touring (manual) front axle ≈ 1,604 lb (3,362 × 47.7%); M3 coupe ≈ 1,718 lb (3,415 × 50.3%). The S54 swap adds front weight, so M3 front springs and struts are sized about right; the rear is the Touring-specific problem the guide already covers. Our arithmetic from BMW USA figures.
- **Alignment check proves the parts:** caster isn't adjustable (ST056), so a caster reading inside the M3 window (7°25' ± 30' at ±10° lock) with M3 top mounts and arms shows the right parts are fitted and the body is straight.

### Gaps
- No source states where the M3 thrust plate's 4 extra screws thread in (body, subframe or brackets).
- Strut-top nut torque: 24 Nm (M3 compilation) vs 34 Nm (TIS via Department 69 for the non-M E46; E85 owner). No M3 TIS page read.
- BMW's E46 ride-height values (TIS 31/33) and the M3's "Normal Position/Inspection Conditions" (TIS 32) were not readable.
- No E46-specific wheel-bearing play limit found.

---

## Q2. Steering: rack, pump, lines, cooler, reservoir, fluid, tie rods, column, bleeding

### Cited findings
- **Racks (ETK):** M3 "Rmfd hydro steering gear ZF" 32132229397; Competition (S7MAA, from 12/2004) 32132282642. Touring 32136753438 (ZF, 04/99–09/01) and 32136755065 (ZF, from 09/01). Same mounting bolts 32106781639 (M10×67-8.8) and nuts 33306760587, and the same "Set pipe" 32131096845 (ZF). [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/power_steering/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/steering/power_steering/) [read]
- **Tie rods (ETK):** M3 inner "Left/Right tie rod" 32112228785/786, outer "Ball joint" 32212229367/368; Touring inner 32106777503/504, outer 32106774220/221. Same lock nut 32116774889 (M14×1.5), clamp ring 32216774890, outer nut 32216769539 and bellows kit 32131096910. [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/steering_linkage_tie_rods/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/steering/steering_linkage_tie_rods/) [read]
- **Pump (ETK):** M3 "Rmfd power steering pump ZF" 32412229679 (also Z3 M3.2 S54), pulley 32427830838. Touring LUK LF-20/LF-30 pumps (32416760036, 32416756582, 32416760034). [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/power_steering_pump/) [read]
- **Lines and cooler (ETK):** M3 suction hose ("Intake manifold") 32412229369; pressure hose ("Expansion hose") 32412283893; hollow bolts M16×28 32416852470 (×2) with A16×22 rings 32411093597 (×4); "Banjo bolt with check valve M14X1,5X27,4" 32416781261 with A14×20 rings 32411093596 (×2); return pipe 32412282354; radiator return line 32412282353; "Cooling coil" 17102282339. Touring: 32416750155, 32416774215, 32416796367, 32416796390 and cooling coil 17111436262; same banjo bolt with check valve. [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/hydro_steering_oil_pipes/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/steering/hydro_steering_oil_pipes/) [read; M3 diagram viewed in Flow p.8, image]
- **Reservoir (ETK):** both cars: "Oil carrier 32416851217 — Only in conjunction with Label, oil container-power steering pump 71246798132 — CHF 11.S" and "Cover 32416851332" likewise; same bracket 32411092940. The label's own page gives its supplement as **"ATF"**, production from 03/2011 (old number 71242122171), used on E36, E46 (M3 included), E8x, E90 and others. [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/oil_carrier_single_parts/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/steering/oil_carrier_single_parts/), [label](https://bmwfans.info/parts-catalog/71246798132/) [read]
- **Column (ETK):** same on both: column 32303450159; lower joint 32301094700 (to 11/2003) / 32306764006 (from 11/2003); flexible coupling 32301094703 (from 04/2001); Torx bolts M8×33 32306778609 (×3); steering-angle sensor 32306793632 with holder 32301094904. [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/steer_col_lower_joint_assy/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/steering/steer_col_lower_joint_assy/) [read]
- **BMW ST041:** "The steering pump produces a maximum pressure of 120 bar and has a delivery capacity of 11 L/min. The total gear ratio is 15.4 : 1. The steering has no hydraulic limit stops. The turning circle is 11.0 m." "The outer track rods… are specific. They have been modified for the larger track width." [ST041 text](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear_djvu.txt) [read]
- **BMW USA 2003:** M3 "Overall ratio 15.4:1, Turns lock-to-lock 3.0, Turning circle 36.1 ft"; 325i Sport Wagon "Overall ratio 13.7:1, Turns lock-to-lock 3.0, Turning circle 34.4 ft", "engine-speed-sensitive power assist" on both. [M3](https://www.press.bmwgroup.com/usa/article/attachment/T0022150EN_US/41463), [325](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437) [read]
- **Fluid evidence:**
  - FCP Euro (vendor): "Everything prior to the NXX engine family of cars, BMW used ATF DEX III as OE fill oil in the power steering system… except those fitted with active steering or hydraulic suspension… Currently all OE catalogs have been updated to show CHF11S as the only option… If you have an older car and you mix CHF11S you will shorten the lifespan of your system… Your replacement cap will now only specify the use of CHF11S fluid regardless of application." [FCP Euro](https://www.fcpeuro.com/blog/heres-how-to-pick-the-right-power-steering-fluid-for-your-car-) [read]
  - M346 Projects (2004 Touring + 2003 M3 donor): at first start the pump rattled dry, "go grab some ATF and pour it in… bleed the system by rotating the steering wheel left and right" — [M346 – Pt 13 Engine start (2024-06-04), 08:00](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=480s) [captions].
  - Tracks and Trails used Red Line fluids for "transmission, diff, power steering" (type not stated) — [Tracks and Trails – first drive (2026-06-01), 68:40](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=4120s) [captions].
  - e46fanatics thread: an owner found the cap "embossed with ATF underneath the green sticker" — [e46fanatics](https://www.e46fanatics.com/threads/power-steering-fluid-chf-11s-or-atf.1275211/) [snippet].
- **Bleeding:** BMW TIS 32 13 006 (printout, issue 10/2001, model not named): engine off, fill to about 25 mm below the edge; start and top up evenly; turn to full lock each way twice; switch off and check against the lid mark. [princeton.edu](https://princeton.edu/~sdepasqu/bmw/steering/Bleeding.power.steering.unit.pdf) [snippet this round; read in an earlier round per the guide]
- **Torques (Flow, EUR M3, annotated):** rack to subframe 42 Nm (p.7); tie-rod lock nut 45 Nm, inner tie rod "100 + 10 Nm", tie-rod end 65 Nm "Do not use impact wrench!" (p.9); hollow bolts M16 **40 Nm** (pump and rack ends), banjo M14 with check valve **35 Nm**, M6 bracket bolt **8 Nm**, "Power steering pump to bracket M8 self-locking nuts 22 Nm; pump bracket to engine block M8 self-locking nuts 22 Nm" (p.8, image); reservoir 5.5 Nm and 22 Nm (p.10); pump mounting bolts M8×80 **21 Nm**, pulley bolts M8×14 **27 Nm** (p.11, image); lower joint Torx bolts 22 Nm (p.12). [Flow](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) [read/image]
- **Department 69 (TIS):** rack 42 Nm; "Inner tie rod to rack — All except M3: **100 Nm +10 Nm** (74 ft-lb +7). **M3: 110 Nm (81 ft-lb)**"; tie-rod end nut 65 Nm, replace, no impact gun; steering column coupling 22 Nm, replace clamping bolt. [Department 69](https://www.department69.com/articles/bmw-e46-torque-specs-complete-reference-all-engines) [read]
- **Builds:** a stored M3 line had been damaged and kinked and was replaced — [Tracks and Trails (2026-06-01), 65:20](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=3920s) [captions]; a weeping rack banjo union on a 330i Touring — [Autoalex v2 (2026-07-04), 20:40](https://www.youtube.com/watch?v=c_2bnLbABCc&t=1240s) [captions].

### Inferences
- **Fluid: ATF (Dexron III type).** ETK supplies one reservoir type (marked CHF 11S) and requires the "ATF" label on it for these cars; that pairing, FCP's account of BMW's OE fill and M346's build all point to ATF. If the donor's reservoir holds green fluid, someone converted it: flush fully to one fluid. Don't mix.
- **Keep your reservoir in place.** The reservoir, lid and bracket are the same parts on both cars, so the M3 suction hose should reach your reservoir in the factory position (inference from ETK). Fit new gasket ring 32411128333 if you open the outlet.
- **The M3 rack has no hydraulic end stops** (ST041), so at full lock the ZF pump runs to its 120 bar limit: don't hold the wheel at full lock while bleeding (our inference).
- **The steering gets slower:** 15.4:1 vs 13.7:1 is about 12% more steering-wheel angle for the same road-wheel angle, with the same 3.0 turns lock to lock and a 1.7 ft wider turning circle. Cross-reference for the coding researcher: the Touring's MK60 is coded with a steering-angle characteristic (`LENKWINKELKENNLINIE_2`) for its own rack; with the M3 rack and knuckles the DSC's yaw-rate target would assume about 12% more road-wheel angle than the car gets. Our inference; no source tested it.
- **Full-lock check:** 3.0 turns lock to lock means roughly ±540° at the steering-angle sensor at full lock each way (our arithmetic from BMW USA's figure); the DSC_MK60 job `STATUS_LWS_LI_RE_MAX` records the left/right maximum.

### Gaps
- No BMW document read that names the E46 power-steering fluid outright (TIS operating fluids and the owner's manual weren't reachable).
- No PS fluid capacity found.
- No E46 TIS bleeding page read this round (the cited printout doesn't name its model).

---

## Q3. Brakes: calipers, discs, pads, hoses, lines, booster and master cylinder, vacuum, fluid, bleeding, parking brake

### Cited findings

**Calipers, discs, pads (ETK, read):**
- Front: M3 caliper housings 34112282617/618, carrier 34112282177 (ZCP 34112282619 from 12/2004), carrier bolts "Hex bolt M12X1,5X41" 34111156989 or 34116767217, guide bolts 34111157041, bleed valve 34116758107, caliper repair set 34111157037, pads 34112282416 (ZCP 34112282995), pad sensor 34356751311, discs 34112229529/530 "325X28" (ZCP drilled 34112282445/446 "345X28" from 12/2004). Touring: housings 34116758113/114, carrier 34106758120, "Collar screw M12X1,5X32" 34116772428, repair set 34111153202, pads 34116761244, pad sensor 34351164371, disc 34116864058 "300X22". [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/front_brake_pad_wear_sensor/), [M3 discs](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/front_brake_brake_disc/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/front_brake_pad_wear_sensor/)
- Rear: M3 housings 34212282195/196 (ZCP 34212282857/858 from 12/2004), carrier 34212229705, repair set 34211166238, pads 34216761248, pad sensor 34352229780, disc 34212229379 "328X20". Touring housings 34216758135/136, carrier 34216758134, repair set 34211158578, pads 34216778168, pad sensor 34351164372, disc 34216864056 "294X19". **Both use the micro-encapsulated carrier screw M10×26.5 34203414763.** [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/rear_brake_brake_pad_wear_sensor/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/rear_brake_brake_pad_wear_sensor/)
- Usage pages: front pad sensor 34356751311 is listed for the US M3 **and the US 325xi Touring**, 330i/Ci and 325xi sedan; rear M3 sensor 34352229780 is M3-only. [34356751311](https://bmwfans.info/parts-catalog/34356751311/), [34352229780](https://bmwfans.info/parts-catalog/34352229780/) [read]
- BMW ST041: "Front brake discs: 325 mm diameter, 28 mm thick; Rear brake discs: 328 mm diameter, 20 mm thick. The tandem (dual circuit) brake master cylinder is 2-stage. The brake booster is a twin chamber (9/10") vacuum assisted unit." [ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear_djvu.txt) [read]

**Piston and bore sizes (no BMW figure found):**
- BimmerWorld: repair set 34111153202 "is described as Repair Set, Caliper, 54mm, for… non-M E46 3-Series (except 330)", i.e. your Touring's front caliper. [BimmerWorld](https://www.bimmerworld.com/Brakes/Caliper-Parts/Caliper-Rebuild-Kit-E46-323-325-328-Z4-Front.html) [read]
- BimmerWorld: the M3 front repair set 34111157037 is shared with the E36 M3, Z3 M, E39 540i/M5, E38, E53 X5 and Z4 M fronts; ZCP and CSL use the same kit. [BimmerWorld](https://www.bimmerworld.com/Brakes/Caliper-Parts/Caliper-Rebuild-Kit-E36-M3-MZ3-Front.html) [read]. The rear M3 kit 34211166238 is shared with the E39 M5 and some E53 X5. [BimmerWorld](https://www.bimmerworld.com/Brakes/Caliper-Parts/Brake-Caliper-Rebuild-Kit-Rear-E46-M3-E39-M5-E53-X5-30-44i.html) [read]
- MaXgear seal kit 27-1562 (front axle) lists "BMW 3 Coupe (E46) M3 CSL", "60 mm" and "ATE" [snippet via eBay listing].
- e46zone forum post (UK, 2012): "M3 - Front is 60mm, rear is 42mm. Discs Front 325mm, rear 328mm. Master 25mm/20mm. 330 - Front is 57mm, rear is 42mm. Discs Front 325mm, rear 320mm. Master 23.8mm/22mm." [e46zone](https://www.e46zone.com/forum/topic/41335-m3-master-cylinder-on-non/) [read; single forum post]
- e46fanatics thread "Help determining Master Cylinder Piston Sizes": from about 09/2002 a change "(25mm/20mm, front:rear to 25mm/22mm…)"; "I looked at the 330 master and it is also stepped (23.81/22.20)" [snippet].
- Master cylinders (ETK/BimmerWorld): your 2003 Touring's DSC MC 34336785666 is the same part as the 2002–06 325i/330i/325Ci/330Ci and Z4 2.5i/3.0i; the M3 MC from 09/2002 (34317838638) is shared with the Z4 M. Both carry two DSC pressure sensors 34521164458, nuts 07129906196 and the same reservoir 34326750798 with cap 34326752698. [Touring MC](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/brake_master_cylinder_dsc/), [M3 MC](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/brake_master_cylinder_dsc/), [BimmerWorld 34336785666](https://www.bimmerworld.com/Brakes/Master-Cylinders/OEM-Brake-Master-Cylinder-34-33-6-785-666.html), [BimmerWorld 34317838638](https://www.bimmerworld.com/Brakes/Master-Cylinders/OEM-Brake-Master-Cylinder-34-31-7-838-638.html) [read]
- Boosters (ETK): Touring 34336779682 (all US non-M E46 incl. 323i/328i/325i/330i and the Touring); M3 34332282193 (to 09/2002) / 34332282622 (from 09/2002, also Z4 M). [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/power_brake_unit_depression_2/), [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/power_brake_unit_depression/), [34336779682](https://bmwfans.info/parts-catalog/34336779682/) [read; diagrams viewed]

**Hoses and pipes (ETK, read; diagrams viewed):**
- Front, Touring (DSC, from 09/2000): "Pipeline with pressure hose M12/M12" 34326759218 and 34326755801 (MC to hydraulic unit); "Pipe M10/M12-590MM" 34326752405; "Pipe M10/M10-2246MM" 34326752407; hoses 34326766966 (×2); clip 34341163565; grommet 34331161163; brackets 34301165471, 34301161568 (×2), 34301165382. [Touring front](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/front_brake_pipe_dsc/)
- Front, M3 from 09/2002: the **same four pipes**, **hoses 34322229723 (M3-only)**, same clip/grommet/4-fold bracket, plus spacer holders 34306756130 and 34321107991 in place of the Touring's bracket 34301165382. [M3 front from 09/02](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/front_brake_pipe_dsc_2/). M3 to 09/2002 (MK20): different pipes incl. 34322282275/277 and a pre-charge-pump line 34532282285. [M3 to 09/02](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/front_brake_pipe_dsc/)
- Rear, both cars (Touring from 09/2000, M3 from 09/2002): "Pipe M10/M12-3684MM" 34326752409, "Pipe M10/M10-3798MM" 34326755704, "Intermediate piece M10X1" 34326757282, "Pipe M10/M10-1206MM" 34326766825, hoses 34301165174 (×2), hose bracket 34301164003 with M6×12 bolt 07119904517, retaining spring 34306771981. [Touring rear](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/rear_brake_pipe_dsc/), [M3 rear from 09/02](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/rear_brake_pipe_dsc_2/)
- BMW ST056: the MK60 "is located in the engine compartment on the left side under the brake master cylinder"; "The hydraulic circuit is split front/rear"; "Two brake pressure sensors are mounted on the master cylinder below the outlet ports for the front and rear brake circuits." [ST056 E46 DSC](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) [read]

**Booster vacuum (S54 to the Touring booster):**
- BMW ST055 "MS S54": "The ECM regulates the Suction Jet Pump to provide sufficient vacuum for the brake booster under all operating conditions… Additional vacuum compensation is activated… when the idle air actuator is regulated for: A/C compressor 'on'; vehicle in gear and the clutch is released; engine in warm-up phase <70 °C. Additional vacuum compensation is applied to the brake booster when the circuit is 'deactivated' (solenoid sprung open)." [ST055](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf) [read, local text copy]
- ETK M3 "Vacuum control – engine": "Sucking jet pump with lines" 11617831663 (to 09/2002) / 11617836745 (current from 09/2004, old number 11617832989); hose elbow 11617831460; **"Air shut-off valve" 11617833212** (M3 only); bracket 11617832037; clamps 11151726340. Touring M54: jet pump 11617545382, elbows 11617503666 and 11617547582. [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/vacuum_control_engine/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/vacuum_control_engine/) [read; diagrams viewed]
- ETK booster port parts: M3 from 09/2002 "Gasket" **34336765316** + "Check valve support" **34331161300** + clamp 11151726340 (M3 to 09/2002: "Gasket ring" 34331158929). Touring: "Gasket" **34336765316** + "Non-return valve" 34331160183 + hose clamps 11151726339 (21.3 mm) + "Hose elbow" 34336751108. Usage pages: **34331161300 is also listed for the US 323i/328i/323Ci/328Ci and the 323i Touring**, which use booster 34336779682; 34336765316 is listed for every US E46 including the M3 and the 325i Touring. [34331161300](https://bmwfans.info/parts-catalog/34331161300/), [34336765316](https://bmwfans.info/parts-catalog/34336765316/), [34331160183](https://bmwfans.info/parts-catalog/34331160183/) [read]
- Builds: Tenza (2004 Touring): "this connector on this side the m3 this plugs in on this side and on the non-m it plugs over on that side so… taking this crimp, removing it, cutting the hose here, moving this connector up" — [Tenza – 5 things (2021-02-26), 07:40](https://www.youtube.com/watch?v=-TXzg2Z8d7w&t=460s) [captions]. Import Modify (E46 328Ci S54 swap): "the brake booster. It turns out it's a check valve. You can blow in one direction, but not the other… This is the hose I removed. It was clearly too long… I'll cut it [at] this U-shaped curve… it should fit perfectly" — [Import Modify – Ep.36 S54 swap part 10 (2018-09-14), 11:04](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=664s) [captions]. heinzboehmer (2002 M3, MK20→MK60): "Adapt the MK20 brake booster vacuum line so that it fits the MK60 booster. The MK20 line is longer than the MK60 line… Crimp the thing onto the MK60 check valve" — [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap) [read].
- DME test: MSS54 job `STEUERN_VENTIL_SAUGSTRAHLPUMPE` opens the valve for 2 s [earlier note `test_values_and_diagnostics.md`, from the SGBD documentation].

**Pedal feel, documented:**
- M346 Projects (2004 Touring, 2003 M3 donor, M3 brakes): a pressure bleeder at "20 psi… barely anything comes out" of a completely open system; bled manually, then "the mk60 bleed procedure with INPA to finish it off… pedal's nice and firm no more air bubbles"; "now that the brakes are bled and all the ABS sensors are in there's no more brake lights… no more TPMS light". Which MK60 and MC were fitted isn't stated. [M346 – Pt 16 (2024-06-07), 04:00](https://www.youtube.com/watch?v=DxMs8VZiXGY&t=240s), [09:20](https://www.youtube.com/watch?v=DxMs8VZiXGY&t=560s), [14:00](https://www.youtube.com/watch?v=DxMs8VZiXGY&t=840s) [captions]
- DBO (330Ci, full M3 swap, M3 booster): the two boosters' studs were "about 10 centimeters on center and… about 9", so they slotted the firewall holes — [DBO (2019-12-22), 08:44](https://www.youtube.com/watch?v=td8MgQ_3KGs&t=524s) [captions]. Relevant to Option B only.

**Brake fluid:**
- TIS 34 00 050 (E70 printout): "Use only BMW-approved brake fluids, see BMW operating fluids." [read, link below]
- BMW TIS "Bleeding brake system with DSC" (2005 issue, copies on 5series.net incl. an E46 M3 DSC3 version): "All vehicles with DSC without precharging pumps must be filled with the new DOT4 low-viscosity brake fluid. All other models can be filled with the DOT4 or DOT4 low-viscosity brake fluid." [5series.net](https://5series.net/forums/attachments/diy-do-yourself-14/5580-brake-fluid-flush-ra__bleeding_brake_system_with_dsc.pdf) [snippet]
- BimmerWorld (vendor): "Cars with DSC use the Low Viscosity; cars without DSC (or with ASC+T) use Normal Viscosity"; BMW part 81220142156. [BimmerWorld](https://www.bimmerworld.com/Brakes/Genuine-BMW-DOT4-ESL-Low-Viscosity-Brake-Fluid-81220142156.html), [types](https://www.bimmerworld.com/BMW-Brake-Fluid-Types/) [read]
- BMW ST056: the MK60 has no pre-charge pump ("The pre-charge pump used on previous systems is no longer required"). [read]

**Bleeding:**
- **BMW TIS 34 00 050 "Bleeding brake system with DSC" (newTIS printout for the E70 X5):** "When replacing or repairing, observe the filling and bleeding instructions for the following parts: Tandem brake master cylinder, Hydraulic unit, Components and connecting lines which are fitted between these assemblies… Connect bleeder unit with max. 2 bar filling pressure… Charging pressure should not exceed 2 bar." Sequence: rinse each wheel until clear and bubble-free, rear right, rear left, front right, front left; then for each circuit run the DIS routine with the vent valve open; "After completing routine, press brake pedal 5 times to floor; clear and bubble-free brake fluid must flow out." Finally set the level to MAX; "Pay attention to rubber seal in sealing cap." [xoutpost PDF](https://xoutpost.com/attachments/x5-e53-forum/83406-low-speed-braking-34-00-050-bleeding-brake-system-dsc.pdf) [read]. Flag: E70 printout of the same TIS number; the pressure limit is a BMW-wide value.
- E46 M3 "bleeding brake system with DSC3" TIS (MK20): bleeder "max. 2 bar"; the routine restarts on each wheel; "For all other work on the brake system (e.g. replacing brake calipers), the instructions 'Bleeding brake system with ABS/ASC+T' must be observed." [5series.net](https://5series.net/forums/attachments/diy-do-yourself-14/5585d1110377606-brake-fluid-flush-e46_m3_bleeding_brake_system_with_dsc3.pdf) [snippet]
- DSC_MK60 SGBD (BMW EF-73, rev. 1.15, "Conti_Teves MK60 DSC3", E46/R50/E85): bleed jobs `NA_ENTLUEFTUNG_LI` and `NA_ENTLUEFTUNG_RE` ("Nachentlüftung" left/right); valve job `STEUERN_DIGITAL` with EVVL/AVVL, EVVR/AVVR, EVHL/AVHL, EVHR/AVHR (inlet/outlet valves front-left … rear-right), SV1/SV2, EUV1/EUV2, PUMPE. [SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC_MK60.md) [read]
- INPA path (E46): E46 → Chassis → DSC MK60 → F6 Activate → F1 Control hydraulic → F2 (FL/RL) or F3 (FR/RR); pedal pressed, bleed screw open, pump pulses the pedal; 2–3 runs per corner, then a conventional bleed [earlier note, madstig guide]. Z4 M (E85, same menus): pedal stayed spongy until pressed hard; about 1.25 L used [earlier note, z4-forum].
- NAM3 heinzboehmer (2002 M3): "Fill up and bleed everything in the standard order (RR, RL, FR, [FL], clutch). Wedge some wood between the seat and the brake pedal (tightly) to pressurize the system. Come back the next day and check all the junctions"; air test of the new dry lines at 20 psi before the MC/booster went in ("Dropped ~0.4 psi… over 22 hrs"); bleed again after driving. [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap) [read]

**Parking brake:**
- ETK: M3 shoe kit 34416761293 (also E39 M5, E60, E65 etc.), springs 34410034938, adjusting screw 34416851437, support 34411163978 (×2) with bolts 34306772869 (M8×22, ×4); Touring kit 34416761291, springs 34410410823, adjusting screw 34416851438. **Same cables 34411165020/021, expanding lock 34416851439, guide bush 34411164583, nuts 07146778500**, lever 34411164489 and switch 61311369771 on both. [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/parking_brake_brake_shoes/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/parking_brake_brake_shoes/) [read]
- BMW TIS "Adjusting parking brake" (printout, issue 10/2001, model not identified; its wording says "parking brake pedal"): loosen the left cable nut, remove one wheel stud per rear wheel, turn the adjuster until the wheel won't turn, "then unfasten the adjusting screw 8 notches"; work the lever 10 times "up to 6th ratchet", engage on the 3rd ratchet and adjust; check "1st tooth… free (can be turned by hand), 4th tooth… fixed (cannot be turned by hand)"; roller-test minimum force (value garbled). [princeton.edu](https://www.princeton.edu/~sdepasqu/bmw/Gas.Tank/RA.Adjusting.parking.brake.pdf) [snippet]
- E46 workshop manual (third-party, translated, bmwman.ru): run in old shoes: "carefully tighten the parking brake at a speed of 40 km/h so that the brake action is slightly felt. Maintaining the speed, tighten the brake by one tooth and drive another 400 m. Release the brake and let it cool." Adjust when shoes, discs or cables are replaced or the lever travels "over 10 teeth"; BMW tool 34 1 030 for the cable nuts; adjuster to lock, then "back by 10 teeth" (left side turns one way, right the other); cable: lever at 4 teeth, nuts until the wheels "can still rotate smoothly by hand"; lamp check: released off, 1 tooth no braking, 2 teeth lamp on. [bmwman.ru](https://www.bmwman.ru/en/3er/E46/chassis/brake/regulirovka-stoyanochnogo-tormoza) [read]
- BimmerWorld (vendor): back off 10 clicks [cited in the guide]; ECS bed-in (vendor) [cited in the guide].

**Massachusetts 540 CMR 4.04(4) (read in full):** "(a) The inspector shall operate the vehicle to test the parking and service brake. The parking brake… will be tested by accelerating the motor to approximately 1,200 to 1,300 RPMs with the vehicle in the lowest forward gear against the brake in the applied position. The vehicle will be rejected if the parking brake will not hold. The service brakes will be tested at a speed of between four and eight MPH. Service brakes must be reasonably equalized so that the vehicle does not pull to either side when applied. A test with the brake meter shall be made at a speed of 15 to 25 MPH in all questionable cases. (b) …stop the vehicle from a speed of 20 MPH in not more than… Service (foot) Brake, Pleasure Vehicles 30 feet… Parking (hand) Brake, All Vehicles 80 feet. (c)1. Hydraulic Brake Systems. While the vehicle is stopped, apply approximately 125 lbs. foot-force to the brake pedal and hold for ten seconds. Reject the vehicle if the brake pedal height cannot be maintained or if less than 20% of the total available brake pedal travel remains or if the brake failure warning light on vehicles so equipped illuminates. 2. Power Brake Systems. Stop the vehicle engine and depress the brake pedal several times to eliminate all vacuum… Depress pedal with a light force, approximately 25 lbs. foot-force and while maintaining this force on pedal, start the vehicle engine and observe if pedal moves slightly… rejected if evidence of fluid leaks or chafing, cracking, swelling, restriction or other damage exists on hydraulic tubing or hoses or if they are not securely fastened…" (6): full lock both ways without "binding or interference"; front end jacked and ball joints checked "in accordance with the applicable manufacturer's specifications". [LII](https://www.law.cornell.edu/regulations/massachusetts/540-CMR-4-04) [read]

**Brake torques (Flow, EUR M3, annotated; Department 69 TIS):** front carrier M12×1.5 110 Nm; guide bolts 30 Nm (Department 69: 25–30 Nm); rear carrier M10 65 Nm; brake line on caliper 19 Nm; bleed screws 7 mm 3.5–5 Nm, 11 mm 12–16 Nm; disc screw 16 Nm; dust-shield screws 9 Nm (p.23, image); MC to booster 26 Nm "Replace"; booster to pedal bracket 25 Nm; DSC pressure sensor "25 + 5 Nm"; wheel bolts 120 ± 10 Nm. [Flow](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing), [Department 69](https://www.department69.com/articles/bmw-e46-torque-specs-complete-reference-all-engines) [read]

### Inferences
- **Your pipes and rear hoses stay; only the front hoses change.** All four front pipes and all rear pipes/hoses are the same parts on the Touring and a 09/2002-on M3; the M3 front hose (34322229723) meets the same pipe end and the M3 caliper. With an M3 built before 09/2002 the brake hardware is still fine (calipers, discs, hoses don't depend on the DSC), but its MK20 pipes and sensors aren't used.
- **Master cylinder arithmetic (Option A).** A tandem master cylinder gives both circuits the same pressure, so front/rear balance is set by the M3 calipers, discs and pads plus the DSC's electronic proportioning, not by the MC. The MC size sets travel and effort. Using the forum sizes: M3 front piston area vs 330i is (60/57)² ≈ 1.11; M3 MC vs 330i/your MC (25/23.81)² ≈ 1.10. So with your MC the front circuit needs about 10% more pedal travel per millimetre of caliper movement than a real M3, and about 10% less pedal force per bar of front pressure. Against your current 325i fronts the M3 front pistons displace (60/54)² ≈ 1.24 times as much. Expect a slightly longer, lighter pedal than an M3's, not a dangerous one; M346's firm pedal fits that. Our arithmetic from forum-reported sizes; no BMW dimension found.
- **Cross-reference for the coding researcher:** the Touring MK60's brake pressure models (`DRUCKMODELL_VORDERACHSE/HINTERACHSE`) assume 325i brakes; with M3 calipers and larger discs the front brake torque per bar rises by roughly a third (piston area × about 9% larger effective radius), so DSC brake interventions may be stronger than modelled. Inference only.
- **Vacuum hose solution:** the M3's check valve elbow seats in the same grommet BMW uses in your booster, and BMW itself fitted that check valve to your booster part on M52 cars. So: new grommet 34336765316 in your booster, the donor's check valve 34331161300 (blow test: passes only from booster toward engine), and the donor's jet-pump hose shortened or re-routed to it with clamp 11151726340, keeping the jet pump, the air shut-off valve and its DME wiring. Our inference from ETK, matching three documented re-terminations.
- **No air test through the MK60.** BMW requires the tester routine only when air has reached the MC/HU/lines between them (TIS 34 00 050). Option A leaves those undisturbed if you cap the open pipe ends at the strut and rear brackets and keep fluid in the reservoir (a pedal depressor closes the MC's central valves, standard practice). Then a conventional bleed (RR, RL, FR, FL, clutch) is all BMW calls for. Blowing 20 psi of air through the system, as the guide suggests, would put air into the HU and force the INPA routine.
- **Parking brake:** the M3 shoes and adjuster differ but the cables are shared, so the Touring's cables and lever stay; adjust from scratch. The 8 vs 10 notch difference is small; the functional checks (free when released, holds at a few teeth, lamp timing, MA hold and 80 ft stop) decide.
- **Inspection lamps:** BMW (ST056) says the red BRAKE lamp means low fluid or parking brake applied, while DSC/ABS faults light the yellow BRAKE lamp, the ABS lamp and the DSC lamp. Massachusetts rejects a lit "brake failure warning light"; get all four brake-related lamps dark before the appointment.

### Gaps
- No BMW figure for caliper piston or MC bore diameters; the non-M 325i rear piston size wasn't found (the search budget ran out).
- No BMW figure for booster sizes other than the M3's "9/10" twin chamber.
- E46-specific parking-brake TIS text (notch count, lever teeth, bedding) not read; brake-pipe union torques not found.
- The E46 MK60 version of TIS 34 00 050 wasn't read (E70 version read; E46 M3 MK20 version seen as snippet).
- Which master-cylinder outlet feeds the front circuit isn't stated in the sources read.

---

## Q4. ABS/DSC hardware: wheel-speed sensors, pad-wear sensors, steering-angle sensor, yaw/lateral sensor, and the 2004 Touring's ABS light

### Cited findings
- **ETK, wheel-speed sensors by build date (read):**
  - Front, M3: "Pulse generator, ABS" 34521165609 (×2) **to 09/2002**; 34526792896 (right) / 34526792897 (left) **from 09/2002**. Touring: 34521165609 (ASC cars), 34526792896/897 (MK60; listed "from Sep '01" and "Sep '00 to Mar '03" rows). Usage page: 34526792896 (old number 34526752682) is used on the US 325i Touring and the US M3 coupe/cabrio. [M3 strut group](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/front_spring_strut_shock_absorber/), [34526792896](https://bmwfans.info/parts-catalog/34526792896/)
  - Rear, M3: 34521164652 / 34521164370 **to 09/2002**; **34526752683 from 09/2002**. Touring: 34521164652/34521164370 to 09/2001 (and to 09/2000 with DSC); 34526752683 from 09/2001 (DSC from 09/2000). Same cable clip 34521164653 (×15). [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/rear_axle/rear_axle_support_wheel_suspension/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/rear_axle/rear_axle_support_wheel_suspension/)
  - Inductive sensors 34521165609 and 34521164370 are listed for the US M3 and US ASC/MK20 non-M cars including the 323i/325i Touring. [34521165609](https://bmwfans.info/parts-catalog/34521165609/)
  - Steering-angle sensor 32306793632: all US E46 incl. M3 and 325i Touring. Sensor cluster ("Speed sensor") 34526764018: US 325i Touring and M3 (MK60). [read]
- **BMW ST056 "E46 DSC" (01/2003) [read]:** MK60 "active wheel speed sensors that operate on the principle of magnetoresistive effect… Signal High-14mA, Signal Low-7mA… The sensor evaluation circuit is supplied 12V by the MK60 control unit. Output voltage from the sensor is approximately 10V. The control unit counts the high and low current pulses… Front sensors are three wire because they have a separate ground wire. Rear sensors are two wire… Different sensors are used on the left and right side front axle… the difference comes in the length of the harness. The connectors are blue… grey connectors used for sensors on the MK20 EI. The DSC III MK60 uses the same metal pulse wheels used with the MK20 inductive sensors… The short sensor is used on the 325i (any transmission) and 330i automatic. The long sensor is used on the 330i manual." For the xi's Bosch system: "The pulse wheel for the rear axle circuit is identical to 2wd E46 models. The pulse wheel is a plastic coated metal wheel attached to the rear stub axle outboard C.V. Both pulse wheels produce 48 pulses: 1 wheel revolution." Steering-angle sensor "mounted towards the lower end of the steering column, above the flexible coupling"; pins 1 KL30, 2 KL87, 3 CAN high, 4 CAN low, 5 KL31, 6 TXD; "requires initialization… Once initialized, the LEW sends an ID number". MY2002: yaw and lateral sensors combined in a "sensor cluster… installed in the same position as the yaw rate sensor [under the driver's seat]… operated at 5 volts and has a separate CAN connection". Pressure sensors: 5 V reference; "The pressure sensors must not detect more that 5 bar when the BLS is not actuated." Fluid-level reed switch in the cap: if open, "the DSC responds by switching off the ASC/DSC functions. Normal braking and ABS operation is unaffected." Lamps: "ABL 'BRAKE' lamp… Red indicates low brake fluid or hand brake engaged. Yellow indicates DSC/ABS fault or system disabled by the switch… The ABS lamp is controlled directly by the DSC III control unit via hardwire." DSC button: short press (<2.5 s) DSC lamp, long press (>2.5 s) DSC lamp plus yellow ABL. "ABS braking is possible when vehicle speeds are above 12 km/h (7mph)." [ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf); the same xi text is in [ST034 part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/14%20P2%20Traction%20and%20Stability%20Control%20Internet.pdf) [read]
- **BMW ST040 "Teves DSC III MK60" (E46 except M3 and xi, from 09/00), Workshop Hints [read]:** DIS service functions: "Connection Speed Sensor: A test to verify the proper wiring to the wheel speed sensors"; "Connection Brake Lines: A test to verify the proper brake pipe connections to the hydraulic unit"; adjustment functions for steering angle, lateral acceleration and pressure sensors. "Coding must be performed after replacement of the MK60 control module or the steering angle sensor." Adjustment required when replacing the control unit, replacing/re-coding the SAS, replacing a pressure sensor or the lateral acceleration sensor; SAS offset adjustment "after the sensor has been replaced, coded or after repairs to the steering or suspension system". Special tools: 47-pin cable 34 5 250, break-out box. [ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/6%20DSC%202010-30-00.pdf)
- **DSC_MK60 SGBD [read]:** status jobs `STATUS_RADGESCHWINDIGKEIT` (VL/VR/HL/HR in km/h), `STATUS_SCHALTER` (brake-light switch, handbrake switch, DSC button, brake-fluid switch), `STATUS_SENSOREN` (yaw °/s, lateral g, push-rod and floating-circuit pressures in bar, control-unit temperature, Uref, pump voltage, KL30, VCC), `STATUS_SENSOREN_OFFSET`, `STATUS_LWS_LI_RE_MAX`; calibrations `LENKWINKEL_DSC_ABGLEICHEN`, `DRUCKSENSOR_DSC_ABGLEICHEN`, `QUERBESCHLEUNIGUNG_DSC_ABGLEICHEN`. Wheel-sensor faults per wheel (FL 0x5D90–95, FR 0x5DA0–A5, RL 0x5DB0–B5, RR 0x5DC0–C5): …0 "elektrisch defekt" (electrically defective), …1 "Extrapolation", …2 "Impulsrad periodische Überwachung" (pulse wheel, periodic monitoring), …3 "Anfahrerkennung v_Vergleich" (drive-off speed comparison), …4 "Langzeitüberwachung" (long-term monitoring), …5 "Check auf doppelte Impulsradfrequenz" (double pulse-wheel frequency). Others: 0x5E1F "ABS/ASC/DSC: VIN nicht initialisiert, LWS-Abgleich durchführen", 0x5E1E LWS CAN timeout, 0x5E20/21/24 pressure sensors, 0x5E40/43 steering-angle sensor, 0x5D8C–99 sensor cluster, 0x5DF0 pump motor, 0x5DF4 supply <9 V, 0x5E5D brake-fluid switch, 0x5E5E brake-light switch, 0x5E59 coding error. [SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC_MK60.md)
- **MK60 47-pin assignments** (heinzboehmer's TIS-derived mapping) [earlier note `body_and_network_circuits.md`, table D6]: FL supply 45 / signal 46; FR signal 33 / supply 34; RL supply 36 / signal 37; RR signal 42 / supply 43; processed rear-right speed pin 8 → DME X60004-22; processed rear-left pin 10 → cluster pin 19; ABS lamp 44 → cluster 22; brake-light switch 41; parking-brake switch 27; fluid level 9; DSC button 39; pressure sensors 18–20 and 21–23; sensor cluster 6/24/25/29; KL30 1 and 32; ground 16 and 47; KL15 4.
- **NAM3 heinzboehmer (2002 M3 MK20→MK60):** "The sensors are different between the two systems so you need to swap the plugs. Fortunately the pins are the same so only the connector housings need to get swapped… The front connectors will have three wires running to them, while the new plugs are only expecting two. The middle back one (pin 3) is a ground that is not needed on the MK60." [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap) [read]
- **Tenza's 2004 Touring (2002 M3 donor), in order:**
  - 2021-04-25, first start, car stationary, brakes not yet bled: "I'm getting the ABS light is on, and I'm a little bit worried that the wheel speed sensors are what's causing that. So, the body side is non-M, but the hubs are M… physically, they're not anything different… If that is the case… cutting the harnesses and then just bringing over the pigtail" — then "I'm going to bleed the brakes. I'm going to bleed the clutch." [Tenza – build finally runs, 07:18](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=438s), [09:27](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=567s) [captions]
  - 2021-07-19: "the m3 runs different wheel speed sensors… they will not plug into each other… I ended up… putting in the non-m sensor into the same position… I have not had any issues with this yet I've only driven the car like 0.3 or 0.4 of a mile"; a bad sensor "will cause your traction control to be weird it'll cause your abs to go nuts it'll affect your speedometer". [Tenza – 5 things part 2, 03:20](https://www.youtube.com/watch?v=mDBiRn30fEs&t=200s), [04:00](https://www.youtube.com/watch?v=mDBiRn30fEs&t=240s), [05:00](https://www.youtube.com/watch?v=mDBiRn30fEs&t=300s) [captions]
  - 2021-10-20: "we've had some hiccups… mainly… a little bit of body damage" (no ABS mention). [Tenza (2021-10-20), 01:00](https://www.youtube.com/watch?v=O63Y52j-4PY&t=60s) [captions]
- **M3projekts (Hungary, facelift 318d Touring + M3 donor):** fitted the M3's ABS unit; "the speed sensor [yaw cluster]… everything is Plug and Play" — [M3projekts – Ep5 (2023-09-17), 20:00](https://www.youtube.com/watch?v=Ipbjt8S2c2g&t=1200s) [captions, manual English]. Not a US car.

### Inferences
- **Plug-in compatibility:** the Touring's own active sensors (or a 09/2002-on donor's) are the same part numbers BMW fits to the MK60 M3, read the M3's front hub pulse wheels and the M3 half-shafts' CV pulse wheels, and plug into the Touring harness. An M3 built before 09/2002 has inductive grey-plug sensors; don't use them or splice their pigtails.
- **Tooth count:** BMW says 2WD E46 rear pulse wheels give 48 pulses per revolution and that MK60 uses the MK20 pulse wheels; the M3 MK60 uses the same sensors on its own pulse wheels. No source gives the M3 front hub's count. The fault list contains exactly the checks that would catch a mismatch (long-term monitoring, double-frequency check), so a steady-speed wheel-speed comparison proves it.
- **Most likely causes of Tenza-type ABS lamps, and the test for each:**
  1. Faults stored during the build (sensors unplugged with the key on) → 0x5Dx0; the lamp stays until cleared and all four wheels are seen at drive-off. Test: read the fault memory, clear, drive above 20 km/h, read again.
  2. Sensor not seated or bore corroded on the donor knuckle/trailing arm → large air gap, weak low-speed signal → x3 or x1. Test: seat flush, ISA screw 8 Nm, check the reading at walking pace.
  3. Damaged or rusty pulse wheel (front hub, rear CV ring) or worn hub bearing → x2. Test: inspect; look for one wheel's speed fluctuating at steady speed.
  4. Wrong sensor type (inductive) or harness damage from the subframe swaps → x0. Test: 12 V supply at each plug with the key on; 7/14 mA current pulses with an ammeter in series while turning the wheel slowly (BMW's operating values).
  5. Mixed wheel/tyre sizes while testing (Touring 16s on one axle, M3 18s on the other) → x4; the M3's 18-inch tyres are about 4.4% larger in circumference than the Touring's 205/55R16 (our arithmetic: 225/45R18 ≈ 2,072 mm, 255/40R18 ≈ 2,077 mm, 205/55R16 ≈ 1,985 mm).
  6. Low fluid (unbled system) lights the red BRAKE lamp and switches off ASC/DSC, not the ABS lamp (BMW ST056) — not Tenza's lamp.
- **Pad-wear sensors:** the M3 front sensor is used on the US 325xi Touring, so it should plug into a Touring front connector (inference from ETK usage). The M3 rear sensor is M3-only; check its plug and lead length against the Touring's right-rear connector.

### Gaps
- No BMW resistance value for either sensor type; BMW's documents give operating currents/voltages only.
- No M3 front pulse-wheel tooth count found.
- No diagnosis of Tenza's light was ever published.

---

## Q5. Checks that prove the work

### Cited findings
- Massachusetts 540 CMR 4.04(4) and (6) as quoted above [read].
- BMW ST056: ABS above 12 km/h; pressure sensors <5 bar with the BLS off; DSC button short/long press behaviour; lamp meanings [read].
- BMW ST040: DIS "Connection Speed Sensor" and "Connection Brake Lines" tests [read].
- DSC_MK60 SGBD status jobs and fault list [read].
- NAM3: overnight pedal-wedged leak check; 20 psi air test on dry new lines (0.4 psi drop in 22 h accepted by that builder) [read].
- TIS 34 00 050: after the routine, five full pedal strokes give clear, bubble-free fluid [read, E70].

### Inferences (our arithmetic and suggested pass values)
- 20 mph = 29.3 ft/s. Stopping within 30 ft needs an average of about 14.3 ft/s² ≈ **0.45 g** from the moment the brakes apply; 80 ft on the parking brake needs about **0.17 g**. A healthy car with M3 brakes stops from 20 mph in roughly 15–17 ft (0.8–0.9 g). The M3 cluster over-reads about 9% (guide), so 20 mph true is about 22 mph indicated; use GPS.
- Wheel speeds: all four within about 1–2 km/h of each other at a steady 30–50 km/h, straight, same tyres all round (suggested pass value, ours).
- Steering-angle sensor: 0° with the wheel straight after calibration (guide); about ±540° at full lock (ours).
- Pressure sensors: both under 5 bar with the pedal released (BMW); both rise together when pressed (ours).
- Yaw ≈ 0 °/s and lateral ≈ 0 g at rest on level ground (ours).

---

## Guide-ready

### Parts tables

**Front axle** (US M3 coupe vs US 325i Touring from 02/2001; ETK)

| Item | M3 (fit) | Your Touring | Action |
|---|---|---|---|
| Front axle support | 31111096902 | 31111096902 | Keep yours or use the donor's |
| Subframe bolts M12×1.5×100 (4) | 31116781023 | same | Buy new (TIS: replace) |
| Thrust/reinforcement plate | 51717893609 + 12 × 31106772199 + jack pad 51717894027 | 51717028433 + 8 × 31106772199 | Donor plate; new screws; confirm all 12 threads at mock-up |
| Control arms | 31122229453 / 454 | 31122282121 / 122 | Donor (renew ball joints if worn) |
| Arm brackets / bushings | 31122229623 / 624, bushing 31122229857 (2) | 31126783376 set | Donor brackets; new bushings if worn |
| Bracket bolts M10×35-10.9 (4) | 33306760652 | same | Buy new ("always replace") |
| Arm nut at subframe M14 (2) | 31106774714 | same | Buy new |
| Ball-joint nut M12 (2) | 31106777806 | 32216769539 | Buy new M3 type |
| Struts | 31312283103 / 104 (coupe) or coilovers | 31312282101/102 etc. | Donor or new |
| Strut clamp bolt M12×1.5×55-10.9 (2) | 31306779487 | same | Buy new |
| Knuckles | 31212229855 / 856 | 31211096429 / 430 | Donor |
| Top mounts (handed) | 31332229165 / 166, plate 31332229427 | Touring support bearing | Donor or new M3 |
| Top-mount nuts M8 (6); rod nuts M14 (2) | 31316769731; 31106774714 | same | Buy new |
| Hubs | 31222229501 | 31226757024 | Donor; new collar nut 31211128336 if a hub comes off |
| Anti-roll bar 26 mm, mounts | 31352229755, 31352229756 | 31351097178 (23 mm) or 31351094542 (24 mm) | Donor bar, new mounts |
| Bar supports; end links | 31351094552; 31356780847 | same parts | Keep or new (same part) |
| Link nuts M10 (4); clamp nuts M8 (4) | 33306760587; 07119905374 | same | Buy new |
| Dust shields | 34112282109 / 110 | 34116750129 / 130 | Donor |

**Steering**

| Item | M3 | Touring | Action |
|---|---|---|---|
| Rack | 32132229397 (ZCP 32132282642 from 12/2004) | 32136755065 | Donor rack |
| Rack bolts/nuts | 32106781639 / 33306760587 | same | Reuse or new |
| Inner tie rods | 32112228785 / 786 | 32106777503 / 504 | Donor |
| Outer tie-rod ends | 32212229367 / 368 + nut 32216769539 | 32106774220 / 221 | Donor; new nuts |
| PS pump | 32412229679 (ZF) | LUK LF-20/30 | With the S54 |
| Suction hose | 32412229369 | 32416750155 | Donor |
| Pressure hose | 32412283893 | 32416774215 | Donor (or new) |
| Hollow bolts M16×28 (2) + rings A16×22 (4) | 32416852470 + 32411093597 | — | New rings |
| Rack banjo with check valve M14 + rings A14×20 (2) | 32416781261 + 32411093596 | same banjo | New rings |
| Return pipe; cooler; radiator return line | 32412282354; 17102282339; 32412282353 | 32416796367; 17111436262; 32416796390 | Donor |
| Reservoir, lid, bracket | 32416851217, 32416851332, 32411092940 + label 71246798132 "ATF" | same | Keep yours |
| Column, lower joint, coupling, Torx M8×33 | 32303450159; 32301094700 (to 11/03) or 32306764006 (from 11/03); 32301094703; 32306778609 | same | Keep; new Torx bolts |
| Steering-angle sensor | 32306793632 | same | Keep; calibrate after alignment |

**Brakes** (Option A: Touring MK60, booster and MC kept)

| Item | M3 | Touring | Action |
|---|---|---|---|
| Front calipers; carriers; carrier bolts | 34112282617/618; 34112282177 (ZCP 34112282619); M12×1.5×41 34111156989/34116767217 | 34116758113/114; 34106758120; M12×1.5×32 34116772428 | Donor; rebuild with 34111157037 |
| Front discs; pads; pad sensor | 34112229529/530 (325×28); 34112282416; 34356751311 | 34116864058 (300×22); 34116761244; 34351164371 | New M3 discs/pads/sensor |
| Rear calipers; carriers; screws | 34212282195/196; 34212229705; 34203414763 (M10×26.5, micro-encapsulated) | 34216758135/136; 34216758134; same screw | Donor; new screws; rebuild with 34211166238 |
| Rear discs; pads; pad sensor | 34212229379 (328×20); 34216761248; 34352229780 | 34216864056 (294×19); 34216778168; 34351164372 | New M3 parts; check sensor plug |
| Front hoses | 34322229723 (M3-only) | 34326766966 | Buy new M3 hoses |
| Front pipes | 34326759218, 34326755801, 34326752405, 34326752407 (from 09/2002) | same | Keep |
| Rear pipes, intermediate piece, hoses | 34326752409, 34326755704, 34326757282, 34326766825; hoses 34301165174 | same | Keep |
| Master cylinder | 34317838638 (from 09/02) | 34336785666 (from 02/2001) | Keep yours (Option A) |
| Booster | 34332282622 (from 09/02) | 34336779682 | Keep yours |
| Booster port grommet | 34336765316 | 34336765316 | Buy new |
| Booster check valve | 34331161300 (check valve support) | 34331160183 (non-return valve) + elbow 34336751108 | Fit the donor's 34331161300 in your booster |
| Jet pump and lines; air shut-off valve | 11617836745 (or 11617832989); 11617833212 | M54 parts | Donor, with the S54; shorten the booster hose to fit |
| Brake fluid | DOT 4 low viscosity (BMW 81220142156) | same | Buy about 1.5 L |

**Parking brake**

| Item | M3 | Touring | Action |
|---|---|---|---|
| Shoe kit; springs; adjusting screw | 34416761293; 34410034938; 34416851437 | 34416761291; 34410410823; 34416851438 | Donor or new M3 parts |
| Expanding lock; guide bush; nuts | 34416851439; 34411164583; 07146778500 | same | Reuse/new |
| Support (2) + bolts M8×22 (4) | 34411163978 + 34306772869 | — | Donor |
| Cables; lever; switch | 34411165020/021; 34411164489; 61311369771 | same | Keep |

**ABS/DSC hardware**

| Item | M3 from 09/2002 | M3 to 09/2002 | Your Touring (from 09/2001) | Action |
|---|---|---|---|---|
| Front sensors | 34526792896 (R) / 34526792897 (L), active, blue | 34521165609, inductive, grey | 34526792896/897 | Keep yours |
| Rear sensors | 34526752683 (short) | 34521164652 / 34521164370 | 34526752683 | Keep yours |
| Yaw/lateral sensor cluster | 34526764018 | separate MK20 sensors | 34526764018 | Keep |
| Steering-angle sensor | 32306793632 | 32306793632 | 32306793632 | Keep |
| Hydraulic unit / control unit | 34512282558 / 34522282559 | 34512229827 (MK20) | 34516765453 / 34526765455 | Keep yours (Option A) |

### Torque tables

**Front axle** (Flow = M3 compilation annotated with TIS values; D69 = Department 69 citing TIS for the E46)

| Fastener | Nm (ft-lb) | Condition | Source |
|---|---|---|---|
| Subframe to body, M12×1.5×100 10.9 | 110 (81) | New bolts; rear bolts first (dowels) | Flow p.2; D69 (replace) |
| Thrust plate, M10×35 10.9 (12) | 59 (44) + 90° (±30°) | New screws | Flow p.2; SI B11 04 04 |
| Arm ball pin to subframe, M14 nut | 90 (66) | New nut | Flow p.2; D69 |
| Arm bracket to body, M10×35 (4) | 59 (44) | New bolts; no ride-height condition in either source | Flow p.2; D69 |
| Ball joint to knuckle, M12 nut | 65 (48) | New nut; no impact wrench | Flow p.2; D69 |
| Strut to knuckle clamp, M12×1.5×55 | 81 (60) | New bolt | Flow p.4; D69 |
| Strut top mount to body, M8 (3 per side) | **24 (18) or 34 (25) — conflict** | New nuts | Flow p.3 (24); D69 and E85 TIS reader (34) |
| Damper rod nut, M14 | 64 (47) | New nut | Flow p.3; D69 |
| Front wheel-speed sensor screw, M6 | 8 (71 in-lb) | — | Flow p.4 |
| End-link nuts, M10 | 65 (48) | New nuts | Flow p.6; D69 |
| Anti-roll bar clamp nuts, M8 | 21 (15) | **At loaded ride height** ("tighten in normal position") | Flow p.6; D69 |
| Front hub collar nut | 290 (214) | New nut 31211128336 | Flow p.14; D69 |
| Wheel bolts | 120 ± 10 (89 ± 7) | — | Flow p.28; D69 |

**Steering and power steering**

| Fastener | Nm (ft-lb) | Condition | Source |
|---|---|---|---|
| Rack to subframe, M10 | 42 (31) | — | Flow p.7; D69 |
| Inner tie rod to rack, M3 | **110 (81)** | (Non-M: 100 Nm +10) | D69; Flow p.9 prints "100 + 10" |
| Outer tie-rod lock nut, M14 | 45 (33) | — | Flow p.9 |
| Tie-rod end to knuckle, M12 | 65 (48) | New nut; no impact wrench | Flow p.9; D69 |
| Lower joint Torx bolts, M8×33 | 22 (16) | New bolts | Flow p.12; D69; SI B11 04 04 |
| PS hollow bolts, M16 (pump outlet, rack) | 40 (30) | New A16×22 rings | Flow p.8 |
| Rack banjo with check valve, M14 | 35 (26) | New A14×20 rings | Flow p.8 |
| PS line bracket bolt, M6 | 8 (71 in-lb) | — | Flow p.8 |
| PS pump mounting bolts, M8×80 | 21 (15) | — | Flow p.11 |
| PS pump pulley bolts, M8×14 | 27 (20) | — | Flow p.11 |
| PS pump/bracket M8 self-locking nuts | 22 (16) | — | Flow p.8 note |
| Reservoir bracket / clamp | 22 (16) / 5.5 (49 in-lb) | — | Flow p.10 |

**Brakes**

| Fastener | Nm (ft-lb) | Condition | Source |
|---|---|---|---|
| Front carrier to knuckle, M12×1.5×41 | 110 (81) | — | Flow p.25; D69 |
| Caliper guide bolts, front and rear | 30 (22) | D69: 25–30 | Flow pp.24–25; D69 |
| Rear carrier, M10×26.5 micro-encapsulated | 65 (48) | New screws | Flow p.24; D69 |
| Brake hose / line into caliper | 19 (14) | — | Flow pp.24–25 |
| Bleed screws | 7 mm: 3.5–5; 11 mm: 12–16 | — | Flow pp.24–25 |
| Disc retaining screw | 16 (142 in-lb) | — | Flow p.23 |
| Dust-shield screws, M6 | 9 (80 in-lb) | — | Flow p.23 |
| MC to booster, M8 | 26 (19) | New nuts 07129906196 | Flow p.27; D69 |
| Booster to pedal bracket | 25 (18) | — | Flow p.26; D69 |
| DSC pressure sensor in MC | 25 (+5) | Option B only | Flow p.27 |

### Step-by-step procedures (in order), with checks

**A. Front axle (Phase 8, Card 8a)**
1. Before the subframe drops: plug every brake pipe end you open (strut-bracket unions, rear hose brackets) and keep the reservoir topped up; a pedal depressor holds fluid in the system. Goal: no air reaches the MK60.
2. Subframe: yours or the donor's (same part). New M12 bolts, 110 Nm, rear bolts first.
3. Bench-build each M3 corner: knuckle, hub (290 Nm new collar nut only if the hub came off), strut (new clamp bolt 81 Nm), top mount (handed L/R), rod nut new 64 Nm.
4. Control arms: ball pin into subframe, new M14 nut 90 Nm; bracket to body with new M10 bolts 59 Nm (any position); ball joint to knuckle, new nut 65 Nm, no impact wrench.
5. Strut tops: three new nuts per side (24 or 34 Nm — confirm in TIS for your parts); leave the camber pin in for a stock alignment.
6. Thrust plate: offer up the M3 plate; check all 12 threads before fitting; new screws 59 Nm + 90°. If any thread is missing, stop and fit your own plate (51717028433) with 8 screws.
7. Anti-roll bar: fit bar and mounts, new link nuts 65 Nm; clamp nuts snug only.
8. Wheel-speed sensors: your own; seat flush in the M3 knuckles, ISA screw 8 Nm; route leads through the strut brackets 34526780591/592; plug in (blue plugs).
9. **Check:** every fastener torqued and paint-marked except the bar clamp nuts; wheels spin freely; no lead or hose tension at full droop.
10. Later, with the car on its wheels at loaded ride height: bar clamp nuts 21 Nm. Then align (B9 below).

**B. Steering (Card 8b)**
1. Rack to subframe 42 Nm. Inner tie rods 110 Nm (M3). Outer ends: count turns from the donor's settings; lock nuts 45 Nm; tie-rod-end nuts new 65 Nm, no impact wrench.
2. Centre: wheel straight, rack centred, notch to the pinch-bolt hole; new Torx M8×33 22 Nm.
3. PS circuit: M3 suction hose (reservoir → pump), M3 pressure hose (hollow bolts 40 Nm, new rings), rack banjo with check valve 35 Nm, return pipe → M3 cooler coil → radiator return line → reservoir. Keep lines clear of the anti-roll bar and sump.
4. **Check (Massachusetts 540 CMR 4.04(6)):** full lock each way, no binding or interference (also tyres vs arch liners and lines).
5. Fill with ATF (Dexron III type), engine off, to about 25 mm below the reservoir edge (TIS 32 13 006); start, top up evenly; full lock each way twice, without holding at lock (the M3 rack has no hydraulic stops); switch off and set to the lid mark.
6. **Check:** no foaming or groaning after a short run; no weeps at the hollow bolts or banjo; level stable after a drive.
7. Align at the car's loaded ride height (TIS 32 conditions; BMW ST056: 68/68/68/21 kg plus a full tank for most cars, while the M3 spec is usually set unladen — tell the shop which one you used). **Pass:** E46 M3 values; caster in the M3 window without adjustment (it isn't adjustable).
8. Then calibrate the steering angle (other researcher's procedure). **Check:** 0° straight; about ±540° at full lock.

**C. Brakes and booster (Card 8c)**
1. M3 calipers on M3 carriers: front carriers 110 Nm (M3 M12×1.5×41 bolts), rear carriers 65 Nm with new micro-encapsulated screws; guide bolts 30 Nm; discs with screw 16 Nm; pads with paste and pad sensors (front sensor to the left-front connector, rear to the right-rear).
2. Front hoses: new M3 hoses 34322229723 from your pipe ends (unchanged) to the calipers, 19 Nm at the caliper. Rear: your hoses 34301165174 to the M3 calipers.
3. **Check:** every hose free of tension and rubbing at full lock both ways and full droop.
4. Booster vacuum: new grommet 34336765316 in your booster; fit the donor's check valve 34331161300 so it points toward the S54; blow test (air passes only from booster toward engine). Connect the donor's jet-pump hose; shorten or re-route it if needed and secure with clamp 11151726340. The jet pump and DME-controlled air shut-off valve 11617833212 come with the S54.
5. **Check (once the engine runs):** `STEUERN_VENTIL_SAUGSTRAHLPUMPE` clicks the valve; engine off, pump the pedal until hard, hold about 25 lb, start: the pedal must drop slightly (540 CMR 4.04(4)(c)2).

**D. Filling and bleeding**
1. Fluid: DOT 4 low-viscosity (BMW 81220142156); have about 1.5 L.
2. If the MK60 never ran dry: conventional bleed, pressure bleeder at no more than 2 bar (29 psi), order RR, RL, FR, FL, then the clutch, each until clear and bubble-free (TIS 34 00 050 sequence; NAM3).
3. If the MC, the hydraulic unit or the lines between them were opened or ran dry: conventional bleed first, then INPA's MK60 routine (F6 → F1 → F2 for FL/RL, F3 for FR/RR), pedal pressed firmly, 2–3 runs per corner; finish with five full pedal strokes per bleeder per TIS and a final conventional pass.
4. Set the level to MAX; check the cap's rubber seal.
5. **Checks:** (a) pedal high and firm with the engine off; (b) static leak test: 125 lb on the pedal for 10 s, pedal height holds and at least 20% of travel remains (540 CMR 4.04(4)(c)1), then pedal wedged overnight with no weeps at any union (NAM3); (c) `STATUS_SENSOREN`: both pressure circuits under 5 bar released, both rising together when pressed; (d) red BRAKE lamp off with the parking brake released.

**E. Parking brake**
1. Release the cable nuts at the lever (BMW tool 34 1 030 or console off). Through a wheel-bolt hole, expand each adjuster until the wheel locks (left side up, right side down per BimmerWorld), then back off 8 notches (TIS, model not identified) to 10 teeth (E46 manual; BimmerWorld).
2. Work the lever several times; set the cables so the wheels still turn by hand at 4 teeth (E46 manual) or are locked by the 4th tooth (TIS) — the checks below decide.
3. **Checks:** released: both wheels free, red lamp off; 1 tooth: no braking; 2 teeth: lamp on (E46 manual).
4. Bed in: at 40 km/h apply gently until braking is felt, one more tooth, 400 m, release and cool (E46 manual); for new shoes, ECS's 10 light + 10 medium stops from 20 mph. Your brake lights don't come on; use an empty road.
5. **Checks (Massachusetts):** in first gear at 1,200–1,300 rpm against the applied parking brake the car doesn't move; from 20 mph the parking brake alone stops within 80 ft (about 0.17 g).

**F. ABS/DSC hardware checks**
1. Key on: ABS, DSC and yellow BRAKE lamps light, then go out after start-up and the first few metres (expect them on until faults are cleared after the build).
2. Read the fault memory; note any 0x5D9x/5DAx/5DBx/5DCx (wheel sensors by wheel), 0x5E1F (VIN not initialised), 0x5E5D/5E5E (fluid switch, brake-light switch). Clear.
3. Car on stands: spin each wheel by hand in turn and confirm the matching channel in `STATUS_RADGESCHWINDIGKEIT` (VL, VR, HL, HR). If a sensor looks dead: 12 V at its plug with the key on; current toggling about 7/14 mA when turning slowly (BMW).
4. `STATUS_SCHALTER`: brake-light switch, parking-brake switch, DSC button and fluid switch each change state as operated.
5. Road: steady 30–50 km/h straight on matching tyres, all four wheel speeds within about 1–2 km/h; read faults again (none).
6. ABS: a firm stop from above 30 km/h on a loose or wet surface; the pedal pulses and the car stays straight (ABS works above 12 km/h). DSC button: short press lights DSC, long press (>2.5 s) lights DSC and yellow BRAKE; another press restores and the lamps go out.
7. If anything fails, use the fault meanings in Q4 to choose between wiring (…0), seating/air gap (…1/…3), pulse wheel (…2) and tooth count or tyre size (…4/…5).

**G. Pre-inspection run (matches 540 CMR 4.04(4))**
1. 4–8 mph stops: no pull either way.
2. From 20 mph true (GPS; about 22 mph on the M3 cluster): service brake stop within 30 ft (needs about 0.45 g; expect about 15–17 ft). Mark the brake-application point and measure.
3. Parking brake: holds in first at 1,200–1,300 rpm; stops from 20 mph within 80 ft.
4. 125 lb pedal for 10 s; ≥20% travel left; booster drop test passes.
5. No brake-related lamp lit (red and yellow BRAKE, ABS, DSC); no leaks, chafing or loose lines; full lock without binding; no ball-joint play.

### Diagram-ready data

**Brake hydraulic layout (US 325i Touring MK60 from 09/2000 = US M3 MK60 from 09/2002; ETK and BMW ST056)**

Nodes: Reservoir (34326750798, cap with level switch 34326752698; clutch feed pick-up) · Tandem MC (34336785666; two outlets; two pressure sensors 34521164458 below the outlets; front/rear split) · MK60 hydraulic unit/control unit (left side under the MC; 2 inlets, 4 outlets; 4 inlet + 4 outlet valves, 2 changeover, 2 intake valves, return pump) · four calipers · clutch master/slave.

| Edge | Part | Ends | Notes |
|---|---|---|---|
| MC outlet 1 → HU inlet | 34326759218 "Pipeline with pressure hose" | M12 / M12 | Flexible section |
| MC outlet 2 → HU inlet | 34326755801 "Pipeline with pressure hose" | M12 / M12 | Flexible section |
| HU → left-front hose | 34326752405 pipe, 590 mm | M12 (HU) / M10 (hose) | Short; HU is on the left (inference from ST056 + lengths) |
| HU → right-front hose | 34326752407 pipe, 2,246 mm | M10 / M10 | Crosses to the right |
| Front pipe → caliper (×2) | 34322229723 hose (M3) | M10 union at strut-bracket clip 34341163565 / male into caliper (19 Nm) | Touring's own hose 34326766966 not used |
| HU → rear hose, side A | 34326752409 pipe, 3,684 mm | M12 (HU) / M10 (hose) | Runs along the floor |
| HU → rear, side B | 34326755704 pipe, 3,798 mm → 34326757282 union (M10×1) → 34326766825 pipe, 1,206 mm | M10 / M10 | Crossover to the far side; which side is A or B isn't stated in the sources |
| Rear pipe → caliper (×2) | 34301165174 hose | At bracket 34301164003 (M6×12 bolt) with retaining spring 34306771981 / into caliper | Same on both cars |
| Reservoir → clutch MC | Clutch feed (Touring part) | — | Bleed after the brakes |
| Pressure sensors | 2 × 34521164458 on MC | MK60 pins 18–20 and 21–23 | Must read <5 bar with the brake light switch off |

**Wheel-speed sensor wiring (MK60, 47-pin plug; active sensors, 12 V supply from the MK60, 7/14 mA current pulses, blue plugs)**

| Wheel | Sensor (Touring = M3 from 09/02) | Wires | MK60 pin (supply / signal) | TIS colour (supply / signal) | Fault codes |
|---|---|---|---|---|---|
| Front left | 34526792897 | 2 used (MK20-era harness had a 3rd ground, pin 3, unused on MK60) | 45 / 46 | BR/RT / BR | 0x5D90–5D95 |
| Front right | 34526792896 | 2 | 34 / 33 | GE / BR | 0x5DA0–5DA5 |
| Rear left | 34526752683 (short) | 2 (case ground) | 36 / 37 | BL / BR | 0x5DB0–5DB5 |
| Rear right | 34526752683 (short) | 2 (case ground) | 43 / 42 | GE/SW / GE/BR | 0x5DC0–5DC5 |

Outputs: processed rear-right speed, pin 8 → DME X60004-22; processed rear-left speed, pin 10 → cluster pin 19; all four speeds also on CAN. Other MK60 pins in this circuit: ABS lamp 44 → cluster 22; brake-light switch 41; parking-brake switch 27; fluid level 9; DSC button 39; sensor cluster 6/24/25/29 (CAN pair 25/29); KL30 1 and 32 (2.5 mm²); ground 16 and 47 (2.5 mm²); KL15 4; CAN 11 (high) / 15 (low). Pulse wheels: front on the M3 hub; rear on the M3 half-shaft outboard CV joint (48 pulses/rev on 2WD E46, BMW). Steering-angle sensor plug: 1 KL30, 2 KL87, 3 CAN high, 4 CAN low, 5 KL31, 6 TXD. (Pin data from heinzboehmer's TIS-derived mapping via the earlier note; colours as printed there — verify against your car's wiring diagram.)

**Booster vacuum circuit (S54 in the Touring)**

S54 air collector (upstream of the throttles) → hard line → **air shut-off valve 11617833212** (DME output; energised = closed, de-energised = open, i.e. extra vacuum) → **suction jet pump** (in assembly 11617836745) → idle-air/vacuum side · jet-pump suction port → hose (shortened as needed) → clamp 11151726340 → **check valve 34331161300** → grommet 34336765316 → **Touring booster 34336779682** (vacuum chamber).

**Power-steering circuit (M3 parts in the Touring)**

Reservoir 32416851217 (label "ATF") → suction hose 32412229369 → ZF pump 32412229679 (max 120 bar, 11 L/min) → hollow bolt M16 (40 Nm) → pressure hose 32412283893 → hollow bolt M16 (40 Nm) at the rack 32132229397 → rack return via banjo bolt with check valve M14 (35 Nm) → return pipe 32412282354 → cooling coil 17102282339 (in front of the radiator) → radiator return line 32412282353 → reservoir.

---

## Guide statements this research corrects

1. README, Front axle and steering, step 2: "Arm bracket to body: new M10 bolts, 59 Nm, at ride height." — **Correction:** neither BMW-derived source puts a ride-height condition on these bolts (Flow p.2: "59 Nm (always replace)"; Department 69: 59 Nm). Torque them on stands. The only front joint marked "tighten in normal position" is the anti-roll-bar clamp (21 Nm).
2. Appendix, Front axle and steering: "Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts; at ride height" — **Correction:** "New bolts" only. Same change in Card 8a ("New bolts; at ride height") and Card 12d (move this row out; keep the bar clamp nuts).
3. Phase 8 step 6 and Card 8a: "Leave the front rubber-bushed joints snug. You torque them at ride height once the engine is in (Phase 12)." — **Correction:** only the front anti-roll-bar clamp nuts wait for ride height.
4. Appendix: "Inner tie rod to rack | 100 + 10 Nm, as the compilation prints it | Check TIS for what the "+ 10" means" — **Correction:** TIS via Department 69: non-M 100 Nm +10 Nm; **M3: 110 Nm (81 ft-lb)**. Same change in Card 8b.
5. Appendix: "Strut top mount to body, M8 collar nuts | 24 Nm (18 ft-lb)" — **Correction:** flag a conflict: TIS for the non-M E46 (Department 69) and the E85 Z4 (owner reading TIS) give 34 Nm; the M3 compilation gives 24 Nm. Check TIS for your parts; fit new nuts (Department 69: replace).
6. Appendix: "Front axle support (subframe) to body, M12 10.9 | 110 Nm" with no note on reuse — **Correction:** add "new bolts 31116781023" (TIS via Department 69: "Replace bolts").
7. Appendix, Engine: "Crank pulley bolts; power-steering pump bolts | 23 Nm (17 ft-lb) | One video only" — **Correction:** for the PS pump, the M3 compilation gives mounting bolts M8×80 **21 Nm** and pulley bolts **27 Nm**; add PS hollow bolts M16 40 Nm and the rack banjo M14 35 Nm.
8. Fluids and capacities: "Power steering | **Not found.** Read the cap on the donor's M3 reservoir (ATF or CHF 11S)…; BimmerWorld lists CHF 11S for no E46" — **Correction:** ATF (Dexron III type). ETK pairs the (CHF-type) reservoir with the "ATF" label 71246798132 on both the US M3 and the US 325i Touring; FCP Euro says BMW's OE fill for pre-2006 cars without active steering was ATF Dexron III; M346 filled its Touring/M3 build with ATF. Don't mix with CHF 11S. Same change in "Brakes and bleeding → Power steering".
9. Fluids and capacities: "Brake and clutch fluid | **Not found.** Check the reservoir cap and TIS" — **Correction:** DOT 4 low-viscosity for MK60 cars (BMW TIS bleeding instructions, 2005: DSC without pre-charge pump; BimmerWorld; BMW 81220142156).
10. Brakes and bleeding, step 2: "BMW's limit for bleeder pressure is reported as 2 bar ([BMW TIS 34 00 050]…, unverified)" — **Correction:** confirmed: "Connect bleeder unit with max. 2 bar filling pressure… Charging pressure should not exceed 2 bar" (TIS 34 00 050, read in its E70 printout; the E46 M3 version gives the same limit per snippet). Link the readable copy: xoutpost.com.
11. Phase 8 step 5 and Card 8c: "test new hard lines with low-pressure air first, about 20 psi" and "Air test holds" — **Correction:** with Option A no hard line changes (same pipes on both cars); don't blow air through a filled MK60 (it makes the INPA routine necessary). Cap open pipe ends during the swap and prove the system with the static pedal test: 125 lb for 10 s with ≥20% travel left, then the pedal wedged overnight with no weeps (NAM3). Keep the air test only for new, dry hard lines.
12. Parts list, Brakes and DSC: "Booster vacuum hose | Donor M3 | On the M3 it meets the booster from the other side…; check its route to your booster at mock-up" — **Correction:** fit a new grommet 34336765316 (same part on both cars) and the donor's check valve 34331161300 (BMW fitted it to your booster part on M52 E46s, the 323i Touring included), then shorten or re-route the donor's jet-pump hose to it, as Tenza, Import Modify and heinzboehmer did. Same in the DSC section's Option B paragraph.
13. DSC, brakes and steering angle, Option A: "Nobody has reported the pedal feel of M3 calipers on the Touring's master cylinder. Bleed, test and judge." — **Correction:** your MC (34336785666) is the 330i's; reported sizes give about 10% longer, lighter front-circuit pedal travel than a real M3 (forum dimensions, our arithmetic); M346's 2004 Touring with M3 brakes reported a "nice and firm" pedal after a manual plus INPA bleed (MC origin not stated).
14. DSC, brakes and steering angle, Wheel-speed sensors: "non-M sensors in the M3 hubs gave an ABS light at first start that was never diagnosed" (and the Driveline section's "had an ABS light at first start with its own sensors in the M3 hubs that was never diagnosed") — **Correction:** the lamp was seen at the first start, stationary, before the brakes were bled; in July 2021 the builder said he'd "not had any issues with this yet" after 0.3–0.4 mile, and his October 2021 video mentions only body damage. It isn't evidence that the sensors don't suit; ETK lists the identical sensor part numbers for the Touring and the 09/2002-on M3.
15. Troubleshooting: "ABS lamp after the first drive | An MK20 donor's wheel-speed sensors, or a sensor not seated" — **Correction:** add faults stored during the build (clear and drive), a damaged pulse wheel, and mixed tyre sizes; read the fault number (0x5D90–0x5DC5, last digit 0 wiring, 1/3 seating, 2 pulse wheel, 4/5 tooth count or tyre size).
16. Massachusetts table: "Brakes | The red brake warning lamp stays off, and the car stops from 20 mph within 30 ft… | A DSC or ABS fault that lights the red lamp fails" — **Correction:** BMW's red BRAKE lamp means low fluid or parking brake on; DSC/ABS faults light the yellow BRAKE, ABS and DSC lamps (ST056). The inspection also tests: parking brake holds in the lowest gear at 1,200–1,300 rpm, parking-brake stop from 20 mph within 80 ft, no pull at 4–8 mph, 125 lb pedal hold for 10 s with ≥20% travel, the booster drop test, and lines/hoses for leaks or chafing (540 CMR 4.04(4)). Get all brake lamps dark.
17. Wheel alignment: "Forum citations of TIS for other BMWs give that as 68 kg in each front seat… (unverified, not confirmed for the E46)" and Open questions: "BMW's 'normal loaded position' weights for the E46" — **Correction:** BMW ST056 (2003) gives 68/68/68 kg plus 21 kg in the trunk and a full tank as the normal weight "for most vehicles", but says the E36/E46 M3 is "usually measured without any weight"; TIS 32 "Normal Position/Inspection Conditions" decides. Ride height is measured from the rim's lower edge to the wheel housing's lower edge (TIS groups 31/33).
18. Brakes and bleeding, Parking brake step 1 and "BMW's own figures are in TIS group 34 41" — **Correction:** add the cable and lamp checks (released: free and lamp off; 1 tooth: no braking; 2 teeth: lamp on — E46 manual) and the run-in (40 km/h, apply until felt, one more tooth, 400 m, cool — E46 manual). A TIS printout of unknown model backs off 8 notches; the E46 manual and BimmerWorld say 10.
19. Parts list, Front axle and steering: "Front sway bar and end links | Donor M3 | Fit new end links" — **Correction:** the end links are the same part on both cars (31356780847; ST041: "adopted from the E46/2"), so new links needn't be M3 parts; only the bar (26 mm) and its mounts are M3.
20. Parts list, Front axle and steering: "Steering-shaft lower joint 32301094700 | Keep | Same part on both cars" — **Correction:** add that both cars changed to 32306764006 from 11/2003; keep whichever your car has.
21. Front axle and steering, steering ratio: the table gives only rack data — **Add:** the 2003 US 325i Touring's overall ratio is 13.7:1 (BMW USA), so the M3's 15.4:1 rack and knuckles make your steering about 12% slower, same 3.0 turns, turning circle 36.1 ft vs 34.4 ft.
22. Open questions, Chassis and brakes: "What the Flow compilation's '100 + 10 Nm' (inner tie rod)… mean[s]", "The power-steering fluid for the M3 rack…, and the brake-fluid specification", "BMW's limit for pressure-bleeder pressure", "How the S54's brake-booster vacuum hose reaches the Touring's booster port" — answered above (110 Nm for the M3; ATF; DOT 4 LV; 2 bar; M3 check valve in your booster grommet plus a shortened hose). "Why one 2004 Touring's own wheel-speed sensors gave an ABS light" — answered as far as sources allow (item 14).
