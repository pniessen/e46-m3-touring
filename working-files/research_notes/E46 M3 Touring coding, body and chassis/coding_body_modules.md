# Body-module coding for the S54/M3 Touring: NCS Expert, the M3 cluster, the light module, the switch centre, the other body modules and the vehicle order

Round 4 research notes, 22 Oct 2026.

**The car.** A US 2003 E46 325i Touring: M54, 5-speed manual, rear-wheel drive, registered in Massachusetts. It has an MS43 DME if built before 03/2003, an MS45.1 from 03/2003.

**The donor.** A US 2003–06 E46 M3 with a manual gearbox. Its DME is an MSS54 to about 09/2003 and an MSS54HP after that; its DSC is a Teves MK60.

**The default plan.**
- The Touring keeps its body harness, light module (LSZ/ALSZ), MK60, booster and master cylinder.
- It takes the M3's axles, steering, brakes, cluster and front end.
- The tools are INPA, NCS Expert and Tool32 on a K+DCAN cable, plus PA-Soft for EEPROM work.

**Tags.**
- **[read]**: I read the text myself, either downloaded and converted or on the page.
- **[snippet]**: I saw only a search-result snippet or a search summary.
- **[title only]**: a YouTube title, obtained through oEmbed; I didn't watch the video.
- **[earlier round]**: read in an earlier research round; the citation is copied from `E46 M3 Touring open questions/coding_body_chassis.md`.
- **Inference**: my own reasoning, which no source documents.
- Each finding says which chassis, market and build date it applies to.
- Translations from German are mine.

**Sources I couldn't reach.** I stopped at the first block each time and got round nothing.
- **WebSearch:** the turn's 200-call budget ran out during this round. I made no further searches and used no other search route.
- **e46fanatics:** a proof-of-work bot check on every page. This round has search snippets only; reads from the earlier round are tagged [earlier round].
- **Challenge pages:** bimmerfest, 1erforum.de, ZHP Mafia, modbm.com and manualmachine.com.
- **bmwfaq:** the "Pérdida FA" thread is behind Cloudflare. Thread 971406 loaded, but it's about a 320d.
- **YouTube:** caption fetches hit the "not a bot" check three times, so I stopped. I have four titles only.

All downloads are under `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/round4-dl/coding-body/`, one folder per source.

---

## Takeaway: what changes in the guide

1. **After the chip route, the M3 cluster carries the donor's vehicle order (FA), not yours.**
   - The FA sits in the cluster's EEPROM. BMW's KOMBI46R job `C_FA_LESEN` reads it from cluster addresses 0xC2–0x181 on coding index > 22.
   - An owner who virginizes index-24 clusters says "the VO is brought back onto the new Chip".
   - So after Session 4, AKMB holds the M3's type key, options and date. Any later session that reads the FA "from AKMB" (the guide's Sessions 4, 5 and 8) would code from an M3 coupe order.
   - **Fix:** read the FA from ALSZ, the Touring's untouched copy. Check it against the Session 1 screenshot, then `FA_WRITE` it to AKMB and re-read both.
   - If NCS refuses AKMB with your FA, keep ALSZ as the only FA source. Section 6 and G4 give the branch.
2. **EWS is not a fallback FA source on a 2003 car.** BMW's E46SGFAM flags EWS as ZCS-only (FA flag 0). The FA lives in AKMB and ALSZ, so the fallback is ALSZ.
3. **Never default-code the M3 cluster in this car.**
   - Default coding means a blank MAN, Expert Mode `SG_CODIEREN`, Process Car/Code Car, or a service coding "from the factory FA".
   - Write it only from a complete `FSW_PSW.MAN` made from its own trace, with only the intended lines changed.
   - Drop "Process Car → Code Car" from Session 8. It would also overwrite the hand-set M3 MK60 values and every customisation (terra: "you'll lose all customizations you've ever made").
4. **`TANK_KENNLINIE` is not a choice of three.**
   - In a real KMB trace, the one function lists `60_l_literskala`, `dad_tank_diesel` and `metalltank` together.
   - NCS lists every keyword that maps to the stored value; Revtor: "If NCS Dummy displays multiple checked parameters for a function they all have the same data value".
   - Leave it as read, and check it with a measured fill.
5. **Use NCS Expert 4.0.1.**
   - Use 4.0.1 from Standard Tools 2.12 with a manipulation profile (Revtor's `NCSDUMMY4.PFL`, or terra's "Expert Mode w/ Manipulation") on 64-bit Windows.
   - Version 3.x "doesn't work at Win x 64bit, because of NTVDMs is not present".
   - IFH-0009 means "NO RESPONSE FROM CONTROLUNIT": check the cable, pins 7/8, the COM port, the ignition and the module chosen. It isn't a version fault.
6. **Lamp switches: confirmed on index 24.**
   - A coding-index-24 cluster in an S54 swap had `GENERATOR_UEBER_CAN` and `TOG_UEBER_CAN` set to aktiv and `CAN_OELDRUCKSCHALTER` set to nicht_aktiv.
   - A pre-2003 non-M cluster trace (KMB_E46.C04) has none of the three, and neither does a 2002 M3 convertible's AKMB list.
   - So look for them on redesign clusters (23/24, and probably 07/08). The guide's values (`nicht_aktiv` with the wires) stand.
7. **The light module.**
   - **Xenon:** BMW's own retrofit (EBA 01 29 9 416 445, 1.2002):
     - It replaces the light module.
     - It adds front-right and rear-right level sensors on LSZ X12 pins 19/22/23 and 46/14/26.
     - It codes through DIS "Retrofit", which "stored [the retrofit] in the central coding key of the IKE/instrument cluster".
   - **Levelling parameter names:** in real traces they are `LEUCHTWEITENREGELUNG`, `LEUCHTWEITENREG_AUTOM` and `LEUCHTWEITENREG_DYNAM`. `AUTO_LWR_ENABLE` appears only in an unsorted "other cars" list.
   - **Fog lights:** ETK lists different light modules without fog lights (61319133022/023) and with them (…024 to …027). Adding fogs to a Touring that lacks them may need a module change.
8. **MFL buttons need no coding.** BMW's retrofit: "Coding of the vehicle must not be carried out."
   - **Wiring:** X10170 pin 8 → DME X60004 pin 27 (the same pin on the MSS54), pin 9 → LSZ X12 pin 21 (K-bus), pin 10 → X12 pin 27 (terminal R).
   - Afterwards, clear DME adaptations so the DME relearns the cruise buttons; the guide's Session 6 already lists `STAT_FGR_MFL_VERBAUT_WERT`.
9. **The switch centre has no NCS coding.**
   - Its SGBD (SZM46) only reads "17 Codierbytes", and no SZM row appears in the E46 coding data samples.
   - `$7MA` is the M3 Competition package option (ETK S7MAA, from 12/2004).
   - M Track = an M3 MK60 coded for it, plus AKMB `ANZEIGE_HOCHLADEN` = `aktiv` written through a MAN. Skip ECUWorx's default `SG_CODIEREN` of AKMB in this car.
10. **The vehicle order.**
    - Keep the Touring's type key and production date.
    - Add option codes only for hardware you actually fit.
    - `FA_WRITE` on its own changes nothing (terra).
    - After an FA change, code only the modules that change affects.
    - Clear DME adaptations only when the change touches the engine side (cruise/MFL wiring, A/C, fuel pump, gearbox). A cluster or light option doesn't need it.
11. **Keep the coding files for the car's life.** Revtor: "if the vehicle is ever recoded using the ZCS or FA all your changes will be lost". Keep:
    - the cluster's final MAN and the MK60's;
    - a note telling any workshop not to run Code Car.
12. **The tank job is misnamed in the guide.** Tool32's `STATUS_TANKINHALT_LESEN` belongs to `KOMBI46.PRG`, the older cluster. The redesign SGBD `KOMBI46R.PRG`, which covers M3 index 23/24, uses `STATUS_AIF_TANKDATEN_LESEN` instead.

---

## 1. NCS Expert on an E46

### Cited findings

**Which module holds the vehicle order**

