# Powertrain and chassis coding, deep dive: S54/MSS54 DME, EWS, MSS54 setup, MK60 DSC — for a US 2003 E46 325i Touring taking a 2003–06 US E46 M3 S54

Research date: 22 Oct 2026. Car: 2003 325i Touring, M54, 5-MT, RWD, Massachusetts; MS43 DME if built to 02/2003, MS45.1 from 03/2003. Donor: 2003–06 US E46 M3, manual, S54, MSS54 (to ~09/2003) or MSS54HP (after); Teves MK60 DSC. Keep the Touring's MK60/booster/master by default; fit M3 brakes, rack, LSD.

**Tags.** **(read)** = read the page/PDF/file/caption this round. **(read, earlier)** = recorded by an earlier researcher in `research_notes/` and relied on, not re-opened. **(snippet)** = search snippet only. "SGBD doc" = the community repo emdzej/ediabasx-docs-sgbd, which renders BMW EDIABAS job/table files as Markdown; not a BMW publication but its job names match jobs forum users ran. INPA prints fault locations in decimal; the SGBD in hex (0x82 = 130).

**Limits kept.** No EWS delete patch content: I deliberately exclude the circulating byte addresses/patterns and the "set 0x__" flag that two forum posts give, because the brief forbids recording immobilizer-delete patch details. Nothing here defeats or masks an emissions function or readiness monitor; the readiness notes are about completing monitors honestly. Mileage is only ever the car's true mileage.

---

## TAKEAWAY — what changes in the guide

1. **Steering-angle Tool32 job conflict is now settled.** The SGBD files show `lenkwinkel_dsc_abgleichen` exists **only** in `DSC_MK60.PRG` and `test_lenkwinkel` exists **only** in `DSC57.PRG` (Bosch 5.7). The guide's Session 7 "try the first and read the job list" can become a definite instruction: MK60 → `lenkwinkel_dsc_abgleichen`; `test_lenkwinkel` is the 325xi/330xi Bosch job, not an MK60 alternative. (read, SGBD DSC_MK60.md, DSC57.md)
2. **The "other two" MK60 compensation routines are named:** Pressure Sensors (`DRUCKSENSOR_DSC_ABGLEICHEN`, KWP $31,$20) and Lateral-Acceleration Sensor (`QUERBESCHLEUNIGUNG_DSC_ABGLEICHEN`, KWP $31,$22); steering angle is `LENKWINKEL_DSC_ABGLEICHEN` ($31,$21). Resolves an open question. (read, SGBD + BMW ST034/ST056)
3. **The Touring's own (non-M) MK60 cannot be set to `BAUART_MK60 = coupe_m/csl`** and **cannot select the M3 rack curve `wert_05`.** A real non-M MK60 dump (coding index C05) offers `BAUART_MK60` = coupe/touring/limousine/cabrio/roadster + the `_s` agility variants (touring_s, limousine_s…), and `LENKWINKELKENNLINIE_2` only `wert_10`/`wert_02`. It **does** offer the M3 brake-pressure models (`DRUCKMODELL_VORDERACHSE typ_0`, `DRUCKMODELL_HINTERACHSE typ_2`). So "set M3 values" on the Touring's own unit means hand-editing the intervention/brake parameters in NCS Dummy; it is not a `coupe_m` body-type change, and the exact M3 rack curve is not available (closest = `wert_02`). (read, bmwclubmalaysia C05 dump + liam821)
4. **MK60 has no tyre-size code.** Different M3 wheels/tyres are handled only by the flat-tyre warning's learned rolling-circumference: set correct pressures, then `RPA_RESET` (RDW reset). `REIFENDRUCKWARNSYSTEM` is just on/off. (read, SGBD DSC_MK60 `STATUS_LESEN_RPA`, `RPA_RESET`)
5. **Why one Touring's M3 MK60 never cleared 5EF1 is explainable and fixable.** The owner only wrote a blank `.man` and re-ran a PA-Soft SAS reset; he never coded the unit from a vehicle order whose production date suits the M3 unit's coding index, nor ran the INPA/Tool32 VIN-initialisation. In a parallel M3 case, setting the session VO production date to `#0902`+ made the MK60 appear and code/initialise correctly. So the fix is: code the M3 unit in an NCS session with a late-enough production date, then run INPA Shift+F4 → F1 (VIN-init + steering angle), not PA-Soft SAS alone. (read, e46fanatics 1260275; NAM3 173720, 189096)
6. **VANOS pass limits can be added** (label as owner/ISTA-derived, not BMW-published): adjustment time (`…_VERSTELLZEIT`) healthy ~180–300 ms, ISTA hard limit 500 ms; leak test (`…_DICHTHEIT`) tolerance about ±5 °KW SOLL vs IST, and `EVAN_STATUS`/`AVAN_STATUS` reading "…vorzeitig weggedriftet" = drifted = leaking; cam travel intake 0–60 °KW, exhaust 0–45 °KW. Run warm (≥85 °C). (read, NAM3 34304/529/253994/88778; BMW S54 module)
7. **Candidate US manual ("HS") WinKFP ZB numbers** for an SMG→manual flash: MSS54 ≈ **7842973** (US HS), MSS54HP ≈ **7842979** or **7842977** (US HS). These are the latest US-HS endpoints in the ISTA-CD table; verify against the car's `MSS54.HIS` daisy-chain in your SP-Daten. (read, NAM3 2052 + Bali MSS54.HIS)
8. **The system-check jobs almost certainly do NOT set an OBD readiness monitor; they test hardware and report pass/fail.** Inference from BMW ST041 (catalyst "once per trip", EVAP "every second time" during driving) + the SGBD having a separate readiness mask in `STATUS_ADAPTIONSBLOCK_26`. Still not explicitly documented. (inference)
9. **Mode 09 VIN:** BMW SI B12 09 13 confirms the state I/M tester reads the stored VIN out of an E46 DME and the fix writes the full 17-char VIN — so a US MSS54 with the full VIN written does expose it to the tester. I could not open the exact CFR/CARB mode-09 clause to byte-level confirm the 2005-MY cutoff, so keep "strongly supported" not "proven".
10. **Steering-angle job files, VANOS limits, compensation-routine names, MK60 parameter availability, and the HS ZB numbers are the main new, citable facts.** Several of the guide's "open questions to verify" can be closed or narrowed (see the final corrections section).

---

## Q1. MSS54 / MSS54HP: ident, versions, VIN write, SMG↔manual, donor check, flash risk/recovery

### Cited findings

**Reading ident and software/ZB numbers**
- `MSS54DS0.PRG` → `IDENT` returns `ID_BMW_NR` (BMW part no.), `ID_HW_NR`, `ID_COD_INDEX`, `ID_DIAG_INDEX`, `ID_SW_NR`, `ID_AI_NR` (change index), `ID_PROD_NR`, `ID_AIF_VORHANDEN` (0/1 AIF present), and MoTest flags `ID_EML` (0 none / 1 EML M70 / 2 EML M73), `ID_OBD2` (0 ECE / 1 OBD2), `ID_SG_HERSTELLER` (0 Bosch / 1 Siemens), `ID_EWS_SS` (EWS-interface identification). (read, SGBD MSS54DS0.md)
- `12MSS54.PRG` is the programming/AIF file. `AIF_LESEN` (arg `AIF_NUMMER`, 1,2,3…) returns `AIF_ADRESSE_LOW/HIGH`, `AIF_ANZ_FREI` (free AIF entries), `AIF_FG_NR` (VIN), `AIF_DATUM`, `AIF_AENDERUNGS_INDEX`, `AIF_SW_NR`, `AIF_BEHOERDEN_NR` (authority), `AIF_ZB_NR` (Zusammenbau/assembly), `AIF_SERIEN_NR`, `AIF_HAENDLER_NR`, `AIF_KM`, `AIF_PROG_NR`. (read, SGBD 12MSS54.md)
- One SGBD covers both DMEs: `MSS54DS0.prg` INFO = "MSS52/MSS54/MSS54HP fuer S54B32", rev 2.09; the DME group file `d_0012.grp` maps diag indexes 1830,1B30,1B31,1860,1B60,1B61,1B70,1B80,1B90 → `MSS54DS0`. (read, SGBD MSS54DS0.md, d_0012.md)

**MSS54 vs MSS54HP**
- Partial-read size: 32 kB = MSS54, 64 kB = MSS54HP. (read, earlier; NAM3 2052)
- Hardware numbers (NAM3 2052 version tables, "auto-parsed from the ISTA CDs"): **MSS54 HW** 7831815, 7833892, 7837941, 7842559, 7842975. **MSS54HP HW** 7834910, 7835564, 7837340, 7837805, 7842569, 7842981. (read, NAM3 2052 tables 0 and 14)
- RPM Motorsport's full supported-HW list for EWS delete: 7831815 … 7838801/7838802 (M3 MSS54/HP). A donor DME HW number outside this family is suspect. (read, rpmmotorsport delete page)

