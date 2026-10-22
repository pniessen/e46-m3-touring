# Job cards

One card per phase of the build, in the guide's order; the longer phases take two or more cards so that each fits one printed page. Print them for the garage, or tick the boxes and type your readings here on a phone; longer records go on the [Worksheets](WORKSHEETS.md). Every value comes from the [build guide](README.md): check TIS for your car's build date before you tighten, fill or re-pin anything.

## Card 0: Paperwork and baseline

**Goal:** prove your Touring is the car this guide assumes, back it up and record its baseline ([Phase 0](README.md#phase-0-paperwork-and-baseline)).\
**Before you start:** the unmodified car with its original modules, and the [coding kit](README.md#factory-documentation-and-coding-kit).

**Tools:** Windows 10 or 11 laptop, run natively; K+DCAN cable (FTDI chip, pins 7 and 8 bridged, COM1, 1 ms latency timer); Standard Tools 2.12 with E46 data files; PA-Soft and its interface; a charger of at least 10 A.

- [ ] <span>VIN decoded: build date (facelift and FA from 09/2001), options, rear-drive 325i ([if it's an xi](README.md#if-your-car-is-a-325xi))</span>
- [ ] <span>Engine code M54B25 and a plastic tank, not the M56 SULEV: a manual doesn't prove it ([checks](README.md#check-your-own-touring-first)); VECI label's test group photographed</span>
- [ ] <span>DME label (MS43 to 02/2003, MS45.1 from 03/2003); DSC, not ASC only; IHKA or IHKR; switch panel</span>
- [ ] <span>Wiring drawings for both cars: WDS by build date, or ISTA by VIN ([manual](WIRING-AND-CODING.md#engine-harness-and-dme))</span>
- [ ] <span>Your state asked what an engine change needs, in writing ([questions](README.md#questions-for-your-state-program))</span>
- [ ] <span>Kit proven on the unmodified car ([manual](WIRING-AND-CODING.md#prove-the-setup-on-your-touring))</span>
- [ ] <span>FA or ZCS, every module's coding, cluster and LCM EEPROMs and fault lists saved ([Session 1](WIRING-AND-CODING.md#session-1-vehicle-order-and-codings))</span>
- [ ] <span>Odometer photographed; the mileage the cluster and the LCM each hold noted</span>
- [ ] <span>RACP at all four mounts; arches, sills, jacking points, battery box, floor at the tank brackets ([RACP](README.md#rear-subframe-mount-reinforcement))</span>
- [ ] <span>Ride height at four corners; alignment printout; photos of engine bay, E-box, harness and underside</span>
- [ ] <span>A/C blows cold; refrigerant recovery booked for [Card 4](#card-4-strip-your-touring)</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Coding kit | INPA shows two solid black dots and reads the DME, cluster, LCM, EWS and DSC; NCS Expert reads the FA or ZCS | |
| Backups | FA or ZCS screenshots, a coding file per module, cluster and LCM EEPROM files and fault lists, stored in two places | |
| Your car | Engine code, tank, DME, DSC, climate control and switch panel recorded | |
| Shell | RACP, arches, sills and jacking points inspected and photographed | |
| Your state | Written answer on what the engine change needs | |
| Mileage | Odometer photographed; cluster and LCM mileage noted | |
| Ride height | Hub-center and arch-lip heights at four corners, level ground, placard pressures | |

**Watch:** [50sKid – coding the vehicle order (2017), 08:52](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=532s) reads the FA from an E46's cluster.\
**Stop and ask:** never back up or code anything until the kit reads every module. An xi, an M56 or an ASC-only car, a torn or rotten floor, or no written answer from your state: re-plan before you buy a donor.

## Card 1: Buy and inspect the donor

**Goal:** buy a manual M3 that meets the model-year rule, and record what you can't test once it's apart ([Phase 1](README.md#phase-1-buy-and-inspect-the-donor)).\
**Before you start:** [Card 0](#card-0-paperwork-and-baseline) done, with your state's written answer in hand.

**Tools:** compression and leak-down testers; a fuel-pressure gauge with an adapter and a relay bypass jumper; INPA, Tool32 and PA-Soft; tape measure, plumb line and a level floor.

- [ ] <span>Manual M3s shortlisted, same model year as your Touring or newer ([Choose the donor](README.md#choose-the-donor))</span>
- [ ] <span>VIN, build date and an engine-number photo; for its DSC, a donor built 09/2002 or later (MK60)</span>
- [ ] <span>Compression and leak-down, warm, all plugs out; cylinders compared</span>
- [ ] <span>Hood, fenders, headlights, bumper, both rear arches with their inner lips, and trunk floor sound</span>
- [ ] <span>INPA: every module's part number, software and faults; MK60 or MK20</span>
- [ ] <span>Tool32: DME identity, fault memory and AIF saved ([Session 2](WIRING-AND-CODING.md#session-2-dme-vin-ews-delete-and-gearbox-software)); PA-Soft: cluster EEPROM saved</span>
- [ ] <span>Tool32 VANOS timing and leak tests, warm; fuel pressure through a relay bypass</span>
- [ ] <span>Road test: all gears, diff, clutch, steering, brakes, ABS, DSC and cold A/C</span>
- [ ] <span>Tire placard and underhood A/C and emissions labels photographed</span>
- [ ] <span>Hub, lip and body-point heights and lip offsets at four corners ([how](README.md#measure-and-mock-up-before-you-cut))</span>
- [ ] <span>Refrigerant recovery booked while it can still be driven or towed to a shop</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Compression | About 11–12 bar (160–174 psi) minimum, about the same on every cylinder (compilation figure; confirm in TIS); leak-down even | |
| VANOS and fuel | VANOS tests recorded; fuel pressure 5.0 ± 0.2 bar (72.5 ± 2.9 psi) | |
| Electronics record | Module IDs and faults, DME identity and AIF, and cluster EEPROM saved | |
| DSC | Unit type noted: MK60 or MK20 | |
| Measurements | Hub, lip and body-point heights and lip offsets at four corners, with hub-to-body and hub-to-lip worked out; placard and labels photographed | |
| Paperwork | Title or salvage paperwork and bill of sale in hand; engine number and VIN plates photographed | |

**Watch:** [Autoalex Cars – Part 1 (2023), 00:40](https://www.youtube.com/watch?v=RyoFFLppseE&t=40s) inspects a donor M3 on a ramp.\
**Stop and ask:** low or uneven compression means a head or engine job, or walk away. An MK20 means keeping your Touring's DSC (option A). Don't buy without the paperwork.

## Card 2a: Strip the donor

**Goal:** every donor part off, tagged and stored dry ([Phase 2](README.md#phase-2-strip-the-donor)).\
**Before you start:** [Card 1](#card-1-buy-and-inspect-the-donor) done; dry storage for two cars' parts ([logistics](README.md#space-storage-and-logistics)).

**Tools:** an engine hoist with a load leveler, or a lift; transmission jack, stands and straps; approved fluid containers; tags, bags and a camera.

| Area | Take (the [Parts list](README.md#parts-list)'s Donor M3 lines; easy to miss) |
|---|---|
| Cabin | Cluster; console switch unit 61316925520 (coupe) or 61316925521 (convertible); clutch-switch module 61319122700; accelerator pedal; shift lever and carrier; mirrors; steering wheel (airbag disarmed per BMW's procedure first) |
| Engine bay | Engine harness with the DME, gearbox-module harness and the whole E-box branch (fuse carrier, X6011, X6021, X6053, X6054, battery feed X64101/X64102); expansion-tank and secondary-air pump brackets; radiator, both fans, oil cooler and lines; power-steering reservoir, lines and cooler; A/C lines; DSC unit, its lines and the master cylinder (booster too for option B) |
| Underside | Fuel filter-regulator with its vacuum hoses; fuel lines 16122229409, 16122229410, 16122229411; exhaust with hangers and heat shields; front heat shields; driveshaft; clutch hard line; front brake hoses 34322229723 |
| Running gear | 420G with gear-identification switch 23142229113; rack, tie rods and lines, control arms and brackets, struts, knuckles, hubs, brakes, sway bar and links, front reinforcement plate; rear axle as one unit with push rod 33312229295 and V-brace 33312229899; wheel-speed sensors from an MK60 donor (09/2002 on) |

- [ ] <span>A shop recovers the refrigerant before any A/C line is opened; receipt kept</span>
- [ ] <span>Oil, coolant, gearbox, diff, power-steering and brake fluid and fuel drained into approved containers ([Safety](README.md#safety))</span>
- [ ] <span>Both halves of every connector tagged; everything photographed; fasteners bagged by assembly</span>
- [ ] <span>Car supported or strapped before the engine or an axle comes out</span>
- [ ] <span>Cabin, engine-bay and underside parts off and tagged</span>
- [ ] <span>Engine and gearbox out: front subframe dropped with the engine (lift), or gearbox out and engine out the top</span>
- [ ] <span>Front axle and steering off; rear axle out as one unit ([Driveline and rear axle](README.md#driveline-and-rear-axle))</span>
- [ ] <span>An MK60 donor's wheel-speed sensors kept as spares; an MK20 donor's don't fit your harness</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Parts | Every Donor M3 line on the parts list removed, tagged, photographed and stored dry | |
| Fluids | Refrigerant recovered (receipt kept); all fluids drained and disposed of | |

**Watch:** [DBO – pulling an E46 M3 engine (2019), 27:01](https://www.youtube.com/watch?v=SH-J8ngKerk&t=1621s).\
**Stop and ask:** never open an A/C line before recovery: venting is prohibited. A part missing or damaged: order it now, while you can still compare it with the donor.

## Card 2b: Cut the donor steel

**Goal:** the front panels off and the arch, filler and floor steel cut out, then the shell gone ([Phase 2](README.md#phase-2-strip-the-donor)).\
**Before you start:** [Card 2a](#card-2a-strip-the-donor) done; the donor's arch targets measured ([Card 1](#card-1-buy-and-inspect-the-donor)).

**Parts:** both rear arch areas; fuel filler flap 51172695524 with its surround; trunk floor with front reinforcement 51717894229 (coupe) and muffler brackets 41122494844, 41112493931; V-brace mounting boxes with their reinforcement panels if you'll fit the V-brace.\
**Tools:** spot-weld drill bits and a spot-weld chisel; cut-off discs; cardboard; a profile gauge.

- [ ] <span>Hood, fenders, headlights, bumper with carrier and supports, kidney grilles and liners off</span>
- [ ] <span>Cardboard templates of each rear flare at three or four stations, before you cut</span>
- [ ] <span>Both rear arch areas cut with generous margins: outer skin and as much inner tub as you can ([how](README.md#rear-arches-and-doors))</span>
- [ ] <span>Spot welds drilled out where you can, instead of cutting</span>
- [ ] <span>Fuel filler flap cut out with its surround</span>
- [ ] <span>Trunk floor round the muffler cut out with its reinforcement and the muffler brackets</span>
- [ ] <span>V-brace mounting boxes cut out with their reinforcement panels, if you'll fit the V-brace</span>
- [ ] <span>SMG parts, interior, glass or a convertible's top sold; the donor's DSC unit kept until your DSC plan has worked</span>
- [ ] <span>Shell and title disposed of as your state requires ([logistics](README.md#space-storage-and-logistics))</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Body steel | Arches with inner tubs, filler surround and floor section cut with margins; templates made | |
| Shell | Shell and title disposed of as your state requires | |

**Watch:** [M346 Projects – SMG Touring build Pt 1 (2023), 06:40](https://www.youtube.com/watch?v=YqM2rQw1HQI&t=400s) cuts the quarters and trunk floor from a convertible donor.\
**Stop and ask:** rotten or damaged donor steel: plan new BMW or aftermarket panels now ([Rear arches and doors](README.md#rear-arches-and-doors)). Keep the donor's paperwork and engine-number photos either way.

## Card 3a: Bench work, rod bearings

**Goal:** new rod bearings, measured and tightened to the procedure for their bolts ([S54 refresh](README.md#s54-refresh-on-the-stand)).\
**Before you start:** the engine on a stand and drained; the bolt type read from the heads, not the build date.

**Parts:** rod bearings, blue 11247835440 (rod side) and red 11247835439 (cap side); rod bolts 11247834310 (12, M10 engines only); pan gaskets, pickup-tube O-ring.\
**Tools:** Plastigauge PG-1; E12 or 12 mm 12-point socket; angle gauge; 5–60 Nm wrench; dial gauge.

| Fastener | Torque | Notes |
|---|---|---|
| Rod bolts, M11×1.25, 12-point head (12 mm socket) | 5 Nm (44 in-lb), then 30 Nm (22 ft-lb), then 70° in one single stroke | Reused, each in the hole it came from |
| Rod bolts, M10×1.25, E-Torx head (E12) | Three cycles. Each cycle: 5 Nm, 30 Nm, then 105° in one single stroke. After cycles 1 and 2, back each bolt off about one turn. Cycle 3 is final | New bolts every time: 11247834310, 12 per engine |
| Oil-pump sprocket nut | 25 Nm (18 ft-lb) | Left-hand thread |
| Oil-pan screws, M6 | 10 Nm (89 in-lb); Flow gives 12 Nm (106 in-lb) for 10.9 screws | Hylomar at the joints (SI) |
| Oil drain plug | 25 Nm (18 ft-lb) | New sealing ring 07119963151 |

- [ ] <span>Every cap marked to its rod, every M11 bolt to its hole ([procedure](README.md#s54-refresh-on-the-stand))</span>
- [ ] <span>Oil pump off for room; its housing checked for chain rub</span>
- [ ] <span>Plastigauge on each clean, oil-free crank pin at bottom dead center, with the old bolts</span>
- [ ] <span>Below 0.040 mm: new shells; still below with new shells: a new rod</span>
- [ ] <span>Pins and shells oiled, caps on by their pair numbers, bolts tightened to their procedure</span>
- [ ] <span>Crank end play checked; oil pump and pan refitted</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Rod bearings | Plastigauge reads 0.040–0.070 mm on every rod (old bolts); final bolts fitted and tightened to the procedure for their type | |
| Crank end play | 0.141–0.253 mm (0.0056–0.0100 in) | |

**Watch:** [FCP Euro – S54 rod bearings (2022), 20:51](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1251s) shows the three M10 cycles; [Paul Vo – rod bearing torque procedure (2017), 08:00](https://www.youtube.com/watch?v=O345BKC8EkM&t=480s).\
**Stop and ask:** out of range: measure the journals; undersize shells mean a machine shop. Skipping the M10 procedure "will result in serious engine damage" (BMW). ARP bolts: [ARP's values](README.md#torque-values), never the angle method.

## Card 3b: Bench work, VANOS

**Goal:** VANOS seals, oil-pump disc, chain guide and hub sorted, and the cams timed ([S54 refresh](README.md#s54-refresh-on-the-stand)).\
**Before you start:** the engine on a stand; Beisan's S54 VANOS procedure, which this job follows.

**Parts:** VANOS seals and oil-pump disc (Beisan BS025); Torx exhaust-sprocket bolts; upper chain guide, tensioner; new exhaust hub if a tab is cracked.\
**Tools:** crank socket 83300491056 (36 mm 12-point on early engines); 32 mm fan wrench, pulley holder 83300491046; S54 timing set; transfer-gear holder.

| Fastener | Torque | Notes |
|---|---|---|
| VANOS solenoid coil screws | 4 Nm (35 in-lb) | One video only |
| VANOS piston covers, lower VANOS bolts, solenoid-block screws | 10 Nm (89 in-lb) | One video only |
| VANOS transfer-gear cover | 55 Nm (41 ft-lb) | One video only |
| VANOS exhaust sprocket Torx bolts | 12 Nm (106 in-lb) with blue thread-locker | One video only |
| Upper chain guide bolt; chain tensioner | Guide 24 Nm (18 ft-lb); tensioner snug plus ½ turn with a new washer | One video only |
| VANOS hub bolts (new M6×25) | About 14 Nm (124 in-lb), by feel, because no torque wrench fits | One video only |
| Fan clutch to water pump | 40 Nm (30 ft-lb) | Left-hand thread: loosen it clockwise |

- [ ] <span>Engine turned on the four balancer bolts, never on the cover's 32 mm hex; balancer inspected</span>
- [ ] <span>Seals and oil-pump disc renewed by Beisan's procedure ([VANOS](README.md#s54-refresh-on-the-stand))</span>
- [ ] <span>Exhaust-hub tabs inspected: the new disc takes out play; a cracked tab means a new hub</span>
- [ ] <span>Upper chain guide and tensioner renewed; Torx sprocket bolts in place of the hex bolts</span>
- [ ] <span>Cams re-timed: the cam bridge sits flat and the crank pin slides in</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| VANOS | New seals and oil-pump disc; exhaust-hub tabs intact or the hub replaced; the cam bridge sits flat and the crank pin slides in after reassembly | |

**Watch:** [ECS Tuning – S54 VANOS rebuild (2025), 17:30](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1050s), which fits E39 M5 (S62) diaphragm springs and plates.\
**Stop and ask:** if the cam bridge won't sit flat or the crank pin won't slide in, re-time before the covers go on. The VANOS torques are one video's: check TIS group 11 36.

## Card 3c: Bench work, valves and seals

**Goal:** valve clearances in range and the top-end seals renewed before the engine goes in ([S54 refresh](README.md#s54-refresh-on-the-stand)).\
**Before you start:** the engine on a stand and cold (below 35 °C).

**Parts:** valve shims; valve-cover gasket and spark-plug-tube seals; CPV O-ring; rear main seal; water pump, thermostat and their gaskets.\
**Tools:** feeler gauges; a micrometer; a magnet.

| Fastener | Torque | Notes |
|---|---|---|
| Spark plugs, M12×1.25 | **No BMW figure found; the videos disagree:** 23 Nm (17 ft-lb), dry, or 25 Nm (18 ft-lb) | Check TIS |
| Valve-cover cap nuts | **No BMW figure found; the videos disagree:** 10 Nm (89 in-lb) or 8 Nm (71 in-lb), in a cross pattern | Check TIS |
| Crankcase-vent return banjo (17 mm) | 19 Nm (14 ft-lb) | New washers; one video only |

- [ ] <span>Plugs out; engine turned clockwise; each valve measured with its lobe pointing straight up ([valves](README.md#s54-refresh-on-the-stand))</span>
- [ ] <span>Valley packed with rags before any shim is lifted: early heads have no screen in the drain gallery</span>
- [ ] <span>Old shim measured; new shim = old shim + (measured clearance − target)</span>
- [ ] <span>Clearances set to the middle of the range: 0.20 mm intake, 0.30 mm exhaust</span>
- [ ] <span>CPV O-ring, valve-cover gasket, rear main seal, water pump and thermostat renewed</span>
- [ ] <span>Throttle actuator tested; idle control valve cleaned</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Valves | Intake 0.18–0.23 mm, exhaust 0.28–0.33 mm, measured below 35 °C | |

**Watch:** [FCP Euro – S54 valve adjustment (2022), 17:19](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1039s).\
**Stop and ask:** a clearance out of range: re-shim before the cover goes on. The spark-plug and cover-nut torques come from videos that disagree: use TIS.

## Card 3d: Bench work, clutch and 420G

**Goal:** flywheel, clutch and driveshaft flex disc on new fasteners, and the 420G resealed ([Phase 3](README.md#phase-3-bench-work), [driveline](README.md#driveline-and-rear-axle)).\
**Before you start:** the engine on its stand with the rear main seal done ([Card 3c](#card-3c-bench-work-valves-and-seals)).

**Parts:** dual-mass flywheel 21212229900 and clutch set 21212282667; flywheel bolts 11222243051 (8); pressure-plate screws 21207548052 (6); pilot bearing 11211720310; 420G seals 23121228493, 23127501582, 23121222769; flex disc 26112226527 with bolts 26117635643 and nuts 26127536563; center mount 26122282495.\
**Tools:** a clutch alignment tool; a flywheel lock.

| Fastener | Torque | Notes |
|---|---|---|
| Dual-mass flywheel to crank | 105 Nm (77 ft-lb), no angle | Eight new bolts 11222243051, threads lightly oiled, no thread locker; cross pattern |
| Pressure plate to flywheel, M8 10.9 | 34 Nm (25 ft-lb) | Six new micro-encapsulated screws 21207548052; 25 Nm is for 8.8 screws |
| 420G drain and fill plugs, M24×1.5 | 52 Nm (38 ft-lb) | Reverse-light switch 20 Nm (15 ft-lb) |
| Flex disc (guibo), M3, M12 10.9: shaft side | 115 Nm (85 ft-lb) | M12×1.5×62 bolts 26117635643 with new self-locking nuts 26127536563; turn the bolt, not the nut. Gearbox side: Card 9b |

- [ ] <span>New flywheel bolts, lightly oiled, tightened in a cross pattern ([clutch](README.md#driveline-and-rear-axle))</span>
- [ ] <span>Pilot bearing renewed; disc centered with the alignment tool; pressure plate on new screws</span>
- [ ] <span>Release-fork pivot pin, fork and guide tube: FCP Euro's M3 clutch job renews them</span>
- [ ] <span>420G: new input, selector-shaft and output seals; fill plug undone before the drain plug</span>
- [ ] <span>Gear-identification switch checked or replaced; new shifter bushings</span>
- [ ] <span>Driveshaft: new flex disc bolted to the shaft on the M3's bolts and new self-locking nuts; new center mount</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Clutch and 420G | Flywheel and pressure plate on new bolts, torqued and marked; three new gearbox seals; gear switch fitted | |

**Watch:** [FCP Euro – E46 M3 clutch (2022), 17:19](https://www.youtube.com/watch?v=NmEOFBqreX8&t=1039s).\
**Stop and ask:** anything wrong here is a gearbox-out job later: fix it now. Ignore the 100 Nm in FCP's non-M DIY and the 120 Nm seen in snippets.

## Card 3e: Bench work, axles

**Goal:** both M3 axles rebuilt, and the running gear chosen for the arch mock-up ([Phase 3](README.md#phase-3-bench-work)).\
**Before you start:** the axles off the donor ([Card 2a](#card-2a-strip-the-donor)); a press and bushing tools.

**Parts:** subframe mounts 33312283573/574 and 33312283419 (two); diff mount 33172282484; trailing-arm bushings; worn arms, ball joints, end links; pads, rotors.\
**Tools:** bushing press kits; a ball-joint separator.

| Fastener | Torque | Notes |
|---|---|---|
| Diff front mount bolt, M14×1.5×65 10.9 | 200 Nm (148 ft-lb) | Not Condor's 128 ft-lb (174 Nm) |
| Diff rear bolts, M12×50 Torx, ×2 | 20 Nm (15 ft-lb) + 90° | Not Condor's 70 ft-lb (95 Nm) |
| Rear caliper carrier, M10 | 65 Nm (48 ft-lb) | Micro-encapsulated screws |
| Front caliper carrier, M12×1.5 | 110 Nm (81 ft-lb) | — |
| Caliper guide bolts, front and rear | 30 Nm (22 ft-lb) | — |
| Rotor retaining screw | 16 Nm (142 in-lb) | — |

- [ ] <span>Subframe and diff mounts, trailing-arm bushings, worn arms, ball joints and end links renewed ([axles](README.md#driveline-and-rear-axle))</span>
- [ ] <span>Rear control arms fitted to the subframe before the diff; then the diff, its mounts torqued here</span>
- [ ] <span>No powder coat in the bushing bores</span>
- [ ] <span>A diff output flange that comes out: its bolt marked first and refitted to the mark</span>
- [ ] <span>Brakes rebuilt with new pads and rotors</span>
- [ ] <span>Rubber-bushed joints left snug, for ride height later</span>
- [ ] <span>Springs, dampers, wheels and tires chosen and bought ([suspension](README.md#suspension-for-touring-weight), [wheels](README.md#wheels-track-and-offsets))</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Axles | Bushings, mounts and arms renewed; the diff on the subframe with its mount bolts torqued; bolts marked, rubber-bushed joints left snug | |
| Running gear | Springs, dampers, wheels and tires in hand for the Card 6 mock-up | |

**Watch:** [FCP Euro – E46 M3 control arms and bushings (2020), 12:23](https://www.youtube.com/watch?v=usfbSLE_1aI&t=743s).\
**Stop and ask:** a bushing that went in crooked: re-press it. Don't start the arches ([Card 6](#card-6-rear-arches)) without your final springs, dampers, wheels and tires.

## Card 3f: Bench work, DME, cluster and fenders

**Goal:** the DME flashed with your VIN and nothing else, the M3 cluster prepared, and the front fenders grafted ([Phase 3](README.md#phase-3-bench-work)).\
**Before you start:** the donor DME's identity, faults and AIF saved ([Card 1](#card-1-buy-and-inspect-the-donor)); your state's answer on DME software.

**Parts:** the donor DME; the M3 cluster; genuine M3 fenders 41357894337/338 and your 4-door fenders, or carbon Touring fenders.\
**Tools:** MIG welder; clamps; hammers and dollies.

- [ ] <span>DME sent away for the EWS delete with your Touring's full 17-character VIN ([Immobilizer (EWS)](README.md#immobilizer-ews))</span>
- [ ] <span>SMG donor: manual (HS) software or a transmission-swap change added</span>
- [ ] <span>Every secondary-air, O2-sensor, catalyst and EVAP delete declined ([brief](README.md#shop-briefs))</span>
- [ ] <span>No Euro software: it may drop US emissions functions such as the fuel-tank leak test</span>
- [ ] <span>Sync route only with a virgin DME: a used one keeps its code table for good</span>
- [ ] <span>Cluster service (if used): your VIN, set to take your true mileage, rear-door LEDs added ([cluster](README.md#instrument-cluster-and-mileage))</span>
- [ ] <span>Genuine M3 fenders grafted off the car onto your 4-door fenders' rear strips ([fenders](README.md#front-end-on-a-4-door-body))</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| DME | Back from the vendor with a written list of changes: EWS delete, your VIN, manual software if needed, and nothing else | |

**Stop and ask:** any emissions function removed: send the DME back. The cluster shows only your car's true mileage ([49 U.S.C. §32704](https://www.law.cornell.edu/uscode/text/49/32704)).

## Card 4: Strip your Touring

**Goal:** a clean, dry, safely supported shell with the fuel system out ([Phase 4](README.md#phase-4-strip-your-touring)).\
**Before you start:** [Card 0](#card-0-paperwork-and-baseline) baseline recorded; refrigerant recovery booked; space for two cars' parts.

**Tools:** tall stands or a lift, straps, an engine hoist with a load leveler, transmission jack, a low table or dollies for the subframes, wheel dollies; approved fuel containers; an extinguisher; a pressure washer.

- [ ] <span>A shop recovers the refrigerant; every opening capped ([Shop briefs](README.md#shop-briefs))</span>
- [ ] <span>Battery disconnected; oil, coolant, power-steering fluid and brake fluid drained</span>
- [ ] <span>Tank run low, the rest pumped into approved containers outdoors, extinguisher at hand ([Safety](README.md#safety))</span>
- [ ] <span>The saddle tank's left half checked separately: it empties through a siphon jet</span>
- [ ] <span>Exhaust, driveshaft, M54 and gearbox, front suspension and steering, and rear axle out</span>
- [ ] <span>Car supported or strapped before and after each heavy part comes out</span>
- [ ] <span>Tank and filler neck out; EVAP parts near the right-rear arch out; every line capped</span>
- [ ] <span>Rear seats, cargo-floor trim and carpet, rear trim, door cards, arch liners and battery out</span>
- [ ] <span>Sound-deadening stripped back from every weld line</span>
- [ ] <span>DME wires tagged first ([worksheet](WORKSHEETS.md#electronics-baseline)); M54 harness and DME out for resale; the body harness stays</span>
- [ ] <span>M54, 5-speed, DME and harness, 325i axle parts and front panels sold ([logistics](README.md#space-storage-and-logistics))</span>
- [ ] <span>Kept and labelled: every part on the [hold list](README.md#space-storage-and-logistics)</span>
- [ ] <span>Underside washed and dried; RACP, rails, inner arches and floor behind the tank and brake-pipe brackets re-checked</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| A/C | Refrigerant recovered (receipt kept); every opening capped | |
| Fuel | Both halves of the tank drained; tank, filler neck and EVAP parts out and stored away from the work area | |
| Support | Shell stable on stands or the lift with the engine and axles out | |
| Fallback parts | Every part on the hold list labelled and stored | |
| Inspection | Underside clean and dry; new findings photographed and added to Card 5 | |

**Watch:** [Tracks and Trails – M54 removal (2025), 06:20](https://www.youtube.com/watch?v=3ud3sHHYU5g&t=380s) supports the rear once the engine is out.\
**Stop and ask:** re-position the supports before anyone works under the car. Fuel left in the left half: drain it through its sender opening. Don't sell the fallback parts yet.

## Card 5: Subframe mounts and floor

**Goal:** rear subframe mounts reinforced and the floor closed round the M3 axle and muffler ([Phase 5](README.md#phase-5-metalwork-1-subframe-mounts-and-floor)).\
**Before you start:** [Card 4](#card-4-strip-your-touring) done, fuel parts and battery out; donor floor cut ([Card 2b](#card-2b-cut-the-donor-steel)).

**Parts:** a reinforcement kit listed for the Touring; V-brace boxes; donor floor or new 41127895619, muffler brackets 41122494844, 41112493931; primers, seam sealer, cavity wax.\
**Tools:** MIG with 0.023–0.024 in or 0.030 in wire, 75/25 argon/CO2 ([settings](README.md#welding-settings-and-safety)); spot-weld drill; clecos; fume extraction and respirator; tram gauge.

- [ ] <span>Coupons welded in the real thicknesses and broken; extraction and a fire watch set up</span>
- [ ] <span>Body diagonals across the rear and front subframe points measured and written down</span>
- [ ] <span>Bare metal; cracks stop-drilled and welded; failed spot welds re-welded</span>
- [ ] <span>Underside plates welded, with the kit's spacers ([reinforcement](README.md#rear-subframe-mount-reinforcement))</span>
- [ ] <span>Spare-wheel well opened by the cut rules, RACP and rail flanges whole ([floor](README.md#exhaust-and-the-spare-wheel-well))</span>
- [ ] <span>From above: three rosette welds on each rear mount, failed rail spot welds, rail plates</span>
- [ ] <span>Front-mount top welds through the cabin floor under the rear seat; opening patched</span>
- [ ] <span>V-brace mounting boxes welded in, if you'll fit the V-brace</span>
- [ ] <span>Fit check with the M3 subframe, diff and muffler; donor hanger brackets welded on</span>
- [ ] <span>Floor closed at about factory spot-weld spacing; battery tray fits; diagonals measured again</span>
- [ ] <span>Primer, seam sealer both sides, underbody coating, cavity wax; no structural foam while welding remains</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Test coupons | Broken coupons tear the metal, not the weld; plug welds penetrate without blowing holes | |
| Repairs | Every crack stop-drilled and welded; failed spot welds re-welded | |
| Reinforcement | Underside plates, rear-mount rosette welds, front-mount top welds and any rail plates and V-brace boxes done, with penetration visible from inside where you can see | |
| Fit check | M3 subframe and muffler clear the new floor; hanger brackets line up | |
| Diagonals | Match your before-welding figures | |
| Protection | All seams sealed both sides, primed, coated and cavity-waxed | |

**Watch:** [Tracks and Trails – RACP plates on a Touring (2025), 07:20](https://www.youtube.com/watch?v=t4CtY_W3vpU&t=440s); [M346 Projects – Touring build Pt 14, body work (2024), 00:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=40s); [Tracks and Trails – perfecting the Touring's rear end (2025), 03:20](https://www.youtube.com/watch?v=eMJLXbvzckE&t=200s).\
**Stop and ask:** diagonals off: stop; compare with BMW's body dimensions in TIS and have a body shop with a jig check. The kit makers recommend a professional shop ([brief](README.md#shop-briefs)).

## Card 6: Rear arches

**Goal:** M3 arch steel welded into both rear quarters around a mock-up of the final axle, wheels and tires ([Phase 6](README.md#phase-6-metalwork-2-rear-arches)).\
**Before you start:** [Card 5](#card-5-subframe-mounts-and-floor) done; final springs, dampers, wheels and tires in hand; the donor's hub-to-body and hub-to-lip figures.

**Parts:** the donor's arch steel; M3 filler flap 51172695524 and surround (hinge 51172695527 coupe, 51178151955 convertible); fill strips and gussets in your panel thickness; epoxy primer, seam sealer, cavity wax.\
**Tools:** MIG welder; a jack for each hub; profile gauge and the Card 2b templates; plumb line and tape; feeler gauges; hammers and dollies.

- [ ] <span>M3 rear axle in with final dampers, wheels and tires, springs out ([mock-up](README.md#measure-and-mock-up-before-you-cut))</span>
- [ ] <span>Each hub jacked to the donor's hub-to-body height, or your own target</span>
- [ ] <span>Full bump: bump stop fully compressed; the tire's outer face and top marked on the body</span>
- [ ] <span>Each new lip marked at the donor's hub-to-lip height and offset, checked from the center line</span>
- [ ] <span>Donor steel checked against your templates ([steel](README.md#rear-arches-and-doors))</span>
- [ ] <span>Outer skin tacked, then stitched in short runs ([graft](README.md#arch-graft-step-by-step))</span>
- [ ] <span>Inner arch extended, or the donor's inner tub grafted; gaps at the rocker and door filled</span>
- [ ] <span>Front of the flare dressed in; M3 filler flap and surround grafted with the right arch</span>
- [ ] <span>Filler neck trial-fitted in the M3 filler pot before the right quarter is sealed</span>
- [ ] <span>Doors decided with them shut and aligned ([Rear doors](README.md#rear-doors))</span>
- [ ] <span>Epoxy-primed, seam-sealed and cavity-waxed; mock-up axle out; filler waits for Card 13</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Symmetry | Lip heights above the hub centers, and lip offsets from the center line, match side to side | |
| Bump clearance | The tire clears the lip and inner arch with the bump stop fully compressed | |
| Doors | Doors open and close freely; shut gaps match the originals (feeler gauges) | |
| Filler | The neck reaches and seals in the M3 filler pot; the flap opens and closes | |
| Inner lip | A sealed, double-skin edge all round | |
| Diagonals | Match your figures from before welding | |

**Watch:** [M346 Projects – Touring build Pt 14, body work (2024), 27:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1640s) grafts the inner tub; [Tracks and Trails – bodywork (2026), 12:40](https://www.youtube.com/watch?v=nADBRfX9DqY&t=760s); [M346 Projects – Pt 22 door flare (2025), 00:20](https://www.youtube.com/watch?v=c6PDOLC94K0&t=20s).\
**Stop and ask:** lips that don't match side to side: re-check the mock-up corner heights before you rework metal. A filler neck that doesn't seal fails the EVAP leak test: rework it before the quarter is sealed.

## Card 7a: Fuel system

**Goal:** the M3 filter-regulator and lines fitted and the pump proven at 5 bar before anything covers it ([Phase 7](README.md#phase-7-fit-the-m3-rear-axle-and-fuel-system), [Fuel system](README.md#fuel-system)).\
**Before you start:** [Card 6](#card-6-rear-arches) done; the tank still easy to drop; the K96 relay socket's pins (X10156) checked in WDS.

**Parts:** M3 filter 13327831089, regulator housing 13537830368 and 5-bar regulator 13531404089 on your bracket 13321435583; O-rings 13531720251, 13531720252 and lock ring 13531736234; M3 lines 16122229410, 16122229409, 16122229411; M3 vacuum hoses; M3 pump 16142229684 and baffle 16112229656 if yours fails; pump lock ring and seal; clamps.\
**Tools:** a fuel-pressure gauge with an adapter; a fused relay-bypass switch; a measuring jug.

- [ ] <span>Your pump kept and tested, or the M3 pump fitted with the M3 baffle</span>
- [ ] <span>Your own pump: the M3 rear feed's quick-disconnect fits its outlet, or your rear feed kept and adapted at the filter</span>
- [ ] <span>Tank refitted, never dropped or carried by its vent hoses</span>
- [ ] <span>Filter, housing and 5-bar regulator on your bracket, with new O-rings and lock ring</span>
- [ ] <span>M3 lines fitted; feed and return labelled and checked before they're connected</span>
- [ ] <span>Regulator vacuum hose routed toward the engine's air distribution pipe</span>
- [ ] <span>K96 socket bridged with the bypass switch (pins checked on WDS); gauge on the end of the front feed line</span>
- [ ] <span>Pressure, 20-minute hold and flow tested; every joint checked for leaks</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Fuel pressure | 5.0 ± 0.2 bar (72.5 ± 2.9 psi) static | |
| After 20 minutes | Above 4.5 bar (65 psi) after switch-off | |
| Fuel flow | At least 1.12 L in 30 s at 12 V, collected as TIS 13 31 describes | |
| Fuel leaks | None at any joint with the system pressurised; feed and return confirmed | |

**Stop and ask:** bleed-down of more than 0.5 bar: clamp the hoses to find whether the pump's check valve or the regulator leaks. Low pressure: regulator O-rings, filter, then the pump. Fix it before the axle goes in.

## Card 7b: Rear axle in

**Goal:** the M3 rear axle bolted in, with the push rod, V-brace and half-shafts ([Phase 7](README.md#phase-7-fit-the-m3-rear-axle-and-fuel-system), [axle](README.md#driveline-and-rear-axle)).\
**Before you start:** [Card 7a](#card-7a-fuel-system) passed; the axle rebuilt ([Card 3e](#card-3e-bench-work-axles)); springs and dampers rated for the Touring.

**Parts:** push rod 33312229295 with the kit's spacer plates; V-brace 33312229899 and bolts 33306760652; sway bar 33552282181 and links 33552283743; half-shaft bolts 33211227664 (12); collar nuts 33411133785; your parking-brake cables.\
**Tools:** a transmission jack or table; a torque wrench to 300 Nm; a torque-angle gauge.

| Fastener | Torque | Notes |
|---|---|---|
| Subframe studs, M12×1.5, to body | 90 Nm (66 ft-lb) | Before the axle goes up |
| Subframe collar nuts; rear M12×1.5×116 bolts | 77 Nm (57 ft-lb) | Front studs lined up first |
| Push rod (front support cradle) bolts, ×4 | 25 Nm (18 ft-lb) | Kit's spacer plates under it |
| V-brace bolts, ×3, M10×35 10.9 | 59 Nm (44 ft-lb) + 90° | Only with its mounting points |
| Half-shaft to diff flange, ×12 | 100 Nm (74 ft-lb) for the M3's black bolts | New bolts; 80 Nm is for silver ones |
| Rear drive-flange collar nut, M27×1.5 | 300 Nm (221 ft-lb) | New nut; oil the contact face lightly |
| Rear damper top-mount nuts, M8 (M3 parts); rod nut, M10×1 | 28 Nm (21 ft-lb); 14 Nm (124 in-lb) | New nuts; no Touring value |
| Trailing-arm bracket to body; the two M12 10.9 ball-joint bolts at the trailing arm | 77 Nm (57 ft-lb); 110 Nm (81 ft-lb) | Any position |

- [ ] <span>Studs torqued; axle raised level over them; push rod and spacers, collar nuts, rear bolts; V-brace if fitted</span>
- [ ] <span>Springs and dampers rated for the Touring; M3 sway bar and links</span>
- [ ] <span>Half-shafts on new bolts; brake lines; your parking-brake cables</span>
- [ ] <span>Your own wheel-speed sensors, or an MK60 donor's; never an MK20 donor's ([sensors](README.md#dsc-brakes-and-steering-angle))</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Rear axle | Every fastener torqued and paint-marked; push rod on its spacers | |

**Watch:** [Tracks and Trails – perfecting the Touring's rear end (2025), 35:00](https://www.youtube.com/watch?v=eMJLXbvzckE&t=2100s) raises the M3 axle into a Touring.\
**Stop and ask:** a subframe that binds: it must go up level over its studs. Never leave out the kit's spacer plates under the push rod (PS Designs calls them "ESSENTIAL").

## Card 7c: Rear axle at ride height

**Goal:** the rubber-bushed joints torqued at loaded ride height, the diff filled and the parking brake set ([Phase 7](README.md#phase-7-fit-the-m3-rear-axle-and-fuel-system)).\
**Before you start:** [Card 7b](#card-7b-rear-axle-in) done; the body on stands; a jack under the axle.

| Fastener | Torque | Notes |
|---|---|---|
| Trailing-arm through-bolt (arm to bracket) | 110 Nm (81 ft-lb) | Loaded ride height |
| Rear control-arm bolts at the subframe, M12 | 77 Nm (57 ft-lb) | Loaded ride height |
| Rear damper lower bolt, M12 | 100 Nm (74 ft-lb) | Loaded ride height |
| Rear anti-roll bar, links and brackets | 22 Nm (16 ft-lb) | Loaded ride height (rubber mounts) |
| Diff drain and fill plugs | 60 Nm (44 ft-lb) with an O-ring; 65 Nm (48 ft-lb) with a sealing washer | — |

| Fluid | Specification | Quantity |
|---|---|---|
| M variable differential | Genuine BMW SAF-XJ+FM 75W-140 GL-5 with its friction modifier (83222282583, 500 ml bottles) | 1.1 L (1.2 US qt); Turner says 1.2 L (unverified), so buy three bottles |

- [ ] <span>Shoes adjusted before the cable: up on the left, down on the right to lock, back 10 clicks ([how](README.md#brakes-and-bleeding))</span>
- [ ] <span>Cable slack taken up at the lever</span>
- [ ] <span>Diff filled to the fill plug with SAF-XJ+FM, not ordinary gear oil</span>
- [ ] <span>Axle jacked until the car just starts to lift off its stands; bushed joints torqued</span>
- [ ] <span>Every fastener paint-marked</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Rear axle | Bushed joints done at loaded height; every fastener paint-marked | |
| Diff | Filled to the fill plug | |
| Parking brake | Rear wheels turn freely with the lever down and lock with it up | |

**Watch:** [Tracks and Trails – perfecting the Touring's rear end (2025), 35:00](https://www.youtube.com/watch?v=eMJLXbvzckE&t=2100s) torques the bushed joints at ride height.\
**Stop and ask:** joints tightened at the wrong height: re-torque them at the right one. A leaking diff plug: check its seal.

## Card 8a: Front suspension

**Goal:** the M3 front suspension fitted to your front subframe ([Phase 8](README.md#phase-8-fit-the-m3-front-suspension-and-steering), [front axle](README.md#front-axle-and-steering-1)).\
**Before you start:** the front corners rebuilt ([Card 3e](#card-3e-bench-work-axles)); new self-locking nuts and bolts at hand.

**Parts:** M3 control arms 31122229453/454 and brackets 31122229623/624; struts, knuckles and hubs 31222229501; new end links; reinforcement plate 51717893609; new nuts and bolts ([consumables](README.md#consumables-and-single-use-parts)).\
**Tools:** a torque wrench to 300 Nm; a torque-angle gauge; a ball-joint separator.

| Fastener | Torque | Notes |
|---|---|---|
| Front axle support (subframe) to body, M12 10.9 | 110 Nm (81 ft-lb) | If it came down: rear bolts first; their dowels center it |
| Control arm to subframe, M14 self-locking nut | 90 Nm (66 ft-lb) | New nut |
| Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts; at ride height ([Card 12d](#card-12d-alignment-and-final-coding)) |
| Ball joint to knuckle, M12 self-locking collar nut | 65 Nm (48 ft-lb) | New nut; no impact wrench |
| Strut to knuckle clamp bolt, M12×1.5×55 10.9 | 81 Nm (60 ft-lb) | New bolt |
| Strut top mount to body, M8 collar nuts | 24 Nm (18 ft-lb) | — |
| Damper rod top nut, M14 | 64 Nm (47 ft-lb) | New nut |
| Front wheel-speed sensor bolt | 8 Nm (71 in-lb) | — |
| Front anti-roll bar link nuts, M10 | 65 Nm (48 ft-lb) | New nuts |
| Front anti-roll bar bracket nuts, M8 | 21 Nm (15 ft-lb) | At ride height |
| Front reinforcement plate, M10×35 10.9 | 59 Nm (44 ft-lb) + 90° | New bolts |
| Front hub collar nut (only if hubs are replaced) | 290 Nm (214 ft-lb) | New nut 31211128336 |

- [ ] <span>M3 control arms and brackets, struts, knuckles and hubs fitted ([order](README.md#front-axle-and-steering-1))</span>
- [ ] <span>Sway bar and new end links fitted</span>
- [ ] <span>Reinforcement plate on new bolts</span>
- [ ] <span>Rubber-bushed joints left snug, for ride height in Card 12d</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Fasteners | Torqued and paint-marked, except the rubber-bushed joints, which stay snug for Card 12d | |

**Watch:** [FCP Euro – E46 M3 control arms and bushings (2020), 15:58](https://www.youtube.com/watch?v=usfbSLE_1aI&t=958s).\
**Stop and ask:** move whole M3 corners: the M3 knuckle takes a bigger ball-joint taper, so non-M parts don't mix in.

## Card 8b: Steering

**Goal:** the M3 rack fitted and centered, with its tie rods and power-steering lines ([Phase 8](README.md#phase-8-fit-the-m3-front-suspension-and-steering)).\
**Before you start:** [Card 8a](#card-8a-front-suspension) done.

**Parts:** M3 rack 32132229397 (32132282642 on ZCP) with its tie rods and lines; steering-joint bolts 32306778609; tie-rod-end nuts 32216769539; new aluminium sealing washers for the banjos.\
**Tools:** an inner tie-rod tool.

| Fastener | Torque | Notes |
|---|---|---|
| Steering rack to subframe, M10 | 42 Nm (31 ft-lb) | — |
| Inner tie rod to rack | 100 + 10 Nm, as the compilation prints it | Check TIS for what the "+ 10" means |
| Outer tie-rod lock nut, M14 | 45 Nm (33 ft-lb) | — |
| Tie-rod end to knuckle, M12 self-locking | 65 Nm (48 ft-lb) | No impact wrench |
| Steering shaft lower joint Torx bolt, M8×33 | 22 Nm (16 ft-lb) | New bolt |

- [ ] <span>A replacement rack's hard lines checked against the subframe before it goes in</span>
- [ ] <span>Rack fitted; turns counted as you swap tie-rod ends, so the toe starts close</span>
- [ ] <span>Wheel straight, the shaft's notch lined up with the coupler's bolt hole; new pinch bolt ([steering](README.md#front-axle-and-steering-1))</span>
- [ ] <span>Power-steering lines connected, clear of the anti-roll bar and oil pan</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Steering | Wheel straight with the rack centered; full lock both ways without binding or line contact | |

**Watch:** [50sKid – rack replacement (2018), 12:35](https://www.youtube.com/watch?v=iwCoomDpICI&t=755s), on a non-M car with the same rack mounting.\
**Stop and ask:** binding or line contact at full lock: re-index the coupler or re-route the lines. After rack or tie-rod work the car needs an alignment ([Card 12d](#card-12d-alignment-and-final-coding)).

## Card 8c: Brakes and bleeding

**Goal:** the brake parts for your DSC option fitted, tested, filled and bled to a firm pedal ([Phase 8](README.md#phase-8-fit-the-m3-front-suspension-and-steering), [brakes](README.md#brakes-and-bleeding)).\
**Before you start:** DSC option chosen ([DSC, brakes and steering angle](README.md#dsc-brakes-and-steering-angle)); an MK20 donor means option A.

**Parts:** M3 front brake hoses 34322229723; option A keeps your DSC unit, booster and master cylinder; option B the M3 DSC unit and master cylinder, with new nuts 07129906196; brake fluid per the reservoir cap.\
**Tools:** a pressure bleeder with an airtight cap; a low-pressure air line for testing.

| Fastener | Torque | Notes |
|---|---|---|
| Brake line to caliper | 19 Nm (14 ft-lb) | — |
| Bleed screws | 7 mm: 3.5–5 Nm (31–44 in-lb); 11 mm: 12–16 Nm (106–142 in-lb) | — |
| Master cylinder to booster, M8 | 26 Nm (19 ft-lb) | New nuts |
| Wheel bolts, M12×1.5 | 120 ± 10 Nm (89 ± 7 ft-lb) | — |

| Fluid | Specification | Quantity |
|---|---|---|
| Brake and clutch fluid | **Not found.** Check the reservoir cap and TIS | Allow about 1.5 L (1.6 US qt) for filling and bleeding |

- [ ] <span>M3 front hoses fitted; every hose checked at full lock and full droop</span>
- [ ] <span>Your brake pipes kept: from 09/2002 the M3 uses the same front pipes, and the rear pipes and hoses are shared</span>
- [ ] <span>New hard lines tested with low-pressure air first, about 20 psi</span>
- [ ] <span>Filled and bled right rear, left rear, right front, left front</span>
- [ ] <span>A dry or replaced DSC unit: INPA's pump routine waits for [Card 11b](#card-11b-power-up-and-coding)</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Brake lines | Air test holds; after filling, no weeps at any union with the pedal held hard | |
| Pedal | High and firm after bleeding | |

**Stop and ask:** a soft pedal: bleed again before you go on. Don't drive until the pedal is firm.

## Card 9a: Engine and gearbox in

**Goal:** the S54 and 420G in on the M3 engine arms and new mounts, clear of the rack ([Phase 9](README.md#phase-9-install-the-s54-and-420g)).\
**Before you start:** the engine refreshed ([Cards 3a–3d](#card-3a-bench-work-rod-bearings)); the front axle in ([Card 8a](#card-8a-front-suspension)).

**Parts:** M3 engine arms and new engine mounts; gearbox support 22312229198 and mounts 22322282340; the secondary-air valve.\
**Tools:** an engine hoist with a load leveler, or a lift and a table for the subframe; a transmission jack.

| Fastener | Torque | Notes |
|---|---|---|
| Bellhousing Torx bolts | M8 28 Nm (21 ft-lb); M10 52 Nm (38 ft-lb); M12 98 Nm (72 ft-lb) | Flow's own general table gives 82 Nm (60 ft-lb) for M12 8.8; confirm the M12 value in TIS |
| Engine mount nuts, M10 | 45 Nm (33 ft-lb) | — |
| Engine support arm to block, M8 | 21 Nm (15 ft-lb) | — |
| Gearbox crossmember to body; gearbox mounts, M8 | 21 Nm (15 ft-lb) | — |
| Starter, M10 Torx | 45 Nm (33 ft-lb) | Leads: M5 5 Nm (44 in-lb), M6 7 Nm (62 in-lb), M8 13 Nm (115 in-lb) |
| Front axle support to body, M12 10.9 | 110 Nm (81 ft-lb) | Only if it came down; rear bolts first |

- [ ] <span>Secondary-air valve fitted; engine and 420G bolted together with the Card 3d clutch and flywheel</span>
- [ ] <span>M3 engine arms, new mounts and the 420G's gearbox support fitted</span>
- [ ] <span>Lowered in from above, or raised in on the subframe; oil-cooler lines unbolted so the cooler clears</span>
- [ ] <span>Before the mounts are tightened: oil pan clear of the rack and subframe ([fitting](README.md#driveline-and-rear-axle))</span>
- [ ] <span>Power-steering lines routed clear of the pan and sway bar</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Oil pan | Clear of the rack and subframe; power-steering lines clear of the pan and sway bar | |
| Mounts | Engine and gearbox mounts torqued and marked | |

**Watch:** [Project BMW – S54 into a Touring (2021), 05:20](https://www.youtube.com/watch?v=iVGU_Yg0ZLw&t=320s) installs the engine and gearbox together; [FCP Euro – E46 M3 clutch (2022), 26:34](https://www.youtube.com/watch?v=NmEOFBqreX8&t=1594s) fits the 420G.\
**Stop and ask:** the pan touching the rack or subframe: check the engine sits on the M3 arms correctly before you tighten anything.

## Card 9b: Driveshaft and clutch

**Goal:** shifter, driveshaft and clutch line in, the clutch bled and the 420G filled ([Phase 9](README.md#phase-9-install-the-s54-and-420g)).\
**Before you start:** [Card 9a](#card-9a-engine-and-gearbox-in) done; the car level for the gearbox fill.

**Parts:** shift carrier and lever with new bushings; M3 driveshaft 26112229240 with its new flex disc and center mount ([Card 3d](#card-3d-bench-work-clutch-and-420g)); clutch hard line 21522229675 and hose bracket 21522229699.\
**Tools:** a pressure bleeder or a slave-cylinder bleed tool; a hose clamp; a helper.

| Fastener | Torque | Notes |
|---|---|---|
| Flex disc (guibo), M3, M12 10.9: gearbox side | 115 Nm (85 ft-lb) | New self-locking nuts 26127536563; turn the bolt, not the nut |
| Driveshaft center mount | 21 Nm (15 ft-lb) | Preload the bearing 4–6 mm forward (compilation only) |
| Driveshaft to diff, M3 (ribbed M10×46 Torx, E14) | 70 Nm (52 ft-lb) | Mark the shaft's position before removal; it's balanced |
| Clutch slave cylinder nuts | 22 Nm (16 ft-lb) | Line unions 14–20 Nm (10–15 ft-lb) |
| 420G drain and fill plugs, M24×1.5 | 52 Nm (38 ft-lb) | Reverse-light switch 20 Nm (15 ft-lb) |

| Fluid | Specification | Quantity |
|---|---|---|
| Getrag 420G gearbox | Genuine BMW MTF-LT-2, 75W-80 GL-4 (83220309031) | 1.9 L (2.0 US qt); check the label on the gearbox |

- [ ] <span>Shift carrier and lever fitted with new bushings</span>
- [ ] <span>M3 driveshaft in: flex disc to the gearbox flange; center mount, bearing preloaded forward</span>
- [ ] <span>M3 clutch hard line fitted, the flexible hose clamped while you change lines</span>
- [ ] <span>Clutch bled after the brakes, at the slave's bleed screw ([bleeding](README.md#brakes-and-bleeding))</span>
- [ ] <span>420G filled to its fill plug with the car level</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Clutch | Pedal firm and returns; the slave's pushrod moves its full stroke (check from below with a helper) | |
| Driveshaft | Flex disc and center mount torqued; center bearing preloaded forward (the Flow compilation gives 4–6 mm) | |
| Gearbox | Filled to the fill plug, no leaks at the seals | |

**Stop and ask:** a soft clutch pedal: bleed again, then bench-bleed the slave ([Brakes and bleeding](README.md#brakes-and-bleeding)). A leaking gearbox seal: fix it now.

## Card 10a: Cooling and intake

**Goal:** radiator, fans, oil cooler, intake and A/C lines in, sensor leads routed, and the cooling system pressure-tested ([Phase 10](README.md#phase-10-cooling-intake-and-exhaust)).\
**Before you start:** the engine and gearbox in ([Card 9b](#card-9b-driveshaft-and-clutch)); the expansion-tank brackets welded in.

**Parts:** M3 radiator, fan clutch 11527831619, electric fan 64546988914 and shroud; new expansion tank 17112283344, thermostat and hoses; oil cooler and lines; power-steering reservoir, lines and cooler; A/C lines, new O-rings and drier 64538377330 or 64536917658.\
**Tools:** a cooling-system pressure tester; a 32 mm fan wrench and pulley holder.

| Fastener | Torque | Notes |
|---|---|---|
| Fan clutch to water pump | 40 Nm (30 ft-lb) | Left-hand thread: loosen it clockwise |
| Oil-cooler pipes | 25 Nm (18 ft-lb) | — |

| Fluid | Specification | Quantity |
|---|---|---|
| Coolant | BMW coolant, 50/50 with distilled water (unverified); system pressure 2 bar (29 psi) | **Capacity not found:** take it from TIS |

- [ ] <span>Radiator, both fans, oil cooler and lines; new expansion tank on the donor brackets ([cooling](README.md#cooling-and-oil-cooler))</span>
- [ ] <span>Intake and airbox; power-steering reservoir, lines and cooler</span>
- [ ] <span>Brake-booster vacuum hose: on the M3 it connects on the opposite side</span>
- [ ] <span>Coolant-level, washer and radiator-outlet sensor leads routed; every extension listed for Card 11a</span>
- [ ] <span>A/C lines with new O-rings and a new drier; system capped for the shop</span>
- [ ] <span>Cooling system filled and pressure-tested with the tester</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Cooling | Holds 2 bar (29 psi) on the tester with no drop and no leaks | |
| A/C | New drier and O-rings; system closed and capped for the shop | |
| Sensor leads | Every plug reaches its sensor without strain | |

**Stop and ask:** a drop on the tester: find and fix the leak before the first start. An O-ring you reused: replace it.

## Card 10b: Exhaust

**Goal:** the M3 exhaust in with every emissions part, hung from the Card 5 brackets and clear of the floor, tank and tires ([Phase 10](README.md#phase-10-cooling-intake-and-exhaust)).\
**Before you start:** [Card 10a](#card-10a-cooling-and-intake) done; a shop booked for the rear section if you won't build it ([brief](README.md#shop-briefs)).

**Parts:** M3 manifolds, catalysts and O2 sensors; secondary-air parts; mid-pipes; a rear section and the M3 muffler; heat shields; new gaskets and nuts; anti-seize.\
**Tools:** an O2-sensor socket; a jack to compress the suspension.

| Fastener | Torque | Notes |
|---|---|---|
| Exhaust manifold to front pipe (US S54) | 24 Nm (18 ft-lb) | New nuts and gaskets |
| O2 sensors | 50 Nm (37 ft-lb) | Anti-seize on the threads only |
| Exhaust flange, M8 | 22 ± 2 Nm (16 ± 1.5 ft-lb) | — |

- [ ] <span>M3 manifolds, catalysts and O2 sensors fitted; sensor plugs labelled so they can't be swapped</span>
- [ ] <span>Secondary-air parts and mid-pipes fitted</span>
- [ ] <span>Rear section built around the new floor on the Card 5 hangers ([floor](README.md#exhaust-and-the-spare-wheel-well))</span>
- [ ] <span>Heat shields over the muffler and near the tank, cargo floor and battery</span>
- [ ] <span>Clearance to floor, tank and tires checked with the suspension compressed</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Exhaust | Clears floor, tank and tires with the suspension compressed; heat shields fitted; new gaskets and nuts | |

**Stop and ask:** keep the M3 catalysts, all four O2 sensors and the secondary-air parts ([Registration and legal](README.md#registration-and-legal-us)). Contact anywhere: re-hang, or modify the rear section.

## Card 11a: Wiring and checks

**Goal:** the M3 engine harness and DME in, the body side re-pinned, and every moved wire checked before power-up ([Phase 11](README.md#phase-11-wiring-immobilizer-and-coding), [manual](WIRING-AND-CODING.md#engine-harness-and-dme)).\
**Before you start:** the DME back from the vendor ([Card 3f](#card-3f-bench-work-dme-cluster-and-fenders)); your DME family known ([how to tell](WIRING-AND-CODING.md#which-dme-your-touring-has)); its wires tagged before it came out.

**Parts:** the M3 engine harness, E-box branch, fuse carrier and DME; clutch-switch module 61319122700; gear switch 23142229113; terminals or repair leads for each housing (X6011 and X60004 differ); 0.35 mm² wire.\
**Tools:** depinning keys and a crimper; a multimeter with back-probe pins; labels.

- [ ] <span>Ignition off whenever a DME plug is joined or parted</span>
- [ ] <span>M3 harness routed; its whole E-box branch, fuse carrier and DME fitted; the M3's own X6053 and X6054 halves together</span>
- [ ] <span>X6011, X6021, X6053, X6054 and X64101/X64102 compared cavity by cavity before joining ([log](WORKSHEETS.md#e-box-plug-log))</span>
- [ ] <span>Body side re-pinned in the table's order: [MS43](WIRING-AND-CODING.md#ms43-touring-what-to-move) or [MS45.1](WIRING-AND-CODING.md#ms451-touring-what-to-move); re-pinned, not spliced</span>
- [ ] <span>Pin-5 ground to X1108 added; on an MS45.1, pins 2 and 15 (both SW/RT) tagged before they came out</span>
- [ ] <span>Pump wiring left alone: X60004 pin 10 to K96; X6021 pin 1 connected to nothing ([pump](WIRING-AND-CODING.md#checks-on-the-pump-circuit))</span>
- [ ] <span>M3 clutch-switch module fitted; its wire to EWS pin 8 stays ([cruise](WIRING-AND-CODING.md#clutch-switch-gear-switch-and-cruise))</span>
- [ ] <span>Sport button, if wanted ([switch center](WIRING-AND-CODING.md#sport-button-and-switch-center)); rear-door LEDs in the M3 cluster</span>
- [ ] <span>Heater valve: your plain one, or the M3's with its pump wired and coded; Card 10a lead extensions done</span>
- [ ] <span>Steps 1–19 of the [checks](WIRING-AND-CODING.md#checks-before-first-power-up) logged ([worksheet](WORKSHEETS.md#power-up-checks))</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Moved wires | Continuity end to end, open to ground (a meter proves wires; Card 11b proves the electronic parts) | |
| Leak-test triangle | Lowest element (the pump) on X60004 pin 30, heater on 18 | |
| Pump circuit | X60004 pin 10 reaches K96 socket pin 4; X6021 pin 1 reaches no K96 terminal | |
| Supplies | Terminal 15 at X60004 pin 26 above 9 V; grounds near 0 Ω | |
| CAN bus | About 60 Ω between X60004 pins 36 and 37, back-probed at the DME with every module plugged in, battery off (BMW) | |

**Watch:** [Tenza Motorsports – 5 things part 2 (2021), 08:45](https://www.youtube.com/watch?v=mDBiRn30fEs&t=525s) wires the Sport button into a Touring.\
**Stop and ask:** a pin that doesn't match the manual's table: stop and re-check. Never connect the US DME's pulsed pump output to the relay. Measure CAN at the DME, not at the diagnosis socket.

## Card 11b: Power-up and coding

**Goal:** first key-on, then the DME VIN, EWS, cluster and DSC sessions, in that order ([Phase 11](README.md#phase-11-wiring-immobilizer-and-coding), [coding](WIRING-AND-CODING.md#coding-step-by-step)).\
**Before you start:** [Card 11a](#card-11a-wiring-and-checks) checks passed; a charger of at least 10 A on; your Card 0 backups at hand.

**Parts:** the M3 cluster prepared for your VIN and true mileage (service, or a new M35080 chip); brake fluid for a DSC bleed.\
**Tools:** INPA, Tool32, NCS Expert and PA-Soft; a generic OBD-II scanner.

- [ ] <span>First key-on, no cranking: steps 20–29; INPA reaches every module; one prime ([what to expect](WIRING-AND-CODING.md#first-key-on-what-to-expect))</span>
- [ ] <span>DME VIN: Tool32 shows your full 17-character VIN, or write it to the next free AIF slot ([Session 2](WIRING-AND-CODING.md#session-2-dme-vin-ews-delete-and-gearbox-software))</span>
- [ ] <span>EWS: after a delete, nothing to sync; the key and clutch interlock read ([Session 3](WIRING-AND-CODING.md#session-3-ews))</span>
- [ ] <span>Cluster takes your true mileage from the LCM; no mileage ever written to the LCM ([Session 4](WIRING-AND-CODING.md#session-4-cluster-and-light-module))</span>
- [ ] <span>Cluster coded: its three lamp switches `nicht_aktiv`; `TANK_KENNLINIE` = `60_l_literskala`</span>
- [ ] <span>DSC coded; VIN and steering angle initialised, provisional until the alignment ([Session 5](WIRING-AND-CODING.md#session-5-dsc-coding-and-vin))</span>
- [ ] <span>A dry or replaced DSC unit bled with INPA's routine and a firm pedal, then conventionally</span>
- [ ] <span>Faults cleared in every module; ignition cycled; faults read again</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Modules | INPA reaches the DME, cluster, LCM, EWS, DSC and the rest | |
| Warning lamps | With the engine off, the red oil-pressure lamp and the charge lamp are lit | |
| Cluster | Shows your car's true mileage (compare with your Card 0 photo), with no tamper dot | |
| DME VIN | A generic OBD-II scanner shows your Touring's full VIN | |
| Clutch chain | With a gear engaged, `STAT_KRAFTSCHLUSS_EIN` = 1 with the pedal up and `STAT_KUP_EIN` = 1 with it down; in neutral both stay fixed | |
| Fuel pump | One prime at key-on; `STEUERN_EKP` clicks K96 | |
| Fault memory | Only location 1 (0x01), the pump fault, and possibly 130 (0x82) after an EWS delete | |

**Watch:** [50sKid – coding an E46 DSC unit (2016), 31:14](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=1874s), then the INPA VIN and steering-angle initialisation at [33:47](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=2027s).\
**Stop and ask:** an M3 DSC unit that won't clear "VIN not initialized": refit your Touring's unit. On a pre-09/2001 (ZCS) car, check that the LCM passes the mileage across. The cluster shows only your car's true mileage ([49 U.S.C. §32704](https://www.law.cornell.edu/uscode/text/49/32704)).

## Card 12a: Front end and oil prime

**Goal:** the front end on in primer, fluids in, and oil pressure proven while cranking with fuel and sparks off ([Phase 12](README.md#phase-12-front-end-first-start-and-shakedown)).\
**Before you start:** [Card 11b](#card-11b-power-up-and-coding) passed; fenders grafted ([Card 3f](#card-3f-bench-work-dme-cluster-and-fenders)); a charger of at least 10 A on for the session.

**Parts:** grafted fenders, M3 hood, headlights, kidney grilles, bumper with carrier and supports (fender supports 51118195295/96 on Tourings built from 09/2001).\
**Tools:** a mechanical oil-pressure gauge on a tee with an M12×1.5 adapter; a fuel-pressure gauge; Tool32.

| Fluid | Specification | Quantity |
|---|---|---|
| S54 engine oil | Castrol TWS Motorsport SAE 10W-60 or Castrol Formula RS 10W-60, BMW 07510009420 | 6.5 L (6.9 US qt) after a rod-bearing job. Fill, then check the dipstick |
| Power steering | **Not found.** Read the cap on the donor's M3 reservoir (ATF or CHF 11S) and don't mix the two | Not found |

- [ ] <span>Front end fitted; the bumper's lower opening and ducting kept for the oil cooler ([front end](README.md#front-end-on-a-4-door-body))</span>
- [ ] <span>Headlight wiring checked if they differ from yours; no driving after dark until Session 9</span>
- [ ] <span>Engine oil and power-steering fluid in; no drips under the car</span>
- [ ] <span>Oil gauge on a tee at the oil-pressure switch port; fuel gauge at the TIS 13 31 fitting</span>
- [ ] <span>Tool32 `MSS54DS0.PRG`: `IDENT` and `FS_LESEN` saved ([Session 6](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check))</span>
- [ ] <span>Fuel-pump relay K96 and injector relay K6327 pulled; six coil plugs off</span>
- [ ] <span>Interlock: no crank with the clutch up; cranks with it down</span>
- [ ] <span>Short bursts of cranking until the gauge shows pressure and the red lamp goes out; the tach moves</span>
- [ ] <span>Relays and coil plugs refitted</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Oil before firing | The gauge shows pressure while cranking with fuel and sparks disabled | |
| Start interlock | The starter turns only with the clutch down | |

**Watch:** [M346 Projects – Pt 13 first start (2024), 03:27](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=207s) primes the oil before refitting the pump fuse.\
**Stop and ask:** no pressure while cranking: stop and check the oil level, the pickup tube's O-ring and the pump before you crank again. Cranks with the clutch up: the clutch-switch wire to EWS pin 8.

## Card 12b: First start

**Goal:** adaptations reset, a clean first start, and hot-idle oil, fuel and trims checked ([Phase 12](README.md#phase-12-front-end-first-start-and-shakedown), [Session 6](WIRING-AND-CODING.md#session-6-first-start-adaptations-and-throttle-check)).\
**Before you start:** [Card 12a](#card-12a-front-end-and-oil-prime) passed; gauges still fitted; the charger on.

**Tools:** Tool32 with `MSS54DS0.PRG`; the oil and fuel gauges; your Card 1 VANOS readings.

| Fastener | Torque | Notes |
|---|---|---|
| Oil-pressure switch, M12×1.5 | 27 Nm (20 ft-lb) | Refitted once the gauge and tee come off |

- [ ] <span>Session 6 steps 2–5: adaptations and faults cleared; throttle self-test heard</span>
- [ ] <span>`STAT_WDK_ADAPT_WERT` reads 0; in gear the clutch bits follow the pedal; brake and Sport bits respond</span>
- [ ] <span>Key on, pump primes: 5.0 ± 0.2 bar (72.5 ± 2.9 psi); no leaks at the lines, filter-regulator or rail</span>
- [ ] <span>Started without touching the accelerator; oil pressure at once, or switch off</span>
- [ ] <span>Idling: no fuel, oil, coolant or power-steering leaks; no knocking or VANOS rattle</span>
- [ ] <span>Cooling bled as it warms; the electric fan runs ([cooling](README.md#cooling-and-oil-cooler))</span>
- [ ] <span>Hot idle: oil pressure, fuel below 5 bar with vacuum, steady idle, trims `STATUS_LAMBDA_ADD_1` and `_2` near zero</span>
- [ ] <span>Warm VANOS jobs (Session 6, step 7) compared with the donor's Card 1 readings</span>
- [ ] <span>Faults read in every module; then switched off, cooled, coolant topped up and oil checked</span>
- [ ] <span>Gauge and tee off; oil-pressure switch refitted; red lamp on at key-on, out once running</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Throttles | `STAT_WDK_ADAPT_WERT` = 0 after the reset; steady idle | |
| Hot oil pressure | At least 0.7 bar at hot idle (compilation figure; confirm in TIS) | |
| Fuel | 5.0 ± 0.2 bar at key-on, lower at idle with vacuum; no leaks | |
| Cooling | Temperature steady, no air in the system, fan cycles | |
| Oil-pressure switch | Refitted at 27 Nm with the gauge off; no oil at the port | |
| Fault memory | Only location 1 (0x01), the pump fault, and possibly 130 (0x82) after an EWS delete | |

**Watch:** [Tenza Motorsports – first start (2021), 05:38](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=338s).\
**Stop and ask:** no oil pressure at once: switch off. Low hot oil pressure: find the cause before you drive. Starts, then dies: not the immobilizer ([Won't start](WIRING-AND-CODING.md#wont-start)). Any fault besides the expected ones: fix it before you drive.

## Card 12c: Shakedown

**Goal:** brakes, ABS, wheel speeds and gauges proven on short drives near home ([Phase 12](README.md#phase-12-front-end-first-start-and-shakedown)).\
**Before you start:** [Card 12b](#card-12b-first-start) passed; a firm pedal; only the expected faults stored.

**Tools:** INPA; GPS; a measured amount of fuel.

| Fastener | Torque | Notes |
|---|---|---|
| Wheel bolts, M12×1.5 | 120 ± 10 Nm (89 ± 7 ft-lb) | Checked after the first drives |

- [ ] <span>Progressive stops on a quiet road, then a careful hard stop from moderate speed ([brakes](README.md#brakes-and-bleeding))</span>
- [ ] <span>Brakes bled again after the first few drives</span>
- [ ] <span>Parking-brake shoes bedded in on an empty road</span>
- [ ] <span>All four wheel speeds agree in INPA's DSC status while rolling ([sensors](README.md#dsc-brakes-and-steering-angle))</span>
- [ ] <span>Short drives near home; then paint marks, wheel-bolt torque, fluid levels and fault memory checked</span>
- [ ] <span>Fuel gauge and range follow a measured fill, starting near empty</span>
- [ ] <span>Speedometer compared with GPS: the M3 cluster over-reads by about 8.9% by design</span>
- [ ] <span>A/C vacuum-tested and charged by weight from the underhood label by a shop; it blows cold</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Shifts | Revs drop cleanly between gears | |
| Brakes and ABS | Firm pedal; ABS pulses in a hard stop; the car stops straight | |

**Stop and ask:** rev hang: check the clutch-switch chain first, then that the DME runs manual software. An ABS light, or wheel speeds that disagree: check the sensor plugs before you go further. Your brake lights don't come on when you slow with the parking brake.

## Card 12d: Alignment and final coding

**Goal:** the front joints torqued on the wheels, the car aligned, then the steering angle and the last coding sessions ([Phase 12](README.md#phase-12-front-end-first-start-and-shakedown), [Wheel alignment](README.md#wheel-alignment)).\
**Before you start:** [Card 12c](#card-12c-shakedown) passed; an alignment shop briefed ([Shop briefs](README.md#shop-briefs)).

**Tools:** INPA (or Tool32) and NCS Expert; the charger.

| Fastener | Torque | Notes |
|---|---|---|
| Control-arm bushing bracket to body, M10 | 59 Nm (44 ft-lb) | New bolts; at ride height |
| Front anti-roll bar bracket nuts, M8 | 21 Nm (15 ft-lb) | At ride height |

| E46 M3 target | Front | Rear |
|---|---|---|
| Total toe | 0°16' ± 7' | 0°22' ± 6' |
| Camber | −1°00' ± 20' (left/right difference max 30') | −1°45' ± 15' (left/right difference max 15') |
| Caster, ±10° / ±20° lock | 7°25' ± 30' / 7°40' ± 30' (left/right difference max 30') | — |
| Thrust angle | — | 0° ± 4' |

- [ ] <span>Front bushed joints torqued with the car's weight on its wheels</span>
- [ ] <span>Aligned to BMW's E46 M3 figures at the car's own loaded ride height</span>
- [ ] <span>Steering angle calibrated: wheel straight, no brake pressure, car level ([Session 7](WIRING-AND-CODING.md#session-7-steering-angle-after-the-alignment))</span>
- [ ] <span>DSC compensation routines run; faults cleared and read again</span>
- [ ] <span>Vehicle-order changes and body modules, if any ([Session 8](WIRING-AND-CODING.md#session-8-vehicle-order-changes-and-body-modules))</span>
- [ ] <span>Light module coded for the M3 headlights if they differ, then aimed at ride height ([Session 9](WIRING-AND-CODING.md#session-9-light-module-and-headlights))</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Alignment | BMW's E46 M3 values, set at the car's loaded ride height, with before and after printouts | |
| Steering angle | Calibrated after the alignment; INPA reads 0° with the wheel straight; DSC lamp out | |

**Watch:** [Evan Goyuk – E46 steering-angle calibration in INPA (2020), 02:48](https://www.youtube.com/watch?v=lseY6SRXWks&t=168s).\
**Stop and ask:** a sensor that won't hold 0° may be faulty ([DSC, brakes and steering angle](README.md#dsc-brakes-and-steering-angle)). If you change the vehicle order, code the other modules one at a time and reset the DME adaptations again.

## Card 12e: Break-in and readiness

**Goal:** the bearings broken in, the oil changed and every readiness monitor set ([Phase 12](README.md#phase-12-front-end-first-start-and-shakedown), [readiness](README.md#inspection-readiness)).\
**Before you start:** [Card 12d](#card-12d-alignment-and-final-coding) done; no faults but the expected ones.

**Parts:** oil filter set 11427833769; drain-plug sealing ring 07119963151.\
**Tools:** a generic OBD-II scanner; Tool32.

| Fastener | Torque | Notes |
|---|---|---|
| Oil drain plug | 25 Nm (18 ft-lb) | New sealing ring 07119963151 |
| Oil filter cover | 33 Nm (24 ft-lb) | Filter housing bolts 22 Nm (16 ft-lb) |

| Fluid | Specification | Quantity |
|---|---|---|
| S54 engine oil | Castrol TWS Motorsport SAE 10W-60 or Castrol Formula RS 10W-60, BMW 07510009420 | 5.5 L (5.8 US qt) for an oil change with filter. Fill, then check the dipstick |

- [ ] <span>1,200 miles (1,930 km) below 5,500 rpm and 105 mph (169 km/h), BMW's figures after new rod bearings</span>
- [ ] <span>Our checks (BMW lists none): oil and leaks at each fuel stop; faults at halfway ([log](WORKSHEETS.md#break-in-log))</span>
- [ ] <span>Closed-throttle coast-downs in gear, so the DME learns the crankshaft wheel</span>
- [ ] <span>Oil and filter changed at the end (our recommendation, not BMW's); oil and filter checked for metal</span>
- [ ] <span>No cleared codes or disconnected battery in the weeks before an inspection</span>
- [ ] <span>Fuel gauge proven first; tank 35–85% for the [drive plan](WIRING-AND-CODING.md#a-drive-plan-for-readiness), on two following days</span>
- [ ] <span>Leak test: engine off, after at least 20 minutes' driving that followed at least 5 hours parked, tank 15–85% full; every second time</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Break-in | 1,200 miles below 5,500 rpm and 105 mph done; oil changed; no metal in the oil or filter | |
| Readiness | A generic scanner shows every monitor ready (purge shows under EVAP). New York, for example, fails a 2001-or-later car with more than one not ready | |
| Fault memory | Only location 1 (0x01), the pump fault, and possibly 130 (0x82); `STAT_MIL_EIN` = 0 | |

**Stop and ask:** metal in the oil: stop driving and find its source. Fuel-tank leak test stuck: check its conditions, the leak-test wiring and the filler-neck seal ([Inspection readiness](README.md#inspection-readiness)).

## Card 13: Paint, trim and paperwork

**Goal:** final bodywork and paint, trim on, inspection passed and the paperwork done ([Phase 13](README.md#phase-13-paint-trim-and-paperwork)).\
**Before you start:** [Card 12e](#card-12e-break-in-and-readiness) done; the paint shop briefed ([Shop briefs](README.md#shop-briefs)).

**Parts:** paint; M3 side skirts with OEM M3 rocker clips; M3 mirrors on adapter bases, with older-type door harnesses on facelift doors; the M3 rear bumper and side brackets for the graft.\
**Tools:** guide coat and long sanding boards; feeler gauges; a plastic welder; a generic OBD-II scanner.

- [ ] <span>Filler, guide coat, block sanding and panel gaps done</span>
- [ ] <span>Painted; the shop briefed on your prep, the colour, and whether jambs and engine bay are included</span>
- [ ] <span>Trim, badges and side skirts on M3 rocker clips ([trim](README.md#rear-bumper-skirts-and-trim))</span>
- [ ] <span>Mirrors on adapter bases; older-type door harnesses on facelift doors</span>
- [ ] <span>Rear bumper with quad-tip cut-outs and the Touring bumper's center section grafted in; reflectors kept</span>
- [ ] <span>Flared doors: rubbing strips reshaped to follow the flare</span>
- [ ] <span>Inspection, registration and insurance; in California, a BAR Referee first ([legal](README.md#registration-and-legal-us))</span>
- [ ] <span>Fallback parts sold once the car has passed</span>

**Done when**

| Check | Pass | Reading |
|---|---|---|
| Lights | All lights, side markers and rear reflectors; headlight aim | |
| Horn and wipers | Horn, wipers and washers work | |
| Brakes and tires | Brakes, parking brake and tires | |
| Warning lamps | ABS, DSC, airbag and check-engine lamps light at key-on and then go out | |
| Exhaust | No exhaust leaks | |
| OBD | Readiness monitors set, and a generic scanner reads your Touring's VIN from the DME | |
| Inspection | Passed; in California, the Referee label fitted | |
| Paperwork | Registration and title updated as your state requires; agreed-value insurance in place | |

**Watch:** [M346 Projects – making an E46 M3 Touring rear bumper (2024), 00:20](https://www.youtube.com/watch?v=R2a68pcDo38&t=20s).\
**Stop and ask:** an emissions fail: see [Inspection readiness](README.md#inspection-readiness). Keep receipts, photos and the donor's paperwork together for the insurer.
