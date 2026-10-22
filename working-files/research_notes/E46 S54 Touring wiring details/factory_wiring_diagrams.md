# Factory wiring diagrams: S54 into a US E46 325i Touring

Research date: 22 Oct 2026. Scope: E46 only.

- **Receiving car:** US 325i Touring, M54B25, 5-speed manual. It has an MS43 DME until about 02–03/2003 and an MS45.1 after that.
- **Donor:** US E46 M3 (S54) with an MSS54 DME. WDS splits the MSS54 drawings at 2001_09, 2004_03 and 2004_09. WDS never uses the name "MSS54HP".

**Reading key.**
- **[read]**: I read the page or drawing myself in this session. WDS drawings were read both as SVG text and as rendered images.
- **[snippet]**: seen only in a search-result snippet.
- **[earlier]**: taken from an earlier project note and not re-read now.
- **Inference**: my own reasoning; no source says it.
- WDS dates such as 2001_09 mean "production from September 2001".

**Wire codes.** Colours use BMW's German codes:

| Code | Colour | Code | Colour |
|---|---|---|---|
| BL | blue | OR | orange |
| BR | brown | RS | pink |
| GE | yellow | RT | red |
| GN | green | SW | black |
| GR | grey | VI | violet |
| | | WS | white |

"BR/GN" means brown with a green tracer. Sizes are in mm². Signal names (S_OLD, DMTLH and so on) are WDS's own.

