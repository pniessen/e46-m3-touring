# S54 swap re-pin practice by receiving DME family: what builders moved, added and removed (US 2001–05 E46 325i Touring target)

Research date: 22 October 2026.

**Reading key.**
- **[read]**: read on the page in this session. NAM3 and r3vlimited threads were fetched with curl and parsed. ETK data came from bmwfans.info pages. The MS4X wiki was read as raw wikitext, vendor pages as HTML, and the pinout workbook as an XLSX export.
- **[image]**: a BMW TIS/WDS diagram or a forum photo viewed as an image in this session.
- **[snippet]**: seen only in a search-engine summary; the page itself was not read.
- **[earlier]**: read in an earlier session and recorded in the named research note (`harness_engine_side.md`, `harness_body_functions.md`, `fuel_pump_control.md`, `youtube_swap_wiring_coding.md`); not re-read today.

**Blocked or unreachable, not worked around.**
- e46fanatics.com served a proof-of-work and headless-browser check (HTTP 202). One plain attempt failed and I stopped, so every e46fanatics fact below is [earlier] or [snippet].
- web.archive.org: the connection was reset by the egress proxy.
- The archive.org availability API returned HTTP 429 at first; I waited and sent only a handful of queries.
- bimmerforums.com: Cloudflare, HTTP 403.
- The bmw-planet.com WDS mirror answers with a JavaScript-token redirect, which is a bot check. Not followed.
- bmwteka.com: connection reset.
- s54swap.com, Kassel's old swap wiki: dead ("Page cannot be displayed").
- YouTube was not re-fetched.

**Downloads** are in `/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/wiring-dl/`. None was executed.

**Conventions.** Wire colours use BMW codes: BK = SW black, BL blue, BR brown, GE yellow, GN green, GR grey, OR orange, RT red, VI violet, WS white.

**DME names.** "MS45" in Kassel's chart and in most forum posts means the North-American **MS45.1**: the BMW parts catalog (ETK) lists only MS45.1 for US 325i/330i built from March 2003. MS45.0 is the non-North-American version: MS4X says "MS45.1 was primarily an emission update and was only used in north american cars". No US E46 uses MS45.0, so there is no separate MS45.0 table.

## Takeaway

- **The US 325i Touring went from MS43 to MS45.1 with March 2003 production.** ETK shows MS43 "to Mar '03" and MS45.1 "from Mar '03". The engine harness, the air-mass meter and a new secondary-air pump with its own air-mass meter all change at the same date. BimmerWorld and RPM say 02/2003, which is the same changeover seen from the other side. Read the DME label in the E-box.
- **A 325xi Touring may stay MS43 for every year.** ETK's programmed-DME data and several forum posts say so, but ETK's harness and secondary-air groups conflict, so read the label.
- **On an MS45.1 Touring the K96 pump relay is driven from X60004 pin 10 (SW/VI).** That is the same pin as the MSS54's "not USA" relay output, so no pump re-pin is needed. A US MSS54 then stores a pump-module fault but doesn't light the check-engine lamp.
- **The workbook tab that lists pin 10 as unused ("MS45 903") is not an M54 table.** Its CAN pump controller on pins 31/35, EAC sensor on pin 25 and missing clutch input on pin 23 match the M56 SULEV automatic, and MS4X marks exactly those pins "only with M56".
- **MS45.1 Tourings very likely have wires at X60004 pins 5 and 15.** ETK lists a secondary-air mass-air-flow sensor from March 2003 on the 2.5-litre Touring, and those pins serve it. Nobody has photographed a 325i Touring's X60004 to confirm. The one documented MS45.1 swap with a pin list (smee123, 2004 ZHP) removed 5, 15 and 19 and moved 28→34 and 2→18, exactly Kassel's MS45 column.
- **Nobody needed a ground at X60004 pin 5.** smee123 added one while chasing a DME relay that stayed on; it changed nothing, and the cause was a worn ignition switch.
- **BMW's TIS diagram settles the clutch question.** On a factory-manual M3 the clutch module's signal wire (KUPPL, GR) crosses into the engine harness at **X6011 pin 7**, then runs X6053 pin 5 → gear-recognition switch → GR/BL wire → X60002 pin 20. terra's photos of the same circuit agree.
- **The M3 clutch module and the 325i's are not interchangeable.** The M3 module (61319122700, "orange/brown") outputs +12 V with the pedal up; the non-M module switches to ground. George Hill and ewcmr2 both fixed no-cruise by fitting the M3 module, and in George's car it also cured intermittent stalling.
- **On an MS43 Touring built from 09/2001, X6011 pin 7 already holds the DM-TL heater wire (BK/RT).** If left there it mates with the M3's clutch wire. Move it to X60004 pin 18 first, then put the clutch wire in pin 7.
- **The rest of the MS43 X6011 map:**
  - pin 3: oil-pressure lamp (BR/GN, to cluster pin 13);
  - pin 4: charge lamp (to cluster pin 2);
  - pin 5: oil level (to cluster pin 17);
  - pin 6: start feedback.

  Pin 3 is confirmed by ISTA (quoted by a swap shop) and by a 2001 325iT owner. Pins 4–6 rest on two independent MS42→MS43 converters. The S54 harness has nothing in X6011 pins 3–6, so these wires must move into X60004 pins 11/1/21/6, or new wires must be added.
- **MS45.1 Tourings send these lamps over CAN.** An MSS54HP in an MS45.1 ZHP would not light the oil-pressure lamp over CAN even with the M3 cluster coded for it. Add X60004 pin 11 → cluster pin 13 and set CAN_OELDRUCKSCHALTER to nicht_aktiv. The charge lamp and oil level can stay on CAN with stock MSS54HP software (GENERATOR_UEBER_CAN, TOG_UEBER_CAN), or be wired to cluster pins 2 and 17.
- **DM-TL (US leak test).**
  - MS43 Touring: only the heater moves, X6011-7 → X60004-18.
  - MS45.1 Touring: 2→18, and very likely a swap of pins 20 and 30 as well, because MS45.1 has the pump (BR/BL) on 20 where MS43 and the MSS54 have it on 30. Kassel's chart omits this swap.
  - Cars built before 09/2001 have a three-wire DM-TL with no heater wire to move, so one has to be added.
  - An MS43 S54 wagon passed the California referee with SW/GN on pin 20, BR/BL on 30 and the heater on 18.
- **MSS54 vs MSS54HP:** no pin difference found. The US pump-module signal is X60002 pin 11 on both, shown in WDS and confirmed by continuity on a 2006 M3.
- **M56 SULEV:** catalogued with an automatic-only gearbox-module harness. The MSS54 can't command its CAN pump controller, so pump control, tank, lines, clutch wiring and reverse lights all need rework. The one documented build (Tenza) also swapped the certified SULEV tank and evaporative parts; that's a legal caution.
- **Vendors:**
  - Kassel's chart: wrong oil-pressure cluster pin (14, not 13). It omits the clutch, charge lamp, MS43 DM-TL heater and MS45.1 pins 20/30, and claims MS45 cars need no added wires.
  - Redline / Race German adapters: sold per DME family, including M54 (MS43) and M54 (MS45) to S54, but publish no circuit list.
  - Tulay's Wire Werks: sells the individual pieces (Sport wires, RDC wire, connector kits, clutch and reverse-light leads) with pin numbers.

## Q1. MS45/MS45.1 cars (2003.5–2005): what swappers moved or added, the K96 pin, pins 5 and 15, and a pin-5 ground

### Cited findings

**First-hand builds on MS45.1 bodies**
- **smee123, 2004 330i ZHP (US, MS45.1 body), S54 swap in progress, Jan–Feb 2023** [read] — [NAM3 "Switched 12v question", posts 10–17](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/201716-switched-12v-question) and [page 2](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/201716-switched-12v-question/page2):
  - "The ms45.1 has slightly different wiring than the mss54, however, I removed the wiring that did not correspond, specifically pin 5, 15, 19. I moved pin 28 to pin 34, pin 2 to pin 18." (post 10)
  - "I wonder if not having a ground on pin 5 on x60004 is causing the transistors inside the dme to go nuts" (post 11). Then: "I added a ground on pin 5. No change… It does close to ground when the ignition is on however." (post 13)
  - heinzboehmer replied with the MSS54 TIS table showing pin 5 "M — Ground — Ground point" [image, fetch id 201831].
  - The fault was the DME relay staying energized after key-off. sapote: "check X60004 pin26: it should only has 12v with ignition sw ON" (post 16). Fix: "It was a lazy ignition switch." (post 17)
- **nextelbuddy, 2003 330i ZHP (US, MS45.1 body), MSS54HP with stock software, Oct 2020** [read] — [NAM3 61405, posts 4, 7, 9 and 11](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off):
  - "my alternator and oil sensors are canbus since my ZHP was canbus for those sensors".
  - With his coding-index-24 M3 cluster: "I had alternator over can bus enabled oil level over can bus enabled but oil pressure over can bus not enabled. I switched that to enabled flashed it back to the cluster but still the oil light doesn't stay on". So **CAN oil pressure does not work with the MSS54HP**.
  - "X6011… looks very similar to an MS-45.1 it only has two wires which are for the starter and some other wire.. and then two additional wires for gear position sensor and TPMS… MS-45.1 was virtually identical out of eight pins only two were used."
  - "The other smaller 4-pin plug… black and purple wire which is for the EKP fuel pump relay which I'm not using."
  - "the back of my cluster pin number 13… it's empty."
  - Fix (post 11): "I just ran a wire from x60004 pin 11 to the cluster plug pin 13. used NCS e[xpert] to change back to oil pressure via CAN bus not active... and now my oil light and alternator light are both on with the engine off."
  - "stock MSS54HP software… does support alternator via canbus"; his earlier CSL software did not.
