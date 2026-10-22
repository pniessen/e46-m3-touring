# Rear arches: grafting E46 M3 rear arches onto a US 2003 325i Touring

*Round 4 research, October 2026. Build: 2003 US 325i Touring (RWD, Massachusetts) + 2003–06 US E46 M3 donor (coupe or convertible). Builds on README "Deep dive: bodywork and fitment", Phases 6 and 13, the Massachusetts title paragraph, Open questions (Body), JOB-CARDS card 6, and the notes `convertible_arch_steel.md` and `youtube_conversion_builds.md`. Those are not repeated here except where this round corrects or extends them.*

**How each claim was checked.**
- **[ETK]**: BMW parts catalog on bmwfans.info, read with curl (22 Oct 2026); diagram images viewed.
- **[TIS screenshot]**: a BMW TIS page reproduced as an image in a forum post; I viewed the image.
- **[read]**: page or PDF text read in full or in the relevant part.
- **[transcript]**: YouTube auto-captions from the previous round's downloads, read in full; timestamps are the start of the 20-second caption block. No new YouTube requests were made.
- **[viewed]**: photo or drawing viewed.
- **[snippet]**: seen only in a search-result summary. Unverified.
- **[scaled]**: a dimension **I measured from a drawing** (pixel analysis scaled by the published wheelbase or width). These are **estimates**; the error band is given with each.
- **[inference]**: my reasoning, labelled.

**Blocked or not used (by policy, nothing was bypassed):** newTIS (Cloudflare challenge), e46fanatics and Bimmerfest (proof-of-work bot check), RealOEM, Pelican Parts, getbmwparts, Schmiedmann, Turner Motorsport and Driftworks (Cloudflare or 403), eBay (403), the Wikimedia API (HTTP 429, stopped at once), bigduckclub.com (HTTP 429). The session's web-search budget ran out near the end, so a few planned look-ups (US dealer prices, consumable prices, generic butt-weld references) were not done; they are listed under Gaps.

---

## Takeaway: what changes in the guide

