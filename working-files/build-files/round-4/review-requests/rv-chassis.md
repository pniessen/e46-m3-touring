# rv-chassis: round-4 review of suspension, ride height, alignment, front axle, steering, power steering, brakes and bleeding

Scope: README 0230, 0240, 0250, 0280, 0390, 0500, 0520, 0530, 0610, 0700, 0890; WIRING 0320; Cards 7b, 7c, 8a, 8b, 8c, 12d; Worksheets 0220, 0230, 0450; figures 13, 31, 32, 33 and their captions. Cross-checked against every other page in `preview/` and a fresh private assembly.

## Checked

- **About 190 facts:** ride heights (both cars, every row), loads and tolerances; every chassis, steering and brake torque in my fragments against Appendix 0870, Cards 3e/7b/7c/8a/8b/8c/12d and torque logs WS 0220/0230/0260; bleeding rules and order; parking-brake setting; fluids; DSC options and routines; alignment values (M3 and Touring); weights, axle loads and ratings; tire pressures and radii; about 60 part numbers; phase-step links; the four figures' labels and aria-labels.
- **Spot-checked at the URL: about 55 BMW pages** (TIS 12/2007 on workshop-manuals.com, ETK on bmwfans.info). WebFetch failed on DNS, so I fetched with curl through the session proxy and read the HTML as text; nothing was bypassed. Read: TIS 31 31 1AZ; 34 00 048 pp.1–2; 34 00 050 pp.1–2; 34 10 014 pp.1–3; 32 00 normal position (M3); 31 00 and 33 00 ride height (Touring, M3 rear); 34 32 1AZ; 31 10 1AZ/8AZ; 32 00 150; 32 13 1AZ; 32 21 1AZ–5AZ; 32 31; 32 41 (4 pages); 31 12 (3 pages); 31 21; 31 35 (2 pages); 33 21; 33 31; 33 32 (4 pages); 33 33; 33 41; 33 55; 33 31 020; 33 32 000, 044, 160; 34 11; 34 21; 36 10; ETK label 71246798132 ("ATF").
- **Confirmed at the source:** strut tops 34 Nm, new nuts; thrust plate 59 Nm + 90 (+30)°, rear screws first; M3 load 2 × 68 kg + 14 kg + full tank; Touring rows 576/589/604/617 over 542/555/570/583 (standard) and 561/574/589/602 over 526/539/554/567 (sport); M3 rear 587/600; ±10 mm, design position ±2 mm; TIS 34 00 048 (2 bar, flush RR/RL/FR/FL, rear circuit per tester, fronts 12 strokes, pedal held, right then left); TIS 34 00 050 (MC/DSC work, restart per wheel, 5 strokes after each run, then close); parking brake 10 notches on the adjuster, 5 × 400 N, 2nd tooth, lamp; union torque has no E46 row (E85/E86 14 Nm); KDS design position for M models; subframe 110 Nm new screws; arm ball pin 90 Nm; bracket 59 Nm new screws, no position; ball joint 65 Nm no impact; clamp bolt 81 Nm; hub nut 290 Nm; front bar clamps 21 Nm in normal position; links 65 Nm; rack 42 Nm; tie-rod end 65 Nm; lock nut 45 Nm; column joint 22 Nm new screw; PS pump 21 Nm, pulley 27 Nm, banjo M14 35 Nm, M16 40 Nm; rear arms at the subframe 77 Nm in normal position; trailing-arm console 77 Nm; studs 90 Nm; carrier mounts 77 Nm; half-shaft black M10×46 100 Nm, silver 80 Nm; flange nut M27 300 Nm; discs 16 Nm; front carrier 110 Nm; rear carrier 65 Nm; guide bolts 30 − 5 Nm; wheel bolts 120 ± 10 Nm. PS fluid label "ATF".
- **No leftovers:** no "unladen", "loaded ride height", 24 Nm strut tops, 8 notches or conventional-bleed-after-caliper-work on any page; parking brake is "2nd tooth" everywhere, and every "10 notches" is the shoe adjuster, in context.

## P1 issues

