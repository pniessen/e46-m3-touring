# Wiring and coding manual

This is the bench companion to the [E46 M3 Touring conversion guide](README.md). It covers a US 2001–05 BMW E46 325i Touring (rear-wheel drive, 5-speed manual, M54 engine, Siemens MS43 or MS45.1 DME, Teves MK60 DSC) taking the S54 engine, its MSS54 or MSS54HP DME and its engine harness from a US 2001–06 E46 M3 with a manual gearbox. The guide's [Deep dive: electronics and coding](README.md#deep-dive-electronics-and-coding) explains the choices and the order of work. This page has the pins, the checks and the coding sessions.

> [!WARNING]
> The pins, colors and sizes here come from BMW's own wiring diagrams (WDS, read on a public mirror), its parts catalog and its training documents, checked against documented builds. WDS has no VIN filter and never says which face of a connector it shows. Before you move a wire, check it on your car: the cavity number moulded into the housing, the wire's color and size, and what the wire does ([checks before first power-up](#checks-before-first-power-up)). ISTA shows the diagrams for your exact VIN ([Factory documentation and coding kit](README.md#factory-documentation-and-coding-kit)). Where sources disagree, the tables give the better-sourced value and flag the other.

> [!CAUTION]
> Three limits apply throughout. The EWS delete appears only as a service you buy or a tool function you run. Nothing here removes or disables an emissions function. Cluster work only ever sets a replacement cluster to your car's true mileage ([49 U.S.C. §32704](https://www.law.cornell.edu/uscode/text/49/32704)).

**Conventions.**

- Wire colors use the German codes WDS prints: BL blue, BR brown, GE yellow, GN green, GR gray, OR orange, RS pink, RT red, SW black, VI violet, WS white. BR/GN is brown with a green stripe. GR is gray, not green: one swapper misread it ([e46fanatics](https://www.e46fanatics.com/threads/manual-swap-wiring-with-mss54-dme.1316134/)). Vendors and forums often write BK for black. Wire sizes are in mm².
- "Pin 28 → 34" means move the wire from pin 28 to pin 34 of the same plug.
- "SP" numbers are WDS drawings and "PA" pages its pin tables, linked to the mirror at [wds.psjr.org](https://wds.psjr.org/en/e46/). WDS dates such as 2001_09 mean "built from 09/2001".
- "MS45.1" is the US 325i Touring's DME from 03/2003; Kassel's chart and most forum posts call it "MS45" ([Which DME your Touring has](#which-dme-your-touring-has)).
- The "pinout sheet" is nextelbuddy's DME pin workbook, a community transcription of WDS pin tables. Its "MS45.1 X3ZHP" tab is a 3.0-litre table for the 330i ZHP and X3, and its "MS45 903" tab is the M56 SULEV layout ([pinout sheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)).
- Tool32 jobs are written as Tool32 shows them. Their files live in `C:\EDIABAS\ECU\`, and a community repository documents the jobs ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)). Fault numbers are given as INPA prints them, in decimal, with the job file's hex location in brackets: 130 (0x82).

<!-- toc -->
**Contents:** [Before you start](#before-you-start) · [Engine harness and DME](#engine-harness-and-dme) · [Body-side wiring](#body-side-wiring) · [Fuel-pump control](#fuel-pump-control) · [Checks before first power-up](#checks-before-first-power-up) · [Coding step by step](#coding-step-by-step) · [Readiness and inspection](#readiness-and-inspection) · [Troubleshooting](#troubleshooting)
<!-- /toc -->

## Before you start

### Hardware

| Item | What to get | Why |
|---|---|---|
| Laptop | A Windows 10 or 11 laptop (64-bit is fine) running Windows directly, not in a virtual machine or Boot Camp, and plugged into its charger | Bali's install guide covers Windows 7–11; virtual machines lag and break flashes ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/)). Advice in 2015–16 videos that the tools need 32-bit Windows XP is out of date; a 2025 video installs them on Windows 10/11 ([Nick Goonan – Install INPA, NCS Expert, WinKFP and Tool32 on Windows 10/11 (2025), 00:32](https://www.youtube.com/watch?v=62pyWB4x03w&t=32s)) |
| Diagnostic cable | A K+DCAN USB cable with a genuine FTDI chip and a switch that bridges OBD pins 7 and 8 | The E46's DME is on pin 7 and every other module on pin 8. Without the bridge you reach the DME but not the cluster, light module or DSC ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/293965-verify-ncsexpert-function-before-doing-manual-swap)). If the cable has no switch, solder the pads for pins 7 and 8 together ([MS4X wiki](https://www.ms4x.net/index.php?title=How_to_connect)) |
| PA-Soft interface | The separate interface that BMW Scanner 1.4 (PA-Soft) uses | Needed for the cluster and light-module memories and the DSC's VIN. Its driver is the install step most likely to fail on Windows 10/11 ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/204464-help-with-coding-issues-re-ncs-and-pasoft), [e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/)) |
| Power supply | A battery charger or power supply that delivers at least 10 A in supply mode | A sagging battery breaks flashes and long coding sessions; ECUWorx uses a CTEK MXS 10 ([ECUWorx](https://www.ecuworx.co.uk/how-to/using-the-mss5x-binary-modification-tool/)) |
| Cluster chip tools (DIY route only) | An EEPROM programmer such as the R270, a hot-air rework station and blank M35080 chips | See [Session 4](#session-4-cluster-and-light-module) ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)) |
| Wiring tools | Depinning keys, a multimeter with back-probe pins, BMW pre-crimped repair leads, labels | See [Terminals, tools and repair leads](#terminals-tools-and-repair-leads) |

If your car has a round 20-pin socket under the hood, you need an adapter and must plug in there: on those cars the under-dash socket reaches only the engine and gearbox modules ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/)).

### Software that works and software that doesn't

BMW's programs and data files are BMW-internal or community-modified files that circulate through forums and vendors; there's no official download ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/)).

| Program | Used for | What works | Avoid or watch |
|---|---|---|---|
| BMW Standard Tools 2.12 (EDIABAS, INPA, Tool32, NCS Expert, WinKFP) | Everything below | Run the installer in compatibility mode, untick the two backup-wizard boxes, then replace `C:\EC-APPS`, `C:\EDIABAS` and `C:\NCSEXPER` with a pre-filled package that already holds the INPA scripts and E46 data files ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/), [Nick Goonan (2025), 02:41](https://www.youtube.com/watch?v=62pyWB4x03w&t=161s)) | The installer alone has no INPA scripts or data files |
| INPA | Fault memory, live data, DSC routines, adaptations. The S54 is under E46 → Engine → "MS S54 for S54 M3" ([bmwfaq](https://bmwfaq.org/threads/duda-con-el-inpa.796332/)) | Builds 3.0.1 and 4.4.7 are reported to have the MK60 steering-angle page ([e46fanatics](https://www.e46fanatics.com/threads/dsc-mk60-replacement-coding-with-ncs-expert.1286178/)) | Two owners' builds lacked it: one labelled "EA-90X 5.00" ([e46fanatics](https://www.e46fanatics.com/threads/dsc-mk60-replacement-coding-with-ncs-expert.1286178/)) and another "5.0.2" ([e46fanatics](https://www.e46fanatics.com/threads/steering-angle-calibration-not-showing-up-in-inpa.1285802/)). A 2016 setup video installs 5.0.1 ([ShopLifeTV – How to set up INPA and NCS Expert (2016), 06:27](https://www.youtube.com/watch?v=9GS21wpt7l4&t=387s)). Keep Tool32 as the fallback |
| Tool32 | Single jobs: EWS, DME VIN, adaptations, steering angle | Any working install | If its result grid misbehaves, register its grid control (below) |
| NCS Expert | Vehicle order and module coding | Version 3.0.x, with the "Expert Mode" and "Factory Coding" profiles and a manipulation profile (Revtor's or FISTER) for writing edited coding files ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-fa-for-at-mt-swap.1290835/), [ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf)) | One forum reply blames "IFH-0009: No Response from Controlunit" in NCS on version 4.x ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/204464-help-with-coding-issues-re-ncs-and-pasoft)) |
| NCS Dummy | Editing coding parameters by name | Optional ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap)) | |
| PA-Soft (BMW Scanner 1.4) | Cluster and light-module memories, DSC VIN | With its own interface | Driver trouble on Windows 10/11 |
| E46 data files (SP-Daten) | The coding rules NCS Expert applies | Bali's package; one M3 owner updated to v69 ([e46fanatics](https://www.e46fanatics.com/threads/ncs-expert-dsc-mk60-car-brain-farts.1305967/)) | Cars built from 2005 may need newer files than older packages carry ([ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf)) |
| BMWFlash (licensed) or MSS Flasher | Reading and reflashing the DME for a DIY delete | The free BMWFlash only reads ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)) | Only needed if you do the delete yourself |
| ISTA | Guided service functions | Optional | Its EWS sync was greyed out in one Touring swap ([e46fanatics](https://www.e46fanatics.com/threads/ews-synch-for-s54-swap-into-e46-touring.1318881/)) |

Generic tools can't do this work. BimmerGeeks' ProTool reads E46 faults but can't code an E46 ([BimmerGeeks](https://www.bimmergeeks.net/protool)), and the Foxwell NT530 has a steering-angle reset and a brake-bleed mode but no module coding ([BimmerWorld](https://www.bimmerworld.com/Tools/Foxwell-NT530-OBD-System-Scanner-for-BMWs.html)).

### Cable and EDIABAS settings

| Setting | Value | Where |
|---|---|---|
| COM port | COM1 | Device Manager → Ports → USB Serial Port → Port Settings → Advanced ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/), [Nick Goonan (2025), 05:53](https://www.youtube.com/watch?v=62pyWB4x03w&t=353s)) |
| `obd.ini` | `Port=Com1` under `[OBD]`, matching Device Manager; the two "must always match" | `C:\EDIABAS\BIN\obd.ini` ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/)); a 2026 guide also copies it to `C:\Windows` ([tippsling](https://tippsling.de/windows-11-bmw-standard-tools-installieren-so-gehts/)) |
| Latency timer | 1 ms (Windows' default is 16) | Same Advanced page. At 16, INPA's battery and ignition indicators "go crazy" ([BMW Doctor – K+DCAN settings for INPA and ISTA (2024), 03:36](https://www.youtube.com/watch?v=2Oebra7Kbn0&t=216s)). The 16 ms in the MS4X wiki is for MS42/MS43 flashing, not this work ([MS4X wiki](https://www.ms4x.net/index.php?title=How_to_connect)) |
| EDIABAS interface | `Interface = STD:OBD`, not remote or ENET | `C:\EDIABAS\BIN\EDIABAS.INI` ([BMW Doctor (2024), 01:35](https://www.youtube.com/watch?v=2Oebra7Kbn0&t=95s)) |
| Paths | Keep the default `C:\` folders and add `C:\EDIABAS\BIN` to the system Path | ([tippsling](https://tippsling.de/windows-11-bmw-standard-tools-installieren-so-gehts/)) |
| Tool32 grid control | From an administrator prompt run `regsvr32 "c:\ediabas\bin\msflxgrd.ocx"`; on 64-bit Windows copy the OCX files to `C:\Windows\SysWOW64` first | ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/), [tippsling](https://tippsling.de/windows-11-bmw-standard-tools-installieren-so-gehts/)) |

Run one program at a time: INPA, NCS Expert and Tool32 can't share the cable ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/)). Connect the cable to the laptop and the car before you start INPA ([tippsling](https://tippsling.de/windows-11-bmw-standard-tools-installieren-so-gehts/)).

### Prove the setup on your Touring

Do this on the unmodified car, before you take anything apart.

1. Connect the charger. Turn the ignition to position 2 with the accessories off.
2. Start INPA. Two solid black dots at the top of the main screen mean it's connected; empty circles mean it isn't ([e46fanatics](https://www.e46fanatics.com/threads/installing-bmw-standard-tools.1322014/)).
3. Read the fault memory of the DME and, on cars built before 09/2001, the KMB and EWS, or from 09/2001 the AKMB and ALSZ (same source). Read the DSC's too.
4. Read the vehicle order in NCS Expert ([Session 1](#session-1-vehicle-order-and-codings)).

If the DME answers but the cluster and light module don't, check the pin 7/8 bridge and the COM port first ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/293965-verify-ncsexpert-function-before-doing-manual-swap)).

### Back up everything first

| What | Tool | How |
|---|---|---|
| Vehicle order (FA) or ZCS | NCS Expert | [Session 1](#session-1-vehicle-order-and-codings), steps 1–3 |
| The coding of every module: KMB or AKMB, LSZ or ALSZ, GM5, DSC, EWS, IHKA or IHKR | NCS Expert | Session 1, step 4: save each `FSW_PSW.TRC` in a folder named after the module |
| Cluster memory (EEPROM) | PA-Soft | Read the cluster's EEPROM and save the file |
| Light-module memory | PA-Soft | Read the light module's EEPROM and save the file |
| Mileage | Camera, PA-Soft | Photograph the odometer and note the light module's mileage, with the date |
| Fault memories | INPA | Read every module; save or photograph the lists |
| DSC identity | INPA or PA-Soft | Note the unit's part number and coding index ([e46fanatics](https://www.e46fanatics.com/threads/mk60-coding-index-the-following-control-unit-is-not-allowed-for-this-coding-job.1264623/)) |
| Your DME's wires | Tool32, a test lamp | Before your Touring's DME comes out, run its leak-test jobs (and `STEUERN_EKP`, `STEUERN_E_LUEFTER`) and tag each X60004 wire with what it does ([DM-TL leak-test pump](#dm-tl-leak-test-pump-test-before-you-swap)) |

Copy the folder off the laptop as well.

**While the donor still runs** (Phase 1):

- Read every module's identity and faults in INPA.
- Save the M3 cluster's EEPROM with PA-Soft and keep that file untouched.
- Run the DME read steps in [Session 2](#session-2-dme-vin-ews-delete-and-gearbox-software).
- Save the donor's light-module coding, to compare lighting settings later.
- Note whether it's an SMG car, which buttons its switch center has, and its build date: it sets the DSC unit (an MK20 before 09/2002), the wheel-speed sensors and the leak-test layout (a heater output from 09/2001).
- Before you strip it, confirm on the donor what WDS shows: a 0.35 BR/SW ground wire in its body-side X60004 pin 5, and the gray clutch wire in X6011 pin 7. Take its clutch-switch module (61319122700).

## Engine harness and DME

The pins, colors and sizes in this chapter come from BMW's Wiring Diagram System (WDS), read on a public mirror ([WDS](https://wds.psjr.org/en/e46/)), with BMW's parts catalog (ETK) and training documents. Each move names the WDS drawing it rests on; the "SP" numbers link to the drawings. WDS has no VIN filter: every drawing is titled with the models, markets and build dates it covers, and you pick the one that fits your car. ISTA, BMW's dealer software, shows the diagrams for your exact VIN; a one-day subscription to BMW's official portal cost \$32 in October 2026 ([BMW AOS](https://bmwtechinfo.bmwgroup.com/)). Where vendor charts or builders say something else, the tables say so.

### Re-pin or swap harness

| Approach | What you do | For | Against |
|---|---|---|---|
| **Re-pin (recommended)** | Fit the complete M3 engine harness and DME, then move a few wires in your X60004 and in the body side of the E-box plug X6011 | Factory connectors and terminals; on an MS42 323i, "I only had to re-pin the X60004 connector on few places, everything else is just plug and play" ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)) | You must get every pin right |
| Swap harness | Redline's adapter (\$265) or Race German's (\$304.88, made to order, no refunds), both sold per DME family, including "M54 (MS43) / S54" and "M54 (MS45) / S54". New connectors, pedal, pump-relay and Sport wiring; needs an EWS-deleted DME ([Redline](https://www.redline-motorsport.com/product/e46-m52tu-m54-s54/), [Race German](https://racegerman.com/products/e46-m52tu-m54-s54-swap-harness-adapter), October 2026) | Leaves your factory plugs alone | Neither publishes its circuit list or instructions. Ask whether it covers the cluster lamps, the brake-switch move, the leak-test heater, the clutch move to X6011 pin 7, and keeping X6021 pin 1 off the pump relay |
| Splicing | Cutting and soldering into the harness | None | "cutting/soldering a BMW harness is the last resort...and not a very good one at that" ([e46fanatics](https://www.e46fanatics.com/threads/330ci-engine-swap-no-start-looking-for-help.1298699/)) |

The guide explains the choice in [Harness and re-pinning](README.md#harness-and-re-pinning).

### Which DME your Touring has

The US 325i Touring changed DME with March 2003 production: MS43 before, MS45.1 from then on ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/programmed_dme_control_unit_2/), [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/basic_cotrol_unit_dme/)). BimmerWorld and RPM Motorsport say 02/2003; that's the same change, since the last MS43 cars were built in February and the first MS45.1 cars in March ([BimmerWorld](https://www.bimmerworld.com/About-Us/MS45-to-MS43-Conversion/)). Three names cause confusion:

- **ETK** calls the US 2.5-litre unit "MS45.1". Kassel's chart and most forum posts write "MS45" for it.
- **WDS** calls the whole family "MS45", but its MS45 pin tables are drawn for the M56 SULEV car: a pump controller on a local CAN at pins 31 and 35, an EAC sensor on pin 25, and nothing on pins 10 and 23 ([WDS PA6000P](https://wds.psjr.org/en/e46/zinfo/E46_PA6000P.htm), [SP0000018268](https://wds.psjr.org/en/e46/svg/SP0000018268.svg)). WDS's own M54 drawings put the pump relay on pin 10 and the clutch on pin 23, as on the MS43 ([SP0000014336](https://wds.psjr.org/en/e46/svg/SP0000014336.svg), [SP0000016193](https://wds.psjr.org/en/e46/svg/SP0000016193.svg)).
- **The pinout workbook's "MS45.1 X3ZHP" tab** is a 3.0-litre table for the 330i ZHP and X3, and its "MS45 903" tab is the M56 layout ([pinout sheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit?usp=sharing)).

**How to tell which you have**, most reliable first:

1. **The DME label** in the E-box: MS43 or MS45.1.
2. **INPA or NCS Expert** identifies the DME.
3. **ETK by VIN**, under "Programmed DME control unit": the manual-gearbox MS45.1 units are 12147561526 (03/2003–07/2004), 12147561528 (07/2004–09/2005) and 12147562340 (from 09/2005) ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/programmed_dme_control_unit_2/)).
4. **Where the leak-test heater wire sits** (0.75 mm² SW/RT): in X60004 pin 2 on an MS45.1; in the body side of X6011, pin 7, on an MS43 built from 09/2001 ([SP0000018609](https://wds.psjr.org/en/e46/svg/SP0000018609.svg), [SP0000017260](https://wds.psjr.org/en/e46/svg/SP0000017260.svg)).
5. **X60004 pins 5 and 15** carry wires (0.5 mm² SW/GE and SW/RT) on an MS45.1. They serve a small air-mass sensor at the secondary-air pump, which ETK lists for the 325i Touring from 03/2003 (11721438814) ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/emission_control_air_pump_2/), [SP0000019608](https://wds.psjr.org/en/e46/svg/SP0000019608.svg)).
6. **The main air-mass meter's plug** is said to have five wires on an MS45.1 and three on an MS43 ([e46fanatics](https://www.e46fanatics.com/threads/ms43-or-ms45.1114142/), unverified).

Don't go by the coils or the valve cover: BMW changed those at 09/2002, before the DME ([BimmerWorld](https://www.bimmerworld.com/About-Us/MS45-to-MS43-Conversion/)). A car built in 02 or 03/2003 needs the label and a look at the plugs.

**A 325xi:** never assume. ETK lists the 325xi Touring with MS43 and no end date, yet with the same "from Mar '03" engine harness and secondary-air sensor as the 325i ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/browse/engine_electrical_system/programmed_dme_control_unit/), [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325xi-M54/browse/engine_electrical_system/engine_wiring_harness_engine_module/)). Read the label.

**An M54 or an M56?** The M56 SULEV engine also runs an MS45.1, with a CAN-controlled pump module and a returnless metal tank, and this manual doesn't cover it. Two readings of ETK disagree about its gearbox. The US 325i M56 Touring's pages list a five-speed gearbox and a manual clutch-switch module ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/L-N/browse/manual_transmission/manual_transmission_s5d_g/)). But those sit in groups shared with other engines, and the only gearbox-module harness ETK lists for the M56 is "For vehicles with Automatic transmission" ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/engine_electrical_system/wiring_harness_engine_trans_module/)), matching BMW's bulletin that introduced the M56 with automatics ([BMW B11 75 02](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%202%29/08_SULEV.pdf)). So a manual M56 is probably a conversion. Either way, check the engine code; a manual gearbox doesn't prove an M54.

![Which DME your Touring has](diagrams/16-flow-which-dme.svg)

*Figure 1. How to tell an MS43 Touring from an MS45.1, and which move table to use. Check the engine code first, then work down the tests from the most reliable until one gives an answer: its arrows lead left to the MS43 table or right to the MS45.1 table. A car built in 02 or 03/2003 needs the label and a look at the plugs, so confirm a label reading with tests 4 and 5.*

### The five DME plugs

All three DMEs use the same five-plug Siemens connector, but the pin assignments differ throughout ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf), [WDS](https://wds.psjr.org/en/e46/zinfo/E46_PA6000L.htm)). Four plugs come with the M3 harness; X60004 is your body harness's.

| Plug | Pins | Belongs to | MSS54 functions that matter here | Source |
|---|---|---|---|---|
| X60001 | 9 | M3 engine harness | 1 terminal 15 to the injector relay K6327; 2 and 9 throttle actuator; 4, 5 and 6 grounds; 7 battery positive; 8 supply from the E-box fuse carrier | [SP0000014290](https://wds.psjr.org/en/e46/svg/SP0000014290.svg) |
| X60002 | 24 | M3 engine harness | O2 sensors and heaters; 5 ground; 11 US pump-module signal (out through X6021 pin 1); 12 E-box fan; 20 clutch and gear-switch chain; 23 DME-relay coil | [SP0000014292](https://wds.psjr.org/en/e46/svg/SP0000014292.svg) |
| X60003 | 52 | M3 engine harness | 8 and 21 crankshaft sensor; 12 starter feedback in; 13 alternator (terminal 61) in; 26 oil-pressure switch; 39 oil level; 33–38 injectors; 19 tire-pressure reset from X6011 pin 8 (M3s with the MK20 only); 51 jet-pump valve; 52 crankcase-breather valve (from 09/2004) | [SP0000014294](https://wds.psjr.org/en/e46/svg/SP0000014294.svg), [SP0000022868](https://wds.psjr.org/en/e46/svg/SP0000022868.svg) |
| X60004 | 40 | Your body harness | The vehicle interface: next table | [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg) |
| X60005 | 9 | M3 engine harness | Coils: pins 1, 2, 3, 6, 7 and 9 drive cylinders 1, 2, 3, 5, 6 and 4; pin 5 ground | [SP0000014296](https://wds.psjr.org/en/e46/svg/SP0000014296.svg) |

The MS45 drives its coils from different pins (1, 4, 6, 7, 8, 9 for cylinders 5, 3, 1, 2, 4, 6), and so does the MS43. Never mix a coil harness and a DME from different families: one 330Ci owner damaged a DME by mixing MS43 and MS45 coil harnesses during an M54 swap ([e46fanatics](https://www.e46fanatics.com/threads/330ci-engine-swap-no-start-looking-for-help.1298699/)).

**Keep the donor's DME and harness together.** WDS splits the M3's drawings at three build dates: 09/2001 (the leak-test heater on X60004 pin 18), 03/2004 (the charge lamp over CAN, and X60004 pins 1 and 2 no longer drawn) and 09/2004 (a crankcase-breather valve on X60003 pin 52). It has no separate "MSS54HP" condition, so an HP donor wires like an MSS54 of the same build date ([SP0000020984](https://wds.psjr.org/en/e46/svg/SP0000020984.svg), [SP0000022868](https://wds.psjr.org/en/e46/svg/SP0000022868.svg)). If the donor was an SMG car, its harness has no gear-switch wire at X60002 pin 20; add one ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/2844-smg-to-6mt-conversion)).

### X60004 pin by pin

From WDS: the MS43 column is its manual-gearbox table from 09/2001 ([PA6000J](https://wds.psjr.org/en/e46/zinfo/E46_PA6000J.htm), [SP0000017224](https://wds.psjr.org/en/e46/svg/SP0000017224.svg)); the MSS54 column is the US M3 from 09/2001 to 03/2004 ([PA6000L](https://wds.psjr.org/en/e46/zinfo/E46_PA6000L.htm), [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg)). WDS has no single drawing for the MS45.1 M54 manual car, so its column combines the MS45 drawing ([SP0000018609](https://wds.psjr.org/en/e46/svg/SP0000018609.svg)) with WDS's M54 drawings for the pump relay, clutch and secondary-air sensor ([SP0000014336](https://wds.psjr.org/en/e46/svg/SP0000014336.svg), [SP0000016193](https://wds.psjr.org/en/e46/svg/SP0000016193.svg), [SP0000019608](https://wds.psjr.org/en/e46/svg/SP0000019608.svg)). Wire sizes are in mm².

**The same on all three DMEs; nothing moves:**

| Pin | Circuit (wire) |
|---|---|
| 3 | Secondary-air pump relay K6304 (0.35 BR/BL) |
| 4 | Electric fan (0.5 SW/GN) |
| 7, 8, 9, 12, 13, 14 | Accelerator pedal sensors (0.35: 7 BR/GN, 8 WS, 9 GE, 12 BR, 13 WS/GN, 14 GE/GN) |
| 17 | Engine-speed signal to OBD pin 9 (0.35 SW) |
| 22 | Road speed from the DSC unit (0.35 WS/GN) |
| 24 | Brake-light switch, first contact, through splice X181 (0.35 BL/RT) |
| 26 | Terminal 15 from F29, 5 A (0.5 GN/VI) |
| 27 | Cruise buttons: serial data from the steering wheel (0.35 BL/SW) |
| 29 | A/C compressor relay K19 (0.5 SW/BL) |
| 32 | Diagnosis line TXD II to OBD pin 7 (0.5 WS/VI) |
| 33 | EWS data line (0.35 SW/VI) |
| 36, 37 | CAN high, CAN low (0.5 GE/RT, GE/BR) |
| 38, 39 | Radiator-outlet temperature sensor (0.35 SW/GN, SW/GR) |
| 40 | Empty on all three |

**Pins that differ:**

| Pin | MS43 (325i, to 02/2003) | MS45.1 (325i, from 03/2003) | MSS54 (US M3) | In your Touring |
|---|---|---|---|---|
| 1 | Empty (charge lamp at body X6011 pin 4) | Empty (lamp over CAN) | Charge lamp out to cluster pin 2 (0.35 BL) | MS43: move from X6011 pin 4. MS45.1: add |
| 2 | Empty (start feedback at body X6011 pin 6) | Leak-test heater (0.75 SW/RT) | Start feedback (terminal 30h) out to splice X276: cluster pin 3 (0.35 SW/GN) | MS43: move from X6011 pin 6. MS45.1: heater to 18 |
| 5 | Empty | Secondary-air sensor ground (0.5 SW/GE) | Ground to point X1108 (0.35 BR/SW) | MS45.1: remove. Both: add the ground (recommended) |
| 6 | Empty | Empty | Terminal 50 in, from connector X18820 (0.35 SW/BL) | Leave empty |
| 10 | Pump relay K96 (0.35 SW/VI) | Same | Pump relay, Euro cars only; "not used" on US drawings | Keep ([Fuel-pump control](#fuel-pump-control)) |
| 11 | Empty (lamp at body X6011 pin 3) | Empty (lamp over CAN) | Oil-pressure lamp out to cluster pin 13 (0.35 BR/GN) | MS43: move from X6011 pin 3. MS45.1: add |
| 15 | Empty | Secondary-air sensor signal (0.5 SW/RT) | Sport button in (0.35 SW/RT/GE) | MS45.1: remove. Sport optional |
| 16 | Empty | Empty | Sport LED out (0.35 SW/GR/GE) | Sport optional |
| 18 | Exhaust flap (3.0-litre only; empty on a 325i) | Empty (flap on 3.0-litre cars) | Leak-test heater (0.75 SW/RT) | Heater goes here |
| 19 | Empty | E-box fan, if fitted (0.5 BR/OR) | Empty (M3 fan on X60002 pin 12) | MS45.1: remove if populated |
| 20 | Leak-test module pin 1; BMW's table says "valve" | Module pin 1; table says "pump" | Module pin 1; table says "valve" | No change on the drawings; [test](#dm-tl-leak-test-pump-test-before-you-swap) |
| 21 | Empty (oil level at body X6011 pin 5) | Empty (over CAN) | Oil level out to cluster pin 17 (0.5 WS/GN) | MS43: move from X6011 pin 5. MS45.1: add |
| 23 | Clutch module (0.35 BL/BR) | Same | Empty: the clutch reaches X60002 pin 20 through the gear switch | Move to body X6011 pin 7 |
| 25 | Empty | Empty (EAC sensor, M56 only) | Empty | — |
| 28 | Brake-light switch, test contact (0.35 BR/GR) | Same | Empty (leak-test pump on M3s built before 09/2001) | Move to 34 |
| 30 | Module pin 3; table says "pump" | Module pin 3; table says "valve" | Module pin 3; table says "pump" | No change on the drawings; test |
| 31, 35 | Empty | Empty (local CAN, M56 only) | Empty | — |
| 34 | Empty | Empty | Brake-light switch, test contact (0.35 BR/GR) | Takes the wire from 28 |

On most drawings pin 20 is 0.75 BR/BL and pin 30 is 0.5 SW/GN. The US MS43 drawing shows them the other way round ([SP0000017224](https://wds.psjr.org/en/e46/svg/SP0000017224.svg); BMW's MS43 function drawing [SP0000017277](https://wds.psjr.org/en/e46/svg/SP0000017277.svg) agrees with the others), and the one documented MS43 wagon had SW/GN on 20, so on an MS43 Touring expect either. Go by the cavity, not the color. WDS prints pin 26 GN/VI on the module drawings and GN/SW on the MS43 supply drawings.

### Connector views and cavity numbers

- **WDS never says which face it shows.** Its connector views draw the housing with cavity numbers, often only at the corners, but don't say whether you're looking at the wire side or the mating side ([WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX60004A.htm)). Go by the numbers moulded into the housing. BMW's training says to "observe cavity numbers on reverse side of socket housing" ([BMW ST051](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/03%20Breakout%20Boxes%20%26%20Connectors.pdf)), and one swapper found X60004's numbers on its underside ([Import Modify – S54 swap, transmission and wiring (2018), 13:57](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=837s)).
- **X60004 runs the opposite way to the other four.** WDS draws X60004 as two blocks of two rows of ten. Its rows run left to right, with pin 1 at the bottom left: 1–10 and 11–20 in the lower block, 21–30 and 31–40 in the upper. X60001, X60002, X60003 and X60005 number right to left, with pin 1 at the bottom right ([WDS X60004](https://wds.psjr.org/en/e46/zinfo/E46_SX60004A.htm), [X60001](https://wds.psjr.org/en/e46/zinfo/E46_SX60001A.htm), [X60002](https://wds.psjr.org/en/e46/zinfo/E46_SX60002A.htm), [X60003](https://wds.psjr.org/en/e46/zinfo/E46_SX60003A.htm)). Don't carry a habit from one plug to the other. The 40-pin housing is a "/B" part where the others are "/A", which may be why (unconfirmed).
- **X6011** (black, 8 cavities, "Engine plug I"): two rows of four, 1–4 in one row and 5–8 in the other, with 5 next to 1. WDS draws pin terminals on this plug where the DME plugs, X6053 and X6021 show sockets ([WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX6011A.htm)). The body half is black and the engine-harness half teal ([Tulay](https://tulayswirewerks.com/product/bmw-8-pin-teal-unsealed-plug-e46-engine-plug-i-x6011-engine-harness-connector-kit/)).
- **X6053** (natural, 8 round cavities): 4-3-2-1 over 8-7-6-5 ([WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX6053A.htm)). The MS45.1's X60531 is a different style: one owner found flat spade pins on a 07/2004 325i where a 10/2003 car had round pins ([e46fanatics](https://www.e46fanatics.com/threads/funky-x6053-connector-on-ebox.1268369/)).
- **X6021** (black, 4): 1-2-3-4 in one row ([WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX6021A.htm)).
- **Body-side plugs:** the cluster's X11175 (black, 26) has 1–13 in one row and 14–26 in the other; the switch center's X1869 (23) has 13 to 1 on top and 23 to 14 below, in uneven groups; the clutch module's X13635 and the brake switch's X78 (4 each) read 4-3-2-1; the leak-test module's plug (X17140 on the M3, X1714 on the MS43, X17141 on the MS45) has four staggered cavities, 3 and 1 over 4 and 2; the pump relay socket X10156 (9) reads 3-6-9 over 1-4-7, with an unnumbered middle row; the OBD socket X19527 (16) reads 8–1 over 16–9 ([WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX11175A.htm), [WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX1869A.htm), [WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX13635A.htm), [WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX17140A.htm), [WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX10156A.htm), [WDS](https://wds.psjr.org/en/e46/zinfo/E46_SX19527A.htm)).

### MS43 Touring: what to move

For a Touring built from 09/2001 to 02/2003, with an M3 donor built from 09/2001. Earlier cars are below the table. Work on the body side in the E-box, and in this order: the heater wire must leave X6011 pin 7 before the clutch wire goes in. Sizes are mm².

| # | Connector and cavity | Wire | From → to | Function | Source |
|---|---|---|---|---|---|
| 1 | Body X6011 pin 7 → X60004 pin 18 | 0.75 SW/RT | Leak-test module plug pin 2 → DME | Leak-test pump heater (US only) | [SP0000017260](https://wds.psjr.org/en/e46/svg/SP0000017260.svg), [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg) |
| 2 | X60004 pin 23 → body X6011 pin 7 | 0.35 BL/BR | Clutch module X13635 pin 2 → M3 engine harness (0.5 GR) → X6053 pin 5 → gear switch → 0.5 GR/BL → X60002 pin 20 | Clutch and gear-switch chain: cruise and idle control | [SP0000016193](https://wds.psjr.org/en/e46/svg/SP0000016193.svg), [SP0000016194](https://wds.psjr.org/en/e46/svg/SP0000016194.svg), [SP0000014314](https://wds.psjr.org/en/e46/svg/SP0000014314.svg) |
| 3 | Body X6011 pin 3 → X60004 pin 11 | 0.35 BR/GN | DME → cluster X11175 pin 13 (switch on X60003 pin 26) | Oil-pressure lamp | [SP0000017260](https://wds.psjr.org/en/e46/svg/SP0000017260.svg), [SP0000014396](https://wds.psjr.org/en/e46/svg/SP0000014396.svg), [SP0000007269](https://wds.psjr.org/en/e46/svg/SP0000007269.svg) |
| 4 | Body X6011 pin 4 → X60004 pin 1 | 0.35 BL | DME → cluster pin 2 (alternator on X60003 pin 13) | Charge lamp | [SP0000014363](https://wds.psjr.org/en/e46/svg/SP0000014363.svg), [SP0000014362](https://wds.psjr.org/en/e46/svg/SP0000014362.svg) |
| 5 | Body X6011 pin 5 → X60004 pin 21 | 0.5 WS/GN | DME → cluster pin 17 (sensor on X60003 pin 39) | Oil level | [SP0000014397](https://wds.psjr.org/en/e46/svg/SP0000014397.svg), [SP0000014426](https://wds.psjr.org/en/e46/svg/SP0000014426.svg) |
| 6 | Body X6011 pin 6 → X60004 pin 2 | 0.35 SW/GN | DME → splice X276: cluster pin 3 and the E-box fan plug (starter on X60003 pin 12) | Start feedback (terminal 30h) | [SP0000014365](https://wds.psjr.org/en/e46/svg/SP0000014365.svg), [SP0000014364](https://wds.psjr.org/en/e46/svg/SP0000014364.svg) |
| 7 | X60004 pin 28 → pin 34 | 0.35 BR/GR | Brake-light switch X78 pin 3, through splice X1179 → DME | Brake-light switch, test contact | [SP0000017224](https://wds.psjr.org/en/e46/svg/SP0000017224.svg), [SP0000014399](https://wds.psjr.org/en/e46/svg/SP0000014399.svg) |
| 8 | Add: X60004 pin 5 | New 0.35 BR/SW | X60004 pin 5 → ground point X1108, under the driver's-seat carpet | DME ground, as on every M3 (recommended) | [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg), [EX1108A](https://wds.psjr.org/en/e46/zinfo/E46_EX1108A.htm) |
| 9 | Add (optional): X60004 pins 15 and 16 | New 0.35 SW/RT/GE and SW/GR/GE | Switch center X1869 pin 17 → X60004 pin 15; X60004 pin 16 → X1869 pin 18 | Sport button and its LED | [SP0000014425](https://wds.psjr.org/en/e46/svg/SP0000014425.svg) |
| 10 | Clutch module | — | Replace 61319231129 with the M3's 61319122700 | The chain needs the M3 module's output | [Clutch switch, gear switch and cruise](#clutch-switch-gear-switch-and-cruise) |
| — | No change | — | X60004 pin 10 (pump relay); pins 20 and 30 (leak-test pump; [test](#dm-tl-leak-test-pump-test-before-you-swap)); X6011 pins 1 and 2; X6021 pins 2, 3 and 4 | — | [SP0000014336](https://wds.psjr.org/en/e46/svg/SP0000014336.svg), [SP0000007729](https://wds.psjr.org/en/e46/svg/SP0000007729.svg) |
| — | Leave empty | — | X60004 pin 6 (an M3 terminal-50 input whose use isn't shown); X6011 pin 8 (tire-pressure reset on MK20-era M3s); X6021 pin 1 (the US pump-module signal) | — | [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/243029-e46-m3-tpms-x60003-to-x6011-question) |

X6011 and X60004 take different terminals, so every wire that moves between them gets a new terminal of the target's type: re-terminate it, or use a BMW repair lead ([Tulay](https://tulayswirewerks.com/product/bmw-e46-ms42-to-ms43-cluster-indicator-plug-and-play-adapter/), [Terminals, tools and repair leads](#terminals-tools-and-repair-leads)).

**Where other sources differ:**

- **Start feedback goes to pin 2, not 6.** A forum mapping sends X6011 pin 6 to X60004 pin 6. WDS shows X6011 pin 6 as the 30h start feedback, whose M3 home is pin 2, and the M3's pin 6 as a separate terminal-50 input ([SP0000017260](https://wds.psjr.org/en/e46/svg/SP0000017260.svg), [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg), [e46fanatics](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)). One builder started his car without it; move it anyway, since the wire is already there.
- **The brake test-contact wire is BR/GR** (brown with gray) in WDS. Kassel's chart and the workbook print BR/GN, probably reading GR as green ([Kassel](https://www.kasselperformance.com/wp-content/uploads/2016/01/E46S54Wiring.png)).
- **The oil-pressure lamp is cluster pin 13.** Kassel's chart says pin 14, which is the K-bus; WDS, BMW's ISTA as a swap shop quoted it, and Trent's working 330i all use 13 ([SP0000018656](https://wds.psjr.org/en/e46/svg/SP0000018656.svg), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off), [NAM3](https://nam3forum.com/forums/forum/main-forum/member-build-journals/173296-trent-s-s54-rebuild-and-sedan-swap/page4)).
- **Kassel's MS43 column** lists only the brake move and the oil-pressure, oil-level and Sport additions; it leaves out the charge lamp, the start feedback, the heater and the clutch. Trent: "Some of the Kassel directions work and some do not" (same thread).
- **The heater wire left in X6011 pin 7** meets the M3's clutch wire. An MS43 S54 wagon had leak-test faults for about two years for that reason; with the heater on 18 (SW/GN on 20 and BR/BL on 30 in his harness) it passed California's referee in 10/2023 ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/102198-requesting-help-with-dmtl-pinout)).
- **One 2001 325iT owner joined the M3's oil-pressure wire to the cluster wire** at X6011 instead of moving it ([e46fanatics](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)). The lamp works that way, but it's a splice; the move keeps BMW's route.

**Earlier MS43 Tourings:**

- **Built before 09/2001:** the leak-test module has three wires and no heater, so X6011 pin 7 is empty; the clutch wire goes in with a new terminal ([SP0000014355](https://wds.psjr.org/en/e46/svg/SP0000014355.svg)). An MSS54 from 09/2001 expects the heated four-wire module, so fit 16137193479 with a four-wire lead (a 2001 325iT owner took one from a junkyard car) and add a 0.75 mm² heater wire from X60004 pin 18 to module pin 2. The four-wire module takes X60004 pin 20 on its pin 1, pin 30 on its pin 3 and the F3 supply on pin 4 ([SP0000017277](https://wds.psjr.org/en/e46/svg/SP0000017277.svg), [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/), [e46fanatics](https://www.e46fanatics.com/threads/2001-325i-wagon-in-steel-grey-now-with-s54-swap.1127936/page-9), unverified). Then prove pump and valve with the [test](#dm-tl-leak-test-pump-test-before-you-swap).
- **A donor built before 09/2001** has an older DME layout: a three-wire leak-test module on X60004 pins 28 and 30, no heater output, and WDS names that conflict ([PA6000G](https://wds.psjr.org/en/e46/zinfo/E46_PA6000G.htm), [SP0000014423](https://wds.psjr.org/en/e46/svg/SP0000014423.svg)). Prefer a donor built from 09/2001.
- **Built before 03/2001:** a clutch switch (S32) instead of the clutch module ([SP0000014357](https://wds.psjr.org/en/e46/svg/SP0000014357.svg)). Check its plug and wiring against the M3 module's in WDS before you buy.

![MS43 pin map: X60004 and body X6011](diagrams/17-pinmap-ms43.svg)

*Figure 2. X60004 and the body side of X6011 on an MS43 Touring, with every cavity that changes and its move number from the table above; five wires cross into X60004, and the clutch wire goes into X6011 pin 7 once the heater wire is out. Layout as WDS draws it. WDS doesn't say which face that is, so your plug may look mirrored: find each cavity by the number moulded on the housing, never by counting positions in this drawing.*

### MS45.1 Touring: what to move

For a Touring built from 03/2003 with the M54 and a manual gearbox, with an M3 donor built from 09/2001. Pins 5, 15 and 19 (if fitted) come out first; the heater leaves pin 2 before anything else goes in. Sizes are mm².

| # | Connector and cavity | Wire | From → to | Function | Source |
|---|---|---|---|---|---|
| 1 | X60004 pin 2 → pin 18 | 0.75 SW/RT | Leak-test module plug X17141 pin 2 → DME | Leak-test pump heater (US only) | [SP0000018609](https://wds.psjr.org/en/e46/svg/SP0000018609.svg), [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg) |
| 2 | X60004 pin 5: out; insulate and tie back | 0.5 SW/GE | Secondary-air air-mass sensor, plug X6206 pin 1 | Sensor ground. On the MSS54, pin 5 is a ground | [SP0000018609](https://wds.psjr.org/en/e46/svg/SP0000018609.svg), [SP0000019608](https://wds.psjr.org/en/e46/svg/SP0000019608.svg) |
| 3 | X60004 pin 15: out; insulate | 0.5 SW/RT | Same sensor, X6206 pin 3 | Sensor signal. On the MSS54, pin 15 is the Sport input | Same |
| 4 | X60004 pin 19: out if populated; insulate | 0.5 BR/OR | E-box fan plug X6506 pin 1 | E-box fan. The M3 harness drives its own fan | [SP0000017918](https://wds.psjr.org/en/e46/svg/SP0000017918.svg) |
| 5 | X60004 pin 28 → pin 34 | 0.35 BR/GR | Brake-light switch X78 pin 3, through splice X1179 → DME | Brake-light switch, test contact | [SP0000018609](https://wds.psjr.org/en/e46/svg/SP0000018609.svg), [SP0000014399](https://wds.psjr.org/en/e46/svg/SP0000014399.svg) |
| 6 | X60004 pin 23 → body X6011 pin 7, with a new X6011-type terminal (body X6011 pin 7 is empty on this car) | 0.35 BL/BR | Clutch module X13635 pin 2 → M3 engine harness → gear switch → X60002 pin 20 | Clutch and gear-switch chain | [SP0000016193](https://wds.psjr.org/en/e46/svg/SP0000016193.svg), [SP0000018632](https://wds.psjr.org/en/e46/svg/SP0000018632.svg), [SP0000016194](https://wds.psjr.org/en/e46/svg/SP0000016194.svg) |
| 7 | Add: X60004 pin 11 → cluster X11175 pin 13 | New 0.35 BR/GN | DME → cluster | Oil-pressure lamp; code `CAN_OELDRUCKSCHALTER` = `nicht_aktiv` | [SP0000007269](https://wds.psjr.org/en/e46/svg/SP0000007269.svg), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off) |
| 8 | Add: X60004 pin 1 → cluster pin 2 | New 0.35 BL | DME → cluster | Charge lamp; code `GENERATOR_UEBER_CAN` = `nicht_aktiv` | [SP0000014362](https://wds.psjr.org/en/e46/svg/SP0000014362.svg) |
| 9 | Add: X60004 pin 21 → cluster pin 17 | New 0.5 WS/GN | DME → cluster | Oil level; code `TOG_UEBER_CAN` = `nicht_aktiv` | [SP0000014426](https://wds.psjr.org/en/e46/svg/SP0000014426.svg) |
| 10 | Only if your body X6011 pin 6 holds a wire: X6011 pin 6 → X60004 pin 2 (after move 1) | 0.35 SW/GN | DME → splice X276: cluster pin 3 | Start feedback (terminal 30h) | [SP0000014365](https://wds.psjr.org/en/e46/svg/SP0000014365.svg) against [SP0000018632](https://wds.psjr.org/en/e46/svg/SP0000018632.svg) |
| 11 | Add: X60004 pin 5 (after move 2) | New 0.35 BR/SW | X60004 pin 5 → ground point X1108, under the driver's-seat carpet | DME ground, as on every M3 (recommended) | [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg), [EX1108A](https://wds.psjr.org/en/e46/zinfo/E46_EX1108A.htm) |
| 12 | Add (optional): X60004 pins 15 and 16 (after move 3) | New 0.35 SW/RT/GE and SW/GR/GE | Switch center X1869 pin 17 → X60004 pin 15; X60004 pin 16 → X1869 pin 18 | Sport button and its LED | [SP0000014425](https://wds.psjr.org/en/e46/svg/SP0000014425.svg) |
| 13 | Clutch module | — | Replace 61319231129 with the M3's 61319122700 | The chain needs the M3 module's output | [Clutch switch, gear switch and cruise](#clutch-switch-gear-switch-and-cruise) |
| — | No change | — | X60004 pin 10 (pump relay); pins 20 and 30 (leak-test pump; [test](#dm-tl-leak-test-pump-test-before-you-swap) before you swap anything); X6011 pins 1 and 2; X6021 pins 2, 3 and 4 | — | [SP0000014336](https://wds.psjr.org/en/e46/svg/SP0000014336.svg) |
| — | Check empty before you use it | — | X60004 pin 18 (an exhaust-flap wire exists on 3.0-litre cars only) | — | [PA6000P](https://wds.psjr.org/en/e46/zinfo/E46_PA6000P.htm) |
| — | Leave empty | — | X60004 pin 6; X6011 pin 8; X6021 pin 1 | — | As the MS43 table |

> [!IMPORTANT]
> Pins 2 and 15 are both SW/RT (black with red). Tag them before you pull them: the 0.75 mm² wire in pin 2 moves to pin 18, and the 0.5 mm² wire in pin 15 comes out.

**Notes:**

- **Pins 5 and 15.** Nobody has photographed a 325i Touring's X60004, but ETK lists the secondary-air air-mass sensor for it from 03/2003, and the one documented MS45.1 swap with a pin list (smee123's 2004 ZHP) removed 5, 15 and 19 and moved 28 → 34 and 2 → 18, exactly Kassel's MS45 column ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/emission_control_air_pump_2/), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/201716-switched-12v-question)). Left in place, the sensor's ground side would sit on the MSS54's ground pin and its signal on the Sport input.
- **Pin 19.** ETK fits the E-box blower only to automatic, SMG and hot-climate cars, so a manual US Touring probably has nothing there ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/browse/engine_electrical_system/control_unit_box/)). Feed the fan from one harness only ([E-box plugs](#e-box-plugs)).
- **The lamps.** The MS45.1 reads the oil-pressure switch, alternator and oil-level sensor itself and sends the lamps to the cluster over CAN, so the Touring's cluster plug may have nothing in pins 2, 13 and 17 ([SP0000018655](https://wds.psjr.org/en/e46/svg/SP0000018655.svg)). An MSS54HP doesn't light the oil-pressure lamp over CAN even with the cluster coded for it: nextelbuddy's MS45.1 ZHP needed the pin-11 wire, and his cluster's pin 13 was empty ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)). Wire all three and code all three switches to `nicht_aktiv` ([Cluster wiring](#cluster-wiring)): then the lamps don't depend on which MSS54 software you run. With stock MSS54HP software you can leave the charge lamp and oil level on CAN instead.
- **Pin 6 of X6011.** WDS disagrees with itself: one drawing routes an MS45 car's start feedback through X6011 pin 6, another shows that X6011 with pins 1 and 2 only. Look at your plug; move 10 covers both cases.
- **Kassel's MS45 column** adds nothing ("ADD N/A"), so it misses the clutch, the lamps and the leak-test question. That may hold only with Kassel's own DME and cluster programming ([Kassel](https://www.kasselperformance.com/wp-content/uploads/2016/01/E46S54Wiring.png)). An ex-automatic MS45.1 330i wired to the chart alone had no cruise ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-cruise-control-not-working.1316868/), unverified).

![MS45.1 pin map: X60004 and body X6011](diagrams/18-pinmap-ms45.svg)

*Figure 3. X60004 and body X6011 on an MS45.1 Touring, laid out like the MS43 map: tag pins 2 and 15 (both SW/RT), take the wires out of 5 and 15 (and 19, if fitted) first, and move the heater from 2 to 18 before anything else goes in; the clutch wire needs a new terminal in X6011 pin 7, and the lamp wires to the cluster are new. Layout as WDS draws it. WDS doesn't say which face that is, so your plug may look mirrored: find each cavity by the number moulded on the housing, never by counting positions in this drawing.*

### DM-TL leak-test pump: test before you swap

The US leak-test pump (DM-TL) is the same part on both cars: 16136756440 to 09/2001, then the heated 16137193479 ([ETK: Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/), [ETK: M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/)). The heated module has four pins: 1 and 3 are the pump and the valve, 2 is the heater, and 4 is the +12 V supply (0.75 RT/WS, F3 20 A, through X6021 pin 2) ([SP0000017659](https://wds.psjr.org/en/e46/svg/SP0000017659.svg)).

**Every heated-module drawing, MS43, MS45 and MSS54, wires X60004 pin 20 to module pin 1 and pin 30 to module pin 3** ([SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg), [SP0000017277](https://wds.psjr.org/en/e46/svg/SP0000017277.svg), [SP0000017914](https://wds.psjr.org/en/e46/svg/SP0000017914.svg)). Only the labels disagree: the MSS54 and MS43 tables call pin 20 the valve and pin 30 the pump, while the MS45 tables say the reverse. On the drawings, neither Touring needs a 20/30 swap. Forum advice to swap 20 and 30 on MS45.1 cars follows the labels, and one builder who swapped still had P2418, "switching valve control circuit open" ([e46fanatics](https://www.e46fanatics.com/threads/e46-m3-sport-button-retrofit-on-non-m.1286041/)). Treat the swap as unproven, and settle it on your car:

1. **Before your Touring's DME comes out,** run its leak-test jobs in Tool32 and note which X60004 wire switches (a test lamp or meter at the back of the plug) and which job makes the pump run. MS45.1 (`MS450DS0.PRG`): `STEUERN_DMTL_P`, `STEUERN_DMTL_V` and `STEUERN_DMTL_H`, each with its `_ENDE` job, and `STATUS_DMTL_P`, `_V`, `_H`. MS43 (`MS430DS0.PRG`): `STEUERN_DMTL_MOTOR`, `STEUERN_DMTL_VENTIL`, `STEUERN_DMTL_HEIZUNG`. Tag each wire with its function ([MS450DS0](https://raw.githubusercontent.com/emdzej/ediabasx-docs-sgbd/main/docs/sgbd/MS450DS0.md), [MS430DS0](https://raw.githubusercontent.com/emdzej/ediabasx-docs-sgbd/main/docs/sgbd/MS430DS0.md)).
2. **Measure the triangle** from X60004 with the DME unplugged ([step 9 of the checks](#checks-before-first-power-up)): the lowest element is the pump.
3. **If still unsure, bench-check the module:** unplug it, feed +12 V through a fused lead to pin 4 (pin 3 on a three-wire unit) and briefly ground pin 1, then pin 3. The pump runs on one and the valve clicks on the other (our inference from the drawings).
4. **The MSS54 wants the pump on pin 30 and the valve on pin 20** (its table, and WDS's signal names DMTLP and DMTL). Pump on 30: change nothing. Pump on 20: swap 20 and 30.
5. **After the swap,** the MSS54 has no separate pump or valve job. `STEUERN_DMTL_HEIZUNG` switches the heater; run `START_SYSTEMCHECK_DMTL`, then `LESEN_SYSTEMCHECK_DMTL`, and read the faults: 14 (0x0E) heater, 27 (0x1B) valve, 127 (0x7F) module ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).

The one unresolved case: Trent's MS43 330i still logged "Heating DMTL module", 14 (0x0E), and "Module, tank-leak diagnosis", 127 (0x7F), after the heater move, with pump current over 50 mA against about 24 mA, and a new pump on order in June 2026 ([NAM3](https://nam3forum.com/forums/forum/main-forum/member-build-journals/173296-trent-s-s54-rebuild-and-sedan-swap/page4)).

![Leak-test module circuit and test](diagrams/19-circuit-dmtl.svg)

*Figure 4. The leak-test module with the M3 DME as BMW draws it, for a Touring and donor built from 09/2001: F3 feeds module pin 4, the heater wire moves into X60004 pin 18, and pins 20 and 30 run to module pins 1 and 3. The tables disagree about which of 20 and 30 is the pump, so run your Touring DME's own leak-test jobs before it comes out, then measure the triangle once the heater is in pin 18: pump on 30, change nothing; pump on 20, swap 20 and 30.*

### E-box plugs

The M3 harness's E-box branch meets your body harness at X6011 and X6021, and the B+ feed enters at X64101/X64102. X6053 and X6054 (X60531 and X60541 on an MS45.1) join the engine harness to the gearbox-module harness inside the M3 set, so use the M3's sections together and never mate an M3 half with a Touring half there. Compare every cavity on both halves before you join a plug, and log it ([worksheet](WORKSHEETS.md#e-box-plug-log)).

**X6011** (black, 8 pins, "Engine plug I") ([SP0000014314](https://wds.psjr.org/en/e46/svg/SP0000014314.svg), [SP0000017260](https://wds.psjr.org/en/e46/svg/SP0000017260.svg), [SP0000014318](https://wds.psjr.org/en/e46/svg/SP0000014318.svg), [SP0000018632](https://wds.psjr.org/en/e46/svg/SP0000018632.svg)):

| Pin | M3, body side | M3, engine side | MS43 Touring, body side | MS45.1 Touring, body side |
|---|---|---|---|---|
| 1 | Terminal 50 from EWS X1659 pin 1 (2.5 SW) | To the starter (2.5 SW) | Same | Same |
| 2 | Terminal 15 from F30, 7.5 A (0.75 GN/BR) | To the oil-level sensor and alternator regulator (1.0 GN/BR) | Same | Same |
| 3 | — | — | Oil-pressure lamp from cluster pin 13 (0.35 BR/GN) | — |
| 4 | — | — | Charge lamp from cluster pin 2 (0.35 BL) | — |
| 5 | — | — | Oil level from cluster pin 17 (0.5 WS/GN) | — |
| 6 | — | — | Start feedback from splice X276 (0.35 SW/GN) | — (one drawing shows it; check) |
| 7 | Clutch from module X13635 pin 2 (0.35 GR) | To X6053 pin 5 and the gear switch (0.5 GR) | Leak-test heater (0.75 SW/RT), from 09/2001; empty before | — |
| 8 | Tire-pressure reset from switch center X1869 pin 2 (0.5 GE/SW), MK20-era M3s only | To X60003 pin 19 | — | — |

After the moves, X6011 on either Touring carries only pins 1, 2 and 7 (the clutch wire). On an MK60 M3 (from 09/2002) the tire-pressure reset goes to the DSC unit and pin 8 is empty ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/243029-e46-m3-tpms-x60003-to-x6011-question)).

**X6021** (black, 4 pins) ([SP0000014315](https://wds.psjr.org/en/e46/svg/SP0000014315.svg), [SP0000007729](https://wds.psjr.org/en/e46/svg/SP0000007729.svg)):

| Pin | US M3 | Your Touring (manual) | Function |
|---|---|---|---|
| 1 | Pump-module signal from X60002 pin 11 (0.35 SW/VI) | Empty | The US M3's pump module; no mate in a 325i, so it stays unconnected |
| 2 | DME-relay power out, F3 (1.5 RT/WS) | Same, to splice X11212 | Feeds the pump relay's coil, the leak-test module and the A/C relay coil |
| 3 | Reverse-light switch output (1.0 BL/GE) | Same | Reverse lights |
| 4 | Reverse-light switch feed from F27, 10 A (1.0 GN/WS) | Same | Reverse lights |

Older forum posts describe a "3-pin plug" with the reverse-light wires and a heavy DME-relay feed that "nothing will work without" ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)). WDS shows no 3-pin E-box plug on these cars: the reverse-light wires and the DME-relay supply to the body share X6021, and the heavy battery feed to the DME relay comes in at X64101/X64102.

**X6053 / X60531** (natural, 8 pins; engine harness to gearbox-module harness) ([SP0000014316](https://wds.psjr.org/en/e46/svg/SP0000014316.svg), [SP0000014319](https://wds.psjr.org/en/e46/svg/SP0000014319.svg), [SP0000018630](https://wds.psjr.org/en/e46/svg/SP0000018630.svg)):

| Pin | M3 (X6053) | MS43 (X6053) | MS45.1 (X60531) |
|---|---|---|---|
| 1 | Injector supply from relay K6327 (2.5 RT/GE) | Terminal 15 to the automatic-gearbox unit | Same as MS43 |
| 2 | F2 supply (2.5 RT/WS/GE) | Same | Same |
| 3 | F3 supply (2.5 RT/WS) | Same | Same |
| 4 | Ground (1.5 BR) | Oil-level sensor ground (0.5 BR) | Same as MS43 |
| 5 | Clutch chain: X6011 pin 7 to the gear switch (0.5 GR) | — | — |
| 6 | Throttle actuator + from X60001 pin 2 (2.5 RT) | — | — |
| 7 | Throttle actuator − from X60001 pin 9 (2.5 WS) | Injector supply from K6327 (2.5 RT/GE) | Same as MS43 |
| 8 | — | — | — |

Mixed halves would put the M3's throttle-actuator lines on the Touring's injector feed. A 330i swap with mixed sections got injector "circuit low" faults on all six ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-fuel-injectors-low-circuit.1277127/)), and Tracks and Trails' ex-automatic Touring had spark but no fuel until the M3's gearbox section went in ([Tracks and Trails – Attempting to drive my E46 M3 Touring (2026), 1:14:00](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=4440s)).

**X6054 / X60541** (natural, 2 pins): 1 coil supply from F1 (30 A, 2.5 mm²); 2 ground from X60005 pin 5 (2.5 BR) ([SP0000014317](https://wds.psjr.org/en/e46/svg/SP0000014317.svg), [SP0000018631](https://wds.psjr.org/en/e46/svg/SP0000018631.svg)).

**X64101 / X64102** (the B+ feed): battery positive from the distributor (F102, 80 A) to DME X60001 pin 7 (1.5 RT) and to the DME relay K6300's terminal 30 (4.0 RT) ([SP0000014406](https://wds.psjr.org/en/e46/svg/SP0000014406.svg), [EX64101C](https://wds.psjr.org/en/e46/zinfo/E46_EX64101C.htm)).

**The E-box fan plug X6506.** The M3 harness's plug takes its control from X60002 pin 12 (0.5 BR/GE) on pin 1, the start feedback on pin 2 and the F3 supply on pin 3. An MS45.1 Touring's, where fitted, takes its control from X60004 pin 19 (0.5 BR/OR) on pin 1 and the F3 supply on pin 2 ([SP0000014366](https://wds.psjr.org/en/e46/svg/SP0000014366.svg), [SP0000017918](https://wds.psjr.org/en/e46/svg/SP0000017918.svg)). The pins differ, so feed the fan from one harness only. If your E-box has no blower, leave the M3 plug unplugged, as Tenza did ([Tenza Motorsports – 5 things they don't tell you, part 2 (2021), 02:05](https://www.youtube.com/watch?v=mDBiRn30fEs&t=125s)).

### Power, relays and fuses

The S54's DME power layout matches the 325i's ([SP0000014406](https://wds.psjr.org/en/e46/svg/SP0000014406.svg), [SP0000014676](https://wds.psjr.org/en/e46/svg/SP0000014676.svg), [SP0000017912](https://wds.psjr.org/en/e46/svg/SP0000017912.svg)):

- Battery positive reaches X60001 pin 7 and the DME relay K6300 (terminal 30, X6300 pin 6) through X64101/X64102.
- The DME switches the relay's coil (X6300 pin 4) from X60002 pin 23. The relay's output (X6300 pins 2 and 5, 4.0 RT/WS) feeds the E-box fuse carrier A8680: F1 30 A (coils, through X6054), F2 30 A (X60001 pin 8 and X6053 pin 2), F3 20 A (X6053 pin 3, and X6021 pin 2 to the pump relay's coil, the leak-test module and the A/C relay's coil) and F4 30 A (O2-sensor heaters and others). BMW's ST055 also lists an F5, 30 A ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)).
- Terminal 15 reaches X60004 pin 26 through F29 (5 A), and X60001 pin 1 feeds the injector relay K6327, whose output goes to the injectors through X6053 pin 1 on the M3 (pin 7 on the Touring).
- The DME holds its relay on for a few seconds after key-off (same source).

| Item | Part or rating | Notes | Source |
|---|---|---|---|
| DME relay K6300 | 61366915327, sky blue | Same on both cars | [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/relay_dme_mss54_k6300/) |
| Injector relay K6327 | 61368373700 | Same on both cars | [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/relay_for_injectors_k6327/) |
| Secondary-air relay K6304 | 12631742690 | Same on both cars | [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/secondary_air_injection_pump_relay_k6304/) |
| Fuel-pump relay K96 | 61368373700, white-green, in holder 61131389111 | Your Touring and the Euro M3; the US M3 uses module 61357892976 | [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_electrical_system/relay_for_fuel_pump_1_k96/) |
| A/C compressor relay K19 | 61368373700 | Same on both cars | [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/relay_for_a_c_compressor_k19/) |

**Glovebox fuses in these circuits**, from the WDS drawings: F9 5 A (terminal R: brake-light switch and clutch module); F10 5 A (cluster, terminal R); F12 (switch center, terminal R; rating not in our sources); F27 10 A (reverse-light switch); F29 5 A (DME, terminal 15); F30 7.5 A (X6011 pin 2: alternator and oil-level sensor; OBD pin 1); F33 5 A (switch center X521, terminal 15); F34 5 A (cluster, terminal 15); F37 50 A (electric fan); F42 30 A (switch center, terminal 30); F43 5 A (cluster, terminal 30; OBD pin 16); F54 15 A (pump power through K96); F62 7.5 A (the M3 heater valve's auxiliary pump; older drawings show F23); F63 7.5 A (A/C relay K19) ([SP0000014399](https://wds.psjr.org/en/e46/svg/SP0000014399.svg), [SP0000014336](https://wds.psjr.org/en/e46/svg/SP0000014336.svg), [SP0000015484](https://wds.psjr.org/en/e46/svg/SP0000015484.svg), [SP0000017567](https://wds.psjr.org/en/e46/svg/SP0000017567.svg), [SP0000011762](https://wds.psjr.org/en/e46/svg/SP0000011762.svg), [SP0000014297](https://wds.psjr.org/en/e46/svg/SP0000014297.svg), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/243243-depinning-center-control-switch)). Check your car's fuse card. Unused positions are usually wired on the power side only, so adding a fuse means adding a terminal on the load side ([e46fanatics](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)).

### Grounds

- The MSS54's grounds are X60001 pins 4, 5 and 6, X60002 pin 5, X60005 pin 5 and X60004 pin 5 ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)). All but X60004 pin 5 come with the M3 harness; keep their ground points intact.
- **Add a ground at X60004 pin 5.** Every M3 drawing in WDS has a real ground wire there: 0.35 mm² BR/SW to ground point X1108, under the driver's-seat carpet ([SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg), [EX1108A](https://wds.psjr.org/en/e46/zinfo/E46_EX1108A.htm)). The same point grounds OBD pin 5, so your Touring has it ([SP0000011831](https://wds.psjr.org/en/e46/svg/SP0000011831.svg)). No source shows what the DME uses this ground for, and the one builder who added one, while chasing a relay that stayed on (a worn ignition switch, it turned out), saw no change ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/201716-switched-12v-question/page2)). It costs one wire and matches BMW's wiring, so fit it. On an MS45.1, take the air-mass-sensor wire out of pin 5 first.
- The engine ground cable (12421737755, 380 mm) and the E-box are the same parts on both cars ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/ground_cable/), [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/engine_electrical_system/control_unit_box/)).

### Fans and CAN

- **Electric fan.** All three DMEs drive it from X60004 pin 4 (0.5 SW/GN) to the fan's power stage, plug X82 pin 2. The fan takes power from F37 (50 A, 6.0 RT/BL) on pin 4 and its ground on pin 1, and the DME reads the radiator-outlet sensor on pins 38 and 39 ([SP0000019629](https://wds.psjr.org/en/e46/svg/SP0000019629.svg)). Nothing moves. The fans differ (M3 64546988914, 325i 64546988913), but both cars list the same 3-pole connector parts, 61138380380 and 61138380385 ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/pusher_fan/), [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/pusher_fan/)).
- **E-box fan.** See the X6506 note under [E-box plugs](#e-box-plugs).
- **CAN.** All three DMEs use X60004 pins 36 and 37 (0.5 GE/RT, GE/BR), which join splices X1893 and X1894 to the cluster, the DSC unit and the steering-angle sensor ([SP0000015023](https://wds.psjr.org/en/e46/svg/SP0000015023.svg)). The bus wiring doesn't change. The network and its check are under [CAN, K-bus and the diagnosis socket](#can-k-bus-and-the-diagnosis-socket).

### Terminals, tools and repair leads

- **Housings** (ETK; the same numbers on both cars): 9-pin socket housing 12521744624 (cap 12527502456); 24-pole 12521744627 and 12521744628 (cap 12521744626); 52-pole 12521744633 and 12521744634 (cap 12521744632 to 07/2003, or 12527526424); 40-pole "/B" 12521744630 and 12521744631 (cap 12521744629) ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/basic_cotrol_unit_dme/)). We found no part numbers for the X6011 and X6021 housings; Tulay's Wire Werks sells kits for X6011, X6053 and X6021 ([Tulay](https://tulayswirewerks.com/product/bmw-8-pin-black-unsealed-receptacle-e46-engine-plug-i-x6011-chassis-harness-connector-kit/), [Tulay](https://tulayswirewerks.com/product/bmw-4-pin-black-unsealed-plug-e46-engine-plug-ii-x6021-transmission-harness-connector-kit/)).
- **Terminal families** in the Touring's catalog ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/contact_system_mlk/), [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/laminated_contacts_spring_contacts/)):

  | Family | Part numbers (wire size in mm²; Sn tin, Ag silver plating) |
  |---|---|
  | MLK 1.2 sockets | 12527510668 (0.25–0.5 Sn); 12527510670 (0.5–1.0 Sn, with grommet 12527503411); 12527510671 (0.25–0.5 Ag); 12527510672 (0.25–0.5 Sn); 12527510673 (0.5–1.0 Ag); 12527510674 (0.5–1.0 Sn); 12527502932 (0.25–0.5 Ag); 12527564537 (0.35 Ag); 12527532371 (0.25–0.5 Ag); 12527560453 and 12527560455 (0.5 Ag); 12527502929 discontinued |
  | Bushing contacts | 12520030685 (0.35); 12520143438 (0.25–0.5 Ag); 12520143439 (0.5–1.0 Ag) |
  | MLK 1.2 flat plug | 12527512135 (0.5 Ag) |
  | SLK 2.8 sockets with wire | 12520007168 (0.25–0.5); 12520007171 (0.5–1.0) |
  | SLK 2.8 ELA with wire | 12520007170 (0.2–0.5); 12520007172 (0.5–1.0 Sn); 12520143427 (0.2–0.5 Ag); 12520143433 (0.5–1.0 Ag); 12520143434 (2.5–4.0 Ag) |
  | Microtimer blade with wire | 12520007251 (0.5) |
  | MDK4 2.8 blades with wire | 12520007252 (1.0 Sn); 12520007253 (2.5 Sn); 12520007254 (0.5 Au); 12520007255 (1.0 Au) |

- **Which terminal goes where** isn't published: ETK doesn't say, and no source maps terminals to the X60004 or X6011 cavities. Pull one terminal from the cavity you'll use, match it to the family and wire size, and order that. Tulay's DME kit gives X60004 terminals for 0.22–0.35 mm² and 0.50–0.75 mm² wire ([Tulay](https://tulayswirewerks.com/product/siemens-ms42-ms43-ms45-mss54-dme-ecu-connector-kit/)). BMW pre-crimped repair leads save crimping.
- **Relay sockets** take double leaf-spring contacts sized by wire: 61130007437 (1.0 mm²), 61130007438 (2.5 mm²), 61130007271 (6.0 mm²) ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/browse/vehicle_electrical_system/relay_dme_mss54_k6300/)).
- **Release tools.** BMW's are 61 1 132, 61 1 134, 61 1 135, 61 1 136 and 61 1 137 for its plug families; the training document doesn't say which fits which E46 plug ([BMW ST051](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/03%20Breakout%20Boxes%20%26%20Connectors.pdf)). Turner lists 12- and 23-piece depinning sets ([Turner](https://www.turnermotorsport.com/c-1681-bmw-repair-kit), unverified).
- **Opening X60004.** Release its two end latches ([Import Modify – S54 swap, transmission and wiring (2018), 13:57](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=837s)).
- **Testing at the DME.** BMW's break-out box 90 88 6 121 300 sits between the DME and its plugs ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)). Back-probe pins work for the rest.
- **Ignition off** whenever you plug or unplug a DME module; BMW warns that arcing can damage the DME (same source).

## Body-side wiring

### Sport button and switch center

The Sport button switches the DME's throttle map; pressed, it grounds the DME's input ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)). M Track needs no wiring; it's MK60 coding ([Session 5](#session-5-dsc-coding-and-vin)).

**The two plugs on the M3's switch center (SZM),** from a newTIS page posted on NAM3 and the WDS drawings ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/243243-depinning-center-control-switch), [SP0000014425](https://wds.psjr.org/en/e46/svg/SP0000014425.svg), [SP0000015484](https://wds.psjr.org/en/e46/svg/SP0000015484.svg)):

| Pin | Function | Wire | Goes to | Needed in your Touring? |
|---|---|---|---|---|
| X1869 pin 7 | Terminal 30 | 4.0 RT/VI | Fuse F42, 30 A | **Yes**: without it the switch center logs "terminal 30 missing" |
| X1869 pin 22 | Terminal R | Not given | Fuse F12 | **Yes**: without it nothing on the panel works, the DSC button included |
| X1869 pin 23 | K-bus | 0.35 WS/RT/GE | Any K-bus point (the cluster's pin 14 wire is WS/RT/GE) | **Yes** |
| X1869 pin 17 | Sport signal; the button grounds it | 0.35 SW/RT/GE | DME X60004 pin 15 | **Yes, for Sport** |
| X1869 pin 18 | Sport LED, driven by the DME | 0.35 SW/GR/GE | DME X60004 pin 16 | **Yes, for the LED** |
| X1869 pin 2 | Tire-pressure reset button | 0.5 GE/SW | MK20-era M3: X6011 pin 8 to the DME. MK60 cars: DSC unit pin 40 | Optional |
| X1869 pins 1, 13, 20, 21 | Seat heating, right and left: buttons and temperature | — | Seat heaters | Only with seat heating |
| X1869 pins 14, 15, 19 | Sunshade up and down; HiFi (spatial sound) | — | Sunshade motor; amplifier | No |
| X521 pin 1 | Terminal 15 | 0.5 GN/BL/GE | Fuse F33, 5 A | Present with a DSC button |
| X521 pin 2 | DSC-off button | Blue/violet (TIS) | DSC unit, MK60 pin 39 | Present |
| X521 pin 3 | Panel lighting (58g) | 0.5 GR/RT | Light module | Present |
| X521 pin 4 | Ground | 0.75 BR, or 0.5 BR/SW (the two drawings differ) | Ground point | Present |

**A Touring with only a DSC button** has the 4-pin X521 plug and nothing for X1869 ([M346 Projects – E46 M3 SMG Touring build, part 2 (2023), 18:05](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=1085s)). George Hill: "Some Non-M's did not come with SZMs as such they just had a DSC button. That button can connect straight to the 4 pin connector at the SZM" (same NAM3 thread).

1. **Fit the M3's console switch unit:** 61316925520 on M3 coupes, 61316925521 on convertibles. Your 325i's is 61316925498 ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/switch_unit_center_console/)). Nobody has confirmed the fit in a Touring console.
2. **Plug the existing DSC-button plug into X521.**
3. **Make up an X1869 plug** with terminals in pins 7, 22, 23, 17 and 18, and run: pin 7 to F42; pin 22 to F12; pin 23 to the K-bus; pin 17 to X60004 pin 15; pin 18 to X60004 pin 16. On an MS45.1, clear X60004 pin 15 first. Check that F42 and F12 are wired on their load side; unused positions often aren't ([e46fanatics](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)). One owner's dead panel was a blown F12 (NAM3 thread above). One non-M swapper routed his wires under the dash and through the E-box fan opening in the firewall ([e46fanatics](https://www.e46fanatics.com/threads/e46-m3-sport-button-retrofit-on-non-m.1286041/)).
4. **Leave out** seat heating, the sunshade and HiFi unless you have them: that's why the HiFi button on Tenza's wagon lit but did nothing, and his panel worked reliably only once every feed had 12 V ([Tenza Motorsports – 5 things they don't tell you, part 2 (2021), 10:22](https://www.youtube.com/watch?v=mDBiRn30fEs&t=622s)).
5. **Test.** Tool32, `SZM46.PRG` → `STATUS_IO`: terminals R, 15 and 50 on and the terminal-30 voltage present ([SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/SZM46.md)). Then `MSS54DS0.PRG` → `STATUS_DIGITAL`: `STAT_FDYN_EIN` changes when you press the button, and the LED follows. Without the LED wire, expect fault 110 (0x6E), "LED Fahrdynamikschalter" ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).

The tire-pressure reset needs your DSC unit coded for the flat-tire warning and the M3 cluster for it; on Tenza's car it didn't work. If you don't want the switch center at all, a tuner can set Sport to stay on (NAM3 thread above). **Watch:** [Tenza Motorsports – 5 things they don't tell you, part 2 (2021), 08:45](https://www.youtube.com/watch?v=mDBiRn30fEs&t=525s).

![Sport button wiring](diagrams/20-circuit-sport.svg)

*Figure 5. The optional Sport button. Two new wires join the M3 switch center's new X1869 plug to X60004 pins 15 and 16, and the switch center also needs three feeds a base Touring lacks: terminal 30 from F42, terminal R from F12 and the K-bus; without terminal R nothing on the panel works, the DSC button included. On an MS45.1, the secondary-air sensor wire comes out of X60004 pin 15 on every swap, Sport or not.*

### Brake-light switch

Both cars use the same switch, 61316967601 ([ETK](https://bmwfans.info/parts-catalog/61316967601/)): switch S29 with a 4-pin plug, X78 ([SP0000014399](https://wds.psjr.org/en/e46/svg/SP0000014399.svg), [SP0000016222](https://wds.psjr.org/en/e46/svg/SP0000016222.svg)).

| Pin | Wire | Function | Goes to |
|---|---|---|---|
| 1 | 0.5 VI/GE | Terminal R | Fuse F9, 5 A |
| 2 | 0.35 BR/SW | Ground | Ground point X217 |
| 3 | 0.35 BR/GR | Second (test) contact | Splice X1179 → X60004 pin 28 (MS43, MS45.1). **Move to pin 34** for the MSS54 |
| 4 | 0.35 BL/RT | First contact | Splice X181 → X60004 pin 24 and the light module |

The DSC unit reads the switch too (MK60 pin 41) and checks it against its pressure sensors ([BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf)).

- **It's electronic.** BMW calls it "The Electronic brake light switch": it "provides a B+ signal when the brakes are applied", and the light module treats an interrupted idle signal as a faulty switch ([BMW ST052](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03c_E46%20Lighting%20Systems.pdf)). A meter proves the wire to pin 34; the DME proves the switch.
- **Test:** in `STATUS_DIGITAL`, `STAT_BLS_EIN` and `STAT_BLTS_EIN` both change with the pedal. If only one changes, the DME can't confirm braking: expect fault 106 (0x6A), "Bremslichtschalter", and no cruise ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).
- **Skip the move** and you get the yellow brake lamp: an S54 xi Touring cleared it by moving the wire from 28 to 34 ([e46fanatics](https://www.e46fanatics.com/threads/s54-xi-touring-swap.1102352/page-6), unverified).

### Clutch switch, gear switch and cruise

**The chain.** The MSS54 reads the clutch through a "power transmission switch": the clutch-switch module and the 420G's gear-recognition switch in series. It gives "a high signal for the MS S54 when the clutch is disengaged [pedal up] and the transmission is in gear", and the DME uses it to cut out cruise control and to enable its idle control ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)). Your Touring's MS43 or MS45.1 reads the clutch module directly on X60004 pin 23.

**The clutch module's plug, X13635** ([SP0000016193](https://wds.psjr.org/en/e46/svg/SP0000016193.svg), [SP0000016194](https://wds.psjr.org/en/e46/svg/SP0000016194.svg)):

| Pin | Wire | Your Touring | In the M3 (and after the swap) |
|---|---|---|---|
| 1 | 0.35 BR/SW | Ground, point X217 | Same |
| 2 | 0.35 BL/BR (Touring); 0.35 GR (M3) | Output to X60004 pin 23 | Output to body X6011 pin 7 → engine harness 0.5 GR → X6053 pin 5 → gear switch pin 1; gear switch pin 2 → 0.5 GR/BL → X60002 pin 20 |
| 3 | 0.5 VI/GE | Terminal R from F9, 5 A | Same |
| 4 | 0.35 BL/SW | To EWS X1659 pin 8: the clutch-start interlock on US and Japanese cars | Same: keep it |

So after the move, your Touring's BL/BR wire sits in body X6011 pin 7 and meets the M3 harness's gray wire, which runs through X6053 pin 5 to the gear switch. A BMW TIS diagram posted on NAM3 shows the same path ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/225235-clutch-switch-help-code-50)). The same poster's text names X6011 "pin 3"; his diagram says pin 7, and so does WDS.

**Fit the M3's clutch module, 61319122700.** It's required, not optional. The M3 module outputs +12 V with the pedal up; the non-M module (61319231129, your Touring's) switches between open and ground, which the chain can't use (terra, [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/225235-clutch-switch-help-code-50)). Two builds cured no cruise this way: George Hill's S54 ZHP, whose intermittent stalling also stopped, and ewcmr2's S54 wagon ([NAM3](https://nam3forum.com/forums/forum/main-forum/member-build-journals/3768-what-s-going-on-in-my-shop-currently/page3), [e46fanatics](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/)). BimmerWorld on 61319122700: "The switch must work to allow the car to start or to disengage from cruise control" ([BimmerWorld](https://www.bimmerworld.com/Driveline-Shifter/Clutch-Parts/Genuine-BMW-Module-Clutch-Switch-61319122700-E39-M5-E46-M3-E85.html)). The Euro-only 61319122701 works only with the EWS interlock coded out, which this guide doesn't do ([ETK](https://bmwfans.info/parts-catalog/61319122701/)). Take the donor's module, or buy one.

**The gear-recognition switch** (23142229113, on the 420G) is closed in gear and open in neutral ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/225235-clutch-switch-help-code-50), [ETK](https://bmwfans.info/parts-catalog/23142229113/)). Its state in reverse isn't documented.

**Cruise also needs:**

- the steering-wheel buttons' data line, X60004 pin 27 (0.35 BL/SW), unchanged: the right-hand buttons reach the DME on one serial wire through the clock spring ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf));
- both brake contacts (above);
- the road speed from the DSC unit over CAN, so a DSC unit with a VIN fault can stop cruise;
- manual-gearbox software in the DME ([ECUWorx](https://www.ecuworx.co.uk/how-to/a-run-down-of-features-of-the-mss5x-binary-modification-tool-and-what-they-do/)).

**Test with a gear engaged.** The DME's `STAT_KUP_EIN` and `STAT_KRAFTSCHLUSS_EIN` read the same input bit with opposite sense, so they can only follow the pedal when the chain's gear switch is closed ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)). Engine off, parking brake on, a gear engaged: pedal up gives `STAT_KRAFTSCHLUSS_EIN` = 1 and `STAT_KUP_EIN` = 0; pedal down gives 0 and 1. In neutral both stay at 0 and 1 whatever the pedal does. That's correct behavior, not a fault. A chain that never closes in gear points to the gear switch or the clutch module's output; one that is always closed points to a short at X60002 pin 20. Fault 80 (0x50), "Schalterkette Kraftschluss", is the chain.

**Meters and electronics.** The clutch module is a Hall-effect sensor, "providing a high signal when the clutch is depressed" to the EWS ([BMW ST051](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)). An ohmmeter proves its wires, not the module: check its supply and ground, then the status bits above and the EWS's clutch input ([Session 3](#session-3-ews)).

![Brake-light switch and clutch chain](diagrams/21-circuit-brake-clutch.svg)

*Figure 6. The brake-light switch and the clutch chain after the swap. Two wires move: the brake switch's test contact from X60004 pin 28 to pin 34, and the clutch module's output from X60004 pin 23 to body X6011 pin 7, where the M3 harness takes it through the gear switch to X60002 pin 20. The chain works only with the M3's clutch module, and both parts are electronic: a meter proves their wires, but only the status jobs prove the parts, run with the key on, the engine off and the parking brake on.*

### Cluster wiring

Both clusters use the same two plugs: X11175 (black, 26 pins) and X11176 (white, 18 pins) ([bmwgm5](https://www.bmwgm5.com/E46_IKE_Connections.htm), a hobby-site transcription; [SP0000017540](https://wds.psjr.org/en/e46/svg/SP0000017540.svg), [SP0000018656](https://wds.psjr.org/en/e46/svg/SP0000018656.svg)). The pins this swap touches, on X11175:

| Pin | Signal | Wire | From, in the swapped car |
|---|---|---|---|
| 1 | Ground | BR/SW | Ground point |
| 2 | Charge lamp | 0.35 BL | DME X60004 pin 1 |
| 3 | Start feedback (terminal 30h) | 0.35 SW/GN | DME X60004 pin 2, through splice X276 |
| 4 | Terminal 30 | RT/GE/WS | F43, 5 A |
| 5 | Terminal 15 | GN/BL | F34, 5 A |
| 6 | Terminal R | VI/GE | F10, 5 A |
| 7 | Backlight (58g), clusters built to 09/2002 only | GR/RT | Light module pin 47: needed when an older cluster goes into a car built from 09/2002 ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)) |
| 9, 10 | CAN high, CAN low | GE/RT, GE/BR | CAN splices |
| 11, 12 | Right tank sender + and − | — | Fuel pump unit |
| 13 | Oil-pressure lamp | 0.35 BR/GN | DME X60004 pin 11 |
| 14 | **K-bus**, not oil pressure | WS/RT/GE | K-bus |
| 15, 16 | Left tank sender + and − | — | Left sender |
| 17 | Oil level | 0.5 WS/GN | DME X60004 pin 21 |
| 19, 20, 21, 22, 23, 24, 26 | Road speed from the DSC; brake fluid; airbag lamp; ABS lamp; parking brake; pad-wear loop; coolant level | — | Unchanged |
| 25 | Diagnosis (D-bus) | WS/VI | OBD pin 8 |

**How the three lamps work with an MSS54.** The oil-pressure switch reads into the DME on X60003 pin 26, and the DME drives the lamp from X60004 pin 11; the switch is closed below about 0.5 bar, so the lamp is on at key-on and goes out once there's pressure ([SP0000007269](https://wds.psjr.org/en/e46/svg/SP0000007269.svg), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)). "The alternator light is powered through the cluster and grounded by the DME whenever the alternator is not charging" (George Hill, same thread). The oil-level sensor sends a pulse-width signal to X60003 pin 39, and the DME repeats it on X60004 pin 21 ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)). On an MS43 Touring these wires bypass the DME through X6011; on an MS45.1 the lamps arrive over CAN.

**Three coding switches in the cluster** choose wire or CAN for each lamp ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-cluster-coding.1330549/), unverified; [NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf)):

| Parameter | Lamp | Set to | Why |
|---|---|---|---|
| `CAN_OELDRUCKSCHALTER` | Oil pressure | `nicht_aktiv` on every car | An MSS54HP didn't light the lamp over CAN even with this `aktiv`; wired to pin 13, it works ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)) |
| `GENERATOR_UEBER_CAN` | Charge lamp | `nicht_aktiv` with pin 1 wired | `aktiv` works only with stock MSS54HP software; the CSL software didn't send it (same thread) |
| `TOG_UEBER_CAN` | Oil level | `nicht_aktiv` with pin 21 wired | `aktiv` only with an MSS54HP: the oil-level byte on CAN is HP-only ([MS4X](https://www.ms4x.net/index.php?title=Siemens_MS45_CAN_Bus_(CAN11h))) |

Wiring all three and coding all three to `nicht_aktiv` works whatever software the DME runs. One snippet says these switches exist on cluster indexes 07, 08, 23 and 24; check that yours has them when you read its coding ([Session 4](#session-4-cluster-and-light-module)).

**A donor built from 03/2004 needs one check.** WDS stops drawing X60004 pins 1 and 2 on M3s built from 03/2004 and shows their charge lamp over CAN ([The five DME plugs](#the-five-dme-plugs)). Nobody has documented whether those DMEs still drive pins 1 and 2. Wire them as the tables say, and if the charge lamp stays dark at key-on with `GENERATOR_UEBER_CAN` = `nicht_aktiv`, code it `aktiv`: a late car's stock MSS54HP software sends the lamp over CAN.

- **Engine speed, coolant temperature, consumption, the check-engine, cruise and overheat lamps, and the M3's oil-temperature gauge and warm-up lights** all arrive over CAN ([BMW ST034](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf), [BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf)). The warm-up and shift lights need DME software that supports them; stock M3 software does ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)).
- **Rear-door lights.** M3 clusters have none; solder in the LEDs or have a cluster service add them (same source).
- **Test** with Tool32, `KOMBI46R.PRG` → `STATUS_IO_LESEN`: `STAT_OELDRUCK_EIN` follows the switch (on at key-on, off running) ([SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46R.md)).

![Warning-lamp wiring](diagrams/22-circuit-lamps.svg)

*Figure 7. The three warning lamps and the start feedback after the swap: each sensor reads into the DME, and the DME drives the cluster from X60004 pins 11, 1, 21 and 2. On an MS43 you move these four wires over from body X6011 pins 3 to 6; on an MS45.1, which sent the lamps over CAN, you add the three lamp wires new and move the start feedback only if X6011 pin 6 holds a wire. Code all three cluster switches to `nicht_aktiv` (with a donor built from 03/2004, check the charge lamp as the text says), and use cluster pin 13 for the oil-pressure lamp: pin 14 is the K-bus.*

### Fuel gauge and tank senders

The cluster reads the two lever senders separately: the right one, in the pump unit, on X11175 pins 11 and 12, and the left one on pins 15 and 16. It converts them through a coded curve, `TANK_KENNLINIE` ([BMW ST034](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf), [NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf)).

- **The curve.** An M3 cluster offers `60_l_literskala`, `dad_tank_diesel` and `metalltank`. The M3 tank holds 63 L ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf)) and the 325i wagon's 16.6 gal (62.8 L) ([Autopadre](https://www.autopadre.com/vehicle-dimensions/bmw-325i/2004--11872), unverified), and both are plastic, so both should use `60_l_literskala`. A Touring that started as an M56 SULEV car with its metal tank would need `metalltank`. This is our reading of the coding list; nobody has reported an M3 cluster on Touring senders.
- **The senders differ by part number but share a plug** (61138352390): Touring left sender 16116768788 and pump unit 16146766942; M3 16142229683 and 16142229684 ([ETK: Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/), [ETK: M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/)). A hobby site gives about 70 Ω empty to 310 Ω full on the left and 70 to 395 Ω on the right ([bmwgm5](https://www.bmwgm5.com/E46_Fuel_Level.htm), unverified). With the M3 pump unit in your tank, the senders are mixed, so check each side.
- **Check** from near empty, adding measured amounts: Tool32 `KOMBI46R.PRG` → `STATUS_TANKINHALT_LESEN` gives litres for each sender and the total ([SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46R.md)). In the cluster's own test 06, phase 3 means "implausible" (BMW ST034). One side stuck: a sender, its plug pins or the coding.
- **Why it matters beyond the gauge.** The DME takes the tank level from the cluster over CAN, for the leak test's 15–85% window and its refueling check ([Readiness and inspection](#readiness-and-inspection)).

### CAN, K-bus and the diagnosis socket

**Powertrain CAN** (twisted pair: high GE/RT, low GE/BR) ([SP0000015023](https://wds.psjr.org/en/e46/svg/SP0000015023.svg), [BMW ST052](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03a_E46%20Power%20Supply%20and%20Bus%20Systems.pdf)):

| Node | CAN high / low | Notes |
|---|---|---|
| DME (MSS54) | X60004 pins 36 / 37 | |
| Cluster | X11175 pins 9 / 10 | The gateway between CAN, the K-bus and the diagnosis line (D-bus) |
| DSC unit (MK60) | Pins 11 / 15 | MK20: pins 17 / 16. Its yaw sensor has a separate CAN of its own |
| Steering-angle sensor | Pins 3 / 4 | |
| Automatic-gearbox unit | — | None on a manual. An ex-automatic Touring keeps the harness stub: leave it unplugged with nothing attached |

The DME's splices X1893 and X1894 join the nodes; WDS draws no terminating resistors. BMW: "A 120 Ohm resistor is installed in two control units… the effective resistance of the complete circuit is 60 Ohms… The terminal resistors are located in the ASC/DSC control unit and either the instrument cluster or in the DME", and modules without one read 10–50 kΩ across their CAN pins when unplugged ([BMW ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/9%20Bus%20System%20Troubleshooting.pdf)). Which of the cluster and DME carries the second resistor on an E46 isn't documented; a forum snippet says the cluster ([Beyond](https://forums.beyond.ca/threads/418337-E46-gauge-cluster), unverified). With the key on, each line sits at about 2.5 V to ground (2.35–2.65 V on a meter) (BMW ST040). The check is step 19 of the [checks before first power-up](#checks-before-first-power-up).

**K-bus** (one WS/RT/GE wire, about 12 V): the cluster (pin 14), light module, body module, climate control, airbag unit, EWS, switch center (X1869 pin 23), the steering wheel's audio buttons, park distance control and others ([BMW ST401b](https://archive.org/download/BMWTechnicalTrainingDocuments/ST401b%20Bus%20System%20Overview%20-%20All%20Models/02_3%20Series%20Bus%20Charts.pdf)).

**The diagnosis socket** (16 pins, driver's footwell, on E46s built from 06/2000) ([SP0000014297](https://wds.psjr.org/en/e46/svg/SP0000014297.svg), [BMW ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/1%202001%20Changes.pdf)):

| Pin | Signal |
|---|---|
| 7 | TXD II: the DME (X60004 pin 32) |
| 8 | TXD (D-bus): the cluster (X11175 pin 25), which gateways to the K-bus modules, the DSC unit and the steering-angle sensor |
| 16 | Battery positive (F43) |
| 1 | Terminal 15 (F30) |
| 4, 5 | Grounds (pin 5 to point X1108) |
| 9 | Engine speed (from X60004 pin 17) |
| 6, 14 | **No CAN**: an E46 socket has no terminals there |

That's why E46 cables bridge pins 7 and 8: BMW's own socket cap bridges both to battery positive when no tester is fitted ([BMW ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/1%202001%20Changes.pdf)).

**What travels over the network in this swap:** the A/C request, the crash signal and the tank level all cross the cluster's gateway, so an M3 cluster that isn't talking on both CAN and the K-bus costs you the A/C, the crash cut-off and the leak test (our reading of BMW's descriptions). The DME logs missing partners: 132 (0x84) DSC, 133 (0x85) steering-angle sensor, 134 (0x86) cluster, and 86 (0x56) for its own CAN ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).

![CAN network, K-bus and diagnosis socket](diagrams/23-can-network.svg)

*Figure 8. The CAN network after the swap: four modules on splices X1893 and X1894, with one 120 Ω terminator in the DSC unit and one in the cluster or the DME. Back-probe the DME or the cluster with the battery disconnected and expect about 60 Ω; the diagnosis socket has no CAN. The cluster is the gateway between CAN, the K-bus and the diagnosis line, so the A/C request, the crash signal and the tank level all pass through it.*

### Sensor leads that may not reach

| Sensor | Why it may not reach | What builders did |
|---|---|---|
| Coolant level (cluster pin 26) | The M3 expansion tank sits on the other side of the engine bay | Extended the lead over the radiator ([UNRIVALED – Watch this before you S54 swap (2021), 01:02](https://www.youtube.com/watch?v=eddLff8yba0&t=62s)), or re-routed the plug through the cabin rather than splicing ([Tracks and Trails – Attempting to drive my E46 M3 Touring (2026), 22:40](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=1360s)) |
| Washer pump and level sensor | The M3 washer tank sits low behind the bumper | Extended both plugs with soldered jumpers (same video, [23:00](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=1380s)); Tenza kept the non-M tank up top instead ([Tenza Motorsports – 5 things they don't tell you, part 1 (2021), 00:40](https://www.youtube.com/watch?v=-TXzg2Z8d7w&t=40s)) |
| Radiator-outlet temperature (X60004 pins 38 and 39) | The M3 radiator and hoses move it | Your 325i already reads this sensor, so check that its lead reaches the M3 radiator's. The one build that extended it was a Euro 318d diesel Touring ([M3projekts – E46 M3 Touring build, episode 6 (2023), 07:31](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=451s)) |
| Leak-test pump | Three wires on Tourings built before 09/2001, four from then | See [MS43 Touring: what to move](#ms43-touring-what-to-move) |
| Wheel-speed sensors | Depends on the donor's build date | See [Wheel-speed and pad-wear sensors](#wheel-speed-and-pad-wear-sensors) |

### Heater valve and auxiliary water pump

The US M3's heater valve carries a small electric pump: "Water valve with additional water pump" 64118369807. Your Touring has the plain "Water valve" 64118369805, the part the CSL and the X3 use too ([ETK: M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/water_hoses_water_valve/), [ETK: Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/water_hoses_water_valve/), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/14592-deleting-auxiliary-water-pump)). The pump isn't a DME circuit: it's fed from F62 (7.5 A, 0.5 RT/GR) and the climate control switches its ground side through pin 6 of its 6-pin plug X608 (0.5 BR/RT) ([SP0000017567](https://wds.psjr.org/en/e46/svg/SP0000017567.svg)). Older drawings show F23 instead of F62 ([SP0000011635](https://wds.psjr.org/en/e46/svg/SP0000011635.svg)). Two options:

1. **Fit the plain valve, 64118369805, on the S54.** No wiring and no coding change: your climate control is already coded for a valve without a pump. Owners running it on M3s report "No notable difference" (NAM3 thread above). Bleed the heater circuit carefully.
2. **Keep the M3 valve and its pump.** Run two wires: the pump's supply from F62 (check your fuse card) and its switched side to pin 6 of the climate control's X608 plug. Then code `ZUSATZWASSERPUMPE` = `aktiv` in the climate control and test with `STEUERN_ZUSATZWASSERPUMPE` (IHKR46 or IHKA46), watching `STAT_ZUSATZWASSERPUMPE_EIN` ([SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKR46.md), [NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf)). One builder whose pump wasn't wired found the cooling hard to bleed ([UNRIVALED – Watch this before you S54 swap (2021), 02:32](https://www.youtube.com/watch?v=eddLff8yba0&t=152s)); Tenza found two plugs on the S54's heater valve where his harness had one ([Tenza Motorsports – 5 things they don't tell you, part 1 (2021), 05:00](https://www.youtube.com/watch?v=-TXzg2Z8d7w&t=300s)).

### A/C with manual or automatic climate control

- **The chain.** Both climate controls send the A/C request, the compressor load and the fan request over the K-bus to the cluster, which passes them to the DME over CAN. The DME then grounds the compressor relay K19's coil from X60004 pin 29 (0.5 SW/BL) ([BMW ST040 IHKR](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/2%20e46%20ihkr.pdf), [BMW ST054](https://archive.org/download/BMWTechnicalTrainingDocuments/ST054%20Climate%20Control%20%28Archive%201%29/12%20IHKA%20E46.pdf)). K19 takes power from F63 (7.5 A) and feeds the compressor clutch; the refrigerant pressure sensor is read by the climate control, not the DME ([SP0000011761](https://wds.psjr.org/en/e46/svg/SP0000011761.svg), [SP0000011762](https://wds.psjr.org/en/e46/svg/SP0000011762.svg)). Nothing moves.
- **Manual climate control (IHKR).** BMW fitted IHKR as standard to the 325i Touring and the M3 from 09/2000, with the same K-bus and CAN messages as IHKA (BMW ST040 IHKR). A/C with the S54 is confirmed on IHKA cars; nobody has reported on IHKR first-hand, but by BMW's description it should work ([e46fanatics](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)). Test it early: in `STATUS_DIGITAL`, `STAT_AC_EIN` should follow the snowflake button and `STAT_KO_EIN` the compressor ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).
- **The cluster is in the path,** so no A/C often means the cluster isn't talking on both buses.
- **Fan.** The electric fan's speed rises with A/C pressure at low road speed; test it with `STEUERN_E_LUEFTER` (BMW ST054).
- If you keep your Touring's compressor, you need a different belt (Kalim, same post).

### Crash fuel cut-off

There's no wire from the airbag unit to the pump on an E46. The airbag unit (MRS III) sends a crash message on the K-bus, the cluster forwards it on CAN, and the DME switches the pump off ([BMW ST034](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/7%20Passive%20Safety%20Systems.pdf)). The MSS54 has the function: fault 126 (0x7E) is "EKP-Crash-Abschaltung", and BMW's S54 texts say the pump relay or module is switched off ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf), [BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)). Nobody documents whether US software, which drives the M3's pump module from X60002 pin 11, also drops the X60004 pin-10 relay output this build uses. Treat the cut-off as unverified with the relay.

**Bench check, without firing anything:** INPA reaches the airbag unit through the cluster, and its fault memory is clear; the DME's `FS_LESEN` shows no 134 (0x86), the cluster-message timeout; and `STEUERN_EKP_AUS` switches K96 off, which shows the DME can drop the relay. Never test the cut-off by deploying anything. If you want BMW's documented US arrangement back, fit the pump module ([Optional: the M3 pump module](#optional-the-m3-pump-module-ekp)). The battery safety terminal, which fires in a severe crash, cuts the main battery cable but leaves the front distribution live, so it doesn't stop the pump by itself ([BMW ST052](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03a_E46%20Power%20Supply%20and%20Bus%20Systems.pdf)).

### Wheel-speed and pad-wear sensors

| Car and build date | DSC unit | Wheel-speed sensors |
|---|---|---|
| US 325i Touring, from 09/2000 | Teves MK60 | Active (magnetoresistive), 12 V from the DSC unit, blue plugs |
| US M3 built before 09/2002 | Teves MK20 | Inductive, AC signal, gray plugs: they don't plug into your harness, and an MK60 isn't made to read them |
| US M3 built from 09/2002 | Teves MK60 | Active, blue plugs, as your Touring's |

Sources: [BMW ST056](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/04%2520E46%2520DSC%25201-27-03.pdf), [ETK: Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/brakes/hydro_unit_dsc_fastening_sensors_2/), [ETK: M3 MK60](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/hydro_unit_dsc_fastening_sensors/), [ETK: M3 MK20](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/hydro_unit_dsc_control_unit_fastening/).

- **Your own sensors should read the M3 hubs:** BMW says the MK60 "uses the same metal pulse wheels used with the MK20" (BMW ST056), and the current front (34526792896) and rear (34526752683) sensors are listed for both cars ([ETK](https://bmwfans.info/parts-catalog/34526792896/), [ETK](https://bmwfans.info/parts-catalog/34526752683/)). The rear sensor for a 325i is the short one (BMW ST056).
- **That explains the builds.** Tenza's 2004 Touring had a 2002 donor, an MK20 car, so the plugs didn't mate; his own sensors in the M3 hubs gave an ABS light that wasn't diagnosed ([Tenza Motorsports – 5 things they don't tell you, part 2 (2021), 03:15](https://www.youtube.com/watch?v=mDBiRn30fEs&t=195s)). A 2003 xi Touring took an M3's sensors ([e46fanatics](https://www.e46fanatics.com/threads/m3-touring-project.1240087/)). Never splice an MK20 donor's sensor pigtails onto your MK60 harness: they're the wrong kind of sensor.
- **Front sensors:** BMW says MK60 front sensors are three-wire, but an owner converting an M3 from MK20 to MK60 found the MK60 plugs expect two, with pin 3 an unneeded ground; the pins are otherwise the same ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap)).
- **Check** each wheel's speed in INPA's DSC status while rolling before you blame a sensor: a sensor not fully seated, the rear lead's length, and the DSC unit's VIN coding all show up there.
- **Pad-wear sensors** differ by part number (M3 front 34356751311, rear 34352229780; Touring 34351164371 and 34351164372) but feed one ground loop to cluster pin 24, and an open loop lights the lamp ([ETK](https://bmwfans.info/parts-catalog/34356751311/), [BMW ST052](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03b_E46%20Driver%20Information%20Systems.pdf)). Check plug shapes and lead lengths at both axles.

### Mirrors and headlights

- **Mirrors.** Facelift Touring doors use "ribbon cable" mirror motors, and M3 mirrors use the older connection. One builder fitted non-ribbon door harnesses from a junkyard sedan ([M346 Projects – E46 M3 SMG Touring build, part 21 (2024), 02:00](https://www.youtube.com/watch?v=a7HeYZ8Ctow&t=120s)).
- **Shared parts.** The US M3 came with halogen lamps as standard and xenon as option S522A, bi-xenon from 09/2001. Both cars' catalogs list the same headlight socket housings, xenon ballasts, levelling motor and front and rear levelling sensors (37146784696, 37146784697), and the same light-switch units: 61319133022 to 61319133025 without xenon, 61319133026 and 61319133027 with it ([ETK: M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/lighting/headlight/), [ETK: Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/lighting/headlight/), [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/switch_unit_light/)).
- **Halogen M3 lamps into a halogen Touring** should plug in with the coding unchanged. Confirm the pin functions at the headlight plug before the first light-up.
- **Xenon or bi-xenon into a halogen US Touring is a system job.** BMW fitted automatic levelling to every US xenon car, run by the light module ([BMW ST034](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf)). You need both levelling sensors with their links (the M3 front link 31122282404 on the M3 arm), their wiring to the light module, levelling motors fed through the headlight plugs, and for bi-xenon a light module of the 09/2001 redesign, which has the bi-xenon output ([BMW ST043](https://archive.org/download/BMWTechnicalTrainingDocuments/ST043%202002%20System%20Diagnosis/8%20E46%20Update.pdf)). The coding is [Session 9](#session-9-light-module-and-headlights). Prefer lamps without adaptive headlights (AHL), which need their own control unit.
- **Mileage safety.** The light module holds your car's true mileage. Never replace the cluster and the light module at the same time. If you need a xenon light module, fit it only after the M3 cluster carries your mileage, code your VIN into it and let it take the mileage from the cluster; never write a mileage into it ([BMW ST034](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf), [49 U.S.C. §32704](https://www.law.cornell.edu/uscode/text/49/32704)).

## Fuel-pump control

### How each car switches the pump

| Car | What switches the pump | Pins and wires | Source |
|---|---|---|---|
| Your 325i Touring, MS43 or MS45.1 (M54) | Relay K96 (61368373700, white-green, socket X10156), behind the glovebox | Pin 4: the DME grounds the coil from X60004 pin 10 (0.35 SW/VI). Pin 8: coil supply from F3 through X6021 pin 2 (1.5 RT/WS), live only while the DME relay is on. Pin 6: load supply from F54, 15 A (2.5 RT/VI). Pin 2: out to the pump (1.5 WS/BL) | [SP0000014336](https://wds.psjr.org/en/e46/svg/SP0000014336.svg), [ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_electrical_system/relay_for_fuel_pump_1_k96/) |
| Euro M3 | Relay K96, same socket and pins | X60004 pin 10 | [SP0000017524](https://wds.psjr.org/en/e46/svg/SP0000017524.svg) |
| US M3 | Pump module (EKP) 61357892976, which WDS still labels "K96 fuel pump relay 1", on its own plug X10157. It slows the pump at idle and part load | Pin 1: signal from X60002 pin 11 through X6021 pin 1 (0.35 SW/VI). Pin 8: F3 supply. Pin 6: F54. Pin 2: out to the pump (2.5 RT/WS). Pin 7: ground (2.5 BR) | [SP0000014408](https://wds.psjr.org/en/e46/svg/SP0000014408.svg), [BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf) |

WDS shows K96 on X60004 pin 10 on both Touring DMEs: the MS45.1 too, despite the workbook tab that lists pin 10 as unused, which is the M56 layout. On US M3 drawings X60004 pin 10 is "not used" (a Euro-only output); the US M3 drives its module from X60002 pin 11 instead ([PA6000L](https://wds.psjr.org/en/e46/zinfo/E46_PA6000L.htm)). Builders report that US software drives pin 10 anyway: swap shops and owners run K96 from it with a stored pump fault and no check-engine lamp ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-california-bar-certification.1307461/page-2), [e46fanatics](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38), [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)). WDS can't show that, so prove it on your car with the checks below. With the relay, the DME grounds K96's coil at key-on and keeps it grounded while it sees engine speed ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/3%20MS42%20MS43.pdf)).

### Recommended: keep the relay

No wiring changes:

1. DME X60004 pin 10 → your body harness → K96 socket pin 4 (SW/VI).
2. K96's contact → the pump, through F54 (15 A).
3. The M3 harness's pump-module wire (X60002 pin 11 → X6021 pin 1, SW/VI) → **connected to nothing.** On a manual 325i the body side of X6021 pin 1 is empty ([SP0000007729](https://wds.psjr.org/en/e46/svg/SP0000007729.svg)); keep it that way. Never put that PWM signal on K96.

Expect one stored fault: location 1 (0x01), "Relais Kraftstoffpumpe" (fuel-pump relay), because US software misses the pump module it expects. It shows in INPA, ISTA and PA-Soft, not on a generic scanner, and doesn't light the check-engine lamp ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-california-bar-certification.1307461/page-2), [SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)). INPA prints fault locations in decimal, so it shows as 1. Don't confuse it with 130 (0x82), the immobilizer fault.

### Checks on the pump circuit

These are steps 10, 28 and part of 22 of the [checks before first power-up](#checks-before-first-power-up).

1. **Pin 10 to the relay** (battery off, DME unplugged, K96 pulled): continuity from the X60004 pin-10 cavity (body side) to K96's socket pin 4, the SW/VI wire. Across the relay's coil, about 90 Ω (a generic value for this relay type, [TE](https://radiolocman.com/datasheet/data.html?di=108521)). If pin 10 goes elsewhere, find K96's coil wire in WDS for your car and bring it to pin 10.
2. **The PWM wire stays off the relay:** from the M3 harness's X6021 pin 1 to every K96 socket terminal: open. If any reads continuity, de-pin the M3 wire and insulate it.
3. **The relay command, without cranking** (DME plugged in, charger on, key at position 2):
   - Listen at K96 and at the tank at key-on: one prime.
   - Tool32 `MSS54DS0.PRG` → `STATUS_DIGITAL`: `STAT_EKP_EIN` reads 1 during the prime.
   - Run `STEUERN_EKP`: K96 clicks and the pump runs. Stop it with `STEUERN_EKP_AUS` ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)). A click proves that your software drives pin 10.
   - If the job returns OKAY but K96 stays silent, the job may drive only the module output on X60002 pin 11. Go by the prime and `STAT_EKP_EIN`. With K96 pulled, a test light across its socket's coil terminals should flash at key-on ([Motor Age](https://www.vehicleservicepros.com/industry-news/article/53089788/evap-monitor-on-european-cars-real-world-diagnosis-of-dmtl-systems-2017-08-04), the generic method).
   - In INPA the engine is under E46 → Engine → "MS S54 for S54 M3". INPA's "Fuel pump EKP" entry won't answer on this build, because there's no module ([bmwfaq](https://bmwfaq.org/threads/duda-con-el-inpa.796332/)).
4. **Pressure:** 5.0 ± 0.2 bar (72.5 ± 2.9 psi) at the prime, and less than 0.5 bar lost after switch-off: BMW's pass/fail ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)). BMW: "DO NOT OPERATE THE FUEL PUMP unless it is properly installed in the fuel tank and is submersed in the fuel" (same source). The full pressure and flow test belongs to the fuel system: see [Fuel system](README.md#fuel-system).

K96, K6327 and K19 are the same relay (61368373700), so swapping K96 with K19 is a quick relay test.

### Optional: the M3 pump module (EKP)

Fit it only if your state reads manufacturer fault codes and won't accept the stored fault, or you want the M3's slow-running pump and BMW's documented crash cut-off back ([Crash fuel cut-off](#crash-fuel-cut-off)). Nobody has documented one in a Touring.

The module takes five wires where K96 takes four: the signal from X60002 pin 11 (through X6021 pin 1, so your body side needs a terminal there and a new wire), F3 and F54 supplies, a 2.5 mm² feed to the pump and a 2.5 mm² ground ([SP0000014408](https://wds.psjr.org/en/e46/svg/SP0000014408.svg)). One owner measured the same layout on an '06 M3 ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/132772-help-fuel-pump-relay-ekp-engine-wiring-schematic)). Another owner's claim that a 2006 car uses pin 10 for the module contradicts both WDS and that measurement (same thread). Kalim suggests rewiring the socket behind the glovebox for the module's black socket ([e46fanatics](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-38)). Loose coil-pack grounds after valve work have killed EKP modules in stock M3s (NAM3 thread above). For BMW's pressure test, bridge terminals 30 and 87b of the module's socket ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%202%29.pdf)).

The other way to clear the fault is to have the DME vendor suppress it. Don't flash Euro software to lose it: that drops the US-only functions, including the leak test.

### Faults that look like pump faults

**The harmless stored fault and a real one carry the same number, location 1 (0x01).** Tell them apart by what the car does:

| What you see | It's | Do |
|---|---|---|
| Fault 1 stored; one prime at key-on (`STAT_EKP_EIN` = 1, K96 clicks); 5.0 bar; the engine starts and runs; `STAT_MIL_EIN` = 0 | The expected fault: US software misses its pump module | Nothing. Record it |
| Fault 1 stored; no prime, no pressure, K96 silent | A real pump-circuit fault | Checks 1–3 above; fuses F54 and F3; swap K96 with K19 |
| Cranks, won't start; fault 1 with all six injectors disabled | Usually not the pump: in the 2002 325iT case it followed an immobilizer problem | Read 130 (0x82) and 66 (0x42) and `STAT_EWS3_FREIGABE` first ([Session 3](#session-3-ews), [e46fanatics](https://www.e46fanatics.com/threads/ews-synch-for-s54-swap-into-e46-touring.1318881/)) |

- **Pump primes but the car won't start:** feed and return swapped at the filter-regulator caused one swap's no-start ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/82513-s54-swap-to-ms42-car-no-start)).
- **No prime at all:** in a swap into a 2000 323i wagon the M3 harness's E-box plugs had no mates in the older E-box. The owner fitted junkyard body-side plugs and used X60004 pin 10 ([e46fanatics](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-39)).
- **Starts only with the pump fuse pulled, then floods:** in an E36 S54 swap a ground terminal at X60003 pin 25 wasn't seated ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/112619-s54-only-starts-when-fuel-pump-fuse-is-pulled-did-i-code-it-wrong)). Different chassis, same lesson: tug-test every terminal you touch.

## Checks before first power-up

One procedure, in order, from the first ohm reading to the oil-priming crank. Log it on the [worksheet](WORKSHEETS.md#power-up-checks).

**What a meter can prove.** A meter proves wires, and the parts at the end of a wire only when they're plain loads: coils, relay coils, the leak-test module, temperature sensors, the gear switch. Three re-pinned circuits end at electronic parts instead. The clutch module is a Hall-effect sensor, high with the pedal down ([BMW ST051](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)); the brake-light switch is electronic and sends battery voltage when you brake ([BMW ST052](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03c_E46%20Lighting%20Systems.pdf)); and the S54's oil-level sensor sends a pulse-width signal ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)). For those, the meter checks the wiring and the DME's status jobs prove the part (steps 26 and 27).

**Which values are BMW's.** Pass values marked "BMW" come from BMW's training documents. The ones marked "generic" are typical figures for that kind of part: a guide, not a limit. Tool32 jobs are in `MSS54DS0.PRG` unless the step names another file ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).

![Checks before first power-up, steps 1–18](diagrams/24-flow-power-up.svg)

*Figure 9. The checks before first power-up with the DME unplugged: the E-box plug comparison, then steps 1–18. The gray labels give each stage's steps and how the battery and DME are set; go down only when the stage's question is answered yes, and on a no, stop and fix what the red box names or that step's "If it fails". The gray numbers on the right are step numbers, and values are marked BMW or generic, as in the tables below.*

### E-box plug comparison

Before you join the E-box plugs (Phase 11), list every cavity on both halves of X6011, X6021, X6053/X60531, X6054/X60541 and X64101/X64102: wire color and where it goes, against the tables in [E-box plugs](#e-box-plugs). Each pair should be the same circuit, or empty on one side. Anything else is a fault waiting to happen: injector "circuit low" codes ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-fuel-injectors-low-circuit.1277127/)) or a dead pump.

### Steps 1–14: battery disconnected, DME unplugged

All five DME plugs off, ignition off.

| Step | Check | Pass | If it fails |
|---|---|---|---|
| 1 | Tug-test every terminal you moved or added. Look into the emptied cavities: X60004 pins 23 and 28 on both cars; on an MS43 also X6011 pins 3–6; on an MS45.1 also X60004 pin 19, and pins 2, 5 and 15 unless they now carry the start feedback, the new ground and the Sport wire | Every terminal locked; every cavity as the move table says | Reseat or replace the terminal |
| 2 | Each moved or added wire to chassis ground (not the new pin-5 ground) | Open | A pinched or misrouted wire |
| 3 | Lamp wires: X60004 pin 11 to cluster X11175 pin 13; pin 1 to pin 2; pin 21 to pin 17; pin 2 to pin 3 (start feedback, if moved) | Continuity, under about 1 Ω (generic) | Wrong cavity; pin 14 instead of 13 |
| 4 | Oil-pressure switch: M3 harness X60003 pin 26 to engine ground, engine stopped | Near 0 Ω: the switch is closed without pressure | Switch plug, wire or switch |
| 5 | Brake test contact: X60004 pin 34 to the brake-switch plug X78 pin 3 | Continuity. The switch itself is proven in step 26 | The move, or the splice X1179 |
| 6 | Clutch chain: clutch-module plug X13635 pin 2 to body X6011 pin 7; through the engine harness to the gear switch's pin 1; gear switch pin 2 to X60002 pin 20; and across the gear switch | Continuous wires. Across the gear switch: near 0 Ω in gear, open in neutral. The module is proven in step 26 | The X6011 crossing, X6053 pin 5, the gear switch |
| 7 | Start interlock: X13635 pin 4 to EWS X1659 pin 8 | Continuity | The wire |
| 8 | Sport, if fitted: X1869 pin 17 to X60004 pin 15; pin 18 to pin 16; then pin 15 to ground with the switch unit in | Continuity; open with the button released, near 0 Ω pressed (BMW: it grounds the input) | Wiring, switch unit |
| 9 | Leak-test triangle, the module plugged in: X60004 pins 18–20, 18–30 and 20–30. Each element = (the two readings that include its pin, added, minus the third) ÷ 2 | A new Bosch module measured about 68, 52 and 44 Ω, solving to heater ≈ 38 Ω on 18, valve ≈ 30 Ω on 20 and pump ≈ 14 Ω on 30 (generic: an E93 unit). The lowest element is the pump; it belongs on 30 | Open on both pairs with 18: no heater (a three-wire module or a missing wire). Pump on 20: see the [leak-test pump](#dm-tl-leak-test-pump-test-before-you-swap). Identical readings or 0 Ω: a short |
| 10 | Pump trigger, K96 pulled: X60004 pin 10 to K96 socket pin 4 (SW/VI); the M3 harness's X6021 pin 1 to every K96 socket terminal; across K96's coil | Continuity; open to every terminal; about 90 Ω (generic) | Find K96's coil wire for your car; isolate the module wire; swap K96 with K19 |
| 11 | Coils: the coil supply (terminal 15 side) to X60005 pins 1, 2, 3, 9, 6 and 7 (cylinders 1–6) | About 0.8 Ω each, all alike (BMW: harness plus primary winding) | Coil or harness. Never a coil harness from another DME family |
| 12 | Injectors: the injector supply to X60003 pins 33–38 | Six equal readings (no BMW figure found) | Injector, plug, an X6053 mix |
| 13 | Temperature sensors: coolant X60003 pins 24 and 25; radiator outlet X60004 pins 38 and 39 | Near the NTC curve at the air temperature: about 2,500 Ω at 20 °C (generic Bosch NTC) | Open or short; compare again in step 24 |
| 14 | Crankshaft sensor: X60003 pins 8 and 21 | A steady coil reading (no BMW figure), open to ground | Sensor or wire |

### Steps 15–18: battery connected, DME still unplugged

| Step | Check | Pass | If it fails |
|---|---|---|---|
| 15 | Terminal 30 at X60001 pin 7 (harness side) | Battery voltage, key on or off | F102 (80 A), the plugs X64101/X64102 |
| 16 | Terminal 15 at X60004 pin 26, key at position 2 | Battery voltage, above 9 V (BMW's threshold); 0 V with the key off | F29, the ignition switch |
| 17 | DME relay supply: K6300 socket terminal 30 (X6300 pin 6, 4.0 RT) | Battery voltage, key on or off | X64101/X64102, the B+ feed |
| 18 | Grounds: X60001 pins 4, 5 and 6 to the battery's negative post | Near 0 Ω; under 0.1 V drop under load (generic) | Ground eyelets, the engine ground strap |

The DME relay and everything behind it (the E-box fuses, the pump relay's coil) stay dead until the DME is plugged in, because the DME switches the relay.

### CAN bus resistance

![Checks before first power-up, steps 19–33](diagrams/24-flow-power-up-2.svg)

*Figure 10. The checks with the DME plugged in, from the CAN bus reading to the oil-priming crank and the reset, then the first start. Go down only when the stage's question is answered yes; on a no, stop and fix what the red box names or that step's "If it fails". Sessions 3–5 come between the first key-on and the oil-priming crank.*

**Step 19.** Disconnect the battery again. Plug the DME in (ignition off), with every other module plugged in: cluster, DSC unit, steering-angle sensor. Back-probe X60004 pin 36 (CAN high) to pin 37 (CAN low) at the plugged-in DME, or X11175 pins 9 and 10 at the cluster. The E46's diagnosis socket has no CAN pins, so don't measure there ([SP0000014297](https://wds.psjr.org/en/e46/svg/SP0000014297.svg)).

| Reading | Means |
|---|---|
| About 60 Ω | Pass: both 120 Ω terminating resistors in place (BMW) |
| About 120 Ω | One terminating module is unplugged or cut off from the bus |
| About 40 Ω | A third terminator |
| 0 Ω | High and low shorted together |
| Open | Both terminators missing, or the wire to the probe point broken |

To find which modules terminate, unplug one at a time: the reading jumps to about 120 Ω when you unplug a terminating module and stays at 60 Ω for the others. An unplugged module without a resistor reads 10–50 kΩ across its own CAN pins ([BMW ST040](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/9%20Bus%20System%20Troubleshooting.pdf)). BMW puts the resistors in the DSC unit and in either the cluster or the DME, so a replaced cluster or DME can change the count. No swapper has reported a CAN wiring fault; the reported problems are coding ones ([e46fanatics](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/)).

### First key-on: what to expect

**Steps 20–29.** DME plugged in, battery connected, charger on, key at position 2, engine off. Plug and unplug the DME only with the ignition off.

| Step | Check | Pass | If it fails |
|---|---|---|---|
| 20 | Relay and comms | K6300 clicks at key-on and stays on a few seconds after key-off (BMW). INPA shows two black dots and reaches the DME (E46 → Engine → "MS S54 for S54 M3"), cluster, light module, EWS and DSC; Tool32 `IDENT` returns OKAY | Steps 15–18; the cable's pin 7/8 bridge |
| 21 | Supplies: `STATUS_UBATT`; `STATUS_UEXT1` and `STATUS_UEXT2` | `STATUS_UBATT` within a few tenths of a volt of the battery (generic). BMW: five seconds after key-on, with terminal 15 above 9 V, the DME sets a fault if its relay supply differs from terminal 15 by more than 3 V. Sensor supplies about 5 V (BMW) | Relay, fuse carrier, grounds; a shorted sensor supply: faults 58 (0x3A) and 59 (0x3B) |
| 22 | Fault memory: `FS_LESEN` | Only fault location 1 (0x01), "Relais Kraftstoffpumpe"; possibly 130 (0x82) after an EWS delete; and the DSC unit's VIN faults until Session 5 | Fix anything else before you crank |
| 23 | Lamps at key-on | Red oil-pressure lamp, charge lamp and check-engine lamp lit. The check-engine bulb check is also an inspection item | Steps 3 and 4; the cluster's three CAN switches ([Session 4](#session-4-cluster-and-light-module)); `STAT_MIL_EIN` shows whether the DME is asking for the check-engine lamp |
| 24 | Temperatures on a cold-soaked engine: `STATUS_MOTORTEMPERATUR`, `STATUS_OEL_TEMPERATUR`, `STATUS_AN_LUFTTEMPERATUR`, `STATUS_KUEHLW_AUSL_TEMPERATUR`, `STATUS_TUMG` | All within a few °C of each other and of the air | A reading pinned near −48 °C (the scale's zero): an open or shorted sensor circuit |
| 25 | Pedal and throttles: `STATUS_PWG_POTI_SPANNUNG`; `STATUS_DKP_WINKEL` against `STATUS_DKP_WINKEL_SOLL` | Pedal sensor 1 about 0.5 V released, rising to about 4.5 V; sensor 2 0.5 to 2.0 V (BMW). Throttle sensor 0.5 V closed to 4.5 V open, the actuator's feedback the reverse (BMW). The throttles follow the pedal; actual follows target | Pedal wiring (X60004 pins 7–14), throttle actuator, synchronization |
| 26 | Switch bits: `STATUS_DIGITAL` | **Clutch, with a gear engaged:** pedal up `STAT_KRAFTSCHLUSS_EIN` = 1 and `STAT_KUP_EIN` = 0; pedal down 0 and 1. In neutral both stay at 0 and 1 whatever the pedal. **Brake:** `STAT_BLS_EIN` and `STAT_BLTS_EIN` both change with the pedal. **Sport:** `STAT_FDYN_EIN` changes; the LED follows. **Cruise buttons:** `STAT_MFL1_EIN` to `STAT_MFL4_EIN` change | [Troubleshooting](#troubleshooting). If buttons 3 and 4 behave oddly while 1 and 2 work, trust a cruise test instead: their bit masks look like table errors |
| 27 | EWS: `EWS3.PRG` → `STATUS_LESEN` | Key sending (`STAT_SCHLUESSEL_SENDET`), not barred, the three "NIO" bits 0. Clutch down: `STAT_P_N_EINGANG` changes and `STAT_ANLASSER_AUS_P_N` = 0 ([SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/EWS3.md)) | Key, ring antenna, EWS; clutch-module pin 4 to EWS pin 8; EWS coding `PARK/NEUTRAL_EINGANG` |
| 28 | Pump | One prime heard at key-on; `STAT_EKP_EIN` = 1 during it; `STEUERN_EKP` clicks K96 and runs the pump (stop it with `STEUERN_EKP_AUS`); 5.0 ± 0.2 bar, under 0.5 bar lost (BMW) | Step 10; fuses F54 and F3; swap K96 with K19; [Checks on the pump circuit](#checks-on-the-pump-circuit) |
| 29 | Outputs: `STEUERN_DMTL_HEIZUNG` ('ein', then 'aus'); `STEUERN_SLP` and `STEUERN_SLV`; `STEUERN_KO` (K19); `STEUERN_E_LUEFTER`; `STEUERN_TEV`; `STEUERN_VENTIL_SAUGSTRAHLPUMPE` | Each part runs or clicks, and `JOB_STATUS` reads OKAY | That part's wiring. "Condition not met": try again with the engine running. Leave the injector and coil jobs alone |

Sources for steps 20–29: [BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf) (power, pedal, throttle and pump values), [SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md) (jobs and bits), [bmwfaq](https://bmwfaq.org/threads/duda-con-el-inpa.796332/) (INPA's menu). On a stock E46 M3, the throttles visibly follow the pedal at key-on ([MotoIQ](https://motoiq.com/project-e46-m3-part-8-the-dreaded-eml-light/5)).

### Steps 30–33: the oil-priming crank

In Phase 12, with the pump relay K96 and the injector relay K6327 pulled and the six coils unplugged ([README, Phase 12](README.md#phase-12-front-end-first-start-and-shakedown)):

| Step | Check | Pass | If it fails |
|---|---|---|---|
| 30 | Start interlock | Clutch up: no crank. Clutch down: cranks | EWS pin 8 input, EWS coding |
| 31 | Engine speed while cranking: `STATUS_MOTORDREHZAHL` | Above 0, and the tachometer moves | Crankshaft sensor and its wires (X60003 pins 8 and 21); fault 16 (0x10). Without it there's no injection, no spark and no pump hold |
| 32 | Oil, on the mechanical gauge | Pressure shows and holds; the red lamp goes out | Stop. Oil level, pickup O-ring, pump |
| 33 | Reset: refit the relays and coils, then [Session 6](#session-6-first-start-adaptations-and-throttle-check) steps 2–4 | `STAT_WDK_ADAPT_WERT` = 0 after the reset | Repeat with the charger on; throttle wiring |

Then the first start, Session 6 step 6.

## Coding step by step

Do the sessions in this order. The guide explains why and shows the order as a figure ([Deep dive: electronics and coding](README.md#deep-dive-electronics-and-coding)).

| Session | When | Main tools |
|---|---|---|
| 1. Vehicle order and codings | Phase 0, before you change anything | NCS Expert |
| 2. DME VIN, EWS delete and gearbox software | Read in Phase 1; vendor work in Phase 3 | Tool32, a vendor |
| 3. EWS | Phase 11 | Tool32 |
| 4. Cluster and light module | Phase 11 | PA-Soft, NCS Expert |
| 5. DSC coding and VIN | Phase 11, after Session 4 | PA-Soft, NCS Expert, INPA |
| 6. First start, adaptations and throttle check | Phase 12 | Tool32 |
| 7. Steering angle after the alignment | Phase 12 | INPA or Tool32 |
| 8. Vehicle-order changes and body modules | Phase 12, after Session 7, and whenever you change the vehicle order | NCS Expert |
| 9. Light module and headlights | Phase 12, last, with the front end on | NCS Expert |

Keep the charger on for every session, and run one program at a time.

### Session 1: Vehicle order and codings

**Background.** Cars built before 09/2001 store their options as a ZCS (three hex strings, GM, SA and VN) in the cluster (KMB), with a backup in the EWS. Cars built from 09/2001 store a vehicle order (FA) in the cluster (AKMB), with a backup in the light module (ALSZ) ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-fa-for-at-mt-swap.1290835/), [e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-zcs-for-at-mt-swap.1290589/), [BMW ST406](https://archive.org/download/BMWTechnicalTrainingDocuments/ST406%20Coding%20%26%20Programming/06%20Vehicle%20Coding%20Information.pdf)). NCS Expert codes each module from that record: the type code sets body (TOUR), engine (M54B25) and market, and the production date (#MMYY) decides which module versions NCS will accept ([e46fanatics](https://www.e46fanatics.com/threads/mk60-coding-index-the-following-control-unit-is-not-allowed-for-this-coding-job.1264623/), [NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/173720-mk60-vin-issue-m3-track-mode-rabbit-hole)).

1. NCS Expert → File → Load Profile → Expert Mode → OK.
2. VIN/ZCS/FA (F1) → ZCS/FA f. ECU (F3) → E46 → OK → AKMB on a car built from 09/2001, or KMB on an earlier car → OK. If AKMB doesn't answer, try ALSZ; if KMB doesn't, try EWS ([e46fanatics](https://www.e46fanatics.com/threads/how-to-change-abs-asc-control-module-trifecta-5df5-error-e46.1275927/)).
3. Screenshot the VIN (FG), the option list or ZCS strings, the production date and the type code.
4. Back (F6) → Process ECU (F4) → choose a module → Change job (F2) → `CODIERDATEN_LESEN` → Execute (F3). Copy `C:\NCSEXPER\WORK\FSW_PSW.TRC` into a folder named after the module. Repeat for KMB or AKMB, LSZ or ALSZ, GM5, DSC, EWS and IHKA or IHKR.

**Expect:** a readable vehicle order and one coding file per module.

**Rules.** Don't write an M3 type code into your stored vehicle order: the body modules (GM5 for the tailgate and rear wiper, the light module for the Touring's lamps) would then code as a coupe (our reading of the coding rules; nobody has documented it). Don't use Process Car until the vehicle order is right.

**Watch:** [50sKid – Code the vehicle order (2017), 08:52](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=532s) for reading the order, and [Motorsport Inspired – Enable the CSL oil-level display (2022), 00:35](https://www.youtube.com/watch?v=SISvhcoWmYE&t=35s) for `CODIERDATEN_LESEN` on an E46 M3 (watch it for the read job only; the option it enables needs CSL software).

### Session 2: DME VIN, EWS delete and gearbox software

**Read the donor DME before it goes anywhere** (charger on, ignition at position 2, engine off):

1. Tool32 → File → Load SGBD → `MSS54DS0.PRG` (a zero, not the letter O; the same file covers the MSS54HP) ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/d_0012.md)). Run `IDENT` and `FS_LESEN`, and save the results.
2. Load `12MSS54.PRG`. Run `AIF_LESEN` with argument 1, then 2, 3 and so on. For each slot record the VIN, software, authority and assembly numbers, plus `AIF_ANZ_FREI` (free slots left) and the first slot with an empty `AIF_FG_NR` and its `AIF_ADRESSE_LOW` ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/12MSS54.md), [ECUWorx](https://www.ecuworx.co.uk/2016/02/26/adding-updating-your-vin-uif-with-tool32/)).
3. For a DIY delete only: BMWFlash → File → Read DME → "No" for a partial read; save it and keep a copy ([ECUWorx](https://www.ecuworx.co.uk/how-to/using-the-mss5x-binary-modification-tool/)). A 32 kB file means an MSS54, 64 kB an MSS54HP ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)).

**Vendor route** (the guide's [Immobilizer (EWS)](README.md#immobilizer-ews) lists vendors and prices): order the EWS delete with your Touring's full VIN, manual-gearbox software if the donor was SMG, and the tampering-fault delete if offered. Decline every emissions delete.

**DIY delete** (a licensed tool function): load the partial read into ECUWorx's MSS5x tool, buy and activate its licence, select "EWS Delete + EWS Tampering DTC Delete" (and "Transmission Swap" to manual for an SMG donor), apply and write the changes, then reflash with BMWFlash (File → Reflash DME), key to 0 and back to 2 ([ECUWorx](https://www.ecuworx.co.uk/how-to/using-the-mss5x-binary-modification-tool/), [ECUWorx](https://www.ecuworx.co.uk/how-to/a-run-down-of-features-of-the-mss5x-binary-modification-tool-and-what-they-do/)). Don't apply any emissions option the tool offers.

**DIY VIN write** (Tool32, `12MSS54.PRG`), after ECUWorx's procedure:

1. Build the string from the free slot's `AIF_ADRESSE_LOW` and ten more fields, separated by semicolons: address; VIN (all 17 characters); today's date (DDMMYY in ECUWorx's example); change index; software number; authority number; assembly number; serial number; dealer number; kilometres; programme number. ECUWorx's example: `7596;WBSBL12345JR12345;260216;DA;7837331;7834533;7834530;NFS01;240;0;000401` ([ECUWorx](https://www.ecuworx.co.uk/2016/02/26/adding-updating-your-vin-uif-with-tool32/)). Copy the software, authority and assembly numbers from the latest filled slot.
2. Run `SEED_KEY`, paste the string into the Arguments box, then run `AIF_SCHREIBEN`. Check that `JOB_STATUS` reads OKAY. If it says Error or Rejected, run `SEED_KEY` again and retry without clicking anything else (same source).
3. Verify: `AIF_LESEN` with argument 0; INPA → E46 → Engine → MS S54 for S54 M3 → Coding; and a generic OBD scanner's VIN read, if it has one.

Slots are finite, so don't write repeatedly. A partial VIN fails state tests ([BMW SI B12 09 13](https://static.nhtsa.gov/odi/tsbs/2013/MC-10150160-9999.pdf)).

**An SMG donor's DME** has the same hardware as a manual one but different software ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)). Choose a vendor conversion, ECUWorx's "Transmission Swap", or a WinKFP flash to the US manual ("HS") data set; we didn't find the right data-set number, so get it from a vendor. Left on SMG software, the DME will probably log SMG bus faults 6 (0x06) and 123 (0x7B) ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)), and one shop's "coding" left a swapped sedan in limp mode ([UNRIVALED – Watch this before you S54 swap (2021), 02:02](https://www.youtube.com/watch?v=eddLff8yba0&t=122s)).

**Expect:** your VIN in the AIF; the engine starts with your EWS and key; fault 130 (0x82) may stay stored unless the tampering fault was deleted ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful)).

### Session 3: EWS

**After a delete** there's nothing to code. Check:

1. Your EWS coding file from Session 1 shows `PARK/NEUTRAL_EINGANG` = `aktiv`. Leave it there ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-ews-to-ignore-clutch-park-neutral-switch.1313143/)).
2. Tool32 → `EWS3.prg` → `STATUS_LESEN`, key in, clutch pressed: the key is sending and not barred, `STAT_ANLASSER_AUS_P_N` (starter blocked by P/N) reads 0, and while cranking `STAT_ANLASSER_FREIGESCHALTET` (starter released) reads 1 ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/EWS3.md)).
3. Tool32 → `MSS54DS0.PRG` → `FS_LESEN`: fault 130 (0x82) may be stored. The engine still starts ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful)).

Don't jumper EWS pins. "If you find yourself having to jump the actual pins in the EWS module itself then you have another EWS related issue" with the module, key or transponder (same source).

**Syncing a virgin DME.** This sequence worked once, on one owner's CSL-clone MSS54: a DME converted in hardware to run CSL software, whose immobilizer code (ISN) he had written in through its BDM programming port. He wasn't sure it works on a virgin DME, and no Touring build has confirmed it ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/145696-ews-sync-issue-with-csl-clone-dme-solved)). A forum moderator says the sync should be done in INPA ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/320555-mss54-and-mss54hp-ews-syncing-or-delete)), but the INPA keys for the MSS54 aren't documented; Kassel's "Shift + F6, F1" is for an MS43 ([KasselPerformance – MS43 EWS sync in INPA (2015)](https://www.youtube.com/watch?v=HPoaKPqLpgE)).

1. Charger on, ignition at position 2, engine off.
2. Tool32 → `EWS3.prg` → `WECHSELCODE_SYNC_DME`. Expect OKAY.
3. Load `MSS54DS0.PRG`. Type `0x01` in the Arguments box and run `EWS3_INITIALISIEREN`. Expect OKAY.
4. Run `EWS3_SYNC`. Expect OKAY.
5. Run `EWS3_GET_STATUS`. The failed Touring showed `EWS3_STATUS` = Invalid and `EWS3_STATUS_WERT` = 3 ([e46fanatics](https://www.e46fanatics.com/threads/ews-synch-for-s54-swap-into-e46-touring.1318881/)).
6. Run `FS_LESEN`: fault 130 (0x82) should be gone. `STATUS_DIGITAL` → `STAT_EWS3_FREIGABE` shows the release.
7. Key off for at least 10 seconds, then try to start.

**Reading the faults** ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md), [BMW ST051](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)):

| Fault 130 (0x82) type | Meaning | Next step |
|---|---|---|
| "Startwert leer" (start value empty) | A virgin DME that hasn't received the code table | Run the sync |
| "Wechselcode verloren" (rolling code lost) | An ordinary loss of sync | Re-run the alignment; BMW allows it any number of times |
| "Manipulation" | The DME is married to another EWS | Delete, virginize, or use the donor EWS |
| Fault 66 (0x42), EWS interface | The EWS–DME line, or the key was on with a module unplugged | Check pin 33's wire; re-run the alignment |

INPA's "ERROR_SG_REJECTED" means the module refused the job, not that the cable failed. "No free starting value storage space available" fits a DME that already holds a married table; "start value not understood" and "start value not set" came from the virginized-DME case ([e46fanatics](https://www.e46fanatics.com/threads/cant-sync-ews-dme-on-s54-swapped-e46-wagon.1300465/), [SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MS450DS0.md)).

**Using the donor's EWS:**

1. Make sure your own EWS's coding file is saved (Session 1).
2. Fit the donor's EWS with its DME, and put the donor key's transponder near the ring antenna.
3. Code the donor EWS to match your file, especially `PARK/NEUTRAL_EINGANG` = `aktiv`.
4. Re-align it with the sync sequence above ([e46fanatics](https://www.e46fanatics.com/threads/ews-synch-for-s54-swap-into-e46-touring.1318881/)).
5. Check `STATUS_LESEN` as after a delete.

### Session 4: Cluster and light module

**Before you start:** the light module untouched, your true mileage photographed, and the M3 cluster's untouched EEPROM saved (Session 1 and the donor list).

**Service route.** Send the cluster with your VIN, the light module's mileage, and a note that it's going into a wagon. Kassel asked Tenza for the car's mileage, year, body (wagon or sedan), the switch-center buttons and whether the DME was tuned, and added the rear-door lights ([Tenza Motorsports – 5 things they don't tell you, part 2 (2021), 05:42](https://www.youtube.com/watch?v=mDBiRn30fEs&t=342s)).

**Chip route, two documented ways:**

| Step | A: blank chip, written by PA-Soft ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)) | B: programmer ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)) |
|---|---|---|
| 1 | With the M3 cluster plugged into your car, read and save its EEPROM in PA-Soft | Photograph the needles at rest (INPA can drive them to known positions), then pull them off carefully |
| 2 | In a copy of the file, clear the mileage and set your car's VIN | Open the cluster and desolder the M35080 |
| 3 | Remove the needles, open the cluster, desolder the M35080 and solder in a blank one (this owner used an 080D0WQ) | In the R270 software, select "EEPROM M35080 3", read the chip, check the VIN, and use "erase odometer" |
| 4 | Plug the cluster in: it shows "code". Write your prepared file with PA-Soft | Solder the chip back, reassemble, and refit the needles: push them on about 2 mm, turn them anticlockwise to the stop, set them to the photographed positions, press them home |
| 5 | The cluster restarts with no tamper dot, and your mileage appears within seconds, read from the light module | Write your VIN with PA-Soft; the mileage then comes from the light module |

Later clusters use M35080 "v6" chips, which a stock R270 can read but not write; write the image to a "3" chip instead (same source). Editing and re-burning the original chip is "hit or miss", so use a new chip ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/154645-cluster-with-coding-index-0x24-virginization)). One owner who dropped in a blank chip needed no programmer at all (same source). Early M3 clusters (coding index 20 or 21) were made by Motometer, whose clusters PA-Soft can program completely: a 323Ci owner set a replacement Motometer cluster's VIN and true mileage that way ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/), [e46fanatics](https://www.e46fanatics.com/threads/cluster-swap-tamper-dot-removal-success.1130431/)). Check who made yours before buying tools.

**Code the options** by editing, not default-coding:

1. NCS Expert → read from AKMB → Process ECU → AKMB → `CODIERDATEN_LESEN` → Execute. Back up the `FSW_PSW.TRC`.
2. Edit the copy, then save it as `FSW_PSW.MAN` (in Notepad, choose "All Files", or it saves as .TXT).
3. Load your manipulation profile → Process ECU → AKMB → `SG_CODIEREN` → Execute ([ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf), [Motorsport Inspired (2022), 02:05](https://www.youtube.com/watch?v=SISvhcoWmYE&t=125s)).

| Parameter | Set to | When |
|---|---|---|
| `CAN_OELDRUCKSCHALTER` (oil pressure over CAN) | `nicht_aktiv` | Every build: X60004 pin 11 is wired to cluster pin 13. An MSS54HP didn't light the lamp over CAN even with this `aktiv` ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)) |
| `GENERATOR_UEBER_CAN` (charge lamp over CAN) | `nicht_aktiv` | With X60004 pin 1 wired to cluster pin 2. `aktiv` only if you leave the lamp on CAN with stock MSS54HP software (same thread) |
| `TOG_UEBER_CAN` (oil level over CAN) | `nicht_aktiv` | With X60004 pin 21 wired to cluster pin 17. `aktiv` only with an MSS54HP and no wire |
| `TANK_KENNLINIE` (fuel-gauge curve) | `60_l_literskala` | A plastic tank, the Touring's or the M3's; `metalltank` only for an ex-M56 SULEV metal tank. Check against a measured fill ([Fuel gauge and tank senders](#fuel-gauge-and-tank-senders)) |
| `OELNIVEAU_M3` | Leave it as it is | The oil-level readout works only on an MSS54HP running the Euro-only CSL software, and this build keeps stock US software ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/17863-how-do-you-code-csl-oil-level-indicator)) |
| `ANZEIGE_HOCHLADEN` | `aktiv` | M Track light, with an M3 MK60 coded for M Track ([liam821](https://liam821.com/MK60-Comparison.pdf)) |
| Units | US | If the cluster came from a km/h car ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/83919-canada-to-u-s-importation-gauge-cluster-programming)) |

The three CAN switches must match the wiring: read why in [Cluster wiring](#cluster-wiring). The names come from an M3's coding list ([NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf)); one forum snippet says they exist on cluster coding indexes 07, 08, 23 and 24 ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-cluster-coding.1330549/), unverified), so look for them in your cluster's file.

Never write a blank coding file to a cluster whose coding index has been changed: one such cluster's tach stuck at 9,000 rpm until its EEPROM backup went back ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)). Keep the M3 index; the non-M index 08 that some retrofit guides use gives non-M gauge definitions (same source).

**Cars built before 09/2001.** The light module may not push the mileage to a new cluster. One 2001 Touring owner had the true reading written into the chip; another owner fitted a newer light module and switched his car to FA ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/), [e46fanatics](https://www.e46fanatics.com/threads/e46-m3-cluster-coding.1278842/)).

**Expect:** no tamper dot; your true mileage, matching the Phase 0 photo; the DSC and parking-brake lamps may go out within a short drive once the VINs match ([e46fanatics](https://www.e46fanatics.com/threads/e46-m3-cluster-coding.1278842/)).

> [!CAUTION]
> The light module is your car's mileage record. PA-Soft can write a VIN and mileage into the light module, and one retrofit guide uses that to match the module to a donor cluster ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)). Don't: it changes your car's recorded mileage. Make the cluster match the light module, keep the photos and screenshots, and see the guide's [Instrument cluster and mileage](README.md#instrument-cluster-and-mileage).

### Session 5: DSC coding and VIN

**Before you start:** the cluster carries your VIN (Session 4); the charger is on.

**Option A, your Touring's own MK60** (already coded for your car):

1. INPA → E46 (F3) → Chassis → DSC MK60 → fault memory (F4) → read (F1). After a cluster change, expect 5EF1 "VIN not initialized" ([e46fanatics](https://www.e46fanatics.com/threads/how-to-change-abs-asc-control-module-trifecta-5df5-error-e46.1275927/); these steps were written on a non-US 2002 318i, whose INPA pages are the same).
2. Shift+F4 (compensation routines) → F1 (steering angle and VIN initialisation) with the wheel straight. Accept the warning; a fault is flagged if the wheel is more than 30° off center. Expect "initialization completed" (same source).
3. Run the other two compensation routines with the wheel straight, no brake pressure and the car level ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap)).
4. Fault memory (F4) → clear (F2) → read (F1): no faults. Clear the faults in every module, cycle the ignition and read again.

Some owners run a non-M MK60 with M3-like values set by hand in NCS Dummy, and on some non-M units changing `BAUART_MK60` from `touring` to `touring_s` is reported to suit a faster rack ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/172815-flashing-the-mk60-with-zcp-software/page2), [e46fanatics](https://www.e46fanatics.com/threads/mk60-coding-index-the-following-control-unit-is-not-allowed-for-this-coding-job.1264623/)). Nobody has documented either in a Touring with M3 brakes and rack. It's a safety system; leave it alone unless you know what each value does.

**Option B, the M3's MK60:**

1. **Write your VIN into it.** PA-Soft → the ABS/DSC module → Reprogramming → Write FGSTNR, and enter the last 14 characters of your VIN, the ones after "WBA" ([LM Auto Repairs – E46 MK60 coding and VIN (2016), 04:47](https://www.youtube.com/watch?v=1dn4c3g6dsA&t=287s), filmed on a 2003 E46 diesel).
2. **Code it.** NCS Expert → Expert Mode → F1 → F3 → E46 → AKMB (try EWS if AKMB fails) → F6 → F4 → MK60 → check the job is `SG_CODIEREN` → F3. Expect "coding active", then "coding ended" ([50sKid – E46 DSC unit replacement and coding (2016), 31:14](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=1874s)).
3. **If NCS doesn't list MK60, or reports "Codierindex … nicht zulässig"**, the production date in the session's vehicle order is too early for the unit. Use #0902 or later for an M3 MK60, entered in Enter FA for this session only, without `FA_WRITE`. Then check the unit's coding index ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap), [NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/173720-mk60-vin-issue-m3-track-mode-rabbit-hole), [e46fanatics](https://www.e46fanatics.com/threads/ncs-expert-coding-is-faulty-resolved-8-12-21.1293250/)).
4. **Set M3 values.** Coded from your Touring's vehicle order, the unit takes 325i values ([liam821](https://liam821.com/MK60-Comparison.pdf)). Read its coding (`CODIERDATEN_LESEN`), set the values below, save as `FSW_PSW.MAN` and write it with `SG_CODIEREN`. These are the values liam821 read from real cars:

   | Parameter | 330i ZHP | M3 | M3 Competition |
   |---|---|---|---|
   | `BAUART_MK60` | `limousine_ms` | `coupe_m` | `csl` |
   | `MOTOR_ART_DSC_2` | `m54b30` | `s54b32` | `s54b32` |
   | `GETRIEBE` | `handschaltung` | `handschaltung` | `handschaltung` |
   | `LENKWINKELKENNLINIE_2` (rack) | `wert_02` | `wert_05` | `wert_04` |
   | `DRUCKMODELL_VORDERACHSE` | `typ_1` | `typ_0` | `typ_0` |
   | `DRUCKMODELL_HINTERACHSE` | `typ_2` | `typ_2` | `typ_3` |
   | `LOGIK_HA_SPERRE` (limited-slip logic) | `nicht_aktiv` | `aktiv` | `aktiv` |
   | `SPERRDIFFERENZREGELUNG` | `aktiv` | `nicht_aktiv` | `nicht_aktiv` |
   | `TRAKTIONDIFFERENZREGELUNG` | `aktiv` | `nicht_aktiv` | `aktiv` |
   | `PRE_MSR` | `nicht_aktiv` | `nicht_aktiv` | `aktiv` |
   | `DBC_MIN_AUSLOESEDRUCK` | `wert_01` | `wert_03` | `wert_03` |
   | `REIFENDRUCKWARNSYSTEM` (flat-tire warning) | `nicht_aktiv` | `aktiv` | `aktiv` |
   | `DTC_LAMPE` | `nicht_aktiv` | `nicht_aktiv` | `aktiv` |

   Several further handling parameters (`UEBERSTEUERN_MUE_0_2`, `UNTERSTEUERSCHWELLE_2`, `GEARMOMENTREGLER_MAX_HA_2` and others) take S54 values only when the vehicle order says `S54B32` (same source). Compare them in liam821's file; edited by hand, they stay at 325i settings. There's no Touring value for `BAUART_MK60` on the M3 unit; ECUWorx gives `cabrio_m` for convertibles and nothing for a Touring ([ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf)).
5. **Initialise** as in Option A, steps 1–4.
6. **M Track (optional).** Leave it until the car runs, and do it with Session 8. ECUWorx's procedure: in Enter FA, add `$7MA`; `FA_WRITE` to ALSZ and AKMB; `SG_CODIEREN` on AKMB, then on MK60; then set `DRUCKMODELL_HINTERACHSE` = `typ_2` for non-Competition brakes, `LENKWINKELKENNLINIE_2` = `wert_05` for the standard rack, and `DTC_LAMPE` = `nicht_aktiv` if your cluster has no M Track light ([ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf)). That's a vehicle-order change, so follow Session 8's rules. `$7MA` is the Competition Package's option code: ETK lists the Competition calipers under option S7MAA, from 12/2004 ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/brakes/rear_brake_brake_pad_wear_sensor/)).

**Bleeding with INPA.** INPA → E46 → Chassis → DSC MK60 → Activate (F6) → Control hydraulic (F1) → F2 for front left and rear left, F3 for front right and rear right. Press the pedal and open the bleed screw; the pump runs and pulses the pedal; close the screw when INPA finishes. Do each corner two or three times, then finish with a conventional bleed ([e46fanatics](https://www.e46fanatics.com/threads/how-to-change-abs-asc-control-module-trifecta-5df5-error-e46.1275927/)). On a Z4 M's MK60, with the same menus, the pedal stayed spongy until the owner pressed it hard rather than the 80% the instructions suggest, and the job used about 1.25 L of fluid ([Z4-forum](https://z4-forum.com/threads/bleed-the-abs-dsc-system-using-inpa.146558/)). The bleed order and method are in the guide's [Brakes and bleeding](README.md#brakes-and-bleeding).

**Expect:** the DSC and brake lamps out, and no 5EF1 or 5E1F.

**If it fails:** an M3 MK60 that never clears "VIN not initialized" in a Touring was cured by refitting the Touring's own unit ([e46fanatics](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/)).

**Watch:** [LM Auto Repairs – E46 MK60 coding and VIN (2016), 04:47](https://www.youtube.com/watch?v=1dn4c3g6dsA&t=287s) for Write FGSTNR (on a 2003 E46 diesel), [50sKid – E46 DSC unit replacement and coding (2016), 31:14](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=1874s) for the NCS coding, and the same video at [33:47](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=2027s) for the Shift+F4 → F1 initialisation.

### Session 6: First start, adaptations and throttle check

**Why.** BMW: if the throttle housing or pedal module is replaced, "the ADAPTATIONS MUST BE CLEARED and ADAPTATION PROCEDURE MUST BE PERFORMED… If this is not performed, the vehicle will not start, or run in 'fail-safe' mode" ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%201%29.pdf)). Do this at the first start, as part of [Phase 12](README.md#phase-12-front-end-first-start-and-shakedown), and again after any wiring or vehicle-order change.

Tool32, `MSS54DS0.PRG` ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)):

1. Charger on, key on, engine off. Run `IDENT` and `FS_LESEN`, and save the results.
2. Run `ADAPT_LOESCHEN`, then `FS_LOESCHEN`.
3. Key off and wait at least 15 seconds: on a cold engine the DME runs its post-drive throttle check 10 seconds after key-off ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%201%29.pdf)). Key on again and listen for the throttles' click (the pre-drive check).
4. `STATUS_ADAPTIONSBLOCK_06` → `STAT_WDK_ADAPT_WERT` should read 0 (throttle adaptation OK).
5. `STATUS_DIGITAL`, with a gear engaged and the parking brake on: `STAT_KRAFTSCHLUSS_EIN` reads 1 with the clutch pedal up and `STAT_KUP_EIN` reads 1 with it down. In neutral both stay fixed whatever the pedal does: they read one input through the gear switch ([Clutch switch, gear switch and cruise](#clutch-switch-gear-switch-and-cruise)). `STAT_BLS_EIN` and `STAT_BLTS_EIN` both follow the brake, and `STAT_FDYN_EIN` follows the Sport button.
6. Start without touching the accelerator and idle to operating temperature. Watch `STATUS_LFR` and `STATUS_LAMBDA_ADD_1` and `_2`.
7. Warm: the VANOS jobs. Run `STEUERN_LLS_TESTDREHZAHL` (raised idle for the test), then the adjustment-time jobs `STEUERN_EVANOS1_VERSTELLZEIT` (intake camshaft) and `STEUERN_AVANOS1_VERSTELLZEIT` (exhaust camshaft), and the leak jobs `STEUERN_EVANOS1_DICHTHEIT` and `STEUERN_AVANOS1_DICHTHEIT`. The S54 is a straight six with one bank, so use the jobs ending in 1; the job file also lists bank-2 jobs, which this engine doesn't use. We found no specification for the results: keep the readings as a baseline and compare them with the donor's from Phase 1.
8. Drive, with several closed-throttle coast-downs in gear from 3,000–5,000 rpm. `STAT_LU_ADAP_CNT_WERT` should rise: that's the crank-wheel adaptation the misfire monitor needs for full sensitivity ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)).

**In INPA**, adaptations are erased under E46 → Engine → F4 → F7, running each entry. That was filmed on an M54 car; the MSS54 script's path isn't documented ([50sKid – Code the vehicle order (2017), 23:59](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1439s)). One owner reportedly "soft-bricked" a DME clearing adaptations in INPA ([z4-forum](https://z4-forum.com/threads/e85-manual-swap-trouble-solved.152760/), unverified), so keep the charger on.

Clearing adaptations also makes the DME relearn which equipment is fitted: pump type, A/C, cruise and the DM-TL heater (`STAT_EKP_CFG_VERBAUT_WERT`, `STAT_KKOS_ST_VERBAUT_WERT`, `STAT_FGR_MFL_VERBAUT_WERT`, `STAT_LDPH_VERBAUT_WERT`) ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).

**Expect:** a steady idle with fuel trims near zero, all four VANOS jobs completing, no new faults.

**Watch:** [50sKid – Code the vehicle order (2017), 23:59](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1439s) for INPA's F4 → F7 adaptation erase (on an M54 car).

### Session 7: Steering angle after the alignment

**When:** after the wheel alignment at the car's loaded ride height ([Wheel alignment](README.md#wheel-alignment)), and after any later steering or suspension work.

**INPA (MK60):**

1. Car level, wheel dead straight, ignition on, no brake pressure.
2. INPA → E46 → Chassis → DSC MK60 → Shift+F4 → F1. Accept the warning. Expect "initialization complete" ([Evan Goyuk – Calibrate the steering-angle sensor (2020), 02:48](https://www.youtube.com/watch?v=lseY6SRXWks&t=168s)).
3. Run the other two compensation routines ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189096-mk20-mk60-swap)).
4. Check: status (F5) → read analog → read DSC sensor (F2). The steering angle should read 0 with the wheel straight; "if it says like two or three then you know that it's not calibrated" ([Evan Goyuk (2020), 03:19](https://www.youtube.com/watch?v=lseY6SRXWks&t=199s)).
5. Clear the faults in every module, cycle the ignition and read again.

**Tool32, if your INPA lacks the MK60 page** (File → Load SGBD, then double-click the job) ([e46fanatics](https://www.e46fanatics.com/threads/how-to-calibrate-steering-angle-using-tool32.1282261/)):

| Unit | File | Job |
|---|---|---|
| MK60 (your Touring; M3 from 09/2002) | `DSC_MK60.PRG` | `lenkwinkel_dsc_abgleichen`. One guide gives `test_lenkwinkel` in the same file ([e46fanatics](https://www.e46fanatics.com/threads/how-to-change-abs-asc-control-module-trifecta-5df5-error-e46.1275927/)); try the first and read the job list |
| MK20 (M3 before 09/2002) | `DSC_E46.PRG` | `lenkwinkelsensor_id_dsc_schreiben` or `abgleich_lws_aq_sensoren`, "whichever succeeds". The thread's MK20 cars are 323i and 328i, so confirm Tool32 identifies an M3 MK20 with it. Only relevant if you run an early donor's MK20, which won't plug into your harness without rewiring |
| Bosch DSC 5.7 | `DSC57.PRG` | `test_lenkwinkel`. For the 325xi and 330xi only |

**Other fallbacks.** A generic scan tool calibrated the angle "straightway" when one shop's INPA couldn't connect ([LM Auto Repairs (2016), 06:23](https://www.youtube.com/watch?v=1dn4c3g6dsA&t=383s)); the Foxwell NT530 lists a steering-angle reset ([BimmerWorld](https://www.bimmerworld.com/Tools/Foxwell-NT530-OBD-System-Scanner-for-BMWs.html)).

**If it fails:**

- Tool32 returns IFH-0009: a swapped steering-angle sensor that was never coded. Code it with NCS Expert, cycle the key, and retry ([e46fanatics](https://www.e46fanatics.com/threads/how-to-calibrate-steering-angle-using-tool32.1282261/)).
- The angle sticks at "!1440" and jumps back after a reset: the sensor has failed ([e46fanatics](https://www.e46fanatics.com/threads/calibrating-steering-angle-with-inpa.1287151/)). It sits at the base of the steering column, and a new one needs calibrating too ([Earl Moorhead – E46 code 5E43, steering-angle sensor (2023), 04:05](https://www.youtube.com/watch?v=2mqz14tWpMI&t=245s)).

**Expect:** the DSC lamp out, 0° with the wheel straight, and a straight wheel on the road test.

**Watch:** [Evan Goyuk – Calibrate the steering-angle sensor (2020), 02:48](https://www.youtube.com/watch?v=lseY6SRXWks&t=168s) for the calibration and [03:19](https://www.youtube.com/watch?v=lseY6SRXWks&t=199s) for the status check.

### Session 8: Vehicle-order changes and body modules

**When:** once the car runs (Phase 12, after Session 7), and whenever you change the vehicle order (M Track, a production date).

1. NCS Expert → Expert Mode → read the vehicle order from AKMB (Session 1).
2. Enter FA → E46 → OK → OK, leaving the VIN as it is. Select an option code and press Delete, or type one under Attribute and press Add. OK → Back.
3. Process ECU → AKMB → Change job → `FA_WRITE` → Execute ("Job active", then "Job ended") → Change ECU → ALSZ → Execute ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-fa-for-at-mt-swap.1290835/), [50sKid – Code the vehicle order (2017), 12:31](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=751s)).
4. Restart NCS Expert and read the order back from AKMB and ALSZ ([50sKid (2017), 15:40](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=940s)).
5. Load the Factory Coding profile → Process Car → Code Car. It stops at the first module that fails, so code the rest one at a time ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-fa-for-at-mt-swap.1290835/), [50sKid (2017), 17:15](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1035s)).
6. Code AKMB and ALSZ themselves as well: one owner's gearbox icon stayed lit until he did ([50sKid (2017), 26:05](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1565s)).
7. Reset the DME adaptations (Session 6).

On a car built before 09/2001, the ZCS equivalent is Enter ZCS: remove the last digit of each string (a checksum), tick "Calculate checksum", make the change, then `ZCS_SCHREIBEN` to KMB and EWS ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-zcs-for-at-mt-swap.1290589/)).

**Modules after a vehicle-order change:** the DSC, the light module, and possibly GM5 and the climate control ([e46fanatics](https://www.e46fanatics.com/threads/diy-how-to-code-fa-for-at-mt-swap.1290835/)).

- **GM5** needs no coding for the swap. A used GM5 is coded by writing a blank coding file, and its stored VIN "doesn't actually impact anything". A COAPI-2060 write error was a loose pin in its plug ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/21981-ncs-error-while-trying-to-recode-used-gm5-module)).
- **EWS:** `PARK/NEUTRAL_EINGANG` stays `aktiv`.
- **Climate control:** no swap coding found.
- **Restoring a module's defaults:** write a blank coding file ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/331072-need-help-starting-with-ncs-expert-manipulation-profile)), except on a cluster whose coding index has been changed (Session 4).

**Watch:** [50sKid – Code the vehicle order (2017), 09:59](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=599s) for editing the order and [12:31](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=751s) for `FA_WRITE`. His car is a non-M E46 converted from automatic, so the option he deletes (205, automatic gearbox) isn't one you'll touch.

### Session 9: Light module and headlights

**When:** last, at the end of Phase 12, with the front end on and the car at ride height.

- The light module keeps your car's VIN and mileage; the swap itself needs no change to it.
- **Halogen M3 lamps in a halogen Touring:** no coding change. Confirm the lamps work as fitted.
- **Xenon or bi-xenon M3 lamps in a halogen Touring,** once the levelling sensors and their wiring are in ([Mirrors and headlights](#mirrors-and-headlights)):
  1. Add `$522` (xenon) to the vehicle order with Session 8's steps, writing it to AKMB and ALSZ ([E46Zone](https://www.e46zone.com/forum/topic/33680-coding-xenon-headlights/)).
  2. Code the light module by editing its coding file, as in Session 4: `BI_XENON` = `aktiv` for bi-xenon lamps; `KALTUEBERWACHUNG_AL` = `nicht_aktiv`, so the module stops sending the cold-check pulse to the low beams; automatic levelling on (`AUTO_LWR_ENABLE`). The levelling sensors' curves are `KENNLINIE_LWR_SENSOR_VO` and `KENNLINIE_LWR_SENSOR_HI` ([NCS list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf), [BMW ST034](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/2%20Driver%20Information%20Internet-1.pdf)). One owner's high beams worked only once `BI_XENON` was `aktiv` ([e46fanatics](https://www.e46fanatics.com/threads/pre-facelift-xenon-retrofit-ncs-expert-coding-questions.1314954/), unverified).
  3. Check with Tool32, `LSZ_2.PRG`: `XENON_VORHANDEN` and `LWR_VORHANDEN` confirm the coding, and `STATUS_LESEN` shows both sensors' voltages, 0–5 V, changing as the car is loaded ([SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ_2.md)). The rear sensor stays on your Touring's axle while the front one now rides on the M3 arm, so check that the beam holds steady as you load the car.
  4. Aim the lamps at ride height, after waiting at least 30 seconds for the levelling to cycle (BMW ST034).
- Upgrading the light module itself (for example from version 1.3 to 4.0) took one owner PA-Soft and NCS work ([e46fanatics](https://www.e46fanatics.com/threads/e46-m3-cluster-coding.1278842/)). Never replace it at the same time as the cluster ([Mirrors and headlights](#mirrors-and-headlights)).
- A vehicle order written to the wrong module mis-coded one light module so its rear lights misbehaved ([bmwfaq](https://bmwfaq.org/threads/perdida-fa-vo-e46.1068598/), unverified).
- Headlight aim is an inspection item; have it set once the front end is final.

## Readiness and inspection

### What the MSS54 monitors

From BMW's M3 training ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)):

| Monitor | Runs when |
|---|---|
| Catalyst | Closed-loop operation, engine at operating temperature, 5–80 km/h (3–50 mph), calculated catalyst temperature 350–650 °C, steady throttle and engine speed; once per trip |
| O2 sensors and heaters | Continuously in closed loop |
| Secondary air | After a cold start between −10 and 40 °C (14–104 °F); the pump runs about 90 seconds, and the pre-cat O2 sensors must respond within a set time |
| EVAP leak test (DM-TL) | See the next section |
| Purge | O2 control active, coolant above 60 °C, engine under load; a second step runs at idle when stationary. A generic scanner doesn't list purge on its own: it reports it as part of the EVAP monitor |
| Misfire | Counted over 1,000- and 200-revolution windows; full sensitivity only after the crankshaft-wheel adaptation ([Session 6](#session-6-first-start-adaptations-and-throttle-check)) |

The S54 has one bank of six cylinders, so there's one set of catalyst and O2 results, not two.

### The DM-TL leak test

The MSS54's leak test runs in the DME's follow-up mode, with the engine off and the ignition off, and needs all of these ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)):

- the car driven for at least 20 minutes before switch-off,
- parked for at least 5 hours before that drive,
- fuel between 15 and 85% of the tank,
- air temperature between −7 and 35 °C (20–95 °F),
- altitude below 2,500 m,
- battery between 11.5 and 14.5 V.

"When these criteria are satisfied every second time, the ECM will start the Fuel System Leak Diagnosis Test. The test will typically be carried out once a day." It takes 45–270 seconds and finds leaks down to 1.0 mm (0.040 in) (same source). EVAP is the monitor reported "not ready" on an MSS54 swap ([e46fanatics](https://www.e46fanatics.com/threads/s54-swaps-and-smog-in-california-update.1303447/)).

**The cluster feeds the test.** The DME takes the fuel level, the outside temperature and the parked time from the cluster over CAN. Its leak-test status has a "waiting for fuel level" state, it has faults for an implausible outside temperature after a long stop, 225 (0xE1), and an implausible parked time from the cluster, 226 (0xE2), and it detects refueling from the cluster's level, for its "Check Filler Cap" message ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md), [BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)). With an M3 cluster reading your Touring's tank senders, a gauge that reads wrongly can keep the test from ever running. Check the gauge against a measured fill first ([Fuel gauge and tank senders](#fuel-gauge-and-tank-senders)).

### A drive plan for readiness

This plan combines BMW's enabling conditions with New York's universal drive cycle; it isn't a BMW-published cycle ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf), [NYVIP3](https://www.nyvip3.com/OBDII/UniversalDriveCycle), [NYVIP3](https://www.nyvip3.com/OBDII/HelpingSetMonitors)).

1. **Before you start:** fix every fault so the check-engine lamp is off, and confirm `STAT_MIL_EIN` = 0. Keep the tank between 35 and 85% full: BMW's leak test needs 15–85%, and New York's tips say some EVAP monitors want 35–85%, so 35–85% suits both. Keep the battery healthy. While parked, prove the hardware with the system checks below.
2. **Evening:** park for at least 5 hours. Don't switch the ignition on before the cold start.
3. **Morning:** cold start between −10 and 40 °C, and let it idle about 2.5 minutes so the secondary-air run and its O2 check finish.
4. **Drive at least 20 minutes:** steady stretches at 50–80 km/h (30–50 mph) for the catalyst monitor, steady 90 km/h (55 mph) stretches, several coast-downs in gear without the clutch or brake, and some warm idling for the purge check.
5. **Park and switch off for at least 5 minutes** so the leak test can run; you may hear the pump. Don't unlock, lock or restart in that time.
6. **Repeat steps 2–5 the next day:** the leak test runs only every second time its conditions are met.
7. **Check readiness** with a generic OBD-II scanner, or in Tool32.

Clearing codes or disconnecting the battery resets readiness, so don't do either in the weeks before a test ([NYVIP3](https://www.nyvip3.com/OBDII/ReadyVSNotReady)).

### Checks with Tool32 and a scanner

All in `MSS54DS0.PRG` ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)):

| Job | Shows |
|---|---|
| `STATUS_ADAPTIONSBLOCK_26` | The readiness mask (`STAT_FF_FF_RDY_WERT`), drive cycles since the last reset, and counters per monitor |
| `START_SYSTEMCHECK_SEK_LUFT`, then `LESEN_SYSTEMCHECK_SEK_LUFT` | Secondary-air system check; "1_SLS_OK" passes |
| `START_SYSTEMCHECK_DMTL`, then `LESEN_SYSTEMCHECK_DMTL` | Leak-test check. A result ending "_DICHT" means sealed; "GROBLECK" and "FEINLECK" mean a coarse or fine leak, "DECKEL_FEHLT" a missing cap, and the "WARTEN" states that it's waiting, for example for the fuel level |
| `STATUS_TANK_DICHTHEIT` | The pump's measuring current against its reference current. BMW: sealed when the measuring current is above the reference |
| `STEUERN_TEV_CHECK` | Purge-valve check; "16_ERGEBNIS_TEV_OK" passes |
| `STEUERN_SLP`, `STEUERN_SLV` | Run the secondary-air pump and valve |
| `STATUS_DIGITAL` | `STAT_MIL_EIN`: whether the DME is asking for the check-engine lamp |

Whether these checks set a monitor to "ready" or only test the hardware isn't documented. A generic scanner shows the monitor status and whether the lamp is commanded on (OBD mode 01), the stored codes (mode 03) and, on many scanners, the stored VIN (mode 09).

### What an inspection checks

- **The federal OBD rule:** a car with stored codes passes if the check-engine lamp isn't commanded on; a model-year 2001-or-later car may pass with one monitor not ready; and it fails if the lamp is commanded on but not lit, or if the lamp doesn't light at all with the key on and the engine off ([40 CFR 85.2222](https://www.ecfr.gov/current/title-40/chapter-I/subchapter-C/part-85/subpart-W/section-85.2222)). So check the bulb at key-on with the M3 cluster fitted. States set their own limits on top: New York fails a 2001-or-later car with more than one monitor not ready ([NYVIP3](https://www.nyvip3.com/OBDII/ReadyVSNotReady)).
- **The stored faults.** Location 1 (0x01), the pump fault, doesn't light the lamp. Whether a leftover 130 (0x82) after an EWS delete commands the lamp hasn't been documented: check `STAT_MIL_EIN` and a generic scanner's mode 01 and 03 rather than guess, and order the tampering-fault delete with the EWS delete ([Session 2](#session-2-dme-vin-ews-delete-and-gearbox-software)).
- **Massachusetts** doesn't emissions-test a 2001–05 car in 2026, so there it's a safety inspection only; its anti-tampering rules still apply ([Massachusetts](README.md#massachusetts)).
- **California** and other states that check DME software: see the guide's [Registration and legal](README.md#registration-and-legal-us).

### When a monitor won't complete

- **EVAP:** check the heater on X60004 pin 18 and the pump on pin 30 with the triangle test (step 9 of the [checks](#checks-before-first-power-up)), and run `LESEN_SYSTEMCHECK_DMTL`. One MS45.1 car swapped pins 20 and 30 by label and still had P2418, "switching valve control circuit open" ([e46fanatics](https://www.e46fanatics.com/threads/e46-m3-sport-button-retrofit-on-non-m.1286041/)): prove the pump's pin, don't follow the label ([DM-TL leak-test pump](#dm-tl-leak-test-pump-test-before-you-swap)). Then check the fuel gauge against a measured fill, the hoses and the filler cap; check that `STAT_LDPH_VERBAUT_WERT` shows the heater after an adaptation reset; and remember the −7 to 35 °C window. With a smoke tester, close the leak-test pump's vent first and stay under 0.1 bar (1.5 psi) ([BMW TechDrive](https://automotivetechinfo.com/wp-content/uploads/2008/02/What-If-It-Is-Not-The-Gas-Cap.pdf)).
- **Secondary air:** run the pump and valve with `STEUERN_SLP` and `STEUERN_SLV`, check the pre-cat O2 sensors' response, and make sure the cold start is inside −10 to 40 °C. Lazy pre-cat sensors are reported to stall this monitor ([e46fanatics](https://www.e46fanatics.com/threads/e46-emission-readiness-monitor-issues.1244521/), unverified).
- **Several monitors at once:** a fault that keeps coming back stops monitors completing, and clearing it resets them all ([NYVIP3](https://www.nyvip3.com/OBDII/ReadyVSNotReady)). Fix the cause, then drive the plan again.

## Troubleshooting

**Fault numbers.** INPA prints fault locations in decimal and the job documentation in hex; this manual gives both. The two you'll see most: **130 (0x82)**, "EWS-Signalmanipulation", the immobilizer fault; and **1 (0x01)**, "Relais Kraftstoffpumpe", the pump fault that US software stores when K96 replaces the pump module ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)).

### Won't start

Work down the questions in order; each one rules out a group of causes. Tool32 jobs are in `MSS54DS0.PRG` unless named otherwise.

![Won't start](diagrams/25-flow-no-start.svg)

*Figure 11. The no-start questions in the order below, with the same numbers. Answer each one: the arrow to the right names what to check, and the arrow down goes to the next question. If the engine starts and then dies, use the next figure instead.*

1. **Key on: does Tool32 `IDENT` (or INPA) reach the DME?**
   - **No:** check the cable's pin 7/8 bridge and that the COM port matches `obd.ini` (the DME talks on OBD pin 7). Does the DME relay K6300 click? If not: terminal 15 at X60004 pin 26 (F29), the relay, its control wire from X60002 pin 23. Battery voltage at X60001 pins 7 and 8 with the relay on? If not: F102, the E-box fuse carrier, X64101/X64102. Then the grounds: X60001 pins 4, 5 and 6, X60004 pin 5, X60005 pin 5. BMW lists "ECM (Not Found)" and no start among the signs of poor power and grounds ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)). Still nothing: compare the E-box plugs pin by pin; a Euro 328i Touring whose X6011 didn't mate cranked without starting, and a scanner saw no modules ([e46fanatics](https://www.e46fanatics.com/threads/328i-touring-s54-swap-dme-wiring.1305546/)).
   - **Yes:** go to 2.
2. **Clutch fully down, key to start: does the starter crank?**
   - **No:** a battery at rest of at least about 12.4 V (generic) with the charger on; Tenza's first attempt failed on a flat battery ([Tenza Motorsports – M3 Touring build finally runs (2021), 03:55](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=235s)). Then `EWS3.PRG` → `STATUS_LESEN`: is the key sending, barred, or failing its ID, password or rolling-code check? With the clutch down, does `STAT_P_N_EINGANG` change and `STAT_ANLASSER_AUS_P_N` read 0? If not: the clutch module's power and ground, its pin 4 to EWS pin 8, and the EWS coding `PARK/NEUTRAL_EINGANG`. `STAT_ANLASSER_AUS_ZV`, `_BC` or `_DREHZAHL` at 1 means the car is double-locked, the code function is on, or the EWS sees engine speed. `STAT_ANLASSER_FREIGESCHALTET` at 1 but no crank: the terminal-50 path from the EWS through X6011 pin 1 to the starter, the starter, its cable and the ground strap ([SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/EWS3.md)). An EWS delete in the DME doesn't change any of this: the EWS still controls the starter. Never jumper EWS pins.
   - **Yes:** go to 3.
3. **While cranking, does the DME see engine speed** (`STATUS_MOTORDREHZAHL` above 0, the tachometer moving)?
   - **No:** the crankshaft sensor, its plug and X60003 pins 8 and 21; fault 16 (0x10). Without that signal there's no injection, no spark and no pump hold ([BMW ST055](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)).
   - **Yes:** go to 4.
4. **Is fault 130 (0x82) or 66 (0x42) stored, or does `STAT_EWS3_FREIGABE` read 0?**
   - **Yes:** the DME isn't released. After a delete, confirm the delete took (re-read the DME; ask the vendor); with a virgin DME, the sync failed ([Session 3](#session-3-ews)). BMW describes this as crank-no-start ([BMW ST051](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)). In the 2002 325iT case a "fuel pump relay" fault 1 and all six injectors disabled followed an immobilizer problem ([e46fanatics](https://www.e46fanatics.com/threads/ews-synch-for-s54-swap-into-e46-touring.1318881/)).
   - **Only a leftover 130 (0x82), after a delete the vendor has confirmed:** that alone isn't the cause. A deleted DME can keep 130 stored and still start (step 22; [Session 2](#session-2-dme-vin-ews-delete-and-gearbox-software)). Go to 5.
   - **No:** go to 5.
5. **Did the pump prime at key-on, and is there 5.0 ± 0.2 bar?**
   - **No prime:** [Checks on the pump circuit](#checks-on-the-pump-circuit): X60004 pin 10 to K96, the fuses, K96 swapped with K19, `STEUERN_EKP`, the E-box plugs. A 323i wagon whose M3 plugs had no mates didn't prime ([e46fanatics](https://www.e46fanatics.com/threads/kalims-s54-sedan-swap-warning-pic-heavy.889867/page-39)).
   - **Primes, but low or no pressure:** feed and return swapped at the filter-regulator ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/82513-s54-swap-to-ms42-car-no-start)), the regulator and its vacuum hose, the pump's delivery (at least 1.12 L in 30 s at 12 V, [Fuel system](README.md#fuel-system)), old fuel.
   - **Yes:** go to 6.
6. **Injector faults 3–5 and 31–33 (0x03–0x05, 0x1F–0x21), or "circuit low" on all six?**
   - **Yes:** the injector relay K6327, its E-box fuse, an X6053/X60531 mix ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-fuel-injectors-low-circuit.1277127/)); six equal injector resistances (step 12).
   - **No:** go to 7.
7. **Coil faults 23–25 and 50–52 (0x17–0x19, 0x32–0x34), or no spark?**
   - **Yes:** about 0.8 Ω from terminal 15 to each coil's pin at the DME (BMW, step 11); the X60005 pin 5 ground; a coil harness from the M3 harness only; plugs and boots.
   - **No:** go to 8.
8. **Air and throttle: does `STATUS_ADAPTIONSBLOCK_06` → `STAT_WDK_ADAPT_WERT` read 0, do the throttles follow the pedal, is the idle actuator plugged in (X60003 pins 46 and 47), and are there no throttle (EML) faults?**
   - **No:** clear the adaptations and let the throttles relearn on a cold engine (Session 6). BMW: without it, the car "will not start, or run in 'fail-safe' mode" ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%201%29.pdf)). Then the throttle sensors, pedal and actuator ([MotoIQ](https://motoiq.com/project-e46-m3-part-8-the-dreaded-eml-light/)).
   - **Yes:** the causes are mechanical (timing, compression), not wiring.

![Starts, then dies, and fault 1](diagrams/25-flow-no-start-2.svg)

*Figure 12. Left: what to check when the engine starts and then dies, by how it dies; an immobilizer mismatch shows as crank-no-start instead. Right: how to tell the expected stored pump fault, location 1 (0x01), from a real one, by what the car does.*

**Starts, then dies.** That isn't the immobilizer's signature: BMW describes a mismatch as crank-no-start, and a deleted DME ignores the code. Look at the EWS only if 130 (0x82) or 66 (0x42) is stored, and after a confirmed delete not for a leftover 130 on its own.

- **Dies within about 3 seconds with the EML lamp on, and won't restart:** a throttle fault shutdown. MotoIQ's stock-hardware M3 "would shut itself off in a matter of roughly 3 seconds and not start back up"; the causes they worked through were throttle sensor 1, the pedal, throttle sensor 2, the throttle synchronization and finally the actuator, with low charging voltage suspected along the way ([MotoIQ](https://motoiq.com/project-e46-m3-part-8-the-dreaded-eml-light/)). Read the faults: 118–121 (0x76–0x79) throttle sensors, 60 and 61 (0x3C, 0x3D) pedal, 228–230 (0xE4–0xE6) throttle control.
- **Dies when the prime would end:** the pump isn't being held. The DME needs the engine-speed signal to keep K96 on; check `STAT_EKP_EIN` with the engine running.
- **Dies at idle, no EML lamp:** the idle actuator, leaks at the idle-air pipe, the adaptation, fuel pressure.
- **Runs only with the pump fuse pulled, then floods:** an unseated terminal; in an E36 S54 swap, a ground at X60003 pin 25 ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/112619-s54-only-starts-when-fuel-pump-fuse-is-pulled-did-i-code-it-wrong)). Tug-test.

### Warning lights

Expected states: key on, engine off, the red oil-pressure lamp, the charge lamp and the check-engine lamp are lit. After the start, oil and charge go out within seconds and the check-engine lamp goes out unless a fault asks for it; Tenza's check-engine and oil lamps went out after 10–15 seconds ([Tenza Motorsports – M3 Touring build finally runs (2021), 05:38](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=338s)). DSC and ABS lamps stay on until Session 5. To tell lamp wiring from a real fault, read `STAT_MIL_EIN`: at 0 with the lamp lit, suspect the cluster or its coding; at 1, read `FS_LESEN`.

![Warning lights](diagrams/26-flow-warning-lights.svg)

*Figure 13. Which lamps are expected at key-on and after the start, how to tell lamp wiring from a real fault with `STAT_MIL_EIN` once the engine runs, and, for each lamp or symptom, its likely causes, most likely first, with the first check.*

| Light | Likely causes, most likely first | Check | Documented fix |
|---|---|---|---|
| Check engine | 1. Leak-test circuit: heater 14 (0x0E), valve 27 (0x1B), module 127 (0x7F), after the pin moves or with a three-wire module. 2. SMG software in the DME (SMG bus faults, "MIL request from SMG"). 3. O2 sensors or their heaters, faults 37–40 (0x25–0x28): a wrong or mixed O2 harness. 4. Secondary air, faults 19, 63, 170 and 171 (0x13, 0x3F, 0xAA, 0xAB). 5. Injector circuits (an X6053 mix). 6. Throttle or pedal (the EML lamp too). 7. Misfire | `STAT_MIL_EIN`; `FS_LESEN` with its stored values; the leak-test triangle (step 9); `START_SYSTEMCHECK_DMTL` and `LESEN_SYSTEMCHECK_DMTL`; `STEUERN_SLS_CHECK` | Re-pin the leak test and find the pump by test, not label; manual-gearbox software; the M3 harness's own O2 section ([UNRIVALED – Watch this before you S54 swap (2021), 04:39](https://www.youtube.com/watch?v=eddLff8yba0&t=279s)); the M3's own X6053 halves |
| None, but faults stored | Location 1 (0x01), the pump fault, expected with US software on K96; possibly 130 (0x82) after an EWS delete; 110 (0x6E) if the Sport LED isn't wired | `FS_LESEN`, and confirm `STAT_MIL_EIN` = 0 | Leave the pump fault (it doesn't light the lamp, per two swappers), or fit the pump module; 130 per your vendor; wire X60004 pin 16 |
| Oil pressure (red) | Out at key-on: the pin-11 wire is missing or on the wrong cluster pin, or the cluster expects oil pressure over CAN. On while running: low oil pressure, or the lamp wire grounded | The key-on lamp; steps 3 and 4; a mechanical gauge | Wire X60004 pin 11 to cluster pin 13 and code `CAN_OELDRUCKSCHALTER` to `nicht_aktiv` (an MS45.1 ZHP, [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)); an MS43 325iT joined the signal to the cluster wire ([e46fanatics](https://www.e46fanatics.com/threads/battery-and-oil-pressure-lights-inop.1207433/)) |
| Charge | Out at key-on: the pin-1 wire, or `GENERATOR_UEBER_CAN`. On while running: alternator, belt, the terminal-61 wire to X60003 pin 13, low voltage | The key-on lamp; `STATUS_UBATT` running | The 325iT owner restored his lamp in 15 minutes once he understood the circuit (same thread) |
| Oil level (yellow) | The pin-21 wire to cluster pin 17, or `TOG_UEBER_CAN`; the sensor itself, fault 44 (0x2C) | `STATUS_OEL_TEMPERATUR` reads plausibly (the sensor is alive) | Wire 21 to 17 |
| EML | Throttle sensor 1 or 2, the pedal, throttle synchronization, the actuator; low charging voltage; adaptation not done | Faults 118–121 (0x76–0x79), 60 and 61 (0x3C, 0x3D), 111 and 112 (0x6F, 0x70), 228–230 (0xE4–0xE6); `STAT_WDK_ADAPT_WERT` | MotoIQ: sensors, two synchronizations, then a new actuator ([MotoIQ](https://motoiq.com/project-e46-m3-part-8-the-dreaded-eml-light/)); the adaptation reset (Session 6) |
| ABS, DSC, brake | 1. VIN not initialized (5EF1, 5E1F) until the cluster carries your VIN. 2. Wheel-speed sensors: an MK20 donor's don't fit. 3. Steering angle not calibrated. 4. An M3 MK60 that won't accept the Touring. 5. The yellow brake lamp: the brake test-contact wire still on pin 28 | INPA's DSC fault memory and wheel speeds | Session 5; your own sensors ([Wheel-speed and pad-wear sensors](#wheel-speed-and-pad-wear-sensors)); refit your Touring's MK60 ([e46fanatics](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/)); move 28 to 34 |
| Cruise won't engage | 1. Not the M3 clutch module. 2. Gear switch missing or open. 3. Brake contacts implausible, fault 106 (0x6A). 4. SMG software. 5. Steering-wheel data line, fault 81 (0x51) | `STAT_KRAFTSCHLUSS_EIN` in gear; `STAT_BLS_EIN`, `STAT_BLTS_EIN`; `STAT_MFL1_EIN`…; faults 80 (0x50), 106 (0x6A), 139 (0x8B), 194 (0xC2) | A new M3 clutch module (an S54 wagon, [e46fanatics](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/); a ZHP, [NAM3](https://nam3forum.com/forums/forum/main-forum/member-build-journals/3768-what-s-going-on-in-my-shop-currently/page3)); fit the gear switch: a 5-speed 323i never got cruise without one ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)) |
| Airbag | A seat swap (belt tensioners, occupancy mat), the steering wheel's slip-ring plugs | INPA's airbag fault memory | Matching tensioners and plugs; clear the codes. Never bypass it: its crash message starts the DME's fuel-pump cut-off, which is unverified with the K96 relay ([Crash fuel cut-off](#crash-fuel-cut-off)) |
| Gearbox or SMG lamp; tamper dot | SMG software; the cluster and light module not re-coded after a vehicle-order change; the cluster's VIN or mileage not matching the light module's | The DME's software; the cluster coding | Manual software (Session 2); code AKMB and ALSZ ([50sKid – Code the vehicle order (2017), 26:05](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1565s)); Session 4 |
| "Check filler cap" | The cap not sealing; a leak found after refueling | `LESEN_SYSTEMCHECK_DMTL`; fault 181 (0xB5) | The cap and its seal; a smoke test with the vent closed, under 0.1 bar ([BMW TechDrive](https://automotivetechinfo.com/wp-content/uploads/2008/02/What-If-It-Is-Not-The-Gas-Cap.pdf)) |

**Other cluster symptoms:**

| Symptom | Likely cause | Check |
|---|---|---|
| Many lamps lit after the first start | Expected until the cluster, light module and DSC are coded | ([ShopLifeTV – Starting the S54 swap car for the first time (2015), 05:45](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=345s)) |
| Tamper dot | The cluster's VIN differs from the light module's, or the light module's mileage is higher | [Session 4](#session-4-cluster-and-light-module) ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/228697-cluster-replacement)); one swapped Touring was left with it ([ThaChileanDude – E46 M3 wagon in 10 days (2024), 35:19](https://www.youtube.com/watch?v=iSgClonTiQg&t=2119s)) |
| DSC and parking-brake lamps yellow | VIN mismatch with the cluster | Session 4 ([e46fanatics](https://www.e46fanatics.com/threads/e46-m3-cluster-coding.1278842/)) |
| Parking-brake lamp always on | Seen once on a 1998 323i (MK20 ASC) with an M3 cluster, cause not found; it worked in a 2001 325iT | The switch on cluster pin 23 and DSC pin 27 ([e46fanatics](https://www.e46fanatics.com/threads/s54-swap-wiring-information.1003871/)) |
| Tach needle stuck at 9,000 rpm after coding | A blank coding file written to a cluster whose coding index was changed | Write back the EEPROM backup ([e46fanatics](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)) |
| No cluster backlight | A cluster from before 09/2002 in a car built from 09/2002 | Backlight wire to cluster pin 7 ([Cluster wiring](#cluster-wiring)) |
| No rear-door warnings | M3 clusters have no rear-door LEDs | Solder them in, or use a cluster service |
| Speedometer about 9% high | The M3 cluster's built-in correction table | Check against GPS ([e46fanatics](https://www.e46fanatics.com/threads/diy-e46-cluster-gauges-definitions.1324535/)) |
| Fuel gauge or range wrong | The tank curve or a sender | `STATUS_TANKINHALT_LESEN` against a measured fill ([Fuel gauge and tank senders](#fuel-gauge-and-tank-senders)) |

### DSC, ABS and steering angle

| Symptom | Likely cause | Check |
|---|---|---|
| DSC lamp; 5EF1 or 5E1F "VIN not initialized" | The cluster's VIN doesn't match yet, or the DSC's VIN and steering angle aren't initialized | [Session 5](#session-5-dsc-coding-and-vin) ([50sKid (2016), 32:47](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=1967s)) |
| 5EF1 never clears with an M3 MK60 | The M3 unit won't accept the Touring | Refit your Touring's MK60 ([e46fanatics](https://www.e46fanatics.com/threads/m3-cluster-swap-dsc-light.1260275/)) |
| NCS doesn't list MK60, or "Codierindex … nicht zulässig" | The production date in the vehicle order is too early for the unit, or the unit's coding index | #0902 or later for the session; check the coding index ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/173720-mk60-vin-issue-m3-track-mode-rabbit-hole), [e46fanatics](https://www.e46fanatics.com/threads/ncs-expert-coding-is-faulty-resolved-8-12-21.1293250/)) |
| ABS lamp after the first drive | Wheel-speed sensors that don't suit the harness: an MK20 donor's are a different type | Read the DSC fault memory and the four wheel speeds; the wheel-speed faults are listed in English on [NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/167185-mk-60-fault-codes-in-english) ([Wheel-speed and pad-wear sensors](#wheel-speed-and-pad-wear-sensors)) |
| No Shift+F4 steering-angle page in INPA | Some INPA builds lack it | Tool32 or another INPA build ([Session 7](#session-7-steering-angle-after-the-alignment)) |
| INPA can't connect to the DSC at all | INPA build or setup | A generic scan tool for the steering angle ([LM Auto Repairs (2016), 06:23](https://www.youtube.com/watch?v=1dn4c3g6dsA&t=383s)) |
| Tool32 IFH-0009 on the steering-angle job | A swapped sensor that was never coded | Code it with NCS Expert, then retry |
| Steering angle stuck at "!1440", or 5E43 "internal" that returns after calibration | A failed sensor | Replace it and calibrate the new one ([e46fanatics](https://www.e46fanatics.com/threads/calibrating-steering-angle-with-inpa.1287151/), [Earl Moorhead (2023), 26:24](https://www.youtube.com/watch?v=2mqz14tWpMI&t=1584s)) |
| Spongy pedal after a DSC change | Air in the hydraulic unit | INPA pump bleed with a firm pedal, then a conventional bleed (Session 5) |

### Driving, emissions and comfort

| Symptom | Likely cause | Check |
|---|---|---|
| Cruise won't engage | See the warning-light table | `STATUS_DIGITAL` bits in gear; fault 80 (0x50). On a non-S54 E46 race car a "plausibility signal brake light switch" fault stopped cruise ([Tenza Motorsports – E46 cruise control stalk wiring (2025), 14:15](https://www.youtube.com/watch?v=8uRGM-OzqWs&t=855s)) |
| Revs hang between shifts, idle hunts on clutch-in, or stalls | Clutch-chain wiring first ("the most common rev hang is from improper clutch switch wiring"), the wrong clutch module, then SMG software in the DME, then a third-party tune. The chain enables the idle control, and a ZHP's intermittent stalling stopped with the M3 module | `STAT_KUP_EIN` and `STAT_KRAFTSCHLUSS_EIN` in gear; fault 80 (0x50) ([e46fanatics](https://www.e46fanatics.com/threads/manual-swap-rev-hang.1315205/), [NAM3](https://nam3forum.com/forums/forum/main-forum/member-build-journals/3768-what-s-going-on-in-my-shop-currently/page3)) |
| Limp mode after an SMG donor's DME was "coded" | The software still thinks it's an SMG car | Manual software (Session 2) ([UNRIVALED (2021), 02:02](https://www.youtube.com/watch?v=eddLff8yba0&t=122s)) |
| Sport works but its LED doesn't | The pin-16 circuit; fault 110 (0x6E) | Continuity from X1869 pin 18 to X60004 pin 16 ([Tenza Motorsports (2021), 06:28](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=388s)) |
| Switch center works only sometimes, or not at all | Missing feeds (F42, F12) or K-bus | [Sport button and switch center](#sport-button-and-switch-center) |
| EVAP monitor never ready; P2418 | Leak-test wiring, hoses, filler cap, the fuel gauge, or the test conditions | [When a monitor won't complete](#when-a-monitor-wont-complete) |
| Secondary-air monitor never ready | Pump relay or valve, pre-cat O2 response, cold-start temperature | Same section |
| A/C won't engage | The cluster not passing the request, then the chain from the climate control through the DME (X60004 pin 29) to relay K19 and 12 V at the compressor clutch | `STAT_AC_EIN`, `STAT_KO_EIN`, `STEUERN_KO`. A dead compressor clutch was the cause in one E46 (an N42 318i) ([e46fanatics](https://www.e46fanatics.com/threads/a-c-compressor-not-engaging.1278940/)) |
| Cooling system hard to bleed; heater odd | The M3 valve's pump isn't wired | [Heater valve and auxiliary water pump](#heater-valve-and-auxiliary-water-pump) |
| Coolant-level or washer warning | A sensor lead not extended or connected | [Sensor leads that may not reach](#sensor-leads-that-may-not-reach) |

### Tools and coding

| Symptom | Likely cause | Check |
|---|---|---|
| INPA shows empty circles | Cable not connected, COM port and `obd.ini` don't match, or ignition off | [Cable and EDIABAS settings](#cable-and-ediabas-settings) |
| The DME answers but the cluster, light module and DSC don't | Pins 7 and 8 not bridged | Flip the cable's switch or solder the pads ([NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/293965-verify-ncsexpert-function-before-doing-manual-swap)) |
| INPA's battery and ignition indicators flicker | Latency timer at 16 | Set it to 1 ([BMW Doctor (2024), 03:36](https://www.youtube.com/watch?v=2Oebra7Kbn0&t=216s)) |
| NCS Expert "IFH-0009" while INPA works | NCS Expert 4.x, or the wrong module chosen to read the vehicle order | Try version 3.0.x; read from AKMB, or EWS on an older car ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/204464-help-with-coding-issues-re-ncs-and-pasoft)) |
| Code Car stops partway | It stops at the first module that fails | Code the remaining modules one at a time ([50sKid (2017), 17:15](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1035s)) |
| COAPI-2060 when coding the GM5 | A loose pin in its plug | Reseat the plug ([NAM3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/21981-ncs-error-while-trying-to-recode-used-gm5-module)) |
