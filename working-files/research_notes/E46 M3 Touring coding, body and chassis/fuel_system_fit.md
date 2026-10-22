# Fuel system fit: the S54's fuel supply in a US 2003 E46 325i Touring (M54), with a 2003–06 US M3 donor

Research date: 22 October 2026. This builds on the guide's README "Fuel system", Phase 7, the Fuel rows of the parts list, Figure 7 and the Fuel open questions; WIRING-AND-CODING.md "Fuel-pump control" and "Fuel gauge and tank senders"; JOB-CARDS.md card 7a; and `research_notes/E46 M3 Touring open questions/fuel_pump_control.md` (round 1). I don't repeat those unless I correct or extend them.

**Source tags**

- **[ETK]**: read on a bmwfans.info parts-catalog page (BMW ETK data). bmwfans shows the current, superseding part numbers, filtered by the build month in the URL (for example `.../325i-M54/L-N/feb2003/...`). The filter works: a Jan 2001 Touring view still lists a pump-flange seal "to Mar '01" and a pipe clip "to Jul '02" that the Feb 2003 view drops.
- **[ETK-img]**: my reading of the ETK exploded drawing. It's an interpretation of a picture, not text.
- **[PDF]**: read in the BMW document.
- **[page]**: read on the page itself.
- **[captions]**: read in the auto-generated YouTube captions cached in round 1 (`yt/conv`, `yt/swap`); nothing was re-downloaded.
- **[round 1]**: read by the round-1 researcher and quoted in `fuel_pump_control.md`. Not re-read now, because e46fanatics.com now serves a proof-of-work bot check, which I didn't get round.
- **[snippet]**: seen only in a search-result summary.
- **[blocked]**: the site refused or challenged the request.

**Blocked or not reached:**

- RealOEM (Cloudflare challenge), so I have no VIN-level original-equipment numbers.
- e46fanatics (proof-of-work page).
- m3post (403).
- princeton.edu's TIS printouts (Cloudflare).
- newTIS, which wasn't tried because of its browser check.
- The shared web-search budget ran out near the end. Searches for BMW's E46 reserve-warning text and for the TIS 13 31 delivery-test text were not finished.

---

## Takeaway: what changes in the guide

1. **The part that meets the pump is the "fuel pipes set", not the rear feed line.** Both cars have a short hose assembly between the pump flange and the floor lines: Touring 16117175998, M3 16112283288 [ETK].
   - In BMW's drawings, the Touring set is clamped at both ends. The M3 set has a moulded push-on end at the pump and a quick-connector that takes the M3 rear feed line [ETK-img].
   - So the guide's question, whether the M3 rear feed's quick-disconnect fits the non-M pump's barb, asks about the wrong joint. The real unknown is whether the M3 pipe set fits the Touring pump. Nobody has documented that.
   - **Recommendation:** move the donor's whole in-tank set into your tank: delivery unit 16142229684, baffle 16112229656, jet pump 16142282208 and left sender 16142229683. Or fit the donor's tank. Then fit the M3 pipe set and the three M3 lines. Kalim (sedan) and Project BMW (Touring) worked this way; Tracks and Trails moved the M3 pump into his Touring's tank, but his lines aren't shown.
   - Keep your own pump only if it passes the 5-bar delivery test and you accept one undocumented adapter joint.
2. **The supply margin is thin if a pump only just meets BMW's floor.** BMW's delivery floor for every E46 engine, 1.12 L in 30 s (≈134 L/h), would leave about 34–44 L/h of return flow at the S54's 333 hp. That's our estimate, about half the M54's margin, and that return flow is what drives the jet pump. No OEM flow rating was found for either pump. Test at 5 bar.
3. **Test points.**
   - BMW puts the S54's pressure test point on a threaded fitting at the regulator under the left front floor (ST041). The M3 rail has no port.
   - To run the pump, bridge K96's socket pins 6 (from F54, terminal 30) and 2 (to the pump, terminal 87) with a fused switch.
   - TIS 13 31's collection point for the delivery volume wasn't found. Collect at the regulator housing's return outlet, so the pump is measured at 5 bar (our method).
4. **The M3 lines route unmodified under a Touring.** Four Touring builds say they fitted M3 fuel lines, a fifth shows new lines, and nobody reported a routing problem. ETK gives both cars the same clips and brackets.
   - Add these to the parts list:
     - the pipe set 16112283288
     - the M3 front purge line 16132229652
     - tubing supports 16122282049 and 16131177494
     - the filter-cover sealing element 13327830949
     - the regulator-housing copper ring 07119963129
     - the M3 vacuum-hose set: 11747797082, 64111368684 and 11727837591, metal sleeve 12517508831, cable tie 61131367599 and four clamps 61131365412.
5. **At the filler, only the flap changes.**
   - These are the same part numbers on the US 325i Touring and the US M3: the filler pot 51718208646, filler pipe 16117177490, pipe seal 16116755071, cap pin 16111184156, flap spring, rubber boot, sleeve and the 03/2003-dependent flap actuator [ETK].
   - Only the flap (Touring 51178208246, M3 51172695524) differs. So does the coupe's hinge (51172695527). The **M3 convertible's hinge, 51178151955, is the same part as your Touring's**.
   - Keep the pot and neck where they are, and graft the M3 skin's filler surround around them (M346). The guide's "the M3 filler pot moves 25–30 mm outboard; check the neck reaches it" is wrong as written.
6. **The EVAP system uses the same canister and leak-test pump, but they're mounted differently.**
   - The canister family and the DM-TL (16137193479, heated since 09/2001) are the same on both cars, and both sit under the right rear cargo floor [PDF, ETK].
   - The M3 mounts its canister crosswise in a holder (16132229735), with its own underbody cover (51717893604) and its own vent and purge lines. The Touring mounts it fore and aft between the battery tray and the spare well [captions, ETK].
   - Keep the Touring mounting if the well stays. Take the M3 holder, cover and EVAP lines if the M3 trunk floor goes in, as Renner's Touring did.
   - The liquid-vapour separator (ETK "expansion tank" 16136752641, the same on both cars, on the shared bracket 41148196386) sits in the right rear wheel well behind the trim [PDF]. That's inside the arch graft.
7. **Gauge.** Both tanks hold 16.6 US gal on BMW USA's spec sheets, and an M3 cluster codes an 8 L reserve threshold [NCS list]. Moving the M3 left sender along with the M3 pump keeps BMW's sender pairing. The guide's sender resistance values aren't on the bmwgm5 page it cites.
8. **Build date.**
   - ETK shows no fuel, line or EVAP part change at 03/2003: Feb 2003 and Mar 2003 Tourings list the same parts in every fuel and EVAP group. May 2005 lists the same pump, tank, line and filter parts; I didn't compare its EVAP group.
   - The one 03/2003 change near the fuel system is the filler-flap actuator (67116988090 to 03/2003, 67116987637 from 03/2003). It stays with your body.
   - M3 Jan 2003 and May 2006 lists match, and the coupe and convertible match.
   - The M56 is a different system throughout.
9. **No build has published a 5-bar delivery figure or a pressure under load.** The only number is one sedan swap's static 71 psi (4.9 bar) with a non-M pump [page].

---

## 1. Parts by build date (2003 325i Touring M54 vs 2003–06 US M3)

### Cited findings

**Touring, US 325i M54, Feb 2003 and Mar 2003 builds (identical lists in all seven fuel and EVAP groups), [ETK].** May 2005 lists the same pump, tank, line and filter parts (EVAP not compared). Jan 2001 differs only by superseded seals and clips and the pre-09/2001 leak-test pump.
- Fuel pump and level sensor ([feb2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/), [mar2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/mar2003/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/)):
  - delivery unit, right 16146766942
  - left fuel level sensor 16116768788
  - sucking jet pump 16146755880
  - rubber seal 16111184084 ×2
  - O-ring 16141183543
  - screw cap 16116762417 ×2
  - universal socket housing 61138352390
- Tank and attaching parts ([feb2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/fuel_supply/fuel_tank_attaching_parts/)):
  - plastic tank with left sensor 16116766940
  - tension strap 16116756583 ×2
  - damper rubber 16111184018 ×2
  - grommet 16111182454 ×2
  - spacer sleeve 16117194458 ×2
  - bolt 07119905532 ×2
  - nut 07146760121
  - fuel vent pipe 16117176511
  - plastic filler pipe 16117177490 ("to Jul '05")
  - plastic nut 51711958025 ×2
  - clamps 07129952119 (L42-48) ×2
  - filler cap pin 16111184156
  - rubber seal 16116755071
  - clamps 16121180240 and 07129952104
  - fuel hose 16117176011 (40×47×170)
  - hose 13537563456 (8×13 mm)
- Lines ([feb2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/fuel_supply/fuel_pipe_and_mounting_parts/)):
  - front feed 16126752183
  - rear feed 16126752180
  - return 16126752186
  - fuel pipes set 16117175998
  - "scavenge air line" (front purge line) 16111184135
  - hose 13537563456 with clamps 07129952104 ×8
  - pipe clip 16126761229 ×2
  - bracket 16127195327 ×2
  - brake-pipe bracket 34301164005
  - pipe clip 16121179396 ×2
  - sealing 16131184380
- Filter-regulator ([feb2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/fuel_preparation_system/fuel_filter_pressure_regulator/)):
  - one-piece filter with regulator 13327512019 (D=55 mm, L=315 mm)
  - bracket 13321435583 (D=55)
  - nut 07129904553
  - "vacuum pipe" 13327561060
  - black hose 11727545323 (3.5×1.8)
  - cable clamps 61138368029 ×2
  - filter cover 13328230397, with nuts 07147154227 ×2, screws 07147129160 ×3 and Prestol cages 07129901746 ×3
- EVAP ([feb2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/fuel_supply/exp_tank_activated_carbon_container/)):
  - expansion tank 16136752641
  - activated charcoal filter 16136751759 or 16136765440 (both "delivery discontinued"), and 16136765271 "only in conjunction with dust filter 16136765272"
  - caps 16131183918 ×2
  - vent pipes 16137176508 and 16131183895
  - rear purge line 16136751175 ("from Aug '99")
  - distribution piece 16137177237
  - hoses 16116772292 (18×24×80) and 13537563456
  - leak diagnosis pump 16137193479 ("from Sep '01")
  - bolts 07119905591 ×2
  - screws for plastic 07147194471 ×3
  - plastic nuts 51711958025 ×2
