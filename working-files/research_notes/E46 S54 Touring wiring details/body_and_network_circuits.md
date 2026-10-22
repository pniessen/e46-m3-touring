# Body-side and network circuits: S54 and M3 parts in a US E46 325i Touring

Scope: a US 2001–05 E46 325i Touring (M54B25, 5-speed manual, MS43 to 02/2003 or MS45 from 02/2003, Teves MK60, IHKA or IHKR) receiving a US E46 M3 drivetrain (S54, MSS54/MSS54HP), the M3 instrument cluster (new EEPROM, true mileage taken from the light module), and keeping its own body harness, light module and MK60. E46 only. Researched 22 Oct 2026.

**Reading key.** **[read]** = I read the statement in the source in this session (PDFs converted to text, pages fetched with curl, images viewed). **[read, image]** = read from a picture or scanned table. **[snippet]** = seen only in a search-engine result; the page was blocked or not fetched. Source classes are named in each line: **BMW** (BMW of North America technical-training PDFs mirrored on archive.org), **ETK** (parts catalog via bmwfans.info), **SGBD** (community markdown export of BMW EDIABAS module description files, GitHub `emdzej/ediabasx-docs-sgbd`), **WDS/newTIS/TIS copy** (owner-posted or transcribed copies of BMW diagrams), **forum**, **vendor**, **hobby site**. e46fanatics.com and bimmerfest.com now serve a proof-of-work bot check, and bimmerforums, newtis.info, realoem.com, pdfcoffee.com and forums.beyond.ca returned 403; I did not get round any of these, so their content appears only as snippets. msextra.com returned "509 Bandwidth Limit Exceeded" twice. Downloads were kept in their own folders and were never executed.

Companion notes: `../E46 M3 Touring open questions/harness_body_functions.md` (X60004 moves), `coding_body_chassis.md` (coding), `youtube_swap_wiring_coding.md`, and the sibling `test_values_and_diagnostics.md` in this folder (status jobs and test values). This file adds the cluster, CAN/D-bus/K-bus, climate, crash, cruise, switch-centre, DSC-sensor and lighting circuits, with diagram data at the end.

## Takeaway

- **Cluster lamps.** Both clusters use the same two plugs: X11175 (26-pin, black) and X11176 (18-pin, white). The oil-pressure lamp (pin 13), charge lamp (pin 2), oil level (pin 17), coolant level, brake fluid, parking brake, pad wear, airbag and ABS lamps are hard-wired. Engine speed, coolant temperature, fuel consumption, check-engine, cruise, overheat, DSC/ASC/yellow-brake and (from MY2002) tyre-defect lamps arrive over CAN, as do the M3 oil-temperature gauge and warm-up LEDs. In an M3 the oil-pressure switch goes to the DME (X60003-26), and the DME drives cluster pin 13 from X60004-11. The charge lamp is fed by the cluster and grounded by the DME through X60004-1 to cluster pin 2. **Pin 14 is the K-bus** (two independent pinouts), so Kassel's "oil pressure to cluster pin 14" is an error. M3 clusters can instead take charge, oil level and oil pressure over CAN (`GENERATOR_UEBER_CAN`, `TOG_UEBER_CAN`, `CAN_OELDRUCKSCHALTER`).
- **Fuel gauge.** The cluster reads the two lever senders separately (left and right litres) and converts them through the coded `TANK_KENNLINIE`. An M3 cluster offers only `60_l_literskala`, `dad_tank_diesel` and `metalltank`. The M3 tank is 63 L and the 325i wagon's 16.6 gal (62.8 L), both plastic, so they should share the 60-litre curve. An ex-M56 SULEV metal tank would need `metalltank`. M3 and non-M senders are different part numbers. Verify with Tool32 `STATUS_TANKINHALT_LESEN` and a measured fill.
- **Network.** The E46 PT-CAN joins the DME, the cluster (gateway to the K-bus and D-bus), the DSC unit, the steering-angle sensor and, on automatics, the EGS. The MK60 sensor cluster has its own CAN to the DSC unit, and SMG M3s have a local SMG-CAN. BMW: two 120 Ω terminators, 60 Ω total, "located in the ASC/DSC control unit and either the instrument cluster or in the DME". From 06/2000 build the E46 diagnosis socket carries TXD II (DME/EGS) on pin 7 and TXD (D-bus, everything else via the cluster) on pin 8, with no CAN at the socket. That is why E46 cables bridge 7 and 8.
- **A/C and cooling.** Both IHKA and IHKR send the A/C request, compressor load and fan stage over K-bus → cluster → CAN, and the DME grounds compressor relay K19 (X60004-29). BMW lists IHKR as standard on the 325iT *and* the M3 from 09/2000, so the MSS54 gets the same messages either way. The electric fan is a DME PWM output (X60004-4) to a power stage on the fan, from a 50 A fuse. The S54's only electric coolant pump is the auxiliary pump built into the US M3 heater valve (64118369807). The climate module switches it; the 325i has a plain valve, and the CSL/non-M valve (64118369805) fits the S54 with no wiring.
- **Crash fuel cut-off.** There is no direct airbag-to-pump wire on an E46. The MRS III sends a crash telegram on the K-bus, the cluster forwards it on CAN, and the DME switches the pump off. The MSS54 has this function (fault location 0x7E "EKP-Crash-Abschaltung"), and BMW's S54 texts say the pump relay or module is switched off. Nobody documents whether a US MSS54 also drops the X60004-10 relay output that this build uses for K96.
- **Cruise.** On both cars the right-hand MFL buttons reach the DME on a single serial wire (X60004-27). The brake inputs are X60004-24 (via the light module) plus the second contact (28 on MS43, 34 on MSS54). The clutch goes to X60004-23 on MS43; on the MSS54 the clutch module and the 420G gear-recognition switch are in series to X60002-20, high only in gear with the pedal up. Cruise speed comes from the DSC over CAN.
- **Sport button and switch centre.** The newTIS pinout gives X1869 (23-pin): pin 7 terminal 30 (F42), pin 22 terminal R (F12), pin 23 K-bus, pins 17/18 Sport signal and LED to DME 15/16, pin 2 tyre-pressure reset. X521 (4-pin) carries terminal 15 (F33), the DSC-off signal to the DSC unit, 58g and ground. A Touring with only a solo DSC button has the 4-pin plug but no X1869 wiring.
- **DSC sensors.** The US 325i's MK60 (from 09/2000) and the M3's MK60 (from 09/2002) use magnetoresistive wheel-speed sensors with blue plugs. M3s built to 09/2002 have the MK20 with inductive sensors and grey plugs: different technology, and they don't plug into the Touring. The full MK60 47-pin pinout is in the diagram data. Pad-wear sensors differ by part number but use one hard-wired loop to cluster pin 24.
- **Lights.** The US M3 had halogen as standard and xenon as option S522A (bi-xenon from 09/2001). The headlight socket housings, xenon ballasts, levelling motors and levelling sensors (front 37146784696, rear 37146784697) are the same parts as the Touring's. BMW fitted automatic levelling to every US xenon car, run by the light module (LSZ). ETK lists different LSZ switch units for xenon and halogen. Coding: `$522` in the vehicle order, `BI_XENON`, `KALTUEBERWACHUNG_AL`, `AUTO_LWR_ENABLE`, `KENNLINIE_LWR_SENSOR_VO/HI`. Never replace the cluster and the light module at the same time, or the true-mileage record is lost.

---

## Q1. Instrument cluster: pinout, hard-wired versus CAN lamps, oil-pressure and charge-lamp feeds

### Cited findings