**Telling US manual ("HS") from SMG, and from Euro/Japan/SA**
- BMW's data-set/model strings in the NAM3 2052 release table (model | region | filename | "Serie…"):
  - MSS54 US **manual**: "E46 M3 US HS USOBD" A7842974.0DA (J469) and A7842972.0DA (J429); older "Serie E46M3-USOBD" A7834747 (from 09/2002), A7834745 (to 09/2002).
  - MSS54 US **SMG**: "Serie E46M3SMG-USOBD" A7834751 (to 09/2002), A7834753 (from 09/2002).
  - MSS54HP US **manual (HS)**: "E46-M3-USA-HS" A7842980.0DA, A7842978.0DA, A7843302.0DA.
  - MSS54HP US **SMG**: "E46-M3-USA-SMG" A7843304, A7843306, A7843308; "E46-M3-SMG-US" A7836366 (04/2004).
  - Euro/ROW carry ECE/EOBD/EU3/EU4/Japan/SA858/SA861 in the string; "LEV" region = US. "HS" = Handschaltung (manual). (read, NAM3 2052 table 2)
- Hardware is identical for coupe/vert/SMG/manual; only software differs; HP vs non-HP is the only year/hardware split ("Hardware differences are only related to year (HP vs non-HP). Firmware is different though"). (read, NAM3 2052, heinzboehmer)

**Writing the Touring's VIN (Tool32, `12MSS54.PRG`)** — ECUWorx verbatim and SGBD confirm:
1. Load `C:\Ediabas\ECU\12MSS54.PRG`. Run `aif_lesen` with Arguments empty/`1`; it returns the first programmed VIN + AIF data.
2. Put `2` in Arguments, run `aif_lesen` again; increment until `AIF_FG_NR` is blank. Note that slot's `AIF_ADRESSE_LOW` (ECUWorx's free slot was 3, address 7596).
3. Build an 11-field semicolon string: `AIF_ADRESS_LOW; VIN(17); date DDMMYY; AIF_AENDERUNGS_INDEX; software no.; authority no.; assembly no.; serial no.; handler no.; km; program no.` Example `7596;WBSBL12345JR12345;260216;DA;7837331;7834533;7834530;NFS01;240;0;000401`. Copy software/authority/assembly from the latest filled slot.
4. Run `seed_key`, paste the string into Arguments, run `aif_schreiben`, confirm `JOB_STATUS = OKAY`. If Error/Rejected, run `seed_key` again and retry `aif_schreiben` only.
5. Verify: `aif_lesen` arg 0; INPA → E46 → Engine → "MS S54 for S54 M3" → Coding; a generic scanner's mode-09 VIN if it has one. (read, ECUWorx AIF guide; SGBD 12MSS54.md)
- Kassel "VIN Recode to Your VIN" = $20. (read, Kassel page)
- AIF writes are finite: "limited to 14 AIF writes (AIF counter), or about 60 writes in total (general reflashes)" — don't write repeatedly. (read, NAM3 2052, NickG)

**Donor-DME check before buying** (Tool32, charger on, key II, engine off):
- `MSS54DS0.PRG` → `IDENT` (HW number in the 783xxxx M3 family; software/coding index), `FS_LESEN` (fault history), and `12MSS54.PRG` → `AIF_LESEN` 1,2,3… to see the VIN history and `AIF_ANZ_FREI` (spent AIF slots; near 0 = little headroom left).
- 32 vs 64 kB tells MSS54 vs HP; confirm manual (HS) vs SMG from the software string via INPA/WinKFP "Choose ZUSB" (Cancel to just read). (read/inference, SGBD + Bali DIY)