- Purge valve, engine side ([feb2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/fuel_preparation_system/fuel_tank_breather_valve/)): valve 13901433603 and lines 13907557924 and 13907558190. These go away with the M54.
- Underbody canister covers ([feb2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/vehicle_trim/underfloor_coating/)): "Cover, activated charcoal filter front" 51718233265 and "bottom" 51718233266.
- Filler area ([feb2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/bodywork/side_panel_tail_trim/), [mar2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/mar2003/browse/bodywork/side_panel_tail_trim/)):
  - fill-in flap 51178208246
  - spring 51171888374
  - hinge 51178151955
  - tank filler pot 51718208646
  - sleeve 51258151536
  - rubber boot 51258151799
  - filler-flap actuator 67116988090 "to Mar '03", or 67116987637 "from Mar '03" (the only 03/2003 split I found near the fuel system)
- Wheelhouse ([feb2003](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/bodywork/rear_wheelhouse_floor_parts/)): fuel expansion-tank bracket 41148196386, beside the right inner wheelhouse 41148231758 ("from Sep '00").

**US M3 S54, coupe; Jan 2003 and May 2006 builds give identical lists, except that the filler-pipe row (16117177490, "to Jul '05") is missing for later cars, which looks like a catalogue gap. The convertible is identical to the coupe. [ETK]**
- Pump and sender ([coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/), [convertible](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/)):
  - delivery unit 16142229684
  - left sensor 16142229683
  - jet pump 16142282208
  - **fuel baffle fixture 16112229656**
  - The same rubber seal 16111184084, O-ring 16141183543, screw cap 16116762417 and socket housing 61138352390 as the Touring.
- Tank ([coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_tank_attaching_parts/)): tank 16112229736. **Every other part on the Touring's list is the same number**: straps, damper rubbers, grommets, spacer sleeves, bolts, nut, vent pipe, filler pipe, filler hose 40×47×170, clamps, cap pin and seal.
- Lines ([coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pipe_and_mounting_parts/)):
  - front feed 16122229410
  - rear feed 16122229409
  - return 16122229411
  - fuel pipes set 16112283288
  - "scavenging line front" 16132229652
  - clamps 07129952104 ×3
  - tubing supports 16122282049 and 16131177494
  - the same pipe clips 16126761229 and 16121179396, bracket 16127195327, brake-pipe bracket 34301164005 and sealing 16131184380 as the Touring
- Filter-regulator ([coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_preparation_system/fuel_filter_pressure_regulator/)):
  - filter 13327831089
  - regulator housing 13537830368
  - gasket ring 07119963129 (A12×15 Cu)
  - regulator 13531404089
  - O-rings 13531720251 (20×2.5) and 13531720252 (5×1.5)
  - lock ring 13531736234
  - sealing element 13327830949
  - vacuum hose blue 11747797082 (3.3×1.8, by length)
  - vacuum hose white 64111368684 (2×4, by length)
  - hose 11727837591
  - corrugated metal tube 12517508831 (Ø4.5 mm, by length)
  - cable tie 61131367599
  - cable clamps 61131365412 ×4
  - The same bracket 13321435583 and cover 13328230397 (with the same nuts and screws) as the Touring.
- EVAP ([coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/)):
  - Same as the Touring: expansion tank 16136752641, charcoal filter 16136751759 (discontinued), leak diagnosis pump 16137193479 ("from Sep '01"), dust filter 16136751758, distribution piece 16137177237 and hose 16116772292.
  - M3-only:
    - **holder for activated charcoal filter 16132229735**, with self-locking M6 nuts 07147153450 ×4
    - charcoal filter 16131183906
    - vent pipes 16132283286 and 16132229415 (US only)
    - "scavenging line rear" 16132229417
  - Underbody cover: "Cover, activated charcoal filter front" 51717893604 ([coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_trim/underfloor_coating/)).
- Engine side (comes with the S54):
  - feed pipe 13317831683 with O-ring 13641730767 ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_preparation_system/valves_pipes_of_fuel_injection_system/))
  - purge valve 13907831770 and lines 13907837661 and 13907837663 ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_preparation_system/fuel_tank_breather_valve/))
  - idle-air distribution pipe, the ETK "additional air line": 13547831481 to 09/2004, 13417834068 from 09/2004 ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_preparation_system/idle_regul_valve_additional_air_line/))
- Filler area ([coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/side_panel_tail_trim/), [convertible](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/bodywork/side_panel_tail_trim/)):
  - fill-in flap 51172695524 (primed)
  - hinge 51172695527 on the coupe, but **51178151955 on the convertible, the same as the Touring's**
  - the same pot 51718208646, sleeve 51258151536, boot 51258151799, spring 51171888374, spacer sleeves and stop buffers as the Touring
  - the same 03/2003 actuator split (67116988090, then 67116987637)

