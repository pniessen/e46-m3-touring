# S54 cooling system and air conditioning in a US E46 325i Touring

*Scope: a 2003 US 325i Touring (M54, 5-speed manual, IHKA or IHKR) receiving a 2003–06 US E46 M3 drivetrain (S54, MSS54/MSS54HP) with the M3 front end, radiator, fans, oil cooler, expansion tank and A/C compressor; the Touring keeps its heater box (heater core, evaporator, expansion valve). E46 only; anything from another model is flagged. Researched 22 Oct 2026.*

*Reading key. **[read]** = I downloaded the page or PDF and read it as text in this session. **[read, image]** = read from a diagram, scanned table or photo. **[read, earlier copy]** = a file saved by an earlier research round, read by me now. **[notes]** = taken from the earlier research notes in this repository (their own source tags apply). **[snippet]** = seen only in a search-engine result. Source classes: **BMW** (training manuals mirrored on archive.org, owner's manuals, Service Information bulletins hosted by NHTSA), **ETK** (BMW parts catalog via bmwfans.info, US-market catalogs, "L-N" = left-hand drive, all gearboxes), **WDS** (BMW wiring-diagram system mirror wds.psjr.org), **SGBD** (community export of BMW EDIABAS module descriptions), **Flow** (the guide's compilation of 2016–17 RealOEM printouts of the European E46 M3 catalog, with torque call-outs), **vendor**, **forum**, **DIY page**.*

*Access limits met (not worked around): e46fanatics.com and bimmerfest.com serve a bot check; newtis.info, m3post.com, forums.pelicanparts.com, bimmerforums.com and zhpmafia.com returned 403; YouTube returned "429 Too Many Requests" and then "Sign in to confirm you're not a bot", so no new captions were fetched and the fetch was stopped; Reddit returned 403. The session's shared web-search budget ran out part-way through, so later lookups used only known URLs. BMW TIS 17 00 (the S54 fill-and-bleed text) was therefore still not read.*

*Downloads are in `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/round4-dl/cooling-ac/` (one folder per source); nothing was executed.*

---

## Takeaway (what changes in the guide)

