# Gap-fill: BMW data on fuel, cooling, A/C, fluids, DME and coding (researcher `bmw-powertrain`)

Research date: 22 October 2026. This file fills gaps left by `fuel_system_fit.md`, `cooling_ac.md` and `coding_powertrain_chassis.md` in this folder. It doesn't repeat what those files already prove; read them first.

**Routes used:** BMW US owner's manuals and BMW training PDFs on archive.org; the ETK on bmwfans.info (read with curl, because WebFetch can't resolve that host); the community SGBD export `emdzej/ediabasx-docs-sgbd`; eCFR's API; Cornell LII for 13 CCR 1968.1 and 1968.2; NHTSA's bulletin PDFs and its TSB index files; GitHub code search; vendor pages. **Web searches used: 15 of 30.**

**Labels:** **[read]** = I read the page, PDF or text layer myself this session. **[image]** = read from a picture. **[snippet]** = seen only in a search-result summary. **[notes]** = taken from the round-4 notes files named above, not re-read. **(inference)** = my reasoning or arithmetic, not a source.

**Hard limits kept:** no EWS-delete bytes, addresses or patch steps; nothing that removes or masks an emissions function or monitor; no odometer content; no refrigerant venting.

---

## Summary

| Gap | Status | The answer in one line | Best source |
|---|---|---|---|
| 1a. TIS 13 31 delivery test: where the fuel is collected, at what pressure, how much | **Still open** | No TIS text was reachable. BMW's own S54 training says only to put the gauge on the test point at the filter, refer to 13 31 if 5 bar isn't reached or more than 0.5 bar bleeds off, and test volume to check pump output and restrictions in the pump, lines and filter. 1.12 L in 30 s is still Bentley's figure | [BMW ST055 "MS S54", pp.41–42](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf) [read] |
| 1b. OEM flow (L/h at bar) and current for 16146766942 and 16142229684 | **Still open** | No OEM rating found. Vendors cross the Touring pump to VDO 228-222-009-002Z, whose listing gives no flow. The only current figure is still the magazine's "nine amps" | [spareto, VDO 228-222-009-002Z](https://spareto.com/products/vdo-fuel-feed-unit/228-222-009-002z) [read] |
| 2. TIS 17 00 S54 fill and bleed, test pressure, "self-bleeding" | **Still open** | TIS 17 00 and an E46 test pressure weren't reachable (newTIS is behind Cloudflare and the Wayback Machine was unreachable). No BMW source calls the S54 self-bleeding, and BMW fits it with a bleed screw | ETK via [notes] |
| 3a. A/C compressor make, oil grade, oil and refrigerant quantities | **Narrowed** (make and oil closed) | Both OE compressors (64526910458, 64526916232) cross to a **Denso 7SBU16C** with **ND-8** oil, **160 ml** in a new unit. No BMW gram figure for the charge: use the underhood label (MAHLE's E46 range is 715–765 g) | [spareto DCP05014](https://spareto.com/products/denso-compressor-air-conditioning/dcp05014), [DCP05039](https://spareto.com/products/denso-compressor-air-conditioning/dcp05039) [read] |
| 3b. Power-steering fluid and capacity | **Narrowed** | ETK gives the US M3 and the US 325i Touring the **same** reservoir (32416851217) and cap label (71246798132), and the label's own entry reads **"ATF"**. Capacity not found | [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/oil_carrier_single_parts/), [ETK label](https://bmwfans.info/parts-catalog/71246798132/) [read] |
| 3c. Brake fluid | **Closed** | **DOT 4** ("factory-approved brake fluids – DOT 4"); BMW says change it every two years | BMW US owner's manuals, MY2003 sedan and MY2002–05 M3 [read] |
| 3d. 420G gearbox oil | **Closed** | BMW's US M3 owner's manuals say **approx. 1.8 L (1.9 US qt)**; ST041's "1.9 L" is very likely the quart figure (inference). Fill to the fill plug | [MY2003 M3 manual, p.153](https://archive.org/details/manualzilla-id-7342203) [read] |
| 3e. S54 coolant | **Closed** | **9.3 L** confirmed (9.9 US qt in the MY2002 M3 manual, 9.8 US qt in MY2003). The 325i's own figure is 8.4 L | MY2002 and MY2003 M3 manuals [read] |
| 3f. E46 reserve fuel | **Closed** | **Approx. 8 L (2.1 US gal)** of the 63 L (16.6 gal) tank, in both the sedan/Sports Wagon and the M3 manuals | [MY2004 Sports Wagon manual](https://archive.org/details/manualsonline-id-5dc7d6b6-3cf5-4fe5-9e58-773e80bb0f50) [read] |
| 4a. MSS54 electric-fan switch points and stages | **Narrowed** | The fan duty is the larger of a coolant-temperature map and the A/C request (16 stages, 0–100 %). It runs at 60 % if IHKA data is lost and at least 60 % at an intake-air temperature of 60 °C or more, then road speed scales it down. The stock coolant switch points weren't found | [MSS54-XDFs wiki, "Aux Fan Speeds"](https://github.com/saildot4k/MSS54-XDFs/wiki/Aux-Fan-Speeds) [read, image]; BMW ST055 p.86 [read] |
| 4b. What IHKR needs before it allows the compressor (`STAT_KLIMABEREITSCHAFT_EIN`) | **Narrowed** | BMW's conditions: snowflake button with the blower at 1 or above, refrigerant pressure within limits, evaporator above its cycling point. IHKR then sends "AC stand-by", "KO request" and the load to the DME. The SGBD defines the bit only as "A/C readiness after compressor run-in" | [BMW ST040 IHKR, pp.4, 10, 13](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/2%20e46%20ihkr.pdf) [read]; [SGBD IHKR46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKR46.md) [read] |
| 5a. BMW VANOS test limits (ms, °KW) | **Still open** | No BMW-published limit found; the result fields in the SGBD carry no limits | — |
| 5b. Do `START_SYSTEMCHECK_*` jobs set readiness? | **Narrowed** | The SGBD calls them function checks whose result is read later; BMW's training says readiness bits set when the drive-cycle tests complete. Still no explicit BMW statement either way | [SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md); [BMW ST055 Emissions Overview, pp.21–22](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%202%29/07_Emissions%20Overview.pdf) [read] |
| 5c. Mode-09 VIN rule and the 2003 MSS54 | **Rule closed; car still open** | CARB requires the VIN over the OBD port from **MY2005** (13 CCR 1968.2(g)(4.8.1)). The MY1994–2003 rule, 1968.1, requires only the calibration ID and software verification. The federal 86.1806-05 has no VIN clause and accepted CARB compliance through MY2006. Whether a 2003 MSS54 answers mode 09 is untested | [13 CCR 1968.2](https://www.law.cornell.edu/regulations/california/13-CCR-1968.2), [1968.1](https://www.law.cornell.edu/regulations/california/13-CCR-1968.1), [eCFR](https://www.ecfr.gov/on/2024-06-03/title-40/section-86.1806-05) [read] |
| 6. Virginized-MSS54 sync success; INPA menu path | **Narrowed** | One vendor-hosted review reports a running S54 in a 2001 330i (EWS3) after RPM Motorsport "synced" a used DME to the car's EWS and key. No DIY virgin sync has been documented, and the INPA path for the MSS54's EWS functions is still undocumented | [RPM product page and reviews](https://rpmmotorsport.net/products/bmw-e39-e46-m3-m5-s54-s62-used-ecu-dme-ews-programming) [read] |
| 7. MK60 coding index of 34516765453; `touring_s`? | **Still open** | ETK lists hydro unit 34516765453 (production from Jun '03, superseding 34516759046) and control-unit kit 34526765455 "from Sep '01" for a Feb 2003 Touring. No published coding index; read `ID_COD_INDEX` on the car | [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/brakes/hydro_unit_dsc_fastening_sensors/), [SGBD DSC_MK60](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC_MK60.md) [read] |

---

## Gap 1. Fuel delivery test and pump ratings

### Cited findings

**BMW's own S54 test text (the closest thing to TIS that was reachable).** In BMW's "MS S54" training module [read] ([ST055 "8 MS S54", pp.41–42](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)):
- "The fuel pump should be tested for delivery pressure and volume. Caution when disconnecting fuel hoses because there is the possibility of residual fuel pressure! Install the fuel pressure gage at the pressure test point at the fuel filter."
- "Remove the fuel pump relay … and connect the Relay Bypass Switch to the relay socket. This will activate the fuel pump without running the engine. If the 5 bar fuel pressure is not achieved or bleed off is more than 0.5 bar, refer to 13 31 of the Repair instructions for further diagnosis."
- "Fuel volume must be tested to verify: 1. Fuel Pump Output 2. Restriction are not present in the pump, lines/hoses and fuel filter."
- The same module lists the Fuel Hose Clamp Tool as #13 3 010 and the Relay Bypass Switch as #61 3 050 (p.45).

BMW's later generic module repeats the same three lines without a number ([ST055 "04_Fuel Management"](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics/04_Fuel%20Management.pdf)) [read]. Its only flow-related statement is that an EKP-module system runs the pump at its "greatest delivery rate (100%)" if the control signals fail. No L/h figure appears in either module.

**No TIS or Bentley wording was reachable.**
- newTIS answered with a Cloudflare challenge (HTTP 403).
- web.archive.org reset every connection, so no archived copy could be read. The availability API answered, and reports **no snapshot** of the e46fanatics thread that quotes Bentley.
- Three web searches (English, German, and the "1.12 l" figure) found no copy of the TIS or Bentley procedure.

**Pump identity, but no rating.**
- Spareto lists Continental/VDO 228-222-009-002Z "Fuel Feed Unit" against BMW 16141184276, 16146752499 and **16146766942** [read] ([spareto](https://spareto.com/products/vdo-fuel-feed-unit/228-222-009-002z)). The page gives no flow or current data.
- A search snippet repeats the cross-reference: "OEM Part Number: 16146752499 … 16146766942 VDO Part Number: 228-222-009-002Z" [snippet] ([clickableautomotive](https://clickableautomotive.com.au/products/bmw-e46-fuel-pump-right-16146752499-16141184276-16146766942)).
- No search returned a VDO number or a rating for the M3 unit, 16142229684.
- The only "120 l/h at 3.5 bar" VDO listing that came up (228-222-008-013Z) is a Citroën/Peugeot part [read] ([winparts](https://www.winparts.co.uk/engine-parts-accessories/fuelsystem/fuel-pump/c721/fuel-feed-unit/p928271.html)), so it doesn't apply.

### Inferences
- **(inference)** BMW's stated purpose, checking for restrictions in "the pump, lines/hoses and fuel filter", means the sample is taken downstream of the filter. On the M3's combined filter-regulator, that's either the housing's return outlet or the open front feed.
  - Collecting at the return outlet measures the pump at the regulated 5 bar, which is the stricter test the fuel notes already chose.
  - An open front feed would measure near-zero-pressure flow and overstate the pump.
- **(inference)** BMW's training puts the gauge "at the fuel filter" (ST055) and "at the fuel pressure regulator" (ST041). On the M3 these are one housing, so the guide's TP1 is right.

### Still open
- TIS 13 31 and 16 14: the collection point, the pressure during the run, and BMW's own volume figure.
- OEM flow and current ratings for both pumps.
- **What would settle it:**
  - a dealer printout of the E46 M3 repair instruction for the fuel-pump delivery check, or a working ISTA or TIS install;
  - Continental's technical data for 228-222-009-002Z and for the M3 unit's VDO equivalent;
  - or the guide's own T3 and T4 measurements, logged on the car: litres in 30 s at about 5 bar, and the pump current.

### Guide impact (writer: **fuel**)

The fuel notes' item 10 already rewrites these lines. This adds BMW's S54 wording, so the guide stops implying TIS describes a method we've read.
- `README.md:813`: "| Fuel flow | At least 1.12 L in 30 s at 12 V, collected as TIS 13 31 describes ([Bentley, quoted on e46fanatics](…)) | …"
- `README.md:1408`: "| Delivery | At least 1.12 L in 30 s at 12 V, collected as TIS 13 31 describes | Bentley, quoted on [e46fanatics](…) |"
- `JOB-CARDS.md:444`: "| Fuel flow | At least 1.12 L in 30 s at 12 V, collected as TIS 13 31 describes | |"
- `WORKSHEETS.md:773`: "| Fuel delivery at 12 V (TIS 13 31) | At least 1.12 L in 30 s | |"
- `README.md:931`: "4. Fit the fuel-pressure gauge at the fuel-pressure fitting that TIS 13 31 shows ([BMW ST041, part 2](…))."
- `README.md:2407` (Open questions): "- Where TIS 13 31 connects the fuel-pressure gauge and collects the flow sample on an S54."

**Proposed text** (Done-when and test tables):

> | Fuel flow | At least 1.12 L in 30 s on the battery with the pump bridged, collected at the filter-regulator housing's return outlet while the gauge holds about 5 bar (our method: BMW says only that volume must be tested "to verify fuel pump output" and that "restriction are not present in the pump, lines/hoses and fuel filter" ([BMW ST055, MS S54, p.42](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)); the 1.12 L figure is Bentley's, quoted on [e46fanatics](https://www.e46fanatics.com/threads/fuel-pressure-info.1116777/)) | Replace the pump: a Touring pump, or the M3 pump and baffle |

**Replacement for README Phase 7 step 4:**

> 4. Fit the fuel-pressure gauge to the threaded test fitting on the M3 filter-regulator housing under the left front floor. BMW puts "the fuel pressure gage at the pressure test point at the fuel filter" and refers to 13 31 if 5 bar isn't reached or more than 0.5 bar bleeds off ([BMW ST055, MS S54, p.41](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf); [BMW ST041, part 2, p.46](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)).

**Open-question replacement:**

> - TIS 13 31's own delivery-volume method and figure for the S54 (the collection point and the pressure during the run). BMW's training gives the purpose but no number; until a TIS printout turns up, use the return-outlet method at about 5 bar. Also open: an OEM flow and current rating for the Touring pump (Continental/VDO 228-222-009-002Z per [spareto](https://spareto.com/products/vdo-fuel-feed-unit/228-222-009-002z)) and for the M3 pump 16142229684. Your T3 and T4 readings are the practical answer.

---

## Gap 2. Coolant fill and bleed, test pressure, "self-bleeding"

### Cited findings
- **No BMW S54 bleed text was reachable.**
  - BMW's newer cooling module covers N-series and electric-pump engines only ([ST055 "09_Cooling Systems"](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics/09_Cooling%20Systems.pdf)) [read].
  - ST041's "M3 DriveLine" describes the coolant flow and the "Coolant Reservoir (2 bar system)" but has no venting or filling text [read].
  - newTIS: Cloudflare 403. Wayback: unreachable.
  - One forum search found no S54 bleed procedure from TIS.
- **Test pressure.** One search for a TIS "test pressure" found only an E53 forum suggestion of "around 20 psi", with no BMW figure [snippet] ([xoutpost](https://xoutpost.com/bmw-sav-forums/x5-e53-forum/108408-pressure-testing-cooling-system-e53.html)). Not usable.
- **Hardware that bears on "self-bleeding":** the S54 has vent screw 17111712788 (2.5 Nm) in water hose 11537830716 [notes: `cooling_ac.md` Q1, from ETK and Flow p.60]. The expansion-tank group also lists a 500 mm hose, 17222246036, which the cooling notes route from the radiator top to the tank. That routing is the notes' own reading of the ETK names and the ST041 drawing, not a labelled BMW hose diagram [notes: `cooling_ac.md` D1].

### Inferences
- **(inference)** BMW fitted a dedicated vent screw on the S54's radiator-feed hose and printed a torque for it. That points to a manual bleed being part of BMW's procedure, so the NAM3 claim that "the cooling system on ours is self-bleeding" should be treated as one owner's opinion.
- **(inference)** If that hose does run from the radiator top to the tank, it would purge small amounts of air while driving, which may be what that owner meant. It doesn't remove the need for the screw after a dry fill.

### Still open
- TIS 17 00 S54 fill and bleed text, and BMW's E46 cooling-system test pressure.
- **What would settle it:**
  - a dealer printout of "Bleeding cooling system (S54)" and "Checking cooling system for leaks" for the E46 M3;
  - or ISTA's service-function text.
- Until then, the cooling notes' procedure P4 and P3 stand: test at the 2.0 bar cap rating, hold 15 minutes, and test the cap.

### Guide impact (writer: **cool**)
- `README.md:1419`: "- **Coolant and bleeding.** Coolant type and mix are in [Fluids and capacities]…; take the capacity from TIS, because we couldn't source it. … BMW's bleeding procedure is in TIS group 17 00; we couldn't read it. Owners of other BMW sixes park nose up…"
- `README.md:2418` (Open questions): "- The S54's coolant capacity, and BMW's S54 cooling-system bleed procedure (TIS 17 00)."

**Proposed addition** (after the cooling notes' replacement, so the claim isn't lost):

> Some owners call the S54's cooling system "self-bleeding" ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/14592-deleting-auxiliary-water-pump)). BMW nonetheless fits a bleed screw (17111712788, 2.5 Nm) in the radiator-feed hose 11537830716, so bleed it after any drain (Flow p.60; ETK). TIS 17 00's own text and BMW's E46 test pressure are still unread; test at the cap's 2.0 bar rating.

**Open-question replacement:**

> - BMW's S54 fill-and-bleed text (TIS 17 00) and BMW's E46 cooling-system test pressure. The capacity is settled at 9.3 L.

---

## Gap 3. Operating fluids

### Cited findings

**Reserve fuel, tank, brake fluid: BMW US owner's manuals [read]**
- **MY2004 US 325i/325xi Sports Wagon manual** (Part-No. 01 41 0 157 605, © 09/03; it has "Tailgate" and "Cargo area" chapters and a rear-window washer reservoir) ([archive.org](https://archive.org/details/manualsonline-id-5dc7d6b6-3cf5-4fe5-9e58-773e80bb0f50)):
  - "Approx. 16.6 gal./63 liters, of which approx. 2.1 gal./8 liters are reserve".
  - Capacities table (p.163): "Fuel tank approx. 16.6/63; Reserve approx. 2.1/8".
  - "factory-approved brake fluids – DOT 4".
- **MY2003 US sedan manual** (320i–330xi; Part-No. 01 41 0 156 804, © 09/02) ([archive.org](https://archive.org/details/manualzilla-id-7292334)):
  - The same tank and reserve wording.
  - "Once the indicator lamp stays on continuously, there are still approx. 2 gallons/8 liters of fuel in the fuel tank".
  - Capacities (p.155): "Cooling system including heater circuit approx. 8.9/8.4" (the M54).
  - "Manual and automatic transmission, transfer box and differential: Lifetime lubricant, no oil change required".
  - Brake fluid: "Your BMW center is familiar with the specifications for factory-approved brake fluids – DOT 4", and change it "every two years".
- **US M3 manuals** give the same 16.6 gal/63 L and "approx. 2.1/8" reserve, and "DOT 4":
  - MY2002, Part No. 01 41 0 156 249 ([archive.org](https://archive.org/details/manualzilla-id-7335091));
  - MY2003 convertible, 01 41 0 156 854 ([archive.org](https://archive.org/details/manualzilla-id-7342203));
  - MY2004 convertible, 01 41 0 157 596 ([archive.org](https://archive.org/details/manualzz-id-1189475));
  - MY2005, 01 41 0 158 512 ([archive.org](https://archive.org/details/manualzilla-id-7299992)).

**420G gearbox oil [read]**
- US M3 manuals: "Manual transmission quarts (liters) approx. 1.9 (approx. 1.8) — Oil change during running-in check and during each inspection II" (MY2002, p.147).
- MY2003 convertible: "approx. 1.9/1.8" (p.153). MY2004 convertible and MY2005 M3: the same.
- The differential is "approx. 1.2 (approx. 1.1)" in all of them.
- BMW's M3 training table instead prints the gearbox "Oil Capacity 1.9 L" (E36 M3 column 1.2 L) and the differential "Oil Change Capacity 1.1 L" ([ST041 "M3 Complete Vehicle", technical data](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf)).
- ETK's US M3 "Transmission oil" group lists MTF LT-2 83220309031 with "All E46 (start 12/97) only lifetime oil" [read] ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/workshop_consumables/transmission_oil/)).

**Coolant [read]:** the MY2002 M3 manual gives "Cooling system including heater circuit quarts (liters) approx. 9.9 (approx. 9.3)" and the MY2003 convertible "approx. 9.8/9.3", which confirms the cooling notes. The MY2004–05 M3 tables omit the line.

**A/C compressor and oil [read]:** spareto's Denso listings (vendor data):
- **DCP05014** "for OE number 64526910458": Compressor ID **7SBU16C**, Compressor Oil **ND-8**, Oil Fill Quantity **160 ml**, magnetic clutch, **5 grooves**, pulley Ø110 mm, R 134a ([spareto](https://spareto.com/products/denso-compressor-air-conditioning/dcp05014)).
- **DCP05039** "for OE number 64526916232": **7SBU16C**, **ND-8**, **160 ml**, magnetic clutch, **4 grooves**, pulley Ø110 mm, R 134a ([spareto](https://spareto.com/products/denso-compressor-air-conditioning/dcp05039)).
- The leebmann24 versions were Cloudflare-blocked. A search snippet of them says "160 ml of PAG 46 oil" [snippet].
- BMW's E46 training confirms a variable-displacement swash-plate compressor: "The system uses the variable displacement compressor" ([ST034 "Climate Control", p.7](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/8%20Climate%20Control.pdf)) [read]. BMW's refrigerant module calls PAG "only to be used for refrigerant circuits with R134a" ([ST054 "02_Refrigerant"](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control/02_Refrigerant.pdf)) [read].
- **Charge:** the only BMW-specific search returned low-quality pages [snippet], so none is cited. MAHLE's 715–765 g E46 range stays the best published figure [notes].

**Power steering [read]:**
- In the current ETK, both the US M3 and the Feb 2003 US 325i Touring "Oil carrier / Single parts" groups list the **same** parts ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/oil_carrier_single_parts/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/steering/oil_carrier_single_parts/)):
  - oil carrier 32416851217 and cover 32416851332, each "Only in conjunction with Label, oil container-power steering pump 71246798132";
  - gasket ring 32411128333, bracket 32411092940.
- The label's own catalog entry reads **"ATF"** (older number 71242122171) ([ETK](https://bmwfans.info/parts-catalog/71246798132/)).
- The reservoir's own entry reads **"CHF 11.S"** (older number 32411097164) ([ETK](https://bmwfans.info/parts-catalog/32416851217/)).
- None of BMW's E46 training texts read this session names the fluid. ST041 gives only the pump's 120 bar and 11 L/min and the 15.4:1 ratio. The owner's manuals say only that additives aren't needed in "the power steering system".

### Inferences
- **(inference)** The 420G figure is **1.8 L**. Four editions of BMW's US M3 manual print "approx. 1.9 US qt / approx. 1.8 L", and ST041's "1.9 L" matches the quart number. Either way, you fill to the fill plug, and 2 L of MTF-LT-2 covers it.
- **(inference)** The current replacement reservoir is a CHF 11S part that BMW supplies "only in conjunction with" an ATF label for these cars. That reads as BMW marking E46 systems as ATF systems. Both cars carry the same parts, so the swap doesn't change the fluid. Still confirm the donor's cap, and don't mix ATF with CHF 11S.
- **(inference)** BMW quotes the A/C oil for a new compressor (Denso: 160 ml) separately from MAHLE's 150 ml system total. So the cooling notes' rule stands: refill a reused or new compressor to the drained amount plus 10 g, per BMW's ST054.
- **(inference, side note for the cool writer)** Denso lists **4 pulley grooves** for 64526916232, which ETK gives the US M3 from Sep '02, yet ETK lists only the 5PK × 829 belt for the M3. Check the donor's pulley and belt before ordering a belt.

### Still open
- BMW's own refrigerant charge in grams for the US M3 and 325i Touring. The underhood label settles it.
- BMW's power-steering capacity. Fill to the reservoir mark.

### Guide impact

Writers: **cool** (coolant, A/C), **front** (brake fluid, power steering), **fuel** (reserve). The gearbox goes to whichever writer owns the Fluids-and-capacities table (driveline).
- `README.md:2267`: "| Getrag 420G gearbox | Genuine BMW MTF-LT-2, 75W-80 GL-4 (83220309031) | 1.9 L (2.0 US qt); check the label on the gearbox | Fluid: [BimmerWorld]; capacity: BMW ST041 technical data |". The same line is at `JOB-CARDS.md:668` and `WORKSHEETS.md:537`, and `README.md:1263` reads "- **Oil:** BMW MTF-LT-2 (75W-80 GL-4), 1.9 L …"
  > | Getrag 420G gearbox | Genuine BMW MTF-LT-2, 75W-80 GL-4 (83220309031) | Approx. 1.8 L (1.9 US qt); fill to the fill plug with the car level ([BMW US M3 owner's manual, MY2003, p.153](https://archive.org/details/manualzilla-id-7342203); BMW's [ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf) prints 1.9 L). Buy 2 L | Fluid: [BimmerWorld](https://www.bimmerworld.com/Genuine-BMW-MTF-LT-2-GL-4-Transmission-Fluid-1-liter.html) |
- `README.md:2269`: "| Power steering | **Not found.** Read the cap on the donor's M3 reservoir (ATF or CHF 11S) and don't mix the two; BimmerWorld lists CHF 11S for no E46 | Not found | …". The same wording is at `JOB-CARDS.md:823` and `WORKSHEETS.md:541`; see also `README.md:1372`.
  > | Power steering | ATF, as marked on the reservoir: BMW's catalog gives the US M3 and the US 325i Touring the same reservoir (32416851217) and cap label 71246798132, whose entry reads "ATF" ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/steering/oil_carrier_single_parts/), [ETK label](https://bmwfans.info/parts-catalog/71246798132/)). Confirm on the donor's cap; don't mix with CHF 11S | Not found: fill to the reservoir mark | ETK |
- `README.md:2271`: "| Brake and clutch fluid | **Not found.** Check the reservoir cap and TIS | Allow about 1.5 L …". The same line is at `JOB-CARDS.md:600`.
  > | Brake and clutch fluid | DOT 4, BMW's "factory-approved brake fluids – DOT 4"; change every two years ([BMW US owner's manual, MY2004 Sports Wagon](https://archive.org/details/manualsonline-id-5dc7d6b6-3cf5-4fe5-9e58-773e80bb0f50); the M3 manuals say the same) | Allow about 1.5 L (1.6 US qt) … (unchanged) | … |
- `README.md:2270`: "| Coolant | … | **Capacity not found** | …". Use the cooling notes' replacement (9.3 L). This file adds only the citation of the MY2002 M3 manual's "approx. 9.9 (approx. 9.3)" ([archive.org](https://archive.org/details/manualzilla-id-7335091)).
- `README.md:2272`: "| A/C refrigerant | Per the underhood label | **Charge not found;** charge by weight from the label | — |"
  > | A/C refrigerant and oil | R134a by weight to the underhood label (MAHLE lists 715–765 g for E46 petrol engines including the S54). Both OE compressors are Denso 7SBU16C units filled with Denso ND-8 PAG oil, 160 ml in a new compressor ([spareto, DCP05014](https://spareto.com/products/denso-compressor-air-conditioning/dcp05014), [DCP05039](https://spareto.com/products/denso-compressor-air-conditioning/dcp05039)) | Label; oil per the cooling notes' procedure | … |
- `README.md:2273`: "| Fuel | Premium unleaded | Your Touring's tank | …"
  > | Fuel | Premium unleaded | 63 L (16.6 US gal), of which about 8 L (2.1 gal) is reserve: the lamp stays on with about 8 L left ([BMW US owner's manual, MY2004 Sports Wagon](https://archive.org/details/manualsonline-id-5dc7d6b6-3cf5-4fe5-9e58-773e80bb0f50)) | … |
- `README.md:2428` (Open questions): "- The power-steering fluid for the M3 rack (the reservoir's ATF label against CHF 11S), and the brake-fluid specification." Replace with:
  > - BMW's power-steering capacity (the fluid is ATF per the catalog label; brake fluid is DOT 4).
- `README.md:2419`: "- The A/C refrigerant charge (read it from the underhood label)." Keep it, and add "BMW's gram figure; MAHLE gives 715–765 g."

---

## Gap 4. Fans and A/C enable

### Cited findings

**BMW, MSS54 fan inputs [read]:** "The fan is activated based on the ECM calculation of: Coolant outlet temperature (monitored by the Radiator Outlet Temperature Sensor); Calculated (by the ECM) catalyst temperature; Vehicle speed; Battery voltage; Air Conditioning pressure (calculated by IHKA and sent via the K-Bus to the ECM)". The fan is driven "by a pulse width modulated signal from the ECM" through a power stage on the fan housing, fed from a 50 A fuse ([ST055 "8 MS S54", p.86](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)). Catalyst temperature as an input is new against the cooling notes.

**Community reverse-engineering of the MSS5x fan logic [read]** ("Courtesy of Terraphantm", on the [MSS54-XDFs wiki, "Aux Fan Speeds"](https://github.com/saildot4k/MSS54-XDFs/wiki/Aux-Fan-Speeds)). Not BMW documentation:
- `KL_ELU_TKA`: radiator-outlet temperature (°C) → fan duty. "If the radiator outlet temperature is bad, the DME takes the value from the block sensor, subtracts 10."
- The A/C request: "If the compressor is off or the intake air temperature is less than 10 ºC, it assumes 0. If there's an error on the IHKA side, the DME assumes 60%. Otherwise the IHKA will send a message … requesting 1 of 16 speeds", looked up in `K_ELU_KKOS[1..16of16]`.
- "The two registers are compared, and the DME picks the larger number."
- "If [intake air] is 60 ºC or higher, the requested speed will be set 60% unless the previously calculated value is higher."
- A road-speed factor (`KL_ELU_V`) then multiplies the result. On the M5 it is 1.0 up to 120 km/h and 0 by 150 km/h; that's the MSS52, quoted as the example.
- The wiki's screenshot, from a Z3 M (S54) bin edited for an E30 swap [image] ([PNG](https://github.com/saildot4k/MSS54-XDFs/blob/master/Engine%20Swap%20XDFs/PWM%20FAN%20WIRING/Fan%20Values%20w%20AC%20Z3M.png)):
  - the A/C stage table, 1–16 of 16 = 0, 30, 36, 42, 48, 53, 58, 63, 68, 73, 78, 83, 88, 93, 98, 100 %. These windows carry no edit marker, while the coolant and speed tables do, so I read them as stock (my reading of the picture);
  - `K_ELU_KKOS_ERSATZ` (substitute when IHKA data is missing) = 60 %, which the wiki calls "the 60% default";
  - the coolant map shown (39 °C → 0 % … 90 °C → 100 %) carries the edit marker and red cells, so it isn't stock.

**IHKR compressor conditions, BMW [read]** ([ST040 "E46 IHKR"](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/2%20e46%20ihkr.pdf)):
- K-bus signals include "Vehicle speed, Engine speed, Coolant temperature, Outside temperature, Terminal 15 …, Compressor load, … Compressor request" (p.4).
- "The air conditioning system is switched on by pressing the snow flake button and having the blower dial on position 1 or greater. The LED in the button signals that the A/C is in stand-by" (p.10).
- IHKR sends "IHKR on stand-by (signal AC), Request for A/C activation (signal KO), Calculated compressor load, Request for auxiliary fan".
- "Pressure values that are too high or too low will cause the compressor to be switched off. Once all of the criteria for compressor operation have been met, the DME control module will activate the compressor relay."
- "The IHKR cycles the compressor at 1 °C if the outside temperature … is above 68 °F … 3 °C if … below 68 °F" (p.10).
- DIS service function "Deactivate transport-lock function" (p.13).

**SGBD [read]:**
- IHKR46 `STATUS_IO` → `STAT_KLIMABEREITSCHAFT_EIN`, "Klimabereitschaft nach Kompressoreinlauf" (A/C readiness after compressor run-in).
- `KOMPRESSOR_SPERRE`, "Codieren der Kompressortransportsperre" (argument 'EIN'/'AUS'); `CODIERUNG_LESEN` → `KOMPRESSOR_SPERRE` "Klimakompressor deaktiviert".
- No job defines what the run-in is ([IHKR46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKR46.md)). IHKA46 has the same transport-lock coding ([IHKA46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKA46.md)).

### Inferences
- **(inference)** BMW's E46 pressure → stage table (8 bar = stage 0 … above 24 bar = stage 15, below 50 mph; in `cooling_ac.md`) maps onto the DME's 16-entry table. With the Z3 M values that appear stock, stage 1 (9 bar) is about 30 % duty and stage 15 is 100 %. These are Z3 M (MSS54) values; the E46 M3's own bin may differ.
- **(inference)** `STAT_KLIMABEREITSCHAFT_EIN` probably reads 1 once the transport lock is off and the IHKR has done its post-lock compressor run-in. If the compressor never engages:
  1. Read `CODIERUNG_LESEN` → `KOMPRESSOR_SPERRE`.
  2. Then `STATUS_IO` → `STAT_KLIMABEREITSCHAFT_EIN`.
  3. Then the DME's `STAT_AC_EIN`/`STAT_KO_EIN`.

### Still open
- The stock E46 M3 `KL_ELU_TKA` switch points and the `KL_ELU_V` road-speed factor. **What would settle it:** open the donor DME's own read file (the vendor makes one for the EWS work) in TunerPro with the MSS54 XDF, read-only, and note the two tables. Or log `STATUS_KUEHLW_AUSL_TEMPERATUR` against the fan output at hot idle.
- BMW's definition of the IHKR "compressor run-in" readiness.

### Guide impact (writers: **cool** for the fan; **coding-body** for IHKR)
- `WIRING-AND-CODING.md:618`: "- **Fan.** The electric fan's speed rises with A/C pressure at low road speed; test it with `STEUERN_E_LUEFTER` (BMW ST054)."
  > - **Fan.** The DME drives the electric fan by PWM from the radiator-outlet temperature, its calculated catalyst temperature, road speed, battery voltage and the A/C pressure the climate control reports ([BMW ST055, MS S54, p.86](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)). Community reverse-engineering adds the following ([MSS54-XDFs wiki](https://github.com/saildot4k/MSS54-XDFs/wiki/Aux-Fan-Speeds), not BMW): the DME takes the larger of a coolant-temperature request and the A/C request (16 stages, 0–100 %); it runs the fan at 60 % if the climate control's data is missing, and at 60 % or more once intake air reaches 60 °C; and it scales the result down with road speed. So a fan running at a steady 60 % with the A/C on suggests the cluster isn't passing the climate-control data. Test with `STEUERN_E_LUEFTER`.
- `WIRING-AND-CODING.md:616` (IHKR bullet). Add after "…by BMW's description it should work":
  > BMW's conditions are the snowflake button with the blower at 1 or above, refrigerant pressure within limits and the evaporator above its cycling point (1 °C above 68 °F outside, 3 °C below) ([BMW ST040 IHKR, p.10](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/2%20e46%20ihkr.pdf)). If it still won't engage, read the IHKR's `CODIERUNG_LESEN` → `KOMPRESSOR_SPERRE` (the transport lock) and `STATUS_IO` → `STAT_KLIMABEREITSCHAFT_EIN`, "A/C readiness after compressor run-in" ([SGBD IHKR46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKR46.md)).

---

## Gap 5. VANOS limits, readiness, mode 09

### Cited findings

**VANOS:**
- The SGBD result fields for `STEUERN_EVANOS1_VERSTELLZEIT` (`EVAN_VERSTELLZEIT_FRUEH`/`_SPAET` with units) and `STEUERN_EVANOS1_DICHTHEIT` (`EVAN_ISTWERT`, `EVAN_SOLLWERT`, `EVAN_STATUS`) carry no limits or comments [read] ([SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).
- BMW's S54 and VANOS training modules read this session give no test limits [read].
- One German search found no BMW figure.

**System checks and readiness:**
- The SGBD describes `START_SYSTEMCHECK_SEK_LUFT`, `START_SYSTEMCHECK_DMTL` and `START_SYSTEMCHECK_TANK_LECK` as "Funktionsueberpruefung … anstossen – erwarte Ergebnis ausserhalb Job" (start a function check; expect the result outside the job). The `LESEN_…` jobs then return a status value and text [read].
- BMW's emissions training [read] ([ST055 "07_Emissions Overview", pp.21–22](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%202%29/07_Emissions%20Overview.pdf)):
  - "The readiness code provides status (Yes/No) of the system having completed all the required monitoring functions or not";
  - "Drive the car in such a manner that all tests listed above can be completed (refer to the drive cycle)";
  - DIS shows the readiness code under "Service Functions → Drive → Digital Motor Electronics → Diagnostic Function" (MS43 example).
- NHTSA's TSB index records two BMW bulletins where DME software affected monitors [read: index summaries only; PDFs not located]:
  - **SI 12 15 99**, voluntary emissions recall 00E-A01 (E46 1999–2000): a DME software error "may prevent communication … with an off-board scan tool … and/or the oxygen sensor readiness code may not set" ([TSB index 2000–2004, record 616159](https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS_RECEIVED_2000-2004.zip)).
  - **SI B12 22 08** (2009), US M3 2001–2005: "As originally installed, the DME programming may cause the OBD diagnostic to erroneously evaluate the efficiency of the catalytic converters" ([TSB index 2005–2009, record 10029304](https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS_RECEIVED_2005-2009.zip)).

**Mode-09 VIN, the rules [read]:**
- **13 CCR 1968.2(g)(4.8.1)**, current text: "All 2005 and subsequent model year vehicles shall have the vehicle identification number (VIN) available in a standardized format through the standardized data link connector in accordance with SAE J1979 … Only one electronic control unit per vehicle shall report the VIN to an SAE J1978 scan tool" ([LII](https://www.law.cornell.edu/regulations/california/13-CCR-1968.2)).
- **13 CCR 1968.1** (the 1994-and-later rule, last amended 1999), which covers a MY2003 car ([LII](https://www.law.cornell.edu/regulations/california/13-CCR-1968.1)):
  - **no VIN clause**;
  - "the software calibration identification number shall be made available through the serial port" (phased in 2000–2002, full by MY2002);
  - software-integrity verification (CVN) on the same phase-in.
- **40 CFR 86.1806-05**, versions of 2017–2024, removed 17 June 2024 (read through the [eCFR API](https://www.ecfr.gov/api/versioner/v1/full/2024-06-03/title-40.xml?part=86&section=86.1806-05); [human page](https://www.ecfr.gov/on/2024-06-03/title-40/section-86.1806-05)):
  - no VIN clause;
  - "(h)(2)(i) Basic diagnostic data (as specified in §§ 86.094-17(e) and (f)) shall be provided in the format and units in SAE J1979";
  - "(j)(1) Through the 2006 model year, demonstration of compliance with California OBDII requirements (… 13 CCR 1968.2) … shall satisfy the requirements of this section".
- **BMW SI B12 09 13** (Nov 2013), re-read: models "E46 … Produced to 12/2006". The state tester "may read out WBAAA00000A123456" when the DME holds only seven VIN digits. It names no DME family [read] ([NHTSA PDF](https://static.nhtsa.gov/odi/tsbs/2013/MC-10150160-9999.pdf)).

### Inferences
- **(inference)** No regulation obliged a MY2003 car to report its VIN over mode 09. CARB's requirement starts at MY2005, and the federal section defers to CARB through MY2006. So the guide shouldn't promise that a 2003 MSS54 answers. A 2004–06 MSS54HP probably does, at least on MY2005–06 cars.
- **(inference)** SI B12 09 13 shows that E46 DMEs which store a full VIN report it. Whether the MSS54's OBD stack does is unproven.
- **(inference)** Nothing found says a service function sets readiness. BMW's own training ties readiness to completing the drive cycle, and the SGBD describes the jobs only as function checks, so keep driving the monitors to completion.
- **(inference)** SI B12 22 08 means an un-updated 2001–05 M3 DME has a known catalyst-monitor calibration fault. Ask the DME vendor to start from BMW's latest US software for the donor's hardware, and avoid any older file.

### Still open
- BMW's VANOS ms and °KW limits. They live in the ISTA or DIS test module; keep the donor's baseline.
- An explicit BMW statement on system checks and readiness.
- Whether a 2003 US MSS54 answers mode 09. **What would settle it:** a generic scanner's "Vehicle info / VIN" on the donor before teardown, logged with the DME's software number.

### Guide impact (writer: **coding-power**)
- `WIRING-AND-CODING.md:1150`: "Whether these checks set a monitor to "ready" or only test the hardware isn't documented. A generic scanner shows … and, on many scanners, the stored VIN (mode 09)."
  > BMW's job descriptions call these "function checks" whose result you read afterwards ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)), and BMW's training says the readiness code is set when the drive cycle has completed each monitor ([BMW ST055, p.21](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%202%29/07_Emissions%20Overview.pdf)). Use them to prove the hardware, then drive the monitors. California requires the VIN over the OBD port only from the 2005 model year ([13 CCR 1968.2(g)(4.8.1)](https://www.law.cornell.edu/regulations/california/13-CCR-1968.2)); the rule for 1994–2003 cars asks only for the calibration ID and a software check ([13 CCR 1968.1](https://www.law.cornell.edu/regulations/california/13-CCR-1968.1)). So a 2001–03 MSS54 may not report a VIN at all. Check it with a generic scanner on the donor before you rely on it.
- `README.md:2398`: "- Whether the US MSS54 reports its VIN to generic OBD-II scanners (mode 09)." Replace with:
  > - Whether a 2001–03 US MSS54 reports its VIN in mode 09. No rule required it before MY2005 ([13 CCR 1968.2](https://www.law.cornell.edu/regulations/california/13-CCR-1968.2)); check the donor with a generic scanner.
- `README.md:2399`: keep it, adding "(BMW calls them function checks; readiness comes from the drive cycle)".
- `README.md:385` (Shop brief, DME flash): "…otherwise stock US software, since a Euro file can drop US emissions functions". Add:
  > Ask for BMW's latest US software for the donor's hardware: BMW reprogrammed 2001–05 US M3 DMEs because the original software could misjudge catalyst efficiency (SI B12 22 08, [NHTSA TSB index, record 10029304](https://static.nhtsa.gov/odi/ffdd/tsbs/TSBS_RECEIVED_2005-2009.zip)).
- `WIRING-AND-CODING.md:1010` and `README.md:2416` (VANOS limits): no change; still open.

---

## Gap 6. EWS sync of a virginized MSS54; INPA path

### Cited findings
- **RPM Motorsport, "BMW E39 E46 M3 M5 S54 S62 used ECU DME EWS programming"** [read] ([RPM](https://rpmmotorsport.net/products/bmw-e39-e46-m3-m5-s54-s62-used-ecu-dme-ews-programming)):
  - $300 ($500 list); "1 to 2 Business days turnaround time upon arrival"; "Overnight shipping both ways using our UPS shipping label";
  - "BMW 3 Series E46 M3 1999 to 2004 DME MSS54 (S54 Engine)" and "E46 M3 2004 to 08/2006 DME MSS54HP";
  - the supported hardware list runs from 7831815 to 7838802.
- A customer review on that page, "Kyle":
  - "I have successfully converted a S54 motor into a 2001 e46 330i sedan… The BIG challenge was getting the motor to crank and fire up…";
  - "If you are starting a motor conversation, you need to spend the money up front and get your DME synced to the EWS and key."
  - A second review is signed "Kalim" ("work on my modules to make my E46 S54 sedan swap complete").
  - The page doesn't say what the owner sends (DME only, or DME and EWS).
- **INPA:** one search found only other platforms' paths [snippet]:
  - "Shift+F6 … F1 (EWS Start Value Synch) and F2 (EWS Start Value Reset)", from a poster who said he was no expert;
  - a diesel (DDE) "write ISN" path on bimmerforums;
  - a 2025 X5 thread saying "EWS re-sync doesn't work correctly on many INPA versions" ([xoutpost](https://xoutpost.com/bmw-sav-forums/x5-e53-forum/116484-inpa-209-ews-code-error.html)).
  - No MSS54 script source is public on GitHub: code search for `EWS3_INITIALISIEREN` finds only the SGBD docs [read].

### Inferences
- **(inference)** That review is the first documented case of a used S54 DME made to start in a different E46 with its own EWS and key. It's a vendor bench job, not the DIY Tool32 virgin sync, so the guide's "no documented success" holds for the DIY route only.
- **(inference)** The Shift+F6 → F1/F2 layout matches the MS43 path Kassel films. Whether "MS S54 for S54 M3" has the same page is unverified: try it read-only and don't run it on a married DME.

### Still open
- A start-to-finish DIY sync of a virginized MSS54 to another E46's EWS3, and the INPA MSS54 EWS menu. **What would settle it:** an owner's screenshot of the INPA "MS S54" Shift-key menus, or asking RPM what they need (DME alone, or DME and EWS).

### Guide impact (writer: **coding-power**)
- `README.md:1558`: "| 2. Virgin DME, synced | … | About \$300 for the clearing, plus the risk that the sync fails | No documented success; two failures |"
  > | 2. Used DME matched to your EWS | A vendor programs the used DME to your car's EWS and key (RPM's "used DME EWS programming", \$300, 1–2 days plus overnight shipping both ways), or clears it for you to sync | About \$300 | One vendor-hosted review reports a running S54 in a 2001 330i after RPM "synced" the used DME "to the EWS and key" ([RPM](https://rpmmotorsport.net/products/bmw-e39-e46-m3-m5-s54-s62-used-ecu-dme-ews-programming)); a DIY sync of a virginized MSS54 is still undocumented, with two failures |
- `README.md:2393`: "- A documented sync of a virginized MSS54 to another car's EWS3, and INPA's key path for it." Replace with:
  > - A documented DIY sync of a virginized MSS54 to another car's EWS3, and INPA's key path for it. A vendor-matched used DME has worked once (RPM review).

---

## Gap 7. The Touring MK60's coding index

### Cited findings
- **ETK, Feb 2003 US 325i Touring, "Hydro unit DSC/fastening/sensors"** [read] ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/brakes/hydro_unit_dsc_fastening_sensors/)): hydro unit DSC 34516765453 "from Sep '01" (with and without M Sports package II), and "Repair kit, control unit DSC" 34526765455 "from Sep '01".
- **ETK part 34516765453** [read] ([ETK](https://bmwfans.info/parts-catalog/34516765453/)): "Hydro unit DSC … Production Jun '03 – … Exchangeable retrospectively; Old partnumber 34516759046"; used across the non-M E46 range, 316–330i including the 325i M54. So it's today's supersession, and a 2003 car may carry the older number.
- **No published coding index** for 34516765453 or 34526765455. GitHub code search found no E46 MK60 coding data, and one web search found only an eBay cross-reference (6759047 ↔ 6765453/6765455) [snippet].
- **How to read it:** `DSC_MK60.PRG` → `IDENT` returns `ID_BMW_NR` (part number), `ID_COD_INDEX` ("Codier-Index"), `ID_DIAG_INDEX` and `ID_VAR_INDEX` [read] ([SGBD DSC_MK60](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC_MK60.md)).

### Inferences
- **(inference)** The unit dates from the 09/2001 CAN-sensor-cluster generation, the same family as the 2002 318i dump (index C05) that offered `touring_s`. So `touring_s` is likely but unproven.

### Still open
- The coding index itself. **What would settle it:** in Session 1, run Tool32 `DSC_MK60.PRG` → `IDENT` (or read the CI in BMW Scanner's header), and read the unit's label for the actual part number. Then open the coding file in NCS Dummy and see whether `BAUART_MK60` offers `touring_s`.

### Guide impact (writer: **coding-power**; **front** for the DSC chapter)
- `WIRING-AND-CODING.md:91`: "| DSC identity | INPA or PA-Soft | Note the unit's part number and coding index (…) |". Add:
  > Tool32 `DSC_MK60.PRG` → `IDENT` shows both: `ID_BMW_NR` and `ID_COD_INDEX` ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC_MK60.md)). ETK lists hydro unit 34516765453 (which superseded 34516759046 in June 2003) and control-unit kit 34526765455 for a 2003 Touring ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/brakes/hydro_unit_dsc_fastening_sensors/)), so read your own unit's label.
- `WIRING-AND-CODING.md:961` (`touring` → `touring_s`). Add: "Whether your unit's coding index offers `touring_s` is unpublished; check it in NCS Dummy after reading the index."

---

## Other leads (outside the seven gaps)
- **Engine oil capacity differs between BMW's US M3 manuals:** MY2002 says "Engine with oil filter change approx. 5.3 (approx. 5.0)" quarts (liters); MY2003–05 say 5.8/5.5 [read]. The guide's 5.5 L (ST041) agrees with the later manuals; fill and check the dipstick.
- **The A/C compressor pulley after 09/2002:** Denso lists 64526916232 with a **4-groove** pulley, while the M3 belt group lists only 5PK × 829 (11287830946) [read]. Check the donor's pulley before buying a belt (cool writer).
- **MSS54 fan logic** uses a substitute coolant temperature (the block sensor minus 10 °C) if the radiator-outlet sensor fails (community wiki, above). A bad radiator-outlet sensor or lead may only show as a hotter-running fan, plus fault 0x2B or 0x60.

---

## Sources tried and blocked
- **web.archive.org and wayback.archive.org:** every connection reset at TLS through the session proxy (repeated through the session). The availability API worked intermittently (HTTP 429 at first) and reported no snapshots for the princeton.edu TIS printouts or the e46fanatics Bentley thread. WebFetch "is unable to fetch from web.archive.org".
- **newtis.info:** Cloudflare challenge (HTTP 403). Not bypassed.
- **turnermotorsport.com:** Cloudflare "Just a moment" page.
- **leebmann24.com:** Cloudflare 403.
- **buycarparts.co.uk:** 403.
- **rpmmotorsport.net E46 DME/EWS removal page:** rate-limited ("try again in a few minutes"). The product page loaded.
- **eCFR human pages:** redirect curl to unblock.federalregister.gov. The eCFR API worked and was used instead.
- **WebFetch** can't resolve bmwfans.info, so ETK pages were read with curl.
- **archive.org "BMW E36 TIS as HTML" (198 MB .7z):** not browsable in place and no 7z tool is installed. Not downloaded; it covers another chassis anyway.
- **GitHub `emdzej/ipo-community-patches` and the API tree listing:** not enabled for this session. Code search across GitHub worked, and raw files on raw.githubusercontent.com were read.
- **Not tried by design:** e46fanatics, m3post (blocked in earlier rounds); YouTube (rate-limited in earlier rounds).
- **Downloads** are in `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/gapfill-dl/bmw-powertrain/` (one folder per source). Nothing downloaded was executed.