**Connectors and pinout**
- Hobby site transcription of the E46 cluster plugs: "A2 - IKE, Instrument Cluster; X11175 - Black 26 pin Connector; X11176 - White 18 pin Connector; Fuse 10 - 5 Amps - Terminal R; Fuse 34 - 5 Amps - Terminal 15; Fuse 43 - 5 Amps - Terminal 30". The full pin table is reproduced in the diagram data (table D1). Selected pins: 1 ground BR/SW; 2 "S_61-1, Battery Charge Indicator" BL; 3 "S_30H, Engine Start Signal Feedback" SW/GN; 9 "D_CAN-H" GE/RT; 10 "D_CAN-L" GE/BR; 11/12 right tank sender; 13 "S_OLD, Oil Pressure Switch (A6000-11)" BR/GN; 14 "K-BUS" WS/RT/GE; 15/16 left tank sender; 17 "F_OLN, Oil Level Sensor", WS/GN "Up to 2003/03", GR/BL "After 2003/03"; 19 "F_DFAHL, Wheel Speed, Rear Left, ASC (A52-12) or DSC (A65-4)"; 20 "BRFN, Brake Fluid Level Sensor"; 21 "AWS, Airbag Warning LED"; 22 "ABS Warning Light"; 23 "FSB, Parking Brake Switch"; 24 "BBV+, Signal, Brake Wear Sensor"; 25 "D_TXD1, Diag Signal TXD" WS/VI; 26 "KFN, Coolant Level Sensor". White plug: 1/2 outside temperature, 4 washer level, 5 "S_FGRL, Signal, Cruise Control Active (M43 only)", 7 "S_RS+, Reverse (Manual Transmission Only)", 13 BC stalk button, 14 gong — [bmwgm5.com: E46 IKE Connections](https://www.bmwgm5.com/E46_IKE_Connections.htm) [read; hobby site, sources not stated, so treat as a transcription].
- Independent bench pinout from a cluster-driving project: X11175 "1, 20, 24, 26 Ground", "4, 5, 6, 7 +12V (pin 7 also feeds the backlight on older IKE clusters)", "9 CAN H", "10 CAN L", "11, 12 Fuel simulation pair A", "15, 16 Fuel simulation pair B", "14 … K-bus (lights, symbols, backlight)", "19 … speed sensor simulation", "22 … ABS light", "23 … parking brake light". White pin 4 is grounded "to clear the washer fluid light" — [r00li/CarCluster: README_WIRING_BMW_E46](https://github.com/r00li/CarCluster/blob/main/Misc/README_WIRING_BMW_E46.md) [read via fetch summary]. The grounds on 20/24/26 confirm that the fluid, pad-wear and coolant-level inputs read "OK" when grounded.
- M3 harness, BMW ISTA as quoted by George Hill (Oct 2020): "F34 -> X11175 pin #5 KOMBI (GN/BL); X11175 Pin #13 KOMBI -> X60004 Pin#11 DME (BR/GN); X60003 Pin #26 DME -> X6231 Oil Pressure switch (BR/GN)". On a ZHP (MS45.1): "X11175 Pin #13 KOMBI -> X6011 #3 (BR/GN)" — [NAM3 61405](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off) [read].
- WDS copy, MSS54 X60004: pin 1 "A | Signal, terminal 61 | Control module for instrument cluster"; pin 2 "E | Engine start signal feedback | Connector Voltage signal, terminal 30h"; pin 6 "A | Signal, terminal 50, ignition lock | Control module for instrument cluster"; pin 11 "A | Signal Oil pressure | Control module for instrument cluster"; pin 21 "A | Signal Oil level | Control module for instrument cluster". X60003: pin 13 "Signal, terminal 61 | Generator", 26 "Signal Oil pressure switch", 39 "Signal Oil level sensor". On the MS43 and MS45 tabs pins 1, 6, 11 and 21 are "Not used" — [community WDS pinout workbook, XLSX export](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing) [read].
- The guide's previous conflict is resolved: Kassel's chart says "Pin 11 (Oil Pressures Signal) to Pin 14 of cluster" ([Kassel chart](https://www.kasselperformance.com/wp-content/uploads/2016/01/E46S54Wiring.png), read by the earlier researcher), but pin 14 is the K-bus in both pinouts above [read].

**Which lamps are hard-wired and which come over CAN**
- BMW, E46 launch training: "SIGNALS WHICH ARRIVE AT THE INSTRUMENT CLUSTER THROUGH THE CAN-BUS: engine speed; fuel consumption; coolant temperature (DME/DDE); selector lever position, gear program, transmission malfunction display (AGS); ASC indicator lamp (ASC); Check-Engine (DME/DDE); FGR indicator lamp - cruise (DME/DDE); EBV indicator lamp (ASC)". Going out: "outdoor temperature → IHKA", "fuel tank level → DME", "VIN → LWS". K-bus inputs include doors and trunk lid (basic module), light faults (LSZ), "DME-S-AC, air condit. Switch" and "DME-LSZ-KK, load torque air conditioning" (IHKR), and "transfer, km reading" (LSZ) — [BMW ST034 E46 Driver Information (part 1)](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf) [read].
- Same document, hard-wired inputs: "DISTANCE SIGNAL - This input is supplied to the cluster by the ABS/ASC+T control module as a square wave signal. Pulses from the left rear wheel speed sensor…"; "OIL TEMPERATURE [sic] - This input is a pulse width modulated signal from the Electronic Oil Level Sensor … the instrument cluster will illuminate the Oil Warning indicator LED in yellow"; "FUEL TANK LEVEL - Two lever action sensors are wired in parallel to the cluster"; "BRAKE PAD WEAR SENSORS"; "The normal ignition switch terminals (KL R, KL 15 & KL 50) are input to the cluster" [read].
- BMW 12/2004 version, "E46 Cluster Overview" figure (drawn for an MS42 car): hard-wired inputs KL R/15/50, fuel level sensor 1 and sensor 2, coolant level, ambient temperature, SI reset, panel button, photo-transistor, BC stalk, KL 58g from LSZ, brake pad wear, vehicle speed from ABS, "AIRBAG (MRS II)", "CHARGING (FROM ALTERNATOR)", "ENGINE OIL PRESSURE", "GR II (Cruise Control) ON", "PARKING BRAKE ON", "BRAKE FLUID LEVEL"; outputs "LOW FUEL" to the DME, speed signal "A", gong, D-bus. Text: "The brake pad circuit is monitored for an open or interruption of the ground" — [BMW ST052 03b E46 Driver Information Systems](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03b_E46%20Driver%20Information%20Systems.pdf) [read; figure read as image].
- BMW, E46 DSC: "The DSC and yellow ABL lamp are controlled by the DSC III control unit via the CAN bus. The ABS lamp is controlled directly by the DSC III control unit via hardwire." The red brake lamp means "low brake fluid or hand brake engaged". The I-P-O chart shows the brake-fluid level switch and the park-brake switch with a "SPLICE TO KOMBI" — [BMW ST056 E46 DSC (01/2003)](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) [read].
- BMW 2002 update: "The tire defect indicator (RPA, RDW, DDC) will be integrated into the DSC control unit. The warning lamps in the instrument cluster will be activated by the DSC control unit via the CAN Bus and not by a separate wire" — [BMW ST043 2002 E46 Update](https://archive.org/download/BMWTechnicalTrainingDocuments/ST043%202002%20System%20Diagnosis/8%20E46%20Update.pdf) [read].
- BMW M3: "The MS S54 engine control system monitors the engine oil temperature and signals the instrument cluster over the CAN line for operation of the oil temperature gauge and illumination of the LEDs" — [BMW ST041 M3 Complete Vehicle](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf) [read].
- Cluster SGBD (KOMBI46 for "KOMBI E46", KOMBI46R for "KOMBI E46 Redesign"; the latter's FA jobs cover coding indices below 7, 7–19, 20–22 and above 22, so M3 clusters too). `STATUS_IO_LESEN` returns `STAT_HANDBREMSE_EIN`, `STAT_OELDRUCK_EIN`, `STAT_KL50_EIN`, `STAT_BREMSFLUESSIGKEIT_EIN`, `STAT_KUEHLMITTELSTAND_EIN`, `STAT_KL15_EIN`, `STAT_KLR_EIN`. `STATUS_CAN_SIGNALE_LESEN` returns `STAT_LAMPE_EBV_EIN`, `STAT_LAMPE_ASC_EIN`, `STAT_LAMPE_CHECK_ENGINE_EIN`, `STAT_LAMPE_TEMPOMAT_EIN`, `STAT_LAMPE_UEBERTEMPERATUR_EIN`, `STAT_DREHZAHLSTUFE_ELUEFTER_WERT` and the mileage. `STATUS_TOENS_IO/SG` reads the thermal oil-level sensor — [SGBD KOMBI46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46.md), [SGBD KOMBI46R](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46R.md) [read].

**Oil-pressure and charge lamps with an MSS54, and the CAN coding options**
- George Hill (Oct 2020): "The oil pressure switch closes at .5bar so anything under that and the light should be on. The alternator light is powered through the cluster and grounded by the DME whenever the alternator is not charging." nextelbuddy's coding-index-24 M3 cluster had "alternator over can bus enabled oil level over can bus enabled but oil pressure over can bus not enabled". With the CSL software "which wasn't originally programmed to handle Alternator via canbus" the lamp misbehaved, whereas "stock MSS54HP software … does support alternator via canbus". The lamp worked once X60004-11 was wired to cluster pin 13 — [NAM3 61405](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off) [read].
- Coding names: "The options that define functions GENERATOR_UEBER_CAN, TOG_UEBER_CAN and CAN_OELDRUCKSCHALTER parameters suggest when particular information goes to the cluster via CAN or via dedicated wire" — [e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/) [snippet]. A 2002 M3 owner's NCS list includes "CAN_OELDRUCKSCHALTER — Oil pressure switch on CAN bus — nicht_aktiv" and "GENERATOR_UEBER_CAN — Generator over CAN — nicht_aktiv". These sit in its "Miscellaneous options – not yet processed or from other cars" section, so their module and default aren't certain — [NikolaiD, 2002 E46 M3 convertible NCS list (2011)](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf) [read].
- Vendor evidence that a non-M E46 cluster can take these lamps over CAN: MaxxECU's E46 330i (MS43) CAN profile drives the tachometer, check-engine, coolant temperature, overheat, consumption, "Oil temperature … only on M3 dash", "Shift light RPM … only on M3 dash", "Oil pressure light", "Cruise control light" and "Charge/alternator light controlled by battery and RPM". The "Low oil level light (yellow) is always off" — [MaxxECU: BMW E46 330i (MS 42/43)](https://www.maxxecu.com/webhelp/can-oem_bmw_e46_330i_ms43.html) [read; vendor page].

**Mileage handover (supports the guide's virgin-EEPROM plan)**
- BMW: "1. If the vehicle ID number is not the same in both modules, the manipulation dot is illuminated… 2. Data will only be transferred from the LSZ to the cluster if the ID numbers match and the cluster mileage is zero. 3. The VIN is entered in the cluster through coding and will only be accepted when the cluster mileage is zero. 4. The stored mileage in the LSZ can only be overwritten by a higher mileage. 5. If the two mileage values stored vary by more than 120, and the VINs are the same, the cluster will continue to accumulate mileage and a fault will be stored…" Also: "If either the Cluster or LSZ has to be replaced, the data is taken from the remaining module … This can only occur ONCE the VIN has been entered into the replacement unit" — [BMW ST034 Driver Information](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf) [read].
- Odometer scaling is coded in the cluster: `K_ZAHL_WEG` "K-number for distance calculation 4797_imp/km / 4912_imp/km", `K_ZAHL_TACHO` 4846/4961 imp/km. The same M3 list shows `TANK_KENNLINIE`, `DREHZAHL_KENNLINIE kennlinie_03`, `SIA_LITER_GRENZE` s54b32 variants and `RDKS aktiv` — [NikolaiD M3 NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf) [read].

### Inferences
- **Inference: oil pressure with an MSS54.** The M3 routes the switch through the DME: switch (B6231/X6231) → X60003-26 → DME → X60004-11 → X11175-13, BR/GN throughout. Whether the DME passes the switch through or drives the output from logic isn't shown. The MSS54 fault list (Q3) has no oil-pressure-switch fault, which suggests a simple pass-through-type output. Either way the cluster sees the same lamp-to-ground behaviour, and the switch closes at about 0.5 bar.
- **Inference: charge lamp.** It is X11175-2, a lamp fed by the cluster. In the M3 the DME grounds it through X60004-1 after reading the alternator's terminal 61 on X60003-13. In the 325i the alternator side grounds it directly through the engine-to-body plug (X6011 pin 4 per the forum mapping, unconfirmed).
- **Inference: oil level.** On a non-M car built to 03/2003 the cluster processes the thermal oil-level sensor's PWM itself (BMW text, `STATUS_TOENS` jobs). In an M3 the sensor goes to the DME (X60003-39) and the DME repeats the signal to cluster pin 17 (X60004-21), or sends it over CAN if `TOG_UEBER_CAN` is active. The wire-colour change "after 2003/03" fits the MS45-era cars moving the sensor to the DME.
- **Inference: coding.** Wire all three (X60004-1 → 2, 11 → 13, 21 → 17) and set the M3 cluster's three over-CAN parameters to `nicht_aktiv`. This doesn't depend on which MSS54 software sends what over CAN (stock MSS54HP sends the alternator status; CSL software originally did not).
- **Inference: KL50.** MSS54 X60004-6 ("terminal 50 → cluster") most likely lands on cluster pin 3. On the 325i that pin gets the start signal from the body side (X6011 pin 6 per the forum mapping). The car starts without it.
- **Inference: odometer.** The M3 cluster's `K_ZAHL_WEG` is set for M3 tyres. With the M3 wheels and tyres it accrues true distance. With other rolling circumferences, check the odometer against a GPS-measured distance and correct only the tyre factor through coding, never the stored mileage.

### Gaps
- The bmwgm5 pinout is an unattributed transcription. Its pin 13 note "(A6000-11)" implies a DME-routed oil-pressure lamp, which doesn't match MS43 cars, so it may mix in a later or M3 diagram.
- No BMW M3-specific X11175/X11176 table was readable (newTIS blocked). The M3 assignments rest on ISTA quotes, the WDS copy and owner fixes.
- The module and default values of `CAN_OELDRUCKSCHALTER` and `GENERATOR_UEBER_CAN` (cluster? which index?) aren't confirmed; `TOG_UEBER_CAN` was seen only in a snippet.
- How the Touring's rear-door, tailgate and rear-window warnings show on an M3 cluster is undocumented beyond "M3 clusters have no rear-door LEDs".

---

## Q2. Fuel gauge: Touring senders versus what the M3 cluster expects

### Cited findings
- BMW: "Two lever action sensors are wired in parallel to the cluster. The two varying voltage signals are processed by the cluster for fuel gauge and low fuel warning display." Cluster test 06: "6.0 = Fuel level averaged • LH sensor input = 23.7 liters • RH sensor Input = 41.5 liters; 6.1 = Total tank level averaged = 65.2 liters; 6.2 = Indicated value and tank phase • 1 = both sensors OK • 2 = one sensor fault • 3 = implausible input" — [BMW ST034 Driver Information](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf) [read]. (The pinout below shows two separate sender pairs, so "in parallel" means two inputs, not one joined circuit.)
- Sender pins: X11175-11 "TANK1+ Fuel Level Right Tank (B6-1)" SW/RT/WS, 12 "TANK1– … (B6-2) Ground" BR/SW/WS, 15 "TANK2+ Fuel Level Left Tank (M2-6)" SW/RT/GE, 16 "TANK2– … (M2-4) Ground" BR/SW/GE. Resistances: "Fuel level sensor left tank: empty about 70 Ohms, full about 310 Ohms. Fuel level sensor right tank: empty about 70 Ohms, full about 395 Ohms" — [bmwgm5: E46 IKE Connections](https://www.bmwgm5.com/E46_IKE_Connections.htm), [bmwgm5: E46 Fuel Level](https://www.bmwgm5.com/E46_Fuel_Level.htm) [read; hobby site, single source, unverified].
- Cluster SGBD: `STATUS_ANALOG_LESEN` → `STAT_HEBELGEBER1_WERT`, `STAT_HEBELGEBER2_WERT` (ADC values of the two lever senders); `STATUS_TANKINHALT_LESEN` → `STAT_TANKINHALT_HEBEL1_WERT`, `…HEBEL2_WERT`, total, and in KOMBI46R filtered and unfiltered totals plus `STAT_RESERVE`. KOMBI46R also has `STATUS_AIF_TANKDATEN_LESEN` — [SGBD KOMBI46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46.md), [KOMBI46R](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46R.md) [read].
- M3 cluster coding: "TANK_KENNLINIE — Tank capacity calibration — 60_l_literskala / dad_tank_diesel / metalltank"; also `TANK_SCHWELLE_RESERVE 8_l`, `TANK_SCHWELLE_AUF/AB 6_l`, `TANK_BERUHIGUNGSZEIT 10_sec`, `TANK_MITTLUNGSZEIT 5_sec`, `TANK_ADC_FEHLER_OG/UG`, `TANK_FILTER_*` — [NikolaiD 2002 M3 NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf) [read]. KamilFKH's gauge thread: "two functions in coding data available - TANK_SCHWELLE_RESERVE and TANK_KENNLINIE, then there is TNK_KENNLINIE in the producer area of EEPROM", with the tank gauge "unresolved yet for the first groups of clusters" — [e46fanatics: DIY E46 cluster gauges definitions](https://www.e46fanatics.com/threads/diy-e46-cluster-gauges-definitions.1324535/) [snippet].
- Capacity: BMW lists the E46 M3 "Fuel Tank Capacity 63 L" and says "The baffling has been modified for the E46 M3 fuel pump pickup in the right hand side of the fuel tank" — [BMW ST041 M3 Complete Vehicle](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf), [BMW ST041 Engine Electronics part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf) [read]. The 2004 325i (Sport Wagon) has a 16.6 gal (62.8 L) tank — [Autopadre](https://www.autopadre.com/vehicle-dimensions/bmw-325i/2004--11872), [The Auto Channel 2003 review](https://theautochannel.com/news/2003/01/16/152896.html) [snippet; aggregators].
- ETK (USA): the 325i Touring has the plastic tank with left sensor 16116766940, right "Delivery unit" 16146766942 and left fuel-level sensor 16116768788. The M3 has 16112229736 (tank), 16142229684 (right delivery unit), 16142229683 (left sensor) and a "Fuel baffle fixture" 16112229656. The non-M left sensor 16116768788 is used across non-M E46s; the M3 tank and left sensor are M3/CSL-only. Both use the same 2-pole sender plug housing 61138352390 — [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/), [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/), [16116768788](https://bmwfans.info/parts-catalog/16116768788/), [16142229683](https://bmwfans.info/parts-catalog/16142229683/) [read].
- The DME uses the cluster's tank reading: the MSS54 SGBD lists the environment value "Tankfuelstand (CAN)" in litres and faults "KAT-Schutz aktiv bei leerem Tank" and "Fehler bei leerem Tank" — [SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md) [read]. BMW's DM-TL test needs 15–85 % fuel (already in the guide, from ST041).

### Inferences
- **Inference: the M3 cluster should read a plastic-tank Touring correctly.** `TANK_KENNLINIE` offers only a 60-litre scale, a diesel tank and a metal tank. Neither the M3 nor the M54 Touring has a diesel or metal tank, so both should use `60_l_literskala`, and the two tanks are within a litre of each other. The M3-specific sender and tank part numbers follow the M3's pickup baffling. Whether their resistance curve differs is unproven.
- **Inference: three real cases.** (a) Touring tank with Touring senders: probably correct as coded. (b) Touring tank with the M3 pump unit (it carries the right sender) and the Touring's left sender: the senders are mixed, so check each side's litres in Tool32. (c) The whole M3 tank: matches the M3 cluster. A Touring that started as an **M56 SULEV car with its metal tank** would need `TANK_KENNLINIE = metalltank`.
- **Inference: why accuracy matters beyond the gauge.** The DME takes the tank level over CAN for low-fuel misfire suppression, the DM-TL enable window and the "Check Filler Cap" logic (BMW ST043: the lamp lights "if change in fuel volume as read by the fuel level sensors precedes a failed Evap System test"). A biased gauge can delay EVAP readiness.
- **Check.** Start near empty and add measured amounts. At each step compare Tool32 `STATUS_TANKINHALT_LESEN` (left, right, total) and the cluster's hidden test 06 with the pumped volume. Test phase 3 ("implausible") or one side stuck means a sender, a plug (pins 11/12 or 15/16) or the coding.

### Gaps
- No second source for the sender resistances; no M3 sender resistances at all.
- The actual `TANK_KENNLINIE` value on a US M3 and on a US 325iT wasn't read from a real car.
- No first-hand report of an M3 cluster with Touring senders.

---

## Q3. CAN, D-bus and the diagnosis socket

### Cited findings

**Topology**
- BMW: "In the E46, the instrument cluster acts as a gateway between the D-Bus, CAN bus and K-Bus. For example, in order to read out fault codes from the LSZ, the instrument cluster provides the gateway between the K-Bus and D-bus." And: "The CAN network on the E46 uses a twisted pair configuration which also uses two terminal resistors of 120 ohms each for a total circuit resistance of 60 ohms." The M-bus is for climate stepper motors (four on the E46); LIN was added from 2003 for AHL and mirrors ("a single yellow/violet (GE/VI) wire") — [BMW ST052 03a E46 Power Supply and Bus Systems (12/04)](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03a_E46%20Power%20Supply%20and%20Bus%20Systems.pdf) [read].
- BMW bus chart "E46 up to 2006": CAN between IKE (cluster), DME, AGS and ABS/ASC5. Separate lines: "ISN" (EWS III → DME) and "GR II Cruise Control Interface" (MFL → DME). The D-bus to the cluster, DME, AGS, ABS/ASC, LWS and MRS II goes to the OBD II and 20-pin sockets. The K-bus joins the cluster, MRS III, IHKA, SM, GM V, PDC, AIC, EWS III, LSZ, MFL, SHD, C23 BM, CVM and telephone — [BMW ST401b 3 Series Bus Charts](https://archive.org/download/BMWTechnicalTrainingDocuments/ST401b%20Bus%20System%20Overview%20-%20All%20Models/02_3%20Series%20Bus%20Charts.pdf) [read, image].
- BMW M3 bus chart: CAN = instrument cluster, DME, "LWS 5", DSC. MFL (with "RADIO" and "GR" outputs) has a separate line to the DME. The D-bus serves the cluster, DME, LWS 5 and DSC, and an "OBD II" line runs to the DME — [BMW ST041 M3 Complete Vehicle](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf) [read, image].
- BMW figure of an E46-type CAN: "GS 20 — MS 43.0 — INSTRUMENT CLUSTER", with "SPLICE CONNECTIONS FOR TWISTED PAIR CAN" feeding "LEW" (steering-angle sensor) and "MK 60". Text: "CAN-Low GE/BR and CAN-High GE/SW or GE/RT"; "A 120 Ohm resistor is installed in two control units of the CAN between CAN-H and CAN-L … the effective resistance of the complete circuit is 60 Ohms. On some vehicles there is a jumper wire that connects the two parallel branches together, others have an internal connection at the instrument cluster"; "The terminal resistors are located in the ASC/DSC control unit and either the instrument cluster or in the DME"; "Modules which do not have the terminal resistor can be checked by disconnecting the module and checking the resistance directly between the pins for CAN-H and CAN-L. The value at these control units should be between 10kOhms and 50kOhms". CAN voltage averages 2.5 V per line (the meter shows 2.35–2.65 V) — [BMW ST040 Bus System Troubleshooting (2/01)](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/9%20Bus%20System%20Troubleshooting.pdf) [read; figure read as image]. The same text, verbatim, is in [BMW ST051 Introduction to Bus Systems](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/10%20Introduction%20to%20Bus%20Systems.pdf) [read].
- MK60 CAN partners: "The MK60 is connected to the CAN bus for communication with the AGS, DME control module, Steering Angle Sensor and the Instrument Cluster"; "All four wheels speed signals are sent over the CAN bus". The steering-angle sensor (LEW) plug: "Pin 1. KL 30, Pin 2. KL 87, Pin 3. CAN high, Pin 4. CAN low, Pin 5. KL 31, Pin 6. TXD" (captioned "CAN BUS CONNECTOR (5 WIRES)"). MY2002 MK60: the yaw/lateral "sensor cluster … is operated at 5 volts and has a separate CAN connection to the control unit" — [BMW ST056 E46 DSC](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) [read].
- WDS copy: DME X60004-36/37 "Signal CAN bus high/low → Connector, CAN bus" on MSS54, MS43 and MS45; the MS45 also has a local CAN on 31/35 — [WDS pinout workbook](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing) [read]. TIS-derived MK60 pinout: CAN-high pin 11 (yellow/red), CAN-low pin 15 (yellow/brown), twisted — [heinzboehmer's MK20→MK60 mapping (2022), NAM3 attachment](https://nam3forum.com/forums/filedata/fetch?id=189181) [read].
- The DME watches the bus partners. MSS54 fault locations include 0x56 "CAN-Bus DME", 0x84 "Timeout DSC-Botschaft", 0x85 "Timeout LWS-Botschaft", 0x86 "Timeout KOMBI-Botschaft", 0x06 "Timeout SMG-CAN", 0x7B "Bus-Off lokaler SMG-CAN" and 0xDE "CAN-Timeout ZSG" — [SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md) [read]. The MS45 SGBD logs missing cluster messages ("Botschaft (I-Kombi 2) … fehlt") — [SGBD MS450DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MS450DS0.md) [read].
- Termination evidence specific to the E46: "one of the resistors is in the gauge cluster" — [Beyond.ca: E46 gauge cluster](https://forums.beyond.ca/threads/418337-E46-gauge-cluster) [snippet]. In a MegaSquirt build driving an E46 cluster, "there should be only 2 120-ohm termination resistors on the entire bus" and removing the MS3's own resistor "brought the bus reading to about 60 ohms" — [MSExtra: BMW E46 Cluster Canbus](https://www.msextra.com/forums/viewtopic.php?t=76069) [snippet].
- Measuring method (German E46 forum): about 60 Ω between low and high with the ignition off; split the bus and measure each direction for 120 Ω; some control units may switch their terminator in only at terminal 15 — [motor-talk E46 forum](https://www.motor-talk.de/forum/can-bus-zu-hohe-spannung-t1117913.html) [read].

**Diagnosis socket**
- BMW, 2001 changes: "20 PIN DIAGNOSTIC SOCKET DELETION — Model: E39, E46, E52, E53 — Production Date: E46 from 6/00 … Previously before 2001, only emissions relevant data could be extracted from the OBD II connector because it did not provide access to TXD (D-bus). The TXD line is connected to pin 8 of the OBD II connector on vehicles without the 20 pin diagnostic connector. The cap to the OBD II connector contains a bridge that links KL 30 to TXD and TXD II. … The OBD II connector is located in the drivers footwell to the left of the steering column" — [BMW ST040 2001 Changes](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/1%202001%20Changes.pdf) [read].
- BMW: "TXD II (pin 17) was introduced as a separate communication line exclusive to DME (ECM), AGS (TCM) and EML. TXD II is technically identical to the D bus (TXD). On vehicles that use only the 16 pin OBD connector in the vehicle, TXD is installed in pin 8. TXD II remains in pin 7." The D-bus is "directly wired to: ASC/DSC, EDC (if equipped), LEW, IKE/KOMBI", "a single WS/VI wire", and needs more than 2.0 V — [BMW ST040 Bus System Troubleshooting](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/9%20Bus%20System%20Troubleshooting.pdf) [read]. BMW's ST052 version says TXD II "is connected only to pin 17 of the OBD II connector and the ECM", but its own figure shows pin 7 on the 16-pin socket and pin 17 on the 20-pin; pin 17 belongs to the 20-pin socket [read].
- No CAN at the socket: "CAN is used in most E46's if not all of them, but, it doesn't connect to the OBDII connector! The OBDII connects to the instrument cluster which acts as a gateway" — [e46fanatics: OBD2 pinout](https://www.e46fanatics.com/threads/obd2-pinout.788026/) [snippet]. Vendor: "OBDII works only when CAN wired to OBDII connector (requires JMTII terminals)", i.e. an E46 socket has no terminals at the CAN positions — [MaxxECU E46 page](https://www.maxxecu.com/webhelp/can-oem_bmw_e46_330i_ms43.html) [read].
- Why cables bridge 7 and 8: "Older BMWs (like E39, E46) have the DME, EGS, and SMG on pin 7, while all other modules are on pin 8 … soldering together the circuit board pads for pins 7 and 8 will put it in the older configuration" — Bali's install thread, already in `coding_body_chassis.md` [read by the earlier researcher].

### Inferences
- **Inference: node list for the Touring after the swap.** PT-CAN: MSS54 (X60004-36/37), M3 cluster (X11175-9/10), the Touring's MK60 or an M3 MK60 (pins 11/15) and the steering-angle sensor (pins 3/4). There is no EGS on a manual. A Touring that was born automatic keeps an EGS stub in the harness, which should be cut back and insulated or left unplugged with nothing attached. The MK60 sensor cluster sits on its own CAN. The donor's SMG local CAN is not used.
- **Inference: terminators.** BMW's wording plus the cluster snippet point to **DSC unit + cluster** on the E46, not the DME. That would also explain the MSExtra reading (stock DME removed, MS3 terminator added gave too low a value). It isn't proven. Because the swap replaces the DME, and possibly the cluster and DSC with M3 units, measure rather than assume.
- **Check (battery disconnected, all modules plugged in):** about 60 Ω between CAN-H and CAN-L. About 120 Ω means one terminator is missing. About 40 Ω means three (a third terminating module). Unplug one module at a time: the reading jumps to about 120 Ω when a terminating module is unplugged and stays at 60 Ω for a non-terminating one. A disconnected non-terminating module shows 10–50 kΩ across its own CAN pins. There are no CAN pins at the E46 socket, so back-probe X11175-9/10 at the cluster, X60004-36/37 at the DME or pins 3/4 at the steering-angle sensor. Key on: each line about 2.5 V to ground.
- **Inference: why bridging 7 and 8 is safe.** BMW says TXD II and TXD are electrically identical K-lines, and BMW's own socket cap bridges both to KL30 when no tester is fitted. A single-K-line cable needs the bridge to reach the cluster gateway (pin 8) as well as the DME (pin 7).

### Gaps
- No BMW E46-specific statement of which two modules hold the 120 Ω resistors (the TIS functional description is on blocked newTIS).
- MK20 (M3 to 09/2002) CAN pins are known only through the MK20→MK60 mapping (MK20 pins 16 L / 17 H); GS20 CAN pins not researched (not needed for a manual).
- The E46 assignment of OBD socket pin 1 (BMW DIS shows KL15 on pin 1 in a generic E38–E53 bus-test screen) and pin 9 (TD engine-speed output from X60004-17?) is not confirmed for the E46.

---

## Q4. Climate control and cooling: A/C request and clutch, pressure sensor, fan stages, auxiliary water pump

### Cited findings
- BMW E46 IHKR (print 10/30/00, "Model: E46 (325i/it/Ci/Cic, M3) — Production Date: From 9/00"): "The 325i/it/Ci/Cic and M3 will be fitted with IHKR as standard equipment. The IHKA system will be available as an option on these models." Components include a "Refrigerant circuit pressure sensor", "Compressor relay (DME controlled)" and "Auxiliary fan (DME controlled)". K-bus signals: "Vehicle speed, Engine speed, Coolant temperature, Outside temperature, Terminal 15, 61, 50, 58G (panel lighting), Compressor load, Diagnosis and coding, Compressor request". "The IHKR control module sends the following signals to the DME over the K-bus-Kombi-CAN -bus connection: IHKR on stand-by (signal AC); Request for A/C activation (signal KO); Calculated compressor load; Request for auxiliary fan." The pressure sensor sits "on the high side line next to the receiver dryer" and "provides a voltage input signal (0-5 volts) to the IHKR". "Once all of the criteria for compressor operation have been met, the DME control module will activate the compressor relay to energize the compressor magnetic clutch. Control of the evaporator temperature is carried out by the IHKR signalling the DME to shut off the compressor when the evaporator reaches the freezing point." Connectors: X608 6-pin, X610 18-pin, X613 3-pin M-bus, X18341 6-pin — [BMW ST040 E46 IHKR](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/2%20e46%20ihkr.pdf) [read].
- BMW E46 IHKA: "Control of the A/C compressor is a function of the MS42.0 engine control module which also regulates auxiliary fan operation … The IHKA control module sends the following signals to the MS42.0 over the K-Bus and CAN Bus via the instrument cluster: Request for A/C activation (signal KO); Load torque for switching the compressor on; Requested auxiliary fan speed." The load torque is "0 to 30 Nm with a variable displacement compressor". Compressor "cut out … 4-10 seconds when the full throttle signal is present and vehicle speed is less than 10 mph". Fan: PWM 10–100 Hz to the motor's output stage; at the 120 °C overheat lamp the fan runs "in the overrun function … at a frequency of 10 Hz"; "Each fan stage that is determined is transmitted from the ECM to the auxiliary fan output stage. Prerequisite is a speed less than 50 mph." The pressure-to-stage table runs from 8 bar = stage 0 to >24 bar = stage 15 (table F2 below) — [BMW ST054 IHKA E46](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/12%20IHKA%20E46.pdf) [read; table read as image].
- BMW: "On the 99 MY (E38/39/46), the A/C on signal is transmitted via the K-Bus/CAN-Bus … On E46/36 models, the A/C compressor relay is activated by the ECM." Generic: "All models except E36/46 use an electrically powered auxiliary coolant pump … The IHKA control module operates the pump directly (E31 uses a relay) by supplying the ground circuit" (E38 example) — [BMW ST054 Output](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/16%20Output.pdf) [read]. As the next items show, this "except E46" is outdated for the M3, diesels and four-cylinders.
- BMW MS42/MS43: the same IHKR → K-bus → cluster → CAN → ECM request; "the ECM will activate a ground circuit to the compressor relay". The electric fan's output stage "receives power from a 50 amp fuse (E46 - located in glove box above the fuse bracket)". The PWM depends on coolant outlet temperature, calculated catalyst temperature, vehicle speed, battery voltage and "Air Conditioning pressure (calculated by IHKA and sent via the K-Bus to the ECM)". "At 10% (sensing ratio) the fan runs at 1/3 speed. At a sensing ratio of between 90-95% the fan is running at maximum speed. Below 10% or above 95% the fan is stationary." — [BMW ST055 MS42/MS43](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/3%20MS42%20MS43.pdf) [read].
- BMW MSS54: the same fan logic ("remote power output final stage (mounted on the fan housing) … 50 amp fuse … pulse width modulated signal"), including "Air Conditioning refrigerant pressure (calculated by IHKA and sent via the K-Bus to the ECM)"; "A/C on request from the climate control system (arming the ECM)" — [BMW ST041 Engine Electronics part 3](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf), [part 1](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%201%29.pdf) [read]. The MSS54 SGBD has `STAT_AC_EIN` / `STAT_KO_EIN` (A/C request and compressor), `STAT_ELU_EIN` (fan), jobs `STEUERN_KO` and `STEUERN_E_LUEFTER`, faults 0x30 "Klimakompressorrelais", 0x35 "Elektroluefter" and 0x8F "E-Box-Luefter", and `STAT_KKOS_ST_VERBAUT_WERT` "Klimaanlage erkannt" in the adaptation block — [SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md) [read].
- Climate-module SGBDs: IHKR46 ("Integrierte Heiz- Klimaregelung E46") reads `STAT_DRUCKSENSOR_WERT` in bar, the heat-exchanger and evaporator sensors and the pots. Its `STATUS_IO` returns `STAT_WASSERVENTIL_EIN`, `STAT_ZUSATZWASSERPUMPE_EIN`, `STAT_RELAIS_HECKSCHEIBE_EIN` and `STAT_KLIMABEREITSCHAFT_EIN`, and there is a job `STEUERN_ZUSATZWASSERPUMPE` (on/off). IHKA46 has the same pump job and status — [SGBD IHKR46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKR46.md), [IHKA46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKA46.md) [read]. A 2002 M3's IHK coding includes "ZUSATZWASSERPUMPE — Auxilary water pump — aktiv / nicht_aktiv" and `ZYLINDER_ZAHL 6_zylinder` — [NikolaiD M3 NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf) [read].
- ETK: the US M3 uses "Water valve with additional water pump" 64118369807 (970 g); the US 325i Touring uses "Water valve" 64118369805 (415 g) — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/water_hoses_water_valve/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/water_hoses_water_valve/) [read]. 64118369807 is also listed for E46 four-cylinder petrol and diesel models — [ETK 64118369807](https://bmwfans.info/parts-catalog/64118369807/) [read].
- NAM3 (April 2020): "1. P/N 64118369807 - found on all North American E46 M3s and S54 powered Z3Ms - heater valve w/attached auxiliary pump; 2. P/N 64118369805 - found on E46 M3 CSL, non-M E46 3-series, and X3 - heater valve only; 3. P/N 64118369806 - … auxiliary pump only, no heater valve". Owners run the non-M/CSL valve on M3s: "No notable difference", some after coding the climate module. repoman89: "One wire ends pin 6 on the plug on the back of the heating controls" (newTIS links for the e46-m3-cou water valve and auxiliary water pump) and "The other makes its way to fuse 62 in the glovebox, but so does the water valve wire". nextelbuddy (edited 04-14-2021): "the hvac module in the m3 specifically is coded for the aux water pump and will display an error code in the hvac module itself of the aux water pump is not present" — [NAM3 14592](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/14592-deleting-auxiliary-water-pump) [read].
- First-hand swap notes: UNRIVALED said the extra two-wire pump needs wiring "inside the cabin to the hvac module" and his system was hard to bleed without it; Tenza found two plugs on the S54 heater valve where his body harness had one (see `youtube_swap_wiring_coding.md`, read by the earlier researcher).

### Inferences
- **Inference: IHKR with the MSS54 will work** in the same way as IHKA. BMW documents the identical K-bus → cluster → CAN request for both panels and a DME-driven K19 for the E46, and lists IHKR as standard on the M3 itself. No swapper has confirmed IHKR + MSS54 first-hand. Whether any US M3 actually shipped with IHKR is unconfirmed (listings and the M3 training text show IHKA). Test it early: Tool32 MSS54 `STATUS_DIGITAL`, where `STAT_AC_EIN` should follow the snowflake button and `STAT_KO_EIN` the compressor, plus IHKR `STATUS_ANALOGEINGAENGE` for the pressure in bar.
- **Inference: the M3 cluster is now in the A/C path.** The request, load and fan stage cross the cluster gateway, so an M3 cluster that isn't talking on both K-bus and CAN gives no A/C and a slow fan. The same applies to the outside temperature that the IHKR uses.
- **Inference: auxiliary pump options.** (1) Simplest: fit the CSL/non-M valve 64118369805 on the S54, which needs no wiring or coding change to the Touring's IHKR/IHKA (it is coded for a valve only). Bleed the heater circuit carefully. (2) Keep the M3 valve with pump: run two wires, the pump supply from the same fuse as the water valve (F62 per the forum; the guide's aggregator list says F23 5 A, so check the fuse card) and the pump's switched side to the climate-module output (pin 6 of a heater-control plug on the M3; the Touring IHKR pin isn't known). Then set `ZUSATZWASSERPUMPE = aktiv` in the IHK coding and test with `STEUERN_ZUSATZWASSERPUMPE`. Per BMW the module switches the ground side.
- **Inference: fan.** No re-pin (X60004-4 on all three DMEs). Checks: MSS54 `STEUERN_E_LUEFTER`, cluster `STAT_DREHZAHLSTUFE_ELUEFTER_WERT`, and fan speed rising with A/C on at low road speed.

### Gaps
- IHKR/IHKA connector pin numbers for the pump output, compressor-request button and pressure sensor (newTIS blocked).
- Which fuse feeds the water valve and pump on a 325iT (F62 vs F23).
- Whether the S54's compressor/plug matches the Touring's lines is a mechanical question covered elsewhere.

---

## Q5. Crash fuel cut-off

### Cited findings
- BMW E46 Passive Safety: "The MRS III includes a fuel pump cut off feature in the event of an airbag deployment" and "FUEL PUMP SHUT-DOWN: The MRS III system is linked via the K-Bus/CAN Bus to the Engine Control Module for deactivation of the fuel pump. The MRS III will signal the DME over the K-Bus through the instrument cluster and CAN Bus to shut off the fuel pump in the event that any crash threshold is exceeded." "The MRS III system is installed in E38/E39 and E46 Sedan vehicles as of 9/99 production and in E46 Coupes as of 6/99 production." The battery safety terminal (BST) fires "in a frontal impact at threshold 2 or greater" and at the rear-impact threshold — [BMW ST034 Passive Safety Systems](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/7%20Passive%20Safety%20Systems.pdf) [read]. BMW 12/04: the BST disconnects the trunk-to-front B+ cable, but "the connection to the power distribution circuits will remain intact to allow other vehicle features to remain operational" — [BMW ST052 03a](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03a_E46%20Power%20Supply%20and%20Bus%20Systems.pdf) [read].
- BMW S54 (M3 and M roadster/coupe text): "The power to the fuel pump relay will be switched off in the event of an airbag activation. The MRS III control module will signal the Engine control module over K-bus and CAN bus for this purpose" — [BMW ST055 MS S54](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf) [read]. The M3 version: "The power to the fuel pump module will be switched off in the event of an airbag activation. The MRS III control module will signal the ECM over K-bus and CAN bus for this purpose" — [BMW ST041 Engine Electronics part 2](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf) [read].
- MSS54 SGBD: fault location 0x7E "EKP-Crash-Abschaltung" (fuel-pump crash shut-off) and DM-TL abort reason "53_ABBRUCH_EKP_CRASH_OFF". There is a separate fault 0x01 "Relais Kraftstoffpumpe" and jobs `STEUERN_EKP` / `STEUERN_EKP_AUS` ("Kraftstoffpumpe (Relais) ausschalten") — [SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md) [read]. The MS43 SGBD shows no crash-related fault — [SGBD MS430DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MS430DS0.md) [read].
- MRS3 SGBD: "KBUS — K-BUS-Anbindung → 1 / D-Bus-Anbindung → 0"; fault and info entries "Crashtelegrammspeicher" and "Crashtelegramm(e) gespeichert"; BST firing circuits "Zuendkreis ZK10/ZK15 → Batterie Pluspoltrennung 1/2" — [SGBD MRS3](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MRS3.md) [read].
- Other crash responses: the LSZ switches the hazard lights on "from the crash sensor input provided by the MRS control module" — [BMW ST034 Driver Information](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf) [read]; the ALSZ coding has `CRASH_WARNBLINKEN` and `CRASH_KLEMME_58G_EIN` — [NikolaiD M3 NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf) [read]. On M56 SULEV cars the pump control unit gets "crash information from the MRS" over the K-bus directly — [BMW ST047 E46 FL](https://archive.org/download/BMWTechnicalTrainingDocuments/ST047%202003%20System%20Diagnosis/5%20E46%20FL.pdf) [read].

### Inferences
- **Inference: on the Touring (MS43/MS45, K96 relay) the cut-off is a DME software action.** There is no airbag wire to K96. The crash telegram leaves the MRS III on the K-bus, crosses the cluster gateway to CAN, and the DME stops grounding the K96 coil (X60004-10).
- **Inference: with the MSS54 the path stays the same** (Touring MRS III → M3 cluster gateway → MSS54), and the MSS54 contains a crash shut-off. BMW's S54 wording ("fuel pump relay" in ST055, "module" in ST041) suggests the function cuts whichever pump output the software drives. It is **not documented** whether US MSS54 software, which drives the EKP module on X60002-11, also drops the "not USA" relay output on X60004-10 that this build uses for K96. Treat the crash cut-off as unverified.
- **Do not try to test it by firing anything.** Verify the path instead: INPA reaches the MRS (K-bus via the cluster) and the DME; the MSS54 stores no 0x86 "Timeout KOMBI-Botschaft"; the MRS shows no fault. Optional: fit the US M3 EKP module (the guide's "Optional: the M3 pump module") to get BMW's documented US arrangement back.
- The BST is a separate, pyrotechnic protection of the B+ cable and doesn't stop the pump by itself, because the distribution side stays live.

### Gaps
- No MSS54 software description of which outputs the crash function controls; no swapper has tested it, and it shouldn't be tested destructively.

---

## Q6. Cruise control, the clutch-switch module and the gear-recognition switch

### Cited findings
- BMW E46: "The K-Bus is used for data communication between the sound system/telephone controls. The cruise control has its own data link to the DME control module for cruise control operation" — [BMW ST034 Driver Information](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf) [read]. **Conflict:** BMW's 12/04 text says the cruise "accelerate" command "is sent to the DME via the gateway (cluster) to the CAN-Bus" — [BMW ST052 03b](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03b_E46%20Driver%20Information%20Systems.pdf) [read]. Both bus charts and the WDS pin tables show the dedicated line ("GR II Cruise Control Interface"; X60004-27 "Data link MFL ← Volute spring"), so the 12/04 sentence is taken as a simplification.
- BMW MS42/MS43: "Cruise control functions are activated directly by the multifunction steering wheel to the ECM. The individual buttons are digitally encoded in the MFL switch and is input to the ECM over a serial data wire … The clutch switch disengages cruise control to prevent over-rev during gear changes. The brake light switch and the brake light test switch are input to the ECM to disengage cruise control as well as fault recognition … The vehicle speed signal for normal engine operation is supplied from the DSC module (right rear wheel speed sensor). The road speed signal for cruise control … is an average taken from both front wheel speed sensors, supplied via the CAN bus." It also cites SI 12 17 99 on rev hang and "upgrade to a three wire switch including ECM reprogramming" (MS42) — [BMW ST055 MS42/MS43](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/3%20MS42%20MS43.pdf) [read].
- BMW MSS54: "All driver requested cruise control function requests are provided to the MS S54 from the MFL II control module in the steering wheel over a single FGR data lead." "Power Transmission Switch: The power transmission switch (circuit) consists of two switches in series. The circuit includes a clutch switch and a gear selector switch on the transmission. The functions of the power transmission switch are as follows: Cutout for cruise control operation; Enable condition for idle control. The switches provide a high signal for the MS S54 when the clutch is disengaged and the transmission is in gear. If either the clutch is engaged or the transmission is in neutral, the cruise control will be disengaged" — [BMW ST041 Engine Electronics part 3](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf) [read]. (BMW's "clutch is disengaged" means pedal up, drive engaged; the SGBD bit is `STAT_KRAFTSCHLUSS_EIN`, "force-closure chain".)
- BMW M3: "The MFL in the E46 M3 is a BMW M development. The assembly and operation of the buttons for audio communication and cruise control function as in the E46/2"; the M3 bus chart draws MFL "GR" straight to the DME — [BMW ST041 M3 Complete Vehicle](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf) [read].
- MSS54 SGBD: `STAT_MFL1_EIN`…`STAT_MFL4_EIN` (wheel buttons), `STAT_KUP_EIN` and `STAT_KRAFTSCHLUSS_EIN` (the same input byte and bit, opposite sense), `STAT_BLS_EIN`, `STAT_BLTS_EIN`, faults 0x51 "MFL-Schnittstelle", 0x6A "Bremslichtschalter", 0xC2 "Sicherheitsabschaltung FGR", 0x2A "Geschwindigkeitseingang direkt", and `STATUS_V_CAN` (speed from the ASC/DSC over CAN) — [SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md) [read]. The MFL module's own SGBD reports `STAT_TEMPOMAT_VARIANTE` and each cruise button (`STAT_TEMP_WA/SB/VER/AUS_BETAETIGT`) — [SGBD MFL](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MFL.md) [read; the file is labelled E38].
- BMW: "The brake light switch is a hall sensor that receives power when KL R is switched on … When the LSZ receives a high signal from the switch the brake lights are switched on" — [BMW ST034 Driver Information](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf) [read]. The MK60 also reads the brake switch (pin 41) and checks it against the pressure sensors ("must not detect more that 5 bar when the BLS is not actuated") — [BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) [read]. The LSZ coding has `BLS_PRUEFEN` and the SGBD `COD_BLS2_ABFRAGE_EIN` ("2. Bremslichtschalter wird abgefragt") — [SGBD LSZ](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ.md) [read].
- Already established (earlier notes, read there): MS43/MS45 clutch at X60004-23, MSS54 at X60002-20 via the gear-recognition switch 23142229113 (wire GR/BL at the DME); clutch-module pinout 1 BR/SW ground, 2 BL/BR DME signal, 3 VI/GE 12 V, 4 BL/SW EWS pin 8; M3 module 61319122700. In the only S54-Touring report, cruise worked after a new M3 module replaced a junkyard 330i one; brake second contact 28 → 34. See `harness_body_functions.md` Q4–Q5.

### Inferences
- **Inference: the path, both cars.** Right MFL keypad → MFL electronics in the wheel → clock spring → one FGR serial wire → DME X60004-27. This needs no change. Audio buttons are on the K-bus and don't involve the DME.
- **Inference: why the M3 clutch module matters.** The MSS54 wants "high" only when the pedal is up *and* the gear switch is closed. The 325i module's DME contact was designed for MS43's direct input, and its idle state and polarity may not suit the series chain. That fits the one report (a 330i module didn't work, a new M3 one did) but isn't proven. Check with `STAT_KRAFTSCHLUSS_EIN`: it should read 1 only in gear with the pedal released.
- **Inference: cruise also depends on the CAN speed message from the DSC.** With the Touring's MK60 this is unchanged, but a DSC that isn't initialised (VIN fault) can stop cruise.

### Gaps
- No BMW statement of the clutch-module contact logic for the 325i versus the M3.
- Where the M3's clutch-to-gear-switch wire crosses from the body harness to the engine harness (X6011 pin 7?) is still unverified (see the earlier notes).

---

## Q7. Sport button: wiring the M3 switch centre (SZM) into a Touring that never had one

### Cited findings
- newTIS screenshot posted on NAM3 (Darbshaw, 11-25-2023; page header "Switching centre"): "X1869 — 23-pin, black — Plug connector Switching centre; X521 — 4-pin, black — Plug connector Switching centre". X1869: 1 "Signal, seat heating on — Seat heating, right"; 2 "Signal, RDC initialisation button — Digital motor electronics control unit"; 3–6 not used; 7 "E — Voltage supply Terminal 30 — Fuse F42"; 8–12 not used; 13 "Signal, seat heating on — Seat heating, left"; 14/15 "Signal, roller sunblind up/down — Sun shade motor"; 16 not used; 17 "A — Signal, driving dynamics — Digital motor electronics control unit"; 18 "E — Driving dynamics active LED — Digital motor electronics control unit"; 19 "Spatial sound function — Amplifier"; 20/21 "Temperature signal, seat heating — right/left"; 22 "E — Terminal R — Fuse F12"; 23 "E/A — K-bus signal — K-bus connector". X521: 1 "E — Voltage supply Terminal 15 — Fuse F33"; 2 "A — Signal, ASC/DSC passive — ABS/DSC unit"; 3 "E — Terminal 58g — Light switching centre control unit"; 4 "A — Ground — Ground point" — [NAM3 243243, post #4 image](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/243243-depinning-center-control-switch) [read, image; the model behind the newTIS page isn't shown].
- Same thread: Darbshaw found "fuse 12 for pin 22 was blown on X1869 that's what was causing my issue for the system to not work", and "The DSC button was never designed to be used without the center switch. Even though pin 1 on the DSC connection is ran and fused the center switch cannot be used without power from pin 22 on X1869." George Hill: "The DSC button goes to the (4) wire connector on the SZM and you can get just a DSC button as some cars didn't come with an SZM"; "Some Non-M's did not come with SZMs as such they just had a DSC button. That button can connect straight to the 4 pin connector at the SZM"; "Solo DSC switch pn# 61316901592". Darbshaw's photo shows the SZM's large 23-pin socket and a small 4-pin socket marked ">ABS<" [read; photo viewed].
- SZM SGBD ("Schaltzentrum Mittelkonsole E46"): `STATUS_IO` covers seat-heater buttons, temperatures and power, the sunshade, the SURROUND button and LED, terminals R, 15, 50 and the terminal-30 voltage. Fault 0x001 is "Klemme 30 nicht vorhanden" (terminal 30 missing), and the info memory includes "Taster HiFi System dauernd betaetigt". There is no DSC or Sport status: those buttons are hard-wired straight to the DSC unit and the DME — [SGBD SZM46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/SZM46.md) [read]. BMW: "The DSC button is located on the SZM, however the SZM provides no processing, it is simply a housing for the button which is hardwired to the MK60 control unit" — [BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) [read].
- BMW MSS54: "The switch provides a ground signal (input) to the ECM when pressed. The MS S54 activates the sport characteristics for the EDR throttle control" — [BMW ST041 part 3](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf) [read]. M3 console buttons A–F: driver seat heater, DSC, Hi-Fi, tyre-pressure warning, Sport, passenger seat heater — [BMW ST041 M3 Complete Vehicle](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf) [read]. MSS54 SGBD: `STAT_FDYN_EIN`, fault 0x6E "LED Fahrdynamikschalter" — [SGBD MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md) [read].
- Where the tyre-pressure reset goes depends on DSC generation. TIS-derived MK60 mapping: MK60 pin 40 "Signal, RDC initialisation button" (blue/red) "Does not exist on MK20" — [heinzboehmer's mapping (2022)](https://nam3forum.com/forums/filedata/fetch?id=189181) [read]. The MSS54 SGBD carries tyre-pressure fault locations 0x64–0x67 ("Reifendruck vorn links" etc.), consistent with the DME handling the warning on MK20-era M3s [read]. The S54 harness's X6011 carries a "TPMS" wire (earlier notes).
- ETK: the M3 coupe's switch unit is 61316925520 (the guide also lists convertible 61316925521). The 325i Touring's SZM 61316925498 is listed "For vehicles with Dynamic stability control S210A: No". Both catalogs list solo "Switch asc" 61316901591 and "Switch dsc" 61316901592 (M3: "from Sep '99") — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/switch_unit_center_console/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_electrical_system/switch_unit_center_console/), [ETK various switches](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_electrical_system/various_switches/) [read].
- Owners' feeds: Tenza's wagon worked reliably only when the panel's constant feeds (red/violet and white/red) and accessory feed (violet/blue) all had 12 V; its HiFi button lit but did nothing, and TPMS didn't work. M346: base Tourings have "no wiring to the K bus for the switch panel or the fuse box" (`youtube_swap_wiring_coding.md`) [read by the earlier researcher].

### Inferences
- **Inference: minimum wiring for Sport (and to keep DSC-off working) in a Touring with only a solo DSC button:** fit an X1869 housing with terminals and run:
  - pin 7 → terminal 30 through F42;
  - pin 22 → terminal R through F12 (without it the SZM, and so the DSC button behind it, does nothing);
  - pin 23 → K-bus (tap any K-bus point; the K-bus colour at the cluster is WS/RT/GE);
  - pin 17 → X60004-15 and pin 18 → X60004-16 (clear MS45 pin 15 first).
  The existing 4-pin DSC plug (X521: terminal 15 F33, DSC signal, 58g, ground) carries the SZM's ground and lighting, as George Hill describes.
- **Inference: pins you can leave empty:** seat heating (1, 13, 20, 21) unless fitted; sunshade (14/15); "spatial sound" (19) unless an amplifier supports it. That explains Tenza's dead HiFi button.
- **Inference: tyre-pressure reset (X1869-2).** With the Touring's MK60, route it to MK60 pin 40 and only if the MK60 is coded for the flat-tyre warning (`REIFENDRUCKWARNSYSTEM`) and the M3 cluster for `RDKS`. If the MSS54 (MK20-era donor) still runs its own tyre-pressure logic, it may log 0x64–0x67 faults. Read the DME faults after the first drive.
- **Check:** Tool32 SZM46 `STATUS_IO` (terminals R/15/50, terminal-30 voltage); MSS54 `STAT_FDYN_EIN` toggles, and the LED follows.

### Gaps
- Which newTIS model page the screenshot came from (M3 or generic E46), and the wire colours for X1869/X521.
- Whether US 325iT fuse positions F42/F12/F33 are populated on the load side (the earlier notes say unused positions are often power-side only).
- The DME pin for the RDC button on MK20-era M3s.

---

## Q8. Wheel-speed sensors, pad-wear sensors and the DSC button by build date

### Cited findings
- BMW E46 DSC (01/2003). MK20: "The E46 DSC III (Mk 20) system uses the wheel speed sensors from the ASC system. The whee[l] speed sensors are the inductive type and generate an AC Analog Signal." MK60: "active wheel speed sensors that operate on the principle of magnetoresistive effect … The sensor evaluation circuit is supplied 12V by the MK60 control unit … Signal High-14mA, Signal Low-7mA … Front sensors are three wire because they have a separate ground wire. Rear sensors are two wire and use the sensor case as a ground point … The connectors are blue to distinguish them apart from the grey connectors used for sensors on the MK20 EI. The DSC III MK60 uses the same metal pulse wheels used with the MK20 inductive sensors." Left and right front sensors differ in harness length. Rear: "The short sensor is used on the 325i (any transmission) and 330i automatic. The long sensor is used on the 330i manual." Applicability: "Teves MK20 99-00 E46 323, 328i … Teves MK20 00- Present M3; Teves MK 60 01 - Present 325, 330" — [BMW ST056 E46 DSC](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) [read]. (The 01/2003 document predates the M3's MK60; the earlier notes put the M3's MK60 from 09/2002 build.)
- First-hand, 2002 M3 MK20→MK60 (heinzboehmer, 10/2022): "The sensors are different between the two systems so you need to swap the plugs. Fortunately the pins are the same so only the connector housings need to get swapped … The front connectors will have three wires running to them, while the new plugs are only expecting two. The middle back one (pin 3) is a ground that is not needed on the MK60." MK60 power and ground pins 1, 16, 32 and 47 use 2.5 mm² wire — [NAM3 189096](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap) [read]. This conflicts with BMW's "front sensors are three wire" for the MK60; the owner's account is the hands-on one.
- TIS-derived pin mapping (attachment to that thread), reproduced as table F4: MK60 47-pin assignments with MK20 equivalents and TIS wire colours, including each wheel's supply/signal pair, CAN, D-bus TXD, brake switch, ABS warning lamp, parking brake, brake fluid, "ASC passive button", RDC button, M-Track input and the sensor cluster — [heinzboehmer's xlsx](https://nam3forum.com/forums/filedata/fetch?id=189181) [read].
- ETK, DSC hardware by date. US 325i Touring: MK60 DSC "from Sep '00 to Sep '01" (hydro unit 34516756291, control unit 34516756293, separate yaw sensor 34526864094 and lateral "Accelerating sensor" 37146781405); MK60 "from Sep '01" (34516765453/34516764087, control unit 34526765455/34526764089, combined sensor cluster "Speed sensor" 34526764018, bracket 34526750817, socket housings 61138383300 and 61136954574); also an MK60 ASC (no-DSC) unit "to Sep '01". US M3: MK20 "to Sep '02" (34512229827, control unit 34512229802, plug housing 61138377146, separate yaw and lateral sensors, pre-charge pump); MK60 "from Sep '02" (34512282558 / 34512282421, control unit 34522282559 / 34522282423, the same sensor cluster 34526764018, bracket and socket housings as the Touring) — [ETK Touring DSC to 09/01](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/hydro_unit_dsc_fastening_sensors/), [from 09/01](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/hydro_unit_dsc_fastening_sensors_2/), [ETK M3 MK60](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/hydro_unit_dsc_fastening_sensors/), [ETK M3 MK20](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/hydro_unit_dsc_control_unit_fastening/) [read].
- ETK pulse generators: rear 34526752683 ("Pulse generator, ABS rear", production "Sep '00 –") is listed for the US M3 coupe and convertible as well as the 325i Touring; front 34526792896 ("Pulse generator, ABS front right") is listed for the M3 too — [ETK 34526752683](https://bmwfans.info/parts-catalog/34526752683/), [ETK 34526792896](https://bmwfans.info/parts-catalog/34526792896/) [read]. (These are current supersessions, so they don't show the MK20-era originals.)
- ETK pad-wear sensors: M3 front 34356751311 (also 330i/330Ci/330xi/325xi), M3 rear 34352229780 (M3/CSL only); 325i Touring front 34351164371, rear 34351164372 — [ETK M3 front](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/front_brake_pad_wear_sensor/), [M3 rear](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/rear_brake_brake_pad_wear_sensor/), [Touring front](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/front_brake_pad_wear_sensor/), [Touring rear](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/rear_brake_brake_pad_wear_sensor/), [34356751311](https://bmwfans.info/parts-catalog/34356751311/) [read]. The M3 rear group lists Competition-package calipers "S7MAA" from Dec '04, which identifies `$7MA` as the Competition Package (ZCP) option code [read].
- BMW cluster: "The brake pad circuit is monitored for an open or interruption of the ground when the sensor is worn through" (X11175-24) [read, ST052 03b].
- DSC button (MK60): short press under 2.5 s turns off yaw control only (DSC lamp); long press over 2.5 s turns everything off (DSC lamp plus yellow brake lamp) — [BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf) [read]. The MK60 input is pin 39 "ASC passive button" (MK20 pin 27), TIS colour blue/violet [read, heinzboehmer mapping].
- Swap reports (earlier notes): Tenza's 2004 Touring with a 2002 M3 donor found the plugs "will not plug into each other"; the Touring's own sensors in the M3 hubs left an ABS light (not diagnosed). A 2003 xi Touring took an M3's sensors. M3projekts found the M3 MK60 used "the same connector" as the Touring's unit.

### Inferences
- **Inference: what fits the Touring's harness.** The US 325iT has had MK60 (active, blue plugs) since 09/2000. It takes its own sensors or those of an M3 built from 09/2002 (MK60). It does **not** take an MK20-era M3's sensors (to 09/2002): grey plugs, inductive, an AC signal the MK60 can't read. Splicing an MK20 donor's M3 sensor pigtails onto the Touring's MK60 harness (one builder's planned fallback) would be wrong. Tenza's donor was a 2002 car, which explains the mismatch.
- **Inference: Touring sensors in M3 hubs should read.** BMW says the MK60 uses the same pulse wheels as the MK20, and the current front and rear pulse generators are listed for both cars. If an ABS light appears, check each wheel's speed in INPA's DSC status before blaming the sensor: look for a seated sensor, the rear lead length, and the DSC VIN/coding.
- **Inference: pad-wear sensors.** The M3 front sensor (shared with the 330i) and the M3 rear sensor plug into the same single ground-loop circuit to cluster pin 24. The difference is lead length and caliper fit. Check plug shape and lead routing at both axles; open loop = lamp on.
- **Inference: DSC button.** The M3 SZM's 4-pin X521 is the same plug a solo DSC button uses (George Hill), so it connects to the Touring's existing DSC-button lead. With an M3 MK60 coded for M Track, the M-Track input (pin 38) and LED coding are separate topics (see `coding_body_chassis.md`).

### Gaps
- Original (pre-supersession) MK20-era M3 sensor part numbers and the grey-plug housing number weren't extracted.
- The rear-sensor lead length on the M3 rear axle versus the 325i "short" sensor is unconfirmed.
- The solo DSC switch's plug (ETK lists a 6-pole housing 61136909058 in that group) versus the 4-pin X521: a forum statement says they match, but this isn't confirmed by ETK or TIS.

---

## Q9. Lights: halogen versus xenon, levelling sensors and light-module coding

### Cited findings
- BMW: "Starting with the 1999 model year all US market vehicles with Xenon Lights incorporate LWR as standard equipment. LWR is not available with standard halogen headlights." "The E46 LWR function is integrated into the control electronics of the LSZ … directly activates the stepper motors in the headlight assemblies. All LWR diagnosis is accessed through the LSZ." "LWR monitors two hall effect level sensors … mounted to a fixed point on the suspension carriers of the front and rear axles … linear voltage signal"; "The 4 wire stepper motors"; "updates the headlight beam positions every 25 seconds"; aim xenon lights after waiting "at least 30 seconds for the LWR to cycle". Xenon: "The xenon control modules (1 per light) receive operating power from the lighting control module (… LSZ E46) when the headlights are switched on"; "cold monitoring for low beam headlights is encoded off in the lighting control module for Xenon headlight equipped vehicle"; a failed bulb shows as the ballast's current dropping to 60 mA. The E46 uses Bosch lights and ballasts — [BMW ST034 Driver Information](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf) [read].
- BMW 2002 (from 09/2001): "The central light switch (LSZ) in the E46 is redesigned with new electronic modules … The voltage for the vehicle lighting is output with a pulse-width-modulated signal at a fixed frequency of 80 Hz. The LSZ has separate outputs for additional rear brakes lights and bi-xenon equipment." "Bi-Xenon head lamps are available as a option only" (sedan/touring facelift) — [BMW ST043 2002 Update](https://archive.org/download/BMWTechnicalTrainingDocuments/ST043%202002%20System%20Diagnosis/8%20E46%20Update.pdf) [read]. From 03/2003 coupe/convertible AHL "will be coupled with Bi-Xenon Lights only" (AHL control unit, LIN to the headlight motors, inputs from the ride-level sensors, steering-angle sensor and DSC) — [BMW ST047 E46 FL](https://archive.org/download/BMWTechnicalTrainingDocuments/ST047%202003%20System%20Diagnosis/5%20E46%20FL.pdf) [read].
- ETK US M3 headlights: halogen 63126904279/280 "to Sep '01" and 63127165903/904 "from Sep '01"; xenon 63126904297/298 "to Sep '01"; bi-xenon 63127165823/824 "from Sep '01"; xenon is option "S522A". US 325iT (from Sep '01): halogen 63127165771/772 (ZKW) or 63127165785/786 (AL), xenon/bi-xenon 63127165779/780, 165791/792 and 165833/834. Both cars' headlight groups list the same "Socket housing, grey" 61138364498, "Plug terminal black" 61138364494, universal housings 61138373332 and 61138365356, "Head light vertical aim control" 67168372381 (also 67168352206) and "Wiring light regulator" 61138373573. Their xenon groups list the same ballasts (61358376273 to 09/01; 63127176068 AL from 09/01; 63126925647 ZKW from 09/02) and igniters — [ETK M3 headlight](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/lighting/headlight/), [M3 xenon parts](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/lighting/single_parts_xenon_headlight_2/), [M3 halogen parts](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/lighting/single_components_for_headlight_2/), [Touring headlight](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/lighting/headlight/), [Touring xenon parts](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/lighting/single_parts_xenon_headlight/), [Touring halogen parts](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/lighting/single_components_for_headlight/) [read].
- ETK levelling sensors: both cars list "Level sensor" 37146784696 and 37146784697 with the same brackets and regulating rod. The M3 uses its own "Front angle joint" 31122282404, the Touring 37146766778 — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/headlight_vertical_aim_control_sensor/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/headlight_vertical_aim_control_sensor/) [read].
- ETK light switch centre: identical lists for both cars. Light switch units 61319133022/023 (rain sensor no/yes, xenon no), 61319133024/025 (with fog switch, xenon **no**), 61319133026/027 (xenon **yes**), 61319133029 (AHL, "from Sep '01"); control units 61318378577 and 61316911647 (xenon no); socket housings 61138364826 and 61138364828 — [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/switch_unit_light/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_electrical_system/switch_unit_light/) [read].
- LSZ SGBDs: the front load sensor is read as `STAT_SPANNUNG_BELADUNGSSENSOR_VORN_WERT` (0–5 V). The input `STAT_EINGANGSSPANNUNG_LWR_POTI_WERT` is "0 bis 5 Volt, bei Xenon-Licht hinterer Beladungssensor" (on xenon cars, the rear load sensor). Jobs `XENON_VORHANDEN`, `LWR_VORHANDEN`, `STEUERN_BELADUNGSSENSOR_VORN`, `STEUERN_DYN_LWR`; faults 0x21–0x24 front/rear load sensor open or short to ground, 0x1E "Steuergeraetefehler im LWR-Teil"; output `BIXENON`; coding results `COD_AL_KALTUEBERWACHUNG_EIN`, `COD_LWR_AUTOMATISCH_CODIERT`, `COD_BLS2_ABFRAGE_EIN` — [SGBD LSZ](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ.md), [SGBD LSZ_2](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ_2.md) [read].
- ALSZ coding names from a 2002 M3 convertible: `BI_XENON`, `BIXENON_EIN_BEI_LICHTHUPE`, `KALTUEBERWACHUNG_AL` (cold testing low beams), `KENNLINIE_LWR_SENSOR_VO` (wert_01–05), `KENNLINIE_LWR_SENSOR_HI` (wert_01–04), `DEF_LWR_SENSOR_HI`, `LWR_VORZEICHEN`, `LWR_NEIGUNG_KONSTANTE`, `POTI_LWR_INVERS`, `XENON_TEST/TIME/TIMEOUT`; miscellaneous `AUTO_LWR_ENABLE` — [NikolaiD M3 NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf) [read].
- Owners' retrofits (UK, ECE cars): "Best way is to add $522 to the VO (vehicle order). This can be done via NCS. Then get the dash height adjuster re-enabled by modifying the LCM"; "In terms of encoding the headlamps, all you're doing is telling it not to send the bulb check pulse every minute"; "Technically it's the same unit and the level adjuster is on all of them but blanked off on the ones with auto levelling" — [E46Zone: Coding Xenon Headlights](https://www.e46zone.com/forum/topic/33680-coding-xenon-headlights/) [read]. Fitting 2003 M3 bi-xenons to a 2003 halogen saloon: add $522; for manual levelling, untick "Dynamic Headlamp adjustment" and "Automatic Headlamp adjustment" in NCS Dummy — [E46Zone: Saloon facelift bi-xenon coding](https://www.e46zone.com/forum/topic/65281-e46-saloon-facelift-bi-xenon-coding/) [read]. "Next I used NCS Expert to change 'BI-XENON' from 'nicht_aktiv' to 'aktiv'. That fixed my high beam issue" — [e46fanatics: pre-facelift xenon retrofit](https://www.e46fanatics.com/threads/pre-facelift-xenon-retrofit-ncs-expert-coding-questions.1314954/) [snippet].

### Inferences
- **Inference: the M3 front end means M3 (coupe-pattern) headlights.** Halogen into a halogen Touring: the socket housings are common in ETK, so the lamps should plug in, with only the halogen coding unchanged. Confirm pin functions at the headlight plug before first light-up.
- **Inference: M3 xenon or bi-xenon into a halogen US Touring is a system job, not a lamp swap:**
  1. Ballast feeds come from the low-beam outputs through the headlight plug.
  2. The LSZ drives the levelling motors (4-wire, inside the lamps), so check the harness has those pins populated.
  3. Fit both level sensors with their linkages (the M3 front link on the M3 arm) and wire them to the LSZ's front-sensor and "LWR pot / rear sensor" inputs.
  4. For bi-xenon (M3 from 09/2001), use an LSZ of the 09/2001 redesign with the bi-xenon output. ETK lists the xenon switch units 61319133026/027 separately; a Touring built before 09/2001 needs that newer LSZ.
  5. Coding: add `$522` to the vehicle order (FA_WRITE to AKMB and ALSZ), then code the ALSZ: `BI_XENON = aktiv`, `KALTUEBERWACHUNG_AL = nicht_aktiv`, automatic levelling on, sensor curves per body.
  6. Verify with LSZ `XENON_VORHANDEN`, `LWR_VORHANDEN` and the sensor voltages in `STATUS_LESEN`.
- **Inference: levelling curves.** `KENNLINIE_LWR_SENSOR_VO/HI` are coded from the body type. The Touring keeps its own rear axle, while the front sensor now rides on the M3 arm and link, so check that the beam doesn't move with load beyond the LSZ's correction. Aim at ride height after the 30-second LWR cycle.
- **Inference: mileage safety.** The LSZ holds the true mileage and VIN (Q1). If a xenon-variant LSZ is needed, do it only after the new cluster has taken the mileage, and give the new LSZ the car's VIN so it copies the mileage from the cluster. Never replace both at once.
- **Inference: AHL.** AHL lamps (M3 from 03/2003 option) also need the AHL control unit, LIN and more coding. Prefer non-AHL M3 lamps.

### Gaps
- LSZ pin numbers and wire colours for the level sensors and levelling motors; whether a US halogen 325iT harness has those cavities populated.
- Whether a US halogen LSZ (control unit 61318378577) can simply be coded for xenon (the UK reports concern ECE units with a manual dial).
- US M3 front side-marker and turn-signal wiring against the Touring's (not researched).

---

## Diagram-ready data

Notation: colours use BMW abbreviations (SW black, BR brown, RT red, GE yellow, GN green, BL blue, VI violet, GR grey, WS white, OR orange); "A/B" = base colour with stripe. **Source** codes: **[B]** BMW training PDF, **[S]** SGBD, **[W]** WDS/ISTA/newTIS/TIS copy, **[H]** hobby-site transcription (bmwgm5), **[C]** CarCluster bench pinout, **[F]** forum, **[E]** ETK. **inf.** = inference.

### D1. Instrument cluster X11175 (black, 26-pin), non-M E46 [H], cross-checked with [C]

| Pin | Wire | Signal | From/to | M3/MSS54 note |
|---|---|---|---|---|
| 1 | 0.5 BR/SW | Ground | Ground point | Same [C] |
| 2 | 0.35 BL | S_61: charge lamp | 325i: alternator side (via E-box plug, X6011-4 per forum) | M3: from DME X60004-1 (DME grounds lamp) [W][F] |
| 3 | 0.35 SW/GN | S_30H: engine start feedback | 325i: body side (X6011-6 per forum) | M3: probably DME X60004-6 "terminal 50" (inf.) |
| 4 | 0.5 RT/GE/WS | Terminal 30 | Fuse F43 (5 A) | |
| 5 | 0.5 GN/BL | Terminal 15 | Fuse F34 (5 A) | ISTA M3: same (GN/BL) [W] |
| 6 | 0.5 VI/GE | Terminal R | Fuse F10 (5 A) | |
| 7 | 0.35 GR/RT | 58G lighting ("MY02 and earlier only") | LSZ | Older cluster in a 09/2002+ car: wire LSZ pin 47 (GR/RT) here (earlier notes) |
| 8 | 0.35 SW/WS | TAA: speed signal output | Other modules | |
| 9 | 0.5 GE/RT | CAN-H | CAN splice | [C] pin 9 CAN H |
| 10 | 0.5 GE/BR | CAN-L | CAN splice | [C] pin 10 CAN L |
| 11 | 0.5 SW/RT/WS | Right fuel sender + | Delivery unit (pump side) | |
| 12 | 0.5 BR/SW/WS | Right fuel sender − | Delivery unit | |
| 13 | 0.35 BR/GN | S_OLD: oil-pressure lamp | 325i MS43: switch via X6011-3 | M3: from DME X60004-11; switch on X60003-26 [W] |
| 14 | 0.35 WS/RT/GE | **K-bus** | K-bus | Not oil pressure (Kassel error) |
| 15 | 0.5 SW/RT/GE | Left fuel sender + | Left sender | |
| 16 | 0.5 BR/SW/GE | Left fuel sender − | Left sender | |
| 17 | 0.5 WS/GN (to 03/2003), GR/BL (after) | F_OLN: oil level (PWM) | 325i MS43: sensor via X6011-5 | M3: from DME X60004-21, or CAN if `TOG_UEBER_CAN` |
| 18 | 0.5 SW/RT | SI reset signal | 20-pin socket era only | Absent on 2001+ |
| 19 | 0.35 GE/GN | F_DFAHL: rear-left wheel speed (processed) | DSC (MK60 pin 10 / MK20 pin 4) | Same |
| 20 | 0.35 BR/GN/GE | BRFN: brake-fluid level | Reservoir switch, spliced to DSC (MK60 pin 9) | Same |
| 21 | 0.35 BR/VI | AWS: airbag warning | MRS | Same |
| 22 | 0.5 GR/SW/GE ([H]); TIS: GN/SW/GE | ABS warning lamp | DSC MK60 pin 44 / MK20 pin 19 | Same |
| 23 | 0.5 BL/BR/GE | FSB: parking-brake switch | Switch, spliced to DSC (MK60 pin 27) | Same |
| 24 | 0.35 GE | BBV+: pad-wear loop | Front and rear pad sensors to ground | Same |
| 25 | 0.35 WS/VI | D_TXD1: diagnosis (D-bus) | OBD pin 8 | Same |
| 26 | 0.35 BR/WS | KFN: coolant level | Expansion-tank switch | Lead must reach the M3 tank position |

### D2. Instrument cluster X11176 (white, 18-pin) [H]

| Pin | Wire | Signal |
|---|---|---|
| 1 | 0.5 BL/RT | Outside temperature + |
| 2 | 0.5 BL/BR | Outside temperature − |
| 4 | 0.35 BR/GN | Washer-fluid level |
| 5 | 0.35 BL/GE | Cruise-active lamp (M43 cars only; others over CAN) |
| 6 | 0.5 WS/BL | Rollover warning (convertible) |
| 7 | 0.35 BL/GE | Reverse (manual) |
| 12 | 0.35 BL/SW/GE | Driver belt (convertible) |
| 13 | 0.35 GE/RT | BC stalk button |
| 14 | 0.35 SW/RT | Gong T3 |
| 3, 8–11, 15–18 | | Not connected |

Fuel senders: left about 70 Ω empty to about 310 Ω full; right about 70 Ω empty to about 395 Ω full [H, unverified].

### D3. Cluster lamp and gauge sources (both cars)

| Item | Path | Bus or wire | Source |
|---|---|---|---|
| Engine speed, consumption (ti), coolant temperature, check-engine, cruise lamp, overheat | DME → CAN → cluster | CAN | [B][S] |
| Oil temperature and warm-up/shift LEDs (M3 cluster) | MSS54 → CAN → cluster | CAN | [B] |
| DSC lamp, yellow brake (EBV/ABL) lamp, ASC lamp, tyre-defect lamp (MY2002+) | DSC → CAN → cluster | CAN | [B] |
| ABS lamp | DSC MK60 pin 44 → X11175-22 | Wire | [B][W] |
| Red brake lamp | Fluid switch → X11175-20; park-brake switch → X11175-23 | Wire | [B][H] |
| Oil pressure | 325i: switch → X6011-3 → X11175-13. M3: switch → X60003-26 → DME → X60004-11 → X11175-13 | Wire (or CAN if `CAN_OELDRUCKSCHALTER`) | [W][F] |
| Charge | 325i: alternator → X11175-2. M3: alternator 61 → X60003-13 → DME → X60004-1 → X11175-2 | Wire (or CAN if `GENERATOR_UEBER_CAN`) | [W][F] |
| Oil level | 325i to 03/2003: sensor → X11175-17. M3: sensor → X60003-39 → DME → X60004-21 → X11175-17 | Wire (or CAN if `TOG_UEBER_CAN`) | [B][W] |
| Road speed | DSC → X11175-19 (rear-left, processed) | Wire | [B][W] |
| Tank level to DME | Cluster → CAN → DME | CAN | [B][S] |
| Outside temperature to IHK | Cluster → K-bus | K-bus | [B] |

### D4. DME X60004 body-side pins in these circuits [W] (full table in `WIRING-AND-CODING.md`)

| Pin | MSS54 | MS43 | MS45 | Goes to |
|---|---|---|---|---|
| 1 | Terminal 61 out to cluster | — | — | X11175-2 |
| 2 | Start feedback in (terminal 30h) | — | DM-TL heater | Starter side |
| 4 | Electric fan PWM | Same | Same | Fan output stage |
| 6 | Terminal 50 out to cluster | — | — | X11175-3 (inf.) |
| 10 | Pump relay ("not USA") | Pump relay K96 | — | K96 coil (SW/VI) |
| 11 | Oil-pressure out to cluster (BR/GN) | — | — | X11175-13 |
| 15 / 16 | Sport input / Sport LED | — | 15: secondary-air HFM (US 3.0) | X1869-17 / X1869-18 |
| 17 | Speed signal to the data-link connector | Same | Same | OBD socket (pin not confirmed) |
| 21 | Oil level out to cluster | — | — | X11175-17 |
| 22 | Rear-right wheel speed in | Same | Same | DSC MK60 pin 8 / MK20 pin 32 |
| 23 | — | Clutch switch | (MS45.1 clutch) | Clutch module pin 2 (BL/BR) |
| 24 | Brake-light signal via LSZ | Same | Brake-light switch | LSZ |
| 26 | Terminal 15 | Same | Same | F29 |
| 27 | MFL cruise data | Same | Same | Clock spring, MFL |
| 28 | — | Brake-light switch, 2nd contact (BR/GN) | Brake-light test | Brake switch |
| 29 | A/C compressor relay | Same | Same | K19 coil |
| 32 | TXD (TXD II) | Same | Same | OBD pin 7 |
| 33 | EWS (ISN line) | Same | Same | EWS |
| 34 | Brake-light switch, 2nd contact | — | — | Brake switch |
| 36 / 37 | CAN-H / CAN-L | Same | Same | CAN splice |
| 38 / 39 | Radiator-outlet sensor | Same | Same | Sensor |
| X60002-11 | US pump module (EKP) PWM | — | — | M3 EKP (not used if K96 kept) |
| X60002-12 | E-box fan | — | (MS45: X60004-19) | E-box blower |
| X60002-20 | Clutch + gear-switch chain (GR/BL) | — | — | 420G gear switch pin 2 |
| X60003-13 / 26 / 39 | Terminal 61 / oil-pressure switch / oil-level sensor (inputs) | | | Engine harness |

### D5. Switch centre (SZM) X1869 (23-pin, black) and X521 (4-pin, black) [W: newTIS screenshot]

| Plug-pin | Type | Function | To | Needed in the Touring? |
|---|---|---|---|---|
| X1869-1 | A | Seat heating on, right | Right seat heater | Only with seat heating |
| X1869-2 | A | RDC (tyre-pressure) reset button | DME per newTIS (MK20-era); MK60 pin 40 on MK60 cars [W] | Optional |
| X1869-7 | E | Terminal 30 | Fuse F42 | **Yes** (SZM fault "Klemme 30 nicht vorhanden") |
| X1869-13 | A | Seat heating on, left | Left seat heater | Only with seat heating |
| X1869-14 / 15 | A | Sunblind up / down | Sun-shade motor | No |
| X1869-17 | A | Sport ("driving dynamics") signal, switches to ground | DME X60004-15 | **Yes, for Sport** |
| X1869-18 | E | Sport LED | DME X60004-16 | **Yes, for Sport** |
| X1869-19 | A | Spatial-sound (HiFi) function | Amplifier | No |
| X1869-20 / 21 | A | Seat-heater temperature, right / left | Seat heaters | Only with seat heating |
| X1869-22 | E | Terminal R | Fuse F12 | **Yes** |
| X1869-23 | E/A | K-bus | K-bus connector (WS/RT/GE, inf.) | **Yes** |
| X521-1 | E | Terminal 15 | Fuse F33 | Present with the DSC button |
| X521-2 | A | ASC/DSC passive (button) | DSC unit (MK60 pin 39, BL/VI per TIS) | Present |
| X521-3 | E | Terminal 58g | Light switch centre | Present |
| X521-4 | A | Ground | Ground point | Present |

### D6. DSC MK60 47-pin (E46; TIS colours from heinzboehmer's mapping [W]; MK20 = M3 to 09/2002)

| MK60 pin | Function | TIS colour | MK20 pin |
|---|---|---|---|
| 1 | Terminal 30 (2.5 mm²) | RT/GE | 42 |
| 2 | Diagnosis TXD (D-bus) | WS/VI | 8 |
| 4 | Terminal 15 | GN/BL/GE | 12 |
| 6 | DSC sensor cluster, sensor pin 3 | SW/RT/WS | — |
| 8 | Processed wheel speed rear-right (to DME X60004-22) | WS/GN | 32 |
| 9 | Brake-fluid level (spliced with fluid switch pin 2, to cluster 20) | BR/GN/GE | 41 |
| 10 | Processed wheel speed rear-left (to cluster 19) | GE/GN | 4 |
| 11 | CAN high (twisted with 15) | GE/RT | 17 |
| 15 | CAN low | GE/BR | 16 |
| 16 | Ground (2.5 mm²) | BR | 1 |
| 18 / 19 / 20 | Pressure sensor 1: supply / ground / signal | BL/SW, WS/BL, SW/VI | 23 / 26 / 11 |
| 21 / 22 / 23 | Pressure sensor 2: ground / supply / signal | WS/BL/GE, BL/SW/GE, SW/VI/GE | 24 / 20 / 36 |
| 24 | DSC sensor cluster, sensor pin 5 | BL/WS/GE | — |
| 25 / 29 | DSC sensor cluster, sensor pins 1/2 (twisted pair; the separate CAN per BMW, inf.) | BL/GE, GE | — |
| 27 | Parking-brake switch (spliced to cluster 23) | BL/BR/GE | 28 |
| 32 | Terminal 30 (2.5 mm²) | RT/BL | 15 |
| 33 / 34 | Wheel sensor front-right: signal / supply | BR / GE | 30 / 31 |
| 36 / 37 | Wheel sensor rear-left: supply / signal | BL / BR | 34 / 33 |
| 38 | M-Track mode input (ZCP) | BR/GN | — |
| 39 | DSC ("ASC passive") button (X521-2) | BL/VI | 27 |
| 40 | RDC reset button (X1869-2) | BL/RT | — |
| 41 | Brake-light switch | BL/RT | 18 |
| 42 / 43 | Wheel sensor rear-right: signal / supply | GE/BR / GE/SW | 6 / 5 |
| 44 | ABS warning lamp (to cluster 22) | GN/SW/GE | 19 |
| 45 / 46 | Wheel sensor front-left: supply / signal | BR/RT / BR | 2 / 3 |
| 47 | Ground (2.5 mm²) | BR | 29 |

MK20-only pins (not used on MK60): 9/10/21 lateral-acceleration sensor, 22/25/38 yaw-rate sensor, 43 second terminal 30. Wheel sensors by system [B]: MK20 inductive, grey plugs; MK60 magnetoresistive, 12 V supply, 7/14 mA current pulses, blue plugs. MK20 front harness has a third (ground) wire, unused on MK60 [F].

### D7. Steering-angle sensor (LEW/LWS) plug [B, as printed]

| Pin | Function |
|---|---|
| 1 | KL30 (keeps counting turns with the ignition off) |
| 2 | "KL 87" (switched supply) |
| 3 | CAN high |
| 4 | CAN low |
| 5 | KL31 ground |
| 6 | TXD (D-bus) |

### D8. Cruise, clutch and brake circuits

| Circuit | 325i Touring (MS43/MS45) | M3 (MSS54), as fitted in this build |
|---|---|---|
| Cruise buttons | MFL right keypad → clock spring → FGR serial wire → X60004-27 | Same |
| Cruise speed reference | DSC → CAN (front-wheel average) | DSC → CAN (`STATUS_V_CAN`) |
| Engine speed reference (road) | DSC MK60 pin 8 → X60004-22 | Same |
| Brake light, 1st | Hall brake switch (KL R) → LSZ → X60004-24 | Same |
| Brake light, 2nd (test) | Switch → X60004-28 (BR/GN) | Move to X60004-34 |
| Brake to DSC | Switch → MK60 pin 41 | Same |
| Clutch to DME | Module pin 2 (BL/BR) → X60004-23 | Module pin 2 → gear switch pin 1 → pin 2 → X60002-20 (GR/BL); high only in gear, pedal up |
| Clutch to EWS (start interlock, US) | Module pin 4 (BL/SW) → EWS pin 8 | Same (keep) |
| Clutch module supply / ground | Pin 3 VI/GE 12 V (splice X205) / pin 1 BR/SW | Same; fit M3 module 61319122700 |

### D9. A/C and cooling-fan chain (both cars, any of the three DMEs)

| Step | Signal | Medium | Pins and parts |
|---|---|---|---|
| 1 | Refrigerant pressure | 0–5 V analog, 5 V supply from the IHK | Sensor on the high side next to the receiver/drier → IHKR/IHKA |
| 2 | A/C standby (AC), request (KO), compressor load (0–30 Nm), fan request/stage | K-bus | IHKR/IHKA → cluster |
| 3 | Same data | CAN | Cluster (gateway) → DME |
| 4 | Compressor relay | DME grounds coil | X60004-29 → K19 (61368373700) → compressor clutch |
| 5 | Electric fan | PWM 10–100 Hz | X60004-4 → output stage on fan (50 A fuse in the glovebox area) |
| 6 | Fan inputs | | Radiator-outlet sensor X60004-38/39; calculated catalyst temperature; road speed; battery voltage; A/C stage |
| 7 | Overheat (cluster lamp at 120 °C) | CAN | Fan overrun at 10 Hz |
| 8 | Heater water valve | IHK output | Valve (F62 feed per forum) |
| 9 | Auxiliary water pump (M3 valve 64118369807 only) | IHK output, switches ground | Pump from the same feed; IHK pin 6 on an M3 per forum; code `ZUSATZWASSERPUMPE = aktiv` |

### F2. Refrigerant pressure to fan stage (E46 IHKA, road speed under 50 mph) [B]

| bar | 8 | 9 | 11 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | >24 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Stage | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 |

PWM sensing ratio: 10 % = one-third speed; 90–95 % = full; below 10 % or above 95 % = off [B].

### D10. Crash chain

| Step | Event | Medium |
|---|---|---|
| 1 | MRS III detects a crash above any threshold; stores the crash telegram | MRS internal |
| 2 | Crash telegram | K-bus |
| 3 | Cluster forwards to the powertrain | CAN |
| 4 | DME stops the pump: MS43 drops the K96 coil ground (X60004-10). MSS54 has crash shut-off "EKP-Crash-Abschaltung" (0x7E); whether US software drops X60004-10 is unverified | DME output |
| 5 | LSZ turns on the hazards (`CRASH_WARNBLINKEN`); interior lights (`CRASH_KLEMME_58G_EIN`) | K-bus |
| 6 | BST fires at front threshold 2+ or the rear threshold, cutting the trunk-to-front B+ cable | MRS firing circuit ZK10/ZK15 |

### D11. E46 diagnosis socket (16-pin, driver footwell; E46 built from 06/2000)

| Pin | Function | Source |
|---|---|---|
| 7 | TXD II: DME (X60004-32) and EGS | [B] |
| 8 | TXD (D-bus, WS/VI): cluster (X11175-25, gateway to the K-bus modules), DSC, LWS | [B] |
| 16 | Battery + (generic OBD-II) | [F] |
| 4, 5 | Grounds (generic OBD-II) | [F] |
| 6, 14 | Not used on the E46 (no CAN at the socket) | [F][vendor] |
| 1 | KL15 (shown in a generic BMW DIS bus test; unconfirmed for the E46) | [B, generic] |
| 9 | TD engine-speed output from X60004-17? (unconfirmed) | inf. |

The socket cap bridges KL30 to TXD and TXD II [B]. A single-K-line cable needs pins 7 and 8 bridged.

### N1. Network topology (nodes and links) for the swapped Touring

**PT-CAN (twisted pair GE/RT high, GE/BR low; 2 × 120 Ω, 60 Ω total)**
- Node DME (MSS54): X60004-36 (H) / 37 (L). Terminator: BMW says "DSC + (cluster or DME)"; most likely not the DME (inf.).
- Node KOMBI (M3 cluster): X11175-9 (H) / 10 (L). Gateway CAN ↔ K-bus ↔ D-bus. Likely terminator (forum snippet).
- Node DSC (Touring MK60 or M3 MK60): pins 11 (H) / 15 (L). Terminator per BMW.
- Node LWS (steering-angle sensor): pins 3 (H) / 4 (L). Non-terminating (10–50 kΩ expected when isolated).
- Node EGS (GS20): absent on a manual; automatic-born Tourings keep an unused stub.
- Links: linear trunk joined by BMW "splice connections for twisted pair CAN" (WDS "Connector, CAN bus"); BMW's figure shows GS20 — DME — cluster with a spliced branch to LWS and MK60.

**Private buses**
- MK60 ↔ DSC sensor cluster (09/2001+ Touring, 09/2002+ M3): MK60 pins 25/29 ↔ sensor pins 1/2, plus pins 6/24 ↔ sensor 3/5.
- SMG ECU ↔ MSS54 local SMG-CAN (SMG donors only; unused).
- MS45 local CAN (pins 31/35) to the M56 pump controller (absent on the M54/MSS54).
- M-bus: IHKR ↔ 3 stepper motors (air distribution, fresh/recirc left and right), plug X613 3-pin; IHKA ↔ 4 motors.
- LIN: E46/3/4 mirrors from 03/2003 (GE/VI); AHL on 03/2003+ coupes.

**K-bus (single wire, about 12 V; WS/RT/GE at the cluster)**
- Nodes: KOMBI (X11175-14), LSZ, GM5, IHKR/IHKA, MRS III, EWS 3, SZM (X1869-23), MFL (audio/telephone part), radio/amplifier, PDC, rain/light sensor (AIC/RLS), seat memory, navigation/BM.

**D-bus (single WS/VI wire, more than 2.0 V)**
- OBD pin 8 ↔ KOMBI (X11175-25), DSC (MK60 pin 2), LWS (pin 6). Other K-bus modules are reached through the KOMBI gateway.
- TXD II: OBD pin 7 ↔ DME (X60004-32), EGS.

**Dedicated wires between nodes (not buses)**
- EWS → DME: ISN line X60004-33.
- MFL → DME: cruise data X60004-27.
- DSC → DME: rear-right wheel speed (MK60 8 → X60004-22).
- DSC → KOMBI: rear-left wheel speed (MK60 10 → X11175-19); ABS lamp (MK60 44 → X11175-22).
- LSZ → DME: brake-light signal (X60004-24).
- Brake switch → DME 2nd contact (X60004-34 MSS54 / 28 MS43); → DSC (MK60 41).
- Clutch → gear switch → DME (X60002-20 MSS54) / clutch → DME (X60004-23 MS43); clutch → EWS pin 8.
- SZM → DME: Sport X1869-17 → X60004-15; DME → SZM LED X60004-16 → X1869-18.
- SZM X521-2 → DSC (MK60 39): DSC button.
- DME → KOMBI (MSS54): X60004-1 → 2 (charge), 11 → 13 (oil pressure), 21 → 17 (oil level), 6 → 3 (terminal 50, inf.).
- DME → K19 (X60004-29); DME → fan stage (X60004-4); DME → K96 (X60004-10).
- Brake-fluid switch → KOMBI 20 and DSC 9; park-brake switch → KOMBI 23 and DSC 27.
- Pad-wear loop → KOMBI 24; coolant level → KOMBI 26; fuel senders → KOMBI 11/12 and 15/16.

### D12. Tool32 checks per circuit (SGBD names as documented)

| Circuit | SGBD → job | Result to watch |
|---|---|---|
| Oil pressure at the cluster | KOMBI46(R) → `STATUS_IO_LESEN` | `STAT_OELDRUCK_EIN` follows the switch (key on vs running) |
| Brake fluid, park brake, coolant level | KOMBI46(R) → `STATUS_IO_LESEN` | `STAT_BREMSFLUESSIGKEIT_EIN`, `STAT_HANDBREMSE_EIN`, `STAT_KUEHLMITTELSTAND_EIN` |
| Fuel senders | KOMBI46R → `STATUS_TANKINHALT_LESEN`, `STATUS_ANALOG_LESEN` | Litres per sender, total, `STAT_RESERVE`; ADC values |
| CAN lamps from DME/DSC | KOMBI46 → `STATUS_CAN_SIGNALE_LESEN` | Check-engine, cruise, ASC, EBV, overheat, fan stage, km |
| Sport, brake, clutch, A/C at the DME | MSS54DS0 → `STATUS_DIGITAL` | `STAT_FDYN_EIN`, `STAT_BLS_EIN`, `STAT_BLTS_EIN`, `STAT_KRAFTSCHLUSS_EIN`, `STAT_AC_EIN`, `STAT_KO_EIN`, `STAT_MFL1-4_EIN` |
| Bus partners seen by the DME | MSS54DS0 → `FS_LESEN` | No 0x84/0x85/0x86 (DSC/LWS/KOMBI timeouts), no 0x56 |
| Switch centre power | SZM46 → `STATUS_IO` | Terminals R/15/50 on, terminal-30 voltage |
| Climate | IHKR46 → `STATUS_ANALOGEINGAENGE`, `STATUS_IO` | Pressure in bar; `STAT_ZUSATZWASSERPUMPE_EIN`; `STAT_KLIMABEREITSCHAFT_EIN` |
| Levelling | LSZ_2 → `XENON_VORHANDEN`, `LWR_VORHANDEN`, `STATUS_LESEN` | Coded flags; front and rear sensor voltage 0–5 V |
| Cruise buttons at the wheel | MFL → `STATUS_LESEN` | `STAT_TEMPOMAT_VARIANTE`, button states |

## Key sources
- BMW technical-training collection (archive.org item `BMWTechnicalTrainingDocuments`): ST034 E46 Driver Information and Passive Safety; ST040 Bus System Troubleshooting, 2001 Changes, E46 IHKR; ST041 M3 Complete Vehicle and Engine Electronics 1–3; ST043 2002 Update; ST047 E46 FL; ST051 Introduction to Bus Systems; ST052 03a/03b; ST054 IHKA E46 and Output; ST055 MS42/MS43 and MS S54; ST056 E46 DSC; ST401b 3 Series Bus Charts.
- SGBD exports: `MSS54DS0`, `KOMBI46`, `KOMBI46R`, `SZM46`, `IHKA46`, `IHKR46`, `LSZ`, `LSZ_2`, `MRS3`, `MFL`, `MS430DS0`, `MS450DS0` at [emdzej/ediabasx-docs-sgbd](https://github.com/emdzej/ediabasx-docs-sgbd/tree/main/docs/sgbd).
- [NikolaiD's 2002 E46 M3 NCS parameter list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf); [heinzboehmer's MK20→MK60 mapping](https://nam3forum.com/forums/filedata/fetch?id=189181); [newTIS SZM pinout screenshot, NAM3 243243](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/243243-depinning-center-control-switch); [bmwgm5 cluster pinout](https://www.bmwgm5.com/E46_IKE_Connections.htm); [CarCluster bench pinout](https://github.com/r00li/CarCluster/blob/main/Misc/README_WIRING_BMW_E46.md); ETK via bmwfans.info (pages linked above).
