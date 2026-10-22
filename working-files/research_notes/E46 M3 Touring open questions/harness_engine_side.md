# M3 engine harness and MSS54/MSS54HP DME into a US 2001–05 E46 325i Touring: connectors, pins, power, grounds and swap-harness options

Unless marked "(snippet only)", every finding below was read on the page or file itself (e46fanatics threads were rendered in headless Chromium; the spreadsheet was downloaded as .xlsx; the Kassel chart and Redline photo were viewed as images; the BMW training module was read as a PDF; ETK data came from bmwfans.info parts pages). NewTIS (Cloudflare "Just a moment…", HTTP 403) and the bmwteka.com WDS mirror (connection reset through the proxy, DNS failure via WebFetch) could not be read, so no claim below rests on them. Wire colours use BMW codes: BR brown, GN green, BK black, RT red, GE yellow, BL blue, GR grey, OR orange, WS white, VI violet.

**Important correction to the existing guide.** The guide's "X60004 pins 11/21/1/2 → X6011 pins 3/5/4/6" row describes an **MS42→MS43** re-pin (an M54 swap into a 1998 323i), not an S54 swap. For an S54 into an MS43 Touring the moves run the other way (X6011 → X60004), and the start signal lands on X60004 pin **6**, not pin 2. Details are under Q2.

## Q1. Which DME connectors do the MSS54/MSS54HP, MS43 and MS45 use, what does each carry, and which mate to the body harness?

### Takeaway
All three DMEs use the same five-module Siemens connector: X60001 (9-pin), X60002 (24-pin), X60003 (52-pin), X60004 (40-pin) and X60005 (9-pin), 134 pins in total on the MSS54. The pin assignments differ throughout. X60004 is the body-harness "vehicle interface". X60001, X60002, X60003 and X60005 arrive with the engine harness, along with a set of small E-box connectors (black 8-pin X6011, white 8-pin X6053, a black 4-pin and a 3-pin plug) and the E-box mini fuse box. Several of those also cross to the body.