**Part usage pages [ETK].**
- The filler pot [51718208646](https://bmwfans.info/parts-catalog/51718208646/), filler-pipe seal [16116755071](https://bmwfans.info/parts-catalog/16116755071/) and cap pin [16111184156](https://bmwfans.info/parts-catalog/16111184156/) are all listed for the US 325i M54 sedan and Touring, the 325i M56 Touring, and the US M3 coupe and convertible.
- Also shared by the US non-M and the US M3:
  - filler pipe [16117177490](https://bmwfans.info/parts-catalog/16117177490/)
  - vent pipe [16117176511](https://bmwfans.info/parts-catalog/16117176511/)
  - expansion tank [16136752641](https://bmwfans.info/parts-catalog/16136752641/)
  - leak pump [16137193479](https://bmwfans.info/parts-catalog/16137193479/), which the M56 uses too
  - dust filter [16136751758](https://bmwfans.info/parts-catalog/16136751758/)
  - canister [16136751759](https://bmwfans.info/parts-catalog/16136751759/)
- Expansion-tank bracket [41148196386](https://bmwfans.info/parts-catalog/41148196386/): every E46 including the M3.
- M3-only:
  - holder [16132229735](https://bmwfans.info/parts-catalog/16132229735/), M3 cover [51717893604](https://bmwfans.info/parts-catalog/51717893604/) and pipe set [16112283288](https://bmwfans.info/parts-catalog/16112283288/), on Euro and US M3s.
  - [16132229415](https://bmwfans.info/parts-catalog/16132229415/), on US M3s only.

**Supersession history (part pages [ETK]; the dates are ETK's ranges for each number; all are "exchangeable retrospectively" unless noted):**

| Part | History |
|---|---|
| Touring tank | [16111184899](https://bmwfans.info/parts-catalog/16111184899/) (Mar '98–Sep '03), then [16116762962](https://bmwfans.info/parts-catalog/16116762962/) (Mar '03–Jul '04), then [16116766940](https://bmwfans.info/parts-catalog/16116766940/) (May '04–) |
| Touring delivery unit | 16141184276 (Mar '98–Mar '00), then [16146752499](https://bmwfans.info/parts-catalog/16146752499/) (Nov '99–Jul '04), then [16146766942](https://bmwfans.info/parts-catalog/16146766942/) (May '04–) |
| Touring left sender | 16146752192, then 16146755879 (Mar '01–Sep '04), then [16116768788](https://bmwfans.info/parts-catalog/16116768788/) (May '04–) |
| Touring jet pump | 16141184282, then 16146752193 (Sep '99–Jul '01), then [16146755880](https://bmwfans.info/parts-catalog/16146755880/) (Mar '01–) |
| Touring filter-regulator | 13321712296, then 13321439407 (Jun '00–Nov '01), then [13327512019](https://bmwfans.info/parts-catalog/13327512019/) (Sep '00–) |
| Touring pipe set | 16111184390 (Mar '98–Aug '05), then 16117175998 |
| M3 pipe set | 16112229751 (Jul '00–Aug '07), then 16112283288 |
| M3 vent pipe | 16132229413, then 16132283286 |
| Leak pump | 16131184849 (Aug '99–Aug '00), then 16136756440, then 16137193479 (heated) |
| Touring dust filter | 16136751758, then 16136765272 (Jun '03–, "non exchangeable retrospectively") |
| M3 tank, pump, sender, jet pump, baffle | One number each since Jul '00 (jet pump Oct '00) |

**Locations, from BMW [PDF]:**
- "The fuel filter assembly is located under the left front floor area (next to the frame rail)… The fuel return line is located on the filter/regulator assembly" ([ST041 Part 2, p.25](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)).
- "The E46 M3 access plates are located under the rear seat… The passenger side allows access to the fuel pump / sending unit. The driver side accesses the sending unit / syphon jet" (same, p.40).
- "Liquid/Vapor Separator (located in the right rear wheel well behind the trim)"; "The Active Carbon Canister is located under the luggage compartment floor with the DM TL Pump"; the purge valve is "located under the intake manifold" and purges "through the idle air distribution pipe into the intake manifold" ([ST041 Part 3, pp.63–64](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf); this applies to the US E46 M3).
- E46 non-M (1999 MS42 module): "The location of the LDP and charcoal canister have changed. This combination assembly is located under the right rear trunk floor" ([ST034, p.46](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/10%20p1%20Engine%20Management%20Sys%20Internet-1.pdf)). A later generic BMW module puts "the Carbon Canister with DM TL and air filter… at the right rear underside of the vehicle, below the luggage compartment floor" ([ST055 Emissions Management, p.53](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics/10_Emissions%20Management.pdf)).
- "All DMTL pumps starting September 09, 2001 are heated… The DM-TL connector has been changed from 3 pin to 4 pin" ([ST043, 2002 E46 update, p.6](https://archive.org/download/BMWTechnicalTrainingDocuments/ST043%202002%20System%20Diagnosis/8%20E46%20Update.pdf)). Both 2003 cars have the heated, 4-pin pump.

**Canister orientation, from a build [captions]:** "because the m3 doesn't have a spare tire or a spare tire well the charcoal canister actually sits in there side to side and in the non-m cars they sit front to back in between the battery tray and the spare tire well" ([Tenza Motorsports – No more SULEV (2021), 01:20](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=80s)). "if you're going from m3 to any non-m car you just make sure that you turn the charcoal canister from side to side to front to back" ([06:00](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=360s)). This was a 2004 US M56 Touring that kept its spare well; the canister he compared against was the M56's metal unit.

**M56 SULEV Touring, US, for comparison [ETK]:**
- metal tank with filler pipe 16116763569 and its own straps 16116757172
- pump control unit 16146912019
- a single feed line 16127513780 and no return
- front purge line 16127514320
- metal canister 16126757177 with holder 16116757507
- dust filter 16136757522
- the same leak pump 16137193479 and filler pot 51718208646
- the pump group lists only the plug: the pump is sealed in the tank.

Pages: [tank](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/L-N/browse/fuel_supply/fuel_tank_mounting_parts/), [lines](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/L-N/browse/fuel_supply/fuel_pipe_and_scavenging_line/), [EVAP](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/L-N/browse/fuel_supply/activated_charcoal_filter_fuel_ventilat/). BMW: SULEV injectors "screw into the rail and a tap to test pressure readings is NOT provided"; "The fuel tank can be exchanged only as a complete unit" ([ST047, 2003 E46 FL, pp.6–8](https://archive.org/download/BMWTechnicalTrainingDocuments/ST047%202003%20System%20Diagnosis/5%20E46%20FL.pdf)).

### Inferences
- **(Inference) Pre- and post-03/2003 Tourings take the same fuel parts in this build.** The MS43-to-MS45.1 change doesn't touch the fuel hardware. A tank number first dated Mar '03 (16116762962) superseded the older one, but ETK treats it as interchangeable, and 16116766940 now replaces both. Original numbers on a 2003 car are most likely tank 16111184899 or 16116762962, delivery unit 16146752499 and left sender 16146755879. Check the labels; RealOEM was blocked.
- **(Inference) The M3 tank fits any 2001–05 US M54 Touring's mounts**, because every interface part is the same number: straps, bolts, nut, filler pipe, filler hose, vent pipe, expansion tank and pot. That's backed by builds on 2002–2004 Tourings (section 5).
- **(Inference) Delivery-unit flanges are interchangeable between the tanks**, because both use the same flange seal 16111184084, lock ring 16116762417 and plug housing 61138352390. That's backed by builds (section 2).
- **(Inference) The canister and DM-TL can stay as your Touring has them**, unless the floor option removes their mounting (section 4).

### Gaps
- VIN-level original numbers (RealOEM blocked).
- Which canister number a given 2003 Touring left the factory with: 16136751759, 16136765440, or the later 16136765271 with dust filter 16136765272.
- Why the M3's left sender and jet pump differ from the non-M parts; ETK doesn't say.

---

## 2. Supply: can the Touring's tank, pump and senders feed the S54 at 5 bar?

### Cited findings

**What BMW says about the M3's supply [PDF]** ([ST041 Part 2, pp.24–26, 33, 40–42, 46](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf); the same text is in [ST055 "MS S54"](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf); this applies to the US E46 M3):
- "The baffling has been modified for the E46 M3 fuel pump pickup in the right hand side of the fuel tank to maintain fuel supply during aggressive cornering"; "A Syphon jet is required… linked to the fuel return line" (p.24).
- "A high output fuel pump is utilized to match the fuel supply demands of the S54 engine (5 Bar)" (p.33).
- "The fuel pressure is set to 5.0 Bar (+/- 0.2)"; the diagram shows 3.8 bar at part throttle (p.26).
- The pump test: "Remove the fuel pump relay/module… Connect the Relay Bypass Switch to pin 87b and 30 of the relay socket… If the 5 bar… fuel pressure is not achieved or bleed off is more than 0.5 bar, refer to 13 31 of the Repair instructions… The Fuel Hose Clamp Tool can be used to isolate bleed off from the pump (non-return check valve) or the pressure regulator (restriction valve). Also verify power supply to the fuel pump." The DIS screenshot reads "4.55 bar Minimum" (p.41).
- "Fuel volume must be tested to verify: 1. Fuel Pump Output 2. Restriction are not present in the pump, lines/hoses and fuel filter." The picture shows a hose into a graduated vessel marked "13 3 020", in a generic engine bay. It doesn't say where the hose is connected (p.42).
- **The gauge connection:** "A threaded fitting provides a test point at the fuel pressure regulator. This threaded adapter fitting allows Adapter #13 5 220 to be coupled to the DIS Pressure Adapter. Caution! Residual fuel pressure may be present" (p.46).
- "DO NOT OPERATE THE FUEL PUMP unless it is properly installed in the fuel tank and is submersed in the fuel" (p.39).

**BMW's generic fuel test module [PDF]** ([ST055 "04_Fuel Management", pp.60–64](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics/04_Fuel%20Management.pdf)). It covers several BMW engines; the method and tools carry over, while the 3.5-bar figure is the M54's.
- It names the repair instructions "REP 13 31 032 Check fuel pressure" and "REP 13 31 029 Checking fuel pump delivery pressure (M54)".
- The hand gauge is SWZ 13 3 060.
- "For vehicles equipped with 'quick-release' couplings, install special tool (SWZ 13 5 270) between the fuel filter (1) and pressure supply hose (2)".
- "Later production fuel rails are equipped with a threaded adapter fitting… Adapter (SWZ 13 5 220)". That is the same adapter ST041 names for the S54 regulator.
- "During fuel system repair that involves 'sealing rings', always replace them with new COPPER rings only."

**Bentley specifications [round 1]**, quoted on [e46fanatics "Fuel pressure info"](https://www.e46fanatics.com/threads/fuel-pressure-info.1116777/):
- S54: 5.0 ± 0.2 bar, and more than 4.5 bar after 20 minutes.
- All other engines: 3.5 ± 0.2 bar, and more than 3 bar after 20 minutes.
- "All engines 1.12 liter… for 30 seconds at 12 Volts or while crank[ing]".

**A trade magazine's E46 test** ([the bimmer pub, March 2013, pp.5–8](https://automotivetechinfo.com/wp-content/uploads/2013/03/the-bimmer-pub-2013-march.pdf) [PDF]). The car was a 2004 325xi M54; the figures were given for the E46.
- "fuel pressure should be 3.5 BAR both Key On Engine Off and Key On Engine Running… fuel volume should be 2.25L per minute". That's 1.125 L per 30 s, which matches Bentley.
- They measured with a flow gauge in series "between the fuel hose and filter on the pump side", after "removing two covers with an 8mm socket and a Phillips screwdriver".
- "BMW simply warns that the pump should not pull more than nine amps on 'passenger cars'."

**A generic BMW technician's article** ([Luke Murray, 2016, reprinted in the bimmer pub, Oct 2019](https://automotivetechinfo.com/wp-content/uploads/2019/10/Diagnosing-Fuel-Delivery-Issues.pdf) [PDF]; [diag.net version](https://diag.net/discussion/sfvx6hdfr76ldruqwqgq6gzyri) [page]):
- "some chassis have the test port built into the fuel filter and pressure regulator assembly".
- Rule of thumb: "one liter in 30 seconds" (diag.net), or "a quart in 30 seconds" (magazine).
- Variable pump speed "first appeared on the E39 and E46 Motorsport vehicles… to only deliver the necessary volume… and a little extra to ensure the return system could still transfer fuel via the syphon pump system in tank".
- At the pump connector under the rear seat, with the pump running, "You should be measuring within half a volt of system voltage"; on the ground side, "A reading of anything over half a volt is a problem".

**Where owners found the test point:**
- "On E46 M3 the valve is next to the fuel filter under the car" (Mangozac, 18 Feb 2019, [z4-forum](https://z4-forum.com/threads/fuel-pressure-measurement.112453/) [page]).
- "no Schrader valve on the M3 fuel rails" ([m3post](https://www.m3post.com/forums/showthread.php?p=23275443) [snippet; 403 when fetched]).

**An S54 swap that kept a non-M pump** ([NAM3 82513](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/82513-s54-swap-to-ms42-car-no-start) [page]; MS42 323i sedan, M3 regulator fitted):
- "Fuel pressure is good, via the port on the FPR" (#4).
- "I didn't touch the wiring on the fuel pump, the pump is working and i have 71 psi at the valve on the FPR" (332, #6, 3 Feb 2021).
- The car ran after EWS and old-fuel fixes. No load or flow data.

**Moving the M3 pump into non-M tanks:**
- Kalim, 2003 325i sedan: M3 pump(s), baffle, transfer pipe and left sender. "remove the old transfer pipe and install the M3 one into the baffle" [round 1].
- rkneeshaw, 2003 330i ZHP: "move the hose out of the lower plastic part… to the top of the M3 baffle, install the fuel pump in front of it". He found the M3 pump body smaller [round 1].
- jacobs323i: "needs a sleeve to fit into a non-m" [round 1]. That conflicts with rkneeshaw's "plug and play".
- TxZHP04, 330i: starvation near ¼ tank until he fitted the M3 pump; he recalled "10-20% more flow" [round 1].
- In Touring tanks:
  - Tracks and Trails: "we're simply going to swap the pumps over to this one… And now M3 fuel pump… Plug at the back. Easy peasy" ([Tracks and Trails – I spent $10,000… rear end (2025), 26:40](https://www.youtube.com/watch?v=eMJLXbvzckE&t=1600s), [27:20](https://www.youtube.com/watch?v=eMJLXbvzckE&t=1640s), [27:40](https://www.youtube.com/watch?v=eMJLXbvzckE&t=1660s)) [captions].
  - Project BMW swapped both "fuel pumps" through the two access holes with the tank lowered ("it's only like three bolts") ([Project BMW – Day 5 (2021), 03:20](https://www.youtube.com/watch?v=t9S0iXJj2GI&t=200s), [03:40](https://www.youtube.com/watch?v=t9S0iXJj2GI&t=220s)) [captions].
- BimmerWorld (vendor): the baffle "installs under the right side (passenger side, on US cars) fuel pump assembly", $123.62 in Oct 2026 ([BimmerWorld](https://www.bimmerworld.com/Intake-Fuel/Fuel-Filters/Genuine-BMW-Fuel-Baffle-Fixture-16112229656-E46-E46-M3.html)) [page].

**Pump circuit wire sizes.** These come from the manual's WDS tables (WIRING-AND-CODING.md, "How each car switches the pump", [SP0000014336](https://wds.psjr.org/en/e46/svg/SP0000014336.svg), [SP0000014408](https://wds.psjr.org/en/e46/svg/SP0000014408.svg)).
- Touring K96 socket: pin 6 is the load supply from F54 (15 A, 2.5 RT/VI); pin 2 is the output to the pump (1.5 WS/BL).
- US M3: the module output to the pump is 2.5 RT/WS.

### Inferences (labelled)
- **(Inference) Demand against supply.**

  | Engine | Power | Estimated full-load fuel use* | Per 30 s | Return left if the pump just meets 1.12 L/30 s |
  |---|---|---|---|---|
  | S54 (US M3) | 333 hp ≈ 248 kW at 7,900 rpm (ST041) | 67–74 kg/h ≈ 90–100 L/h | 0.75–0.83 L | 34–44 L/h (26–33% of pump flow) |
  | M54B25 (325i) | 184 hp ≈ 137 kW (BMW USA 2003 sheet) | 37–41 kg/h ≈ 50–55 L/h | 0.41–0.46 L | 79–84 L/h (59–63%) |

  *Assumes a full-load BSFC of 0.27–0.30 kg/kWh and petrol at 0.745 kg/L. These are my assumptions, not BMW figures.

  The return flow drives the jet pump that moves fuel from the left half to the pump side. At the S54's full power it is roughly half what it is on the M54 with the same pump. That matches TxZHP04's starvation near ¼ tank, and it explains why BMW gave the M3 a high-output pump and a baffle.
- **(Inference) Test at the S54's regulated pressure, not the M54's.** A turbine pump flows less at 5 bar than at 3.5 bar. A Touring pump that meets 1.12 L at 3.5 bar may not at 5 bar.
- **(Inference) The donor's in-tank set is the better default, not a fallback.** It's BMW's validated combination: pump, baffle, jet pump and senders. It arrives with the donor, mates with the M3 pipe set and lines with no adapter (section 3), and gives the M3 cluster its own senders (section 4). Keeping the Touring pump saves no parts and adds one undocumented joint.
- **(Inference) On the K96 relay, an M3 pump runs at full speed all the time.** That's more return flow, which helps the jet pump, plus more heat and noise. No failures have been reported. The Touring's 1.5 mm² pump feed is thinner than the M3's 2.5 mm², so check the voltage at the pump connector (≤0.5 V drop).
- **(Inference) Neither car's rail has a test port for the S54 build.** The test point is the threaded fitting at the M3 regulator housing. The 323i swapper's "valve on the FPR" and the z4-forum post agree. Because BMW names the same adapter (13 5 220) for this fitting and for the M54's later rails, one gauge adapter should do both: the M54 baseline before the swap and the S54 test after. That's an inference from the shared tool number.

### Gaps
- No OEM flow rating (L/h at bar) for 16146766942 or 16142229684, and no current-draw figure other than the magazine's "nine amps".
- I found no TIS 13 31 text for the E46 or S54 delivery-volume test: neither where the fuel is collected nor at what pressure. Bentley's 1.12 L/30 s may be measured at low pressure (open feed) or at regulated pressure (return line). Our procedure uses the stricter case.
- No build has published a 5-bar delivery figure or a pressure under full load, with either pump.
- Whether the M3 delivery unit needs a sleeve in a non-M tank (round-1 posts conflict).

---

## 3. Lines and routing

### Cited findings

**Which joint mates with the pump [ETK-img].** The drawings are Touring [8de](https://ills.bmwfans.info/8de.png) and M3 [1scw](https://ills.bmwfans.info/1scw.png), from the line pages cited in section 1.
- Both cars: the pump flange connects to the floor lines through the "fuel pipes set" (position 4). That's two hoses: feed (pump to rear feed line) and return (return line to a nipple on the tank).
- Touring: hose clamp 07129952104 (L12-15) on both ends of both hoses. The rear feed line, return and front feed line are plain tubes joined to the filter by short hoses (13537563456, 8×13 mm) and clamps, eight clamps in all.
- M3: the feed hose has a moulded connector at the pump end with no clamp drawn, and a quick-connector at its lower end. The M3 rear feed line's angled male end sits in that quick-connector. The rear feed line's other end is a quick-connector on the filter inlet. Only the return hose has clamps (three clamps in all).
- So the rear feed line doesn't touch the pump on either car.
- A round-1 snippet said "The fitting on the M3 pump is press not clamp, sender fitting is same clamp" [snippet]. That fits these drawings, but the source thread wasn't opened.

**Filter-regulator [ETK-img]** (drawings: Touring [1oqq](https://ills.bmwfans.info/1oqq.png), M3 [1p6t](https://ills.bmwfans.info/1p6t.png)):
- The Touring's one-piece unit has two ports at the rear end (inlet and return) and the outlet plus the vent nipple at the front. The vent pipe 13327561060 runs from that nipple.
- The M3 filter takes the rear feed line's quick-connector at its rear inlet. The regulator housing sits on its front end and carries the regulator, the front-feed outlet (quick-connector) and the return outlet.
- Both sit on the same bracket 13321435583 under the same cover 13328230397. The M3 adds sealing element 13327830949 at the cover.
- BMW: "The fuel return line is located on the filter/regulator assembly", and the "regulator is influenced by engine vacuum via a hose connected to the idle air distribution pipe" ([ST041 Part 2, p.25](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)) [PDF].

**Your M54's regulator hose is a vent [PDF].** BMW on the E46 M52TU, whose regulator design the M54 carries over (inference): "The maintained fuel pressure at the fuel distribution rail is a constat 3.5 Bar. the vacuum line no longer connects to intake manifold vacuum, but is routed to the crankcase cyclone separator (in case of regulator diaphragm leakage)" ([ST034, p.32](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/10%20p1%20Engine%20Management%20Sys%20Internet-1.pdf)). That's BMW backing for the guide's "vent, not vacuum" statement.

**The S54's vacuum reference [ETK, ETK-img]:**
- M3 parts: blue hose 11747797082, white hose 64111368684, hose 11727837591 and corrugated metal sleeve 12517508831 (Ø4.5 mm, which suggests the run passes heat), cable tie 61131367599 and clamps 61131365412 ×4 (M3 filter page above).
- The S54's idle-air distribution pipe ("additional air line" 13547831481, or 13417834068 from 09/2004) has a small nipple in its ETK drawing ([1p85](https://ills.bmwfans.info/1p85.png)). That is most likely the regulator's reference port (inference).

**Engine end of the feed:**
- The S54 feed pipe 13317831683 is "the fuel supply pipe from the fuel line up to the fuel rail… Use with o-ring part # 13641730767… for the connection to the fuel rail" ([BimmerWorld](https://www.bimmerworld.com/Intake-Fuel/Fuel-Feed-Pipe-BMW-E46-M3-MZ3-S54-MZ4-13317831683.html)) [page].
- The Touring's front feed line instead ends at the M54's inlet hose 13537548987 [ETK].

**Purge (EVAP) line [ETK]:**
- Touring: front 16111184135 and rear 16136751175, to the M54 purge valve 13901433603.
- M3: front 16132229652 and rear 16132229417, to the S54 valve 13907831770 and its hose 13907837663. In the M3 drawing, that hose has a quick-connector end ([1pnj](https://ills.bmwfans.info/1pnj.png)) [ETK-img].
- Project BMW: "this is the 325 line and it's not going to work with this motor so i'm going to have to pull it out the m3" ([Project BMW – Day 5 (2021), 00:40](https://www.youtube.com/watch?v=t9S0iXJj2GI&t=40s)) [captions].

**M3 lines under Tourings [captions, page]:**
- Project BMW, US 325i Touring: "a lot of the fuel lines are different on the m3 so basically i'm gonna have to drop all the fuel lines from the tank to the front of the car" ([00:20](https://www.youtube.com/watch?v=t9S0iXJj2GI&t=20s)). Then: "there's a lot of room right here for all these fuel lines… let me take a look at the m3 if it's the same yeah sure enough so it is it is the same" ([03:00](https://www.youtube.com/watch?v=t9S0iXJj2GI&t=180s)). The car ran ([00:00](https://www.youtube.com/watch?v=t9S0iXJj2GI)).
- yavz, UK 318i Touring: "Proceeded to plum in the m3 loom. Along with the brake and fuel lines." ([PistonHeads, 24 Feb 2017](https://www.pistonheads.com/gassing/topic.asp?h=0&f=47&t=1655205)) [page].
- ThaChileanDude, Touring: "s54 has different fuel pumps and different fuel lines so all that has to come out and all that's going to be being replaced by M3 parts" ([10 days (2024), 02:20](https://www.youtube.com/watch?v=iSgClonTiQg&t=140s)).
- Renner (Miami), Touring: "all these lines are M3 because the fuel filter and pressure regulator… is different" ([Larry Chen – Renner's E46 M3 Touring (2025), 21:00](https://www.youtube.com/watch?v=YM2gyQOaJCk&t=1260s)).
- puma1824, US 2003 325iT built by M3Projekts: photo captions "Some nice new fresh fuel lines" and "M3 fuel tank" (#145–146, 3 Jan 2023, [NAM3](https://nam3forum.com/forums/forum/main-forum/member-build-journals/155763-e46-m3-touring-conversion-to-europe-and-back/page10)) [page]. Where the lines came from isn't stated.
- Tenza, 2004 M56 Touring: "I went through all of the mounting points on the bottom of the m3 and they match exactly to the wagon" ([01:40](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=100s)). "on the wagon even though there's no fuel filter there's even a spot for this to lock in" ([06:20](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=380s)). The M56 has no external filter; the M54 does.
- Feed and return reversed at the filter caused a no-start ([NAM3 82513, #5](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/82513-s54-swap-to-ms42-car-no-start)) [page].

**Near the rear subframe [captions].** Fitting the M3 canister's vent hoses on his Touring: "i've got to be really careful because the subframe sits right here so i don't have a lot of room back behind here". He made one hose from radiator hose with an insert so it wouldn't kink, and pulled another through on a string because "it doesn't flex for probably good eight inches" ([Tenza – No more SULEV (2021), 04:40](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=280s), [05:20](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=320s)).

### Inferences
- **(Inference) The M3 lines clip to the Touring's existing points.** Both lists use the same pipe clips, brackets, brake-pipe bracket and sealing. The M3 adds two tubing supports, and the floor from the front to the tank is common to E46 bodies. Five Touring builds bear this out without a reported problem.
- **(Inference) The feed and return lines end at the tank, ahead of the rear subframe.** They run along the left floor past the filter (BMW: under the left front floor). The subframe-mount reinforcement plates don't touch them.
  - The parts that do pass the right rear subframe, RACP and wheelhouse are the EVAP vent lines, the filler pipe (over the axle) and the canister lines (under the right rear floor).
  - After welding plates, check that every EVAP clip stud and route is still clear.
- **(Inference) The M3 exhaust relationship is the M3's own.** The lines run on the left floor beside the tunnel, as on the M3, and the M3's metal-sleeved vacuum hose is BMW's answer for the heat along that run. Don't swap the sleeve for plain hose.
- **(Inference) With M3 lines, feed and return are harder to mix up.** The feed joints are quick-connectors and the return is hose and clamp. With the Touring's all-hose joints they look alike, so label them anyway.

### Gaps
- The quick-connector size isn't documented (5/16 in, 7.89 mm and 3/8 in adapters are all on sale). Measure if you ever need an adapter.
- Whether the M3 pipe set's pump end latches onto the Touring pump's outlet, and the reverse.
- The joint type between the M3 front feed line and the S54 feed pipe. Probably a quick-connector, as on the M3.
- Whether the M3 front purge line (16132229652) mates with the Touring's rear purge line (16136751175). If it doesn't, take the M3 rear line (16132229417) too.

---

## 4. Gauge and filler

### Cited findings

**Capacity [page, PDF]:**
- BMW USA, "2003 BMW 325 Sedan and Sport Wagon Specifications": "Fuel capacity, U.S. gal. | 16.6", marked as applying to all models (325i and 325xi sedan and Sport Wagon) ([BMW USA press](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437)). The same sheet lists the engine management as "Siemens MS 43".
- BMW USA, "2002 BMW M3 Coupe & Convertible Specifications": "Fuel capacity, U.S. gal. 16.6" ([BMW USA press](https://www.press.bmwgroup.com/usa/article/attachment/T0022127EN_US/41385)).
- ST041 gives the M3 63 L ([ST041 "M3 Complete Vehicle", p.6](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf)).

**How the E46 cluster reads the senders [PDF]** ([ST052 "E46 Driver Information Systems", pp.9, 11, 20](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03b_E46%20Driver%20Information%20Systems.pdf)):
- "Two lever action sensors are wired in parallel to the cluster. The two varying voltage signals are processed by the cluster for fuel gauge and low fuel warning display."
- "Low Fuel – Based on the processing for the low fuel indicator lamp, this output is also sent to the DME (ECM) control module. The signal is stored along with a mis-fire detection fault for troubleshooting purposes."
- Cluster test 06 example: "LH sensor input = 23.7 liters RH sensor = 41.5 liters… Total tank level averaged = 65.2 liters… 1 = both sensors OK 2 = one sensor fault 3 = implausible".

**Coding: a 2002 M3 coupe's cluster [page]** ([NCS FSW/PSW list, NikolaiD 2011, AKMB pp.4–5](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf)):
- `TANK_KENNLINIE` (tank calibration): `60_l_literskala / dad_tank_diesel / metalltank`.
- `TANK_SCHWELLE_RESERVE` (reserve threshold): `8_l`.
- `TANK_SCHWELLE_AUF/AB`: `6_l`.
- `TANK_SICHERHEITSFAKTOR`: 1.3.
- `TANK_BERUHIGUNGSZEIT`: 10 s.
- `TANK_FILTER_FALLEND`: 1.9 l/min.

These are one car's values. The guide's chosen curve, `60_l_literskala`, is among the options.

**Where the leak test depends on the gauge [PDF, page]:**
- BMW's "Check Filler Cap" lamp "will be activated if change in fuel volume as read by the fuel level sensors precedes a failed Evap System test" ([ST043, p.6](https://archive.org/download/BMWTechnicalTrainingDocuments/ST043%202002%20System%20Diagnosis/8%20E46%20Update.pdf)).
- The MSS54's leak-test status table includes `8_WARTEN_FUELLSTAND` (waiting for fuel level), `51_ABBRUCH_NACHTANKEN` (aborted, refuelling detected), `52_ABBRUCH_TANKDECKEL_FEHLT`, the result `35_ERGEBNIS_DECKEL_FEHLT` (cap missing) and `34_ERGEBNIS_FEIN_DICHT` (sealed against a fine leak) ([SGBD MSS54DS0, table LDPSTATUS](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)) [page].
- The manual already lists the jobs (`START_SYSTEMCHECK_DMTL`, `LESEN_SYSTEMCHECK_DMTL`, `STATUS_TANK_DICHTHEIT`).

**Sender resistance [page].** The guide cites [bmwgm5 "E46 Fuel Level"](https://www.bmwgm5.com/E46_Fuel_Level.htm) for about "70 Ω empty to 310 Ω full on the left and 70 to 395 Ω on the right". Fetched today (3.7 KB), that page lists only the pins and wire colours:
- X11175 pin 11: right sender signal, 0.5 SW/RT/WS.
- Pin 12: right sender ground, BR/SW/WS.
- Pin 15: left sender signal, SW/RT/GE.
- Pin 16: left sender ground, BR/SW/GE.

It has no resistance values.

**Plugs [captions].** On a normal M54 or S54 tank there are "six wires there is a large power and ground and then there are two small powers and two small grounds… four of these wires will go to the fuel pump side… on the driver's side of the car you'll have the other small ones". The M56 has "all of them all in one plug". He matched the pairs by their yellow and white tracer dots ([Tenza – No more SULEV (2021), 07:20](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=440s), [08:00](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=480s)). His naming of which tracer goes to which side conflicts with bmwgm5's; go by the tracer pairs on your own plugs.

**Filler [ETK, captions]:**
- The common filler parts are listed in section 1. Only the flap differs, and the hinge on a coupe donor.
- M346: "this hole for the most part lines up and a lot of guys take their quarter panel and… line the M3 filler neck hole… it's still not 100% right… the shape of this is all different so what we did was we actually have the piece from the M3… we held the outer skin up and this lined up with the outer skin and then we had to mark the holes for the gas tank flap" ([M346 Projects – Pt 14 (2024), 36:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2200s), [37:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2240s)).
- M346 again: "the stock piece was a slightly different shape, molded differently, sat back a little bit further and it had the two holes for the gas tank flap bracket" ([39:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2340s)).
- In the shared tank drawing ([272s](https://ills.bmwfans.info/272s.png)) [ETK-img], the plastic filler pipe runs from the pot down to the tank's filler stub, where the 40×47×170 hose and two L42-48 clamps join it.

**Leak-test plumbing at the arch [PDF, ETK]:**
- The separator is in the right rear wheel well behind the trim (ST041 Part 3, above).
- It sits on bracket 41148196386, which is common to every E46, beside the inner wheelhouse.
- The canister and DM-TL are under the right rear cargo floor.

### Inferences
- **(Inference) M3 senders plus an M3 cluster plus a 16.6 gal plastic tank is BMW's own calibration.** Both tanks hold 16.6 gal. With the M3 delivery unit and the M3 left sender in your tank, the cluster reads its factory senders. That removes the guide's open question about Touring senders.
  - If you keep the Touring senders, or mix them, the reading is unreported. Check each side.
  - The reserve lamp is a cluster threshold (8 L on the coded M3 above), so it moves with sender accuracy.
- **(Inference) The filler pot doesn't move.** BMW fits the same pot and the same rigid filler pipe on both bodies, so the pot sits in the same place relative to the tank and inner structure. What differs is the M3 skin's drawn surround around it and the flap. Graft the M3 skin's surround so it meets your pot (M346's method). The 25–30 mm figure is the arch's outward shift (from HARD's flares), not the pot's.
- **(Inference) The leak-test plumbing doesn't move with the arch, but it sits in the graft zone.** Remove the separator, its vent hoses and the filler pipe before cutting. If you graft the donor's inner tub, carry over or keep bracket 41148196386 (it's common). Afterwards, prove it with the DM-TL test.
- **(Inference) The canister mount depends on the floor option in README "Choose the floor":**
  - Option 4 (keep the well): keep the Touring canister mount and covers 51718233265 and 51718233266.
  - Options 1 and 2 (M3 trunk floor): use the M3 holder 16132229735 and cover 51717893604 with the M3 vent and purge lines, as Renner's Touring did ("the EVAP system is from the M3… all the floor was… replace[d] to… integrate the M3 floor", [Larry Chen (2025), 22:40](https://www.youtube.com/watch?v=YM2gyQOaJCk&t=1360s)).
  - Option 3 (flat panel): give the canister a fixed mount and cover equivalent to one of these. No tested design exists.
  - In all cases, check the canister's clearance to the M3 muffler at full bump.

### Gaps
- Sender resistance curves for either car.
- Whether an M3 cluster's default `TANK_KENNLINIE` is the same value a US 325i cluster uses.
- BMW's E46 reserve figure in litres from an owner's manual (the search budget ran out). The NCS value of 8 L is the best available.

---

## 5. What builds did

| Build | Car | Fuel approach | Results and problems | Source |
|---|---|---|---|---|
| Tracks and Trails | 2004 325i Touring, automatic to manual (ex-Las Vegas, Ontario) | Broke a prong on the M3 tank, so put "brand new fuel pump… M3 fuel pump" into the Touring tank with a new gasket; new hose clamps; fitted the M3 filter and regulator only after a no-start | Fuel system pressurised ("when I went to change the fuel filter, it all dumped on me"); the no-start was the gearbox harness; no pressure figure | [rear end (2025), 26:20](https://www.youtube.com/watch?v=eMJLXbvzckE&t=1580s), [29:00](https://www.youtube.com/watch?v=eMJLXbvzckE&t=1740s); [first drive (2026), 1:14:00](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=4440s), [1:15:20](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=4520s) [captions] |
| Project BMW | 325i Touring (M54), US | Both in-tank units moved from the M3 into the Touring tank (tank lowered); M3 lines from the tank to the front; the 325's purge line didn't suit the S54 | Ran; no pressure figure | [Day 5 (2021), 00:20](https://www.youtube.com/watch?v=t9S0iXJj2GI&t=20s), [03:20](https://www.youtube.com/watch?v=t9S0iXJj2GI&t=200s) [captions] |
| Tenza Motorsports | 2004 325i Touring, M56 SULEV, US | M3 tank and pump in place of the sealed SULEV tank; M3 canister turned fore and aft on the wagon's mounting points; vent hoses remade; sender and pump wiring re-terminated from the M56's single plug | "does in fact work the car runs" ([10:40](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=640s)); broke both M3 tank vent nipples and fitted brass barbs ([GdCUQY-Xn-s, 06:40](https://www.youtube.com/watch?v=GdCUQY-Xn-s&t=400s)); "everything fit absolutely perfect the bolts are the same" ([15:00](https://www.youtube.com/watch?v=GdCUQY-Xn-s&t=900s)). A certified-emissions question on a SULEV car | [captions] |
| Renner (Miami), filmed by Larry Chen | Touring, US | "everything is M3 fuel pump lines fuel…" (tank, pump, lines, filter, regulator); M3 EVAP system; M3 floor; M3 underbody covers | Driven and shown; no figures | [18:40](https://www.youtube.com/watch?v=YM2gyQOaJCk&t=1120s), [21:00](https://www.youtube.com/watch?v=YM2gyQOaJCk&t=1260s), [22:40](https://www.youtube.com/watch?v=YM2gyQOaJCk&t=1360s) [captions] |
| ThaChileanDude | Touring, automatic to manual, US | M3 tank, pumps and lines | Running in about 10 days; no figures | [02:20](https://www.youtube.com/watch?v=iSgClonTiQg&t=140s), [17:00](https://www.youtube.com/watch?v=iSgClonTiQg&t=1020s) [captions] |
| puma1824, built by M3Projekts | US 2003 325iT | M3 fuel tank; "new fresh fuel lines" | No figures | [NAM3 #145–146](https://nam3forum.com/forums/forum/main-forum/member-build-journals/155763-e46-m3-touring-conversion-to-europe-and-back/page10) [page] |
| yavz | UK 318i Touring | M3 tank ("the pumps are different from normal e46's"); M3 fuel and brake lines | No figures | [PistonHeads, 26 Feb 2017](https://www.pistonheads.com/gassing/topic.asp?h=0&f=47&t=1655205&i=20), [24 Feb 2017](https://www.pistonheads.com/gassing/topic.asp?h=0&f=47&t=1655205) [page] |
| M346 Projects | Touring, SMG | Tank removal was "a pain" because of the EVAP hoses on top; one-time clamps replaced | The regulator leaked at first start (O-rings) and was replaced | [Pt 14 (2024), 21:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1300s); [Pt 13 (2024), 05:40](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=340s) [captions] |
| Calvin's Car Diary | UK 330d Touring, turbo S54 | Diesel tank replaced by a refurbished M3 tank, plus an aftermarket (Radium) system | Not a stock comparison | [PT15 (2025), 30:20](https://www.youtube.com/watch?v=WZaYROuG1jo&t=1820s) [captions] |
| Kalim | 2003 325i sedan (another car was MS43) | M3 pump(s), baffle, transfer pipe and left sender into the non-M tank; M3 lines, filter, regulator, O-rings and clamps | Lines "return lines are identical, but the high-pressure lines have different fittings" | [round 1] |
| 332 (NAM3) | 323i sedan, MS42 | Non-M pump with the M3 regulator; pump wiring untouched | "71 psi at the valve on the FPR"; ran | [NAM3 82513](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/82513-s54-swap-to-ms42-car-no-start) [page] |
| solspeeds | S54 wagon | "now we're going to check fuel pressure" | No value in the captions | [Part 4 (2023), 05:40](https://www.youtube.com/watch?v=xkRHbKlNzJU&t=340s) [captions] |

**Pattern.** Every Touring build used either the M3 tank or the M3 pump in the Touring tank, together with M3 lines. None kept a 325i pump. The one documented non-M-pump S54 car is a sedan with only a static reading.

---

## Guide-ready

### Parts table

Notes: "Common" means the same part number on the US 325i Touring M54 (2001–05; Feb 2003 = Mar 2003) and the US M3 (2003–06, coupe = convertible). Plan A (recommended) means the M3 in-tank set goes into your tank. Plan B means the donor's whole tank. Plan C means keeping your pump.

| Item | 325i Touring M54 (yours) | US M3 S54 (donor) | M56 (doesn't apply) | Plan A / B / C |
|---|---|---|---|---|
| Tank, plastic, with left sender | 16116766940 (originally 16111184899, or by ETK's date ranges 16116762962 from 03/2003; check the label) | 16112229736 | Metal with filler pipe 16116763569 | A, C: keep yours. B: donor's |
| Delivery unit (pump and right sender) | 16146766942 (original 16146752499) | 16142229684 | Sealed in tank, controller 16146912019 | A, B: M3. C: yours, if it passes the test |
| Left level sender | 16116768788 (original 16146755879) | 16142229683 | (in tank) | A, B: M3. C: yours |
| Sucking jet pump (transfer pipe) | 16146755880 | 16142282208 | — | A, B: M3. C: yours |
| Fuel baffle | none | 16112229656 | — | A, B: M3. C: optional |
| Flange seals, O-ring, lock rings, plug | 16111184084 ×2, 16141183543, 16116762417 ×2, 61138352390 | Common | — | New seals and O-ring |
| Straps, damper rubbers, grommets, spacers, bolts, nut | 16116756583 ×2, 16111184018 ×2, 16111182454 ×2, 16117194458 ×2, 07119905532 ×2, 07146760121 | Common | Different straps 16116757172 | Keep |
| Filler pipe, filler hose and clamps | 16117177490; 16117176011 (40×47×170); 07129952119 ×2 | Common | Integral to tank | Keep; new clamps |
| Filler pot, seal, cap pin | 51718208646; 16116755071; 16111184156 | Common | Common pot | Keep |
| Fill-in flap / hinge | 51178208246 / 51178151955 | 51172695524 / coupe 51172695527, convertible 51178151955 | — | Donor flap (and a coupe donor's hinge) |
| Flap actuator | 67116988090 to 03/2003; 67116987637 from 03/2003 | Same split | — | Keep yours |
| Tank vent pipe; vapour hose | 16117176511; 16116772292 | Common | — | Keep |
| Liquid-vapour separator ("expansion tank") and bracket | 16136752641; 41148196386 | Common | — | Keep; refit after the arch graft |
| Fuel pipes set (pump to floor lines) | 16117175998 (clamped) | 16112283288 (push-on and quick-connector) | — | A, B: M3. C: yours plus an adapter (undocumented) |
| Rear feed line | 16126752180 | 16122229409 | Single feed 16127513780 | M3 |
| Return line | 16126752186 | 16122229411 | none | M3 |
| Front feed line | 16126752183 | 16122229410 | — | M3 |
| Line clips and brackets | 16126761229 ×2, 16127195327 ×2, 34301164005, 16121179396, 16131184380 | Common; M3 adds tubing supports 16122282049, 16131177494 | — | Keep; add the M3 supports |
| Filter-regulator | 13327512019 (one piece, vent pipe 13327561060) | Filter 13327831089; housing 13537830368; copper ring 07119963129; regulator 13531404089; O-rings 13531720251, 13531720252; lock ring 13531736234 | — | M3 (new filter, O-rings, copper ring) |
| Filter bracket and cover | 13321435583; 13328230397 | Common; M3 adds sealing element 13327830949 | — | Keep; add the M3 sealing element |
| Regulator vacuum reference | Vent pipe 13327561060, hose 11727545323 | 11747797082 (blue), 64111368684 (white), 11727837591, metal sleeve 12517508831, tie 61131367599, clamps 61131365412 ×4 | — | M3 set |
| Engine feed pipe and rail joint | (M54 inlet hose 13537548987) | 13317831683 with O-ring 13641730767 | — | Comes with the S54; new O-ring |
| Purge valve and engine hoses | 13901433603, 13907557924, 13907558190 | 13907831770, 13907837661, 13907837663 | — | Comes with the S54 |
| Front purge line (floor) | 16111184135 | 16132229652 | 16127514320 | M3 |
| Rear purge line (canister) | 16136751175 | 16132229417 | 16136757559 | Keep yours with the Touring floor; M3's with the M3 floor |
| Canister | 16136751759 or 16136765440 (later 16136765271) | 16136751759 / 16131183906 | Metal 16126757177 | Keep yours |
| Leak-test pump (DM-TL), heated, 4-pin | 16137193479 | Common | Common | Keep |
| Dust filter | 16136751758 (06/2003-on 16136765272) | 16136751758 | 16136757522 | Keep |
| Canister vent pipes | 16137176508, 16131183895 | 16132283286, 16132229415 | — | Keep yours with the Touring floor; M3's with the M3 floor |
| Canister holder | none (plastic nuts 51711958025) | 16132229735, nuts 07147153450 ×4 | 16116757507 | M3 floor only |
| Canister underbody covers | 51718233265 (front), 51718233266 (bottom) | 51717893604 (front) | Common with the Touring | Match the floor option |
| Pump relay | K96 61368373700 | EKP 61357892976 | Controller 16146912019 | Keep K96 (see the manual) |

### Fit and test procedure, in order

Assumes the guide's phase order. The tank is drained and out by Phase 4. Phase 7 runs before the engine goes in.

**Phase 0, baseline (optional but useful):**
1. Confirm M54B25 and a plastic tank (guide).
2. With your engine still running, put the gauge on the M54 rail's threaded test fitting. BMW names adapter 13 5 220 for it, the same adapter as the S54 regulator fitting (ST055).
   - Pass: 3.5 ± 0.2 bar.
   - Pass: more than 3 bar after 20 minutes (Bentley [round 1]).
   - A pump that is weak at 3.5 bar won't pass at 5.

**Phase 1, donor:**

3. On the donor, with the filter cover off (8 mm socket and Phillips, per the bimmer pub), gauge the regulator's test fitting next to the filter.
   - Pass: 5.0 ± 0.2 bar with the relay or module bypassed.
   - Pass: 4.5 bar or more after 20 minutes (ST041, Bentley).
   - This proves the donor's pump, regulator and check valve before you move them.

**Phase 2, strip the donor.**

4. Label every line end (feed, return, purge) and photograph the clip positions. Take:
   - the in-tank set (delivery unit with plug, left sender, jet pump with transfer pipe, baffle), or the whole tank, with all hoses off before lowering it. Its vent nipples snap and aren't sold separately (Tenza).
   - pipe set 16112283288
   - lines 16122229409, 16122229410 and 16122229411
   - tubing supports 16122282049 and 16131177494
   - the filter cover's sealing element 13327830949
   - the regulator housing and regulator, as cores
   - the vacuum-hose set with its metal sleeve and clamps
   - front purge line 16132229652
   - flap 51172695524, and the hinge if the donor is a coupe
   - for an M3 floor graft: holder 16132229735 with its nuts, cover 51717893604, vent pipes 16132283286 and 16132229415, and rear purge line 16132229417

**Phases 4 to 6, strip and weld.**

5. Remove the filler pipe, the separator (16136752641) from the right rear wheel well, the canister and DM-TL, and the EVAP lines before any welding. Keep the separator bracket 41148196386; transfer it if the inner tub is replaced.
6. After the right-arch graft, check the filler parts:
   - Pass: the pot (51718208646) seats in the M3 skin's opening.
   - Pass: the flap closes flush and the actuator locks it.
   - Pass: the filler pipe and its 40×47×170 hose sit unstrained, with both L42-48 clamps on.
   - If not, rework before you seal the quarter.

**Phase 7, fuel (engine not yet in).** Start with the tank empty and log every litre you add; that log is your gauge-calibration reference later. Put in at least about 10 L before running the pump, since BMW says never to run it dry.

7. **In-tank (Plan A).**
   - Open both covers under the rear seat: the right one for the pump and sender, the left one for the sender and syphon jet (ST041).
   - Remove your delivery unit and left sender.
   - Fit the M3 baffle in the right half under the pump. Fit the M3 jet pump's transfer pipe into the baffle (Kalim). Then fit the M3 delivery unit and M3 left sender with new seals 16111184084 and O-ring 16141183543, and the lock rings 16116762417.
   - Pass: both plugs latched (housing 61138352390 on both cars); the floats move freely.
   - Plan B: fit the donor tank instead, with intact vent nipples.
8. **Pipe set and tank.**
   - Push the M3 pipe set's feed connector onto the pump and give it a pull test. Clamp the return hose to the tank's return nipple with a new L12-15 clamp.
   - Lift the tank on its straps, connect the vent pipe to the separator, and keep every hose free of the straps.
9. **Filter-regulator** on your bracket:
   - a new M3 filter, with its flow arrow toward the engine
   - the housing with a new copper ring 07119963129
   - the regulator with new O-rings 13531720251 and 13531720252 and lock ring 13531736234
   - Fit the cover with the M3 sealing element.
10. **Lines.**
    - Rear feed: the pipe set's quick-connector to the filter inlet.
    - Return: the housing to the pipe set's return hose.
    - Front feed: the housing outlet forward.
    - Front purge line.
    - Use your existing clip points and add the two M3 tubing supports.
    - Pass: every quick-connector clicks and passes a pull test; feed and return labelled; no line touches the exhaust, driveshaft or brake lines. With the engine out, cap the front feed line's engine end with a 5-bar-rated quick-connect plug, or put the gauge there.
11. **Vacuum hose.** Route it from the regulator nipple forward in its metal sleeve, with four clamps, along the feed line, away from the exhaust. Leave its engine end open or capped until the engine is in; either way the regulator reads its full 5-bar setpoint.
12. **Pump bypass.**
    - Pull K96 (behind the glovebox).
    - Fit a fused (15 A) switch across socket pin 6 (from F54, terminal 30) and pin 2 (to the pump, terminal 87). The pin functions are from the manual's WDS table; the terminal names are my mapping.
    - Battery only, no charger, for the 12 V tests.
13. **T1 Static pressure.** Gauge at the regulator test fitting (TP1), or dead-ended at the capped front feed line (TP2). Run 30 s.
    - Pass: 5.0 ± 0.2 bar (72.5 ± 2.9 psi) (BMW ST041; Bentley).
    - Low: regulator O-rings, filter, pump voltage (T4), pump.
    - High: return path restricted (a kinked return or pipe-set hose) or the regulator.
14. **T2 Hold.** Switch off and wait 20 minutes.
    - Pass: no more than 0.5 bar lost (BMW; DIS minimum 4.55 bar) and 4.5 bar or more (Bentley).
    - Fail: pinch the pipe set's rubber feed hose at the tank, then the return hose, with a hose clamp tool, to find out whether the pump's check valve or the regulator is leaking (BMW).
15. **T3 Delivery volume.** Our method; the TIS collection point wasn't found.
    - Disconnect the return line at the regulator housing and lead it with a fuel hose into a graduated container of 2 L or more, outdoors, with an extinguisher at hand.
    - Run 30 s on the battery, with the gauge on TP1 and the voltage noted at the pump connector.
    - Pass: 1.12 L or more (Bentley; the bimmer pub's 2.25 L/min), with TP1 holding about 5 bar during the run.
    - Our margin, not BMW's: the S54 at peak power uses an estimated 0.75–0.83 L of every 30 s, so keep a non-M pump only if it delivers well above the floor (we suggest 1.3 L or more). Otherwise fit the M3 unit (Plan A or B).
    - Reconnect the return with a new clamp.
16. **T4 Pump voltage.** With the pump running on the bypass:
    - Pass: the voltage at the pump connector (under the right rear seat) is within 0.5 V of the battery.
    - Pass: the ground-side drop is 0.5 V or less (Luke Murray).
    - Optional: current 9 A or less (BMW's passenger-car limit, per the bimmer pub).
    - This matters more with an M3 pump on the Touring's 1.5 mm² feed.
17. **T5 Leaks.** After T2, inspect the pump flange, the pipe-set joints, every quick-connector, the filter, the housing, the regulator lock ring and the return clamps.
    - Pass: dry.
    - Refit the filter cover.

**Phases 9 to 10, engine in.**

18. Connect the front feed line to the S54 feed pipe, with a new O-ring 13641730767 at the rail end.
19. Fit the vacuum hose to the idle-air distribution pipe's nipple.
20. Connect the front purge line to the S54 purge valve's hose (13907837663).
21. Confirm feed and return again.

**Phase 12, first start.** Leave the gauge on TP1 and tie it where you can read it.

22. **T6 Key-on.**
    - Pass: one prime, and 5.0 ± 0.2 bar.
    - Pass: K96 clicks (manual).
23. **T7 Vacuum reference at hot idle.**
    - Pass: with the hose on, pressure is below 5 bar (BMW's diagram shows 3.8 bar at part-throttle vacuum).
    - Pass: with the hose pulled, pressure returns to 5.0 ± 0.2 bar.
    - Pass: the hose is dry inside. Fuel in it means a leaking regulator diaphragm (our check).
24. **T8.** Fuel trims near zero (guide, `STATUS_LAMBDA_ADD_1` and `_2`).
25. **T9 Gauge.** Use your litre log, then refill from low.
    - Pass: `KOMBI46R` `STATUS_TANKINHALT_LESEN` left plus right equals the known contents.
    - Pass: cluster test 06 shows phase "1" (both sensors OK) (BMW ST052).
    - Pass: the reserve lamp comes on with about 8 L left (the coded threshold on an M3 cluster, per the NCS list).
26. **T10 EVAP.** After the arch, filler and canister work, and with the fuel between 15 and 85%:
    - Pass: `START_SYSTEMCHECK_DMTL` then `LESEN_SYSTEMCHECK_DMTL` gives a "…_DICHT" result.
    - Fail: `GROBLECK`, `FEINLECK` or `DECKEL_FEHLT`.
    - `STEUERN_TEV` should click the purge valve (our check).
    - Pass: no "Check Filler Cap" lamp after refuelling.
27. **Optional T11, on a dyno.** At wide-open throttle the manifold vacuum is about zero, so pressure should stay at 5.0 ± 0.2 bar. A droop under load means a supply shortfall (our inference from BMW's specification).

### Diagram-ready data

**Zones:** the front of the car is on the left; driver on the left (US).

| Zone | Where | What's there |
|---|---|---|
| Z1 | Under the rear seat | Saddle tank. Right half (passenger side): delivery unit (pump and right sender) under the right access cover, with the M3 baffle beneath it. Left half: left sender and jet pump under the left access cover. On top: the pump's feed outlet (right flange), the return nipple, two vent nipples, and the filler stub (right side) |
| Z2 | Right rear wheel well, behind the trim | Liquid-vapour separator 16136752641 on bracket 41148196386. The filler pipe runs up to the filler pot 51718208646 behind the flap (Touring flap 51178208246 before, M3 flap 51172695524 after), with the 03/2003-dependent flap actuator |
| Z3 | Under the right rear cargo floor | Canister with the DM-TL 16137193479 and its dust filter. Touring: fore and aft between the battery tray and the spare well, under covers 51718233265 and 51718233266. M3 floor: crosswise in holder 16132229735 under cover 51717893604. The M3 muffler sits behind (in the old well) |
| Z4 | Under the left front floor, beside the frame rail, under cover 13328230397 | Before: the 325i's one-piece filter-regulator 13327512019 (3.5 bar), with vent pipe 13327561060 to the engine bay. After: M3 filter 13327831089 (inlet at the rear), then housing 13537830368 with regulator 13531404089 (5.0 bar), the test fitting (TP1), the front-feed outlet and the return outlet, on bracket 13321435583 |
| Z5 | Engine bay, intake side | S54 feed pipe 13317831683 to the rail 13537830974 to six injectors 13647830975. Idle-air distribution pipe ("additional air line") with the regulator's vacuum nipple. Purge valve 13907831770 under the intake manifold, purging into the idle-air pipe |
| Z6 | Behind the glovebox | Relay K96 (socket X10156), fed from F54 (15 A). The pump feed runs to the pump connector under the right rear seat (1.5 mm² WS/BL on the Touring) |

**Lines and joints, after the swap:**

| ID | From → To | Part | Joint at the "from" end | Joint at the "to" end | Pressure |
|---|---|---|---|---|---|
| L1 | Pump outlet (Z1) → L2 | M3 pipe set 16112283288, feed hose | Moulded push-on (no clamp) | Quick-connector, female | 5 bar |
| L2 | L1 → filter inlet (Z4) | Rear feed 16122229409 | Angled male end into L1 | Quick-connector onto the filter's stub | 5 bar |
| — | Filter → housing (Z4) | Integral (housing on the filter's front end) | — | — | 5 bar |
| L3 | Housing outlet → S54 feed pipe (Z5) | Front feed 16122229410 | Quick-connector | Probably a quick-connector (inference); then O-ring 13641730767 at the rail | 5 bar |
| L4 | Housing return outlet → L5 | Return 16122229411 | Hose and clamp (inference from the clamp count) | — | about 0 bar |
| L5 | L4 → tank return nipple (Z1) | M3 pipe set, return hose | L12-15 clamp | L12-15 clamp | about 0 bar; feeds the jet pump, which moves fuel from the left half to the right |
| V1 | Regulator vacuum nipple → idle-air pipe nipple | 11747797082, 64111368684 in sleeve 12517508831, then 11727837591 | Push-on | Push-on | Manifold vacuum |
| P1 | Canister (Z3) → purge valve (Z5) | Rear purge 16136751175 (Touring floor) or 16132229417 (M3 floor), front purge 16132229652, then 13907837663 | Push-on | Quick-connector at the valve hose | Vacuum when purging |
| E1 | Tank vent nipples → separator (Z2) | 16117176511 and hoses | Clamps | Clamps | Vapour |
| E2 | Separator → canister (Z3) | Touring 16137176508 and 16131183895, or M3 16132283286 and 16132229415 | Clamps | Clamps | Vapour |
| E3 | Canister → DM-TL → dust filter → air | Integral or short hoses | — | — | Small pressure during the test (DM-TL) |
| F1 | Filler pot (Z2) → tank filler stub | Filler pipe 16117177490, then hose 16117176011 (40×47×170) | Pot seal 16116755071 | Two L42-48 clamps | Liquid |

**Before the swap (325i), for the left panel of Figure 7:** the Touring pipe set 16117175998 is clamped at both ends. The rear feed 16126752180, return 16126752186 and front feed 16126752183 are joined by short 8×13 mm hoses and clamps. The one-piece filter-regulator holds 3.5 bar, and its vent pipe runs to the engine bay; BMW says it goes to the crankcase separator on the M52TU, and an owner says the intake boot on the M54. The M54 rail has a threaded test fitting (later rails).

**Test points:**

| ID | Point | Use |
|---|---|---|
| TP1 | Threaded test fitting at the M3 regulator housing (Z4). Remove the filter cover. BMW adapter 13 5 220 | Pressure: T1, T2, T6, T7, T11 |
| TP2 | Capped end of the front feed line in the engine bay, before the engine is in | Alternative pressure point; needs a quick-connect gauge adapter |
| FS1 | Return line disconnected at the regulator housing, led to a graduated container | Delivery volume, T3 |
| RB | K96 socket pins 6 and 2, through a 15 A fused switch | Runs the pump |
| VD | Pump connector under the right rear seat, against the battery posts | Voltage drop, T4 |
| DI | Diagnosis socket | Tool32: `STATUS_DIGITAL`, `STEUERN_EKP`, `STATUS_TANKINHALT_LESEN`, the DM-TL jobs |

**Floor variants:** with the spare well kept (option 4), Z3 uses the Touring canister mounting and covers. With the M3 trunk floor (options 1 and 2), Z3 uses the M3 holder, cover and E2/P1 lines.

---

## The guide's statements that these findings correct

1. **README, Fuel system, "Lines" bullet:** "If you keep your pump, the M3 rear feed's quick-disconnect may not fit the non-M pump's barb outlet. Check it, or keep your rear feed line and adapt at the filter."
   - The rear feed line never reaches the pump on either car. A separate "fuel pipes set" joins the pump to the rear feed line: Touring 16117175998, clamped at both ends; M3 16112283288, with a push-on pump end and a quick-connector to the M3 rear feed line ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pipe_and_mounting_parts/), drawings [8de](https://ills.bmwfans.info/8de.png) and [1scw](https://ills.bmwfans.info/1scw.png)).
   - To keep your pump, either fit your own pipe set with an adapter to the M3 rear feed line, or keep your rear feed line and adapt at the M3 filter's quick-connect inlet. Neither is documented.
   - Simpler: fit the M3 delivery unit with the M3 pipe set.
2. **README, Fuel system, "Lines":** "The Touring's lines share part numbers with the sedan's, so the M3 lines should route the same way, but no Touring build has confirmed it."
   - Four Touring builds report fitting M3 fuel lines, with no routing problem: Project BMW, yavz on PistonHeads, ThaChileanDude, and Renner filmed by Larry Chen. A fifth (M3Projekts) shows new lines.
   - Both cars' ETK lists use the same clips and brackets; the M3 adds two tubing supports.
3. **README, Fuel parts row and JOB-CARDS 7a, Parts:** "M3 fuel lines: front feed 16122229410, rear feed 16122229409, return 16122229411" and "M3 lines 16122229410, 16122229409, 16122229411; M3 vacuum hoses; M3 pump 16142229684 and baffle 16112229656 if yours fails".
   - Add pipe set 16112283288, front purge line 16132229652, tubing supports 16122282049 and 16131177494, filter-cover sealing element 13327830949 and housing copper ring 07119963129.
   - List the vacuum set by number: 11747797082, 64111368684, 11727837591, sleeve 12517508831, tie 61131367599, clamps 61131365412 ×4.
   - With the M3 pump, also take the M3 jet pump 16142282208 and left sender 16142229683 (Kalim), plus new flange seals 16111184084 and O-ring 16141183543.
4. **README Phase 6, step 8:** "The M3 filler pot (51718208646, the same on both M3s) and the flap end up about 25–30 mm further outboard."
   - 51718208646 is also your US 325i Touring's filler pot, and the filler pipe, its seal, the cap pin, spring, boot, sleeve and actuator are common too ([ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/bodywork/side_panel_tail_trim/), [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/side_panel_tail_trim/)).
   - Only the flap (51172695524 against your 51178208246) and a coupe donor's hinge (51172695527) differ. A convertible donor's hinge, 51178151955, is your Touring's part.
   - The pot stays in place. Graft the M3 skin's filler surround around it (M346).
5. **README Phase 6, step 6:** "trial-fit the Touring's filler neck to the M3 filler pot… a neck that doesn't reach or seal will fail the EVAP leak test." The same claim appears in Phase 6's Done-when, "The neck reaches and seals in the M3 filler pot", and in WORKSHEETS ("the Touring's filler neck reaches the M3 filler pot").
   - Neck and pot are the same parts on both cars. Check instead that your pot seats in the M3 skin's opening, the flap closes and latches, and the filler pipe and its 40×47×170 hose sit unstrained. Then prove it with the DM-TL test.
6. **README Parts list, Body:** "With the flap moved outboard, check that your filler neck still reaches it and seals."
   - As item 5. Also note that the actuator (67116988090 to 03/2003, 67116987637 from 03/2003) stays with your car.
7. **README Fuel system, "Handling the tank":** "Early E46s have single-width tank strap brackets with one M8 nut, while later cars and M3s have double-width ones, which matters if you fit the M3 tank."
   - Redish ties the double-width bracket to the non-M convertible's V-brace pick-up, not to the tank ([Redish (2022), 08:00](https://www.youtube.com/watch?v=lf-52XqXSTk&t=480s)). ETK gives both tanks the same strap 16116756583, bolts 07119905532 and nut 07146760121.
   - A 2003 car has the later brackets anyway.
8. **README Fuel system, "Lines" bullet:** "Project BMW also found that the 325's purge-valve line wouldn't work with the S54, so check the EVAP purge line."
   - ETK gives the M3 its own front purge line, 16132229652 (Touring 16111184135), to the S54's own purge valve and hoses. Fit the donor's line.
   - Fit its rear line 16132229417 too if you fit the M3 floor's canister mount, or if the front line won't mate with your rear line 16136751175.
9. **README Phase 7, step 3; Card 7a; WORKSHEETS:** "put a gauge on the end of the front feed line in the engine bay" and "gauge on the end of the front feed line".
   - BMW's S54 test point is "a threaded fitting… at the fuel pressure regulator" with adapter 13 5 220 ([ST041 Part 2, p.46](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)). It's under the left front floor with the cover off. The rail has no port.
   - A gauge dead-ended on the front feed line works before the engine is in, but needs a quick-connect adapter.
   - For the bypass, name the pins: K96 socket pin 6 (F54 supply, terminal 30) to pin 2 (pump, terminal 87).
10. **README Phase 7 Done-when, Fuel system test table, WORKSHEETS:** "At least 1.12 L in 30 s at 12 V, collected as TIS 13 31 describes."
    - TIS 13 31's collection point wasn't found. BMW's training says only that volume must be tested, to check pump output and restrictions in the pump, lines and filter.
    - Say how to collect: return line off at the regulator housing, into a graduated container, so the pump is measured at 5 bar (our method). Note that 1.12 L is the floor for every E46 engine and leaves thin margin on an S54.
11. **README Fuel system and Figure 7 caption:** "The tank stays, and so does the pump if it passes the 5-bar test; plan on the M3's high-pressure lines, whose fittings differ from the Touring's."
    - Recommend moving the donor's in-tank set (or tank) with the M3 pipe set and lines; keeping the Touring pump becomes the fallback.
    - Figure 7 should show the pipe set, the quick-connector joints, TP1 at the regulator, the return-flow sample point, the vacuum hose to the idle-air pipe and the purge line (see the diagram data above).
12. **WIRING-AND-CODING.md, Fuel gauge and tank senders:** "…and the 325i wagon's 16.6 gal (62.8 L) ([Autopadre], unverified)…"
    - BMW USA's 2003 325 Sedan and Sport Wagon specifications give 16.6 US gal for all models ([BMW USA](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437)), and its 2002 M3 sheet also gives 16.6 gal ([BMW USA](https://www.press.bmwgroup.com/usa/article/attachment/T0022127EN_US/41385)). Replace the Autopadre citation.
13. **WIRING-AND-CODING.md, same section:** "A hobby site gives about 70 Ω empty to 310 Ω full on the left and 70 to 395 Ω on the right ([bmwgm5], unverified)."
    - The cited page lists only the X11175 pins (11/12 right, 15/16 left) and wire colours. It has no resistance values ([bmwgm5](https://www.bmwgm5.com/E46_Fuel_Level.htm), fetched 22 Oct 2026). Drop the values or find another source.
14. **WIRING-AND-CODING.md, same section:** "With the M3 pump unit in your tank, the senders are mixed, so check each side."
    - Move the M3 left sender (16142229683) with the pump, as Kalim did. Then the M3 cluster reads its own sender pair in a tank of the same 16.6 gal capacity. Still check each side with `STATUS_TANKINHALT_LESEN`.
15. **README Open questions (Fuel)**, all four now partly answered:
    - "Whether the M3 rear feed line's quick-disconnect mates with the Touring pump's outlet, and whether the M3 lines route unmodified under a Touring." The joint is the pipe set (item 1), and the lines route unmodified (item 2). Replace it with: "Whether the M3 pipe set fits the Touring pump's outlet; the quick-connector sizes."
    - "Whether the M3 tank and pump fit every model year of Touring: the builds that fitted them didn't compare part numbers." ETK shows identical mounting and interface parts for Jan 2001, Feb and Mar 2003, and May 2005 Tourings and for the 2003–06 M3. Builds on 2002–2004 Tourings confirm the fit.
    - "Where TIS 13 31 connects the fuel-pressure gauge and collects the flow sample on an S54." The gauge goes on the regulator's threaded fitting (BMW ST041). The collection point is still open.
    - "How accurately an M3 cluster's fuel gauge reads the Touring's tank senders…" This is moot if the M3 senders move with the pump; otherwise it's still open.
16. **README Fuel system, Pump and tank:** "So the donor's delivery unit fits your tank too."
    - It does. Add that BMW pairs it with the M3 jet pump and baffle (Kalim moved the transfer pipe into the baffle), and that ETK's shared flange seal and lock ring explain why the flanges fit.

---

## Other leads (outside this topic, for the pump-control and coding notes)

- **`STATUS_ADAPTIONSBLOCK_06` → `STAT_EKP_CFG_VERBAUT_WERT` ("which EKP was fitted")** is an MSS54 adaptation value ([SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)) [page]. Reading it on the donor (EKP fitted) and again in the Touring (relay) might show whether the US DME learns the pump hardware, which bears on the stored fault 1 (0x01). Untested.
- The MSS54 leak-test status `53_ABBRUCH_EKP_CRASH_OFF` (test aborted, pump crash cut-off active) ties the DM-TL logic to the crash cut-off (same SGBD) [page].
- The US M3 feeds its pump with 2.5 mm² (RT/WS); the Touring with 1.5 mm² (WS/BL) through K96 (manual's WDS tables). Check the voltage drop if an M3 pump runs on the relay.
