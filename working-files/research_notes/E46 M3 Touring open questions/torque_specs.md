# S54 flywheel and rod-bolt tightening specs, and E46 M3 driveline/rear-axle torque cross-check

Research date: 22 October 2026. Each finding says how it was read: **[page]** means I read the page or file itself (HTML text, PDF text, or an image I opened), and **[snippet]** means I saw it only in a search-result summary and could not open the page. Values are in Nm; ft-lb conversions are mine (1 Nm = 0.7376 ft-lb).

How to read the sources: the strongest are BMW documents. These are SI B11 04 04 (BMW's service bulletin for the rod-bearing campaign), a NewTIS screenshot, a TIS printout, the ST041 training manual and the ETK parts catalog, plus ARP's own instruction sheets. Department 69, the "Flow" E46 M3 torque PDF and FCP Euro's blogs are compilations or vendor DIYs. NewTIS and the other full TIS mirrors were blocked (see the Gaps under the last question).

## Q1. What is the S54 dual-mass flywheel-to-crankshaft spec, and does it differ from the M54's 105 Nm?

### Takeaway
BMW TIS gives **105 Nm** for the S54 flywheel. TIS adds no angle step, says to install without thread-locking compound, and says the bolt threads should be oiled. The bolts are eight **M12×1.5×50** hex bolts (11 22 2 243 051), the same part the E46 M54 uses, and ETK marks them "Required for repair", so fit new ones. The S54 figure therefore matches the M54's 105 Nm. The guide's note that "the often-quoted 105 Nm is the M54 value" should be corrected.

### Cited Findings
- **BMW TIS (NewTIS screenshot) [page, read as image]:** A NAM3 member posted a screenshot of NewTIS › BMW E46 M3 Coupe › Repair Manuals and Technical Data › 11 Engine › 11 22 Flywheel › Tightening Torques. It shows "1AZ Flywheel to crankshaft – Manual gearbox flywheel to crankshaft", Type "S62 / M60/1 / M60/2 / M62 /S54", Torque "105 Nm". The tightening-specification column reads: "Do not install with screw locking agent. The bolts are integral components on the flywheel. Threads on bolts oiled." The thread column is blank, no angle is listed, and the screenshot is cropped below that row. Sources: [NAM3 thread "Loctite on Flywheel Bolts?", post #2 by Slideways, 08-23-2021](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/122587-loctite-on-flywheel-bolts) and [the attachment image](https://nam3forum.com/forums/filedata/fetch?id=122599&d=1629744750).
- **ETK, E46 M3 S54 "Flywheel / Twin Mass Flywheel" diagram [page]:** The twin-mass flywheel is 21 21 2 229 900, with the note "Info: Required for repair – (#4) Hex bolt 11 22 2 243 051, Quantity: 8". Item 4 is "Hex bolt 11 22 2 243 051, M12X1,5X50", qty 8. Also listed: dowel pins 11 22 1 709 069 (10×23, qty 3), dowel 11 11 1 743 118, and pilot bearing 11 21 1 720 310. [bmwfans.info ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/flywheel_twin_mass_flywheel/)
- **ETK usage of bolt 11 22 2 243 051 [page]:** It is listed for the E46 M3 S54 (coupe and convertible, US and Europe), the M3 CSL S54, the Z3 M3.2 S54 and S52, the Z4 M3.2 S54 (E85 and E86), and the E46 325i/325Ci/330i-type M54 cars. The S54 and the M54 share the same flywheel bolt. [bmwfans.info part page](https://bmwfans.info/parts-catalog/11222243051/)
- **ETK usage of DMF 21 21 2 229 900 [page]:** E46 M3 S54, M3 CSL S54, Z4 M3.2 S54 (E85/E86); Z3 M is not listed. [bmwfans.info part page](https://bmwfans.info/parts-catalog/21212229900/)
- **BimmerWorld [page]:** Describes 11222243051 as "Genuine BMW Flywheel Bolt (M12x1.5x50)", "Only for cars with manual transmission… 8 bolts required per vehicle", superseding 11221730533. Its fitment list includes the Z3 M S52 and S54 and the Z4 M; it doesn't list the E46 M3, though ETK does. [BimmerWorld](https://www.bimmerworld.com/Driveline-Shifter/Flywheels/Flywheel-Mounting-Bolt-M12x50-E39-Z3-Z3M-Z4M.html)
- **Department 69 [page]:** Lists "Flywheel bolts, M54: 105 Nm (77 ft-lb), Replace bolts" and "M43TU: 120 Nm". It has no S54 flywheel row. The M54 row links to a TIS PDF from a Z3 M Roadster document set ([rfdm.com 11_22_AZD.pdf](https://www.rfdm.com/Daniel/MRoadster/BMWDocs/TIS/pdf/11_22_AZD.pdf)), which I could not open. [Department 69](https://www.department69.com/articles/bmw-e46-torque-specs-complete-reference-all-engines)
- **"Flow" E46 M3 torque PDF (forum compilation drawn on RealOEM printouts; updated 2024) [page, p. 68]:** "105 Nm / 77 ft-lb. Do not use loctite! Thread lightly oiled. Torque in star pattern. Always replace." [Google Drive PDF linked from NAM3](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing), via [NAM3 torque-spec thread](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/414-e46-m3-torque-spec-thread-every-bolt-on-the-car-on-diagrams)
- **NAM3 forum discussion [page]:** The original poster was tightening new bolts to 77 ft-lb. He noted the bolts came with "what appears to be a yellow threadlocker" and that the torque PDF says to fit them slightly oiled without Loctite. Later replies call the yellow coating a thread sealant that "prevents oil creeping up the spiral of the thread, as the other side of the bore is exposed to the crankcase", and say "Per the spec, use only oil". This is forum opinion. [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/122587-loctite-on-flywheel-bolts)
- **Disagreeing values:**
  - FCP Euro's non-M E46 clutch DIY torques the flywheel bolts "in a crossing pattern to 100Nm" [page]. [FCP Euro](https://www.fcpeuro.com/blog/how-to-replace-the-clutch-flywheel-rear-main-seal-on-a-bmw-e46)
  - A Bimmerpost post says an attached PDF lists 65 ft-lb while "Bentley and ISTA have 120Nm (88 ft-lb)" [snippet; HTTP 403, and the car or engine isn't clear]. [Bimmerpost](https://g42.bimmerpost.com/forums/showthread.php?p=29537995)
  - MotoIQ's E46 M3 lightweight-flywheel build torqued each bolt to 85 ft-lb with Loctite [snippet; aftermarket flywheel]. [MotoIQ](https://motoiq.com/project-e46-m3-part-13-lightweight-clutch-and-flywheel-and-more/10)
  - Turner advises blue or orange Loctite on factory flywheel bolts that lack pre-applied threadlocker [snippet; exact Turner page not confirmed]. [Turner flywheels listing](https://www.turnermotorsport.com/c-1226-bmw-flywheels?N=1z141y8)
  - An e46fanatics owner reported "105 nm… according to my haynes manual, seems to be confirmed in TIS" [snippet; exact thread not confirmed, HTTP 406]. [e46fanatics](https://www.e46fanatics.com/threads/help-flywheel-install-torque-spec.774321/)

### Inferences
- For the S54 dual-mass flywheel: fit eight new M12×1.5×50 bolts (11 22 2 243 051), oil the threads lightly, add no thread locker, and torque to 105 Nm (77 ft-lb). TIS gives no angle step. The cross or star pattern comes from the compilations and FCP, not from what TIS shows.
- "Integral components on the flywheel" and ETK's "Required for repair" both point to new bolts with each flywheel fit. Read with the vendors' "single use / stretch" language, reusing old bolts is not supported.
- The 120 Nm figure seen in snippets matches Department 69's M43TU (four-cylinder) value, so it was probably mixed up with that engine. 100 Nm (FCP) is lower than TIS. Neither should be used for the S54 DMF.
- An aftermarket single-mass flywheel follows its maker's instructions, which often call for thread locker. TIS's "no screw locking agent" applies to the OEM part.
- The TIS row lists the engine type ("S54"), and the Z4 M shares both the DMF and the bolt in ETK, so 105 Nm very likely applies to the Z4 M S54 as well. I didn't read Z4 M TIS directly.

### Gaps
- I couldn't open the NewTIS page itself (Cloudflare challenge at newtis.info, and DNS failure from WebFetch), so the screenshot is the evidence. Its cropped lower part may hold further notes.
- I couldn't fetch the rfdm.com TIS PDF (the egress tunnel closed; web.archive.org was also unreachable through the proxy). The claim that Bentley or ISTA give 120 Nm is unverified.

## Q2. What exact procedure does BMW give for the S54 rod bolts (M11 early, M10 late), and what are the reuse rules?

### Takeaway
BMW's service bulletin SI B11 04 04 gives both procedures. **M11×1.25 twelve-point bolts:** reuse them in the same holes, then 5 Nm, 30 Nm, and **70° in a single stroke**. **M10×1.25 E-Torx bolts (11 24 7 834 310):** always new, tightened **three times**: 5 Nm, 30 Nm, 105° in one stroke, then back off about one turn and repeat, with the third cycle as the final one. Department 69's "+105°, done three times" is therefore correct, but its "Replace bolts" for the M11 row contradicts BMW. BMW's change-over date is **12/12–13/2002 production**, not 02/2003 as vendors and ETK say, so identify the bolts by their heads.

### Cited Findings
- **BMW SI B11 04 04, "Service Action: E46 M3 S54 Connecting Rod Bearings Replacement" (October 2004 revision; PDF hosted on NAM3) [page, PDF text].** [BMW SI via NAM3](https://nam3forum.com/forums/filedata/fetch?id=5213)
  - **Scope:** "E46 M3 coupe/convertible with S54B32 engine produced from 02/12/2001 up to 05/22/2003."
  - **Step 28, tools and reuse:** "use M12 mm, 12-point socket on vehicles with M11 x 1.25 bolts; or Torx E12 on vehicles equipped with M10 x 1.25". "On vehicles produced up to 12/13/2002, the M11 x 1.25 connecting rod bolts (A) will be reused with the new bearings. It is essential to mark them and then reinstall them in the same order (e.g. bolt from the exhaust side must be reinstalled again on the exhaust side, etc). On vehicles produced from 12/13/2002, the new design M10 x 1.25 connecting rod bolts (B) have to be replaced… (p/n 11 24 7 834 310 – 12 bolts per vehicle)."
  - **Step 36, M11 bolts:** "settling torque: 5 Nm – initial torque: 30 Nm – angle torque to 70°, in one single stroke."
  - **Step 37, M10 bolts:** "On vehicles from 12/12/2002 production, the M10 x 1.25 con rod bolts must be tighten at least three times in order to reach its maximum tensile strength. Important: Not adhering to the tightening specifications detailed below, will result in serious engine damage."
    - First tightening: 5 Nm, 30 Nm, 105° in one single stroke, "Then, release the torque by backing off conrod bolts by approximately one turn and then retighten them again."
    - Second tightening: the same, then "back off conrod bolts again by approximately one turn and finally retighten them again."
    - Third tightening: 5 Nm, 30 Nm, 105° in one single stroke.
  - **Parts table:** "11 24 7 834 310 M10 x 1.25 Conrod Bolt (vehicles from 12/12/02), 12"; warranty work packages split the cars "up to 12/13/2002" (M11) and "from 12/13/2002" (M10).
  - **Other values from the same procedure [page]:**
    - Oil-pump sprocket nut: 25 Nm, left-hand thread.
    - Front reinforcement (thrust) plate: new M10 screws, 59 Nm then 90°.
    - Steering-spindle clamp screw: new M8×33, 22 Nm.
    - Oil-pan M6 screws: 10 Nm; Hylomar at the timing cover, block and bell-housing joints.
    - Bearing shells: blue on the rod side, red on the cap side.
    - Oil: 6.5 L of 10W-60 for this job (5.5 L normal service).
    - Break-in: 1,200 miles below 5,500 rpm.
    - The bulletin also states BMW NA's 6-year/100,000-mile extended warranty on internal oil-lubricated parts for MY2001–03 S54 cars, including 2001–02 M roadster/coupe.
- **BMW ST041 S54 training module [page, archive.org text; the OCR reads "554" for S54]:** "The S54 uses reinforced forged steel 'cracked' connecting rods… The connecting rod bolts must be angle torqued (refer to Repair Instructions and Technical Data). The bolts can not be replaced separately, if damaged; the connecting rod must be replaced (supplied with new bolts)." This text predates the M10 bolt. [archive.org ST041 "2 M3 DriveLine" (text)](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine_djvu.txt), [PDF](https://ia801005.us.archive.org/11/items/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/2%20M3%20DriveLine.pdf)
- **ETK, E46 M3 "Crankshaft Connecting Rod" [page]:** The connecting-rod bolt line reads "See repair manual". Bolt 11 24 7 834 310 "Only applies to (#1) Set connecting rod 11 24 7 834 437 from Feb '03 M10X1,25". The bearing shells are blue 11 24 7 835 440 and red 11 24 7 835 439 (standard, 49.00 mm), with 0.25 mm undersize versions. [bmwfans.info ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/crankshaft_connecting_rod/). The Flow PDF's RealOEM printout of the same diagram adds "Pos. 2 – Connecting rod bolt M11 x 1,25, up to 02.03, See repair manual" [page, p. 44].
- **Department 69 [page]:** "Connecting rod bolts, S54 (M11 bolts): 5 Nm, 30 Nm, then +70°, Replace bolts". "S54 (M10 Torx bolts): 5 Nm, 30 Nm, then +105°, done three times, Replace bolts. Check which bolt type you have". Both rows cite "BMW TIS" and link to a PDF of BMW repair instruction 11 24 571 on adkusters.dsmynas.com, which I couldn't resolve. [Department 69](https://www.department69.com/articles/bmw-e46-torque-specs-complete-reference-all-engines)
- **FCP Euro kit 11410395192KT1 [page]:** "M11x1.25mm bi-hexagonal (12 point) bolts and are intended to be reused. It is required to install the bolts into the same connecting rod location… 1) Jointing torque – 5 Nm (~4 ft lbs) 2) Setting torque – 30 Nm (~15 ft lbs) 3) Angle of rotation – 70°". FCP also says BMW's service kit 11410395192 is no longer available as a kit. [FCP Euro](https://www.fcpeuro.com/products/bmw-s54-connecting-rod-bearing-kit-11410395192kt1)
- **BimmerWorld [page]:**
  - On the M11 bolt: "BMW actually does not sell the M11 rod bolt separately. Unlike most other rod bolts, the M11 is not a torque-to-yield and it can be re-used." Early kit, "up to 2/2003": [early kit](https://www.bimmerworld.com/Engine/Engine-Maintenance/Rod-Bearing-Overhaul-Kit-Basic-OEM-E46-M3-2003.html)
  - On 11247834310: "These bolts stretch when properly tightened and they cannot be re-used (also known as torque-to-yield bolts). These bolts must be replaced any time one is removed… M10 diameter with 1.25 thread pitch." It lists fitment for the E46 M3 and Z4 M: [M10 bolt](https://www.bimmerworld.com/Engine/BMW-Engine-Internals/Genuine-BMW-Connecting-Rod-Bolt-M10X1-25-11247834310-E46-M3-E85.html)
  - The late kit is "from 4/2003 production" and says cars "from 2/2003 have a M10 connecting rod bolt". [late kit](https://www.bimmerworld.com/Engine/Engine-Maintenance/Rod-Bearing-Overhaul-Kit-Basic-OEM-E46-M3-2004.html)
- **NAM3 owner summary [page, 04-08-2020]:** "M11 (reuse) for pre 12/13/2002 -> 1x (5Nm, 30Nm, 70degrees); M10 (replace) for post 12/12/2002 -> 3x (5Nm, 30Nm, 105 degrees)". [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/8128-s54-connecting-rod-bolt-torque-late-model-m10)
- **Flow PDF p. 44 [page]:** It repeats the SI: M11 "Do not replace bolt!", 5 Nm, 30 Nm, 70° in a single stroke. M10 "Replace bolts! Bolts have to be tightened 3 times", 5 + 30 Nm + 105° in a single stroke, "Release bolt one full turn", repeated, with the third cycle final.
- **Search snippets only [snippet]:**
  - e46fanatics: "Connecting rod bolts (B) must be tightened at least three times but no more than five times". This possibly quotes a later SI revision or the repair instruction. The page returned HTTP 406, even in a headless browser. [e46fanatics](https://www.e46fanatics.com/threads/s54-rod-bolt-torque.1178865/)
  - Another e46fanatics post: "Many web store's data bases supercede the M11 bolts to the M10 bolts, and THAT won't work!"
  - A vendor snippet claimed earlier engines got M10 bolts under the recall. BMW's SI contradicts this: M11 bolts were reused under the recall.

### Inferences
- **Early engines, built up to 12/13/2002, M11 bolts:** keep the original bolts, mark each bolt's rod and side, and refit each in its own hole. Tighten 5 Nm, then 30 Nm (22 ft-lb), then 70° in one continuous pull. BMW doesn't sell them separately; if one is damaged, replace the rod, which comes with new bolts.
- **Late engines, from 12/12–13/2002, M10 E-Torx bolts:** fit 12 new 11 24 7 834 310 bolts. Each bolt gets three full 5 Nm / 30 Nm / 105° cycles, backed off about one turn between cycles, and the third cycle is final.
  - Because of this, do Plastigauge clearance checks with the old bolts and use new bolts only for the final assembly.
  - Each extra tighten-and-release cycle may count against an unverified "no more than five" limit.
- **Build-date thresholds disagree:** BMW's SI says 12/12–13/2002, ETK says Feb '03, BimmerWorld says 2/2003 or "up to and including 01/2003", and the guide says 02/2003. Rods replaced after the change can carry M10 bolts on an older engine (ETK ties the M10 bolt to rod set 11 24 7 834 437). The reliable check is the bolt head, as BMW's own tool call-out implies: 12-point head (12 mm socket) means M11; E-Torx head (E12) means M10.
- **Corrections to sources:** FCP's "30 Nm (~15 ft lbs)" is a conversion error; 30 Nm ≈ 22 ft-lb. Department 69's "Replace bolts" on the M11 row is wrong per BMW.
- **Z3 M and Z4 M:** BimmerWorld lists the M10 bolt for the Z4 M and the ARP M11 kit for the Z3 M S54. The SI covers only the E46 M3. Applying the same two procedures by bolt type to the Z3 M/Z4 M S54 is an inference.

### Gaps
- I couldn't read BMW repair instruction 11 24 571 (adkusters.dsmynas.com doesn't resolve; web.archive.org was unreachable through the proxy) or a newer revision of SI B11 04 04. The "no more than five tightenings" limit is unverified.
- I didn't find the SI saying whether to oil the M10 bolts. The snippet claim "wash and oil the replacement M10 rod bolts" was not in the text I read.
- I couldn't open NewTIS 11 24 tightening torques (Cloudflare).

## Q3. What does ARP specify for its S54 rod bolts?

### Takeaway
ARP's own sheets give stretch first, with a torque fallback using ARP Ultra-Torque lube:
- **201-6103 (S54, M11):** stretch 0.0075–0.0080 in (0.19–0.20 mm), or 70 ft-lb (≈95 Nm).
- **201-6102 (sold for late M10 S54s):** stretch 0.0065–0.0070 in (0.165–0.178 mm), or 50 ft-lb (≈68 Nm).
Both sheets say the rods "should always be re-sized after new rod bolts are installed." That is a machine-shop step that in-car bearing swaps skip. ARP's 201-6102 sheet names the BMW 3.0L S50 Euro, not the S54.

### Cited Findings
- **ARP instruction sheet 201-6103, "BMW 3.2L (S54) INLINE 6-CYL" [page, PDF].** [ARP 201-6103](https://cdn.arp-bolts.com/instructions/201-6103.pdf)
  - Lubricate threads and underhead with ARP Ultra-Torque.
  - "ARP recommends using the STRETCH METHOD… Stretch the bolts to .0075 – .0080." "If you do not have a stretch gauge, torque the bolts to 70 ft-lbs using ARP Ultra-Torque Fastener Assembly Lubricant."
  - "The connecting rods should always be re-sized after new rod bolts are installed."
  - Keep a log of free lengths; replace any bolt with permanent deformation or more than .001 in growth.
- **ARP instruction sheet 201-6102, application "BMW 3.0L (S50EURO) INLINE 6-CYL" [page, PDF]:** Same wording, with stretch ".0065 – .0070" or "50 ft-lbs" with Ultra-Torque, and the same rod re-sizing note. [ARP 201-6102](https://cdn.arp-bolts.com/instructions/201-6102.pdf)
- **ARP catalog [snippet; arp-bolts.com is behind a Cloudflare challenge]:** 201-6102 is described as an "M10, 45mm UHL, ARP2000" kit with a 7/16 12-point socket for the S50 Euro. ARP's product list is said to pair 201-6102 with the 3.2L S54 in one place. [ARP kit page](https://arp-bolts.com/kit/201-6102)
- **Vendors [page]:**
  - BimmerWorld sells 201-6102 for the "later S54 (February 2003 and newer…) which used an M10 sized bolt" and notes the set "is also commonly used on Euro E36 M3 models". [BimmerWorld M10 kit](https://www.bimmerworld.com/Engine/Gaskets/ARP-Rod-Bolt-Kit-S54-02-03-M10.html)
  - BimmerWorld sells 201-6103 for M3s "up to and including 01/2003 production", plus the Z3 M S54. [BimmerWorld M11 kit](https://www.bimmerworld.com/About-Us/Free-Shipping-BMW-Parts/ARP-Rod-Bolt-Kit-S54-01-03-M11.html)
  - Hack Engineering's 201-6103 is "twelve ARP2000 rod bolts" for pre-Feb-2003 S54s (E46 M3, Z3 M) and links ARP's sheet. [Hack Engineering](https://www.hackengineering.co.uk/product/arp-con-rod-bolts-early-s54b32/)
  - R44 Performance reproduces the same stretch and torque numbers for "M11 Early" and "M10 Late". [R44](https://r44performance.com/products/bmw-s54-arp-connecting-rod-bolts)

### Inferences
- Measure ARP bolts with a stretch gauge, and treat the torque figures (70 ft-lb M11, 50 ft-lb M10) only as ARP's no-gauge fallback with ARP lube. Never use BMW's 5/30/angle procedures on ARP bolts.
- ARP's re-sizing instruction means a fully by-the-book ARP install needs the rods off the engine and sent to a machine shop. That is easy with the S54 on a stand but conflicts with the common in-car swap. Many builders skip it; that is a judgment call the guide should flag.
- Because 201-6102's sheet names the S50 Euro, check the kit against your rods (M10 thread, bolt length) before fitting it to a late S54.

### Gaps
- I couldn't open ARP's catalog pages (Cloudflare), so the UHL, material and socket size come from snippets only. I found no ARP sheet that names the S54 for the M10 kit.

## Q4. Do the guide's other S54/M3 driveline and rear-axle torque values hold up?

### Takeaway
Every value in the guide's table matches at least two independent compilations. Only the guibo value is now confirmed against a BMW TIS printout: **115 Nm for M3/M5 M12 10.9**. I couldn't read the TIS pages for the remaining values (Cloudflare), so they stay "compilation-verified". Two notes worth adding:
- The M3's ETK pressure-plate screws are **10.9 grade, micro-encapsulated**, so the 34 Nm figure applies to the M3.
- One vendor snippet gives 128 ft-lb (174 Nm) for the M14 front diff bolt, against 200 Nm in Department 69, the Flow PDF and NAM3.

### Cited Findings
- **Pressure plate:**
  - Department 69: "M8 grade 8.8: 25 Nm (18 ft-lb). M8 grade 10.9: 34 Nm (25 ft-lb)", cited to TIS [page].
  - Flow PDF p. 69: the same, plus "Always replace screws" [page].
  - ETK E46 M3 clutch: "Fillister-head screw, micro-encapsulated, M8X18-10.9-ZNS3", 21 20 7 548 052, qty 6; clutch set 21 21 2 282 667 (240 mm) [page]. [bmwfans.info ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/clutch/clutch/)
  - FCP's non-M E46 DIY: "six pressure plate bolts… to 25Nm" [page]. [FCP Euro](https://www.fcpeuro.com/blog/how-to-replace-the-clutch-flywheel-rear-main-seal-on-a-bmw-e46)
  - An e46fanatics snippet credits Bentley with "M8 (8.8 grade) = 24 Nm… M8 (10.9 grade) = 34 Nm" [snippet; exact thread not confirmed, site returns HTTP 406]. [e46fanatics clutch DIY thread](https://www.e46fanatics.com/threads/update-the-complete-diy-clutch-install-with-pics.641850/)
- **Flex disc (guibo):**
  - **BMW TIS printout "26 11 Propeller Shaft, complete", 1AZ "Universal joint to propeller shaft and transmission" [page, PDF; "BMW AG – TIS", issue status 10/2001, printed 20.05.2011]:** "M3 / M5, M12 10.9: 115 Nm"; "E32/E34/E36/E38/E39/E46/E53, M12 10.9: 100 Nm"; "M12 8.8: 81 Nm"; "M10 10.9: 64 Nm"; "M10 8.8: 48 Nm". [TIS PDF on princeton.edu](https://www.princeton.edu/~sdepasqu/bmw/Gas.Tank/AZD.Propeller.Shaft,complete.pdf)
  - ETK E46 M3 driveshaft [page]:
    - flex disc 26 11 2 226 527 (LK 96 mm/12)
    - bolts "M12X1.5X62 ZNS3", 26 11 7 635 643 (earlier 26 11 2 283 795 up to Jan '13)
    - "Self-locking hex nut M12X1,5-10-ZNS3", 26 12 7 536 563 from Dec '04 (earlier 07 12 9 900 047 PHR)
    - [bmwfans.info ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/drive_shaft/drive_shaft_cen_bearing_const_vel_joint/)
  - Department 69: "M3 with M12 10.9 bolts: 115 Nm" [page].
  - Flow PDF p. 79: 115 Nm on both sides, "Tighten the bolt / not the nut to avoid guibo preload" [page].
- **Center mount:**
  - Department 69: "Driveshaft center support bearing: 21 Nm" [page].
  - Flow PDF p. 79: 21 Nm, plus "CSB must be preloaded… (Move forward 4 – 6 mm)" [page].
  - ETK: two "Flange nut with washer M8-8-ZNS3" (26 11 7 574 872); center mount 26 12 2 282 495 [page].
- **Driveshaft to diff (M3):**
  - Department 69: "M3 M10 Torx: 70 Nm" [page].
  - FCP Euro M3 subframe part 3: "Use an E14 socket… Torque the bolts to 70Nm" [page]. [FCP part 3](https://www.fcpeuro.com/blog/how-to-overhaul-the-bmw-e46-m3-rear-subframe-part-3)
  - Flow PDF p. 79: 70 Nm, "Driveshaft is balanced – Mark before disassembly" [page].
  - ETK: six "Torx screw with ribs M10X46-ZNS3" (33 21 7 571 990) with three reinforcement plates (33 20 7 572 717) [page].
- **Half-shaft to diff output flange:**
  - FCP part 3: "use an E12 socket to torque them to 100Nm" [page].
  - Flow PDF p. 83, a RealOEM printout: "Torx screw with ribs M10X46", 33 21 1 227 664, qty 12, reinforcement plates 33 21 1 209 543; "Black: 100 Nm / 74 ft-lb <- E46 M3. Silver: 80 Nm / 59 ft-lb (always replace)"; M27×1.5 collar nut 300 Nm [page].
  - Department 69 has no half-shaft row.
- **Diff mounts:**
  - Department 69: front "All except M3 95 Nm… M3: 200 Nm"; rear "All except M3 174 Nm… M3: 20 Nm, then +90°", both cited to TIS. They link to 330i M54 TIS pages I couldn't open [page].
  - Flow PDF pp. 15 and 81 [page]:
    - front bolt "Hex bolt with washer M14X1,5X65-10.9" (33 17 7 840 535): 200 Nm, "Observe repair instructions!"
    - rear bolts "Torx bolt M12X50-8.8-ZNS3" (23 00 1 222 891, ×2, with A13 washers): "20 Nm joint torque + 90 degree angle (some use loctite)"
  - NAM3, 05-01-2020: "Torque front bolt to 200 Nm / Torque rear bolts to 20 Nm + 90°" and "33177840535 superceded 33172282077" [page]. [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/19815-diff-bolt-question)
  - NAM3, 09-13-2023: the original poster first used 128 ft-lb, then edited to "Proper torque should be 200nm or 147.5 ft-lb"; a reply: "the front diff bolt is 200NM" [page]. [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/233495-advice-on-getting-the-front-differential-bolt-torqued-to-spec-on-jack-stands)
  - **Conflict:** an ECS/Rogue Engineering listing says the "factory recommended torque spec of this bolt (when it was an M14 bolt) is 128 ft lbs" [snippet; ECS is behind a Cloudflare challenge]. [ECS Tuning](https://www.ecstuning.com/b-rogue-engineering-parts/rogue-engineering-e46-m3-differential-bushing-front-position-fix/re.484.fix~rog/)
- **Rear subframe to body:**
  - Department 69: "77 Nm, M12 x 1.5. Subframe stud to body: 90 Nm" [page].
  - FCP part 3: "torque the subframe nuts and bolts to 77Nm" [page].
  - Flow PDF p. 15 [page]:
    - "Threaded bolt M12X1,5 ZNS3" (stud, 33 32 6 760 360): 90 Nm
    - "Self-locking collar nut M12X1,5-10" (33 32 6 760 374): 77 Nm
    - "Reduced-shaft bolt M12X1,5X116-8.8" (33 32 6 760 361, rear mounts): 77 Nm
- **Trailing arm:**
  - Department 69: trailing arm to bracket 110 Nm; bracket to body 77 Nm [page].
  - FCP part 2: "reinstall the trailing arm brackets… torque the bolts to 110Nm" [page]. [FCP part 2](https://www.fcpeuro.com/blog/how-to-overhaul-the-bmw-e46-m3-rear-subframe-part-2)
  - FCP part 3 summary: "Rear Trailing Arm Brackets = 110Nm" [page].
  - Flow PDF p. 16: through-bolt 110 Nm, bracket to body 77 Nm, "Car must be in « loaded » position when tightening to avoid bushing pre-load" [page].
- **Provenance caveats [page]:**
  - Department 69 says "Every spec comes from BMW's own repair manual (TIS) and links to the page it came from" (updated October 2026). However, its M3-specific driveline and diff rows link to workshop-manuals.com pages for the 330i M54 sedan, not the M3.
  - The Flow PDF is a forum member's compilation ("credit goes to Florian (Flow) from M3F"). A Z4-forum member noted "some small inconsistencies in that document", for example the reinforcement-plate angle. [Z4-forum](https://z4-forum.com/threads/torque-settings.102802/)

### Inferences
- **Status of each value:**

| Guide row | Status after this check | Change? |
|---|---|---|
| Rear subframe to body 77 Nm; 90 Nm for the stud | Department 69, the Flow PDF and FCP agree; ETK names the stud and bolts | Keep. Could add "M12×1.5 stud 90 Nm; nut and M12×1.5×116 bolts 77 Nm" |
| Trailing arm to bracket 110 Nm; bracket to body 77 Nm | Three compilations agree | Keep. Add "tighten rubber-bushed joints at ride height" (Flow note, not BMW-verified) |
| Half-shaft to diff, M3 100 Nm (non-M 80 Nm) | FCP and the Flow PDF agree; ribbed M10×46 Torx bolts | Keep. Note black (M3) vs silver bolts and new bolts |
| Driveshaft to diff, M3 70 Nm | Department 69, FCP and the Flow PDF agree; ETK confirms M10×46 ribbed Torx | Keep. Mark the shaft's position before removal (it's balanced) |
| Guibo, M3 M12 10.9, 115 Nm | **BMW TIS printout confirms** (M3/M5 row) | Keep. Upgrade source to TIS; ETK bolt M12×1.5×62, self-locking nuts |
| Center mount 21 Nm | Department 69 and the Flow PDF | Keep. Add the 4–6 mm forward preload (compilation-only) |
| M3 diff front 200 Nm | Department 69, the Flow PDF and NAM3 agree; one vendor snippet says 128 ft-lb | Keep 200 Nm. Flag the conflict |
| M3 diff rear 20 Nm + 90° | Department 69, the Flow PDF and NAM3 agree | Keep |
| Pressure plate 25 Nm (8.8) / 34 Nm (10.9) | Department 69 and the Flow PDF; ETK shows the M3 uses 10.9 micro-encapsulated screws | Say "M3: 34 Nm (10.9 screws)"; new screws |
| Flywheel to crank "use BMW's S54 figure" | **TIS: 105 Nm for S54**, oiled, no thread locker | Change to 105 Nm, new M12×1.5×50 bolts |
| Rod bolts M11 5/30/+70°, reuse | **BMW SI confirms**; change-over date is 12/2002 | Keep. Fix the date, add "single stroke" |
| Rod bolts M10 5/30/+105° | **BMW SI confirms**, and it is three full cycles with about one-turn release between | Change to "×3 cycles"; date 12/2002 |

- The pressure-plate screws are "micro-encapsulated" (pre-applied locking compound), which normally works only once. Together with the Flow note, fit new screws. ETK does not state "replace" here; this is an inference.
- The 128 ft-lb (174 Nm) figure equals the non-M E46 rear-mount value in Department 69. It probably comes from the non-M car, not the M3's M14 front bolt, but I couldn't verify that.

### Gaps
- **TIS mirrors I couldn't read** (each blocked rather than worked around):
  - newtis.info: Cloudflare challenge, and DNS failure from WebFetch
  - workshop-manuals.com: Cloudflare "Sorry, you have been blocked"
  - bolidenforum.de: Cloudflare
  - tis.spaghetticoder.org: DNS and TLS failure
  - rfdm.com and web.archive.org: egress tunnel closed
  - adkusters.dsmynas.com: DNS failure
- **Other blocked pages:** princeton.edu directory listing (Cloudflare), zhpmafia.com (Cloudflare), bimmerpost (403), e46fanatics (406 even when rendered), ecstuning.com and arp-bolts.com (Cloudflare).
- So the group 21 (clutch) and group 33 (rear axle) values, the center mount and the driveshaft-to-diff value are not traced to BMW directly. They rest on Department 69's TIS-cited table, the Flow compilation, FCP Euro and NAM3, which agree.
- I didn't verify the guide's statement that the M3's guibo bolts are longer than the 325i's. I only read the M3 bolt (M12×1.5×62) in ETK.
- No source I read gave a BMW instruction on bolt replacement for the half-shaft, driveshaft-to-diff or diff-mount bolts. "Always replace" for the half-shaft bolts comes only from the Flow PDF.
