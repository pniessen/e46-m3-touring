# rv-body: round-4 review of the body work (arches, quarters, trunk floor, subframe mounts, exhaust under the floor, welding)

## Summary

- **Facts checked against the notes:** about 120 (prices, part numbers, flare profile and seam figures, ride heights, gaps, body control dimensions, weld rules, coupon pass values, torques, weights), plus cross-page greps of each value and the old value it replaced.
- **Spot-checked at their URLs (11 sources, about 35 claims), BMW first:**
  - TIS 41 00 "Welding and soldering steel parts", pp.1–3: 8 mm plug holes, 25 mm minimum spacing, G3Si1/G4Si1, 82/18, paint off about 30 mm, ground on the part, no MIG brazing, filler only under 2 mm. Confirmed.
  - TIS 41 00 gaps, p.2: rear door to side wall 4 ± 0.75 mm, front to rear door 4.5 ± 0.75, doors to sill 5 ± 1, parallelism 1 mm. Confirmed.
  - TIS 41 35 101 Touring, pp.1, 2, 8, 11, 15: C-pillar cut 200 mm from the roof edge (p.1), strips about 60 mm and about 30 mm in, plug holes drilled in the body (p.8), continuous seam (p.11), "Cringe edge of wheel arch… Seal connection points" (p.15). Confirmed.
  - TIS 41 35 101 coupe: contact pattern ≤ 1 mm and strips 40/60 mm are on **p.9** (page_1889), adhesive 51 0 032 and "Combustible foam in welding area!" on **p.12** (page_1892). The guide labelled them p.8 and p.11; fixed.
  - TIS 41 00 top view, rear (image R41 1103): E–E 440 mm ahead of the damper mounts, F–F 660 mm at the front corners of the spare-wheel well, R–R and S–S 845 mm. So F–F is the rear pair, as the guide says.
  - TIS 41 12 535 p.1 (bench, tank and axle carrier out), TIS 33 00 M3 (587/600 mm, ±10, design position 2 mm). Confirmed.
  - BMWPartsDeal, 22 Oct 2026: 41357894541 \$2,105.60, 41217894553 \$127.54, 41217894554 \$118.80, 41217890677 \$1,311.70, 41217890689 \$6,932.63, 41127895619 \$763.61, 51717894229 \$88.22, 41117000246 "This part is discontinued" (\$1,304.68). All match the guide.
  - ETK trunk-floor groups, M3 and Touring: 41127895619 (12 kg, "Additionally required: Item 26" = 51717894229), 41112497585 on both, 41122494844 and 41112493931 M3 only, 41118204223 on the Touring. Confirmed.
  - I-CAR practice welding guide: thin-thin 6 mm hole, face 8–10, 3–8 mm tear-out; thick-thick 8 mm hole, face 10–13, 5–10 mm tear-out. Matches the guide's coupon table.
  - CMP part 2: the "within 5"/120mm of the chassis rails" access cut is for the topside of the rear mounts; the hidden-spot-weld quote. Confirmed.
- **WebSearch:** none used.
- **P1:** none found.
- **Open items from the brief:** (1) README 0470 now names the hangers H1 front-left, H2 rear-left, H3 right rail, as figure 29 and WS 0150 do; Phase 5 and WS 0184 use the same names. (2) WS 0150's 660 mm ± 1 mm agrees with Key numbers (E–E 440 front pair, F–F 660 rear pair, ±1 mm) and with WS 0180's tolerance; README 0470's datum step now carries the 660 mm too. (3) Cards 2b and 6 trimmed of text that repeats the guide; growth now 2b +38% words / +33% text, Card 6 +39% / +37%, Card 10b +39% / +38%.

## Fixed directly in my fragments

