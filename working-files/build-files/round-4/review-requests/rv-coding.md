# rv-coding: round-4 review of WIRING-AND-CODING and the coding steps elsewhere

Scope: my 80 fragments (most of WIRING; README 0140, 0260, 0420, 0560, 0570, 0590, 0600, 0620; Cards 3f, 11a, 11b, 12e; the worksheets' electronics, coding and readiness sections), the captions of figures 06, 12, 20, 26, 38–41, and the guide-wide hard-limits check.

## Checked

- About 150 facts on the changed lines: job and result names, fault codes, pins, coding values and indexes, rules and their order, part numbers, version numbers and the sources they cite. I grepped all four preview pages for each value and for the old values it replaced.
- 9 spot-checks at the source, plus one local read of BMW's data:
  - SGBD `EWS3`: `FGNR_LESEN` "Auslesen der Fahrgestellnummer aus der EWS"; ZCS jobs; no FA job. So the EWS holds a VIN but no vehicle order.
  - SGBD `12MSS54`: `AIF_SCHREIBEN` argument `AIF_KM` = "Kilometerstand".
  - SGBD `KOMBI46R`:
    - `STATUS_AIF_TANKDATEN_LESEN` gives `STAT_TANKINHALT_HEBEL1/2_WERT` in litres, and there's no `STATUS_TANKINHALT_LESEN`;
    - `STATUS_IO_LESEN` → `STAT_OELDRUCK_EIN`;
    - `STATUS_AIF_FG_NR_LESEN`, `STATUS_AIF_GWSZ_LESEN`, `C_FG_LESEN` and `SIA_RESET` exist;
    - the `STEUERN_LEUCHTE` BYTE3 bits are as quoted;
    - the cluster holds the FA (`C_FA_LESEN`, `C_FA_AUFTRAG`).
  - SGBD `LSZ_2`:
    - `SIA_LESEN` `FG_NR` is 7 characters and `GESAMTWEGSTRECKE_WERT` counts in 100 km;
    - `XENON_VORHANDEN` and `LWR_VORHANDEN` exist;
    - the level-sensor voltages read 0–5 V;
    - fault locations 0x1F, 0x21–0x24, 0x41 and 0x42 are as quoted;
    - `STEUERN_IO` takes `REL_NSW`;
    - `C_FG_AUFTRAG` writes the FG number.
  - SGBD `DSC_MK60` (raw file):
    - all three compensation jobs, `RPA_RESET`, `IDENT_VIN_SCHREIBEN` (18 characters), `STATUS_SCHALTER` bits and `IDENT` → `ID_COD_INDEX` exist; there's no `TEST_LENKWINKEL`;
    - 5E59, 5E1E, 5E40, 5E43, 5E20, 5E21 and 5E24 are as quoted;
    - **0x5E1F is "VIN nicht initialisiert, LWS-Abgleich durchfuehren", and the file has no 5EF1.**
  - SGBD `MSS54DS0` (raw file): every job and result name the guide uses exists, among them:
    - "1_SLS_OK", "16_ERGEBNIS_TEV_OK", `STAT_FF_FF_RDY/DCY/WUC/RDY_CNT0_WERT`, `STAT_EKP_CFG_VERBAUT_WERT`, "8_WARTEN_FUELLSTAND", "48_/50_ABBRUCH_…", `STAT_VAN_ADAP_ST_WERT`, `EWS3_*`, `STAT_EWS3_FREIGABE`, `STAT_MFL1_EIN`;
    - fault 0x82 is "EWS-Signalmanipulation", 0x42 "EWS-Schnittstelle", 0x6E the Sport LED, 0x51 the MFL line and 0x60 radiator-outlet plausibility.
  - WDS `E46_PA6000L` (MSS54): X60004 pin 33 "Electronic vehicle immobilisation", pin 27 "Data link MFL", plus pins 1, 11, 15, 16, 18, 20, 21, 30 and 34 as the guide has them.
  - TIS 34 00 050, both pages: 2 bar; "restarted on each wheel"; "Run bleeding routine with DIS with bleeder valve open. After completing the routine, press brake pedal 5 times … Close bleed valve."
  - 13 CCR 1968.2(g)(4.8.1): the VIN over the OBD port is required from "2005 and subsequent model year" vehicles.
  - BMW `E46CVT.000` (the gap-fill's extracted copy, read-only): the rule group `LSZ_M3undAllrad` is there; the gap-fill decoded its values.
- WebSearch calls used: 0.

## Brief items

1. **Levelling curves (Session 9).** The "read `wert_01` in every trace seen" wording was already gone: Session 9 gave BMW's M3 values. It lacked the `ALLRAD` case that README 0519 sends xi owners to, and its step 3 put the rear sensor "on your Touring's axle", against the M3 rear axle the guide fits and step 6's "both sensors on M3 suspension". **Fixed in 0560:**
   - rear sensor on the rear axle you fit, with the shared sensor and rod numbers (ETK);
   - a 325xi bullet: the order gives `wert_02`, `wert_01`, `wert_02`, `wert_02`. Converted to rear drive, set the M3 values; kept on all-wheel drive with the xi's own axles, leave them;
   - the table row and WORKSHEETS 0410 row 9 now say "for your axles".
2. **AW33.** No coding step depends on it:
   - EN33 appears only for 2003 FA cars;
   - 0519 ties the VIN to the type key only from 09/2001, and rv-plan has since added the pre-09/2001 caveat.
   - No change.
3. **Bleed.**
   - **WIRING 0520:** rewritten BMW-first (34 00 048 and 34 00 050 as two bullets, then BMW's at-wheel sequence). The "two or three times, then a conventional bleed" and Z4 tips now sit under "Owners' tips, not BMW's procedure".
   - **WIRING 0670:** the "spongy pedal" row now gives BMW's 34 00 050 routine and leak test.
   - **README 0420 step 13:** also ended "Then bleed conventionally again"; now BMW-first, with a pass check pointing to README 0530 step 6.
4. **EWS and VIN.** The EWS3 job file confirms the EWS holds a VIN and no FA. Now said in:
   - README 0590 (with `FGNR_LESEN`);
   - WIRING 0471;
   - figure 41's caption.
   - The drawing fix is F1 below.
5. **Confirmed:** WIRING 0520 says "yellow BRAKE"; WIRING 0500's fault table says "X60004 pin 33 (EWS data line)", and WDS agrees.
6. **Hard limits, all four pages:**
   - no EWS patch bytes, addresses or EEPROM steps (the delete appears only as a vendor service or ECUWorx's licensed function; the ISN/BDM mention reports one owner's case);
   - nothing defeats or masks emissions or readiness;
   - refrigerant is always recovered;
   - every odometer path leads to the true mileage;
   - airbag notes intact.
   - One tightening: Session 2's AIF write had the `AIF_KM` ("Kilometerstand") field as 0 in the example. **Fixed (0490):** enter the car's true reading in km.

## Fixed in my fragments (other than the above)

- **P1, WIRING 0330:** it still called US M3 headlight washers "an open question". Gap 7 closed it as option 502, not standard. Fixed, and now in step with WIRING Session 8, README 239 and WS 223.
- **P2, 5E1F against 5EF1:** BMW's job file prints 5E1F for "VIN not initialized"; 5EF1 is one owner's PA-Soft reading.
  - 5E1F now leads in WIRING 0470, 0520 step 1, 0640 and 0670.
  - The "5EF1 or 5E1F" pairs elsewhere stay.
- **P2, WIRING 0670:** the "nicht zulässig" row gave only the date. It now adds the type-key rule (M3 unit: an M3 type key and a date from 09/2002; non-M: neither `S54B32` nor `ALLRAD`) and the xi `$203` step. The "never clears" row now adds the M3 type key.
- **P2, WIRING 0650 (Won't start):** question 4 and the two figure captions now include the brief fire that never catches (EWS-to-DME). Before, a builder could take it for "starts, then dies", which the figure calls "not the immobilizer".
- **P2, WIRING 0520 Option B:** the 325xi line. This is rv-plan's R1, sent by the coordinator. **Applied in substance; declined its rationale clause.** "BMW's coding data admits no non-M MK60 index for an `ALLRAD` order" is true, but Option B codes the M3 unit, index C06, whose rule is `PU02 AND S54B32` with no `ALLRAD` term (`gapfill_coding_body.md`, gap 1 table). Applied text: "On a 325xi converted to rear drive, also delete `$203` (all-wheel drive) from the session order, as the guide's [325xi section](README.md#route-1-code-the-mk60-from-an-xi-order) explains."
- **P3:**
  - WIRING 0090: "ULEV-II group (UL2)" → "LEV II ULEV group (UL2)", as the xi notes' EPA table has it.
  - WIRING 0610: "they don't set readiness" softened to our inference, to match WIRING 0600 and README 0620.
  - The vendor-matched used DME (README 0590 route 2) carried into README 0420 step 10, README 0560's route table, WIRING 0470's choices table, Card 3f and figure 06's caption.

Found and already fixed by rv-chassis while I worked: README 0610 "Coding by hand" said an M3 MK60 "gets 325i values" from the Touring's order. BMW's rule refuses it outright.

## Conflicts

- **5E1F against 5EF1:** BMW's job file against forum and PA-Soft readings. I treat 5E1F as the code and mention 5EF1 once in Session 5 step 1.
- **rv-plan R1's reasoning:** see above. The `ALLRAD` exclusion governs non-M MK60 indexes only.

---

### R1: README 0610__dsc-brakes-and-steering-angle.md: name BMW's code next to the owner's 5EF1 (P3, rv-chassis)
- **Change:** replace
- **Find (exact current text):**
  > The S54 wagon whose M3 unit never cleared 5EF1, "VIN not initialized",
- **New text:**
  > The S54 wagon whose M3 unit never cleared 5EF1 (5E1F in BMW's job file), "VIN not initialized",
- **Why:** the `DSC_MK60` job file lists 0x5E1F "VIN nicht initialisiert, LWS-Abgleich durchfuehren" and has no 5EF1 ([SGBD documentation](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/DSC_MK60.md), checked at source). The manual now leads with 5E1F.

### R2: research.md (no fragment; coordinator): three stale MK60 points (P3)
- **Change:** replace (three finds, lines 199 and 201 of `$G/research.md`)
- **Find 1:**
  > NCS hides the M3 MK60 until the FA's production date is late enough
- **New text 1:**
  > NCS hides the M3 MK60 until the session order's production date is late enough and its type key is an M3's (BMW's rule for the M3 unit, index C06: `PU02 AND S54B32`)
- **Find 2:**
  > first shows 5EF1 "VIN not initialised"
- **New text 2:**
  > first shows 5E1F "VIN not initialised" (one owner's PA-Soft showed it as 5EF1)
- **Find 3:**
  > (one guide names `test_lenkwinkel` instead, so read the job list)
- **New text 3:**
  > (`test_lenkwinkel`, which one guide gives, is the xi's Bosch DSC 5.7 job, in `DSC57.PRG`)
- **Why:** `gapfill_coding_body.md` gap 10 (C06 rule); the `DSC_MK60` and `DSC57` job files. WIRING Sessions 5 and 7 already say all three.

## Figure fixes (for the diagram makers)

### F1: `41-identity-storage.svg`: the EWS holds your VIN (P2)
- **What's wrong:** the EWS box says only that it holds no vehicle order. README 0590 and the EWS3 job file (`FGNR_LESEN`) say it holds a VIN. The caption now says "Your EWS holds your VIN too, but no vehicle order."
- **Exact fix:**
  - In the EWS box (visible text "EWS  yours" … "backup copy."), add a line: "holds your VIN, but no vehicle order (from 09/2001)".
  - In the `aria-label`, change "Your EWS holds no vehicle order on a car built from 09/2001, so it is no backup copy." to "Your EWS holds your VIN but no vehicle order on a car built from 09/2001, so it is no backup copy."

### F2: `39-flow-dsc-coding.svg`: step 4 omits the type key; 5E1F (P2)
- **What's wrong:**
  - Step 4 says "… nicht zulässig"? The date / is too early: a later one in 2, …". The text (Session 5 step 4) says the date is too early or the type key isn't an M3's: fix both.
  - The figure also leads with 5EF1, while BMW's job file prints 5E1F.
- **Exact fix:**
  - Step 4 visible text: "The date is too early, or the type key isn't the donor's M3 one (BL93, BR93): fix both in 2 and retry".
  - `aria-label` step 4: change "the date is too early, so enter a later one and retry" to "the date is too early or the type key isn't the donor's M3 one, so fix both and retry".
  - Change "expect 5EF1, "VIN not initialized"" (visible and `aria-label`) to "expect 5E1F (5EF1 in some tools), "VIN not initialized"".

### F3: `25-flow-no-start.svg` and `25-flow-no-start-2.svg`: the brief fire belongs to question 4 (P2)
- **What's wrong:** both tell a reader whose engine "starts, then dies" that it isn't the immobilizer. A brief fire that never catches is the EWS-to-DME refusal (README 0590, WIRING 0500 and 0650; NAM3 2025). WIRING 0650's text and captions now say so.
- **Exact fix:**
  - **25-flow-no-start**:
    - Change "Starts, then dies: see the next figure. An immobilizer / mismatch gives crank-no-start instead (question 4)." to "Runs a few seconds, then dies: see the next figure. An immobilizer mismatch gives crank-no-start, or a brief fire that never catches (question 4)."
    - In question 4, add "(it may fire once or twice)".
    - Make the same changes in the `aria-label`.
  - **25-flow-no-start-2**: after "Not the immobilizer's signature: … ignores the code", add "Exception: a brief fire while cranking that never catches is an EWS-to-DME refusal (question 4)". Make the same change in the `aria-label`.

### F4: `40-flow-ews-recovery.svg`: question 2 (P3)
- **What's wrong:** the question reads "It cranks: is fault 130 …". WIRING 0500 step 2 says "It cranks, and may fire once or twice, but never runs". The caption now says so.
- **Exact fix:** change "2   It cranks: is fault 130 (0x82) or 66 (0x42) stored, or" to "2   It cranks, perhaps firing once or twice: is fault 130 (0x82) or 66 (0x42) stored, or". Make the same change in the `aria-label`.

### F5: `12-coding-order.svg`: Session 5 option B, Session 2 routes, Session 1 tools (P3)
- **What's wrong:**
  - Option B reads "write your VIN, code M3 values / by hand, then initialise". Session 5 codes the M3 unit from a session order with the donor's type key and #0902 or later first, then sets values for your parts.
  - Session 2's choice omits README 0590's vendor-matched used DME.
  - Session 1 now also uses Tool32 (VIN and mileage).
- **Exact fix:**
  - Option B: "write your VIN, code from a session order (donor's type key, #0902+), set values for your parts, then initialise".
  - Session 2 alternative: "a used DME matched to your EWS by a vendor, or virginized and synced by you".
  - Session 1 tools: "NCS Expert, PA-Soft, INPA, Tool32".
  - Make the same changes in the `aria-label`.

### F6: `38-flow-coding-sessions.svg`: immobilizer route (P3)
- **What's wrong:** "sync the virgin DME, or fit the …" and, in the `aria-label`, "or a virginized DME, which no Touring has documented working" omit the vendor-matched used DME (README 0590 route 2; WIRING 0470's table now names it).
- **Exact fix:** in the `aria-label`, replace "or a virginized DME, which no Touring has documented working" with "or a used DME matched to your EWS by a vendor (once, in a 330i) or virginized and synced yourself (no Touring success)". In the Session 3 box, "after a delete or a vendor's match, a check; with a virgin DME, the sync, or …".

### F7: `06-electronics.svg`: DME label (P3)
- **What's wrong:** "or virginized and synced". The caption now reads "or matched to your EWS, by a vendor or by your own sync".
- **Exact fix:** change the visible line "or virginized and synced" to "or matched to your EWS". In the `aria-label`, change "or virginized and synced to your EWS" to "or matched to your EWS by a vendor or by your own sync".

### F8: `26-flow-warning-lights.svg`: code order (P3)
- **Exact fix:** change "VIN not initialized (5EF1, 5E1F)" (visible and `aria-label`) to "VIN not initialized (5E1F; 5EF1 in PA-Soft)".

Figure 20 matches the text: switch 61316901592; 61316925498 is the non-DSC unit.
