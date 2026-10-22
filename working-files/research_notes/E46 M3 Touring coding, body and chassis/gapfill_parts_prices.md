# Gap-fill: parts-catalog facts, vendor data and prices

Researcher: `parts`. Date: 22 October 2026. Scope: the nine gaps in the gap-fill brief, in priority order, against the round-4 notes `rear_arches.md`, `rear_floor_exhaust.md`, `suspension_touring_weight.md`, `fuel_system_fit.md`, `cooling_ac.md` and `front_axle_brakes_abs.md`.

**Evidence tags.** [read] = I fetched the page, its embedded product data (JSON) or the PDF text and read it. [image] = my reading of a catalog drawing, part drawing or photo. [snippet] = seen only in a search-result summary; the page itself was blocked or not opened. Inferences and arithmetic are labelled **(inference)** or **(arithmetic)**.

**How prices were read.** BMWPartsDeal pages embed a `partInfo` record (price, list price, shipping line, status flag) and a schema.org `availability` value; I parsed those from the saved HTML. Every BMWPartsDeal page below showed "Ships in 1-3 Business Days" and `InStock`, except where stated. That is the dealer's display, not proof of stock.

Web searches used: 20 of 30.

---

## Summary

| Gap | Status | Answer in one line | Best source |
|---|---|---|---|
| 1. US prices and stock | **Closed** (US prices); second dealer **narrowed** | BMWPartsDeal: M3 convertible side panel 41357894541/542 \$2,105.60 each; inner lateral trim panel 41217894553/554 \$127.54/\$118.80; coupe interior side frame 41217890677/678 \$1,311.70 each; M3 coupe side panel 41217890689/690 \$6,932.63 each; floor \$763.61 and reinforcement \$88.22 re-confirmed there; no second US dealer was reachable, eStore-Central (EU) lists €717.97 and €81.79 | [BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-left_rear_side_panel-41357894541.html) [read] |
| 2. Inner panel flange | **Narrowed** | BMW's catalog drawing shows 41217894553 as the inner quarter panel with the arched outer wheelhouse half built in, and it is an M3-only replacement for the non-M convertible's 41217022593, at the same 4.8 kg; that points to an M3-width arch, but nothing says so outright | [ETK, M3 convertible wheelhouse](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/) [read, image] |
| 3. LBL Panels | **Still open** | No website, listing or company page found (two searches, domain checks) | — |
| 4. Springs | **Closed** (part numbers); rates and M3-axle Touring kits **still open** | 2003 manual 325i Touring: front 31331093068 (standard) or 31331093082/083 or 084/085 (sport); rear 33536750756/758/759/760 (standard) or 33536750250 or 33531095714 (sport). M3 coupe front 31332283130, convertible 31332282332; rear coupe 33532283135/136/137, convertible 33532283137. No published OEM rates; no Touring kit for an M3 axle | [FCP Euro fitment notes](https://www.fcpeuro.com/products/bmw-front-coil-spring-31331093068) [read] |
| 5. Damper lengths | **Closed** (Bilstein equivalents); fit **narrowed** | Bilstein B4 non-M rear 19-103150: 370–618 mm; B4 M3 rear 19-199511: 377–597 mm; B6 non-M 368.5–599 mm, B6 M3 367.5–593.5 mm; all 12 mm lower eye and stem top | [ShockWarehouse (Bilstein data)](https://www.shockwarehouse.com/products/bilstein-19-199511-rear-b4-oe-replacement-bilstein-touring-class-shock-absorber-bmw-m3) [read] |
| 6. Fuel | **Narrowed** | Pipe sets and purge lines priced; both tanks share the pump-flange seal and screw cap, so the "sleeve" is probably the M3 baffle (inference); connector sizes, purge-line mating, flow ratings and sender curves still open | [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/) [read] |
| 7. Cooling | **Narrowed** (pusher fan, X82); **closed** (which brackets) | M3 holder 17112229108 carries both the expansion tank and the secondary-air pump; the only M3-only welded brackets nearby are 41147894115/116 "secondary air pump bracket", absent from the US 325i Touring; manual non-M E46s have only the shroud fan (forum snippet) | [ETK, M3 air pump](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/emission_control_air_pump/) [read] |
| 8. Floor and exhaust | **Narrowed** (canister, heat shield); muffler size **still open** | Canister holder sits on four M6 studs (four self-locking nuts); rear-silencer shield fixes with flanged nuts on body studs; no published muffler dimensions | [ETK, M3 EVAP](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/) [read, image] |
| 9. Front axle | Tooth count **still open**; thrust plate **narrowed** | Both hubs carry their own ABS rings (M3 31222229501 = FAG 805387; Touring 31226757024 = FAG 805349); no count published; ETK and ST041 show the M3 plate is broader at the front, but not where the four extra screws thread in | [FCP Euro](https://www.fcpeuro.com/products/bmw-wheel-hub-assembly-z4-m3-oem-31222229501) [read]; [ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear.pdf) [read, image] |

Side finding: the RACP repair insert 41117000246, an open question in the guide, is marked **"This part is discontinued"** at BMWPartsDeal (last price \$1,304.68, list \$1,564.82) [read] ([BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-repair_part_insert_rear_axle_support-41117000246.html)).

---

## Gap 1. US prices and stock in 2026

### Cited findings

**BMWPartsDeal (US dealer site, South El Monte, CA), 22 October 2026** [read]. Prices, list prices, the item weight the site prints, and fitment as the site gives them:

| Part | Number | Price (list) | Site's fitment | Link |
|---|---|---|---|---|
| M3 convertible rear side panel, left / right | 41357894541 / 41357894542 | **\$2,105.60 each** (\$2,561.00) | 2001–2006 M3 Convertible | [L](https://www.bmwpartsdeal.com/parts/bmw-left_rear_side_panel-41357894541.html), [R](https://www.bmwpartsdeal.com/parts/bmw-right_rear_side_panel-41357894542.html) |
| M3 convertible inner lateral trim panel, left / right | 41217894553 / 41217894554 | **\$127.54** (\$174.63) / **\$118.80** (\$162.66) | 2001–2006 M3 Convertible | [L](https://www.bmwpartsdeal.com/parts/bmw-left_inner_lateral_trim_panel-41217894553.html), [R](https://www.bmwpartsdeal.com/parts/bmw-right_inner_lateral_trim_panel-41217894554.html) |
| M3 coupe interior side frame, left / right | 41217890677 / 41217890678 | **\$1,311.70 each** (\$1,595.39) | 2001–2006 M3 Coupe | [L](https://www.bmwpartsdeal.com/parts/bmw-left_interior_side_frame-41217890677.html), [R](https://www.bmwpartsdeal.com/parts/bmw-right_interior_side_frame-41217890678.html) |
| M3 coupe rear side panel, left / right | 41217890689 / 41217890690 | **\$6,932.63 each** (\$8,432.01) | 2001–2006 M3 Coupe | [L](https://www.bmwpartsdeal.com/parts/bmw-left_rear_side_panel-41217890689.html), [R](https://www.bmwpartsdeal.com/parts/bmw-right_rear_side_panel-41217890690.html) |
| Rear wheelhouse inner half, left / right (shared with the Touring) | 41148231757 / 41148231758 | \$302.56 each (\$359.78) | E46 range incl. 325i Wagon | [L](https://www.bmwpartsdeal.com/parts/bmw-rear_left_wheelhouse_inner_half-41148231757.html), [R](https://www.bmwpartsdeal.com/parts/bmw-rear_right_wheelhouse_inner_half-41148231758.html) |
| M3 trunk floor | 41127895619 | **\$763.61** (\$942.03), unchanged from round 4 | M3 Convertible, Coupe | [link](https://www.bmwpartsdeal.com/parts/bmw-trunk_floor-41127895619.html) |
| Reinforcement, trunk floor front | 51717894229 | **\$88.22** (\$105.20), unchanged | M3 Convertible, Coupe | [link](https://www.bmwpartsdeal.com/parts/bmw-reinforcement_trunk_floor_front-51717894229.html) |
| Rear silencer bracket, rear | 41122494844 | \$27.19 (\$36.00), now shown `InStock` (round 4 had flagged "isNA" in a related-parts list) | M3 | [link](https://www.bmwpartsdeal.com/parts/bmw-rear_silencer_bracket_rear-41122494844.html) |
| Bracket, rear silencer right | 41112493931 | \$71.40 (\$94.55) | M3 | [link](https://www.bmwpartsdeal.com/parts/bmw-bracket_rear_silencer_right-41112493931.html) |
| RACP repair insert | 41117000246 | \$1,304.68 (\$1,564.82); **"This part is discontinued"**, schema `Discontinued`, ordering disabled | E46 range | [link](https://www.bmwpartsdeal.com/parts/bmw-repair_part_insert_rear_axle_support-41117000246.html) |

- The site's own "Item Weight" figures are not BMW's: it prints 1.50 lb for 41217894553, where BMW's catalog says 4.8 kg ([ETK](https://bmwfans.info/parts-catalog/41217894553/)), and 21.4 lb for both the M3 and the Touring rear mufflers [read]. Don't use the dealer weights.
- **Second dealer.** No second US dealer page was reachable (see Sources). eStore-Central (European seller, prices in EUR, "World wide delivery with DHL") lists the M3 trunk floor 41127895619 at **€717.97** and the front reinforcement 51717894229 at **€81.79**, plus the rear silencer brackets 41122494844 €30.38 and 41112493931 €63.25 [read] ([eStore-Central, M3 trunk floor group](https://www.estore-central.com/bmw-parts-catalog/E46-M3-S54/Coupe/Bodywork/Mounting-Parts-For-Trunk-Floor-Panel/)). BMW USA's own shop (shop.bmwusa.com, where shopbmwusa.com redirects) carries accessories and apparel, not body panels [read].

### Inferences

- **(arithmetic)** New-steel arch route with convertible panels: left \$2,105.60 + \$127.54 = **\$2,233.14**, right \$2,105.60 + \$118.80 = **\$2,224.40**, both sides **\$4,457.54**. Coupe route: \$6,932.63 + \$1,311.70 = **\$8,244.33 a side**, \$16,488.66 for both. Add the floor and its reinforcement (\$851.83): **\$5,309.37** for both convertible arches and the floor; \$5,667.08 with the two muffler brackets and the M3 rear-silencer heat shield (\$259.12). All before freight, tax and core charges (none listed); a 2 m side panel will likely ship as oversize freight, which the pages don't price.
- **(inference)** The guide's "about \$2,390–\$2,610 each at US dealers" for 41357894541/542 brackets BMWPartsDeal's list price (\$2,561.00); the selling price is lower. The US price (\$2,105.60) is close to eStore-Central's €1,979.88 (ratio 1.06).

### Still open

- Stock: only an order (or a phone call quoting the part number) proves it. Ask the dealer to confirm stock and freight for the two side panels before you commit to the new-steel route.
- A second US dealer price for 41127895619 and 51717894229: every RevolutionParts-type dealer site tried was behind Cloudflare. A phone quote from any BMW dealer parts counter would settle it.

### Guide impact

**Writers: arches (side panels, inner panels), floor (trunk floor, reinforcement, RACP insert).**

1. README.md:277 (arches), current text: "The right M3 coupe quarter (41217890690) is \$5,525 at R44, October 2026 (…); M3 convertible quarters (41357894541/542) list at about \$2,390–\$2,610 each at US dealers (October 2026, unverified) ([BMW of South Atlanta](…))".
   **Replace those two clauses with** (keep the R44 correction from round 4, and the Redish, LBL and Autoalex sentences as they are):
   > At one US dealer on 22 October 2026, the M3 convertible's rear side panels 41357894541/542 were \$2,105.60 each (list \$2,561.00) and its inner lateral trim panels 41217894553/554, which include the outer half of the wheelhouse, \$127.54 and \$118.80; the M3 coupe's side panels 41217890689/690 were \$6,932.63 each and its interior side frames 41217890677/678 \$1,311.70 each ([BMWPartsDeal: 41357894541](https://www.bmwpartsdeal.com/parts/bmw-left_rear_side_panel-41357894541.html), [41217894553](https://www.bmwpartsdeal.com/parts/bmw-left_inner_lateral_trim_panel-41217894553.html), [41217890689](https://www.bmwpartsdeal.com/parts/bmw-left_rear_side_panel-41217890689.html), [41217890677](https://www.bmwpartsdeal.com/parts/bmw-left_interior_side_frame-41217890677.html)). That makes about \$2,230 a side for new convertible steel and \$8,240 a side for coupe steel, before freight and tax (our arithmetic). Each page said "Ships in 1-3 Business Days"; stock isn't confirmed until you order.
2. README.md:1771–1772 (arches), Steel sources table. **Replace the price cells:**
   - Row "New M3 coupe quarter, right 41217890690 (left 41217890689)": `\$6,932.63 each, list \$8,432.01 ([BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-right_rear_side_panel-41217890690.html), October 2026)` (keep the round-4 R44 £4,420 figure beside it).
   - Row "New M3 convertible quarter 41357894541/542": `\$2,105.60 each, list \$2,561.00 ([BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-right_rear_side_panel-41357894542.html), October 2026)`.
   - **Add rows:**
     `| New M3 convertible inner lateral trim panel 41217894553 (L) / 41217894554 (R) | Inner quarter panel with the outer wheelhouse half (BMW drawing) | \$127.54 / \$118.80 ([BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-left_inner_lateral_trim_panel-41217894553.html)) | Candidate new inner arch flange; see the next section before relying on it |`
     `| New M3 coupe interior side frame 41217890677 (L) / 41217890678 (R) | Inner quarter structure with the arch flange | \$1,311.70 each ([BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-left_interior_side_frame-41217890677.html)) | M3 coupe and CSL only |`
3. README.md:1110 (floor), option 2 row, current text ends: "Redish used it on two Tourings (…). We found no US listing". **Replace "We found no US listing" with:** `\$763.61 (list \$942.03) in the US, with the front reinforcement 51717894229 at \$88.22 ([BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-trunk_floor-41127895619.html), October 2026); €717.97 and €81.79 in Europe ([eStore-Central](https://www.estore-central.com/bmw-parts-catalog/E46-M3-S54/Coupe/Bodywork/Mounting-Parts-For-Trunk-Floor-Panel/))`.
4. README.md:2443–2444 (arches, floor), Open questions: "current US prices for the convertible quarters" and "US availability and prices of the new M3 trunk floor (41127895619) and the RACP repair panel (41117000246)". **Replace with:** `- A second US dealer's price and stock for the M3 floor 41127895619 (one dealer lists it at \$763.61). BMWPartsDeal marks the RACP repair insert 41117000246 "This part is discontinued" (last price \$1,304.68) ([BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-repair_part_insert_rear_axle_support-41117000246.html)); ask a dealer whether a successor exists.`

---

## Gap 2. Does 41217894553/554 carry the M3-width arch flange?

### Cited findings

- **ETK, US M3 convertible, "Rear wheelhouse/floor parts"** [read] ([ETK](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/)): item 12 "Left/Right inner lateral trim panel" 41217894553/554, 4.8 kg each, "Additionally required parts: Pos. 14" (molded part 41217013017 ×2). The part page gives "Production Mar '01 –" and usage only on the E46 M3 convertible, Europe and USA ([ETK part page](https://bmwfans.info/parts-catalog/41217894553/)) [read].
- **The same position on the other bodies** (same group drawing, `2s5a`) [read]:
  - Non-M 325Ci convertible: item 12 is **41217022593/594, also 4.8 kg**, also "Additionally required parts: Pos. 14" ([ETK 325Ci convertible](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/325Ci-M54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/)).
  - Non-M 325Ci coupe: item 10 "interior side frame" **41218242067/068, 5.5 kg**; M3 coupe item 10 is 41217890677/678, 5.7/5.6 kg ([ETK 325Ci coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/325Ci-M54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/), [ETK M3 coupe](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/)).
  - US 325i Touring: item 11 "Wheelhouse rear, outer half" **41218242355/356, 1.8/2.0 kg** ([ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/)).
- **The drawings** [image]: in BMW's group drawing ([2s5a](https://ills.bmwfans.info/2s5a.png)) item 12 is an inner quarter panel whose rear part is the arched outer wheelhouse half, with a flanged lower edge following the wheel opening. BMWPartsDeal's single-part drawing of 41217894553 shows the same shape, and its drawing of 41217890677 shows the coupe's full inner side frame with the arch at its lower rear ([BMWPartsDeal 41217894553](https://www.bmwpartsdeal.com/parts/bmw-left_inner_lateral_trim_panel-41217894553.html), [41217890677](https://www.bmwpartsdeal.com/parts/bmw-left_interior_side_frame-41217890677.html)).
- No seller photo of a real 41217894553 was found: one search on the number returned nothing, and eBay is blocked [snippet: no results].

### Inferences

- **(inference)** In every body, BMW gives the M3 its own number at the panel that forms the outer wheelhouse half: convertible 41217022593 → 41217894553, coupe 41218242067 → 41217890677. The convertible pair weigh the same (4.8 kg), so the M3 part is the same panel changed somewhere; the M3's difference from a 325Ci convertible at the rear quarter is the wider arch. That makes an M3-width arch flange on 41217894553/554 likely, not proven.
- **(inference)** For a Touring, only the arched wheelhouse portion of 41217894553 is useful. The rest is convertible quarter structure, to be trimmed off.

### Still open

- Confirm with the part in hand or a convertible shell: lay the panel's arch flange against an M3 skin, or measure flange-to-centreline on both. At \$127.54, buying one to check is cheaper than any other test.

### Guide impact

**Writer: arches.** README.md:1758, current text ends: "…and the interior side frame (41217894557/558) and inner lateral trim panel (41217894553/554) on the convertible. That is our reading of BMW's diagrams (…), not a BMW statement."
**Add after it:**
> BMW gives the M3 its own part wherever this panel forms the outer wheelhouse: the non-M 325Ci convertible's 41217022593/594 becomes the M3's 41217894553/554 (both 4.8 kg), and the 325Ci coupe's interior side frame 41218242067/068 becomes the M3's 41217890677/678 ([ETK, 325Ci convertible](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/325Ci-M54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/), [ETK, M3 convertible](https://bmwfans.info/parts-catalog/E46-Cabrio/USA/M3-S54/L-N/browse/bodywork/rear_wheelhouse_floor_parts/)). BMW's drawing shows 41217894553 as an inner quarter panel with the arched outer wheelhouse built in ([drawing](https://ills.bmwfans.info/2s5a.png)). An M3-only number on an otherwise identical panel suggests the M3 arch flange, but nobody has confirmed it: at about \$128, buy one and check it against an M3 skin before you plan around it.

---

## Gap 3. LBL Panels

### Cited findings

- Two searches ("LBL Panels E46 rear arch repair panel"; `"LBL Panels" BMW M3 arches`) returned nothing from or about LBL [snippet: no results].
- Domain checks: lblpanels.co.uk, www.lblpanels.co.uk, lblpanels.com, lbl-panels.co.uk, lblpanels.uk and lblmetalwork.co.uk do not resolve [read: DNS failure].
- The only source remains the m3cutters thread the round-4 researcher saw as a snippet (m3cutters blocked). The Wayback Machine was unreachable this session (see Sources).

### Inferences

- None beyond round 4's ("LBL is probably the 'Lawrence' Redish mentions").

### Still open

- LBL's current range and fitment. What would settle it: ask on m3cutters (forum account) or ask Redish Motorsport, who mention using "Lawrence"'s panels.

### Guide impact

**Writer: arches.** README.md:1774, current row: "| LBL Panels (UK) M3 arch sections | 1.2 mm mild-steel arch, standard or full | £225 / £375 ([m3cutters](…), unverified) | Coupe or convertible fitment not stated |". **Replace the Notes cell with:** `Coupe or convertible fitment not stated; no website or current listing found in October 2026, so ask on the m3cutters thread before planning on them`. README.md:2443 ("whether LBL Panels' sections are still sold, and for which bodies") stays open.

---

## Gap 4. Springs: part numbers, rates, Touring kits

### Cited findings

**OE spring numbers from FCP Euro's fitment notes** [read]. FCP's notes cite BMW option codes and say "VIN confirmation required", i.e. they follow BMW's spring table; several numbers can apply to one model, chosen by weight class. Rows below are for manual-gearbox cars.

| Car | Front spring | Rear spring |
|---|---|---|
| 2003 US 325i Touring, standard suspension | **31331093068** ("manual transmission, but without Sports suspension settings (S226A)", 2002–04 Wagon) ([FCP](https://www.fcpeuro.com/products/bmw-front-coil-spring-31331093068); Bilstein B3 36-269013 cross-references it, [FCP](https://www.fcpeuro.com/products/bmw-coil-spring-bilstein-b3-bil-36269013)) | **33536750756/759** (Lesjöfors 4208432: "Up to 9/2003… manual… without S226A"; "From 9/2003… manual") ([FCP](https://www.fcpeuro.com/products/bmw-coil-spring-lesjofors-4208432)); **33536750758** ([FCP, Mubea 90152937](https://www.fcpeuro.com/products/bmw-coil-spring-mubea-90152937)); **33536750760** ([FCP, Mubea](https://www.fcpeuro.com/products/bmw-coil-spring-mubea-33536750760)) |
| 2003 US 325i Touring, sport (S226A) | **31331093082/083** (Lesjöfors 4008441) ([FCP](https://www.fcpeuro.com/products/bmw-coil-spring-lesjofors-4008441)) or **31331093084/085** (Lesjöfors 4008469) ([FCP](https://www.fcpeuro.com/products/bmw-coil-spring-lesjofors-4008469)) | **33536750250** ([FCP, Genuine](https://www.fcpeuro.com/products/bmw-coil-spring-rear-33536750250)); **33531095714 / 33539071951** (Lesjöfors 4208468) ([FCP](https://www.fcpeuro.com/products/bmw-coil-spring-lesjofors-4208468)) |
| US M3 coupe | **31332283130 / 31332282330** (Lesjöfors 4008488, \$74.99) ([FCP](https://www.fcpeuro.com/products/bmw-coil-spring-lesjofors-4008488)) | **33532283135 / 33532229490** (Lesjöfors 4208475, \$74.99) ([FCP](https://www.fcpeuro.com/products/bmw-coil-spring-lesjofors-4208475)); **33532283136 / 33532229491** (Mubea, \$97.99) ([FCP](https://www.fcpeuro.com/products/bmw-coil-spring-mubea-33532283136)); **33532283137 / 33532229492** (Mubea \$86.99; Lesjöfors 4208487 \$100.99), listed for coupe *and* convertible ([FCP](https://www.fcpeuro.com/products/bmw-coil-spring-mubea-33532283137), [FCP](https://www.fcpeuro.com/products/bmw-coil-spring-lesjofors-4208487)) |
| US M3 convertible | **31332282332** (Lesjöfors 4008516, \$87.99) ([FCP](https://www.fcpeuro.com/products/bmw-coil-spring-lesjofors-4008516)) | **33532283137 / 33532229492** (as above) |

- Heavier-duty Touring rear springs exist off the shelf: Lesjöfors **4208445** "Reinforced Version, w/o sports suspension" and **4208446** "Heavy duty, w/ sports suspension", both listed for the 325i Wagon ([FCP 4208445](https://www.fcpeuro.com/products/coil-spring-lesjofors-4208445), [FCP 4208446](https://www.fcpeuro.com/products/coil-spring-lesjofors-4208446)) [read].
- **Rates:** none published by BMW or the OE makers. One search for measured E46 M3 rates found only an E9x M3 thread quoting rates "from memory" [snippet], not usable.
- **Touring-specific kits** [read]:
  - H&R Sport Springs **29419**, "2000-2005 BMW 325i Sport Wagon RWD", linear, −1.3 in front / −1.2 in rear ([springrates](https://www.springrates.com/products/h-r-sport-springs-for-2000-2005-bmw-325i-sport-wagon-e46)); a retailer adds "Fits E46 323, 325 2WD Sport Wagon only" [snippet].
  - Eibach Pro-Kit **2067.140**, one kit for the 2001–05 325i sedan and wagon ([springrates](https://www.springrates.com/products/eibach-front-and-rear-coil-spring-lowering-kit-set-of-4-for-2001-2005-bmw-325i)).
  - Vogtland **951069**, E46 Touring 6-cylinder, progressive, −40 mm front and rear, "reduced by the measure of the original sport suspension" ([springrates](https://www.springrates.com/products/vogtland-sport-lowering-springs-for-2001-2006-bmw-3-series-touring-6-cyl-e46)).
  - Ground Control: an E46 M3 coilover conversion kit (SKU 2031, \$599) with rear height adjusters, "All racing and street/show spring rates are available" (Eibach ERS), and a Koni kit (2031.100, \$1,499) with an unstated "street spring rate"; no default rates are printed ([Ground Control](https://groundcontrolstore.com/products/coilover-conversion-kit-bmw-e46-m3-01-up), [kit](https://groundcontrolstore.com/products/e46-m3-bread-butter-kit)).
  - UUC: no E46 Touring spring found [snippet: one search].

### Inferences

- **(inference)** The M3 convertible's rear spring (33532283137) is also one of the M3 coupe's choices, so it is the heaviest M3 rear class, not a convertible-only spring. Round 4's "M3 convertible-rated rear springs" therefore means 33532283137.
- **(inference)** No maker sells a spring for an M3-axle Touring. All the Touring kits above are for the non-M axle. Because the rear spring sits on the same lower arm (33326770813) and pads on both cars (round-4 ETK finding), a Touring rear spring physically fits the M3 axle. The Touring's "reinforced" or "heavy duty" rear springs (Lesjöfors 4208445/4208446) are a cheap candidate for the extra rear load, but nobody publishes their rates, and the M3's own rear springs are progressive and M3-tuned (BMW ST041, round 4). Treat them as a test option, judged by measured ride height.
- **(inference)** The front still needs M3-type springs on M3 struts (different upper pocket and pad, round 4), so a Touring kit's front springs don't apply.

### Still open

- OEM spring rates for any of these numbers. What would settle it: a spring-rate tester at a suspension shop, or Lesjöfors catalog wire/coil data (not reached).
- Which of the VIN-dependent numbers your Touring and donor carry: ask a dealer to run both VINs, or read the paint marks before teardown (round-4 advice stands).

### Guide impact

**Writer: susp.** README.md:481, current row: "| Rear springs and dampers rated for the Touring | Buy new | The Touring's own rear dampers (33526750783 standard, …) … The M3 coupe's springs and dampers sat too low in one Touring (…) |". **Add a sentence to the Notes cell:**
> BMW assigns springs by VIN; FCP Euro's fitment notes give the candidates: M3 coupe front 31332283130, M3 convertible front 31332282332, M3 rear 33532283135/136/137 (the convertible takes 33532283137, the heaviest), and for a manual 2003 325i Touring front 31331093068 (standard) or 31331093082–085 (sport) ([FCP Euro](https://www.fcpeuro.com/products/bmw-coil-spring-lesjofors-4008488), [FCP Euro](https://www.fcpeuro.com/products/bmw-coil-spring-mubea-33532283137), [FCP Euro](https://www.fcpeuro.com/products/bmw-front-coil-spring-31331093068)). No maker sells springs for an M3-axle Touring: H&R 29419, Eibach 2067.140 and Vogtland 951069 are for the non-M Touring ([springrates](https://www.springrates.com/products/h-r-sport-springs-for-2000-2005-bmw-325i-sport-wagon-e46)); Ground Control's M3 kit takes any Eibach rate ([Ground Control](https://groundcontrolstore.com/products/coilover-conversion-kit-bmw-e46-m3-01-up)).

README.md:1316, current text: "Plan on M3 front struts or coilovers plus rear dampers and springs rated for the Touring, and ask the vendor to confirm the combination." **Add:** `The Touring's own "reinforced" and "heavy duty" rear springs (Lesjöfors 4208445 and 4208446) fit the M3 rear arm, which carries the spring on the same lower arm and pads, but their rates aren't published; judge them by measured ride height ([FCP Euro](https://www.fcpeuro.com/products/coil-spring-lesjofors-4208445)).`

---

## Gap 5. Damper lengths and fit

### Cited findings

**Bilstein data on ShockWarehouse product pages** (read from the store's product JSON) [read]:

| Bilstein | Covers (OE numbers, per FCP Euro) | Collapsed | Extended | Stroke **(arithmetic)** | Mounts |
|---|---|---|---|---|---|
| B4 **19-103150** (non-M rear) | 33526750781/782/**783**/784, 33522282099/100, 33522282461, 33521095913 and others ([FCP](https://www.fcpeuro.com/products/bmw-shock-absorber-rear-e36-e46-w-standard-suspension-touring-19-103150)) | **370.0 mm** (14.57 in) | **618.0 mm** (24.33 in) | 248 mm | Eye 12 mm / stem ([ShockWarehouse](https://www.shockwarehouse.com/products/bilstein-19-103150-rear-b4-oe-replacement-bilstein-touring-class-shock-absorber-bmw-318i-318is-323ci-323i-323is-325ci-325i-325is-328ci-328i-328is-330ci-330i)) |
| B4 **19-199511** (M3 rear) | **33522283105**, **33522282267**, 33522282477, 33522282217, 33522229510 ([FCP](https://www.fcpeuro.com/products/bmw-shock-absorber-rear-m3-bilstein-bil-19199511)) | **377.0 mm** (14.84 in) | **597.0 mm** (23.50 in) | 220 mm | Eye 12 mm / stem ([ShockWarehouse](https://www.shockwarehouse.com/products/bilstein-19-199511-rear-b4-oe-replacement-bilstein-touring-class-shock-absorber-bmw-m3)) |
| B6 **24-027243** (non-M rear) | non-M list as above ([FCP](https://www.fcpeuro.com/products/bmw-shock-absorber-rear-e36-hd-24-027243)) | 368.5 mm | 599.0 mm | 230.5 mm | Eye 12 mm / stem ([ShockWarehouse](https://www.shockwarehouse.com/products/bilstein-24-027243-rear-4600-heavy-duty-b6-shock-absorber-bmw-318i-318is-323ci-323i-323is-325ci-325i-325is-328ci-328i-328is-330ci-330i)) |
| B6 **24-143998** (M3 rear) | 33522282267, 33522283105, 33522282477 ([FCP](https://www.fcpeuro.com/products/bmw-shock-absorber-m3-24-143998)) | 367.5 mm | 593.5 mm | 226 mm | Eye 12 mm / stem ([ShockWarehouse](https://www.shockwarehouse.com/products/bilstein-24-143998-rear-4600-heavy-duty-b6-shock-absorber-bmw-m3)) |

- Sachs equivalents: non-M rear **556 882** (also Boge 27-C42-A) covers 33526750783; M3 rear **310 053** covers both 33522283105 and 33522282267 ([FCP 556 882](https://www.fcpeuro.com/products/bmw-shock-absorber-rear-e36-e46-sachs-556-882), [FCP 310 053](https://www.fcpeuro.com/products/bmw-shock-absorber-rear-m3-e46-310-053)) [read]. No Sachs or Boge lengths were reachable (TecDoc shops behind Cloudflare).
- Prices at FCP Euro [read]: Genuine 33526750783 \$226.99; Genuine 33522283105 and 33522282267 \$262.99 each; Bilstein 19-199511 \$107.00; Sachs 310 053 \$152.58; Bilstein 24-143998 \$147.00.
- One search for direct reports of non-M dampers on M3 trailing arms found nothing on point [snippet].

### Inferences

- **(inference)** Every aftermarket line treats the M3 coupe and convertible rear dampers as one part. The choice between 33522283105 and 33522282267 doesn't matter for length or mounting.
- **(inference)** The non-M rear damper (B4) is 21 mm longer at full extension and 7 mm shorter fully compressed than the M3 one; the B6 pair differ by only 5.5 mm and 1 mm. The mounts are the same type (12 mm lower eye, stem top), matching round 4's ETK finding of common lower bolt and rod nut. So a non-M damper bolts to an M3 arm. But the rear damper is also the rebound stop, so a non-M B4 would allow roughly 21 mm more droop at the damper (more at the wheel), and its valving is for non-M springs. Keep M3 dampers, as round 4 recommended.

### Still open

- OE Sachs/Boge lengths for 33526750783, 33522283105 and 33522282267 (Bilstein's are equivalents, not the OE part). What would settle it: measure the donor's and the Touring's dampers, eye centre to stem shoulder, extended and compressed.

### Guide impact

**Writer: susp.** README.md:1315, current text: "**Dampers.** BMW lists 33526750783 (standard) and 33526750784 (sport or rough-road) rear dampers for the Touring … The M3's rear damper (33522283105) is a coupe part (…)". **Add:**
> Bilstein's replacements show the difference: its B4 for every non-M E46 rear (19-103150) runs 370–618 mm, its B4 for the M3 (19-199511) 377–597 mm, both with a 12 mm lower eye and a stem top ([ShockWarehouse](https://www.shockwarehouse.com/products/bilstein-19-199511-rear-b4-oe-replacement-bilstein-touring-class-shock-absorber-bmw-m3), [ShockWarehouse](https://www.shockwarehouse.com/products/bilstein-19-103150-rear-b4-oe-replacement-bilstein-touring-class-shock-absorber-bmw-318i-318is-323ci-323i-323is-325ci-325i-325is-328ci-328i-328is-330ci-330i)). The same Bilstein and Sachs parts serve both M3 rear numbers, 33522283105 and 33522282267 ([FCP Euro](https://www.fcpeuro.com/products/bmw-shock-absorber-rear-m3-e46-310-053)). A non-M damper bolts on but extends 21 mm further, so use M3 dampers.

---

## Gap 6. Fuel

### Cited findings

- **Prices, BMWPartsDeal, 22 October 2026** [read]:
  - M3 fuel pipes set **16112283288**: \$159.88 (list \$193.89), replaces 16112229751 ([link](https://www.bmwpartsdeal.com/parts/bmw-fuel_pipes_set-16112283288.html)); Touring set **16117175998**: \$150.04, replaces 16111184390 ([link](https://www.bmwpartsdeal.com/parts/bmw-fuel_pipes_set-16117175998.html)).
  - M3 front purge line **16132229652** \$89.59 ([link](https://www.bmwpartsdeal.com/parts/bmw-scavenging_line_front-16132229652.html)); M3 rear purge line **16132229417** \$77.76 ([link](https://www.bmwpartsdeal.com/parts/bmw-scavenging_line_rear-16132229417.html)); Touring rear purge line **16136751175** \$25.60 ([link](https://www.bmwpartsdeal.com/parts/bmw-scavenge_air_line-16136751175.html)); Touring front 16111184135 \$107.47 ([link](https://www.bmwpartsdeal.com/parts/bmw-scavenge_air_line-16111184135.html)).
  - Delivery units: M3 **16142229684** \$559.16 (list \$754.48) ([link](https://www.bmwpartsdeal.com/parts/bmw-delivery_unit_right-16142229684.html)); Touring **16146766942** \$370.59 (list \$495.77), replaces 16146752499 ([link](https://www.bmwpartsdeal.com/parts/bmw-delivery_unit_right-16146766942.html)).
- **Connector types** [image]: BMWPartsDeal's single-part drawing of 16112283288 shows one hose with a moulded end and a quick-connector body, and a second hose with plain ends for clamps; this matches round 4's reading. The Touring set's page shows the whole group drawing, with clamps (item 6) at both ends of the set (item 5). No drawing or listing gives sizes.
- **Connector sizes** [snippet]: aftermarket E46 M3 fuel fittings are sold for both 5/16 in (7.89 mm) and 3/8 in (9.49 mm) quick-connects (Turner/Precision Raceworks listings); no source ties either to a BMW line number.
- **Purge-line joint** [read, image]: in the ETK EVAP groups, the Touring's rear line 16136751175 (item 12, 32 g, "from Aug '99") and the M3's rear line 16132229417 (item 16, 40 g) are both drawn with the same small push-fit coupling at their forward ends ([ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/feb2003/browse/fuel_supply/exp_tank_activated_carbon_container/), [drawing](https://ills.bmwfans.info/1x7z.png); [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/), [drawing](https://ills.bmwfans.info/1x81.png)).
- **Sleeve question** [read]: the M3 pump group lists the same rubber seal 16111184084 ×2, O-ring 16141183543 and screw cap 16116762417 ×2 that round 4 found on the Touring, plus the M3-only "Fuel baffle fixture" 16112229656 ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/)). BimmerWorld: the baffle "installs under the right side (passenger side, on US cars) fuel pump assembly inside the fuel tank", \$123.62 ([BimmerWorld](https://www.bimmerworld.com/Intake-Fuel/Fuel-Filters/Genuine-BMW-Fuel-Baffle-Fixture-16112229656-E46-E46-M3.html)). The guide already reports an owner who found the M3 pump body smaller in diameter (README.md:1397).
- **Flow ratings**: none found. BimmerWorld's non-M VDO page names Continental as the maker and the superseded numbers, with no flow figure ([BimmerWorld](https://www.bimmerworld.com/Intake-Fuel/Fuel-Filters/Fuel-Pump-Assembly-E46-Non-M.html)) [read]; one search for 16142229684's rating found none [snippet].
- **Sender curves**: none found for the E46; one search returned only other makes [snippet].
- (bmwfans returned HTTP 500 for the Touring pump page this session; round 4 had already read it.)

### Inferences

- **(inference)** Same flange seal and screw cap on both tanks means the same opening. A smaller M3 pump body in that opening would explain both forum reports: "plug and play" at the flange, and "needs a sleeve" to locate the body. The M3 baffle 16112229656 is the likely "sleeve". Fit the baffle with the M3 pump, as the guide already recommends.
- **(inference)** The two rear purge lines end in the same style of coupling, so the M3 front line probably mates with the Touring's rear line; at \$77.76 the M3 rear line is cheap insurance if it doesn't.

### Still open

- Quick-connector sizes at each end of both pipe sets: measure the donor's with calipers, or ask a dealer for the connector part numbers.
- Whether 16132229652 mates with 16136751175: try them on the bench.
- VDO/Continental flow for 16146766942 and 16142229684: not published where reachable. The guide's 5-bar delivery test still decides.
- Sender resistance curves: measure both senders across their travel with an ohmmeter.

### Guide impact

**Writer: fuel.** README.md:1397, current text: "…owners have fitted the M3 delivery unit (16142229684) and baffle (16112229656) into sedan tanks; one says it needs a sleeve, and another found the M3 pump body smaller in diameter (…)". **Add after it:**
> Both tanks take the same pump-flange seal (16111184084), O-ring and screw cap (16116762417), so the opening is the same; the "sleeve" is most likely the M3's own baffle, which sits under the pump ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/fuel_pump_and_fuel_level_sensor/), [BimmerWorld](https://www.bimmerworld.com/Intake-Fuel/Fuel-Filters/Genuine-BMW-Fuel-Baffle-Fixture-16112229656-E46-E46-M3.html)). Fit the pump and baffle together.

README.md:431 (parts table, M3 fuel pump row): **add prices** `New: delivery unit 16142229684 \$559.16, pipe set 16112283288 \$159.88, front purge line 16132229652 \$89.59, rear purge line 16132229417 \$77.76 (BMWPartsDeal, October 2026) ([BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-delivery_unit_right-16142229684.html))`.

README.md:2404, open question "Whether the M3 rear feed line's quick-disconnect mates with the Touring pump's outlet…" (round 4 already reworded it to the pipe set): **add** `; and whether the M3 front purge line 16132229652 mates with the Touring's rear purge line 16136751175 (the drawings show the same coupling style).`

---

## Gap 7. Cooling

### Cited findings

- **Pusher fan on a manual Touring.**
  - ETK, US 325i Touring "Pusher fan": 64546988913 (plus superseded 64548373957 "to Sep '05", 64546905076, 64546922554), compression shroud 64548377795, grids, nuts, 3-pole universal housing 61138380380 and pin terminal 61138380385; **no gearbox condition on any row** [read] ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/heater_and_air_conditioning/pusher_fan/)).
  - bmwfans offers only a "Neutral" gearbox view for the US and the European 325i Touring, so the catalog can't be filtered to a manual car [read] ([US](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/), [Europe](https://bmwfans.info/parts-catalog/E46-Touring/Europe/325i-M54/)).
  - BMW's MS42/MS43 and MS45 training describes one PWM electric fan "controlled by the ECM… remote power output final stage (mounted on the fan housing)", with no gearbox split [read] ([ST055 MS42/MS43](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/3%20MS42%20MS43.pdf), [ST055 MS45](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%202%29/02_MS45.pdf)). The IHKR modules send a "Request for auxiliary fan" to the DME [read].
  - zhpmafia (forum; Cloudflare-blocked): "The ELECTRIC FAN as it relates to the E46 originates ONLY in manual transmission cars (except M3) from 1998 to 2006… between the back of the radiator and empty space in front of the engine"; automatics "come with a Mechanical Fan (engine driven) as well as an Auxiliary Fan"; an owner replaced both with one OEM electric fan "with no wiring or fitment" changes [snippet] ([zhpmafia](https://www.zhpmafia.com/forums/archive/index.php/t-4929.html)).
- **X82.** WDS's connector index calls X82 "Connector, auxiliary-blower motor", and its only location page shows X82 "(4-pin, black), Electric fan" on the shroud fan's power stage [read, image] ([WDS index](https://wds.psjr.org/en/e46/find/X82), [WDS M9/X82](https://wds.psjr.org/en/e46/zinfo/E46_EM9A.htm)). The photo is too small to read the housing.
- **Expansion-tank holder 17112229108.**
  - ETK, M3 "Expansion tank/tubing": holder 17112229108 (440 g), grommets 17112229059 ×2, expanding nut 64121379221 (ST 6.3), sheet-metal screws 07119901587 (6.3 × 22) ×2 [read] ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/radiator/expansion_tank_tubing/)).
  - **The same holder 17112229108 is item 7 in the M3 "Emission control air pump" group**, with air pump 11727837138 on mounting bolts 11727830688 ×3, rubber grommets 35411160590 ×3, expanding nut 64121379221 and one sheet-metal screw 07119901587 [read] ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/emission_control_air_pump/)). The drawing shows the pump sitting on the holder's grommets, and the holder's top tab taking the expanding nut and screw [image] ([drawing](https://ills.bmwfans.info/199q.png)); the tank drawing shows the tank's pegs in the holder's two grommets [image] ([drawing](https://ills.bmwfans.info/3s8w.png)).
  - ETK "Front body bracket right": the M3 has two body brackets the US 325i Touring lacks, **41147894115 "Secondary air pump bracket, front"** (59 g) and **41147894116 "rear"** (44 g), plus 41147893376 "Bracket ABS+ASC". The Touring's left and right lists add only a rough-road (S815A) "Reinforcement, supporting bearing" 51717036781 with a blind rivet; every other row in both groups, and the whole front-wheelhouse group, is the same part on both cars [read] ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/front_body_bracket_right/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/front_body_bracket_right/)). The drawing places items 13 and 14 on the front of the right strut tower, near the longitudinal member [image] ([drawing](https://ills.bmwfans.info/1pkj.png)).
  - Prices, BMWPartsDeal [read]: holder 17112229108 \$175.36 ([link](https://www.bmwpartsdeal.com/parts/bmw-bracket-17112229108.html)); 41147894115 \$16.99 ([link](https://www.bmwpartsdeal.com/parts/bmw-secondary_air_pump_bracket_front-41147894115.html)); 41147894116 \$14.63, with three real photos on the page ([link](https://www.bmwpartsdeal.com/parts/bmw-secondary_air_pump_bracket_rear-41147894116.html)); M3 pusher fan 64546988914 \$760.88 ([link](https://www.bmwpartsdeal.com/parts/bmw-pusher_fan-64546988914.html)); Touring shroud fan 17117561757 \$580.39 ([link](https://www.bmwpartsdeal.com/parts/bmw-fan_housing_with_fan-17117561757.html)).

### Inferences

- **(inference, strong)** A manual 2003 325i Touring has no pusher fan: one DME fan output, the shroud fan on X82, BMW's "auxiliary fan" being the automatic's, and the forum report. Look behind the bumper to confirm.
- **(inference)** WDS uses one designation (X82) for both the shroud fan and the auxiliary fan, and an owner plugged a shroud fan into an automatic's auxiliary-fan plug unchanged. So the Touring's X82 probably mates with a non-M pusher fan, and ETK lists the same 3-pole housing for the M3 and non-M pusher fans. That points to a plug match, needing only a longer or re-routed lead. WDS's "4-pin" against ETK's "3-pole" is unresolved: compare the plugs before cutting.
- **(inference)** The M3 expansion-tank holder is a combined tank and secondary-air-pump bracket. It most likely bolts to the two M3-only welded brackets 41147894115/116, plus one expanding nut in a body hole. These are the "brackets [that] don't exist on a non-M body" the guide mentions. New ones cost about \$32 the pair.

### Still open

- Whether a manual Touring has a pusher fan: look behind the bumper.
- X82 housing match: compare the plug on the Touring's shroud fan with the M3 pusher fan's.
- The welded brackets' exact positions: measure on the donor from the strut-tower studs before cutting.

### Guide impact

**Writer: cool.** README.md:1417, current text: "It sits on the other side of the engine bay from the Touring's, and its brackets don't exist on a non-M body; builders cut them off the donor or bought copies and welded them in (…)". **Replace the bracket clause with:**
> It sits on the other side of the engine bay from the Touring's, on holder 17112229108, which also carries the M3's secondary-air pump ([ETK: tank](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/radiator/expansion_tank_tubing/), [ETK: air pump](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/engine/emission_control_air_pump/)). The only M3-only body brackets there are the "secondary air pump bracket, front" 41147894115 and "rear" 41147894116 on the front of the right strut tower, which the 325i Touring's body lacks ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/front_body_bracket_right/)); they are about \$15–17 each new ([BMWPartsDeal](https://www.bmwpartsdeal.com/parts/bmw-secondary_air_pump_bracket_front-41147894115.html)). Measure their positions on the donor, then weld copies or the new parts in (builders cut them off the donor or bought copies (…)).

README.md:866 ("…on the donor brackets from Phase 2") and JOB-CARDS.md:703 ("new expansion tank on the donor brackets"): **add** `(41147894115/116 and holder 17112229108, which also carries the air pump)`.

README.md:412, current text: "The M3 fan and shroud are M3 parts but use the same 3-pole connector, and the fan's control wire needs no re-pin". Round 4 already proposed a correction; **add:** `WDS names X82 the "auxiliary-blower motor" connector, and a manual car's shroud fan is reported to plug into an automatic's auxiliary-fan connector unchanged, so the plug probably matches; the lead may still need lengthening ([WDS](https://wds.psjr.org/en/e46/find/X82)).` Keep round 4's "compare the plugs first".

---

## Gap 8. Floor and exhaust

### Cited findings

- **Canister holder fixings.** ETK, M3 EVAP group: "Holder for activated charcoal filter" 16132229735 (1.4 kg) with **"Self-locking hex nut M6" 07147153450 ×4**; in the drawing the holder is a tray with a nut at each corner [read, image] ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/), [drawing](https://ills.bmwfans.info/1x81.png)). The holder costs \$92.19 at BMWPartsDeal [read].
- **Body parts near it.** Both the M3 and the US 325i Touring "Mounting parts for trunk floor panel" groups list the same **2 × "Bracket activated carbon container" 41128204385** (20 g) and **2 × "Holder, activated carbon container cover" 41128227776**; the drawing places the two brackets at the front edge of the floor pressing [read, image] ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/bodywork/mounting_parts_for_trunk_floor_panel/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/bodywork/mounting_parts_for_trunk_floor_panel/), [drawing](https://ills.bmwfans.info/dhv0.png)). No M3-only stud or bracket appears in the floor or wheelhouse groups [read].
- **Canister covers.** M3 "Underfloor coating" group: "Cover, activated charcoal filter front" 51717893604 (872 g, \$132.40) with ST4.8 screws and body nuts; the Touring instead has covers 51718233265 (front) and 51718233266 (bottom) held by **8 × M6 nuts 07119905544** [read] ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_trim/underfloor_coating/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_trim/underfloor_coating/)).
- **Rear heat shield fixings.** In the insulation group drawing, item 5 "Heat insulator rear silencer" is fastened with item 12, shown as a flanged nut [image] ([drawing](https://ills.bmwfans.info/3liq.png)). On the M3 list, item 12 is "Body nut" 07129901662 ×1, "Body nut" **07146949379 "D=18MM, ZNS-3" ×9** and "Nut" 51418176418 ×9, shared among several shields; the Touring list has the same 07146949379 ×9 and 51418176418 ×9 [read] ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_trim/insulation/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_trim/insulation_2/)). The shield 51482494848 is \$259.12, `InStock` [read].
- **Muffler dimensions.** One search found no published dimensions for 18107831783 or a direct-fit copy [snippet]. BMWPartsDeal prints the same placeholder weight (21.4 lb) for the M3 and Touring mufflers, and no dimensions [read].

### Inferences

- **(inference)** The M3 canister holder sits on four M6 studs. The only canister brackets in either body's catalog are the same two parts (41128204385) at the front of the floor, so the studs are probably on body parts both cars share. A Touring body may therefore already carry them; the donor check in the guide (Phase 1, step 1.5) decides.
- **(inference)** The M3 rear-silencer shield threads onto body studs with 18 mm-flange nuts. On a new M3 floor 41127895619 the studs may or may not come fitted (the catalog doesn't say), so count and photograph them on the donor.

### Still open

- Stud positions for the canister holder and the shield: photograph and measure them on the donor.
- M3 muffler dimensions: measure the donor's (round 4's datum method stands).

### Guide impact

**Writer: floor.** README.md:1140, current text begins: "**Heat shields.** Take the donor's floor and tunnel heat shields with its exhaust." **Add:**
> The M3's rear-silencer shield 51482494848 (\$259.12 new) hangs on body studs with 18 mm-flange nuts 07146949379 ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_trim/insulation/), [drawing](https://ills.bmwfans.info/3liq.png)); count and photograph its studs on the donor floor before you cut, because a new floor may not have them.

README.md:1172, current text: "BMW lists … carbon-canister brackets on the trunk floor (…)". **Add:**
> On the M3 the canister sits in holder 16132229735 on four M6 studs (four self-locking nuts 07147153450) ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/fuel_supply/exp_tank_activated_carbon_container/)); both cars list the same two floor brackets 41128204385, so check on the donor whether the studs are on those shared brackets.

README.md:2445 (open questions, "the M3 floor's heat-shield part numbers"): **add** `; the canister-holder and rear-shield stud positions, and the M3 muffler's dimensions (no source publishes them).`

---

## Gap 9. Front axle

### Cited findings

- **Hubs.** ETK "Wheel bearing": M3 **"Wheel hub with bearing, front" 31222229501** (2.2 kg); US 325i Touring **"Wheel hub, front, symmetric" 31226757024** (2.2 kg); same dust collar, collar nut 31211128336 and cap on both [read] ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/wheel_bearing/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/wheel_bearing/)). FCP Euro: the M3 hub is Schaeffler (FAG) 805387 and "Includes ABS ring and wheel bearing", 83 mm bearing; the Touring hub is FAG 805349 (Meyle 300 652 0007) and "Includes bearing and ABS ring, 83mm" [read] ([FCP M3](https://www.fcpeuro.com/products/bmw-wheel-hub-assembly-z4-m3-oem-31222229501), [FCP Touring](https://www.fcpeuro.com/products/bmw-wheel-hub-front-31226757024f), [FCP Meyle](https://www.fcpeuro.com/products/bmw-wheel-hub-meyle-3006520007)).
- **Tooth count.** Not found for either hub. Aftermarket listings for other BMW 3 Series hubs give "Number of teeth, ABS ring: 48" [snippet; pages behind Cloudflare]. A Z4 forum thread shows replacement front hubs coming with either a toothed ring or a different ring style, with no count [read] ([z4-forum](https://z4-forum.com/threads/z4-font-hub-replacement-ring-or-teeth.134988)).
- **Thrust plate.** ETK: M3 "Reinforcement plate" 51717893609, 3.4 kg, **12 ×** M10×35 31106772199, plus jack fixture 51717894027 and blind rivet; Touring (from Feb '01) 51717028433, 2.4 kg, **8 ×** 31106772199; front axle support 31111096902 on both [read] ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/front_axle_support_wishbone/), [ETK Touring](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/front_axle_support_wishbone_2/)). The drawings show the M3 plate broad across the front with holes at its front corners and along both sides, and the Touring plate narrowing to a nose at the front; neither drawing shows where each screw goes [image] ([M3](https://ills.bmwfans.info/1nu0.png), [Touring](https://ills.bmwfans.info/dnz4.png)). BMW ST041: "The thrust zone is made of aluminum and is bolted to the control arm joints, front axle carrier and the rear control arm mounts"; its photo (31410005) shows bolt heads along the plate's front edge, sides and rear corners [read, image] ([ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear.pdf)).
- One search for the plate's bolt locations found nothing [snippet].

### Inferences

- **(inference)** The M3 hubs come with their own pulse rings and the conversion keeps the M3 DSC unit that reads them. A tooth-count mismatch can only arise if you mix hubs and DSC units from different cars.
- **(inference)** The front axle support is the same part on both cars, and the M3's extra holes sit at the plate's wider front corners and sides. So at least some of the four extra screws probably thread into the shared subframe, where the Touring's holes already exist but go unused. Unproven.

### Still open

- Front pulse-wheel tooth counts: count the teeth on a donor hub and a Touring hub (mark one tooth, turn the hub), or compare all four wheel speeds in INPA at a steady 50 km/h.
- Where the M3 plate's four extra screws thread in: before removing the donor's plate, note which holes go into the subframe, the M3 control-arm brackets or the body, and check the matching threads on the Touring.

### Guide impact

**Writer: front.** README.md:460, current row: "| Front reinforcement plate 51717893609 | Donor M3 | The Touring's (51717028433) is a different part. Fit new bolts (…) |". **Add to the Notes cell:**
> The M3 plate takes 12 M10×35 screws to the Touring's 8 and is broader at the front ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/front_axle_support_wishbone/)); BMW bolts it "to the control arm joints, front axle carrier and the rear control arm mounts" ([BMW ST041](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/4%20RunningGear.pdf)). Before removing it from the donor, note which part each hole threads into, and check those threads on your car.

README.md:477, ABS sensors row. **Add:**
> The M3 and Touring front hubs (31222229501, 31226757024) each come with their own ABS ring ([FCP Euro](https://www.fcpeuro.com/products/bmw-wheel-hub-assembly-z4-m3-oem-31222229501)); nobody publishes the tooth count, so keep the M3 hubs with the M3 DSC unit.

---

## Sources tried and blocked

Nothing was bypassed. Where a site challenged or refused, I noted it and moved on.

| Site | What happened | Used for |
|---|---|---|
| ECS Tuning | Cloudflare "Just a moment…" (403) | Second-dealer prices |
| Turner Motorsport | Cloudflare (403) | Second-dealer prices |
| eEuroparts | Cloudflare (403) | Second-dealer prices |
| getbmwparts.com, bmwpartsdirect.com, bmw.oempartsonline.com (RevolutionParts-type dealers) | Cloudflare "Attention Required" (403) | Second-dealer prices |
| Pelican Parts | Cloudflare (403) | Catalog pages |
| Bavarian Autosport | 403 | Second-dealer prices |
| AutohausAZ | Incapsula bot page | Second-dealer prices |
| oembmwparts.com | Connection reset | Second-dealer prices |
| Summit Racing | 403 and "Pardon Our Interruption" | Bilstein lengths |
| JEGS | Cloudflare (403) | Bilstein lengths |
| autopartspro.co.uk, autodoc.co.uk, onlinecarparts.co.uk, azmotorfactors.co.uk | Cloudflare (403) | TecDoc lengths, ABS tooth counts |
| zhpmafia.com | Cloudflare (403) | Fan thread (snippet only) |
| archive.org Wayback API, web.archive.org | HTTP 429; proxy tunnel closed mid-exchange; WebFetch refuses the domain | Archived zhpmafia and LBL pages |
| de.bmwfans.info | DNS failure | German ETK part names |
| bmwfans.info, Touring fuel-pump group | HTTP 500 at the time (round 4 had read it) | Pump-group comparison |
| bilsteinus.com | Redirects to the Bilstein home page; no catalogue data | Bilstein lengths |
| shop.bmwusa.com | Works, but sells accessories, not body panels | Second dealer |
| FCP Euro | Works; doesn't list body panels | Second dealer |
| eBay, RealOEM, Schmiedmann | Not retried (blocked in round 4) | — |

Worked this round: BMWPartsDeal, eStore-Central, bmwfans.info (ETK pages and drawings), FCP Euro, ShockWarehouse, springrates.com and groundcontrolstore.com (Shopify product JSON), BimmerWorld, wds.psjr.org, archive.org downloads (BMWTechnicalTrainingDocuments), z4-forum.com.