| Priority | Fragment | What was wrong | Fix |
|---|---|---|---|
| P2 | README 0470 | Record step 4 named the hangers "front-left, rear-left or right"; figure 29 and the worksheet use H1/H2/H3 | "H1 front-left, H2 rear-left or H3 on the right rail, as in *Hangers* below" |
| P2 | README 0470 | Datum step had no BMW pass value for the rear-mount spacing | Added BMW's 660 mm (26.0 in) ± 1 mm, F–F, with the TIS 41 00 rear top-view link and "our reading of the drawing" |
| P2 | README 0470 | Option 4: "three swaps … ran a US E36 M3 muffler … and called it quiet". Only Trent's post says so ("Blissfully quiet now", after a loud Stromung); Kaiv's and Bry5on's posts say nothing about noise (gapfill_builds_forums, Gap 7) | Split the sentence: three ran it; one owner, who replaced a loud Stromung, called it "blissfully quiet" |
| P2 | Card 10b | "three swaps used a US E36 M3 muffler, no louder than stock": no source says that, and it reads as a Massachusetts pass | "…; it must be no louder than your original", matching README 0470 |
| P2 | README 0670 | "a styling line about 475 mm above the hub at the top and about 490 mm at its front shoulder": 490 mm is the distance from the hub center at 50° (notes C1: X +315, Y +376), not a height | The line peaks about 475 mm above the hub and ends at the front about 315 mm ahead and 375 mm up; flat band "about 50–65 mm" |
| P2 | README 0370, Card 6, WS 0190 | Seam positions given without saying they are our inference | Labelled as our inference from scaled drawings (README 0670, 0680, figures 08/27/28 and Key numbers already did) |
| P2 | README 0480 | The welding section didn't carry the Safety section's brake-pipe rule, though the pipes stay full through Phase 5 | Lead-in now "Fuel, brakes, battery and electrics", with a bullet: unclip or shield the brake pipes, ends capped ([Safety](#safety)) |
| P2 | README 0480 | Fire paragraph lacked BMW's own warning | Added TIS 41 35 101 (coupe, p.12) "combustible foam in welding area": check the cavity behind each arch seam and cut foam back |
| P2 | README 0680 | Step 16 (filler) had no pass value | BMW's rule from TIS 41 00 p.2: filler only under 2 mm, deeper is tinned; check: no low spot 2 mm deep under a straightedge or template |
| P3 | README 0670 | BMW ride height cited to NAM3 screenshots although TIS was read directly | Cites TIS 33 00 and TIS 31 00 (M3) on workshop-manuals.com |
| P3 | README 0680 | "Cut 200 mm below the roof edge…" cited p.8, which doesn't show the cut lines | Cites p.1 and p.2 |
| P3 | README 0680 | Coupe TIS page labels p.8 and p.11 are p.9 and p.12 | Relabelled |
| P3 | README 0680 | Card 6 says "arch edge crimped over the inner flange"; the README only described BMW crimping | Step 10 bullet is now an action: close any opened lip by crimping, as BMW does, before sealing |
| P3 | README 0680 | Backing strip: "plug-welded" only | "plug-welded through holes drilled in the body's side of the joint" (TIS p.8: "Drill the holes for the plug welding … in the body"), which also matches figure 28's "to one side only" |
| P3 | README 0360 | Phase 5 step 8: hanger names and canister clearance without a number | H1/H2/H3 added; "clears the muffler's right end by 25 mm (1 in)" |
| P3 | Card 2b | Repeats of the guide; bracket step covered only the right bracket, Phase 2 covers both | Dropped "(coupe and convertible alike)" and the cheapest-steel aside; templates line points to the worksheet's seven stations; "Unless bought new: both muffler brackets out, the right one cut off its rail…" |
| P3 | Card 5 | "BMW's body dimensions in TIS" | "BMW's control dimensions (TIS 41 00)" |
| P3 | Card 6 | "(BMW publishes no travel figure)" repeats the README | Dropped |
| P3 | WS 0184 | Hanger rows unnamed | "(H2)", "(H3)" |
| P3 | WS 0190 | Refers to the "*Arch section and wheel offsets*" diagram; the redraw renamed it "Arch section at the axle" | Renamed |

All edited fragments re-checked: headings unchanged, tables even, every `$` escaped, every internal anchor present in the preview.

## Requests to other owners

### R1: README 0900__key-numbers.md: plug-weld row lacks the arch-lip hole (P3, rv-ref)
- **Change:** replace
- **Find (exact current text):**
  > | Plug welds | BMW: 8 mm (5/16 in) holes, at least 25 mm (1 in) apart, at the factory spot-weld positions. I-CAR: an 8 mm plug 10–13 mm across and no more than 3 mm high | BMW TIS 41 00; [I-CAR CRN 1484](https://rts.i-car.com/crn-1484.html), [I-CAR (2022)](https://rts.i-car.com/collision-repair-news/spot-and-plug-weld-nugget-size.html) |
- **New text:**
  > | Plug welds | BMW: 8 mm (5/16 in) holes, at least 25 mm (1 in) apart, at the factory spot-weld positions. I-CAR: an 8 mm plug 10–13 mm across and no more than 3 mm high. On the arch lip this guide uses I-CAR's 6 mm thin-to-thin hole: face 8–10 mm, and a 3–8 mm hole torn from the bottom coupon | [BMW TIS 41 00](https://workshop-manuals.com/bmw/3_series_e46/325i_m54_tour/2_repair_instructions/41__body_%28tour%29/0__body/48_ra__welding_and_soldering_steel_parts/); [I-CAR CRN 1484](https://rts.i-car.com/crn-1484.html), [I-CAR (2022)](https://rts.i-car.com/collision-repair-news/spot-and-plug-weld-nugget-size.html), [I-CAR practice welding guide](https://info.i-car.com/getmedia/5bf41ea3-7245-46a2-9d3f-9e6723bcb69f/i-car_practice-welding-guide.pdf) |
- **Why:** the graft (README 0680 step 10, Card 6, WS 0170/0190) uses 6 mm holes on the lip; Key numbers gave only the floor's 8 mm. Values confirmed in the I-CAR PDF (rear_arches.md Q3).

### R2: README 0920__open-questions-to-verify.md: answered item points to the wrong section (P3, rv-ref)
- **Change:** replace
- **Find (exact current text):**
  > - US prices for new M3 arch steel, and BMW's E46 body control dimensions and panel gaps (in TIS 41 00, not 51 00): [Rear arches and doors](#rear-arches-and-doors).
- **New text:**
  > - US prices for new M3 arch steel: [Rear arches and doors](#rear-arches-and-doors). BMW's E46 panel gaps: [Rear doors](#rear-doors). BMW's E46 body control dimensions, in TIS 41 00 rather than 51 00: [Phase 5](#phase-5-metalwork-1-subframe-mounts-and-floor) and [Key numbers](#key-numbers).
- **Why:** "Rear arches and doors" holds neither the control dimensions (Phase 5 step 2, Key numbers) nor the gaps (Rear doors, Measure and mock up); gapfill_bmw_chassis_body.md Gap 6.

### R3: research.md (not a fragment): two stale body values (P3, coordinator)
- **Change:** replace (two sentences in the older sections that the round-4 summary says it supersedes)
- **Find:**
  > The 28 kg M3 silencer hangs on two mounts on the left and one on the right, while the non-M floor has one hanger on the driver's side and none on the passenger side, so hangers must be moved, cut from the donor or welded to the passenger rail
- **New text:**
  > The M3 silencer (26.7 kg in BMW's catalog) hangs on two mounts on the left and one on the right, while the Touring's floor has only left-side brackets for its small muffler, so the rear-left stud plate is swapped and the right bracket added, new or cut from the donor
- **Find:**
  > R44 lists the right coupe quarter at \$5,525, US dealers reportedly list convertible quarters at about \$2,400–2,600 each (search snippets only)
- **New text:**
  > R44, a UK shop, lists each coupe quarter at £4,420, and a US dealer lists the convertible quarters at \$2,105.60 each (BMWPartsDeal, October 2026)
- **Why:** README now gives 26.7 kg (ETK) and the October 2026 prices (rear_floor_exhaust.md correction 5; rear_arches.md correction 3; gapfill_parts_prices.md Gap 1). Keep the existing links.

## Figure fixes (for the diagram makers)

### F1: 27-arch-profile.svg (README Figure 26): "490" is a radius, not a height
- **What's wrong:** the label "(≈490 at its front)" under "M3 bulge, edge ≈475", and the aria-label's "The bulge's edge is about 475 mm above the hub at the top and 490 mm at its front shoulder". 490 mm is the bulge line's distance from the hub center at 50° forward (notes C1: X +315, Y +376). Read as a height it puts the front of the bulge 115 mm too high. The dashed outline itself is drawn correctly: its front end sits at x 572, y 201.6, which is +315 mm, +376 mm at the figure's 0.4 px/mm.
- **Exact fix:**
  - label text: "(≈490 at its front)" → "(front end ≈375 up, 315 ahead)"
  - aria-label: replace "The bulge's edge is about 475 mm above the hub at the top and 490 mm at its front shoulder, and meets the bumper line about 300 mm behind the axle." with "The bulge's edge peaks about 475 mm above the hub over the axle, ends at the front about 315 mm ahead of the axle and 375 mm above the hub, and meets the bumper line about 300 mm behind the axle."
- The caption file needs no change. README 0670 now says the same.

The other figures in my area match the text: 01 ("fit M3 floor"; aria no longer "fabricated"), 05, 08, 09, 14, 28, 29 (H1/H2/H3, rear mounts 132 px = 660 mm apart, rails at about ±422 mm as in TIS R–R/S–S 845), and 30. Every redraw caption replaces its old inline caption at assembly, and no placeholders are left.

## Not verified

- Which physical plate each of BMW's three bracket numbers is; where the M3 canister holder's four M6 studs sit; the muffler and floor dimensions. These are still open; the donor measurements settle them.
- The flare-profile and seam figures: scaled-drawing estimates from the notes. I didn't re-scale the drawings.
- The NAM3 E36-muffler posts: not opened. I relied on the gap-fill's quoted text.
- Massachusetts "no louder than the original equipment" wording (rv-plan's area).
- Left as is, by choice: the 8 mm floor coupon uses I-CAR's thick-thick pass values (face 10–13 mm, 5–10 mm tear-out) on about 1 mm steel. I-CAR has no 8 mm thin-thin coupon, and the table labels it as the thick-thick one.