- **BMW E46 data (E46SGFAM.DAT), as quoted by the ncsx reverse-engineering project** [read] ([ncsx: daten-format §2.6](https://github.com/emdzej/ncsx/blob/main/docs/daten-format.md), [ncsx: ecu-selection](https://github.com/emdzej/ncsx/blob/main/docs/ecu-selection.md)). *(E46, all markets; the data NCSEXPER 4.0.1 ships with.)*
  - Rows: `S AKMB A_AKMB46 C_KMB46 0 1`, `S KMB A_KMB46 C_KMB46 1 0`, `S EWS A_EWS3 C_EWS3 1 0`, `S AEWS A_AEWS3 C_EWS3 0 0`, `S DSC A_ASCDSC C_ASCDSC 0 0`.
  - Columns 5 and 6 are the ZCS and FA flags. Column 6 means "does this SG carry FA data".
  - The ALSZ row is in E46SGET: `LSZ C31 A_ALSZ C_LSZA ALSZ`.
- **The cluster stores the FA in its EEPROM** [read] ([SGBD: KOMBI46R](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46R.md)).
  - KOMBI46R.PRG is "KOMBI E46 Redesign", BMW TI-431, rev 2.10.
  - Its `C_FA_LESEN` reads "Gueltiger Adressbereich: 0x10 - 0xDF (416 Bytes) für E46 (Codierindex < 7 und 19 < Codierindex <= 22); Gueltiger Adressbereich: 0xC2 - 0x181 (384 Bytes) für E46 (Codierindex > 22 und 7 <= Codierindex <= 19)".
  - It also has `C_FA_AUFTRAG` (write) and `C_FA_LOESCHEN` (delete).
  - *(E46 clusters; the second range covers M3 23/24 and non-M 07/08.)*
- **The light module holds the second copy** [read] ([SGBD: LSZ_2](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ_2.md)). *(E46 from 09/2001.)*
  - LSZ_2.PRG is "LSZ fuer E46 PU 09 / 2001, E85, E83 bis MÜ 09 / 2006", rev 4.000.
  - Its jobs include `C_FA_LESEN`, `C_FA_AUFTRAG` ("Fahrzeugauftrag schreiben mit Gegenverifikation", write the vehicle order and verify it) and `C_FG_AUFTRAG` ("Beschreiben der red. Datenablage mit der FG-Nummer", write the VIN into the redundant storage).
- **terra (NAM3 administrator, Mar 2020)** [read] ([NAM3: Getting started with NCS Expert](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert)): "In the E46 you'll see 4 different options: AKMB, ALSZ, EWS, and KMB. If your car is built in 09/2001 or later, you'll want to pick AKMB or ALSZ (both should have the same options stored unless your car has been messed with in the past). If your car was built earlier, pick EWS or KMB".
- **bmwfnatic (NAM3, Sep 2023)** [read] ([NAM3: MK60 swap coding](https://nam3forum.com/forums/forum/special-interests/coding-tuning/232995-mk60-swap-coding)): "for FA cars this is stored in the LSZ (light switch) or the KOMBI". Without those modules, "create a purely virtual Vehicle Order that we load into NCS via a .ssd file".
- **The ZCS block moved in 2003** [read] ([ncsx: zcs-write](https://github.com/emdzej/ncsx/blob/main/docs/zcs-write.md)): it's at WORTADR 104 in `KMB_E46.C02–.C06` ("pre-2003 layout") and at 368 in `KMB_E46.C07–.C08` ("2003+ layout").
- **FA string format** [read] ([ncsx: fa-format](https://github.com/emdzej/ncsx/blob/main/docs/fa-format.md)):
  - Example: `E46_#0303*BW32%0A08&N6TT|7531125|7529012$205$210…$880`.
  - `#` is the production date, `*` the type key, `%` the paint, `&` the upholstery and `$` the option codes.
  - The E46 `AT.M00` dictionary lists type keys and option codes as selectable "W" entries (examples BW32, EP31, BL91, 205, 880).
  - It lists only four "Z" production-date markers (#0904, #0305, #0905, #0306) in a file dated `DATUM 22.01.2007` ([ncsx: daten-format §2.3–2.4](https://github.com/emdzej/ncsx/blob/main/docs/daten-format.md)).

**Profiles and "Expert Mode"**

- **The profiles NCSEXPER 4.0.1 ships with** [read] ([ncsx: pfl-format](https://github.com/emdzej/ncsx/blob/main/docs/pfl-format.md)):

  | File | Display name | What it allows |
  |---|---|---|
  | `01_Default.pfl` | Default Profil | Read only |
  | `Car Key Memory.pfl` | Car & Key Memory | — |
  | `Expertenmodus.pfl` | Expertenmodus 2.0 | Per-ECU and per-car coding; FSW/PSW manipulation through an inline dialog |
  | `Expertmodus (offen).pfl` | — | The loosest profile |
  | `Expertmodus (Werkseinstellung).pfl` | — | "Factory variant — Individual disabled, FSW/PSW manipulation off" |
  | `ZCS bei Änderung schreiben.pfl` | — | — |
  | `NCSDUMMY4.PFL` | — | For NCS Dummy |

  Key settings:
  - `[FSWPSW] FswPswLesenModus`, 0–2. Value 1 builds the FSW/PSW values from the FA.
  - `FswPswManipulieren`.
  - `FswPswLeseDatei`, which reads FSW/PSW from a file.
  - `[CODING] FktFzgCodieren`, which shows the "Code car" button.
  - `FktSgAuslesen`, which shows "Read ECU".
- **Revtor (NCS Dummy manual v0.6.10, 2020)** [read] ([Revtor: NCS Dummy manual](https://revtor.be/ncsdummy/ncsdummy.pdf)):
  - "The default profile that comes with NCS Expert, 'Expertenmodus' (C:\NCSEXPER\PFL\FZG2.PFL), does not support trace manipulation."
  - Download the NCS Dummy profile for NCS Expert 3.x or 4.x and put `NCSDUMMY3.PFL` or `NCSDUMMY4.PFL` in `C:\NCSEXPER\PFL\`.
  - In `C:\NCSEXPER\WORK\`, "create a new empty text file named FSW_PSW.MAN".
  - His profile defaults to the read job `CODIERDATEN_LESEN`.
- **terra** [read] ([NAM3 1281](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert)): "An NCS Expert Profile with manipulation enabled … (requires NCS Expert V4 – included with the BMW Standard Tools 2.12 …). Copy the profile to C:\NCSEXPER\PFL". Then load "Expert Mode w/ Manipulation".
- **E46Zone (Razza77, Jun 2012)** [read] ([E46Zone: Guide to coding with NCS Expert](https://www.e46zone.com/forum/topic/36596-guide-to-coding-with-ncs-expert/)). *(E46, UK; NCS Expert version not given.)*
  - Copy "Expertmode" to a new profile and open File → Edit; the post gives the editor password.
  - Under 'Individualisierung' cross all the options.
  - Under 'FSW/PSW' choose 'from CVT' and cross the bottom two boxes.
  - Press 'consistence check'.
  - "You read using the 'Expertmode' profile, and code using the 'Godfather' profile."
- **ECUWorx** [read] ([ECUWorx: M-Track PDF](https://www.ecuworx.co.uk/uploads/M-Track.pdf)): "NCS-Expert profile that allows for manipulation … 'FISTER Profile' or 'Revtor's NCS Expert Profile' both work well".
- **NAM3, Dec 2025** [read] ([NAM3 331072](https://nam3forum.com/forums/forum/special-interests/coding-tuning/331072-need-help-starting-with-ncs-expert-manipulation-profile)): "Contact Alphabimmer for revtor's profile and the daten update".

**NCS Expert version and Windows**

- **ppm008 (NAM3, Feb 2024)** [read] ([NAM3 1281, page 3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert/page3)): "Old NCSexper doesn't work at Win x 64bit, because of NTVDMs is not present. New NCSexper not working on E46". Later in the thread: "NCSEXPER Ver3 works under Win7 on E46 perfectly, Ver4 didn't work".
- **Tbonem3 (Mar 2025)** [read], same page:
  - "You don't need Win 7, but you do need to install the software suite as administrator with win 7 compatibility."
  - "I installed it last night on win 10 x64 and it's working fine."
  - "whatever suite of standard tools you download will have the datens only for the chassis that matches the forum you found the links on".
- terra's E46 profile requires version 4 (above).

**Reading a module's coding: Revtor's steps** [read] ([Revtor](https://revtor.be/ncsdummy/ncsdummy.pdf))

| Step | Action |
|---|---|
| 1–3 | File → "Load Profil" → choose the profile |
| 4 | "VIN/ZCS/FA" (F1) |
| 5 | "ZCS/FA f. ECU" (F3) |
| 6 | Choose the chassis |
| 7 | Choose a module that stores the ZCS or FA |
| 8 | The VIN and car data appear |
| 9 | "Back" (F6). Revtor: "the default job is 'SG_CODIEREN' (coding) which we definitely don't want, so pay attention" |
| 10 | "Process ECU" (F4), which "really means 'Select ECU'" |
| 11 | Choose the module |
| 12–15 | "Change job" (F2) → `CODIERDATEN_LESEN`; confirm JOBNAME |
| 16 | "Execute job" (F3). "NCS Expert may indicate it's coding but it's really only reading" |
| 17 | "write down the *.C?? module description file name displayed right below 'JOBNAME = CODIERDATEN_LESEN' … after reading, as the module description file shown before reading is the one NCS Expert expects and not necessarily the one that is actually present in the vehicle!" |

- **"Read ECU" (F4)** does steps 12–16 in one go but "always opens an annoying nettodata window".
- **The trace file is temporary.** "NCS Expert uses FSW_PSW.TRC as a temporary file for other purposes as well … most of the time the FSW_PSW.TRC trace file does not contain valid traces." "Do not perform any other actions in NCS Expert until the trace files are … saved to another location."
- **Naming:** `CHASSIS-MODULE[-optionaltext].TRC`, for example `E31-EKM.C25-FSW_PSW.TRC` and `E31-EKM.C25-NETTODAT.TRC`.
- **E46Zone** [read]: "this file is overwritten each time a read out of a module is performed … If you make some mistake, use your original as the .man file to change them back."

**Writing a module's coding from a MAN file**

- **Revtor §6.2** [read]: the same screens, with job `SG_CODIEREN`.
  - "Make sure the 'FSW_PSW.MAN' manipulation file in C:\NCSEXPER\WORK\ is for the same module."
  - "some modules require the ignition to be switched off and on before the changes take effect".
  - "When switching between chassis it is recommended to empty (not delete) the FSW_PSW.MAN file after coding."
- **What a MAN covers** [read], same source:
  - "If NCS Dummy displays multiple checked parameters for a function they all have the same data value."
  - "Excluded functions are ignored by NCS Expert and whatever was set for this function before coding will remain after coding."
  - "FSW/PSW or nettodata coding does not change the vehicle central coding key (ZCS) or vehicle order options (FA)… if the vehicle is ever recoded using the ZCS or FA all your changes will be lost… keep a backup of the FSW_PSW.MAN … It is also strongly recommended to keep a backup of the original unmodified FSW_PSW.TRC and NETTODAT.TRC."
  - NCS Dummy can load two traces and show their differences ("Compare Trace 2…").
- **A blank MAN with terra's profile** [read] ([NAM3 1281](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert)):
  - "Since your FSW_PSW.MAN file is blank, NCS Expert will determine how to set every option in your ALSZ module by your VO… If you had previously customized your ALSZ module, you'll lose the customizations you've made."
  - "you should never use someone else's FSW_PSW file."
- **Save it as .MAN, not .TXT** [read] ([E46Zone 36596](https://www.e46zone.com/forum/topic/36596-guide-to-coding-with-ncs-expert/)): "common mistakes here is saving the .man folder incorrectly as a .txt file". In Notepad's Save As, choose "All files".

**Process ECU versus Process Car**

- **terra** [read]: "You can also hit the 'Process Car' button instead of the 'Process ECU' button, and NCS Expert will attempt to recode every module in the car. I generally don't recommend this since it can be buggy and you'll lose all customizations you've ever made."
- **Bali** [earlier round] ([e46fanatics FA DIY](https://www.e46fanatics.com/threads/diy-how-to-code-fa-for-at-mt-swap.1290835/)): Code Car "fails out on the first module coding failure. In this case just code the rest of the modules singly."

**Changing the vehicle order**

- **terra** [read]:
  - Read the VO, then "Enter VO/FA" → chassis → OK at the VIN.
  - "To add a VO code, type it in the box, and click the 'Add' button. To remove a VO code, select it from the list, and hit the 'delete' button."
  - "From this point, NCS Expert will be basing its coding decisions based on the VO you entered, not what the car has stored in its modules."
  - Process ECU → AKMB → "Change Job" → `FA_WRITE` → Execute; then "Change SG/SGET" → ALSZ → `FA_WRITE`.
  - "The VO and ZCS … do not directly impact the code itself (i.e. changing the VO/ZCS without also coding modules will not actually change how your car functions)."
- **ECUWorx** [read] ([M-Track PDF](https://www.ecuworx.co.uk/uploads/M-Track.pdf)): "Under Attribute type in '$7MA' and click 'add'".
- **terra, May 2020** [read] ([NAM3 21981](https://nam3forum.com/forums/forum/special-interests/coding-tuning/21981-ncs-error-while-trying-to-recode-used-gm5-module)):
  - "You can just read the VO from the other car. Or even just enter the VO manually. The module itself doesn't actually care what the VO is. You can also just code it on the bench".
  - "VIN will only be written if you specifically do the FGNR_SCHRIEBEN job".
- **How NCS picks the module file** [read] ([ncsx: ecu-selection §5–8](https://github.com/emdzej/ncsx/blob/main/docs/ecu-selection.md), [ncsx: assumptions A7](https://github.com/emdzej/ncsx/blob/main/docs/assumptions.md)):
  - It walks `E46SGET.000` with the session's FA. Each row carries an `AUFTRAGSAUSDRUCK`, a true/false expression over the FA's option bits.
  - It then reads the module's own coding index and opens `<name>.C<index>`.
  - The metadata panel shows the result, for example "KMB_E46.C08, A_AKMB46.IPO, KOMBI46R.PRG".
  - Sample E46SGET rows: `KMB_E46 C06` for KMB and AKMB; `KMB_E46 C07` with SGBD `KOMBI46R`; `KMBE46M3 C20`; `EWS C81`; `LSZ C31`.
  - The AKMB job script handles `SG_CODIEREN`, `TEILBEREICH_CODIEREN`, `FGNR_SCHREIBEN`, `ZCS_SCHREIBEN` and `ZCS_LOESCHEN`. `FGNR_SCHREIBEN` uses `C_FG_LESEN` to verify ([ncsx: call-architecture](https://github.com/emdzej/ncsx/blob/main/docs/call-architecture.md)).

**Data files (SP-Daten) for 2003–06 cars and M3 modules**

- **ncs-expert.com (vendor)** [read] ([product page](https://ncs-expert.com/product/e46-sp-daten), [update matrix](https://ncs-expert.com/sp-daten-update-matrix)): "E46 model 2025/12 V75 SP-DATEN". The matrix, updated 17 Apr 2026, lists V75 as the latest and V32 as "Base / Original".
- **Two claims seen only in snippets** [snippet]: V32 dates from 2008, and v74 was "the last" BMW release.
- **ECUWorx** [read], for E46 M3s with MK60: "Daten files applicable for your car (if 2005 or later, updated files from Progman or Ista/P are required)".
- **Cluster files** [snippet] (e46fanatics "DIY E46 cluster gauges definitions"; KamilFKH's layout notes are [earlier round]): `KMB_E46.C07`, `KMB_E46.C08`, `KMBE46M3.C23` and `KMBE46M3.C24` are in the E46 SP-Daten.

**Error messages**

| Message | Meaning | Fix | Source |
|---|---|---|---|
| IFH-0002 | "NO RESPONSE FROM INTERFACE" | Cable, driver, COM port in `obd.ini` | [EdiabasLib](https://github.com/uholeschak/ediabaslib) (EdiabasNet.cs) [read] |
| IFH-0003 | "DATATRANSMISSION TO INTERFACE DISTURBED" | Cable, USB, latency | same [read] |
| IFH-0009 | "NO RESPONSE FROM CONTROLUNIT" | Ignition on, pins 7/8 bridged, right module, module powered | same [read]; pins 7/8: terra, sapote ([NAM3 1281](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert), [page 3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert/page3)) [read] |
| IFH-0010 | "DATATRANSMISSION TO CONTROLUNIT DISTURBED" | Wiring, power, bus | EdiabasLib [read] |
| IFH-0018 | "INITIALIZATION ERROR" | Interface not set up | same [read] |
| IFH-0032 | "IGNITION IS OFF" | Key to position 2 | same [read] |
| IFH-0037 | "LOW UBATT" | Charger on | same [read] |
| SYS-0002 / SYS-0005 | "ECU OBJECT FILE NOT FOUND" / "OBJECT FILE NOT FOUND" | SGBD missing from `C:\EDIABAS\ECU` | same [read] |
| SYS-0008 | "JOB NOT FOUND" | Wrong SGBD for that job (KOMBI46 vs KOMBI46R) | same [read] |
| COAPI-1020 | "can not open file for reading" | `FSW_PSW.MAN` missing, or saved as `FSW_PSW.MAN.txt` | [Revtor](https://revtor.be/ncsdummy/ncsdummy.pdf) [read] |
| COAPI-1063 | "CABD-parameter error" | Job the module doesn't support, such as nettodata coding | Revtor [read] |
| COAPI-1141 / 1142 | "FSW faulty" / "PSW faulty" | MAN not emptied after coding: empty it, don't delete it | Revtor [read] |
| COAPI-1143 | "error during processing of CBD-file" | Errors in the MAN, or the wrong module | Revtor [read] |
| COAPI-2000 | "EDIABAS or SGBD error" | With "VIN is faulty": interface or pins 7/8. Otherwise outdated DATEN/SGDAT/ECU files | Revtor [read]; sapote: "Most of the time it's due to the switch on the cable connector that not connecting pin7 and pin8" ([NAM3 1281, page 3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert/page3)) [read] |
| COAPI-2020 | "no answer from ECU" | Module not fitted, dead or unpowered | Revtor [read] |
| COAPI-2060 to 2099 | BMW: end the session, disconnect all equipment and the charger, "Perform a battery reset for 15 minutes", reconnect | On a used GM5, the cause was "one of the inner blue wires" loose in the GM5 plug | [BMW CoApi list](https://nam3forum.com/forums/filedata/fetch?id=21984) [read]; [NAM3 21981](https://nam3forum.com/forums/forum/special-interests/coding-tuning/21981-ncs-error-while-trying-to-recode-used-gm5-module) [read] |
| COAPI-7032, 7042, 7052, 7062, 7412, 7422, 7432 | BMW: as above, then "Check power supply", "Check ground supply", check the bus (SI B61 03 03) | — | BMW CoApi list [read] |
| "Codierindex … nicht zulässig" | The FA's production date or type doesn't allow this module's index | Session-only FA change | [earlier round] e46fanatics 1293250 and 1264623 |
| "Ungültiger Codierindex 24" | M3 cluster selected as KMB | Select AKMB | [earlier round] e46fanatics 1278842 |

### Inferences

- **Which version.** On 64-bit Windows, use NCS Expert 4.0.1 with a manipulation profile. A 32-bit Windows 7 laptop with 3.x is the fallback for anyone who can't get 4.x to talk to the car. Reports conflict, but none of the IFH errors above is version-specific.
- **Which module to read the FA from.** During the build, always read it from **ALSZ**: it's the copy that never leaves the car. AKMB is reliable only once it has been re-read and matches.
- **Use complete MANs.** A MAN copied in full from a fresh trace is safe whichever way a profile treats missing functions: "blank = default from the FA" (terra's) or "missing = keep" (Revtor's). A partial MAN isn't, so always export the complete trace.
- **The "Factory Coding" profile.** The guide's "Factory Coding" profile is almost certainly `Expertmodus (Werkseinstellung)`, which has manipulation off and codes purely from the FA. That's correct for Touring modules you haven't customised, and wrong for the M3 cluster and a hand-coded M3 MK60.
- **Verify every write.** Re-read the module, load the new trace and your MAN into NCS Dummy's compare mode, and expect only the lines you changed to differ.
- **Data files.** Check that the files exist rather than chasing version numbers: `KMBE46M3.C23/C24`, `LSZ.C35`–`C37`, and the MK60 index of the unit you code.

### Gaps

- I found no BMW document for NCS Expert's English button labels. They vary by version and language pack ("Change ECU" or "Change SG/SGET").
- I didn't find which SP-Daten version first carries `KMBE46M3.C24`, `LSZ.C37` or the latest MK60 index.
- The only evidence on 3.x versus 4.x on E46s is conflicting single reports.

---

## 2. The M3 cluster in a 325i Touring

### Cited findings

**Generation, coding index and files**

- **Coding-index groups** [earlier round] (KamilFKH, [e46fanatics: DIY E46 cluster gauges definitions](https://www.e46fanatics.com/threads/diy-e46-cluster-gauges-definitions.1324535/), [DIY M3 cluster into non-M, post #43](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)):
  - **Indexes:** non-M 02–05, then 06, then 07/08; M3 20–21, then 22, then 23/24.
  - **What the redesign brought:** "The redesign clusters are the only clusters with proper support for the Brake Force Display, M-Track control light". Index 08/24 adds only `ATEMP_WARNUNG_KALTLAND` over 07/23.
  - **The oil-level area:** non-M redesign clusters carry 15 extra oil-level functions there; M3 clusters fill it with `FF`.
- **ECUswap (German specialist)** [read] ([ECUswap: Kombiinstrument-Austausch E46](https://ecuswap.de/technikinfo-kombiinstrument-austausch-e46/)). *(E46, all markets.)*
  - There are "2 wichtige Baujahrgrenzen" (two important build-date limits): "das technische Facelift um 09/2001, und … um 09/2002".
  - "Neuere Kombiinstrumente in ältere Fahrzeuge zu verbauen ist kein Problem, im umgekehrten Fall aber führt es zu Problemen" (newer clusters in older cars are fine; the reverse causes problems).
  - "Ist das Fahrzeug jünger als 09/2002 so muss auch zwangsweise ein Kombiinstrument aus 09/2002 oder neuer verbaut werden" (a car built after 09/2002 must have a cluster from 09/2002 or later).
  - There are two looks: "Limo/Touring/Compact und … Cabrio/Coupé".
- **KOMBI46R covers index > 22** [read]: its FA address text says so, which makes it the SGBD for M3 index 23/24. `IDENT` returns `ID_COD_INDEX`, `ID_DIAG_INDEX`, `ID_BUS_INDEX` and `ID_DATUM_KW`.
- **BMW ST052, cluster test 01** [read] ([BMW ST052: E46 Driver Information Systems](https://archive.org/download/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03b_E46%20Driver%20Information%20Systems.pdf)):
  - Subtests: "1.0 VIN", "1.3 Coding/Diagnosis/Bus index", "1.4 Manufacturing date (Calender week/year".
  - "Tests 1 & 2 are always unlocked".
- **Selecting the module** [earlier round] ([e46fanatics: E46 M3 cluster coding](https://www.e46fanatics.com/threads/e46-m3-cluster-coding.1278842/)): NCS showed "Ungültiger Codierindex 24" when KMB was selected; the owner then selected AKMB for a 2004 M3 cluster.

**How a cluster legitimately gets the car's VIN and true mileage (BMW)**

- **BMW ST052, "Redundant Data Storage"** [read]. *(E46, all markets.)*
  - "Specific information is stored redundantly in the instrument cluster and in the Light Switch Module … VIN, Total Mileage, Service Interval data … The data is compared each time KL 15 is switched on. If the data does not match, the manipulation dot in the mileage display block will be illuminated."
  - The six rules, verbatim:
    1. "If the vehicle ID number is not the same in both modules, the manipulation dot is illuminated. All functions of both modules continue to operate."
    2. "Data will only be transferred from the LSZ to the cluster if the ID numbers match and the cluster mileage is zero."
    3. "The VIN is entered in the cluster through coding and will only be accepted when the cluster mileage is zero."
    4. "The stored mileage in the LSZ can only be overwritten by a higher mileage."
    5. "If the two mileage values stored vary by more than 120, and the VINs are the same, the cluster will continue to accumulate mileage and a fault will be stored in the cluster for data transfer."
    6. "If the K-Bus link fails, the cluster will continue to store mileage and set a fault for the Bus link."
  - Service interval: "After replacing the instrument cluster, completing encoding and allocation based on the vehicle identification number, the SIA data are transferred to the instrument cluster."
- **BMW ST052 Lighting** [read] ([BMW ST052: E46 Lighting Systems](https://ia800902.us.archive.org/26/items/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03c_E46%20Lighting%20Systems.pdf)): "If either the Cluster or LSZ has to be replaced, the data is taken from the remaining module and transferred to the replacement unit. This can only occur ONCE the VIN has been entered into the replacement unit. Once the VIN is entered, the module becomes part of the vehicle and can not be interchanged with another vehicle."
- **ECUswap** [read] ([technical page](https://ecuswap.de/technikinfo-kombiinstrument-austausch-e46/), [M3 cluster service](https://ecuswap.de/shop/e46-m3-kombiinstrument-programmierung-vin-km-codierung/), [cluster service](https://ecuswap.de/shop/e46-kombiinstrument-programmierung-vin-km-codierung/)):
  - VIN over OBD works "nur bei den allerersten Generationen der E46 Tachos" (only on the very first generation of E46 clusters).
  - They adapt mileage "ausschließlich zu Reparaturzwecken" (only for repairs).
  - On the FA: "Dieser muss wieder korrekt hinterlegt werden damit das Fahrzeug im Falle eines Werkstattaufenthalts korrekt diagnostiziert werden kann" (it must be stored again correctly so a workshop can diagnose the car).
  - Service text: "Den aktuellen Kilometerstand erhält das Kombiinstrument automatisch aus dem Fahrzeug" (the cluster takes the current mileage from the car automatically). If the car's reading is wrong, they require proof of the true mileage.
  - Coding: "Codierung anhand der Fahrgestellnummer mittels serienmäßigem Fahrzeugauftrag" (coding by VIN, from the factory vehicle order).
  - The M3 cluster service costs €120.
- **Huggins Racing** [read] ([cluster mileage/VIN correction](https://racehuggins.com/product/e46-cluster-mileage-vin-correction/)): "virginize a used e46 cluster, to allow it to be coded to your car's VIN, Mileage, and build specification", $125.
- **NAM3 154645** [read] ([NAM3: Cluster with coding index 0x24 virginization](https://nam3forum.com/forums/forum/special-interests/coding-tuning/154645-cluster-with-coding-index-0x24-virginization)):
  - nextelbuddy, Feb 2022: PA-Soft reads the cluster, but "the mileage and VIN areas are protected in the sense that they do not allow writing data via OBD". He writes a new chip, and "as soon as you turn ignition on in a car with an LCM that has a matching VIN, the mileage just updates and displays on the cluster".
  - Also: "the VO is brought back onto the new Chip … if its a 24 CI and you read the file … it should be exactly as it was except the proper Vin and Miles now".
  - t3ddftw (Feb 2022) was "dropping a C24h IKE into my Touring".
  - Bry5on ("'02 332iT", Mar 2025): "Dropping a new blank chip onto the cluster also works … I did write the VIN using PASoft but I'm not convinced even that was necessary".
- **Earlier-round reports:**
  - "You cannot write the VIN using NCS Expert, even after the odometer is reset" ([e46fanatics 1278842](https://www.e46fanatics.com/threads/e46-m3-cluster-coding.1278842/)) [earlier round].
  - A dealer "can program a 'brand new' cluster, but not a used one" ([NAM3 228697](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/228697-cluster-replacement)) [earlier round].
  - Bryson's S54 wagon (24H cluster, blank chip, PA-Soft): after the write, "pulled up NCS Expert, tweaked a few settings to read oil level and show the m-track button" ([e46fanatics 1277945 #32](https://www.e46fanatics.com/threads/diy-m3-cluster-into-non-m-retrofit.1277945/)) [earlier round].
- **Read-only checks** [read]:
  - KOMBI46R `STATUS_AIF_FG_NR_LESEN` returns `STAT_AIF_FG_NR`.
  - `C_FG_LESEN` returns `FG_NR`.
  - `STATUS_AIF_GWSZ_LESEN` returns `STAT_GWSZ_WERT` (unit "km").
  - LSZ_2 `SIA_LESEN` returns `FG_NR` ("7-stellig", 7 characters) and `GESAMTWEGSTRECKE_WERT` ("nur 100er Einheiten!", only in steps of 100; unit "100 km"), plus the SI counters ([SGBD: LSZ_2](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ_2.md)).

**The three lamp switches**

- **nextelbuddy (NAM3, Oct 2020): an S54 swap into a ZHP sedan** [read] ([NAM3 61405](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)):
  - "my cluster which is a coding index 24 cluster. I had alternator over can bus enabled oil level over can bus enabled but oil pressure over can bus not enabled."
  - "I switched that to enabled flashed it back to the cluster but still the oil light doesn't stay on."
  - The fix: "I just ran a wire from x60004 pin 11 to the cluster plug pin 13. used NCS export to change back to oil pressure via CAN bus not active... and now my oil light and alternator light are both on with the engine off."
  - He'd been on CSL software, "which wasn't originally programmed to handle Alternator via canbus", and found that "stock MSS54HP software … does support alternator via canbus".
  - *(US ZHP; the cluster is index 24, which is the M3 file number. He doesn't say whether it's an M3 or ZHP unit.)*
- **George Hill, same thread** [read]. From ISTA, M3: "X11175 Pin #13 KOMBI -> X60004 Pin#11 DME (BR/GN)" and "X60003 Pin #26 DME -> X6231 Oil Pressure switch (BR/GN)". ZHP: "X11175 Pin #13 KOMBI -> X6011 #3 (BR/GN)" and "X6011 #3 -> X6231 Oil Pressure switch".
- **NikolaiD's 2002 M3 convertible list (2011)** [read] ([ncs-expert.com FSW_PSW list](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf)):
  - His "AKMB – Instrument Cluster" section has none of the three switches.
  - They appear only under "Miscellanious options – not yet processed or from other cars": `CAN_OELDRUCKSCHALTER nicht_aktiv`, `GENERATOR_UEBER_CAN nicht_aktiv`, `TOG_UEBER_CAN aktiv`.
  - *(US M3, MY2002; his cluster index isn't stated.)*
- **kd7iwp's non-M trace** [read] ([GitHub kd7iwp/BMW-Coding, E46](https://github.com/kd7iwp/BMW-Coding/tree/master/E46)): the original `KMB_E46.C04` trace (126 functions) has no lamp-switch function. *(Canadian-coded, pre-2003 layout.)*

**Fuel gauge: curve and capacity with two senders**

- **The raw C04 trace** [read] (same repo) lists one function with three keywords:
  ```
  TANK_KENNLINIE
  	60_l_literskala
  	dad_tank_diesel
  	metalltank
  ```
  `LITER_SERVICE_INTERVALL` and `SIA_LITER_GRENZE` list seven engine/body keywords in the same way.
- **Revtor** [read]: "If NCS Dummy displays multiple checked parameters for a function they all have the same data value."
- **NikolaiD's M3 list** [read] gives the same three keywords for `TANK_KENNLINIE` in the M3 AKMB.
- **Tank thresholds** [read]. The M3 list and the non-M trace have identical values:

  | Parameter | Value |
  |---|---|
  | `TANK_SCHWELLE_RESERVE` | `8_l` |
  | `TANK_SCHWELLE_AUF/AB` | `6_l` |
  | `TANK_SICHERHEITSFAKTOR` | `1.3` |
  | `TANK_BERUHIGUNGSZEIT` | `10_sec` |
  | `TANK_MITTLUNGSZEIT` | `5_sec` |
  | `TANK_FILTER_FALLEND` | `1.9_l/min` |

- **BMW ST052, test 06** [read]: "6.0 Fuel level averaged - LH sensor input … RH sensor"; "6.1 Total tank level averaged"; "6.2 … tank phase 1 = both sensors OK, 2 = one sensor fault, 3 = implausible input".
- **Tool32** [read] ([KOMBI46R](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46R.md), [KOMBI46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46.md)):
  - On KOMBI46R the job is `STATUS_AIF_TANKDATEN_LESEN`. It returns `STAT_TANKINHALT_HEBEL1_WERT` and `…HEBEL2_WERT` (litres for each sender), `STAT_TANKINHALT_UNGEF_WERT` and `…GEF_WERT` (total, unfiltered and filtered) and `STAT_RESERVE`.
  - `STATUS_TANKINHALT_LESEN` exists only in KOMBI46 ("KOMBI E46", rev 2.41).
  - KOMBI46R `STATUS_ANALOG_LESEN` gives each sender's raw input as an ADC value (`STAT_HEBELGEBER1_WERT`, `STAT_HEBELGEBER2_WERT`).

**Doors, tailgate, rear window and check-control**

- **BMW ST052** [read]:
  - "The Cluster receives signals for the Check Control Pictogram over the K-Bus."
  - "The indicators for the directionals, fog lights, high beams and the LED's in the pictogram are also triggered based on K-Bus telegrams from the LSZ."
- **The C04 trace** [read]: `CC_LAMPEN aktiv`, `CC_TUEREN aktiv`.
- **GM5** [read]:
  - A US sedan's `GM5.C02` trace has `FUNKTIONEN_TOURING nicht_aktiv`, `HECKKLAPPEN_LOGIK geschlossen`, `HECKSCHEIBE_ENTR_SENDER_1…4 nicht_aktiv` and `HECKSCHEIBE_ENTRI_INNEN nicht_aktiv` ([kd7iwp](https://github.com/kd7iwp/BMW-Coding/tree/master/E46)).
  - A community patch for Touring GM5s sets `FUNKTIONEN_TOURING aktiv` and `HECKSCHEIBE_ENTR_SENDER_1…4 aktiv` ([ncsx community patches: unlock Touring tailgate](https://github.com/emdzej/ncsx-community-patches/tree/main/patches/E46)).
- **Rear-door lights** [read] ([Huggins: M3 cluster mod for non-M](https://racehuggins.com/product/e46-m3-cluster-mod-for-non-m/)): "Have a 4-door and need the LED's added to indicate open doors?" ($100). The same mod adjusts the redline LEDs and the speedometer ("The M3 is configured to be 9% fast versus the non-M at 6% fast").
- **Solder pads and resistor** [snippet]: the pads are on M3 clusters; use red LEDs with a 196 Ω resistor.

**Oil temperature, warm-up and shift lights, rev scale**

- **NikolaiD's M3 AKMB** [read]: `DREHZAHL_KENNLINIE kennlinie_03`.
- **ECUWorx MSS5x tool** [read] ([ECUWorx features](https://www.ecuworx.co.uk/how-to/a-run-down-of-features-of-the-mss5x-binary-modification-tool-and-what-they-do/)): "6MT Shift Lights Settings … allows SMG style shift lights to operate on manual E46 M3s", with Disabled / "Enabled (Always active)" / "Enabled with Sport Mode", and "Warm Up Light Recalibration". These are DME software options, not cluster coding.

**Service interval (SIA)**

- **BMW ST052** [read]:
  - "the SIA IV system calculates service intervals based on fuel used."
  - "The 'Coded Inspection Limit' value for each vehicle can be found in a Group62 Service [Information bulletin]".
  - SIA reset by the cluster's reset mode, "from 9/99".
- **The M3 list** [read]: `SIA_LITER_GRENZE` offers `s54b32`, `s54b32_aut`, `s54b32_aut_sa8st`, `s54b32_aut_sa988`, `s54b32_sa8st` and `s54b32_sa988`. `SIA_ANZEIGEPARAMETER` offers `ohne_zeitinspektion` / `mit_zeitinspektion` / `mit_zeitinspektion_japan`.
- **The non-M trace** [read] uses M52/M54 keywords.
- **KOMBI46R** [read] has `SIA_RESET` and `STATUS_AIF_SIA_DATEN_LESEN`.

**Units, country and gearbox**

- **The US M3 list** [read]:

  | Parameter | US value | Other options |
  |---|---|---|
  | `SPRACHE` | `us` | — |
  | `TEMPERATUR_EINHEIT` | `grad_f` | — |
  | `VERBRAUCH_D1` | `mpg_us` | `mpg_uk`, `km/l`, `l/100km` |
  | `WEG_DURCHSCHNITT` | `mph` | `km/h` |
  | `WEG_EINHEIT` | `mls` | `km` |
  | `WARNUNG_GESCHW_LIMIT` | — | "Speed limit warning at 75mph" |

- **The C04 trace** [read] has `SPRACHE kanada`, `WEG_EINHEIT km`, `ZEIT_EINHEIT 12_stunden`, `TEMPERATUR_EINHEIT grad_c` and `VERBRAUCH_D1 l/100km`.
- **The community "UK to EU" patch** [read] edits `LL/RL`, `WEG_EINHEIT`, `ZEIT_EINHEIT`, `WEG_DURCHSCHNITT`, `VERBRAUCH_D1`, `WEG_REICHWEITE` and `WEG_LIMIT`.
- **The "automatic to manual" patch** [read] sets `GETRIEBEART handschaltung`.
- **BMW ST052, test 10** [read]: "Country Coding … 02 … US".

### Inferences

1. **The donor FA is in AKMB.** After a DIY chip route, or a service that doesn't rewrite the FA, AKMB holds the donor M3's FA. This follows from where the cluster stores its FA (KOMBI46R) and from nextelbuddy's statement.
   - The danger: a Session 8 Code Car or a "blank MAN" coding run with that FA would code the GM5, light module, climate control, MK60 and airbag module as an M3 coupe.
   - So restore your FA into AKMB from ALSZ, or keep ALSZ as the only FA source.
2. **NCS may refuse the M3 cluster with a 325iT FA. Untested.**
   - The non-M retrofit guide changes index 24 to 08 because that "will give you access to coding data" [earlier round].
   - The owners who coded an M3 cluster in a non-M car after a chip job (Bryson's wagon, the 2004-cluster 330Ci) most likely had the donor's FA still in AKMB during that session.
   - So code the M3 cluster while a donor (M3) FA is in the session. Then write your FA to AKMB if NCS lets you (G4 gives the order).
3. **Don't default-code the M3 cluster.** With a 325iT FA, NCS would apply `KMBE46M3` rules to non-M options (M54 service limits, possibly the K-numbers and gauge curves), or refuse.
   - The one documented default-coding of an altered cluster froze the tachometer at 9,000 rpm [earlier round].
   - ECUswap's "coding from the factory vehicle order" is exactly what to stop a service from doing on this car. Ask them to keep the M3 coding and write your FA.
4. **Lamp switches.** They exist on redesign clusters (24 confirmed; 23 almost certainly; 07/08 likely, given the extra oil-level functions there). They're absent on 20–22 and 02–06. Your cluster's own trace settles it.
5. **`TANK_KENNLINIE`.** At least in `KMB_E46.C04`, and in the M3 list, it's one stored value with three names, so there's nothing to choose. Whether the M3 index-24 curve matches the Touring's senders is an open question for the fill test.
6. **Doors and tailgate.** The cluster shows open doors and the tailgate from GM5 telegrams on the K-bus. The rear-door LEDs, once fitted, should work like a four-door cluster's. Huggins and Kassel sell the mod, so presumably they do.
7. **Service interval.**
   - Keep the M3 cluster's `SIA_LITER_GRENZE` (s54b32): the engine is an S54.
   - The counters themselves come from your light module.
   - Reset the interval once at the first oil service with the S54, using the cluster's reset mode or KOMBI46R `SIA_RESET`.
8. **Units.** A US donor cluster is already in US units, so only check them. Change the unit parameters only if the cluster came from a km/h car.
9. **K-numbers.** Keep the M3 cluster's `K_ZAHL_TACHO` and `K_ZAHL_WEG` (and their `_KOMPL` twins). They convert wheel pulses to road speed for the M3's wheels and tyres, which this car now runs.

### Gaps

- Factory values of the three lamp switches on US M3 index 23 versus 24, by build date and MSS54 versus MSS54HP.
- Whether NCS Expert accepts `KMBE46M3.C24` (for coding, and for `FA_WRITE`) with a 325iT FA in the session.
- Whether `TANK_KENNLINIE` has more than one real value on index 07/08/23/24.
- Whether the M3 cluster's check-control shows the Touring's tailgate and rear glass open.
- I found no source on what an M3 cluster shows for the Touring's rear-window switch, nor whether any cluster parameter covers it.

---

## 3. The light module (LSZ/LCM/ALSZ) with the M3 front end

### Cited findings

**Generations by build date**

- **The older LSZ** [read]: SGBD "Lichtschaltzentrum E46", rev 1.25 ([SGBD: LSZ](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ.md)).
- **LSZ_2** [read]: "LSZ fuer E46 PU 09 / 2001", coded as ALSZ in NCS (`LSZ C31 A_ALSZ C_LSZA ALSZ`).
- **Coding indexes** in the US traces read this round [read] ([kd7iwp](https://github.com/kd7iwp/BMW-Coding/tree/master/E46)):

  | Trace | Build | Functions |
  |---|---|---|
  | `LSZ.C29` | Pre-09/2001 | 142 |
  | `LSZ.C35` | — | 311 |
  | `LSZ.C36` | — | 324 |

  The extra functions in C36 include `CYCL_TI_BLK` (triple blink), `DAUERFAHRLICHT_US`, `LAENGE_LWR_REF` and `LWR_DIAG_PARAM`.
- **Index and software versions** [snippet]: index 34 = software 3.56, 35 = 3.6, 36 = 4.0, 37 = 4.5.
- **Huggins** [read] ([LCM firmware 4.5](https://racehuggins.com/product/e46-light-control-module-lcm-firmware-update-to-4-5/)): "Requires a core LCM of version 3.6 or greater (found in 2003+ cars)."
- **BMW ST052** [read]: "From 2002, there some changes to the LSZ module. These include a modified PWM signal for lighting control (freq 80hz), there a additional outputs circuits added for rear brake lights and bi-xenon systems and a new headlight switch to accommodate RLS."
- **Body variant** [read] ([SGBD: LSZ_2](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ_2.md)). The "VARIANTEFZG" table is read "aus Codierblock 0, Byte 30" (from coding block 0, byte 30):

  | Value | Body |
  |---|---|
  | 0x01 | "E46/4 > PU 09.01" (sedan from 09/2001) |
  | 0x02 | "E46/2,3,C + (E46/4 + !PU 09.01)" (coupe, Touring, convertible, and the pre-09/2001 sedan) |
  | 0x03, 0x04 | E46/5 (Compact) |

  The country table: 0x00 ECE, 0x01 US.

**Variants: fog, xenon, AHL (ETK, US)** [read] ([ETK: 325iT light switch unit](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_electrical_system/switch_unit_light/), [ETK: M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/switch_unit_light/))

| Part | ETK name | Rain sensor S521A | Xenon S522A | AHL S524A |
|---|---|---|---|---|
| 61319133022 | "Switch unit, light" | No | No | — |
| 61319133023 | "Switch unit, light" (from 09/2001) | Yes | No | — |
| 61319133024 | "Switch unit, light / foglamps" | No | No | No |
| 61319133025 | "Switch unit, light / foglamps" | Yes | No | No |
| 61319133026 | "Switch unit, light / foglamps" | No | Yes | No |
| 61319133027 | "Switch unit, light / foglamps" | Yes | Yes | No |
| 61319133029 | "… light / ALC" (from 09/2001) | Yes | Yes | Yes |
| 61318378577 / 61316911647 | "Control, switch unit for lights" (the switch panel) | No / Yes | — | — |
| 61318378576 / 61316911648 | "Contr.pan.sw.unit light/front fog lamp" (switch panel with fog button) | No / Yes | — | — |

The fog condition's Yes/No didn't render. Reading "with" or "without" fog lights from the item names is an inference.

**What the light module does (BMW ST052, Lighting)** [read] ([ST052 Lighting](https://ia800902.us.archive.org/26/items/BMWTechnicalTrainingDocuments/ST052%20Body%20Electronics%20II/03c_E46%20Lighting%20Systems.pdf))

- **Fog relay:** "The fog light relay (if equipped) is located behind the glove box. It is controlled as a direct output of the LSZ."
- **Fog interlock:** "the fog lights can only be switched on when the parking or headlights are on."
- **Lamp monitoring:** "Due to the Hot and Cold monitoring capabilities, it is very important to use the specified lamps with the correct wattage rating."
- **Xenon monitoring:** "Xenon bulb function is monitored by the LSZ. The bulbs are only 'hot' monitored … cold monitoring for low beam headlights is encoded off in the lighting control module for Xenon headlight equipped vehicle."
- **AHL:** "available on the E46 from 2003. This system is only available with the optional Bi-Xenon headlights", with its own control unit behind the glovebox.
- **Rain/light sensor:** "Beginning in 2002, the Rain Sensor was replaced by the new Rain and Light Sensor (RLS). The RLS is connected to the K-Bus".

**BMW's xenon retrofit** [read] ([BMW EBA 01 29 9 416 445, "Xenon Light with Automatic Headlight Adjustment Control", 1.2002](https://bmw.etk.club/eba_docs/596en.pdf)). *(E46, all bodies; a dealer instruction.)*

- **Scope:** "The installation time is approx. 5 hours". Kit 63 12 9 416 523, among others.
- **ECE condition:** "This retrofit system may only be operated in ECE countries in conjunction with a headlight cleaning system". BMW installs the SRA together with it where required.
- **Sensors:** "Level sensor front right" and "Level sensor rear right" (B42, B64). The front holder is secured to the arm, "check the coding on the level sensor".
- **Wiring:** see the table below.
- **Low-beam plugs:** "The pins on the 2-pin grey connection plugs X130 and X135 must have the following assignments: Pin 1 (1): Earth (BR cable). Pin 2 (2): Power supply (GE/GN cable (left) or GE/BL cable (right))."
- **Bi-xenon from 09/2001:** "adapter cables … between the plugs X134 (full beam headlight, right) and X131 (full beam headlight left) … The free plugs X10106 and X10107 on the adapter cables are to be connected to the corresponding connections … on the bi-xenon headlights."
- **The light module is replaced:** "7. To install the xenon wiring harness and replace the light module … The light module is no longer required."
- **Coding:** "This retrofit system requires coding … In addition the retrofit system is stored in the central coding key of the IKE/instrument cluster. The coding process is completed using the DIS/MoDiC … in the 'Retrofit' path."
- **Function test:** "When the dipped headlight switch is activated the headlights must adjust automatically. Test the function … by loading the front and then the rear of the car (delay approx. 15 seconds)."

The diagram labels the pins HSSV/HSGV/HSPV (front) and HSSH/HSGH/HSPH (rear). Reading S/G/P as signal, ground and supply is an inference from the abbreviations.

| Light module X12 pin | Wire | Level-sensor pin | Diagram label |
|---|---|---|---|
| 22 | GR/GN | X1451/4 (front right) | HSSV |
| 19 | GR/WS | X1451/1 | HSGV |
| 23 | GR/BR | X1451/5 | HSPV |
| 14 | SW/GN | X13251/4 (rear right) | HSSH |
| 46 | SW/WS | X13251/1 | HSGH |
| 26 | SW/GR | X13251/5 | HSPH |

**Real US light-module codings** [read] ([kd7iwp](https://github.com/kd7iwp/BMW-Coding/tree/master/E46); the owner's cars aren't identified)

The original `LSZ.C35` is a US bi-xenon car with sedan variant 1. It codes:

| Parameter | Value |
|---|---|
| `VARIANTE_LSZ` | `wert_01` |
| `LAENDERVARIANTE_LSZ` | `wert_02` |
| `SIDEMARKER_US` | `aktiv` |
| `AH_US_OPTION` | `aktiv` |
| `TAGFAHRLICHT_ECE` | `nicht_aktiv` |
| `GED_FL_ALS_DRL` | `aktiv` |
| `BI_XENON` | `aktiv` |
| `XENON_TEST` | `aktiv` |
| `KALTUEBERWACHUNG_AL` | `nicht_aktiv` |
| `PWM_ANSTEUERUNG_AL` | `wert_02` |
| `PWM_WERT2_FL_BIXENON` | `wert_02` |
| `LEUCHTWEITENREGELUNG` | `aktiv` |
| `LEUCHTWEITENREG_AUTOM` | `aktiv` |
| `LEUCHTWEITENREG_DYNAM` | `aktiv` |
| `KENNLINIE_LWR_SENSOR_VO` | `wert_01` |
| `KENNLINIE_LWR_SENSOR_HI` | `wert_01` |
| `FL_UND_NSW_NICHT_GLEICHZ` | `aktiv` |

- **Body variant drives the rear-lamp coding.** The owner's modified copy changes `VARIANTE_LSZ` to `wert_02` together with about 25 rear-lamp and brake-force-display settings, and turns `BI_XENON` off. Examples: `BREMSLICHT_ALS_STANDLICHT`, `PIN_20_ALS_NSL`, `KALTUEBERWACHUNG_RL_3_*`, `BFD_*`.
- **The C29 trace (pre-09/2001, US)** also has `LEUCHTWEITENREGELUNG`, `_AUTOM` and `_DYNAM` set to `aktiv`, and `KALTUEBERWACHUNG_AL` set to `nicht_aktiv`. That suggests a xenon car too. I found **no US halogen trace**, so your Session 1 trace is your halogen reference.
- **terra's ALSZ list** [read] ([NAM3 1281](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert)): `PWM_WERT2_FL_BIXENON` ("Halogen High Beams"), `FL_UND_NSW_NICHT_GLEICHZ` ("Allows fogs with highbeams"), `GED_FL_ALS_DRL` ("Disable DRL"), `SIDEMARKER_US` ("disables US-style parking lights"), `CYCL_TI_BLK dreimal`.
- **`AUTO_LWR_ENABLE`** appears only in NikolaiD's "Miscellanious options – not yet processed or from other cars" [read].

**Status, fault and test jobs** [read] ([LSZ_2](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/LSZ_2.md))

- **Presence checks:** `XENON_VORHANDEN` ("Xenonlicht") and `LWR_VORHANDEN` ("Leuchtweitenregulierung").
- **`STATUS_LESEN`** returns:
  - `STAT_SPANNUNG_BELADUNGSSENSOR_VORN_WERT` ("0.0 bis 5.0 Volt", front sensor);
  - `STAT_SPANNUNG_BELADUNGSSENSOR_HINTEN_WERT` (rear sensor);
  - `STAT_TASTER_NSW_EIN` (fog button);
  - `STAT_LICHTSCHALTER_POS_NR` ("0=aus, 1=SL, 2=FLC, 3=AL", i.e. off, side lights, automatic, low beam).
- **Fault codes:**
  - 0x21 "LWR, vorderer Beladungssensor Unterbrechung" (front sensor open circuit);
  - 0x22 front sensor short to ground;
  - 0x23 and 0x24, the same for the rear sensor;
  - 0x1F "Spulen Schrittmotoren defekt" (stepper-motor coils faulty).
- **Production job:** `STEUERN_DYN_LWR`, "Fertigungsmodus schnelle Scheinwerfernachregelung" (a factory mode for fast headlight adjustment).

**Fog lights and side markers (ETK, US)** [read]

- **Bulbs:**
  - M3 / M-Technik fog lamp: "HB4 12V 51W", later "HB4 12V 55W".
  - Facelift Touring fog lamp (63176911007): "H11 55W".
- **Relay K47:** the same on both cars (61368373700 white-green).
  - Sources: [ETK M3 fog](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/lighting/fog_lamp_m_technik/), [ETK 325iT fog](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/lighting/fog_lights/), [ETK K47](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_electrical_system/relay_front_fog_lamp_k47/).
- **US M3 headlights** [read] ([ETK: M3 headlight](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/lighting/headlight/)): halogen 63127165903/904 and bi-xenon 63127165823/824, both "from Sep '01".

**Services and used modules** [read]

- **RPM Motorsport** ([RPM: used LCM programming](https://www.rpmmotorsport.net/products/bmw-e46-e38-e39-z4-x5-x3-lcm-vin-number-mileage-programming)), $300: used LCMs "are meant to only be programmed once". After their programming, the LCM "will take whatever mileage that is stored in the Instrument Cluster".
- **Huggins** ([LCM coding](https://racehuggins.com/product/e46-light-control-module-lcm-coding/)), $50: "VIN/Mileage coding only".
- **What not to do** [read]: two owners matched a light module to the *cluster* with PA-Soft ([E46Zone 36161](https://www.e46zone.com/forum/topic/36161-coding-lcm/), [bmw-syndikat 385798](https://www.bmw-syndikat.de/bmwsyndikatforum/topic385798_E46_Kombiiinstrument_codierung_3er_BMW_-_E46.html)): "just put in the mileage from the cluster and change the vin" and "Einfach die VIN vom Kombi ins LSZ schreiben" (just write the cluster's VIN into the LSZ). With a donor cluster, that's exactly the error the guide warns about.

### Inferences

- **Keep the Touring's light module and its coding with halogen M3 headlights.** Both cars' light modules use the same body variant (0x02 covers coupe and Touring). Even so, the rear-lamp pin functions follow the body, so don't import the donor's ALSZ trace.
  - For hot and cold monitoring, the M3 lamps must use the same bulb types and wattages as the Touring's: low and high beam, indicator and side light. I didn't verify the bulb lists this round, so check both cars' ETK bulb lists.
- **Front fogs:**
  - If your Touring has factory fogs (a "light / foglamps" module, …024/…025), the M3 fogs need only wiring. Their connector may differ (HB4 versus H11), and the relay is the same.
  - If it doesn't, ETK suggests the light module itself differs, so fitting fogs may mean a fog-variant module (the mileage-safe sequence in G6), the switch panel with the fog button, and K47 with its wiring.
  - Whether a no-fog module can drive the relay after a coding change is unknown.
- **Xenon done BMW's way** (G6):
  - Replace the light module with the xenon variant (…026 without rain/light sensor, …027 with), matching your rain/light-sensor equipment.
  - Fit both level sensors: the front one on the M3 arm with the M3 angle joint, the rear one on the Touring axle.
  - Add `$522` to the FA and code the new module from the FA. A new module in a Touring with a Touring FA is the right case for default coding.
  - Then check the module's xenon and levelling values against the C35 list.
- **Mileage safety.** The replacement light module must start at zero mileage: new, or virginized by a service. ST052 says the light module's mileage can only go up. A used module with a higher reading would carry a false record into your car.
- **Level-sensor curves.** `KENNLINIE_LWR_SENSOR_VO` and `_HI` are `wert_01` in every trace seen. With the M3 front link (different angle joint) on a Touring body, keep the default and judge it by the BMW load test and aiming. If the beam rides high or low under load, the curve or link geometry is the suspect.

### Gaps

- I have no US halogen ALSZ trace.
- The meaning of each `KENNLINIE_LWR_SENSOR_*` value.
- Whether a US halogen light module (…022/…024) can run levelling after coding alone. BMW's retrofit replaces the module, which suggests it can't.
- Whether front fogs need `$520` in the FA, or only the fog-variant module.
- The pin layout of the M3 (coupe) headlamp plugs against the Touring's sedan-type lamps.
- Whether the US M3 has headlight washers (SRA) as standard, and the SRA option code. `S502A` is unverified.

---

## 4. The switch centre (SZM), the console switches, and `$7MA`

### Cited findings

- **SZM46** [read] ([SGBD: SZM46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/SZM46.md)): "Schaltzentrum Mittelkonsole E46", rev 1.06. It has only `IDENT`, `FS_LESEN`, `IS_LESEN` and `CODIERUNG_LESEN`, the last described as "Auslesen der Codierdaten" (read the coding data).
- **No SZM in the NCS samples** [read]: none of the E46 SGFAM/SGET rows I saw has an SZM entry ([ncsx docs](https://github.com/emdzej/ncsx/blob/main/docs/ecu-selection.md)). The E46Zone and NikolaiD module lists have none either ([E46Zone 36596](https://www.e46zone.com/forum/topic/36596-guide-to-coding-with-ncs-expert/), [NikolaiD](https://ncs-expert.com/wp-content/uploads/2013/06/FSW_PSW.pdf)).
- **ETK part numbers** [read]:
  - US M3: "Switch unit, center console" 61316925520 ([ETK](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/vehicle_electrical_system/switch_unit_center_console/)).
  - The 325iT page I fetched is filtered to "Dynamic stability control S210A No" and shows 61316925498 only ([ETK](https://bmwfans.info/parts-catalog/E46-Touring/USA/325i-M54/L-N/browse/vehicle_electrical_system/switch_unit_center_console/)).
- **Sport and DSC buttons** [earlier round; already in the guide]: the Sport button is hard-wired from SZM plug X1869 pins 17/18 to DME X60004 pins 15/16.
- **`$7MA`** (the guide already cites ETK S7MAA, the Competition package, from 12/2004):
  - ECUWorx adds `$7MA` in Enter FA to enable M Track [read].
  - liam821's E46.MK60.C12 rules key on `M_TRACK_MODE`. In the cluster, `ANZEIGE_HOCHLADEN` is "M track mode light": `nicht_aktiv` on ZHP and standard M3, `aktiv` on ZCP [read] ([liam821](https://liam821.com/MK60-Comparison.pdf)).
  - NikolaiD's 2002 M3C AKMB lists "ANZEGIE_HOCHLADEN M-Track mode symbol" (sic) [read].
- **Grosvenor BMW (UK)** [read] ([Grosvenor: E46 option coding](https://bmwspecialistreading.co.uk/bmw-e46-option-coding/)): "M-Track Mode … can only be retrofitted to an E46 M3 … Only some vehicles have the required M-Track Mode LED on the dashboard."

### Inferences

- **The switch centre needs no coding.** It has coding bytes, but nothing in NCS addresses them, and its buttons are hard-wired or K-bus. Whether the M3 switch unit fits the Touring's console is a fit question, not a coding one.
- **M Track in this car** needs three things:
  - the M3 MK60 coded with M Track values (the DSC research covers that);
  - AKMB `ANZEIGE_HOCHLADEN` = `aktiv`, written through a MAN while NCS accepts the cluster (G4);
  - an M Track LED in the cluster.
- **Leave `$7MA` out of the stored FA** unless you also accept the M3 MK60 being default-coded from it. In this car, set the MK60 and cluster values directly through MANs, and keep the FA as the Touring's.

### Gaps

- No ETK entry for the US DSC-equipped 325iT's switch unit was captured.
- I found no first-hand fit report of the M3 switch unit in a Touring console.

---

## 5. Other body modules

### Cited findings

- **Climate control (IHKA/IHKR)** [read]:
  - Traces (US 6-cylinder petrol sedan, IHK_E46.C14/C17): `ZYLINDER_ZAHL 6_zylinder`, `MOTOR_ART benziner`, `GEREGELTER_KOMPRESSOR gross`, `ZUSATZWASSERPUMPE nicht_aktiv`, `TEMPERATUR_EINHEIT grad_c` ([kd7iwp](https://github.com/kd7iwp/BMW-Coding/tree/master/E46)).
  - SGBDs IHKA46 and IHKR46 have `STEUERN_ZUSATZWASSERPUMPE` and `KOMPRESSOR_SPERRE`, "Codieren der Kompressortransportsperre" (coding of the compressor's transport lock) ([IHKR46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKR46.md), [IHKA46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/IHKA46.md)).
  - ETK compressors: 325iT and M3 share 64526910458 to 09/2002; the M3 lists 64526936883 and 64526916232 from 09/2002 ([ETK M3](https://bmwfans.info/parts-catalog/E46-Coupe/USA/M3-S54/L-N/browse/heater_and_air_conditioning/air_conditioner_compressor_2/)).
- **PDC** [read]:
  - BMW ST052: "The PDC control module activates the ultrasonic sensors mounted in the rear bumper" (US: rear only).
  - NikolaiD's "other cars" list shows PDC echo thresholds tied to bumper shape: `ECHOSCHWELLWERTE_ECKE_HI e46_m3_3/01`, `ECHOSCHWELLWERTE_MITTE_HI e46_m3_3/01`, `…_VO e46_m3`.
- **Airbag (MRS)** [read]:
  - NikolaiD's ABG list includes `ERKENNUNG_SITZBELEGUNG_1/2`, `GURTSCHLOSS_*`, `GURTSTRAFFER_*`, `VERRIEGELN_SITZLEHNE_FA/BF_*` (seat-back lock) and `AUSLOESEKRITERIUM us/ece`.
  - NAM3 161484: coding out the passenger occupancy sensor means "the passenger airbag will go off in a crash even if you don't have a passenger seated" ([NAM3 161484](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/161484-after-market-seats-coding-for-air-bag-light)).
  - NAM3 168158: after seat electronics were removed, INPA showed "OC3" ([NAM3 168158](https://nam3forum.com/forums/forum/special-interests/coding-tuning/168158-seat-electronics-needed-to-code-out-the-driver-s-seat-occupancy-sensor-airbag-light)).
- **MFL (multifunction steering wheel) and cruise** [read] ([BMW EBA 01 29 0 023 076 / kit 65 71 0 016 106 and 108](https://etk.club/eba_docs/284en.pdf)):
  - Scope: "only valid for vehicles with SMART airbag sports steering wheel. These are E46 coupé, touring, saloon as from 06/99 and convertible from start of series"; "Installation time is approx. 1 hour."
  - Wiring: see the table below.
  - Finishing: "3. Coding of the vehicle must not be carried out."
  - The MFL serial line reaches X60004 pin 27 on the MSS54 as well ([earlier notes: harness_body_functions.md](../E46%20M3%20Touring%20open%20questions/harness_body_functions.md)) [earlier round].

  | MFL wire | Wire | Goes to | Signal |
  |---|---|---|---|
  | X10170 (10-pin green, at the switch fixture) pin 8 | BL/SW | DME X60004 pin 27 | MFL serial line to the DME |
  | pin 9 | WS/RT/GE | LSZ X12 pin 21 | K-bus |
  | pin 10 | VI/GE | LSZ X12 pin 27 | Terminal R (KL R) |

  BMW says to cut the two X12 leads about 40 mm behind the plug and splice them.
- **Headlight washers (SRA)** [read] ([BMW EBA "Headlight Cleaning System (SRA)", kit 82 19 9 416 441](https://bmw.etk.club/eba_docs/594en.pdf)): "This retrofit system requires coding … stored in the central coding key of the IKE/instrument cluster". The US sedan's GM5 trace has `SCHEINWERFERREINIGUNG aktiv` ([kd7iwp](https://github.com/kd7iwp/BMW-Coding/tree/master/E46)).
- **Rain/light sensor** [read]: BMW ST052 says it is on the K-bus and the light module uses it, with no front-end dependence.
- **GM5** [read]: the Touring functions are listed under §2 above. A used GM5 is coded with a blank MAN, and its VIN "doesn't actually impact anything" ([NAM3 21981](https://nam3forum.com/forums/forum/special-interests/coding-tuning/21981-ncs-error-while-trying-to-recode-used-gm5-module)).
- **Steering-angle sensor (LWS)** [read]: E46Zone's and NikolaiD's lists call LWS "Light Switch" or "Light module". The parameters (`LWS5_KENNFELD_*`) show it is the steering-angle sensor.

### Inferences

- **Climate control.** Both cars are six-cylinder petrol, and ETK lists the same climate-control units, so the Touring's IHK coding should stand.
  - Re-code it from the FA only if you change the FA. Compare with the donor's IHK trace first.
  - `GEREGELTER_KOMPRESSOR` describes the compressor's control type; check it against the compressor actually fitted (the cooling and A/C research covers which one).
- **PDC.** On a US car the swap changes nothing while the Touring's rear bumper stays. If an M3 rear bumper with its PDC sensors goes on, copy the M3 echo-threshold values (`…_HI e46_m3_3/01`) into the PDC module through a MAN.
- **Airbag.** Only if seats change. Keep the occupancy mat and its electronics, and never code them out. With M3 coupe seats, their seat-back lock switches (`VERRIEGELN_SITZLEHNE_*`, a two-door feature) go unmonitored in a Touring. Nobody documents this.
- **MFL.** Wiring only. Afterwards clear DME adaptations so it learns the buttons (`STAT_FGR_MFL_VERBAUT_WERT`).

### Gaps

- The year split between the US OC3 and SBE passenger-occupancy systems, and whether an OC3 seat works with an earlier airbag module.
- Whether a US 325iT is coded with the same `GEREGELTER_KOMPRESSOR` value as an M3 from 09/2002.
- The SRA option code and whether US M3s have headlight washers.

---

## 6. The vehicle order (FA)

### Cited findings

- **The FA alone changes nothing** [read]. terra: "changing the VO/ZCS without also coding modules will not actually change how your car functions", and "NCS Expert will be basing its coding decisions based on the VO you entered" ([NAM3 1281](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert)).
- **The type key drives the coding rules** [read].
  - In liam821's MK60 rules, the keys include `S54B32`, `TOUR`, `LIM`, `COUP`, `CABR`, `M54B25`, `M_TRACK_MODE` and `CSL` ([liam821](https://liam821.com/MK60-Comparison.pdf)).
  - [earlier round] An `E46ZST.000` type line maps a type key to body, engine, drive side and market.
- **What the type key is.** The FA's `*` slot is the type key ([ncsx: fa-format](https://github.com/emdzej/ncsx/blob/main/docs/fa-format.md)) [read].
  - The US 325iT's key is probably the VIN's characters 4–7 (WBA**EN33**…). This is an inference; Hagerty VIN snippets show WBAEN33 for 325iT [snippet].
- **Production dates** [earlier round, already in the guide]: the date gates which module versions NCS accepts. Session-only FA changes without `FA_WRITE` are the documented fix for MK60s.
- **A wrong FA on the light module** [snippet]: an FA written to the wrong module mis-coded one light module so its rear lights misbehaved ([bmwfaq](https://bmwfaq.org/threads/perdida-fa-vo-e46.1068598/)).
- **How the body variant moves the rear lamps** [read]: see §3, where kd7iwp's change from `VARIANTE_LSZ` `wert_01` to `wert_02` moved about 25 rear-lamp settings.
- **No documented S54 swap changed a stored type key.** Owners changed options (`$7MA`) and dates (`#0902`, `#0304`), always for the M3's own car or for one session ([earlier round](../E46%20M3%20Touring%20open%20questions/coding_body_chassis.md)).

### Inferences (decision for this build)

- **Type key and production date:** keep the Touring's. Never write an M3 type key into AKMB or ALSZ.
  - The chip route can do this silently (§2), so verify after Session 4.
- **Options:** add or remove codes only for hardware actually fitted.

  | Option | When to add it |
  |---|---|
  | `$522` | Xenon, with the full BMW system |
  | `$520` | Fogs, if the car lacks them (unverified whether it's needed) |
  | SRA | Headlight washers, if added |

  Leave `$7MA` out (§4). Don't remove the Touring's own codes.
- **After any FA change:** `FA_WRITE` to ALSZ (and to AKMB if NCS accepts it), re-read both, then code only the modules the change touches (the table in G5).
- **What the FA doesn't change:** the DME (MSS54) isn't coded from the FA. Clearing DME adaptations isn't needed for body-only FA changes. Clearing DME faults or adaptations resets the OBD readiness monitors, which is standard OBD-II behaviour, so plan drive cycles before an inspection.

### Gaps

- The US type keys for the 325iT (EN33?) and the US M3 coupe.
- The `E46ZST` rule lines for `TOUR` versus `COUP` in GM5 and the light module. I couldn't read the E46 DATEN directly.
- No source confirms how NCS treats `AKMB` with an M3 index-24 cluster and a non-M FA.

---

## Guide-ready material

### G1. Software and data check (at the desk, about 10 minutes)

1. **Profiles.** Copy `NCSDUMMY4.PFL` (Revtor, for NCS Expert 4.x) or terra's "Expert Mode w/ Manipulation" into `C:\NCSEXPER\PFL\`.
   - **Expect:** File → Load Profile lists it.
   - **If not:** you have NCS Expert 3.x. Use `NCSDUMMY3.PFL`, but only on 32-bit Windows.
2. **The MAN file.** Windows Explorer → View → tick "File name extensions". In `C:\NCSEXPER\WORK\`, create an empty `FSW_PSW.MAN`.
   - **Expect:** the name shows exactly `FSW_PSW.MAN`, not `FSW_PSW.MAN.txt`.
3. **Data files.** In `C:\NCSEXPER\DATEN\E46\`, look for:
   - `KMBE46M3.C23` and `KMBE46M3.C24` (M3 redesign clusters);
   - `KMB_E46.C07` and `KMB_E46.C08`;
   - `LSZ.C35`, `LSZ.C36`, `LSZ.C37`;
   - the MK60 file for your unit's index.

   **If any is missing:** update the SP-Daten. ECUWorx: cars from 2005 need newer files. The latest is V75 (2025/12).
4. **Data age.** Open `E46AT.000` in Notepad, read-only, and note the `DATUM` line (a sample set reads `DATUM 22.01.2007`). Record it with your backups.
5. **SGBDs.** Check that `C:\EDIABAS\ECU\` has `KOMBI46R.PRG`, `KOMBI46.PRG` and `LSZ_2.PRG`.
   - **If not:** Tool32 reports SYS-0002 or SYS-0005.
6. **Before any session:** close INPA, put the charger on, and switch the ignition to position 2.

### G2. NCS Expert screen map (4.0.1, English labels from owner guides)

| You are at | Press | You get |
|---|---|---|
| Empty main screen | File → Load Profile → choose → OK | Labelled F-keys |
| Main | F1 "VIN/ZCS/FA" | The identity screen |
| Identity | F3 "ZCS/FA f. ECU" → E46 → module (ALSZ during the build) → OK | FG (VIN) and FA loaded for this session only |
| Identity | "Enter FA" → E46 → OK → OK at the VIN | The FA dialog. Type a code under Attribute → Add; select one → Delete key; OK |
| Identity | F6 "Back" | Main, showing modules and the default job (often `SG_CODIEREN`) |
| Main | F4 "Process ECU" → module → OK | JOBNAME and the module file appear |
| ECU screen | F2 "Change job" → job → OK | `CODIERDATEN_LESEN` reads; `SG_CODIEREN` writes; `FA_WRITE` stores the session FA |
| ECU screen | F3 "Execute job" | "coding active", then "coding ended". After a read, note the `.Cxx` name under JOBNAME |
| ECU screen | "Change ECU" / "Change SG/SGET" → module | Same job on another module |
| ECU screen | F4 "Read ECU" | Read with a nettodata window; close it |
| Main | "Process Car" → "Code Car" | **Never on this car** |

### G3. Session 1: backups, on the Touring first, then on the donor before it's stripped

**On the Touring** (original cluster, light module and DSC fitted):

1. **Identity.** Load profile Expert Mode → F1 → F3 → E46 → **ALSZ** → screenshot FG, the option list, the production date (#MMYY) and the type key. Back → F1 → F3 → E46 → **AKMB** → screenshot.
   - **Expect:** identical. If not, the car "has been messed with" (terra); trust ALSZ.
2. **Every module's coding.**
   - Back → F4 Process ECU → module → F2 → `CODIERDATEN_LESEN` → F3.
   - Note the `.Cxx` name, then at once copy both `C:\NCSEXPER\WORK\FSW_PSW.TRC` and `NETTODAT.TRC` to your backup folder as `E46-<MODULE>.<Cxx>-FSW_PSW.TRC` and `E46-<MODULE>.<Cxx>-NETTODAT.TRC`.
   - Do this for every module NCS lists, including AKMB, ALSZ, GM5, DSC, EWS, IHK, MRS/ABG, LWS and PDC if fitted.
   - Never press anything else between the read and the copy (Revtor).
3. **Identity jobs in Tool32** (screenshots):
   - `KOMBI46R.PRG` (or `KOMBI46.PRG` on an older cluster) → `IDENT` (`ID_COD_INDEX`, `ID_BMW_NR`), `STATUS_AIF_FG_NR_LESEN` and `STATUS_AIF_GWSZ_LESEN`.
   - `LSZ_2.PRG` → `IDENT`, then `SIA_LESEN` (`FG_NR`, and `GESAMTWEGSTRECKE_WERT`, which is ×100 km).
   - Photograph the odometer the same day.
4. **EEPROMs.** PA-Soft dumps of the cluster and light module, as the guide's backup list says.
5. **Two copies.** Store everything in two places, and write down the light-module and cluster part numbers.

**On the donor** (same steps 1–4, in the donor car):

- **FA:** screenshot the donor's FA. You may need to type it later for a session-only FA when coding the M3 cluster (G4).
- **Traces:** AKMB (expect `KMBE46M3.C23` or `C24`), ALSZ, DSC/MK60, IHK and LWS. Also save the donor cluster's PA-Soft EEPROM.

### G4. Session 4: the M3 cluster, after its VIN and mileage are set

**Before you start:** your mileage photo, the backups from G3, and the charger on.

1. **First look** (ignition on):
   - no tamper dot;
   - the odometer equals your photo plus the miles driven since;
   - the service display shows your car's interval (it is copied from the light module).
2. **VIN and mileage in Tool32.**
   - `KOMBI46R.PRG` → `STATUS_AIF_FG_NR_LESEN` (your VIN) and `C_FG_LESEN` (your VIN).
   - `STATUS_AIF_GWSZ_LESEN` gives km.
   - `LSZ_2.PRG` → `SIA_LESEN`: `FG_NR` is your last 7, and `GESAMTWEGSTRECKE_WERT` × 100 km should agree with the cluster.
   - **If the tamper dot is on:** the VIN differs between cluster and light module. Fix the cluster, never the light module.
3. **Which vehicle order is where.**
   - NCS → Expert Mode → F1 → F3 → E46 → **ALSZ**: screenshot. It must match the G3 Touring screenshot.
   - Back → F1 → F3 → E46 → **AKMB**: screenshot.
   - **Expect** the donor's type key and options after a DIY chip route. A service may already have written yours.
   - **If AKMB = ALSZ:** skip to step 6, using an FA read from ALSZ.
4. **Back up the cluster coding** while AKMB still holds the donor FA (the FA read from AKMB in step 3 is loaded):
   - Back → F4 → AKMB → F2 → `CODIERDATEN_LESEN` → F3.
   - **Expect** `KMBE46M3.C23` or `C24` under JOBNAME. Copy the TRC and NETTODAT now.
5. **Code the options from a complete MAN.**
   - Copy the TRC, edit only the lines in the G9 table, and save it as `FSW_PSW.MAN` in WORK, as "All files".
   - File → Load Profile → your manipulation profile → F1 → F3 → E46 → AKMB (the donor FA again) → F6 → F4 → AKMB → F2 → `SG_CODIEREN` → F3.
   - **Expect** "coding ended". Cycle the ignition.
   - Re-read (`CODIERDATEN_LESEN`). In NCS Dummy, load the new trace and compare it with your MAN: only your edited lines may differ.
   - **If it fails:**
     - COAPI-1020 → the MAN is missing or named `.MAN.txt`.
     - COAPI-1143 → the MAN is for another module, or has a typo.
     - COAPI-1141/1142 → empty the MAN.
6. **Store your FA in the cluster.**
   - F1 → F3 → E46 → **ALSZ** (your FA in session) → F6 → F4 → AKMB → F2 → `FA_WRITE` → F3 ("Job active", then "Job ended").
   - Restart NCS, read the FA from AKMB, and compare it with ALSZ: they should be identical.
   - **If NCS refuses AKMB with your FA** ("Codierindex … nicht zulässig" or "Ungültiger Codierindex"):
     - stop, and leave the donor FA in AKMB;
     - from now on, read the FA **only from ALSZ**;
     - for later cluster edits, use a session FA that NCS accepts (the donor FA from G3, typed in Enter FA, without `FA_WRITE`);
     - write this rule on the car's coding sheet. A cluster service can write your FA instead.
7. **Empty the MAN.**
8. **Functional checks.**
   - Oil lamp: Tool32 `KOMBI46R.PRG` → `STATUS_IO_LESEN`: `STAT_OELDRUCK_EIN` = 1 at key-on, 0 running. The charge and oil lamps should be on at key-on with the engine off, per the guide's lamp table.
   - Fuel: `STATUS_AIF_TANKDATEN_LESEN` → litres per sender (`HEBEL1`, `HEBEL2`) and total; check against a measured fill (the guide's procedure).
   - Doors: open each door, the tailgate and the rear glass, and record what the cluster shows.
   - Speedometer: against GPS.

### G5. Session 8: vehicle-order changes and the body modules

1. **Decide whether you need an FA change at all** (table below). Most of this build needs none.
2. **Read the FA from ALSZ** (or from AKMB, only if G4 step 6 succeeded). Then Enter FA → change → OK → Back.
3. **Write it:** F4 → ALSZ → F2 `FA_WRITE` → F3; Change ECU → AKMB → F3 (skip AKMB if G4 step 6 refused it). Restart NCS and re-read the FA from both.
4. **Code only the affected modules**, one at a time:
   - **A Touring module you never customised:** blank MAN → `SG_CODIEREN`. It takes defaults from the new FA.
   - **A module you customised** (ALSZ, GM5, IHK), or **M3 hardware coded by hand** (the M3 cluster, the M3 MK60): `CODIERDATEN_LESEN` → copy the trace to the MAN → edit → `SG_CODIEREN`. Never blank.
5. **Empty the MAN.** Clear faults in each coded module, cycle the ignition, and read faults again.
6. **Clear DME adaptations (Session 6) only** for changes on the engine side: MFL/cruise wiring, A/C hardware, fuel-pump or gearbox changes. Not for `$522` or `$7MA`. That keeps the readiness monitors from resetting needlessly.
7. **Never use Process Car / Code Car on this car.**

| Change | FA code | Modules to code | How | Source |
|---|---|---|---|---|
| None (the swap itself) | — | None from the FA. Cluster options through a MAN (G4); MK60 per the DSC session | — | §2, §4 |
| M Track (with the M3 MK60) | Leave `$7MA` out | MK60 (DSC research); AKMB `ANZEIGE_HOCHLADEN` = `aktiv` | MAN only | [liam821](https://liam821.com/MK60-Comparison.pdf), [ECUWorx](https://www.ecuworx.co.uk/uploads/M-Track.pdf) |
| Xenon or bi-xenon | `$522` | New xenon ALSZ: default from FA, then check; AKMB stores it in the central key | G6 | [BMW EBA xenon](https://bmw.etk.club/eba_docs/596en.pdf) |
| Front fogs added | `$520`? (unverified) | ALSZ, if a fog-variant module is fitted | G6 | ETK |
| Headlight washers | SRA code (unverified, `S502A`?) | GM5 `SCHEINWERFERREINIGUNG`, AKMB key | Default from FA, or a MAN | [BMW EBA SRA](https://bmw.etk.club/eba_docs/594en.pdf) |
| MFL buttons | None | None (BMW: no coding) | Wiring (G7); clear DME adaptations | [BMW EBA MFL](https://etk.club/eba_docs/284en.pdf) |
| M3 rear bumper with PDC | None | PDC echo thresholds (`…_HI e46_m3_3/01`) | MAN | NikolaiD list |
| Production date for an M3 MK60 | `#0902` or later, session only | MK60 | Session only, no `FA_WRITE` | Guide, Session 5 |

**The body modules after the swap:**

| Module | NCS name | For this swap | Check |
|---|---|---|---|
| General module | GM5 | No change; keep the Touring coding | `FUNKTIONEN_TOURING` and `HECKSCHEIBE_*` stay as read |
| Climate control | IHK (IHKA/IHKR) | No change while the FA is unchanged | `ZYLINDER_ZAHL 6_zylinder`, `MOTOR_ART benziner`, `GEREGELTER_KOMPRESSOR` (compare with the donor), `ZUSATZWASSERPUMPE` |
| Immobilizer | EWS | No coding change; `PARK/NEUTRAL_EINGANG` stays `aktiv` | — |
| Airbag | MRS/ABG | Only if the seats change; never code out occupancy detection | `ERKENNUNG_SITZBELEGUNG_*` |
| Park distance | PDC | Only with a different rear bumper | `ECHOSCHWELLWERTE_*_HI` |
| Rain/light sensor | RLS | None | — |
| Switch centre | (none in NCS) | None | — |
| Steering wheel | MFL | None | — |
| Steering angle | LWS | Coding only if the sensor is replaced; then calibrate (Session 7) | — |

### G6. Session 9: the light module and headlights

**Halogen M3 headlamps on the halogen Touring** (no coding):

1. Before the first light-up, check the plug pins at each lamp. Low beam X130/X135: pin 1 ground (BR), pin 2 supply (GE/GN left, GE/BL right), per BMW's EBA table.
2. Fit the bulbs the Touring's module expects: the wattages the module monitors. Wrong wattages give lamp-out warnings.
3. Run Tool32 `LSZ_2.PRG` → `FS_LESEN`. **Expect** no lamp faults (the lamp-fault codes are in the 0x32–0x47 range).
4. **Fogs:**
   - With factory fogs (module …024/…025): wire the M3 lamps (HB4) to the Touring's fog circuit (relay K47 is the same). `STATUS_LESEN` → `STAT_TASTER_NSW_EIN` follows the button.
   - Without factory fogs: you need the fog-variant module, the switch panel with the fog button (61318378576, or 61316911648 with a rain/light sensor) and K47. Treat it as a light-module swap (below).
5. **Side markers:** `SIDEMARKER_US` stays `aktiv`.

**Xenon or bi-xenon M3 headlamps (BMW's system)**, only after Session 4 is complete:

1. **Back up the old module:** its trace and NETTODAT, PA-Soft EEPROM, `SIA_LESEN` values and a mileage photo.
2. **Get the right module:** a xenon-variant light module (61319133026 without a rain/light sensor, …027 with one), **new, or virginized by a service**. Never a used module that still has a mileage on it.
3. **Fit the sensors and wiring** per BMW's EBA:
   - front-right sensor on the M3 arm (M3 angle joint 31122282404);
   - rear-right sensor on the Touring axle;
   - X12 pins 19/22/23 → X1451 pins 1/4/5;
   - X12 pins 46/14/26 → X13251 pins 1/4/5;
   - bi-xenon adapter cables X10106/X10107 at X131/X134.
4. **Fit the new module.** In NCS: F1 → F3 → E46 → **AKMB** (your FA, after G4 step 6). The new module has no FA yet; if AKMB was refused, type your FA from the G3 screenshot.
   - Enter FA → add `$522` → OK → Back.
   - F4 → ALSZ → `FA_WRITE`; then AKMB → `FA_WRITE`.
5. **Give the new module your VIN**, or have the service do it. ST052: data passes between modules "ONCE the VIN has been entered into the replacement unit".
   - **Inference, untested on ALSZ:** use NCS Expert's `FGNR_SCHREIBEN` job, which terra describes as the job that writes a module's VIN. The light module's own SGBD job for this is `C_FG_AUFTRAG`.
   - **Expect:** the module takes the mileage from the cluster. Check with `LSZ_2` → `SIA_LESEN`.
6. **Code the module:** blank MAN → F4 → ALSZ → `SG_CODIEREN` (default from your FA plus `$522`). Then re-read, and compare in NCS Dummy with:
   - your old halogen trace, for Touring rear-lamp and customisation lines, which you re-apply through a MAN;
   - the C35 xenon list (§3), for `BI_XENON`, `KALTUEBERWACHUNG_AL`, `LEUCHTWEITENREGELUNG`, `_AUTOM`, `_DYNAM`, `XENON_TEST` and `PWM_ANSTEUERUNG_AL`.
7. **Checks in Tool32 `LSZ_2.PRG`:**
   - `XENON_VORHANDEN` and `LWR_VORHANDEN` report present.
   - `STATUS_LESEN`: `STAT_SPANNUNG_BELADUNGSSENSOR_VORN_WERT` and `…HINTEN_WERT` read between 0 and 5 V and change as you load the car.
   - `FS_LESEN`: no 0x21–0x24 (sensor) or 0x1F (stepper) faults.
8. **BMW function test:** switch the low beam on; the lamps must adjust automatically. Load the front, then the rear, and allow about 15 seconds for each.
9. **Aim** at ride height, after the levelling has cycled (the guide's ST034 note: at least 30 seconds).

### G7. MFL retrofit wiring (BMW EBA 01 29 0 023 076; E46 with the SMART airbag sports wheel from 06/99)

| From (X10170, 10-pin green, at the switch fixture) | Wire | To | Function |
|---|---|---|---|
| Pin 8 | 0.35 BL/SW | DME X60004 pin 27 | MFL serial line (cruise buttons) to the DME |
| Pin 9 | 0.35 WS/RT/GE | LSZ X12 pin 21 (splice the cut lead, about 40 mm behind the plug) | K-bus |
| Pin 10 | 0.5 VI/GE | LSZ X12 pin 27 (splice) | Terminal R |

- **Finishing:** "Coding of the vehicle must not be carried out." Run a short test and a function test.
- **On this car:** the same DME pin 27 on the MSS54. Clear DME adaptations afterwards (Session 6).

### G8. Error and symptom table

| What you see | Meaning | Do this |
|---|---|---|
| IFH-0002 / IFH-0003 | No or garbled reply from the cable | Driver, COM1 in `obd.ini`, latency, USB port |
| IFH-0009 in NCS but INPA reads the DME | Body modules unreachable | Bridge pins 7/8; ignition at 2; choose ALSZ or AKMB |
| IFH-0032 / IFH-0037 | Ignition off / low voltage | Key to 2; charger on |
| SYS-0008 "JOB NOT FOUND" in Tool32 | Wrong SGBD for that job | Redesign cluster: `KOMBI46R.PRG`; older: `KOMBI46.PRG` |
| "VIN is faulty" lines when reading the FA | Bad communication | Pins 7/8 switch; test in INPA first |
| COAPI-1020 | No MAN file | Create `FSW_PSW.MAN`; show file extensions |
| COAPI-1141 / 1142 | An old MAN left in WORK | Empty it (don't delete it) |
| COAPI-1143 | MAN errors, or the wrong module | Use the trace from the same module; check spelling |
| COAPI-2000 | EDIABAS or SGBD error | Interface, pins 7/8; otherwise update DATEN, SGDAT and `ECU` |
| COAPI-2020 | Module not answering | Is it fitted and powered? Check its fuses and plugs |
| COAPI-2060 to 2099 | Communication broke during the job | BMW: end the session, disconnect everything, battery off 15 min, retry. On a GM5: a loose plug pin |
| "Codierindex … nicht zulässig" | The session FA's date or type excludes this module | Session-only FA (date or donor FA) without `FA_WRITE` |
| Tamper dot | VIN differs between cluster and light module, or the light module shows more mileage | Fix the cluster's VIN; never the light module |
| DSC and parking-brake lamps yellow after a cluster change | VIN mismatch | They clear after a short drive once the VINs match |
| Rear lights wrong after an FA change | Body coding from the wrong FA | Restore the ALSZ trace through a MAN; check the FA's type key |
| Lamp-out warning after fitting M3 lamps | Wrong bulb wattage | Use the specified bulbs |

### G9. Cluster parameters for this build (M3 cluster, index 23/24)

| Parameter | Set to | Why | Source |
|---|---|---|---|
| `CAN_OELDRUCKSCHALTER` | `nicht_aktiv` | Pin 13 wired from X60004 pin 11 | NAM3 61405 |
| `GENERATOR_UEBER_CAN` | `nicht_aktiv` with the wire, or `aktiv` with stock MSS54HP and no wire | Charge lamp | NAM3 61405, guide |
| `TOG_UEBER_CAN` | `nicht_aktiv` with pin 17 wired | Oil level | guide |
| `TANK_KENNLINIE` | **As read** (one value with three names) | Aliases | kd7iwp trace, Revtor |
| `OELNIVEAU_M3` | As read (`nicht_aktiv`) | CSL software only | guide |
| `ANZEIGE_HOCHLADEN` | `aktiv` only with an M Track MK60 and the LED | M Track light | liam821 |
| `SPRACHE`, `WEG_EINHEIT`, `WEG_DURCHSCHNITT`, `WEG_REICHWEITE`, `WEG_LIMIT`, `VERBRAUCH_D1`, `TEMPERATUR_EINHEIT`, `ZEIT_EINHEIT` | `us`, `mls`, `mph`, `mls`, `mls`, `mpg_us`, `grad_f`, `12_stunden` | US units (check only on a US cluster) | NikolaiD, kd7iwp |
| `K_ZAHL_TACHO`, `K_ZAHL_WEG` (+ `_KOMPL`) | As read (M3) | M3 wheels and tyres | inference |
| `SIA_LITER_GRENZE` / `LITER_SERVICE_INTERVALL` | As read (`s54b32…`) | S54 service limit | NikolaiD |
| `DREHZAHL_KENNLINIE` | As read (`kennlinie_03`) | M3 tachometer | NikolaiD |
| `GETRIEBEART` | `handschaltung` | Manual (a manual donor already has it) | ncsx patch |
| `CC_TUEREN`, `CC_LAMPEN` | As read (`aktiv`) | Check-control | kd7iwp |
| Any tamper or "Austauschpunkt" item | **Never touch** | The tamper dot is your proof of a matched VIN and true mileage | — |

### G10. Light-module parameter reference (US traces, kd7iwp; original C35 = bi-xenon)

| Parameter | US bi-xenon (C35) | Halogen Touring | Notes |
|---|---|---|---|
| `VARIANTE_LSZ` | `wert_01` (sedan from 09/2001) | Your trace (expect `wert_02`, Touring) | Body variant; drives the rear-lamp pins |
| `LAENDERVARIANTE_LSZ` | `wert_02` | Your trace | US |
| `SIDEMARKER_US` | `aktiv` | `aktiv` | Keep |
| `BI_XENON` | `aktiv` | `nicht_aktiv` | Bi-xenon high beam |
| `KALTUEBERWACHUNG_AL` | `nicht_aktiv` | Your trace | No cold check on xenon low beam (BMW ST052) |
| `XENON_TEST` | `aktiv` | Your trace | — |
| `PWM_ANSTEUERUNG_AL` | `wert_02` | Your trace | Low-beam drive |
| `LEUCHTWEITENREGELUNG` | `aktiv` | Your trace | Levelling on |
| `LEUCHTWEITENREG_AUTOM` | `aktiv` | Your trace | Automatic levelling |
| `LEUCHTWEITENREG_DYNAM` | `aktiv` | Your trace | Dynamic levelling |
| `KENNLINIE_LWR_SENSOR_VO` / `_HI` | `wert_01` / `wert_01` | — | Sensor curves |
| `FL_UND_NSW_NICHT_GLEICHZ` | `aktiv` | Your trace | Fogs with high beam (terra's list) |
| `GED_FL_ALS_DRL` | `aktiv` | Your trace | US daytime lights using dimmed high beams |

### G11. Data for diagrams

**D1. Where the car's identity lives** (nodes, then edges)

Nodes:

| Node | Holds | Changed by |
|---|---|---|
| ALSZ (Touring light module, LSZ_2) | VIN (7 characters), total distance in steps of 100 km, SI data, FA copy | Stays in the car; never written to match a donor |
| AKMB (M3 cluster, KOMBI46R, index 23/24) | VIN, total distance, SI data, FA copy (0xC2–0x181), coding (KMBE46M3.C2x) | VIN and mileage by the chip route or a service; FA by `FA_WRITE` |
| DME (MSS54/HP) | VIN in its AIF slots | Tool32 (Session 2); not coded from the FA |
| MK60 (DSC) | VIN; coding (`MK60.Cxx`) | PA-Soft VIN; NCS coding |
| GM5, IHK, PDC, MRS | Coding only | NCS, from the FA or a MAN |
| SZM | 17 coding bytes, not reachable from NCS | None |
| PC: NCS Expert session | The session FA (from the module you read, or Enter FA) | Every coding decision uses this |

Edges:

- ALSZ ⇄ AKMB: compare the VIN and mileage at every key-on (KL 15), over the K-bus. If they differ, the tamper dot lights.
- ALSZ → AKMB: mileage and SI data, only if the VINs match **and** the cluster's mileage is 0.
- AKMB → ALSZ: the light module's mileage only ever rises.
- Session FA → `FA_WRITE` → ALSZ and AKMB.
- Session FA → `SG_CODIEREN` (blank MAN) → each module's coding.
- MAN → `SG_CODIEREN` → one module's coding. The FA is unchanged.
- The bus topology is in `E46 S54 Touring wiring details/body_and_network_circuits.md` (Q3, N1).

**D2. Coding order with dependencies**

1. G1 software check → G3 backups (Touring) → G3 backups (donor).
2. Session 2 (DME VIN), done separately.
3. Cluster VIN and mileage set (service or chip) → G4 steps 1–2 check → step 3 FA comparison.
4. If AKMB ≠ ALSZ: step 4 back up AKMB → step 5 MAN coding → step 6 `FA_WRITE` (or the ALSZ-only rule).
5. Session 5, DSC, with a session FA from ALSZ, plus a session-only date if needed.
6. Session 6 DME → Session 7 steering angle.
7. Session 8 FA changes (only if needed) → affected modules only.
8. Session 9 lamps last.

Dependency rules:
- Never change the cluster and the light module in the same session (or on the same day).
- Never run Code Car.

**D3. Lamp-switch decision table** (per lamp)

| Wire fitted? | DME software | Coding |
|---|---|---|
| Yes | Any | `nicht_aktiv` |
| No (charge lamp only) | Stock MSS54HP | `GENERATOR_UEBER_CAN` `aktiv` |
| No (charge lamp only) | CSL software | Wire it; CAN doesn't work |
| No (oil pressure) | Any | Wire it; CAN doesn't light the lamp (NAM3 61405) |
| No (oil level) | MSS54HP | `TOG_UEBER_CAN` `aktiv` |

**D4. NCS error triage**

1. Does INPA reach the module?
   - **No:** pins 7/8, COM port, ignition, the module's fuse and plug.
   - **Yes:** go to question 2.
2. Does NCS read the FA from ALSZ?
   - **No, "VIN is faulty":** cable or pins.
   - **Yes:** go to question 3.
3. Does Process ECU show the module and its `.Cxx`?
   - **No, "Codierindex nicht zulässig":** session FA or date.
   - **Yes:** go to question 4.
4. Does `SG_CODIEREN` fail?
   - **COAPI-1020:** no MAN.
   - **COAPI-1141/1142:** an old MAN.
   - **COAPI-1143:** MAN content.
   - **COAPI-20xx:** communication or power.

**D5. Xenon path**

1. Cluster done → back up the light module → a new or virginized xenon module.
2. Sensors front right (M3 arm) and rear right (Touring axle) → X12 wiring → bi-xenon adapters.
3. Fit the module → FA + `$522` → `FA_WRITE` to ALSZ and AKMB → VIN into ALSZ → the module takes the cluster's mileage.
4. `SG_CODIEREN` (blank, then your MAN tweaks) → Tool32 checks → load test (about 15 s each end) → aim.

---

## Guide statements these findings correct

1. **WIRING-AND-CODING.md, Software table:** "| NCS Expert | Vehicle order and module coding | Version 3.0.x, with the "Expert Mode" and "Factory Coding" profiles and a manipulation profile (Revtor's or FISTER)… | One forum reply blames "IFH-0009: No Response from Controlunit" in NCS on version 4.x…"
   - **Correction:** "Version 4.0.1 (Standard Tools 2.12) with a manipulation profile: Revtor's `NCSDUMMY4.PFL` or terra's 'Expert Mode w/ Manipulation'. Version 3.x doesn't run on 64-bit Windows (no NTVDM), so use it only on a 32-bit laptop. IFH-0009 is 'NO RESPONSE FROM CONTROLUNIT': check pins 7/8, the ignition and the module chosen before blaming the version."
   - Sources: [NAM3 1281](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert) and [page 3](https://nam3forum.com/forums/forum/special-interests/coding-tuning/1281-getting-started-with-ncs-expert/page3), [Revtor](https://revtor.be/ncsdummy/ncsdummy.pdf), [EdiabasLib](https://github.com/uholeschak/ediabaslib).
2. **Troubleshooting row:** "| NCS Expert "IFH-0009" while INPA works | NCS Expert 4.x, or the wrong module chosen to read the vehicle order | Try version 3.0.x; read from AKMB, or EWS on an older car…"
   - **Correction:** "Cause: body modules not reached (pins 7/8 not bridged, ignition off), or the wrong module. Fix: bridge 7/8, key to 2, read from ALSZ (AKMB once verified), or KMB/EWS on a pre-09/2001 car."
3. **Session 1, step 4:** "Copy `C:\NCSEXPER\WORK\FSW_PSW.TRC` into a folder named after the module. Repeat for KMB or AKMB, LSZ or ALSZ, GM5, DSC, EWS and IHKA or IHKR."
   - **Add:**
     - Note the `.Cxx` name shown under JOBNAME *after* the read.
     - Copy `NETTODAT.TRC` too.
     - Name the files `E46-<MODULE>.<Cxx>-FSW_PSW.TRC`.
     - Copy before pressing anything else, because NCS reuses the TRC as a temporary file.
     - Include every module NCS lists (MRS, LWS, PDC too).
     - Repeat on the donor, including a screenshot of its FA (Revtor).
4. **Session 1, Rules:** "Don't write an M3 type code into your stored vehicle order… (our reading of the coding rules; nobody has documented it)."
   - **Correction/addition:** "The chip route does this for you: the cluster's EEPROM carries the donor's vehicle order ('the VO is brought back onto the new Chip', NAM3 154645; KOMBI46R stores the FA at 0xC2–0x181). After Session 4, read the FA from ALSZ and `FA_WRITE` it to AKMB (G4). Evidence that the body variant drives the rear-lamp coding: kd7iwp's change of `VARIANTE_LSZ` from `wert_01` to `wert_02` changed about 25 rear-lamp parameters."
5. **Session 4, step 1:** "NCS Expert → read from AKMB → Process ECU → AKMB → `CODIERDATEN_LESEN` → Execute. Back up the `FSW_PSW.TRC`."
   - **Correction:** "First compare the FA in ALSZ and in AKMB (AKMB will hold the donor's after a chip job). Read and code the cluster while NCS accepts it, then `FA_WRITE` your FA from ALSZ into AKMB; if NCS refuses, keep ALSZ as your only FA source." Use the G4 steps.
6. **Session 4 table:** "| `TANK_KENNLINIE` (fuel-gauge curve) | `60_l_literskala` | A plastic tank, the Touring's or the M3's; `metalltank` only for an ex-M56 SULEV metal tank…"
   - **Fuel gauge section:** "**The curve.** An M3 cluster offers `60_l_literskala`, `dad_tank_diesel` and `metalltank`… both should use `60_l_literskala`…"
   - **README:** "**Fuel-gauge curve:** `TANK_KENNLINIE` at `60_l_literskala`, for a plastic tank; our reading of the coding list"
   - **Correction for all three:** "In real traces the three keywords are listed together under one stored value (NCS shows every name for the same data). There's nothing to choose: leave `TANK_KENNLINIE` as read, and judge the gauge by a measured fill."
   - Sources: [kd7iwp KMB_E46.C04](https://github.com/kd7iwp/BMW-Coding/tree/master/E46), [Revtor](https://revtor.be/ncsdummy/ncsdummy.pdf).
7. **Fuel gauge, Check:** "Tool32 `KOMBI46R.PRG` → `STATUS_TANKINHALT_LESEN` gives litres for each sender and the total"
   - **Correction:** "`KOMBI46R.PRG` → `STATUS_AIF_TANKDATEN_LESEN` (`STAT_TANKINHALT_HEBEL1_WERT`, `…HEBEL2_WERT`, `…UNGEF_WERT`, `…GEF_WERT`, `STAT_RESERVE`). `STATUS_TANKINHALT_LESEN` is a `KOMBI46.PRG` job, for pre-redesign clusters, and returns SYS-0008 on KOMBI46R."
   - Sources: [KOMBI46R](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46R.md), [KOMBI46](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/KOMBI46.md).
8. **Cluster wiring:** "One snippet says these switches exist on cluster indexes 07, 08, 23 and 24; check that yours has them…"
   - **Session 4:** "one forum snippet says they exist on cluster coding indexes 07, 08, 23 and 24 … unverified"
   - **README open question:** "Which cluster coding indexes have the three lamp switches…; one snippet says 07, 08, 23 and 24."
   - **Correction:** "Confirmed on an index-24 cluster: nextelbuddy found 'alternator over can bus enabled oil level over can bus enabled but oil pressure over can bus not enabled' ([NAM3 61405](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/61405-why-does-my-oil-light-turn-off-with-ignition-ii-engine-off)). Absent from a pre-2003 non-M trace (`KMB_E46.C04`) and from a 2002 M3's cluster list. Index 23 and 07/08 are likely but unconfirmed." Keep the open question for 23 and 07/08 only.
9. **Session 5, Option B step 2:** "NCS Expert → Expert Mode → F1 → F3 → E46 → AKMB (try EWS if AKMB fails) → F6 → F4 → MK60…"
   - **Correction:** "… → E46 → **ALSZ** (AKMB only once G4 has verified it carries your FA) …". EWS holds no vehicle order on a car built from 09/2001: BMW's E46SGFAM flags EWS as ZCS-only.
   - Also note: an FA read from an unverified AKMB is the donor's, so the MK60 would be default-coded from an M3 coupe order.
10. **Session 5, step 6 (M Track):** "ECUWorx's procedure: in Enter FA, add `$7MA`; `FA_WRITE` to ALSZ and AKMB; `SG_CODIEREN` on AKMB, then on MK60…"
    - **Correction:** "In this car, don't run `SG_CODIEREN` on AKMB from the FA (default-coding the M3 cluster). Set `ANZEIGE_HOCHLADEN` = `aktiv` through a MAN (G4), set the MK60's M Track values through a MAN as well, and keep `$7MA` out of the stored FA."
11. **Session 8, step 1:** "NCS Expert → Expert Mode → read the vehicle order from AKMB (Session 1)."
    - **Correction:** "… from ALSZ (or AKMB once verified, G4 step 6)."
12. **Session 8, step 5:** "Load the Factory Coding profile → Process Car → Code Car. It stops at the first module that fails, so code the rest one at a time"
    - **Correction:** "Don't use Code Car on this car: it default-codes every module from the FA, including the M3 cluster and a hand-coded M3 MK60, and erases every customisation ('you'll lose all customizations you've ever made', terra). Code only the modules the change affects, one at a time (G5 table)."
13. **Session 8, step 6:** "Code AKMB and ALSZ themselves as well: one owner's gearbox icon stayed lit until he did"
    - **Correction:** "That owner changed his gearbox type. For this car, code ALSZ only when its options change, and the M3 cluster only through a MAN."
14. **Session 8, step 7:** "Reset the DME adaptations (Session 6)."
    - **Correction:** "Only after changes on the engine side (MFL/cruise wiring, A/C, pump, gearbox). Body-only FA changes don't touch the DME, and every reset clears readiness."
15. **Session 8:** "- **Climate control:** no swap coding found."
    - **Replace with:** "IHK coding carries `ZYLINDER_ZAHL`, `MOTOR_ART`, `GEREGELTER_KOMPRESSOR` and `ZUSATZWASSERPUMPE` (US six-cylinder sedan: `6_zylinder`, `benziner`, `gross`, `nicht_aktiv`). Both cars are six-cylinder petrol, so the Touring's coding stands. Compare it with the donor's IHK trace, and check `GEREGELTER_KOMPRESSOR` against the compressor fitted."
16. **Session 8:** "- **Restoring a module's defaults:** write a blank coding file…, except on a cluster whose coding index has been changed (Session 4)."
    - **Correction:** "… except on the M3 cluster (any index) and on any M3 module coded by hand (the M3 MK60). Restore those from their saved complete MAN or trace."
17. **Session 9, step 2:** "automatic levelling on (`AUTO_LWR_ENABLE`)"
    - **Correction:** "`LEUCHTWEITENREGELUNG`, `LEUCHTWEITENREG_AUTOM` and `LEUCHTWEITENREG_DYNAM` = `aktiv` (a US bi-xenon trace). `AUTO_LWR_ENABLE` appears only in an unsorted list of other cars' options."
18. **Session 9, step 3:** "The rear sensor stays on your Touring's axle while the front one now rides on the M3 arm"
    - **Clarify:** "A US halogen Touring has no level sensors. Both are new: rear right on the Touring axle, front right on the M3 arm with the M3 angle joint, per BMW's EBA."
    - Also add BMW's test: "load the front and then the rear … (delay approx. 15 seconds)".
19. **Mirrors and headlights:** "and for bi-xenon a light module of the 09/2001 redesign, which has the bi-xenon output"
    - **Correction:** "A 2003 Touring's light module is already the 09/2001 type, but BMW's xenon retrofit still replaces it with the xenon variant (61319133026, or …027 with a rain/light sensor). Fit it new or virginized, in the mileage-safe order (G6). Coding goes into the light module and the cluster's central coding key ([BMW EBA](https://bmw.etk.club/eba_docs/596en.pdf))."
    - Also: "the same light-switch units: 61319133022 to 61319133025 without xenon" → add "(…022/023 without fog lights, …024/025 with them)".
20. **README, Instrument cluster and mileage:** "PA-Soft can read the cluster, but its VIN and mileage areas are write-protected, and NCS Expert can't write the cluster's VIN at all"
    - **Nuance:** "…on a used cluster. BMW's own rule is that 'the VIN is entered in the cluster through coding and will only be accepted when the cluster mileage is zero' (ST052). That's why the routes that work start from a zero-mileage chip, and why a dealer can program a new cluster but not a used one."
21. **README, donor table (cluster row):** "Prefer a redesign cluster…"
    - **Sharpen:** "For a Touring built from 09/2002, use a cluster from 09/2002 or later (ECUswap: 'zwangsweise', mandatory). A 2003–06 donor gives index 23/24."
22. **README, open questions:**
    - **"What the M Track option code `$7MA` stands for":** answered in the manual already (Competition, ETK S7MAA, from 12/2004). Remove it.
    - **"How to add multifunction steering-wheel buttons":** answered by BMW's EBA (G7: three wires, no coding).
    - **"The light-module parameters and levelling-sensor wiring for M3 headlights that differ from the Touring's":** wiring answered (BMW EBA pin table). Parameter names answered (traces); values for the M3 front link remain open.
    - **"Whether the M3 console switch unit fits a Touring's console":** still open. It needs no coding.

---

## YouTube titles found (not watched; captions blocked)

- [Piotrek Chojnacki – E46 ZCS/FA Coding NCS Expert](https://www.youtube.com/watch?v=AvV4VMbdP0E) [title only]
- [Nicholas Gorkes – BMW Standard Tools: How to use NcsExpert and NcsDummy to code your E Series BMW!](https://www.youtube.com/watch?v=hW60zd2unUM) [title only]
- [DIY module – BMW e46 instrument cluster coding Explained](https://www.youtube.com/watch?v=PayuJE1uTds) [title only]
- [CSI E36 Tuners Channel – S.I.P BMW E46 KMB Instrument Cluster re-coding via magic bluetooth dongle](https://www.youtube.com/watch?v=OmW07nt4J94) [title only]

## Still open (summary)

- Whether NCS Expert accepts an M3 index-24 cluster (for coding and for `FA_WRITE`) with a 325iT FA in the session.
- The factory lamp-switch values on US M3 index 23 versus 24.
- Whether `TANK_KENNLINIE` has more than one real value on redesign clusters.
- The tailgate and rear-glass display on an M3 cluster.
- A US halogen ALSZ trace.
- The `KENNLINIE_LWR_SENSOR_*` values for the M3 front link on a Touring.
- Whether fogs need `$520` or a fog-variant light module.
- The SRA code and US M3 SRA fitment.
- The OC3 versus SBE occupancy-sensor split.
- The DSC-equipped US 325iT switch-unit part number.
- Which SP-Daten version first contains each M3 index.
- The US type keys.