### Cited Findings
- BMW's US training module for the MS S54: "The 134 pin MS S54 Engine Control Module is manufactured by Siemens … uses 5 modular connectors": X60001 9-pin, X60002 24-pin, X60003 52-pin, X60004 40-pin, X60005 9-pin. Test with the Universal Adapter Set (break-out box) 90 88 6 121 300 — [BMW ST055 MS S54 (archive.org)](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- A forum member's (nextelbuddy's) spreadsheet transcribes BMW-format pin-assignment tables ("Pin | Type | Description / Signal type | Connection / Measuring notes") for the MSS54, MS42, MS43, MS45 and MS45.1. All of them list the same five modules: X60001 9-pin black, X60002 24-pin black, X60003 52-pin black, X60004 40-pin black, X60005 9-pin black — [MSS54/MS4x pinout spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing) (linked by its author in [Kalim's thread #750](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)). This is a third-party transcription, so treat it as secondary.
- **MSS54 per module** (same spreadsheet):
  - **X60001:** pin 1 terminal 15 to the injector relay; 2 and 9 EDK (electric throttle actuator) supply and negative activation; 4, 5 and 6 ground; 7 terminal 30 via fuse F102; 8 supply from the "fuse carrier, engine electronics"; 3 not used.
  - **X60002:** O2 heater and signal pins 1, 7, 13–16, 18, 19; 5 ground; 10 exhaust temperature sensor; 11 fuel pump relay 1 "USA only"; 12 E-box fan; 20 gear-recognition switch; 23 main (DME) relay activation.
  - **X60003:** engine sensors and actuators, including injectors 33–38, oil-pressure switch 26, oil level 39, alternator terminal 61 on pin 13, VANOS, knock, MAF, idle valve, EDK potentiometers, and the brake-booster jet-pump valve 51.
  - **X60005:** coils, with pins 1/2/3/6/7/9 driving coils 1/2/3/5/6/4, and pin 5 ground.
  - **X60004:** the vehicle interface; the pins are in Q2's table.
  — [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
- **MS43 per module:**
  - **X60001:** 1 terminal 15 to the injector relay; 4, 5 and 6 ground; 7 terminal 30 ("B+ terminal"); 8 fuse-carrier supply; 2, 3 and 9 not used.
  - **X60002:** O2 sensors; 3/4/6 CAN low, CAN high and TxD to the transmission control unit; 23 main relay.
  - **X60003:** its own layout, for example oil temperature 27/28, the M54 throttle 7/10/19/20/43/44, map thermostat 45, DISA 49, DM-TL heater 51 (USA), secondary-air valve 52, and the oil-pressure switch pin "not used".
  - **X60005:** coils on 1, 2, 3, 7, 8, 9.
  — [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
- **MS45 (sheet "MS45 903") and MS45.1:**
  - **X60001:** pin 3 is TxD to the transmission.
  - **X60002:** separate O2 heater and signal pins plus CAN to the transmission control unit.
  - **X60003:** completely re-arranged. Injectors on 6/7/8/11/13/26, oil-pressure switch 16, alternator bi-directional interface 19, oil level 50 (MS45.1), local CAN high 38 (MS45).
  - **X60005:** coils in yet another order, with pins 1/4/6/7/8/9 driving coils 5/3/1/2/4/6.
  — [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
- Swapper e34m5freak199 compared a 323i (MS43-configured) and an M3 harness:
  - X5 (X60005) "is irrelevant to a swap… if you get a complete engine harness and box this simply plugs in there".
  - "X4 – This runs from DME to the Body".
  - He also compared X2 and X1 and found M3-only wires on them: X2 pins 5, 7, 10, 11, 16, 18, 19, 22, with the 323 having pin 20; X1 pin 2 "Fat Red" and pin 3 "White with purple stripe".
  — [e46fanatics #1](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
- "I only had to re-pin the X60004 connector on few places, everything else is just plug and play" (HakenTT, 2004 S54 into a 2000 323i) — [e46fanatics #6](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
- Kalim (2003 325i sedan): "the engine harness connectors get pulled from the DME. Harness stays with the motor". His stated plan was to "Make the MSS54 DME interface with the sedan body harness without hacking the OEM wiring up" — [e46fanatics, Kalim thread (first post, shown on page 30)](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-30)
- e34m5freak199: make sure the engine harness is complete. "Did you get the mini fuse box with it? That plug should be in there along with another 3 pin plug which is VERY IMPORTANT. It has 3 wires, 2 for revers to gearbox and 1 really thick wire which is DME relay, nothing will work without it." — [e46fanatics #27](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
- On an M3 race car, "you have three connectors that went into the E box". Two were identified:
  - **Black 8-pin:** pin 1 BK "starter run wire from ignition switch"; pin 2 GN "+12v power supply to oil level sensor"; pin 7 GR "connects to the white 8 pin connector"; pin 8 GE/BK "connects to x60003 pin 19".
  - **White 8-pin:** "Almost all wires are red". The NAM3 moderator identified it as **X6053** and noted that TIS/WDS lists X60003 pin 19 as "not used", yet "it's definitely populated by the yellow/black wire that comes from that black connector".
  — [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/116033-s54-wiring-harness-identification)
- nextelbuddy (MSS54HP and M3 engine harness in an MS45.1 ZHP): "X6011 is the larger 8 pin plug and it looks very similar to an MS-45.1 it only has two wires which are for the starter and some other wire.. and then two additional wires for gear position sensor and TPMS. No alternator, oil level or oil pressure signal wires." Also "The other smaller 4-pin plug … one of the pins is a black and purple wire which is for the EKP fuel pump relay" — [NAM3 #9](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)
- "X6011 appears to be a plug in the same box as the DME" — [e46fanatics #15](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/). A later poster calls it "the X6011 black connector in the DME box" — [e46fanatics #5](https://www.e46fanatics.com/threads/manual-swap-wiring-with-mss54-dme.1316134/)
- Kalim: the fuel-pump trigger wire "is present in the DME compartment (e-box)… Check the 4-pin black plug for that wire" — [e46fanatics #746](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)
- **ETK harness part numbers.** The US M3 engine harness has three modules:
  - "engine module": 12517831646 to 09/2004, then 12517836015;
  - "engine trans. module": 12517831756 to 09/2003, then 12517835540; SMG versions 12517831659 and 12517836378;
  - "engine ignition module": 12517831537.
  — [ETK M3 engine module](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/engine_wiring_harness_engine_module/), [trans. module](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/wiring_harness_engine_trans_module/), [ignition module](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/wiring_harness_engine_ignition_module/)
  The US 325i Touring's equivalents are all different parts:
  - engine module: 12517513554 to 03/2003, then 12517523220;
  - trans. module, manual: 12517506794 to 09/2002, 12517518041 from 09/2002 to 03/2003, then 12517523223;
  - ignition module: 12511440006 to 09/2002, then 12517551908.
  — [ETK 325iT engine module](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/engine_wiring_harness_engine_module/), [trans. module](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/wiring_harness_engine_trans_module/), [ignition module](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/wiring_harness_engine_ignition_module/)
- Kassel's chart shows a BMW E-box photo with X60004 and X60005 labelled, and lists modifications only for "X6004" (X60004) — [Kassel chart](https://www.kasselperformance.com/wp-content/uploads/2016/01/E46S54Wiring.png)

### Inferences
- Treat X60004 as the only DME module that stays with the Touring. X60001/2/3/5, the E-box mini fuse box, and the X6011/X6053/4-pin/3-pin plugs come with the complete M3 engine harness. Each small plug's body-side mate must be checked pin by pin, because they carry body circuits:
  - X6011: starter terminal 50, oil-level supply, clutch/gear-recognition path, and the MS43 lamp wires;
  - 4-pin: fuel-pump trigger;
  - 3-pin: reverse lights and the heavy DME-relay feed.
- The M3 X60002 also carries body-bound circuits: X60002-11 (US fuel-pump output) reaches the body through the E-box plugs, and X60002-20 (gear recognition/clutch) is fed from the clutch switch in the body. That is why e34m5freak199 described X1/X2 as partly "body harness".
- The MS43, MS45 and MSS54 layouts of X60003 and X60005 are incompatible: different injector and coil pin orders. Never mix a DME with a harness from another DME family.
- The M3 harness's "engine trans. module" changes at 09/2003, about when the MSS54HP arrived. Keep the donor's DME and the donor's harness as a matched pair.

### Gaps
- No published MSS54 vs MSS54HP pinout comparison was found, and no MSS54HP pin list was seen. ETK only shows the harness and DME part-number changes at 09/2003 and 09/2004.
- Which harness (engine or body) BMW assigns the E-box fuse carrier and the X6053 counterpart (X60531) to could not be confirmed from WDS. bmwteka.com and NewTIS were unreachable or blocked.
- Full pin lists for X6011, X6053, the 4-pin and the 3-pin E-box plugs (M3 and 325iT) were not obtained from BMW sources; only forum descriptions are available.

## Q2. Pin-level differences between a US 325i (MS43 or MS45) and a US M3: what to move, add or leave empty

### Takeaway
On X60004, most circuits sit on the same pins in all three DMEs and need no work: pedal, CAN, TxD, EWS, terminal 15/F29, A/C relay, electric fan, secondary-air relay, speed, wheel speed, MFL/cruise and radiator-outlet sensor. Work for both Touring generations:
- Move the brake-light-test wire from pin 28 to pin 34.
- Move the DM-TL heater wire into pin 18 (from X6011 pin 7 on MS43 cars, from X60004 pin 2 on MS45 cars).
- Clear pin 23 (clutch); the M3 routes the clutch signal through the gear-recognition switch to X60002 pin 20.
- Optionally add Sport pins 15/16.

The cluster warnings differ by generation. On MS43 cars, oil pressure, oil level, charge lamp and start signal run through the E-box plug X6011; move them into X60004 pins 11/21/1/6. On MS45 cars those warnings come over CAN. With an MSS54 at least the oil-pressure lamp must be hard-wired from X60004 pin 11 to cluster pin 13; the charge lamp and oil level can be wired too, or coded as CAN.

### Cited Findings
**What builders did (first-hand):**
- 1998 Australian 323i with an MS43-configured body harness, S54 swap. He "moved 4 wires round" on X60004:
  - "Pin 1 - signal battery charge indicator - battery light on cluster";
  - "Pin 3 - didnt wire - i deleted air pump";
  - "Pin 6 - engine start feedback - again from cluster. It started without this";
  - "Pin 11 - oil pressure again to cluster";
  - "Pin 15 and 16 … for the sport button, only on m3";
  - "Pin 21 oil level sensor. Same as ms42 but different place on ms43";
  - "Pin 34 - brake switch. Move Pin 28 from ms42/43 to pin 34";
  - "If you dont want sport button, NO WIRES Need to be run to cabin."
  — [e46fanatics #19](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
- Same builder's harness comparison at X4: the MS43-configured 323 harness lacks pins 1 (BL), 3 (BR), 6 (BK/BL), 11 (BR/GN), 15 (BK/RT with yellow dots), 16 (BK/GN with yellow dots), 21 (WS/GN) and 34 (BR/GR). The M3 harness lacks 17, 23 and 28. "EVERYTHING ELSE IS EXACTLY THE SAME PIN SPOT AND COLOUR" — [e46fanatics #1](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
- **Direction of the X6011 moves.** The guide's mapping (oil pressure "take from x4 pin11 and put to Pin 3 on x6011", oil level 21→X6011-5, battery 1→X6011-4, start feedback "from pin 2 on x4 and move to pin 6") was posted "Going off memory on my m54b30 swap". That swap was an MS42→MS43 conversion, and the same post says "the ms42 and mss54 are allot more closer in how they wire than the ms43" — [e46fanatics #27](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/). The MS42 X60004 list confirms the starting point: pins 1 battery-charge lamp, 2 engine-start feedback, 11 oil-pressure switch, and 21 oil level, all to the cluster — [spreadsheet, MS42 sheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
- 2001 325iT (MS43) with the M3 harness. Neither cluster showed the oil or battery lamp. X60004 pin 11 was "Vacant". After pre-loading the wagon's VIN in newTIS: "The oil pressure switch (B6231) does NOT go to the DME… On my wagon the oil switch goes to X6011 pin 3 in and out". On the M3 the signal passes through the DME ("X60003 Pin 26 in and X60004 pin 11 out"). He joined the M3 harness's X60003-26 wire to the X6011 cluster wire and "now the red oil light comes on". Later: "it took me 15 minutes to establish the battery light" — [e46fanatics #19, #26, #29](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/). Another member in the same thread: "the battery light on MS43 cars doesn't go through the DME but it does on the M3s. On the MS43 the battery light also goes through the x6011 IIRC" — [#27](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)
- George Hill (swap shop), quoting ISTA:
  - **M3:** "F34 -> X11175 pin #5 KOMBI (GN/BL); X11175 Pin #13 KOMBI -> X60004 Pin#11 DME (BR/GN); X60003 Pin #26 DME -> X6231 Oil Pressure switch (BR/GN)".
  - **"A ZHP":** "X11175 Pin #13 KOMBI -> X6011 #3 (BR/GN); X6011 #3 -> X6231 Oil Pressure switch".
  — [NAM3 #10](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)
- MSS54HP in a 2003 ZHP (MS45.1 body) with an index-24 M3 cluster:
  - "my alternator and oil sensors are canbus since my ZHP was canbus for those sensors"; cluster pin 13 "is empty on mine".
  - Fix: "I just ran a wire from x60004 pin 11 to the cluster plug pin 13. used NCS export to change back to oil pressure via CAN bus not active... and now my oil light and alternator light are both on with the engine off."
  - He also notes the stock MSS54HP software "does support alternator via canbus", unlike the older CSL software he had run.
  — [NAM3 #4, #7, #9, #11](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)
- George Hill: "The alternator light is powered through the cluster and grounded by the DME whenever the alternator is not charging"; "The oil pressure switch closes at .5bar"; a lamp that goes out before the engine starts means it's "either no coded correctly to function over CAN or because the wiring wasn't added during the swap" — [NAM3 #6](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)
- nextelbuddy's "MS43 to MSS54 Wiring" sheet:
  - Sport signal: switch-centre (SZM) pin 17 → ADD X60004-15. Sport LED: SZM pin 18 → ADD X60004-16.
  - Brake signal: "X60004 pin 28 - Brown/Green" → MOVE to pin 34.
  - Oil pressure: X60004-11 → ADD to cluster black plug pin 13.
  - Oil level: X60004-21 → cluster pin 17 ("Should work via can bus but add anyway").
  - Alternator: X60004-1 → cluster pin 2.
  - DM-TL heater (BK/RT): MSS54 X60004-18; MS43 "X6011" pin 7 ("black 8 PIN connector"). DM-TL pins 1 and 3 go to X60004-20 and -30 on both. DM-TL power: "F3 Fuse – 20A – X8680 (Fuses in DME BIN)".
  - Clutch switch (all non-M sheets): ground BR/BK, "DME Signal" BL/BR → X60004 pin 23, power VI/GE, EWS signal BL/BK → EWS pin 8.
  — [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)

**Kassel chart ("S54Swap E46 Wiring Modifications"):**
- **MS43 cars (325, 330, 01–02):**
  - MOVE pin 28 (BR/GN) BLTS to 34.
  - ADD pin 11 (oil pressure) "to Pin 14 of cluster"; pin 15 Sport and 16 Sport LED (optional); pin 21 (oil level) to cluster pin 17.
  - REMOVE: N/A.
- **MS45 cars (325, 330, 03–):**
  - MOVE 28 (BR/GN) BLTS to 34; pin 2 (BK/RT) DMTLH to 18.
  - ADD: N/A.
  - REMOVE pin 5 (BK/GE), pin 15 (BK/RT), pin 19 (BR/OR).
- **MS42 cars:** move 28→30 and 30→20 (DM-TL); add the six pedal wires; remove pin 1 (BL, "went to cluster Pin 2") and pin 2 (BK/GN, "went to starter 30h").
— [Kassel chart](https://www.kasselperformance.com/wp-content/uploads/2016/01/E46S54Wiring.png)

**Conflicts between sources:**
- Cluster pin for oil pressure: Kassel says 14; ISTA (via George Hill) and nextelbuddy's working fix say X11175 pin 13 ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)).
- Kassel's MS45 column needs no added wires. nextelbuddy's MS45.1 car needed the oil-pressure wire added.
- Kassel's MS42 column removes pin 1 (charge lamp). Two builders and the MSS54 pin list keep it (pin 1 = "Signal, terminal 61 → instrument cluster").

**BMW pin lists for X60004** (from the spreadsheet's MSS54, MS43, MS45 ("903") and MS45.1 sheets; [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)). The action column combines the builder and Kassel sources above.

| Pin | MSS54 (US M3) | MS43 (325i to 02/03) | MS45 / MS45.1 (325i from 02/03) | Action on the Touring's body side |
|---|---|---|---|---|
| 1 | Terminal 61 (charge lamp) to cluster | Not used (lamp via X6011-4) | Not used (CAN) | MS43: move from X6011-4. MS45: add wire to cluster pin 2, or code CAN (works with stock MSS54HP) |
| 2 | "Engine start signal feedback" (terminal 30h) | Not used | DM-TL heater (BK/RT) | MS45: move BK/RT to 18. No builder used MSS54 pin 2 |
| 3 | Secondary-air pump relay | Same | Same | None |
| 4 | Electric fan | Same | Same | None |
| 5 | **Ground** (ECM ground per BMW ST055) | Not used | MS45: secondary-air HFM ground (BK/GE, "3.0 USA") | MS45: remove BK/GE (Kassel). See Q4 about a ground here |
| 6 | Terminal 50 signal to cluster | Not used (start feedback via X6011-6) | Not used | MS43: move from X6011-6 (optional; one car "started without this") |
| 7–9, 12–14 | Pedal-position sensor | Same | Same | None ("MS43 and MS45 pedal and wiring is exactly the same", [HakenTT #13](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)) |
| 10 | Fuel-pump relay 1, "not USA" | Fuel-pump relay | MS45: not used; MS45.1: fuel-pump relay | Out of scope (fuel pump) |
| 11 | Oil pressure to cluster | Not used (switch via X6011-3) | Not used | MS43: move from X6011-3. MS45: add wire to cluster X11175-13 and turn off "oil pressure via CAN" |
| 15 | Sport switch signal | Not used | Secondary-air HFM signal (BK/RT, US 3.0) | MS45: remove. Optional: add Sport from switch centre pin 17 |
| 16 | Sport LED | Not used | Not used | Optional: add from switch centre pin 18 |
| 17 | Speed signal to data-link connector | Same | Same | None (e34m5freak199's donor harness lacked it) |
| 18 | DM-TL heater (USA) | Exhaust-flap valve ("M54 3.0 l only") | MS45: not used; MS45.1: exhaust flap | Insert DM-TL heater wire (MS43 from X6011-7, MS45 from pin 2); remove any flap wire first |
| 19 | Not used | Not used | E-box fan activation (BR/OR) | MS45: remove (Kassel) |
| 20 / 30 | DM-TL (USA) | DM-TL | DM-TL (TIS swaps the "pump"/"valve" labels) | None; builders keep 20 and 30 |
| 21 | Oil level to cluster | Not used (via X6011-5) | Not used (CAN) | MS43: move from X6011-5 (or add wire to cluster pin 17). MS45: add wire, or code CAN |
| 22 | Rear-right wheel speed | Same | Same | None |
| 23 | Not used | Clutch switch (manual) | MS45.1: clutch switch | Remove; clutch goes via the M3 gear-recognition switch to X60002-20 |
| 24 | Brake-light switch (via LCM) | Same | Brake-light switch | None |
| 25 | Not used | Not used | EAC sensor (MS45) | Not used by the MSS54 |
| 26 | Terminal 15, fuse F29 | Same | Same | None |
| 27 | MFL data (cruise) | Same | Same | None |
| 28 | Not used | Brake-light switch (BR/GN) | Brake-light test (BR/GN) | Move to 34 |
| 29 | A/C compressor relay | Same | Same | None |
| 31 / 35 | Not used | Not used | MS45: local CAN low/high to the fuel-pump control (EKPS) | Out of scope (fuel pump) |
| 32 | TxD diagnosis | Same | Same | None |
| 33 | EWS | Same | Same | None (an EWS-deleted DME ignores it) |
| 34 | Brake-light switch | Not used | Not used | Receives the pin-28 wire |
| 36 / 37 | CAN high / low | Same | Same | None |
| 38 / 39 | Radiator-outlet temperature sensor | Same | Same | None |

**E-box plug X6011 (black 8-pin):**
- MS43 body side: pin 3 oil pressure (BR/GN, [snaponbob](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)); pins 4/5/6 charge lamp, oil level and start feedback (inferred from the MS42→MS43 mapping, [#27](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)); pin 7 DM-TL heater ([spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)).
- M3 engine-harness side: pin 1 starter, 2 oil-level supply, 7 GR, 8 GE/BK to X60003-19 ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/116033-s54-wiring-harness-identification)).
- MS45.1: "out of eight pins only two were used" ([NAM3 #9](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)).

**Clutch and X60002:**
- With an MSS54, "I have to wire in the gear position switch inline between the clutch switch and DME 6002 Pin 20". The M3 diagram's clutch wire colour is GR (grey). Another member read the diagram as "pin 2 of the clutch safety switch to pin 7 of the X6011 black connector in the DME box" — [e46fanatics #2, #5](https://www.e46fanatics.com/threads/manual-swap-wiring-with-mss54-dme.1316134/)
- The MSS54 X60002 pin 20 is "Signal Switch, gear recognition"; the MS43 has no such pin — [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
- e34m5freak199's SMG donor "is Missing Pin 20 which is on the 323 harness" at X2 — [#1](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)

**X60003:**
- The guide's "pin 19 populated" claim is confirmed: populated by GE/BK from the black 8-pin plug, although TIS/WDS says not used — [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/116033-s54-wiring-harness-identification)
- snaponbob's 2001 325iT had X60004 pin 7 populated with BR/GN and he read it as "not used". The spreadsheet's MS43 list shows pin 7 is the pedal-sensor ground (BR/GN pedal ground → X60004-7), so that wire is expected — [e46fanatics #19](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/); [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)

**Source quality notes:**
- "The x60004 is not identical across different models of the E46, electrically" (AndreBXP). snaponbob found the Bentley's ELE-259 misleading, and newTIS changed what it showed once his wagon's VIN was entered — [e46fanatics #18, #8, #26](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)
- Out of scope, pins only: the 2017 asker in post #743 asked about "Pin 10 on DME X60004" for the fuel-pump EKP (MS45.1 donor car). Kalim says the SW/VI trigger "is present in the DME compartment (e-box)" — [e46fanatics #743, #746](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)

### Inferences
**Practical move list for an MS43 Touring (built to 02/2003), body side, in the E-box:**
1. X6011-3 → X60004-11 (oil pressure).
2. X6011-4 → X60004-1 (charge lamp).
3. X6011-5 → X60004-21 (oil level).
4. X6011-6 → X60004-6 (start/terminal 50 to cluster; optional).
5. X6011-7 (BK/RT DM-TL heater) → X60004-18.
6. X60004-28 → X60004-34 (brake-light switch).
7. Remove the clutch wire from X60004-23 and route it into the M3's gear-recognition path (reported to be body-side X6011-7, once the DM-TL wire has left it).
8. Optionally add X60004-15/16 from the switch centre for the Sport button.

Keeping X60003-26 on the DME and moving the cluster wire into X60004-11 preserves the M3's factory pass-through. snaponbob's splice took the oil-pressure signal away from the DME, which may set a DME fault (not verified).

**For an MS45 Touring (from 02/2003):**
1. Move 28 → 34 and 2 (BK/RT) → 18.
2. Pull 5, 15 and 19 if present. Pin 5 matters: it is an MSS54 ground, so a leftover secondary-air HFM wire there would be grounded.
3. Pins 23 and 31/35 as in the table.
4. Hard-wire X60004-11 → cluster pin 13 and turn off "oil pressure via CAN" in the M3 cluster.
5. For the charge lamp and oil level, either hard-wire 1 → cluster pin 2 and 21 → cluster pin 17, or code them as CAN. CAN is confirmed only for alternator and oil level with stock MSS54HP software. For an early non-HP MSS54, hard-wiring is the safer assumption.

**Other notes:**
- Verify cluster pin 13 vs 14 against the M3 cluster's own X11175 before inserting a terminal. ISTA and a working car support pin 13.
- The guide's statement that a 323i swap "moved four wires from X60004 to body connector X6011" should be rewritten as the reverse direction for this conversion, with start feedback ending at X60004 pin 6.

### Gaps
- No BMW-source pin list for the 325iT's X6011 pins 4, 5 and 6 was obtained. Their roles are inferred from one builder's MS42→MS43 mapping plus "IIRC" support from a second.
- Whether a US MS45 325i (as opposed to a 330i or ZHP with MS45.1) has the secondary-air HFM wires at X60004 pins 5 and 15: the spreadsheet tags them "3.0 USA".
- The exact body-side termination of the M3 clutch/gear-recognition path (X6011-7 vs X6053) is only one forum member's reading of the diagram.
- Whether the non-HP MSS54 supports CAN for the charge lamp and oil level was not found.
- Kassel's MS43 column omits the charge lamp, start signal, DM-TL heater and clutch. Kassel's reasoning for its MS42 "remove pin 1" could not be checked.

## Q3. The M3's extra power feeds, fuses and relays, and whether the Touring is prewired

### Takeaway
The S54's DME power architecture matches the 325i's:
- B+ to X60001-7;
- terminal 15 via F29 to X60004-26;
- the K6300 main relay (switched by X60002-23) feeding X60001-8 and the loads;
- a K6327 injector relay;
- a K6304 secondary-air relay;
- an engine fuse block in the E-box.

BMW's catalog lists the same relay part numbers and the same E-box relay carrier for the US M3 and the US 325i Touring. The genuinely M3-only feeds are the throttle actuator (powered by the DME itself), the US cycled fuel-pump relay or EKP (out of scope), SMG items, and an E-box fan that exists only on automatic, SMG or hot-climate cars. Kalim reports that unused fuse-box slots are half-wired (power side only). He added nothing to his MS45.1-era car.

### Cited Findings
- **Post #743 (Mr.ZHP, 13 Mar 2017)**, 2002 M3 into a 2004 330i MS45.1: "M3s have additional Fuses that goes to 3 different slots in fuse box how am i going to tackle them? Just add the fuses? They are prewired?"
  - **Kalim (#744):** "Your fuse box will usually be half wired (power wire only) in positions that aren't normally used on your chassis. You'll need to insert a contact if you want to add a fuse to power something."
  - **Kalim (#746):** "As for the fuse box, I didn't need to add anything. MS45.1 cars are very close to M3s in terms of wiring."
  — [e46fanatics page 38](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)
- **BMW ST055 (MS S54):**
  - "KL30 - Battery Voltage: B+ is the main supply of operating voltage to the ECM."
  - "The power supplies (KL15 and ECM Relay) are fused… The fuses are housed in the Engine Fuse Block located in the Electronics Box." The diagram shows ECM fuses F1 30A, F2 30A, F3 20A, F4 30A and F5 30A, and upstream F109 80A and F114 50A.
  - "KL15 (fused) supplies voltage to the Engine Control Module Relay and the Fuel Injector Relay."
  - The ECM relay supplies the ECM, fuel injector relay, idle air actuator, evaporative emission valve, fuel pump relay, ignition coils, DMTL, camshaft sensors, hot-film air mass meter and oxygen-sensor heaters.
  - The ECM holds the relay on a few seconds after KL15 off.
  - The ECM relay is "located in the Electronics Box".
  — [BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- **TIS-format pin lists:**
  - MSS54: X60001-7 "Terminal 30 – Fuse F102"; X60001-8 "Voltage supply – Fuse carrier, engine electronics"; X60004-26 "Terminal 15 – Fuse F29"; X60002-23 main relay; X60001-1 terminal 15 to "Relay, fuel injectors"; X60001-2/-9 EDK (throttle actuator) supply and negative activation.
  - MS43: X60001-7 "Terminal 30 – B+ terminal", plus the same 8, 26, 23 and 1, with no EDK pins.
  - MS45: X60001-7 F102; X60001-8 "Terminal 87 – fuse carrier".
  - MS45.1: X60001-7 "A2076 B+ potential distributor".
  — [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
  - Corroboration that the MS43 gets switched +12 V from F29 at X60004-26 and B+ at X60001-7: [HP Academy forum](https://www.hpacademy.com/forum/cam-control-tuning/show/ms43-ecu-with-m54-powered-bmw-e30) (snippet only)
- **ETK relays, US M3:**
  - K6300 DME relay: "Relay, make contact, sky-blue" 61366915327, holder 61131389111 — [K6300](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/relay_dme_mss54_k6300/)
  - K6327 injector relay: white-green 61368373700 — [K6327](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/relay_for_injectors_k6327/)
  - K6304 secondary-air pump relay: "Relay changer salmon red" 12631742690 — [K6304](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/secondary_air_injection_pump_relay_k6304/)
  - The M3's relay index also lists "Relay for fuel pump 1 K96", "Relay for fuel pump, cycled", "Relay for hydraulic pump SMG K5360" and "Relay for a/c compressor K19" — [M3 vehicle electrical index](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/)
- **ETK relays, US 325i Touring:**
  - "Relay DME-MS43 K6300" and "Relay DME-MS45 K6300": both 61366915327 (sky-blue) — [MS43 K6300](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/vehicle_electrical_system/relay_dme_ms43_k6300/), [MS45 K6300](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/vehicle_electrical_system/relay_dme_ms45_k6300/)
  - K6327: 61368373700 — [link](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/vehicle_electrical_system/relay_for_injectors_k6327/)
  - K6304: 12631742690 — [link](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/vehicle_electrical_system/secondary_air_injection_pump_relay_k6304/)
  - Plus K96, K19, a backup-light relay K6325 (61368364582, not in the M3 list) and "Relay for hydraulic pump SMG K6318" — [325iT index](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/vehicle_electrical_system/), [K6325](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/vehicle_electrical_system/relay_for_backup_light_k6325/)
- **E-box fan.** In both cars' ETK "Control unit box" the "Cover with blower" (12907571019 to 09/2003, then 12907570074) is listed only "For vehicles with Automatic transmission (S205A) Or Sequential manual transmission (SMG) (S206A) Or Hot-climate version (S823A)". Other cars get the plain "Cover" 12907534511 — [M3 control unit box](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/control_unit_box/), [325iT control unit box](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/control_unit_box/). The MSS54 drives an E-box fan from X60002-12; the MS45 drives it from X60004-19 — [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
- **Glovebox fuse list (generic E46, not M3-specific)** from an aggregator:
  - F8 5A "Sequential mechanical gear" and F22 5A "[S54]: Sequential mechanical gear box" (SMG);
  - F23 5A "Auxiliary water pump";
  - F29 5A DME "(BMS46, MS42, MS43, MSS54)";
  - F30 7.5A "Oil level sensor, Alternator…";
  - F34 5A "Instrument cluster control unit, Fuel pump control (EKPS) [only MS45]";
  - F36 50A "Secondary air pump relay"; F37 50A "Electric fan";
  - F54 15A "Fuel pump relay 1" (MS45: EKPS 20A).
  — [StartMyCar 2004 M3 fuse box](https://www.startmycar.com/bmw/m3/info/fusebox/2004). Aggregator data, so not authoritative.
- The M3 heater valve "also has a pump attached… The pump requires 2 wires not present on non m" (a 1998 323i) — [e46fanatics #19](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
- "Same fuse for an M3 as a 325it" (F34 for the warning lamps); F34 "powers the entire instrument cluster" — [e46fanatics #9, #10](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)
- Out of scope, noted only: Kalim says "The EKP module (tall black relay) from the M3 is carried over for USDM swaps. A standard seafoam green relay can be used for Euro swaps." TerraPhantm: "The non-M/Euro setup works fine with the US MSS54 - it won't throw errors." nextelbuddy still logged an EKP fault (no CEL) — [e46fanatics #744, #748, #749](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)

### Inferences
- **Main relay, injector relay, secondary-air relay and E-box fuse block:** the M3 needs nothing beyond what the 325i already has (same relay parts and holders, same pins at X60002-23, X60001-1 and X60004-3). They come over with the M3 engine harness's E-box section. The heavy DME-relay feed in the 3-pin E-box plug must be connected ("nothing will work without it").
- **Throttle actuator:** no added feed. The DME powers it through X60001-2/-9 from its own B+ and relay supplies.
- **E-box fan:** a manual Touring with a manual M3 donor normally has no E-box blower, so nothing to wire. If either car was automatic, SMG or hot-climate, decide whether to keep the blower and drive it from MSS54 X60002-12.
- **Mr.ZHP's "3 slots":** unidentified. The likely candidates in the generic list are SMG feeds (F8/F22, not needed with a manual), the auxiliary water pump (F23) and fuel-pump items (out of scope). If one is needed, unused positions accept a new terminal on the already-present power side, per Kalim.

### Gaps
- No M3-specific glovebox fuse chart (BMW fuse card or owner's manual) was found, so the three "M3-only" slots in post #743 remain unidentified.
- F102, F109 and F114 positions (B+ distributor) and the X8680 E-box fuse-carrier assignments of F1–F5 for the 325i vs the M3 were not found in a BMW source.
- Whether the Touring's E-box fuse carrier is reused or replaced by the M3's: forum sources say the "mini fuse box" comes with the M3 engine harness, but no BMW confirmation was found.

## Q4. Grounds, the E-box and the DME connector housing

### Takeaway
The plastic E-box, its relay carrier and the engine-to-body ground cable are identical BMW parts on the US M3 and the US 325i Touring, so they carry over. What differs is the wiring inside the box: the harness-side connectors and the E-box branch (X6053/X60531, X6011, the 4-pin and 3-pin plugs). The 330i swapper's injector-circuit-low codes point at that mismatch, not at the plastic housing. BMW lists the MSS54's grounds as X60001 pins 4/5/6, X60004 pin 5 and X60005 pin 5. X60004 pin 5 is body-side and is not a ground on the 325i's DMEs.

### Cited Findings
- BMW: "Ground: Multiple ground paths are necessary… The ECM ground pin numbers are: Connector X60001 Pin 4, 5, 6 – Ground for ECM; Connector X60004 Pin 5 – Ground for ECM; Connector X60005 Pin 5 – Ground for ECM." The ECM "Internally links a constant ground to the engine sensors" and "Switches ground to activate components". Workshop hint: "The ignition (KL15) must be switched off when removing or installing the ECM connector to prevent voltage spikes (arcing) that can damage the Control Module!" — [BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- TIS-format lists:
  - MSS54: X60001-4 "Ground – Ground point", X60001-5/-6 "Ground connector", X60002-5 "Negative activation – Ground connector", X60004-5 "Ground – Ground point", X60005-5 "Ground connector".
  - MS43: X60004-5 "Not used".
  - MS45: X60004-5 is the "Ground Secondary air, hot-film air mass meter".
  — [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
- The ETK "Ground cable" is 12421737755, "L=380MM", on both the US M3 and the US 325i Touring — [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/ground_cable/), [325iT](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/vehicle_electrical_system/ground_cable_2/). The M3's engine-compartment B+ terminal point is base 61138387540 — [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/b_terminal_point_engine_compartment/)
- A vendor describes the BMW engine ground strap as spanning "from the engine mount arm to the frame horn" — [Turner](https://www.turnermotorsport.com/BMW-E46-M3-Parts/c-1279-bmw-ground) (snippet only; generic, not S54-specific)
- **ETK "Control unit box", identical on both cars:** cover 12901436443 (to 09/2002) or 12907521582 (from 09/2002); bottom part 12907534921; relay carrier 12901437378; grommet 12901436449; plus the blower or plain cover as in Q3 — [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/control_unit_box/), [325iT](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/control_unit_box/)
- **ETK DME connector housings for the US M3 ("Basic control unit DME"):**
  - Socket housing 12521744624 with cap 12527502456. The pin count isn't shown; it is presumably the 9-pin.
  - "24 POL./A" socket housings 12521744627 and 12521744628 (cap 12521744626).
  - "52 POL./A" 12521744633 and 12521744634 (cap 12521744632 to 07/2003, or 12527526424 "Z-CODE").
  - "40 POL./B" 12521744630 and 12521744631 (cap 12521744629).
  - DME basic units: 12147835564 ("MSS54/FLASH", to 09/2004), 12147836454 (to 08/2005), 12147836455 (RMFD), 12147837806, 12147837805.
  — [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/basic_cotrol_unit_dme/)
- **Injector-circuit-low, 330i with M3 driveline:**
  - All six injectors threw "Circuit Low" codes, with the DME, fuse 5 in the E-box and the relay checked.
  - Then: "I believe the issue stems from me not changing over the M3 DME housing that contains different connectors and wiring placement for some of the connectors on it. X6053/X60531 are fairly different when it comes to the throttle bodies and fuel injectors… the M3 DME housing is now broken, so what I will ultimately end up doing is repinning the connector to match what should be there for the M3."
  - The thread ends on 19 May 2020 without confirming the fix.
  - A responder noted newTIS "didn't have the correct DME wiring diagram for the MSS54 system".
  — [e46fanatics #1, #3, #4](https://www.e46fanatics.com/threads/s54-swap-fuel-injectors-low-circuit.1277127/)
- X6053 is the white 8-pin connector on the S54 harness in the E-box. Its wires are "Almost all… red", read as "+12v supply to engine sensors" — [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/116033-s54-wiring-harness-identification)

### Inferences
- **Grounds:**
  - Reuse the Touring's E-box and ground strap. Both are the same part numbers.
  - Keep the M3 harness's own grounds intact: X60001 4/5/6, X60002-5 and X60005-5 land at the M3 harness's ground points.
  - X60004-5 is the one body-side ground BMW lists for the MSS54. The MS43 Touring has nothing there, and the MS45 car has an HFM wire there that Kassel says to remove. Check the donor's body-side X60004 for a brown wire at pin 5. If BMW's ground is real, add a ground there to the E-box ground point. No swapper reported doing this, and e34m5freak199's comparison showed no pin-5 difference.
- **Connector housing:** "fit the M3 DME housing" means bringing the M3 harness's complete E-box branch, with its connectors and their mates (X6053/X60531 especially, which feed the injectors and throttle). Where the Touring's half must mate with the M3's half, compare them pin by pin. A mismatch there disables the injector or throttle supply without damaging anything, which is what produces the injector-circuit-low codes. The plastic box itself carries over.
- **Spare housings:** if a DME module housing breaks during depinning, ETK lists the replacements above. Order by the M3 VIN.

### Gaps
- The physical location of the S54's engine-harness ground points (cylinder head or intake ground eyelets) and of the body ground stud in the E46 engine bay was not found in a primary source.
- Whether the M3's body harness actually populates X60004 pin 5 (BMW says ground; one builder's comparison implies not) is unresolved.
- The X60531 counterpart's pin list and harness assignment (body or E-box branch) were not obtained.

## Q5. What the Kassel wiring guide and the Redline E46 swap harness cover, cost and require

### Takeaway
Kassel's chart is free and covers only the X60004 pin moves, adds and removes for MS42, MS43 and MS45 E46s. Kassel sells the DME coding separately: EWS delete or engine-swap coding, plus an optional $429 core charge. Redline's $265 E46 harness is a plug-in adapter with new connectors. It provides electronic-pedal wiring, fuel-pump wiring with a relay and Sport-button wiring, and requires an EWS-deleted MSS54/MSS54HP. Neither covers the cluster lamps on MS45 cars, the MS43 X6011 moves, the DM-TL heater on MS43 cars, the clutch or gear-recognition path, the E-box sub-connectors or cluster coding. Those remain the builder's job.

### Cited Findings
- **Kassel chart** "S54Swap E46 Wiring Modifications" (1800×1796 PNG, uploads path 2016/01). It says: "The E46 M3 MSS54 / MSS54HP DME can be programmed by Kassel Performance for any of your swap needs". It has three columns of X60004 edits:
  - MS42 cars (323, 328 99–00);
  - MS43 cars (325, 330 01–02): move 28→34; add 11→cluster 14, 15/16 Sport (optional), 21→cluster 17; remove N/A;
  - MS45 cars (325, 330 03–): move 28→34 and 2→18; add N/A; remove 5, 15, 19.
  - It shows BMW images of the pedal sensor R10/X11400 and of the E-box with X60004 and X60005 labelled.
  — [Kassel chart](https://www.kasselperformance.com/wp-content/uploads/2016/01/E46S54Wiring.png)
- **Kassel product page:**
  - "Coding for engine swaps is our specialty. All check engine lights are operational and the DME is coded for your specific setup."
  - "DME will be plug and play for any E46 M3 if the EWS delete option is selected."
  - Options: CSL SMG shift parameters, "EWS Delete – Coding delete for EWS. Immo off. Plug and play", SAP delete, post-cat delete, and "Engine Swap Coding – … full consult will be conducted… any and all options are included with this package".
  - Listed at "$0.00" before options; "$429 core charge optional".
  — [Kassel](https://www.kasselperformance.com/product/bmw-e46-m3-s54-mss54-hp-tuning/)
- Kalim on Kassel's chart: "I haven't looked at the Kassel Performance guide, so I can't comment on that." The asker thought "MS45 seems more closer wiring wise than older E46s" — [e46fanatics #744, #745](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)
- **Redline "E46 M52TU, M54, S54 Engine Wiring Swap Harness":**
  - $265.00, SKU E46M5XS54, "M52TU/M54/S54 Adapter for E46".
  - "M54 must use MS43 DME (MS45 option now available!)"; "S54 must use MSS54 or MSS54HP DME".
  - "Plug-and-Play… All crimp terminals and connectors are new… high temperature automotive grade wiring… Continuity tested on every wire… Wrapped in high temperature expandable nylon sheathing… Instruction sheets are included."
  - Includes: "Electronic pedal wiring (M54 and S54)", "Fuel pump wiring and relay", "Sport mode button (S54)".
  - "EWS (Immobilizer) delete is required." Weight 1.5 lb. No reviews.
  — [Redline](https://www.redline-motorsport.com/product/e46-m52tu-m54-s54/)
- Redline's "E46 Wiring" category also sells harnesses for M50/S50/M52/S52, M62/S62, N52/N54 and S65 engines going into an E46, an "SMG-to-Manual (E46/Z3M) Wiring Harness Modification" ($130–$300) and an "E46 Wiring Harness Extension Kit" ($200). So the product is aimed at an E46 recipient — [Redline category](https://www.redline-motorsport.com/product-category/e46-wiring/), [Redline E46 search](https://www.redline-motorsport.com/?s=E46&post_type=product)
- Redline's product photo shows a sleeved harness with a white multi-cavity connector, a black connector with a teal secondary lock, small 2-pin connectors, and two black rectangular multi-pin connectors (likely DME-module style). The page does not say which car connectors it mates with; this description is my reading of the photo — [Redline photo](https://www.redline-motorsport.com/wp-content/uploads/2025/10/photoroom_20251005_002306.jpg)

### Inferences
- **With Kassel's chart, the builder still has to:**
  - for MS43 cars, move the charge-lamp, start and DM-TL-heater wires out of X6011 (Kassel's MS43 column omits them);
  - for MS45 cars, add or code the cluster warnings, at least oil pressure to cluster pin 13;
  - handle the clutch and gear-recognition switch, and the fuel-pump or EKP trigger;
  - get an EWS delete or sync and code the cluster and DSC;
  - check the E-box sub-connectors.
  Its cluster-pin numbers (14 for oil pressure) should be checked against the cluster.
- **With Redline's harness:** a 325i Touring already has the electronic pedal, so much of its value here is the fuel-pump relay and Sport wiring plus avoiding work on the factory connectors. Ask Redline before buying:
  - whether the S54 version handles the MS43-to-MSS54 cluster-lamp and brake changes;
  - which body generation (MS43 or MS45) it is pinned for;
  - whether it supports the US EKP (cycled pump) arrangement.
  It needs an EWS-deleted DME, which matches the guide's preferred immobilizer route.

### Gaps
- Redline's instruction sheet and connector list are not online. Its coverage of cluster lamps, brake, DM-TL and clutch is unknown.
- Kassel's swap-coding option price is not shown in the page text (menu-driven).
- No third-party reviews of either product were found.

## Q6. Re-pin vs splice: first-hand outcomes, tools, terminals and common mistakes

### Takeaway
Builders who re-pinned at X60004 (and in the E-box) report quick, clean results: "started… 1st time", or "15 minutes" once the circuit was understood. The most-cited failures come from wrong documentation (wrong VIN, Bentley, TIS "not used" pins), from mismatched E-box connectors (injector circuit low) and from mixing coil harnesses and DMEs. That last case came from an M54 swap, not an S54 swap. Use depinning keys, not splices, and keep the DME and harness as a matched set.

### Cited Findings
- **Outcomes:**
  - "Wiring: IS S PIECE OF CAKE… my 323 with m54 engine swap (alread wired 6 wires for drive by wire) started with the s54 1st time… i just moved 4 wires round on x00004 connector" — [e46fanatics #19](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
  - HakenTT re-pinned X60004 "on few places" — [#6](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
  - "AND with my new knowledge, it took me 15 minutes to establish the battery light… The parking brake light works" — [e46fanatics #29](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)
  - "I just made a google doc that had DME pinouts for MSS54 and MS45 and compared PINouts and made sure to repin my pins to match MS54" — [e46fanatics #750](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)
  - Kalim: "you definitely shouldn't be stripping the main harness. This is a minimally invasive swap as far as wiring goes" — [#746](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)
- **Advice:**
  - "I would recommend breaking the habit of cutting and soldering the wires. Learning to de-pin is faster, neater, and less prone to error. With a few cheap de-pinning keys you can remove the wires and put them in the right place or connector" (Archbid).
  - "cutting/soldering a BMW harness is the last resort...and not a very good one at that" (Effduration).
  — [e46fanatics #3, #8](https://www.e46fanatics.com/threads/330ci-engine-swap-no-start-looking-for-help.1298699/)
  - "If you disconnect the plug you'll see how easy it is to add/remove pins to the connector to test" — [e46fanatics #18](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)
- **Coil-harness damage case (context matters).** It came from an M54 swap into an 01 330Ci, mixing the MS43 square-coil harness with a later pencil-coil harness ("the pin out on the new harness is different (MS45/MS43)"):
  - "Mistake on wiring the ignition coil could be deadly."
  - A spare DME "fired right up".
  - "Apparently using the wrong pinout coil harness can in fact damage the DME."
  — [e46fanatics #1, #4, #5](https://www.e46fanatics.com/threads/330ci-engine-swap-no-start-looking-for-help.1298699/)
  The coil pin orders differ between DME families (MSS54 X60005 1/2/3/6/7/9 = coils 1/2/3/5/6/4; MS45 1/4/6/7/8/9 = coils 5/3/1/2/4/6) — [spreadsheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)
- **Other documented mistakes:**
  - Diagrams for the wrong VIN ("Preloading the wagon's VIN changed what I was seeing") and a Bentley page that didn't match the car — [e46fanatics #26, #10](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)
  - TIS "not used" pins that are populated (X60003-19) — [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/116033-s54-wiring-harness-identification)
  - Lamps not wired or coded after an MS45-body swap (oil pressure only from oil level) — [NAM3 #11](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)
  - Reading "GR" as green instead of grey on the clutch wire — [e46fanatics #2](https://www.e46fanatics.com/threads/manual-swap-wiring-with-mss54-dme.1316134/)
  - Missing E-box mini fuse box or 3-pin plug — [#27](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
  - Unplugging the DME with the ignition on — [BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
  - After an MS43-car swap, one owner reported "INPA shows a different vin, and I have a ton of dash lights on… no coolant temp", unresolved on that page — [e46fanatics #759](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)
- **Terminals (ETK, US M3 engine electrical):**
  - "Socket terminal SLK 2.8" (12520007168, 12520007171) and "SLK 2.8 ELA" (12520007170, 12520007172, 12520143427/433/434);
  - "Blade terminal cont. microtimer" (12520007251) and "MDK4 2.8" (12520007252–255) — [ETK laminated/spring contacts](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/laminated_contacts_spring_contacts/)
  - "Terminal socket for MLK 1, 2" (12527510668–674, 12527560453/455, others) with rubber grommet 12527503411, and "Flat plug terminal MLK 1.2" (12527512135) — [ETK contact system MLK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/contact_system_mlk/)
  - E-box relay sockets use "Double leaf spring contact" terminals by wire size: 61130007437 (1.0 mm²), 61130007438 (2.5 mm²), 61130007271 (6.0 mm²), 61138377730/731/732/734 — [ETK K6300](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/relay_dme_mss54_k6300/)
- **Tools:**
  - BMW break-out box 90 88 6 121 300 and relay test kit 88 88 6 613 010 — [BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
  - Turner lists "12pc De-Pin Tool Set - T#386379" and "23pc De-Pin Tool Set - T#641943" — [Turner](https://www.turnermotorsport.com/c-1681-bmw-repair-kit) (snippet only)
  - A small-maker depin tool for E30/E36/E46 round-pin connectors (C101, X20, X6031…) does not list the DME modules — [Falk Mfg via reach.dog](https://m.reach.dog/shop/falk-mfg/products/depin-tool) (snippet only)

### Inferences
- Re-pinning within X60004 and X6011 in the E-box keeps every terminal in a factory housing. Moving wires between X6011 and X60004 may need the terminal swapped to the target housing's type, because the two housings may use different terminal families. Buy matching terminals with pre-crimped repair leads, by part number from ETK for the target housing, rather than forcing a mismatched terminal.
- Before power-up:
  - verify each moved circuit with an ohmmeter from end component to DME pin;
  - pre-load the Touring's VIN when reading diagrams;
  - keep the ignition off when plugging DME modules.
- Splices that bypass the DME (oil-pressure switch straight to the cluster) work as a lamp fix. They remove the input from the MSS54, which reads that switch, so prefer the factory pass-through.

### Gaps
- No source states which terminal family (MLK 1.2, MQS, SLK, etc.) is used in the X60004 40-pin housing, or which depin key size fits it. The X6011 terminal type is likewise unknown.
- No first-hand S54-into-Touring wiring write-up was found. Garagistic's S54 Touring thread says only that a "local shop" did the swap "keeping it clean to keep an OEM look", with no wiring details — [e46fanatics](https://www.e46fanatics.com/threads/reintroduction-garagistics-e46-s54-swapped-touring.1304132/). The relevant first-hand data come from sedans or coupes (323i, 325i, 330i, ZHP) and one 2001 325iT whose wiring details are partial.
- Blocked or unreachable sources that may hold the definitive pin lists: NewTIS (Cloudflare 403) at [newtis.info](https://www.newtis.info/tisv2/a/en/e46-m3-cou/wiring-functional-info/power-train/engine-control/vBtD9Pa), and the bmwteka WDS mirror pages for X6053 ([c6afbff8](https://bmwteka.com/wds/en/e46/c6afbff8)) and X60003 pin 19 ([546965ba](https://bmwteka.com/wds/en/e46/546965ba)).
