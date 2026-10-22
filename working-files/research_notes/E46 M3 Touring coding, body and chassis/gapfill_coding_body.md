# Gap-fill: body-module coding (M3 cluster, donor coding, light module and the rest)

Gap-filling round after Round 4, 22 Oct 2026. Researcher: `coding-body-gaps`. Source notes: `coding_body_modules.md` (same folder).

**The car:** US 2003 E46 325i Touring (M54, manual, RWD, DSC). **The donor:** US 2003–06 E46 M3, manual.

## How this round got its answers

Earlier rounds could not read BMW's own coding data, so the main gaps rested on forum reports. This round read it.

- **BMW's E46 coding data (SP-Daten V32).** The archive.org item [SP DATEN V 32](https://archive.org/details/sp-daten-v-32) holds a partial torrent archive ([resume.tar.gz](https://archive.org/download/sp-daten-v-32/resume.tar.gz)) of BMW's coding data. Its `SP-DATEN V32/E46/daten/` folder is complete. Its file list matches the item's [SP-DATEN_V32.torrent](https://archive.org/download/sp-daten-v-32/SP-DATEN_V32.torrent).
  - I streamed the archive, saved only the E46 data files, and stopped the download once that folder had passed.
  - `E46AT.000` is dated `DATUM 22.01.2007`.
  - These are the same files every NCS Expert install keeps in `C:\NCSEXPER\DATEN\E46\`.
- **What I read:**
  - `E46SGVT.000`: which coding index each module family may have, for a given vehicle order.
  - `E46SGET.000`: which coding file and SGBD go with each module.
  - `E46CVT.000`: what NCS codes from each order option.
  - `E46AT.000` and `E46ZST.000`: type keys, option codes and production-date words.
  - The module files: `KMBE46M3.C20–C24`, `KMB_E46.C02–C08`, `LSZ.C26–C37`, `GM5.C02`, `C04`–`C06`, `MRS3.C31`, `MRS4_16.C29/C32`.
  - The keyword dictionaries: `SWTASW06`, `SWTFSW06` and `SWTPSW06`.
- **How I read them:**
  - The binary files were decoded with my own read-only parser, written to the [ncsx DATEN format notes](https://github.com/emdzej/ncsx/blob/main/docs/daten-format.md). The predicate grammar is from [ncsx ecu-selection §6](https://github.com/emdzej/ncsx/blob/main/docs/ecu-selection.md).
  - The text files were read directly.
  - Scripts are in `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/gapfill-scripts/coding-body-gaps/`. The extracted files are in `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/gapfill-dl/coding-body-gaps/ia-sp-daten-v-32/extract/`.
- **Check of the method.**
  - I evaluated BMW's `E46CVT.000` rules for a Canadian xenon sedan order and compared the result with a real factory light-module trace (kd7iwp's original `LSZ.C35`, Canadian: `SPRACHE kanada`).
  - The order used: `E46 LIM M54B30 LL US KANADA TAGFAHRLICHT XENON NEBELSCHEINW`, plus the #0303 date words.
  - Result: **all 311 of 311 functions match** ([kd7iwp](https://github.com/kd7iwp/BMW-Coding/tree/master/E46)).
  - So the factory values computed below for the US Touring and the US M3 can be trusted. They remain computations, though, not reads from a car.
- **Owners can repeat this.** NCS Dummy can disassemble any DATEN file to plain text. Its comments resolve `AUFTRAGSAUSDRUCK` lines into option names. For example: "AUFTRAGSAUSDRUCK : !(S00F7,S00F8) // !(M5,M6)" ([Revtor, NCS Dummy manual §4.1.1](https://revtor.be/ncsdummy/ncsdummy.pdf)).

**Tags.**
- **[read]:** I read the text or file myself. For BMW binary data this means my decode of the file.
- **[snippet]:** a search snippet only.
- **[earlier round]:** carried over from `coding_body_modules.md`.
- **Inference:** my own reasoning.
- **Computed:** BMW's rules evaluated by my script for an order I assembled.

**Keywords used in BMW's rules:**
- `S54B32`: the S54 engine, set by M3 type keys.
- `M54B25`: the 325i engine.
- `TOUR`, `COUP`, `CABR`, `LIM`: body styles.
- `PU01`: built from 09/2001.
- `PU02`: built from 09/2002.
- `MAERZ03` and `MAERZ04`: built from 03/2003 and from 03/2004.

---

## 1. Summary

| Gap | Status | Answer in one line | Best source |
|---|---|---|---|
| 1. Cluster acceptance | **Closed** from BMW's data; one harmless read on the car confirms it | No. An M3 cluster (index 22, 23 or 24) is admissible as AKMB only when the session order has `PU01 AND S54B32`. A 325iT order (`EN33`, `M54B25`) fails, so NCS will refuse it, and `FA_WRITE` of your order into it is very likely refused too | BMW `E46SGVT.000` / `E46SGET.000` (SP-Daten V32) [read] |
| 2. Lamp-switch values | **Closed** | The three switches exist only on indexes 07, 08, 23 and 24. The rules are the same for 23 and 24 and depend on the build date. US M3: `TOG_UEBER_CAN` = `aktiv`, `CAN_OELDRUCKSCHALTER` = `nicht_aktiv`, `GENERATOR_UEBER_CAN` = `nicht_aktiv` before 03/2004 and `aktiv` from 03/2004 | BMW `E46CVT.000`, `KMBE46M3.C23/C24` [read] |
| 3. Tailgate and rear glass | **Narrowed** | The redesign cluster has one rear-lid LED and four door LEDs, and no door or lid coding at all. The GM5 reads separate tailgate and rear-glass contacts but broadcasts one rear-lid bit. Whether the rear glass lights that LED, and whether an M3 cluster has rear-door LEDs, is a 10-minute Tool32 test | KOMBI46R and ZKE5 SGBDs; wilhelm-docs 0x7A [read] |
| 4. Light-module read-out | **Closed as a computed reference** (no real US halogen dump found) | A 2003 US halogen 325iT `LSZ.C36` computes to `VARIANTE_LSZ` = `wert_02`, `LAENDERVARIANTE_LSZ` = `wert_02`, `SIDEMARKER_US` = `aktiv`, the levelling functions `nicht_aktiv`, `KALTUEBERWACHUNG_AL` = `aktiv`, and `GED_FL_ALS_DRL` = `nicht_aktiv`. All 324 functions are in the appendix | BMW `E46CVT.000`, checked 311/311 against a real trace [read + computed] |
| 5. Level-sensor curves | **Closed** | BMW codes the M3 `KENNLINIE_LWR_SENSOR_VO` = `wert_03`, `_HI` = `wert_02`, `DEF_LWR_SENSOR_HI` = `wert_03` and `OFFSET_LWR` = `wert_03`. Every RWD non-M body (the Touring included) gets `wert_01` for all four | BMW `E46CVT.000` group `LSZ_M3undAllrad`; `LSZ.C36/C37` [read] |
| 6. Fog lights | **Closed** for coding | Option `$520` (NEBELSCHEINW) changes nothing in the light module. It only switches the GM5's heated washer jets (cars from 03/04). Front fogs need the fog-variant light module, the fog button panel and relay K47, not an order change | BMW `E46AT.000`, `E46CVT.000`; ETK [read] |
| 7. Headlight washers | **Closed** (code); **narrowed** (US fitment) | The code is **502**, keyword `SWA`, "Scheinwerfer-Waschanlage" (ETK `S502A`). Its only coding effect is GM5 `SCHEINWERFERREINIGUNG` = `aktiv`. The US M3 type key has no `SWA`, and its ETK splits parts by S502A Yes/No, so washers were an option on US M3s, not standard | BMW `E46AT.000`/`E46CVT.000`; ETK US M3 [read] |
| 8. Seat occupancy | **Narrowed** | E46 airbag coding has no OC3 setting. The Touring's module family is MRS3 (`C31`), or MRS4 at index `C32`, according to the module. Tool32 `AUSSTATTUNG_LESEN` shows SBE, SBE2 or OC3. Seat-back-lock monitoring is coded on convertibles only, so M3 coupe seats need no seat-back coding. The year split is still open | BMW SGET/CVT/MRS files; MRS3 and MRS4 SGBDs [read] |
| 9. Switch unit | **Closed** (ETK) | A DSC-equipped US 325iT uses the separate "Switch DSC" 61316901592. The console unit 61316925498 that the guide calls "your 325i's" is ETK's non-DSC unit (S210A No). The DSC console unit 61316925512 is listed for the US sedan, not the US Touring | ETK via bmwfans [read] |
| 10. Coding data and type keys | **Closed** (type keys); **narrowed** (data version) | US type keys: 325iT `EN33` (09/01–05/06; `AW33` 09/00–08/01), M3 coupe `BL93`, M3 convertible `BR93`. V32's E46 data (2007) has `KMBE46M3.C20–C24` and `LSZ.C26–C37`; a January 2001 data set had only `C20/C21` | BMW `E46AT.000`, `E46ZST.000`, V32 file list; zcs_all/fzgident [read] |

---

## 2. Gap by gap

### Gap 1. Will NCS Expert accept a US M3 cluster (index 23/24) with a 325iT vehicle order?

#### Cited findings

**BMW's admissibility table** [read] ([E46SGVT.000](https://archive.org/download/sp-daten-v-32/resume.tar.gz), block `AUFTRAGSAUSDRUCK`: SG family, coding index, rule). This is the table that decides whether a module's coding index is allowed for the vehicle order:

| Module family | Coding index | Allowed when the vehicle order has |
|---|---|---|
| AKMB | C06, C07, C08 | `PU01 AND NOT S54B32` |
| AKMB | C22, C23, C24 | `PU01 AND S54B32` |
| KMB | C02–C08 | `NOT (PU01 OR S54B32)` |
| KMB | C20–C24 | `NOT PU01 AND S54B32` |
| ALSZ | C31–C37 | `PU01` (no body or engine condition) |
| MK60 | C06 (M3) | `PU02 AND S54B32` |
| MK60 | C04, C05, C09, C10, C12, C13 | `PU01 AND NOT (ALLRAD OR S54B32)` |

**BMW's module-selection rows** [read] (`E46SGET.000`, block `SGAUSWAHL_SGBD`):

| File | Coding index | SGBD | Module | Rule |
|---|---|---|---|---|
| `KMBE46M3` | C22 | `C_KMB46` | AKMB | `PU01 AND S54B32 AND NOT KMBI_CI_23` |
| `KMBE46M3` | C23 | `KOMBI46R` | AKMB | `PU01 AND S54B32 AND KMBI_CI_23 AND NOT KMBI_CI_24` |
| `KMBE46M3` | C24 | `KOMBI46R` | AKMB | `PU01 AND S54B32 AND KMBI_CI_24` |
| `KMB_E46` | C07 | `KOMBI46R` | AKMB | `PU01 AND KMBI_CI_07 AND NOT (KMBI_CI_08 OR S54B32)` |
| `KMB_E46` | C08 | `KOMBI46R` | AKMB | `PU01 AND KMBI_CI_08 AND NOT S54B32` |

**Where the keywords come from** [read] (`E46AT.000`):
- **The US 325iT** is `W EN33 … E46 TOUR M54B25 LL US KLIMAREGELUNG FH_HINTEN RADIO_US ENGLISCH` plus `RADIO_NG TROPEN BATT_KOFFERRAUM AK_GUWA`, "//Touring 325i US 09/01 - 05/06". It has no `S54B32`.
- **The US M3** is `W BL93 V0302/N0302 … E46 COUP S54B32 LL US NEBELSCHEINW GESCHW_REG TROPEN …`.
- **`PU01`** is in every production-date word from `#0901` on.
- **`KMBI_CI_23` and `KMBI_CI_24`** appear in no type or date record. They appear only in `E46SGVT.000`'s `VERSIONS_ASW` sets (`[KMBI_CI_23]`, `[KMBI_CI_23, KMBI_CI_24]`).

