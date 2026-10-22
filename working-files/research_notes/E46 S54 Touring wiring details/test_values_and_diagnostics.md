# Test values, status checks and diagnostic paths: S54 into a US E46 325i Touring

Research date: 22 October 2026. Scope: a US 2001–05 E46 325i Touring (M54, MS43 to 02/2003 or MS45 from 02/2003, 5-speed manual, MK60 DSC) receiving a US E46 M3 S54 with an MSS54 or MSS54HP DME (EWS-deleted, Touring VIN written) and keeping the Touring's K96 fuel-pump relay on X60004 pin 10. Findings are labelled by DME family ([MSS54], [MSS54HP], [MS43], [MS45]) and market ([US], [Euro]) where it matters.

**Tags.** **(read)** = read on the page, PDF or file in this session. **(read, earlier note)** = read by an earlier researcher and recorded in `research_notes/E46 M3 Touring open questions/` (file named), not re-opened now. **(snippet)** = seen only in search-result text. **(blocked)** = refused (HTTP 403 or a Cloudflare check) and not used. "SGBD doc" = the community repository emdzej/ediabasx-docs-sgbd, which renders BMW's EDIABAS job and table files as Markdown; it is not a BMW publication. INPA prints fault locations in decimal: SGBD 0x82 = INPA 130.

**Limits kept.** No EWS patch details. Nothing here hides, clears or masks a readiness monitor; the readiness notes are about getting monitors to complete honestly.

## Takeaway

- **Several re-pinned circuits end at electronic parts, not plain switches.** BMW describes the manual clutch switch as a Hall sensor ("high signal when the clutch is depressed"), the E46 brake-light switch as an electronic switch that sends B+ when braking, and the S54 oil-level sensor as a PWM sender. A meter proves the wires; the MSS54's own status bits prove the parts.
- **The MSS54 reads clutch and gear switch as one input.** Its SGBD maps `STAT_KUP_EIN` and `STAT_KRAFTSCHLUSS_EIN` to the same bit with opposite sense. So the clutch status can only follow the pedal with a gear engaged; in neutral both are fixed. Test the chain in gear (inference from the table).
- **BMW pass/fail numbers exist for power, pedal, throttle, coils and fuel.** KL15 above 9 V with the DME-relay supply within 3 V of it; pedal Hall 1 0.5→4.5 V and Hall 2 0.5→2.0 V; throttle pot 0.5 V closed→4.5 V open (EDR feedback the reverse); coil primary plus harness ≈0.8 Ω; fuel 5.0 ± 0.2 bar with under 0.5 bar bleed-off.
- **Generic reference values fill most other gaps.** Bosch NTC 2,500 Ω at 20 °C and 323 Ω at 80 °C; TE mini-ISO 12 V relay coil 90 Ω; a new Bosch DM-TL measured pump 14 Ω, valve 30 Ω, heater 38 Ω; BMW purge valve about 28 Ω. No OEM figure was found for S54 injectors, crank or cam sensors.
- **Tool32 can prove most of the swap before the first crank.** With `MSS54DS0.PRG`: supplies (`STATUS_UBATT`, `STATUS_UEXT1/2`), every temperature sensor (they should agree on a cold-soaked engine), pedal and throttle, every re-pinned switch (`STATUS_DIGITAL`), and most outputs (`STEUERN_EKP`, `STEUERN_DMTL_HEIZUNG`, `STEUERN_SLP`/`SLV`, `STEUERN_KO`, `STEUERN_E_LUEFTER`, `STEUERN_TEV`). Whether `STEUERN_EKP` drives the X60004-10 relay output on US software isn't documented; a click at K96 settles it.
- **No-start path.** On EWS 3.3 a DME/EWS mismatch gives crank-no-start, not start-then-die (BMW). After a DME EWS delete the starter still needs the Touring's EWS, key and clutch input. Then: engine speed seen while cranking, EWS release and faults, pump prime and 5 bar, injector circuits, spark, throttle adaptation.
- **Inspection.** Under the federal OBD rule a car with stored codes passes if the MIL isn't commanded on, and a MY2001+ car may pass with one unset monitor (40 CFR 85.2222). Whether a leftover 130 (0x82) commands the MIL wasn't found: check `STAT_MIL_EIN` and a generic scanner's mode 01/03. Clearing faults resets readiness. The DM-TL leak test also uses the cluster's CAN data (fuel level, ambient temperature, parked time), which matters with an M3 cluster reading Touring senders.

## Q1. Continuity and resistance: moved and added circuits and their components

### Cited findings

**What kind of part sits at the end of each circuit**