1. **The "25–30 mm" needs a profile, not one number.** BMW publishes 70.1 in (1,780 mm) of width for the M3 and 68.5 in (≈1,739–1,740 mm) for the 325i Sport Wagon: **+20.3 mm per side at the widest point** [read: BMW USA spec sheets]. Scaled from BMW's own M3 dimension drawing and a Touring drawing, the M3 quarter stands out about **+21–23 mm** from 300 mm ahead of the axle to 100 mm behind it, **+25–32 mm** from 150 to 350 mm behind it, and fades to about **+10 mm** 500 mm behind it [scaled, ±5–8 mm]. The 25–30 mm figure (HARD, the e46fanatics owner) fits only the rear half of the flare. Upward, the M3 skin rejoins the Touring's surface about **470–530 mm above the hub centre**, just under the shoulder crease at about **540 mm above the hub** on both bodies [scaled]. **Caveat [inference]:** from roughly 150–220 mm behind the axle rearward, and below the bumper line (≈ 305 mm above the hub), the visible surface on both bodies is the rear bumper cover, whose top line runs forward to the arch edge [viewed: drawings]. So much of the +25–32 mm behind the axle is probably the M3 bumper corner, not quarter steel (Q1, item 3).
2. **The side-view arch opening is the same on all of them.** BMW-style drawings of the M3 coupe, M3 convertible, non-M coupe and Touring all show an arch edge about **340–350 mm above the hub at the top** and **355–365 mm ahead of it at hub height** [scaled, ±10 mm]. The M3's difference is lateral (the flare), not a bigger opening. So the graft is a lateral move of the skin and lip, not a re-cut of the opening.
3. **There is a BMW ride-height figure for the M3.** TIS 33 00 gives the rear as **587 mm on 18-inch rims and 600 mm on 19-inch rims**, measured from the rim flange at the bottom to the lower edge of the wheel arch, in normal position; tolerance 10 mm, and left/right within 10 mm (2 mm in design position). The front is 605 and 619 mm [TIS screenshot]. This replaces "no BMW ride-height figure was found" and gives a pass/fail check on the donor and on the finished car.
4. **The rear door's trailing edge forms the front of the Touring's arch opening.** The Touring's rear door (41527034155/156; the sedan's is 41527034153/154) is cut around the arch [ETK, viewed]. The M3 flare starts ≈ 380–420 mm ahead of the axle in plan view [scaled], while the door/arch junction is roughly 300–350 mm ahead of it [scaled from a non-dimensioned drawing, ±50 mm]. So the first 50–100 mm of the flare's ramp falls on the door. At the shut line, the M3 surface stands about **11–20 mm proud** of the stock door [scaled]: that is the "forward nose" every builder had to beat in, or carry onto the door.
5. **Where to put the joints [inference from the scaled data].** Put the top outer-skin joint in the narrow band between the M3 flare boundary (≈475–490 mm above the hub) and the crease (≈540 mm): **about 500–515 mm above the hub**. Put the rear vertical joint about **550–600 mm behind the axle**, ahead of the Touring's tail-lamp, whose front edge is ≈700 mm behind the axle; that removes any need to weld near the tail-light pocket. Put the front joint 25–40 mm behind the shut line, or on the door if you carry the flare across.
6. **Steel prices are higher and differently sourced than the guide says.** R44 is a **UK** shop pricing in GBP: **£4,420 each** for the left and right M3 coupe quarters (the guide's "$5,525" was a currency-converted figure). An EU retailer lists the coupe quarter at **€6,518.67** each but the **M3 convertible quarter at €1,979.88**, and the convertible's **inner lateral trim panel 41217894553/554 at €131.82–141.50**. That BMW panel appears in the wheelhouse diagram as the convertible's outer wheelhouse half, so it may carry the M3-width inner arch flange [ETK diagram, inference]. **New-BMW-steel route per side (EU prices):** ≈ €2,120 for the convertible skin plus inner panel. That route avoids donor steel and with it the Massachusetts "reconstructed" question.
7. **Corrections:** the vTuned garage video the guide cites twice is an **F80 M3 / F31 328i wagon**, not an E46. Petroyle's rear quarters are **steel**; "carbon wings" means front fenders. The filler pot 51718208646 is **also the Touring's own part**, and the filler area is "virtually the same width" on M3 and non-M (M346), so the guide's "pot and flap end up about 25–30 mm further outboard" is not supported. Details are in the corrections list at the end.
8. **Factory arch-lip construction to reproduce.** The quarter skin and the outer wheelhouse flange form a nested, spot-welded U-channel about 15 mm deep; on the CSL it is bonded and about 4 mm [read: Redish; NAM3]. Reproduce a sealed double skin, or follow Redish's bonded "CSL-style" lip (≈8 mm), which also gains about 7 mm of tire clearance.

---

## Q1. Geometry: the M3 rear quarter and arch against the 325i Touring's

### Cited findings

**Published widths, tracks, wheels and heights (BMW)**
- **BMW USA 2002 "325 models" sheet**, columns 325i sedan, 325xi sedan, 325i Sport Wagon, 325xi Sport Wagon, 325Ci coupe, 325Ci convertible:
  - width **68.5 / 68.5 / 68.5 / 68.5 / 69.2 / 69.2 in**;
  - track front/rear 57.9/58.4 in (xi 57.9/58.3);
  - wheelbase 107.3 in;
  - standard wheels 16 × 7.0 with 205/55R16; Sport Package 225/45R17 (205/50R17 on xi).

  [read, PDF] [BMW USA T0022131EN_US/41405](https://www.press.bmwgroup.com/usa/article/attachment/T0022131EN_US/41405).
- **BMW USA 2003 325 sedan and Sport Wagon sheet:** width 68.5 in for all four; track 57.9/58.4 in (325i), 57.9/58.3 in (325xi); wheelbase 107.3 in; height 55.5 in (325i Sport Wagon) [read, RTF] [T0022146EN_US/41437](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41437). The 2003 330Ci coupe and convertible sheet gives 69.2 in width and the same 57.9/58.4 in track [read] [T0022146EN_US/41438](https://www.press.bmwgroup.com/usa/article/attachment/T0022146EN_US/41438).
- **BMW USA 2002 M3 sheet:** track 59.4/60.0 in; L × W × H 176.9 × 70.1 × 54.0 in (coupe), 53.9 in (convertible); 18 × 8.0 front and 18 × 9.0 rear wheels [read] [T0022127EN_US/41385](https://www.press.bmwgroup.com/usa/article/attachment/T0022127EN_US/41385).
- **BMW training ST041 (M3):**
  - vehicle width **1,780 mm**;
  - "Compared to the E46/2 production vehicle, the track width on the front and rear axle of the E46 M3 have been increased considerably (track width: front axle +37 mm, rear axle +47mm)";
  - heights 1,372 mm unloaded and 1,363 mm loaded;
  - its side-view drawing gives front overhang 774, wheelbase 2,731, rear overhang 987 and length 4,492 mm;
  - "Due to the larger tire sizes, the side frame structures of the E46 M3 are modified in the area of the wheel cutouts"; "The rear quarter panels have also been formed corresponding to the tire sizes and track width".

  [read, PDF p. 5 and body section] [ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/1%20M3%20Complete%20Vehicle.pdf).
- **BMW training ST034 (E46/3 Sport Wagon):** "The wheel base, width and turning radius are the same as the E46 sedan." "From the 'B' pillar rearward, the body shell of the Sport Wagon is all new and includes: New Rear doors…". The E46 convertible width is 1,757 mm (1,947 mm with mirrors) [read, djvu text] [ST034 "1 models"](https://archive.org/download/BMWTechnicalTrainingDocuments/ST034%20E46%20Complete%20Vehicle/1%20models_djvu.txt).
- **Arithmetic** [inference]:
  - M3 vs Touring: 70.1 − 68.5 in = 1.6 in = 40.6 mm, so **+20.3 mm per side at the widest point**; rear track +1.6 in, also +20.3 mm per side.
  - Coupe vs Touring: +0.7 in = 17.8 mm, so +8.9 mm per side, with the **same** 58.4 in rear track: the coupe's extra width is body, not track.
  - M3 vs coupe: +0.9 in, so +11.4 mm per side.

**BMW ride height (TIS 33 00 / 31 00, E46 M3)**
- Screenshot of TIS "33 00 Rear axle – ride height E46/M3": "Ride level height in normal position. Attach tape measure to bottom middle of rim flange and measure to lower edge of wheel arch". Tolerance: normal position max 10 mm, design position max 2 mm; left/right: normal position 10 mm, design position 2 mm. **18" rim 587 mm; 19" rim 600 mm.**
- Screenshot of "31 00 Front axle – ride height E46/M3": **18" 605 mm, 19" 619 mm**, same method and tolerances.
- Screenshot of TIS "33 53 … Measuring ride-level height of vehicle": "Move vehicle into normal position… attach tape measure to rim flange (2) at bottom middle and measure to lower edge of wheel arch (1)", with drawing R31 0177.

[TIS screenshot, viewed] posted by a member, NAM3 thread "What is OE E46 M3 stock ride height from factory?", post #2, 23 Jul 2024: [thread](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/272922-what-is-oe-e46-m3-stock-ride-height-from-factory), images [272931](https://nam3forum.com/forums/filedata/fetch?id=272931), [272932](https://nam3forum.com/forums/filedata/fetch?id=272932), [272933](https://nam3forum.com/forums/filedata/fetch?id=272933). In the same thread, #3 converts by subtracting 9 in (half the rim diameter): front 14.85 in, rear 14.11 in to the hub centre [read]; #12 says the Bentley manual gives 605 mm front for 18 in [read].
- **Non-M E46 values (rear 15" 542, 16" 555, 17" 590, 18" 603 mm; front 576/589/621/634 mm) and the "normal position" load (68 kg in each front seat, 68 kg in the middle of the rear seat, 21 kg in the middle of the trunk, full tank)** were seen only in search summaries of e46fanatics posts [snippet; e46fanatics blocked]. The 16-to-17-inch step (35 mm) is not the 12.7 mm a rim change alone gives, so those rows probably mix variants (an xi, for example); treat them as unverified.

**Factory construction of the arch lip**
- Redish Motorsport: "E46's have a 'U' shaped channel on the inside of the rear wheel arches. This is where two panels meet: The Inner Arch and The Outer Arch… so the robots had something to spot weld"; "All E46 Rear Arch corrosion starts from the Inner Arch area"; "Most E46 rear arches are approx 15mm thick. The CSL rear arches are approx 4mm thick. Our CSL-style arches are approx 8mm thick… approx 7mm more clearance between your tyre and bodywork". Redish bonds its CSL-style lip with "Multi-stage 2k hardened panel bond adhesive… (how the factory created the CSL arch)" [read] [Redish – E46 M3 Rear Arches](https://www.redish-motorsport.com/BMWE46M3RearWheelArchesRust.html).
- NAM3 #2 (Oct 2022): "Both the outer rear arch (quarter panel) and the inner rear arch have a U-shaped channel where they overlap, these two are connected together by a series of spot welds"; #3: "held together with spot welds and seam sealer" [read] [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/189875-how-is-the-rear-quarter-panel-supposed-to-be-attached-to-the-wheel-well).
- Redish (2020 video): "it's normally these seamed edges where the quarter panel laps around on [a] U shape and then just finishes and where it joins then the inner wheel arch" [transcript] [Redish – BMW E46 Rear Arches (2020), 01:00](https://www.youtube.com/watch?v=OWSjvh_28v0&t=60s).

**Which panels carry the arch (ETK, US models; weights from ETK)**
- **US 325i Touring:**
  - rear side panel 41218242347/348 (8.4/8.3 kg);
  - **"Wheelhouse rear, outer half" 41218242355/356** (1.8/2.0 kg; Touring only, from Jun '99);
  - inner half 41148231757/758 (3.6/5.4 kg).

  [ETK] [Touring body-side frame](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/body_side_frame/), [Touring rear wheelhouse](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/), [41218242355](https://bmwfans.info/parts-catalog/41218242355/).
- **M3 coupe:** rear side panel 41217890689/690 (14.5/14.4 kg); **interior side frame 41217890677/678** (5.7/5.6 kg, M3 coupe and CSL only, from Mar '00), listed in both the wheelhouse and the side-frame diagrams [ETK] [M3 coupe rear wheelhouse](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/), [41217890677](https://bmwfans.info/parts-catalog/41217890677/).
- **M3 convertible:** rear side panel 41357894541/542 (11.5 kg); interior side frame 41217894557/558 (33.5 kg); **inner lateral trim panel 41217894553/554** (4.8 kg), listed as item 12 in the rear wheelhouse diagram [ETK] [M3 convertible rear wheelhouse](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/).
- **One diagram image (2s5a.png) serves all three bodies** [viewed]. Item 2 is the inner half (a large tub). Item 11 is the Touring's outer half, a narrow arch-shaped flanged strip. Item 10 is the coupe's interior side frame, a large inner quarter panel with the wheel cut-out. Item 12 is the convertible's inner lateral trim panel, an arch-shaped inner panel with flanges. So on each body the panel that meets the outer skin's lip is item 11 (Touring), 10 (M3 coupe) or 12 (M3 convertible).
- The Touring and sedan rear doors differ: 41527034155/156 (Touring, 12.1 kg) against 41527034153/154 (sedan, 11.4 kg). The ETK door image shows the lower rear corner of the shell cut back around the wheel opening [ETK, viewed] [Touring rear door](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/rear_door_hinge_door_brake/), [sedan rear door](https://bmwfans.info/parts-catalog/E46-Sedan/USA/325i-M54/L-N/browse/bodywork/rear_door_hinge_door_brake/).
- **Fuel filler parts:**
  - Touring: flap 51178208246, hinge **51178151955**, tank filler pot **51718208646**.
  - M3 coupe: flap 51172695524, hinge 51172695527, pot **51718208646**.
  - M3 convertible: flap 51172695524, hinge **51178151955**, pot **51718208646**.

  [ETK] [Touring side panel/tail trim](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/side_panel_tail_trim/), [M3 coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/side_panel_tail_trim/), [M3 convertible](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/bodywork/side_panel_tail_trim/).
- **Rear lamp cups differ:** coupe 41217021957/958 (412 g), convertible 41217022603/604 (391 g), Touring 41217022411/412 (1.2 kg) [ETK, same pages].
- **Rear "additional shock absorber" (bump stop):** M3 33532229777; the Touring uses a "repair kit, additional damper guard tube" 33502290317. ETK gives no length [ETK] [M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/rear_axle/rear_spring_strut_mounting_parts/), [Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/rear_axle/rear_spring_strut_mounting_parts/).

**Builders' observations of the shape**
- M346 Projects (US, 2004 Touring and 2003 M3 convertible donor):
  - "an M3 or a coupe is physically wider than a sedan or a touring even down to here… this forward nose part… sits wider on a coupe or an M3 and on sedan and touring… they actually have to beat in and massage and blend in that forward piece… on the sedan touring this part is actually pushed in more and then starts to flare out more up here to the proper width" [transcript] [Pt 14 (2024), 28:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1700s), [28:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1720s), [29:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1740s).
  - At the filler area: "it's almost the same distance here… it's not wide on the M3 here it gets wide here and here but on a non-M and an M they're virtually the same width sheet metal wise and chassis wise… this hole will still line up" [transcript] [Pt 14, 17:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1020s), [17:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1040s).
  - "a lot of little small differences that all add up between the M and the non-M chassis… this quarter panel is going to go in a couple millimeters more" [transcript] [Pt 14, 25:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1520s), [26:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1580s).
  - "the new M3 inner tub is so wide it almost looked like it is the fender compared to the other side" [transcript] [Pt 14, 40:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2440s).
- Tracks and Trails (Canada, 2004 325i Touring and 2002 M3 coupe donor): "The old inner wheel well comes down a little bit lower" than the donor flare [transcript] [What it really takes (2026), 17:40](https://www.youtube.com/watch?v=nADBRfX9DqY&t=1060s).
- HARD Motorsport (ABS rivet-on flares "created the molds directly from actual M3 fenders"): "REARS: Aprox 30mm wider"; "Rear Door pieces are separate"; fitment "E46 non-M Sedan (pre and post facelift) E46 Touring / Wagon"; $294.00 list, $264.60 sale in Oct 2026 [read] [HARD Motorsport](https://www.hardmotorsport.com/hard-motorsport-bmw-e46-sedan-touring-m3-style-motorsport-fender-flares-rear-set/).
- Big Duck Club (US drift kit, coupe only): "+60mm width per side" over a non-M coupe [read] [DriftHQ listing](https://drifthq.com/products/big-duck-club-e46-coupe-rqp-rear-quarter-panel). A search summary adds "35 mm wider than the M chassis", which would put the M3 about 25 mm per side over the non-M coupe [snippet; bigduckclub.com returned HTTP 429]. This is aftermarket marketing, not a measurement.

### Inferences: measured from drawings [scaled]

**Method.** I measured four orthographic drawings by pixel analysis: line tracing from the fitted wheel centres, and outline extraction in plan and rear views.
- Two are **BMW press dimension drawings**, distributed by getoutlines.com under a "Creative Commons" licence: the **M3 coupe** (2,919 × 1,565 px, with BMW's dimension lines 2731/4492/1780/1924/1508/1525/1383 [viewed] [getoutlines 6769](https://getoutlines.com/blueprints/6769/2007-bmw-m3-e46-coupe-blueprints)) and the **M3 convertible** (2,500 × 1,315 px, same template [viewed] [getoutlines 453](https://getoutlines.com/blueprints/453/2004-bmw-m3-e46-c-cabriolet-blueprints)).
- One is a **BMW-template non-M facelift coupe** drawing (2,500 × 1,328 px [viewed] [getoutlines 356](https://getoutlines.com/blueprints/356/2004-bmw-3-series-e46-coupe-blueprints)).
- One is a **facelift E46 Touring** drawing (1,600 × 887 px; artist unknown; no dimension lines [viewed] [getoutlines 372](https://getoutlines.com/blueprints/372/2004-bmw-3-series-e46-touing-wagon-blueprints)).

Each side view was scaled by its published wheelbase (M3 2,731 mm; coupe and Touring 2,725 mm).
- **M3 coupe drawing:** the width scaled this way came out at **1,782 mm against 1,780** published (0.1%) and the length at 4,508 against 4,492 mm, so it is reliable to about ±3–5 mm.
- **Touring drawing:** its side and top views disagree by 2%, so I normalized its plan view to the published 1,739 mm. Its numbers are good to ±5–8 mm.
- Positions are given relative to the **rear hub centre**: X positive forward (negative behind the axle), Y positive up.

1. **Side-view arch opening** (stroke centre of the bold arch line; radius from the hub centre):

   | Angle from hub (0° = forward horizontal, 90° = top, 180° = rearward) | M3 coupe (BMW) | M3 convertible (BMW) | Non-M coupe (BMW template) | Touring |
   |---|---|---|---|---|
   | 0° (front, hub height) | 364 | 364 | 361 | ≈ 355 (10°) |
   | 20° | 355 | 348 | 347 | 350 |
   | 30° | 355 | 346 | 346 | 348 |
   | 40° | 357 | 346 | 343 | 346 |
   | 50° | 355 | 344 | 339 | 346 |
   | 90° (top) | **348** | not resolved | **350** | **340** |
   | 120° | 352 | 346 | 341 | 353 |
   | 140° | 356 | 352 | 347 | 353 |
   | 160° | 361 | 360 | 360 | 360 |
   | 180° (rear, hub height) | 379 | 387 | 382 | 383 |

   Circle fits: M3 coupe R ≈ 365–372 mm centred ≈ 30–50 mm below the hub; non-M coupe R ≈ 365 mm, 23 mm below; Touring R ≈ 369 mm, 28 mm below.

   **Reading:** the openings agree within drawing error (±5–10 mm). The M3 coupe and convertible openings agree within 2–9 mm. Below about 70°, a double line about 18–21 mm outside the bold edge, drawn on every one of them, represents the lip band.
2. **Height of the lip above the hub, cross-checked with TIS.**
   - Read with the tape hooked on the outer edge of the rim flange, the TIS rear value gives **hub-to-arch = 587 − (228.6 + 17.5 J-flange) ≈ 341 mm**. Read from the bead seat it gives 587 − 228.6 = 358 mm. The 19-inch value gives the same body height either way (600 mm minus a 12.7 mm larger radius).
   - The BMW drawing shows 348 mm [scaled].
   - **Practical rule:** if the donor and the Touring wear the same M3 wheels, compare the TIS-style rim-flange-to-arch figures directly and skip the conversion.
   - The M3 tire, 255/40R18, has an unloaded radius of about 330.6 mm (457.2/2 + 0.40 × 255), so the radial gap at the top in normal position is about 10–28 mm, depending on which reading is right [inference].
3. **Plan-view half-width** (distance from the car's centre line to the outermost body outline at each station; + = behind the axle):

   | Station from rear axle (mm) | M3 coupe | Non-M coupe | Touring (normalized) | **M3 − Touring** | M3 − non-M coupe |
   |---|---|---|---|---|---|
   | −800 (ahead) | 871 | 874 | 867 | +4 | −3 |
   | −600 | 870 | 871 | 862 | +7 | −1 |
   | −500 | 868 | 868 | 859 | +9 | 0 |
   | −400 | 866 | 865 | 856 | +9 | +1 |
   | −350 | 871 | 863 | 855 | **+16** | +8 |
   | −300 | 883 | 863 | 861 | **+22** | +20 |
   | −200 | 889 | 868 | 868 | +21 | +21 |
   | −100 | 890 | 870 | 869 | +21 | +20 |
   | 0 (axle) | **890** | 870 | 867 | **+23** | +20 |
   | +100 | 889 | 869 | 866 | +23 | +21 |
   | +150 | 888 | 867 | 863 | +25 | +21 |
   | +200 | 887 | 864 | 858 | **+29** | +23 |
   | +250 | 884 | 861 | 855 | +29 | +23 |
   | +300 | 881 | 858 | 850 | **+31** | +23 |
   | +350 | 874 | 852 | 841 | **+32** | +22 |
   | +400 | 857 | 846 | 835 | +22 | +11 |
   | +450 | 844 | 839 | 831 | +13 | +5 |
   | +500 | 836 | 832 | 825 | +11 | +4 |
   | +600 | 819 | 816 | 812 | +7 | +4 |

   **Reading** [scaled, ±5–8 mm for the Touring columns]:
   - The M3 flare (measured against the non-M coupe) runs from **≈ 380 mm ahead to ≈ 420 mm behind the axle, about 800 mm long**, and stands about **20–23 mm** proud.
   - The Touring body is **7–9 mm narrower than the coupe** ahead of −400 and behind +200, and about equal at the axle (≈ 867–870). That is consistent with BMW's widths, 1,739 (Touring, widest at the arch "hip") and 1,757 (coupe, widest at its doors: ≈ 877–878 mm half-width in the coupe drawing).
   - The M3 convertible drawing matches the M3 coupe's outline within 3–7 mm after a uniform 0.7% scale offset, except 350–400 mm behind the axle, where it turns in about 10 mm sooner (probably drawing detail; check with templates).
   - **Caution: steel or bumper behind the axle?** [inference] In both side views (M3 coupe and Touring), the rear bumper's top line (≈ 305 mm above the hub) runs forward to meet the arch edge roughly 150–220 mm behind the axle. Behind that point and below the bumper line, the visible surface is the bumper cover on both cars [viewed: drawing crops]. The M3 flare line drops onto the bumper line about 300 mm behind the axle, so above the bumper line the steel flare tapers to nothing between about 200 and 300 mm behind the axle.
     - The table's values at stations +250 to +450 (behind the axle: +29, +31, +32, +22, +13) are therefore probably the M3 bumper corner against the Touring bumper corner, not quarter steel.
     - Consequences: the Touring bumper corner must come out by about that much (M346's relief cuts, Ultimate Klasse's plastic welding; Q4), and the steel and arch lip hidden under the bumper there may need less move-out than the table suggests. Measure the donor with its bumper off.
4. **The M3 flare's boundary line in side view.** The BMW coupe drawing draws a styling line: **≈ 475 mm above the hub at the top**, ≈ 490 mm at 50° forward (X +315, Y +376), and running down into the bumper top line at about **X −300, Y +305**. The non-M coupe's and Touring's equivalent "eyebrow" lines sit at ≈ 425–436 mm [scaled]. The **shoulder crease** is at ≈ **540 mm above the hub** on both the M3 coupe and the Touring drawings [scaled].
5. **Rear-view silhouettes** (M3: scaled from BMW's 1,780/1,924 mm width dimensions; Touring: normalized to 1,739 mm):
   - Both cars are widest at **≈ 600–690 mm above the ground**, about the height of the arch crown (hub ≈ 315 mm above the ground + 340–350 mm).
   - M3 − Touring half-width: ≈ +18–21 at 650 mm above the ground (the crown), +20–22 at 500–530, +25 at 465, +16 at 700, +11 at 750, +6 at 780, ≈ 0 at 840.

   So upward the M3 bulge fades out about **470–530 mm above the hub** [scaled, ±5 mm]. The tires are the outermost outline below ≈ 430 mm above the ground in both drawings.
6. **Tire against body, laterally.** With the hub face at ≈ 788 mm from the centre line on both cars (README), the M3 rear tire's widest sidewall sits at ≈ 762 + 130 = **≈ 892 mm** from the centre line, assuming 255/40R18 measures about 260 mm across on a 9J rim [inference].
   - That is about flush with the M3's flare crown (≈ 890–891).
   - It is **≈ 22 mm outside the stock Touring's widest point** (≈ 869.5). An unflared Touring on M3 wheels therefore has tires standing proud of the body, which matters for Massachusetts inspection rule 540 CMR 4.04(12)(c) (README table) [inference].
7. **Where the door meets the arch on the Touring** [scaled from the non-dimensioned Touring drawing, ±50 mm; and viewed in the guide's photo `photos/touring-rear.jpg` and the prototype photo]:
   - The rear door's trailing edge reaches the arch at roughly the **10 o'clock** position, about **X +300 to +350 mm, Y +150 to +250 mm**. Below that point the door's cut edge forms the front of the opening.
   - With the M3 flare beginning at X ≈ +380 to +420 (plan view), the first ≈ 50–100 mm of the flare's ramp lies on the door.
   - At the shut line the M3 surface would stand **≈ 11–20 mm** proud of the stock door (the table at X +300 to +350 gives +16 to +22, less the ramp) [inference].
8. **Tail-lamp and bumper positions** (Touring drawing): the tail-lamp's front edge is at ≈ X −700 mm and its lower edge ≈ Y +360; the bumper top line is at ≈ Y +300–310 on both bodies [scaled, ±20 mm].
9. **Filler flap position:** not measurable here; the drawings show the left side. M346 found the hole "lines up for the most part"; the M3 bracket holes differ and its surround "sat back a little bit further" with a different lip depth [transcript] [Pt 14, 36:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2200s), [39:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2340s).

### Gaps
- No BMW body dimension sheet (TIS 51 00) and no BMW drawing of the Touring with dimension lines was opened (newTIS blocked). The Touring numbers rest on a 1,600 px drawing of unknown origin, normalized to BMW's width.
- No 3D scan or dimensioned photo of an E46 M3 quarter was found. Searches for scans found none, and the search budget ran out before a second pass.
- The lip's lateral position against the tire face on a real donor is unmeasured: measure it (Phase 1).
- The Touring shut-line/arch intersection is ±50 mm: measure it on the car.
- The non-M TIS ride-height table is snippet-only.

---

## Q2. Steel sources: part numbers, 2026 availability and prices

### Cited findings
- **R44 Performance (UK shop; prices in GBP; "Since Brexit, orders shipped from the UK into the EU are imports…"):**
  - Genuine BMW E46 M3 rear quarter panel, **right 41217890690: £4,420.00**, Shopify flag `"available": true` [read, product JSON, 22 Oct 2026] [R44 right](https://r44performance.com/products/genuine-bmw-e46-m3-rear-quarter-panel-right-41217890690).
  - **Left 41217890689: £4,420.00**, `"available": true` [read] [R44 left](https://r44performance.com/products/genuine-bmw-e46-m3-rear-quarter-panel-left-41217890689).
  - R44's policy page says orders with backorder items ship together, so "available" may still mean a lead time [read].
- **eStore-Central** (European online BMW parts seller, "World wide delivery with DHL"; prices in EUR, Oct 2026; no stock information shown, every line has "Add to Cart") [read]:
  - M3/CSL coupe rear side panel 41217890689/690: **€6,518.67 each** [eStore-Central, M3 CSL body-side frame](https://www.estore-central.com/bmw-parts-catalog/E46-M3_CSL-S54/Coupe/Bodywork/Body-Side-Frame/).
  - M3 convertible rear side panel 41357894541/542: **€1,979.88 each**; interior side frame 41217894557/558 €959.57; section of entrance 41217895725/726 €983.74–1,005.77 [M3 convertible body-side frame](https://www.estore-central.com/bmw-parts-catalog/E46-M3-S54/Cabrio/Bodywork/Body-Side-Frame/).
  - M3 convertible **inner lateral trim panel 41217894553 €141.50, 41217894554 €131.82**; wheelhouse inner half 41148231757/758 €284.46 [M3 convertible rear wheelhouse](https://www.estore-central.com/bmw-parts-catalog/E46-M3-S54/Cabrio/Bodywork/Rear-Wheelhouse-Floor-Parts/).
  - M3 coupe **interior side frame 41217890677/678: €1,205.48 each** [M3 coupe rear wheelhouse](https://www.estore-central.com/bmw-parts-catalog/E46-M3-S54/Coupe/Bodywork/Rear-Wheelhouse-Floor-Parts/).
  - Touring outer wheelhouse half 41218242355 €29.83, 41218242356 €189.75 [Touring rear wheelhouse](https://www.estore-central.com/bmw-parts-catalog/E46-325i-M54/Touring/Bodywork/Rear-Wheelhouse-Floor-Parts/).
  - Touring rear side panel 41218242347 €1,699.87, 41218242348 €1,795.28 [Touring body-side frame](https://www.estore-central.com/bmw-parts-catalog/E46-325i-M54/Touring/Bodywork/Body-Side-Frame/).
  - M3 filler flap 51172695524 (primed) €45.06; hinge 51178151955 €12.99; filler pot 51718208646 €18.57 [M3 convertible side panel/tail trim](https://www.estore-central.com/bmw-parts-catalog/E46-M3-S54/Cabrio/Bodywork/Side-Panel-Tail-Trim/).
- bmwfans shows EUR "price" tooltips (for example €633.58 for the coupe quarter and €431.78 for the convertible quarter). These are far below every live retailer and undated; treat them as stale [ETK].
- **ETK lists no "section" or arch repair part for the M3 rear quarter.** The only E46 rear "Section of rear fender" (41217057389/390, 14.9 kg, from Mar '01) is for sedans only [ETK] [41217057389](https://bmwfans.info/parts-catalog/41217057389/).
- **Redish's "Genuine BMW Inner Wheel Arch Panels":** "around £300 per side" in 2015, NLA in 2024, "£990 EACH PANEL" in 2025 [read] [Redish](https://www.redish-motorsport.com/BMWE46M3RearWheelArchesRust.html). In 2016 Redish described "the BMW repair panel… a genuine BMW panel cut that to size" for an M3's inner arch [transcript] [Redish (2016), 01:40](https://www.youtube.com/watch?v=7bZRLQqmEkg&t=100s), [02:40](https://www.youtube.com/watch?v=7bZRLQqmEkg&t=160s).
- **Redish on the side-panel route** (Autoalex Part 3, 2023): "we've tried buying an entire BMW side panel and it works fine but it's 2,300 and something pounds each side… and then Lawrence does some which are like 10% of that… we've used them and they work well" [transcript] [Autoalex Cars – Part 3, 06:00](https://www.youtube.com/watch?v=cwbRDG7XHa8&t=360s). Same video: "inner wheel arch panels because they're always rotten out on the M3 and we convert them to a CSL one" [04:20](https://www.youtube.com/watch?v=cwbRDG7XHa8&t=260s).
- **LBL Panels (UK):** "Standard arch £225 and Full arch panel £375 each", 1.2 mm mild steel; fitting 8–12 hours [snippet; m3cutters blocked]. No web presence found by search.
- **Generic E46 coupe/convertible repair arches** are "All models except M3" (Mecatechnic, prior note). A forum snippet mentions **0.8 mm Klokkerholm** E46 quarter repair panels that "always need some modifications" [snippet; e46fanatics "Replacement panels for rear arch rust repair"].
- **Aftermarket M3-look panels for 4-doors:** HARD ABS rivet-on, rear set $294 list ($264.60 sale), separate rear-door pieces [read, above]. Big Duck Club (fibreglass, coupe only), TH Components (FRP over-fenders, coupe only, about €312–337) and FineLine Aero (coupe track quarters, $800) [snippet]: none fits a Touring.
- **Historical German prices** (bmw-syndikat, Jun 2007): a new M3 side panel "so um die 300–350€ je seite… dann brauchst auch noch das innere radhaus… um die 200€ je seite"; cutting a side panel out of a crashed car is "locker ein Tag" (an easy full day) of drilling spot welds [read] [bmw-syndikat 115032](https://www.bmw-syndikat.de/bmwsyndikatforum/topic115032_E46_M3_Radlaeufe_fuer_hinten_woher___BMW-Talk.html).

### What documented builds used
| Build | Steel | Source |
|---|---|---|
| M346 Projects (US, 2024) | Donor 2003 M3 **convertible** quarters with their inner tubs; the donor quarters had accident damage and filler | [transcript] [Pt 14, 57:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=3420s) |
| Tracks and Trails (CA, 2026) | Donor 2002 M3 coupe **outer skin only**; Touring's inner well kept | [transcript] [12:40](https://www.youtube.com/watch?v=nADBRfX9DqY&t=760s), [15:00](https://www.youtube.com/watch?v=nADBRfX9DqY&t=900s) |
| SOS Customz (US shop, 2023) | Pre-cut M3 quarter sections supplied by the owner | [transcript] [03:20](https://www.youtube.com/watch?v=L8m9gEOklVY&t=200s), [14:40](https://www.youtube.com/watch?v=L8m9gEOklVY&t=880s) |
| M3projekts (HU) | Ep8 (Dec 2023): M3 rear fenders "cut together with part of the inner edge… drilled down at the point welds, leaving only the outer plate" | [transcript, manual English subs] [Ep8, 14:00](https://www.youtube.com/watch?v=5xBcY33CPCM&t=840s) |
| Bimmer Invasion car (San Diego) | First quarters "understated… didn't go into the door"; redone with **new M3 quarter panels** welded on by "Lauren" | [transcript] [11:20](https://www.youtube.com/watch?v=GfxQDkaxeN8&t=680s) |
| Renner car (Larry Chen, 2025) | Donor M3 outer quarter; "the inner quarter is metal and the inner structure is also metal so we have to fabricate everything from scratch" | [transcript] [03:00](https://www.youtube.com/watch?v=YM2gyQOaJCk&t=180s) |
| Calvin's Car Diary / VRS (UK, 2020) | Donor M3 rear quarters | [transcript] [PT9, 02:00](https://www.youtube.com/watch?v=-BMrhOr8fdg&t=120s) |
| Autoalex / Redish (UK) | "welding M3 exterior panels on the existing body"; work on "the section in the door" in progress (Mar 2024) | [transcript] [Finale, 03:40](https://www.youtube.com/watch?v=N8pdzFoVu9k&t=220s), [v2 update, 09:00](https://www.youtube.com/watch?v=vAHWkcGu8ek&t=540s) |
| Stuart Moulton (US, 2013) | "the entire rear end is chopped and fitted from a salvaged M3. He welded in the rear quarter panels" | [read] [Ultimate Klasse](https://www.ultimateklasse.com/blog/2013/5/27/stuart-moultons-e46-zhp-touring) |
| Henry Schwantner (Berlin, 2019) | 2005 320d LCI Touring: "an der Hinterachse entsprechenden Radläufe eingeschweißt und die Türen angepasst" (matching arches welded in at the rear axle, doors adapted); spec list "Kotflügeln, Seitenwänden, hinteren Türen" (front wings, side panels, rear doors) | [read] [Eurotuner, 17 Feb 2019](https://eurotuner.de/m3-transformation-fuer-den-e46-touring/) |
| Petroyle (UK, 2026) | "The quarter panels stay in steel"; carbon rear bumper, sills, boot floor, front wings | [read] [BMWBlog, 9 Apr 2026](https://www.bmwblog.com/2026/04/09/e46-bmw-m3-touring-petroyle/) |

### Inferences
- **Cheapest new-BMW outer skin: the M3 convertible quarter.** At €1,980 it costs about 30% of the coupe panel's €6,519 at the same retailer. It contains the whole arch, flare and filler opening (prior note; ETK weights 11.5 against 14.5 kg).
- **Candidate new-BMW inner arch: the convertible's inner lateral trim panel 41217894553/554 (≈ €132–142).** It occupies the outer-wheelhouse-half position in BMW's diagram (item 12). Its arch flange should match the M3 skin. This is a reading of a generic diagram, so inspect one before you rely on it.
- **Redish's £990 "inner wheel arch panel" is probably the M3 coupe interior side frame 41217890677/678** (€1,205 at eStore-Central ≈ £1,000), not the shared inner half 41148231757/758 (€284). The £-price match and "cut that to size" support this; Redish never names the part.
- **Massachusetts.** A Touring built from **new BMW quarters plus new inner arch panels** has no donor-body steel welded in, which removes the c. 90D §20F question for the arches. The statute's trigger is "welding together or connecting the frames or unit bodies of two or more motor vehicles"; its affidavit asks for "the location of the point of connection or weld joint of the two or more vehicle frames" [read] [c. 90D §20F](https://malegislature.gov/Laws/GeneralLaws/PartI/TitleXIV/Chapter90D/Section20F). Whether quarter-skin grafts from a donor count is still the RMV's call.
- **Per side, new steel route (EU retail, ex-shipping):** €1,980 (convertible skin) + €137 (inner lateral trim panel) + €45 (flap, right side only) ≈ **€2,160**; about **€4,280 for both sides plus one flap**. The coupe route is €6,519 + €1,205 ≈ €7,724 per side. US prices are unverified.
- **LBL is probably the "Lawrence"** Redish mentions: "~10% of £2,300" ≈ £230 matches LBL's £225 "standard arch" [inference]. LBL's 1.2 mm steel is thicker than the OEM skin (I-CAR notes typical outer panels around 0.70 mm; the Klokkerholm snippet says 0.8 mm), so you'd be welding a thin skin to a thicker repair panel.

### Gaps
- US dealer prices and stock in 2026 for 41357894541/542, 41217894553/554 and 41217890677/678: US dealer sites (RevolutionParts and similar) were behind Cloudflare, and the search budget ran out. The guide's $2,390–2,610 is still snippet-only.
- Whether 41217894553/554 really carries the arch flange: inspect a part or a convertible shell.
- LBL Panels' current range and fitment.

---

## Q3. Cut and join plan

### Cited findings

**BMW and OEM guidance (no E46 TIS 41 text was accessible)**
- I-CAR on BMW: "sectioning a part is only allowed if supported by vehicle maker repair information… Vehicle-specific BMW/Mini repair manuals offer procedures for sectioning of various parts"; BMW's "Repair Stage 3" covers "Repairs that are carried out by bonding and riveting with the use of a straightening bench or welding"; the manuals are at bmwtechinfo.bmwgroup.com [read] [I-CAR – Structural Sectioning Procedures: BMW/Mini (2017, validated 2025)](https://rts.i-car.com/crn-599.html).
- I-CAR on the 2017 BMW X5 (F15; **another model**, a modern bonded body): "The outer quarter panel uses adhesive only and welded butt joints with reinforcement plates as the backings. There is a special procedure and parts for completing the sectioning joint" [read] [I-CAR crn-834 (updated Oct 2026)](https://rts.i-car.com/crn-834.html). This is current BMW practice for outer quarters, but not an E46 procedure.
- I-CAR: GM's overlap joint is cut "to overlap the original part on the vehicle 25 mm (1")" and fillet-welded with "a skip or stitch technique… 25 mm (1") welds along the seam with 25 mm (1") gaps between each weld, and then going back to fill in the gaps" [read] [I-CAR crn-25](https://rts.i-car.com/crn-25.html). **Another make**; the stitch rhythm transfers.
- I-CAR GMA test standards:
  - "thin-to-thin" plug weld (22 ga, 0.68–0.81 mm) in a **6 mm hole**, representing "plug welds on a pinchweld flange joining two exterior panels, such as along a wheelhouse opening";
  - "thick-to-thick" (16 ga) in an **8 mm hole**;
  - pass: a tearout hole in the bottom coupon "at least 5 mm, but no greater than 10 mm";
  - "Many of today's steel-structured vehicles use steel in the range of 0.70 mm thickness for the outer panels".

  [read] [I-CAR – Revised Steel GMA Welding Course](https://rts.i-car.com/oem-restraints-system-part-replacement-search/51df0590-ca17-4e8f-a0c4-939263a9c236.html).
- Miller: ER70S-6 wire; ".023–.024 wire size is best for body panels and thickness up to 1/16"; stick-out 1/4–3/8 in; push technique on sheet; butt weld with the gun at 90° and a 5–15° travel angle; "On thin body panels, a spot or spot stitch weld while moving around the panel will help keep heat soaking and warping to a minimum"; plug welds at 90° with "a small circular movement"; overhead: reduce settings 10–15% [read] [Miller – MIG basics for automotive repair](https://www.millerwelds.com/en-US/resources/knowledge-hub/mig-welding/how-to/mig-basics-for-automotive-welding-repair).
- Redish (BMW inner-arch repair on an M3, 2016):
  - "whilst we've got the quarter panel lip folded out to remove the old panel";
  - zinc-phosphate metal prep and "weld through Edge primer";
  - heat-shield gel on painted areas;
  - "the plug weld[s] are done on the inside… hardly any [paint] damage, little bit distortion up in the corner";
  - infrared drying "over an hour" before sealing; POR-15 two coats; high-build primer;
  - two-stage sprayable seam sealer, first "low volume but high pressure… on the welded lines", then a thicker coat, brushing sealer into the U-channel "to fill the channel up", 24 h cure between stages.

  [transcript] [Redish (2016), 04:00](https://www.youtube.com/watch?v=7bZRLQqmEkg&t=240s), [04:20](https://www.youtube.com/watch?v=7bZRLQqmEkg&t=260s), [05:20](https://www.youtube.com/watch?v=7bZRLQqmEkg&t=320s), [06:40](https://www.youtube.com/watch?v=7bZRLQqmEkg&t=400s), [07:00](https://www.youtube.com/watch?v=7bZRLQqmEkg&t=420s), [09:20](https://www.youtube.com/watch?v=7bZRLQqmEkg&t=560s).
- Redish on BMW and adhesives: "manufacturers (including BMW)… now a days insist on replacement panels being bonded"; the screenshot offered as proof is an **F30** side-frame diagram listing body adhesive 83 19 2 158 654 [viewed]. That is **another model**: it shows BMW's modern practice, not an E46 instruction [Redish](https://www.redish-motorsport.com/BMWE46M3RearWheelArchesRust.html).

**What the builds did (method, joint, sequence)**
- **SOS Customz:**
  - cut "right here up to right here… flare out this door… we're not going to weld anything [on the door]";
  - "keep the inner structure all intact… leave a little lip… make sure that this matches up with our gas door area";
  - "created a step on the existing quarter panel… a little bit of a ledge to line up our replacement section… all these little holes that's where we're going to… tack it on… then we'll do a full bead and then we'll grind it";
  - "lifted up the inner structure just a bit to give us that raised edge so when we flare out the door this is going to sit real nice";
  - both quarters welded on days 4–5.

  [transcript] [02:00](https://www.youtube.com/watch?v=L8m9gEOklVY&t=120s), [02:20](https://www.youtube.com/watch?v=L8m9gEOklVY&t=140s), [14:00](https://www.youtube.com/watch?v=L8m9gEOklVY&t=840s), [14:20](https://www.youtube.com/watch?v=L8m9gEOklVY&t=860s), [15:00](https://www.youtube.com/watch?v=L8m9gEOklVY&t=900s).
- **Tracks and Trails:**
  - "preserve as much of the inner wheel well from the non-M chassis as possible… I need this arch going over the rear door";
  - "cut off the inner lip… drill out some spot welds… separate just the outer skin";
  - "butt weld this part of the fender flare where it's replacing… the old fender flare… this part… overlay that onto the door";
  - bonding plan: "Panel bond here to here. That lip lines up beautifully… hammer it out, make a lip, and then panel bond that… Weld it in place";
  - weld-through primer on the back first; tack, let the glue set, then weld; gussets from tape templates.

  [transcript] [12:40](https://www.youtube.com/watch?v=nADBRfX9DqY&t=760s), [13:20](https://www.youtube.com/watch?v=nADBRfX9DqY&t=800s), [15:40](https://www.youtube.com/watch?v=nADBRfX9DqY&t=940s), [18:00](https://www.youtube.com/watch?v=nADBRfX9DqY&t=1080s), [19:00](https://www.youtube.com/watch?v=nADBRfX9DqY&t=1140s), [20:40](https://www.youtube.com/watch?v=nADBRfX9DqY&t=1240s), [23:20](https://www.youtube.com/watch?v=nADBRfX9DqY&t=1400s).
- **M346 (with a visiting metalworker):**
  - donor: separate the inner and outer skins by drilling spot welds; "make sure to cut as much of the wheel tub as possible… if you don't have that you're going to have a gap";
  - the Touring's inner-tub lip "was originally pointed straight down… gently massaged with a hammer… to form this lip";
  - "buckling… from stretching the metal… cut and test fit so many times… throw [in] three tack welds";
  - inner tub fully welded to the shell **before** the outer skin; a deformed factory hole plated over; "spot welds… happen to line up with the M3 skin";
  - 3M weldable zinc primer on all bare metal; sound-deadening mat cut back 1 inch;
  - moon-shaped gap at the rocker/door plated "with… a ton of little tiny welds".

  [transcript] [Pt 14, 27:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1640s), [30:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1820s), [31:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1860s), [33:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1980s), [34:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2080s), [36:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2160s), [41:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2480s), [46:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2760s), [48:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=2880s).
  - **Second side:** with no filler, "doesn't have to do a big square cutout"; "went a little bit quicker"; did not unfold the inner lip [transcript] [55:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=3340s).
- **Calvin's body man (VRS):** "you can't continuously weld this thickness gauge metal because you'll get heat distortion… so you have to stitch it… what you want to look for is… penetration… through both sides of the metal" [transcript] [PT9, 12:40](https://www.youtube.com/watch?v=-BMrhOr8fdg&t=760s).

**Distortion and mistakes recorded**
- M346, a year later: the left rear quarter's corner where it meets the bumper "always looked a little [off]… it must have been when we welded the inner tub to the outer tub… maybe it was too much heat, but it caused the quarter panel to bend in a little bit". He pulled it out with a ratchet strap anchored to a tree, plus heat [transcript] [Pt 23 (2025), 14:00](https://www.youtube.com/watch?v=oaycAZRakfc&t=840s), [14:40](https://www.youtube.com/watch?v=oaycAZRakfc&t=880s), [16:20](https://www.youtube.com/watch?v=oaycAZRakfc&t=980s).
- M346's painter: "when you do a lot of welding, there's a lot of rippling that you can't really see, but you can feel… we did a skim coat"; and "maintaining the definition of this arch. A lot of times when people do conversions, they get so much bondo and glaze that… the arch just kind of gets lost" [transcript] [Pt 24 (2025), 00:20](https://www.youtube.com/watch?v=yQF7MbuPDVI&t=20s), [01:20](https://www.youtube.com/watch?v=yQF7MbuPDVI&t=80s).
- M346: started with 100% argon (a TIG gas); "could not get a good solid bead"; switched to 75/25 [transcript] [Pt 14, 14:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=880s).

**Protection after welding (builds)**
- Tracks and Trails: 100-grit scuff, 2K epoxy, filler, epoxy, high-build; "seam sealing everything… dousing the inside with some wool wax cavity wax" [transcript] [24:20](https://www.youtube.com/watch?v=nADBRfX9DqY&t=1460s), [27:40](https://www.youtube.com/watch?v=nADBRfX9DqY&t=1660s).
- M346: zinc coating, primer, seam sealer, rock chip, etching primer [transcript] [Pt 14, 52:20](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=3140s).
- Calvin: "BMW multi-purpose body filler… dolphin glaze… self-leveling polyurethane" [transcript] [PT9, 13:40](https://www.youtube.com/watch?v=-BMrhOr8fdg&t=820s).

### Inferences
- **Joint choice for an amateur, outer skin:** a **butt joint with a 0.8–1.0 mm gap**, tacked and spot-stitched, is the cleanest finish (Tracks and Trails, Calvin) and the lowest-filler option. A **joggle (step) with plug holes**, as SOS did, is easier to align and more forgiving of gaps, but it leaves a double thickness on the outside face that traps moisture unless it is sealed from inside, and a stepped seam needs more filler.
- Given BMW's own modern preference (adhesive plus welded butt joints with backing strips; I-CAR on the X5), a **butt joint with a narrow backing strip behind it**, plug-welded or bonded to one side only, is a reasonable home approach. The backing makes alignment and penetration easier [inference].
- **Arch lip:** reproduce the factory U-channel. Either:
  - (a) graft the donor's outer wheelhouse/lip region with it (M346), or
  - (b) extend the Touring's outer half (41218242355/356) outward by the flare offset (≈ 20 mm at the crown, 25–30 mm behind the axle; see Q1) with a fill strip or a hammered lip (Tracks and Trails).

  Then join the skin lip to it with 6 mm plug welds (I-CAR's thin-to-thin class), adhesive, or both. Finish with seam sealer brushed into the channel (Redish).
- **Sequence:** structure (inner lip) first, skin second, as M346 did. M346's later corner pull-in is a warning: weld the inner tub with short stitches, cool between them, and re-check the outer surface against templates **before** the skin goes on.
- **Thickness.** Expect OEM skins of about 0.7–0.8 mm (I-CAR's typical outer-panel thickness, the Klokkerholm snippet). Measure at a cut edge. With 0.6 mm (0.023 in) wire this is at the bottom of Miller's sheet range, so run coupons on donor offcuts.

### Gaps
- BMW's E46 TIS 41 sectioning procedure (permitted cut lines, joint type, weld schedule) was not accessible (newTIS behind Cloudflare). No forum reproduction was found before the search budget ran out.
- No factory spot-weld pitch for the arch lip: count the drilled spots on the donor and match them.

---

## Q4. Rear doors, gaps, bumper and skirts

### Cited findings
- **BMW-prototype style (door stock):**
  - Petroyle: "one of the most difficult bits is actually the rear arches because they don't go into the doors… BMW never have done that… probably because they didn't wanna make a different rear door… we would finish the arch before the door exactly the same as the concept car" [transcript, manual subtitles] [Hagerty (2026), 07:40](https://www.youtube.com/watch?v=--YbwCS4F_g&t=460s), [08:00](https://www.youtube.com/watch?v=--YbwCS4F_g&t=480s), [08:40](https://www.youtube.com/watch?v=--YbwCS4F_g&t=520s).
  - Perfects Auto on Petroyle: "rear quarters… remain steel, shaped and welded to match the BMW concept's arches, while the rear doors stay standard to avoid expensive new tooling" [read] [Perfects Auto](https://perfectsauto.xyz/driving-e46-m3-touring.html).
  - Renner car: "some people… continue the quarter panel to here and that's not correct so you got to be very careful how do you contour the door… this is the stock touring door" [transcript] [Larry Chen (2025), 05:20](https://www.youtube.com/watch?v=YM2gyQOaJCk&t=320s).
- **Door flared or extended:**
  - M346 flared with a 2x4 after marking start and stop points; this opened the gap "by about 3 to 4 mm". He rebuilt the gap with 3M panel bond "38315" against a 4 mm card wall, "about a 90 minute work time", 24 h cure, about 2 h of sanding to feeler gauges. He rejected welding the leftover flare caps to the door because of "a bulbous effect" [transcript] [Pt 22 (2025), 00:20](https://www.youtube.com/watch?v=c6PDOLC94K0&t=20s), [01:00](https://www.youtube.com/watch?v=c6PDOLC94K0&t=60s), [04:40](https://www.youtube.com/watch?v=c6PDOLC94K0&t=280s), [05:40](https://www.youtube.com/watch?v=c6PDOLC94K0&t=340s), [22:20](https://www.youtube.com/watch?v=c6PDOLC94K0&t=1340s).
  - His friend "Lauren… flares the door first and then he puts on the quarter panel" [01:00](https://www.youtube.com/watch?v=c6PDOLC94K0&t=60s). Probably the same San Diego "Lauren" who rebuilt the Bimmer Invasion car's quarters [inference].
  - Calvin: the door section welded in so the door "flicks out"; the straight door rubbing strip must be modified; a plastic side skirt was heated and bent out [transcript] [PT9, 02:20](https://www.youtube.com/watch?v=-BMrhOr8fdg&t=140s), [04:20](https://www.youtube.com/watch?v=-BMrhOr8fdg&t=260s), [11:20](https://www.youtube.com/watch?v=-BMrhOr8fdg&t=680s).
  - Automotive Anatomy: "the rear and the door arch… the most difficult… we have the door flare out to match the rear door arch" [transcript] [12:00](https://www.youtube.com/watch?v=QU8BE8J2x84&t=720s).
  - Ultimate Klasse: "seamlessly butting up to the rear doors… the M3 rear quarters are quite long and it took some serious skill and fabrication to work them into the rear doors" [read].
  - German forum (2006): "denk daran das du ein Problem mit den hinteren Türen bekommen wirst. Da diese im Weg sind. Also must du die Türe auch etwas verbreitern" (remember the rear doors will be a problem because they're in the way, so you'll have to widen the door a bit too). A second poster planned to weld the M3 side panel "bis über die hinteren Türen" (right across the rear doors) and "den Türspalt wieder aufsägen im Bereich der geweiteten Radläufe" (saw the door gap open again around the widened arches) [read] [bmw-syndikat 57244](https://www.bmw-syndikat.de/bmwsyndikatforum/topic57244_M3_hintere_Seitenwaende_in_eine_Limo__3er_BMW_-_E46.html).
- **Rear bumper:**
  - M346: relief cuts in the Touring bumper's corners "so that it'll follow the contour of the M3 flare because originally… the stock touring bumper doesn't come out this wide" [transcript] [rear bumper video, 62:40](https://www.youtube.com/watch?v=R2a68pcDo38&t=3760s). The bumper had to move in and forward to meet his flares [Pt 14, 58:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=3520s).
  - M3projekts: the wide M3 rear fenders are needed "with the M3 bumper corner" [transcript] [Ep3, 03:00](https://www.youtube.com/watch?v=TT0sd2JB5dY&t=180s).
  - Ultimate Klasse: the Touring bumper "was given the proper widening treatment with plastic weld to line up with the newly fattened arches" [read].
- **Side skirts:** coupe skirts are "a few mm shorter" than the Touring's; the white clips must be replaced with black M3 ones [transcript] [M3projekts Ep3, 06:00](https://www.youtube.com/watch?v=TT0sd2JB5dY&t=360s). M3 skirts 51717890011/012 and intermediate pieces 51717890511/512 are common to both M3 bodies (prior note).

### Inferences
- **The step at the shut line, door left stock** (Q1, item 7): ≈ 11–20 mm [scaled]. Three ways to deal with it:
  - (a) beat the M3 nose in over the last 60–100 mm before the shut line so it lands flush with the door (BMW and Petroyle);
  - (b) flare the door's rear edge out by the same amount (M346; Lauren flares first, then fits the quarter);
  - (c) weld the M3 nose across the shut line and re-cut the gap from a template (Tracks and Trails; the 2006 German forum idea).
- **Bumper corner widening.** The plan-view M3 − Touring difference 250–450 mm behind the axle (≈ +29–32 mm, falling to +13 mm; Q1, item 3) is the best available estimate of how far the Touring bumper's corner must come out to follow the M3 arch [scaled; inference]. Trial-fit the bumper before final welding (plan step 8).
- **Gap target.** Restore the car's own baseline shut gap, measured with feeler gauges at three marked points in Phase 0. M346 judged against his "stock gap" on the unaltered upper part of the same door. No BMW E46 gap specification was found [Gap].

### Gaps
- BMW's E46 panel-gap specifications (TIS 41 00) were not accessible.
- No published measurement of the door-edge flare amount: estimate it from the scaled data, then measure on the car.

---

## Q5. Templates and measurement

### Cited findings
- BMW TIS ride height, as in Q1: measure from the bottom middle of the rim flange to the lower edge of the wheel arch, in normal position; tolerance ±10 mm normal and 2 mm design position; left/right within 10 mm normal and 2 mm design [TIS screenshot]. NAM3 #11: "Measure as indicated by TIS. You will never be able to accurately place the tape in the exact center of the rim" [read].
- Tracks and Trails' door template: "The cardboard's really just there to keep the general shape. The tape outline's doing most of the work"; it "held its shape remarkably well. That means the line's going to be accurate" [transcript] [16:20](https://www.youtube.com/watch?v=nADBRfX9DqY&t=980s), [21:40](https://www.youtube.com/watch?v=nADBRfX9DqY&t=1300s).
- M346: with the rear bumper on, mock up "so we can start lining things up"; the fuel filler circle and a body line give alignment references [transcript] [Pt 14, 25:40](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1540s), [26:00](https://www.youtube.com/watch?v=4_LqrbAlNmw&t=1560s).
- German forum advice: measure the arch ("Radhausmaße vermessen", measure the wheel-arch dimensions) before buying wheels [snippet, e39-forum; **another model**].

### Inferences: a measurement scheme
- **Level datum.** Support the shell on the four jacking pads. Level the sill pinch welds side to side and fore and aft with a digital level (record the readings). Set the hub heights with the springs out (README mock-up).
- **Centre line.** Drop plumb bobs from matching left and right points (for example the centres of the four rear subframe mounting bolts, on the axle carrier panel 41117000246 that both cars share, and the front subframe bolts). Mark the midpoint of each pair on the floor and snap a chalk line.
- **Reference plane.** Set a cross-line laser parallel to the centre line, at, say, 950 mm, beside each rear wheel. Measure laser-to-skin at every 100 mm station along the arch, at three heights: the lip, the crown + 100 mm, and the crease −30 mm. That gives the plan-view and section offsets in the tables below on your own car. **Pass:** left and right within ≤ 3 mm.
  - The 3 mm is my suggestion. BMW's design-position ride-height tolerance is 2 mm L/R, and body-measuring practice is about ±2–3 mm. It is not a BMW body figure.
- **Templates.**
  - Cardboard or 3 mm hardboard section templates (profile-gauge copies) at stations −400, −300, −150, 0, +150, +300 and +450 mm (− = ahead of the axle), taken off the donor before you cut and off the Touring before you cut.
  - One side-view template of the cut line, taped on and traced.
  - A tape-and-card template of the door edge if you'll touch it (Tracks and Trails).
- **Tram gauge.** Use it for the body diagonals already in the guide, plus two cross-car checks: lip crown left to right, and crease-at-station-0 left to right.
- **Full bump.**
  - Remove the spring, jack the hub until the bump stop (M3 33532229777) is fully compressed, and rotate the wheel.
  - Check clearances: tire tread to lip, sidewall to the outer wheelhouse half and lip flange, inner sidewall to the inner half and brake lines.
  - Repeat at your static camber and with the toe link at its limits.
  - **Suggested pass:** ≥ 10 mm to sheet metal at full bump. Not published; no BMW wheel-travel figure was found.

### Gaps
- No published E46 M3 rear wheel-travel or bump-stop length.
- No BMW E46 Touring body dimension sheet was opened.

---

## Q6. Documented builds in detail

| Build | Where, when | Donor / base | Arch method | Door | Time and notes | Mistakes and lessons |
|---|---|---|---|---|---|---|
| **M346 Projects** | Georgia, US; 2024–25 | 2003 M3 convertible / 2004 Touring | Donor skin and inner tub separated; Touring tub lip bent up; M3 tub welded to the shell first; then the skin; M3 filler surround grafted; rocker moon gap plated | Flared with a 2x4 after the quarter; gap rebuilt with panel bond | Metalwork by a visiting metalworker; paint about 4 months | 100% argon at first; accident-damaged donor quarters curled in; corner pulled in after welding the inner tub; heat ripple needed a skim coat |
| **Tracks and Trails** | Ontario, CA; 2026 | 2002 M3 coupe / 2004 325i Touring | Outer skin only; butt weld; lips bonded with panel bond plus a hammered lip; gussets | Flare overlaid on the door; gap re-cut from a template | First welding project; "hours and hours" of sanding | Each panel a different colour pending paint; filler over welds |
| **SOS Customz** | US shop; 2023 | Pre-cut M3 quarters / clapped-out Touring | Joggle (step) with plug holes, full bead, ground; inner structure "lifted up a bit" | Pounded out, not welded | 2 people, about 4 weeks at 40–50 h/week for the whole body conversion | Bent doors needed repair |
| **Calvin's / VRS (UK)** | 2020 | M3 / 2003 330d Touring | Stitch-welded quarters | Door section welded so it "flicks out" | Car not running in 2026 | Rubbing strip and skirt reshaped |
| **M3projekts (HU)** | 2022–23 | M3 convertible / 318d and US 325iT | Fenders cut from the donor with part of the inner edge, spot welds drilled | Flare carried onto the door (NAM3 #106 photos, prior note) | Body shop 4–6 weeks without paint (prior note) | — |
| **Autoalex / Redish (UK)** | 2023–25 | M3 coupe / 330i Touring | M3 panels, CSL-style inner arches | "Section in the door" | — | Rotten M3 inner arches |
| **Bimmer Invasion car** | San Diego | M3 / Touring | Redone with new M3 quarters (by "Lauren") | Doors "pulled a little bit" | — | First quarters "understated" |
| **Renner (Larry Chen)** | US; 2025 | Running M3 / Touring | Outer quarter, inner quarter and inner structure fabricated in metal | Door contoured, not continued | Show build | — |
| **Petroyle** | UK; 2026 | Coupes / Tourings | Steel quarters shaped to the concept | Doors stock (concept) | Production series | — |
| **Ultimate Klasse (S. Moulton)** | US; 2013 | Salvaged M3 / 325i Touring (ZHP-built) | M3 quarters welded | "Worked into the rear doors" | Bumper plastic-welded wider | — |
| **Eurotuner (H. Schwantner)** | Berlin; 2019 | M3 parts / 2005 320d Touring | Arches welded in | "Türen angepasst" (doors adapted) | 10×19 ET25 with 255/30ZR19 at the rear | — |
| **Sub2club track wagon** | San Diego; 2022 | Touring | HARD rivet-on flares, cut | — | 18×10.5 wheels, 285 tires | Not steel |

Sources for the rows are cited in Q2–Q4. Prior-round notes cover Tenza (no flares; rubbing on M3 springs) and Project BMW (no arches). Rows without a link here are from the prior notes or the guide.

**Gaps:** written UK, German and Dutch build threads with measured arch work were mostly behind bot checks (e46fanatics, m3cutters, Driftworks). The e46-forum.de thread "Radhausblech/Einschweissblech E46 Touring hinten" (wheelhouse panel / weld-in panel, E46 Touring rear) loaded [read, HTTP 200] but I didn't analyse it before moving on. It is about Touring wheelhouse repair panels, worth a look. [e46-forum.de](https://www.e46-forum.de/forum/thread/43947-radhausblech-einschweissblech-e46-touring-hinten/).

---

## Guide-ready

### A. Cut-and-weld plan, in order

Numbers marked **[P]** are published (BMW or vendor), **[M]** are to be measured on your cars, and **[E]** are estimated from the scaled drawings or inferred.

1. **Record before anything moves (Phase 0/1).**
   - Touring: shut gaps at three marked points per door (feeler gauges) [M]; laser-to-skin offsets every 100 mm from 400 mm ahead of the axle to 500 mm behind it, at the lip and at crease −30 mm, both sides [M]; body diagonals (README) [M].
   - Donor: the same offsets, plus TIS rim-flange-to-arch at the rear.
   - **Pass for the donor before you trust it as a reference:** 587 ± 10 mm on 18-inch wheels, left/right within 10 mm, in normal position. Unloaded it will read higher; BMW's height figures differ by 9 mm, unloaded against loaded [P].
   - Section templates at the seven stations of Q5 (400, 300 and 150 mm ahead of the axle; at the axle; 150, 300 and 450 mm behind it), on both cars [M].
2. **Mock-up (README):** M3 axle, final dampers and wheels, springs out, hubs set. Run the full-bump check (Q5). Set the **target lip** at donor rim-flange-to-arch ± 3 mm, with lateral offsets matching the donor's at each station ± 3 mm [M].
3. **Choose the door treatment now.** Stock door (BMW style): the M3 nose must come in ≈ 11–20 mm over its last 60–100 mm [E]. Flared door: the door's trailing edge comes out by the same amount [E].
4. **Mark the cut lines on the Touring** (template in C1):
   - top ≈ 500–515 mm above the hub, at least 25 mm below the crease [E/M];
   - rear vertical ≈ 550–600 mm behind the axle, at least 100 mm ahead of the tail-lamp's leading edge [E/M];
   - front 25–40 mm behind the shut line, parallel to it, down to the sill flange [M].

   **Check:** the line runs on surfaces where the donor and Touring templates agree within ≤ 1 mm. Move it if not.
5. **Prepare the donor section.**
   - Cut 40–50 mm oversize.
   - Drill the spot welds (count them) and separate the skin from the inner arch panel (coupe: interior side frame 41217890677/678; convertible: inner lateral trim panel 41217894553/554 or interior side frame) [P/M]. Keep as much of the inner arch flange as you can.
   - Strip seam sealer and zinc where you'll weld.
   - **Check:** no rust in the U-channel (Redish), and the shape matches its templates.
6. **Open the Touring.**
   - Drill the arch-lip spot welds and remove the skin inside the line, leaving the outer wheelhouse half (41218242355/356) in place.
   - Grind the sound-deadening mat back 25 mm (M346).
   - Fuel system out first (README).
7. **Inner arch first.** Either graft the donor's arch flange to the Touring's outer half, or extend the outer half's flange outward with a fill strip by the offset table (≈ 20 mm at the crown; up to 25–30 mm from 200 to 350 mm behind the axle, but from about 200 mm behind the axle rearward, below the bumper line, the drawn outline is the bumper corner, so take the under-bumper value from the donor) [E/M].
   - Tack, check with the skin dry-fitted, then plug-weld or stitch and cool.
   - Weld-through primer on the faying faces.
   - **Check:** templates at the axle and 300 mm behind it still read as before; corner not pulled in (M346's lesson).
8. **Fit the skin.**
   - Trim to a 0.8–1.0 mm butt gap (about the panel thickness), or form a 0.8 mm joggle if you choose the lap.
   - Hold with clecos or butt-weld clamps every 75–100 mm.
   - **Checks:** flush across the seam ≤ 0.5 mm before welding [E: suggested]; lip at target ± 3 mm; door opens and closes; bumper corner trial-fitted.
9. **Tack** the top seam first (centre, then ends, then halves) to a final pitch of 25–30 mm (guide: 25–40 mm), then the rear seam, then the front seam. Re-check gaps and flushness.
10. **Lip joint.** Plug-weld the skin's lip flange to the inner flange through 6 mm holes (I-CAR thin-to-thin) at the factory spot positions [P: hole size], or bond and plug every second position.
    - **Pass:** coupon tearout 5–10 mm (I-CAR) [P].
11. **Stitch.** Use 10–15 mm spot-stitches between tacks in a skip pattern (see C4). Move seam to seam and side to side. Let each area cool to hand-warm before welding next to it [E: suggested]. Overhead: settings −10–15% (Miller) [P].
12. **Close the sill/dogleg gaps** with template-cut gussets (Tracks and Trails, M346).
13. **Dress.** Grind with 80-grit flap discs without thinning the panel, then planish (hammer on dolly) to relieve shrinkage.
    - **Check:** templates at all stations within ≤ 1 mm; laser offsets left/right within ≤ 3 mm; body diagonals unchanged within ±2 mm [E: suggested]; door gaps back to the Phase 0 readings.
14. **Seal and protect.** Brush seam sealer into the lip channel (Redish two-stage). Seam-seal the inside of every joint, epoxy-prime (Tracks and Trails), and cavity-wax the quarter (Tracks and Trails Wool Wax, Redish).
    - **Check:** the lip is a sealed double skin all round.
15. **Door edge** if flared: rebuild the gap with panel bond against a 4 mm card wall, cure 24 h, sand to feeler gauges (M346).
16. **Filler:** skim only. Keep the arch's definition (M346's painter).

### B. Tables

**B1. Steel: part numbers and 2026 prices**

| Part | Number(s) | Body | Weight | Price seen (Oct 2026) | Notes |
|---|---|---|---|---|---|
| M3 coupe rear side panel L/R | 41217890689 / 41217890690 | M3 coupe, CSL | 14.5 / 14.4 kg | **£4,420 each** (R44, UK, "available"); **€6,518.67 each** (eStore-Central) | Panel runs to the roof rail |
| M3 convertible rear side panel L/R | 41357894541 / 41357894542 | M3 convertible | 11.5 kg | **€1,979.88 each** (eStore-Central); US $2,390–2,610 [snippet, prior note] | Whole arch and filler opening |
| M3 coupe interior side frame L/R | 41217890677 / 41217890678 | M3 coupe, CSL | 5.7 / 5.6 kg | €1,205.48 each | Probably Redish's £990 "inner arch panel" [inference] |
| M3 convertible inner lateral trim panel L/R | 41217894553 / 41217894554 | M3 convertible | 4.8 kg | €141.50 / €131.82 | Outer wheelhouse position in the ETK diagram; candidate inner arch [inference] |
| M3 convertible interior side frame L/R | 41217894557 / 41217894558 | M3 convertible | 33.5 kg | €959.57 each | Large; arch flange sits on it |
| Wheelhouse inner half L/R | 41148231757 / 41148231758 | All, incl. US 325i Touring | 3.6 / 5.4 kg | €284.46 each | Same part on both cars |
| Touring wheelhouse outer half L/R | 41218242355 / 41218242356 | Touring | 1.8 / 2.0 kg | €29.83 / €189.75 | The part you extend |
| Touring rear side panel L/R | 41218242347 / 41218242348 | Touring | 8.4 / 8.3 kg | €1,699.87 / €1,795.28 | Reference |
| M3 fuel filler flap (primed) | 51172695524 | Both M3s | 268 g | €45.06 | Touring flap 51178208246 |
| Filler flap hinge | 51178151955 (Touring and M3 convertible); 51172695527 (M3 coupe) | — | 50 g / 31 g | €12.99 (51178151955) | Use your own Touring hinge with a convertible-pattern flap |
| Tank filler pot | 51718208646 | Touring **and** both M3s | 100 g | €18.57 | Common part |
| Rear bump stop (M3) | 33532229777 | M3 | 70 g | — | For the full-bump check |
| HARD ABS rear flares (alternative) | — | E46 sedan and Touring | — | $294 list / $264.60 sale | Rivet-on; door pieces separate |

**B2. Dimensions** (rear hub centre = origin; X + forward, Y + up; mm)

| Quantity | Value | Basis |
|---|---|---|
| Width, M3 / coupe / Touring | 1,780 / 1,757 / 1,739 (70.1 / 69.2 / 68.5 in) | [P] BMW |
| Rear track, M3 / Touring | 1,524 (60.0 in) / 1,483 (58.4 in); ST041: M3 +47 mm vs E46/2 | [P] |
| Wheelbase, M3 / Touring | 2,731 / 2,725 (107.5 / 107.3 in) | [P] |
| M3 TIS rim-flange-to-arch, rear | 587 (18 in), 600 (19 in); ±10; L/R ≤ 10 (2 in design position) | [P] TIS |
| M3 TIS rim-flange-to-arch, front | 605 (18 in), 619 (19 in) | [P] TIS |
| Hub-to-arch-edge, M3 rear | ≈ 341 (flange reading) or 358 (bead-seat reading); drawing 348 | [E] |
| Arch edge radius (front at hub height / top / rear at hub height) | M3 ≈ 364 / 348 / 379; Touring ≈ 355 / 340 / 383 | [E ±10] |
| M3 flare length (plan view) | X ≈ +420 → −500 (ramp X +420 to +300; full X +300 to −350; fade X −350 to −500). Behind X ≈ −150 to −220 and below the bumper line, the outline is the bumper corner, not steel | [E ±30 in X] |
| M3 flare boundary line, side view | Y ≈ +475 at the top; meets the bumper line at X ≈ −300, Y ≈ +305 | [E] |
| Shoulder crease height (both) | Y ≈ +540 | [E ±15] |
| Bumper top line (both) | Y ≈ +300–310 | [E ±20] |
| Touring tail-lamp front edge / lower edge | X ≈ −700 / Y ≈ +360 | [E ±20] |
| Touring door/arch junction | X ≈ +300 to +350, Y ≈ +150 to +250 | [E ±50]; measure |
| Lip-channel depth (U-channel), standard / CSL / Redish CSL-style | ≈ 15 / ≈ 4 / ≈ 8 | [P] Redish |
| Outer skin thickness | ≈ 0.7–0.8 (measure) | [E] I-CAR typical; Klokkerholm snippet |

**B3. Consumables and tools** (as used by the builds; prices not checked, search budget exhausted)

| Item | Used by | Spec / note |
|---|---|---|
| MIG wire ER70S-6, 0.023–0.024 in (0.6 mm); 75/25 Ar/CO2 | Miller; M346 (not 100% Ar) | Coupons on donor offcuts |
| Weld-through (zinc) primer | M346 (3M weldable zinc), Tracks and Trails, Redish | On faying faces only; grind it off where the arc strikes |
| Zinc-phosphate metal prep | Redish | Before sealing the lip |
| 2K epoxy primer | Tracks and Trails | Over bare metal before filler |
| Panel-bond adhesive | Tracks and Trails (lips), M346 3M "38315" (door gap; ≈ 90 min working time, 24 h cure) | Small non-flexing areas |
| Seam sealer (brushable and sprayable) | Redish (two-stage), M346, Tracks and Trails | Fill the U-channel |
| Cavity wax (lanolin "Wool Wax" or similar) | Tracks and Trails, Redish | Inject after paint |
| Rust-preventive paint (POR-15) | Redish | Optional |
| BMW multi-purpose filler; polyurethane glaze | Calvin / VRS | Skim only |
| Heat-shield gel | Redish | Protects paint near welds |
| Spot-weld cutter, hole punch (6 mm), panel flanger (joggle), clecos, butt-weld clamps, hammer and dollies, profile gauge, cross-line laser, plumb bobs, tram gauge, feeler gauges, infrared lamp | Builds and inference | — |

### C. Diagram-ready data (all coordinates relative to the rear hub centre; X + forward, Y + up; mm; **[E]** = estimated ±5–10 mm unless noted)

**C1. Side-view cut template (right side; mirror for the left)**

*Existing arch edge (both cars):* (+364, 0), (+334, +122), (+307, +177), (+274, +230), (+228, +272), (+175, +303), (+120, +329), (+61, +344), (0, +348), (−61, +344), (−119, +327), (−176, +305), (−227, +271), (−273, +229), (−308, +178), (−339, +123), (−362, +64), (−379, 0). [E, from the BMW M3 drawing; the Touring is within ±10.]

*M3 flare boundary (dashed "bulge" outline):* (+315, +376), (+244, +422), (+165, +454), (+83, +473), (0, +475), (−82, +463), (−158, +435), (−227, +393), (−285, +339), (−306, +306), then along the bumper top line to (−450, +300). [E]

*Plan-view flare start/end markers (for a top-view inset):* start ramp at X = +420 (0 mm proud) → X = +300 (≈ +20 proud); full to X = −350; fade to X = −500 (≈ +10). [E]

*Reference lines:* crease Y = +540 (X +350 to −700); bumper top Y = +305; tail-lamp front edge X = −700 (from Y = +360 up); door/arch junction near (+330, +200) [E ±50], door trailing edge running up to the beltline at Y ≈ +640.

*Recommended outer-skin cut line (polyline):*
- A (+300, +505): front top, 25–40 mm behind the shut line [M];
- B (−560, +505): rear top;
- C (−560, +250): rear bottom, 50 mm under the bumper top, hidden;
- D: down the front edge from A, parallel to the shut line, to the sill flange at about (+300, −40) [M].

Donor cut line: the same polyline offset 40–50 mm outward.

*Inner lip joint:* follows the arch, 0–15 mm inside the edge (the U-channel).

**C2. Cross-section at the axle line (station X = 0; looking forward; right side). Half-width from the car centre line, in mm**

| Height above hub (Y) | Height above ground (≈) | Touring skin | M3 skin | Move-out |
|---|---|---|---|---|
| +345 (arch crown and lip) | ≈ 660 | ≈ 868 | ≈ 890 | **≈ +21** |
| +385 | ≈ 700 | ≈ 861 | ≈ 877 | ≈ +16 |
| +435 | ≈ 750 | ≈ 851 | ≈ 863 | ≈ +12 |
| +465 | ≈ 780 | ≈ 847 | ≈ 853 | ≈ +6 |
| +500 (proposed top joint) | ≈ 815 | ≈ 842 | ≈ 844 | ≈ +2 |
| +525 | ≈ 840 | ≈ 834 | ≈ 832 | ≈ 0 |
| +540 (crease) | ≈ 855 | — | — | 0 |

[E: rear-view silhouettes and the plan view combined; ±5–8 mm.]

*Wheel geometry for the same section:* hub face ≈ 788 from the centre line (README); M3 rim (9J ET26) bead-seat edge 876.3; M3 tire maximum sidewall ≈ 892 [E]; the old Touring 8J ET47 rim edge would be at 842.6.

*Lip channel:* the skin returns inward ≈ 15 mm at the lip and nests over the outer wheelhouse flange; joint plug-welded at the factory pitch [P: depth; M: pitch].

*Inner lip extension needed:* the Touring outer-half flange must move out by the move-out value at each station along the arch: ≈ +21 at the crown; ≈ +16–22 at X +300; ≈ +25–32 at X −150 to −350 (behind the axle) [E]. Behind X ≈ −150 to −220 and below the bumper line (Y ≈ +305), those figures are the bumper corner's outline; the steel lip under the bumper may need less, so measure the donor with its bumper off [M].

**C3. Plan-view offset strip (top view), M3 − Touring half-width, mm** [E]

X: +600 → +7 · +500 → +9 · +400 → +9 · +350 → +16 · +300 → +22 · +200 → +21 · +100 → +21 · 0 → +23 · −100 → +23 · −150 → +25 · −200 → +29 · −250 → +29 · −300 → +31 · −350 → +32 · −400 → +22 · −450 → +13 · −500 → +11 · −600 → +7.

(The +7 to +9 mm ahead of +400 is the coupe-against-Touring body difference. It exists only where the M3 piece covers the door region, which the plan does not take.)

(Behind X ≈ −150 to −220 and below the bumper line, Y ≈ +305, the outline is the bumper cover on both cars. The values from −250 to −450 are therefore mostly bumper corner: use them as the target for widening the Touring bumper, not for the steel. See Q1, item 3.) [inference]

**C4. Weld sequence (outer skin, one side; repeat on the other side between passes)**

Seams (from C1):
- S1: top, A→B, ≈ 860 mm;
- S2: rear, B→C, ≈ 255 mm;
- S3: front, A→D, ≈ 545 mm;
- S4: lip, ≈ 1,150 mm along the arch (plug welds).

1. **Tack order:**
   - S1: centre (T1) → A end (T2) → B end (T3) → midpoints T4, T5 → quarter points T6–T9 → down to a 25–30 mm pitch (≈ 30 tacks).
   - S2: ends, then the middle (≈ 9 tacks).
   - S3: top, bottom, middle, then halves (≈ 18 tacks).
2. **Check** gap, flushness, door and template; adjust before any stitching.
3. **S4 plug welds:** every second factory position first, working from the crown outward alternately front and rear; then fill the rest.
4. **Stitching:**
   - 10–15 mm spot-stitches in the gaps between tacks, in a skip pattern: S1 gaps 1, 5, 9…, then S2 gaps 1, 3…, then S3 gaps 1, 5, 9…, then the other side of the car.
   - Return to S1 gaps 3, 7, 11… only when the first area is hand-warm, then gaps 2, 6, 10…, then 4, 8, 12….
   - No more than ≈ 150 mm of weld per seam per pass [E: suggested].
   - GM's equivalent rhythm on overlap seams is 25 mm welds with 25 mm gaps, then fill [P, another make].
5. **Penetration** visible on the back along every seam (Calvin's body man). Grind and planish after each completed seam, not at the end.

---

## Statements in the guide that these findings correct

1. **Figure 15 caption** (README, "Arch section and wheel offsets"): "…so the outer skin moves out about 25–30 mm and the inner wheelhouse lip is extended to meet it." Diagram 09 labels "≈ 25–30 mm"; diagram 08 labels "M3 arch bulge, about 25–30 mm proud".
   **Correction:** BMW's widths give +20.3 mm per side at the widest point. Scaled from BMW's drawing, the M3 skin moves out ≈ +21–23 mm from 300 mm ahead of the axle to 100 mm behind it (crown and lip ≈ +21), ≈ +25–32 mm from 150 to 350 mm behind it, and fades to ≈ +10 mm by 500 mm behind it and to 0 about 470–530 mm above the hub. Use a profile (table C3), not one figure. From roughly 150–220 mm behind the axle rearward and below the bumper line, the larger figures are probably the bumper corner rather than steel [inference; Q1, item 3].
2. **Phase 6 step 6:** "The new arch sits about 25–30 mm further out" (same correction). And README step 8 of the graft: "The M3 filler pot (51718208646, the same on both M3s) and the flap end up about 25–30 mm further outboard."
   **Correction:** 51718208646 is also the US 325i Touring's filler pot (ETK), and its hinge 51178151955 is the same part as the M3 convertible's. M346 found the filler area "virtually the same width sheet metal wise" on M3 and non-M (Pt 14, 17:00), and the flare fades above ≈ 475 mm above the hub. Expect the pot to move out much less than 25–30 mm; trial-fit it.
3. **Steel sources table:** "New M3 coupe quarter, right 41217890690… \$5,525 for the right ([R44]); no price found for the left".
   **Correction:** R44 is a UK shop pricing in GBP: **£4,420 each** for left 41217890689 and right 41217890690, both flagged available (Oct 2026). \$5,525 was a currency conversion. An EU retailer, eStore-Central, lists **€6,518.67 each**.
4. **Steel sources table:** "New M3 convertible quarter 41357894541/542… About \$2,390–\$2,610 each at US dealers… (unverified)".
   **Add:** €1,979.88 each at eStore-Central (Oct 2026). US prices are still unverified. Add the convertible's **inner lateral trim panel 41217894553/554 (€131.82–141.50)** as a candidate new inner arch flange.
5. **Steel sources table:** "BMW inner wheel-arch panels | Inner arch | £990 each (2025) | … Redish doesn't give the part number".
   **Add [inference]:** this is most likely the M3 coupe interior side frame 41217890677/678 (€1,205.48 each), which carries the M3 arch flange, not the shared inner half 41148231757/758 (€284.46).
6. **Graft step 3:** "One builder cut off the donor quarter's tail-light pocket because the Touring's tail-lights are longer ([vTuned garage – M3 wagon quarter swap (2025), 07:20])". And **step 6:** "Keep welds away from the tail-light pocket if you can, and accept more filler there ([vTuned garage (2025), 09:00])."
   **Correction:** vTuned's video is an **F80 M3 → F31 328i wagon** conversion ("base model 328i… converted everything off of a F80 M3", 2015–2018 generation; transcript 00:00–00:40), not an E46. Drop it as an E46 source.
   For the E46 the scaled drawings put the Touring's tail-lamp front edge ≈ 700 mm behind the axle, beyond the M3 flare's end (≈ 450–500 mm). A rear joint at ≈ 550–600 mm behind the axle never comes near the pocket.
7. **"Where the steel comes from":** "Petroyle's cars were reported with steel rear quarters ([Rush]), but in 2026 Petroyle said it is moving to carbon panels for production ([Hagerty…]), and one review says its car's arches are carbon ([candyshowroom…])."
   **Correction:** in Hagerty (Apr 2026), Gregg's "carbon wings" are the **front wings (fenders)**; production cars add carbon sills, rear bumper and options. BMWBlog (9 Apr 2026): "all the Touring-specific panels — rear bumper, side sills, boot floor, front wings — are made in carbon fiber. The quarter panels stay in steel". Perfects Auto: the rear quarters "remain steel, shaped and welded to match the BMW concept's arches, while the rear doors stay standard". candyshowroom's "arches" claim conflicts with both.
8. **Measure-and-mock-up section and Phase 6 step 1:** "We found no BMW ride-height figure, so take the targets from your donor." / "No BMW ride-height figure was found for this car".
   **Correction:** TIS 33 00 and 31 00 give E46 M3 ride height as rim flange (bottom middle) to the lower edge of the wheel arch, in normal position: **rear 587 mm on 18-inch and 600 mm on 19-inch rims; front 605 and 619 mm**; tolerance 10 mm; left/right 10 mm normal, 2 mm design position (TIS screenshots on NAM3, Jul 2024). Use them to vet the donor and to check the result. The Touring's own figure is still unverified (snippet).
   Also correct the Open questions (Body/Chassis) line "An E46 ride-height specification…" to: found for the M3; the Touring is still open.
9. **Welding settings, panel table:** "Your floor, RACP and arch skins | Not published; this guide assumes roughly 0.8–1.2 mm (estimate)".
   **Refine for the arch skin:** expect about 0.7–0.8 mm (I-CAR: typical outer panels "in the range of 0.70 mm"; a forum snippet on 0.8 mm Klokkerholm E46 quarter repair panels). LBL's 1.2 mm sections would be thicker than the skin they join. Still measure at a cut edge.
10. **Figure 14 caption:** "The bulge's front edge reaches the rear door's shut line: stop there, as BMW did, or reshape the door edge."
    **Add numbers:** the Touring's rear door forms the front of the arch opening. Its trailing edge meets the arch at about the 10 o'clock position, ≈ 300–350 mm ahead of the axle (estimate; measure). The M3 flare begins ≈ 380–420 mm ahead of the axle, so its first 50–100 mm lies on the door, and at the shut line the M3 surface stands ≈ 11–20 mm proud of the stock door. That is the amount to beat in, or to flare the door by.
11. **Graft step 2:** "Lay out the cut line on your quarter a little outside the donor's bulge, so the joint sits on flat panel".
    **Make it measurable:** the flat band between the M3 bulge's edge (≈ 475–490 mm above the hub) and the shoulder crease (≈ 540 mm) is only ≈ 50 mm. Put the top joint ≈ 500–515 mm above the hub and confirm with section templates (≤ 1 mm disagreement). Put the rear joint ≈ 550–600 mm behind the axle.
12. **"Two M3 quarters" / "Almost certainly the same arch":** "Nobody has published a measured comparison."
    **Partial answer [scaled]:** BMW's own dimension drawings of the M3 coupe and convertible show the same arch opening (within 2–9 mm) and the same plan-view flare (within 3–7 mm after a uniform scale offset), except possibly 350–400 mm behind the axle. That is still an estimate; confirm with templates.
13. **Massachusetts title paragraph:** "Ask the RMV Title Division whether grafting the donor's arch steel or trunk floor counts. New BMW panels avoid the question".
    **Add:** a fully new-BMW arch route exists and is affordable at EU prices: convertible skin 41357894541/542 plus inner lateral trim panel 41217894553/554, ≈ €2,120 per side. The statute (c. 90D §20F) is framed around "welding together or connecting the frames or unit bodies of two or more motor vehicles", and its affidavit asks for "the location of the point of connection or weld joint of the two or more vehicle frames".

---

## What's still open
- Touring-specific BMW body data: TIS 51 00 dimensions, TIS 41 sectioning procedure, gap specifications, ride height.
- US 2026 prices and stock for 41357894541/542, 41217894553/554 and 41217890677/678.
- Whether 41217894553/554 carries a usable M3-width arch flange.
- The real lip-to-tire offsets on a donor, and the shut-line/arch junction on the target car (both to be measured).
- E46 M3 rear wheel travel and bump-stop length.
- How far the M3's steel and arch lip move out under the rear bumper (from about 150–220 mm behind the axle rearward). The drawings show only the bumper there; measure a donor with its bumper off.
- LBL Panels' range; the e46-forum.de Touring wheelhouse thread (loaded, not analysed).