**Where the WDS pages are.** Every "SP…" drawing is on the WDS mirror at `https://wds.psjr.org/en/e46/svg/<ID>.svg`, for example [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg). Pin tables, connector views and locations are at `https://wds.psjr.org/en/e46/zinfo/E46_<page>.htm`:
- PA = pin assignment, e.g. [E46_PA6000L](https://wds.psjr.org/en/e46/zinfo/E46_PA6000L.htm)
- SX = connector view
- EX = location

**DME labels used throughout:**

| Label | Meaning |
|---|---|
| **MS43-US** | US 325i (sedan or Touring) M54B25, manual, Siemens MS43. WDS splits it at 2001_03 (clutch switch becomes clutch module) and at 2001_09 (heated DM-TL). |
| **MS45.1-325i** | US 325i M54B25 from 03/2003. ETK calls this DME MS45.1; WDS calls the whole family "MS45". |
| **MS45-WDS** | What WDS's MS45 module drawing and pin tables show. They are drawn for the **M56 SULEV** 325i (2.5-litre, automatic only in the US), not for the M54 manual car. Corrections are given where needed. |
| **MSS54-US** | US M3. The baseline in the tables is **MSS54 2001_09–2004_03**; other dates are noted. |
| 3.0-litre | Data from the 330i, ZHP or X3 are always marked as 3.0-litre. |

---

## Takeaway

- **Source.** BMW's own wiring system (WDS) for the E46 can be read publicly on an unofficial mirror, wds.psjr.org. It covers MS43, MS45 and MSS54, with:
  - module pin drawings;
  - dated pin tables;
  - drawings of the plugs in the electronics box (E-box);
  - connector face views and locations.

  It answers nearly every pin question here with factory data. The official route is BMW AOS (ISTA/AIR) at bmwtechinfo.bmwgroup.com, which is paid ($32 for one day). Bentley was not readable.
- **US 2.5-litre DME name.** ETK labels the US 325i Touring's M54 DME from Mar '03 **"MS45.1"**, so the name is not limited to the 3.0-litre ZHP. WDS's "MS45" pin tables describe the M56 SULEV car:
  - local CAN on pins 31/35;
  - EAC sensor on pin 25;
  - pins 10 and 23 "not used".

  WDS's own M54 drawings in the same tree put the **pump relay on X60004-10 and the clutch on X60004-23**, as on the MS43.
- **X60004 is half the same.** 20 of the 40 X60004 pins (pins 3, 4, 7–9, 12–14, 17, 22, 24, 26, 27, 29, 32, 33 and 36–39) carry the same signal, wire colour and size on MS43, MS45 and MSS54, and pin 40 is empty on all three. The pins that differ are:
  - 1, 2, 5, 6, 11, 15, 16, 18, 19, 21 and 23;
  - the brake test contact (28 → 34);
  - the DM-TL leak-check pins (20/30 by name only; see the DM-TL bullet below);
  - 10 on a US M3;
  - 25, 31 and 35 on the M56 only.
- **MS43 Touring: the wires are already there.** The cluster and start-feedback wires that the M3 takes at X60004-1/2/11/21 already exist in the Touring's body harness. They end at body plug **X6011 pins 4, 6, 3 and 5**, with exactly the M3's colours and sizes.
  - Re-pin X6011-3 → X60004-11, -4 → -1, -5 → -21 and **-6 → -2** (X6011-6 is the "30h" start feedback, *not* terminal 50).
  - From 09/2001, re-pin X6011-7 (DM-TL heater) → X60004-18.
  - That frees **body X6011-7**, which is exactly where the M3 sends the **clutch signal** into the engine harness (clutch module → X6011-7 → X6053-5 → gear switch → X60002-20). So the Touring's clutch wire moves from X60004-23 to body X6011-7.
- **MS45.1 Touring.**
  - X6011 has only pins 1–2.
  - The DM-TL heater is on X60004-2 and moves to 18.
  - X60004-5/15 carry the **secondary-air air-mass sensor**. ETK lists that sensor on the US 325i Touring from Mar '03. These wires must come out, because the MSS54 uses pin 5 as a ground and pin 15 as the Sport input.
  - Pin 19 is the E-box fan, on cars that have one.
  - The oil-pressure, charge and oil-level lamps work over CAN on the MS45, so hard-wiring them to the cluster needs new wires to cluster pins 2, 13 and 17.
- **MSS54 X60004-5 is a real ground** (0.35 BR/SW to ground X1108 under the driver's seat) on every M3 version in WDS.
  - X60004-6 is a terminal-50 input (SW/BL).
  - Pins 1 and 2 disappear from the from-2004_03 drawing, where the charge lamp runs over CAN. The pin tables still list them.
- **DM-TL (the US leak-check pump).**
  - Every heated-module drawing (MS43, MS45, MSS54) wires X60004-20 to module pin 1 and X60004-30 to module pin 3. All but one show 0.75 BR/BL on 20 and 0.5 SW/GN on 30; the exception is the MS43 module-4 drawing SP0000017224, which reverses the colours. So **on the drawings, the MS45 harness needs no 20/30 swap**.
  - Only the pin-table labels disagree: MSS54 and MS43 say "20 valve, 30 pump"; MS45 says "20 pump, 30 valve".
  - Forum practice says to swap 20/30 on MS45 cars, and one builder who swapped still had P2418.
  - Settle it on the car (method in D12).
- **Fuel pump.**
  - The US M3 drives its pump module (WDS still calls it "K96 fuel pump relay 1", but with a different plug, X10157, and a ground pin) from **X60002-11 via X6021-1**.
  - X60004-10 on a US M3 is "not used" (Euro-only).
  - The Touring's K96 relay hangs on X60004-10 on both MS43 and MS45 (M54).
- **CAN and OBD.**
  - WDS draws no CAN terminating resistors. BMW training says the 120 Ω resistors sit in the DSC unit and in either the cluster or the DME, giving 60 Ω across the bus.
  - The OBD socket has no CAN on pins 6/14. DME diagnosis is on pin 7 (TXD II) and body diagnosis on pin 8.
- **Still open:**
  - WDS connector views don't say whether you are looking at the wire side or the mating side.
  - No source maps terminal part numbers to X60004/X6011 cavities.
  - X6011/X6021 housing part numbers were not found.
  - DM-TL 20/30 (above).
  - Pin X6011-6 on MS45 cars: two WDS drawings disagree.
  - A few colour conflicts inside WDS.

### Corrections to sibling notes in this folder

- `swap_repin_practice.md` maps body **X6011-6 → X60004-6**. Per WDS:
  - X6011-6 is S_30H, the start feedback (0.35 SW/GN from splice X276 to cluster pin 3 and the E-box fan). Its M3 home is **X60004-2**.
  - The M3's X60004-6 is a separate terminal-50 signal (0.35 SW/BL from X18820).
- That file's "MS45.1: swap 20↔30" conflicts with the factory drawings, which show identical DM-TL wiring on the MS45 and the M3. Treat it as unproven until tested.
- That file's "X60004-5: none / not needed": WDS shows a real ground wire on every M3. Fitting one costs one wire; whether it matters was not shown by any source.

---

## Q1. Where the factory diagrams can be read

### Cited findings

- **BMW AOS (official, paid).** [bmwtechinfo.bmwgroup.com](https://bmwtechinfo.bmwgroup.com/) [read].
  - It is the US/Canada portal; other markets use aos.bmwgroup.com.
  - Subscriptions give access to ISTA (VIN-based diagnosis, wiring diagrams and repair) and AIR (repair information and wiring diagrams).
  - Listed prices: **$32 for 1 day, $270 for 1 month, $2,700 for 1 year**.
  - [System requirements PDF](https://bmwtechinfo.bmwgroup.com/assets/system_requirements.pdf) [read].
  - Not used, because it needs payment and a login.
- **WDS mirror (BMW content on an unofficial host).** [wds.psjr.org/en/e46/](https://wds.psjr.org/en/e46/) [read]. It is a public copy of BMW's Wiring Diagram System; a US-English copy is under `/us/`. It has:
  - system drawings by DME family under *Complete vehicle → Drive → Engine management MS43 / MS45 / MSS54*;
  - per-DME component pages with dated pin tables;
  - "A6000 module 1–5" pin drawings;
  - E-box plug drawings;
  - connector views (SX) and locations (EX).

  Drawing titles carry conditions such as `M3_S54_COUPE or M3_S54_CONV`, `USA_LHD`, `(Saloon or Compact or Touring)` and dates. For example, the electric-fan drawing [SP0000019629](https://wds.psjr.org/en/e46/svg/SP0000019629.svg) is "(Saloon or Compact or Touring) as of 2003_03", and [SP0000019630](https://wds.psjr.org/en/e46/svg/SP0000019630.svg) is "(Coupe or convertible)". There is no VIN filter, so you pick the variant by date and options yourself.

  Pin-table validity, as linked from the WDS component pages [read]:

  | DME | Page | Valid for |
  |---|---|---|
  | MSS54 | [PA6000G](https://wds.psjr.org/en/e46/zinfo/E46_PA6000G.htm) | without SMG, up to 2001_09 |
  | MSS54 | [PA6000L](https://wds.psjr.org/en/e46/zinfo/E46_PA6000L.htm) | without SMG, 2001_09 up to 2004_09 |
  | MSS54 | [PA6000R](https://wds.psjr.org/en/e46/zinfo/E46_PA6000R.htm) | without SMG, from 2004_09 |
  | MSS54 | H / M / S | the same three periods with SMG |
  | MSS54 | T | CSL |
  | MS43 | [PA6000E](https://wds.psjr.org/en/e46/zinfo/E46_PA6000E.htm) | without automatic, up to 2001_09 |
  | MS43 | [PA6000J](https://wds.psjr.org/en/e46/zinfo/E46_PA6000J.htm) | without automatic, from 2001_09 |
  | MS43 | F / K | automatic |
  | MS45 | [PA6000O](https://wds.psjr.org/en/e46/zinfo/E46_PA6000O.htm) | 2002_09 up to 2003_03 |
  | MS45 | [PA6000P](https://wds.psjr.org/en/e46/zinfo/E46_PA6000P.htm) | from 2003_03 |

- **Sites that blocked me.** newTIS (newtis.info) returned a Cloudflare challenge (HTTP 403), so I stopped. bmwteka: connection failed.
- **Bentley**, *BMW 3 Series (E46) Service Manual 1999–2005*. Marketplace listings say it covers the M3 and the Sport Wagon and has an electrical wiring diagram section [snippet]. The [Turner product page](https://www.turnermotorsport.com/p-4102-e46-3-series-bentley-service-manual/) returned 403 and bentleypublishers.com did not resolve. Content not read.
- **BMW training (archive.org "BMWTechnicalTrainingDocuments")** [read]. These cover conventions, buses and connector tools; they give no pin data for these cars.
  - [ST052 E46 Power Supply and Bus Systems](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03a_E46%20Power%20Supply%20and%20Bus%20Systems.pdf)
  - [ST052 E46 Driver Information Systems](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03b_E46%20Driver%20Information%20Systems.pdf)
  - [ST040 Bus System Troubleshooting](https://archive.org/download/BMWTechnicalTrainingDocuments/ST040%202001%20System%20Diagnosis/9%20Bus%20System%20Troubleshooting.pdf)
  - [ST051 Wiring Diagrams and Associated Documents](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I/02_Wiring%20Diagrams%20and%20Associated%20Documents.pdf)
  - [ST051 Archive 1 Breakout Boxes & Connectors](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/03%20Breakout%20Boxes%20%26%20Connectors.pdf)
- **Community copies of WDS data.**
  - The project's pinout workbook ([Google Sheet](https://docs.google.com/spreadsheets/d/1I_2XAvziPCiRlZXnkfk4x1tUIKy4TKPbmdJcGCBdGIg/edit), read from its XLSX export) [read]. Its tables are WDS PA tables. Its two embedded drawings are WDS **SP0000017224** (MS43 module 4) and **SP0000018609** (MS45 module 4).
  - [ms4x.net MS43 pinout](https://www.ms4x.net/index.php?title=Siemens_MS43_Pinout) [read]: a multi-chassis MS43 table that agrees with SP0000017224.
- **ETK** at [bmwfans.info](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/) [read]: DME, housing, terminal and component part numbers.
- **Diagnostic job lists** (EDIABAS docs on GitHub) [read], used here to verify wiring with actuator tests:
  - [MSS54DS0](https://raw.githubusercontent.com/emdzej/ediabasx-docs-sgbd/main/docs/sgbd/MSS54DS0.md)
  - [MS450DS0](https://raw.githubusercontent.com/emdzej/ediabasx-docs-sgbd/main/docs/sgbd/MS450DS0.md)
  - [MS430DS0](https://raw.githubusercontent.com/emdzej/ediabasx-docs-sgbd/main/docs/sgbd/MS430DS0.md)

### Inferences

- WDS answers the pin questions with BMW's own drawings and covers both US M3 and US 325i Touring conditions. Its weak points:
  - no VIN filter;
  - views that don't state the viewing side;
  - a few colour or size disagreements between drawings (each listed under Gaps);
  - MS45 tables written for the M56.
- Before cutting wires, an ISTA lookup by the Touring's VIN is the only way to confirm its exact harness. A one-day AOS subscription would cover it. I did not use it.

### Gaps

- Bentley's ETM and ISTA were not read. newTIS and bmwteka were blocked or unreachable.

---

## Q2. X60004 full pinout per DME; MS45 or MS45.1 on the US 2.5-litre

### Cited findings

**MSS54-US module 4 drawings** [read]: [SP0000014295](https://wds.psjr.org/en/e46/svg/SP0000014295.svg) (to 2001_09), [SP0000017646](https://wds.psjr.org/en/e46/svg/SP0000017646.svg) (2001_09–2004_03) and [SP0000020984](https://wds.psjr.org/en/e46/svg/SP0000020984.svg) (from 2004_03). Pin tables PA G, L and R [read]. Full table in D1.
- **Pin 5:** "31E<2 0.35 BR/SW → X1108" on all three drawings. X1108 is a ground point "under carpet of driver's seat" ([EX1108A](https://wds.psjr.org/en/e46/zinfo/E46_EX1108A.htm)) [read]. PA L/R: "5 M Ground — Ground point".
- **Pin 6:** "S_50 0.35 SW/BL ← X18820". PA L/R: "Signal, terminal 50, ignition lock".
- **Pin 10:** "S_EKP 0.35 SW/VI → K96 X10156-4" under condition J27 "EUR". The USA branch is "J40 not used". PA L: "Fuel pump relay 1 not USA".
- **DM-TL pins:**
  - To 2001_09: 28 DMTLP 0.5 SW/GN and 30 DMTL 0.75 BR/BL.
  - From 2001_09: 18 DMTLH 0.75 SW/RT, 20 DMTL 0.75 BR/BL and 30 DMTLP 0.5 SW/GN, all on a USA branch (EUR: "not used").
  - I checked the 2001_09 drawing visually: pin 18 → module X17140-2, pin 20 → X17140-1, pin 30 → X17140-3.
- **From 2004_03,** pins 1 (S_61--1) and 2 (S_30H) are not drawn. The from-2004_03 alternator drawing [SP0000021003](https://wds.psjr.org/en/e46/svg/SP0000021003.svg) [read] sends the charge lamp from the alternator → X60003-13 → DME → CAN → cluster X11175-9/10. PA R (from 2004_09) still lists pins 1 and 2.
- **PA tables leave out pass-through pins** that the drawings do wire. Example: X60003-12 (S_30H in) and X60003-19 (tyre-pressure reset) are listed as "not used".

**MS43-US module 4 drawings** [read]:
- [SP0000014303](https://wds.psjr.org/en/e46/svg/SP0000014303.svg) (2000_06–2001_03)
- [SP0000016113](https://wds.psjr.org/en/e46/svg/SP0000016113.svg) (2001_03–2001_09)
- [SP0000017224](https://wds.psjr.org/en/e46/svg/SP0000017224.svg) (from 2001_09, with DM-TL, i.e. USA)
- [SP0000017227](https://wds.psjr.org/en/e46/svg/SP0000017227.svg) (the same period without DM-TL)

Pin tables PA E and J [read]:
- **Unused on a manual MS43:** 1, 2, 5, 6, 11, 15, 16, 19, 21, 25, 31, 34, 35, 40.
- **Pin 18** is "Valve, exhaust flap M54 3.0 l only", i.e. 330i. A 325i has nothing there.
- **Pin 23** is the clutch switch. **Pin 28** is the brake light switch (test contact).
- **From 2001_09:** pin 20 is "Activation, valve for fuel tank leak diagnosis module USA only" and pin 30 is "Activation, pump … USA only".

**MS45-WDS** [read]: module 4 drawing [SP0000018609](https://wds.psjr.org/en/e46/svg/SP0000018609.svg) and pin tables PA O/P.
- **Not used:** 1, 6, 10, 11, 16, 18, 21, 23, 34.
- **Pin 2:** DM-TL heater.
- **Pins 5 and 15:** secondary-air air-mass sensor.
- **Pin 19:** E-box fan.
- **Pins 20/30:** "pump" / "valve".
- **Pin 25:** EAC sensor (PA P only).
- **Pins 31/35:** "Local CAN-bus … Control unit for electronically controlled fuel pump".

The EAC sensor and the CAN-controlled pump are M56 SULEV parts. WDS has an "EAC sensor … (M56 Engine)" drawing, [SP0000020740](https://wds.psjr.org/en/e46/svg/SP0000020740.svg), and "Fuel supply, local CAN bus … (325i_M56_SAL or 325i_M56_TOUR or 325Ci_M56_COUPE)", [SP0000018268](https://wds.psjr.org/en/e46/svg/SP0000018268.svg) [read].

The same MS45 tree links two M54-specific drawings [read]:
- "Fuel pump (M54 engine)" = [SP0000014336](https://wds.psjr.org/en/e46/svg/SP0000014336.svg): K96 X10156-4 ← S_EKP 0.35 SW/VI ← X60004-10.
- "Clutch switch module" = [SP0000016193](https://wds.psjr.org/en/e46/svg/SP0000016193.svg): X60004-23 S_KUP 0.35 BL/BR ↔ X13635-2.

**MS45 or MS45.1 on the US 2.5-litre.** ETK, US 325i Touring M54, "Programmed DME control unit" [read] ([page](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/programmed_dme_control_unit_2/)):

| Part number | ETK text |
|---|---|
| 12 14 7 561 526 | "MS45.1 from Mar '03 to Jul '04" |
| 12 14 7 561 528 | "MS45.1 from Jul '04 to Sep '05" |
| 12 14 7 562 340 | "MS45.1 from Sep '05" |
| 12 14 7 561 532 / 12 14 7 562 342 | automatic |

- ETK, US 325i Touring **M56**: 12 14 7 577 220 "MS45.1 to Sep '05" and 12 14 7 562 346 "MS45.1 from Sep '05" [read] ([page](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M56/L-N/browse/engine_electrical_system/programmed_dme_control_unit/)).
- The basic-unit page lists the MS43 units ("MS43/ FLASH") up to Mar '03 [read] ([page](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/basic_cotrol_unit_dme/)).

**Workbook** [read]: its "MS45.1 X3ZHP" tab is an M54 layout:
- 10 pump relay;
- 23 clutch;
- 18 exhaust flap marked 3.0;
- 5/15 secondary-air sensor marked "3.0 USA".

It is a **3.0-litre (X3 / 330i ZHP)** table, not a 325i table.

### Inferences

- **The answer:** the US 325i Touring from 03/2003 uses an **MS45.1** (per ETK). WDS's "MS45" is that family. For the M54 manual Touring, build the X60004 from the MS45 module drawing **plus** the M54 function drawings:
  - 10 → K96 relay;
  - 23 → clutch module;
  - 5/15 → secondary-air air-mass sensor (fitted from 03/2003; see Q6);
  - 25, 31 and 35 empty (M56 only);
  - 18 empty (3.0-litre only);
  - 19 only if an E-box fan is fitted.
- The M54 MS45.1 in a 325i and in a 330i/ZHP should share these pins, apart from 3.0-litre-only items such as the exhaust flap (inference).

### Gaps

- The mirror has no WDS module-4 drawing for the M54 MS45.1 manual car. The column in D1 is assembled from function drawings.
- Colour conflicts inside WDS:
  - X60004-26 is GN/VI on every module drawing, but the MS43 supply drawings print GN/SW.
  - MS43 pins 20/30 are 0.5 SW/GN / 0.75 BR/BL on [SP0000017224](https://wds.psjr.org/en/e46/svg/SP0000017224.svg) but 0.75 BR/BL / 0.5 SW/GN on [SP0000017277](https://wds.psjr.org/en/e46/svg/SP0000017277.svg) (see D8.2).

---

## Q3. X6011, X6021, X6053/X60531, X6054/X60541 and the B+ plugs

### Cited findings

**Locations (WDS EX pages)** [read]:

| Plug | WDS description | Location |
|---|---|---|
| X6011 | 8-pin black, "Engine plug I" | "in electronics box in water box left" ([EX6021B](https://wds.psjr.org/en/e46/zinfo/E46_EX6021B.htm)) and "rear LH side of engine compartment" ([EX6011C](https://wds.psjr.org/en/e46/zinfo/E46_EX6011C.htm)) |
| X6021 | 4-pin black, "Engine plug" | same two pages as X6011 |
| X6053 | 8-pin natural, "Plug connector, engine wiring harness I" | "in electronics box in water box left" ([EX6053D](https://wds.psjr.org/en/e46/zinfo/E46_EX6053D.htm)) |
| X6054 | 2-pin natural | same page as X6053 |
| X64101 / X64102 | 2-pin black, "Connector, B+ distribution" | "rear LH side of engine compartment" ([EX64101C](https://wds.psjr.org/en/e46/zinfo/E46_EX64101C.htm)) |
| X60004 / X60005 | DME plugs | "rear LH side of engine compartment" ([EX60004C](https://wds.psjr.org/en/e46/zinfo/E46_EX60004C.htm)) |

**X6011** [read]. Contents in D2.

| DME | Drawing |
|---|---|
| MSS54 | [SP0000014314](https://wds.psjr.org/en/e46/svg/SP0000014314.svg) |
| MS43 to 2001_09 | [SP0000014318](https://wds.psjr.org/en/e46/svg/SP0000014318.svg) |
| MS43 from 2001_09 | [SP0000017260](https://wds.psjr.org/en/e46/svg/SP0000017260.svg) |
| MS45 | [SP0000018632](https://wds.psjr.org/en/e46/svg/SP0000018632.svg) |

- **MS43 pins 4–6** are: 4 charge lamp (S_61--1, body 0.35 BL ↔ engine 0.75 BL → alternator X6524-2); 5 oil level (F_OLN); 6 **30h start feedback** (S_30H, body 0.35 SW/GN from splice X276 ↔ engine 0.75 SW/GE → starter X6511).
- **Pin 7:**
  - On the MS43 from 2001_09 it is the DM-TL heater, USA only (body 0.75 SW/RT from DM-TL X1714-2 ↔ engine 0.75 SW/RT → X60003-51).
  - On the **M3** it is the **clutch crossing**: body KUPPL 0.35 GR from clutch module X13635-2 (or switch S32 before 2001_03) ↔ engine S_GANG 0.5 GR → X6053-5.
- **MS45:** pins 1 and 2 only.
- The MSS54 and MS43 drawings use the same plug ID and the same "8-pin black" description.

**X6011-6 on MS45 cars.** [SP0000014365](https://wds.psjr.org/en/e46/svg/SP0000014365.svg), titled "Starter (DME MS43 or DME MS45)" [read], routes S_30H from starter X6511 through X6011-6 to X276 (cluster X11175-3 and E-box fan X6506-2). For MS45 cars this contradicts SP0000018632.

**Clutch and gear-switch chain** (M3, [SP0000016194](https://wds.psjr.org/en/e46/svg/SP0000016194.svg), "Clutch switch module, gear recognition switch (MSS54 as of 2001_03)") [read]:
- X13635-2 KUPPL 0.35 GR → X6011-7 → X6053-5 → S_GANG 0.5 GR → gear recognition switch S5271 X5271-1.
- X5271-2 → S_GANG 0.5 GR/BL → **X60002-20**.
- PA L: "X60002-20 Signal Switch, gear recognition".

**X6021** [read]: MSS54 [SP0000014315](https://wds.psjr.org/en/e46/svg/SP0000014315.svg); MS42/MS43 manual [SP0000007729](https://wds.psjr.org/en/e46/svg/SP0000007729.svg) (pins 2–4 as on the M3, pin 1 empty); automatic [SP0000007730](https://wds.psjr.org/en/e46/svg/SP0000007730.svg) (reverse lamps via relay K6325). Details in D3.

**X6053 and X6054** [read]:
- X6053: MSS54 [SP0000014316](https://wds.psjr.org/en/e46/svg/SP0000014316.svg); MS43 [SP0000014319](https://wds.psjr.org/en/e46/svg/SP0000014319.svg); MS45 X60531 [SP0000018630](https://wds.psjr.org/en/e46/svg/SP0000018630.svg).
- X6054: [SP0000014317](https://wds.psjr.org/en/e46/svg/SP0000014317.svg); MS45 X60541 [SP0000018631](https://wds.psjr.org/en/e46/svg/SP0000018631.svg).
- Details in D4/D5. Key point: **the MSS54 X6053 differs from the MS43 X6053.** The MSS54 has injector supply on pin 1 and the throttle-actuator lines on 6/7; the MS43 has injector supply on pin 7.

**Forum: [e46fanatics 1268369, "Funky X6053 connector on ebox"](https://www.e46fanatics.com/threads/funky-x6053-connector-on-ebox.1268369/)** [read]:
- The poster says the 8-pin engine-to-E-box plug he had always seen ("pin outs at 1-4 and 7") has "round male/female pins".
- A Jul '04 325i (automatic) instead had "flat/spade style pins". The donor was an Oct '03 325i, and the two plugs did not match.
- The same car "had the MAF version of the SAP" (secondary air pump).

**Forum: [NAM3 243029, "E46 M3 TPMS X60003 to X6011 question"](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/243029-e46-m3-tpms-x60003-to-x6011-question)** [read]: on MK60-DSC M3s the tyre-pressure reset goes to the DSC unit, and body X6011-8 is empty. The X6011-8 → X60003-19 path in SP0000014314 is the MK20-era layout.

**B+ feed** ([SP0000014406](https://wds.psjr.org/en/e46/svg/SP0000014406.svg) M3; [SP0000014676](https://wds.psjr.org/en/e46/svg/SP0000014676.svg) MS43; [SP0000017912](https://wds.psjr.org/en/e46/svg/SP0000017912.svg) MS45) [read]:
- X64101/X64102 bring B+ from the B+ distributor A2076 (F102 80 A).
- They feed DME X60001-7 (30H<102, 1.5 RT) and DME relay K6300 terminal 30 (4.0 RT).
- Details in D6.

### Inferences

- **MS43 Touring:** every body-side wire the M3 needs at X60004-1/2/11/21/18 is present at body X6011-4/6/3/5/7 with matching colour and size. They are re-pinned, not added.
- **MS43 X6011-7:** after the heater wire moves to X60004-18, the empty body X6011-7 can take the clutch wire (from X60004-23). The M3 engine harness's X6011-7 then carries it to the gear switch and on to X60002-20.
- **MS45 Touring:** the body X6011 has no wires in 3–7, so the clutch wire needs a new terminal in body X6011-7. Lamp wires run straight from X60004 to the cluster (D9).
- **X6053/X6054 stay inside the engine-harness set.** Because the MSS54 and MS43/MS45 pinouts differ (injector supply on 1 versus 7; throttle actuator on 6/7), mixing M3 and Touring harness sections at X6053 would misroute power. Use the M3's complete engine harness, E-box section included.
- The forum report suggests the round-pin plug changed to a spade-pin plug during MS45.1 production (Oct '03 versus Jul '04). The exact date is not known.

### Gaps

- **X6011-3 engine-side lead (MS43):** SP0000017260 and SP0000014318 print "2.5 BR/GR"; the oil-pressure drawing [SP0000014396](https://wds.psjr.org/en/e46/svg/SP0000014396.svg) prints 0.5 BR/GN. The 0.5 BR/GN version is the plausible one; the 2.5 is likely a drawing error (inference). It is only relevant if reusing that lead.
- **MS45 X6011-6:** the two WDS drawings disagree (above). Check the car.
- X6011 and X6021 housing and terminal part numbers were not found in the ETK pages I read.

---

## Q4. MSS54 X60001–X60005 swap-relevant pins; MSS54HP differences

### Cited findings

**Drawings read:**

| DME | Module drawings |
|---|---|
| M3 | module 1 [SP0000014290](https://wds.psjr.org/en/e46/svg/SP0000014290.svg); module 2 [SP0000014292](https://wds.psjr.org/en/e46/svg/SP0000014292.svg); module 3 [SP0000014294](https://wds.psjr.org/en/e46/svg/SP0000014294.svg) (to 2004_09) and [SP0000022868](https://wds.psjr.org/en/e46/svg/SP0000022868.svg) (from 2004_09); module 5 [SP0000014296](https://wds.psjr.org/en/e46/svg/SP0000014296.svg) |
| MS43 | module 1 [SP0000014301](https://wds.psjr.org/en/e46/svg/SP0000014301.svg); module 3 [SP0000014302](https://wds.psjr.org/en/e46/svg/SP0000014302.svg) and [SP0000017222](https://wds.psjr.org/en/e46/svg/SP0000017222.svg); module 5 [SP0000014304](https://wds.psjr.org/en/e46/svg/SP0000014304.svg) |
| MS45 | modules 1, 2, 3, 5: [SP0000018606](https://wds.psjr.org/en/e46/svg/SP0000018606.svg), [SP0000018607](https://wds.psjr.org/en/e46/svg/SP0000018607.svg), [SP0000018608](https://wds.psjr.org/en/e46/svg/SP0000018608.svg), [SP0000018610](https://wds.psjr.org/en/e46/svg/SP0000018610.svg) |

All [read]. Table D7.

**Swap-relevant pins on the M3.**
- **Signals the DME passes through to the body plug X60004:**
  - X60003-12 S_30H in (from the starter) → out on X60004-2;
  - X60003-13 S_61 in (from the alternator, to 2004_03) → out on X60004-1;
  - X60003-26 S_OLD in (oil-pressure switch) → out on X60004-11.
- **Other M3 pins:**
  - X60003-39 is F_OLN in (oil-level sensor); the DME outputs oil level on X60004-21.
  - X60003-19 is the tyre-pressure reset input from X6011-8.
  - X60002-11 drives the US pump module.
  - X60002-12 drives the E-box fan.
  - X60002-20 is the gear-switch input.
  - X60002-23 switches the DME relay coil.
- **By date** (WDS has no "HP" condition):
  - the from-2004_03 module-4 drawing drops X60004-1/2 (charge lamp over CAN);
  - from 2004_09, X60003-52 S_KGE 0.5 BR/SW → crankcase breather valve Y5256 (USA) is added ([SP0000022868](https://wds.psjr.org/en/e46/svg/SP0000022868.svg), [SP0000022872](https://wds.psjr.org/en/e46/svg/SP0000022872.svg));
  - X60003-51 S_SSP → jet-pump valve Y6165 is on both module-3 versions ([SP0000022871](https://wds.psjr.org/en/e46/svg/SP0000022871.svg)).
- **MS43 module 3 ([SP0000017222](https://wds.psjr.org/en/e46/svg/SP0000017222.svg)):** X60003-51 is the DM-TL heater input coming from X6011-7.
- **MS45 module 3 ([SP0000018608](https://wds.psjr.org/en/e46/svg/SP0000018608.svg)):**
  - X60003-16 S_OLD (the oil-pressure switch reads into the DME);
  - X60003-19 D_BSD (alternator data line);
  - X60003-50 F_OLN;
  - X60003-38/51 local CAN to terminating resistor R8554 (M56).

### Inferences

- With a complete M3 engine harness (all five DME plugs, the fuse carrier and relays included), nothing on X60001/2/3/5 is re-pinned. Their pins matter only:
  - for the pass-through functions above, which need the matching body wires on X60004;
  - for the crossings at X6011 and X6021.
- The ~09/2003 hardware change to MSS54HP has no matching date split in WDS. The splits are 2004_03 (charge lamp over CAN) and 2004_09 (breather valve). So, on WDS evidence, an HP donor wires like an MSS54 of the same production date.

### Gaps

- **MS43 coil order conflict:** the MS43 module-5 drawing puts cylinders 1/2/3/6/5/4 on pins 3/2/1/7/8/9, while the PA table says pins 1/2/3/7/8/9 = cylinders 1/2/3/6/5/4. This is irrelevant to the swap, because the M3 coil harness comes with the engine.
- The date at which charge-lamp-over-CAN was really used depends on DME software as well as hardware; not resolved here.

---

## Q5. Circuits the swap touches

Each item gives the drawings read and the key facts. Full tables are in D8.

### a) K96 fuel pump relay and the US M3 pump module

**[read]**
- **Touring (MS43, and MS45 with M54)**, [SP0000014336](https://wds.psjr.org/en/e46/svg/SP0000014336.svg), relay X10156:
  - -6 is load supply (30<54 2.5 RT/VI from F54 15 A);
  - -8 is coil supply (U_HR<3 1.5 RT/WS from F3 20 A via X6961, X6021-2 and X11212);
  - -4 is the DME control (S_EKP 0.35 SW/VI ← X60004-10);
  - -2 is the output (EKPM 1.5 WS/BL → pump M2 X638-2). Pump X638-1 is grounded via 31<7 1.5 BR → X494.
- **Euro M3:** same relay and pins ([SP0000017524](https://wds.psjr.org/en/e46/svg/SP0000017524.svg)).
- **US M3**, [SP0000014408](https://wds.psjr.org/en/e46/svg/SP0000014408.svg), "Fuel pump (MSS54 with USA_LHD)". The device is labelled "K96 Fuel pump relay 1" but sits on connector **X10157**:
  - -1 S_EKP 0.35 SW/VI ← X6021-1 ← X60002-11;
  - -8 U_HR<3;
  - -6 F54;
  - -2 EKPM 2.5 RT/WS → pump;
  - -7 ground 31L<6 2.5 BR → X13006.

**Inference:** WDS shows no US-M3 connection from X60004-10 to a relay, and nothing ties the M3's X6021-1 to a body pin on a 325i (its pin 1 is empty). Driving the Touring's K96 from X60004-10 therefore depends on the US MSS54 software driving pin 10. Earlier notes say forum builders report it works with a stored pump fault [earlier: `fuel_pump_control.md`]; WDS does not show this.

### b) DM-TL leak-check module

**ETK [read]:** "Leak diagnosis pump" 16 13 6 756 440 to Sep '01, then 16 13 7 193 479 from Sep '01, on **both** the US M3 ([page](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/)) and the US 325i Touring ([page](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/)).

**WDS [read]:**
- To 2001_09 the module has **3 wires**: pump, valve, +12 V.
  - MSS54 [SP0000014423](https://wds.psjr.org/en/e46/svg/SP0000014423.svg); MS43 [SP0000014355](https://wds.psjr.org/en/e46/svg/SP0000014355.svg).
- From 2001_09 the module is **heated, 4 wires**: 1 and 3 = pump/valve; 2 = heater; 4 = +12 V (0.75 RT/WS U_HR<3 from F3 20 A via X6021-2 and X11212).
  - MSS54 [SP0000017659](https://wds.psjr.org/en/e46/svg/SP0000017659.svg); MS43 [SP0000017277](https://wds.psjr.org/en/e46/svg/SP0000017277.svg); MS45 [SP0000017914](https://wds.psjr.org/en/e46/svg/SP0000017914.svg) and module 4 SP0000018609.
- Where the heater wire goes:
  - **MSS54:** X60004-18.
  - **MS43:** body X6011-7 → X60003-51.
  - **MS45:** X60004-2.

Pin-by-pin conflicts are in D8.2.

**Inference:** the factory drawings show the same pump/valve wiring on the MS45 and the M3. The pin-table labels disagree, and so does forum practice. Test before deciding (D12).

### c) Brake light switch, two contacts

[SP0000014399](https://wds.psjr.org/en/e46/svg/SP0000014399.svg) (MSS54) and [SP0000016222](https://wds.psjr.org/en/e46/svg/SP0000016222.svg) [read]. Switch S29, plug X78 (4-pin):

| Pin | Wire | Function and destination |
|---|---|---|
| 1 | R<9 0.5 VI/GE | from F9 5 A |
| 2 | 0.35 BR/SW | ground → X217 |
| 3 | S_BLTS 0.35 BR/GR | test contact → **X60004-34** (MSS54) or → splice X1179 → **X60004-28** (MS43/MS45) |
| 4 | S_BLS 0.35 BL/RT | → splice X181 → X60004-24 and light module X12-25 |

### d) Clutch and gear recognition

[SP0000016193](https://wds.psjr.org/en/e46/svg/SP0000016193.svg) (MS43 from 2001_03; also linked in the MS45 tree), [SP0000016194](https://wds.psjr.org/en/e46/svg/SP0000016194.svg) (MSS54 from 2001_03), and [SP0000014357](https://wds.psjr.org/en/e46/svg/SP0000014357.svg) / [SP0000014424](https://wds.psjr.org/en/e46/svg/SP0000014424.svg) (switch S32, before 2001_03) [read].

Clutch module S805, plug X13635:

| Pin | Wire | Function and destination |
|---|---|---|
| 1 | 0.35 BR/SW | ground → X217 |
| 2 | output | 0.35 BL/BR → X60004-23 (MS43/MS45) or KUPPL 0.35 GR → X6011-7 → gear switch → X60002-20 (MSS54) |
| 3 | R<9 0.5 VI/GE | from F9 5 A |
| 4 | WFSI 0.35 BL/SW | → EWS X1659-8 (starter interlock; conditions USA J22 / Japan J18) |

### e) Oil-pressure, oil-level and charge lamps

[read] Table in D8.4.
- **MS43** goes through body X6011-3/-5/-4: [SP0000014396](https://wds.psjr.org/en/e46/svg/SP0000014396.svg), [SP0000014397](https://wds.psjr.org/en/e46/svg/SP0000014397.svg), [SP0000014363](https://wds.psjr.org/en/e46/svg/SP0000014363.svg).
- **MSS54** goes through the DME:
  - oil pressure [SP0000007269](https://wds.psjr.org/en/e46/svg/SP0000007269.svg): X60003-26 → X60004-11;
  - oil level [SP0000014426](https://wds.psjr.org/en/e46/svg/SP0000014426.svg): X60003-39 → X60004-21;
  - charge lamp [SP0000014362](https://wds.psjr.org/en/e46/svg/SP0000014362.svg) to 2004_03: X60003-13 → X60004-1; from 2004_03 over CAN, [SP0000021003](https://wds.psjr.org/en/e46/svg/SP0000021003.svg).
- **MS45** reads the sensors into the DME and sends the lamps over CAN: [SP0000018655](https://wds.psjr.org/en/e46/svg/SP0000018655.svg), [SP0000017919](https://wds.psjr.org/en/e46/svg/SP0000017919.svg), [SP0000017917](https://wds.psjr.org/en/e46/svg/SP0000017917.svg).
- The oil-pressure lamp is cluster **X11175-13**. Pin 14 is the K-bus ([SP0000017540](https://wds.psjr.org/en/e46/svg/SP0000017540.svg), [SP0000018656](https://wds.psjr.org/en/e46/svg/SP0000018656.svg)).

### f) Sport button and switch centre

[SP0000014425](https://wds.psjr.org/en/e46/svg/SP0000014425.svg) "Driving dynamics switch (M3)" and [SP0000015484](https://wds.psjr.org/en/e46/svg/SP0000015484.svg) "DWS reset switch (MSS54)" [read].
- **Signals:**
  - switch centre A169 X1869-17 FDYN 0.35 SW/RT/GE → X60004-15;
  - X1869-18 FDYNLED 0.35 SW/GR/GE → X60004-16.
- **Switch X521:**
  - LED lighting 58G 0.5 GR/RT from light module X12-47 via X1019/X908 → X521-3;
  - ground X521-4 0.75 BR → X219 (SP0000014425). SP0000015484 shows X521-4 as 31E<1 0.5 BR/SW → X10012 instead.
- **Switch-centre supplies (SP0000015484):**
  - X521-1 15<33 0.5 GN/BL/GE from F33 5 A;
  - X1869-7 30<42 4.0 RT/VI from F42 30 A;
  - X1869-23 K-bus 0.35 WS/RT/GE;
  - X1869-2 S_RDKS 0.5 GE/SW → X6011-8 → X60003-19 (tyre-pressure reset, MK20-era).

### g) Electric radiator fan

[SP0000011770](https://wds.psjr.org/en/e46/svg/SP0000011770.svg) (to 2003_03); [SP0000019629](https://wds.psjr.org/en/e46/svg/SP0000019629.svg) (Saloon/Compact/Touring from 2003_03); [SP0000019630](https://wds.psjr.org/en/e46/svg/SP0000019630.svg) (coupe/convertible) [read].
- Same DME pins on every family:
  - X60004-4 T_ELUE 0.5 SW/GN → fan M9 X82-2;
  - radiator-outlet temperature sensor X87-1/-2 ↔ X60004-38/39.
- Power: F37 50 A, 30<37 6.0 RT/BL → X82-4. Ground: X82-1 6.0 BR → ground X166/X165 on saloon/Touring, X14250/X14249 on coupe/convertible.

### h) E-box fan

**M3** ([SP0000014366](https://wds.psjr.org/en/e46/svg/SP0000014366.svg)):

| X6506 pin | Wire | Source |
|---|---|---|
| 1 | S_EBOX 0.5 BR/GE | ← X60002-12 |
| 2 | S_30H | ← X276 |
| 3 | U_HR<3 0.5 RT/WS | supply |

**MS45 and MS43-USA from 2003_03** ([SP0000017918](https://wds.psjr.org/en/e46/svg/SP0000017918.svg)):

| X6506 pin | Wire | Source |
|---|---|---|
| 1 | S_EBOXL 0.5 BR/OR | ← X60004-19 |
| 2 | U_HR<3 | supply |

**MS42/MS43 otherwise** ([SP0000008137](https://wds.psjr.org/en/e46/svg/SP0000008137.svg)): a thermostatic switch B6235 and F28 5 A.

All [read]. **The M3 and MS45 fan plugs use different pins.** Feed the fan from one harness only.

### i) A/C compressor

[SP0000011762](https://wds.psjr.org/en/e46/svg/SP0000011762.svg) (non-M) and [SP0000011761](https://wds.psjr.org/en/e46/svg/SP0000011761.svg) (M3) [read].
- **Same DME pin on all families:** X60004-29 S_KOREL 0.5 SW/BL → compressor relay K19 X51-8.
- **Relay K19:**
  - X51-2 30<63 0.75 RT/VI/GE from F63 7.5 A;
  - X51-4 coil feed;
  - X51-6 0.75 SW/GR → compressor clutch;
  - X51-5 → climate unit X610-9.
- The A/C pressure sensor is read by the climate unit (A11), not the DME.

### j) Auxiliary water pump

[SP0000017567](https://wds.psjr.org/en/e46/svg/SP0000017567.svg) (from 2000_03), [SP0000011635](https://wds.psjr.org/en/e46/svg/SP0000011635.svg) (older version, F23 feed) and [SP0000007511](https://wds.psjr.org/en/e46/svg/SP0000007511.svg) (water valve) [read].
- Pump M37: X122-1 30<62 0.5 RT/GR from F62 7.5 A; X122-2 0.5 BR/RT → climate unit A11 X608-6.
- No DME involvement.
- **ETK** [read]: US M3 "Water valve with additional water pump 64 11 8 369 807"; US 325i Touring "Water valve 64 11 8 369 805" (no pump).

### k) DME power, main relay, fuses and grounds

[SP0000014406](https://wds.psjr.org/en/e46/svg/SP0000014406.svg) (M3), [SP0000014676](https://wds.psjr.org/en/e46/svg/SP0000014676.svg) (MS43), [SP0000017912](https://wds.psjr.org/en/e46/svg/SP0000017912.svg) (MS45), and main relay [SP0000014337](https://wds.psjr.org/en/e46/svg/SP0000014337.svg) / [SP0000014407](https://wds.psjr.org/en/e46/svg/SP0000014407.svg) [read]. Table in D6.

### l) EWS–DME

[SP0000007256](https://wds.psjr.org/en/e46/svg/SP0000007256.svg) [read]: X60004-33 D_EWS 0.35 SW/VI ↔ EWS A836 X1659-4. Same on every family. Terminal 50 to the starter also runs through EWS (X1659-1 → X6011-1); see D2.

### m) CAN

[SP0000015023](https://wds.psjr.org/en/e46/svg/SP0000015023.svg) (MSS54 with MK60, LHD), [SP0000014266](https://wds.psjr.org/en/e46/svg/SP0000014266.svg) (MSS54 with MK20) and [SP0000017172](https://wds.psjr.org/en/e46/svg/SP0000017172.svg) (petrol LHD) [read].
- **Wiring:** DME X60004-36/37 (0.5 GE/RT and GE/BR) → splices X1893/X1894, which join:
  - cluster X11175-9/10;
  - DSC X18303-11/15 (MK20: X1746-17/16);
  - steering-angle sensor;
  - adaptive-headlight unit (AHL, A214 X10513-13/14, where fitted).
- **Other CAN users:** the automatic gearbox unit uses DME X60002-3/4 (MS43, automatic only); SMG uses X60002-21/22 (SMG only).
- **No terminating resistors are drawn.**
- **BMW ST040** [read]: "A 120 Ohm resistor is installed in two control units … the effective resistance of the complete circuit is 60 Ohms … The terminal resistors are located in the ASC/DSC control unit and either the instrument cluster or in the DME. … [non-terminating units] should be between 10kOhms and 50kOhms."
- **ST052 (E46)** [read]: "two terminal resistors of 120 ohms each for a total circuit resistance of 60 ohms".

### n) OBD socket

[SP0000014297](https://wds.psjr.org/en/e46/svg/SP0000014297.svg) [read]: no CAN on pins 6/14. Pin table in D8.10.

ST052 [read]: "In the E46, the instrument cluster acts as a gateway between the D-Bus, CAN bus and K-Bus." It also says the 20-pin underhood connector was deleted in model year 2001. ST040 [read]: "TXD is installed in pin 8. TXD II remains in pin 7."

### o) Road speed

[SP0000015064](https://wds.psjr.org/en/e46/svg/SP0000015064.svg) [read]: X60004-22 F_DFAHR 0.35 WS/GN ← DSC MK60 X18303-8 (via splice X1101). Same pin on every family.

---

## Q6. MS45 X60004 pins 5 and 15; the MSS54 pin-5 ground

### Cited findings

- **WDS MS45 module 4** [read]: X60004-5 M_SHFM 0.5 SW/GE and X60004-15 A_SHFM 0.5 SW/RT → secondary-air air-mass sensor B6206 X6206-1/-3.
- **[SP0000019608](https://wds.psjr.org/en/e46/svg/SP0000019608.svg)** "Secondary air system (as of 2003_03)" [read]: the sensor's X6206-2 is fed U_HR<3 1.5 RT/WS via X6021-2, X11212 and X18241.
- **ETK, US 325i Touring M54, "Emission control-air pump" from Mar '03** [read] ([page](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/emission_control_air_pump_2/)):
  - "Mass air flow sensor 11 72 1 438 814 from Mar '03";
  - "Secondary air filter 11 72 1 438 813";
  - "Air pump 11 72 7 571 589".

  The to-Mar '03 group has no air-mass sensor ([page](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine/emission_control_air_pump/)).
- **Forum** [read]: a Jul '04 325i "had the MAF version of the SAP" ([e46fanatics 1268369](https://www.e46fanatics.com/threads/funky-x6053-connector-on-ebox.1268369/)).
- **MSS54:** X60004-5 = 31E<2 0.35 BR/SW → ground X1108 on all three M3 module-4 drawings [read].
  - X1108 is "under carpet of driver's seat".
  - [SP0000011831](https://wds.psjr.org/en/e46/svg/SP0000011831.svg) [read] shows X1108 also grounding other body units, including OBD pin 5 (signal ground).

### Inferences

- On an MS45.1 Touring, pins 5 and 15 are populated. Remove both wires and insulate them; the secondary-air sensor wiring itself is not needed by the S54.
  - Otherwise the sensor's ground-side wire sits on the MSS54's ground pin 5.
  - And the sensor signal reaches the MSS54's Sport input on pin 15.
- **Pin 5 ground:**
  - MS45 car: once pin 5 is cleared, a new 0.35 BR/SW lead from X60004-5 to the X1108 ground (or another body ground of the same family) copies the M3.
  - MS43 car: the same applies (pin 5 is empty).
  - No source shows what the MSS54 uses pin 5 for, and one forum test found no change [earlier].

### Gaps

- Whether the MSS54 needs pin 5 grounded (for example as a reference for a sensor or diagnosis) is unknown.

---

## Q7. Connector views, terminal families, housing part numbers

### Cited findings

**WDS connector views** [read]. Layouts are in D10.

| Plug | Page | Image |
|---|---|---|
| X60004 | [SX60004A](https://wds.psjr.org/en/e46/zinfo/E46_SX60004A.htm) | B400001 |
| X60001 / X60005 | [SX60001A](https://wds.psjr.org/en/e46/zinfo/E46_SX60001A.htm) / [SX60005A](https://wds.psjr.org/en/e46/zinfo/E46_SX60005A.htm) | B090009 |
| X60002 | [SX60002A](https://wds.psjr.org/en/e46/zinfo/E46_SX60002A.htm) | B240002 |
| X60003 | [SX60003A](https://wds.psjr.org/en/e46/zinfo/E46_SX60003A.htm) | B520001 |
| X6011 | [SX6011A](https://wds.psjr.org/en/e46/zinfo/E46_SX6011A.htm) | B080032 |
| X6053 | [SX6053A](https://wds.psjr.org/en/e46/zinfo/E46_SX6053A.htm) | B080002D |
| X6021 | [SX6021A](https://wds.psjr.org/en/e46/zinfo/E46_SX6021A.htm) | B040036A |
| X11175 | [SX11175A](https://wds.psjr.org/en/e46/zinfo/E46_SX11175A.htm) | — |
| X1869 | [SX1869A](https://wds.psjr.org/en/e46/zinfo/E46_SX1869A.htm) | — |
| X13635 | [SX13635A](https://wds.psjr.org/en/e46/zinfo/E46_SX13635A.htm) | — |
| X78 | [SX78A](https://wds.psjr.org/en/e46/zinfo/E46_SX78A.htm) | — |
| X10156 | [SX10156A](https://wds.psjr.org/en/e46/zinfo/E46_SX10156A.htm) | — |
| X17140 / X1714 | [SX17140A](https://wds.psjr.org/en/e46/zinfo/E46_SX17140A.htm) / [SX1714B](https://wds.psjr.org/en/e46/zinfo/E46_SX1714B.htm) | — |
| X19527 | [SX19527A](https://wds.psjr.org/en/e46/zinfo/E46_SX19527A.htm) | — |
| X1659 | [SX1659A](https://wds.psjr.org/en/e46/zinfo/E46_SX1659A.htm) | — |

- Each view shows the housing face with cavity numbers (often only the corner numbers) and a small symbol for the terminal type: a socket (female) symbol on X60004, X60001–X60003, X6053, X6021 and others; a **pin (male) symbol on X6011**.
- **No page states the viewing side.**
- The X60004 view numbers its rows left → right (1 at bottom left). The X60001/2/3/5 views number right → left (1 at bottom right).

**ETK housings and caps** (US 325i Touring "Basic control unit DME" group [read]; the US M3 group lists the same numbers):

| Housing | Part numbers | Cap |
|---|---|---|
| 9-pin socket housing | 12 52 1 744 624 (pin count from a retailer snippet) | 12 52 7 502 456 |
| 24-pole "/A" | 12 52 1 744 627 and 12 52 1 744 628 | 12 52 1 744 626 |
| 52-pole "/A" | 12 52 1 744 633 and 12 52 1 744 634 | 12 52 1 744 632 (to Jul '03) or 12 52 7 526 424 ("52POL./Z-CODE") |
| 40-pole "/B" | 12 52 1 744 630 and 12 52 1 744 631 | 12 52 1 744 629 |

**ETK terminals** ("Contact system MLK" and "Laminated contacts/spring contacts", US 325i Touring [read]): listed in D11. ETK does not say which terminal goes in which DME cavity.

**BMW ST051 Archive 1 "Breakout Boxes & Connectors"** [read]:
- It describes BMW's plug systems in general (MQS/MPQ from AMP; Elo/Elo-Power from Siemens) and release tools 61 1 132, 61 1 134, 61 1 135, 61 1 136 and 61 1 137.
- For one housing type it says to "observe cavity numbers on reverse side of socket housing".
- It gives no E46 DME-specific instructions.

**Forum** [read]: the E-box 8-pin X6011/X6053-type plugs normally have "round male/female pins"; the spade-pin version is described in Q3 ([e46fanatics 1268369](https://www.e46fanatics.com/threads/funky-x6053-connector-on-ebox.1268369/)).

### Inferences

- The housings carry moulded cavity numbers. Match WDS numbers to the moulding, not to the drawing's orientation, and treat the D10 layouts as "which number is next to which", not as a viewing side.
- The 40-pole housing being "/B" while the 24- and 52-pole are "/A" may be why X60004's numbering runs the other way. This is unconfirmed.

### Gaps

- The viewing side of WDS views is not stated.
- There is no cavity → terminal-part mapping.
- X6011 and X6021 housing part numbers were not found.

---

## Diagram-ready data

All values come from WDS drawings or pin tables [read] unless marked otherwise. "→" means signal direction or wire run as drawn; "↔" means a two-way or undirected link. A "—" means not present or not used.

### D1. X60004 (40-pin black, "DME module 4", body harness): side by side

Column sources:
- **MS43-US** = SP0000017224 + PA J (manual, from 2001_09). Pre-2001_09 differences are in the notes column.
- **MS45.1-325i (M54, manual, from 2003_03)** = SP0000018609 + PA O/P, corrected with the M54 drawings SP0000014336 (pin 10), SP0000016193 (pin 23) and SP0000019608 (pins 5/15).
- **MSS54-US** = SP0000017646 + PA L (2001_09–2004_03).

| Pin | MS43-US (325i, manual, from 2001_09) | MS45.1-325i (M54 manual, from 2003_03) | MSS54-US (M3, 2001_09–2004_03) | Notes and other dates |
|---|---|---|---|---|
| 1 | — | — | S_61--1 0.35 BL → cluster X11175-2 (charge lamp) | MS43: lamp wire is at body X6011-4. MS45: lamp over CAN. MSS54 from 2004_03: not drawn (CAN), PA R still lists it |
| 2 | — | S_DMTLH 0.75 SW/RT → DM-TL X17141-2 (heater) | S_30H 0.35 SW/GN ↔ splice X276 → cluster X11175-3 + E-box fan X6506-2 (start feedback; fed from X60003-12) | MS43: S_30H wire is at body X6011-6. MSS54 from 2004_03: not drawn |
| 3 | S_SLP 0.35 BR/BL → secondary-air relay K6304 X6304-4 | same | same | — |
| 4 | T_ELUE 0.5 SW/GN → electric fan M9 X82-2 | same | same | — |
| 5 | — | M_SHFM 0.5 SW/GE ↔ secondary-air sensor B6206 X6206-1 (ground side) | 31E<2 0.35 BR/SW → ground X1108 | MSS54: on all dates |
| 6 | — | — | S_50 0.35 SW/BL ← X18820 (terminal 50, "ignition lock") | MSS54: on all dates |
| 7 | M_FWG1 0.35 BR/GN ↔ pedal R10 X11400-1 | same | MFW1 0.35 BR/GN ↔ X11400-1 | pedal sensor |
| 8 | A_FWG1 0.35 WS ↔ X11400-4 | same | AFW1 0.35 WS | — |
| 9 | U_FWG1 0.35 GE ↔ X11400-5 | same | UFW1 0.35 GE | — |
| 10 | S_EKP 0.35 SW/VI → K96 X10156-4 | S_EKP 0.35 SW/VI → K96 X10156-4 (SP0000014336) | S_EKP 0.35 SW/VI → K96, **EUR only**; USA "not used" | US M3 pump control is on X60002-11 |
| 11 | — | — | S_OLD 0.35 BR/GN → cluster X11175-13 (oil-pressure lamp; fed from X60003-26) | MS43: wire is at body X6011-3 |
| 12 | M_FWG2 0.35 BR ↔ X11400-2 | same | MFW2 0.35 BR | — |
| 13 | A_FWG2 0.35 WS/GN ↔ X11400-6 | same | AFW2 0.35 WS/GN | — |
| 14 | U_FWG2 0.35 GE/GN ↔ X11400-3 | same | UFW2 0.35 GE/GN | — |
| 15 | — | A_SHFM 0.5 SW/RT ↔ B6206 X6206-3 (sensor signal) | FDYN 0.35 SW/RT/GE ← switch centre X1869-17 (Sport) | — |
| 16 | — | — | FDYNLED 0.35 SW/GR/GE → X1869-18 (Sport LED) | — |
| 17 | F_TD 0.35 SW → splice X243 (engine-speed signal; OBD pin 9) | same | same | — |
| 18 | (S_AKL 0.5 GR/VI → exhaust-flap valve; **3.0-litre only**) | — | DMTLH 0.75 SW/RT → DM-TL X17140-2 (heater, USA) | MSS54 to 2001_09: not used. MS43 heater wire is at body X6011-7 |
| 19 | — | S_EBOXL 0.5 BR/OR → E-box fan X6506-1 (if fitted) | — | M3 fan is driven from X60002-12 |
| 20 | DMTL 0.5 SW/GN ↔ DM-TL X1714-1 (PA: "valve") | S_DMTLP 0.75 BR/BL ↔ X17141-1 (PA: "pump") | DMTL 0.75 BR/BL ↔ X17140-1 (PA: "valve") | MS43 function drawing SP0000017277: 0.75 BR/BL. MS43 to 2001_09: DMTL 0.5 SW/GN ↔ X6139-2. MSS54 to 2001_09: not used |
| 21 | — | — | F_OLN 0.5 WS/GN → cluster X11175-17 (oil level) | MS43: wire is at body X6011-5 |
| 22 | F_DFAHR 0.35 WS/GN ← splice X1101 (road speed from DSC) | same | same | — |
| 23 | S_KUP 0.35 BL/BR ← clutch module X13635-2 | S_KUP 0.35 BL/BR ← X13635-2 (SP0000016193) | — (clutch goes via X6011-7 → gear switch → X60002-20) | MS43 to 2001_03: clutch switch S32 |
| 24 | S_BLS 0.35 BL/RT ← splice X181 (brake switch, contact 1) | same | same | — |
| 25 | — | — (EAC sensor, M56 only) | — | — |
| 26 | 15<29 0.5 GN/VI ← F29 5 A | same | same | MS43 supply drawings print GN/SW |
| 27 | FGRS 0.35 BL/SW ← steering-wheel buttons X10170-8 (cruise) | same | same | — |
| 28 | S_BLTS 0.35 BR/GR ← splice X1179 (brake test contact) | same | — | MSS54 to 2001_09: DMTLP 0.5 SW/GN ↔ X17140-2 |
| 29 | S_KOREL 0.5 SW/BL → A/C relay K19 X51-8 | same | same | — |
| 30 | DMTLP 0.75 BR/BL ↔ X1714-3 (PA: "pump") | S_DMTLV 0.5 SW/GN ↔ X17141-3 (PA: "valve") | DMTLP 0.5 SW/GN ↔ X17140-3 (PA: "pump") | SP0000017277: 0.5 SW/GN. MS43 to 2001_09: DMTLP 0.75 BR/BL ↔ X6139-1. MSS54 to 2001_09: DMTL 0.75 BR/BL ↔ X17140-1 |
| 31 | — | — (local CAN, M56 only) | — | — |
| 32 | D_TXD2 0.5 WS/VI ↔ OBD X19527-7 | same | same | — |
| 33 | D_EWS 0.35 SW/VI ↔ EWS X1659-4 | same | same | — |
| 34 | — | — | S_BLTS 0.35 BR/GR ← brake switch X78-3 | — |
| 35 | — | — (local CAN, M56 only) | — | — |
| 36 | D_CAN-H 0.5 GE/RT → splice X1893 | same | same | — |
| 37 | D_CAN-L 0.5 GE/BR → splice X1894 | same | same | — |
| 38 | M_TKA 0.35 SW/GN ↔ radiator-outlet temp sensor X87-1 | same | same | — |
| 39 | A_TKA 0.35 SW/GR ↔ X87-2 | same | same | — |
| 40 | — | — | — | — |

### D2. X6011 (8-pin black, "Engine plug I", E-box): body side ↔ engine side

| Pin | MSS54-US (SP0000014314) | MS43-US from 2001_09 (SP0000017260) | MS43-US to 2001_09 (SP0000014318) | MS45 (SP0000018632) |
|---|---|---|---|---|
| 1 | S_50EWS 2.5 SW from EWS X1659-1 ↔ S_50 2.5 SW → starter X6510 | S_50 2.5 SW ↔ 2.5 SW → X6510 | same | same |
| 2 | 15<30 0.75 GN/BR from F30 7.5 A ↔ 1.0 GN/BR → splice X6831 (oil-level sensor and alternator feed) | 0.75 GN/BR ↔ 0.75 GN/BR → X6831 | same | same |
| 3 | — | S_OLD 0.35 BR/GN from cluster X11175-13 ↔ S_OLD (printed "2.5 BR/GR"; 0.5 BR/GN on SP0000014396) → oil-pressure switch X6231-1 | same | — |
| 4 | — | S_61--1 0.35 BL from X11175-2 ↔ 0.75 BL → alternator X6524-2 | same | — |
| 5 | — | F_OLN 0.5 WS/GN from X11175-17 ↔ 0.5 GR/BL → oil-level sensor X6254-3 | same | — |
| 6 | — | S_30H 0.35 SW/GN from X276 (→ X11175-3, X6506-2) ↔ 0.75 SW/GE → starter X6511 | same | — (but SP0000014365 shows it; conflict) |
| 7 | KUPPL 0.35 GR from clutch X13635-2 (S32 before 2001_03) ↔ S_GANG 0.5 GR → X6053-5 → gear switch | DMTLH 0.75 SW/RT from DM-TL X1714-2 ↔ 0.75 SW/RT → X60003-51 (USA only) | — | — |
| 8 | RDKS 0.5 GE/SW from switch centre X1869-2 ↔ 0.5 GE/SW → X60003-19 (tyre-pressure reset, MK20-era) | — | — | — |

### D3. X6021 (4-pin black, "Engine plug", E-box)

| Pin | MSS54-US (SP0000014315) | MS42/MS43 manual (SP0000007729) | Function |
|---|---|---|---|
| 1 | USA: S_EKP 0.35 SW/VI from X60002-11 ↔ pump module X10157-1. EUR: empty | empty | US M3 pump-module control |
| 2 | engine side U_HR<3 1.5 RT/WS (F3 via X6962) ↔ body 0.5 RT/WS → splice X11212 | engine U_HR<3 ↔ body 1.5 RT/WS → X11212 | F3-fused DME-relay power to body loads: K96/pump-module coil, DM-TL, E-box fan (MS45), secondary-air sensor (MS45), A/C relay coil |
| 3 | S_RS+ 1.0 BL/GE: reverse switch X8511-1 ↔ X428 | same | reverse lamps |
| 4 | 15<27 1.0 GN/WS: F27 10 A ↔ X8511-2 | same | reverse-switch feed |

Automatic cars (SP0000007730) switch the reverse lamps via relay K6325.

### D4. X6053 / X60531 (8-pin natural; inside the engine-harness set, E-box)

| Pin | MSS54 X6053 (SP0000014316) | MS43 X6053 (SP0000014319) | MS45 X60531 (SP0000018630) |
|---|---|---|---|
| 1 | U_EVR 2.5 RT/GE: injector relay K6327 X6327-2 ↔ X6970 (injector supply) | 15<30 → automatic-gearbox unit X70001-1 | 15<30 0.5 GN/BR: X6831 ↔ X70001-1 |
| 2 | U_HR<2 2.5 RT/WS/GE (F2) | U_HR<2 | U_HR<2 2.5 RT/WS/GE: X6964 ↔ X6960 |
| 3 | U_HR<3 2.5 RT/WS (F3) | U_HR<3 | U_HR<3 2.5 RT/WS: X6965 ↔ X6961 |
| 4 | 31L 1.5 BR: X6458 ↔ X6461 | 31L 0.5 BR (oil-level sensor ground) | 31L 0.5 BR: X6254-2 ↔ X6458 |
| 5 | S_GANG 0.5 GR (clutch → gear switch) | — | — |
| 6 | P_DKSM+ 2.5 RT: X60001-2 ↔ throttle actuator Y5392-2 | — | — |
| 7 | P_DKSM-- 2.5 WS: X60001-9 ↔ Y5392-1 | U_EV 2.5 RT/GE ← K6327 (injector supply) | U_EV 2.5 RT/GE: X6970 ↔ K6327 X6327-2 |
| 8 | — | — | — |

### D5. X6054 / X60541 (2-pin natural, E-box)

| Pin | MSS54 / MS43 X6054 (SP0000014317) | MS45 X60541 (SP0000018631) |
|---|---|---|
| 1 | U_HR<1 2.5 from F1 30 A (X8680-2) ↔ 15_ZSP 2.5 GN (ignition coils) | U_HR<1 2.5 RT/WS: X8680-2 (F1 30 A) ↔ X6969 |
| 2 | 31L 2.5 BR: X60005-5 ↔ X6458 | 31L 2.5 BR: X60005-5 ↔ X6454 |

### D6. B+ feed, DME relay, injector relay, fuse carrier (E-box)

| Item | Pin or terminal | Wire | From → to | Notes |
|---|---|---|---|---|
| X64101 (2-pin cable lug) / X64102 (2-pin plug) | — | 6.0 RT in | B+ distributor A2076 (F102 80 A) via X18326-1 → E-box | "Connector, B+ distribution" |
| X60001-7 | 30H<102 | 1.5 RT | X64101/X64102 → DME | all families |
| K6300 DME relay, terminal 30 | X6300-6 | 4.0 RT | X64102 → relay | — |
| K6300 terminal 87 | X6300-2 and -5 | 4.0 RT/WS | relay → fuse carrier A8680 | — |
| K6300 coil (85) | X6300-4 | S_HR 0.5 BR/WS (M3); BR (MS43); BR/SW (MS45) | relay → DME X60002-23 | the DME switches the relay |
| A8680 F1 30 A | X8680-1 in / -2 out | U_HR<1 2.5 | → coils via X6054-1 (MS45: X60541-1) | — |
| A8680 F2 30 A | -3 / -4 | U_HR<2 (M3 2.5; MS43/MS45 1.0 at the DME) RT/WS/GE | → X60001-8 and X6053-2 | — |
| A8680 F3 20 A | -5 / -6 | U_HR<3 RT/WS | → X6053-3 and X6021-2 → body loads; M3 E-box fan X6506-3 | — |
| A8680 F4 30 A | -7 / -8 | U_HR<4 | → oxygen-sensor heaters etc. | — |
| X60001-1 | 15 | 0.5 GN | DME ↔ injector relay K6327 X6327-8 | K6327 output X6327-2 → X6053-1 (M3) / X6053-7 (MS43) / X60531-7 (MS45) |
| X60004-26 | 15<29 | 0.5 GN/VI | F29 5 A → DME | terminal 15 |
| Grounds | X60001-4 | 31E 1.5 BR/OR | → X6454 (automatic via X6459) | — |
| Grounds | X60001-5/-6 | 31L 1.5 BR | → X6458 | — |
| Grounds | X60005-5 | 31L 2.5 BR | → X6054-2 (MS45: X60541-2) → X6458/X6454 | — |
| Grounds | X60004-5 | 0.35 BR/SW | → X1108 | **MSS54 only** |

### D7. X60001 / X60002 / X60003 / X60005: swap-relevant pins

| Plug-pin | MSS54-US | MS43-US | MS45 | Relevance |
|---|---|---|---|---|
| X60001-2 / -9 | P_DKSM+ 2.5 RT / P_DKSM-- 2.5 WS → X6053-6/-7 → throttle actuator | (not on X6053) | (not on X60531) | why X6053 differs |
| X60001-3 | — (non-SMG) | — | — | — |
| X60002-11 | S_EKP 0.35 SW/VI → X6021-1 → pump module (USA) | — | — | US M3 pump control |
| X60002-12 | S_BOX 0.5 BR/GE → E-box fan X6506-1 | — | — | M3 E-box fan |
| X60002-20 | S_GANG 0.5 GR/BL ← gear switch X5271-2 | — | — | clutch/gear chain |
| X60002-21/-22 | SMG CAN (SMG only) | — | — | — |
| X60002-23 | S_HR 0.5 BR/WS → K6300 X6300-4 | DME relay | DME relay | — |
| X60002-3/-4 | — | gearbox-unit CAN (automatic) | — | — |
| X60003-12 | S_30H 0.75 SW/GE ← starter X6511 | — (via X6011-6) | — | → X60004-2 |
| X60003-13 | S_61 0.5 BL ← alternator X6524-2 (to 2004_03) | — (via X6011-4) | D_BSD on pin 19 | → X60004-1 |
| X60003-16 | — | — | S_OLD 0.5 BR/GN ← oil-pressure switch | MS45 reads it, lamp over CAN |
| X60003-19 | RDKS 0.5 GE/SW ← X6011-8 | — | D_BSD 0.5 BL (alternator data line) | — |
| X60003-26 | S_OLD 0.5 BR/GN ← oil-pressure switch X6231 | — (via X6011-3) | — | → X60004-11 |
| X60003-39 / -50 | -39 F_OLN 0.5 GR/BR ← oil-level sensor X6254-3 | — (via X6011-5) | -50 F_OLN 0.5 GR/BL | MSS54 → X60004-21 |
| X60003-51 | S_SSP 0.5 GE/BR → jet-pump valve Y6165 | DMTLH ← X6011-7 (USA, from 2001_09) | local CAN (M56) | — |
| X60003-52 | S_KGE 0.5 BR/SW → crankcase breather valve Y5256 (USA, from 2004_09) | — | — | — |
| X60005 coils | pins 1/2/3/6/7/9 = cyl 1/2/3/5/6/4 | 3/2/1/7/8/9 = cyl 1/2/3/6/5/4 (PA: 1/2/3/7/8/9) | 1/4/6/7/8/9 = cyl 5/3/1/2/4/6 | comes with the engine harness |
| X60005 coil wire colours (M3 drawing) | cyl 1 SW/WS, 2 SW/RT, 3 SW/GE, 4 SW/BL, 5 SW/GN, 6 SW/VI, all 1.5 | — | — | pin 5 = 31L 2.5 BR |

### D8. Circuit tables

#### D8.1 Fuel pump

| Point | MS43 / MS45.1 (M54) 325i: K96, X10156 (SP0000014336) | Euro M3: K96, X10156 (SP0000017524) | US M3: "K96", X10157 (SP0000014408) |
|---|---|---|---|
| DME control | X60004-10 → X10156-4, S_EKP 0.35 SW/VI | X60004-10 → X10156-4 | X60002-11 → X6021-1 → X10157-1, 0.35 SW/VI |
| Coil / module supply | X10156-8 ← U_HR<3 1.5 RT/WS (F3 via X6961, X6021-2, X11212) | same | X10157-8 ← U_HR<3 1.5 RT/WS (F3 via X6962, X6021-2, X11212) |
| Load supply | X10156-6 ← 30<54 2.5 RT/VI (F54 15 A) | same | X10157-6 ← 30<54 2.5 RT/VI (F54 15 A) |
| Pump output | X10156-2 → EKPM 1.5 WS/BL → pump X638-2 | same | X10157-2 → EKPM 2.5 RT/WS → pump X638-2 |
| Grounds | pump X638-1 31<7 1.5 BR → X494 | — | pump X638-1 and X10157-7 31L<6 2.5 BR → X13006 |

#### D8.2 DM-TL leak-check module: every WDS drawing

| Drawing | DME, date | Module plug | → X60004 (or other) | Wire | WDS name | Pin-table label |
|---|---|---|---|---|---|---|
| SP0000014423 | MSS54, to 2001_09 | X17140-1 | 30 | 0.75 BR/BL | DMTL | PA G: 28 and 30 both "Leakage diagnosis pump" |
| | | X17140-2 | 28 | 0.5 SW/GN | DMTLP | |
| | | X17140-3 | supply U_30<3 0.75 RT/WS (F3) | | | |
| SP0000014355 | MS43, to 2001_09 | X6139-1 | 30 | 0.75 BR/BL | DMTLP | PA E: "Diagnostic module, fuel tank leakage" (both) |
| | | X6139-2 | 20 | 0.5 SW/GN | DMTL | |
| | | X6139-3 | supply U_HR<3 0.75 RT/WS (F3) | | | |
| SP0000017646 + SP0000017659 | MSS54, from 2001_09 (also SP0000020984 from 2004_03) | X17140-1 | 20 | 0.75 BR/BL | DMTL | PA L/R: 20 "valve" |
| | | X17140-2 | 18 | 0.75 SW/RT | DMTLH | heater |
| | | X17140-3 | 30 | 0.5 SW/GN | DMTLP | PA L/R: 30 "pump" |
| | | X17140-4 | supply U_HR<3 0.75 RT/WS (F3 via X6021-2, X11212) | | | |
| SP0000017224 | MS43-US module 4, from 2001_09 | X1714-1 | 20 | **0.5 SW/GN** | DMTL | PA J: 20 "valve" |
| | | X1714-3 | 30 | **0.75 BR/BL** | DMTLP | PA J: 30 "pump" |
| SP0000017277 | MS43 heated-module function drawing, from 2001_09 | X1714-1 | 20 | **0.75 BR/BL** | DMTL | — |
| | | X1714-3 | 30 | **0.5 SW/GN** | DMTLP | — |
| | | X1714-2 | X6011-7 → X60003-51 | 0.75 SW/RT | DMTLH | heater |
| | | X1714-4 | supply U_HR<3 0.75 RT/WS (F3 20 A via X6021-2, X11212) | | | |
| SP0000018609 | MS45 module 4 | X17141-1 | 20 | 0.75 BR/BL | S_DMTLP | PA O/P: 20 "pump" |
| | | X17141-2 | 2 | 0.75 SW/RT | S_DMTLH | heater |
| | | X17141-"30" (drawing typo for 3) | 30 | 0.5 SW/GN | S_DMTLV | PA O/P: 30 "valve" |
| SP0000017914 | MS45 heated-module function drawing | X17141-1 | 20 | 0.75 BR/BL | S_DMTLP | — |
| | | X17141-2 | 2 | 0.75 SW/RT | S_DMTLH | heater |
| | | X17141-3 | 30 | 0.5 SW/GN | S_DMTLV | — |
| | | X17141-4 | supply U_HR<3 0.75 RT/WS (F3 20 A via X6021-2, X11212) | | | |

What the table shows:
- **Wire to module pin, consistent.** In every drawing but SP0000017224, the 0.75 BR/BL wire goes to module pin 1. The 0.5 SW/GN wire goes to the other pump/valve pin (2 on the 3-wire module, 3 on the 4-wire module).
- **DME pin to module pin, consistent.** Every heated drawing, SP0000017224 included, connects X60004-20 ↔ pin 1 and X60004-30 ↔ pin 3.
- **Labels, inconsistent.** The WDS names and pin-table labels for which pin is the pump contradict each other, both across DMEs and between drawings of the same module.
- **Inference:** the drawings support "no 20/30 change" for both MS43 and MS45 Tourings. The MS45-versus-MSS54 label clash is what drives forum advice to swap 20/30. One reported swap left P2418 (switching-valve circuit open) unresolved ([e46fanatics 1286041](https://www.e46fanatics.com/threads/e46-m3-sport-button-retrofit-on-non-m.1286041/) [earlier]). Decide by test (D12), not by label.

#### D8.3 Brake switch and clutch

| Device, pin | Wire | MS43 / MS45.1 Touring | MSS54-US |
|---|---|---|---|
| Brake switch S29 X78-1 | R<9 0.5 VI/GE | F9 5 A | same |
| X78-2 | 31E<2 0.35 BR/SW | → ground X217 | same |
| X78-3 (test contact) | S_BLTS 0.35 BR/GR | → X1179 → X60004-28 | → X60004-34 |
| X78-4 | S_BLS 0.35 BL/RT | → X181 → X60004-24 and light module X12-25 | same |
| Clutch module S805 X13635-1 | 31E<2 0.35 BR/SW | → X217 | same |
| X13635-2 | output | S_KUP 0.35 BL/BR → X60004-23 | KUPPL 0.35 GR → X6011-7 → S_GANG 0.5 GR → X6053-5 → gear switch X5271-1; X5271-2 → S_GANG 0.5 GR/BL → X60002-20 |
| X13635-3 | R<9 0.5 VI/GE | F9 5 A | same |
| X13635-4 | WFSI 0.35 BL/SW | → EWS X1659-8 (USA) | same |

#### D8.4 Cluster lamps: path per DME

| Lamp (cluster X11175 pin) | MS43-US (via X6011) | MS45 (CAN) | MSS54-US (via DME) |
|---|---|---|---|
| Oil pressure (13; lamp fed from 15<34 GN/BL on pin 5, F34 5 A) | 13 → S_OLD 0.35 BR/GN → X6011-3 → oil-pressure switch X6231-1 | X6231 → X60003-16 → DME → CAN | 13 ← X60004-11 S_OLD 0.35 BR/GN; DME ← X60003-26 ← X6231 |
| Oil level (17) | 17 ← F_OLN 0.5 WS/GN ← X6011-5 ← sensor X6254-3 (GR/BL); sensor feed X6254-1 via X6011-2/X6831; ground X6254-2 0.5 BR → X6053-4 → X6458 | sensor → X60003-50 → CAN; ground via X60531-4 | 17 ← X60004-21 F_OLN 0.5 WS/GN; DME ← X60003-39 (GR/BR); ground via X6053-4 |
| Charge (2) | 2 → S_61--1 0.35 BL → X6011-4 → 0.75 BL → alternator X6524-2 (alternator feed X6524-1 0.75 GN/BR via X6011-2) | alternator data line → X60003-19 → CAN | 2 ← X60004-1 0.35 BL; DME ← X60003-13 0.5 BL ← X6524-2 (to 2004_03); from 2004_03 via CAN |
| 30h start feedback (3) | 3 ← X276 ← S_30H 0.35 SW/GN ← X6011-6 ← starter X6511 (0.75 SW/GE) | conflict (D2) | 3 ← X276 ← X60004-2; DME ← X60003-12 ← X6511 |

#### D8.5 Cluster X11175 (26-pin black): pins used here (SP0000017540 to 2002_09; SP0000018656 from 2002_09)

| Pin | Signal | Pin | Signal |
|---|---|---|---|
| 1 | ground 31E<2 BR/SW → X217 | 9 / 10 | CAN-H / CAN-L |
| 2 | charge lamp (S_61) | 13 | oil-pressure lamp (S_OLD) |
| 3 | S_30H | 14 | K-bus WS/RT/GE |
| 4 | 30<43 RT/GE/WS (F43) | 17 | oil level (F_OLN) |
| 5 | 15<34 GN/BL (F34) | 19 | F_DFAHL GE/GN (road-speed output) |
| 6 | R<10 VI/GE (F10 5 A) | 25 | D_TXD1 WS/VI (diagnosis) |
| 7 | 58G GR/RT (to 2002_09 only) | | |

#### D8.6 Sport and switch centre

| Point | Wire | To | Source |
|---|---|---|---|
| X1869-17 FDYN | 0.35 SW/RT/GE | X60004-15 | SP0000014425 |
| X1869-18 FDYNLED | 0.35 SW/GR/GE | X60004-16 | SP0000014425 |
| X521-3 LED lighting | 58G 0.5 GR/RT | light module X12-47 via X1019/X908 | SP0000014425 |
| X521-4 ground | 0.75 BR → X219 (SP0000014425) or 31E<1 0.5 BR/SW → X10012 (SP0000015484) | — | conflict |
| X521-1 | 15<33 0.5 GN/BL/GE | F33 5 A | SP0000015484 |
| X1869-7 | 30<42 4.0 RT/VI | F42 30 A | SP0000015484 |
| X1869-23 | K-bus 0.35 WS/RT/GE | — | SP0000015484 |
| X1869-2 | S_RDKS 0.5 GE/SW | X6011-8 → X60003-19 | SP0000015484 |

#### D8.7 Fans

| Fan | Point | MS43 / MS45.1 Touring | MSS54-US |
|---|---|---|---|
| Electric fan M9 X82 | -2 control | T_ELUE 0.5 SW/GN ← X60004-4 | same |
| | -4 power | 30<37 6.0 RT/BL from F37 50 A | same |
| | -1 ground | 6.0 BR → X166/X165 (saloon/Touring) | → X14250/X14249 (coupe/convertible) |
| Radiator-outlet sensor X87 | -1 / -2 | → X60004-38 / -39 | same |
| E-box fan X6506 | -1 control | MS45 / MS43-US from 2003_03: S_EBOXL 0.5 BR/OR ← X60004-19. Earlier MS43: thermostatic switch B6235 (F28 5 A) | S_EBOX 0.5 BR/GE ← X60002-12 |
| | -2 | MS45: U_HR<3 supply | S_30H ← X276 |
| | -3 | — | U_HR<3 0.5 RT/WS |

#### D8.8 A/C relay K19 (X51)

| Pin | Wire | Function and destination |
|---|---|---|
| 8 | S_KOREL 0.5 SW/BL | ↔ X60004-29 (all families) |
| 2 | 30<63 0.75 RT/VI/GE | from F63 7.5 A |
| 6 | 0.75 SW/GR | → compressor clutch |
| 5 | — | → climate unit X610-9 |
| 4 | coil feed | U_HR via X6021-2/X11212 (non-M); the M3 drawing names U_HR<4 instead (inconsistency) |

#### D8.9 DME–EWS, CAN and speed

| Point | Wire | Same on all families? |
|---|---|---|
| X60004-33 ↔ EWS X1659-4 | D_EWS 0.35 SW/VI | yes |
| X60004-36 / -37 → X1893 / X1894 → cluster X11175-9/10, DSC MK60 X18303-11/15, steering-angle sensor, adaptive headlights (AHL, where fitted) | 0.5 GE/RT / 0.5 GE/BR | yes (MK20 DSC: X1746-17/16). No terminating resistors drawn |
| X60004-22 ← X1101 ← DSC X18303-8 | F_DFAHR 0.35 WS/GN | yes |

#### D8.10 OBD socket X19527 (16-pin), SP0000014297

| Pin | Signal | Wire | From |
|---|---|---|---|
| 1 | 15<30 | 0.75 GN/BR | F30 |
| 4 | 31L<3 | 0.5 BR | → X173 |
| 5 | 31E<2 | 0.5 BR/SW | → X1108 |
| 7 | D_TXD2 | 0.5 WS/VI | DME X60004-32 (and automatic-gearbox unit) |
| 8 | D_TXD1 | 0.35 WS/VI | → X183 (body diagnosis bus via the cluster gateway) |
| 9 | F_TD | 0.35 SW | → X243 (engine speed from X60004-17) |
| 16 | 30<43 | 0.5 RT/GE/WS | F43 5 A |
| 6, 14 | no CAN | — | — |

### D9. Re-pin lists derived from the factory drawings

These are **inferences built from the WDS data above**. Each row cites the drawings it rests on. Forum practice is in `swap_repin_practice.md`.

#### D9a. MS43 Touring built from 09/2001 (US, manual), MSS54 donor

| # | Action | Wire | Basis |
|---|---|---|---|
| 1 | Body X6011-7 → **X60004-18** | DMTLH 0.75 SW/RT | SP0000017260, SP0000017646 |
| 2 | Body X6011-3 → **X60004-11** | S_OLD 0.35 BR/GN | SP0000017260, SP0000014396, SP0000007269 |
| 3 | Body X6011-4 → **X60004-1** | S_61--1 0.35 BL | SP0000017260, SP0000014363, SP0000014362 |
| 4 | Body X6011-5 → **X60004-21** | F_OLN 0.5 WS/GN | SP0000017260, SP0000014397, SP0000014426 |
| 5 | Body X6011-6 → **X60004-2** (not 6) | S_30H 0.35 SW/GN | SP0000017260, SP0000014365, SP0000014364 |
| 6 | X60004-28 → **X60004-34** | S_BLTS 0.35 BR/GR | SP0000017224, SP0000014399 |
| 7 | X60004-23 → **body X6011-7** (after row 1) | S_KUP 0.35 BL/BR (clutch module pin 2) | SP0000016193, SP0000016194, SP0000014314. It then meets the M3 harness's S_GANG at X6011-7 → X6053-5 → gear switch → X60002-20. WDS cannot show whether the 325i clutch module's output suits the MSS54 input; earlier notes say the modules differ [earlier] |
| 8 | X60004-20 / -30 | no change on the drawings | D8.2. Verify (D12) |
| 9 | X60004-10 | keep | Touring K96. US MSS54 behaviour: see D8.1 note |
| 10 | Optional: add X60004-5 → ground X1108 type | new 0.35 BR/SW | M3 module-4 drawings |
| 11 | Optional: add X60004-6 ← terminal 50 | new 0.35, SW/BL to match | M3 module-4 drawings; consumer unknown |
| 12 | Optional: X60004-15 / -16 ← X1869-17 / -18 | 0.35 SW/RT/GE, SW/GR/GE | SP0000014425; Touring may lack the switch-centre wiring |
| 13 | X6011-1/-2 | as is | — |
| 14 | X6011-8 | only with MK20-era tyre-pressure reset | SP0000014314; [NAM3 243029](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/243029-e46-m3-tpms-x60003-to-x6011-question) |
| 15 | X6021 | Touring has pins 2–4; the M3 harness's pin 1 (US pump signal) finds no mate; leave it | SP0000007729, SP0000014315 |

#### D9b. MS43 Touring built before 09/2001 (differences from D9a)

- **No body X6011-7 wire** (unheated DM-TL). Row 7's clutch wire takes the empty X6011-7 cavity, using a new terminal in the body housing.
- **DM-TL with a from-2001_09 MSS54:** the M3 DME expects the 4-wire heated module (heater on 18). Fit 16 13 7 193 479 and add a heater wire and a module plug to match. The Touring's 3-wire module pins: X6139-1 = 0.75 BR/BL (DME 30); X6139-2 = 0.5 SW/GN (DME 20); X6139-3 = supply. Basis: ETK and SP0000014355.
- **DM-TL with a pre-2001_09 M3 donor DME:** that DME uses 28 (0.5 SW/GN, module pin 2) and 30 (0.75 BR/BL, module pin 1). By wire and module pin, the Touring's pin-20 wire would go to **28** (after moving S_BLTS 28 → 34) and pin 30 stays. Inference; WDS names conflict.
- **Touring built before 03/2001:** clutch *switch* S32 instead of the clutch module (SP0000014357).

#### D9c. MS45.1 Touring built from 03/2003 (US, M54, manual), MSS54 donor

| # | Action | Wire | Basis |
|---|---|---|---|
| 1 | X60004-2 → **X60004-18** | S_DMTLH 0.75 SW/RT | SP0000018609, SP0000017646 |
| 2 | X60004-5 out, insulate | M_SHFM 0.5 SW/GE (secondary-air sensor) | SP0000018609, SP0000019608; ETK sensor from Mar '03 |
| 3 | X60004-15 out, insulate | A_SHFM 0.5 SW/RT | same |
| 4 | X60004-19 out, insulate (if populated) | S_EBOXL 0.5 BR/OR | SP0000017918; the M3 harness drives its own E-box fan from X60002-12. Use one or the other |
| 5 | X60004-28 → **X60004-34** | S_BLTS 0.35 BR/GR | SP0000018609 |
| 6 | X60004-23 → **body X6011-7** (new terminal; MS45 X6011 has only 1–2) | S_KUP 0.35 BL/BR | SP0000016193, SP0000018632, SP0000016194 |
| 7 | X60004-20 / -30 | no change on the drawings | D8.2; verify (D12) |
| 8 | Add X60004-11 → cluster X11175-13 | new 0.35 (BR/GN to match the M3) | SP0000007269; the MS45 lamp is CAN-only (SP0000018655) |
| 9 | Add X60004-21 → X11175-17 | new 0.5 (WS/GN) | SP0000014426 versus SP0000017919 |
| 10 | Add X60004-1 → X11175-2 | new 0.35 (BL) | SP0000014362. Not needed if the donor DME and cluster coding run the charge lamp over CAN (SP0000021003) |
| 11 | X60004-2 ← S_30H | only if the Touring's body has the X276 / X6011-6 wire | conflict SP0000014365 versus SP0000018632; check the car |
| 12 | X60004-10 | keep | SP0000014336 |
| 13 | Optional: X60004-5 ground, X60004-6 terminal 50, X60004-15/16 Sport | as D9a rows 10–12 (after clearing rows 2–3) | — |
| 14 | X6053 / X60531 | do not mix harness sections | D4 |

Whether the cluster's pins 2/13/17 are populated on an MS45.1 Touring was not checked (needs ISTA by VIN or a look at the plug). Cluster coding for CAN versus wired lamps is covered in sibling notes, not here.

### D10. Connector cavity layouts (WDS SX drawings; viewing side not stated)

Only the corner numbers are printed in WDS. In-between numbers are inferred as consecutive.

**X60004 (40-pin black; image B400001; socket symbol)**
```
upper block   31 32 33 34 35 36 37 38 39 40
              21 22 23 24 25 26 27 28 29 30
lower block   11 12 13 14 15 16 17 18 19 20
               1  2  3  4  5  6  7  8  9 10
```

**X60001 / X60005 (9-pin; image B090009)**
```
9 8 7
6 5 4
3 2 1
```

**X60002 (24-pin; image B240002)**
```
upper block   24 23 22 21 20 19
              18 17 16 15 14 13
lower block   12 11 10  9  8  7
               6  5  4  3  2  1
```

**X60003 (52-pin; image B520001)**, 13 cavities per row:
```
upper block   52 51 50 49 48 47 46 45 44 43 42 41 40
              39 38 37 36 35 34 33 32 31 30 29 28 27
lower block   26 25 24 23 22 21 20 19 18 17 16 15 14
              13 12 11 10  9  8  7  6  5  4  3  2  1
```

**X6011 (8-pin black, "Engine plug I"; image B080032; pin symbol)**
```
5 6 7 8
1 2 3 4
```

**X6053 (8-pin natural; image B080002D; round cavities; socket symbol)**
```
4 3 2 1
8 7 6 5
```

**X6021 (4-pin black; image B040036A; socket symbol)**
```
1 2 3 4
```

**Cluster X11175 (26-pin black; image B260005C)**
```
 1  2  3  4  5  6  7  8  9 10 11 12 13
14 15 16 17 18 19 20 21 22 23 24 25 26
```

**Switch centre X1869 (23-pin; image B230001)**: top row 13 … 1 (13 at left), bottom row 23 … 14 (23 at left), in uneven groups.

**Clutch module X13635 and brake switch X78 (4-pin; image B040021B)**
```
4 3 2 1
```

**K96 relay socket X10156 (9-pin; image B090005C)**
```
3 6 9
. . .   (middle row not numbered; presumably 2 5 8)
1 4 7
```

**DM-TL X17140 / X1714 (4-pin; image B040034A)**
```
  3   1
4   2
```

**OBD X19527 (16-pin; image B160004)**
```
 8  7  6  5  4  3  2  1
16 15 14 13 12 11 10  9
```

**EWS X1659 (13-pin; image B130005A)**
```
13 12 11 10  9
 8  7  6  5  4  3  2  1   (3–1 are wide cavities)
```

### D11. Housings and terminals (ETK, US 325i Touring; DME housings also on the US M3)

| Item | Part number(s) | ETK text |
|---|---|---|
| 9-pin DME socket housing / cap | 12 52 1 744 624 / 12 52 7 502 456 | — |
| 24-pole "/A" housings / cap | 12 52 1 744 627, 12 52 1 744 628 / 12 52 1 744 626 | — |
| 52-pole "/A" housings / cap | 12 52 1 744 633, 12 52 1 744 634 / 12 52 1 744 632 (to Jul '03) or 12 52 7 526 424 | — |
| 40-pole "/B" housings / cap | 12 52 1 744 630, 12 52 1 744 631 / 12 52 1 744 629 | — |
| MLK 1.2 socket terminals | 12 52 7 510 668 | 0.25–0.5 Sn |
| | 12 52 7 510 670 | 0.5–1.0 Sn, with grommet 12 52 7 503 411 |
| | 12 52 7 510 671 | 0.25–0.5 Ag |
| | 12 52 7 510 672 | 0.25–0.5 Sn |
| | 12 52 7 510 673 | 0.5–1.0 Ag |
| | 12 52 7 510 674 | 0.5–1.0 Sn |
| | 12 52 7 502 929 | 0.25–0.5 Sn, discontinued |
| | 12 52 7 502 932 | 0.25–0.5 Ag |
| | 12 52 7 564 537 | 0.35 Ag |
| | 12 52 7 532 371 | 0.25–0.5 Ag |
| | 12 52 7 560 453, 12 52 7 560 455 | 0.5 Ag |
| Bushing contacts | 12 52 0 030 685 | 0.35 |
| | 12 52 0 143 438 | 0.25–0.5 Ag |
| | 12 52 0 143 439 | 0.5–1.0 Ag |
| Flat plug MLK 1.2 | 12 52 7 512 135 | 0.5 Ag |
| SLK 2.8 socket with wire | 12 52 0 007 168 | 0.25–0.5 |
| | 12 52 0 007 171 | 0.5–1.0 |
| SLK 2.8 ELA with wire | 12 52 0 007 170 | 0.2–0.5 |
| | 12 52 0 007 172 | 0.5–1.0 Sn |
| | 12 52 0 143 427 | 0.2–0.5 Ag |
| | 12 52 0 143 433 | 0.5–1.0 Ag |
| | 12 52 0 143 434 | 2.5–4.0 Ag |
| Microtimer blade with wire | 12 52 0 007 251 | 0.5 |
| MDK4 2.8 blade with wire | 12 52 0 007 252 | 1.0 Sn |
| | 12 52 0 007 253 | 2.5 Sn |
| | 12 52 0 007 254 | 0.5 Au |
| | 12 52 0 007 255 | 1.0 Au |

Sources: [basic control unit DME](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/basic_cotrol_unit_dme/), [contact system MLK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/contact_system_mlk/) and [laminated/spring contacts](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/engine_electrical_system/laminated_contacts_spring_contacts/) [read]. No source maps these terminals to X60004 or X6011 cavities.

### D12. Checking the DM-TL and other moved circuits on the car

Job names come from the EDIABAS documentation [read]. How to use them is inference.

| When | DME | Jobs |
|---|---|---|
| Before removing the Touring's DME | MS43 (MS430DS0) | STEUERN_DMTL_MOTOR, STEUERN_DMTL_VENTIL, STEUERN_DMTL_HEIZUNG, STEUERN_EKP, STEUERN_E_LUEFTER |
| Before removing the Touring's DME | MS45.1 (MS450DS0) | STEUERN_DMTL_P, STEUERN_DMTL_V, STEUERN_DMTL_H (each with an _ENDE job), STATUS_DMTL_P / _V / _H, STEUERN_EKP, STEUERN_E_LUEFTER, STEUERN_SLP |
| After the swap | MSS54 (MSS54DS0) | STEUERN_DMTL_HEIZUNG / STEUERN_DMTL_HEATER, START_SYSTEMCHECK_DMTL then LESEN_SYSTEMCHECK_DMTL, STEUERN_EKP / STEUERN_EKP_AUS, STEUERN_SLP, STEUERN_E_LUEFTER |

- **Before removal:** run each job and note which X60004 wire switches (test lamp or meter at the back of the plug). Label each wire with its function.
- **After the swap:** MSS54DS0 has **no separate pump or valve actuation job**. Pump/valve order shows only through the system check result and the fault memory.
- **Bench check of the DM-TL module** (inference): with the module unplugged, feed +12 V through a fused lead to module pin 4 (pin 3 on the 3-wire unit). Briefly ground pin 1, then the other pump/valve pin. The pump runs on one and the valve clicks on the other. Combined with D8.2 (DME pin → module pin), this shows which X60004 pin must carry the MSS54's pump output.

---

## Open items

1. **Viewing side of WDS connector views.** Not stated; X60004 numbers its rows the opposite way to X60001/2/3/5. Use the numbers moulded on the housing.
2. **DM-TL 20/30 on MS45.1 Tourings.** The factory drawings say the wiring is identical to the M3; the pin-table labels and forum practice say swap. Settle by test (D12).
3. **WDS colour and size conflicts:**
   - X60004-26 is GN/VI on the module drawings and GN/SW on the MS43 supply drawings.
   - MS43 pins 20/30 colours differ between SP0000017224 and SP0000017277.
   - The X6011-3 engine-side lead (MS43) is printed "2.5 BR/GR" on the plug drawings and 0.5 BR/GN on the oil-pressure drawing.
   - The switch-centre X521-4 ground differs between SP0000014425 and SP0000015484.
   - K19 coil feed U_HR versus U_HR<4.
4. **X6011-6 (S_30H) on MS45 cars:** SP0000014365 versus SP0000018632.
5. **What feeds MSS54 X60004-6 (splice X18820), and what the DME does with pins 5 and 6.** Not shown.
6. **Terminals and housings.** No cavity-to-terminal part mapping for X60004/X6011. No ETK part numbers found for the X6011/X6021 housings and terminals.
7. **US MSS54 driving X60004-10.** No WDS drawing shows a US M3 using pin 10, so whether US software drives it is not shown (forum reports say yes [earlier]).
8. **Touring E-box fan and cluster pins.** Whether a given MS45.1 Touring has the E-box fan (pin 19) and populated cluster pins 2/13/17 is unknown. Check by VIN in ISTA or by looking at the plugs.
9. **Charge lamp over CAN.** The from-2004_03 drawing puts it on CAN, but whether a given donor's software does so (and how the cluster is coded) is not answered by WDS.
10. **Unread sources.** Bentley ETM, ISTA, newTIS and bmwteka were not read (paywalled, blocked or unreachable).
11. **X60531 (spade-pin) plug.** The forum report (Oct '03 versus Jul '04) suggests a change during MS45.1 production. The exact date is unknown.