**Two known errors fit the same tables:**
- "Ungültiger Codierindex 24" when the cluster was selected as KMB [earlier round] ([e46fanatics 1278842](https://www.e46fanatics.com/threads/e46-m3-cluster-coding.1278842/)). KMB C24 requires `NOT PU01`, which no vehicle-order car has.
- The MK60 "#0902 or later" fix [earlier round]. MK60 C06 requires `PU02`.

**The earlier "it works" reports** fit too.
- nextelbuddy's coded index-24 cluster had its donor's order "brought back onto the new Chip" ([NAM3 154645](https://nam3forum.com/forums/forum/special-interests/coding-tuning/154645-cluster-with-coding-index-0x24-virginization)) [read].
- His index-24 values are exactly BMW's US M3 values for cars built from 03/2004 (gap 2).

#### Inferences

- **NCS will refuse the M3 cluster with the Touring's order.** With the Touring's order in the session (read from ALSZ, or written into the cluster), the `AKMB C22/C23/C24` rule is false.
  - So NCS will reject the index-23/24 cluster ("Codierindex … nicht zulässig" or "…not allowed for this coding job"). This holds for coding and, very likely, for any job on AKMB, `FA_WRITE` included.
  - The exact wording of the message, and whether `FA_WRITE` goes through the same check, are untested inferences.
- **What works.** Code the M3 cluster with any session order whose type key carries `S54B32` (BL93, BR93) and whose date is 09/2001 or later.
  - The donor's own order works; it is what a chip job leaves in the cluster.
  - Your Touring order with only the type key changed to BL93 for the session also works, with no `FA_WRITE`.
- **The Touring's order cannot live in the cluster in practice.** If it were stored there, every later cluster session would first need a typed session order.
  - So keep the donor's order in AKMB and treat **ALSZ as the car's only true order**.
  - Tell any cluster service not to write the Touring's order into the cluster. Or, if they already have, enter a BL93 session order before coding the cluster.
- **Why index-08 retrofit guides work.** Converting an M3 cluster to index 08 makes it admissible with a non-M order (`PU01 AND NOT S54B32`), but loads the non-M coding file (`KMB_E46.C08`). The guide already warns against this.

#### Still open

- A first-hand screenshot of the refusal with a Touring order.
- **Settle it at no risk:**
  1. NCS → F1 → F3 → E46 → ALSZ (your order).
  2. F6 → F4 → AKMB → F2 → `CODIERDATEN_LESEN` → F3.
  3. **Expect** a refusal. Then load the order from AKMB (the donor's) and repeat; **expect** `KMBE46M3.C24` under JOBNAME.

#### Guide impact (writer: coding-body)

**`WIRING-AND-CODING.md:925–927`** currently reads: "1. NCS Expert → read from AKMB → Process ECU → AKMB → `CODIERDATEN_LESEN` → Execute. Back up the `FSW_PSW.TRC`." … "3. Load your manipulation profile → Process ECU → AKMB → `SG_CODIEREN` → Execute"

Add before step 1, ready to paste:

> **Which vehicle order the cluster needs.** BMW's coding data allows an M3 cluster (index 22, 23 or 24) only with a vehicle order that has an M3 type key (engine keyword `S54B32`) and a build date from 09/2001; a non-M order allows only indexes 06–08. Your Touring's order (type key `EN33`, `M54B25`) therefore can't be used to read or code the M3 cluster: by BMW's rule NCS refuses that coding index, which a harmless read with your ALSZ order will show ([BMW E46SGVT.000 / E46SGET.000, SP-Daten V32](https://archive.org/details/sp-daten-v-32), [format](https://github.com/emdzej/ncsx/blob/main/docs/ecu-selection.md)). After a chip job the cluster still holds the donor's order, which is exactly what it needs, so "read from AKMB" below works. If a cluster service wrote your Touring's order into it, use Enter FA to change the type key to `BL93` for this session only (no `FA_WRITE`), then continue. Use ALSZ, never AKMB, as the source of your car's order for every other module.

**The Round-4 plan's step "Store your FA in the cluster"** (`FA_WRITE` of the ALSZ order to AKMB, notes G4 step 6): **replace** with:

> Don't write your Touring's order into the M3 cluster: NCS won't accept the cluster with it (BMW requires `S54B32` for indexes 22–24), and you'd need a typed session order for every later cluster edit. Leave the donor's order in AKMB, label it on the coding sheet ("AKMB holds the donor M3 order; the car's order is in ALSZ"), and never run Code Car.

**`WIRING-AND-CODING.md:941`** currently reads: "Keep the M3 index; the non-M index 08 that some retrofit guides use gives non-M gauge definitions (same source)."

Append:

> That's also why those guides change it: index 08 is the one BMW's data allows with a non-M vehicle order ([BMW E46SGVT.000](https://archive.org/details/sp-daten-v-32)). Keeping index 23/24 means coding the cluster with an M3 type key in the session order.

**`README.md:386`** (Cluster service row) currently reads: "Your Touring's VIN in the M3 cluster, with the odometer set so it takes your true mileage from the light module; the M3 coding index kept; rear-door warning lights added if offered"

Add:

> "…; the donor's vehicle order left in the cluster (an M3 type key). NCS codes an index-23/24 cluster only with an M3 order."

---

### Gap 2. Lamp-switch factory values, index 23 versus 24

#### Cited findings

**Which coding files have the switches** [read] (decoded files):

| File | `GENERATOR_UEBER_CAN` | `TOG_UEBER_CAN` | `CAN_OELDRUCKSCHALTER` |
|---|---|---|---|
| `KMBE46M3.C20`, `.C21`, `.C22` | absent | absent | absent |
| `KMBE46M3.C23`, `.C24` | yes | yes | yes |
| `KMB_E46.C02`–`.C06` | absent | absent | absent |
| `KMB_E46.C07`, `.C08` | yes | yes | yes |

- In C23/C24 each sits at the same address as in C07/C08:
  - `GENERATOR_UEBER_CAN`: word 112, mask 20.
  - `TOG_UEBER_CAN`: word 115, mask 02.
  - `CAN_OELDRUCKSCHALTER`: word 120, mask 20.
- Each has two settings, `aktiv` = 01 and `nicht_aktiv` = 00.
- The same files also carry `KLEMME_50_UEBER_CAN` (word 112, mask 40) and `OELNIVEAU_M3`.
- `ATEMP_WARNUNG_KALTLAND` is in C24 and C08 only.

**BMW's coding rules** [read] (`E46CVT.000`). AND binds tighter than OR.

| Function | Group | `aktiv` when |
|---|---|---|
| `GENERATOR_UEBER_CAN` | `Generator-ueber_can` | `N40… OR N42… OR N45… OR N46… OR M56B25 OR M47D20 AND KW_105 OR M57D30 AND KW_150 OR (M47D20 AND KW_85 OR (M54B25 OR M54B30) AND US AND NOT ALLRAD) AND MAERZ03 OR S54B32 AND MAERZ04` |
| `TOG_UEBER_CAN` | `Tog_Ueber_Kan` | `… OR M56B25 OR S54B32 OR (M54B25 OR M54B30) AND US AND MAERZ03 AND NOT ALLRAD` |
| `CAN_OELDRUCKSCHALTER` | `Can_Oeldr` | `PU02 AND M56B25 OR (M54B25 OR M54B30) AND US AND MAERZ03 AND NOT ALLRAD OR M57D30 AND KW_150` |
| `OELNIVEAU_M3` | `CSL` | `CSL` only |
| `KLEMME_50_UEBER_CAN` | `feste_Daten_E46` | Never (`nicht_aktiv` on every E46) |

None of these rules mentions the cluster's coding index.

#### Computed factory values (from the rules above)

| Car | `GENERATOR_UEBER_CAN` | `TOG_UEBER_CAN` | `CAN_OELDRUCKSCHALTER` |
|---|---|---|---|
| US M3 (BL93) built before 03/2004, index 23 or 24 | `nicht_aktiv` | `aktiv` | `nicht_aktiv` |
| US M3 (BL93) built from 03/2004, index 23 or 24 | `aktiv` | `aktiv` | `nicht_aktiv` |
| US 325iT (EN33) built before 03/2003 (MS43) | `nicht_aktiv` | `nicht_aktiv` | `nicht_aktiv` |
| US 325iT (EN33) built from 03/2003 (MS45.1) | `aktiv` | `aktiv` | `aktiv` |

- **A cross-check:** nextelbuddy's index-24 cluster had "alternator over can bus enabled oil level over can bus enabled but oil pressure over can bus not enabled" ([NAM3 61405](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)) [read]. That is exactly the 03/2004-and-later M3 row.
- **The MS45.1 row** matches the guide's statement that the MS45.1 sends all three lamps over CAN.

**Extra finding: the fuel-gauge curve** [read] (affects the Round-4 correction of the guide's `TANK_KENNLINIE` row):
- On C07, C08, C23 and C24, `60_l_literskala` and `dad_tank_diesel` carry the same 30-byte curve. `metalltank` carries a **different** curve: every point differs, for example bytes 14–15 are `01 86` against `01 D6`.
- On C04 and C22 all three names carry one identical curve. That is why Round 4 saw "one value, three names".
- BMW's rule (`Tankkennlinie`): `60_l_literskala` unless `M56B25` (→ `metalltank`) or `M47D20 AND KW_105` (→ `dad_tank_diesel`).
- So the guide's existing text (`60_l_literskala` for a plastic tank, `metalltank` only for the SULEV metal tank) is **right** for an index-23/24 cluster. **Don't apply** Round 4's takeaway 4 ("not a choice of three … leave it as read") to a redesign cluster: it holds only for older files.

**Also for the Round-4 G9 table:** `CC_TUEREN`, `CC_LAMPEN` and `LITER_SERVICE_INTERVALL` **don't exist** in `KMBE46M3.C23/C24` or `KMB_E46.C07/C08` [read]. `SIA_LITER_GRENZE` does (US M3 value `s54b32`; US 325iT manual `m54b25_man_tour`, computed).

#### Inferences

- The index doesn't decide these switches; the donor's build date does. A donor built from 03/2004 will read `GENERATOR_UEBER_CAN` = `aktiv`.
- The guide's plan (wire all three lamps, code all three `nicht_aktiv`) is unaffected and stays the robust choice.

#### Still open

Nothing for coding. Whether a stock MSS54 (not HP) drives any lamp over CAN is a powertrain question.

#### Guide impact (writer: coding-body; the 539 line is in the cluster-wiring section)

**`WIRING-AND-CODING.md:539`** currently reads: "One snippet says these switches exist on cluster indexes 07, 08, 23 and 24; check that yours has them when you read its coding"

**Replace with:**

> BMW's coding data confirms it: these three switches exist on cluster indexes 07 and 08 (non-M) and 23 and 24 (M3), and on no earlier index ([BMW KMBE46M3.C23/C24, KMB_E46.C07/C08, SP-Daten V32](https://archive.org/details/sp-daten-v-32)). From the factory a US M3 has oil level over CAN `aktiv` and oil pressure over CAN `nicht_aktiv` at any date, and the charge lamp over CAN `aktiv` only on cars built from 03/2004 (BMW E46CVT.000; one index-24 cluster read exactly that, [NAM3](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)).

**`WIRING-AND-CODING.md:939`** currently reads: "…one forum snippet says they exist on cluster coding indexes 07, 08, 23 and 24 ([e46fanatics](…), unverified), so look for them in your cluster's file."

Replace the clause with:

> "…BMW's coding files confirm they exist on indexes 07, 08, 23 and 24 only ([SP-Daten V32](https://archive.org/details/sp-daten-v-32))."

**`README.md:2384`** (open question "Which cluster coding indexes have the three lamp switches…"): **delete**, as answered.

**`README.md:1612`** currently reads: "`TANK_KENNLINIE` at `60_l_literskala`, for a plastic tank; our reading of the coding list".

Replace "our reading of the coding list" with "BMW's coding rule for both the M54 and the S54 ([BMW E46CVT.000](https://archive.org/details/sp-daten-v-32))". Tell the coding-body and fuel writers **not** to fold in Round 4's "one value, three names" correction for index 23/24.

**`WIRING-AND-CODING.md:555`** (writer: fuel / coding-body) currently ends: "…A Touring that started as an M56 SULEV car with its metal tank would need `metalltank`. This is our reading of the coding list; nobody has reported an M3 cluster on Touring senders."

**Replace** the last sentence with:

> "BMW's own rule says the same: `60_l_literskala` for every engine but the M56 (`metalltank`) and one diesel; on index 23/24 clusters `metalltank` is a genuinely different curve, while `dad_tank_diesel` is identical to `60_l_literskala` ([BMW E46CVT.000, KMBE46M3.C24](https://archive.org/details/sp-daten-v-32)). Nobody has reported an M3 cluster on Touring senders, so check with a measured fill."

---

### Gap 3. What an M3 cluster shows for the Touring's tailgate and rear glass

#### Cited findings

- **The cluster's pictogram LEDs** [read]. The KOMBI46R job `STEUERN_LEUCHTE` lists them ([SGBD KOMBI46R](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46R.md)):
  - BYTE3: "Bit0: CC-Ruecklicht rechts Bit1: CC-Ruecklicht links Bit2: CC-Heckklappe Bit3: CC-Tuer hinten rechts Bit4: CC-Tuer hinten links Bit5: CC-Tuer vorne rechts".
  - BYTE4: "Bit0: CC-Kontur Bit1: CC-Tuer vorne links Bit2: CC-Abblendlicht links Bit3: CC-Abblendlicht rechts".
  - So there is **one** rear-lid (Heckklappe) LED and no rear-glass LED.
- **No door or lid coding in the cluster** [read]. `KMBE46M3.C24` has no `CC_TUEREN` or any other door or lid function.
- **The GM5 reads both contacts** [read]. The ZKE5 (GM5) job `STATUS_DIGITAL` returns `STAT_HKK` "Eingang: Heckklappen-Kontakt" (tailgate contact) and `STAT_HSK` "Eingang: Heckscheiben-Kontakt" (rear-glass contact) ([SGBD ZKE5](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/ZKE5.md)).
- **The GM5 broadcasts one rear-lid bit** [read]. GM broadcast `0x7A` "Door/Lid Status" has one `REAR_LID` bit (byte 2, `0x20`).
  - wilhelm-docs: "On Touring models, the rear lid and rear-window/hatch contacts may both contribute to the luggage-compartment-open state" ([wilhelm-docs gm/7a.md](https://github.com/piersholt/wilhelm-docs/blob/master/gm/7a.md)). The wording is hedged.
  - The same doc lists the cluster (IKE) among the modules that request this status (`0x79`).
- **The GM5's Touring coding** [read] (`E46CVT.000`, group `GM_Touring`). `FUNKTIONEN_TOURING` and `HECKSCHEIBE_ENTR_SENDER_1…4` = `aktiv` only `IF TOUR`.
- **Rear-door LEDs.** M3 clusters lack them; services add them [earlier round] ([Huggins](https://racehuggins.com/product/e46-m3-cluster-mod-for-non-m/): "Have a 4-door and need the LED's added to indicate open doors?").

#### Inferences

- **Tailgate open:** the M3 cluster lights its rear-lid symbol, provided the GM5 stays Touring-coded.
- **Rear glass open:** probably the same symbol, if the GM5 merges the contacts as wilhelm-docs suggests. Unverified.
- **Rear doors:** nothing shows unless LEDs are added.
- **Nothing can be fixed by cluster coding.**

#### Still open

Whether the rear glass alone lights the rear-lid symbol. **Settle it on the car (about 10 minutes):**
1. Tool32 `ZKE5.PRG` → `STATUS_DIGITAL`. Open the tailgate, then the rear glass. **Expect** `STAT_HKK`, then `STAT_HSK`, to change.
2. Watch the cluster for each.
3. Tool32 `KOMBI46R.PRG` → `STEUERN_LEUCHTE` with BYTE3 = `0x04` (rear lid), then `0x18` (both rear doors), other bytes 0, to see which LEDs the cluster actually has.

#### Guide impact (writer: coding-body)

**`README.md:2390`** currently reads: "How accurately an M3 cluster's fuel gauge reads the Touring's tank senders, and whether it shows the tailgate and rear-window warnings."

**Replace** with:

> "How accurately an M3 cluster's fuel gauge reads the Touring's tank senders, and whether the rear glass alone lights the cluster's single rear-lid symbol (the cluster has one rear-lid LED and no door coding; the GM5 reads the tailgate and rear-glass contacts separately; [KOMBI46R](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46R.md), [ZKE5](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/ZKE5.md))."

**Session 4 functional checks** (notes G4 step 8, "Doors: open each door, the tailgate and the rear glass…"): add:

> "…; if a symbol doesn't light, check the input in Tool32 `ZKE5.PRG` → `STATUS_DIGITAL` (`STAT_HKK` tailgate, `STAT_HSK` rear glass) and the LED itself with `KOMBI46R.PRG` → `STEUERN_LEUCHTE` (BYTE3 bit 2 = rear lid, bits 3/4 = rear doors). There's nothing to code in the cluster for doors or lids."

---

### Gap 4. A US halogen light-module read-out to compare against

#### Cited findings

- **No real US halogen trace turned up** [read]. GitHub code search finds only:
  - kd7iwp's `LSZ.C29/C35/C36` traces. Their KMB trace says `SPRACHE kanada` and `WEG_EINHEIT km`, so they are **Canadian**, not US ([kd7iwp](https://github.com/kd7iwp/BMW-Coding/tree/master/E46)).
  - An ECE halogen sedan's MAN with `LAENDERVARIANTE_LSZ` = `wert_01` and `SIDEMARKER_US` = `nicht_aktiv` ([gerchanovsky](https://github.com/gerchanovsky/BMW_KBus_Pioneer_Helper/blob/master/packet_samples/FSW_PSW_LSZ1.MAN)).
- **BMW's light-module rules** [read] (`E46CVT.000`):

| Function | Rule |
|---|---|
| `VARIANTE_LSZ` | `wert_02` IF `TOUR OR COUP OR CABR OR LIM AND NOT PU01…`; `wert_01` IF `LIM AND (PU01 OR HKL_FL)` |
| `LAENDERVARIANTE_LSZ` | `wert_02` IF `US` |
| `GED_FL_ALS_DRL` | `aktiv` IF `US AND TAGFAHRLICHT` (SA 896 "Tagfahrlichtschaltung", per `E46AT.000`) |
| `LEUCHTWEITENREGELUNG` | `aktiv` IF `NOT (US AND NOT XENON) AND NOT ALC` |
| `LEUCHTWEITENREG_AUTOM` | `aktiv` IF `XENON` |
| `LEUCHTWEITENREG_DYNAM` | `aktiv` IF `PU00 AND XENON` |
| `KALTUEBERWACHUNG_AL` | `nicht_aktiv` IF `XENON` |
| `AL_KL_50` | `aktiv` IF `NOT (XENON OR ALC)` |
| `CYCL_TI_BLK` | `einmal` (fixed data) |

#### Computed: a 2003 US 325iT (EN33, #0303 date words, halogen), `LSZ.C36`

Adding fog lights (`NEBELSCHEINW`) changes **none** of the 324 functions. The full list is in the appendix.

| Function | US halogen 325iT (computed) | US xenon 325iT (computed) | Round-4 "US bi-xenon C35" (actually Canadian) |
|---|---|---|---|
| `VARIANTE_LSZ` | `wert_02` | `wert_02` | `wert_01` (sedan) |
| `LAENDERVARIANTE_LSZ` | `wert_02` | `wert_02` | `wert_02` |
| `SIDEMARKER_US` / `AH_US_OPTION` | `aktiv` / `aktiv` | `aktiv` / `aktiv` | `aktiv` / `aktiv` |
| `TAGFAHRLICHT_ECE` | `nicht_aktiv` | `nicht_aktiv` | `nicht_aktiv` |
| `GED_FL_ALS_DRL` | **`nicht_aktiv`** | `nicht_aktiv` | `aktiv` (Canadian DRL, SA 896) |
| `DAUERFAHRLICHT_US` | `nicht_aktiv` | `nicht_aktiv` | — |
| `BI_XENON` / `XENON_TEST` | `nicht_aktiv` / `nicht_aktiv` | `aktiv` / `aktiv` | `aktiv` / `aktiv` |
| `KALTUEBERWACHUNG_AL` | `aktiv` | `nicht_aktiv` | `nicht_aktiv` |
| `AL_KL_50` | `aktiv` | `nicht_aktiv` | — |
| `PWM_ANSTEUERUNG_AL` / `PWM_WERT2_FL_BIXENON` | `wert_01` / `wert_01` | `wert_02` / `wert_02` | `wert_02` / `wert_02` |
| `LEUCHTWEITENREGELUNG` / `_AUTOM` / `_DYNAM` | `nicht_aktiv` (all three) | `aktiv` (all three) | `aktiv` (all three) |
| `KENNLINIE_LWR_SENSOR_VO` / `_HI` | `wert_01` / `wert_01` | `wert_01` / `wert_01` | `wert_01` / `wert_01` |
| `FL_UND_NSW_NICHT_GLEICHZ` | `aktiv` | `aktiv` | `aktiv` |
| `CYCL_TI_BLK` | `einmal` | `einmal` | — |

- **Fourteen functions** differ between halogen and xenon.
- **Against an M3 coupe order (BL93)**, 37 functions differ from the Touring's: rear-lamp PWM, cold and warm monitoring, brake-force-display pins, check-control and the LWR curves (gap 10).

#### Inferences

- **The table is a reliable stand-in for a real dump.** The same method reproduced 311 of 311 functions of a real factory trace.
- **Your Session 1 trace should match the halogen column**, unless a previous owner changed something. Every difference is a customisation to keep through a MAN.
- **The Round-4 G10 note "GED_FL_ALS_DRL `aktiv` … US daytime lights" is wrong for a US car.** That trace is Canadian.

#### Still open

A real US halogen Touring trace. The owner's own Session 1 read supplies it.

#### Guide impact (writer: coding-body)

**`WIRING-AND-CODING.md:1080`** currently reads: "**Halogen M3 lamps in a halogen Touring:** no coding change. Confirm the lamps work as fitted."

Append:

> "Your Session 1 light-module trace should show the US halogen factory values: `VARIANTE_LSZ` `wert_02`, `LAENDERVARIANTE_LSZ` `wert_02`, `SIDEMARKER_US` `aktiv`, `KALTUEBERWACHUNG_AL` `aktiv`, `BI_XENON` and the three `LEUCHTWEITENREG*` functions `nicht_aktiv`, `GED_FL_ALS_DRL` `nicht_aktiv` (computed from [BMW's E46CVT.000](https://archive.org/details/sp-daten-v-32); the method reproduced a real factory trace exactly). A difference is a past customisation: keep it."

Also tell the coding-body writer that **the Round-4 G10 table's "US bi-xenon (C35)" column is from a Canadian car** ([kd7iwp](https://github.com/kd7iwp/BMW-Coding/tree/master/E46): `SPRACHE kanada`). Relabel it as Canadian, and set the US `GED_FL_ALS_DRL` to `nicht_aktiv`.

---

### Gap 5. Level-sensor curves with the M3 front link on a Touring (xenon)

#### Cited findings

**BMW's curve rules** [read] (`E46CVT.000`, group `LSZ_M3undAllrad`):

| When | `KENNLINIE_LWR_SENSOR_VO` | `KENNLINIE_LWR_SENSOR_HI` | `DEF_LWR_SENSOR_HI` | `OFFSET_LWR` |
|---|---|---|---|---|
| `NOT LSZ_CI_29 OR LSZ_CI_29 AND NOT (ALLRAD OR S54B32)`: every RWD non-M body, Touring included | `wert_01` | `wert_01` | `wert_01` | `wert_01` |
| `LSZ_CI_29 AND ALLRAD` (xi) | `wert_02` | `wert_01` | `wert_02` | `wert_02` |
| `LSZ_CI_29 AND S54B32 AND NOT CSL` (M3) | **`wert_03`** | **`wert_02`** | **`wert_03`** | **`wert_03`** |
| `LSZ_CI_29 AND S54B32 AND CSL` | `wert_01` | `wert_02` | `wert_06` | `wert_06` |

Every order built from 09/2001 has `LSZ_CI_29` (date words `#0901` on).

**The data behind the values** [read] (`LSZ.C36` and `LSZ.C37`):
- `KENNLINIE_LWR_SENSOR_VO`:
  - `wert_01` = `15 FD 15 FE 15`
  - `wert_02` = `11 …`
  - `wert_03` = `13 FD 13 FE 13`
  - `wert_04` = `17 …`
  - `wert_05` = `13 …`
- `KENNLINIE_LWR_SENSOR_HI`:
  - `wert_01` = `12 FD 12 FE 12`
  - `wert_02` = `13 FD 13 FE 13`
  - `wert_03` = `14 …`
  - `wert_04` = `10 …`

**The hardware** [read] (ETK):
- Both cars list the same sensors (37146784696 front, 37146784697 rear) and the same rear regulating rod (37146752797, 71.5 mm).
- Only the front angle joint differs: M3 31122282404, 325iT 37146766778 ([ETK 325iT](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/front_axle/headlight_vertical_aim_control_sensor/), [ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/front_axle/headlight_vertical_aim_control_sensor/)).

**`AUTO_LWR_ENABLE`** [read]. It is a function of the adaptive-headlight control unit (`ALC_DS2.C05/C06`, `ALC_KWP.C07`), not of the light module: it isn't among `LSZ.C36`'s 324 functions. BMW's fixed data set it `aktiv` for every E46. The light module's levelling switches are `LEUCHTWEITENREGELUNG`, `_AUTOM` and `_DYNAM`.

#### Inferences

- **Default coding gives the wrong curves.** A Touring order default-codes the four values to `wert_01`, the non-M curve.
- **This guide moves the M3 rear axle into the Touring** (README step 2). With both sensors on M3 suspension, the matching curves are the M3 set: VO `wert_03`, HI `wert_02`, `DEF_LWR_SENSOR_HI` `wert_03`, `OFFSET_LWR` `wert_03`.
  - Set them through a MAN after default-coding the xenon module.
  - If the Touring's rear axle stays, keep HI and `DEF_LWR_SENSOR_HI` at the Touring values and change only VO and OFFSET. This last split is my inference: BMW never pairs an M3 front with a non-M rear.
- **Then aim.** BMW's load test (front, then rear, about 15 s each) and the aim at ride height remain the final check. The Touring body carries more weight at the rear than a coupe.

#### Still open

Whether `OFFSET_LWR` should follow the front or the rear axle in a mixed car. The load test settles it.

#### Guide impact (writer: coding-body; front writer for the hardware)

**`WIRING-AND-CODING.md:1083`** currently reads: "…automatic levelling on (`AUTO_LWR_ENABLE`). The levelling sensors' curves are `KENNLINIE_LWR_SENSOR_VO` and `KENNLINIE_LWR_SENSOR_HI` ([NCS list](…), [BMW ST034](…))."

**Replace** the levelling sentences with:

> "…automatic levelling on: `LEUCHTWEITENREGELUNG`, `LEUCHTWEITENREG_AUTOM` and `LEUCHTWEITENREG_DYNAM` = `aktiv` (BMW sets these from `$522`; `AUTO_LWR_ENABLE` belongs to the adaptive-headlight unit, not the light module). Then set the M3's sensor curves, because coding from your Touring order gives the non-M ones: `KENNLINIE_LWR_SENSOR_VO` = `wert_03`, `KENNLINIE_LWR_SENSOR_HI` = `wert_02`, `DEF_LWR_SENSOR_HI` = `wert_03`, `OFFSET_LWR` = `wert_03` (BMW's values for an M3; every non-M RWD car gets `wert_01`: [BMW E46CVT.000, group LSZ_M3undAllrad](https://archive.org/details/sp-daten-v-32)). These match both sensors riding on M3 suspension; if your rear axle is still the Touring's, leave `_HI` and `DEF_LWR_SENSOR_HI` at `wert_01`. Confirm with BMW's load test and the aim."

---

### Gap 6. Do fog lights need `$520` or a different light module?

#### Cited findings

- **The option code** [read] (`E46AT.000`): `W 520 NEBELSCHEINW //Nebelscheinwerfer`, with the change-log line "S520A NEBELSCHEINW wird bei allen E46/2/C Serienumfang" (standard on all coupes and convertibles).
  - The ETK uses the same code: "Filters | S520A | Fog lights" ([ETK 325iT 2003, various switches](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/2003/browse/vehicle_electrical_system/various_switches/)).
- **Standard on the M3, not on the 325iT** [read]. The US 325iT type key `EN33` has no `NEBELSCHEINW`; the US M3 `BL93` has it.
- **What `NEBELSCHEINW` drives** [read] (`E46CVT.000`). It affects only two GM5 functions:
  - `SPRITZDUESEN_HZG` = `aktiv` IF `MAERZ04 AND NEBELSCHEINW` (heated washer jets, cars from 03/2004);
  - `SPIEGELHEIZUNG_VERBAUT`, where it is one of several alternatives; every M54 and S54 car is `aktiv` anyway.
  - In the GM5 files, `SPRITZDUESEN_HZG` appears from `GM5.C05`.
- **No fog switch in the light module** [read]. `LSZ.C36` has no fog-enable function. My computed `LSZ.C36` coding is identical with and without `NEBELSCHEINW`.
- **Separate hardware** [earlier round]. ETK lists separate light-module variants ("Switch unit, light" 61319133022/023 against "Switch unit, light / foglamps" 024–027) and separate switch panels with a fog button.
- **A test for the fog output** [read]. The LSZ_2 SGBD job `STEUERN_IO` accepts `'REL_NSW' = Relais Nebelscheinwerfer` and `'T_NSW' = Taster Nebelscheinwerfer` ([SGBD LSZ_2](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ_2.md)).

#### Inferences

- **Fogs are a hardware job:** a fog-variant light module, the switch panel with the fog button, relay K47 and the wiring. The order is not involved.
- **`$520` is optional.** If added, a default-coded GM5 also turns on the heated washer jets (cars from 03/04), so add it only if the jets are fitted.
- **Whether a non-fog module merely lacks the relay driver** (a test with `STEUERN_IO` `REL_NSW` and a relay fitted would show it) is untested.

#### Still open

Whether a no-fog light module can drive K47 at all. Run the Tool32 `REL_NSW` test before buying a module.

#### Guide impact (writer: coding-body; front writer for parts)

**`WIRING-AND-CODING.md:646`** (Shared parts) currently reads: "…and the same light-switch units: 61319133022 to 61319133025 without xenon, 61319133026 and 61319133027 with it"

Append:

> "(…022/023 without a fog-light output, …024 to …027 with one). Front fogs need a fog-variant module, the switch panel with the fog button and relay K47; no coding turns them on: option `$520` changes no light-module setting, only the GM5's heated washer jets on cars from 03/2004 ([BMW E46AT.000 / E46CVT.000](https://archive.org/details/sp-daten-v-32)). Test a module's fog output with Tool32 `LSZ_2.PRG` → `STEUERN_IO` `REL_NSW` ([SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ_2.md))."

---

### Gap 7. Headlight washers: option code, and do US M3s have them?

#### Cited findings

- **The option code** [read] (`E46AT.000`): `W 502 SWA //Scheinwerfer-Waschanlage`.
  - The ETK uses `S502A` "Headlight cleaning system" ([ETK US M3, washer container](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/windshield_cleaning_container/)).
- **Its only coding effect** [read] (`E46CVT.000`, group `Scheinwerfer`): `SCHEINWERFERREINIGUNG = aktiv IF SWA`, otherwise `nicht_aktiv`. The function is in `GM5.C02`, `C04`, `C05` and `C06`.
  - The fixed data also set `SRA_MIT_WASCH_WISCH_SW = nicht_aktiv`.
- **Not standard on the US M3** [read]. The US M3 type record (BL93) contains no `SWA`. `XENON` comes only from SA 522 or 524.
- **But fitted to some US M3s** [read] (US M3 ETK):
  - The washer container is split "Headlight cleaning system S502A No" (61677892702 / 61677895571) against "S502A Yes" (61677892700 / 61677895577).
  - The catalog has pages for "Single parts for head lamp cleaning" (telescopic nozzles 61678362823 and so on) and "Relay for headlight cleaning system K6" (61366915327) ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/single_parts_for_head_lamp_cleaning/), [ETK K6](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/relay_for_headlight_cleaning_system_k6/)).
- **BMW's retrofit kit** [earlier round] codes through DIS "Retrofit" and stores the option in the cluster ([BMW EBA SRA](https://bmw.etk.club/eba_docs/594en.pdf)).

#### Inferences

US M3s had headlight washers only when ordered with SA 502. Check the donor before relying on its bumper:
- nozzle covers in the bumper;
- the second pump on the washer bottle;
- `$502` in its order (G3 screenshot).

#### Still open

How common SA 502 was on US M3s.

#### Guide impact (writer: coding-body)

**Session 8, table of order changes** (Round-4 notes G5 row "Headlight washers | SRA code (unverified, `S502A`?)"): **replace** with:

> "| Headlight washers (only if the donor had them) | `$502` (`SWA`) | GM5: `SCHEINWERFERREINIGUNG` = `aktiv` (its only coding effect) | Add `$502` and default-code GM5 only if it was never customised; otherwise set that one line in a MAN | [BMW E46AT.000 / E46CVT.000](https://archive.org/details/sp-daten-v-32), [ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/windshield_cleaning_container/) |"

Add to the README's donor checks:

> "Headlight washers were an option (502) on US M3s, not standard: check for bumper nozzle covers and the second pump on the washer bottle."

---

### Gap 8. Seat occupancy: OC3 against SBE if the seats change

#### Cited findings

- **Which airbag module family** [read] (`E46SGET.000`, airbag rows):

| File | Coding index | Rule |
|---|---|---|
| `MRS2` | C07 | `NOT (TOUR OR COUP AND US OR PU99) AND NOT MRS4_CI_29` |
| `MRS4_16` | C29 | `NOT (TOUR OR COUP AND US OR PU99) AND US AND MRS4_CI_29` |
| `MRS3` | C31 | `(TOUR OR COUP AND US OR PU99) AND NOT MRS4_CI_32` |
| `MRS4_16` | C32 | `MRS4_CI_32` |

  So a 2003 US Touring runs MRS3 `C31`, unless its module reports index 32 (MRS4).
- **What the coding files contain** [read] (`MRS3.C31`, `MRS4_16.C29/C32`):
  - seat occupancy: `ERKENNUNG_SITZBELEGUNG_1/2`, `SBE2_1/2`, `SBE1_STATUS_VERZ_1/2`;
  - seat-back locks: `VERRIEGELN_SITZLEHNE_FA/BF_1/2`;
  - **no OC3 function**.
- **BMW's rules** [read]:
  - `ERKENNUNG_SITZBELEGUNG_1/2` = `aktiv` for every E46.
  - `VERRIEGELN_SITZLEHNE_*` = `aktiv` **only IF `CABR`** (group `Cabrio`); coupes and Tourings get `nicht_aktiv`.
- **The SGBDs identify the system** [read]:
  - MRS3 `AUSSTATTUNG_LESEN` returns `SBE_VERBAUT`, `SBE2_VERBAUT`, `LEHNE_F_VERBAUT` and `LEHNE_BF_VERBAUT`. Its `STATUS_LESEN` returns `STAT_SBE2_KIND` (child seat) and `STAT_SBE2_OOP` ([MRS3](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MRS3.md)).
  - MRS4 ("MRS4 fuer Airbag SG … E46 E53 R50 R53 (Bosch)") returns `SBE_VERBAUT` and `OC3_VERBAUT` "Occupant Classification System", `STAT_OC3_1…5`, and fault 0x71 "OC3" ([MRS4](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MRS4.md)).
- **NHTSA** [read]. The OC3 mat recalls and warranty extension found cover E60, E61, E90, E91, E85 and MINI ([15V-205](https://static.nhtsa.gov/odi/rcl/2015/RCRIT-15V205-8849.pdf), [MC-10148018](https://static.nhtsa.gov/odi/tsbs/2014/MC-10148018-9999.pdf), [MC-10142910](https://static.nhtsa.gov/odi/tsbs/2018/MC-10142910-9999.pdf)). None covers the E46.

#### Inferences

- **OC3 against SBE/SBE2 is hardware** (the seat mat and the module), not coding. Never code occupancy detection out.
- **Read the system first.** Before any seat swap, read Tool32 `MRS3.PRG` (or `MRS4.PRG`) → `AUSSTATTUNG_LESEN` and record what it reports. Keep the Touring's passenger-seat mat and its electronics, or a seat carrying the same type.
- **M3 coupe seats need no seat-back coding.** BMW codes seat-back monitoring only on convertibles.
- **M3 convertible seats** would carry lock sensors the Touring's module ignores, as a coupe's does.

#### Still open

- The model year in which US E46s changed to OC3 or MRS4.
- Whether an OC3 seat works on an MRS3.
- **What would settle it:** the Tool32 read on both cars, or a dealer lookup by VIN of the passenger-seat upholstery part.

#### Guide impact (writer: coding-body)

**`WIRING-AND-CODING.md:1233`** (Airbag row) currently reads: "| Airbag | A seat swap (belt tensioners, occupancy mat), the steering wheel's slip-ring plugs | INPA's airbag fault memory | Matching tensioners and plugs; clear the codes…"

Add to the check column:

> "; before swapping seats, read Tool32 `MRS3.PRG` (or `MRS4.PRG`) → `AUSSTATTUNG_LESEN` (SBE, SBE2 or OC3 fitted) and keep a passenger mat of that type. E46 coding has no OC3 setting, and seat-back-lock monitoring is coded only on convertibles, so M3 coupe seats need no seat-back coding ([BMW MRS3.C31 / E46CVT.000](https://archive.org/details/sp-daten-v-32), [MRS3 SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MRS3.md), [MRS4 SGBD](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MRS4.md))"

---

### Gap 9. Switch unit on a DSC-equipped 325iT

#### Cited findings (ETK via bmwfans) [read]

- **The US 325iT 2003 "Various switches" page** lists "Switch asc" 61316901591 and **"Switch dsc" 61316901592** ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/2003/browse/vehicle_electrical_system/various_switches/)).
  - The 61316901592 part page: "Production May '99 –", old number 61318363695.
  - Its usage includes 325i M54 Touring USA, and also the M3 coupe ([part](https://bmwfans.info/parts-catalog/61316901592/)).
- **The US 325iT "Switch unit, center console" page** lists only **61316925498**, "For vehicles with Dynamic stability control S210A No" ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/2003/browse/vehicle_electrical_system/switch_unit_center_console/)).
- **The same page for the US 325i sedan and the Euro 325i Touring** lists 61316925498 (DSC No) **and 61316925512** "For vehicles with Dsc" ([sedan](https://bmwfans.info/parts-catalog/E46-Sedan/USA/325i-M54/2003/browse/vehicle_electrical_system/switch_unit_center_console/)).
  - 61316925512: from Sep '02, replaces 61316914744. Its usage covers the 325i sedan USA and the Touring in Europe, **not the Touring USA** ([part](https://bmwfans.info/parts-catalog/61316925512/)).
- **M3: 61316925520**, from Sep '02, replaces 61316914752; coupe EU and US, CSL ([part](https://bmwfans.info/parts-catalog/61316925520/)).
- **DSC became standard in 03/2003** [read]. BMW's `E46AT.000` change log: "S210A DSC3 wird ab 03/03 Serie fuer E46".

#### Inferences

- **A DSC US 325iT has the single DSC button 61316901592**, on the 4-pin plug the guide already describes, not a console switch block.
- **61316925498 is ETK's non-DSC console unit.** The guide's "Your 325i's is 61316925498" is wrong for this car.

#### Still open

Nothing for parts. Look at the car: one DSC button on a 4-pin plug confirms it.

#### Guide impact (writer: coding-body; the Sport-button section is shared with coding-power)

**`WIRING-AND-CODING.md:444`** currently reads: "1. **Fit the M3's console switch unit:** 61316925520 on M3 coupes, 61316925521 on convertibles. Your 325i's is 61316925498 ([ETK](…))."

**Replace** "Your 325i's is 61316925498" with:

> "A DSC-equipped US 325i Touring has no console switch unit, just the DSC button 61316901592 on the 4-pin X521 plug; 61316925498 is ETK's console unit for cars without DSC ([ETK: 325iT switches](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/2003/browse/vehicle_electrical_system/various_switches/), [ETK: console unit](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/2003/browse/vehicle_electrical_system/switch_unit_center_console/))."

**`README.md:507`** currently reads: "your 325i's (61316925498) has none". **Replace** with "a DSC-equipped 325i Touring has only the DSC button (61316901592), so it has no Sport button".

---

### Gap 10. Coding-data versions and US type keys

#### Cited findings

**Type keys** [read] ([zcs_all](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/zcs_all.md) and [fzgident](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/fzgident.md) SGBD tables agree):

| Type key | Model | Production | Keywords | Source |
|---|---|---|---|---|
| **EN33** | 325i Touring US | 09/01 – 05/06 | `E46 TOUR M54B25 LL US …` | `E46AT.000` |
| AW33 | 325i Touring US | 09/00 – 08/01 | `TOUR M54B25 LL US` | `E46ZST.000` comment; [etk.club AW33](https://bmw.etk.club/etk/AW33/): 05.2000 – 08.2001 |
| **BL93** | M3 coupe US | 09/00 – 11/05 | `E46 COUP S54B32 LL US NEBELSCHEINW GESCHW_REG TROPEN …`; V0302 rows add `KLIMAREGELUNG`, N0302 rows `KLIMAAUTOMATIK` | `E46AT.000` |
| **BR93** | M3 convertible US | 01/01 (N0302: 03/02) – 11/06 | as BL93 with `CABR` | `E46AT.000` |

- The [etk.club EN33 page](https://bmw.etk.club/etk/EN33/) gives 04.2001 – 05.2005, though its label reads "AW33".
- A 2003 US 325iT is therefore EN33, which matches its VIN characters 4–7 (inference). The FA screenshot from ALSZ confirms it.

**Coding-data versions** [read]:
- The V32 torrent's file list and the V32 E46 folder (`E46AT.000` `DATUM 22.01.2007`) contain:
  - `KMBE46M3.C20–C24`;
  - `KMB_E46.C02–C08`;
  - `LSZ.C26–C37`;
  - `MK60.C01`, `C03`–`C06`, `C09`, `C10`, `C12` and `C13`;
  - `GM5.C01`, `C02`, `C04`, `C05` and `C06`.
- An older E46 data set kept inside V32's E39 folder (`E46AT.000` `DATUM 26.01.2001`) has only `KMBE46M3.C20/C21` and `LSZ.C26–C29`.
- ncs-expert.com names V32 as the "Base / Original" set and V75 as the latest [earlier round].

**What an M3 type key would do to the body modules** (computed from BMW's rules). This checks the guide's rule against writing an M3 type key into the stored order. A BL93 order instead of EN33 changes:
- **37 `LSZ.C36` functions:** rear-lamp PWM, cold and warm lamp monitoring, check-control of the rear lamps, `BREMSLICHT_ALS_STANDLICHT`, the brake-force-display pin assignment and the four LWR curve values;
- **GM5 functions:** `FUNKTIONEN_TOURING`, `HECKSCHEIBE_ENTR_SENDER_1…4` (all switched off), rear anti-pinch, rear one-touch windows and others.

  BMW codes `FUNKTIONEN_TOURING` = `aktiv` only `IF TOUR` [read].

**Cross-topic note for the coding-power writer** [read, `E46SGVT.000` / `E46SGET.000`]:
- The M3 MK60 is index `C06`, allowed only with `PU02 AND S54B32`.
- Every non-M MK60 index (C04, C05, C09, C10, C12, C13) requires `NOT S54B32`.
- So the "#0902 or later" session order for an M3 MK60 (`WIRING-AND-CODING.md:967`) also needs an M3 type key such as BL93. `coding_powertrain_chassis.md` already suggests this.
- Check against your data version: V32 data shows it this way.

#### Inferences

- **Any SP-Daten from V32 (2007-era E46 data) on carries every M3 cluster index and LSZ up to C37.** Older packages from the early 2000s may not.
- **The first release carrying C23/C24 is unknown.** The clusters date from about 2003, so probably a 2003–04 release.

#### Still open

The exact first SP-Daten version with `KMBE46M3.C23`/`.C24`. **What would settle it:** the `DATUM` lines of 2003–2005 data sets.

#### Guide impact (writer: coding-body)

**`WIRING-AND-CODING.md:51`** (SP-Daten row) currently reads: "| E46 data files (SP-Daten) | The coding rules NCS Expert applies | Bali's package; one M3 owner updated to v69 (…) | Cars built from 2005 may need newer files than older packages carry (…) |"

Append to the last column:

> "; any set from V32 on has the M3 cluster files `KMBE46M3.C23/C24` and light-module files up to `LSZ.C37` (an E46 data set from 01/2001 had only `C20/C21`; [SP-Daten V32 file list](https://archive.org/download/sp-daten-v-32/SP-DATEN_V32.torrent)). Check `C:\NCSEXPER\DATEN\E46\` for them."

**`WIRING-AND-CODING.md:829`** currently reads: "…the type code sets body (TOUR), engine (M54B25) and market…"

Add:

> "(a 2003 US 325i Touring's type code is `EN33`; a US M3 coupe's is `BL93`, a convertible's `BR93`; [BMW E46AT.000](https://archive.org/details/sp-daten-v-32), [zcs_all](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/zcs_all.md))"

**`WIRING-AND-CODING.md:838`** currently reads: "…would then code as a coupe (our reading of the coding rules; nobody has documented it)."

**Replace** the parenthesis with:

> "(BMW's coding rules confirm it: an M3 type key switches off the GM5's Touring functions, `FUNKTIONEN_TOURING` and the remote rear-glass release, and changes 37 light-module settings for the rear lamps; [BMW E46CVT.000](https://archive.org/details/sp-daten-v-32))."

---

## 3. Sources tried and blocked

- **web.archive.org (Wayback).**
  - The availability API first answered "429 Too Many Requests" repeatedly.
  - After a wait it returned a snapshot of [e46fanatics 1277945](https://web.archive.org/web/20240306164850/https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/) (2024-03-06). Thirteen downloads of it were reset by the remote end (the proxy logged "tunnel closed after 11s").
  - WebFetch reports it is "unable to fetch from web.archive.org".
  - No archived e46fanatics thread was read this round. BMW's data made it unnecessary for gap 1.
- **Blocked sites:**
  - bimmerforums.com: Cloudflare "Just a moment…" (403).
  - drive2.ru: DDoS-Guard (403).
  - m3forum.net: the proxy answered 502 to CONNECT.
  - reddit.com and old.reddit.com: "Blocked" (403).
  - e46fanatics, 1erforum, ZHP Mafia, modbm, manualmachine and bmwfaq: not retried (known blocks).
- **GitHub API:** refused for repositories outside this session. I read public files through raw.githubusercontent.com instead.
- **etk.club deep pages:** the retrofit-group pages are script-driven, and the EBA index is "403 Forbidden". I found no fog-light retrofit EBA.
- **No result:**
  - The NHTSA documents found (OC3) cover later models only.
  - WebSearch found no first-hand report of the AKMB refusal with a non-M order, and no post with `KENNLINIE_LWR_SENSOR_VO` values.
- **WebSearch calls used:** 12 of 20. A last search for the year the E46 changed to OC3 found only E60/E90 recalls and an eBay emulator listing.

---

## Appendix A. Computed factory `LSZ.C36` coding for a 2003 US 325i Touring, halogen

- **Basis:** BMW's `E46CVT.000` (SP-Daten V32), evaluated for the order `EN33` plus the `#0303` date words. Adding `NEBELSCHEINW` (front fogs) changes nothing.
- **Check:** the same method reproduces all 311 functions of a real factory `LSZ.C35` trace (Canadian xenon sedan).
- **Xenon (`$522`)** changes 14 lines: `PWM_ANSTEUERUNG_AL` → `wert_02`, `KALTUEBERWACHUNG_AL` → `nicht_aktiv`, `AL_KL_50` → `nicht_aktiv`, `XENON_TEST` → `aktiv`, `BI_XENON` → `aktiv`, `PWM_WERT2_FL_BIXENON` → `wert_02`, `LEUCHTWEITENREGELUNG`/`_AUTOM`/`_DYNAM` → `aktiv`, `SCHRITTE_0_OD_ALC_AKTIV_0` → `wert_02`, `SCHRITTE_2_OD_ALC_AKTIV_2` → `wert_04`, `ABS_MIN_2_OD_ALC_AKTIV_3` → `wert_04`, `HYSTERESE_OD_AL_XENON_IO` → `wert_02`, `T_STROM_OD_ALC_PARA_02` → `wert_02`.
- **For an M3-style front end,** also set the four LWR values from gap 5.

```
PWM_ANSTEUERUNG_BL_MITTE=wert_01              PWM_ANSTEUERUNG_SL_VO_RE=wert_02              PWM_ANSTEUERUNG_SL3_LI_HI=wert_01
PWM_ANSTEUERUNG_BL=wert_01                    PWM_ANSTEUERUNG_BLK_VORN=wert_01              PWM_ANSTEUERUNG_NSL_LI=wert_01
PWM_ANSTEUERUNG_SL3_RE_HI=wert_01             PWM_ANSTEUERUNG_FERNLICHT=wert_01             PWM_ANSTEUERUNG_SL_VO_LI=wert_02
PWM_ANSTEUERUNG_AL=wert_01                    PWM_ANSTEUERUNG_SL_LI_HI=wert_02              PWM_ANSTEUERUNG_SL2_RE_HI=wert_01
PWM_ANSTEUERUNG_KZL=wert_01                   PWM_ANSTEUERUNG_SL_RE_HI=wert_02              PWM_ANSTEUERUNG_BLK_HI=wert_01
PWM_ANSTEUERUNG_ZUSTZBLK=wert_01              PWM_ANSTEUERUNG_BIXENON=wert_01               PWM_ANSTEUERUNG_NSW=wert_01
SPG_NACHREGELUNG_0=wert_01                    SPG_NACHREGELUNG_1=wert_01                    SPG_NACHREGELUNG_2=wert_01
SPG_NACHREGELUNG_3=wert_01                    LOAD_DUMP_U_GR=wert_01                        LOAD_DUMP_TIME_OUT=wert_01
LOAD_DUMP_PWM_BLK=wert_01                     LOAD_DUMP_EINVER=wert_01                      VARIANTE_LSZ=wert_02
LAENDERVARIANTE_LSZ=wert_02                   LENKSEITE_LSZ=wert_01                         KALTUEBERWACHUNG_BL_MI=nicht_aktiv
KALTUEBERWACHUNG_SL_RE=nicht_aktiv            KALTUEBERWACHUNG_RL_3_LI=nicht_aktiv          KALTUEBERWACHUNG_BL=aktiv
KALTUEBERWACHUNG_BLK_VO=aktiv                 KALTUEBERWACHUNG_NSL_LI=nicht_aktiv           KALTUEBERWACHUNG_RL_3_RE=nicht_aktiv
KALTUEBERWACHUNG_FL=aktiv                     KALTUEBERWACHUNG_SL_LI=nicht_aktiv            KALTUEBERWACHUNG_AL=aktiv
KALTUEBERWACHUNG_RL_LI=aktiv                  KALTUEBERWACHUNG_RL_2_RE=nicht_aktiv          KALTUEBERWACHUNG_KZL_LI=nicht_aktiv
KALTUEBERWACHUNG_RL_RE=aktiv                  KALTUEBERWACHUNG_BLK_HI=aktiv                 KALTUEBERWACH_ZUSATZ_BLK=aktiv
KL_50_FUNK_AKT=aktiv                          LOAD_DUMP=aktiv                               AL_KL_50=aktiv
FL_KL_50=aktiv                                NSW_KL_50=aktiv                               LOAD_DUMP_AUSVER=wert_01
WARMUEBERWACHUNG_BL_MI=nicht_aktiv            WARMUEBERWACHUNG_SL_RE=nicht_aktiv            WARMUEBERWACHUNG_RL_3_LI=nicht_aktiv
WARMUEBERWACHUNG_BL=aktiv                     WARMUEBERWACHUNG_BLK_VO=aktiv                 WARMUEBERWACHUNG_NSL_LI=nicht_aktiv
WARMUEBERWACHUNG_RL_3_RE=nicht_aktiv          WARMUEBERWACHUNG_FL=aktiv                     WARMUEBERWACHUNG_SL_LI=nicht_aktiv
WARMUEBERWACHUNG_AL=aktiv                     WARMUEBERWACHUNG_RL_LI=aktiv                  WARMUEBERWACHUNG_RL_2_RE=nicht_aktiv
WARMUEBERWACHUNG_KZL_LI=nicht_aktiv           WARMUEBERWACHUNG_RL_RE=aktiv                  WARMUEBERWACHUNG_BLK_HI=aktiv
WARMUEBERWACH_ZUSATZ_BLK=nicht_aktiv          LOAD_DUMP_KL58G=aktiv                         LOAD_DUMP_P5_10=nicht_aktiv
LOAD_DUMP_P30_29=aktiv                        LOAD_DUMP_P44_45=aktiv                        LOAD_DUMP_P20=aktiv
LOAD_DUMP_P37=aktiv                           LOAD_DUMP_P38=aktiv                           LOAD_DUMP_P49=aktiv
CC_BREMSLICHT_MITTE=nicht_aktiv               CC_STANDLICHT_RECHTS=nicht_aktiv              CC_RUECKLICHT_3_LINKS=nicht_aktiv
CC_BREMSLICHT=aktiv                           CC_BLINKER_VORN=aktiv                         CC_NSL_LINKS=aktiv
CC_RUECKLICHT_3_RECHTS=nicht_aktiv            CC_FERNLICHT=aktiv                            CC_STANDLICHT_LINKS=nicht_aktiv
CC_ABBLENDLICHT=aktiv                         CC_RUECKLICHT_LINKS=aktiv                     CC_RUECKLICHT_2_RECHTS=nicht_aktiv
CC_KENNZEICHENLEUCHTE_LI=nicht_aktiv          CC_RUECKLICHT_RECHTS=aktiv                    CC_BLINKER_HINTEN=aktiv
CC_ZUSATZBLINKER=nicht_aktiv                  FEHLER_BL_BLINKEN=nicht_melden                FEHLER_NSL_RECHTS=nicht_melden
BLK_H_R_PICT=aktiv                            BLK_H_L_PICT=aktiv                            BLK_V_R_PICT=aktiv
BLK_V_L_PICT=aktiv                            FEHLER_SCHALTER_BREMSL=nicht_melden           FEHLER_ANHAENGER=melden
ENTPRELLZAHL_FEHLERERK=wert_01                ANZAHL_QUICK_RUNDEN=wert_01                   ZEIT_KALT_RUNDEN=wert_01
ZEIT_KALT_PULSE=wert_01                       ZEIT_KALT_PULSE_QUICK=wert_01                 ZYKLUS_KALT_RUNDEN_QUICK=wert_01
BLS_PRUEFEN=nicht_aktiv                       SCHALTER_BREMSL_SCHWELLW=wert_01              SCHALTER_BREMSL_WARTEZEIT=wert_01
DAUERFAHRLICHT_US=nicht_aktiv                 DEF_PIN_20_DEFEKTBLINKEN=nicht_aktiv          DEF_PIN_37_DEFEKTBLINKEN=nicht_aktiv
DEF_PIN_5_10_DEFEKTBLK=aktiv                  PIN_38_RE_LI_MELDEN=rechts_defekt             PIN_38_VO_HI_MELDEN=hinten_defekt
DEF_PIN_29_30_DEFEKT_BL=nicht_aktiv           DEF_PIN_5_10_DEFEKT_SL=nicht_aktiv            DEF_PIN_29_30_DEFEKT_SL=aktiv
DEF_PIN_37_VOR=nicht_aktiv                    DEF_PIN_20_VOR=nicht_aktiv                    NACHREG_DYN_SLOW=aktiv
FO_ME_HOME_SL2=nicht_aktiv                    PIN37_49_PARKL=nicht_aktiv                    BFD_SW1_STUFE3=nicht_aktiv
ST3_SCHWEL=nicht_aktiv                        BLST1_BLST3=nicht_aktiv                       BFD_SW1_STUFE2=aktiv
BFD_MINDEST_GESCHW=wert_01                    BFD_STUFE_2_VERZOEG=wert_01                   BFD_STUFE_2_MAX_EIN=wert_01
PIN29_30_BFD=aktiv                            PIN49_37_BFD=nicht_aktiv                      PIN38_20_BFD=nicht_aktiv
PIN5_10_BFD=nicht_aktiv                       BFD_BLINK_EINZEIT=wert_02                     BFD_BLINK_AUSZEIT=wert_02
BEI_NSL_KEIN_BFD=nicht_aktiv                  BFD3_ASC_TIMER=wert_01                        BFD_SW2_STUFE2=nicht_aktiv
BFD_SW2_STUFE3=nicht_aktiv                    BFD_ABS_STUFE2=aktiv                          BFD_ABS_STUFE3=nicht_aktiv
BFD_STUFE2_TIMER=wert_01                      BFD_STUFE3_TIMER=wert_02                      FLC_LED_AKTIV=nicht_aktiv
ALC_DEF_AKTIV=nicht_aktiv                     PIN49_BFD=nicht_aktiv                         PIN38_BFD=nicht_aktiv
ALC_BLK_PER=wert_02                           INTERM_FL=nicht_aktiv                         AH_US_OPTION=aktiv
PIN38_20_PARK=nicht_aktiv                     PIN29_30_PARK=nicht_aktiv                     HEIMLEUCHTEN_SL3_H=nicht_aktiv
PIN29_30_BL_NSL=nicht_aktiv                   FL_AL_AUS=nicht_aktiv                         ANHAENGERMODUL_PWM_WERT=wert_01
BL_ERSETZ_DEFEKT_SL=nicht_aktiv               PIN_29_30_AHM_ERS_FU_GESP=aktiv               PIN_5_10_AHM_ERS_FU_GESP=aktiv
XENON_TEST=nicht_aktiv                        XENON_TIMEOUT=wert_01                         XENON_TIME=wert_01
KL58_HELLIGKEITSSTUFE=wert_01                 U_POTI_DIMMER_MIN=wert_01                     U_POTI_DIMMER_DELTA=wert_01
MELDUNG_AENDERUNG_DIMMER=wert_01              POTI_DIMMER_INVERS=aktiv                      POTI_LWR_INVERS=nicht_aktiv
LEUCHTDICHTE_EXPO=aktiv                       TELEGRAMM_ZEIT_ZYKLUS=nicht_aktiv             TAGFAHRLICHT_ECE=nicht_aktiv
FL_UND_NSW_NICHT_GLEICHZ=aktiv                BI_XENON=nicht_aktiv                          SL_VO_ANSTEUERUNG=nicht_aktiv
SIDEMARKER_US=aktiv                           NSL_ALS_STANDLICHT=nicht_aktiv                PIN_20_ALS_SL_LI_3_ANSTEU=nicht_aktiv
PIN_20_ALS_FRA_LI_VO_2=nicht_aktiv            PIN_37_ALS_SL_RE_2=nicht_aktiv                PIN_37_ALS_FRA_RE_VO_2=nicht_aktiv
PIN_38_ALS_SL_RE_3=nicht_aktiv                BREMSLICHT_ALS_STANDLICHT=aktiv               STANDLICHT_ALS_NSL_LINKS=nicht_aktiv
STANDLICHT_ALS_BREMSLICHT=nicht_aktiv         DRL_BLK_VORN_GEDIMMT=nicht_aktiv              GED_FL_ALS_DRL=nicht_aktiv
BLINKIMPULS_WARNBLK=wert_02                   BLINKIMPULS_CRASHBLK=wert_02                  DRL_BLK_VORNE_2_GEDIMMT=nicht_aktiv
STANDLICHT_ALS_NSL_RECHTS=nicht_aktiv         BEGRENZUNGSLICHT_IN_PARK=nicht_aktiv          CRASH_WARNBLINKEN=aktiv
TAXI_ENABLE=nicht_aktiv                       BETR_STD_NICHT_LOESCHEN=nicht_aktiv           SCHALTER2_BL=nicht_aktiv
CRASH_KLEMME_58G_EIN=aktiv                    DRL_DIMMUNG=wert_02                           TASTVERH_KL_58G_MIN=wert_01
ZUWACHS_TASTVERH_KL_58G=wert_01               TAST_WBLKTASTER_MIN=wert_01                   TAST_WBLKTASTER_ZUWACHS=wert_01
HEIMLEUCHTEN=wert_02                          HEIMLEUCHTEN_AL=aktiv                         HEIMLEUCHTEN_SL_H=aktiv
HEIMLEUCHTEN_FL=nicht_aktiv                   HEIMLEUCHTEN_KL58G=nicht_aktiv                HEIMLEUCHTEN_SL_V=nicht_aktiv
HEIMLEUCHTEN_NSW=nicht_aktiv                  HEIMLEUCHTEN_KZL=aktiv                        HEIMLEUCHTEN_BL=nicht_aktiv
ADU_UNTERGRENZE=wert_01                       ADU_OBERGRENZE=wert_01                        ABSCHALTUNG_UNTERSPG=wert_01
ABFRAGEZEIT_AHM=wert_01                       KL58_HELLIGKEITSSTUFE_FLC=wert_01             STEIG_KL58_T_PER_D=wert_01
BLK_DIMMEN=nicht_aktiv                        SL_X_3_ERSETZT_DEFEKT_BL=nicht_aktiv          SL_ERSETZT_DEFEKT_BL=aktiv
RECHTS_LINKS=nicht_aktiv                      NSL_ERSETZT_DEFEKT_BL=nicht_aktiv             SL_ERSETZT_DEFEKT_BLK=nicht_aktiv
SL_3_ERSETZT_DEFEKT_BLK=nicht_aktiv           BL_ERSETZT_DEFEKT_BLK=aktiv                   BIXENON_EIN_BEI_LICHTHUPE=nicht_aktiv
PIN_20_ALS_SIDEMARKER=nicht_aktiv             PIN_20_ALS_NSL=aktiv                          GEDIMMT_BLK_BEGRENZ_LICHT=aktiv
GEDIMMT_BL__BEGRENZ_LICHT=aktiv               PHASE_AUS_GEDIM_LICHT_AUS=aktiv               SPG_NACHREGELUNG_LANGSAM=nicht_aktiv
P_10_5_ALS_BL_FUNKTION=aktiv                  PWM_WERT2_ALS_BL_AUSGANG=wert_01              PWM_WERT2_ALS_SL_AUSGANG=wert_02
PWM_WERT2_NSL_ZUSATZFKT=wert_01               PWM_WERT2_BLK_ZUSATZFKT=wert_02               PWM_WERT2_FL_BIXENON=wert_01
PWM_WERT2_SL3_ZUSATZFKT=wert_01               LEUCHTWEITENREGELUNG=nicht_aktiv              HALB/VOLLSCHRITT=halbschritt
TEST_OD_ST2_OHNE_NSW=nicht_aktiv              SP_MOTOR_STOP=nicht_aktiv                     SP_F_EINTR_OD_ALC_NSW_PIC=aktiv
TR_F_EINTR_OD_ALC_AL_FPIC=aktiv               SP_BEWERT_OD_ALC_NSW_AUS=aktiv                TREIBER_STOP_OD_ALC_RE_OK=aktiv
U_POTI_0_OD_FAILSAFE_ON=wert_01               U_POTI_1_OD_DAEMMERSTUFE=wert_01              U_POTI_2_OD_ALC_PARA_01=wert_01
SCHRITTE_0_OD_ALC_AKTIV_0=wert_04             SCHRITTE_1_OD_ALC_AKTIV_1=wert_07             SCHRITTE_2_OD_ALC_AKTIV_2=wert_09
ABS_MIN_2_OD_ALC_AKTIV_3=wert_09              SCHRITT_GRENZE_OD_ALC_IO=wert_01              TEMP_GRENZE_OD_ALC_NIO=wert_01
HYSTERESE_OD_AL_XENON_IO=wert_01              T_STROM_OD_ALC_PARA_02=wert_01                REF_LAUF_ZAHL_OD_ALC_1=wert_02
REF_LAUF_STEP_OD_ALC_2=wert_02                REF_LAUF_T2_OD_ALC_3=wert_01                  REF_LAUF_T1_OD_ALC_4=wert_02
SCHRITTABSTAND_STARTPHASE=kennlinie_01        M_TELEGRAM_OD_ALC_5=nicht_aktiv               LWR_INVERS_OD_ALC_6=wert_01
S_MOTORWEG_OD_ALC_7=wert_02                   TEMP_RAMPE_OD_ALC_8=aktiv                     LWR_VORZEICHEN=nicht_aktiv
LEUCHTWEITENREG_AUTOM=nicht_aktiv             LEUCHTWEITENREG_DYNAM=nicht_aktiv             AUSWERT_PROP_ABWEICHUNG=aktiv
AUSWERT_GRADIENT=aktiv                        KENNLINIE_LWR_SENSOR_VO=wert_01               KENNLINIE_LWR_SENSOR_HI=wert_01
DEF_LWR_SENSOR_HI=wert_01                     LWR_NEIGUNG_KONSTANTE=wert_01                 OFFSET_LWR=wert_01
EPSILON_DELTA_AV=wert_01                      EPSILON_DELTA_A=wert_01                       ANHEBUNG_175_KM/H=wert_01
ABSENKUNG_10_KM/H=wert_01                     VMAX_BESCHLEUNIGUNG=wert_01                   VMIN_BESCHLEUNIGUNG=wert_01
VMAX_BREMSEN=wert_01                          VMIN_BREMSEN=wert_01                          SCHW_GRAD_BESCHLEUNIGUNG=wert_01
SCHW_GRAD_BREMSEN=wert_01                     SCHW_PROP_ABWEICHUNG=wert_01                  DIFFERENZ_MSP_DYN_STAT=wert_01
DAUER_DYN_NACHFUEHRUNG=wert_01                ABTASTRATE_DYN=wert_01                        MITTELUNGSINTERV_DYN=wert_01
MIN_STEIGUNG_VZ_WECHSEL=wert_01               MITTELUNGSINTERV_VZ_WECHS=wert_01             MINDESTANZAHL_VZ_WECHSEL=wert_01
HOEHENWEG=wert_01                             ABTASTRATE_TREND=wert_01                      MITTELUNGSINTERV_TREND=wert_01
SCHW_TREND=wert_01                            ABWEICHUNG_TREND=wert_01                      GRADIENT_SCHLECHTWEG=nicht_aktiv
NACHLAUF_SCHLECHTWEG=wert_01                  SAETT_TIMER_SCHLECHTWEG=aktiv                 SCHW_GRADIENT_SCHLECHTWEG=wert_01
LH_MIT_BIX=nicht_aktiv                        FL_ALS_SL_LR=nicht_aktiv                      FL_DRL_MIT_RL=nicht_aktiv
PO_ALS_DRL=nicht_aktiv                        PIN_20_37_ALS_PO=nicht_aktiv                  HEIMLEUCHTEN_BLK=aktiv
CYCL_TI_BLK=einmal                            PIN20_PWM_BLK=wert_01                         PIN37_PWM_BLK=wert_01
PIN49_PWM_BFD=wert_01                         LAENGE_LWR_REF=wert_01                        LAENGE_LWR_STELL=wert_01
LWR_DIAG_PARAM=wert_01                        PROGRAMMPARAMETER_LCM_1=wert_01               PROGRAMMPARAMETER_LCM_2=wert_01
PROGRAMMPARAMETER_LCM_3=wert_01               PROGRAMMPARAMETER_LCM_4=wert_01               PROGRAMMPARAMETER_LCM_5=wert_01
PROGRAMMPARAMETER_LCM_6=wert_01               PROGRAMMPARAMETER_LCM_7=wert_01               PROGRAMMPARAMETER_LCM_8=wert_01
```