1. **Coolant capacity found.** BMW's US owner's manuals for the 2002 and 2003 M3 give **"Cooling system including heater circuit approx. 9.9 (approx. 9.3)" quarts (liters)** and **approx. 9.8/9.3** respectively. The 2001 manuals print 6.0 L and 6.7 L (with other obvious oddities) and the 2004–05 manuals drop the line, so use **9.3 L (9.8 US qt)** and fill by level. At BMW's 50 % mix that is about 4.7 L of BMW antifreeze (82141467704 is the 1-gallon jug) plus 4.7 L of water.
2. **Fill and bleed: BMW's documented elements are now in hand, but TIS 17 00 itself still isn't.** The S54's bleed screw (vent screw 17111712788, **2.5 Nm**) sits in water hose 11537830716; the system cap on the M3 expansion tank is **2.0 bar**; the thermostat opens at **80 °C**. BMW's own fill rule for cars with an auxiliary water pump is "turn on ignition, blower low, heating at maximum… This ensures that the heater valves are fully opened and the auxiliary water pump starts", fill slowly, don't overfill, check cold (≤30 °C). The guide-ready procedure below combines these with the M3 owner's manual level check and one M3 DIY (key on, the heater pump audible, ~2 US gal before coolant reaches the bleeder, about two heat cycles).
3. **The fans are a bigger change than the guide says on a manual Touring.** ETK lists the mechanical fan, its coupling and its shroud for the 325i Touring **only "for vehicles with automatic transmission"**; a manual 325i Touring has an **electric fan inside the radiator shroud** (17117561757, 390 W), and WDS shows the DME's one electric fan (M9) with its plug X82 **on that shroud**. The M3 has a **viscous fan** (fan 11521712058 + coupling 11527831619, left-hand thread, 40 Nm; on at 92 °C, off at 60 °C) plus an electric **pusher fan in front of the condenser** (64546988914). The DME pin doesn't move (X60004 pin 4), but the X82 lead must reach the pusher fan, so plan to extend or re-route it. Whether manual Tourings also carry a pusher fan isn't settled (ETK lists 64546988913 for the 325i Touring with no gearbox note); look at the car.
4. **Radiator support: everything bolts to the Touring.** Both cars use front panel 51717111691, radiator supports 41118199613/614 and the same radiator mounting kit (supports 17117530252/254, gaskets 17111436247/249, brackets 17117514402 ×2 and 17111436264 ×2, rubber buffers 17111178412 ×2). The M3 radiator (17102228941, no drain plug), shroud (17112228943 + air ducts 17112228945/946), oil cooler set and pusher fan are M3-only parts from the donor. Only the expansion tank needs body work (brackets welded or rivnutted, per earlier build notes).
5. **A/C: almost every refrigerant part is common.** Condenser 64538377614, condenser-to-drier hose 64536904013, drier 64538377330, drier-to-evaporator hose 64536909448, double pipe 64536908907, suction pipe 64536923956, pressure sensor 64539181464, expansion valve 64503452759, evaporator 64119135744 and the compressor bracket 64551432237 are the same part numbers on the US M3 and the US 325i Touring. **Only the compressor-to-condenser pressure hose differs** (M3 64536902681, non-M 64536984883). Keep the Touring's lines and fit the donor's pressure hose. **64536917658 is the drier's bracket, not an alternative drier**, so the guide's "drier 64538377330 or 64536917658" is wrong.
6. **Charge and oil (no BMW figure read; the car's label rules).** MAHLE's 2021–22 fill-quantity handbook lists the E46 petrol engines **including the S54**, 1998–05, at **715–765 g R134a**, OE oil **PAG**, **150 ml** for the whole system. An E46 M3 owner's DIY says "25–27 oz". BMW's generic A/C service rules: evacuate **at least 30 minutes**, then a 5-minute hold in which more than **2 in Hg** of change means a leak; replace the drier if the system was open over 24 h; when swapping a compressor, refill it with the old compressor's oil quantity **+ 10 g**; add 2 oz for a new condenser or evaporator and 1 oz for a new receiver-drier.
7. **Control and checks.** The chain (IHKA/IHKR → K-bus → cluster → CAN → DME X60004-29 → relay K19 → clutch) is unchanged from the earlier notes. New: both IHKR46 and IHKA46 carry a coded **compressor transport lock (`KOMPRESSOR_SPERRE`)**, so read `CODIERUNG_LESEN` if the compressor never engages. IHKR + MSS54 still has no first-hand report; the one documented A/C success (Kalim, 2003 325i Steptronic) was IHKA, with the 325i's own compressor kept and "a different A/C belt".
8. **Pass values for the shakedown now exist** from BMW: cooling pressure test at the 2.0 bar cap rating, held 15 minutes (BMW's practice on a later model); thermostat 80 °C; overheat lamp 120 °C; the A/C efficiency test (evaporator ≤ 15 °C within 3–4 min); normal pressures **1–2 bar low / 10–15 bar high**; vent air 40–68 °F, at least 20 °F below ambient; BMW's refrigerant-pressure-to-fan-stage table (8 bar = stage 0 … >24 bar = stage 15, below 50 mph).
9. **Law.** EPA (pages updated 2026): no one may vent; anyone servicing MVAC **for payment** needs Section 609 certification and approved equipment; refrigerant in containers over 2 lb may be sold only to 608/609-certified technicians, while **small cans of R-134a (≤2 lb, self-sealing valve) can still be sold to DIYers**. Nothing Massachusetts-specific was found (earlier round read MassDEP's HFC rule, which has no MVAC category).

---

## Q1. Cooling parts on the Touring

### Cited findings

**Radiator and its mounting (ETK).**
- US M3 "Radiator/frame": radiator **17102228941** ("43/9,4/66", 4.9 kg), fan shroud **17112228943**, air duct left **17112228945**, right **17112228946**, expanding rivets 17111712963 ×3, supporting parts **17117530252** and **17117530254**, gaskets left/right **17111436247/17111436249**, brackets **17117514402** ×2 and **17111436264** ×2, rubber buffers **17111178412** ×2, screws 17117536971 ×4 and 17117536972, bracket fan housing 17112282209 — [ETK M3 radiator/frame](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/radiator/radiator_frame/) [read]. The radiator is listed only for the US M3 coupe and convertible, from Jul '00 — [ETK 17102228941](https://bmwfans.info/parts-catalog/17102228941/) [read].
- US 325i Touring "Mounting parts f radiator": radiator **17119071518** "for vehicles with air conditioning S530A or automatic air conditioning S534A and manual transmission, to May '05" (17119071517 from May '05; 17119071519 for automatics); radiator adjusting screw, manual gearbox 17111437359; drain plug 17111437361; lower seal 17111436245; and the same rubber buffers, brackets, gaskets and supporting parts as the M3 (17111178412, 17111436264, 17111436247/249, 17117530254/252, 17117514402) — [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/radiator/mounting_parts_f_radiator/) [read].
- Both cars list front panel **51717111691** and "Support for left/right radiator" **41118199613/41118199614** — [ETK M3 front body parts](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/front_body_parts/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/front_body_parts/), [M3 left brackets](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/front_body_bracket_left/), [Touring left brackets](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/front_body_bracket_left/) [read].
- The M3 radiator has no drain plug: "it says 'Open the radiator drain plug' which does not exist on the M3"; drain the radiator at the lower hose, and the block at its drain plug (13 mm, new 14 mm crush washer, "18 ft-lbs") — [Blankowski, E46 M3 coolant change DIY (undated)](https://blankowski.com/Cars/m3_coolant_change/) [read].

**Fans.**
- US M3 "Cooling system-fan/fan coupling": fan 11 blade **11521712058** (D = 420 mm), fan coupling **11527831619**, screws 07129905536 ×3, pulley **11517840403**, bolts 07119904517 ×4 — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/cooling_system_fan_fan_coupling/) [read]. The RealOEM page in Flow adds: "Fan clutch to water pump 40 Nm / 29.5 ft lb **Reverse thread!**", "Radiator cooling fan to coolant pump 40 Nm", 10 Nm for the fan and pulley screws, "**Switch-on temperature 92 °C, Switch-off temperature 60 °C**, Tilt play of bearing (with dia. 120 mm) ± 0.65 mm" — [Flow p.61](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) [read, image, earlier copy]. Coupling 11527831619 is listed for the US E46 M3 and the S54 Z3 M (and some older sixes) — [ETK](https://bmwfans.info/parts-catalog/11527831619/) [read].
- US 325i Touring "Cooling system-fan/fan coupling": the 11-blade fan 11521712058, the coupling **11527505302** and its screws are marked **"For vehicles with Automatic transmission S205A"**; only the pulley 11511436590 has no note — [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/cooling_system_fan_fan_coupling/) [read].
- US 325i Touring "Fan shroud": item 1 shroud **17111436259** "for vehicles with automatic transmission and (automatic) air conditioning"; item 2 **"Fan housing with fan" 17117561757, 390 W**; item 3 fan shroud 17117511168 "only applies to Bosch" or 17117507604 "only applies to Siemens" — [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/radiator/fan_shroud/) [read]. The group drawing shows item 1 as an empty shroud and item 2 as a shroud carrying an electric fan motor — [ETK drawing](https://ills.bmwfans.info/a2tf.png) [read, image]. 17117561757 is listed for the US 325i Touring (and other US E46 sixes) — [ETK](https://bmwfans.info/parts-catalog/17117561757/) [read].
- "Pusher fan" groups: US M3 **64546988914** (old 64546928032) + compression shroud **64546905077** + upper grid 64548377800 + hex nuts 07129900546 (BM8) ×4 + 3-pole housing 61138380380/terminal 61138380385; US 325i Touring **64546988913** (old 64546922554) + compression shroud 64548377795 + upper grid 64548377800 + lower grid 64548385345 + the same connector parts, **no gearbox note** — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/pusher_fan/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/pusher_fan/) [read].
- WDS: the electric fan is **M9**, plug **X82** "(4-pin, black), Electric fan", location "front of engine compartment"; the location photo shows the fan motor and its power stage **inside the radiator shroud**, X82 at the shroud's upper edge — [WDS M9/X82](https://wds.psjr.org/en/e46/zinfo/E46_EM9A.htm) [read, image]. The circuit is the same for all petrol DMEs: X82 pin 2 ← DME X60004 pin 4 (0.5 SW/GN), pin 4 ← F37 50 A (6.0 RT/BL), pin 1 ground (6.0 BR); radiator-outlet sensor on X60004 pins 38/39 — [SP0000011770 (to 2003_03)](https://wds.psjr.org/en/e46/svg/SP0000011770.svg), [SP0000019629 (Saloon/Compact/Touring from 2003_03)](https://wds.psjr.org/en/e46/svg/SP0000019629.svg), [SP0000019630 (Coupe/Convertible)](https://wds.psjr.org/en/e46/svg/SP0000019630.svg) [read].
- One S54 Touring build replaced both M3 fans with a single electric fan — [Tracks and Trails – Attempting to Drive my BMW E46 M3 Touring (2026), 1:02:40](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=3760s) [notes]. An E46 automatic owner replaced the mechanical and auxiliary fans with one OEM electric fan "with no wiring or fitment changes", and the same thread says this "is not recommended for the M3 cars" — zhpmafia/e46fanatics [snippet only; page blocked].

**Expansion tank (ETK + builds).**
- US M3 "Expansion tank/tubing": tank **17112283344**, cap **17117639022 "2,0BAR"** (old 17111742231), level switch **17137553919** (old 17137524812), hose 17222246036 (L = 500 mm), holder **17112229108**, grommets 17112229059 ×2, expanding nut 64121379221, screws 07119901587 ×2, connecting line 17112229053, cap 17121719356, hose clamp 32411712735, tubing supports 17112228439 ×2, 2-pole housing 61138365340 or repair kit 61132359999 — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/radiator/expansion_tank_tubing/) [read]. 17112283344 replaced 17112228944, "exchangeable retrospectively"; holder 17112229108 is M3-only — [ETK 17112283344](https://bmwfans.info/parts-catalog/17112283344/), [17112229108](https://bmwfans.info/parts-catalog/17112229108/) [read].
- US 325i Touring "Expansion tank, manual transmission": mounting plate 17111436250, screw plug 17111707818, tank **17117573781**, clamp 17111707777, the **same level switch 17137553919, cap 17117639022 (2.0 bar) and 2-pole connector parts** — [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/radiator/expansion_tank_manual_transmission/) [read].
- Side of the engine bay: "the expansion tank moves to the passenger side" (UNRIVALED, US sedan) and "from the left side to the right" (M3projekts, LHD) — [notes: youtube_swap_wiring_coding.md, lines 103, 115, 182]. The M3 DIY: the expansion tank is "on the right side of the engine" — [Blankowski](https://blankowski.com/Cars/m3_coolant_change/) [read]. Bracket fixes on Tourings: welded on (Tracks and Trails), or Hungarian-made brackets fitted with rivnuts (M346) — [notes: youtube_conversion_builds.md line 266; youtube_swap_wiring_coding.md line 137].
- M3-only body brackets on the right front structure: secondary-air-pump brackets 41147894115 (front) and 41147894116 (rear) and "Bracket ABS+ASC" 41147893376; the Touring's list lacks all three — [ETK M3 right brackets](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/front_body_bracket_right/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/front_body_bracket_right/), [ETK drawing](https://ills.bmwfans.info/1pkj.png) [read, image]. Which welded bracket carries the expansion-tank holder isn't shown.

**Thermostat, water pump, hoses (ETK, Flow, BMW).**
- US M3 "Waterpump — Thermostat": coolant pump **11517838118**, gasket 11517831099, thermostat housing 11537831103, **thermostat 11531318274 "80GRAD"**, O-ring 11531318402 (64.77 × 2.62), pipe 11537830710 + O-rings 11537830709 ×2, holder 11537838119 — [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/waterpump_thermostat/) [read]; RealOEM call-outs "Opening temperature (stamped in thermostat) 80 °C" and 10 Nm for housing and pump bolts — [Flow p.59](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) [read, image, earlier copy]. BMW: "Thermostat Housing (80° C thermostat)", "Coolant Reservoir (2 bar system)" — [BMW ST041 M3 DriveLine, p.13](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine.pdf) [read, image].
- The 325i Touring instead has "Thermostat housing with thermostat" 11537509227 — [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/waterpump_thermostat/) [read], the DME-heated map thermostat — [BMW ST034 E46 Engines](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/9%20Engines.pdf) [read].
- US M3 "Cooling System Water Hoses": water hose **11537830716** with **vent screw 17111712788**, water hose 11537830715, temperature sensor coolant **13621433077** (radiator outlet), pipe 11537830711, water hose 11537830713, return pipe 11537838756, pipe 11537830714, gaskets 11537830708 ×3, O-rings 11537830712 ×2 and 11537830709, clamps 07129952119 ×2, temperature sensor water/oil 13621433076 — [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/cooling_system_water_hoses/) [read]. RealOEM call-outs: "Coolant pressure: 2 bar system"; **2.5 Nm** on the vent screw (item 2) — [Flow p.60](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) [read, image, earlier copy]. The 325i Touring uses the same sensor 13621433077 in its own (M54) hose set — [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/cooling_system_water_hoses/) [read].
- M3 DIY: "You will need to remove the air intake plumbing in order to get at the air bleed screw" — [Blankowski](https://blankowski.com/Cars/m3_coolant_change/) [read].

**Heater valve, auxiliary pump and heater hoses (ETK, forum).**
- US M3 "Water hoses/water valve": hose engine inlet → valve **64216902678**, water valve with additional water pump **64118369807**, hose valve → heater core **64216902679**, hose heater core → engine return **64216902680**, clamps 64218367179 ×2, 64218386477, 64216911339, inlet clamp 64212229718 — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/water_hoses_water_valve/) [read].
- E46 M3 CSL (Europe): the **same engine-side hoses 64216902678 and 64216902680**, the plain **water valve 64118369805**, and its own valve → heater-core hose **64212282548** (from May '03, CSL only) — [ETK CSL](https://bmwfans.info/parts-catalog/E46-Coupe/Europe/M3_CSL-S54/L-N/browse/heater_and_air_conditioning/water_hoses_water_valve/), [ETK 64212282548](https://bmwfans.info/parts-catalog/64212282548/) [read].
- US 325i Touring: hose engine inlet → valve 64218376999, **water valve 64118369805**, hose valve → heater core 64218363198, hose "radiator [heater core] and expansion tank" 64218376153 — all non-M parts — [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/water_hoses_water_valve/), [ETK 64218363198](https://bmwfans.info/parts-catalog/64218363198/) [read].
- 64118369807 is listed for the E46 M3 coupe and convertible in **Europe and the USA** and the S54 Z3 M; 64118369805 for the CSL and the non-M cars — [ETK 64118369807](https://bmwfans.info/parts-catalog/64118369807/), [64118369805](https://bmwfans.info/parts-catalog/64118369805/) [read].
- Heater core 64118372783, its double pipe 64118372784, seals 64118377824 ×2 and the valve bracket **41148209658** ("Bracket f addit. water pump and valve") are identical on both cars — [ETK M3 heater core](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/heater_radiator_air_conditioning/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/heater_radiator_air_conditioning/), [ETK 41148209658](https://bmwfans.info/parts-catalog/41148209658/) [read].
- NAM3 "Deleting auxiliary water pump" (2020–26): owners run the non-M/CSL valve on M3s, "No notable difference"; ZUSATZWASSERPUMPE set to `nicht_aktiv`; a 2023 post claims "Unlike non-M cars, the cooling system on ours is self-bleeding"; a 2026 post (non-M facelift IHKA in an M3, pump deleted) still had DTC 29 "Kommunikation mit dem Zuheizer" until ZUHEIZER was changed from `k_bus` to `konventionell` — [NAM3 14592, p.1–3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/14592-deleting-auxiliary-water-pump) [read]. No post mentions which valve-to-heater hose they used.
- Without the pump wired, one sedan swap was hard to bleed; Tenza found two plugs on the S54 valve where his harness had one — [notes: youtube_swap_wiring_coding.md lines 189, 491]. The pump's wiring (F62 feed, IHK X608 pin 6) is in the guide's manual and in `body_and_network_circuits.md` Q4.

**Oil cooler (ETK, Flow, BMW).**
- US M3 "Engine oil cooler": cooler **17212228942**, "oil cooler rackside" **17212229744**, brackets 17212229771 ×2, screws 17117536971 ×4, oil cooling pipe **17222283209** (old 17222282270), O-rings **17222245358** (13.4 × 1.78) ×4, screws 17227833189 (M8 × 28) ×2, pipe brackets 17201712209 ×2, spacer 17227798686, bolt 07119903994 — all M3-only — [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/radiator/engine_oil_cooler/) [read]. Call-outs: "Pipes to engine oil cooler: 25 Nm", 20 Nm at the M8 screws, 6 Nm at the M6 bracket bolt; the drawing shows the cooler clipped under a long air guide ("rackside") — [Flow p.57](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) [read, image, earlier copy].
- BMW: "Oil Cooler (flow controlled by 95 °C thermostat in oil filter housing)" — [BMW ST041 M3 DriveLine, oil circuit](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine.pdf) [read; OCR "95m- C"].
- Two side screws hold the cooler up under the radiator — [Blankowski](https://blankowski.com/Cars/m3_coolant_change/) [read]. With a ZHP bumper the cooler got "about half the air it needs" until a lip was cut — [notes: youtube_conversion_builds.md line 436].
- M3 front air-duct group: cover top 51717893229, front air duct 51717893351, air channel 51717893051, intermediate piece 51717892754, brackets 51717892797/798, brake ducts 51712695701/702 — [ETK M3 air duct](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_trim/air_duct/) [read].

### Inferences
- **Inference (strong): a manual 2003 325i Touring has no viscous fan and its DME-driven fan is the shroud fan.** Basis: the ETK restrictions above, the "fan housing with fan" drawing, and WDS's single M9 with X82 on the shroud. A car has only one DME fan output (X60004 pin 4), so a manual car is unlikely to carry a second, DME-driven pusher fan. Not proven: whether manual Tourings also have a pusher fan; check behind the bumper.
- **Inference: X82 may not reach the M3 pusher fan.** The Touring's X82 sits at the top of the radiator shroud; the M3's fan sits in front of the condenser. Pins are unchanged (1 ground, 2 DME signal, 4 battery feed), so it's a lead extension in 6.0 mm² for pins 1 and 4. ETK lists the 3-pole pusher-fan connector for both cars, but WDS calls X82 a 4-pin plug and ETK lists no plug for the 390 W shroud fan: compare the two plugs before cutting anything.
- **Inference: the M3 radiator, shroud and oil cooler bolt to the Touring's radiator support unmodified,** because the front panel, radiator supports and every radiator mounting part are common part numbers. The Touring's radiator adjusting screw (17111437359), drain plug and lower seal are left off.
- **Inference: with the plain valve, use the CSL's valve-to-heater-core hose 64212282548.** It is the only ETK pairing of 64118369805 with the S54's engine-side hoses (64216902678 in, 64216902680 out). The M3's 64216902679 is drawn for the pump valve; the Touring's 64218363198 joins the same two parts on the same bracket and may fit, but nobody has shown it.
- **Inference: the earlier guide's "US M3 valve" wording is narrow.** ETK fits the pump valve to every E46 M3 except the CSL, European cars included.

### Gaps
- Whether a US manual 325i Touring carries a pusher fan, and the length of its X82 lead.
- Which welded body bracket carries the M3 expansion-tank holder 17112229108.
- A test-fit of the Touring's own valve-to-heater hose with the S54 hoses.

---

## Q2. Coolant: capacity, specification, fill and bleed, pressure test

### Cited findings
- **Capacity (BMW US owner's manuals, M3 convertible; the coupe shares the S54 circuit):**
  - MY2002 (Part No. 01 41 0 156 249, © 09/01): "Cooling system including heater circuit quarts (liters) approx. 9.9 (approx. 9.3)" — [archive.org manualzilla-id-7335091](https://archive.org/details/manualzilla-id-7335091) [read].
  - MY2003 (Part-No. 01 41 0 156 854, © 09/02): "Cooling system including heater circuit … approx. 9.8/9.3" — [archive.org manualzilla-id-7342203](https://archive.org/details/manualzilla-id-7342203) [read].
  - MY2001 manuals print other values: M3 coupe (© 08/00) "Cooling system including heater … approx. 6.3 (approx. 6.0)", with engine oil 6.9/6.5 qt/L, which is the non-M figure — [manualzilla-id-7328330](https://archive.org/details/manualzilla-id-7328330); M3 convertible (© 12/00) "approx. 7.1 (approx. 6.7)" — [manualzilla-id-7337212](https://archive.org/details/manualzilla-id-7337212) [read].
  - MY2004 convertible (© 09/03) and MY2005 M3 (© 09/04): the capacities table no longer lists the cooling system — [manualzz-id-1189475](https://archive.org/details/manualzz-id-1189475), [manualzilla-id-7299992](https://archive.org/details/manualzilla-id-7299992) [read].
  - DIY: "System takes a total of 10 quarts of coolant. I only used about 8" (after a drain) — [Blankowski](https://blankowski.com/Cars/m3_coolant_change/) [read].
- **Specification (BMW):**
  - "The antifreeze concentration should be 50%, throughout the year… ethylene glycol antifreeze with corrosion inhibitors that are nitrite- and amino-acid free and compatible with aluminum radiators" — [BMW ST054 03 Engine Cooling/Heating System](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control/03_Engine%20Cooling-Heating%20System.pdf) [read; generic BMW module, illustrated on E60].
  - BMW antifreeze "1 GALLON" **82141467704** (production from Apr '93) — [ETK](https://bmwfans.info/parts-catalog/82141467704/) [read]. BMW bulletins use it at "50/50 mixture" — [SI B17 02 17 (G30/G12, 2017)](https://static.nhtsa.gov/odi/tsbs/2017/MC-10149234-9999.pdf) [read] — and set "coolant freezing protection level should be -38°C" — [SI B17 10 17 (F22/F23, 2017)](https://static.nhtsa.gov/odi/tsbs/2017/MC-10136717-9999.pdf) [read]. *Later models; the antifreeze part and the 50/50 rule transfer; treat −38 °C as a target, not an E46 figure.*
  - Owner's manual: "Coolant consists of water and coolant additives. Not all commercially available additives are suitable… Only use approved additives" — [M3 manual © 09/04](https://archive.org/details/manualzilla-id-7299992) [read]. Retailers describe BMW's newer green HT-12 coolant (83192468442) as backward-compatible with the blue, and say not to mix colors [snippet only].
  - Distilled water: the M3 DIY uses "50/50 mix of distilled water and coolant" — [Blankowski](https://blankowski.com/Cars/m3_coolant_change/) [read]. No BMW text on water quality was read.
- **Level check (BMW, MY2003 M3):** "Check the coolant level when the engine is cold, approx. 68 °F/+20 °C … correct when the upper end of the red float is at least even with the upper edge of the filler neck … but no more than 3/4 in/2 cm above it — that is, up to the second mark on the float … do not overfill" — [manualzilla-id-7342203, p.126](https://archive.org/details/manualzilla-id-7342203) [read].
- **BMW generic fill rules (ST054, E60 illustrated):** "Perform filling operation slowly. Pour coolant into expansion tank up to MAX mark. Start engine and run at idle speed for approx. one minute (cap open). Then adjust coolant level to MAX. Close cap and run engine up to operating temperature until main thermostat opens. Check cooling circuit and drain plug for leaks." "The engine must be cooled down before the coolant level is checked. Coolant temperature must not exceed 30°C." "Before filling: Turn on ignition. Set blower to low level. Set heating controller to maximum temperature. This ensures that the heater valves are fully opened and the auxiliary water pump starts." "Do not fill coolant expansion tank over MAX level as overfilling will cause the coolant to overflow and the auxiliary water pump must deliver coolant in order to ensure fully venting!" — [BMW ST054 03](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control/03_Engine%20Cooling-Heating%20System.pdf) [read].
- **Why heat at maximum matters (BMW):** IHKA water valves "are normally held open by spring pressure (failsafe), and are electrically closed by pulses"; the auxiliary pump is switched on by "Maximum heating requested", "Maximum defrost mode", "Y-factor > 5%" and coolant > 32 °F (E38 example) — [BMW ST054 Output](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/16%20Output.pdf) [read]. On the E46 IHKR "the water valve is closed (energized) in the blower zero (off) position", and turning the temperature dial fully right gives "water valve full open" — [BMW ST054 IHKR E46](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/13%20IHKR%20E46.pdf) [read].
- **S54 DIY bleed (E46 M3, year not stated):** remove the bleed screw completely; "very SLOWLY add your coolant to the expansion tank… It will take about 2 gallons until fluid starts to flow from the bleeder"; refit loosely, "turn the key to 1 position. You should hear the heater pump moving coolant"; after a few minutes add more until it seeps, tighten, top up; run to temperature, cool completely, open the bleeder half-way, "If you get a hiss of air, repeat… It will probably take 2 heat cycles" — [Blankowski](https://blankowski.com/Cars/m3_coolant_change/) [read]. A snippet of an e46fanatics thread describes the same cold method: "engine off, ignition on, heater at maximum, fan on low, then top up … until coolant flows from the bleed screw … until you no longer see any air bubbles" [snippet only; site bot-checked].
- **Pressure.** Cap 17117639022 "2,0BAR" on both cars — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/radiator/expansion_tank_tubing/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/radiator/expansion_tank_manual_transmission/) [read]; "Coolant pressure: 2 bar system" — [Flow p.60](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) [read, image, earlier copy]. BMW's leak-test practice on a later car: "Perform a complete cooling system, and coolant expansion tank cap, pressure test according REP 17 00 009… Maintain pressure for at least 15 minutes due to the small size of reported leaks" — [SI B17 03 16 (G12, 2016)](https://static.nhtsa.gov/odi/tsbs/2016/MC-10146885-9999.pdf) [read; later model, method transfers]. No E46 test pressure from TIS was read.

### Inferences
- **Inference: use 9.3 L (9.8 US qt).** Two consecutive BMW manuals agree; the 2001 prints are inconsistent in several lines. The swapped car has the same S54, M3 radiator and tank and an E46 heater core, so the figure transfers; fill to the level mark, not by volume.
- **Inference: the bleed sequence below is BMW-consistent but not the TIS text.** Every step is either BMW-documented for E46 hardware, a generic BMW rule, or the M3 DIY; the ordering is mine.
- **Inference: with the plain valve, bleeding relies on the engine's pump.** BMW's own wording makes the auxiliary pump part of venting, which matches the one hard-to-bleed report without it, and NAM3's CSL-valve owners report no difference in use.
- **Inference: monitor coolant temperature with a tool.** The M3 cluster's "temperature gauge" reads 80–120 °C as normal and 150 °C as maximum, which are oil-temperature figures (MY2003 M3 manual "Temperature gauge", [read]); read coolant with Tool32 `STATUS_MOTORTEMPERATUR` or a generic OBD scanner.

### Gaps
- BMW TIS 17 00 S54 fill and bleed text, and a TIS E46 cooling-system test pressure.
- Whether the S54 is "self-bleeding" (one NAM3 assertion).

---

## Q3. A/C hardware, charge, oil, evacuation, law

### Cited findings
- **Compressor and drive.** US M3: compressor **64526910458** to Sep '02, **64526916232** from Sep '02 (reman 64526911340, 64526936883); bracket **64551432237** with M8 bolts; belt **11287830946 (5PK × 829)**, adjusting pulley 11281433571, bolts 07119912478 + washers 07119907030 — [ETK compressor](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/air_conditioner_compressor_2/), [bracket](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/climate_compressor_supporting_bracket/), [belt](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/belt_drive_climate_compressor/) [read]. Call-outs: bracket bolts 20 Nm, adjusting-pulley bolts 24 Nm — [Flow p.62, p.65](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) [read, image, earlier copy].
- US 325i Touring: compressor 64526910458; bracket 64551432237 (to and from Sep '02) and a second bracket group 64557512556 (from Sep '02); belt 11281437450 (5PK × 863) to Sep '02, **11287512762 (4PK × 863)** from Sep '02, adjusting pulley 11287512758 from Sep '02 — [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/belt_drive_climate_compressor/), [ETK 64557512556](https://bmwfans.info/parts-catalog/64557512556/) [read]. 64526916232 is listed for the US M3 and the US 325i sedan, not the US 325i M54 Touring — [ETK](https://bmwfans.info/parts-catalog/64526916232/) [read].
- **Refrigerant lines ("Coolant lines").** US M3: pressure hose compressor → condenser **64536902681** (M3 only); condenser → drier **64536904013**; drier → evaporator **64536909448** (from Sep '99); double pipe **64536908907**; suction pipe evaporator → compressor **64536923956** with cover 64538385711; gasket rings **64508374959** (9.5 × 2.5) ×4, **64508375741** (10.8 mm) ×3, **64508363041** (23 mm) ×1, **64538375742** (13.7 mm) ×2; valve inserts 64509177579 (suction), 64509177577/64538391215 (pressure); cap 64538387437; bracket 64538376911; **pressure sensor 64539181464** (old 64539141957); screws 07119905720 (M8 × 30) ×6; 3-pole sensor housing 61138365348/61132359998 — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/coolant_lines/) [read]. The US 325i Touring lists the same parts **except pressure hose 64536984883** (old 64536908754) — [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/coolant_lines/), [ETK 64536902681](https://bmwfans.info/parts-catalog/64536902681/), [64536984883](https://bmwfans.info/parts-catalog/64536984883/) [read]. Call-outs: "Coolant lines M8 20 Nm", "Fill up plug 30 Nm" — [Flow p.63](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing) [read, image, earlier copy].
- **Condenser, drier, evaporator, expansion valve.** Both cars: condenser **64538377614**; "Drying container" **64538377330** with "**Bracket drying container 64536917658**"; evaporator **64119135744**; expansion valve **64503452759** with rings 64538375742, 64508374959, 64508390603 (14 mm), 64508390602 (11.1 mm) — [ETK M3 condenser](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/condenser_air_conditioning/), [drier](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/drying_container/), [evaporator/valve](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/evaporator_expansion_valve/); Touring [condenser](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/condenser_air_conditioning/), [drier](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/drying_container/), [evaporator/valve](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/evaporator_expansion_valve/) [read].
- **Charge and oil (vendor and forum):**
  - MAHLE "Refrigerant and oil filling quantities 2021–22", BMW: "3 Series (E46) gasoline engine: M43/M43TU/M52/M54/N40/N42/**S54** · 1998–05 · R134a · **715–765** [g] · [OE oil] PAG · [Behr oil] PAO 68 or PAG ISO 46 · **150** [ml, whole system]"; diesel E46 670–690 g — [MAHLE handbook p.23–24](https://www.mahle-aftermarket.com/media/homepage/facelift/media-center/klima/thermokampagne/2021/2-2-handbuch-fuellmengen-pkw-&-nkw-210112-en-screen.pdf) [read].
  - NAM3 DIY (2020): "The system is filled by weight, and not by pressure. It calls for 25-27 oz of R134a … Make sure the 3 oz can of oil recharge you get contains PAG 46 oil. PAG 100 or 150 is NOT compatible with e46 system"; low-side port "on the passenger side near the firewall", high-side port "next to passenger headlight"; vacuum 10 min, 5-min hold, then 45 min. A reply quotes an aggregator: "2002-03 6 Cyl. 3.2 Eng. – 26.00 Oz. R-134a; 5.10-5.70 Oz. PAG-46" (2004–05 the same; 2006 26.10 oz) — [NAM3 30199](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/30199-diy-a-c-system-service-charging) [read].
- **BMW A/C service rules (ST054, 2007, generic BMW):** "Replace the dryer following intervention… if it was left open for longer than 24 hours"; "After extracting the refrigerant, measure and replace the quantity of oil also extracted"; "First evacuate the system for at least 30 minutes"; "Always replace the seals of the connections that were opened"; compressor swap: "the new compressor is filled with 120 to 200g of refrigerant oil at the factory… fill the same quantity as extracted from the old compressor + 10g"; recharge: "If you have replaced the condenser or evaporator, 2 additional ounces… If you have replaced the receiver dryer… 1 additional ounce… Hoses do not collect much oil"; evacuation test: "run for a minimum of 30 minutes… let the vehicle sit for five minutes… If the gauge readings differ more then 2" of vacuum in 5 minutes, then there is a leak"; new-compressor run-in: "Switch off air conditioning… Set all air outlet nozzles… to 'OFF'… Set blower capacity to min. 75%… Switch on air conditioning and allow to run for at least 2 minutes at idle speed" — [BMW ST054 07 AC Service and Diagnosis, p.6–10, 17](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control/07_AC%20Service%20and%20Diagnosis.pdf) [read].
- **Keeping the 325i's own compressor:** Kalim (2003 325i Steptronic, S54): "The A/C should work without any trouble, but I've only confirmed this on cars with IHKA… You will need to use a different A/C belt if you keep the original A/C compressor from the chassis as I did in my build"; during the swap "I left the A/C and P/S lines connected" and "A/C components tied off to the side" — [e46fanatics 889867 p.38](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38) [read, earlier copy]. Removing an S54 from a Touring, the "AC pulley/bracket" sat close to the condenser — [notes: youtube_conversion_builds.md line 336].
- **Law (EPA, read 22 Oct 2026):** refrigerant "cannot be intentionally released (vented)"; "When payment of any kind is involved… any person working on an MVAC system must be certified under section 609… and they must use approved refrigerant handling equipment"; certified equipment "must be used to remove refrigerant prior to servicing or repairing an MVAC system" — [EPA MVAC servicing](https://www.epa.gov/mvac/regulatory-requirements-mvac-system-servicing). "Refrigerant can only be sold to technicians certified under the Section 608 or Section 609… except for the sale of small cans of substitute refrigerants (e.g., R-134a for use in motor vehicle air conditioners)… Small cans of non-exempt MVAC refrigerant (i.e., containers designed to hold two pounds or less of refrigerant) that have unique fittings, and self-sealing valves can continue to be sold to persons without certification for DIY use" (updated 23 Mar 2026) — [EPA sales restriction](https://www.epa.gov/section608/refrigerant-sales-restriction); the overlap page says the restriction covers HFCs from 1 Jan 2018 except small cans — [EPA 608/609 overlap](https://www.epa.gov/section608/section-608-and-section-609-overlap); approved 609 programs include ASE, ESCO Institute and MACS (updated 25 Jun 2026) — [EPA 609 programs](https://www.epa.gov/mvac/section-609-technician-training-and-certification-programs) [all read].
- **Massachusetts:** the earlier round read MassDEP's HFC rule 310 CMR 7.76, whose end-use table "has no motor-vehicle A/C category", and found nothing else — [notes: massachusetts_rules.md, A/C refrigerant]. Not re-checked here.

### Inferences
- **Inference: keep the Touring's A/C system and add only the M3 pressure hose.** With the compressor and bracket arriving on the S54 and every other line, the condenser, drier, sensor and heater-box parts identical, the only new joint pair is compressor-to-condenser. A compressor-only swap keeps the oil balance simple.
- **Inference: the charge is ~0.74 kg, but the Touring's label decides.** MAHLE's range is drawn from manufacturer data and covers the S54; the forum figures sit inside it. BMW's label is per model, and the M3 hose is a little longer than the non-M one.
- **Inference: a sealed-system shortcut exists but is risky here.** Kalim never opened his refrigerant circuit. For this build (months of storage, a new front end, a possibly 4PK post-09/2002 compressor pulley on a 5PK S54 drive, the non-M pressure hose on an S54) it's simpler to recover, swap, evacuate and charge.

### Gaps
- BMW's own E46 refrigerant charge and oil quantity (TIS 64 operating fluids) and the compressor make and oil viscosity.
- Whether the post-09/2002 Touring compressor's pulley is 4- or 5-groove (only matters if you keep it).

---

## Q4. How the MSS54 runs the compressor and fans with IHKA and IHKR

### Cited findings
- The request chain, K19 on X60004 pin 29, the pressure sensor read by the climate control, and BMW's statement that IHKR is standard on the 325i Touring and the M3 from 09/2000 are already in `body_and_network_circuits.md` (Q4, D9, F2) [notes].
- IHKR: "The IHKR cycles the compressor at 1°C if the outside temperature is above 68°F. The compressor is cycled at 3°C if the outside temperature is below 68°F"; "Pressure values that are too high or too low will cause the compressor to be switched off"; DIS service function "Deactivate transport-lock function" — [BMW ST054 IHKR E46](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/13%20IHKR%20E46.pdf) [read].
- IHKA: "As long as the evaporator temperature is above 36°F, the IHKA will signal the… control module to activate the compressor"; full-throttle cut-out "4-10 seconds when the full throttle signal is present and vehicle speed is less than 10 mph"; fan: "Radiator outlet temperature sensor input exceeds a preset temperature", IHKA pressure signals, vehicle speed, battery voltage; "When the over temperature light in the instrument cluster is on (120°C) the fan is run in the overrun function… at a frequency of 10 Hz"; refrigerant pressure → fan stage table, "Prerequisite is a speed less than 50 mph" (8 bar = 0, 9 = 1, 11 = 2, 13 = 3, 14 = 4 … 24 = 14, >24 = 15) — [BMW ST054 IHKA E46, p.15–17](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/12%20IHKA%20E46.pdf) [read; table read as image].
- Fan output (WDS functional text, E46 petrol DMEs): "square-wave signal with duty factors… between 10 and 90 %… less than 5 % and greater than 95 % do not trigger activation but rather they are used for fault detection… The fan speed is influenced by the coolant temperature at the radiator outlet and the pressure in the air conditioning system. The fan speed is reduced as the vehicle speed increases" — [WDS Electric Fan](https://wds.psjr.org/en/e46/zinfo/HEL0498FB1214_M0ELU.htm) [read]. MSS54: the same inputs, "remote power output final stage (mounted on the fan housing)… 50 amp fuse" — [BMW ST041 Engine Electronics part 3](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf) [read].
- MSS54 SGBD: `STEUERN_E_LUEFTER` (fan), `STEUERN_KO` (compressor relay), `STATUS_MOTORTEMPERATUR` (MW_TMOT, °C), `STATUS_KUEHLW_AUSL_TEMPERATUR` (radiator outlet, MW_TKA, °C), `STAT_ELU_EIN`, `STAT_KO_EIN`, `STAT_AC_EIN`, adaptation `STAT_KKOS_ST_VERBAUT_WERT` "Klimaanlage erkannt"; faults 0x2B radiator-outlet sensor, 0x30 compressor relay, 0x35 electric fan, 0x4E coolant sensor, **0x60 "Plausibilisierung Kühleraustrittstemp."** (radiator-outlet temperature plausibility); the same SGBD's fault-type table includes 0x50 "T-Erhöhung zu gering oder Kühler wärmer als Motor" (temperature rise too small, or radiator warmer than engine), without saying which fault uses it — [SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md) [read].
- IHKR46 and IHKA46 SGBD: `STATUS_ANALOGEINGAENGE` (`STAT_DRUCKSENSOR_WERT` in bar, `STAT_TVERDAMPFER_WERT` evaporator °C, heater-core sensor), `STATUS_IO` (`STAT_WASSERVENTIL_EIN`, `STAT_ZUSATZWASSERPUMPE_EIN`, IHKR `STAT_KLIMABEREITSCHAFT_EIN` "Klimabereitschaft nach Kompressoreinlauf"), `STEUERN_ZUSATZWASSERPUMPE`, `STEUERN_WASSERVENTIL` (0–100 %), and **`KOMPRESSOR_SPERRE` "Codieren der Kompressortransportsperre"**; IHKR `CODIERUNG_LESEN` returns `KOMPRESSOR_SPERRE` "Klimakompressor deaktiviert" — [IHKR46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKR46.md), [IHKA46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKA46.md) [read].
- Swaps: A/C works with IHKA (Kalim, above). No IHKR report found (also none in the earlier notes).

### Inferences
- **Inference: IHKR should work** (unchanged from the earlier notes), and the first things to check if it doesn't are the cluster gateway, the transport lock and `STAT_AC_EIN`/`STAT_KO_EIN`.
- **Inference: fault 0x60 is the MSS54's thermostat check.** A stuck-open thermostat or an unplugged or mis-routed radiator-outlet sensor would show there.

### Gaps
- MSS54 fan-stage coolant temperatures (BMW gives only "a preset temperature").
- What `STAT_KLIMABEREITSCHAFT_EIN` requires before the IHKR allows the compressor.
- A first-hand IHKR + MSS54 report.

---

## Q5. Checks and pass values

### Cited findings
- **Cooling:** cap and system 2.0 bar (ETK, Flow); hold ≥15 min and test the cap too (BMW SI B17 03 16, later model); thermostat 80 °C (ETK, ST041); viscous coupling on 92 °C / off 60 °C (Flow p.61); overheat lamp 120 °C (ST054 IHKA E46); oil-cooler flow from 95 °C oil (ST041); level cold per owner's manual (above). Sources as cited in Q1–Q2.
- **A/C (BMW ST054 07, generic):**
  - Quick check at 90 °F/50 % RH, 1,500–2,000 rpm, blower medium, max cold, A/C on for more than 3 min: "Center vent discharge = 20°F less than the ambient temperature".
  - Efficiency test (ambient 20–30 °C): heat the cabin (recirculation, footwell/defrost, max heat, max fan, 2,000 rpm to operating temperature, then idle), switch the A/C on at 50 °C cabin temperature: "After 3-4 minutes, the evaporator sensor temperature must be 15°C (59°F) or below"; if not, recover and weigh the charge.
  - "Normal Operation Readings: Low pressure - normal 1 to 2 bar (15 to 30 psi); High pressure - normal 10 to 15 bar (150 to 225 psi). Outlet temperatures may vary from 40 to 68°F… Readings of about 20° less than ambient temperatures are considered acceptable."
  - "Low side pressures should average 28 to 32 psi… between 15 and 45 psi"; "High side… about 2 to 2.5 times the ambient temperature… 80°F should produce a pressure of 160 to 200 psi".
  - The R-134a ambient/humidity reference chart (p.24, below) — [BMW ST054 07, p.12–24](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control/07_AC%20Service%20and%20Diagnosis.pdf) [read; chart read as image].

### Gaps
- E46-specific pressure figures from TIS; MSS54 fan switch points.

---

## Guide-ready

### Parts tables

**Cooling: what comes from where (US M3 donor 2003–06, US 325i Touring 2003 manual).** "Keep" = the Touring's part stays; "Donor" = from the M3; "New" = buy.

| Function | US E46 M3 | US 325i Touring (manual) | Action |
|---|---|---|---|
| Radiator | 17102228941 (M3 only, no drain plug) | 17119071518 (A/C, manual, to 05/2005) | Donor (or new M3) |
| Radiator mounting: supports 17117530252/254, gaskets 17111436247/249, brackets 17117514402 ×2 and 17111436264 ×2, buffers 17111178412 ×2, screws 17117536971 | Same | Same | Keep; new buffers if hard |
| Radiator extras | Fan-housing bracket 17112282209, rivets 17111712963 ×3, screw 17117536972 | Adjusting screw 17111437359, drain plug 17111437361, lower seal 17111436245 | Donor's in; Touring's off |
| Viscous fan | Fan 11521712058 (420 mm, 11 blades), coupling 11527831619 (LH thread, 40 Nm), pulley 11517840403 | None on a manual (automatic only: 11521712058 + 11527505302) | Donor |
| Fan shroud | 17112228943 + air ducts 17112228945 (L), 17112228946 (R) | "Fan housing with fan" 17117561757 (electric, 390 W) | Donor's in; sell the Touring's |
| Electric fan | Pusher 64546988914 + compression shroud 64546905077 + grid 64548377800 + nuts 07129900546 ×4; plug 61138380380/61138380385 | Shroud fan above (automatics: pusher 64546988913) | Donor; extend X82 if short |
| Expansion tank | 17112283344 (was 17112228944), holder 17112229108, hose 17222246036, line 17112229053, grommets 17112229059 ×2, tubing supports 17112228439 ×2 | 17117573781 on mounting plate 17111436250 | New M3 tank; weld or rivnut brackets |
| Cap, level switch, plug | Cap 17117639022 (2.0 bar), switch 17137553919, 2-pole 61138365340/61132359999 | Same parts | Keep or new; extend the lead (cluster pin 26) |
| Thermostat | 11531318274 (80 °C) + O-ring 11531318402; housing 11537831103 | Map-thermostat housing 11537509227 | New 11531318274 and O-ring |
| Water pump | 11517838118 + gasket 11517831099 | 11517509985 | Donor (refresh: new) |
| Engine hoses and pipes | 11537830716 (vent screw 17111712788), 11537830715, 11537830713, 11537830711, 11537830714, return pipe 11537838756, gaskets 11537830708 ×3, O-rings 11537830712 ×2 and 11537830709, clamps 07129952119 ×2 | M54 hoses | Donor or new; new vent screw |
| Radiator-outlet sensor | 13621433077 | Same | Keep; check the lead reaches |
| Oil cooler | 17212228942, holder 17212229744, brackets 17212229771 ×2, screws 17117536971 ×4, pipe 17222283209, O-rings 17222245358 ×4, M8 screws 17227833189 ×2, pipe brackets 17201712209 ×2, spacer 17227798686, bolt 07119903994 | None | Donor; new O-rings |
| Front air ducts | 51717893229, 51717893351, 51717893051, 51717892754, brackets 51717892797/798, brake ducts 51712695701/702 | Touring parts | Donor (with the M3 bumper) |
| Coolant | BMW antifreeze 82141467704 (1 gal), 50/50, ~9.3 L system | — | New: 2 gallons concentrate covers a fill plus top-ups |

**Heater circuit (Touring keeps its heater box).**

| Function | US E46 M3 | Plain-valve option (CSL parts) | US 325i Touring | Action |
|---|---|---|---|---|
| Heater core, double pipe, seals | 64118372783, 64118372784, 64118377824 ×2 | Same | Same | Keep |
| Valve bracket | 41148209658 | Same | Same | Keep |
| Water valve | 64118369807 (with pump) | 64118369805 | 64118369805 | Option A: keep the Touring's; option B: donor's + 2 wires + coding |
| Hose engine → valve | 64216902678 | 64216902678 | 64218376999 | Donor's |
| Hose valve → heater core | 64216902679 | 64212282548 (CSL, from 05/03) | 64218363198 | A: CSL hose (or test-fit the Touring's); B: donor's |
| Hose heater core → engine | 64216902680 | 64216902680 | 64218376153 (to tank) | Donor's |
| Clamps | 64218367179 ×2, 64218386477, 64216911339, 64212229718 | — | — | New |

**A/C.**

| Function | US E46 M3 | US 325i Touring | Action |
|---|---|---|---|
| Compressor | 64526910458 (to 09/02), 64526916232 (from 09/02) | 64526910458 (2003 car: check) | Donor's, on the S54 |
| Bracket | 64551432237 (20 Nm) | 64551432237 or 64557512556 (from 09/02) | Donor's |
| Belt and tensioner | 11287830946 (5PK × 829), 11281433571, bolts 07119912478 + washers 07119907030 (24 Nm) | 11281437450 or 11287512762 (4PK, from 09/02), 11287512758 | Donor's (new belt) |
| Pressure hose compressor → condenser | 64536902681 (M3 only) | 64536984883 | **Donor's** |
| Condenser | 64538377614 | Same | Keep |
| Hose condenser → drier | 64536904013 | Same | Keep |
| Receiver-drier | 64538377330 (bracket 64536917658) | Same | **New drier**; keep the bracket |
| Hose drier → evaporator | 64536909448 | Same | Keep |
| Double pipe at evaporator | 64536908907 | Same | Keep |
| Suction pipe | 64536923956 (+ cover 64538385711) | Same | Keep |
| Pressure sensor | 64539181464 (was 64539141957) | Same | Keep |
| Expansion valve, evaporator | 64503452759, 64119135744 | Same | Keep (heater box) |
| Service valve cores, caps | 64509177579, 64509177577/64538391215, cap 64538387437 | Same | Inspect; caps on |
| O-rings | Lines: 64508374959 ×4, 64508375741 ×3, 64508363041 ×1, 64538375742 ×2. Expansion valve: 64538375742, 64508374959, 64508390603, 64508390602 | Same | New at every opened joint |
| Flange screws | 07119905720 (M8 × 30) ×6, 20 Nm | Same | — |
| Relay K19 | 61368373700 | Same | Keep |

### Procedures

**P1. Before teardown (Phases 0, 1 and 4).**
1. Photograph both cars' underhood A/C labels (charge and oil).
2. Run the BMW quick check on the Touring (BMW's condition is 90 °F and 50 % humidity; 1,500–2,000 rpm, windows and doors shut, blower medium, max cold, A/C on >3 min): centre vent at least 20 °F below ambient.
3. Note the Touring's fan layout (electric shroud fan, or viscous fan plus pusher) and its climate control (IHKA or IHKR), and photograph X82's position.
4. A Section 609-certified shop recovers both systems before any line is opened. Ask it to record **the refrigerant and oil recovered from each car**; you'll need the oil figure later.
5. Drain the donor at the S54 block plug (13 mm, new 14 mm washer, 18 ft-lb per the DIY) and at the lower radiator hose; the M3 radiator has no drain plug.

**P2. Fit the cooling parts (Phase 10).**
1. Radiator on the Touring's supports, brackets and buffers (same parts). Leave off the Touring's adjusting screw, drain plug and lower seal.
2. Oil cooler under the radiator: new O-rings 17222245358 ×4; pipe unions **25 Nm**, M8 flange screws **20 Nm**, M6 bracket bolt **6 Nm**.
3. Shroud and air ducts; fan on the coupling (screws **10 Nm**); coupling on the water pump, **left-hand thread, 40 Nm**.
4. Pusher fan with its compression shroud in front of the condenser (nuts 07129900546 ×4). Route X82 to it: pin 1 ground (6.0 BR), pin 2 DME signal (0.5 SW/GN, X60004-4), pin 4 +12 V (6.0 RT/BL, F37 50 A). If the lead is short, extend pins 1 and 4 in 6 mm² and pin 2 in 0.5 mm², matching the factory sizes. Compare plug housings first.
5. Expansion tank on its holder and the welded or rivnutted brackets; level switch plugged in; lead extended to cluster pin 26.
6. Heater hoses per option A (plain valve, CSL hose) or B (M3 valve, wire F62 and X608-6, code `ZUSATZWASSERPUMPE` = `aktiv`).
7. New thermostat 11531318274 (80 °C) and O-ring; housing and pump bolts **10 Nm**.
8. New vent screw 17111712788 in hose 11537830716, **2.5 Nm** (plastic: don't overtighten).
9. Radiator-outlet sensor 13621433077 plugged in; no lead under strain.

**P3. Pressure test (before filling or after the first fill, engine cold).**
1. Tester on the expansion-tank neck; pump to **2.0 bar (29 psi)**, never above the cap rating.
2. Hold **15 minutes**: no drop, no seepage at hoses, oil-cooler joints, heater hoses and the valve.
3. Test the cap 17117639022 on the tester's cap adapter: it should hold and relieve at its 2.0 bar rating.

**P4. Fill and bleed.** (Assembled from BMW sources and one M3 DIY; TIS 17 00 not read.)
1. Mix BMW antifreeze 82141467704 with distilled water 50/50, about 10 L. Engine cold.
2. Battery on a charger. Front of the car level or slightly raised (forum practice).
3. Remove the intake ducting over the front of the engine; open (or remove) the vent screw in hose 11537830716.
4. Ignition on, engine off. **IHKA:** temperature at maximum (HI), blower low but on, A/C off. **IHKR:** blower at position 1 (at 0 the valve is energized shut), temperature dial fully right (red). This holds the water valve open and, with the M3 valve wired, runs the auxiliary pump (BMW).
5. Fill the expansion tank slowly. Expect about 2 US gal before coolant reaches the vent screw (DIY). With the pump, wait a few minutes with the ignition on, then top up again.
6. When coolant runs from the vent screw without bubbles, fit it and tighten to 2.5 Nm.
7. Top up to the cold mark: the top of the red float level with the filler-neck rim, at most 2 cm above (owner's manual). Don't overfill (BMW).
8. Start the engine and idle about one minute with the cap off; top up; fit the cap (BMW).
9. Run to temperature until the thermostat opens. Watch `STATUS_MOTORTEMPERATUR` and `STATUS_KUEHLW_AUSL_TEMPERATUR` in Tool32 (the M3 cluster's gauge reads oil): the radiator-outlet temperature should climb steadily once the engine passes about 80 °C. Check for leaks.
10. Switch off; let it cool to ≤30 °C coolant (BMW); crack the vent screw: a hiss of air means repeat steps 8–10 (DIY: usually two heat cycles). Re-check the level after the first drives.

**P5. A/C reassembly, oil, evacuation and charge (shop brief, after first start).**
1. Fit the donor's pressure hose 64536902681 between compressor and condenser; keep the Touring's other lines.
2. New O-rings at every opened joint, wetted with the system's oil; flange screws **20 Nm**.
3. **Oil.** If the donor compressor is reused, drain and measure its oil and refill it with fresh PAG equal to that amount + 10 g (BMW). Add the oil the shop recovered from the Touring's system, plus 1 oz (~30 ml) for the new drier (BMW). Target whole-system total about 150 ml (MAHLE). Use the oil the label specifies; MAHLE lists PAG, and the NAM3 DIY says PAG 46.
4. Fit the new drier 64538377330 last; it stays capped until then (BMW: replace if open >24 h).
5. **Evacuate at least 30 minutes**; close off; **5-minute hold: more than 2 in Hg of change = leak** (BMW).
6. **Charge by weight to the underhood label.** Expect about 0.74 kg (MAHLE's E46 petrol range 715–765 g).
7. **Run-in** (BMW, for a newly fitted compressor): A/C off, all vents shut, idle, blower ≥75 %, then A/C on for at least 2 minutes at idle.
8. Read the climate module: `CODIERUNG_LESEN` → `KOMPRESSOR_SPERRE` = 0 (not locked); `FS_LESEN` clear; `STATUS_ANALOGEINGAENGE` pressure in bar; MSS54 `STATUS_DIGITAL` `STAT_AC_EIN` follows the button and `STAT_KO_EIN` the clutch.

### Checks and pass values

| Check | How | Pass | Source |
|---|---|---|---|
| Cooling-system leak | Tester at 2.0 bar, 15 min, engine cold | No drop, no seepage | Cap rating ETK; hold time BMW SI B17 03 16 (G12, method) |
| Cap | Tester's cap adapter | Holds, relieves at 2.0 bar | ETK 17117639022 |
| Level, cold | Owner's-manual float | Float top at the neck rim to 2 cm above | M3 manual MY2003 |
| Air in the system | Vent screw cracked when cold | No hiss after two heat cycles | Blankowski DIY |
| Thermostat | Tool32 radiator-outlet vs engine temperature | Outlet rises once the engine passes ~80 °C; no fault 0x60 | ETK/ST041; SGBD |
| Viscous fan | Hot idle; listen and watch the fan | BMW's coupling switch-on 92 °C, switch-off 60 °C (temperature at the coupling); engaged it roars and pulls air hard (inference). Check bearing play ±0.65 mm at 120 mm diameter | Flow p.61 (ETK note) |
| Electric fan | Tool32 `STEUERN_E_LUEFTER`; A/C on at idle | Fan runs on command; runs with A/C on at a standstill; faster as high-side pressure rises (stage 1 from 9 bar … 15 above 24 bar, below 50 mph) | SGBD; ST054 IHKA E46 |
| Overheat behaviour | — | Overheat lamp at 120 °C; fan overrun at 10 Hz | ST054 IHKA E46 |
| Oil cooler | Feel the lines after a hard drive | Lines warm once oil passes 95 °C (thermostat in the filter housing) | ST041 |
| A/C engages | Snowflake button, blower ≥1 | `STAT_AC_EIN`=1, `STAT_KO_EIN`=1, clutch pulls in, idle holds | SGBD; ST041 |
| A/C efficiency | BMW test, ambient 20–30 °C | Evaporator ≤15 °C within 3–4 min | ST054 07 |
| A/C pressures | Gauges, engine 1,500–2,000 rpm | Low 1–2 bar (15–30 psi; up to 45 psi on a hot day); high 10–15 bar (150–225 psi), about 2–2.5 × ambient °F in psi | ST054 07 |
| Vent temperature | Thermometer in the centre vent | 40–68 °F, at least 20 °F below ambient | ST054 07 |

**BMW R-134a reference, 50 % relative humidity** (ST054 07, p.24, generic BMW chart):

| Ambient °F | Discharge °F | Low psi | High psi |
|---|---|---|---|
| 70 | 45 | 14 | 102 |
| 80 | 51 | 36 | 164 |
| 90 | 59 | 54 | 229 |
| 100 | 70 | 67 | 229 (as printed) |
| 110 | 80 | 76 | 368 |

### Diagram-ready data

**D1. S54 coolant circuit in the Touring** (from BMW ST041 p.13 numbering, ETK parts; arrows = flow, engine running, thermostat open). The two expansion-tank rows are routed from the ST041 drawing and the ETK part names, not from a BMW hose diagram with labels; check against the parts when drawing.

| From | To | Via (part) | Note |
|---|---|---|---|
| Water pump 11517838118 (on the block, front) | Block, exhaust side | Internal | ST041: "from the engine block on the exhaust side into the cylinder head" |
| Block | Cylinder head (cross-flow) | Gasket passages | Exits at three outlets on the intake side (ST041 items 6, 7, 8) |
| Head outlets 6/7/8 | Thermostat housing 11537831103 | Return pipe 11537838756 (ST041 item 9) | Engine coolant sensor 13621433076 on this path (ST041 item 5) |
| Return pipe (front end) | Heater valve | Hose 64216902678 | Valve 64118369807 (pump) or 64118369805 (plain) on bracket 41148209658 |
| Heater valve | Heater core 64118372783 | Hose 64216902679 (M3) or 64212282548 (CSL plain valve) | Through the Touring's double pipe 64118372784 at the bulkhead |
| Heater core | Water pump inlet / thermostat housing | Hose 64216902680 → ST041 item 11 return line | — |
| Thermostat housing (80 °C, 11531318274) | Radiator inlet (top) | Water hose 11537830716 with **vent screw 17111712788** | **Bleed point 1** |
| Radiator 17102228941 outlet (bottom) | Water pump inlet | Water hose 11537830715 | **Radiator-outlet sensor 13621433077** (X60004 38/39) |
| Radiator top / vent | Expansion tank 17112283344 (passenger side) | Vent hose 17222246036 (500 mm) | — |
| Expansion tank bottom | Engine (pump/thermostat side) | Connecting line 17112229053 | **Fill point: tank neck, cap 17117639022, 2.0 bar**; level switch 17137553919 → cluster pin 26 |
| Oil filter housing (95 °C oil thermostat) | Oil cooler 17212228942 (under the radiator) and back | Oil pipe 17222283209 | Air from the M3 bumper's lower opening |
| Fans | — | Viscous fan 11521712058 + coupling 11527831619 behind the radiator, in shroud 17112228943 | Pusher 64546988914 in front of condenser 64538377614 |

Bleed and drain points: **vent screw** on hose 11537830716 at the front of the engine under the intake ducting (2.5 Nm); **fill** at the expansion-tank neck; **drains**: S54 block plug (13 mm, 14 mm washer) and the lower radiator hose (no radiator drain plug).

**D2. Fan layouts to draw side by side.**
- *Manual 325i Touring as built:* radiator → shroud with electric fan 17117561757 (power stage and X82 on the shroud); no viscous fan; X82 ← X60004-4 (signal), F37 50 A (feed), ground.
- *After the swap:* condenser ← pusher fan 64546988914 (power stage on the fan, X82 lead extended forward); radiator; shroud 17112228943 with viscous fan 11521712058/11527831619 on the S54 pump; same X60004-4 / F37 / ground wiring.

**D3. A/C refrigerant circuit** (high side solid, low side dashed).

| # | Component | Part | Next | Line part | Side |
|---|---|---|---|---|---|
| 1 | Compressor (S54, low front of engine, belt 5PK × 829) | 64526910458 / 64526916232 on bracket 64551432237 | Condenser | Pressure hose **64536902681 (M3)** | High (discharge) |
| 2 | Condenser (front, ahead of the radiator; pusher fan in front of it) | 64538377614 | Receiver-drier | 64536904013 | High (liquid) |
| 3 | Receiver-drier (bracket 64536917658) | 64538377330 | Expansion valve | 64536909448, carrying **pressure sensor 64539181464**, then double pipe 64536908907 | High |
| 4 | Expansion valve (at the heater box) | 64503452759 | Evaporator | Integral | Low after the valve |
| 5 | Evaporator (Touring's heater box; evaporator sensor read by IHK) | 64119135744 | Compressor | Double pipe 64536908907 → suction pipe 64536923956 | Low (suction) |
| Service ports | Low: passenger side near the firewall; high: next to the passenger headlight (NAM3, M3) | Cores 64509177579 / 64509177577 | — | — | — |

Control overlay (from `body_and_network_circuits.md` D9): pressure sensor (0–5 V) → IHKA/IHKR → K-bus → cluster → CAN → DME → X60004-29 → relay K19 (F63 7.5 A) → compressor clutch; DME → X60004-4 → fan power stage; coded `KOMPRESSOR_SPERRE` in the IHK can block it.

**D4. BMW refrigerant pressure → electric-fan stage (IHKA E46, below 50 mph).**

| bar | 8 | 9 | 11 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | >24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stage | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |

---

## Guide statements this research corrects

1. README, Fluids and capacities: *"Coolant | BMW coolant, 50/50 with distilled water (unverified); system pressure 2 bar (29 psi) | **Capacity not found** | Mix: forum posts (unverified); pressure: Flow p.60"* → **About 9.3 L (9.8 US qt) including the heater** (BMW US owner's manuals, MY2002 and MY2003 M3; earlier prints differ). BMW antifreeze 82141467704 at 50 % (BMW ST054 training and SI bulletins); cap and system 2.0 bar (ETK 17117639022). Distilled water is DIY practice.
2. README, Fluids and capacities: *"A/C refrigerant | Per the underhood label | **Charge not found;** charge by weight from the label"* → Charge by weight to the label; MAHLE lists 715–765 g R134a for E46 petrol engines including the S54, with PAG oil, 150 ml for the whole system.
3. README, Consumables: *"A/C drier 64538377330 or 64536917658, and O-rings"* and Shop briefs: *"A new drier (64538377330 or 64536917658)"* → The drier is **64538377330**; **64536917658 is its bracket** (ETK). List the O-rings by number (Q3 table).
4. README, Parts list: *"A/C lines | Donor M3 | Have the refrigerant recovered first"* → Only the **compressor-to-condenser pressure hose 64536902681** is M3-specific; every other line, the drier, sensor and condenser are the same part numbers on both cars, so keep the Touring's.
5. README, Cooling and oil cooler: *"Use the M3 radiator, shroud and both fans; the electric fan's wiring doesn't change"* → On a **manual** Touring the DME's electric fan is a 390 W fan in the radiator shroud (17117561757) with X82 on the shroud, and there's no viscous fan. The M3's electric fan is a pusher in front of the condenser, so the pins don't change but the X82 lead may need extending or re-routing. Compare the plug housings.
6. WIRING-AND-CODING, Fans and CAN: *"The fans differ (M3 64546988914, 325i 64546988913), but both cars list the same 3-pole connector parts"* → 64546988913 is the pusher fan of Tourings with the mechanical fan (automatics); a manual Touring's fan is 17117561757. WDS calls X82 a 4-pin plug with pins 1, 2 and 4 used.
7. README and manual, Heater valve: *"The US M3's heater valve carries a small electric pump"* / *"your plain valve (64118369805, also the CSL's) fits the S54 with no wiring"* → Every E46 M3 except the CSL (Europe too) has the pump valve (ETK). With the plain valve, the CSL's ETK pairing uses valve-to-heater-core hose **64212282548**, and the engine-side hoses are the M3/CSL parts 64216902678 and 64216902680. The Touring's engine-side heater hoses are M54 parts (its return runs to the radiator's expansion tank, which goes), so plan on the S54 hoses; the Touring's valve-to-core hose 64218363198 is an untested alternative to the CSL hose.
8. README, Cooling and oil cooler: *"BMW's bleeding procedure is in TIS group 17 00; we couldn't read it. Owners of other BMW sixes park nose up…"* → TIS 17 00 still unread, but BMW's training gives the fill rules (ignition on, blower low, heat maximum so the valve opens and the auxiliary pump runs; fill slowly; don't overfill; check at ≤30 °C), and the S54 vent screw is in hose 11537830716 at 2.5 Nm. Use procedure P4.
9. README, Cooling and oil cooler / Phase 10: *"pressure-test the system to its 2 bar working pressure"* → Keep 2.0 bar (the cap rating, not above it), hold 15 minutes, and test the cap too.
10. README, Open questions: *"The S54's coolant capacity, and BMW's S54 cooling-system bleed procedure (TIS 17 00)"* and *"The A/C refrigerant charge (read it from the underhood label)"* → Capacity settled (9.3 L); bleed partly settled (BMW rules, not TIS text); charge has an E46 range (715–765 g). Replace with: the TIS bleed text, E46 fan switch points, and BMW's own E46 refrigerant and oil quantities.
11. README, Phase 12 Done-when: *"Cooling | Temperature steady, no air in the system, fan cycles"* → Name the tools: the M3 cluster's temperature gauge reads oil, so read coolant and radiator-outlet temperatures in Tool32; pass = outlet rises after ~80 °C, no fault 0x60, fan runs on `STEUERN_E_LUEFTER` and with A/C on at idle.
12. README, Phase 12 step 10: *"have a shop vacuum-test the system and charge it by weight from the underhood label, then check it blows cold"* → Add BMW's numbers: ≥30 min vacuum, ≤2 in Hg change in 5 min, compressor run-in, evaporator ≤15 °C within 3–4 min, vents 40–68 °F and ≥20 °F below ambient, low 1–2 bar, high 10–15 bar.
13. WIRING-AND-CODING, A/C: *"A/C with the S54 is confirmed on IHKA cars; nobody has reported on IHKR first-hand"* → Unchanged, but add: if the compressor never engages, read the IHK's coded transport lock (`KOMPRESSOR_SPERRE`), and the IHKR cycles the compressor at 1 °C evaporator temperature above 68 °F ambient (3 °C below).
14. README, Phase 4 step 1: *"Have a shop recover the Touring's A/C refrigerant before you open any line"* → Keep, and ask the shop to record the refrigerant and oil recovered per car; the oil figure sets the refill (BMW).

## Key sources
- BMW technical training (archive.org `BMWTechnicalTrainingDocuments`): ST041 M3 DriveLine (coolant and oil circuits), ST041 Engine Electronics part 3; ST054 IHKA E46, IHKR E46, Output, 03 Engine Cooling/Heating, 07 AC Service and Diagnosis; ST055 MS42/MS43 and MS45; ST034 E46 Engines and Climate Control.
- BMW US owner's manuals on archive.org: M3 2001 (coupe and convertible), 2002, 2003 and 2004 convertible, 2005 M3.
- BMW SIBs on NHTSA: SI B17 02 17, SI B17 10 17, SI B17 03 16 (later models).
- ETK via bmwfans.info: US M3 coupe and US 325i Touring groups linked above; CSL water-hose group; part pages.
- WDS: SP0000011770, SP0000019629/30, E46_EM9A, Electric Fan text.
- SGBD exports: MSS54DS0, IHKR46, IHKA46.
- Flow compilation pp.57, 59–63, 65 (RealOEM printouts).
- MAHLE refrigerant and oil filling quantities 2021–22.
- Forum and DIY: NAM3 30199 and 14592; Blankowski E46 M3 coolant DIY; Kalim's e46fanatics thread (earlier copy).
- EPA MVAC, sales-restriction, 608/609 overlap and 609-program pages (2026).