- **George Hill (swap shop) quoting ISTA, same thread, post 10** [read]: M3: "X11175 Pin #13 KOMBI → X60004 Pin#11 DME (BR/GN); X60003 Pin #26 DME → X6231 Oil Pressure switch". "A ZHP": "X11175 Pin #13 KOMBI → X6011 #3 (BR/GN); X6011 #3 → X6231 Oil Pressure switch". His swap method: take the M3 donor's 13→11 lamp wire, "cut it to length and wire it from X60004 Pin#11 DME to X6011 #3".
- **nextelbuddy, MS45-era body, US MSS54 with EWS removed, 2017** [earlier, `fuel_pump_control.md`]: "we are using the euro fuel pump output on MS54 BUT DME is still throwing a code for Fuel pump EKP… it doesnt trigger CEL" — [e46fanatics, Kalim p.38 #749](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38). In #750 he says he compared WDS pin lists and re-pinned to match. The thread title of his own build is ["My 2003 330i ZHP S54 Swap Conversion"](https://www.e46fanatics.com/threads/my-2003-330i-zhp-s54-swap-conversion.1129960/) [snippet: "printed out WDS PINOUTs for MSS54 for a 2002 MSS54 NON SMG and compared it to MS45 DME pinouts and made my harness pinouts match"].
- **Kalim (cyberkaa), red car MS45.1** [earlier]: "MS45.1 cars are very close to M3s in terms of wiring"; added nothing to the fuse box — [e46fanatics p.38 #746](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38).
- **Unnamed owner, S54 + 6-speed into an ex-automatic 330i (MS45.1), wired "per Kassel's S54 wiring chart"** [snippet]: no cruise. A reply says the DME only reads the clutch/cruise input when its software is set up for a manual — ["S54 swap: cruise control not working", e46fanatics 1316868](https://www.e46fanatics.com/threads/s54-swap-cruise-control-not-working.1316868/).
- **BH93, 330i (MS45) EVAP** [earlier, `harness_body_functions.md`; snippet]: "no PINS need to be changed on X60003 harness… Just need to swap the DMTL plugs on X60004", and "move pin 2 to 18" — [e46fanatics 1291729](https://www.e46fanatics.com/threads/e46-s54-sedan-swap-evap-pin-outs.1291729/).
- **steevo_102, non-M swap cross-referenced to MS45.1** [earlier, `harness_body_functions.md`]: MS45.1 X60004 pins 20/30 are "reversed" against the MSS54. After swapping them he still had P2418 (switching-valve circuit), unresolved. Sport wires were added to 15/16 — [e46fanatics 1286041](https://www.e46fanatics.com/threads/e46-m3-sport-button-retrofit-on-non-m.1286041/).
- **Tenza Motorsports, 2004 US Touring, originally M56 SULEV (an MS45.1 variant)** [earlier, `youtube_swap_wiring_coding.md`, captions]:
  - Kassel DME and Kassel-programmed M3 cluster.
  - "there's really not much of that [pin moving]". Kassel sent written instructions to "move pins around", which he understood only by tracing the donor.
  - Sport: switch-centre pins 17/18 → X60004 15/16.
  - Check-engine and oil lamps went out about 10–15 s after the first start.
  - [Tenza – M3 touring build finally runs (2021)](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=413s), [Tenza – 5 things… part 2 (2021)](https://www.youtube.com/watch?v=mDBiRn30fEs&t=525s).

**Pin tables**
- **Kassel chart, "MS45 Cars – 325, 330 (03-)"** [image, read]:
  - MOVE: "Pin 28 (Brown/Green) BLTS to Pin 34"; "Pin 2 (Black/Red) DMTLH to 18".
  - ADD: "N/A".
  - REMOVE: "Pin 5 (Black/Yellow)", "Pin15 (Black/Red)", "Pin 19 (Brown/Orange)".

  The posting says "Please consult the BMW WDS before making any changes" — [chart](https://www.kasselperformance.com/wp-content/uploads/2016/01/E46S54Wiring.png), [post, 1 Jan 2016](https://www.kasselperformance.com/e46-non-m-s54-wiring-modifcations/).
- **MS4X wiki "Siemens MS45 Pinout"** [read]. A combined MS45.0/MS45.1 table: "Wire colors are based on e46 wiring diagrams. Also some pins differ between M54 and M56. And between MS45.0 and MS45.1." X60004 rows:

  | Pin | Name | Wire | Function | Wiki note |
  |---|---|---|---|---|
  | 2 | S_DMTLH | 0.75 SW/RT | DM-TL heater | only with MS45.1 |
  | 5 | M_SHFM | 0.5 SW/GE | Secondary-air hot-film air-mass meter, negative supply | only with MS45.1 |
  | 10 | S_EKP | 0.35 SW/VI | "Activation, fuel pump relay" | |
  | 15 | A_SHFM | 0.5 SW/RT | Secondary-air HFM signal | only with MS45.1 |
  | 18 | S_AKL | 0.5 GR/VI | Exhaust flap | |
  | 19 | S_EBOXL | 0.5 BR/OR | E-box fan | |
  | 20 | S_DMTLP | 0.75 BR/BL | DM-TL pump | only with MS45.1 |
  | 23 | S_KUP | 0.35 BL/BR | Clutch switch | |
  | 25 | S_EAC | 0.5 BL/GE | EAC sensor | only with M56 |
  | 28 | S_BLTS | 0.35 BR/GR | Brake-light test switch | |
  | 30 | S_DMTLV | 0.5 SW/GN | DM-TL valve | only with MS45.1 |
  | 31 / 35 | Local CAN | 0.5 GN / BL/GN | Fuel pump control (EKPS) | only with M56 |

  X60003 pin 16 is the oil-pressure switch, pin 50 oil level, and pin 19 the alternator "BSD" data line. X60003 pins 38/51 are local CAN to a terminating resistor, "only with M56". The wiki's main MS45 page says MS45.1 "adds wideband pre-cat O2 sensors and uses a MAF in the SAP… only used in north american cars".
  — [MS4X MS45 pinout](https://www.ms4x.net/index.php?title=Siemens_MS45_Pinout), [MS4X Siemens MS45](https://www.ms4x.net/index.php?title=Siemens_MS45)
- **Pinout workbook** [read; [sheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)]:
  - "MS45.1 X3ZHP" tab: X60004-10 "Activation, fuel pump relay"; 23 "Signal Clutch switch"; 5 and 15 secondary-air HFM tagged "3.0 USA"; 18 exhaust flap; 19 E-box fan; 2/20/30 DM-TL heater, pump and valve; 31/35 "Not used".
  - "MS45 903" tab:
    - X60004-10 "Not used"; 23 "Not used"; 25 EAC sensor; 31/35 "Local CAN-bus… Control module for electronically controlled fuel pump".
    - X60003 38/51 "Local CAN-bus… Resistor, CAN terminal".
    - X60002 3/4 CAN to the transmission control unit (automatic).
- **ETK, US 325i M54 Touring** [read]:
  - "Programmed DME control unit" group 2: 12 14 7 561 526 "MS45.1 from Mar '03 to Jul '04", 7 561 528 (Jul '04–Sep '05), 7 562 340 (from Sep '05), plus automatic variants — [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/programmed_dme_control_unit_2/).
  - "Emission control-air pump" group 2, all "from Mar '03": air pump 11 72 7 571 589, secondary air filter 11 72 1 438 813, **"Mass air flow sensor 11 72 1 438 814"** — [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine/emission_control_air_pump_2/).
  - Group 1, "to Mar '03": pump 11 72 7 553 056 with no air-mass sensor — [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine/emission_control_air_pump/).
- **ETK, E-box blower**: "Cover with blower" only "for vehicles with Automatic transmission… Or SMG… Or Hot-climate version" [read, M56 Touring control-unit-box page, same parts as the M54 Touring per `harness_engine_side.md`] — [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/engine_electrical_system/control_unit_box/).
- **MS45 CAN message DME4 (0x545), MS4X** [read]:
  - Byte 3 bits 0–2: oil-level indicator.
  - Byte 5 bit 0: "Battery Chargelight (Alpina Roadster Only)".
  - Byte 6: oil level "(MSS54HP only)".
  - Byte 7 bit 7: "Status Engine Oil Pressure Low".

  — [MS4X MS45 CAN](https://www.ms4x.net/index.php?title=Siemens_MS45_CAN_Bus_(CAN11h))
- **Cluster coding names** [read; snippet for the thread]:
  - A Bimmerfest coding dump lists "CAN_OELDRUCKSCHALTER Oil pressure switch on CAN bus. nicht_aktiv", "GENERATOR_UEBER_CAN Generator over CAN nicht_aktiv" and "TOG_UEBER_CAN aktiv" — [Bimmerfest](https://www.bimmerfest.com/threads/list-of-options-that-can-be-coded.634379/).
  - An e46fanatics thread names the same three parameters as the switches between CAN and hard-wired lamp inputs for cluster indexes 07, 08, 23 and 24 [snippet] — ["S54 swap cluster coding"](https://www.e46fanatics.com/threads/s54-swap-cluster-coding.1330549/).

### Inferences (mine)
- **K96 pin.** On an M54 325i Touring with MS45.1 (03/2003 on), the K96 coil wire is SW/VI on X60004 pin 10, the same pin and colour as on the MS43. Three things support it: the MS4X table, the MS45.1 WDS tab, and nextelbuddy's MS45.1 ZHP, which ran its pump from the MSS54's "Euro" pin-10 output.
- **The "MS45 903" tab is the M56 SULEV (automatic) layout and doesn't apply to an M54 Touring.** It shows pin 10 unused, the local-CAN pump controller and EAC sensor, no clutch input and automatic-gearbox CAN, and MS4X flags each of those pins "only with M56". The label may be a DME number: ETK has a 12 14 7 532 903 "MS45.1/FLASH" basic unit, production May–Jun '03, model not shown [read, [ETK](https://bmwfans.info/parts-catalog/12147532903/)].
- **Pins 5 and 15 are very likely populated on a 03/2003+ US 325i Touring.** ETK gives it the secondary-air mass-air-flow sensor that these pins serve. The workbook's "3.0 USA" tag probably comes from the X3/ZHP diagram it was copied from. Remove both: pin 15 is the MSS54's Sport input, so a leftover HFM signal there could toggle Sport, and pin 5 is an MSS54 ground. On MS43 Tourings, which have no secondary-air MAF, both pins are empty.
- **A pin-5 ground is not needed.** The MSS54's grounds on X60001 4/5/6, X60002-5 and X60005-5 come with the M3 harness. The only test of a pin-5 ground changed nothing.
- **What the MS45.1 Touring list still needs beyond Kassel's column:**
  - the clutch move (pin 23 → X6011-7) plus the M3 clutch module (Q2);
  - the oil-pressure lamp wire (11 → cluster 13) with CAN_OELDRUCKSCHALTER set to nicht_aktiv;
  - the DM-TL pin 20/30 swap (Q7);
  - charge lamp and oil level by wire or by coding.

  Kassel's "ADD N/A" may hold only with Kassel's own DME and cluster programming. Tenza's Kassel-coded cluster showed a working oil lamp, but the method wasn't shown.
- **Pin 19 (E-box fan) is likely empty on a manual US Touring,** since ETK fits the blower only to automatic, SMG or hot-climate cars. Pin 18 (exhaust flap) is likely empty on a 2.5-litre car. Check both before inserting the heater wire.

### Gaps
- No documented S54 swap into an MS45.1 Touring with a complete pin list. Tenza's Kassel instructions were not shown on camera.
- Which two X6011 cavities the MS45.1 body harness uses (nextelbuddy: "only two"; a conversion snippet: "three wires in the same positions"). Assumed to be pin 1, terminal 50, and pin 2, the terminal-15 feed.
- Whether a non-HP MSS54 sends the charge lamp over CAN. Only the stock MSS54HP is confirmed.

## Q2. MS43 cars: what X6011 pins 4–6 carry, and where the clutch wire crosses

### Cited findings

**MS43 routes the cluster lamps through X6011, not the DME**
- **Tulay's Wire Werks, "E46 MS42 to MS43 Cluster Indicator Plug and Play Adapter"** [read; vendor]:
  - Four wires carry "the battery charge indicator, oil level indicator, oil pressure indicator, and starter feedback signal. The MS42 DME connects these pins internally, while the MS43 DME doesn't and routes these wires through the larger 8-pin X6011 connector."
  - MS42 engine-side X60003: 13 Blue, 12 Black/Green, 26 Brown/Green, 39 Gray/Brown.
  - Chassis-side X60004: 1 Blue, 2 Black/Green, 11 Brown/Green, 21 White/Green.

  — [Tulay](https://tulayswirewerks.com/product/bmw-e46-ms42-to-ms43-cluster-indicator-plug-and-play-adapter/)
- **MS4X MS43 pinout** [read]:
  - X60004 pins 1, 2, 6, 11 and 21 are empty.
  - X60004-23 S_KUP 0.35 BL/BR, clutch switch.
  - X60004-28 S_BLTS 0.35 BR/GR.
  - X60004-20 "DMTL" 0.50 SW/GN; X60004-30 DMTLP 0.75 BR/BL.
  - X60004-10 S_EKP 0.35 SW/VI, fuel-pump relay.
  - **X60003-51 DMTLH 0.75 SW/RT "DMTL Heater"**.

  — [MS4X MS43 pinout](https://www.ms4x.net/index.php?title=Siemens_MS43_Pinout)

**The X6011 map from conversions and diagrams**
- **MS42→MS43 conversion thread** [snippet]: "MS43 does not use pin 11, so you must disconnect it from X60004. Pin 4 goes to cluster pin 2. Pin 5 goes to cluster pin 17. Pin 6 goes to X276." — [e46fanatics 1231278, p.2](https://www.e46fanatics.com/threads/upgrade-from-ms42-to-ms43-teething-problems-and-updates.1231278/page-2)
- **e34m5freak199, from memory, MS42→MS43** [earlier]: X60004 11 → X6011 3 (oil pressure), 21 → 5 (oil level), 1 → 4 (charge lamp), 2 → "pin 6" (start feedback) — [e46fanatics 1003871 #27](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)
- **ISTA via George Hill** [read, NAM3 61405 post 10, above]: cluster X11175-13 → X6011-3 (BR/GN) → oil-pressure switch. This is a "ZHP". ETK puts 330i ZHPs on MS43 to March 2003 [read, [ETK 330i](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330i-M54/browse/engine_electrical_system/programmed_dme_control_unit/)], and nextelbuddy's MS45.1 ZHP had cluster pin 13 empty, so George's lookup fits an MS43-era ZHP.
- **snaponbob, 2001 325iT (MS43)** [earlier]: "On my wagon the oil switch goes to X6011 pin 3 in and out". **AndreBXP**: "On the MS43 the battery light also goes through the x6011 IIRC" — [e46fanatics 1207433](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)

**The DM-TL heater is on X6011 pin 7 on MS43 cars**
- **nextelbuddy (May 2021)** [read]:
  - DM-TL plug X17140 on all M3s: 1 BR/BL → X60004-20; 2 BK/RT → X60004-18; 3 BK/GN → X60004-30. (Conflicts with JaredMV's working layout below.)
  - "On ms45/45.1 sedan/touring pin 2 x17140 goes to pin 2 x60004."
  - "On ms43 sedan/touring Pin 2 x17140 goes to a separate 8 pin body harness connector called x6011… that actually routes back through the x60003 engine harness connector."

  — [NAM3 102198](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/102198-requesting-help-with-dmtl-pinout)
- **JaredMV, S54 wagon, MS43 body (heater on X6011), 09/2001 M3 donor** [read, same thread]: "my black/red wire terminates at x6011 (pin 7) and from there becomes a light grey wire that goes back into the body harness" (May 2021). So the heater wire was meeting the M3 harness's grey wire.
- **Workbook "MS43 to MSS54 Wiring" tab** [read]: DM-TL pin 2 (Black/Red) → "X6011 pin 7".
- **MS43→MS45.1 conversion thread** [snippet]: on MS43 cars the black/red DM-TL wire "runs through x6011 to pin 51 on x60003"; MS45.1 takes it straight to X60004. The poster pulled it out of X6011 and connected it to X60004 pin 2 — ["MS43 to MS45.1 conversion", e46fanatics 1317174](https://www.e46fanatics.com/threads/ms43-to-ms45-1-conversion.1317174/)
- **Trent (tlow98), S54 into a US 330i sedan, MS43, manual** [read, [NAM3 173296 p.4, posts 55 and 60](https://nam3forum.com/forums/forum/main-forum/member-build-journals/173296-trent-s-s54-rebuild-and-sedan-swap/page4)]:
  - "Moved Pin 7 of x60011 to Pin 18 of x60004" (June 2023).
  - Trent gave the build date as "2004/02"; its next owner gives "03/2002". ETK puts US 330i on MS43 only to Mar '03, so 03/2002 fits.

**On the M3, the clutch signal crosses at X6011 pin 7**
- **BMW TIS diagram posted by terra, NAM3, 13 Jul 2023** [image] — [NAM3 225235 post 15](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/225235-clutch-switch-help-code-50), [diagram](https://nam3forum.com/forums/filedata/fetch?id=225277):
  - F9 5 A (terminal R) → X10016-18 → "R<9 0.5 VI/GE" → S805 clutch-switch module pin 3.
  - Pin 1: "31E<2 0.35 BR/SW" → X217 ground.
  - Pin 2: **"KUPPL 0.35 GR" → X6011 pin 7 → X6053 pin 5 → "S_GANG 0.5 GR" → X5271 pin 1, S5271 gear-recognition switch → X5271 pin 2 → "S_GANG 0.5 GR/BL" → X60002 pin 20.**
  - Pin 4: "WFSI 0.35 BL/SW" → X1659 pin 8, EWS ("USA", "Japan").
- **terra's text and photos, same post** [read, image]:
  - "Clutch Switch (+12V with pedal up, 0V with pedal depressed) → gear position sensor (open in neutral, closed in gear) → DME."
  - "Connect one probe… to X6011 pin 3 (gray wire)". His photo shows 11.76 V at a grey wire in the black 8-pin plug. The pin number contradicts his own TIS diagram (pin 7).
  - "If you get no voltage, then either the switch is bad or you have a non-M switch (the non-M switch switches between open and ground instead of open and 12v)."
  - Gear-switch test: continuity from the grey X6011 wire to X60002 pin 20 "in gear… near 0 ohms. With the lever in neutral… no continuity".
- **NAM3 race-car harness ID** [read] — [NAM3 116033](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/116033-s54-wiring-harness-identification):
  - M3 engine harness X6011: "Pin 1-black wire- starter run wire from ignition switch"; "Pin 2- Green… +12v power supply to oil level sensor"; "Pin 7 - grey wire- connects to the white 8 pin connector"; "Pin 8- yellow/blk wire- connects to x60003 pin 19".
  - The white connector is X6053 (heinzboehmer).
- **X6011 pin 8** [read]: the GE/BK wire is "the TPMS initialization wire". On an MK60 M3 convertible "body harness connector x6011 does not have pin 8" (nextelbuddy). heinzboehmer: "MK20 cars have the wire running to the DME and MK60 cars have it running directly to the traction control module" — [NAM3 243029](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/243029-e46-m3-tpms-x60003-to-x6011-question)
- **Andrew325is (harness vendor)** [read]: X6011 carries "starter terminal 50 and ignition switched power for the alternator voltage regulator (terminal 15)… E46 WDS shows 7.5 amp". X6021 is "the E46 version… It has wires for the fuel pump relay (EKP-Modul) and the back-up lights switch" — [r3vlimited 336723](https://www.r3vlimited.com/board/forum/e30-technical-forums/24v-engine-swaps/m54-s54/336723-what-are-these-connectors-for-s54)
- **Earlier readings of the M3 diagram** [earlier]: yayyap159 read it as clutch-switch "pin 2… to pin 7 of the X6011", and DaveVolvoBMW (2002 325i Touring + 2002 M3) said "wire in the gear position switch inline between the clutch switch and DME 6002 Pin 20" — [e46fanatics 1316134](https://www.e46fanatics.com/threads/manual-swap-wiring-with-mss54-dme.1316134/)

**The two clutch modules differ**
- **George Hill, S54-swapped Imola ZHP sedan, Dec 2020** [read]: "intermittently stall and the cruise control didn't work. First, the clutch switch was not even wired let alone properly to the DME and secondly the clutch switch was the wrong one. M3s use a different switch (orange) than all the other E46s (black). New switch and correctly wiring the switch got the cruise working and fixed the stalling issue." — [NAM3 3768 p.3, post 38](https://nam3forum.com/forums/forum/main-forum/member-build-journals/3768-what-s-going-on-in-my-shop-currently/page3)
- **ETK usage** [read]:
  - 61319122700 "Module, clutch switch": E46 M3 (Europe and USA), M3 CSL, E39 M5, Z4 M.
  - 61319122701: E46 M3 Europe only, plus CSL, Euro M5 and Z4 M.
  - 61319231129: non-M BMWs, including the 325i.

  — [61319122700](https://bmwfans.info/parts-catalog/61319122700/), [61319122701](https://bmwfans.info/parts-catalog/61319122701/), [61319231129](https://bmwfans.info/parts-catalog/61319231129/)
- **ewcmr2, S54 E46 wagon** [earlier]: "replacing the junk yard 330i clutch switch module with new M3 part fixed the no cruise control problem" — [e46fanatics 1260275](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/)
- **NAM3 225235, posts 7–8** [read]:
  - "OG NLA Brown Clutch Switches" sell used for $280–300.
  - Pklauser: "Euro part 61319122701… code out the clutch interlock. I did this and have functional cruise."
- **Tulay's non-M clutch-module lead** [read]: "0.35 mm² Brown – to Chassis Ground"; "0.35 mm² Blue – to DME X60004-23"; "0.50 mm² Violet – to Ignition Switched Power… from Fuse 9"; "0.35 mm² Black – to EWS X1659-8". Clutch modules on the master cylinder date "from 03/2001" — [Tulay](https://tulayswirewerks.com/product/e46-clutch-switch-module-wire-harness/)

**First-hand MS43 swap results**
- **Trent, 330i MS43** [read, post 55]:
  - "X60004 pin 11 - Pin 13 of Cluster – Kassel calls this out as pin 14 of the cluster. This is not correct."
  - "The oil level sensor is correct as Kassel calls it out."
  - "x60004 pin 1 - Pin 2 of cluster".
  - "You will likely find the clutch switch for the M54-based cars in pin 23 of x60004. Pin 23 goes unused in the mss54 DME… x60004 Pin 23 to Pin 20 x60002". This is an SMG donor with no gear switch.
  - Post 54: "some of the wiring specs Kassel publishes doesn't cover all e46 permutations, so I moved about 4 wires. One of them, critically, being the oil pressure light."
- **George Hill, 2001 325iT (5-speed, RWD) S54 conversion for MJWeimer, 2019–20** [read]:
  - "running wires to the instrument cluster, SZM (switch center in the console), fuse box, IHKA and DSC sensor"; "routed the wires through the loom with the original wire set"; "And the E-box all back together with the MSS54 DME installed".
  - "VIN, Correct mileage and M-Track mode coded to cluster (which was also modified for the rear door indicators)".
  - "Wiring was completed using the Euro transmission wiring harness".
  - No pin list. — [NAM3 3768 p.1, posts 14–15](https://nam3forum.com/forums/forum/main-forum/member-build-journals/3768-what-s-going-on-in-my-shop-currently)

### Inferences (mine)
- **MS43 body-side X6011:**
  - 1: terminal 50 to the starter.
  - 2: terminal-15 feed to the oil-level sensor and alternator regulator.
  - 3: oil-pressure lamp, BR/GN, to X11175-13.
  - 4: charge lamp, to X11175-2.
  - 5: oil-level signal, to X11175-17.
  - 6: start feedback (destination "X276", unidentified).
  - 7: DM-TL heater, BK/RT, on cars built from 09/2001 (Q7).
  - 8: unknown, probably empty on an MK60 Touring.

  Pins 1 and 2 are taken from the M3 side, assuming the same circuits. Colours on 4–6 are inferred from the MS42/M3 chassis colours of the same circuits: BL, WS/GN, and BK/GN or BK/BL.
- **The S54 harness side of X6011 has only pins 1, 2, 7 and 8.** So MS43 pins 3–6 face empty cavities, which is why the 2001 325iT showed neither lamp. MS43 pin 7 (DM-TL heater) faces the M3's clutch wire. If left, the MSS54's clutch input sees the heater circuit, the heater is never driven and a heater fault sets. That likely contributed to JaredMV's DM-TL troubles.
- **Order of work on an MS43 Touring:**
  1. Move the heater from X6011-7 to X60004-18.
  2. Move the clutch BL/BR from X60004-23 into the now-empty body-side X6011-7.
  3. Fit the M3 clutch module, because the 325i module's output is wrong for the MSS54 chain.
  4. Move or jumper X6011-3/4/5/6 to X60004-11/1/21/6. George Hill's alternative is a cut-to-length jumper from X60004-11 to X6011-3.

  X60004 and X6011 use different terminal kits (Tulay), so moving a wire between them means re-terminating it.

### Gaps
- No BMW pin table for the MS43 Touring's X6011. Pins 4–6 rest on two converters, a "from memory" post and an "IIRC".
- "X276" (pin 6's destination) is unidentified.
- terra's "pin 3" text against his own TIS diagram's pin 7: trust the diagram, but confirm on the donor.
- Current availability and supersession of the US 61319122700: one poster calls the newer replacement untested.

## Q3. MSS54HP (from about 09/2003): pin differences that matter for the swap

### Cited findings
- **US pump-module output stays on X60002 pin 11.**
  - WDS screenshot posted by Pnick ("Fuel pump (DME Motor Electronics MSS54 with USA_LHD)", from the bmw-planet WDS mirror) [image]: A6000 X60002 pin 11 → **X6021 pin 1 → "S_EKP 0.35 SW/VI"** → K96 "Fuel pump relay 1" (the EKP module, connector X10157) pin 1. F3 20 A (E-box fuse carrier X8680-6) → "U_HR<3 1.5 RT/WS" → module pin 8. F54 15 A → "30<54 2.5 RT/VI" → pin 6. Pin 2 → "EKPM 2.5 RT/WS" → pump. Pin 7 and pump to ground X13006 — [NAM3 132772 post 12](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/132772-help-fuel-pump-relay-ekp-engine-wiring-schematic), [image](https://nam3forum.com/forums/filedata/fetch?id=133069).
  - gheorghe's 2006 M3 (MSS54HP era): "I have continuity from DME X60002 pin 11 all the way back to the EKP pin 1 (same wire)" (post 20) [read].
  - Lukem3's "2006 is showing pin 10" (post 13) [read] is unexplained, and the measurement above contradicts it for an '06.
- **The workbook's MSS54 tab ("MSS54 DME 901-904")** [read]: X60002-11 "Fuel pump relay 1 USA only"; X60004-10 "not USA"; X60004-18/20/30 DM-TL "USA only". steevo_102 [earlier] said the WDS MSS54 table "applies… from 09/2001 onward".
- **The "Comprehensive MSS54/MSS54HP DME information" thread** [read]:
  - "32kb = MSS54, 64kb = MSS54HP".
  - "Hardware differences are only related to year (HP vs non-HP). Firmware is different though."
  - "You need an HP (or a non-HP converted to HP spec) to run a MAP sensor."

  — [NAM3 2052](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)
- **CAN data.** DME4 byte 6, oil level, is "MSS54HP only" [read, MS4X CAN]. Stock MSS54HP software sends the charge lamp over CAN; older CSL software did not [read, NAM3 61405].
- **TPMS reset input.** MK20 M3s route the reset to the DME (X60003-19 via X6011-8); MK60 M3s route it to the DSC. nextelbuddy guesses that "2003.5 cars engine harness doesn't have that wire" [read, NAM3 243029].
- **ETK** [earlier]: the M3 "engine trans. module" harness changes at 09/2003 (12517831756 → 12517835540) and the engine module at 09/2004.
- **Kassel's chart** treats "MSS54 / MSS54HP" as one [image].
- **The bimmer-service "DME MSS54 (S54) pinout"** [read] is the **Z3 M** table, not E46: it has an LDP leak pump on 28/30, EWS III TD on 17 and reverse light on 19. Its X60002-11 "A_PEKP… Electrical fuel pump relay, timed" and X60002-20 "S_KUPPLU clutch" agree in principle — [bimmer-service](https://www.bimmer-service.com/2025/11/14/dme-mss54-s54-pinout-schematic-diagram/).

### Inferences (mine)
- No source shows an X60004 or pump-output pin change between MSS54 and MSS54HP for the E46. The differences that matter are in software and CAN: charge lamp over CAN, the oil-level byte, MAP support. The DME and its matching harness should still stay together by date.
- An early (pre-09/2001) MSS54 may not drive the DM-TL heater on pin 18. The M3's DM-TL changed at 09/2001 (Q7). Donor date matters for the US leak test.

### Gaps
- No HP-specific WDS X60004 table was found, and no statement of which production range "901-904" covers.
- Whether the 09/2003 trans-module change moved anything in the clutch or gear-switch path or in X6021.

## Q4. When the US 325i Touring changed from MS43 to MS45.1, and how an owner can tell

### Cited findings
- **ETK, US 325i M54 Touring** [read]:
  - Programmed DMEs: MS43 automatic variants to Dec '01 in group 1; group 2 lists MS45.1 "from Mar '03" ([group 2](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/programmed_dme_control_unit_2/)).
  - Basic MS43 units are listed "to Mar '03" ([basic DME](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/basic_cotrol_unit_dme/)).
  - The US 325i sedan shows the same: MS43 "from Jul '02 to Mar '03", MS45.1 "from Mar '03" ([ETK](https://bmwfans.info/parts-catalog/E46-Sedan/USA/325i-M54/browse/engine_electrical_system/programmed_dme_control_unit_2/)).
  - Engine-module harness 12 51 7 513 554 "to 03/2003", then 12 51 7 523 220 [earlier for the 325i Touring, `harness_engine_side.md`, [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/engine_wiring_harness_engine_module/)]. Read today on the 325xi Touring page: "to Mar '03" / "from Mar '03" ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/browse/engine_electrical_system/engine_wiring_harness_engine_module/)).
  - Manual gearbox-module harness 12 51 7 518 041 "from Sep '02 to Mar '03", then 12 51 7 523 223 "from Mar '03" ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/engine_electrical_system/wiring_harness_engine_trans_module/)).
  - Air-mass meter 13 62 1 432 356, one entry marked "to Mar '03"; ETK also lists 13 62 7 566 984 ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/browse/fuel_preparation_system/hot_film_air_mass_meter/)).
  - Secondary-air pump with its own mass-air-flow sensor "from Mar '03" (Q1).
- **BimmerWorld** [read]: "MS43 for 2001-2/2003* 325i/330i, and MS45 for 2/2003-2006 325i/330i… There was a period of six months from 9/2002-3/2003 where BMW mixed MS43 and MS45 components. Ignition coils, valve cover, and coil harness changed early (in 9/2002) but the ECU and engine harness remained MS43 until 2/2003." Also: "There are two transmission harnesses - one for manual (#12517506794) and one for automatic" (early) — [BimmerWorld](https://www.bimmerworld.com/About-Us/MS45-to-MS43-Conversion/).
- **RPM Motorsport** [read]: the MS45.0/MS45.1 support list covers "BMW 3 Series E46 Years 02/2003 to 05/2006". It names 325i sedans (M54 and M56), the 325i Touring (M56), 325Ci and 330i/330Ci; the M54 Touring isn't named, probably an incomplete list. MS45.1 part numbers run 7512523 … 7561383 — [RPM](https://www.rpmmotorsport.net/products/bmw-ms45-0-ms45-1-ecu-repair-dme-ram-checksum-error).
- **Forum identification tips** [snippet]: "3 wires is MS43. 5 wires is MS45" (air-mass meter plug); MS43 "until 02/2003, MS45 from 03/2003"; "XI 01-05 received ms43 for all years" — [e46fanatics "Ms43 or Ms45"](https://www.e46fanatics.com/threads/ms43-or-ms45.1114142/), ["MS45.1 vs MS43"](https://www.e46fanatics.com/threads/ms45-1-vs-ms43.1308066/).
- **Alternator plug.** Tulay lists its three-pin connector as fitting "E46 Alternator (excluding MS45-BSD)" [read], and MS4X shows MS45's X60003-19 as the BSD alternator data line [read]. The MS45.1 car has a data-line alternator.
- **xi cars, conflicting ETK data** [read]:
  - 325xi Touring: programmed DME MS43 "from Jul '02" with no end date, and no MS45.1 group ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/browse/engine_electrical_system/programmed_dme_control_unit/)).
  - 330xi: several MS43 units "from Mar '03" ([ETK](https://bmwfans.info/parts-catalog/E46-Sedan/USA/330xi-M54/browse/engine_electrical_system/programmed_dme_control_unit/)).
  - Against that, the 325xi Touring lists the same "from Mar '03" engine harness 12 51 7 523 220 and the same secondary-air MAF as the 325i ([ETK harness](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/browse/engine_electrical_system/engine_wiring_harness_engine_module/), [ETK SAP](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/browse/engine/emission_control_air_pump_2/)).
  - Part 12517523220's usage list includes 325xi and 330xi ([ETK](https://bmwfans.info/parts-catalog/12517523220/)).

### Inferences (mine)
- **The change is the March 2003 production change.** "02/2003" (BimmerWorld, RPM, the guide) and "03/2003" (ETK) describe the same event: the last MS43 cars were built in February and the first MS45.1 cars in March. A Touring built in February or March 2003 needs a physical check.
- **Owner checks, roughly in order of reliability:**
  1. The DME label in the E-box reads MS43 or MS45.1.
  2. INPA or NCS identification.
  3. ETK by VIN for "Programmed DME".
  4. The DM-TL heater wire (BK/RT) sits in X60004 pin 2 (MS45.1) or in the black 8-pin X6011 (MS43).
  5. X60004 pins 5 and 15 are populated (MS45.1) and a small air-mass meter sits on the secondary-air pump inlet.
  6. The main air-mass meter plug has 5 wires (MS45.1) or 3 wires with a separate intake-air sensor in the manifold (MS43). On MS45.1 cars that manifold port carries a blanking plug (BimmerWorld).
  7. Engine and gearbox-module harness part numbers.
- **Coil type and valve cover don't identify the DME,** because they changed at 09/2002.
- **For a 325xi Touring, never assume.** ETK's DME data and forum posts say MS43 for all years, but its harness and secondary-air listings say otherwise.

### Gaps
- No BMW service information giving the first MS45.1 VIN or production date.
- The xi conflict is unresolved.

## Q5. US M56 SULEV Tourings: harness, E-box, pump control, and S54 swaps

### Cited findings
- **ETK, US 325i M56 Touring** [read]:
  - Programmed DME "12 14 7 577 220 MS45.1 to Sep '05" and 7 562 346 "from Sep '05" ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/engine_electrical_system/programmed_dme_control_unit/)); basic units 7527015 … 7561383, all "MS45.1/FLASH" ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/engine_electrical_system/basic_cotrol_unit_dme/)).
  - Engine module harness 12 51 7 528 594 ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/engine_electrical_system/engine_wiring_harness_engine_module/)).
  - **The only gearbox-module harness listed is 12 53 7 523 597, "For vehicles with Automatic transmission".** The same applies to the M56 sedan and coupe ([Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/engine_electrical_system/wiring_harness_engine_trans_module/), [sedan](https://bmwfans.info/parts-catalog/E46-Sedan/USA/325i-M56/browse/engine_electrical_system/wiring_harness_engine_trans_module/), [coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/325Ci-M56/browse/engine_electrical_system/wiring_harness_engine_trans_module/)). The M54 Touring lists both manual and automatic versions.
  - The shared pedals group lists a clutch-switch module "For vehicles with Manual Transmission" (61319231129) and a five-speed S5D 250G gearbox ([pedals](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/pedals/pedals_stop_light_switch/), [gearbox](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/manual_transmission/manual_transmission_s5d_g/)).
  - "Control unit for fuel pump" 16 14 6 912 019 ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/fuel_supply/control_unit_for_fuel_pump/)). A K96 relay group (61368373700) is also listed ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/vehicle_electrical_system/relay_for_fuel_pump_1_k96/)).
- **BMW bulletin B11 75 02, Oct 2002** [earlier, `fuel_pump_control.md`]: M56 "2003 325iA (E46) sedan, coupe and sport wagon with automatic transmission", for CA, NY and MA, and VT from 2004.
- **"M56 SULEV Manual Trans Swap"** [snippet]: the car "never had a manual from day one" — [e46fanatics 1291304](https://www.e46fanatics.com/threads/m56-sulev-manual-trans-swap.1291304/). Wikipedia's M56 page says "automatic or a manual" [snippet].
- **Pin layout.** MS4X marks X60004 25 (EAC), 31/35 (local CAN to the fuel-pump controller) and X60003 38/51 "only with M56" [read]. The workbook's "MS45 903" tab has exactly this layout, with pin 10 and pin 23 unused [read].
- **Tenza, 2004 ex-M56 Touring** [earlier, captions]:
  - S54 plus 6-speed; Kassel DME and Kassel-programmed cluster.
  - The SULEV tank's single six-wire plug was replaced by an M54/S54-type tank with two plugs; the driver-side sender pair was extended.
  - The M3 charcoal canister was fitted.
  - The E-box fan plug on the M3 engine harness was "left disconnected" because the wagon's fan plug was already fed from the body side.
  - Pump switching after the swap was not shown.
- **M56→M54 conversions (not S54)** [snippet]:
  - "Change EKP for standard Fuel Pump Relay and repin DME" — [e46fanatics 1288397](https://www.e46fanatics.com/threads/m56-to-m54-conversion-afterthoughts-and-information.1288397/).
  - The round SULEV tank connector's six wires map to four pins in the non-SULEV pump connector — [e46fanatics 1268017](https://www.e46fanatics.com/threads/diy-sulev-to-ulev-conversion.1268017/).
  - The EKPS is "either in your trunk or cargo area" [earlier].

### Inferences (mine)
- **ETK does not show a manual M56 build.** The manual parts appear only in shared groups; the M56-specific gearbox-module harness is automatic-only. An M56 Touring with a manual is most likely a conversion. Check the VIN option list.
- **For an S54 in an M56 Touring:**
  - The MSS54 has no local CAN, so the fuel-pump controller can't be commanded. Fit either a K96 relay driven from the MSS54's X60004-10 (that pin is unused in the M56 harness, so a wire has to be added) or the M3 pump module on X60002-11 / X6021-1.
  - The returnless stainless tank must give way to a return-type tank and lines for the M3 filter-regulator. Tenza's route changes a SULEV-certified evaporative system: legal caution.
  - The clutch module, its power, ground and EWS pin-8 wires, and the X6011-7 clutch path all have to be added, because pin 23 is empty on an automatic.
  - Reverse lights move to the manual gearbox-module harness's X6021-3/4.
  - Remove X60004 25, 31 and 35, and 19 (E-box fan), plus everything in the MS45.1 list.

### Gaps
- No documented pump wiring from Tenza's build or any other S54-in-M56 swap.
- Whether the M56 body harness has a wired K96 socket.

## Q6. Swap harnesses and adapters for non-M E46s: what they change, what their instructions say

### Cited findings
- **Kassel Performance:**
  - The chart, analysed above [image]. The MS43 column omits charge lamp, start feedback, DM-TL heater and clutch. The MS45 column omits the clutch, all cluster lamps and the 20/30 DM-TL swap. The oil-pressure cluster pin is given as 14, where two working cars and ISTA say 13.
  - The 2016 post asks builders to "consult the BMW WDS" [read].
  - The DME product page (Oct 2026) [read] offers "Engine Swap Coding (Includes Any/All Options Specific to Swap)" at $349 with a "full consult", "I need a DME $889 or DME Swap Program", "Performance Tune (Only with Swap Coding)" at $349, and a form field for "Chassis, trans, drive by wire, VIN" — [Kassel](https://www.kasselperformance.com/product/bmw-e46-m3-s54-mss54-hp-tuning/). It also lists emissions-equipment deletes (caution, not documented here).
  - Kassel launched "www.S54swap.com" in March 2015 [read, [blog](https://www.kasselperformance.com/blog/)]; the site is now dead.
  - Builders' accounts:
    - Tenza received written instructions [earlier].
    - Trent calls the chart "the brief DIY that Kassel published… Some of the Kassel directions work and some do not" [read].
    - smee123 followed the MS45 column exactly [read].
    - A vendor who thinned Trent's SMG harness, whom he names as Kassel, left O2-sensor wiring "messed up" ("O2 sensors giving crazy readings") [read, post 57].
    - Kassel also "doctor'd" Trent's cluster, which later failed [read, post 69].
- **Redline Motorsport "E46 M52TU, M54, S54 Engine Wiring Swap Harness"** [read]:
  - "M54 must use MS43 DME (MS45 option now available!)… S54 must use MSS54 or MSS54HP DME".
  - "All crimp terminals and connectors are new… Instruction sheets are included".
  - Includes "Electronic pedal wiring (M54 and S54) / Fuel pump wiring and relay / Sport mode button (S54)"; "EWS (Immobilizer) delete is required".
  - $265, no reviews — [Redline](https://www.redline-motorsport.com/product/e46-m52tu-m54-s54/).
- **Race German, same product text** [read, Shopify JSON]:
  - $304.88, "made to order… no refunds".
  - Sold as "original engine / new engine / harness source" variants, including **"M54 (MS43) / S54 / E46"** and **"M54 (MS45) / S54 / E46"**.
  - "If you are using a mechanical gas pedal… let us know" — [Race German](https://racegerman.com/products/e46-m52tu-m54-s54-swap-harness-adapter).
- **Tulay's Wire Werks**, individual parts with pinouts [read]:
  - "M3 Sport Button Wiring": "0.35mm² (Used) Black/Red/Yellow or (New) Black – X60004-15 to X1869-17; 0.35mm² (Used) Black/Gray/Yellow or (New) Gray/Black – X60004-16 to X1869-18"; "The pins used at the X60004 and X1869 connectors are similar but different!" — [Tulay](https://tulayswirewerks.com/product/bmw-e46-m3-sport-button-wiring/)
  - "M3 RDC Initialization Button Wire": "0.50mm² Yellow/Black – X6011-8 to X1869-2" — [Tulay](https://tulayswirewerks.com/product/bmw-e46-m3-rdc-initialization-button-wire/)
  - X6011 kits: body side "8-pin Black Unsealed Receptacle… Both the M54 and S54 engines use this version"; engine side "8-pin Teal… Engine Plug I" — [receptacle](https://tulayswirewerks.com/product/bmw-8-pin-black-unsealed-receptacle-e46-engine-plug-i-x6011-chassis-harness-connector-kit/), [plug](https://tulayswirewerks.com/product/bmw-8-pin-teal-unsealed-plug-e46-engine-plug-i-x6011-engine-harness-connector-kit/)
  - X6053: "white connector of the engine harness that plugs into the transmission harness. The M52TU, MS43 M54 and S54 engines use this version… while the MS45 M54 engine uses a different style white 8-pin connector" — [Tulay](https://tulayswirewerks.com/product/bmw-8-pin-white-unsealed-receptacle-e46-engine-plug-ii-x6053-transmission-harness-connector-kit/)
  - X6021: "4-pin black connector of the transmission harness that plugs into the chassis harness", same on MS43, MS45 and MSS54; MS42 uses round pins. Reverse lights "1.00 mm² Blue – to X6021-3; 1.00 mm² Green – to X6021-4" — [X6021](https://tulayswirewerks.com/product/bmw-4-pin-black-unsealed-plug-e46-engine-plug-ii-x6021-transmission-harness-connector-kit/), [reverse-light lead](https://tulayswirewerks.com/product/e46-reverse-light-switch-wire-harness/)
  - DME connector kit: X60004 takes pins for 0.22–0.35 and 0.50–0.75 mm² wire — [Tulay](https://tulayswirewerks.com/product/siemens-ms42-ms43-ms45-mss54-dme-ecu-connector-kit/)
  - The non-M clutch-module lead and the MS42→MS43 cluster adapter are cited under Q2.
- **Not applicable to an E46 non-M with MSS54** [read]:
  - Kassel's E30 plug-and-play S54 harness (E30 chassis).
  - Road Race Rally Engineering's "S54 adapter", which is for an Ecumaster EMU standalone ([PDF](https://cdn.shopify.com/s/files/1/0451/8563/0367/files/S54_adapter_functions_assignment.pdf)).
  - Harvey Racing (Andrew325is) adapters for E30/E36.

### Inferences (mine)
- **No vendor publishes a harness that does the MS43 or MS45.1 body-side moves for a 325i Touring.** The Redline/Race German adapter lists pedal, pump-relay and Sport wiring, which a 325i already has apart from Sport, and its instruction sheet isn't online. Ask, per variant, whether it handles each of these:
  - the cluster lamps (11→13, 1→2, 21→17);
  - the brake move 28→34;
  - DM-TL 2/X6011-7 → 18 and the 20/30 swap;
  - the clutch move to X6011-7;
  - keeping X6021-1 off K96.
- **Kassel's value is the DME and cluster programming;** its chart needs the corrections above.
- **Tulay's parts are the most precise published references for the Sport, RDC and E-box connector work.**

### Gaps
- Redline/Race German instruction sheets and connector lists are not online.
- No third-party reviews were found.

## Q7. Documented wiring mistakes, how they showed up, and the fixes

| Symptom | Car (DME family) and donor | Cause and fix | Source |
|---|---|---|---|
| No oil-pressure or battery lamp | 2001 325iT, MS43; S54 | MS43 routes lamps through X6011-3/4. Owner joined the M3 harness's X60003-26 wire to the X6011 cluster wire; battery lamp fixed in "15 minutes" | [e46fanatics 1207433](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/) [earlier] |
| Oil lamp goes out at key-on with engine off | 2003 330i ZHP, MS45.1 body; MSS54HP | Cluster pin 13 empty; CAN oil pressure didn't work even when coded. Wire X60004-11 → cluster 13, coded "oil pressure via CAN" off | [NAM3 61405](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off) [read] |
| Kassel's chart didn't cover his car; "moved about 4 wires. One of them, critically, being the oil pressure light" | 330i (03/2002), MS43; SMG M3 donor | Kassel's cluster pin 14 "is not correct"; used X60004-11 → cluster 13. Also wired X60004-1 → cluster 2 | [NAM3 173296 p.4](https://nam3forum.com/forums/forum/main-forum/member-build-journals/173296-trent-s-s54-rebuild-and-sedan-swap/page4) [read] |
| Oil and charge lamps dead | S54-swapped ZHP sedan (DME family not stated) | Oil-pressure lamp wiring routed; charge lamp "turned on with coding" | [NAM3 3768 p.3](https://nam3forum.com/forums/forum/main-forum/member-build-journals/3768-what-s-going-on-in-my-shop-currently/page3) [read] |
| Intermittent stalling and no cruise | Same ZHP | Clutch switch not wired to the DME and the wrong (non-M, black) switch; fixed with the M3 (orange) switch wired correctly | same [read] |
| No cruise | S54 E46 wagon; M3 MK60 and cluster | Junkyard 330i clutch module replaced with a new M3 one | [e46fanatics 1260275](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/) [earlier] |
| No cruise | S54 xi Touring (MS43 assumed for an xi; not stated in the snippet) | Brake and clutch pins relocated, still no cruise; "To get my cruise control working I had to disable the clutch switch 'chain grip' code" | [e46fanatics 1102352 p.6](https://www.e46fanatics.com/threads/s54-xi-touring-swap.1102352/page-6) [snippet] |
| No cruise | ex-automatic 330i, MS45.1; Kassel chart followed | Clutch not on the M3 path; DME must also run manual software | [e46fanatics 1316868](https://www.e46fanatics.com/threads/s54-swap-cruise-control-not-working.1316868/) [snippet] |
| No cruise, ever | 2000 323i, MS42; S54 with 5-speed | No gear-recognition switch on the 5-speed | [e46fanatics 1003871](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/) [earlier] |
| "Yellow brake light" | xi Touring, MS43 | Brake-light test wire still on X60004-28; moving it to 34 cleared it | [e46fanatics 1102352](https://www.e46fanatics.com/threads/s54-xi-touring-swap.1102352/page-6) [snippet] |
| DM-TL faults for about 2 years | S54 wagon, MS43; 09/2001 M3 donor | Heater wire was still in X6011-7 facing the M3's grey wire. Working layout: SW/GN → 20, BR/BL → 30, SW/RT heater → 18. Then passed the California smog referee (Oct 2023) | [NAM3 102198](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/102198-requesting-help-with-dmtl-pinout) [read] |
| DM-TL faults "OE [014] Heating DMTL module", "7F [127] Module, tank-leak diagnosis"; pump current 50+ mA against about 24 mA | Trent's 330i, MS43, after X6011-7 → 18 | Unresolved as of June 2026 (new pump on order; 20/30 assignment being checked) | same thread, posts 5–6 [read] |
| DM-TL code | 2001 325i Touring (early, three-wire DM-TL wiring) | Added the fourth (heater) wire from the DME to the DM-TL; four-wire harness from a junkyard car | [e46fanatics 1127936 p.9](https://www.e46fanatics.com/threads/2001-325i-wagon-in-steel-grey-now-with-s54-swap.1127936/page-9) [snippet] |
| P2418 (switching valve) | non-M, MS45.1 cross-reference | Swapped pins 20/30; code persisted (unresolved) | [e46fanatics 1286041](https://www.e46fanatics.com/threads/e46-m3-sport-button-retrofit-on-non-m.1286041/) [earlier] |
| Pump shadow fault, no CEL | MS45.1 ZHP; MS43 330i; others | US MSS54 on the relay (X60004-10); expected | [Kalim p.38](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38) [earlier], [NAM3 173296](https://nam3forum.com/forums/forum/main-forum/member-build-journals/173296-trent-s-s54-rebuild-and-sedan-swap/page4) [read] |
| Pump won't prime | 2000 323i wagon, MS42 | S54 X6011/X6021 had no mates in the MS42 E-box; fitted junkyard MS43-type body plugs and used X60004-10 | [Kalim p.39](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-39) [earlier] |
| DME relay stays on after key-off; hot PCV solenoid | 2004 ZHP, MS45.1 | Not wiring: a worn ignition switch kept X60004-26 live. An added pin-5 ground did nothing | [NAM3 201716](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/201716-switched-12v-question/page2) [read] |
| O2 sensors "crazy readings" | Trent's 330i | Vendor-thinned SMG harness had O2 wires mixed up | [NAM3 173296 p.4](https://nam3forum.com/forums/forum/main-forum/member-build-journals/173296-trent-s-s54-rebuild-and-sedan-swap/page4) [read] |
| ABS/DSC lights | Trent's 330i | MK20 sensors on one side and MK60 on the other; all MK60 sensors fixed it, plus MK60 coded via ALSZ | same [read] |
| ABS light at first start | Tenza, M56 Touring | Non-M wheel-speed sensors in M3 hubs; plugs differ | [Tenza, part 2](https://www.youtube.com/watch?v=mDBiRn30fEs&t=195s) [earlier] |
| DSC light, "VIN not initialized" | S54 wagon with M3 MK60 | Refitted the wagon's own 325i MK60 | [e46fanatics 1260275](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/) [earlier] |
| Injectors "circuit low" ×6 | 330i with M3 driveline | Suspected X6053/X60531 mismatch from mixed harnesses (unresolved). Tulay: MS45 X6053 is a different style | [e46fanatics 1277127](https://www.e46fanatics.com/threads/s54-swap-fuel-injectors-low-circuit.1277127/) [earlier] |
| EWS/DME sync failure | 2001 325xi wagon, Kassel virgin MSS54, Kassel guide followed (incl. clutch wire to EWS) | Unresolved in snippet | [e46fanatics 1300465](https://www.e46fanatics.com/threads/cant-sync-ews-dme-on-s54-swapped-e46-wagon.1300465/) [snippet] |

### Inferences (mine)
- The recurring failures are:
  - lamp circuits that pass the DME on the M3 but not on the 325i;
  - the clutch chain, by connector position and by module type;
  - the DM-TL positions;
  - mixed-generation parts (sensors, gearbox harnesses).

  A pin-by-pin continuity and voltage check before first start would have caught most of them; see the diagram tables.
- **Stalling is a clutch-chain symptom as well as cruise loss.** BMW describes the chain as an idle-control enable condition [earlier, ST055], and a factory M3 with a bad chain logged "switch chain, frictional connection" [read, NAM3 225235].

### Gaps
- No report shows the symptom of leaving the brake wire on pin 28 beyond the snippet's "yellow brake light".

## Diagram-ready data

Columns: connector, pin, action, wire colour (BMW codes), from, to, function, sources agreeing / disagreeing. "Body" means the Touring's chassis harness. "M3" means the donor engine harness and gearbox-module harness, kept together. Cluster = M3 cluster plug X11175.

### MS43 receiving car (US 325i Touring built to 02/2003; also check any 325xi). Donor: MSS54 or MSS54HP

| Connector | Pin | Action | Wire colour | From | To | Function | Agreeing / disagreeing |
|---|---|---|---|---|---|---|---|
| X60004 | 28 → 34 | Move | BR/GR (MS4X); "BR/GN" per Kassel and workbook | X60004-28 | X60004-34 | Brake-light test switch (second contact) | Agree: Kassel MS43 column; workbook; e34m5freak199; xi Touring (cleared "yellow brake light"). Colour: MS4X and the M3 harness (pin 34 BR/GR) against Kassel's BR/GN, probably the GR = grey misreading |
| X6011 (body) | 7 → X60004-18 | Move (cars built from 09/2001) | BK/RT (SW/RT) 0.75 | DM-TL X17140-2, via body X6011-7 | X60004-18 | DM-TL heater | Agree: JaredMV (working), Trent, nextelbuddy, workbook, MS43→MS45.1 conversion, MS4X (X60003-51 SW/RT). Kassel MS43: omits |
| X60004 | 18 | Add (cars built before 09/2001) | new 0.75 | X60004-18 | DM-TL pin 2 (fit the four-wire pump 16137193479) | DM-TL heater | 2001 Steel Grey 325iT [snippet]; ETK DM-TL change 09/2001; DBO 2001 330Ci three-wire |
| X60004 | 20, 30 | No change | 20 SW/GN (valve); 30 BR/BL (pump) | DM-TL 3 / 1 | same | DM-TL valve / pump | Agree: JaredMV (passed California referee), MS4X MS43, MSS54 TIS naming. Disagree: nextelbuddy's "all M3s: BR/BL → 20" |
| X60004 | 23 → body X6011-7 | Move (after the heater has left X6011-7) | BL/BR 0.35 (body); becomes GR "KUPPL" in the M3 harness | Clutch module pin 2 | X6011-7 → X6053-5 → gear switch X5271 1→2 → X60002-20 (GR/BL) | Clutch + gear-recognition chain (cruise, idle enable) | Agree: BMW TIS diagram (terra); NAM3 race-car ID (X6011-7 GR to X6053); yayyap159; DaveVolvoBMW. Disagree: terra's text "X6011 pin 3"; Trent wired 23 → X60002-20 directly (SMG donor, no gear switch) |
| Clutch module | — | Replace | — | 325i module 61319231129 (black; switches to ground) | M3 module 61319122700 (US; orange/brown; switches +12 V) or 61319122701 (Euro, needs EWS interlock coded off) | Correct output for MSS54 X60002-20 | Agree: terra; George Hill; ewcmr2; ETK usage; Pklauser (Euro part) |
| X6011 (body) | 3 → X60004-11 | Move or jumper | BR/GN | Cluster X11175-13 wire (body X6011-3) | X60004-11 | Oil-pressure lamp (DME passes switch input X60003-26 to output 11) | Agree: ISTA via George Hill; snaponbob; Trent (to cluster 13); nextelbuddy. Disagree: Kassel ("pin 14 of cluster") |
| X6011 (body) | 4 → X60004-1 | Move or add | BL (inferred) | Cluster X11175-2 wire | X60004-1 | Charge lamp (terminal 61) | Agree: Trent (1 → cluster 2, working); workbook; MS42→MS43 thread (X6011-4 → cluster 2); e34m5freak199. Kassel MS43: omits |
| X6011 (body) | 5 → X60004-21 | Move or add | WS/GN (inferred) | Cluster X11175-17 wire | X60004-21 | Oil-level signal | Agree: Kassel (21 → cluster 17); Trent; workbook; MS42→MS43 thread; redneckvtek (pin 17 on both) |
| X6011 (body) | 6 → X60004-6 | Move (optional) | BK/GN or BK/BL (inferred) | Start-feedback wire (to "X276") | X60004-6 | Terminal 50 / start signal to cluster | e34m5freak199 ("started without this"); MS42→MS43 thread. Not in Kassel |
| X60004 | 15, 16 | Add (optional) | 0.35; OEM BK/RT/GE and BK/GR/GE (Tulay) or BK/GN with yellow dots (e34m5freak199) | Switch centre X1869-17 / -18 | X60004-15 / -16 | Sport input / Sport LED | Agree: Kassel; workbook; steevo_102; Tenza; Tulay. Base Tourings may lack a switch centre, power and K-bus |
| X60004 | 10 | No change | SW/VI 0.35 | X60004-10 | K96 coil | Fuel-pump relay (MSS54 "not USA" output) | Agree: MS4X MS43; George Hill; NAM3 82513. Expect a stored pump-module fault without check-engine lamp |
| X6021 | 1 | Check | SW/VI 0.35 (M3 side) | M3 X60002-11 → X6021-1 | Must not reach K96 | US pump-module PWM signal | WDS (Pnick); Andrew325is; Tulay. Body-side mate on a 325i: unknown |
| X6011 | 1, 2 | No change | M3: 1 BK, 2 GN | — | — | 1 terminal 50 to starter; 2 terminal-15 feed to oil-level sensor and alternator regulator | NAM3 116033; Andrew325is; nextelbuddy |
| X6011 | 8 | None | GE/BK (M3 side) | M3 X60003-19 | Body side probably empty (MK60) | TPMS init (MK20 cars) | NAM3 243029; Tulay RDC wire (X6011-8 ↔ X1869-2) |
| X60004 | 5 | None | — | — | — | MSS54 ground; empty on MS43 | TIS; smee123 test (no effect) |
| X6053 | all | Mate M3 to M3 | Mostly red feeds; pin 5 = clutch path | M3 engine harness | M3 gearbox-module harness | Engine harness ↔ gearbox harness | Tulay (MS43 and S54 same style); TIS diagram |
| Cluster coding | — | Code | — | — | — | CAN_OELDRUCKSCHALTER nicht_aktiv; GENERATOR_UEBER_CAN and TOG_UEBER_CAN to match wiring | Bimmerfest list; e46fanatics 1330549 [snippet] |

### MS45.1 receiving car (US 325i Touring built from 03/2003; also US 325i/330i/ZHP sedans and coupes). Donor: MSS54 or MSS54HP

| Connector | Pin | Action | Wire colour | From | To | Function | Agreeing / disagreeing |
|---|---|---|---|---|---|---|---|
| X60004 | 28 → 34 | Move | BR/GR (MS4X); "BR/GN" per Kassel | X60004-28 | X60004-34 | Brake-light test switch | Agree: Kassel MS45 column; smee123 |
| X60004 | 2 → 18 | Move | SW/RT 0.75 | X60004-2 | X60004-18 | DM-TL heater | Agree: Kassel; smee123; BH93; nextelbuddy; MS4X |
| X60004 | 20 ↔ 30 | Swap | BR/BL 0.75 (pump) 20 → 30; SW/GN 0.5 (valve) 30 → 20 | X60004-20/30 | X60004-30/20 | DM-TL pump / valve to MSS54 positions | Agree: MS4X colours against MSS54 TIS and JaredMV's working layout; steevo_102 ("reversed"); BH93 ("swap the DMTL plugs"). Disagree/omit: Kassel; nextelbuddy's M3 mapping. steevo still had P2418 |
| X60004 | 5 | Remove | SW/GE (BK/GE) 0.5 | X60004-5 | Insulate and tie back | Secondary-air HFM ground (pin is an MSS54 ground) | Agree: Kassel; smee123; ETK secondary-air MAF from Mar '03 on the 325i Touring; MS4X "only with MS45.1". Workbook tags "3.0 USA" |
| X60004 | 15 | Remove | SW/RT (BK/RT) 0.5 | X60004-15 | Insulate | Secondary-air HFM signal (would hit MSS54 Sport input) | Agree: Kassel; smee123 |
| X60004 | 19 | Remove if populated | BR/OR 0.5 | X60004-19 | Insulate | E-box fan (automatic/SMG/hot-climate only) | Kassel; smee123; ETK blower applicability |
| X60004 | 18 | Check empty before the heater move | GR/VI if present | — | — | Exhaust flap (3.0-litre only) | MS4X; workbook |
| X60004 | 23 → body X6011-7 | Move | BL/BR 0.35 | Clutch module pin 2 | X6011-7 → X6053-5 → gear switch → X60002-20 | Clutch chain | TIS diagram; nextelbuddy (MS45.1 X6011 "only two" pins used). Kassel omits; e46fanatics 1316868: no cruise after Kassel chart only |
| Clutch module | — | Replace | — | 61319231129 | 61319122700 (US) or …701 (Euro + EWS interlock coded off) | M3 output polarity | As MS43 table |
| X60004 | 11 | Add | new 0.35, BR/GN to match | X60004-11 | Cluster X11175-13 (empty on MS45.1) | Oil-pressure lamp; code CAN_OELDRUCKSCHALTER nicht_aktiv | Agree: nextelbuddy (CAN didn't work with MSS54HP); George Hill. Disagree: Kassel "ADD N/A" |
| X60004 | 1 | Add, or code GENERATOR_UEBER_CAN aktiv | new 0.35 | X60004-1 | Cluster X11175-2 | Charge lamp | nextelbuddy (CAN works with stock MSS54HP, not old CSL software); George Hill ("turned on with coding") |
| X60004 | 21 | Add, or keep TOG_UEBER_CAN aktiv | new 0.35 | X60004-21 | Cluster X11175-17 | Oil level | nextelbuddy (CAN worked); workbook ("add anyway") |
| X60004 | 10 | No change | SW/VI 0.35 | X60004-10 | K96 coil | Fuel-pump relay | MS4X MS45; workbook MS45.1 tab; nextelbuddy's MS45.1 ZHP ran on it. Disagree: the "MS45 903" tab (M56 layout) |
| X60004 | 15, 16 | Add (optional, after removing the HFM wire) | as MS43 table | X1869-17/18 | X60004-15/16 | Sport | Tenza; Tulay; Kassel ("remove 15" first) |
| X6053 | — | Do not mate the Touring's MS45 gearbox harness to the S54 engine harness | — | — | — | Engine harness ↔ gearbox harness | Tulay: MS45 uses a different X6053 style; use the M3 gearbox-module harness |
| X6011 | 1, 2, 8 | As MS43 table | | | | | |
| X60004 | 5 ground | Not needed | — | — | — | — | smee123 added one: no change |

### M56 SULEV receiving car (US 325i M56, MS45.1 SULEV, automatic-only in ETK). Rows in addition to the MS45.1 table

| Connector | Pin | Action | Wire colour | From | To | Function | Agreeing / disagreeing |
|---|---|---|---|---|---|---|---|
| X60004 | 31, 35 | Remove / insulate | GN; BL/GN | X60004-31/35 | — | Local CAN to the fuel-pump controller (EKPS), unused by MSS54 | MS4X "only with M56"; workbook "MS45 903" |
| X60004 | 25 | Remove / insulate | BL/GE | X60004-25 | — | EAC sensor (M56 only) | MS4X; workbook |
| X60004 | 10 | Add (if fitting a relay) | new SW/VI 0.35 | X60004-10 | K96-type relay coil | Pump relay (pin unused in the M56 harness) | Inference; M56→M54 "repin DME" [snippet]; ETK lists K96 parts for the M56 |
| X6021 / X60002 | 1 / 11 | Alternative | SW/VI (M3) | M3 X60002-11 → X6021-1 | M3 pump module 61357892976 | US pump module | WDS (Pnick) |
| Tank / lines | — | Replace | — | M56 returnless stainless tank (one 6-wire plug) | M54/S54-type tank and return lines | Fuel supply | Tenza. **Legal caution: changes a certified SULEV evaporative system** |
| Clutch module and leads | 1–4 | Add | BR/BK ground, VI/GE term R (F9), BL/BR signal, BL/BK EWS-8 | — | Clutch module; signal to X6011-7 | Manual conversion | Tulay clutch lead; TIS diagram |
| X6021 | 3, 4 | Rework | BL, GN 1.0 | — | Manual gearbox-harness reverse-light switch | Reverse lights (automatic used a relay) | Tulay reverse-light lead; ShopLifeTV [earlier] |
| E-box fan plug | — | Leave M3 plug unplugged if the body already feeds a fan | — | — | — | E-box blower | Tenza |

### MS42 receiving car (US 323i/328i 1999–2000), for reference only; not the target

| Connector | Pin | Action | Wire colour | From | To | Function | Agreeing / disagreeing |
|---|---|---|---|---|---|---|---|
| X60004 | 7–9, 12–14 | Add | Kassel colours (BR/GN, WS, GE, BR, WS/GN, GE/GN) | Pedal R10 pins 1/4/5/2/6/3 | X60004 | Electronic pedal (cable-throttle cars) | Kassel; Import Modify (on camera) |
| X60004 | 28 → 30; 30 → 20 | Move | BR/GN; BR/BL | | | Leak-test pump wiring to DM-TL positions | Kassel; Import Modify |
| X60004 | 1, 2 | Remove (Kassel) | BL; BK/GN | | | MS42 charge lamp / start feedback | Kassel; Import Modify did it. Disputed: the MSS54 uses pin 1 for the charge lamp |
| X6011 / X6021 | — | Fit MS43-type body plugs | — | | | MS42 X6011 is 2-pin and X6021 has round pins | nextelbuddy 2000 323i wagon; Tulay |
| X60004 | 10 | No change | SW/VI | | K96 | Pump relay | nextelbuddy; NAM3 82513 |

### E-box plug map (both Touring generations)

| Plug | What it joins | M3 contents relevant to the swap | Touring side | Notes |
|---|---|---|---|---|
| X6011, black 8-pin, "engine plug I" | Engine harness ↔ chassis harness | 1 BK terminal 50; 2 GN terminal 15 (oil-level sensor, alternator); 7 GR clutch "KUPPL"; 8 GE/BK TPMS init (MK20) | MS43: 1, 2, 3 oil pressure, 4 charge, 5 oil level, 6 start feedback, 7 DM-TL heater (from 09/2001). MS45.1: "only two" pins used | Same style on M54 and S54 (Tulay); MS42 is 2-pin |
| X6021, black 4-pin, "engine plug II" | Gearbox-module harness ↔ chassis harness | 1 SW/VI pump-module signal (US M3 only, WDS); 3/4 reverse-light switch (1.0 mm², Tulay). Tulay's kit also has one 1.5–2.5 mm² pin, so probably one heavy feed | Same housing style on MS43 and MS45 (Tulay) | Inference: this is both the "4-pin black plug" with the black/violet pump wire (nextelbuddy, US M3 harness) and e34m5freak199's "3-pin plug" with "2 for revers… and 1 really thick wire" (three wires used on a non-US harness without the pump-module signal) |
| X6053, white 8-pin | Engine harness ↔ gearbox-module harness | Mostly red feeds; pin 5 clutch path to gear switch | MS43 same style; MS45 different style | Keep the M3 engine and gearbox harnesses together |
| X6506, white | E-box fan (engine harness) | M3 fan feed | Fan plug may already be fed from the body (Tenza) | |
| X64102, single red 4.0 mm² | B+ to DME relay K6300 terminal 30 | — | — | From the K6300 TIS image posted by heinzboehmer, [NAM3 201716](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/201716-switched-12v-question) |