1. **Inner tie-rod torque, wrong source note (all pages).** The guide said "TIS gives 110 Nm for the M3; '100 + 10 Nm' is for other E46s". TIS 32 21 2AZ in the M3's own manual says: "E46, E85 / except S54, E86 / except S54 — 100 +10 Nm"; "… E85 / S54, E86 / S54 — 110 Nm". So every E46, M3 included, is "100 + 10 Nm"; the 110 Nm row is the Z4 M's (Department 69 mapped "S54" to the M3). I kept 110 Nm, which meets "100 + 10" whether the "+ 10" is a tolerance or a final step, and fixed the note in README 0390, 0500, Card 8b and WS 0230. **R1/R2** for 0870 and 0920.
2. **README 0610, Option B "Coding by hand"** said an M3 unit coded from the Touring's order "gets 325i values". BMW's coding data admits the M3 MK60 (index C06) only with `S54B32` and a 09/2002 date, so NCS refuses it outright (WIRING Session 5 step 2; SP-Daten V32). **Fixed** (bullet rewritten as "Coding from a session order"). Figure 13 says the same wrong thing: **F1**.
3. **WIRING 0520 "Bleeding with INPA"** said "close the screw when INPA finishes", against TIS 34 00 050's five pedal strokes with the screw open. Found independently; **already fixed by rv-coding**, together with WIRING 0670's row and README 0420 step 13. No request.

## Fixed in my fragments

