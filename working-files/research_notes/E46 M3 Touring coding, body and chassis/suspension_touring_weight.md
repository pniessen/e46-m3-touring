# Springs, dampers, ride height and alignment for an S54/M3-axle E46 Touring

Research date: 22 October 2026. Car: 2003 US 325i Touring (M54, 5-speed, RWD, Massachusetts), M3 front and rear axles from a 2003–06 US E46 M3 coupe or convertible donor.

How to read this file:

- **[read]** means I read the document or page itself (PDF text, HTML, an owner's-manual page image, ETK table, or video captions with timestamps). **[read, saved copy]** means I read a copy saved by an earlier research round of this project (in its scratchpad), not a fresh fetch. **[snippet]** means I saw only a search-engine summary.
- Every value says which car, body and date it belongs to. Anything not from an E46 is flagged, with a note on whether it transfers.
- Source ranking used: BMW documents (owner's manuals, training manuals ST0xx, TIS printouts, ETK via bmwfans.info, BMW USA spec sheets, BMW wheel/tyre lists), then documented builds, then suspension makers' data, then single forum posts.
- Blocked or unavailable, so not used: RealOEM (Cloudflare challenge), newTIS, brakeandfrontend.com/underhoodservice.com (Cloudflare block), eibach.ch (Cloudflare), notice-facile.com (Cloudflare), forum.rs246.com (522). I did not log in anywhere (FCP Euro's article prints public ETK credentials; I did not use them). The shared web-search budget ran out near the end; after that I only fetched pages whose URLs I already had.

---

## Takeaway (what changes in the guide)

1. **Weights are now BMW numbers, axle by axle.** BMW USA's spec sheets give the 2003 325i Sport Wagon (manual) 3,362 lb at 47.7/52.3, i.e. about **727 kg front / 798 kg rear**; the M3 coupe 3,415 lb at 50.3/49.7 (**779 / 770 kg**); the M3 convertible 3,781 lb at 49.9/50.1 (**856 / 859 kg**). Built the usual way, an S54 Touring should weigh about **1,584–1,614 kg (3,490–3,560 lb), about 760–772 kg front and 824–842 kg rear** (our estimate). The guide's current comparison mixes a US curb weight with a DIN weight and gets the direction wrong: in like-for-like US curb terms the stock 325i Touring is *lighter* than an M3 coupe, but carries ~28 kg more on its rear axle.
2. **The Touring's door-label ratings bind the finished car.** BMW's 2004 US Sports Wagon owner's manual gives the 325i Touring an approved **front axle load of 900 kg (1,984 lb), rear 1,210 kg (2,668 lb), GVWR 2,045 kg (4,509 lb, manual)**. The M3 coupe's are 970 / 1,150 / 2,020 kg, the M3 convertible's 990 / 1,170 / 2,100 kg (2003 US M3 manuals). The swap eats roughly 60–90 kg of payload; the front stays inside 900 kg in normal use but with only ~45–55 kg to spare at BMW's design load (our estimate).
3. **Front: M3 coupe parts suit.** The estimated front axle load is within 1–3% of an M3 coupe's, so the coupe's front struts (31312283103/104), springs and top mounts (31332229165/166) are the right baseline. A convertible donor's front springs are sized for ~856 kg and would probably stand the nose high (inference).
4. **Rear: the M3 rear axle needs ~7–9% more spring than an M3 coupe.** The estimated rear axle load (824–842 kg) sits between the M3 coupe (770 kg) and M3 convertible (859 kg). Spring seats and pads are common to the Touring, sedan and both M3s in ETK, so any E46 RWD rear barrel spring fits physically; choose by rate and height. Tenza's moved-over M3 coupe springs sat low enough to rub.
5. **Rear dampers and top mounts: no mystery.** BMW states the M3's rear shock-mount hole pattern is the same as standard (ST041). ETK shows the M3 rear top mount 33526779670 is also the mount on every non-M E46 convertible, which runs the *Touring's own* rear dampers; the Touring/sedan use 33521092362 with the same nuts. Use M3 dampers (coupe 33522283105, convertible 33522282267) or M3-fitment coilovers with the M3 trailing arms. No E46 Touring, US or European, has self-levelling.
6. **Ride height now has a BMW method, a BMW load and a BMW published height.** BMW measures from the lower edge of the wheel rim to the lower edge of the wheel housing (front spec in TIS group 31, rear in 33), with the car loaded 68 kg per front seat, 68 kg rear seat, 21 kg in the trunk and a full tank — except M3s, which BMW measures without ballast (BMW ST056, ST503). The E46 TIS ride-height *numbers* were still not found. For Massachusetts, BMW publishes the 325i Touring's height as **55.5 in / 1,409 mm (56.8 in / 1,444 mm with roof rails)**; measure roof and jacking-point heights, not arch lips, because the arches are replaced.
7. **Alignment: use the M3 test condition.** Align to BMW's TIS M3 values with the car unladen and the tank full (BMW: M3s are measured without weight), after checking ride height. E46 front camber can move only about ±0.5° through the slotted strut-tower holes once the locating pin is driven out (special tool 32 3 140); caster isn't adjustable; rear camber is set at an eccentric bolt, rear toe at the trailing-arm front mount (tool 32 3 030).
8. **Anti-roll bars and links have part numbers:** Touring 23 mm front (24 mm sport) and 18 mm rear (19 mm sport); M3 coupe 26 mm front, M3 convertible 27 mm front, both M3s 21.5 mm rear; front links 31356780847 are common to every E46; M3 rear links 33552283743.
9. **Tyre pressures (closes an open question):** BMW's 2003 US M3 owner's manuals give 33/35 psi (230/240 kPa) front/rear for up to four occupants and 41/48 psi (280/330 kPa) fully loaded, for both the 18- and 19-inch sizes.

---

## Q1. Weights, axle loads, design load and permitted axle loads

### Cited findings

**BMW USA spec sheets (US curb weight, weight distribution):**

- **2003 325 Sedan and Sport Wagon** [read, RTF attachment]: 325i Sport Wagon curb weight 3,362 lb (manual), 3,450 lb (automatic); distribution 47.7/52.3 (manual), 48.4/51.6 (automatic). 325i Sedan 3,219 lb, 50.3/49.7 (manual). Wagon height 55.5 in, sedan 55.7 in; track 57.9/58.4 in. Suspension: struts and "arc-shaped forged-aluminum lower arms" front, central-link multi-link rear; "Sport Package … sport suspension calibration"; standard wheels 16 × 7.0 with 205/55R16, Sport Package 17 × 8.0 with 225/45R17 W. [BMW USA, 2003 325 sedan and Sport Wagon](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437)
- **2003 330 coupe and convertible** [read]: 330Ci coupe 3,285 lb, 50.1/49.9 (manual); 330Ci convertible 3,616 lb, 48.7/51.3 (manual); both height 54.0 in. [BMW USA, 2003 330Ci](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41438)
- **2003 330 Sedan** [read]: 330i sedan 3,285 lb, 50.1/49.9 (manual). [BMW USA, 2003 330i](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41439)
- **M3 coupe and convertible** [read]: coupe 3,415 lb, 50.3/49.7; convertible 3,781 lb, 49.9/50.1; height 54.0 / 53.9 in. The 2002, 2003 and 2006 sheets print the same figures. [2002](https://www.press.bmwgroup.com/usa/article/attachment/T0022127EN_US/41385), [2003](https://www.press.bmwgroup.com/usa/article/attachment/T0022150EN_US/41463), [2006](https://www.press.bmwgroup.com/usa/article/attachment/T0019121EN_US/37451)

**BMW US owner's manuals ("Weights" pages):**

- **2004 325i/325xi Sports Wagon**, part no. 01 41 0 157 605, © 09/03 BMW AG, p.162 [read]: 325i curb weight 3,362 lb / 1,525 kg (manual), 3,450 lb / 1,565 kg (automatic); approved gross vehicle weight 4,509 lb / 2,045 kg (manual), 4,597 lb / 2,085 kg (automatic); **approved front axle load 1,984 lb / 900 kg; approved rear axle load 2,668 lb / 1,210 kg**; 325xi 970 / 1,205 kg; roof 75 kg. "Approved axle loads and approved gross vehicle weight must never be exceeded." p.27: tyre pressures 32/38 psi (220/260 kPa) front/rear and 38/45 psi (260/310 kPa) for the 16- and 17-inch sizes, including staggered 225/45ZR17 + 245/40ZR17. p.161 (dimension drawing, image): height 55.5 in / 1,409 mm (325xi 56.3 in / 1,429 mm); "Height with roof rail 56.8 in / 1,444 mm (57.6 in / 1,464 mm)"; track 1,471 / 1,483 mm; wheelbase 2,725 mm. The index has no trailer-towing entry. [manual](https://manualsnet.com/bmw/325i-sports-wagon-3-series-2004); pages: [p.162](https://manualsnet.com/pdf-content/0945ee845d7bf99b78315dcf/html/162.page.html), [p.27](https://manualsnet.com/pdf-content/0945ee845d7bf99b78315dcf/html/27.page.html), [p.161](https://manualsnet.com/pdf-content/0945ee845d7bf99b78315dcf/html/161.page.html)
- **2003 M3 coupe**, part no. 01 41 0 156 842, © 09/02, p.146 [read]: curb weight 3,415 lb / 1,549 kg; approved GVW 4,453 lb / 2,020 kg; **approved front axle load 2,138 lb / 970 kg; rear 2,535 lb / 1,150 kg**. p.145: height 54.0 in / 1,372 mm, track 1,508 / 1,525 mm, wheelbase 2,731 mm. [manual](https://manualsnet.com/bmw/m3-coupe-3-series-2003), [p.146](https://manualsnet.com/pdf-content/1dd38ae4fde1bb1b66502638/html/146.page.html), [p.145](https://manualsnet.com/pdf-content/1dd38ae4fde1bb1b66502638/html/145.page.html)
- **2003 M3 convertible**, part no. 01 41 0 156 854, © 09/02, p.152 [read]: curb weight 3,782 lb / 1,715 kg; approved GVW 4,630 lb / 2,100 kg; **approved front axle load 2,183 lb / 990 kg; rear 2,579 lb / 1,170 kg**. [manual](https://manualsnet.com/bmw/m3-convertible-3-series-2003), [p.152](https://manualsnet.com/pdf-content/39629294e87697522874e8d1/html/152.page.html)
- **2006 325xi Sports Wagon** (AWD; for context only), part no. 01 41 0 159 808, © 09/05, p.212 [read]: approved front axle load 1,040 kg, rear 1,200 kg, GVWR 2,195 kg (manual), load 500 kg. [printed p.212 (HTML page 213)](https://manualsnet.com/pdf-content/a76ae40d5f6cbb83e2fcb66d/html/213.page.html)

**BMW training manuals and other BMW data:**

- **BMW ST041 "M3 Complete Vehicle"** (E46 M3, 01/2001) [read, archive.org OCR text]: "Curb Weight, DIN 1495 kg"; "Gross Vehicle Weight Rating 2000 kg"; "Permissible Front Axle Load 970 kg"; "Permissible Rear Axle Load 1140 kg"; roof 75 kg; "vehicle heights: 1372 mm Unloaded, 1363 mm loaded position". [ST041 part 1](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf)
- **BMW AG M3 data table** reproduced at the end of the Flow compilation [read]: "Weight, unladen, to DIN" 1,570 kg coupe, 1,655 kg convertible, 1,385 kg CSL; "Max perm weight, overall" 2,000 kg; "Max perm trailer load" "-" for all three (no towing approval). The 1,570 kg is 1,495 kg DIN + 75 kg, i.e. the EU kerb-weight convention (our reading). [Flow PDF](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing)
- **BMW ST034 "E46 Models", Sport Wagon module** (E46/3, production 1/00) [read, OCR]: "Up to the 'B' pillars, the Sport wagon is identical to the E46 sedan"; "The E46 Sport Wagon is 7 mm longer that the sedan and the unloaded height is 6 mm lower. The wheel base, width and turning radius are the same as the E46 sedan"; maximum loads "540KG in the rear", "75 KG on the roof". [ST034 part 1](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/1%20models.pdf)
- **BMW's normal loading for ride height and alignment** — BMW ST056 "Suspension Systems and Alignment Procedures" (US training, 1-20-03) [read, OCR]: "In order to obtain the correct ride height, the vehicle must be loaded with the specified weight. The normal specified weight for most vehicles is as follows: 68 kg. in each front passenger seat; 68 kg in the rear seat; 21 kg in the trunk; Fuel tank full. Not all vehicle need to be weighed down. Usually E39 M5 and E36/E46 M3 are measured without any weight. Always check TIS under Technical Data Group 32 … 'Normal Position/Inspection Conditions'." Fuel compensation: "approximately 7 pounds (about 3.2 kg) per gallon", added in the trunk. [ST056 01](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/01%20Suspension%20Systems%20and%20Alignment%20Procedures%201-20-03.pdf)
- **BMW ST503 "Wheel Alignment Procedures"** (initial print 3/06) [read, OCR]: same load list, plus: "In Technical Data, there are two terms used to describe the position of the vehicle during alignment … The Normal Position refers to a vehicle without any weight added. The Design Position is a vehicle with the specified weight already added. Not all vehicle need to be weighed down. Usually, Motorsport vehicles are measured without any weight." [ST503 03](https://archive.org/download/BMWTechnicalTrainingDocuments/ST503%20Undercar%20Technology/03_Wheel%20Alignment%20Procedures.pdf)
- **ADAC catalogue, BMW 325i Touring Automatic (08/00–08/01, European)** [read]: manufacturer data "Leergewicht (EU) 1580 kg", "Zul. Gesamtgewicht 2030 kg", "Zuladung 450 kg", "Anhängelast gebremst 12% 1600 kg", unbraked 720 kg, nose weight 75 kg, roof 75 kg, height 1,409 mm. European car; towing figures do not apply to US cars, which have no towing data in the manual. [ADAC](https://www.adac.de/rund-ums-fahrzeug/autokatalog/marken-modelle/bmw/3er-reihe/e46/253237)
- **Forum, 330i Touring (Germany, 2001)** [snippet]: papers show 1,140 kg rear axle, 1,250 kg when towing. [bmw-syndikat](https://www.bmw-syndikat.de/bmwsyndikatforum/topic258322_Welches_Sportfahrwerk_bei_1250kg_Achslast____3er_BMW_-_E46.html&whichpage=0)

### Inferences

- **Axle loads in kg** (our arithmetic from BMW USA curb weight × distribution; 1 lb = 0.4536 kg):

  | Car (US curb weight, manual) | Total | Front axle | Rear axle |
  |---|---|---|---|
  | 2003 325i Touring | 1,525 kg (3,362 lb) | 727 kg (1,604 lb) | 798 kg (1,758 lb) |
  | 2003 325i Touring, automatic | 1,565 kg | 757 kg | 807 kg |
  | 2003 325i sedan | 1,460 kg | 734 kg | 726 kg |
  | 2003 330i sedan / 330Ci coupe | 1,490 kg | 747 kg | 744 kg |
  | 2003 330Ci convertible | 1,640 kg | 799 kg | 841 kg |
  | M3 coupe (2002–06) | 1,549 kg (3,415 lb) | 779 kg (1,718 lb) | 770 kg (1,697 lb) |
  | M3 convertible (2002–06) | 1,715 kg (3,781 lb) | 856 kg (1,887 lb) | 859 kg (1,894 lb) |

- **S54 Touring estimate.** Take the 325i Touring and add the "M3 package" difference measured on the closest pair of bodies BMW USA lists, M3 coupe minus 330Ci coupe (+32.6 kg front, +26.3 kg rear). That package covers the S54 and 420G, M3 axles, brakes, 18-inch wheels, exhaust and M3 body panels.
  - **Lower bound** (assumes the 325i's drivetrain weighs the same as the 330's): **760 kg front, 824 kg rear, 1,584 kg (3,492 lb), 48.0/52.0.**
  - **Upper bound**, the more complete derivation: also add the 330's extra weight over the 325i that the M3-minus-330Ci difference doesn't cover (330i minus 325i sedan: +12.1 kg front, +17.9 kg rear). This gives **772 kg front, 842 kg rear, 1,614 kg (3,558 lb), 47.8/52.2.**
  
  Tracks and Trails' "3600lb wagon" fits the upper end once extras are added. Uncertainty is ±20–30 kg (equipment, fuel, aftermarket parts); weigh the car on corner scales if you can.
- **Front:** 0.975–0.991 × an M3 coupe's front axle load. **Rear:** 1.07–1.09 × an M3 coupe's, and 0.96–0.98 × an M3 convertible's.
- **BMW design (normal) load added to the S54 Touring.** With 68 kg on each front seat, 68 kg on the rear seat and 21 kg in the cargo area, and our assumed positions (front seats 1.25 m and rear seat 2.15 m behind the front axle, cargo 3.2 m; wheelbase 2.725 m), the load adds about **+84 kg front and +141 kg rear**: about **844–856 kg front and 965–982 kg rear** at BMW's design load (stock Touring about 812 / 938 kg). Positions are our assumption.
- **Margins against the Touring's ratings:** front 900 − (760…772) = 128–140 kg at curb, about 44–56 kg at design load; rear 1,210 − (824…842) = 368–386 kg; payload 2,045 − (1,584…1,614) = **431–461 kg, against 520 kg stock**.
- The 2002–06 M3 sheets all print 3,415 lb; the US curb weight includes a full tank (US convention). DIN (1,495 kg) excludes the driver and assumes 90% fuel; EU kerb (1,570 kg) adds 75 kg. Don't mix them: the guide's "3,362 lb against 1,495 kg (3,296 lb)" compares US curb with DIN.

### Gaps

- The 2003 325i Sport Wagon owner's manual itself (I read the 2004 one; the curb weight matches the 2003 spec sheet, so the axle ratings are very likely the same; check your door-pillar label).
- Measured corner weights of any finished S54 Touring: none published.
- The E46 TIS "Normal position / inspection conditions" page itself (32 00) for the Touring and the M3: not read (newTIS blocked). The loads above come from BMW's training manuals, which cover all BMWs of the period including the E46.

---

## Q2. Springs: part numbers, identification, rates, fit

### Cited findings

- **ETK gives no fixed spring numbers for any of these cars** [read]: the "Front coil spring" and "Barrel spring rear" pages for the US 325i Touring, 325i sedan, M3 coupe and M3 convertible all say "For front [rear] coil spring application refer To spring table", and list no parts. [ETK Touring front](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/front_coil_spring/), [ETK Touring rear](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/rear_axle/barrel_spring_rear/), [M3 coupe front](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/front_coil_spring/), [M3 convertible rear](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/rear_axle/barrel_spring_rear/)
- **How the spring table works** — FCP Euro (vendor, 2014) [read]: "they calculate the exact weight distribution of a particular car using all of its specific options down to even navigation systems and xenon headlamps. This info is then automatically combined with the suspension type of the car to determine the appropriate part numbers … BMW … call[s] a Spring Table"; it is looked up by chassis number in BMW's online ETK. [FCP Euro](https://www.fcpeuro.com/blog/repair-resource-bmw-coil-spring-parts-lookup)
- **Identifying the suspension variant on an E46** — BMW ST056 [read]: "E46 – There is a symbol (or code) located on the front strut assembly. There is a chart in repair instructions to match to the symbol found." (E38: paint marks on the front springs.) [ST056 01](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics%20%28Archive%201%29/01%20Suspension%20Systems%20and%20Alignment%20Procedures%201-20-03.pdf)
- **What BMW says about M3 springs** — ST041 "4 RunningGear" (E46 M3, 01/2001) [read]: front: "The spring rate of the front springs on the E46 M3 has been increased as compared to the E46/2"; front mount: "The spring and damper are insulated from each other … Additional damping (rubber) has been inserted between the spring and damper mounting." Rear: "The coil (barrel) springs on the rear axle are progressive rate. The tuning is M3-specific." No rates are given. [ST041 Running Gear](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear.pdf)
- **Sport suspension height** — BMW ST043 "E46 Update" (2002 model year) [read]: "A new standard suspension is used for all E46 models … Redesign of spring/damper tuning (E46/2/4) and additional sport chassis and suspension tuning with lowering of the vehicle by approximately 15mm"; also "harder front and rear axle carrier mounts". BMW USA's 2003 sheet lists "sport suspension calibration" with the Sport Package. [ST043](https://archive.org/download/BMWTechnicalTrainingDocuments/ST043%202002%20System%20Diagnosis/8%20E46%20Update.pdf)
- **Spring seats and pads are common** [read, ETK]:
  - Front lower spring pad 31331096664: Touring, sedan, M3 coupe, M3 convertible.
  - Front upper: the Touring and sedan use "Upper spring pocket with spacer" 31326769667 + "Spring pad upper" 31331091867; both M3s use "Upper spring pocket w/axial cage bearing" 31331090612 + "Spring pad upper" 31331091233 + "Support" 31321139423, inside the M3's own top mount 31332229165/166.
  - Rear: "Spring pad lower" 33531094518 and "Spring pad 5MM" 33531136385 on the US Touring, US sedan, M3 coupe and M3 convertible.
  - The lower control arm that carries the rear spring, "Wishbone, lower" 33326770813, is the same part on all four.
  - European rough-road cars (S815A, to 09/2001) instead take "Spring pad upper 14,5MM" 33531094754 with "Adapter" 33531091598 and a different auxiliary damper (330d/330i Touring, 330d sedan, 330Ci coupe and convertible pages).
  
  [Touring rear](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/rear_axle/rear_spring_strut_mounting_parts/), [M3 coupe rear](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/rear_axle/rear_spring_strut_mounting_parts/), [Touring arm](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/rear_axle/rear_axle_support_wheel_suspension/), [M3 arm](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/rear_axle/rear_axle_support_wheel_suspension/), [EU 330d Touring rear](https://bmwfans.info/parts-catalog/E46-Touring/Europe/330d-M57/browse/rear_axle/rear_spring_strut_mounting_parts/), [Touring front](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/guide_support_spring_pad_attaching_parts/), [M3 front](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/guide_support_spring_pad_attaching_parts/)
- **No ZCP-specific suspension rows**: the US M3 coupe ETK pages for struts, dampers, bars, top mounts and bump stops carry no option conditions (only the xenon-sensor page mentions an option) [read]. Whether the spring table gives Competition cars different springs: not checked.
- **Aftermarket M3 rates** (makers' data via retailers):
  - Öhlins Road & Track BMS MI30S1 for the E46 M3 [read, springrates.com product JSON]: "Spring Rates – Front 70 N/mm // 400 lbs/in. // 7 Kg/mm", "Rear 110 N/mm // 628 lbs/in."; target height reduction 30 mm front and rear; "approx. 0 – 30 mm lower than standard with recommended setup"; "Use with original top mounts". [springrates](https://springrates.com/products/ohlins-road-track-coilovers-2000-2006-bmw-m3-e46)
  - BC Racing BR true-rear kit I-64-BR, E46 M3 coupe [read, JSON]: 6 kg/mm front and rear, with the rear spring on the damper, so not comparable with a spring on the lower arm. [bc.springrates](https://bc.springrates.com/collections/frontpage/products/bc-racing-br-series-coilovers-true-rear-for-2000-2006-bmw-m3-coupe-rwd-e46)
  - BC Racing BR type RA I-14 (E46 M3): 6 kg/mm front, 9 kg/mm rear per Tegiwa; 6/8 kg/mm per a springrates listing [snippet].
  - KW Variant 2 15220023 (E46 M3 coupe, convertible, CSL) [read, winparts]: lowering 20–40 mm front and rear; TÜV axle loads front up to 990 kg, rear up to 1,170 kg (exactly the M3 convertible's approved axle loads). KW Variant 3 35220051 (non-M E46 including Tourings 316i–328i; not M3) [read]: front up to 910 kg, rear up to 1,215 kg; lowering 40–75 mm front, 30–60 mm rear. [KW V2 M3](https://www.winparts.co.uk/drivetrain-suspension/shock-absorbers-coil-springs/coilover-kits/c1198/kw-variant-2-screw-set/p1034959.html), [KW V3 non-M](https://www.winparts.co.uk/drivetrain-suspension/shock-absorbers-coil-springs/coilover-kits/c1198/kw-variant-3-screw-set/p1140486.html)
  - H&R Street Performance coilovers 50415 (E46 M3) [read, JSON]: front lowering 1.2–2.3 in, rear 0.75–1.5 in; progressive springs, rates not given. [springrates](https://www.springrates.com/products/h-r-street-performance-coilovers-for-2001-2006-bmw-m3-e46)
- **Not E46, for scale only**: Eibach Z4 M (E85/E86, whose rear axle shares parts with the E46 M3, e.g. rear links 33552283743) quoted on z4-forum: front progressive 23→34 N/mm, rear progressive 70→140 N/mm, "about 15% stiffer than OEM" [snippet]. Transfers only as an order of magnitude.
- **Forum, 2008** [read, saved copy]: "Rear springs and shocks different to handle additional weight and loads (See ETK)"; "Wagon is 160lbs heavier"; "H&R is only company with Touring specific lowering spring"; a later post corrects that UUC also had one; "Turner has pads for the rear springs that can raise the height"; sport bars "24/19". [e46fanatics](https://www.e46fanatics.com/threads/is-e46-touring-rear-suspension-same-as-on-the-sedan.561211/)

### Inferences

- **Front springs:** M3 coupe front springs (on M3 struts, with M3 top mounts and pads) suit the Touring. Its estimated front axle load is 1–3% below an M3 coupe's, so it should stand at about M3 coupe height, perhaps a millimetre or two higher. A convertible donor's springs were assigned for ~856 kg front (10% more), so expect the nose to sit high. With a convertible donor, order coupe springs from a dealer against a coupe VIN, or use an M3 coilover. (BMW assigns springs by weight; that the convertible's differ is inference.)
- **Rear springs:** for the same ride height and ride frequency as an M3 coupe, the rear spring needs about **7–9% more rate and preload** than the M3 coupe's. Practical routes:
  1. M3 convertible-rated rear springs (assigned for ~859 kg), checked against your measured heights.
  2. An M3 coilover kit with the rear spring uprated ~10%. For example, Öhlins' 110 N/mm rear becomes ~120 N/mm, and KW will supply alternative rates; their M3 approval tops out at 1,170 kg rear, below the Touring's 1,210 kg rating.
  3. Keep M3 coupe springs and add rear preload or height (only possible with a height-adjustable perch, or with the 14.5 mm European rough-road upper pad + adapter). This keeps the coupe's rate, so the car still sags more under load.
- **Fit:** any E46 RWD rear barrel spring sits on the same lower arm and pads, so physical fit is not the issue; rate, free length and progression are. Don't use non-M front springs on M3 struts: the M3 upper spring pocket and pad differ.
- **Rate numbers you can quote:** BMW publishes none. The best documented E46 M3 aftermarket street rates are Öhlins 70/110 N/mm and BC Racing 6/9 kg/mm (59/88 N/mm).

### Gaps

- The spring-table part numbers and paint codes for this Touring and for both M3s. They need a VIN lookup in BMW's ETK (login) or a dealer; RealOEM was blocked. Ask the dealer for both VINs' front and rear spring numbers, and photograph the paint marks on the donor's springs and the symbol on its front struts before teardown.
- OEM spring rates: not published by BMW; no measured E46 M3 or Touring rates found.
- Touring-specific spring kits for the M3 axle (H&R, Eibach, UUC): not found.

---

## Q3. Dampers, top mounts, bump stops, self-levelling

### Cited findings

- **Front struts (ETK)** [read]:
  - US 325i Touring: 31316750789/790 standard; 31312282101/102 sport suspension S226A with M Sport II S338A (from 11/2000); 31316750791/792 sport S226A or rough-road S815A. Knuckles ("king pin") 31211096429/430, 3.6 kg.
  - M3 coupe: 31312283103/104. M3 convertible: 31312282265/266. Both M3s: knuckles 31212229855/856, 4.2 kg.
  
  [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/front_spring_strut_shock_absorber/), [M3 coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/front_spring_strut_shock_absorber/), [M3 convertible](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/front_axle/front_spring_strut_shock_absorber/)
- **Front top mount**: M3 left/right guide supports 31332229165/166 (M3 coupe, convertible, CSL only) [read, ETK usage]. ST041 [read]: "The geometric layout (offset center) of the front axle mount makes it possible to increase the caster angle … A locating bolt can be removed and the upper mount bolt holes in the strut tower are slotted to allow the mount to be re-positioned for minimum camber adjustment." ST041 part 1 [read]: "The hole pattern of the front spring strut towers and rear shock absorber mounts is the same as on the standard parts." [ETK 31332229165](https://bmwfans.info/parts-catalog/31332229165/), [ST041 part 1](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf)
- **Rear dampers (ETK)** [read]:
  - US Touring: 33526750783 (standard), 33526750784 (sport S226A or rough-road S815A), 33522282099 (S226A with M Sport II, from 03/2001).
  - US sedan: 33521095913, 33526759100, 33526757045, 33521096366, 33522282461, 33522282099.
  - M3 coupe: 33522283105 (from 11/2004; old number 33522282477), 1.9 kg against 1.4 kg for 33526750783.
  - M3 convertible: 33522282267.
  - Usage: 33526750783 is listed for every European E46 Touring, the US 323i/325i Touring (incl. M56) and the non-M convertibles 320Ci/325Ci/330Ci/320Cd/330Cd.
  
  [Touring rear](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/rear_axle/rear_spring_strut_mounting_parts/), [M3 convertible rear](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/rear_axle/rear_spring_strut_mounting_parts/), [ETK 33526750783](https://bmwfans.info/parts-catalog/33526750783/), [ETK 33522283105](https://bmwfans.info/parts-catalog/33522283105/), [ETK 33522282267](https://bmwfans.info/parts-catalog/33522282267/)
- **M3 rear damper construction** — ST041 [read]: "Compared to the E46/2, the diameter of the piston rod and the piston have been increased (piston 32mm, piston rod 15mm). The auxiliary cushion on the rear axle shock absorber is new. It differs from the standard auxiliary cushion by an additional groove and the black coloring."
- **Rear top mounts (ETK usage)** [read]:
  - 33521092362: every non-M E46 sedan, coupe, Touring and compact (and the E36).
  - 33526779670: every non-M E46 convertible, the E46 M3 coupe, convertible and CSL, and the E85/E86 Z4 including the Z4 M.
  - Both are fixed by four M8 self-locking collar nuts 07119905374 (two per side). Damper rod nut 33526773882 (M10×1), plates 33526762325/33526788999, washer-gasket 33526772864 and lower bolt 07119900402 (M12×1.5×60) are common. The Touring and sedan also list a shim 33526779398 (10×16) that the M3 page doesn't. The non-M convertible pairs the Touring's own dampers with the M3's top mount.
  
  [ETK 33526779670](https://bmwfans.info/parts-catalog/33526779670/), [ETK 33521092362](https://bmwfans.info/parts-catalog/33521092362/), [EU 330Ci convertible rear](https://bmwfans.info/parts-catalog/E46-Cabrio/Europe/330Ci-M54/browse/rear_axle/rear_spring_strut_mounting_parts/)
- **Bump stops** [read, ETK]: rear: M3 33532229777 (both M3s); Touring "repair kit, additional damper guard tube" 33502290317 (Value Line). Front: M3 31332229778; Touring sport 31336778544 (S226A or S338A); Touring standard in kit 31302290314.
- **Torques** (Flow compilation of RealOEM pages, M3) [read]: rear top-mount nuts 28 Nm, "Always replace"; rod nut 14 Nm, "Always replace"; lower bolt 100 Nm, "Car must be in loaded position". Front top mount 24 Nm; rod nut 64 Nm, replace. [Flow p.17 and p.3](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing)
- **Self-levelling** [read]:
  - ETK rear-axle group lists for the US 325i Touring and the European 330d and 330i Touring contain no level-control or air-spring group.
  - BMW's ST056 "Level Control Systems" (1-13-03) lists level control on the E34 Touring, E39 Touring and E53 only: "Air Suspension systems were first introduced on the 1999 E39 Sportwagon."
  - A 2008 forum post: "E46 tourings don't have that" [read, saved copy].
  
  [ETK EU 330d Touring rear axle](https://bmwfans.info/parts-catalog/E46-Touring/Europe/330d-M57/browse/rear_axle/), [ST056 05a](https://archive.org/download/BMWTechnicalTrainingDocuments/ST056%20Chassis%20Dynamics/05a_Level%20Control%20Systems%201-13-03.pdf)
- **Build evidence** [read, captions]: Tenza moved the M3's springs and dampers into the wagon; it "just isn't gonna cut it … the wagon is heavier in different places than the M3 … we can't adjust the ride height … just a little bit too low for those wider tires in the back … barely rubbing on the fender, especially the rear bumper" ([Tenza (2022), 00:40](https://www.youtube.com/watch?v=Sit-SmfU-9k&t=40s), [01:20](https://www.youtube.com/watch?v=Sit-SmfU-9k&t=80s)). Its ECS coilovers had camber plates in front, with the rear "still the strut and the spring separate" ([01:40](https://www.youtube.com/watch?v=Sit-SmfU-9k&t=100s)).

### Inferences

- **Use M3 rear dampers with the M3 trailing arms**, with the M3 top mount 33526779670 and new M8 nuts at 28 Nm. The rear damper top position is common to E46 sedan, coupe and Touring (they share M Sport damper 33522282099). BMW says the M3 mount hole pattern is standard. The M3 mount already runs on non-M convertibles. So the M3 damper with its M3 mount bolts into the Touring as it does into a coupe. The Touring's own mount 33521092362 would very likely also fit the M3 damper (same nut, rod thread and plates), but use the M3 part.
- **Which M3 damper:** the convertible's 33522282267 is the M3 damper built for the heavier rear (859 kg), closest to the S54 Touring's 824–842 kg; the coupe's 33522283105 is built for 770 kg (our inference; BMW gives no valving data).
- **The Touring's own non-M rear dampers** (33526750783/784) are made for the non-M trailing arm; whether their length and stroke suit the M3 arm wasn't verified. Don't plan on them.
- **Rear damper top-mount torque for the Touring:** the nut part (07119905374) is the same on the Touring and the M3 diagrams, so 28 Nm very likely applies to both. Confirm in TIS 33 52.
- Tenza's car kept standard rear arches, so part of its rubbing was the M3 wheel in a non-M arch. On a car with grafted M3 arches, M3 coupe springs would rub less but still stand the rear low and reduce bump travel under load.

### Gaps

- Damper extended/compressed lengths for 33526750783, 33522283105 and 33522282267 (Bilstein/Sachs catalogue data): not obtained (search budget exhausted).
- Which damper or coilover part numbers Tracks and Trails, Tenza (ECS) and the BaT car used at the rear.

---

## Q4. Ride height: BMW's specification and method, and Massachusetts

### Cited findings

- **BMW method** — ST056 (1-20-03) [read]: "When performing alignments on BMW vehicle, the ride height must be set and checked before proceeding with any measurement or adjustments. Ride height is measured from the lower edge of the wheel rim to the lower edge of the wheel housing. Ride height specifications are in millimeters … The front axle ride height is in Group 31 and the rear axle ride height is in Group 33 … depend upon rim size (15", 16", 17" etc.), engine size and the type of suspension": Series, Low-Slung Sports Suspension, Rough Road (not US) and M Sports Package. "Use a metric tape measure with divisions of 1 mm." Procedure: install the specified weight → compensate sensors → "Lower Vehicle and Jounce" → check ride height. ST503 (3/06) repeats this [read].
- **BMW's tolerance format, E38 and E39 examples** (not E46; the format transfers, the numbers don't):
  - [read] TIS "33 00 General – Ride Level Height E38" (issue 10/2001): "Ride level in normal position (attach tape measure to rim flange at bottom middle and measure to lower edge of wheel arch)"; "Deviation from nominal value for all wheels together max. mm 10"; Series 16"/17"/18" rims 569/584/597 mm ± 10; rough road without level control 589/604/617 mm. [princeton.edu](https://www.princeton.edu/~sdepasqu/bmw/RideHeight/RideLevelHeightE38.pdf)
  - [read] ST056's E39 540i front example: Series 15"–18" rims 579/592/607/620 mm ± 10; low-slung sports 559/572/587/600; rough road 599/612/627/640.
- **E46 heights BMW publishes**:
  - [read] 2004 325i Sports Wagon manual: height 55.5 in / 1,409 mm; with roof rail 56.8 in / 1,444 mm (325xi 1,429 / 1,464 mm).
  - [read] BMW USA 2003 sheet: wagon 55.5 in, sedan 55.7 in. ST034: the wagon's "unloaded height is 6 mm lower" than the sedan's.
  - [read] M3 coupe 54.0 in / 1,372 mm (manual); ST041: 1,372 mm unloaded, 1,363 mm loaded position. The 330Ci coupe is also 54.0 in (BMW USA 2003).
  - [read] ST043: sport suspension lowers the car about 15 mm (from the 2002 model year).
- **Headlight levelling** (xenon cars only) [read, ETK]: rear level-sensor parts identical on the Touring and M3 rear axles; front "angle joint" differs (Touring 37146766778, M3 31122282404). [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/rear_axle/headlight_vertical_aim_control_sensor/), [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/rear_axle/headlight_vertical_aim_control_sensor/)
- **Massachusetts** [read, by the earlier round]: c. 90 §7P bars raising or lowering "by more than two inches above or below the original manufacturer's specified height"; 540 CMR 4.04(13) rejects such cars; no measuring method is published for cars (540 CMR 6.03's sill method applies to 4WD vehicles only). [c. 90 §7P](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter90/Section7P)
- **Trade press** (Brake & Front End / Underhood Service E46 alignment articles) [snippet; site blocked]: ride height "within ±2mm", "measured from the wheel-well lip to the bottom of the rim"; "camber can be adjusted ±0.5º by moving the upper strut mount in slots cut in the strut tower".
- **Forum, Germany** [snippet]: on alignment rigs used by the poster, E46 setpoints are "calculated dynamically" from the ride height entered.

### Inferences

- **Rim size changes BMW's number.** BMW's figure runs from the rim's lower edge, so it rises by about the rim radius change (≈12.7 mm per inch of rim diameter; BMW's E38/E39 tables step 13–15 mm per inch) with no change in body height. A 16-inch Phase 0 reading and an 18-inch Phase 12 reading aren't comparable. Record **hub-centre-to-arch-edge** as well, which is independent of rim size.
- **Tyres raise the car.** Unloaded radii: 205/55R16 316 mm, 225/45R17 317 mm, 225/45R18 330 mm, 255/40R18 331 mm, 225/40R19 331 mm, 255/35R19 331 mm. The M3 tyres lift the body about **14 mm** at the same suspension position.
- **The M3 suspension sits lower relative to the hub.** The M3 coupe and 330Ci coupe are both 54.0 in tall on tyres ~12–14 mm larger in radius, so the M3's wheel-centre-to-body height is ~12–14 mm less than a standard E46's (±3 mm; BMW rounds to 0.1 in).
- **Net:** an S54 Touring set to M3-like hub-to-body heights stands within about ±10 mm of a stock standard-suspension Touring's roof height. A Touring that left the factory with sport suspension (−15 mm) would end up ~15 mm higher than its own baseline. Either is comfortably inside 2 in (50.8 mm). The risks are heavy coilover lowering (non-M kits go 40–75 mm down; M3 kits 20–40 mm), rear sag from under-sprung rear springs, or a baseline taken on sagging old springs.
- **What to measure for Massachusetts:** the rear arch lips are replaced and the front fenders change, so arch-lip-to-ground before and after doesn't compare like with like. Record roof height (BMW publishes it), the four jacking-point heights and hub-to-arch at Phase 0, and compare the roof and jacking points at the end.
- **When to measure:** BMW measures M3s unladen; the Touring's "normal position" uses the 68/68/68/21 kg load. Record the car unladen with a full tank (comparable with the M3 donor and with BMW's published heights); optionally also at BMW's load, so the baseline matches whichever condition a shop's database uses.

### Gaps

- The E46 TIS ride-height tables (groups 31 00 and 33 00) for the Touring (series and sport, by rim size) and the M3. Not found. A BMW-equipped alignment shop's database or printout usually shows them; ask for that page in Phase 0.
- Measured ride heights of any S54 Touring on named springs or coilovers.

---

## Q5. What documented builds used, and how they drove

### Cited findings

| Build | Suspension | Result or comment | Source |
|---|---|---|---|
| BMW M prototype (2000) | not stated | — | — |
| Petroyle (UK, 2026) | evo: "Mechanically this car is very much stock", with the RACP strengthened and "additional bracing"; carbon wings, sills, rear bumper and boot floor keep kerb weight close to an M3 coupe's (PistonHeads: "1,570kg"); rides on 18-inch wheels | Hagerty: "such an easy car to drive, but with such wonderful natural balance … as soon as you get on the throttle, just drive it through with the rear"; "riding on 18 inch wheels, which is … always the best choice dynamically"; steering "quite slow". evo: "the balance feels spot-on" | [evo](https://www.evo.co.uk/bmw/m3/208970/bmw-m3-touring-e46-review-driving-the-perfect-super-estate-that-never-was) [read, saved copy]; [PistonHeads](https://www.pistonheads.com/news/ph-germancars/finally-an-e46-m3-touring-you-can-actually-buy/51036) [read, saved copy]; [Hagerty (2026), 12:40](https://www.youtube.com/watch?v=--YbwCS4F_g&t=760s), [13:00](https://www.youtube.com/watch?v=--YbwCS4F_g&t=780s), [10:40](https://www.youtube.com/watch?v=--YbwCS4F_g&t=640s) [read, captions] |
| Tenza Motorsports (US, 2004 325i Touring, standard arches) | M3 springs and dampers first, then ECS Tuning coilovers (front camber plates; rear separate spring with height adjustment) | M3 parts sat too low and rubbed; on coilovers "a little bit low in the front with a little bit too much camber … in the back it's about right … feels so much better" | [Tenza (2022), 00:40](https://www.youtube.com/watch?v=Sit-SmfU-9k&t=40s), [01:40](https://www.youtube.com/watch?v=Sit-SmfU-9k&t=100s), [07:40](https://www.youtube.com/watch?v=Sit-SmfU-9k&t=460s) [read] |
| Tracks and Trails (Canada, 2004 325i Touring) | "Billstein struts, and Ibach springs" rear and front ("Bilstein struts and IBOK lowering springs"); new rear top mounts; solid subframe bushes, spherical bushes; no rear bar at first ("laughably bad") | Rear bushed joints torqued by jacking the axle until the body lifted | [rear end (2025), 00:20](https://www.youtube.com/watch?v=eMJLXbvzckE&t=20s), [22:20](https://www.youtube.com/watch?v=eMJLXbvzckE&t=1340s), [39:20](https://www.youtube.com/watch?v=eMJLXbvzckE&t=2360s), [43:00](https://www.youtube.com/watch?v=eMJLXbvzckE&t=2580s); [first drive (2026), 12:20](https://www.youtube.com/watch?v=pvR3ovRfQHg&t=740s) [read] |
| Autoalex/Redish (UK, 330i Touring) | BC Racing coilovers, Powerflex bushes | "It's not a stance car. It's not slammed … It sits right. It sits OEM"; "the balance, the handling, the grip" | [Finale (2025), 04:20](https://www.youtube.com/watch?v=N8pdzFoVu9k&t=260s), [12:00](https://www.youtube.com/watch?v=N8pdzFoVu9k&t=720s), [13:20](https://www.youtube.com/watch?v=N8pdzFoVu9k&t=800s) [read] |
| Sloan Motor Cars (2004 325i Touring) | KW coilovers; OEM 19-inch ZCP wheels | — | [BMWBlog](https://www.bmwblog.com/2024/11/11/custom-e46-m3-touring-wagon-s54-build/) [read, saved copy] |
| BaT car (2001 325xi made RWD) | Bilstein PSS10 coilovers, H&R anti-roll bars, polyurethane bushings, camber plates, carbon front strut brace | — | [Motor1](https://www.motor1.com/news/730222/bmw-e46-m3-wagon-for-sale/) [read, saved copy] |
| Baca (2004 325xi, AWD) | KW V1 coilovers; all bushings; TMS plates; custom rear subframe with reinforced bar mounts; UUC rear bar; custom drop links (Road Race Technologies) | RRT "provided an alignment to aggressive street specs" (no numbers) | [BimmerLife](https://bimmerlife.com/2022/07/04/a-perfect-one-car-solution-the-e46-m3-touring/), [Built for Backroads](https://www.builtforbackroads.com/listing/2004-bmw-325xit-touring-awd-s54-swap) [read, saved copies] |
| Renner (US, filmed by Larry Chen) | "KW … V3"; new arms, links and anti-roll bars | Builder: on the Touring "the towers are the same, the rails are the same" | [Larry Chen (2025), 08:40](https://www.youtube.com/watch?v=YM2gyQOaJCk&t=520s), [20:20](https://www.youtube.com/watch?v=YM2gyQOaJCk&t=1220s) [read] |
| San Diego car | Ground Control coilovers with camber plates; SPC rear camber arms | — | [Bimmer INVASION (2023), 16:20](https://www.youtube.com/watch?v=GfxQDkaxeN8&t=980s) [read] |
| Project BMW (325i Touring, S54) | Captions: "I put some diamond springs on with konys" (probably Dinan springs with Koni dampers) | "basically built how BMW would have done it" | [Project BMW (2021), 04:00](https://www.youtube.com/watch?v=8ItILfnYuuY&t=240s) [read] |
| ThaChileanDude (Touring on air suspension) | Air suspension removed for coilovers; tried M3 front knuckles, then fitted 330Ci ZHP front knuckles for wheel fitment ("non-M front suspension with the M suspension in the rear") | Not this guide's route | [10 days (2024), 01:00](https://www.youtube.com/watch?v=iSgClonTiQg&t=60s), [22:20](https://www.youtube.com/watch?v=iSgClonTiQg&t=1340s) [read] |
| 2008 Touring owner (non-M, 325iT sport) | Bilstein PSS coilovers, which Bilstein lists for both sedan and wagon | "comfy, well controlled and no bouncing … body roll is drastically reduced"; at near-maximum drop, ~3 in ground clearance at the front jack point | [e46fanatics](https://www.e46fanatics.com/threads/is-e46-touring-rear-suspension-same-as-on-the-sedan.561211/) [read, saved copy] |

**Load carrying and towing:**

- BMW gives the M3 no trailer load ("-", BMW AG data) [read].
- Autoalex/Redish: the M3's dry-carbon rear bumper carrier "we cannot tie into … certainly not Towing", and the silencer and diffuser sit where a hitch goes ([Autoalex v2 (2024), 11:20](https://www.youtube.com/watch?v=vAHWkcGu8ek&t=680s)) [read].
- The US 2004 Sports Wagon manual has no trailer-towing section [read]; European 325i Tourings were rated 1,600 kg braked (ADAC) [read].

### Inferences

- No build reports rear sag under load, rubbing with M3 arches fitted, or measured heights; most owners went straight to M3-fitment coilovers.
- Petroyle's "very much stock" mechanicals plus carbon panels show one way to keep stock M3 springs working: keep the weight near a coupe's. A steel-panel home build adds ~60–90 kg over a coupe, mostly at the rear (our estimate).
- Towing: treat the converted car as not for towing (M3 bumper carrier, no US rating, approval gone with the M3 rear).
- **Load carrying:** the car keeps the Touring's ratings (Q1). Coilover approvals (KW M3: 1,170 kg rear) are below the Touring's 1,210 kg rear rating. Use full-load tyre pressures and check bump-stop clearance when the car is loaded.

### Gaps

- What springs the BMW prototype ran; spring rates or part numbers on any S54 Touring; any loaded-ride-height report.

---

## Q6. Alignment and anti-roll bars

### Cited findings

- **BMW TIS "32 00 Wheel alignment E46 / M3"**, issue 01/2005, printed 18.04.2008, reproduced in the Flow compilation [read]: "Observe test conditions".
  - Front: total toe 0°16' ± 7'; camber −1° ± 20' (left/right difference max 30'); "Track differential angle with 20° lock on inside wheel" −1°32' ± 30'; caster 7°25' ± 30' at ±10° lock and 7°40' ± 30' at ±20° (left/right difference max 30'); "Front wheel displacement" (set-back) 0° ± 10'; maximum lock approx. 40.90° inside, 33.81° outside.
  - Rear: total toe 0°22' ± 6'; camber −1°45' ± 15' (left/right difference max 15'); "Geometrical axis deviation" 0° ± 4'.
  - The same compilation has **"32 00 Wheel Alignment E46 / M3 CSL"**, issue 02/2004: front toe 0°4' ± 7', camber −1°45' ± 20', toe-out on turns −1°40' ± 30', caster 7°34' / 7°48' ± 30', lock 40.85° / 33.65°; rear toe 0°4' ± 6', camber −1°50' ± 15'. CSL has its own springs, dampers and tyres; use it only as BMW's "sportier" reference.
  
  [Flow PDF](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing)
- **Which adjustments exist on an E46** — ST056 [read]:
  - "Front toe is adjustable on all variants. Caster is NOT adjustable."
  - "Camber is adjustable on the E46 and E85. There is a slot in the upper strut tower which will allow small Camber changes. A pin must be driven down in order to allow the Camber changes. The upper strut plate can then be moved to make a slight Camber correction of up to .5 degrees … Use Special tool # 323 140." "If the Camber adjustment cannot be achieved, check for suspension damage. Make sure the vehicle is at the proper ride height."
  - Rear: "Rear Camber is adjusted by rotating an eccentric bolt located at the outer end of the rear lower lateral link"; "Toe is adjusted by moving the forward central arm bushing mount with a special tool" (90 88 6 323 030 for E46).
- **Test conditions:** M3s "usually … measured without any weight" (ST056); "Normal Position refers to a vehicle without any weight added" (ST503). See Q1.
- **Anti-roll bars and links (ETK)** [read]:

  | Car | Front bar | Rear bar | Front links | Rear links |
  |---|---|---|---|---|
  | US 325i Touring, standard | 31351097178, 23 mm; mounts 31351097179 | 33551095758, 18 mm; mounts 33551138104 | 31356780847 | 33551094619 |
  | US 325i Touring, sport S226A or M Sport II S338A | 31351094542, 24 mm; mounts 31351094556 | 33551094545, 19 mm; mounts 33551094551 | 31356780847 | 33551094619 |
  | M3 coupe | 31352229755, 26 mm; mounts 31352229756 | 33552282181, 21.5 mm; mounts 31352229711; supports 33556780707 | 31356780847 | 33552283743 |
  | M3 convertible | 31352229485, 27 mm; mounts 31352229436 | 33552282181, 21.5 mm | 31356780847 | 33552283743 |

  Front bar supports 31351094552 are common. ST041: "The front stabilizer bar is 26 mm in diameter. The stabilizer links have been adopted from the E46/2"; rear "21.5 mm. The mounting on the rear axle carrier has been modified for the E46 M3."
  
  [Touring front](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/stabilizer_front/), [Touring rear](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/rear_axle/stabilizer_rear/), [M3 coupe front](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/stabilizer_front/), [M3 convertible front](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/front_axle/stabilizer_front/), [M3 rear](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/rear_axle/stabilizer_rear/)
- **Bar torques (Flow, RealOEM annotations)** [read]: front link nuts 65 Nm, always replace; front bracket nuts 21 Nm, "Tighten in normal position to avoid preload"; rear bar, links and brackets 22 Nm.
- **Street settings from builds:** only qualitative — RRT's "aggressive street specs" on the Baca car; Tenza's coilovers gave "a little bit too much camber" in front before adjustment.

### Inferences

- **Align to the M3 values**, not the Touring's: every geometry part is M3 (knuckles, arms, offset top mounts, trailing arms). Use BMW's M3 test condition (unladen, full tank) with the ride height checked first.
- **Street suggestion** (our recommendation, inside BMW's M3 tolerance, so the guide's pass/fail still works): front camber toward −1°10' to −1°20' using the strut-tower slot (stock mounts allow about ±0.5°); rear camber −1°45' to −2°00' at the eccentric; toes at nominal. Going beyond (CSL-like −1°45' front) needs camber plates and is outside the M3 tolerance.
- **Bars:** keep the M3's 26/21.5 mm. The convertible's 27 mm front bar is BMW's answer for a heavier M3 and is an OEM way to add understeer if the rear-heavy Touring feels loose. The non-M rear bar can't be used (it hits the M3 diff — the guide already says so). Front links are the same part on every E46, so new ones are cheap and common.

### Gaps

- BMW's TIS alignment values for the E46 Touring (series and sport), and whether its specs depend on ride height: not read.
- Numerical street settings from a documented S54 Touring.

---

## Guide-ready

### Parts table

| Item | Your Touring (reference) | M3 coupe | M3 convertible | Fit to the S54 Touring | Source |
|---|---|---|---|---|---|
| Front strut L/R | 31316750789/790 (std); 31312282101/102 (sport + M Sport II, from 11/2000); 31316750791/792 (sport or rough road) | 31312283103/104 | 31312282265/266 | M3 coupe struts (front axle load within 1–3% of a coupe's), or an M3-fitment coilover | ETK |
| Front knuckle | 31211096429/430 | 31212229855/856 | same as coupe | M3, with the struts | ETK |
| Front top mount (guide support) | non-M mount (not shown on the US page) | 31332229165 L / 31332229166 R, offset center (caster) | same | M3, side-specific; the M3 hole pattern matches standard towers | ETK; BMW ST041 |
| Front upper spring pocket, pad, support, boot | 31326769667 pocket; 31331091867 pad | 31331090612 pocket with axial bearing; 31331091233 pad; 31321139423 support; 31332229427 plate; 31331093344 boot | same | M3 set with the M3 strut | ETK |
| Front lower spring pad | 31331096664 | 31331096664 | 31331096664 | common | ETK |
| Front bump stop | 31336778544 (sport); kit 31302290314 (std) | 31332229778 | 31332229778 | M3 | ETK |
| Front spring | by VIN (spring table) | by VIN | by VIN (sized for ~856 kg front) | M3 **coupe** springs, or M3 coilover springs | ETK, FCP Euro |
| Rear damper | 33526750783 (std); 33526750784 (sport or rough road); 33522282099 (sport + M Sport II, from 03/2001) | 33522283105 (from 11/2004; old 33522282477) | 33522282267 | M3 damper (convertible's suggested for the heavier rear) or M3-fitment coilover | ETK |
| Rear top mount | 33521092362 (sedan/coupe/Touring) | 33526779670 | 33526779670 (also all non-M E46 convertibles) | 33526779670 with new M8 nuts 07119905374, 28 Nm; rod nut 33526773882, 14 Nm | ETK; Flow p.17; ST041 |
| Rear bump stop | kit 33502290317 | 33532229777 (black, extra groove) | 33532229777 | M3 | ETK; ST041 |
| Rear spring | by VIN | by VIN (~770 kg rear) | by VIN (~859 kg rear) | rated for ~825–845 kg rear axle at curb: convertible-rated, or ~7–9% stiffer than the coupe's with height to suit; any E46 RWD barrel spring fits the seats | ETK; our estimate |
| Rear spring pads | lower 33531094518; upper 5 mm 33531136385 | same | same | common. European rough-road 14.5 mm upper pad 33531094754 (+ adapter 33531091598) is an OEM height-trim option (inference) | ETK |
| Rear lower control arm (spring seat) | 33326770813 | 33326770813 | 33326770813 | common | ETK |
| Front anti-roll bar | 23 mm 31351097178 / 24 mm 31351094542 | 26 mm 31352229755; mounts 31352229756 | 27 mm 31352229485; mounts 31352229436 | M3 coupe bar (27 mm optional for more understeer) | ETK |
| Front bar links | 31356780847 | 31356780847 | 31356780847 | new, common part; nuts 33306760587, 65 Nm | ETK; Flow p.6 |
| Rear anti-roll bar | 18 mm 33551095758 / 19 mm 33551094545 | 21.5 mm 33552282181; mounts 31352229711; supports 33556780707 | same | M3 (non-M bar hits the M3 diff) | ETK |
| Rear bar links | 33551094619 | 33552283743 | 33552283743 | M3 | ETK |
| Xenon levelling (if fitted) | front angle joint 37146766778 | 31122282404 | — | M3 joint with the M3 arm; rear sensor parts common | ETK |

**M3-fitment coilover data, for choosing:**

| Kit | Rates F/R | Lowering vs M3 standard | Notes | Used on |
|---|---|---|---|---|
| Öhlins R&T BMS MI30S1 | 70 / 110 N/mm (400 / 628 lb/in) | target −30 mm F/R (0 to −30) | OEM top mounts | — |
| KW V2 15220023 | not published | 20–40 mm F/R | approved to ≤990 kg F / ≤1,170 kg R | KW (variant not stated) on Sloan; V3 on Renner |
| BC Racing BR | I-14: 6 / 9 kg/mm (snippet); I-64 true rear 6 / 6 kg/mm | adjustable | custom rates on request | Autoalex |
| Bilstein PSS10 | not found | adjustable | — | BaT car |
| H&R Street Performance 50415 | progressive, not published | 1.2–2.3 in F, 0.75–1.5 in R | — | — |

For the Touring's rear, ask for a rear spring ~10% stiffer than the kit's M3-coupe spring (our estimate).

### Set-up procedure (in order)

Torques as in the guide's appendix (Flow/Department 69/BMW SI) unless stated.

**A. Phase 0: baseline on your Touring** (unmodified, level floor, tyres at placard pressure, full tank or note the fuel and add 3.2 kg per US gallon short in the cargo area; bounce each corner and roll the car a few feet first; no occupants).

1. Decode the VIN for suspension options: S226A sport suspension, S338A M Sport II, Sport Package. Read the door-pillar label: GVWR, front and rear GAWR (expect 2,045 / 900 / 1,210 kg, 4,509 / 1,984 / 2,668 lb for a manual).
2. At each corner, record:
   - BMW's figure H: lower edge of the rim flange directly below the hub centre, up to the lower edge of the wheel arch directly above it, 1 mm tape;
   - hub centre to arch edge, h;
   - ground to the jacking point.
3. Record roof height at a marked point (or roof-rail top) front and rear. BMW publishes 1,409 mm (55.5 in), or 1,444 mm (56.8 in) with rails, for a 325i Touring.
4. Optional: repeat H and h with BMW's design load (68 kg each front seat, 68 kg rear seat, 21 kg cargo).
5. Ask an alignment shop for a printout that includes BMW's ride-height specification for your car and the measured values.

**Pass:** left/right H within 10 mm, front and rear (BMW's E38 sheet uses "max. 10 mm" deviation; E46 value unverified). A bigger split means a sagging spring or a damaged part: note it so it isn't copied into the targets.

**B. Phase 1: donor targets** (same conditions, unladen M3): H, h and hub-to-body at all four corners; photograph the spring paint marks and the symbol on each front strut; note the strut and damper part numbers.

**C. Phase 3: buy** per the parts table:
- M3 coupe front struts and springs (or an M3 coilover);
- M3 rear dampers with M3 top mounts and bump stops;
- rear springs rated for ~840 kg rear axle at curb;
- M3 bars and links.

Before ordering springs, get the M3 coupe and convertible spring numbers from a dealer by VIN.

**D. Phase 6 mock-up:** set each rear hub to the donor's hub-to-body height (springs out), as the guide says. Record h at full bump.

**E. Phase 7 rear axle:**
- M3 dampers on M3 top mounts: four new M8 collar nuts at 28 Nm; new rod nut at 14 Nm.
- Springs on the 5 mm upper pad and the lower pad.
- Bump stops and protection tubes on the damper rods.
- Leave the bushed joints snug.

**F. Bushed joints at ride height** (rear: trailing-arm through-bolt 110 Nm, control arms at the subframe 77 Nm, damper lower bolt 100 Nm, bar brackets and links 22 Nm; front: control-arm bracket bolts 59 Nm, bar brackets 21 Nm). Torque with the suspension at the target height, measured as h at each corner. Either:
- the car is complete on its wheels, unladen with a full tank; or
- before the engine is in, jack each hub until h equals the target (the Phase 6 method), not "until the body lifts".

An engineless car is lighter than the finished one, so its springs would hold the body higher than final.

**Pass:** h within ±5 mm of target at each corner when tightened.

**G. Phase 8 front:**
- M3 struts complete with M3 top mounts (left and right are different parts), new M8 nuts at 24 Nm, rod nut at 64 Nm (new).
- Leave the camber locating pin in place for now.

**H. Phase 12: settle and measure**: drive 5–10 miles, then measure as in A (unladen, full tank).

**Pass:**
- h within ±10 mm of the donor M3's (or your chosen) target, front and rear;
- left/right within 10 mm;
- the tyre clears the arch lip and inner arch at full steering lock both ways.

**Fail:** springs too soft or too stiff for the axle load (rear especially); adjust the perches, change springs, or trim the rear with the pad.

**I. Massachusetts check** (unladen, same marked points):

**Pass:** roof height within ±50.8 mm (2 in) of 1,409 mm (or 1,444 mm with rails) and of your Phase 0 reading; the jacking points within ±50.8 mm of Phase 0. **Our target:** within ±25 mm, to leave margin for load and measuring error.

**Fail:** raise or lower the coilovers or change springs. Keep the measurements and BMW's published height in the car's file.

**J. Loaded check** (people and cargo up to, but not over, the Touring's 900 / 1,210 kg axle ratings; full-load tyre pressures):

**Pass** (our recommendation, not a BMW figure):
- static rear h at least 30 mm above the full-bump h recorded in step D;
- no tyre contact at the arches when you bounce the rear;
- headlights still in range (xenon cars level themselves).

**Fail:** stiffer or longer rear springs, or more rear preload on coilovers.

**K. Alignment** (unladen, full tank, ride height checked: BMW's M3 test condition):

| Item | BMW M3 target (TIS 32 00, 01/2005) | Our street pick |
|---|---|---|
| Front total toe | 0°16' ± 7' (0°09'–0°23') | 0°16' |
| Front camber | −1°00' ± 20' (−0°40' to −1°20'), left/right ≤ 30' | −1°10' to −1°20' (strut-tower slot, pin driven out) |
| Caster (±10° lock) | 7°25' ± 30', left/right ≤ 30' | not adjustable |
| Toe-out on turns (20°) | −1°32' ± 30' | — |
| Set-back | 0° ± 10' | — |
| Rear total toe | 0°22' ± 6' | 0°22' |
| Rear camber | −1°45' ± 15' (−1°30' to −2°00'), left/right ≤ 15' | −1°45' to −2°00' (eccentric) |
| Thrust angle | 0° ± 4' | 0° |

Adjust front toe at the tie rods; front camber only ±0.5° (slot, tool 32 3 140); rear camber at the eccentric bolt; rear toe at the trailing-arm front mount (tool 32 3 030).

**Pass:** every value inside tolerance, with before and after printouts.

**Fail:**
- caster out of range: a bent part, a mount fitted on the wrong side (they are left/right parts), or the wrong height;
- camber unreachable within the slot: check ride height and parts before reaching for camber plates.

Then calibrate the steering angle (the guide's Session 7), and aim the headlights at ride height.

**L. Tyre pressures** (BMW 2003 US M3 manuals, cold):
- up to four occupants: 33 psi (230 kPa) front, 35 psi (240 kPa) rear;
- occupants plus luggage: 41 psi (280 kPa) front, 48 psi (330 kPa) rear;
- 18- and 19-inch alike.

The Touring itself ran 32/38 and 38/45 psi on its own tyres: its heavier rear wants more pressure. Check the tyres' load index against the axle ratings with the guide's calculator.

### Diagram-ready data

**Figure 1: ride-height measuring points (one wheel, side view; same at all four corners)**

- **C:** hub (wheel) centre.
- **R:** lower edge of the rim flange directly below C. It sits about 220.7 mm below C on a 16-inch rim, 233.4 mm on a 17-inch, 246.1 mm on an 18-inch and 258.8 mm on a 19-inch (rim radius + ~17.5 mm flange; flange height is our assumption).
- **A:** lower edge of the wheel arch (wheel housing) directly above C.
- **BMW's ride height H = A − R** (vertical, 1 mm tape; front spec TIS group 31, rear group 33).
- **Hub-to-arch h = A − C**, so H = h + (C − R).
- **Ground to A = static tyre radius + h.** Unloaded tyre radius: 205/55R16 315.9 mm, 225/45R17 317.1 mm, 225/45R18 329.9 mm, 255/40R18 330.6 mm, 225/40R19 331.3 mm, 255/35R19 330.5 mm; the loaded radius is ~10–15 mm less.
- Annotate: "16 → 18-inch rim: H rises ~25 mm with no change in body height; M3 tyres lift the body ~14 mm".
- **Body points (side view of the car):** four jacking points; roof (BMW: 1,409 mm / 55.5 in; 1,444 mm / 56.8 in with rails, 325i Touring; M3 coupe 1,372 mm / 54.0 in).
- **Wheelbase:** Touring 2,725 mm; M3 2,731 mm (the M3 front arms move the wheel forward). **Track:** Touring 1,471 / 1,483 mm; M3 1,508 / 1,525 mm.

**Figure 2: loading for ride height and alignment (top view)**

- Touring and other non-M E46s: 68 kg on each front seat, 68 kg on the rear seat, 21 kg in the cargo area, fuel tank full (63 L).
- M3 (and, per this guide, the converted car): no ballast, tank full.

**Figure 3: axle loads, kg (bar chart: front and rear per car, with approved-load markers)**

| Car | Front | Rear | Total | Approved front | Approved rear | GVWR |
|---|---|---|---|---|---|---|
| 325i Touring (US, 2003, manual) | 727 | 798 | 1,525 | 900 | 1,210 | 2,045 |
| M3 coupe (US) | 779 | 770 | 1,549 | 970 | 1,150 (ST041: 1,140) | 2,020 (ST041: 2,000) |
| M3 convertible (US) | 856 | 859 | 1,715 | 990 | 1,170 | 2,100 |
| 330Ci convertible (US, reference: shares the Touring's rear dampers) | 799 | 841 | 1,640 | — | — | — |
| S54 Touring, estimate low / high | 760 / 772 | 824 / 842 | 1,584 / 1,614 | Touring's 900 | Touring's 1,210 | Touring's 2,045 |
| S54 Touring at BMW design load, estimate | 844–856 | 965–982 | ~1,809–1,839 | 900 | 1,210 | 2,045 |

The first four rows are BMW USA curb weight × distribution; approved loads come from the BMW US owner's manuals. The estimate rows are ours (design load assumes the seat and cargo positions given under Q1).

**Figure 4: tyre pressures, psi (kPa), cold**

| | Up to 4 occupants F / R | Occupants + luggage F / R |
|---|---|---|
| M3, 18-inch and 19-inch (2003 US manual) | 33 / 35 (230 / 240) | 41 / 48 (280 / 330) |
| 325i Touring, 16-inch and 17-inch (2004 US manual) | 32 / 38 (220 / 260) | 38 / 45 (260 / 310) |

---

## Guide statements this research corrects

1. **README, Suspension for Touring weight, Weight bullet:** "An E46 M3 coupe weighs 1,495 kg (about 3,296 lb) DIN … Expect the finished car to weigh more than an M3 coupe, with more of it over the rear axle".
   **Correction:** compare like with like. BMW USA's curb weights are 3,415 lb for the M3 coupe (50.3/49.7, 779/770 kg) and 3,781 lb for the convertible (856/859 kg), against 3,362 lb for the 325i Touring (727/798 kg). The stock Touring is lighter overall than an M3 coupe but heavier on the rear axle. Estimated S54 Touring: 1,584–1,614 kg (3,490–3,560 lb), about 760–772 kg front and 824–842 kg rear. Add the approved axle loads (Touring 900/1,210 kg, GVWR 2,045 kg).
   The same correction applies to the **Tires for Touring weight** paragraph ("… against 1,495 kg (about 3,296 lb) DIN for an M3 coupe") and the **Key numbers "Weight" row**.
2. **Dampers bullet:** "The M3's rear damper (33522283105) is a coupe part".
   **Correction:** add the M3 convertible's 33522282267 and the mounts. The M3 rear top mount 33526779670 is also the non-M convertible's (which runs the Touring's dampers); the Touring uses 33521092362. BMW (ST041): the M3 rear shock-mount hole pattern "is the same as on the standard parts". Use M3 dampers with the M3 mount on the M3 trailing arms.
3. **"Plan on M3 front struts or coilovers plus rear dampers and springs rated for the Touring"** (and the Parts list row "Rear springs and dampers rated for the Touring", and the Decisions row "Coilovers, or springs and dampers rated for the Touring").
   **Correction:** front: M3 coupe struts and springs (front load within 1–3% of a coupe's). Rear: M3 dampers (Touring non-M dampers are made for non-M trailing arms; fit unverified) with rear springs rated ~7–9% above an M3 coupe's, or M3-fitment coilovers with an uprated rear spring.
4. **"Flow gives 28 Nm with new nuts for the M3's top mounts …; we didn't find the Touring's, so take them from TIS"** (and Torque table: "No value found for the Touring's own top mounts"; Open question "Torques for the Touring's own rear damper top mounts").
   **Correction:** with the M3 axle you fit the M3 mount anyway (28 Nm, new nuts). ETK shows the same M8 self-locking collar nut 07119905374 on the Touring's own mount, so 28 Nm very likely applies there too (confirm in TIS 33 52).
5. **"BMW's catalog lists no self-levelling rear suspension for the US 325i Touring."**
   **Correction (extend):** no E46 Touring had it, US or European. ETK's 330d/330i Touring rear-axle groups list none, and BMW's level-control training (ST056, 2003) lists only the E34/E39 Touring and E53.
6. **"We found no E46 ride-height specification, so the target comes from the donor"** (also Phase 6 step 1, "No BMW ride-height figure was found for this car", and Measure and mock up, "We found no BMW ride-height figure").
   **Correction:** BMW's method and loading are now documented (ST056/ST503: rim lower edge to wheel-housing lower edge, front group 31, rear group 33, 68/68/68/21 kg + full tank; M3s unladen). BMW publishes the Touring's height (1,409 mm / 55.5 in; 1,444 mm / 56.8 in with rails), and sport suspension sits ~15 mm lower (ST043). The TIS numbers are still missing, so the donor remains the target for the arches.
7. **Wheel alignment appendix:** "It says 'observe test conditions', meaning BMW's normal loaded position. Forum citations of TIS for other BMWs give that as 68 kg … (unverified, not confirmed for the E46). Your Touring sits differently from an M3 coupe, so treat these as targets measured at the car's own loaded ride height."
   **Correction:** BMW's own training manuals (ST056 2003, ST503 2006) give that 68/68/68/21 kg + full-tank load for most BMWs, but say "Usually E39 M5 and E36/E46 M3 are measured without any weight". Align to the M3 values with the car unladen and full of fuel, ride height checked first. Add the adjustment limits: front camber ±0.5° via the strut-tower slot (tool 32 3 140); caster not adjustable; rear camber eccentric; rear toe tool 32 3 030.
8. **Phase 12 step 6:** "have the car aligned to BMW's E46 M3 figures at its own loaded ride height"; **Done-when row** "set at the car's loaded ride height"; **Shop briefs row** "BMW's E46 M3 values, set at the car's loaded ride height"; **Suspension section** "have the car aligned at loaded ride height to BMW's M3 figures"; and the Worksheets alignment note.
   **Correction:** "aligned to BMW's E46 M3 figures with the car unladen and the tank full (BMW's M3 test condition), after its ride height has been checked".
9. **Phase 7 step 8:** "With the body on stands, jack under the axle until the car just starts to lift off them".
   **Correction:** without the engine and gearbox the car is lighter than when finished, so "just lifting" leaves the suspension a little extended. Set each corner to the target hub-to-arch height h with the jack (the Phase 6 method) and torque there, or torque once the car is complete on its wheels.
10. **Parts list, M3 struts row:** "struts (coupe: 31312283103/104; a convertible's carry other numbers)".
    **Correction:** convertible 31312282265/266. Take the M3 top mounts 31332229165 (L) / 31332229166 (R), M3 upper spring pocket 31331090612, pad 31331091233 and bump stop 31332229778 with the struts. Prefer coupe struts and springs.
11. **Parts list, front sway bar row:** "Front sway bar and end links | Donor M3 | Fit new end links".
    **Correction:** coupe 26 mm 31352229755, convertible 27 mm 31352229485 (either fits; the convertible's adds understeer). End links 31356780847 are the same part on every E46, including your Touring.
12. **Massachusetts table, ride height:** "Record the Touring's ride height in Phase 0 and finish within 2 inches of it".
    **Correction:** say how. Record roof height (BMW: 55.5 in / 1,409 mm; 56.8 in / 1,444 mm with rails) and the four jacking-point heights unladen, full tank, placard pressures. Don't rely on arch lips, which are replaced. Note that the M3's 18-inch tyres alone lift the body ~14 mm.
13. **Massachusetts table, tyres:** "BMW never listed staggered sizes for a Touring".
    **Correction:** BMW's own MY2003 wheel/tyre list for the E46 Touring (Stand 05/03) lists staggered 17-inch (225/45ZR17 on 7½J ET41 front, 245/40ZR17 on 8½J ET50 rear) and 18-inch (225/40ZR18 on 8J ET47 front, 255/35ZR18 on 8½J ET50 rear) combinations for the 325i. BMW didn't list the M3's sizes, which is the question to put to the station. [BMW list](https://myair-bdr.bmwgroup.com/static/manual/RadReif/RadReif/00/mj2003/e46touring3_2003.htm) [read]
14. **Wheels, offsets:** "325i Sport Package wheel, 8J at an assumed ET47 (… the ET47 is unverified)".
    **Correction:** the same BMW list gives 225/45R17 on 8J × 17 IS (ET) 47 alloy wheels for the 325i Touring (and 205/55R16 on 7J × 16 alloys at ET46 or ET47, depending on the style; a style-12 7J × 16 ET47 steel wheel for winter tyres).
15. **Tires, Pressures:** "We found no BMW pressures for the M3 sizes" (and the Open question "BMW tire pressures for the 18- and 19-inch M3 sizes …").
    **Correction:** 2003 US M3 coupe and convertible manuals: 33/35 psi (230/240 kPa) up to four occupants, 41/48 psi (280/330 kPa) with occupants plus luggage, for 225/45ZR18 + 255/40ZR18 and 225/40ZR19 + 255/35ZR19.
16. **Open questions:** "An E46 ride-height specification, and BMW's 'normal loaded position' weights for the E46."
    **Correction:** loading answered (BMW training manuals). Method answered. The numeric TIS ride heights for the E46 remain open.

### Incidental findings outside this topic (for the fluids appendix)

- **S54 coolant capacity:** "Cooling system including heater circuit … approx. 9.8 [US quarts] / approx. 9.3 [liters]" (2003 US M3 coupe manual p.147 and convertible manual p.153) [read]. This closes the guide's "Capacity not found" and the open question on S54 coolant capacity.
- **420G oil:** the same US M3 manuals print "Manual transmission quarts/liters approx. 1.9/approx. 1.8". The guide's fluids table says "1.9 L (2.0 US qt)" from ST041. Flag the discrepancy and fill to the plug.
- **Differential 1.2 qt / 1.1 L and engine oil with filter 5.8 qt / 5.5 L** agree with the guide.

---

## Sources (beyond those linked inline)

- BMW wheel/tyre list, E46 M3 coupe MY2005 (Stand 11/04) [read]: [myair-bdr](https://myair-bdr.bmwgroup.com/static/manual/RadReif/RadReif/00/M-GmbH/MJ2005/e46m3_2005.htm)
- ETK part-usage pages [read]: [33526779670](https://bmwfans.info/parts-catalog/33526779670/), [33521092362](https://bmwfans.info/parts-catalog/33521092362/), [33532229777](https://bmwfans.info/parts-catalog/33532229777/), [31352229485](https://bmwfans.info/parts-catalog/31352229485/), [33552283743](https://bmwfans.info/parts-catalog/33552283743/), [31356780847](https://bmwfans.info/parts-catalog/31356780847/), [31331091233](https://bmwfans.info/parts-catalog/31331091233/)
- ETK sedan pages for comparison [read]: [US 325i sedan rear struts](https://bmwfans.info/parts-catalog/E46-Sedan/USA/325i-M54/L-N/browse/rear_axle/rear_spring_strut_mounting_parts/), [US 325i sedan front bar](https://bmwfans.info/parts-catalog/E46-Sedan/USA/325i-M54/L-N/browse/front_axle/stabilizer_front/)
- Downloads for this round are in `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/round4-dl/suspension/` (ETK HTML in `etk1/` and `etkparts/`, BMW USA sheets in `bmwusa/`, training-manual OCR in `archive/`, owner's-manual pages and extracted images in `manuals/`).
