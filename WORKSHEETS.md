# Worksheets

Print these sheets and fill them in by hand, or fill them in here on a phone or computer: type in the blank cells and tick the boxes. What you enter is saved in this browser on this device only, so print the records you need to keep, or save them as a PDF from the print dialog.

## Touring baseline record

**Phase 0,** before you change anything. The guide's [Check your own Touring first](README.md#check-your-own-touring-first) explains each item. An xi, an M56 SULEV or an ASC-only car changes the plan: re-plan the axle, fuel or DSC parts before you buy a donor.

| Item | Look for | Record |
|---|---|---|
| VIN | All 17 characters | |
| Model, from the VIN decode | 325i, not 325xi | |
| Build date | From 09/2001: facelift, vehicle order (FA). Before: ZCS | |
| Option codes | — | |
| Engine code | M54B25, not M56 SULEV; a manual gearbox doesn't prove an M54 | |
| Emissions (VECI) label, under the hood | Test group and category: LER = LEV, the S54's category; UL2 or SMG = ULEV; M56 = SULEV. Photograph it ([Massachusetts](README.md#massachusetts)) | |
| Fuel tank | Plastic, not the M56's sealed metal tank | |
| DME family and part number | E-box label: MS43 to 02/2003, MS45.1 from 03/2003 ([how to tell](WIRING-AND-CODING.md#which-dme-your-touring-has)) | |
| Leak-test heater wire (0.75 SW/RT) | In X60004 pin 2: MS45.1. In the body side of X6011 pin 7: MS43 from 09/2001 | |
| X60004 pins 5, 15 and 19 | Wires in 5 and 15 (0.5 SW/GE, SW/RT): MS45.1. Note whether 19 holds one | |
| DSC unit and part number | Hydraulic-unit label: MK60, not ASC only | |
| Climate control | IHKA or IHKR; A/C with IHKR should work by BMW's description, but nobody has reported it with the S54 | |
| A/C | Blows cold, before recovery in Phase 4 | |
| Console switches fitted | A switch center, or only a DSC button | |
| Headlights | Halogen or xenon | |
| Door mirror harness | Ribbon cable on facelift doors | |
| State's written answer | In hand before you buy the donor | |

### Mileage

| Reading | Mileage | Date | Photo or file |
|---|---|---|---|
| Odometer, as the cluster shows it | | | |
| Light module (LCM), read with PA-Soft | | | |

> [!CAUTION]
> This is your car's true mileage, and after Phase 11 the M3 cluster must show it. Never write a mileage into the light module ([Instrument cluster and mileage](README.md#instrument-cluster-and-mileage), [49 U.S.C. §32704](https://www.law.cornell.edu/uscode/text/49/32704)).

## Touring shell record

**Phases 0 and 4** ([what to look for](README.md#rear-subframe-mount-reinforcement)). Copy your last alignment printout into the [alignment table](#alignment).

### Shell inspection

Mounts from above and below. Cracks: repair in Phase 5; torn or rotten floor: body-shop quote first.

| Area | Phase 0 finding | Phase 4 finding (stripped) |
|---|---|---|
| RACP at the left front subframe mount | | |
| RACP at the right front mount | | |
| RACP at the left rear mount | | |
| RACP at the right rear mount | | |
| RACP front edge and V-beam ends | | |
| Rails and their boot-floor spot welds | | |
| Rear arches: inner lips, inner arches | | |
| Sills, jacking points, battery box | | |
| Floor at the tank and brake-pipe brackets | | |

**Ride height,** at normal ride height: the car on its wheels on level ground, unladen, at placard tire pressures, measured up from the floor as you'll measure the donor in Phase 1 ([Phase 0](README.md#phase-0-paperwork-and-baseline), step 7):

| Measurement | Front left | Front right | Rear left | Rear right |
|---|---|---|---|---|
| Hub center (mm) | | | | |
| Arch lip, straight above the hub center (mm) | | | | |
| Hub to lip: lip minus hub (mm) | | | | |

| Condition | Record |
|---|---|
| Date, fuel level and tire pressures | |

**Photos:**

- [ ] Engine bay, the E-box with the DME label readable, and the harness routing
- [ ] Underside, and the RACP at all four subframe mounts, top and bottom
- [ ] Rear arches, sills, jacking points, battery box and the floor around the tank brackets
- [ ] Rear door gaps, and the door-jamb labels with the axle load ratings

## Electronics baseline

**Phases 0 and 1.** Prove the kit on your unmodified Touring ([Before you start](WIRING-AND-CODING.md#before-you-start)), then read both cars' modules.

**Coding kit:**

- [ ] Windows 10 or 11 laptop running natively, on its charger; a battery charger of at least 10 A
- [ ] K+DCAN USB cable with a genuine FTDI chip, OBD pins 7 and 8 bridged; PA-Soft interface and driver
- [ ] COM1 in Device Manager, matching Port=Com1 in obd.ini; latency timer 1 ms; EDIABAS STD:OBD
- [ ] INPA 3.0.1 or 4.4.7: two owners' builds, one labelled "EA-90X 5.00" and one "5.0.2", lacked the MK60 steering-angle page (Tool32 runs the job either way); NCS Expert 3.0.x
- [ ] INPA shows two solid black dots and reads the DME, cluster, light module, EWS and DSC
- [ ] NCS Expert reads the vehicle order (FA), or the ZCS on a car built before 09/2001

**Touring modules** (Phase 0):

| Module | Part number | Software or coding index | Faults found |
|---|---|---|---|
| DME (MS43 or MS45.1) | | | |
| Cluster (KMB or AKMB) | | | |
| Light module (LSZ or ALSZ) | | | |
| EWS | | | |
| DSC | | | |
| GM5 | | | |
| Climate control (IHKA or IHKR) | | | |
| Airbag | | | |

**Before your Touring's DME comes out** (Phase 0, or Phase 4 at the latest): run each job in Tool32 (`MS430DS0.PRG` on an MS43, `MS450DS0.PRG` on an MS45.1) with a test lamp or meter at the back of the plug, and tag each wire with what it does ([DM-TL leak-test pump](WIRING-AND-CODING.md#dm-tl-leak-test-pump-test-before-you-swap)).

| Job | Where to look | Wire that switched: plug, pin, color | What ran or clicked | Tagged ✓ |
|---|---|---|---|---|
| Leak-test pump: MS43 `STEUERN_DMTL_MOTOR`; MS45.1 `STEUERN_DMTL_P` | X60004 pin 20 or 30: find out which | | | |
| Leak-test valve: MS43 `STEUERN_DMTL_VENTIL`; MS45.1 `STEUERN_DMTL_V` | The other of pins 20 and 30 | | | |
| Leak-test heater: MS43 `STEUERN_DMTL_HEIZUNG`; MS45.1 `STEUERN_DMTL_H` | MS45.1: X60004 pin 2. MS43 from 09/2001: body X6011 pin 7 | | | |
| Pump relay: `STEUERN_EKP` | X60004 pin 10; K96 clicks | | | |
| Electric fan: `STEUERN_E_LUEFTER` | X60004 pin 4 | | | |

**Donor modules** (Phase 1):

| Module | Part number | Software or coding index | Faults found |
|---|---|---|---|
| DME (MSS54 or MSS54HP) | | | |
| DSC (MK20 or MK60) | | | |
| Cluster | | | |
| Light module | | | |
| EWS | | | |
| Airbag | | | |

## Coding backups log

**Phase 0** for your Touring, **Phase 1** for the donor, then before and after each coding session ([Back up everything first](WIRING-AND-CODING.md#back-up-everything-first)). Keep two copies of every file, one of them off the laptop. Tick **Re-read** once you've opened the saved file, or read the module again, and found it complete.

| Backup, and the tool | File name | Date | Re-read ✓ | Copy 1 | Copy 2 |
|---|---|---|---|---|---|
| FA or ZCS screenshots: VIN, options, production date, type code (NCS Expert) | | | | | |
| Cluster coding, KMB or AKMB, `FSW_PSW.TRC` (NCS Expert) | | | | | |
| Light-module coding, LSZ or ALSZ (NCS Expert) | | | | | |
| GM5 coding (NCS Expert) | | | | | |
| DSC coding (NCS Expert) | | | | | |
| EWS coding, with `PARK/NEUTRAL_EINGANG` = `aktiv` (NCS Expert) | | | | | |
| Climate-control coding, IHKA or IHKR (NCS Expert) | | | | | |
| Cluster EEPROM (PA-Soft) | | | | | |
| Light-module EEPROM (PA-Soft) | | | | | |
| Fault memories, every module (INPA) | | | | | |
| DSC part number and coding index (INPA or PA-Soft) | | | | | |
| Donor: every module's identity and faults (INPA) | | | | | |
| Donor DME: `IDENT` and `FS_LESEN` (Tool32, `MSS54DS0.PRG`) | | | | | |
| Donor DME: VIN slots, `AIF_LESEN` (Tool32, `12MSS54.PRG`) | | | | | |
| Donor DME partial read, for a DIY delete only; 32 kB means an MSS54, 64 kB an MSS54HP (BMWFlash) | | | | | |
| Donor cluster EEPROM, kept untouched (PA-Soft) | | | | | |
| Donor light-module coding (NCS Expert) | | | | | |
| DME back from the vendor: `IDENT`, `FS_LESEN`, `AIF_LESEN` (Tool32) | | | | | |
| Cluster before and after Session 4: EEPROM, VIN and mileage screenshots (PA-Soft) | | | | | |
| Cluster coding as written, `FSW_PSW.MAN` (NCS Expert) | | | | | |
| M3 DSC coding as written, option B only (NCS Expert) | | | | | |
| First start: `IDENT` and `FS_LESEN` (Tool32) | | | | | |
| Vehicle order after a Session 8 change (NCS Expert) | | | | | |
| Light-module coding after Session 9 (NCS Expert) | | | | | |

### Donor DME VIN slots

Run `AIF_LESEN` with argument 1, then 2, 3 and so on, and record each slot ([Session 2](WIRING-AND-CODING.md#session-2-dme-vin-ews-delete-and-gearbox-software)).

| Slot | VIN | Software number | Authority number | Assembly number |
|---|---|---|---|---|
| Slot 1 | | | | |
| Slot 2 | | | | |
| Slot 3 | | | | |
| Slot 4 | | | | |
| Slot 5 | | | | |

| Item | Record |
|---|---|
| Free slots left, `AIF_ANZ_FREI` | |
| First slot with an empty `AIF_FG_NR`, and its `AIF_ADRESSE_LOW` | |
| After the vendor: your Touring's full VIN in the AIF (`AIF_LESEN` with argument 0) | |
| A generic OBD-II scanner shows your Touring's full VIN | |

## Donor M3: record and tests

**Phase 1,** while the car still runs and before anything comes off. How to run each test: [Choose the donor](README.md#choose-the-donor) (Test it while it still runs) and [Phase 1](README.md#phase-1-buy-and-inspect-the-donor).

### The donor

| Item | Look for | Record |
|---|---|---|
| VIN | — | |
| Build date | It sets the DME, DSC, wheel-speed sensors, leak-test layout (heater output from 09/2001), rod bolts and cluster | |
| Model year | Your Touring's, or newer | |
| Body | Coupe or convertible | |
| Gearbox | Manual; an SMG car's DME needs manual software | |
| Engine number | Photographed | |
| DME and part number | MSS54 to about 09/2003, MSS54HP after | |
| DSC unit and part number | MK60 from 09/2002; an MK20 won't plug in | |
| Rod bolts to expect | M11 to 12/12–13/2002 (vendors: 02/2003), then M10; go by the heads | |
| Cluster coding index | 20–22 early (20 or 21: Motometer); 23–24 redesign, preferred | |
| Competition package (ZCP) | From 12/2004 | |
| Switch-center buttons | — | |
| Wheel-speed sensors | From 09/2002 (MK60): the same type as yours. Before (MK20): they don't fit your harness | |

### Compression and leak-down

Warm engine, all plugs out. About 11–12 bar (160–174 psi) minimum, about the same on every cylinder (a compilation figure: confirm it in TIS). No leak-down figure turned up; judge how even they are.

| Cylinder | Compression (bar or psi) | Leak-down (%) |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |
| 6 | | |

### VANOS tests

Warm, after `STEUERN_LLS_TESTDREHZAHL` (raised idle), as in [Session 6](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check), step 7. No BMW limits were found: compare after the refresh.

| Test | Donor (Phase 1) | After the refresh (Phase 12) |
|---|---|---|
| Rattle at warm idle | | |
| `STEUERN_EVANOS1_VERSTELLZEIT` | | |
| `STEUERN_AVANOS1_VERSTELLZEIT` | | |
| `STEUERN_EVANOS1_DICHTHEIT` | | |
| `STEUERN_AVANOS1_DICHTHEIT` | | |
| VANOS faults stored | | |
| Exhaust-hub tabs and oil-pump disc, valve cover off, if the seller allows | | — |

**Fuel pressure,** gauge on the feed, pump run through a relay bypass as BMW's test does:

| Test | Pass | Result |
|---|---|---|
| Static pressure | 5.0 ± 0.2 bar (72.5 ± 2.9 psi) | |
| 20 minutes later | Still above 4.5 bar | |

**Road test:**

- [ ] No knock at warm idle; no diff clunk or whine
- [ ] Clean shifts into all six gears and reverse, without a grind
- [ ] Clutch, steering and brakes normal; DSC and ABS lights out; ABS works in a careful hard stop on a quiet road
- [ ] The A/C blows cold and its compressor engages

**Donor paperwork:**

- [ ] Title or salvage paperwork and a bill of sale; engine number and VIN plates photographed
- [ ] Refrigerant recovery booked while the car can still be driven or towed to a shop

## Donor arch targets

**Phase 1,** on a level floor before teardown: your Phase 6 targets ([method](README.md#measure-and-mock-up-before-you-cut), step 1).

### Arch targets

Placard pressures. A to C up from the floor; D by plumb line from the lip. Front corners: reference only.

| Measurement | Front left | Front right | Rear left | Rear right |
|---|---|---|---|---|
| A. Hub center | | | | |
| B. Arch lip, straight above the hub center | | | | |
| C. A body point both cars share, such as the floor beside a rear subframe mount | | | | |
| D. Lip outboard of the tire's outer face | | | | |
| Hub to lip: B minus A | | | | |
| Hub to body: C minus A | | | | |

| Condition | Record |
|---|---|
| Date, fuel level, tire pressures | |
| The body point you used, and how to find it on your Touring | |

**Labels and photos:**

- [ ] B-pillar tire placard
- [ ] Underhood A/C and emissions labels
- [ ] Engine number and VIN plates

**Trace before you strip it** (the manual's [donor list](WIRING-AND-CODING.md#back-up-everything-first)):

| Item | What you found |
|---|---|
| Donor's body-side X60004 pin 5: WDS shows a 0.35 BR/SW ground wire to point X1108. Confirm it, then add the same to yours (recommended) | |
| Donor's X6011 pin 7: the gray clutch wire, 0.35 GR on the body side from the clutch module, 0.5 GR on the engine side on to X6053 pin 5 and the gear switch | |
| Donor's clutch-switch module, 61319122700, taken | |
| SMG donor only: a gear-switch wire at X60002 pin 20? An SMG harness has none: add one | |

## S54 refresh measurements

**Phase 3,** engine on the stand. Limits and method: [S54 refresh on the stand](README.md#s54-refresh-on-the-stand); torques in the [torque log](#torque-log).

**Rod bearings.** By the heads: 12-point (12 mm socket) is M11, reused in its own hole, tightened once (log as cycle 1); E-Torx (E12) is M10, new, three cycles. Plastigauge with the old bolts: 0.040–0.070 mm.

| Item | Spec | Record |
|---|---|---|
| Rod-bolt heads | 12-point (M11) or E-Torx E12 (M10) | |
| Crankshaft end play, dial gauge | 0.141–0.253 mm (0.0056–0.0100 in) | |

| Rod | Clearance (mm) | Cycle 1 | Cycle 2 | Cycle 3, final | Notes, ARP free length |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |

**Valve clearances (mm),** coolant below 35 °C, lobe straight up. New shim = old + clearance − target (aim 0.20, 0.30).

| Cylinder | Intake 0.18–0.23 | Exhaust 0.28–0.33 | Shims changed |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |

**VANOS refresh:**

- [ ] New seals and oil-pump disc; hub tabs intact or hub replaced; cam bridge flat, crank pin slides in

## Floor and welding log

**Phase 5,** and after every welding session in Phases 5 and 6. Method: [Welding settings and safety](README.md#welding-settings-and-safety). The *Subframe mount reinforcement* and *Rear floor reinforcement plan* diagrams in [Rear subframe mount reinforcement](README.md#rear-subframe-mount-reinforcement) show where the mounts sit.

### Panel thickness

Measure with a vernier caliper at a cut edge.

| Part | Guide's figure | Measured (mm) |
|---|---|---|
| Your trunk floor | Not published; the guide assumes roughly 0.8–1.2 mm (estimate) | |
| Your RACP | Not published; the guide assumes roughly 0.8–1.2 mm (estimate) | |
| Your arch skin | Not published; the guide assumes roughly 0.8–1.2 mm (estimate) | |
| Your kit's plates | Properparts 1.5 mm; Condor 14 gauge (about 1.9 mm); CMP rail plates 2.5 mm, zinc-coated | |
| Arch repair sections, if bought | LBL M3 arch sections 1.2 mm (unverified) | |

### Test coupons

For each new combination of thicknesses, weld coupons of the same materials in the position you'll use, overhead included, with plug welds through holes the size of the kit's, and break one in a vise. Start from the chart in your welder's door. Miller recommends 0.023–0.024 in (0.6 mm) wire for body panels up to 1/16 in (1.6 mm), 0.030 in (0.8 mm) wire for 20 gauge to 1/8 in, and 75/25 argon/CO2.

| Coupon | Thicknesses | Position | Wire, gas, settings | Fused, no blow-through |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

### Body diagonals

Mark the four rear subframe mounting points and the front subframe points, and measure both diagonals across each set with a tape or tram gauge; a plumb bob down to the floor helps. LF is the left front point, RR the right rear, and so on; write millimetres. If a figure changes, the floor is pulling: stop, compare with BMW's body dimensions in TIS (group 51 00), and have a body shop with a jig check it.

| Points | How you marked them |
|---|---|
| Rear subframe mounting points | |
| Front subframe points | |

| When | Date | Rear LF–RR | Rear RF–LR | Front LF–RR | Front RF–LR |
|---|---|---|---|---|---|
| Before the first weld | | | | | |
| After session 1 | | | | | |
| After session 2 | | | | | |
| After session 3 | | | | | |
| After session 4 | | | | | |
| After session 5 | | | | | |
| After session 6 | | | | | |
| After session 7 | | | | | |
| After session 8 | | | | | |
| After session 9 | | | | | |
| After session 10 | | | | | |
| After session 11 | | | | | |
| After session 12 | | | | | |
| Floor closed (Phase 5, step 10) | | | | | |
| Arches welded, before sealing | | | | | |

## Arches and doors

**Phase 6.** Method: [Measure and mock up before you cut](README.md#measure-and-mock-up-before-you-cut). The *Rear quarter cut lines* and *Arch section and wheel offsets* diagrams in [Rear arches and doors](README.md#rear-arches-and-doors) show where the new lip goes.

**Rear door gaps,** with feeler gauges at points you mark: before any welding, and again with the arches on.

| Gap | Left, before | Left, arches on | Right, before | Right, arches on |
|---|---|---|---|---|
| Point 1 | | | | |
| Point 2 | | | | |
| Point 3 | | | | |

**Mock-up,** with the final dampers, brakes, wheels and tires at road pressure, springs out. Targets: the donor's [arch targets](#arch-targets), or yours if your springs set the car higher or lower.

| Measurement | Left target | Left as set | Right target | Right as set |
|---|---|---|---|---|
| Hub to body (jack the hub to it) | | | | |
| Hub to lip: the lip mark's height above the hub center | | | | |
| Lip mark outboard of the tire's outer face | | | | |
| Lip mark to the same center point on the floor | — | | — | |

- [ ] Donor steel checked against your Phase 2 templates: shape matches, no accident damage
- [ ] Full bump: each tire clears the inner wheelhouse, brake lines and planned lip
- [ ] Right side: the Touring's filler neck reaches the M3 filler pot

**After welding,** before you seal and prime:

| Must match side to side | Left rear | Right rear |
|---|---|---|
| Lip height above the hub center | | |
| Lip offset from the car's center line | | |

- [ ] Tires clear the lips and inner arches at full bump; inner lips a sealed double skin all round
- [ ] Filler neck reaches and seals in the M3 pot; the flap opens and closes
- [ ] Doors open and close freely; the body diagonals still match

## Torque log

**Phases 3 to 12.** Values are copied from the guide's [Torque values](README.md#torque-values), which gives the source for each; confirm compilation and video values in TIS. "New" means fit a new fastener. Write the date under **Done**, and tick **Marked** once the fastener is paint-marked.

### Phase 3: on the bench

| Fastener | Value | Notes | Done | Marked |
|---|---|---|---|---|
| Rod bolts, M11×1.25 with a 12-point head (12 mm socket); engines built before the change-over in mid-December 2002 | 5 Nm (44 in-lb), then 30 Nm (22 ft-lb), then 70° in one single stroke | Reuse each bolt in the hole it came from | | |
| Rod bolts, M10×1.25 with an E-Torx head (E12); engines built from the change-over | Three cycles. Each cycle: 5 Nm, 30 Nm, then 105° in one single stroke. After cycles 1 and 2, back each bolt off about one turn. Cycle 3 is final | New bolts every time: 11247834310, 12 per engine. Log each rod on the [S54 refresh sheet](#s54-refresh-measurements) | | |
| ARP rod bolts, if fitted | 201-6103 (M11): stretch 0.19–0.20 mm (0.0075–0.0080 in), or 95 Nm (70 ft-lb) with ARP Ultra-Torque. 201-6102 (sold for M10 engines; the sheet names the S50 Euro): stretch 0.165–0.178 mm (0.0065–0.0070 in), or 68 Nm (50 ft-lb) | Never use BMW's angle procedure on ARP bolts. Log each bolt's free length; ARP says to replace any that grows more than 0.001 in | | |
| Oil-pump sprocket nut | 25 Nm (18 ft-lb) | Left-hand thread | | |
| Oil-pan screws, M6 | 10 Nm (89 in-lb); Flow gives 12 Nm (106 in-lb) for 10.9 screws | Sealant at the timing-cover, block and bellhousing joints: the SI says Hylomar | | |
| Oil drain plug | 25 Nm (18 ft-lb) | New sealing ring 07119963151 | | |
| Oil filter cover | 33 Nm (24 ft-lb) | Filter housing bolts 22 Nm (16 ft-lb) | | |
| Crank pulley bolts; power-steering pump bolts | 23 Nm (17 ft-lb) | One video only | | |
| Spark plugs, M12×1.25 | **No BMW figure found; the videos disagree:** 23 Nm (17 ft-lb), dry, or 25 Nm (18 ft-lb) | Check TIS | | |
| Valve-cover cap nuts | **No BMW figure found; the videos disagree:** 10 Nm (89 in-lb) or 8 Nm (71 in-lb), in a cross pattern | Check TIS | | |
| Crankcase-vent return banjo (17 mm) | 19 Nm (14 ft-lb) | New washers; one video only | | |
| VANOS: solenoid coil screws | 4 Nm (35 in-lb) | One video only; no BMW figure found | | |
| VANOS: piston covers, lower VANOS bolts, solenoid-block screws | 10 Nm (89 in-lb) | One video only | | |
| VANOS: transfer-gear cover | 55 Nm (41 ft-lb) | One video only | | |
| VANOS: exhaust sprocket Torx bolts | 12 Nm (106 in-lb) with blue thread-locker | One video only | | |
| Upper chain guide bolt; chain tensioner | Guide 24 Nm (18 ft-lb); tensioner snug plus ½ turn with a new washer | One video only | | |
| VANOS hub bolts (new M6×25) | About 14 Nm (124 in-lb), by feel, because no torque wrench fits | One video only | | |
| Dual-mass flywheel to crank | 105 Nm (77 ft-lb), no angle | Eight new M12×1.5×50 bolts 11222243051, threads lightly oiled, no thread locker | | |
| Pressure plate to flywheel, M8 10.9 | 34 Nm (25 ft-lb) | Six new micro-encapsulated screws 21207548052 | | |
| Flex disc (guibo), M3, M12 10.9: shaft side, on the bench | 115 Nm (85 ft-lb) | Bolts 26117635643 with new self-locking nuts 26127536563. Turn the bolt, not the nut | | |
| M3 diff front mount bolt, M14×1.5×65 10.9 (33177840535), diff on the subframe | 200 Nm (148 ft-lb) | Not the 128 ft-lb (174 Nm) in Condor's video | | |
| M3 diff rear bolts, M12×50 Torx, ×2 | 20 Nm (15 ft-lb) + 90° | Not the 70 ft-lb (95 Nm) in Condor's video | | |

### Phase 7: rear axle

In this order: the studs before the axle goes up; the collar nuts, rear bolts and push rod; the joints that don't need ride height; then the rubber-bushed joints at loaded ride height ([Phase 7](README.md#phase-7-fit-the-m3-rear-axle-and-fuel-system), steps 4, 5 and 8). The diff mounts were done on the bench (Phase 3).

| Fastener | Value | Notes | Done | Marked |
|---|---|---|---|---|
| Subframe to body: M12×1.5 studs 33326760360, one at each front mount | 90 Nm (66 ft-lb) | Before the axle goes up | | |
| Subframe to body: collar nuts 33326760374 and rear M12×1.5×116 bolts 33326760361 | 77 Nm (57 ft-lb) | Front studs lined up first, then the rear bolt holes; push rod and spacers over the studs under the nuts | | |
| Subframe front support cradle (push rod) bolts, ×4 | 25 Nm (18 ft-lb) | Keep your reinforcement kit's spacer plates under it | | |
| M3 V-brace bolts, ×3 (M10×35 10.9) | 59 Nm (44 ft-lb) + 90° | Only if your body has the mounting points | | |
| Half-shaft to diff output flange (ribbed M10×46 Torx 33211227664, ×12, E12) | 100 Nm (74 ft-lb) for the M3's black bolts | New bolts (Flow). The 80 Nm (59 ft-lb) Flow also prints is for silver bolts | | |
| Rear drive-flange collar nut, M27×1.5 | 300 Nm (221 ft-lb) | New nut 33411133785; lightly oil the contact face | | |
| Diff drain and fill plugs | 60 Nm (44 ft-lb) with an O-ring; 65 Nm (48 ft-lb) with a sealing washer | — | | |
| Trailing arm to bracket (through-bolt) | 110 Nm (81 ft-lb) | At loaded ride height | | |
| Trailing-arm bracket to body | 77 Nm (57 ft-lb) | Any position | | |
| Rear control-arm bolts at the subframe, M12 | 77 Nm (57 ft-lb) | At loaded ride height | | |
| M12 10.9 bolts at the trailing arm (the two ball joints; one is the eccentric bolt) | 110 Nm (81 ft-lb) | Any position | | |
| Rear damper lower bolt, M12 | 100 Nm (74 ft-lb) | At loaded ride height | | |
| Rear damper top-mount nuts, M8 (M3 parts) | 28 Nm (21 ft-lb) | New nuts. No value found for the Touring's own top mounts | | |
| Rear damper rod nut, M10×1 | 14 Nm (124 in-lb) | New nut | | |
| Rear anti-roll bar, links and brackets | 22 Nm (16 ft-lb) | At loaded ride height (rubber mounts) | | |

### Phase 8: front axle, steering and brakes

The front rubber-bushed joints wait for Phase 12.

| Fastener | Value | Notes | Done | Marked |
|---|---|---|---|---|
| Front axle support (subframe) to body, M12 10.9 | 110 Nm (81 ft-lb) | Tighten the rear bolts first; their dowels center the subframe | | |
| Control arm to subframe, M14 self-locking nut | 90 Nm (66 ft-lb) | New nut | | |
| Ball joint to knuckle, M12 self-locking collar nut | 65 Nm (48 ft-lb) | New nut; no impact wrench | | |
| Front reinforcement plate, M10×35 10.9 | 59 Nm (44 ft-lb) + 90° | New bolts | | |
| Strut top mount to body, M8 collar nuts | 24 Nm (18 ft-lb) | — | | |
| Damper rod top nut, M14 | 64 Nm (47 ft-lb) | New nut | | |
| Strut to knuckle clamp bolt, M12×1.5×55 10.9 | 81 Nm (60 ft-lb) | New bolt | | |
| Front wheel-speed sensor bolt | 8 Nm (71 in-lb) | — | | |
| Front anti-roll bar link nuts, M10 | 65 Nm (48 ft-lb) | New nuts | | |
| Steering rack to subframe, M10 | 42 Nm (31 ft-lb) | — | | |
| Inner tie rod to rack | 100 + 10 Nm, as the compilation prints it | Check TIS for what the "+ 10" means | | |
| Outer tie-rod lock nut, M14 | 45 Nm (33 ft-lb) | — | | |
| Tie-rod end to knuckle, M12 self-locking | 65 Nm (48 ft-lb) | No impact wrench | | |
| Steering shaft lower joint Torx bolt, M8×33 | 22 Nm (16 ft-lb) | New bolt | | |
| Front hub collar nut (only if hubs are replaced) | 290 Nm (214 ft-lb) | New nut 31211128336 | | |
| Front caliper carrier, M12×1.5 | 110 Nm (81 ft-lb) | — | | |
| Caliper guide bolts, front and rear | 30 Nm (22 ft-lb) | — | | |
| Rear caliper carrier, M10 | 65 Nm (48 ft-lb) | Micro-encapsulated screws | | |
| Brake line to caliper | 19 Nm (14 ft-lb) | — | | |
| Bleed screws | 7 mm: 3.5–5 Nm (31–44 in-lb); 11 mm: 12–16 Nm (106–142 in-lb) | — | | |
| Rotor retaining screw | 16 Nm (142 in-lb) | — | | |
| Master cylinder to booster, M8 | 26 Nm (19 ft-lb) | New nuts | | |
| Booster to pedal bracket | 25 Nm (18 ft-lb) | — | | |
| DSC pressure sensor in the master cylinder | 25 + 5 Nm, as the compilation prints it | Check TIS for what the "+ 5" means | | |
| Wheel bolts, M12×1.5 | 120 ± 10 Nm (89 ± 7 ft-lb) | — | | |

### Phase 9: engine, gearbox and driveshaft

| Fastener | Value | Notes | Done | Marked |
|---|---|---|---|---|
| Bellhousing Torx bolts | M8 28 Nm (21 ft-lb); M10 52 Nm (38 ft-lb); M12 98 Nm (72 ft-lb) | Flow's own general table gives 82 Nm (60 ft-lb) for M12 8.8; confirm the M12 value in TIS | | |
| Engine mount nuts, M10 | 45 Nm (33 ft-lb) | — | | |
| Engine support arm to block, M8 | 21 Nm (15 ft-lb) | — | | |
| Gearbox crossmember to body; gearbox mounts, M8 | 21 Nm (15 ft-lb) | — | | |
| Starter, M10 Torx | 45 Nm (33 ft-lb) | Leads: M5 5 Nm (44 in-lb), M6 7 Nm (62 in-lb), M8 13 Nm (115 in-lb) | | |
| Clutch slave cylinder nuts | 22 Nm (16 ft-lb) | Line unions 14–20 Nm (10–15 ft-lb) | | |
| 420G drain and fill plugs, M24×1.5 | 52 Nm (38 ft-lb) | Reverse-light switch 20 Nm (15 ft-lb) | | |
| Flex disc (guibo), M3, M12 10.9: gearbox side, in the car | 115 Nm (85 ft-lb) | New self-locking nuts 26127536563. Turn the bolt, not the nut | | |
| Driveshaft center mount | 21 Nm (15 ft-lb) | Preload the bearing 4–6 mm forward (compilation only) | | |
| Driveshaft to diff, M3 (ribbed M10×46 Torx, E14) | 70 Nm (52 ft-lb) | Mark the shaft's position before removal; it's balanced | | |

### Phase 10: cooling and exhaust

| Fastener | Value | Notes | Done | Marked |
|---|---|---|---|---|
| Oil-cooler pipes | 25 Nm (18 ft-lb) | — | | |
| Fan clutch to water pump | 40 Nm (30 ft-lb) | Left-hand thread | | |
| Exhaust manifold to front pipe (US S54) | 24 Nm (18 ft-lb) | New nuts and gaskets | | |
| O2 sensors | 50 Nm (37 ft-lb) | Anti-seize on the threads only | | |
| Exhaust flange, M8 | 22 ± 2 Nm (16 ± 1.5 ft-lb) | — | | |

### Phase 12: at ride height, and the oil-pressure switch

Torque the front rubber-bushed joints with the car's weight on its wheels, before the alignment.

| Fastener | Value | Notes | Done | Marked |
|---|---|---|---|---|
| Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts; at ride height | | |
| Front anti-roll bar bracket nuts, M8 | 21 Nm (15 ft-lb) | At ride height | | |
| Oil-pressure switch, M12×1.5 | 27 Nm (20 ft-lb) | — | | |

## Fluids log

**Phases 2 to 12,** from [Fluids and capacities](README.md#fluids-and-capacities). Later top-ups and re-bleeds go in the [break-in log](#break-in-log).

| Fluid, and when | Specification | Quantity | Date | Amount and notes |
|---|---|---|---|---|
| A/C recovered, donor (Phase 2) | Recovered by a shop; venting it is prohibited | — | | |
| A/C recovered, Touring (Phase 4) | Recovered by a shop; venting it is prohibited | — | | |
| M diff (Phase 7) | Genuine BMW SAF-XJ+FM 75W-140 GL-5, with the friction modifier the M differential needs (83222282583, 500 ml bottles) | 1.1 L (1.2 US qt); Turner says 1.2 L (unverified), so buy three bottles | | |
| Brakes, fill and bleed (Phase 8) | **Not found.** Check the reservoir cap and TIS | Allow about 1.5 L (1.6 US qt) for filling and bleeding | | |
| Clutch bleed (Phase 9) | The brake fluid | — | | |
| 420G gearbox (Phase 9) | Genuine BMW MTF-LT-2, 75W-80 GL-4 (83220309031) | 1.9 L (2.0 US qt); check the label on the gearbox | | |
| Coolant (Phase 10) | BMW coolant, 50/50 with distilled water (unverified); system pressure 2 bar (29 psi) | **Capacity not found** | | |
| DSC INPA bleed, if dry or replaced (Phase 11) | The brake fluid | One INPA DSC bleed on a Z4 M's MK60 used about 1.25 L | | |
| Engine oil, first fill (Phase 12) | Castrol TWS Motorsport SAE 10W-60 or Castrol Formula RS 10W-60, BMW 07510009420 | 6.5 L (6.9 US qt) after a rod-bearing job. Fill, then check the dipstick | | |
| Power steering (Phase 12) | **Not found.** Read the cap on the donor's M3 reservoir (ATF or CHF 11S) and don't mix the two | Not found | | |
| A/C charge, by a shop (Phase 12) | Per the underhood label | **Charge not found;** charge by weight from the label | | |
| Oil and filter, end of break-in | As the first fill | 5.5 L (5.8 US qt) for an oil change with filter | | |

- [ ] Donor drained (Phase 2): every fluid and the tank, into approved containers; disposed of properly
- [ ] Your Touring drained (Phase 4): oil, coolant, power steering, brakes, both halves of the tank

## Re-pin log: MS43 Touring

**Phase 11,** step 3, Touring built from 09/2001 to 02/2003 with a donor built from 09/2001 ([MS43 move list](WIRING-AND-CODING.md#ms43-touring-what-to-move); earlier cars: the notes under that table). Work in this order: the heater wire leaves X6011 pin 7 before the clutch wire goes in. Every wire that moves between X6011 and X60004 gets a new terminal of the target's type. Log continuity end to end, then check each wire is open to ground ([Power-up checks](#power-up-checks), steps 2–8).

Colors, as in BMW's diagrams: SW black, WS white, RT red, GN green, BL blue, BR brown, GE yellow, GR gray, VI violet, OR orange. BR/GR is brown with a gray tracer. Sizes are mm².

| Move | From | Wire | To | Done | Continuity (Ω) |
|---|---|---|---|---|---|
| 1. Leak-test heater, first | Body X6011 pin 7 | 0.75 SW/RT | X60004 pin 18 | | |
| 2. Clutch signal, after move 1 | X60004 pin 23 | 0.35 BL/BR | Body X6011 pin 7, meeting the M3 harness's 0.5 GR wire to X6053 pin 5, the gear switch and X60002 pin 20 | | |
| 3. Oil-pressure lamp | Body X6011 pin 3 | 0.35 BR/GN | X60004 pin 11 (to cluster X11175 pin 13) | | |
| 4. Charge lamp | Body X6011 pin 4 | 0.35 BL | X60004 pin 1 (to cluster pin 2) | | |
| 5. Oil level | Body X6011 pin 5 | 0.5 WS/GN | X60004 pin 21 (to cluster pin 17) | | |
| 6. Start feedback (terminal 30h) | Body X6011 pin 6 | 0.35 SW/GN | X60004 pin 2 (through splice X276 to cluster pin 3) | | |
| 7. Brake-light switch, test contact | X60004 pin 28 | 0.35 BR/GR | X60004 pin 34 | | |
| 8. DME ground (recommended) | New wire | 0.35 BR/SW | X60004 pin 5 to ground point X1108, under the driver's-seat carpet | | |
| 9. Sport button input (optional) | X1869 pin 17 | New 0.35 SW/RT/GE | X60004 pin 15 | | |
| 9. Sport LED (optional) | X60004 pin 16 | New 0.35 SW/GR/GE | X1869 pin 18 | | |
| 10. Clutch module | 61319231129 | — | Replace with the M3's 61319122700 | | — |
| No change | X60004 pin 10 (pump relay); pins 20 and 30 (leak-test pump: [test it](WIRING-AND-CODING.md#dm-tl-leak-test-pump-test-before-you-swap)); X6011 pins 1 and 2; X6021 pins 2, 3 and 4 | — | — | | — |
| Leave empty | X60004 pin 6; X6011 pin 8; X6021 pin 1 | — | — | | — |

Kassel's chart prints the brake wire BR/GN and puts the oil-pressure lamp on cluster pin 14 (the K-bus), and a forum mapping sends X6011 pin 6 to X60004 pin 6: follow this table, which is BMW's ([Where other sources differ](WIRING-AND-CODING.md#ms43-touring-what-to-move)).

## Re-pin log: MS45.1 Touring

**Phase 11,** step 3, Touring built from 03/2003 with the M54 and a manual gearbox ([MS45.1 move list](WIRING-AND-CODING.md#ms451-touring-what-to-move)). Pins 5, 15 and 19 come out first; the heater leaves pin 2 before anything else goes in. Log continuity end to end, then check each wire is open to ground ([Power-up checks](#power-up-checks), steps 2–8). Colors as in the MS43 log above.

> [!IMPORTANT]
> Pins 2 and 15 are both SW/RT (black with red). Tag them before you pull them: the 0.75 mm² wire in pin 2 moves to pin 18, and the 0.5 mm² wire in pin 15 comes out.

| Move | From | Wire | To | Done | Continuity (Ω) |
|---|---|---|---|---|---|
| 1. Leak-test heater, first | X60004 pin 2 | 0.75 SW/RT | X60004 pin 18 (check it's empty first) | | |
| 2. Secondary-air sensor ground: out | X60004 pin 5 | 0.5 SW/GE | Out; insulate and tie back | | — |
| 3. Secondary-air sensor signal: out | X60004 pin 15 | 0.5 SW/RT | Out; insulate | | — |
| 4. E-box fan: out, if populated | X60004 pin 19 | 0.5 BR/OR | Out; insulate | | — |
| 5. Brake-light switch, test contact | X60004 pin 28 | 0.35 BR/GR | X60004 pin 34 | | |
| 6. Clutch signal | X60004 pin 23 | 0.35 BL/BR | Body X6011 pin 7, with a new X6011-type terminal (pin 7 is empty on this car) | | |
| 7. Oil-pressure lamp: add | X60004 pin 11 | New 0.35 BR/GN | Cluster X11175 pin 13; code `CAN_OELDRUCKSCHALTER` = `nicht_aktiv` | | |
| 8. Charge lamp: add | X60004 pin 1 | New 0.35 BL | Cluster pin 2; code `GENERATOR_UEBER_CAN` = `nicht_aktiv` | | |
| 9. Oil level: add | X60004 pin 21 | New 0.5 WS/GN | Cluster pin 17; code `TOG_UEBER_CAN` = `nicht_aktiv` | | |
| 10. Start feedback, only if your body X6011 pin 6 holds a wire | Body X6011 pin 6 | 0.35 SW/GN | X60004 pin 2, after move 1 | | |
| 11. DME ground (recommended), after move 2 | New wire | 0.35 BR/SW | X60004 pin 5 to ground point X1108, under the driver's-seat carpet | | |
| 12. Sport button input (optional), after move 3 | X1869 pin 17 | New 0.35 SW/RT/GE | X60004 pin 15 | | |
| 12. Sport LED (optional) | X60004 pin 16 | New 0.35 SW/GR/GE | X1869 pin 18 | | |
| 13. Clutch module | 61319231129 | — | Replace with the M3's 61319122700 | | — |
| No change | X60004 pin 10 (pump relay); pins 20 and 30 (leak-test pump: [test](WIRING-AND-CODING.md#dm-tl-leak-test-pump-test-before-you-swap) before you swap anything); X6011 pins 1 and 2; X6021 pins 2, 3 and 4 | — | — | | — |
| Leave empty | X60004 pin 6; X6011 pin 8; X6021 pin 1 | — | — | | — |

Nobody has photographed a 325i Touring's X60004, so note what you found in pins 5, 15 and 19. Forum advice to swap pins 20 and 30 on MS45.1 cars follows BMW's table labels, not the drawings: test first.

## E-box plug log

**Phase 11,** step 2, before you join the plugs ([E-box plugs](WIRING-AND-CODING.md#e-box-plugs), [E-box plug comparison](WIRING-AND-CODING.md#e-box-plug-comparison)). For every cavity, write the wire color on each half and where it goes. Each pair should be the same circuit, or empty on one side. "M3 side" is the M3 engine harness's half; "your side" is your body harness's.

### X6011, black, 8 pins

| Cavity | Manual says, after the re-pin | M3 side | Your side | Match ✓ |
|---|---|---|---|---|
| 1 | Terminal 50: M3 side 2.5 SW to the starter; your side 2.5 SW from EWS X1659 pin 1 | | | |
| 2 | Terminal 15: M3 side 1.0 GN/BR to the oil-level sensor and alternator regulator; your side 0.75 GN/BR from F30, 7.5 A | | | |
| 3 | Empty on your side (MS43: the oil-pressure wire has moved to X60004 pin 11) | | | |
| 4 | Empty on your side (MS43: the charge-lamp wire has moved to X60004 pin 1) | | | |
| 5 | Empty on your side (MS43: the oil-level wire has moved to X60004 pin 21) | | | |
| 6 | Empty on your side (the start feedback has moved to X60004 pin 2) | | | |
| 7 | Clutch: M3 side 0.5 GR to X6053 pin 5 and the gear switch; your side your 0.35 BL/BR clutch wire (MS43: after the heater wire has gone to X60004 pin 18) | | | |
| 8 | M3 side: the tire-pressure reset to X60003 pin 19 on MK20-era M3s, empty on MK60 cars. Your side: empty | | | |

### X6053 and X60531, natural, 8 pins

These join the engine harness to the gearbox-module harness, so both halves must be M3 parts: never an M3 half with a Touring half. Mixed halves put the throttle-actuator lines on the injector feed: one swap got injector "circuit low" faults on all six. Values: the M3's X6053.

| Cavity | Manual says (M3) | Engine-harness half | Gearbox-module half | Match ✓ |
|---|---|---|---|---|
| 1 | Injector supply from relay K6327 (2.5 RT/GE) | | | |
| 2 | F2 supply (2.5 RT/WS/GE) | | | |
| 3 | F3 supply (2.5 RT/WS) | | | |
| 4 | Ground (1.5 BR) | | | |
| 5 | Clutch chain, X6011 pin 7 to the gear switch (0.5 GR) | | | |
| 6 | Throttle actuator + from X60001 pin 2 (2.5 RT) | | | |
| 7 | Throttle actuator − from X60001 pin 9 (2.5 WS) | | | |
| 8 | Empty | | | |

### X6021, black, 4 pins

| Cavity | Manual says | M3 side | Your side | Match ✓ |
|---|---|---|---|---|
| 1 | M3 side: the US pump-module signal from X60002 pin 11 (0.35 SW/VI). Your side: empty on a manual 325i; keep it empty | | | |
| 2 | DME-relay power out, F3 (1.5 RT/WS); on your side to splice X11212: K96's coil, the leak-test module, the A/C relay's coil | | | |
| 3 | Reverse-light switch output (1.0 BL/GE) | | | |
| 4 | Reverse-light switch feed from F27, 10 A (1.0 GN/WS) | | | |

### X6054 or X60541, and the battery feed

There's no 3-pin E-box plug on these cars: the reverse-light wires and the DME-relay supply share X6021, and the heavy battery feed comes in at X64101/X64102.

| Plug and cavity | Manual says | M3 side | Your side | Match ✓ |
|---|---|---|---|---|
| X6054 or X60541 pin 1 (M3 halves together) | Coil supply from F1, 30 A (2.5 mm²) | | | |
| X6054 or X60541 pin 2 | Ground from X60005 pin 5 (2.5 BR) | | | |
| X64101/X64102 | Battery positive from F102 (80 A): 1.5 RT to X60001 pin 7, 4.0 RT to the DME relay K6300 | | | |

- [ ] E-box fuse carrier fitted with the M3 harness: F1 30 A, F2 30 A, F3 20 A (K96's coil, the leak-test module, the A/C relay's coil), F4 30 A
- [ ] E-box fan fed from one harness only; the M3 plug left unplugged if your E-box has no blower

## Power-up checks

**Phase 11,** steps 7 and 8, and **Phase 12** for steps 30–33. The procedure is the manual's [Checks before first power-up](WIRING-AND-CODING.md#checks-before-first-power-up); this sheet logs it. Pass values marked BMW are BMW's; "generic" ones are a guide, not a limit. A meter proves wires: the clutch module, the brake-light switch and the oil-level sensor are electronic, so steps 26 and 27 prove those parts. Tool32 jobs are in `MSS54DS0.PRG` unless a step names another file.

### Steps 1–14: battery off, DME unplugged

All five DME plugs off, ignition off.

| Step | Check | Expect | Measured | Pass |
|---|---|---|---|---|
| 1 | Tug-test every moved or added terminal; look into the emptied cavities: X60004 pins 23 and 28; MS43 also X6011 pins 3–6; MS45.1 also X60004 pin 19, and 2, 5 and 15 unless they now carry the start feedback, the new ground and the Sport wire | Every terminal locked; every cavity as the move table says | | |
| 2 | Each moved or added wire to chassis ground (not the new pin-5 ground) | Open | | |
| 3 | X60004 pin 11 to cluster X11175 pin 13; pin 1 to pin 2; pin 21 to pin 17; pin 2 to pin 3 (start feedback, if moved) | Continuity, under about 1 Ω (generic) | | |
| 4 | M3 harness X60003 pin 26 to engine ground, engine stopped | Near 0 Ω: the oil-pressure switch is closed without pressure | | |
| 5 | X60004 pin 34 to the brake-switch plug X78 pin 3 | Continuity (the switch: step 26) | | |
| 6 | Clutch chain: X13635 pin 2 to body X6011 pin 7; on to the gear switch's pin 1; gear switch pin 2 to X60002 pin 20; across the gear switch | Continuous wires; across the gear switch near 0 Ω in gear, open in neutral (the module: step 26) | | |
| 7 | Start interlock: X13635 pin 4 to EWS X1659 pin 8 | Continuity | | |
| 8 | Sport, if fitted: X1869 pin 17 to X60004 pin 15; pin 18 to pin 16; then pin 15 to ground with the switch unit in | Continuity; open released, near 0 Ω pressed (BMW: it grounds the input) | | |
| 9 | Leak-test triangle, module plugged in: X60004 pins 18–20, 18–30, 20–30 (table below) | The lowest element is the pump, and it belongs on 30 | | |
| 10 | K96 pulled: X60004 pin 10 to K96 socket pin 4 (SW/VI); the M3 harness's X6021 pin 1 to every K96 socket terminal; across K96's coil | Continuity; open to every terminal; about 90 Ω (generic) | | |
| 11 | Coil supply (terminal 15 side) to X60005 pins 1, 2, 3, 9, 6 and 7 (cylinders 1–6) | About 0.8 Ω each, all alike (BMW: harness plus primary winding) | | |
| 12 | Injector supply to X60003 pins 33–38 | Six equal readings (no BMW figure) | | |
| 13 | Coolant sensor X60003 pins 24 and 25; radiator outlet X60004 pins 38 and 39 | About 2,500 Ω at 20 °C (generic Bosch NTC) | | |
| 14 | Crankshaft sensor X60003 pins 8 and 21 | A steady coil reading, open to ground (no BMW figure) | | |

**Step 9, the triangle.** Each element = (the two readings that include its pin, added, minus the third) ÷ 2. One new Bosch module (generic, an E93 unit) read about 68, 52 and 44 Ω: heater ≈ 38 Ω on 18, valve ≈ 30 Ω on 20, pump ≈ 14 Ω on 30. Pump on 20: see the manual's [leak-test pump](WIRING-AND-CODING.md#dm-tl-leak-test-pump-test-before-you-swap).

| Pair or element | Reading (Ω) |
|---|---|
| 18–20 | |
| 18–30 | |
| 20–30 | |
| Heater, on 18: (18–20 + 18–30 − 20–30) ÷ 2 | |
| Valve, on 20: (18–20 + 20–30 − 18–30) ÷ 2 | |
| Pump, on 30: (18–30 + 20–30 − 18–20) ÷ 2 | |

### Steps 15–18: battery on, DME still unplugged

| Step | Check | Expect | Measured | Pass |
|---|---|---|---|---|
| 15 | Terminal 30 at X60001 pin 7 (harness side) | Battery voltage, key on or off | | |
| 16 | Terminal 15 at X60004 pin 26, key at position 2 | Battery voltage, above 9 V (BMW's threshold); 0 V with the key off | | |
| 17 | DME relay supply: K6300 socket terminal 30 (X6300 pin 6, 4.0 RT) | Battery voltage, key on or off | | |
| 18 | Grounds: X60001 pins 4, 5 and 6 to the battery's negative post | Near 0 Ω; under 0.1 V drop under load (generic) | | |

### Step 19: CAN bus

Battery disconnected again. DME plugged in (ignition off), with every other module plugged in: cluster, DSC unit, steering-angle sensor. Back-probe X60004 pin 36 (CAN high) to pin 37 (CAN low) at the plugged-in DME, or X11175 pins 9 and 10 at the cluster. Not at the diagnosis socket: an E46's has no CAN pins.

| Step | Check | Expect | Measured | Pass |
|---|---|---|---|---|
| 19 | CAN high to CAN low | About 60 Ω: both 120 Ω terminating resistors in place (BMW). About 120 Ω: a terminating module unplugged or cut off. About 40 Ω: a third terminator. 0 Ω: high and low shorted. Open: both missing, or the probe wire broken | | |

### Steps 20–29: first key-on

DME plugged in, battery connected, charger on, key at position 2, engine off. Plug and unplug the DME only with the ignition off.

| Step | Check | Expect | What you saw | Pass |
|---|---|---|---|---|
| 20 | Relay and comms | K6300 clicks at key-on and stays on a few seconds after key-off (BMW). INPA shows two black dots and reaches the DME (E46 → Engine → "MS S54 for S54 M3"), cluster, light module, EWS and DSC; Tool32 `IDENT` returns OKAY | | |
| 21 | `STATUS_UBATT`; `STATUS_UEXT1` and `STATUS_UEXT2` | `STATUS_UBATT` within a few tenths of a volt of the battery (generic). BMW: the relay supply within 3 V of terminal 15, which is above 9 V. Sensor supplies about 5 V (BMW) | | |
| 22 | `FS_LESEN` | Only fault location 1 (0x01), "Relais Kraftstoffpumpe"; possibly 130 (0x82) after an EWS delete; and the DSC unit's VIN faults until Session 5 | | |
| 23 | Lamps at key-on | Red oil-pressure lamp, charge lamp and check-engine lamp lit | | |
| 24 | Temperatures on a cold-soaked engine: `STATUS_MOTORTEMPERATUR`, `STATUS_OEL_TEMPERATUR`, `STATUS_AN_LUFTTEMPERATUR`, `STATUS_KUEHLW_AUSL_TEMPERATUR`, `STATUS_TUMG` | All within a few °C of each other and of the air; none pinned near −48 °C | | |
| 25 | `STATUS_PWG_POTI_SPANNUNG`; `STATUS_DKP_WINKEL` against `STATUS_DKP_WINKEL_SOLL` | Pedal sensor 1 about 0.5 V released, rising to about 4.5 V; sensor 2 0.5 to 2.0 V (BMW). Throttle sensor 0.5 V closed to 4.5 V open (BMW). Actual follows target | | |
| 26 | `STATUS_DIGITAL` | **Clutch, with a gear engaged:** pedal up `STAT_KRAFTSCHLUSS_EIN` = 1 and `STAT_KUP_EIN` = 0; pedal down 0 and 1. In neutral both stay at 0 and 1 whatever the pedal. **Brake:** `STAT_BLS_EIN` and `STAT_BLTS_EIN` both change with the pedal. **Sport:** `STAT_FDYN_EIN` changes; the LED follows. **Cruise buttons:** `STAT_MFL1_EIN` to `STAT_MFL4_EIN` change | | |
| 27 | `EWS3.PRG` → `STATUS_LESEN` | Key sending (`STAT_SCHLUESSEL_SENDET`), not barred, the three "NIO" bits 0. Clutch down: `STAT_P_N_EINGANG` changes and `STAT_ANLASSER_AUS_P_N` = 0 | | |
| 28 | Pump | One prime heard at key-on; `STAT_EKP_EIN` = 1 during it; `STEUERN_EKP` clicks K96 and runs the pump (stop it with `STEUERN_EKP_AUS`); 5.0 ± 0.2 bar, under 0.5 bar lost (BMW) | | |
| 29 | Outputs: `STEUERN_DMTL_HEIZUNG`; `STEUERN_SLP` and `STEUERN_SLV`; `STEUERN_KO` (K19); `STEUERN_E_LUEFTER`; `STEUERN_TEV`; `STEUERN_VENTIL_SAUGSTRAHLPUMPE` | Each part runs or clicks, and `JOB_STATUS` reads OKAY. Leave the injector and coil jobs alone | | |

### Steps 30–33: the oil-priming crank

**Phase 12,** with K96 and the injector relay K6327 pulled and the six coils unplugged.

| Step | Check | Expect | What you saw | Pass |
|---|---|---|---|---|
| 30 | Start interlock | Clutch up: no crank. Clutch down: cranks | | |
| 31 | Engine speed while cranking: `STATUS_MOTORDREHZAHL` | Above 0, and the tachometer moves | | |
| 32 | Oil, on the mechanical gauge | Pressure shows and holds; the red lamp goes out | | |
| 33 | Relays and coils refitted, then Session 6 steps 2–4 | `STAT_WDK_ADAPT_WERT` = 0 after the reset | | |

## Coding sessions log

**Phases 3, 11 and 12** ([Coding step by step](WIRING-AND-CODING.md#coding-step-by-step)). Back up first, keep the charger on, run one program at a time.

| Session | Expect | Date | Result |
|---|---|---|---|
| 1. Vehicle order and codings (Phase 0) | A readable vehicle order and one coding file per module, logged in the [coding backups log](#coding-backups-log) | | |
| 2. DME back from the vendor (Phase 3) | A written list of changes: EWS delete, your VIN, manual software if needed, and nothing else. Any emissions function removed: send it back | | |
| 2. DME VIN read back (Phase 11) | Your Touring's full 17-character VIN in the AIF; a generic OBD-II scanner shows it | | |
| 3. EWS | `PARK/NEUTRAL_EINGANG` = `aktiv`. In `STATUS_LESEN`, key in, clutch pressed: key sending, not barred; `STAT_ANLASSER_AUS_P_N` = 0; `STAT_ANLASSER_FREIGESCHALTET` = 1 while cranking. After a delete, 130 (0x82) may be stored; the engine still starts | | |
| 4. Cluster and light module | Options edited, not default-coded: `CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN` and `TOG_UEBER_CAN` = `nicht_aktiv`, with the three lamp wires in place; `TANK_KENNLINIE` = `60_l_literskala`. No tamper dot; your true mileage, matching the Phase 0 photo | | |
| 5. DSC coding and VIN | DSC and brake lamps out; no 5EF1 or 5E1F | | |
| 6. First start, adaptations and throttle check | `STAT_WDK_ADAPT_WERT` = 0. With a gear engaged, `STAT_KRAFTSCHLUSS_EIN` = 1 with the pedal up and `STAT_KUP_EIN` = 1 with it down; the brake and Sport bits follow. Steady idle, fuel trims near zero; all four VANOS jobs complete; no new faults | | |
| 7. Steering angle after the alignment | DSC lamp out; 0° with the wheel straight; a straight wheel on the road test | | |
| 8. Vehicle-order changes and body modules, if any | The order reads back from AKMB and ALSZ; each module coded; DME adaptations reset | | |
| 9. Light module and headlights | Lights work as fitted; headlights aimed at ride height | | |

### Fault log

After each session: clear every module's faults, cycle the ignition, read again. Expect only fault location 1 (0x01), the pump fault, and possibly 130 (0x82), the immobilizer fault, after an EWS delete; fix anything else before the first start ([Troubleshooting](WIRING-AND-CODING.md#troubleshooting)).

| # | Date | Module | Fault code and text | Cause and fix | Cleared |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |

## First start

**Phases 7 to 12** ([Phase 7](README.md#phase-7-fit-the-m3-rear-axle-and-fuel-system) to [Phase 12](README.md#phase-12-front-end-first-start-and-shakedown), and the manual's [Session 6](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check)). Log the warm VANOS jobs in [VANOS tests](#vanos-tests).

**Tests before the first start:**

| Test | Pass | Result and date |
|---|---|---|
| Fuel, static, pump on a relay bypass (Phase 7) | 5.0 ± 0.2 bar (72.5 ± 2.9 psi) | |
| Fuel, 20 minutes after switch-off | Above 4.5 bar (65 psi); no more than 0.5 bar lost | |
| Fuel delivery at 12 V (TIS 13 31) | At least 1.12 L in 30 s | |
| Fuel leaks; feed and return confirmed | None | |
| Brakes: air test, fill, bleed (Phase 8) | Holds; no weeps, pedal held hard; pedal high and firm | |
| Clutch (Phase 9) | Pedal firm, returns; slave pushrod moves full stroke | |
| Driveshaft center bearing preload | 4–6 mm forward (compilation only) | |
| Cooling, pressure tester (Phase 10) | Holds 2 bar (29 psi), no drop, no leaks | |

**First start readings:**

| Reading | Pass | Result |
|---|---|---|
| Oil-priming crank: [power-up checks](#steps-3033-the-oil-priming-crank), steps 30–33 | All passed | |
| Fuel pressure at key-on | 5.0 ± 0.2 bar (72.5 ± 2.9 psi) | |
| Oil pressure at the start | Shows at once; if not, switch off | |
| Leaks at idle; knocking or VANOS rattle | None | |
| Oil pressure at hot idle | At least 0.7 bar (10 psi); confirm in TIS | |
| Fuel pressure at hot idle, vacuum hose on | Below 5 bar; BMW's diagram: 3.8 bar at part-throttle vacuum | |
| Idle; fuel trims `STATUS_LAMBDA_ADD_1`, `_2` | Steady; trims near zero | |
| Cooling | Temperature steady, no air, fan cycles | |
| Fault memory, every module | Only location 1 (0x01), the pump fault; possibly 130 (0x82) after an EWS delete | |
| Oil-pressure switch refitted, gauge and tee off | 27 Nm (20 ft-lb); no oil at the port; the red lamp lights at key-on and goes out running | |

## Shakedown log

**Phase 12,** from the first drive to the end of the break-in. The checks come from [Phase 12](README.md#phase-12-front-end-first-start-and-shakedown), and the alignment targets from [Wheel alignment](README.md#wheel-alignment).

### Alignment

Torque the front bushed joints on the wheels, align at the car's own loaded ride height, then calibrate the steering angle ([Session 7](WIRING-AND-CODING.md#session-7-steering-angle-after-the-alignment)). The M3 values are targets, since your Touring sits differently.

| Item | BMW E46 M3 target | Phase 0 printout | After (Phase 12) |
|---|---|---|---|
| Front total toe | 0°16' ± 7' | | |
| Front camber | −1°00' ± 20' (left/right difference max 30') | | |
| Front caster at ±10° lock / ±20° lock | 7°25' ± 30' / 7°40' ± 30' (left/right difference max 30') | | |
| Front toe-out on turns (20° inner lock) | −1°32' ± 30' | | |
| Front set-back | 0° ± 10' | | |
| Front maximum lock (approx.) | 40.90° inner, 33.81° outer | | |
| Rear total toe | 0°22' ± 6' | | |
| Rear camber | −1°45' ± 15' (left/right difference max 15') | | |
| Rear thrust angle (geometric axis) | 0° ± 4' | | |
| Shop and date | — | | |
| Steering angle after calibration | INPA reads 0° with the wheel straight | — | |

### Speedometer and fuel gauge

| Check | Expect | Measured | Cluster shows |
|---|---|---|---|
| Road speed against GPS, at a steady speed | The M3 cluster over-reads by about 8.9% by design | | |
| Fuel added from near empty, in litres | The gauge, the range and Tool32's `STATUS_TANKINHALT_LESEN` follow it. Nobody has reported an M3 cluster on Touring tank senders, and the leak test relies on the reading | | |

### Break-in log

BMW's break-in after new rod bearings is 1,200 miles (1,930 km) below 5,500 rpm and 105 mph (169 km/h). BMW's bulletin gives no checks along the way and needs no oil service at the end; the check points below are the guide's suggestions ([Phase 12](README.md#phase-12-front-end-first-start-and-shakedown)). Include closed-throttle coast-downs in gear: that's when the DME learns the crankshaft wheel.

| Check point | Date | Odometer | Leaks | Re-torques, marks | Fault codes | Notes |
|---|---|---|---|---|---|---|
| First slow drive: wheel speeds agree in INPA; DSC faults read | | | | | | |
| Brakes: progressive stops, then a careful hard stop; ABS pulses, the car stops straight | | | | | | |
| Short drives near home: paint marks, wheel-bolt torque, fluid levels, fault memory | | | | | | |
| Parking-brake shoes bedded in on an empty road | | | | | | |
| After the first few drives: brakes bled again | | | | | | |
| After the first few heat cycles: coolant level | | | | | | |
| Every fuel stop: oil level, and a look for leaks | | | | | | |
| About 600 miles, halfway: every module's faults read | | | | | | |
| Shifts: revs drop cleanly between gears | | | | | | |
| Coast-downs in gear: `STAT_LU_ADAP_CNT_WERT` rising | | | | | | |
| Your own check | | | | | | |
| Your own check | | | | | | |
| Your own check | | | | | | |
| 1,200 miles below 5,500 rpm and 105 mph done; oil and filter changed (our recommendation); no metal in the oil or filter | | | | | | |

## Inspection readiness

**Phases 12 and 13** ([Readiness and inspection](WIRING-AND-CODING.md#readiness-and-inspection), [Phase 13](README.md#phase-13-paint-trim-and-paperwork)). **Don't clear codes or disconnect the battery** in the weeks before the test: both reset readiness. Fix the faults, then let the DME run its own tests.

### Readiness drives

One column per day, following the manual's [drive plan](WIRING-AND-CODING.md#a-drive-plan-for-readiness). The leak test runs only every second time its conditions are met. For each monitor, write R (ready) or N (not ready).

| Item | Day 1 | Day 2 | Day 3 | Day 4 | Day 5 | Day 6 |
|---|---|---|---|---|---|---|
| Date | | | | | | |
| Parked 5 hours or more; no ignition before the cold start | | | | | | |
| Cold-start air temperature (−10 to 40 °C; leak test −7 to 35 °C) | | | | | | |
| Fuel level, 35–85% (suits BMW's 15–85% and New York's tips) | | | | | | |
| Idled about 2.5 minutes after the cold start | | | | | | |
| Drove 20 minutes or more, as the drive plan says | | | | | | |
| Switched off 5 minutes or more, untouched | | | | | | |
| Catalyst (one bank: one result) | | | | | | |
| O2 sensors and heaters | | | | | | |
| Secondary air | | | | | | |
| EVAP leak test (DM-TL) | | | | | | |
| Purge (a generic scanner shows it under EVAP) | | | | | | |
| Misfire | | | | | | |
| Tool32 readiness mask, `STAT_FF_FF_RDY_WERT` | | | | | | |

### Hardware checks in Tool32

While parked, with `MSS54DS0.PRG`. Whether these checks set a monitor to "ready" or only test the hardware isn't documented.

| Check | Job | Result |
|---|---|---|
| Secondary-air system | `START_SYSTEMCHECK_SEK_LUFT`, then `LESEN_SYSTEMCHECK_SEK_LUFT` | |
| Leak-test pump and tank | `START_SYSTEMCHECK_DMTL`, then `LESEN_SYSTEMCHECK_DMTL`; `STATUS_TANK_DICHTHEIT` | |
| Purge valve | `STEUERN_TEV_CHECK` | |
| Secondary-air pump and valve | `STEUERN_SLP`, `STEUERN_SLV` | |

### Inspection day

- [ ] All lights, side markers and rear reflectors (kept on the modified bumper), and headlight aim
- [ ] Horn, wipers and washers; brakes, parking brake and tires
- [ ] ABS, DSC, airbag and check-engine lamps light at key-on, then go out
- [ ] No exhaust leaks
- [ ] Readiness monitors set, and a generic scanner reads your Touring's VIN from the DME
- [ ] Stored faults: only location 1 (0x01), the pump fault, and possibly 130 (0x82); `STAT_MIL_EIN` = 0
- [ ] Brought: your state's written answer, the donor's VIN and title, engine-number photos and receipts
- [ ] In California, the BAR Referee appointment booked first: (800) 622-7733

### Results and paperwork

| Visit | Date | Station | Result | To fix |
|---|---|---|---|---|
| First inspection | | | | |
| Re-test | | | | |
| BAR Referee (California) | | | | |

- [ ] In California, the Referee label fitted inside the engine compartment
- [ ] Registration and title updated as your state requires; agreed-value insurance, backed by receipts, photos and an appraisal
- [ ] Only now, the fallback parts sold