- **Clutch switch (BMW, EWS 3.x).** "The clutch switch signal is provided by a hall-effect sensor providing a high signal when the clutch is depressed" (E31/E36 from MY1997); for EWS III (3.2) "A Hall-Effect Switch is added to the clutch system… High signal status indicates the clutch is depressed and vehicle starting is allowed" (read). — [BMW ST051 "05 EWS", pp. 16, 19](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- **Clutch-switch generations.** BMW SI 12 17 99 ("Engine Speed Appears To Hang During Shifts") covers "troubleshooting regarding the Clutch Switch/Circuit and upgrade to a three wire switch including ECM reprogramming" [MS42] (read). — [BMW ST055 "MS42 MS43", p. 30](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/3%20MS42%20MS43.pdf)
- **The M3 clutch module matters.** BimmerWorld on 61319122700: "The switch must work to allow the car to start or to disengage from cruise control." The alternative 35426876898 "will allow the engine to start but will not cancel the cruise control" (read). — [BimmerWorld](https://www.bimmerworld.com/Driveline-Shifter/Clutch-Parts/Genuine-BMW-Module-Clutch-Switch-61319122700-E39-M5-E46-M3-E85.html)
- **Brake-light switch (E46).** "The switch provides a B+ signal when the brakes are applied… The brake light switch provides a low voltage digital signal to the LSZ when the brake lights are not actuated. If this signal is interrupted the LSZ interprets this as a faulty brake light switch and initiates emergency mode." BMW also calls it "The Electronic brake light switch" (read). — [BMW ST052 "E46 Lighting Systems", pp. 7, 10](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03c_E46%20Lighting%20Systems.pdf)
- **Why the DME reads both brake contacts.** "The brake light switch and the brake light test switch are input to the ECM to disengage cruise control as well as fault recognition during engine operation of the MDK/EDK" [MS42/MS43; the MS45 module repeats it] (read). — [BMW ST055 "MS42 MS43", p. 109](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/3%20MS42%20MS43.pdf)
- **Sport switch [MSS54].** "The switch provides a ground signal as an input when pressed" (read). — [BMW ST055 "MS S54", p. 84](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **Clutch-and-gear chain [MSS54].** "two switches in series… a clutch switch and a gear selector switch… provide a high signal for the MS S54 when the clutch is disengaged and the transmission is in gear. If either the clutch is engaged or the transmission is in neutral, the cruise control will be disengaged" (read). — [BMW ST055 "MS S54", p. 84](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **Oil temperature and level sensor [S54].** A thermal probe in the sump; "The microprocessor in the base of the sensor produces a pulse width modulated signal proportional to the oil level. The pulse width increases with a decreased level of oil" (read). — [BMW ST055 "MS S54", p. 85](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf). The MSS54 fault 0x2C (44) "Signal aktiver Oelniveaugeber" carries the types "Pulsbreite zu gross" and "Pulsbreite zu klein" (read). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- **Oil-pressure switch [S54].** ETK lists 12 61 1 710 509 superseded through to 12 61 8 611 273, M12 × 1.5 (read). — [ETK, US M3 sensors](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/sensors/). Retailer listings describe this switch as normally closed, switching between 0.2 and 0.5 bar (snippet; the ECS page itself returned 403). — [Turner](https://www.turnermotorsport.com/p-5944185-oilpressuresensor/), [ECS (Meyle 12618611273)](https://www.ecstuning.com/b-meyle-parts/oilpressuresensor/12618611273~mey/). A swap shop: "The oil pressure switch closes at .5bar" (read, earlier note `harness_engine_side.md`). — [NAM3 61405](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)
- **Crank and cam sensors [S54].** The crank sensor is "an inductive pulse type sensor… on the left side at the rear of the engine block", reading a 58-tooth wheel with a two-tooth gap, and provides "the crankshaft position and engine speed (RPM) signal to the ECM for Fuel Pump and Injector operation". BMW tests it by "Power Supply, AC Voltage, Status Display, Oscilloscope". The cam sensors are Hall sensors fed from the ECM relay (intake wheel 6 lugs, exhaust 7); with a cam-sensor fault "the system will maintain engine operation based on the Crankshaft Position/RPM Sensor" with reduced torque (read). — [BMW ST055 "MS S54", pp. 29–30, 44](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **Coolant sensor [S54].** A "dual sensor (ECM/Temp Gage)" in the coolant return pipe, an NTC on a 5 V supply; if it fails the ECM uses the oil-temperature sensor. BMW tests it on the "Status Page - Degrees C" and by "Multimeter - Resistance" (read). — [BMW ST055 "MS S54", pp. 31, 44](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **Pedal module.** The US M3 and the US 325i Touring both list "Accelerat.pedal module, manual gearbox" 35 42 6 786 282 (read). — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/pedals/acceleration_accelerator_pedal_module/), [ETK 325iT](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/pedals/acceleration_accelerator_pedal_module/)
- **DM-TL parts.** The US M3 and the US 325i Touring list the same "Leak diagnosis pump": 16 13 6 756 440 to 09/2001, then 16 13 7 193 479 (read). — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/fuel_supply/exp_tank_activated_carbon_container/), [ETK 325iT](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/fuel_supply/exp_tank_activated_carbon_container/). A 2001 330Ci had a three-wire DM-TL where the M3's is four-wire (read, earlier note `youtube_swap_wiring_coding.md`). — [DBO, 03:41](https://www.youtube.com/watch?v=cEAIugEHkRQ&t=221s)

**Resistance and test values**

- **Ignition coils [MSS54], BMW.** "Resistance of the harness and ignition coil primary winding (terminal 15 to 1 approx. 0.8 ohms) - using the 134 Pin Adapter Set with the ECM disconnected." Also: "Terminal 1 of the ignition coil must not be connected to Ground or B+" (read). — [BMW ST055 "MS S54", pp. 57–58](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **Injectors [MSS54], BMW.** Test for "Resistance, Power Supply, Status Display, ECM Final Stage transistor activation", with no value given (read). — [BMW ST055 "MS S54", p. 43](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf). Aftermarket S54 injector sets are sold as "high impedance" and plug into the OEM harness (snippet). — [Turner](https://www.turnermotorsport.com/BMW-E46-M3-Parts/c-929-bmw-fuel-injectors)
- **Throttle sensors [MSS54], BMW.** "DIS Status Page (approx. 0.5v to 4.5v)" or a "Resistance check of the entire circuit, using the Universal Adapter with the ECM disconnected" (read). — [BMW ST055 "MS S54", p. 21](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **DM-TL, measured (generic Bosch).** On a new Bosch 0 261 222 018 (from a 2009 E93): "Pump motor: 14 ohms. Switching valve: 30 ohms. Heater: 38 ohms." The connector has four wires: "One supplies battery voltage during the test, and the others are ground circuits operated by drivers inside the PCM for the heater, pump and switching valve solenoid." Pump current rises when the valve opens. A test light from each driver wire to ground "should turn ON when power is on and the circuit is not active, and turn OFF when the circuit is activated" (read). — [Jacques Gordon, Motor Age/Vehicle Service Pros, 4 Aug 2017](https://www.vehicleservicepros.com/industry-news/article/53089788/evap-monitor-on-european-cars-real-world-diagnosis-of-dmtl-systems-2017-08-04)
- **DM-TL logic [MSS54], BMW.** A 1.0 mm reference orifice; "A large leak is detected… if the amperage value is not achieved. A small leak is detected if the same reference amperage is achieved. The system is sealed if the amperage value is higher than the reference amperage" (read). — [BMW ST055 "MS S54", p. 64](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf). BMW's X5 version of the same text uses a 0.5 mm orifice (read). — [BMW DM-TL training excerpt (X5)](https://www.princeton.edu/~sdepasqu/bmw/pdfs/Leak.Diag.Sys.pdf)
- **Purge valve and EVAP testing (BMW, generic).** "The resistance of the purge solenoid is about 28 ohms"; don't "pressurize the EVAP system to over 0.1 BAR (1.5 psi)"; "the DMTL unit is the vent for the system, so you must close the vent to use smoke detection"; "if the motor amperage is abnormally high, this indicates the motor may be locked up or debris has entered the reference orifice" (read). — [BMW TechDrive, "What If It's Not the Gas Cap?", pp. 20–23](https://automotivetechinfo.com/wp-content/uploads/2008/02/What-If-It-Is-Not-The-Gas-Cap.pdf)
- **Relay coil (generic).** BMW 61 36 8 373 700 is sold as "Tyco V23134-K59-X312 61.36-8 373 700/01" (snippet). — [eBay.de listing](https://www.ebay.de/itm/405201030575). TE's 12 V mini-ISO relay V23134-A52-X205 lists "Coil Resistance: 90 Ohm" (read). — [TE datasheet listing](https://radiolocman.com/datasheet/data.html?di=108521). ETK gives K96 (pump), K6327 (injectors) and K19 (A/C) the same part, 61368373700 (read, earlier note `harness_engine_side.md`).
- **NTC curve (generic Bosch).** Bosch NTC M12 (0 280 130 026), 2.5 kΩ ± 5 % at 20 °C: −10 °C 9,397 Ω; 0 °C 5,896 Ω; 10 °C 3,792 Ω; 20 °C 2,500 Ω; 30 °C 1,707 Ω; 40 °C 1,175 Ω; 60 °C 596 Ω; 80 °C 323 Ω; 90 °C 243 Ω; 100 °C 187 Ω (read). — [Bosch Motorsport datasheet](https://www.bosch-motorsport.com/content/downloads/Raceparts/Resources/pdf/Data%20Sheet_70101387_Temperature_Sensor_NTC_M12.pdf)
- **Pin endpoints [MSS54].** X60003: crank sensor 8 (signal) and 21 (ground); coolant temperature 24 (ground 25, shared with knock-sensor shield); intake-air temperature 22; oil-pressure switch 26; oil level 39; injectors 33–38 for cylinders 1–6; purge valve 42; idle actuator 46/47. X60004: DM-TL heater 18, valve 20, pump 30 ("USA only"); pedal grounds 7/12, signals 8/13, supplies 9/14; radiator-outlet sensor 38 (ground) and 39 (signal). X60005: coils 1/2/3/9/6/7 for cylinders 1/2/3/4/5/6, ground 5 (read). — [pinout sheet, "MSS54 DME 901-904" tab](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing) (community transcription of BMW tables)

### Inferences

- **Sort the checks by part type.**
  - Plain wires (lamps, Sport, brake second contact, pump trigger, DM-TL, chain wiring): end-to-end continuity, well under 1 Ω (generic), and open to ground.
  - Passive loads, measurable with the DME unplugged: coils (≈0.8 Ω each through the harness, BMW), DM-TL elements, K96 coil, injectors, NTC sensors.
  - Electronic parts (clutch module, brake-light switch, TOG oil-level sensor): an ohmmeter says little. Check their supply and ground, then their output with the key on: voltage or the DME's status bits (Q2, Q3).
- **DM-TL "triangle" test, from the X60004 connector alone.** With the DME unplugged and the DM-TL plugged in, the three driver pins meet at the DM-TL's common supply pin, so each pair of X60004 pins reads two elements in series. With the Bosch reference values: pins 18–20 ≈ 68 Ω, 18–30 ≈ 52 Ω, 20–30 ≈ 44 Ω. Each element = (sum of the two pairs that include it − the third pair) ÷ 2. The lowest (≈14 Ω) is the pump, ≈30 Ω the valve, ≈38 Ω the heater. This settles pump-versus-valve by resistance rather than by TIS label (the MS45 tables swap the labels). Open on both pairs that include pin 18 means no heater circuit: an early three-wire unit or a missing wire. The E46 unit's values may differ from the E93 reference; the method still separates the three.
- **Pre-09/2001 Touring with an early DM-TL.** The M3 and Touring share DM-TL numbers by date. The later unit is presumably the four-wire one with the heater (the 2001 330Ci's three-wire unit against the M3's four-wire unit fits that date split, but no source states it). If your Touring has a three-wire unit, the MSS54 heater output (X60004-18) has nothing to drive; fitting 16 13 7 193 479 should match what the MSS54 expects. Whether the MSS54 instead learns "heater not fitted" (`STAT_LDPH_VERBAUT_WERT`, Q3) wasn't documented.
- **Gear-recognition switch.** Closed in gear, open in neutral, from BMW's description of the chain; reverse isn't documented. Measure across its two pins in each position.
- **Oil-pressure switch.** X60003-26 (M3 harness side) to engine ground should read near 0 Ω with the engine stopped, and the lamp circuit opens once pressure exceeds about 0.2–0.5 bar.
- **Clutch module pins.** Pin 4 (EWS) should be high with the pedal down (BMW's EWS description). The chain wants a high signal in gear with the pedal up, which implies pin 2 has the opposite sense. Check both on the donor car before you strip it.
- **Relay swap test.** K96, K6327 and K19 are the same part, so swapping K96 with K19 is a quick relay check. Expect roughly 90 Ω across the coil (85–86); open or near 0 Ω is a failed coil (generic TE family value).
- **Temperature sensors.** After an overnight cold soak, each NTC's resistance should sit near the generic curve at ambient. The stronger check is that the DME's readings agree with each other (Q2).

### Gaps

- No BMW or E46-M3 resistance specification was found for S54 injectors, the crank or cam sensors, the E46 DM-TL, the K96 coil, the S54 temperature sensors (coolant dual sensor, intake air in the HFM, radiator outlet, TOG), the O2-sensor heaters, the idle actuator or the VANOS solenoids. BMW's TIS data sit on newTIS, which is behind a Cloudflare check.
- E46 voltage levels for the brake switch's two signals, and the polarity of the clutch module's DME output, weren't published in any source found.
- The gear switch's state in reverse.

## Q2. Key-on checks: DME power, the EWS handshake and the pump command

### Cited findings

- **Power layout [MSS54], BMW.** KL30 is the main supply. "KL15 (fused) supplies voltage to the Engine Control Module Relay and the Fuel Injector Relay." The ECM relay feeds the ECM, injector relay, idle actuator, purge valve, fuel-pump relay, coils, DM-TL, cam sensors, air-mass meter and O2 heaters. Grounds: X60001 pins 4, 5, 6; X60004 pin 5; X60005 pin 5 (read). — [BMW ST055 "MS S54", pp. 5–6](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **The DME's own supply check.** "Five seconds after the ignition is switched on and the voltage at the KL15 input is >9 volts, the ECM compares the voltage to the ECM Relay supplied voltage. If the voltage difference between the two terminals is greater than 3 volts, a fault code will be set." The ECM compensates between about 6 V and 14 V and holds the relay "for a few seconds" after KL15 off (read). — [BMW ST055 "MS S54", p. 7](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **What poor power and grounds look like.** "No Start; Hard Starting (Long Crank Times); Inaccurate Diagnostic Status or ECM (Not Found); Intermittant / Constant 'ENGINE EMISSION' Light; driveability problems". Test "Available Voltage; Voltage Drop (Dynamic Resistance); Resistance of Cables and Wires"; test the relay for "Battery Voltage and Switched Ground; Resistance; Battery Voltage and Voltage Drop"; measure at the ECM connector with break-out box 90 88 6 121 300, ignition off while connecting (read). — [BMW ST055 "MS S54", pp. 8–9](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **Power pins [MSS54].** X60001-7 "Terminal 30 – Fuse F102"; X60001-8 "Voltage supply – Fuse carrier, engine electronics"; X60001-1 "Terminal 15 – Relay, fuel injectors"; X60002-23 "Activation, main relay"; X60004-26 "Terminal 15 – Fuse F29" (read). — [pinout sheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
- **Measured values the DME reports [MSS54/MSS54HP].** `STATUS_UBATT` "Bordnetzspannung Hauptrelais" (main-relay supply, 0.1 V steps); `STATUS_UEXT1` and `STATUS_UEXT2` "Sensorversorgung 1 (Master)/2 (Slave)"; `STATUS_MOTORTEMPERATUR`, `STATUS_AN_LUFTTEMPERATUR`, `STATUS_OEL_TEMPERATUR` ("Oeltemperatur (TOG)"), `STATUS_KUEHLW_AUSL_TEMPERATUR`, `STATUS_TUMG`, all scaled with a −48 °C offset; related faults 0x36 (54) "Bordnetzspannung Hauptrelais", 0x3A (58) and 0x3B (59) sensor supplies 1 and 2, 0x4E (78) coolant sensor, 0x4D (77) intake-air sensor, 0x2B (43) radiator-outlet sensor (read). — [SGBD doc MSS54DS0 (BETRIEBSWTAB, FORTTEXTE)](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- **Pedal and throttle voltages [MSS54], BMW.** The ECM supplies 5 V. "Hall sensor 1 (request) = 0.5 to 4.5 volts; Hall sensor 2 (plausibility) = 0.5 to 2.0 volts." EDR feedback potentiometer "closed 4.5v - full open 0.5v"; throttle-valve potentiometer "closed 0.5v - full open 4.5v" (read). — [BMW ST055 "MS S54", p. 11](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **Throttles follow the pedal at key-on.** On a stock-hardware E46 M3: "with the key turned to 'on' and the manifold off, I looked… and pressed the throttle pedal down, only to see that the throttles were only opening about 30% of the way"; after a second throttle synchronisation they opened fully (read). — [MotoIQ, Project E46 M3 part 8, p. 5](https://motoiq.com/project-e46-m3-part-8-the-dreaded-eml-light/5)
- **EWS 3.x start sequence, BMW.** The EWS powers the key through the ring antenna, checks ID, password and changing code, then "looks at the other inputs for correct status (e.g. Code function not active, Transmission in P or N or clutch depressed, engine speed below specified RPM) and energizes the internal relay to begin starter operation. As the starter begins to operate, the EWS III module sends the ISN to the DME." "The entire process takes place in under 750ms." "If the starter engages the following inputs are functioning normally: Key, Code Function, Trans Range (Clutch Switch)" (read). — [BMW ST051 "05 EWS", pp. 15, 19–20](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- **EWS status job.** `EWS3.prg` → `STATUS_LESEN` returns `STAT_ANLASSER_FREIGESCHALTET` (starter released), `STAT_ANLASSER_AUS_DREHZAHL` (starter off: engine speed), `STAT_ANLASSER_AUS_P_N` (off: P/N input), `STAT_ANLASSER_AUS_ZV` (off: central locking), `STAT_ANLASSER_AUS_BC` (off: board-computer code), `STAT_P_N_EINGANG`, `STAT_KL_R_EINGANG`, `STAT_DME_LEITUNG_FREI`, `STAT_SCHLUESSEL_SENDET`, `STAT_SCHLUESSEL_GESPERRT`, `STAT_SCHLUESSEL_NIO_ID/_PW/_WC`, `STAT_AKTUELLE_SCHLUESSELNUMMER` and `STAT_MOTORDREHZAHL_KBUS`. EWS fault texts include key invalid by identification, password or changing code; "DME-Wechselcode verloren"; and info-memory entries "Keine Anlasserfreigabe durch EWS-Steuergeraet", "Kein Motorstart bei laufendem Anlasser" and "Übertraungsfehler auf Datenleitung zur DME D_EWS" (read). — [SGBD doc EWS3](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/EWS3.md)
- **DME side of the handshake.** `MSS54DS0` → `STATUS_DIGITAL` → `STAT_EWS3_FREIGABE` (byte 27, mask 0x80); `EWS3_GET_STATUS` → `EWS3_STATUS` and `EWS3_STATUS_WERT`; faults 0x82 (130) "EWS-Signalmanipulation" and 0x42 (66) "EWS-Schnittstelle" (read). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md). In the one failed Touring sync, `EWS3_GET_STATUS` read "Invalid", `EWS3_STATUS_WERT` = 3 (read, earlier note `coding_dme_ews.md`).
- **Pump command [MSS54 US], BMW.** "After the ignition is switched ON, the ECM provides voltage for the fuel pump module and the voltage is maintained (pulse width modulated) with the presence of the engine speed signal" (read). — [BMW ST055 "MS S54", p. 33](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf). On relay cars [MS42/MS43]: activated at KL15 on, held only with an engine-speed signal (read, earlier note `fuel_pump_control.md`).
- **Pump jobs and status.** `STEUERN_EKP` "Kraftstoffpumpenrelais ansteuern", `STEUERN_EKP_AUS` "Kraftstoffpumpe (Relais) ausschalten", `STATUS_DIGITAL` → `STAT_EKP_EIN` (byte 8, mask 0x40) (read). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- **BMW's pressure test and a warning.** Remove the pump relay and fit the relay bypass switch to the socket; "If the 5 bar fuel pressure is not achieved or bleed off is more than 0.5 bar, refer to 13 31". And: "DO NOT OPERATE THE FUEL PUMP unless it is properly installed in the fuel tank and is submersed in the fuel" (read). — [BMW ST055 "MS S54", pp. 39, 41](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **INPA's E46 menu.** A posted E46 engine-selection file ("Select E46 V1.30") contains "ENTRY= MSS54M3,MS S54 for S54 M3" and a separate "ENTRY= EKP_DS2,Fuel pump EKP" (read). — [bmwfaq, 2014](https://bmwfaq.org/threads/duda-con-el-inpa.796332/)

### Inferences: expected values at the first key-on

With the DME connected (back-probe or break-out box), charger on, key at position 2, engine off:

| Point | Expect | Fail means |
|---|---|---|
| X60001-7 (KL30) | Battery voltage, key on or off | Fuse F102 or the B+ feed |
| X60004-26 (KL15, F29) | Battery voltage with key on; 0 V key off | F29, ignition switch feed |
| DME relay K6300 | Clicks at key-on; X60001-8 at battery voltage while it's on; stays on a few seconds after key-off (BMW) | No click: X60002-23 control wire, relay coil feed from KL15, relay. Click but no X60001-8 voltage: E-box fuse carrier, the 3-pin plug's heavy feed |
| Grounds X60001-4/5/6, X60002-5, X60004-5, X60005-5 | Voltage drop to battery negative under load well under 0.1 V (generic) | Ground eyelets, the engine ground strap |
| `STATUS_UBATT` | Within a few tenths of a volt of the battery (generic); BMW sets a fault above a 3 V difference from KL15 | Relay contacts, fuse carrier, grounds |
| `STATUS_UEXT1`, `STATUS_UEXT2` | About 5 V (BMW's sensor supply) | Shorted sensor feed (pedal, throttle pots); faults 0x3A/0x3B |
| Temperatures (cold-soaked engine) | Coolant, oil (TOG), intake air, radiator outlet and ambient all close to ambient. NY's cold-start rule (coolant and air within 11 °F) is a fair tolerance | A reading pinned near −48 °C (raw 0) or wildly off points to an open or shorted sensor circuit (inference from the scaling) |
| Pedal | `STATUS_PWG_POTI_SPANNUNG` ≈ 0.5 V released, rising towards 4.5 V; `STATUS_PWG_POTI_WINKEL` and `_2` 0→100 % | Pedal wiring X60004 7–9/12–14 |
| Throttles | Follow the pedal at key-on (MotoIQ); `STATUS_DKP_WINKEL` follows `STATUS_DKP_WINKEL_SOLL` | EDR, potentiometers, adaptation |
| Pump | Runs briefly at key-on (prime); `STAT_EKP_EIN` = 1 during the prime; `STEUERN_EKP` makes K96 click and the pump run; 5.0 ± 0.2 bar at the test port | See the pump checks below |
| EWS (`EWS3.prg` → `STATUS_LESEN`) | Key sending, not barred, all three "NIO" bits 0; with the clutch down `STAT_P_N_EINGANG` changes and `STAT_ANLASSER_AUS_P_N` = 0 | Key, ring antenna, clutch module pin 4 to EWS pin 8, EWS coding |
| DME release | `STAT_EWS3_FREIGABE` = 1 (expected; not confirmed for a deleted DME) | Read `FS_LESEN` for 0x82/0x42 |
| MIL | Lit at key-on, engine off (bulb check). Whether `STAT_MIL_EIN` reads 1 during that check isn't documented; it shows whether the DME itself commands the lamp | Cluster coding or the DME's CAN message; also an inspection failure point (Q6) |

**Confirming the pump relay is commanded without cranking**, in order of certainty:

1. Listen at K96 (behind the glovebox) and at the tank at key-on: one prime.
2. Watch `STAT_EKP_EIN` in `STATUS_DIGITAL` change during the prime.
3. Run `STEUERN_EKP`. If K96 clicks and the pump runs, the X60004-10 output is proven; stop it with `STEUERN_EKP_AUS`. If the job returns OKAY but K96 stays silent, the job may be driving only the US module output (X60002-11); fall back to the next step and the manual's fused-jumper test.
4. With K96 pulled, a test light across the socket's two coil terminals should flash at key-on (the generic test-light method in the Motor Age DM-TL article); with K96 fitted, the pin-10 side of the coil drops to near 0 V during the prime.
5. A gauge on the filter-regulator test port shows 5.0 ± 0.2 bar during the prime (BMW). Never run the pump without fuel in the tank (BMW).

INPA's "Fuel pump EKP" module won't answer on this build because there's no module, so don't chase it.

### Gaps

- The "good" `EWS3_STATUS` text and value for a synced MSS54, and what `STAT_EWS3_FREIGABE` reads on an EWS-deleted DME.
- Which output `STEUERN_EKP` drives on US software, and whether the `STEUERN_*` jobs need particular conditions (the SGBD's IO-control result table includes "Ansteuerbedingung nicht erfuellt", activation condition not met).
- The length of the MSS54's key-on prime.

## Q3. MSS54 status jobs for each circuit

### Cited findings

- **One file covers both DMEs.** `MSS54DS0.prg` is "MSS52/MSS54/MSS54HP fuer S54B32", revision 2.09, with 223 jobs; the DME group file maps the MSS54 and MSS54HP variants to it; `12MSS54.prg` is the programming and AIF file (read). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md), [d_0012](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/d_0012.md), [12MSS54](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/12MSS54.md)
- **`STATUS_DIGITAL` bit map (BITS table).** `S_KUP` byte 24, mask 0x08, value 0x08; `S_GANG` byte 24, mask 0x08, value 0x00; `S_BLS` byte 24 0x10; `S_BLTS` byte 24 0x04; `S_KL15` byte 24 0x20; `S_KL50` byte 30 0x80; `S_FDYN` byte 30 0x01; `EWS3` byte 27 0x80; `MIL` byte 26 0x80; `EKP` byte 8 0x40; `FGR` byte 12 0x01; `SMFL1`–`SMFL4` byte 32 with masks 0x01, 0x02, 0x03, 0x04 (read). The job's result `STAT_FGRA_EIN` is commented "Status Lambdaregler Bank 2", an apparent copy error; the table names it FGR (cruise). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- **Fault memory structure.** `FS_LESEN` returns per fault the location, eight fault-type texts (`F_ART1…8_TEXT`) and up to 15 environment values (`F_UW…`). The fault-type matrix pairs most locations with "Fehler abgasrelevant OBD" (emission-relevant) in type slot 5, alongside "momentan vorhanden/nicht vorhanden" and "statisch/sporadisch". Environment values include "Sondenheizwiderst. 1 v. Kat" and its three siblings in ohms (O2-heater resistance), "LDP-Referenzstrom" and "LDP-Messstrom" in mA, "Versorgungsspannung HR" and "Tankfuelstand (CAN)" (read). — [SGBD doc MSS54DS0 (FARTMATRIX, FARTTEXTE, FUMWELTTEXTE)](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- **System-check result tables.** `LDPSTATUS` (DM-TL) runs from wait states such as "8_WARTEN_FUELLSTAND", "11_WARTEN_FEHLER_LOESCHEN" and "12_WARTEN_VENTIL_FEHLER" to results "32_ERGEBNIS_DECKEL_DICHT", "33_ERGEBNIS_GROB_DICHT", "34_ERGEBNIS_FEIN_DICHT", "35_ERGEBNIS_DECKEL_FEHLT", "36_ERGEBNIS_GROBLECK", "37_ERGEBNIS_FEINLECK", and aborts including "43_ABBRUCH_KL15_EIN", "48/49_ABBRUCH_REFERENZSTROM_HI/LO", "50_ABBRUCH_VERSTOPFT" and "53_ABBRUCH_EKP_CRASH_OFF". `SLSSTATUS`: "1_SLS_OK", "2_SLS_FEHLER", "32_TEST_LAEUFT". `TEVSTATUS`: "16_ERGEBNIS_TEV_OK", "17_ERGEBNIS_LL_OK", "18_ERGEBNIS_LL_NICHT_MOEGLICH" (read). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- **INPA path.** E46 → Engine → "MS S54 for S54 M3" (script `MSS54M3`) (read). — [bmwfaq](https://bmwfaq.org/threads/duda-con-el-inpa.796332/). One owner of a factory-manual 2003 M3 (CSL software) reports "INPA test for chain grip function works as intended (off with pedal out and on with the clutch pressed to the floor)"; his cruise still didn't work (read, rendered page). — [NAM3 318576](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/318576-factory-manual-car-cruise-control-shift-lights-not-working)
- **VANOS testing in practice [MSS54HP, Z4 M].** Owners compare DIS/ISTA VANOS results: a "15 degree deviation… on the leak test" is "massive"; adjustment times went from the 300s (ms) at 40 bar VANOS oil pressure to "the low 200s" with a new unit at 115 bar (read). — [z4-forum, page 2](https://z4-forum.com/threads/bmw-z4m-e86-s54-marbles-in-a-can-type-noise-possible-vanos.156718/page-2). "DIS contains a very useful VANOS test which isn't available on INPA" (snippet). — [z4-forum](https://z4-forum.com/threads/need-a-favour-from-someone-with-inpa-bmw-diagnostics.70651)
- **MSS54HP differences documented elsewhere.** Same SGBD and job names (above). A 32 kB partial read is an MSS54, 64 kB an MSS54HP; stock MSS54HP software sends the charge lamp (and oil level) over CAN; one owner says a 2006 car drives the pump module from pin 10 rather than pin 11 (read, earlier notes `coding_dme_ews.md`, `harness_engine_side.md`, `fuel_pump_control.md`). The gear-switch logic exists in both: a published software change for deleting the gear switch lists separate MSS54 and MSS54HP locations (read). — [NAM3 318576](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/318576-factory-manual-car-cruise-control-shift-lights-not-working)

**Per-circuit job map** (all in `MSS54DS0.PRG` unless noted; fault numbers hex/decimal from the SGBD's FORTTEXTE):

| Circuit | Job → result | Expected | Faults |
|---|---|---|---|
| Clutch + gear-recognition chain (X60002-20) | `STATUS_DIGITAL` → `STAT_KUP_EIN`, `STAT_KRAFTSCHLUSS_EIN` | In gear, pedal up: KRAFTSCHLUSS 1, KUP 0. In gear, pedal down: 0 and 1. Neutral: 0 and 1 whatever the pedal (inference from the shared bit) | 0x50/80 "Schalterkette Kraftschluss": "Kraftschluss im Stillstand", "Kein Kraftschluss bei Fahrt" |
| Brake light switch (X60004-24 via LSZ) and second contact (X60004-34) | `STATUS_DIGITAL` → `STAT_BLS_EIN`, `STAT_BLTS_EIN` | Both bits change with the pedal; record the released/pressed pattern | 0x6A/106 "Bremslichtschalter" |
| Sport button (15) and LED (16) | `STATUS_DIGITAL` → `STAT_FDYN_EIN` | Changes when the button is pressed; LED follows the Sport state | 0x6E/110 "LED Fahrdynamikschalter" |
| Cruise buttons (X60004-27, MFL data) | `STATUS_DIGITAL` → `STAT_MFL1…4_EIN`, `STAT_FGRA_EIN`; `STATUS_ADAPTIONSBLOCK_06` → `STAT_FGR_MFL_VERBAUT_WERT` | Bits change with each steering-wheel button; FGR flag learned after an adaptation reset | 0x51/81 "MFL-Schnittstelle", 0x8B/139 "Tempomatsystem", 0xC2/194 "Sicherheitsabschaltung FGR" |
| DM-TL (18 heater, 20 valve, 30 pump) | `STEUERN_DMTL_HEIZUNG` ('ein'/'aus'), `STEUERN_DMTL_HEATER`; `START_SYSTEMCHECK_DMTL` then `LESEN_SYSTEMCHECK_DMTL` (LDPSTATUS text); `STATUS_TANK_DICHTHEIT` → `LDP_STROM`, `LDP_REFSTROM`; `STAT_LDPH_VERBAUT_WERT` | Heater switches; a check ending "…_DICHT" (tight); sealed system: measuring current above reference current (BMW logic) | 0x0E/14 "LDP-Heizung", 0x1B/27 "Ventil Tankleckdiagnose", 0x7F/127 "Modul Tankleckdiagnose", 0xB4/180 "Tankleck", 0xB5/181 "Info Tankdeckel fehlt" |
| Pump relay (X60004-10 → K96) | `STEUERN_EKP`, `STEUERN_EKP_AUS`; `STAT_EKP_EIN`; `STAT_EKP_CFG_VERBAUT_WERT` | K96 clicks, pump runs | 0x01/1 "Relais Kraftstoffpumpe" (expected with US software and no module), 0x7E/126 "EKP-Crash-Abschaltung" |
| Oil pressure (switch → X60003-26 → X60004-11 → cluster) | No status result in the SGBD | Red lamp on at key-on, out after start; mechanical gauge | None listed for the switch |
| Oil level/temperature (TOG → X60003-39) | `STATUS_OEL_TEMPERATUR` | Plausible oil temperature (proves the TOG is alive) | 0x2C/44 "Signal aktiver Oelniveaugeber" |
| Throttle and pedal | `STATUS_DKP_WINKEL`, `STATUS_DKP_WINKEL_SOLL`, `STATUS_PWG_POTI_WINKEL`/`_2`, `STATUS_PWG_POTI_SPANNUNG`; `STATUS_ADAPTIONSBLOCK_06` → `STAT_WDK_ADAPT_WERT` ("0 = ok"), `STAT_PWG1/2_A0_WERT`, `STAT_WDK1/2_A0_WERT` | Actual follows target; adaptation state 0 | 0x3C/60, 0x3D/61 pedal sensors; 0x6F/111, 0x70/112 pedal comparisons; 0x76–0x79/118–121 throttle pots; 0x2D/45 EDK hardware; 0x55/85 EDK sensor; 0xE4–0xE6/228–230 EGAS |
| VANOS | `STATUS_EVANOS1_IST`/`_SOLL` (and bank 2, exhaust); `STEUERN_LLS_TESTDREHZAHL`; `STEUERN_EVANOS1_VERSTELLZEIT`, `…_DICHTHEIT`, `…_FRUEHANSCHLAG`/`SPAETANSCHLAG` per cam; `STAT_VAN_ADAP_ST_WERT` | Engine warm; no BMW limits found; owners report low-200 ms adjustment times on healthy units (DIS) | 0x07/0x08/0x0A/0x0B cam Hall sensors; valve and control faults 0x15/0x16/0x43/0x48/0x4A/0x4B/0x53/0x54/0x71/0x72/0xB8/0xB9 |
| Power | `STATUS_UBATT`, `STATUS_UEXT1`/`2` | Battery voltage; about 5 V | 0x36/54, 0x3A/58, 0x3B/59 |
| EWS | `STAT_EWS3_FREIGABE`; `EWS3_GET_STATUS` | Released | 0x82/130, 0x42/66 |
| Speed inputs | `STATUS_GESCHWINDIGKEIT` (direct, X60004-22) and `STATUS_V_CAN` | Agree while rolling | 0x2A/42 direct speed input, 0x87/135 both speed sources |
| Secondary air (pump relay X60004-3) | `STEUERN_SLP`, `STEUERN_SLV`; `START_SYSTEMCHECK_SEK_LUFT` then `LESEN_SYSTEMCHECK_SEK_LUFT`; `STEUERN_SLS_CHECK` | Pump runs, valve clicks; "1_SLS_OK" | 0x13/19 relay, 0x3F/63 valve, 0xAA/170 minimum flow, 0xAB/171 valve stuck |
| Purge valve | `STEUERN_TEV`; `STEUERN_TEV_CHECK` | Valve clicks; "16_ERGEBNIS_TEV_OK" | 0x24/36, 0xE8/232 |
| O2 heaters | `STEUERN_LSHV1/2`, `STEUERN_LSHN1/2`; `STAT_LSHV1_EIN`… | Heater status bits on | 0x25–0x28/37–40, with heater resistance stored in the fault record |
| Fans, A/C, brake jet pump | `STEUERN_E_LUEFTER`; `STEUERN_KO` (`STAT_KO_EIN`); `STEUERN_VENTIL_SAUGSTRAHLPUMPE` (opens 2 s) | Fan runs; K19 clicks; valve clicks | 0x35/53 fan, 0x8F/143 E-box fan, 0x30/48 A/C relay, 0x89/137 and 0x8E/142 jet pump |
| Misfire per cylinder (running) | `STATUS_SYSTEMCHECK_LAUFUNRUHE` (physical cylinder order, %) | Six similar values | 0xC4–0xD5 misfire |
| Readiness | `STATUS_ADAPTIONSBLOCK_26` → `STAT_FF_FF_RDY_WERT`, `…_RDY_CNT0…15_WERT` | See Q6 | — |

### Inferences

- **Test the chain in gear, engine off, parking brake on.** If `STAT_KUP_EIN` "follows the pedal" only in gear, that's correct behaviour, not a fault. The manual's Session 6 step 5 and the guide's Phase 11 "Done when" row say `STAT_KUP_EIN` follows the clutch pedal without mentioning the gear; add "with a gear engaged". The NAM3 owner's "chain grip" toggling with the pedal is consistent with testing in gear. A chain that never closes in gear points to the gear switch or the clutch module's DME output; one that is always closed points to a short at X60002-20.
- **Brake bits.** Both must change state when the pedal moves. A pressed pedal that changes only one of them leaves the DME unable to confirm braking; expect 0x6A and no cruise. The non-S54 E46 race car in Tenza's cruise video showed "plausibility signal brake light switch" with no cruise (read, earlier note `youtube_swap_wiring_coding.md`).
- **Sport LED.** If the LED wire (pin 16) isn't fitted, fault 0x6E is the likely result (inference from the fault table); Tenza's LED didn't work at first start (read, earlier note).
- **SMFL bits.** The masks for buttons 3 and 4 (0x03, 0x04) look like table errors; if `STAT_MFL3_EIN` or `STAT_MFL4_EIN` behave oddly while 1 and 2 work, trust the cruise function test instead.
- **Fault records do the measuring for you.** Read the environment values in `FS_LESEN`: an O2-heater fault stores the heater resistance, a DM-TL fault stores the reference and measuring currents, a supply fault stores the main-relay voltage.
- **Actuator jobs, safely.** Run them key-on, engine off, charger on, one at a time. Before `STEUERN_EV1…6` (injectors), pull K96 so the jobs don't squirt fuel into the cylinders. Run `STEUERN_ZS1…6` (coils) only with every coil seated on its plug, given BMW's warnings about terminal 1 and secondary voltage. Both are inferences from BMW's ignition and fuel cautions, not documented procedures.

### Gaps

- The F-key layout of INPA's MS S54 script (status, activation, adaptation pages), including where its "chain grip" test sits.
- No SGBD status result for the oil-pressure input or the oil-level value itself.
- BMW limits for the VANOS jobs and the meaning of the `EWS3_STATUS` values.
- Whether `ADAPT_LOESCHEN` resets readiness, and whether the "verbaut" flags relearn on the first drive or need a specific event.

## Q4. No-start diagnosis for an S54 swap

### Cited findings

- **EWS mismatch symptom, BMW.** On EWS 3.3, if the DME can't match the rolling code, "Failure to find a match will result in the engine cranking but not starting" (read, earlier note `coding_dme_ews.md`). — [BMW ST051 "05 EWS", pp. 21–23](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- **After an EWS delete the starter is still the EWS's.** The EWS "is now simply looking for a proper matchup with the key transponder itself"; don't jumper EWS pins (read, earlier note `coding_dme_ews.md`). — [NAM3 38046](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful). Import Modify's vendor-deleted DME still needed "the EWS matching the key" (read, earlier note `youtube_swap_wiring_coding.md`). — [Import Modify, 11:50](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=710s)
- **Crank signal drives fuel and spark.** The crank sensor provides speed "for Fuel Pump and Injector operation"; injector triggering is established from it at KL15 on; a cam-sensor fault leaves the engine running on the crank signal (read). — [BMW ST055 "MS S54", pp. 29–30, 34](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **Throttle adaptation.** If adaptations aren't cleared and relearned after throttle or pedal changes, "the vehicle will not start, or run in 'fail-safe' mode" (read, earlier note `coding_dme_ews.md`). — [BMW ST041 Engine Electronics Part 1, p. 15](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%201%29.pdf)
- **EML shutdown [S54].** "when this light would come on, the car would shut itself off in a matter of roughly 3 seconds and not start back up. The engine would turn over but there would be no fuel or ignition". Causes worked through: throttle sensor 1, pedal module, throttle sensor 2, throttle synchronisation, finally the throttle actuator; pulling fuse 29 and refitting it with the key off cleared it for about 20 minutes; low charging voltage (12.55 V at idle) was suspected along the way (read). — [MotoIQ, Project E46 M3 part 8, pp. 1–5](https://motoiq.com/project-e46-m3-part-8-the-dreaded-eml-light/)
- **Documented swap no-starts** (read, earlier notes `coding_dme_ews.md`, `fuel_pump_control.md`, `harness_engine_side.md`):
  - 2002 325iT: after the EWS fault was cleared with the donor EWS, still crank-no-start with "fuel pump relay error code 1" and "all six injectors disabled and zero pulse duration"; unresolved. — [e46fanatics 1318881](https://www.e46fanatics.com/threads/ews-synch-for-s54-swap-into-e46-touring.1318881/)
  - MS42 323i: old fuel and an EWS plug left connected; the pump had primed (71 psi). — [NAM3 82513](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/82513-s54-swap-to-ms42-car-no-start)
  - Feed and return swapped at the filter: no start (same thread).
  - 330i: injector "circuit low" on all six from an X6053/X60531 mismatch. — [e46fanatics 1277127](https://www.e46fanatics.com/threads/s54-swap-fuel-injectors-low-circuit.1277127/)
  - Euro 328i Touring (MS42 body): X6011 didn't mate; cranked without starting; a scanner saw no modules; unresolved. — [e46fanatics 1305546](https://www.e46fanatics.com/threads/328i-touring-s54-swap-dme-wiring.1305546/)
  - E36 S54: started only with the pump fuse pulled, then flooded; a ground terminal at X60003-25 wasn't seated. — [NAM3 112619](https://nam3forum.com/forums/forum/special-interests/coding-tuning/112619-s54-only-starts-when-fuel-pump-fuse-is-pulled-did-i-code-it-wrong)
  - Tenza's Touring: first attempt failed on a flat battery. — [Tenza, 03:55](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=235s)
  - M54 330Ci: mixing coil harnesses from different DME families damaged a DME. — [e46fanatics 1298699](https://www.e46fanatics.com/threads/330ci-engine-swap-no-start-looking-for-help.1298699/)

### Inferences

- **"Starts then dies" isn't the EWS 3.3 signature.** BMW describes a mismatch as crank-no-start, and a deleted DME ignores the code. If the engine catches and dies, look first at EML/throttle faults (MotoIQ), the pump not being held (no engine-speed signal reaching the relay logic, or a K96 hold problem), idle air (actuator unplugged, leaks at the idle-air pipe), and fuel pressure collapse. Chase the EWS only if 0x82 or 0x42 is present.
- **Order the checks by what each one excludes:** DME communication → starter release (EWS) → engine speed while cranking → EWS faults on the DME side → fuel (prime, 5 bar) → injector circuits → spark → air and throttle. The full tree is in the diagram data below.

### Gaps

- What the MSS54 does at start with a cam signal missing: BMW says injection timing is affected but not whether it still starts.
- No first-hand no-start report from a 2001–05 US MS43/MS45 325i Touring beyond the 2002 325iT case.

## Q5. Warning lights after the first start

### Cited findings (documented outcomes)

- **Many lamps at first start, most cleared by coding.** ShopLifeTV's swapped sedan lit "like a Christmas tree" (read, earlier note `youtube_swap_wiring_coding.md`). — [ShopLifeTV, 05:45](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=345s). Tenza's Touring (Kassel EWS-deleted DME): "The check-engine and oil lights went out after about 10–15 s"; airbag/seat-belt (seat out), washer and headlight lamps were expected; the Sport LED didn't work (read, earlier note). — [Tenza, 05:38](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=338s)
- **ABS/DSC.** Tenza: non-M wheel-speed sensors in M3 hubs gave an ABS light; fallback was the donor's sensor pigtails (read, earlier note). — [Tenza, 07:18](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=438s). An S54 wagon with an M3 MK60 and M3 cluster never cleared 5EF1 "VIN not initialized"; refitting the 325i MK60 fixed it (read, earlier note `harness_body_functions.md`). — [e46fanatics 1260275](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/). ThaChileanDude's Touring kept an ABS light, a tamper dot and a check-engine light, undiagnosed (read, earlier note). — [ThaChileanDude, 35:19](https://www.youtube.com/watch?v=iSgClonTiQg&t=2119s)
- **Parking-brake lamp.** Permanently lit in a 1998 323i (MK20 ASC) with an M3 cluster, cause not found; it worked in a 2001 325iT (read, earlier note `harness_body_functions.md`). — [e46fanatics 1003871](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/), [e46fanatics 1207433](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)
- **Oil and charge lamps.** 2001 325iT (MS43): neither lamp until the oil-pressure signal was joined to the cluster wire and the battery lamp re-established; 2003 ZHP (MS45.1): pin 11 wired to cluster pin 13 and "oil pressure via CAN" coded off; "The alternator light is powered through the cluster and grounded by the DME whenever the alternator is not charging" (read, earlier note `harness_engine_side.md`). — [e46fanatics 1207433](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/), [NAM3 61405](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)
- **Check engine, documented causes.**
  - Pump-module fault with US software on a relay car: stored, visible in INPA/ISTA/PA-Soft, "does not set the CEL" (read, earlier note `fuel_pump_control.md`). — [e46fanatics 1307461 p.2](https://www.e46fanatics.com/threads/s54-swap-california-bar-certification.1307461/page-2), [Kalim p.38](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38). The "fuel pump relay" code these swappers describe (and the "error code 1" in the 2002 325iT case) matches SGBD location 0x01 (1), "Relais Kraftstoffpumpe"; 130 (0x82) is the separate EWS fault, not a pump fault.
  - EWS 130 after a delete: "the code still shows up, but I confirmed that the engine can start"; MIL status not stated (read, earlier note `coding_dme_ews.md`). — [NAM3 38046](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful)
  - DM-TL: an MS45.1-body swap still set "P2418 - Evaporative Emission System Switching Valve Control Circuit / Open" after swapping pins 20 and 30; unresolved (read, earlier note `harness_body_functions.md`). — [e46fanatics 1286041](https://www.e46fanatics.com/threads/e46-m3-sport-button-retrofit-on-non-m.1286041/)
  - SMG software in a manual car: the DME logged "SMG No CAN"; also "Steering angle sensor no CAN" in a car without that sensor (read, earlier note). — [e46fanatics 1003871](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/). The SGBD lists "MIL-Anforderung durch SMG" as a fault type (read).
  - "make sure you swap over all harnesses including the oxygen sensor harness, the smg harness" (read, earlier note). — [UNRIVALED, 04:39](https://www.youtube.com/watch?v=eddLff8yba0&t=279s)
  - O2 heater and secondary-air faults are two-trip: BMW lights the lamp when the fault is present again at the next monitoring or the next cold start (read). — [BMW ST055 "MS S54", pp. 76–77](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **EML.** See MotoIQ in Q4: throttle sensors, pedal, synchronisation, actuator, charging voltage (read).
- **Cruise.** A new M3 clutch module (replacing a junkyard 330i one) fixed no-cruise in an S54 wagon (read, earlier note). — [e46fanatics 1260275](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/). A 5-speed S54 323i never got cruise without a gear switch (read, earlier note). — [e46fanatics 1003871](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/). BimmerWorld: the non-M3 number lets the car start "but will not cancel the cruise control" (read, above).
- **Airbag.** On seat swaps, the light came from E46 pretensioners or the occupancy plug, and a slip ring pulled apart during a wheel swap (snippet). — [z4-forum](https://z4-forum.com/threads/airbag-light-on-after-swapping-to-e46-seats.117343). M346 cleared airbag codes with a scan tool and "disabled" the occupancy sensor for M6 seats (read, earlier note `youtube_conversion_builds.md`). — [M346, 13:20](https://www.youtube.com/watch?v=DxMs8VZiXGY&t=800s). BMW: the airbag unit tells the DME to cut fuel-pump power in a crash (read, earlier note `fuel_pump_control.md`).
- **Gearbox/SMG lamp and tamper dot.** SMG lamp "which the tuner… would code out"; a gearbox icon stayed lit until AKMB and ALSZ were coded (read, earlier note). — [Tenza cruise video, 16:19](https://www.youtube.com/watch?v=8uRGM-OzqWs&t=979s), [50sKid, 26:05](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1565s)
- **"Check filler cap".** The ECM detects refuelling from the tank level reported by the cluster and shows "Check Filler Cap" if the leak test then finds a leak (read). — [BMW ST055 "MS S54", p. 72](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)

### Inferences

- **Expected lamp states for this build.** Key on, engine off: red oil, charge and check-engine lamps lit (the check-engine bulb check is also an inspection item, Q6). After start: oil and charge out within seconds; check-engine out unless a MIL-relevant fault is stored. DSC/ABS until Session 5 is done. A stored pump-module fault (and possibly 130) without a lamp is the expected end state.
- **Use the DME to tell "lamp wiring" from "real fault".** `STAT_MIL_EIN` shows whether the DME is commanding the MIL. If the bit is 0 and the lamp is lit, suspect the cluster or its coding; if the bit is 1, read `FS_LESEN`.

### Gaps

- No first-hand reports of O2-heater or secondary-air check-engine faults in an S54 swap that kept these systems; ThaChileanDude's and ShopLifeTV's later check-engine lights were never diagnosed on camera.
- Whether 0x82 (130) lights the MIL, with or without the vendor's tampering-fault option.

## Q6. Readiness monitors and inspection

### Cited findings

- **Monitors BMW documents for the MSS54:** catalyst, O2 sensors and heaters, secondary air, EVAP (DM-TL leak test plus purge), misfire, plus fuel-system diagnosis; the DM-TL test needs a 5-hour park, a 20-minute drive, engine and ignition off with the DME in follow-up mode, 15–85 % fuel, −7 to 35 °C, below 2,500 m and 11.5–14.5 V, and runs only every second time (read; already in `coding_dme_ews.md` and the manual). — [BMW ST055 "MS S54", pp. 64, 70–72, 76–78](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf). The SGBD's fault list includes "Kraftstoffsystemdiagnose 1/2" (0xAE/0xAF) and "KAT-Konvertierung 1/2" (0xB2/0xB3) (read).
- **The DM-TL test waits on other systems.** `LDPSTATUS` includes "8_WARTEN_FUELLSTAND" (waiting for fuel level), "11_WARTEN_FEHLER_LOESCHEN" and "12_WARTEN_VENTIL_FEHLER" (read). The DME logs the tank level received "(CAN)", and has faults for the cluster's ambient temperature (0xE1, including "Erkennung hängender Sensor nach längerer Fzg.-Standzeit") and the cluster's relative time (0xE2, "unplausible Fzg.-Standzeit") (read). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md). BMW: "The ECM detects refueling from a change in the fuel tank sending unit level via the Instrument Cluster" (read). — [BMW ST055, p. 72](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf). A general DM-TL test condition list includes "No existing EVAP fault codes" (read). — [Motor Age](https://www.vehicleservicepros.com/industry-news/article/53089788/evap-monitor-on-european-cars-real-world-diagnosis-of-dmtl-systems-2017-08-04)
- **Readiness in Tool32.** `STATUS_ADAPTIONSBLOCK_26` → `STAT_FF_FF_RDY_WERT` "Readinessmaske", driving cycles and warm-up cycles since reset and since fault clearing, and per-function counters `STAT_FF_FF_RDY_CNT0…15_WERT` (read). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- **Federal OBD inspection rule.** "If the MIL bit is not commanded to be illuminated the vehicle shall pass the OBD inspection, even if DTCs are present"; MY2001+ vehicles may pass "with no more than one unset readiness monitor"; a car fails if the MIL is commanded on but not lit, or if "the MIL does not illuminate at all when the vehicle is in the key-on/engine-off condition"; the connector must be present and working (read). — [40 CFR 85.2222](https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-85/subpart-W/section-85.2222), [40 CFR 85.2207](https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-85/subpart-W/section-85.2207)
- **New York (example state).** MY2001+ fail "when more than 1 monitor is reported as Not Ready"; "Erasing stored codes with a scan tool. This also resets all of the monitors back to zero… If any of the erased fault codes reappear, it may prevent one or more of the monitors from completing"; disconnecting the battery also erases stored codes and monitor results (read). — [NYVIP3 Ready vs Not Ready](https://www.nyvip3.com/OBDII/ReadyVSNotReady)
- **Swap outcomes.** A shop that leaves the relay pump wiring and runs stock US software "save for the EWS delete": "the DME will… show all the readiness codes just like a stock M3 and will pass an OBD2 plug in emissions test" (read, earlier note `fuel_pump_control.md`). — [e46fanatics 1307461 p.2](https://www.e46fanatics.com/threads/s54-swap-california-bar-certification.1307461/page-2). An MSS54-swapped sedan in California: "All my monitors show as ready except EVAP. No CEL" (read, earlier note). — [e46fanatics 1303447](https://www.e46fanatics.com/threads/s54-swaps-and-smog-in-california-update.1303447/). An E46 M3 owner's catalyst and O2 monitors weren't ready after the battery had died (snippet; the thread returned 403). — [bobistheoilguy](https://bobistheoilguy.com/forums/threads/smog-check-failed-for-catalyst-not-ready.294508/)

### Inferences

- **Does a stored 130 (0x82) matter?** Under the federal rule, only if it commands the MIL. It isn't a readiness monitor and shouldn't stop one completing unless the DME treats it as emission-relevant (it's not an EVAP fault, so the DM-TL "waiting for faults" states shouldn't apply; inference). To check your car rather than guess:
  1. Engine running: `STATUS_DIGITAL` → `STAT_MIL_EIN` should be 0 and the lamp out.
  2. A generic scanner: mode 01 MIL status off; mode 03 shows no code that maps to the EWS fault.
  3. In `FS_LESEN`, look at the 0x82 record's fault-type texts: the SGBD's matrix has an "emission-relevant OBD" slot, and if it's set for 0x82 the DME regards it as emissions-relevant (inference about how the slot is used).
- **Don't clear faults or disconnect the battery after the readiness drive.** Clearing resets the monitors (NY), and a 130 that re-stores on the next key cycle comes straight back anyway (the HoDoo report).
- **The M3 cluster in a Touring feeds the leak test.** The DM-TL test waits for a valid fuel level, uses the ambient temperature and parked time from the cluster, and the cluster's level comes from the Touring's senders. If the gauge reads wrongly (an open question in the guide), the 15–85 % window may be judged wrongly and EVAP may never run. Check the fuel gauge against a measured fill before driving for readiness.
- **The MIL bulb check is an inspection item.** With an M3 cluster, confirm the check-engine lamp lights at key-on, engine off.

### Gaps

- Whether 0x82 or 0x01 is ever reported as a generic P-code in mode 03, and whether either is flagged emission-relevant in a real `FS_LESEN` read.
- The list of monitors the US MSS54 reports as supported in mode 01 (EGR and heated catalyst presumably unsupported; not confirmed).
- Whether an MSS54 keeps readiness through a battery disconnect or an `ADAPT_LOESCHEN` (NY's statement is generic).
- A BMW-published E46 M3 drive cycle: none found; the guide's assembled plan stands.

## Diagram-ready data

### (a) Pre-power-up and first key-on test sequence

Each step: action → pass value → if it fails. "DME out" = all five DME plugs disconnected; take the battery off for resistance checks.

**Phase P — battery off, DME out, ignition off**

1. **P1 Terminals.** Tug-test every moved terminal; emptied cavities empty (X60004 23 and 28; on MS45 also 2, 5, 19, and 15 unless it now carries Sport). → Pass: all locked, cavities empty. → Fail: reseat or replace terminal.
2. **P2 Insulation.** Each moved wire to chassis ground. → Pass: open (OL). → Fail: pinched or misrouted wire.
3. **P3 Lamp wires.** X60004-11 → cluster X11175-13; X60004-1 → cluster charge-lamp pin; X60004-21 → cluster 17; X60004-6 → cluster (if moved). → Pass: continuity, under about 1 Ω (generic). → Fail: wrong cavity, wrong cluster pin (13 versus Kassel's 14).
4. **P4 Oil-pressure switch.** M3 harness X60003-26 → engine ground. → Pass: near 0 Ω, engine stopped (normally-closed switch). → Fail: switch plug, wire, or switch.
5. **P5 Brake second contact.** X60004-34 → brake-switch plug second-contact pin. → Pass: continuity. (The switch is electronic; prove it in step K7.)
6. **P6 Clutch chain wiring.** Clutch plug pin 2 → gear switch pin 1; gear switch pin 2 → X60002-20; gear switch across its pins. → Pass: wires continuous; gear switch near 0 Ω in gear, OL in neutral (inferred from BMW's chain description). → Fail: gear switch, wiring, the E-box crossing.
7. **P7 EWS interlock wire.** Clutch plug pin 4 → EWS pin 8. → Pass: continuity.
8. **P8 Sport.** X1869-17 → X60004-15; X1869-18 → X60004-16; X60004-15 to ground with the switch unit fitted. → Pass: continuity; OL released, near 0 Ω pressed (BMW: ground when pressed).
9. **P9 DM-TL triangle.** DM-TL connected; X60004 18↔20, 18↔30, 20↔30. → Pass with the Bosch reference: about 68, 52 and 44 Ω, solving to heater ≈38, valve ≈30, pump ≈14 Ω. → Fail: OL on pairs with 18 = no heater (early unit or wire); identical readings or 0 Ω = short.
10. **P10 Pump trigger.** X60004-10 → K96 coil terminal (SW/VI); M3 module wire (X60002-11, black 4-pin plug) → every K96 terminal; K96 coil 85–86. → Pass: continuity; OL to every terminal; about 90 Ω (generic). → Fail: find K96's coil wire for your VIN; isolate the module wire; swap K96 with K19.
11. **P11 Coils.** Coil supply (terminal 15 side) → X60005-1/2/3/9/6/7. → Pass: about 0.8 Ω each, all alike (BMW). → Fail: coil or harness; never a non-MSS54 coil harness.
12. **P12 Injectors.** Injector-relay output feed → X60003-33…38. → Pass: six equal readings (no OEM figure found). → Fail: injector, plug, X6053/X60531 mismatch.
13. **P13 Temperature sensors.** Coolant X60003-24↔25; radiator outlet X60004-38↔39 (and intake air at the air-mass meter). → Pass: near the NTC curve at ambient (about 2.5 kΩ at 20 °C, generic). → Fail: open/short; confirm later with step K5.
14. **P14 Crank sensor.** X60003-8↔21. → Pass: a steady coil resistance (no OEM figure), open to ground. → Fail: sensor or wire.
15. **P15 CAN.** All modules connected, ignition off: CAN high↔low (X60004-36↔37 back-probed). → Pass: about 60 Ω (generic). → Fail: about 120 Ω = one terminator missing; 0 Ω = short.

**Phase V — battery on, DME still out**

16. **V1 KL30.** X60001-7 (harness side) → Pass: battery voltage.
17. **V2 KL15.** Key on: X60004-26 → Pass: battery voltage; key off 0 V.
18. **V3 Heavy feed.** 3-pin E-box plug heavy wire → Pass: battery voltage where the diagram shows it live.
19. **V4 Grounds.** X60001-4/5/6 → battery negative → Pass: near 0 Ω / under 0.1 V drop under load (generic).

**Phase K — DME connected (ignition off while plugging), charger on, key on, engine off**

20. **K1 Relay and comms.** K6300 clicks; INPA two black dots; Tool32 `IDENT` OKAY. → Fail: power/ground (V1–V4), cable pins 7/8.
21. **K2 Faults.** `FS_LESEN` → Pass: only expected faults (0x01 pump relay; possibly 0x82; DSC VIN faults in the DSC until Session 5).
22. **K3 Supplies.** `STATUS_UBATT` ≈ battery voltage; `STATUS_UEXT1/2` ≈ 5 V. → Fail: relay, fuse carrier, a shorted sensor supply.
23. **K4 Lamps.** Oil, charge and check-engine lamps lit at key-on (the check-engine bulb check is also an inspection item). → Fail: lamp wiring (P3), cluster coding; `STAT_MIL_EIN` tells you whether the DME is commanding the MIL.
24. **K5 Temperatures.** Coolant, oil, intake air, radiator outlet, ambient → Pass: within a few °C of each other on a cold-soaked engine. → Fail: sensor circuit.
25. **K6 Pedal and throttles.** Pedal 0→100 % on both channels; voltage ≈0.5 V released; throttles follow the pedal; actual follows target. → Fail: pedal wiring, EDR, sync.
26. **K7 Switch bits (`STATUS_DIGITAL`).** In gear: pedal up → `STAT_KRAFTSCHLUSS_EIN` 1, `STAT_KUP_EIN` 0; pedal down → 0/1. Neutral → 0/1 whatever the pedal. Brake: `STAT_BLS_EIN` and `STAT_BLTS_EIN` both change with the pedal. Sport: `STAT_FDYN_EIN` changes. Cruise buttons: `STAT_MFL1…4_EIN` change. → Fail: see the Q3 table.
27. **K8 EWS.** `EWS3.prg` → `STATUS_LESEN`: key sending, not barred, no NIO bits; clutch down → P/N input changes, `STAT_ANLASSER_AUS_P_N` = 0. → Fail: key/antenna/EWS; clutch pin 4 → EWS pin 8.
28. **K9 Pump.** Prime heard; `STAT_EKP_EIN` toggles; `STEUERN_EKP` clicks K96; gauge 5.0 ± 0.2 bar; under 0.5 bar bleed-off. → Fail: P10, fuses, relay swap, lines (feed/return).
29. **K10 Outputs.** `STEUERN_DMTL_HEIZUNG` 'ein'/'aus'; `STEUERN_SLP`, `STEUERN_SLV`; `STEUERN_KO` (K19 clicks); `STEUERN_E_LUEFTER`; `STEUERN_TEV`; `STEUERN_VENTIL_SAUGSTRAHLPUMPE`. → Pass: each part runs or clicks, `JOB_STATUS` OKAY. → Fail: that part's wiring; "condition not met" means try with the engine running later.

**Phase C — oil-priming crank (K96 and K6327 out, coils unplugged)**

30. **C1 Interlock.** Clutch up → no crank; clutch down → cranks. → Fail: EWS pin 8 input, EWS coding.
31. **C2 Engine speed.** While cranking, `STATUS_MOTORDREHZAHL` > 0 (or the tach moves) and `STAT_KL50_EIN` = 1. → Fail: crank sensor (X60003-8/21).
32. **C3 Oil.** Mechanical gauge shows pressure; red lamp goes out. → Fail: stop; mechanical check.
33. **C4 Reset.** Refit relays and coils; `ADAPT_LOESCHEN`, `FS_LOESCHEN`; key off at least 15 s; key on → throttle click; `STAT_WDK_ADAPT_WERT` = 0. Then the first start (Session 6 of the manual).

### (b) No-start decision tree

- **Q1. Key on: does Tool32 `IDENT` (or INPA) reach the DME?**
  - **No →**
    - Is the cable's 7/8 bridge set, COM port and `obd.ini` matched? (DME is on OBD pin 7.)
    - Does K6300 click? No → X60004-26 KL15 (F29), relay coil feed, X60002-23, relay.
    - Battery voltage at X60001-7 and X60001-8 (relay on)? No → F102, E-box fuse carrier, 3-pin plug heavy feed.
    - Grounds X60001-4/5/6, X60004-5, X60005-5 good? (BMW: bad power/ground → "ECM not found", no start.)
    - Still no → compare the E-box plugs pin by pin (the 328i Touring case: X6011 didn't mate, scanner saw no modules).
  - **Yes → Q2.**
- **Q2. Clutch fully down, key to start: does the starter crank?**
  - **No →**
    - Battery at rest at least about 12.4 V (generic) and the charger on? (Tenza's first attempt failed on a flat battery.)
    - `EWS3.prg` → `STATUS_LESEN`: key sending? barred? NIO-ID/PW/WC? → key, ring antenna, EWS module (an EWS delete in the DME doesn't change this).
    - With the clutch down, does `STAT_P_N_EINGANG` change and `STAT_ANLASSER_AUS_P_N` read 0? No → clutch module power and ground, pin 4 → EWS pin 8 (Hall high with pedal down), EWS `PARK/NEUTRAL_EINGANG` coding.
    - `STAT_ANLASSER_AUS_ZV`, `_BC` or `_DREHZAHL` = 1? → car double-locked, code function, or the EWS sees engine speed.
    - `STAT_ANLASSER_FREIGESCHALTET` = 1 but no crank → terminal 50 path from the EWS to the starter (E-box X6011 pin 1 on the M3 harness), starter, main cable and ground strap.
    - Never jumper EWS pins: if it needs that, the key/EWS has a fault.
  - **Yes → Q3.**
- **Q3. While cranking, does the DME see engine speed (`STATUS_MOTORDREHZAHL` > 0, tach moves)?**
  - **No →** crank sensor, its plug, X60003-8/21; fault 0x10 (16). Without it there's no injection, no spark and no pump hold (BMW).
  - **Yes → Q4.**
- **Q4. Any EWS fault in the DME (0x82/130, 0x42/66), or `STAT_EWS3_FREIGABE` = 0?**
  - **Yes →** the DME isn't released: confirm the delete took (re-read the partial file; ask the vendor), or the sync failed (virgin DME only). By BMW's description this gives crank-no-start. A "pump relay" 1 with all injectors disabled followed the EWS problem in the 2002 325iT.
  - **No → Q5.**
- **Q5. Did the pump prime at key-on, and is there 5.0 ± 0.2 bar?**
  - **No prime →** X60004-10 → K96 coil continuity; pump fuse; K96 swapped with K19; `STEUERN_EKP`; a fused jumper from pin 10 to ground; E-box 4-pin/8-pin plugs (the 323i wagon with no matching plugs).
  - **Primes, low or no pressure →** feed and return swapped at the filter-regulator; regulator and its vacuum hose; pump volume (≥ 1.12 L in 30 s at 12 V, Bentley as quoted); old fuel.
  - **OK → Q6.**
- **Q6. Injector faults (0x03/0x05/0x04/0x21/0x1F/0x20), or "circuit low" on all six?**
  - **Yes →** injector relay K6327, its E-box fuse, X6053/X60531 mismatch; six equal injector resistances.
  - **No → Q7.**
- **Q7. Spark: coil faults (0x19/0x17/0x18/0x32/0x34/0x33), or no spark?**
  - **Yes →** coil primary about 0.8 Ω terminal 15 → 1 at the DME (BMW); X60005-5 ground; coil harness from the M3 harness only; plugs and boots.
  - **No → Q8.**
- **Q8. Air and throttle: `STAT_WDK_ADAPT_WERT` = 0, throttles follow the pedal, idle actuator plugged in (X60003-46/47), no EML faults?**
  - **No →** clear adaptations and let the throttles relearn with a cold engine (BMW: otherwise "will not start, or run in fail-safe"); throttle sensors, pedal, actuator (MotoIQ).
  - **Yes →** mechanical causes (timing, compression), outside wiring.
- **Branch S. Starts, then dies.**
  - **Dies within about 3 s with EML →** throttle/pedal fault (MotoIQ): read faults, check sensors, synchronisation, actuator, charging voltage.
  - **Dies when the prime would end →** the pump isn't held: engine-speed signal and K96 hold path (`STAT_EKP_EIN` with the engine running).
  - **Dies at idle, no EML →** idle actuator, leaks at the idle-air pipe, adaptation, fuel pressure.
  - **Runs only with the pump fuse pulled, then floods →** an unseated ground terminal (the E36 X60003-25 case); tug-test.
  - **EWS 3.3 mismatch isn't this symptom** (BMW: crank-no-start); look at the EWS only if 0x82/0x42 is stored.

### (c) Warning-light table

| Light | Likely causes, in order | Check | Fix (documented build where there is one) |
|---|---|---|---|
| Check engine (MIL) | 1. DM-TL circuit (heater 0x0E, valve 0x1B, module 0x7F) after the pin moves or with an early three-wire unit; 2. SMG software in the DME (SMG CAN faults, "MIL-Anforderung durch SMG"); 3. O2-sensor or heater circuits (0x25–0x28), wrong or mixed O2 harness; 4. secondary air (0x13, 0x3F, 0xAA, 0xAB); 5. injector circuits (X6053 mismatch); 6. throttle/pedal (also EML); 7. misfire | `STAT_MIL_EIN`; `FS_LESEN` with environment values; DM-TL triangle (P9); `START/LESEN_SYSTEMCHECK_DMTL`; `STEUERN_SLS_CHECK` | Re-pin DM-TL and identify pump/valve by resistance (one MS45.1 case left P2418 unresolved); manual-gearbox software; use the M3 harness's own O2 section (UNRIVALED); repin X6053 (330i case). Tenza's CEL went out 10–15 s after start with a Kassel DME |
| Stored, no lamp | 0x01 "Relais Kraftstoffpumpe" (expected with US software and K96); possibly 0x82 (130) after a delete; possibly 0x6E if the Sport LED isn't wired | `FS_LESEN`; confirm `STAT_MIL_EIN` = 0 | Leave the pump fault (it doesn't set the CEL per two swappers) or fit the module; 130 per vendor; wire pin 16 |
| Oil pressure (red) | Off at key-on: pin-11 wire missing or wrong cluster pin; cluster expects oil pressure over CAN. On while running: low oil pressure; lamp wire grounded | Key-on lamp; P3/P4; mechanical gauge | Wire X60004-11 → X11175-13 and code "oil pressure via CAN" off (ZHP case); 325iT joined the signal to the cluster wire |
| Charge (battery) | Off at key-on: pin-1 wire or CAN coding. On while running: alternator, belt, terminal 61 wire (X60003-13), low voltage | Key-on lamp; running voltage (`STATUS_UBATT`) | 325iT owner re-established it in 15 minutes once the circuit was understood. MotoIQ's stock-hardware M3 showed 12.55 V at idle on an underdrive pulley and a battery light that stayed on after the stock pulley went back; its cause isn't on the pages read |
| Oil level (yellow) | Pin-21 wire to cluster 17 or CAN coding; TOG sensor (0x2C) | `STATUS_OEL_TEMPERATUR` plausible; fault 0x2C | Wire 21 → 17 (sheet: "add anyway") |
| EML | Throttle sensor 1 or 2, pedal module, throttle synchronisation, actuator; low charging voltage; adaptation not done | Faults 0x76–0x79, 0x3C/0x3D, 0x6F/0x70, 0xE4–0xE6; `STAT_WDK_ADAPT_WERT` | MotoIQ: sensors, two synchronisations, then a new actuator; adaptation reset (Session 6) |
| ABS / DSC / brake | 1. VIN not initialised (5EF1/5E1F) until the cluster VIN matches; 2. wheel-speed sensor plugs/sensors (M3 hubs, non-M sensors); 3. steering-angle not calibrated; 4. an M3 MK60 that won't accept the Touring; 5. parking-brake lamp stuck (cause unknown in one MK20 car) | INPA DSC fault memory and wheel speeds | Session 5 initialisation; M3 sensor pigtails (Tenza); refit the 325i MK60 (S54 wagon) |
| Cruise (won't engage) | 1. Clutch module not the M3's 61319122700; 2. gear switch missing or open; 3. brake contacts implausible (0x6A); 4. SMG software; 5. MFL data line (0x51) | `STAT_KRAFTSCHLUSS_EIN` in gear; `STAT_BLS/BLTS_EIN`; `STAT_MFL…`; faults 0x50, 0x6A, 0x8B, 0xC2 | New M3 clutch module (S54 wagon); fit the gear switch (5-speed 323i never got cruise without one) |
| Airbag | Seat swap (pretensioners, occupancy mat), steering-wheel slip-ring plugs | INPA airbag fault memory | Matching pretensioners/plugs; clear codes. Don't bypass: the airbag unit also cuts the fuel pump in a crash |
| Gearbox/SMG lamp, tamper dot | SMG software; AKMB/ALSZ not coded after a vehicle-order change; cluster VIN or mileage mismatch | DME software variant; cluster coding | Manual software; code AKMB and ALSZ (50sKid); Session 4 |
| "Check filler cap" | Cap not sealing; leak found after refuelling | `LESEN_SYSTEMCHECK_DMTL`; fault 0xB5 | Cap and seal; smoke test with the DM-TL vent closed, under 0.1 bar (BMW TechDrive) |

## Key sources

- BMW: [ST055 MS S54](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf); [ST051 EWS](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf); [ST052 E46 Lighting](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03c_E46%20Lighting%20Systems.pdf); [ST055 MS42/MS43](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/3%20MS42%20MS43.pdf); [TechDrive EVAP article](https://automotivetechinfo.com/wp-content/uploads/2008/02/What-If-It-Is-Not-The-Gas-Cap.pdf).
- EDIABAS job documentation: [MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md), [EWS3](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/EWS3.md), [12MSS54](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/12MSS54.md).
- Regulation: [40 CFR 85.2222](https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-85/subpart-W/section-85.2222), [40 CFR 85.2207](https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-85/subpart-W/section-85.2207), [NYVIP3](https://www.nyvip3.com/OBDII/ReadyVSNotReady).
- Generic component data: [Motor Age DM-TL](https://www.vehicleservicepros.com/industry-news/article/53089788/evap-monitor-on-european-cars-real-world-diagnosis-of-dmtl-systems-2017-08-04), [Bosch NTC M12](https://www.bosch-motorsport.com/content/downloads/Raceparts/Resources/pdf/Data%20Sheet_70101387_Temperature_Sensor_NTC_M12.pdf), [TE V23134 relay](https://radiolocman.com/datasheet/data.html?di=108521).
- Blocked or not used: newTIS (Cloudflare), ECS Tuning product page (403), bobistheoilguy thread (403), classicmotorsports thread (Cloudflare), GitHub wiki of saildot4k/MSS54-XDFs (403), xoutpost via WebFetch (DNS; fetched by curl instead, no values).