**SMG → manual software**
- Routes: (a) vendor conversion (Kassel "Engine Swap Coding" $349 bundles it; ask DUDMD/RPM); (b) ECUWorx MSS5x "Transmission Swap: SMG→Manual" (auto-disables SMG DTCs) applied in the same BMWFlash read/reflash as the EWS delete; (c) WinKFP ZUSB flash to a US-HS data set. (read, ECUWorx features; Kassel; NAM3 2052)
- Candidate US-HS ZB numbers (verify against your SP-Daten `MSS54.HIS`): MSS54 ≈ **7842973**; MSS54HP ≈ **7842979**/**7842977**. (read, NAM3 2052 table 3; Bali MSS54.HIS)
- Left on SMG software, the DME logs SMG-CAN faults 0x06 (Timeout SMG-CAN), 0x7B (Bus-Off lokaler SMG-CAN), possibly 0x11/0x44, and fault-type "0x30 MIL-Anforderung durch SMG" — an inspection-fail risk. (read, SGBD MSS54DS0 FARTTEXTE/FARTMATRIX)

**WinKFP ZUSB flash flow** (Bali DIY, verbatim substance): key II engine off; charger on, Windows power mgmt off; `Comfort mode` → `Update ZUSB` → family `MSS54` → `Prog ZB-Update` (it shows current + suggested, Yes) → two phases (code then data) → "programming okay"; key off, wait, key II; reset adaptations; clear codes in all CAN modules; start (may need a couple of crank/clear tries). To force a specific ZB: `Choose ZUSB` → pick ECU family + ZB → `Enter VIN` (full VIN) → `Done` → `Program`. Entering the VIN in comfort mode also writes the VIN. (read, e46fanatics 1324566, Bali)

**Flash risk & recovery**
- Partial-read method is the safe one: keep the unmodified partial read; a bad partial reflash recovers by re-flashing the known-good partial with BMWFlash. "Recovering from a bad flash after writing a bad **full** bin to the DME … is much more involved." (read, ECUWorx "how safe is flashing")
- WinKFP failure modes and recovery (E39/E46 M54, but same tool/DME family): a cancelled 2nd phase left crank-no-start + error **209 "UIF cannot be read"**; recovery is "a successful flash using WinKFP" with **all settings back to defaults**, fast-baudrate off, latency 1 ms; keep voltage ≥13.8 V. One case needed a replacement DME. A different failed MSS54 flash came back after reflashing with fast baudrate OFF, ignition off/on before retry. (read, e46fanatics 1327944; snippets e90post/bimmerforums)
- Flash-lockout counter (boot-code "feature", ~60 reflashes) and the 14-AIF limit can be reset with MSS Flasher. (read, NAM3 2052, R3Z3N/NickG)

### Inferences
- For this build: buy a **manual (HS) MSS54/HP** donor DME, EWS-delete it with the Touring VIN written in (Q2). Only if the donor is SMG do you need software conversion — prefer the vendor route or ECUWorx "Transmission Swap," because a WinKFP HS flash consumes flash-counter headroom and the exact HS ZB must be confirmed.
- Reading `IDENT` + `AIF_LESEN` on the donor before purchase both verifies family/market and shows AIF headroom; a donor already written many times (low `AIF_ANZ_FREI`) leaves little room for your VIN.

### Gaps
- Exact byte-for-byte confirmation of which ZB the WinKFP "Update ZUSB" lands on for a given US M3 HW; the HS numbers above are the table endpoints, not a flash test.
- Whether every US MSS54 software version answers mode 09 at byte level (see Q3).

---

## Q2. Immobilizer: documented virgin-DME sync, EWS3 coding, bought delete

(No patch content recorded — see the "Limits kept" note.)

### Cited findings
- **EWS 3.3 is in all E46 from start of production.** The rolling-code table is burned into the EWS at the factory and "cannot be over-written by ZCS Coding or DME alignment." A replacement DME is "off the shelf"; after programming, the next key-on makes the EWS send the whole table to the DME and reset to code #1; the DME burns it in once and is then "Married" and will not work in another car. "Alignment" only resets to code #1 and may be done an unlimited number of times. On a mismatch the DME rolls forward up to 200 codes; failure = **crank, no start** (not start-then-die). On manual cars clutch status is input directly to the DME. (read, BMW ST051 pp. 20–24)
- **Tool32 sync sequence** (worked once, on a CSL-clone MSS54HP whose ISN had been written in by BDM; the poster "wasn't sure it works with a virgin ISN"):
  1. `EWS3.prg` → `WECHSELCODE_SYNC_DME` (no args) → expect `JOB_STATUS OKAY`.
  2. `MSS54DS0.PRG` → `EWS3_INITIALISIEREN`, Arguments `0x01` (`EWS3_MODE`) → OKAY.
  3. `EWS3_SYNC` → OKAY (`EWS3_STATUS` read "reset" in the failed Touring).
  4. `EWS3_GET_STATUS` → read `EWS3_STATUS`/`EWS3_STATUS_WERT`. Fail state in the Touring case: "Invalid", value 3. (read, NAM3 145696 ValVal456; e46fanatics 1318881)
- **INPA route exists but the MSS54 key path is undocumented.** A moderator: "EWS sync should be done via INPA." Kassel's MS43 video uses "Select E46, Engine M54 MS43, **Shift+F6, F1**, start car" — that is the **M54/MS43** path, 40-second clip, not MSS54. The failed 2002 325iT used INPA "EWS3 Synch … Shift F6 … F2 Reset, F1 Store" and got "no free starting value storage space available" + "Interface error" (these texts match the **MS45** SGBD's `EWSSTART`/`EWSEMPFANGSSTATUS` tables word-for-word, implying the INPA engine script selected was the M54 one, or the MSS54 returns the same family of texts). (read, NAM3 320555; KasselPerformance video desc; e46fanatics 1318881; SGBD MS450DS0.md)
- **Why a used DME can't sync, confirmed again:** Bali — "DME and EWS are a matched/married set … otherwise you get crank no start … An EWS Delete patch of the MSS54 software gets around that." A Reddit tip to the same owner: "you can't synch the EWS and DME from different vehicles without having the DME virginized, alternatively having the DME EWS deleted." (read, e46fanatics 1318881)
- **EWS3 coding `PARK/NEUTRAL_EINGANG`:** two real E46 NCS traces (`E46-EWS.C81`) show it `aktiv` in one car and `nicht_aktiv` in another; both share `K_BUS_FREI_OHNE nicht_aktiv`, `ZEIT_BIS_AUTOM_SPERREN wert_01`, `EWS_3_SCHNITTSTELLE aktiv`. For a US manual keep `aktiv` (keeps the clutch-start interlock). Setting it `nicht_aktiv` removes the clutch interlock (lets the engine crank in gear). (read, kd7iwp & Mael-Le-Garrec GitHub traces; e46fanatics 1313143 earlier)
- **EWS3.prg status/jobs** for verifying the starter/key side: `STATUS_LESEN` → `STAT_ANLASSER_FREIGESCHALTET` (starter released), `STAT_ANLASSER_AUS_P_N` (off by P/N), `STAT_P_N_EINGANG`, `STAT_SCHLUESSEL_SENDET` (key sending), `STAT_SCHLUESSEL_GESPERRT` (barred), `STAT_SCHLUESSEL_NIO_ID/_PW/_WC` (key ID/password/rolling-code not OK), `STAT_EWS_JUNGFRAEULICH` (EWS virgin), `STAT_DME_LEITUNG_FREI`. `ISN_LESEN` reads the EWS's 16-bit ISN; `FGNR_SCHREIBEN` writes the 17-char VIN into the EWS. (read, SGBD EWS3.md)
- **DME side of the handshake:** `MSS54DS0.PRG` → `STATUS_DIGITAL` → `STAT_EWS3_FREIGABE` (EWS release); fault 0x82 (130, "EWS-Signalmanipulation") with sub-types 0x10 Startwert defekt / 0x11 Wechselcode verloren / 0x12 Startwert leer / 0x13 Manipulation; fault 0x42 (66, "EWS-Schnittstelle"). (read, SGBD MSS54DS0 FARTMATRIX/FARTTEXTE)
- **Bought-delete service — what the owner sends/gets:**
  - **DUDMD** $215 bench / $225 remote (remote mails you a keep-it OBD2 cable; Windows 8+; "in some rare cases remote doesn't work" → bench). Provide full VIN; print and mail the repair form with a bench DME. Lists MSS54 (2000–03) and MSS54HP (2004–06). Notes legal/insurance implications and that the EWS module may still carry the clutch switch for ABS/cruise. (read, dudmd page)
  - **Severn** $100 (if you own a flashing tool) or $200 with "Shipping"; "off-road use only"; one EWS delete per ECU. (read, severn page)
  - **RPM Motorsport** "Ready to start" delete $300; 1–2 business days on arrival; overnight both ways; supported-HW list 7831815…7838802. Separate "used DME EWS programming" $300. (read, rpm pages)
  - **Kassel** EWS delete $109; VIN recode $20; "Engine Swap Coding (any/all options, full consult)" $349; optional $429 core; MSS54 & MSS54HP; return postage for working cores. Store lists only **MS43** virginize ($142) — no MSS54 virginize listed Oct 2026. (read, kassel page/store, earlier)
  - After return: fit, key II, `FS_LESEN` — 130 (0x82) may remain unless the "tampering DTC delete" was applied; the engine still starts with it. Read the VIN back with `AIF_LESEN`. (read, NAM3 38046 HoDoo)
- **Documented Touring sync failures:** (A) 2002 325iT, donor DME not virginized — INPA refused the job, Tool32 reported OKAY but `EWS3_GET_STATUS` stayed Invalid/3, 130 remained; fitting the **donor EWS + key** and re-running the Tool32 sync cleared the EWS fault, but the car stayed crank-no-start with "fuel pump relay error code 1" and all six injectors disabled (thread ended there). (B) 03/2001 325xi wagon with a Kassel-virginized 2003.5 MSS54 — "start value not understood"; couldn't reset either. (read, e46fanatics 1318881, 1300465)

### Inferences
- Recommended: **buy the delete** with the Touring VIN written in; keep the Touring EWS/keys/ring antenna and the clutch wire to EWS pin 8; don't jumper pins. The sync route needs a vendor-virginized DME and still has a real failure rate; it is not cheaper or more certain than the delete.
- If a **virginized** DME is chosen, the Tool32 sequence above is the documented attempt; run it with a charger on, key II, and be ready to fall back to the donor EWS or a delete. The INPA path for the MSS54 remains unproven, so Tool32 is the practical tool.
- The donor-EWS route carries two keys and the donor VIN; useful only as a test/fallback.

### Gaps
- A first-hand, start-to-finish success syncing a **virginized** MSS54 to a different E46's EWS3. None found; the one solved case used BDM-written ISN.
- The INPA "MS S54 for S54 M3" EWS-sync key layout and whether it has its own sync page.
- Whether a left-over 130 (0x82) commands the MIL (see Q3).

---

## Q3. After first start: throttle (EDR) adaptation, idle, VANOS, misfire, readiness, mode 09

### Cited findings
- **BMW throttle/pedal rule:** "the ADAPTATIONS MUST BE CLEARED and ADAPTATION PROCEDURE MUST BE PERFORMED … If this is not performed, the vehicle will not start, or run in 'fail-safe' mode." (read, BMW ST041 EngineElectronics Pt1 p.15)
- **Pre-drive check** (every KL15-on, 3 phases): phase 1 throttles closed (EDR pot zero read), phase 2 opened 3% (throttle-shaft pot read), phase 3 opened ~20% then EDR off, springs close them — "a mechanical clicking sound can be heard." "The full load adaptation stop is learned in a new ECM the first time KL15 is recognized." **Post-drive check:** "10 seconds after KL15 is switched OFF the EDR actuator is opened 102% … renewed full load adaptation … only carried out when the engine is turned off before reaching operating temperature." (read, BMW ST041 Pt1 pp.16–17)
- **Tool32 jobs** (`MSS54DS0.PRG`): `ADAPT_LOESCHEN` (clear all adaptations, no args), `ADAPT_SELEKTIV_LOESCHEN` (arg `STATUS_ADAPT`), `FS_LOESCHEN`, `SG_RESET` ("Adaptionen/FS nicht gesichert!"). Verify in `STATUS_ADAPTIONSBLOCK_06`: `STAT_WDK_ADAPT_WERT` "Zustand Drosselklappenadaption mit 0 = ok", plus `STAT_PWG1/2_A0_WERT`, `STAT_WDK1/2_A0_WERT` (zero positions), `STAT_WDK_MAX_DIFF_ADAPT_WERT`, `STAT_PWG_MAX_DIFF_ADAPT_WERT`. `STATUS_ADAPTIONSBLOCK_06` also holds the learned-equipment flags `STAT_KKOS_ST_VERBAUT_WERT` (A/C), `STAT_FGR_MFL_VERBAUT_WERT` (cruise), `STAT_EKP_CFG_VERBAUT_WERT` (pump type), `STAT_LDPH_VERBAUT_WERT` (DM-TL heater) — they relearn after an adaptation clear. (read, SGBD MSS54DS0.md)

**`STAT_EKP_CFG_VERBAUT_WERT` — the fuel-pump-control config value (coordinator's lead):**
- It is a result of the Tool32 job `STATUS_ADAPTIONSBLOCK_06` in `MSS54DS0.PRG`, type unsigned int, SGBD comment "**welche EKP wurde verbaut**" (which fuel-pump control/EKP is fitted). It sits in the learned-"verbaut" group with the A/C, cruise (FGR) and DM-TL-heater flags. (read, SGBD MSS54DS0.md line 3809)
- **What it reads back:** an unsigned integer that encodes which pump control the DME thinks is present (US PWM pump module vs. Euro relay). **The SGBD gives no decode table/enum for its specific values**, so which integer means "relay" vs "EKP module" is **untested** — record the raw number on the donor (Phase 1, M3 wiring) and again on the swapped car and compare, rather than assume a meaning.
- **Which job sets it:** it is a *learned* flag, not a coded one — there is no write job for it. The DME relearns it after `ADAPT_LOESCHEN` (the whole "verbaut" group relearns on an adaptation clear), so its value is only trustworthy after a clear + a run. No NCS/coding parameter selects it. (read/inference, SGBD; BMW ST041 says clearing adaptations relearns fitted equipment)
- **Dealer-tool exposure:** Tool32 exposes it directly by running `STATUS_ADAPTIONSBLOCK_06` (one of ~60 results). Whether INPA's "MS S54 for S54 M3" script, DIS or ISTA show it on a *labelled* page is **not documented** — INPA/DIS read the same adaptation block, but no source names a screen field for it. (read SGBD; inference)
- **Relation to the stored pump-relay fault 0x01/1 "Relais Kraftstoffpumpe":** consistent with, and the likely mechanism behind, George Hill's description — "The S54 DME has two fuel pump outputs, one for the US EKPS cars and one for the Euro Relay cars … this DOES leave a shadow code for the Fuel Pump Relay (shows in ISTA/INPA but not on a generic scan tool) but does not set the CEL." Running the Touring's K96 off the Euro relay output while the US software's learned/expected config is the EKP module is a plausible cause of the harmless shadow 0x01. **Marked inference:** the SGBD does not state that a mismatch between `STAT_EKP_CFG_VERBAUT_WERT` and the wiring sets 0x01, so treat the causal link as unconfirmed; after an `ADAPT_LOESCHEN` the DME relearns the fitted config and 0x01 may re-store on the next cycle regardless. (read, fuel_pump_control.md George Hill / e46fanatics 1307461 p.2; SGBD MSS54DS0.md)
- **Idle/trims:** `STATUS_LFR` (idle-controller adaptation), `STATUS_LAMBDA_ADD_1/_2` (additive offset, ms), `STATUS_LAMBDA_MUL_1/_2`, `STATUS_N_LL_SOLL`. BMW: additive adaptation at idle/low load, multiplicative at higher load; ">0.0 ms the ECM is trying to richen." (read, SGBD; BMW ST041 Pt3 p.74)
- **VANOS jobs** (warm engine): `STEUERN_LLS_TESTDREHZAHL` raises idle for the test; `STEUERN_EVANOS1_VERSTELLZEIT` / `STEUERN_AVANOS1_VERSTELLZEIT` return `E/AVAN_VERSTELLZEIT_FRUEH` and `_SPAET` in **ms**; `STEUERN_EVANOS1_DICHTHEIT` / `STEUERN_AVANOS1_DICHTHEIT` return `E/AVAN_ISTWERT`, `_SOLLWERT` (Grad KW) and a text `E/AVAN_STATUS`; `…_FRUEHANSCHLAG` / `…_SPAETANSCHLAG` drive to the advance/retard stops. S54 = one bank, use the "1" jobs. (read, SGBD MSS54DS0.md)
  - **Procedure that works without DIS** (Tomba, confirmed by others): open `mss54ds0.prg`, select `STEUERN_EVANOS1_VERSTELLZEIT`, click the `1=>` (run) button; idle rises, engine sounds odd; result is a time in ms. `…_FRUEHANSCHLAG` forces the advance stop (target ~70° while max is 60 ±2°); `…_SPAETANSCHLAG` the retard stop (target −10° while 0 ±2° reached); `…_DICHTHEIT` checks the position is held. A ready-made `.tst` test file runs all eight in sequence (F8) and prints SOLL/IST. (read, NAM3 34304)
  - **Pass values (owner/ISTA-derived, NOT BMW-published):** adjustment time healthy ~180–300 ms, "under 500 ms acceptable" (ISTA limit 500 ms); one healthy car 195–235 ms both cams. Leak tolerance ±5 °KW SOLL vs IST; `…_STATUS` "…vorzeitig weggedriftet" (drifted away prematurely) = leaking (worn seals/valve block/sealing plate); a ~5 °KW exhaust deviation failed and ~3.9 °KW passed on a warmer retest. Run only when warm (≥85 °C/185 °F); leaks shrink as the engine warms. VANOS oil pressure spec 100 bar (BMW S54 module says the 100-bar regulating valve; owners target ~115 bar at the regulator). Cam travel: intake 60°, exhaust 45° (BMW). (read, BMW S54 module; NAM3 529/253994/88778/34304)
- **Misfire / smooth running:** `STATUS_SYSTEMCHECK_LAUFUNRUHE` returns per-cylinder roughness in % (physical cylinder order, not firing order 1-5-3-6-2-4); `LESEN_SYSTEMCHECK_LAUFUNRUHE` the crank-wheel segment deviation. `STATUS_ADAPTIONSBLOCK_16` holds per-cylinder misfire counters (lifetime + driving-cycle) and `STAT_LU_ST_WERT` (0 off / 1 idle / 2 misfire detection active / 4 adaptation). BMW: emissions window 1000 rev, catalyst-damage window 200 rev; crank-wheel adaptation during decel fuel cut-off needed for full sensitivity, else "misfire detection is less sensitive." (read, SGBD; BMW ST041 Pt3 pp.68–69,77)
- **Crank-wheel adaptation:** `STATUS_ADAPTIONSBLOCK_06` → `STAT_LU_ADAPT1…6_WERT` (segment deviation ppm) and `STAT_LU_ADAP_CNT_WERT` (work cycles) rising with coast-downs in gear; `STATUS_GEBERRAD_ADAPTION` as a direct read. (read, SGBD)
- **Readiness:** `STATUS_ADAPTIONSBLOCK_26` → `STAT_FF_FF_RDY_WERT` (readiness mask), `STAT_FF_FF_DCY_CNT_WERT` / `_WUC_CNT_WERT` (driving/warm-up cycles since reset), `_DCY_CLR_WERT` (since fault clear), and `STAT_FF_FF_RDY_CNT0…15_WERT` (per diagnostic-function counts). (read, SGBD)
- **System-check vs readiness (the open question):** the SGBD exposes `START_SYSTEMCHECK_SEK_LUFT`+`LESEN_SYSTEMCHECK_SEK_LUFT` (SLS, "1_SLS_OK"), `START_SYSTEMCHECK_DMTL`+`LESEN_SYSTEMCHECK_DMTL` (LDPSTATUS text, e.g. "32_ERGEBNIS_DECKEL_DICHT/33_GROB_DICHT/34_FEIN_DICHT" sealed; "35_DECKEL_FEHLT/36_GROBLECK/37_FEINLECK"; many "WARTEN_…" waits incl. "8_WARTEN_FUELLSTAND" and aborts "48/49_REFERENZSTROM_HI/LO", "50_VERSTOPFT", "53_EKP_CRASH_OFF"), `STATUS_TANK_DICHTHEIT` (`LDP_STROM` vs `LDP_REFSTROM`), `STEUERN_TEV_CHECK` ("16_ERGEBNIS_TEV_OK"). These are "Funktionsüberprüfung" (function checks) returning pass/fail; the OBD readiness mask sits in a different block (`…_26`) updated by the real monitors during driving (catalyst "once per trip", EVAP "every second time"). **Inference: the system-check jobs test hardware and report pass/fail; they do not flip the OBD readiness bit.** (read SGBD + BMW ST041 Pt3; inference — still not explicitly documented)
- **Mode 09 VIN:** BMW SI B12 09 13 (E46, to 12/2006): the state I/M test/OBD scan tool reads the VIN "stored in the DME"; when only the last 7 digits were written the tester "may read out WBAAA00000A123456"; the fix is to reprogram the full 17-char VIN and verify on the DME ident page. So an E46 DME with the full 17-char VIN written does report it to the tester. (read, BMW SI B12 09 13). A California MSS54-swap sedan "coded to the chassis VIN and reflected as a 330i … passed CA smog … All my monitors show as ready except EVAP." (read, e46fanatics 1303447 — note passing as a 330i hides the engine change)
- **Throttle-body synchronisation after an actuator swap** (only if you replace/disturb the EDR actuator): MotoIQ's stock-hardware M3 needed two TB syncs plus finally a new actuator to cure a 3-second EML shutdown; dealer/AEM software does the sync. For this build the M3 actuator comes with the M3 engine untouched, so normally only an adaptation clear + relearn is needed, not a sync. (read, MotoIQ pt8; Pelican note, snippet)

### Inferences — assembled first-start sequence
1. Charger on, key II engine off. `IDENT`, `FS_LESEN`, save.
2. `ADAPT_LOESCHEN`, then `FS_LOESCHEN`.
3. Key off ≥15 s (post-drive check runs on the cold engine). Key II, listen for the phase-3 throttle click.
4. `STATUS_ADAPTIONSBLOCK_06` → `STAT_WDK_ADAPT_WERT = 0`.
5. Start without touching the pedal; idle to temperature watching `STATUS_LFR`, `STATUS_LAMBDA_ADD_1/2`, `STATUS_N_LL_SOLL`.
6. Warm: `STEUERN_LLS_TESTDREHZAHL`, then the four VANOS `…_VERSTELLZEIT`/`…_DICHTHEIT` jobs (bank 1). Compare ms/°KW to the limits above and the donor's Phase-1 baseline.
7. Drive with several closed-throttle in-gear coast-downs 3,000–5,000 rpm; `STAT_LU_ADAP_CNT_WERT` should climb.
8. Re-check trims and `STAT_VAN_ADAP_ST_WERT` bits (bit0 intake, bit1 exhaust adapted).

### Gaps
- Exact BMW ms/°KW VANOS limits (owners/ISTA give ~300 ms / ±5°; no BMW number found).
- Byte-level confirmation that a US MSS54 answers mode 09 (TSB strongly implies it; CFR/CARB clause not opened).
- Explicit statement that `START_SYSTEMCHECK_*` does/does not set a readiness bit (inference only).

---

## Q4. MK60 DSC: coding with M3 brakes/rack/LSD/wheels, VIN init, steering-angle & compensation routines

### Cited findings
**Which unit / wheel-speed sensors**
- US fitments: 323/328 MK20; 325i/Ci/330i/Ci MK60; 325xi/330xi Bosch 5.7; M3 MK20 to 09/2002 then MK60. From 09/2001 the non-M MK60 and (09/2002+) M3 MK60 use the CAN "sensor cluster" (combined yaw + lateral accel, 12 V, CAN); 09/2000–08/2001 MK60 uses the old MK20 3-wire analog yaw/accel sensors and lacks the later rack data. (read, e46fanatics 1282261; BMW ST056; e46fanatics 1264623 blarf)
- MK20→MK60 wheel-speed plugs differ (front pin-3 ground unused on MK60); swap the connector housings, pins the same. (read, NAM3 189096)

**Coding the Touring's own MK60 toward M3 values — what is actually available**
- NCS codes every MK60 from one rule file (`E46.MK60.C12` on M3-index units) that selects M3 values only when the VO says `S54B32`; a Touring VO (`M54B25`, `TOUR`) yields 325i values. (read, liam821)
- **Real non-M MK60 dump, coding index C05** (2002 318i, NCS Dummy): `BAUART_MK60` options = coupe, touring, limousine(sedan), cabrio, roadster, roadster/c, compact_s, coupe_s, touring_s, limousine_s, cabrio_s (no `_m`/`csl`). `DRUCKMODELL_VORDERACHSE` = typ_0/typ_1; `DRUCKMODELL_HINTERACHSE` = typ_0/typ_1/typ_2; `LENKWINKELKENNLINIE_2` = only wert_10/wert_02; `MOTOR_ART_DSC_2` = m43…m54 family only (no s54b32 on this index); `GETRIEBE` = handschaltung/automatik/sequentiell_*; `REIFENDRUCKWARNSYSTEM`, `TRAKTIONDIFFERENZREGELUNG`, `SPERRDIFFERENZREGELUNG`, `LOGIK_HA_SPERRE`, understeer/oversteer `…_MUE_*_2`, `UNTERSTEUERSCHWELLE_2`, `GEARMOMENTREGLER_*_HA_2`, `VOLUMENDURCHFLUSSPARA_2` all present. (read, bmwclubmalaysia C05 dump)
- **liam821 target values read from real cars** (330i ZHP / M3 std / M3 ZCP): `BAUART_MK60` limousine_ms/coupe_m/csl; `MOTOR_ART_DSC_2` m52b20/s54b32/s54b32; `LENKWINKELKENNLINIE_2` wert_02/wert_05/wert_04 ("02=ZHP, 05=M3 std, 04=ZCP"); `DRUCKMODELL_HINTERACHSE` typ_2/typ_2/typ_3; `DRUCKMODELL_VORDERACHSE` typ_1/typ_0/typ_0; `LOGIK_HA_SPERRE` nicht_aktiv/aktiv/aktiv; `SPERRDIFFERENZREGELUNG` aktiv/nicht_aktiv/nicht_aktiv; `TRAKTIONDIFFERENZREGELUNG` aktiv/nicht_aktiv/aktiv; `REIFENDRUCKWARNSYSTEM` nicht_aktiv/aktiv/aktiv; `DTC_LAMPE` nicht/nicht/aktiv; `DBC_MIN_AUSLOESEDRUCK` wert_01/wert_03/wert_03. (read, liam821)
- A non-M MK60 run with CSL values by hand works: thegenius46m set CSL intervention values on a ZHP non-M MK60 via NCS Dummy, left `BAUART_MK60 = limousine_ms`; Bry5on's S54 **wagon** "worked on both the non-m and M3 MK60 … much better with m-track mode and M3 settings." S54B32 warns units have different internal "mappings" and only some part numbers can be flashed; but hand-setting NCS parameters is not a flash. (read, NAM3 172815 p.2)
- Coding-index history: early 325 units CI01; 04–09/2001 330 units CI03 (-291/-292) added the `_s` BAUART variants; "going from 'touring' to 'touring_s' (not available on CI01) seems to be the trick" for the faster rack. (read, e46fanatics 1264623 blarf)
- **No tyre-size parameter.** Wheel/tyre differences are handled by the flat-tyre warning (RDW/RPA): `STATUS_LESEN_RPA` exposes DRUCKSCHWELLE_GROB/FEIN per speed band, MOMENTEN/KURVEN-KOMPENSATION and `LERNZAEHLERSTAND`; `RPA_RESET` re-teaches after you set correct pressures. `REIFENDRUCKWARNSYSTEM` is only on/off. (read, SGBD DSC_MK60.md)

**Steering ratios (for choosing LENKWINKELKENNLINIE):** M3 total steering gear ratio **15.4:1** (BMW); 330i ZHP ~13.7:1 (forum). So an M3 rack wants `wert_05` on an M3 (C12) unit; a non-M MK60 lacking wert_05 is set to its closest, `wert_02`. (read, BMW ST041 RunningGear p.6; forum snippet)

**VIN into an M3 MK60 (Option B)**
- PA-Soft (BMW Scanner 1.4) → ABS/DSC → Reprogramming → "Write FGSTNR", enter the 14 characters after "WBA". (read, LM Auto Repairs caption, on a 2003 E46 diesel)
- Tool32 alternative: `DSC_MK60.PRG` → `IDENT_VIN_SCHREIBEN` (arg `FG_NR`, an 18-char string, last char a dummy, e.g. `WBAAX71010JR25000` + dummy), or `C_FG_AUFTRAG`. Read back with `IDENT_VIN` (returns `FG_NR` 14-char WBA-prefixed) or `C_FG_LESEN`. (read, SGBD DSC_MK60.md)
- "You don't directly code the VIN" via NCS — VIN comes from a dedicated job; NCS coding reads the VO from cluster/LSZ. If NCS can't connect because cluster/LSZ are absent, load a virtual VO via an `.ssd` file. (read, e46fanatics 1286178; NAM3 232995)

**NCS coding an M3 MK60 into the Touring (Option B), heinzboehmer/ECUWorx step list:**
- NCS Expert → Load manipulation profile → VIN/ZCS/FA → ZCS/FA f. ECU → E46 → read VO from AKMB or ALSZ → Enter FA → add `$7MA` (M Track) if wanted → delete the production date, add `#0902` (any late-enough date) → Back → Process ECU ALSZ `FA_WRITE` → Change ECU AKMB `FA_WRITE` then `SG_CODIEREN` → Change ECU MK60 `SG_CODIEREN`. Then READ ECU the MK60, edit `FSW_PSW.TRC`→`.MAN`: non-ZCP brakes `DRUCKMODELL_HINTERACHSE typ_2`; non-ZCP rack `LENKWINKELKENNLINIE_2 wert_05`; convertible `BAUART_MK60 cabrio_m`; no M-track LED `DTC_LAMPE nicht_aktiv`; `SG_CODIEREN`. (read, NAM3 189096 post #3; ECUWorx M-Track.pdf)
- If NCS won't list MK60 or rejects "Codierindex … nicht zulässig": the session VO production date is too early for the unit — use `#0902`+; the real fix in one case was correcting the VO date (VIN was a red herring). (read, NAM3 173720, 189096; e46fanatics 1293250)

**Steering-angle calibration + the three compensation routines**
- INPA: E46 (F3) → Chassis → DSC MK60 → **Shift+F4 (Compensation Routines)** → wheel dead straight → **F1 (Compensation Steering Angle / Initialisation VIN-Nr)** → accept the warning (a fault is flagged if the wheel is >30° off centre) → "initialization complete." Verify: F5 status → read analog → read DSC sensor (F2) → steering angle 0° straight ("if it says two or three then it's not calibrated"). Run **all three** compensation routines wheel-straight, no brake pressure, car level & stationary; clear codes in all modules; cycle ignition; recheck. The other two routines are **Pressure Sensors** and **Lateral Acceleration Sensor** (confirmed on an MK60: "Only 'Pressure Sensors' and 'Lateral Acceleration Sensor'"). (read, 50sKid caption 33:47; Evan Goyuk caption; madstig 1275927; e46fanatics 1216321; NAM3 189096)
- SGBD mapping (Tool32 fallback, `DSC_MK60.PRG`): `LENKWINKEL_DSC_ABGLEICHEN` ($31,$21) steering angle; `DRUCKSENSOR_DSC_ABGLEICHEN` ($31,$20) brake-pressure-sensor offset; `QUERBESCHLEUNIGUNG_DSC_ABGLEICHEN` ($31,$22) lateral-acceleration offset. `test_lenkwinkel` is **not** in this file — it is only in `DSC57.PRG` (Bosch 5.7). `STATUS_SENSOREN_OFFSET` reads the stored offsets (`STAT_OFFSET_LENKWINKEL/QUERBESCHLEUNIGUNG/DREHRATE/DRUCKSENSOR_1/_2`); `STATUS_CAN_LWS_1_LESEN` → `STAT_LENKWINKEL_WERT` + `STAT_ID_LWS` (confirms the SAS is coded). (read, SGBD DSC_MK60.md, DSC57.md)
- BMW: adjustment/initialisation required when replacing the DSC unit, replacing/re-coding the SAS, replacing one/both brake pressure sensors, or replacing the lateral-acceleration sensor; and after steering/suspension work. A swapped SAS "had never been coded" → code with NCS, cycle key, then Tool32 calibrate (Tool32 had given IFH-0009 before coding). A SAS stuck at "!1440" that jumps back after reset = failed sensor. (read, BMW ST034 Pt13/14 Workshop Hints; e46fanatics 1282261, 1287151)
- INPA pump-bleed (used/dry unit): Chassis → DSC MK60 → F6 Activate → F1 Control Hydraulic → F2 FL/RL, F3 FR/RR; press pedal **hard** (not the "80 %" the screen says), open bleeder, pump pulses, close when INPA finishes; 2–3× per corner; ~1.25 L fluid; finish with a conventional bleed. (read, madstig 1275927; Z4-forum 146558 earlier)

**Why the M3 MK60 never cleared 5EF1 in one Touring, and what fixes it**
- Wagon #1: S54 + M3 MK60 + M3 cluster; PA-Soft reported 5EF1, INPA "VIN not initialized, initiate LWS calibration"; VINs in DSC/LWS/cluster all matched; owner coded a **blank .man** to cluster and DSC and recalibrated SAS **with PA-Soft**; no change. Fix was refitting the 325i MK60. A member noted "the M3 MK60 controls the LSD or at least electronically assists it." (read, e46fanatics 1260275)
- **Inference (well-supported):** the blank-.man default-code does not necessarily load valid M3-index coding, and PA-Soft SAS reset ≠ the INPA/Tool32 VIN-initialisation routine. In the parallel M3 case, the unit only coded/initialised once the session VO production date was late enough for the unit's coding index. So the likely fix for an M3 MK60 in a Touring: (1) write the car VIN to the MK60 (PA-Soft/Tool32), (2) code it in an NCS session using a VO with `#0902`+ production date (and, to get M3 values, a type code that yields `S54B32` for that session only, no `FA_WRITE`), (3) run INPA Shift+F4 → F1 (VIN-init + steering angle) then the other two routines. If it still won't initialise, refit the Touring MK60 (the documented cure).

### Inferences — build decision
- **Option A (recommended, per the guide): keep the Touring MK60.** Its VIN already matches, so only the steering-angle/compensation routines are needed after the alignment. It accepts the M3 brake-pressure models (VA typ_0, HA typ_2) and `touring_s` (faster-rack agility) on a C03/C05+ index, but **not** the exact M3 rack curve `wert_05`; leave it at defaults unless you deliberately hand-tune, because it is a safety system. Confirm the unit's coding index first (BMW Scanner header "CI").
- **Option B (M3 MK60):** must be VIN-written and coded from a late-enough VO; set M3 values by hand (`DRUCKMODELL_HINTERACHSE typ_2`, `LENKWINKELKENNLINIE_2 wert_05`, leave `BAUART_MK60` at coupe_m — no Touring value exists), then initialise.

### Gaps
- The exact coding index of the 2003 325i Touring MK60 (34516765453) and whether it carries `touring_s`; the C05 dump is a 2002 318i. Check the unit's CI with BMW Scanner.
- No first-hand M3-MK60-into-Touring success coded step-by-step (only sedans/wagons with sedan shells).

---

## Q5. Session order, dependencies, decision points, recovery

### Dependency logic
- **S1 Backup (Phase 0)** must precede everything: it is the only way back. Save VO/ZCS, every module's `FSW_PSW.TRC`, cluster+LCM EEPROM, mileage photos, all fault memories, DSC identity.
- **S2 DME delete/VIN (Phase 1 read, Phase 3 bench)** must happen before first power-up: the DME won't run without the EWS delete (or a working virgin sync). Independent of cluster/DSC.
- **Wire + checks** before S3–S6.
- **S3 EWS** after the DME is back and wired: with a delete there's nothing to sync, just verify starter/key/clutch; with a virgin DME, sync here.
- **S4 Cluster VIN** must precede **S5 DSC**: the DSC checks its VIN against the cluster's; 5EF1 won't clear until the cluster carries the car VIN.
- **S5 DSC** after S4; initialise VIN+steering angle; but the **final** steering-angle zero waits for **S7** (after the loaded-ride-height alignment).
- **S6 First start/adaptations (Phase 12)** after the engine runs; re-do after any wiring or VO change.
- **S7 Steering angle** after the wheel alignment.
- **S8 VO options / S9 lights** last, each tested on a running car; any VO change → re-code DSC/LCM/GM5/IHKA as needed and re-reset DME adaptations (S6).

### Decision points
- **Immobilizer route** decides S2/S3: delete (recommended) → S3 is a check; virgin sync → S3 runs the Tool32 sequence; donor EWS → fit + re-align, carry two keys.
- **DME is SMG?** → add manual (HS) software/transmission-swap in S2.
- **DSC choice** decides S5: Option A (Touring MK60) → VIN already matches, calibrate only; Option B (M3 MK60) → VIN-write + code from late VO + set M3 values + initialise.
- **MS43 vs MS45.1 Touring** decides the wiring (not the coding sessions) — but the cluster lamp-switch coding (`CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN`, `TOG_UEBER_CAN` = nicht_aktiv) is the same for both.

### Recovery paths
- **S2 bad partial flash:** reflash the saved known-good partial with BMWFlash → DME back to prior state. **Bad full-bin flash:** much harder; vendor/BDM or replacement DME. **WinKFP hang/209:** settings to defaults, latency 1 ms, fast-baudrate off, boot-sector-update off, voltage ≥13.8 V, retry; worst case replacement DME. Flash-counter lockout → MSS Flasher reset.
- **S3 lost sync / 130 stays:** re-read the DME to confirm the delete took (or ask the vendor); for a virgin DME re-run the Tool32 alignment (unlimited times per BMW); fall back to the donor EWS+key; the 130 alone, after a confirmed delete, still starts.
- **S4 cluster:** tach stuck at 9,000 rpm after a blank code to a changed-index cluster → write back the EEPROM backup. Tamper dot → make the cluster VIN/mileage match the LCM (never write the LCM).
- **S5 wrong coding:** write back the saved `.man`/default; M3 MK60 won't initialise → refit the Touring MK60 (documented cure).
- **S6 adaptations:** if a clear leaves it rough/no-start, re-clear and relearn on a charger; one unverified report of a "soft-brick" clearing adaptations in INPA, so keep the charger on (prefer Tool32 `ADAPT_LOESCHEN`).
- **S7 steering angle:** Tool32 IFH-0009 → SAS not coded, code with NCS then retry; stuck "!1440" → replace the SAS and calibrate the new one.

---

## GUIDE-READY — step-by-step for Sessions 2, 3, 5, 6, 7

Conventions: charger on every session; one program at a time; key position 1 = electrics on/engine off, 2 = run, unless a job needs the engine running.

### Session 2 — DME VIN, EWS delete, gearbox software (Phase 1 read; Phase 3 bench/vendor)
**Read the donor DME first** (Tool32, key 2, engine off):
1. `MSS54DS0.PRG` → `IDENT` (record `ID_BMW_NR`, `ID_HW_NR`, `ID_COD_INDEX`, `ID_SW_NR`; HW should be in 7831815…7838802) and `FS_LESEN`; save.
2. `12MSS54.PRG` → `AIF_LESEN` arg 1,2,3… Record each slot's VIN/SW/authority/assembly, `AIF_ANZ_FREI`, and the first blank `AIF_FG_NR` with its `AIF_ADRESSE_LOW`.
3. Confirm MSS54 vs HP (32/64 kB partial read, or HW number) and manual (HS) vs SMG (software string via INPA/WinKFP "Choose ZUSB", Cancel to read).

**Order the delete** (vendor; Phase 3): send the DME (bench) or keep the cable (remote). Give the full 17-char VIN; add manual/HS or "transmission swap" if the donor was SMG; order the tampering-DTC delete; decline every emissions delete and Euro flash. Vendors/prices: Kassel $109 + $20 VIN (or $349 swap coding), DUDMD $215/$225, Severn $100/$200, RPM $300.

**DIY VIN write** (after any delete, Tool32 `12MSS54.PRG`): build the 11-field string (Q1), run `seed_key`, paste, run `aif_schreiben` → `JOB_STATUS OKAY`; verify `aif_lesen` arg 0 + INPA Coding. Don't write repeatedly (14-AIF limit).

**SMG→manual** (only if donor SMG): vendor conversion, or ECUWorx "Transmission Swap" with the delete, or WinKFP ZUSB to US-HS (MSS54 ≈7842973, MSS54HP ≈7842979/7842977 — verify in SP-Daten).

**Expect:** your VIN in the AIF; starts with your EWS/key; 130 (0x82) may remain unless the tampering DTC was deleted.
**Fix fails:** reflash the saved partial read (bad partial flash); WinKFP defaults + latency 1 ms + boot-sector-update off + fast-baudrate off (hang/209); MSS Flasher for the flash-counter lockout.

### Session 3 — EWS (Phase 11)
**After a delete** (nothing to sync):
1. Confirm your saved EWS coding has `PARK/NEUTRAL_EINGANG = aktiv`; leave it.
2. `EWS3.prg` → `STATUS_LESEN`, key in, clutch down: key sending, not barred, all "NIO" bits 0; `STAT_ANLASSER_AUS_P_N = 0`; cranking → `STAT_ANLASSER_FREIGESCHALTET = 1`.
3. `MSS54DS0.PRG` → `FS_LESEN`: 130 (0x82) may be stored; `STATUS_DIGITAL` → `STAT_EWS3_FREIGABE` shows release. Don't jumper EWS pins.

**Virgin-DME sync** (only route that works for an un-deleted used DME, vendor-virginized):
1. `EWS3.prg` → `WECHSELCODE_SYNC_DME` → OKAY.
2. `MSS54DS0.PRG` → `EWS3_INITIALISIEREN`, Arguments `0x01` → OKAY.
3. `EWS3_SYNC` → OKAY.
4. `EWS3_GET_STATUS` → `EWS3_STATUS` should not read "Invalid"/value 3 (that was the documented failure).
5. `FS_LESEN`: 130 gone; `STATUS_DIGITAL` → `STAT_EWS3_FREIGABE`. Key off ≥10 s, start.
Read 130's sub-type to steer: Startwert leer (virgin, run sync) / Wechselcode verloren (re-align) / Manipulation (married — delete, virginize, or donor EWS) / 66 (0x42) interface (check the EWS–DME line or a module was unplugged key-on).

### Session 5 — DSC coding and VIN (Phase 11, after Session 4)
**Option A — Touring's own MK60** (recommended):
1. INPA → E46 → Chassis → DSC MK60 → F4 → F1 read: after a cluster change expect 5EF1 "VIN not initialized."
2. Shift+F4 → F1 (steering angle + VIN-init), wheel straight → "initialization complete."
3. Run the other two compensation routines (Pressure Sensors; Lateral Acceleration Sensor), wheel straight, no brake pressure, car level.
4. F4 → F2 clear → F1 read: no faults; clear all modules, cycle ignition, re-read.
   (Optional, advanced: with the M3 brakes/rack fitted you may hand-set `DRUCKMODELL_VORDERACHSE typ_0`, `DRUCKMODELL_HINTERACHSE typ_2`; the M3 rack curve `wert_05` is not available on a non-M index — leave `wert_10`/set `wert_02`. Safety system: change only if you understand each value.)

**Option B — M3's MK60** (donors 09/2002+):
1. Write the car VIN: PA-Soft → ABS/DSC → Reprogramming → Write FGSTNR (14 chars after WBA); or Tool32 `DSC_MK60.PRG` → `IDENT_VIN_SCHREIBEN` (18-char, last char dummy).
2. NCS: read VO from AKMB → Enter FA → set production date `#0902`+ (and, for M3 values, a type code that yields `S54B32` for this session only, no `FA_WRITE`) → Process ECU MK60 → `SG_CODIEREN` ("coding active"/"coding ended").
3. If MK60 isn't listed or "Codierindex … nicht zulässig": the VO date is too early — fix it (`#0902`+) and retry.
4. Set M3 values via `CODIERDATEN_LESEN` → edit `.MAN` → `SG_CODIEREN`: `MOTOR_ART_DSC_2 s54b32`, `LENKWINKELKENNLINIE_2 wert_05`, `DRUCKMODELL_VORDERACHSE typ_0`, `DRUCKMODELL_HINTERACHSE typ_2`, `LOGIK_HA_SPERRE aktiv`, `REIFENDRUCKWARNSYSTEM aktiv` (no Touring `BAUART_MK60`; leave coupe_m).
5. Initialise as in Option A 1–4.

**Fallback (Tool32)** if INPA lacks the MK60 page: `DSC_MK60.PRG` → `LENKWINKEL_DSC_ABGLEICHEN` (not `test_lenkwinkel`, which is Bosch 5.7's `DSC57.PRG`).
**Flat-tyre warning after M3 wheels:** set pressures, then `RPA_RESET` (there is no tyre-size code).
**Expect:** DSC/brake lamps out; no 5EF1/5E1F.
**Fix fail:** M3 MK60 that never clears 5EF1 → refit the Touring MK60.

### Session 6 — First start, adaptations, throttle check (Phase 12)
1. Key 2 engine off: `MSS54DS0.PRG` → `IDENT`, `FS_LESEN`, save.
2. `ADAPT_LOESCHEN`, then `FS_LOESCHEN`.
3. Key off ≥15 s (cold post-drive check), key 2, listen for the phase-3 throttle click.
4. `STATUS_ADAPTIONSBLOCK_06` → `STAT_WDK_ADAPT_WERT = 0`.
5. `STATUS_DIGITAL` in gear, parking brake on: `STAT_KRAFTSCHLUSS_EIN = 1` clutch up, `STAT_KUP_EIN = 1` clutch down (in neutral both are fixed — one input via the gear switch); `STAT_BLS_EIN`/`STAT_BLTS_EIN` follow the brake; `STAT_FDYN_EIN` the Sport button.
6. Start without touching the pedal; idle to temperature watching `STATUS_LFR`, `STATUS_LAMBDA_ADD_1/_2`, `STATUS_N_LL_SOLL`.
7. Warm: `STEUERN_LLS_TESTDREHZAHL`, then `STEUERN_EVANOS1_VERSTELLZEIT`, `STEUERN_AVANOS1_VERSTELLZEIT`, `STEUERN_EVANOS1_DICHTHEIT`, `STEUERN_AVANOS1_DICHTHEIT`. Targets (owner/ISTA, not BMW): adjustment ~180–300 ms (≤500 ms), leak ±5 °KW and `…_STATUS` not "weggedriftet"; compare to the donor baseline.
8. Drive with closed-throttle in-gear coast-downs 3,000–5,000 rpm; `STAT_LU_ADAP_CNT_WERT` rises.
**Expect:** steady idle, trims near zero, all four VANOS jobs complete, no new faults.
**Fix fail:** re-clear/relearn on a charger; check `STAT_WDK_ADAPT_WERT`, throttle sensors/pedal/actuator (EML 3-second shutdown chain). Re-run after any wiring or VO change.

### Session 7 — Steering angle after the alignment (Phase 12)
1. Car level, wheel dead straight, key 1/2, no brake pressure.
2. INPA → E46 → Chassis → DSC MK60 → Shift+F4 → F1 → accept warning (>30° off = fault) → "initialization complete." Run the other two routines (Pressure Sensors, Lateral Acceleration).
3. Verify: F5 → read analog → read DSC sensor (F2) → steering angle 0°.
4. Clear all modules, cycle ignition, re-read.
**Tool32 fallback:** `DSC_MK60.PRG` → `LENKWINKEL_DSC_ABGLEICHEN`.
**Fix fail:** IFH-0009 → code the SAS with NCS, cycle key, retry; stuck "!1440"/5E43 returning → replace SAS, calibrate the new one.

---

## DIAGRAM-READY DATA

### Session order with dependencies (nodes → edges)
- S1 Backup (Phase 0) → S2 DME (Phase 1 read / Phase 3 bench) → [Wire + power-up checks] → S3 EWS → S4 Cluster VIN → S5 DSC → S6 First start/adaptations → [Wheel alignment] → S7 Steering angle → S8 VO options → S9 Lights.
- Hard prerequisites: S4 before S5 (DSC checks cluster VIN); S2 before first power-up; S6 before S7 narrative-wise but S7 waits for the alignment; any S8 VO change loops back to re-code DSC/LCM and re-run S6 adaptation reset.

### Decision points (diamonds)
1. Immobilizer route? → {Delete: S3=check} / {Virgin sync: S3=Tool32 sequence} / {Donor EWS: fit+align, 2 keys}.
2. Donor DME SMG? → {Yes: add HS/transmission-swap in S2} / {No: keep software}.
3. DSC unit? → {Touring MK60: VIN matches, calibrate only} / {M3 MK60: VIN-write + code from `#0902` VO + M3 values + initialise}.
4. MS43 or MS45.1 Touring? → wiring branch only (coding identical).

### Recovery paths (dashed back-edges)
- S2 → bad partial flash → reflash saved partial (BMWFlash) → S2 ok.
- S2 → WinKFP hang/209 → defaults+latency 1 ms+boot off+fast-baud off → retry; else vendor/replace DME.
- S3 → 130 persists / sync Invalid → re-read DME (confirm delete) / re-align (unlimited) / donor EWS.
- S4 → tach stuck 9000 → write back EEPROM backup.
- S5 → M3 MK60 won't init → refit Touring MK60.
- S7 → IFH-0009 → NCS-code SAS → retry; "!1440" → replace SAS.

### Steering-angle / compensation job map (table)
| Routine | INPA (DSC MK60) | Tool32 `DSC_MK60.PRG` | KWP | When |
|---|---|---|---|---|
| Steering angle + VIN-init | Shift+F4 → F1 | `LENKWINKEL_DSC_ABGLEICHEN` | $31,$21 | DSC/SAS swap, steering/suspension work, alignment |
| Pressure sensors | Shift+F4 → (2nd) | `DRUCKSENSOR_DSC_ABGLEICHEN` | $31,$20 | DSC unit or a brake-pressure sensor replaced |
| Lateral acceleration | Shift+F4 → (3rd) | `QUERBESCHLEUNIGUNG_DSC_ABGLEICHEN` | $31,$22 | DSC unit or lateral-accel/sensor cluster replaced |
| (Bosch 5.7 only) | — | `DSC57.PRG` → `test_lenkwinkel` | — | 325xi/330xi, not MK60 |

### MK60 parameter availability (non-M coding index C05 vs M3 index C12)
| Parameter | Non-M (C05) options | M3 std (C12) | M3 rack/brake target |
|---|---|---|---|
| `BAUART_MK60` | coupe/touring/limousine/cabrio/roadster + _s variants (touring_s…) | coupe_m / csl | coupe_m (no Touring value) |
| `LENKWINKELKENNLINIE_2` | wert_10, wert_02 only | wert_02/04/05 | wert_05 (M3 rack) — N/A on C05 |
| `DRUCKMODELL_VORDERACHSE` | typ_0, typ_1 | typ_0 | typ_0 |
| `DRUCKMODELL_HINTERACHSE` | typ_0, typ_1, typ_2 | typ_2 | typ_2 (non-Comp) / typ_3 (Comp) |
| `MOTOR_ART_DSC_2` | m43…m54 only | s54b32 | s54b32 — N/A on C05 |
| Tyre size | none (use RPA_RESET / REIFENDRUCKWARNSYSTEM) | — | — |

---

## Corrections to the guide's current statements

1. **WIRING-AND-CODING.md Session 7 table:** "`lenkwinkel_dsc_abgleichen`. One guide gives `test_lenkwinkel` in the same file … try the first and read the job list." — **Correction:** the SGBD files show `test_lenkwinkel` is **not** in `DSC_MK60.PRG`; it is only in `DSC57.PRG` (Bosch 5.7, 325xi/330xi). For the MK60 use `lenkwinkel_dsc_abgleichen` definitively; madstig's note conflated the two files. (read, SGBD DSC_MK60.md / DSC57.md)

2. **README DSC section / WIRING Session 5 note "There's no Touring value for `BAUART_MK60` on the M3 unit; ECUWorx gives `cabrio_m` … nothing for a Touring."** — Add: the **non-M (Touring) MK60** has no `coupe_m`/`csl` either; its `BAUART_MK60` list is coupe/touring/limousine/cabrio/roadster plus the `_s` agility variants, so "set M3 values" on the Touring's own unit is hand-editing the brake/intervention parameters (it does accept `DRUCKMODELL_HINTERACHSE typ_2`), **not** a body-type change, and the M3 rack curve `wert_05` is not selectable (closest `wert_02`). (read, bmwclubmalaysia C05 dump)

3. **README "Open questions": "The names of the other two MK60 compensation routines …"** — **Resolved:** Pressure Sensors (`DRUCKSENSOR_DSC_ABGLEICHEN`) and Lateral Acceleration Sensor (`QUERBESCHLEUNIGUNG_DSC_ABGLEICHEN`). (read, SGBD + e46fanatics 1216321 + BMW ST034)

4. **README "Open questions": "The US manual-gearbox ('HS') data-set numbers …"** — **Narrowed:** candidate US-HS ZB numbers MSS54 ≈ 7842973, MSS54HP ≈ 7842979/7842977 (verify against the car's `MSS54.HIS`). "HS" = Handschaltung; the ISTA-CD table labels US manual "…-USA-HS"/"E46 M3 US HS" and US SMG "…-USA-SMG". (read, NAM3 2052; Bali MSS54.HIS)

5. **WIRING "Whether these checks set a monitor to 'ready' or only test the hardware isn't documented."** — Can be sharpened to an inference: the `START_SYSTEMCHECK_*`/`LESEN_SYSTEMCHECK_*` jobs are "Funktionsüberprüfung" routines that return pass/fail; the OBD readiness mask is a separate field (`STATUS_ADAPTIONSBLOCK_26` → `STAT_FF_FF_RDY_WERT`) that the real monitors set during the drive cycle, so the service jobs most likely test hardware only and do not flip a readiness bit. Still label it inference. (read, SGBD + BMW ST041 Pt3)

6. **README "Open questions": "Whether the US MSS54 reports its VIN to generic OBD-II scanners (mode 09)."** — **Narrowed to "strongly supported":** BMW SI B12 09 13 shows the state I/M tester/OBD scan tool reads the VIN out of an E46 DME and the fix writes the full 17-char VIN, so an MSS54 with the full VIN written reports it to the tester. Byte-level mode-09 confirmation and the exact CARB/CFR model-year cutoff were not opened. (read, BMW SI B12 09 13)

7. **WIRING Session 6 step 7 "We found no specification for the results"** — Add owner/ISTA figures (clearly not BMW-published): adjustment-time ~180–300 ms, ISTA hard limit 500 ms; leak-test tolerance ≈ ±5 °KW and a drift/"weggedriftet" status = leak; run warm (≥85 °C); cam travel intake 60°/exhaust 45° (BMW S54 module). (read, NAM3 34304/529/253994; BMW S54 module)

8. **README/WIRING "If it fails: an M3 MK60 that never clears 'VIN not initialized' … was cured by refitting the Touring's own unit."** — Keep the cure, but add the likely cause and a prior remedy: the failed owner only wrote a blank `.man` and reset the SAS in PA-Soft; the documented path is to write the car VIN, code the unit from a VO whose production date (`#0902`+) suits the unit's coding index, then run the INPA Shift+F4 → F1 VIN-initialisation (not PA-Soft SAS alone). (read, e46fanatics 1260275; NAM3 173720/189096)

9. **WIRING Session 3 "Kassel's 'Shift + F6, F1' is for an MS43"** — Confirmed from the video description: that clip is "Select E46, Engine M54 MS43, Shift + F6, F1, Start car" — an M54/MS43 sync, 40 s long; not transferable to the MSS54. (read, KasselPerformance video description)

10. **README DSC "the M3 … total gear ratio"** (if a ratio is ever cited): BMW ST041 gives the M3 steering total gear ratio **15.4:1** (pump 120 bar, 11 L/min, no hydraulic limit stops). Supports using the M3 rack curve (`wert_05`) when the M3 rack is fitted to an M3-index MK60. (read, BMW ST041 RunningGear p.6)