- **README 0610:** Option B coding bullet (P1 above); Option A recommendation now says plainly "leave your unit as it's coded and run the three routines", matching WIRING Session 5 and the coordinator's rule; "Coding and VIN" no longer reads as if Option A needs a PA-Soft VIN write; coordinator item from rv-coding applied: "5EF1 (5E1F in BMW's job file)".
- **README 0390, 0500; Card 8b; WS 0230:** inner tie-rod note (P1 above), citing TIS 32 21 2AZ.
- **README 0530 step 6 and WS 0230:** BMW's leak test now has a home pass value: press until INPA reads about 36 bar, and after 2 minutes it must still read at least about 33 bar (8%).
- **README 0520:** "a caster reading … proves" → "is good evidence … (our inference)".
- **README 0520 step 3 and 0890:** the design-position rule only adds weight, so they now say what to do with a corner already within 2 mm or up to 10 mm low: align it at the M3 load as it sits (our inference; BMW's normal-position tolerance is ±10 mm).
- **README 0240:** coordinator item from rv-plan applied (the xi case proves only that the plugs mate; xi notes correction 9).
- **Card 8c:** added the front hose-to-pipe union row, 14 Nm (10 ft-lb), which README 0530 step 2 and WS 0230 already give but the card lacked; fronts bled "right then left" (TIS 34 00 048).
- **Card 7b, Card 7c, WS 0220** (TIS 33 32 / 33 55, read): new nuts on the two ball-joint bolts at each trailing arm (11AZ "Replace nut"); new V-brace screws (23AZ "Replace screws"); new nuts on the rear bar links and link brackets (4AZ, 5AZ); Card 7b parts list adds new subframe collar nuts 33326760374 (TIS 33 32 160 "Replace self-locking nuts"; already in Consumables). WS 0220 also notes that both trailing-arm joints are ball joints on the M3 (TIS 33 32 044: "S54: A ball joint is fitted instead of the rubber mount").
- **WS 0220:** added a parking-brake check table (adjuster 10 notches; 5 × 400 N; 2nd tooth; released free; lamp).
- **Captions:** stale writer notes in `proposed-ride-height-points` and `proposed-brake-hydraulics` marked resolved (below the `---`, so nothing published changes).
- Card growth after edits: 7b +24%, 7c +40%, 8a +26%, 8b +20%, 8c +35%, 12d +34%. Tables and `$` clean (tablecheck); private assembly: all links, ids and dollars OK.

## Requests

### R1: README 0870__torque-values.md: inner tie-rod note (P1, rv-ref)
- **Change:** replace
- **Find (exact current text):**
  > | Inner tie rod to rack, M3 | 110 Nm (81 ft-lb) | TIS gives 110 Nm for the M3; the compilation's "100 + 10 Nm" is TIS's figure for other E46s | Department 69; Flow p.9 |
- **New text:**
  > | Inner tie rod to rack | 110 Nm (81 ft-lb) | TIS prints "100 + 10 Nm" for every E46, the M3 included, as the M3 compilation does; 110 Nm meets it whether the "+ 10" is a tolerance or a final step (our reading). TIS's separate 110 Nm row is for the Z4 M (E85/E86 with the S54), the figure Department 69 gives for the M3 | [TIS 32 21 2AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/32__steering_and_wheel_alignment/21__steering_arms_tie_rods_steer._damper/1_azd__steering_arms/); Flow p.9; Department 69 |
- **Why:** TIS 32 21 2AZ, M3 manual, read at the URL: "E46, E85 / except S54, E86 / except S54 … 100 +10 Nm; E53, E60 … E85 / S54, E86 / S54 … 110 Nm". The value stays; the note is wrong. Card 8b, WS 0230, README 0390 and 0500 now say the same. Note for your leftover check: "100 + 10" now appears on purpose, as TIS's print.

### R2: README 0920__open-questions-to-verify.md: answered list wording (P3, rv-ref)
- **Change:** replace
- **Find (exact current text):**
  > - The power-steering pump bolts, the M3's inner tie-rod torque (110 Nm), the front strut-top nuts
- **New text:**
  > - The power-steering pump bolts, the inner tie-rod torque (110 Nm, which meets TIS's "100 + 10 Nm" for every E46), the front strut-top nuts
- **Why:** as R1.

### R3: README 0870__torque-values.md: BMW's "replace" rules on four rear-axle rows (P2, rv-ref)
- **Change:** replace (four rows)
- **Find (exact current text):**
  > | M12 10.9 bolts at the trailing arm (the two ball joints; one is the eccentric bolt) | 110 Nm (81 ft-lb) | Any position: they pass through ball joints, not bushings | Flow p.16 |
- **New text:**
  > | M12 10.9 bolts at the trailing arm (the two ball joints; one is the eccentric bolt) | 110 Nm (81 ft-lb) | **New** nuts. Any position: on the M3 both joints are ball joints ("S54: A ball joint is fitted instead of the rubber mount", TIS 33 32 044); TIS's E46 row says "tighten in normal position" for the non-M rubber mount | [TIS 33 32 11AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/33__rear_axle/32__control_arms_and_struts/1_azd__control_arms_and_struts/page_3587/); Flow p.16 |
- **Find (exact current text):**
  > | M3 V-brace bolts, ×3 (M10×35 10.9) | 59 Nm (44 ft-lb) + 90° | Only if your body has the mounting points; see [Rear subframe mount reinforcement](#rear-subframe-mount-reinforcement) | PS Designs/Redish instructions |
- **New text:**
  > | M3 V-brace bolts, ×3 (M10×35 10.9) | 59 Nm (44 ft-lb) + 90° | **New** screws. Only if your body has the mounting points; see [Rear subframe mount reinforcement](#rear-subframe-mount-reinforcement) | [TIS 33 32 23AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/33__rear_axle/32__control_arms_and_struts/1_azd__control_arms_and_struts/page_3589/); PS Designs/Redish instructions |
- **Find (exact current text):**
  > | Rear anti-roll bar link nuts | 22 Nm (16 ft-lb) | **At ride height** (rubber mounts; the diagram doesn't mark it, our recommendation) | Flow p.18 |
- **New text:**
  > | Rear anti-roll bar link nuts | 22 Nm (16 ft-lb) | **New** nuts on the links and on the link brackets at the upper control arms. **At ride height** (rubber mounts; BMW doesn't mark it, our recommendation) | [TIS 33 55 4AZ, 5AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/33__rear_axle/55__stabiliser_bar/1_azd__stabilizer_bar/); Flow p.18 |
- **Find (exact current text):**
  > | Subframe to body: collar nuts 33326760374 on the front studs | 77 Nm (57 ft-lb) | A nut on each front stud; line the studs up first |
- **New text:**
  > | Subframe to body: collar nuts 33326760374 on the front studs | 77 Nm (57 ft-lb) | **New** self-locking nuts (TIS 33 32 160). A nut on each front stud; line the studs up first |
- **Why:** BMW's E46 tables in the M3 manual, read at the URLs: 33 32 11AZ "Upper/lower control arms to trailing arm, E36, E46, M12 × 1.5, Replace nut … 110 Nm"; 23AZ "V-strut … E46 / M3 / M3 CSL, Replace screws, 59 Nm, 90°"; 33 55 4AZ/5AZ "Replace nut(s), 22 Nm"; 33 32 160 "Replace self-locking nuts". Card 7b, 7c and WS 0220 now carry these notes, so the table should match.

### R4: push-rod (front support cradle) torque: BMW's 21 Nm against PS Designs' 25 Nm (P2, rv-ref, rv-body, rv-plan; coordinator to decide)
- **Change:** replace, in five places, if accepted
- **README 0870, find:**
  > | Subframe front support cradle (push rod) bolts, ×4 | 25 Nm (18 ft-lb) | Keep your reinforcement kit's spacer plates under it |
- **New text:**
  > | Subframe front support cradle (push rod) bolts, ×4 | 21 Nm (15 ft-lb) | BMW's figure for its M8 8.8 screws ([TIS 33 32 17AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/33__rear_axle/32__control_arms_and_struts/1_azd__control_arms_and_struts/page_3588/), via TIS 33 32 160). Keep your reinforcement kit's spacer plates under it; PS Designs' instructions give 25 Nm |
- **README 0460 (rv-body), find:** `PS Designs calls them "ESSENTIAL" and gives 25 Nm for the four bolts` → **new:** `PS Designs calls them "ESSENTIAL" and gives 25 Nm for the four bolts; BMW's figure for its M8 8.8 screws is 21 Nm (TIS 33 32 17AZ), which we use`
- **README 0510 (rv-plan), find:** `then the push rod's bolts to 25 Nm` → **new:** `then the push rod's bolts to 21 Nm, BMW's figure`
- **Card 7b (mine), find:** `| Push rod (front support cradle) bolts, ×4 | 25 Nm (18 ft-lb) | Kit's spacer plates under it |` → **new:** `| Push rod (front support cradle) bolts, ×4 | 21 Nm (15 ft-lb) | BMW's figure; kit's spacer plates under it |`
- **WS 0220 (mine), find:** `| Subframe front support cradle (push rod) bolts, ×4 | 25 Nm (18 ft-lb) | Keep your reinforcement kit's spacer plates under it | | |` → **new:** `| Subframe front support cradle (push rod) bolts, ×4 | 21 Nm (15 ft-lb) | BMW's figure (TIS 33 32 17AZ); keep your reinforcement kit's spacer plates under it | | |`
- **Why:** TIS 33 32 160 "Removing and installing / replacing tension strut for rear axle carrier" (M3 manual; "M3: remove strut" first) gives the strut's screws "Tightening torque 33 32 17AZ", and 17AZ reads "E46 … M8 8.8 21 Nm". The 25 Nm is the kit maker's. Not dangerous either way; I left my two rows unchanged so the five places can change together.

### R5: README 0510__driveline-and-rear-axle.md and README 0380__phase-7…: new nuts on the trailing-arm ball-joint bolts (P3, rv-plan, rv-fluids)
- **Change:** replace
- **README 0510, find:**
  > and the two M12 10.9 ball-joint bolts at each trailing arm (one of them the eccentric bolt) 110 Nm ([Flow p.16](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing)).
- **New text:**
  > and the two M12 10.9 ball-joint bolts at each trailing arm (one of them the eccentric bolt) 110 Nm, with new nuts ([Flow p.16](https://drive.google.com/file/d/1GS3Hirx6x0c0WG8hPeXiwfXfeUldkQnm/view?usp=sharing), [TIS 33 32 11AZ](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/33__rear_axle/32__control_arms_and_struts/1_azd__control_arms_and_struts/page_3587/)).
- **README 0380 (rv-fluids), find:**
  > the trailing-arm brackets to the body and the two ball-joint bolts at each trailing arm.
- **New text:**
  > the trailing-arm brackets to the body and the two ball-joint bolts at each trailing arm, with new nuts.
- **Why:** TIS 33 32 11AZ "Replace nut" (see R3).

### R6: README 0290__consumables-and-single-use-parts.md: the rear nuts BMW says to replace (P3, rv-plan)
- **Change:** replace
- **Find (exact current text):**
  > | Rear axle fasteners and bushings: subframe collar nuts 33326760374, damper top-mount nuts 07119905374 (four) and rod nuts 33526773882 (two), RTABs | Buy new | |
- **New text:**
  > | Rear axle fasteners and bushings: subframe collar nuts 33326760374, damper top-mount nuts 07119905374 (four) and rod nuts 33526773882 (two), nuts for the four control-arm bolts at the trailing arms, the three V-brace screws if you fit it, the anti-roll-bar link nuts, RTABs | Buy new | BMW says to replace each of these ([TIS 33 32](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/33__rear_axle/32__control_arms_and_struts/1_azd__control_arms_and_struts/page_3587/), [TIS 33 55](https://workshop-manuals.com/bmw/3_series_e46/m3_s54_coupe/4_tightening_torques/33__rear_axle/55__stabiliser_bar/1_azd__stabilizer_bar/)) |
- **Why:** as R3. Part numbers for those nuts aren't in the notes: take them from ETK when ordering.

### R7: README 0070__decide-these-before-you-spend-money.md: the springs option still says "rated for the Touring" (P2, rv-plan)
- **Change:** replace
- **Find (exact current text):**
  > | **Springs, dampers and wheels** | Springs and dampers rated for the Touring, or coilovers; 18-inch Style 67 or 19-inch wheels |
- **New text:**
  > | **Springs, dampers and wheels** | M3 struts and dampers with a stiffer rear spring, or M3-fitment coilovers; 18-inch Style 67 or 19-inch wheels |
- **Why:** the guide now says not to fit the Touring's own rear dampers on the M3 arms (README 0520, 0240; suspension notes correction 3); the options cell is the old wording, though the recommendation cell is right.

### R8: README 0120__budget.md: same label (P3, rv-plan)
- **Change:** replace
- **Find (exact current text):**
  > | Springs and dampers rated for the Touring, or coilovers | \$1,200–\$3,500 |
- **New text:**
  > | Rear springs about 7–9% stiffer than an M3 coupe's, or M3 coilovers | \$1,200–\$3,500 |
- **Why:** as R7; the row's note already describes exactly this.

### R9: research.md line 147, table row "15. Bleed" (P3, coordinator)
- **Change:** replace
- **Find (exact current text):**
  > | 15. Bleed | Conventional RR, RL, FR, FL, then clutch; INPA DSC MK60 → F6 → F1 → F2/F3 | Hydraulic-unit routine at each corner with a firm pedal | Firm pedal; ABS works on a cautious hard stop |
- **New text:**
  > | 15. Bleed | Flush RR, RL, FR, FL at no more than 2 bar, then clutch; INPA DSC MK60 → F6 → F1 → F2/F3 | BMW's way: after caliper or hose work the routine on the rear circuit and 12 pedal strokes per front (TIS 34 00 048); after master-cylinder or DSC-unit work the routine at every wheel, five pedal strokes after each (TIS 34 00 050) | Firm pedal; ABS works on a cautious hard stop |
- **Why:** matches README 0530 step 4 and the TIS pages read at the URLs.

## Figure fixes

### F1: 13-dsc-brake-options.svg (README Figure 22): route B's coding text contradicts BMW's rule (P1)
- **What's wrong:** box B says "From your Touring's order NCS Expert gives it 325i values: set M3 values by hand", and makes the 09/2002 order a fallback ("'VIN not initialized' won't clear? Code it from a vehicle order dated 09/2002 or later …"). BMW's coding data refuses the M3 unit from the Touring's order; the session order with the donor's M3 type key and a 09/2002+ date is the first step (WIRING Session 5 steps 2–5; README 0610 as fixed).
- **Exact fix, drawn text:** replace the three lines "From your Touring's order NCS Expert / gives it 325i values: set M3 values by / hand. It has no Touring body type" with "Codes only from a session order with / the donor's M3 type key and a 09/2002+ / date; it then takes the M3's values. / No Touring body type: leave coupe_m". Replace the four lines "'VIN not initialized' won't clear? Code / it from a vehicle order dated 09/2002 / or later, run INPA's VIN initialisation, / and only then refit your own unit" with "Then INPA's VIN and steering-angle / initialisation. 'VIN not initialized' / still on? Refit your own unit".
- **Exact fix, aria-label:** replace "From your Touring's vehicle order NCS Expert gives it 325i values, so you set M3 values by hand, and its coding has no Touring body type." with "NCS Expert codes it only from a session-only vehicle order with the donor's M3 type key and a date from 09/2002, and it then takes the M3's values; its coding has no Touring body type, so it stays coupe_m." Replace "If VIN not initialized won't clear, code it from a vehicle order dated 09/2002 or later and run INPA's VIN initialisation, and only if it still fails refit your own unit." with "Then run INPA's VIN and steering-angle initialisation; if VIN not initialized still won't clear, refit your own unit."
- The caption (`redraw-13-dsc-brake-options.caption.md`) needs no change.

### F2: 31-ride-height.svg (README Figure 11): "16- to 18-inch adds about 25 mm" beside BMW's own table, which steps 28 mm (P3)
- **What's wrong:** the figure's TIS table shows 589 → 617 mm (front) and 555 → 583 mm (rear) from 16 to 18 inches, 28 mm, next to the note "16- to 18-inch adds about 25 mm". The 25 mm is the rim geometry alone; README 0520 no longer gives it.
- **Exact fix, drawn text:** in "A bigger rim raises BMW's figure about 12.7 mm (0.5 in) per inch with the body / where it was: 16- to 18-inch adds about 25 mm, and hub-to-lip stays the same.", replace "16- to 18-inch adds about 25 mm" with "BMW's rows step 13–15 mm per inch".
- **Exact fix, aria-label:** replace "so 16- to 18-inch adds about 25 mm, while hub-to-lip doesn't change" with "and BMW's rows step 13–15 mm per inch, while hub-to-lip doesn't change".

### Checked, no change needed
- **32-brake-hydraulics.svg:** every label, number and the bleeding panel match README 0530 (TIS 34 00 048/050), Card 8c and WS 0230. The `proposed-booster-vacuum` placeholder still in README 0530 is dropped at assembly by `apply_redraws.py`.
- **33-power-steering.svg:** matches README 0500/0530 and TIS 32 41 (21/27/35/40 Nm).
- **31-ride-height.svg:** apart from F2, matches README 0520 (loads, both tables, tolerances, MA pass values). The missing strut-label hint is carried by the text (coordinator's decision).

## Coordinator items

- **rv-plan, README 0240 (xi sensors):** applied as worded. The car had a Bosch DSC 5.7 harness with the same blue housings, so it proves only that the plugs mate (BMW ST056 p.17; xi notes correction 9); the same wording is in 0610 and WIRING 0320.
- **rv-fluids R7, Card 7b (canister and leak-test pump refit):** applied as worded, after the wheel-speed sensor task. README 0380 step 9 and its "EVAP" Done-when row exist and match (same part numbers). Card 7b is now +35% on its round-3 size; Card 7c was already at +40%, so 7b is the right place.
- **rv-coding, README 0610 (5EF1):** applied as worded. The `DSC_MK60` job file lists 0x5E1F "VIN nicht initialisiert", and WIRING 0320 and Session 5 use 5E1F.

## Could not verify

- WebFetch couldn't resolve any host (DNS); all URL checks went through curl via the session proxy.
- What BMW's "+ 10" in "100 + 10 Nm" means (tolerance or final step). 110 Nm satisfies both readings, so the guide's value stands.
- That TIS 33 32 17AZ's "compression strut on body" is the M3's push rod: inferred from TIS 33 32 160, which sends the strut's screws to 17AZ. The PS Designs PDF wasn't re-read.
- Not re-read this round: TIS 34 32 971 (pedal prop), BMW ST056/ST041/ST503 text, the 5series.net DOT 4 low-viscosity note (still marked unverified in the guide), and the forum and video claims (M346 pedal, Tenza lamp, spring measurements), which I checked against the notes only.
