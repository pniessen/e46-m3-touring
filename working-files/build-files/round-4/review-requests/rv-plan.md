# rv-plan: round-4 review of README framing, plan, legal and the 325xi subchapter

Scope: README 0000–0180, 0190/0220/0270/0290, Phases 0–4, 9, 12, 13, deep dives 0450/0490/0510/0519/0630/0650, Registration and legal 0720–0760, the 325xi subchapter (0050, 0519) and Figure 42 (`42-xi-driveline.svg`, caption `proposed-xi-driveline.caption.md`).

## Checked

- About 140 facts in my area against the notes (`xi_convert_rwd.md`, `xi_keep_awd.md`, `gapfill_coding_body.md`, `gapfill_builds_forums.md`, `gapfill_parts_prices.md`, `suspension_touring_weight.md`), plus the budget arithmetic (\$23,455 × 1.10 and \$63,784 × 1.15), the arch-steel sums (\$4,457.54; \$5,309.37; €2,121), and the 325xi torque and gearing arithmetic (1,544 / 587 / 957 / 2,294 / 3,744 Nm; 14.05 / 15.05 / 15.83 / 17.01 against 15.30).
- 14 spot-checks at the source:
  - BMW ST040 4wd PDF: SA 203, 38:62, 300 Nm, 2,000 / 3,000 Nm, 0.24 L, 33 Nm, 17 mm, 100 kg, the body-pan and tube quotes, S5D-280Z, 17 × 7.0.
  - BMW ST056 DSC PDF: 5.7 on the right, MK60 on the left under the master cylinder, the sensor quotes on pp.17–18, the 5 bar rule, the MY2002 RDW function, and where each yaw sensor sits.
  - BMW ST041 DriveLine text: 355 Nm at 4,900 rpm; the scavenge pickup at the front of the pan.
  - ETK on bmwfans:
    - 18207502523 usage and the xi exhaust-suspension group: on every xi to 09/2001 and on manual xi cars from 09/2001, with no end date. So the "to 09/2001" in the rwd notes was a partial reading, and 0519, which gives no date, is right.
    - The xi gearbox-suspension group: 2 × M8×22, 2 × M8×60, M12×1.5×115.
  - bmwfans VIN decoder:
    - WBAAW33421EN80596 is a 325xi Touring, May 2001.
    - WBAEP33484PE91920 (Baca's car) is a 325xi Touring, 11/2003.
  - NHTSA vPIC reads the same 2001 VIN as a "325i" wagon with no drive type.
  - WDS CAN drawing: 11/15 for both ABS/ASC and MK60; 24/40 for "DSC all-wheel drive".
  - 540 CMR 4.04(1), (4), (6), (12)(d) and (13), and 540 CMR 6.01–6.06 (LII).
  - FCP Euro part 1: the failure quotes.
  - The Bring a Trailer listing: bid to \$59,250 with the reserve not met (8/20/24); "True mileage is unknown"; the seller's "custom plate (brace) … to accommodate the wider transmission tunnel for the XI", "reinforcement plate welded in", and "won't pass CA SMOG".

## Fixed in my fragments

1. **0519, 540 CMR 6.00 (P1).** The text said a Route 2 car falls under "the 2-inch height rule". 540 CMR 4.04(13) exempts four-wheel-drive vehicles from the general 2-inch rule. Instead, 6.00 sets their own lift limits, keeps the body level to within 2 in front to rear, bans spacers and limits a track increase to 4 in. I rewrote the verdict-table cell and the "four-wheel-drive rule" paragraph to match, and added the 4.04(13) citation. A Route 1 car falls back under the general rule. For Route 2 I also added 6.03's own height measure, to record in Phase 0: unladen, floor to the lower edge of the driver's door.
2. **0519, misattributed ST056 quote (P2).** BMW's "installed in the same position" compares the MK60 sensor cluster with the MK60's own earlier yaw sensor, not with the xi's sensor. Both do sit under the driver's seat (ST056 pp.22, 25), so the text now says that, in the body table and the DSC table.
3. **0519 and 0130, time breakdown (P2).** The five jobs added up to 4–9 weekends against a total of 4–8. I folded the anti-roll-bar brackets into the front-end trial fit and transplant ("1–2, with any brackets"). The total of 4–8 stays.
4. **0519, verdict (P2).** "Three xi Tourings have been converted this way" was wrong: the Buffalo car kept its Bosch DSC and the BaT car's DSC route is unknown. Now: "made rear-drive on M3 running gear, though none has documented its DSC swap".
5. **0519, type key AW33 (conflict 2).** No AW33 appears anywhere in the guide. I added one sentence: the type key doesn't settle it before 09/2001, because the coding data lists AW33 for the 325i Touring of 09/2000–08/2001 while bmwfans decodes a May 2001 AW33 VIN as a 325xi. Go by the decode and `$203`. EP33 is now confirmed by the decode, not just "our reading".
6. **0519 and 0080, Colorado diffs (conflict 6).** "X3 2.5i 3.91 pairs" for both builds was our inference. The sources say only "X3 … 3.91", and the Colorado listing says "X3 3.0". The text now reads "X3 3.91 pairs (the X3 2.5i's ratio)", and the table reads "(the builds' ratio)".
7. **0519, smaller fixes (P3):**
   - The Phase 11 row now runs in Session 5's order: VIN, then coding, then the routines.
   - The trial-fit step 4 says what the diagonals are for.
   - "Expect the M3 crossmember to need an adapter".
   - JMCCRNA: "the gearbox mount in the xi tunnel needed a custom bracket", which is the source's wording, not "the M3 gearbox mount".
   - The S54 pump and pickup are shared only with the Z3 M and Z4 M. The return pipe's usage isn't sourced.
   - "centre" changed to "center" to match the guide.
8. **The 2003 xi sensor anecdote (correction 9).** It now says the plugs mated with a Bosch-harness xi, not that the sensors work. Changed in 0080 lesson 6, 0110 (sensor row), 0330 (Phase 2) and 0510.
9. **Decisions where the builder meets them (P2):**
   - 0070: new row, "A 325xi's drive": convert to rear drive, with a donor built from 09/2002 of the xi's model year or newer.
   - 0110: new bullet, "If your Touring is a 325xi, choose its route first".
   - 0730: the ride-height row notes that a 325xi stands 20 mm higher and links to its baseline.
10. **0000 preamble (P3).** The research history now mentions the two 325xi studies.

Already fixed by rv-chassis while I worked: README 0610 Option B "Coding by hand", which wrongly said an M3 unit gets 325i values from the Touring's order.

## Conflicts: how I judged them

- **AW33:** item 5.
- **Colorado diff ratios:** item 6. The listing's "factory diffs were 2:94s" stays out, because ETK says 3.23 for a manual 325xi.
- **Exhaust bracket 18207502523:** ETK lists it on every xi to 09/2001 and on manual xi cars after, with no end date. 0519, which gives no date, is right. No change.

---

### R1: WIRING-AND-CODING 0520__session-5-dsc-coding-and-vin.md: the 325xi case in Option B (P2, rv-coding)
- **Change:** insert after
- **Find (exact current text):**
  > BMW's rule requires the M3 type key; nobody has documented this order in a Touring.
- **New text** (same paragraph, after that sentence):
  > On a 325xi converted to rear drive, also delete `$203` (all-wheel drive) from the session order: BMW's coding data admits no non-M MK60 index for an `ALLRAD` order, and the whole xi procedure is in the guide's [325xi section](README.md#route-1-code-the-mk60-from-an-xi-order).
- **Why:** README 0519 sends xi owners to Option B "with one more change: delete `$203`", and Session 5 itself never mentions it (`gapfill_coding_body.md`, gap 1: MK60 C04/C05/C09/C10/C12/C13 = `PU01 AND NOT (ALLRAD OR S54B32)`).

### R2: README 0240__rear-axle.md: what the xi sensor case shows (P2, rv-chassis)
- **Change:** replace
- **Find (exact current text):**
  > while a 2003 xi Touring took an M3's "right in" ([e46fanatics](https://www.e46fanatics.com/threads/m3-touring-project.1240087/))
- **New text:**
  > while on a 2003 xi Touring, whose Bosch sensors use the same blue housings, the M3 sensors' plugs mated ([e46fanatics](https://www.e46fanatics.com/threads/m3-touring-project.1240087/))
- **Why:** that car had a Bosch DSC 5.7 harness, so the case proves only that the plugs fit (BMW ST056 p.17; `xi_convert_rwd.md`, correction 9). It's now worded this way in README 0080, 0110, 0330, 0510, 0610 and WIRING 0320.

### R3: README 0920__open-questions-to-verify.md: the pre-09/2001 type key (P3, rv-ref)
- **Change:** replace
- **Find (exact current text):**
  > and the US 325xi Touring's type keys by build date.
- **New text:**
  > and the US 325xi Touring's type keys by build date, including whether a pre-09/2001 xi shares AW33 with the 325i Touring.
- **Why:** BMW's coding data lists AW33 as the 325i Touring's key for 09/2000–08/2001 (`gapfill_coding_body.md`, gap 10), while bmwfans decodes the 2001 AW33 VIN WBAAW33421EN80596 as a 325xi Touring (checked at bmwfans, October 2026).

## Figure fixes (for the diagram makers)

### F1: `42-xi-driveline.svg`: the builds' diff pair (P3)
- **What's wrong:** the "Diff ratios must match" box says "Both builds used an X3 2.5i 3.91 pair". The sources say only "X3 … 3.91", and the Colorado listing says "X3 3.0". The text now says "X3 3.91 pairs (the X3 2.5i's ratio)".
- **Exact fix:**
  - In the visible text, change "Both builds used / an X3 2.5i 3.91 pair;" to "Both builds used / an X3 3.91 pair;".
  - In the `aria-label`, change "both builds used an X3 2.5i 3.91 pair" to "both builds used an X3 3.91 pair (the X3 2.5i's ratio)".

### F2: `42-xi-driveline.svg`: the rack comes out on the rear-drive route (P3)
- **What's wrong:** the convert panel's "Comes out" box lists "the xi front subframe and knuckles" but not the xi rack, which 0519 replaces with the donor's.
- **Exact fix:**
  - In the visible text, change "the xi front subframe and knuckles; the Bosch DSC 5.7 with" to "the xi front subframe, knuckles and rack; the Bosch DSC 5.7 with".
  - Make the same change in the `aria-label` ("the xi front subframe and knuckles, and the Bosch DSC 5.7" becomes "the xi front subframe, knuckles and rack, and the Bosch DSC 5.7").
- **Already right:** every other label, and the caption, agree with the final 0519. The caption file needed no change.

## Not verified

- EPA test groups by year (spreadsheets; taken from the notes, [read]).
- The MK60 pins not on the WDS pages read: brake-light switch, ABS lamp, diagnosis line and wheel-speed outputs. 0519 already says to read them off the donor's plug.
- JMCCRNA's thread, behind e46fanatics' bot check: not bypassed.
- BMW Group Classic's 330xd torque: already marked "(unverified)".
