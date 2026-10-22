# DME and EWS coding for an S54 swap into a US 2001–05 E46 325i Touring

Tags used below: **(read)** = I read it on the page, PDF or file itself (e46fanatics threads were read through a headless-browser render because they return HTTP 406 to curl); **(snippet)** = seen only in a search-result snippet, not verified. Vendor prices were captured on 22 Oct 2026. "SGBD doc" means the community repository emdzej/ediabasx-docs-sgbd, which renders BMW EDIABAS SGBD job and table definitions as Markdown. It is not a BMW publication, but its job names match the ones forum users ran successfully (for example `ews3_initialisieren`, `aif_schreiben`).

## 1. EWS delete route: what the flash changes, who sells it, the DIY path, and what to expect afterwards

### Takeaway
An EWS delete flips one flag in the MSS54/MSS54HP's data area so the DME stops checking the EWS rolling code. The Touring's own EWS still checks the key and still controls the starter. In Oct 2026 it costs about $100–$300 from mail-in or remote-flash vendors, or a DIY license plus a partial read and reflash with BMWFlash. A stored DTC 130 (0x82) can remain afterwards and doesn't stop the engine starting, unless the "tampering DTC delete" is also applied.

### Cited Findings

#### What the delete changes
- BMW's description of EWS 3.3 (fitted to "the E46 beginning of production"): when the key is accepted, the EWS energizes its internal starter relay and sends a rolling code to the DME. "If the 'Codes' match the drive away protection is released and injection and ignition are enabled." If they don't match, the DME rolls forward "up to a maximum of 200 times… Failure to find a match will result in the engine cranking but not starting." (read) — [BMW ST051 Body Electronics I, "05 EWS", pp. 21–23](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- The EWS III (3.3) module checks "Code function not active, Transmission in P or N or clutch depressed, engine speed below specified RPM" and then "energizes the internal relay to begin starter operation" (read). So the starter interlock stays in the EWS, not the DME. — [BMW ST051, p. 23](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- A forum member who has done S54 swaps into MS42/43/45 cars: "When you EWS delete on the S54 DME or any DME you are removing the DME from that equation and the EWS module is now simply looking for a proper matchup with the key transponder itself" (read). — [NAM3 "MSS54 EWS Delete – Anyone Successful?", nextelbuddy, 01-31-2021](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful)
- The flag is a single byte. "You can EWS delete your binary quite easily, set 0x8A to 1" (read). — [NAM3 "MSS54 and MSS54HP EWS Syncing or Delete", bmwfnatic, 09-25-2025](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/320555-mss54-and-mss54hp-ews-syncing-or-delete)
- The same flag as a byte pattern in the partial .bin: "Extract partial .bin file from DME using BMWFlash. Modify hex code (I used HxD) by doing a find/replace of 64005a0000 with 64015a0000. Save new .bin file; give it another name to keep the native file. Reflash the new .bin file using BMWFlash" (read). That poster's car had no EWS module at all ("the car was sans-EWS"), so he also jumpered EWS connector pins 1 and 2. — [NAM3 38046, notrod, 06-26-2020](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful)
- Another owner made the same change ("updating the CRC, and flashing") and checked it by re-reading the partial bin (read). — [NAM3 38046, HoDoo, 04-01-2024](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful)
- Kassel describes its option as "EWS Delete – Coding delete for EWS. Immo off. Plug and play" (read). — [Kassel Performance MSS54/HP tuning page](https://www.kasselperformance.com/product/bmw-e46-m3-s54-mss54-hp-tuning/)
- ECUWorx's MSS5x tool has a combined option: "EWS Delete + EWS Tampering DTC Delete: Enables the vehicle to run with a foreign ECU, useful for ECU swaps or motor swaps" (read). — [ECUWorx MSS5x feature rundown](https://www.ecuworx.co.uk/how-to/a-run-down-of-features-of-the-mss5x-binary-modification-tool-and-what-they-do/)

#### Vendors (as listed on 22 Oct 2026)
- **Kassel Performance** (read; prices are embedded in the order form): "I am sending my DME to KP" $0, or "I need a DME $889 or DME Swap Program" $889; "EWS Delete" **$109**; "VIN Recode to Your VIN" **$20**, with a "VIN (For Recoding)" text field; "Engine Swap Coding (Includes Any/All Options Specific to Swap)" **$349**, described as "full consult will be conducted to ensure the DME is setup proper for each and every swap", with a text field for "Details of your engine swap. Chassis, trans, drive by wire, VIN, special requests". Optional "$429 core charge". Covers MSS54 and MSS54HP. No turnaround is stated. — [Kassel](https://www.kasselperformance.com/product/bmw-e46-m3-s54-mss54-hp-tuning/)
- **Kassel store** (read): the only "virginize" product is "MS43 Virginize" at $142 (for the M54's MS43 DME, not the MSS54). Also listed: "MSS54 to MSS54HP Conversion" $255 and "MSS54 / MSS54HP Full CSL Hardware/Firmware Conversion" $235. — [Kassel MS43 Virginize](https://www.kasselperformance.com/product/ms43-virginize/)
- **DUDMD** (read, Shopify product data): "E46 M3 EWS Delete – Bench Flash" **$215** ("Remove the DME/ECU and mail it in… ship it right back same day"); "Remote Flash" **$225**, marked "(Recommended)": "We mail out a OBD2 flash cable to you that you will keep… Windows 8 or newer laptop is required… In some rare cases, remote flashing doesn't work, we would have to go to bench flashing method." It lists MSS54 for 2000–2003 and MSS54HP for 2004–2006. California-customer variants are offered at the same prices. — [DUDMD](https://www.dudmd.com/products/e46-m3-mss54-ews-delete-service)
- **Severn Tuning** (read): "BMW MSS54/HP EWS Delete (2001-2006 E46 M3)", **$100** with the option "No, I have FlashApp or another flashing tool", or **$200** with "Yes (+$100)" (the option is named "Shipping"). "You must purchase an EWS delete for EACH ECU." The page says "You do need to ship your ECU(s) to us for the EWS delete if you have a method of reading/writing a full binary file to the ECU", which reads like a typo for "do not need". It ends "Recommended for off-road use only!" — [Severn](https://www.severntuning.com/products/bmw-mss54-hp-ews-delete-2001-2006-e46-m3)
- **RPM Motorsport** (read): "EWS DELETE SERVICE READY TO START!" is now **$300** (the guide's $100 is out of date). MSS54 and MSS54HP, with a list of supported hardware numbers (7831815 … 7838802). "1 to 2 Business days turnaround time upon arrival. Overnight shipping both ways using our UPS shipping label." — [RPM Motorsport](https://www.rpmmotorsport.net/collections/bmw-unlocked-ecu-service-ews-cas-delete/products/bmw-e46-m3-s54-m5-e39-s62-ews-delete-ready-to-start)
- **Poverty Built** (read): an MSS54/MSS54HP Stage 1/2/3 tune for **$220**, delivered by email ("No physical tune is shipped"). Its calibration list includes "Supported diagnostic, immobilizer, and swap configuration when selected". "For swaps or custom builds, contact Poverty Built directly." "A full ECU read is not required unless Poverty Built requests one." Flashing software and cables are separate. Emissions-related options are "intended only for lawful closed-course competition or off-road use." — [Poverty Built](https://povertybuilt.com/products/e46-m3-s54-custom-tune-mss54)
- **Hack Engineering** (read): MSS54 coding service, **£250**, done on a file: "use any INPA-compatible USB/OBD cable along with free BMWFlash Software to take a partial DME read. Email us the file…" The listed services don't name an EWS delete. — [Hack Engineering](https://www.hackengineering.co.uk/?p=49060)
- Others seen only in snippets: Renovelo's MSS54HP swap tunes ($149.99–$199.99, EWS removed, need ByteTuner to flash) (snippet) — [Renovelo](https://www.renovelo.com/?p=3234); Miller Performance's pre-configured S54 swap ECU at $1,250 (snippet) — [Miller](https://www.millerperformancecars.com/store/w-a-r-flash-tune-system/s54-swap-tuning-solution-miller-performance-detail).

#### DIY path (documented end to end)
- ECUWorx's guide needs: the MSS5x Binary Modification Tool, "BMWFlash or MSSFlasher", "A FTDI based OBD2 diagnostic cable such as a BMTechnic cable / BM or a KKL Vag-Com cable", and "A trickle charger that can supply 10A… I use a CTEK MXS 10". Its steps, verbatim in substance (read):
  1. Connect the charger and the cable; "Turn your ignition to position 2 but don't start the car. Next, click 'File' and then 'Read DME'."
  2. "Select 'No' to take a partial read." Save it and "take a copy of this and keep it somewhere safe".
  3. Load it in the tool and request and activate a license ("Action" → "Generate License", paid via PayPal; "Action" → "Activate License").
  4. "Make the desired changes and then click 'Apply Changes' and then 'Write Changes'", then save.
  5. In BMWFlash: "Click 'File' and 'Reflash DME'". Accept the power warning, choose the file ("BMW Flash Binary (*.bin)"); "This should take no more than a few minutes"; it returns to "Ready To Upgrade".
  6. "Turn the key back to position 0 and back to position 2."
  — [ECUWorx: Using the MSS5x Binary Modification Tool](https://www.ecuworx.co.uk/how-to/using-the-mss5x-binary-modification-tool/)
- BMWFlash's free version only reads; a NAM3 summary describes it as "can read FULL EPROM data dumps and write in limited fashion (licensed version only)" (read). — [NAM3 "Comprehensive MSS54/MSS54HP DME Information"](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)
- Cable: "I believe the Bimmergeeks K+DCAN cable is the gold standard, but their site shows all cables out of stock at this time" (read, 09-27-2025). — [NAM3 320555, D-O](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/320555-mss54-and-mss54hp-ews-syncing-or-delete)
- 32 kB binaries are MSS54 and 64 kB are MSS54HP: "The variant is most easy to determine by size, 32kb = MSS54, 64kb = MSS54HP" (read). — [NAM3 2052](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)

#### After the delete
- "It turns out my mistake was assuming that the engine wouldn't start because the 0x82 DTC existed… Since I didn't disable the DTC, the code still shows up, but I confirmed that the engine can start. If using a normal set of EWS - keys, jumpering the pins on the EWS connector is unnecessary." (read) — [NAM3 38046, HoDoo](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful)
- "You don't actually have to bridge any pins regardless of which DME your car originally was… If you find yourself having to jump the actual pins in the EWS module itself then you have another EWS related issue with either the EWS module and a mismatch between the key or the transponder and the key is bad." (read) — [NAM3 38046, nextelbuddy](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful)
- 0x82 and 130 are the same code. The MSS54 SGBD's fault-location table lists "0x82 | EWS-Signalmanipulation" and "0x42 | EWS-Schnittstelle" (read), and INPA lists them in decimal as "130 EWS 3.3 Anti Tampering Protection" and "66 DME-EWS Communication" (read). — [SGBD doc MSS54DS0 (FORTTEXTE)](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md); [NAM3 38046, notrod's DTC list](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/38046-mss54-ews-delete-anyone-successful)
- In one 325xi wagon, flashing an EWS delete gave "a no crank/no start condition". The owner read this as the EWS not completing the starter circuit, and the thread closed unresolved (read). — [e46fanatics "Can't sync EWS/DME on S54 swapped E46 wagon"](https://www.e46fanatics.com/threads/cant-sync-ews-dme-on-s54-swapped-e46-wagon.1300465/)

### Inferences
- **Recommended route for this Touring:** an EWS delete of the donor MSS54/HP, with the Touring's VIN written in (Q4) and, if the donor was SMG, the manual software variant or conversion (Q5). Keep the Touring's EWS, keys, ring antenna and the clutch-switch wire to EWS pin 8 untouched, and don't jumper anything. This follows from BMW's description (the EWS still releases the starter) and from the NAM3 reports.
- **Vendor route, step by step:**
  1. Read and save the donor DME's fault memory, hardware number and AIF (Tool32, Q4) before shipping it.
  2. Order "EWS delete" with "VIN recode", plus "manual/6MT" if the donor was SMG. At Kassel, "Engine Swap Coding" ($349) bundles all swap options with a consult.
  3. **Decline** SAP delete, post-cat O2 delete, cat-efficiency DTC delete and any EVAP coding-out. Kassel, ECUWorx, Hack Engineering and Poverty Built all offer such options, and they are illegal on a road car.
  4. Fit the DME, switch on and read faults. Expect a possibly stored 130 (0x82) unless the tampering DTC was also deleted.
- **DIY route** (from ECUWorx and NAM3): partial read with BMWFlash; apply "EWS Delete + EWS Tampering DTC Delete" in the ECUWorx tool, or hand-edit the flag and correct the checksum as HoDoo did; reflash with a licensed BMWFlash or MSS Flasher on a 10 A charger; key cycle. Hand-editing without fixing the checksum is a risk. The tool route avoids it.
- **Security trade-off:** after the delete, the only immobilizer layer left is the EWS's starter release. The DME will run whatever turns the engine over. This is my inference from BMW's description of the EWS III and DME roles.
- **If the car won't crank after a delete,** the cause is upstream of the DME: key, ring antenna, EWS, or the clutch/P-N input to the EWS (Q3 lists the EWS3 status fields to check). If it cranks but won't start, confirm the flash took (re-read the bin) and look at fuel-pump control (Q2).

### Gaps
- Kassel's turnaround, and whether Kassel still virginizes MSS54s. Only MS43 virginizing is listed in Oct 2026.
- Price of the ECUWorx MSS5x license. The £275 on the FAQ is the MSS6x remap, not this license.
- Whether a stored 130 (0x82) lights the MIL or affects OBD readiness on an inspection. No source covers it.
- Whether an EWS delete has any legal or insurance implications in US states. Not researched, and no source raised it.
- Terra's bimmerforums thread (cited by NAM3 for the sync method) is behind Cloudflare and the Wayback Machine was unreachable, so it is unverified.

## 2. EWS sync route: virginizing, the Tool32 sequence, INPA functions, reading the status, and the Touring failure modes

### Takeaway
A used donor DME can't be synced to the Touring's EWS. BMW burns the EWS 3.3 rolling-code table into the DME once, and "alignment" only resets it to code #1. Syncing only works with a virgin DME (blanked at memory level by BDM or a vendor) or one pre-loaded with matching data. The Tool32 sequence is `EWS3.prg` → `WECHSELCODE_SYNC_DME`, then `MSS54DS0.PRG` (which also covers the MSS54HP) → `EWS3_INITIALISIEREN` with `0x01` → `EWS3_SYNC`, then check `EWS3_GET_STATUS`. Both reported Touring failures fit a non-virgin DME, and the INPA messages they saw match the MS45 SGBD's texts.

### Cited Findings

#### Why a used DME won't sync (BMW)
- "The DME will automatically burn the 'Rolling Code Table' into its memory. Once the table has been burned into the DME memory it can NOT be changed. For this reason once a DME is 'Married' to the vehicle it will not work in any other vehicle. Under certain condition 'Alignment' of the DME and EWS III (3.3) modules may still be necessary. The alignment procedure only resets the code table to code #1 it does not change the 'Rolling Code Table'." (read) — [BMW ST051, p. 24](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- For a new DME: "After programming the DISplus software informs the EWS III (3.3) control module that a new DME has been installed. The next time the ignition is switched on, the EWS III (3.3) module will send the entire 'Rolling Code Table' to the DME and reset it to 'Rolling Code' #1." (read) — [BMW ST051, p. 24](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- The EWS's own rolling code "is burned into the module and cannot be over-written by ZCS Coding or DME alignment procedures." (read) — [BMW ST051, p. 21](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- "If during diagnosis the key is switched on while the DME or EWS modules are 'Disconnected', the alignment procedure will need to be carried out. The 'Alignment' procedure may be carried out an unlimited number of times." (read) — [BMW ST051, p. 22](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- Forum consensus matches: "DME and EWS are a matched/married set and need to be together, otherwise you get crank no start… An EWS Delete patch of the MSS54 software gets around that." (read) — [e46fanatics "EWS synch for S54 swap into e46 touring", Bali, Sep 18 2023](https://www.e46fanatics.com/threads/ews-synch-for-s54-swap-into-e46-touring.1318881/)

#### SGBD files and job definitions
- `MSS54DS0.prg` is described as "MSS52/MSS54/MSS54HP fuer S54B32", revision 2.09, so **the MSS54HP uses the same SGBD** (read). The DME group file `d_0012.grp` maps variant IDs 1830, 1B30, 1B31, 1860, 1B60, 1B61, 1B70, 1B80 and 1B90 to `MSS54DS0` (read). — [SGBD doc index](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/index.md); [SGBD doc d_0012](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/d_0012.md)
- `EWS3.prg` ("Elektronische Wegfahrsperre Entwicklungs SGBD", rev 2.000) contains, among 47 jobs (read):
  - `WECHSELCODE_SYNC_DME` "Wechselcodesynchronisation EWS 3 - DME anstossen", no arguments, returns `JOB_STATUS`
  - `ISN_LESEN` returns `ISN` ("16 Bit"), and `ISN_SCHREIBEN` takes an argument `ISN`
  - `STATUS_LESEN`, `FGNR_LESEN`, `SCHL_SPERREN_FREIGEBEN` (key bar/release), `C_C_LESEN` (coding data)
  — [SGBD doc EWS3](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/EWS3.md)
- `MSS54DS0.prg` jobs (read):
  - `EWS3_GET_STATUS` "EWS3 Synchonisierungsstatus abfragen": no arguments; results `JOB_STATUS`, `EWS3_STATUS` (string), `EWS3_STATUS_WERT` (int)
  - `EWS3_INITIALISIEREN` "EWS3 initialisieren/abgleichen": argument `EWS3_MODE` (int); same results
  - `EWS3_SYNC` "EWS3-Steuergeraet ruecksetzen": results `JOB_STATUS`, `EWS3_STATUS`
  - `STEUERN_SYNC_MODE` "Synchronisation EWS" (argument `MODE`) and `STATUS_SYNC_MODE` "Status EWS auslesen"
  - `STATUS_DIGITAL`, which includes `STAT_EWS3_FREIGABE` "Status Freigabe EWS3"
  - No ISN read/write job and no AIF write job
  — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- The MSS54DS0 fault matrix lists these fault types for location 0x82 (EWS-Signalmanipulation): "0x10 Startwert defekt", "0x11 Wechselcode verloren", "0x12 Startwert leer", "0x13 Manipulation" (read). That is: start value defective, rolling code lost, start value empty, manipulation. — [SGBD doc MSS54DS0 (FARTMATRIX, FARTTEXTE)](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- The MS45 SGBD (`MS450DS0`) has a start-value status table `EWSSTART` (read):
  - "0x00 MS45 bereit Startwert zu empfangen"
  - "0x01 kein freier Startwert Speicherplatz vorhanden"
  - "0x02 noch kein Startwert gespeichert"
  - "0x03 Startwert nicht plausibel"

  And a receive-status table `EWSEMPFANGSSTATUS`:
  - "0x00 Startwert verstanden und akzeptiert"
  - "0x02 Startwert nicht verstanden"
  - "0x03 Interfacefehler: Frame oder Parity oder Timeout"
  - "0x07 Kein Startwert programmiert"

  Its job `DME_STARTWERT_ABGLEICH` "Kopiert die ISN auf beide Wechselcodes" (copies the ISN to both rolling codes). The MSS54DS0 documentation has no equivalent text tables.
  — [SGBD doc MS450DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MS450DS0.md)

#### The documented Tool32 sequence (worked once, on a CSL-clone MSS54HP)
- "First load EWS3.prg then execute "wechselcode_sync_dme". Then load MSS54DS0.prg and execute "ews3_initialisieren" with 0x01 argument (just write 0x01 in the argument line). To finish execute "ews3_sync". If every job returned "OKAY" the code 130 should clear and the car should fire up correctly. I did it with my ISN written in the DME throught BDM, I'm not sure if it works with a virgin ISN." (read) — [NAM3 "EWS sync issue with csl clone DME – Solved", ValVal456, 01-04-2022](https://nam3forum.com/forums/forum/special-interests/coding-tuning/145696-ews-sync-issue-with-csl-clone-dme-solved)
- In the same thread, INPA gave "error_SG_rejected", and running EWS3 jobs from `MSS52DSO.prg` (the wrong SGBD) failed at "EWS3 initialisation" with the same error. The poster had tried the ISN "set at FFFF FFFF FFFF". Another member: "You need to flash a virgin CSL with BDM on both Eeproms (Master/Slave) and sync with Inpa." A third: "I was lucky with DIS via ussual obd cable." (read) — [NAM3 145696](https://nam3forum.com/forums/forum/special-interests/coding-tuning/145696-ews-sync-issue-with-csl-clone-dme-solved)
- The method came from a bimmerforums thread, "Tool32 EWS Alignment process help" (unverified: blocked by Cloudflare). — [bimmerforums](https://www.bimmerforums.com/forum/showthread.php?2426174-Tool32-EWS-Alignment-process-help)
- A moderator in 2025: "EWS sync should be done via INPA" (read). — [NAM3 320555](https://nam3forum.com/forums/forum/main-forum/e46-2001-2006/320555-mss54-and-mss54hp-ews-syncing-or-delete)

#### Touring failure case A: 2002 325iT, donor DME not virginized
- INPA "Synch EWS to DME page": "ApiCheckJobStatus: Job-Status error: (ERROR_SG_REJECTED)" followed by "Error #134 API-0014 Result not found" (read).
- After reinstalling the tools: "EWS3 Synch using the Shift F6 function… after clicking F2 Reset and F1 Store under the EWS3 Synch page I got the error message (translated from German) 'no free starting value storage space available' followed by 'Interface error: frame or parity or timeout'" (read).
- ISTA+: the EWS–DME sync button "is grayed out". ISTA-P crashed on launch (read).
- Tool32: "Load EWS3.prg / Execute job "wechselcode_sync_dme". / Load MSS54DSO.prg / Execute job "ews3_initialisieren" with 0x01 argument. / Execute job "ews3 _sync". All three jobs return an "OKAY". After the ews3_synch the ews3_status is "reset". However, when I then execute ews3_get_status the result is Job status OKAY, ews3_status Invalid, and ews3_status_wert=3." Still crank-no-start, with "Code 82 EWS 3.3 Anti-tampering protection" (read).
- Fix: "I brought the EWS and key over from the donor vehicle… It still had an EWS error until I ran EWS synch jobs in Tool32 which worked to resynch the donor vehicle EWS and DME. This cleared the EWS error code". The car stayed crank-no-start with "fuel pump relay error code 1" and "all six injectors disabled and zero pulse duration" (read).
- Source for all of case A: [e46fanatics 1318881, DaveVolvoBMW, Sep 12–17 2023](https://www.e46fanatics.com/threads/ews-synch-for-s54-swap-into-e46-touring.1318881/)

#### Touring failure case B: 03/2001 325xi wagon (auto, being converted), Kassel-virginized 2003.5 MSS54
- "I'm trying to sync a virginized 2003.5 MSS54 DME with the EWS from a 2001 325xi wagon but am getting a 'start value not understood' error in INPA. ISTA-P isn't able to align either… I can't 'reset' the start value in INPA either - doing so gives a 'start value not set' error." DTCs: "066 'EWS interface: no communication' and 130 'EWS Signal manipulation'". "Kassel advised to sync with ISTA-P" (read).
- Before virginizing, the car ran only with two keys: "M3 key in the antenna, wagon key to turn the ignition switch" (read).
- Bali: "pre-09/2001 EWS uses ZCS style coding while that post-09/2001 MSS54 DME uses FA style coding. It's not fun mixing modules of those two together… You can usually get the mixed modules coded, but first you have to identify what you have" (read). The thread closed without a resolution.
- Source for all of case B: [e46fanatics 1300465, S54ever, Dec 28 2021](https://www.e46fanatics.com/threads/cant-sync-ews-dme-on-s54-swapped-e46-wagon.1300465/)

#### Other sync notes
- BMW: the E46 stores its ZCS in "Instrument Cluster/LSZ", not the EWS, and "an alternative to the ZCS code was introduced on 9/01 production E46 vehicles… the Vehicle Order (VO/FA)" (read). — [BMW ST406 "06 Vehicle Coding Information", pp. 5, 10–11](https://archive.org/download/BMWTechnicalTrainingDocuments/ST406%20Coding%20%26%20Programming/06%20Vehicle%20Coding%20Information.pdf)
- A Z3 page says the INPA steps for EWS alignment are F5, then F6 for EWS alignment, then F2 to reset the start value, then key off for about 25 seconds, and that a voltage drop can make the sync fail. That is a non-M Z3, a different DME (snippet). — [zroadster](https://zroadster.org/threads/time-for-an-overhaul-of-my-1-9-98-bmw-z3-individual.60313/page-53)
- Kassel Performance's YouTube video "BMW M54 Siemens MS43 325 330 EWS Sync - INPA" exists. It covers the MS43, not the MSS54; I saw only the title and channel via oEmbed and didn't watch it. — [YouTube, KasselPerformance](https://www.youtube.com/watch?v=HPoaKPqLpgE)
- Vendor "used DME to your car" service: RPM Motorsport, "BMW E39 E46 M3 M5 S54 S62 USED ECU DME EWS PROGRAMMING MSS54 - MSS52", $300. The description only lists supported hardware (read). — [RPM](https://rpmmotorsport.net/products/bmw-e39-e46-m3-m5-s54-s62-used-ecu-dme-ews-programming)

### Inferences
- **Which SGBD:** load `C:\EDIABAS\Ecu\MSS54DS0.PRG` (zero, not the letter O; posters typed "MSS54DSO") for both MSS54 and MSS54HP. `MSS52DS0` and `MSS52DS1` are the wrong files.
- **Assembled Tool32 sync procedure** (only for a virgin or pre-matched DME; from ValVal456's sequence and the SGBD doc):
  1. Battery on a charger, ignition at position 2 with the engine off.
  2. Tool32 → File → Load SGBD → `EWS3.prg` → run `WECHSELCODE_SYNC_DME`. Expect `JOB_STATUS = OKAY`.
  3. Load `MSS54DS0.PRG`. Type `0x01` in the Arguments box and run `EWS3_INITIALISIEREN`. Expect `OKAY`.
  4. Run `EWS3_SYNC`. Expect `OKAY`; `EWS3_STATUS` read "reset" in case A.
  5. Run `EWS3_GET_STATUS`. In case A the failing state was `EWS3_STATUS = Invalid`, `EWS3_STATUS_WERT = 3`.
  6. Run `FS_LESEN`. DTC 130/0x82 should be gone. Run `STATUS_DIGITAL` and check `STAT_EWS3_FREIGABE`.
  7. Key off for at least 10 s, then try to start.
- **Reading DTC 130 (0x82) by fault type** (from the SGBD fault matrix):
  - "Startwert leer": the DME is virgin and hasn't received the table.
  - "Wechselcode verloren": an ordinary loss of sync. Alignment should fix it.
  - "Manipulation": the DME is married to another EWS. Virginize, delete, or use the donor EWS.
  - DTC 66 (0x42, "EWS-Schnittstelle"): check the EWS–DME line, or the key was on while a module was unplugged (BMW: re-run alignment).
- **INPA messages decoded:**
  - `ERROR_SG_REJECTED` means the control unit refused the job (the EWS3 SGBD's job-result table lists 0xA2 = `ERROR_ECU_REJECTED`). It points at the DME, not the cable.
  - The texts in case A ("no free starting value storage space available", "Interface error: frame or parity or timeout") and case B ("start value not understood", "start value not set") match the MS45 SGBD's `EWSSTART` and `EWSEMPFANGSSTATUS` tables word for word, and MSS54DS0 has no such tables.
  - Two readings follow. The INPA page used may have been the M54 engine script rather than "MS S54 for S54 M3". Or the MSS54 returns the same family of messages. In both readings, "no free start-value storage" fits a DME that already holds a married table.
- **The ZCS-versus-FA theory is unlikely to be the cause.** BMW says the rolling code is independent of ZCS coding, the E46 keeps its ZCS in the cluster and LSZ, and the MSS54 isn't ZCS/FA-coded at all (no coding jobs in its SGBD). Case B's more likely causes are a DME that wasn't fully virginized, the wrong INPA script, or supply voltage.
- **How to virginize:** there's no documented OBD job to write an ISN or rolling-code table into an MSS54. MSS54DS0 has no ISN jobs, while MSS52DS1 has `ISN_LESEN`. NAM3 posters did it with BDM on both EEPROMs. So virginizing is effectively a vendor job: send the DME to someone who offers it (RPM's $300 "used DME EWS programming", or ask Kassel), then do the sync above. A plausible alternative to ask about is a DME pre-loaded with the Touring EWS's data. ValVal456 had the ISN written by BDM, and `EWS3.prg` → `ISN_LESEN` can read the EWS's 16-bit ISN. No vendor offering this was found.
- **Cost and benefit:** virginizing ($142–$300 plus shipping, with a sync risk) costs about the same as a delete ($100–$300) and is less certain, which is why most Touring builders delete.
- **After the EWS is fixed,** a crank-no-start with an MSS54 fuel-pump-relay DTC (SGBD location 0x01 "Relais Kraftstoffpumpe") and injectors disabled points to the fuel-pump control difference: US MSS54 PWM to the EKP module versus a relay. That is covered in the guide's Fuel system section and by other researchers.

### Gaps
- What the other `EWS3_INITIALISIEREN` modes and `EWS3_STATUS_WERT` values mean (only "3 = Invalid" and "reset" are reported).
- Whether INPA's "MS S54 for S54 M3" script has its own EWS3 sync page, and its key layout. Case A reports Shift+F6, then F2 Reset and F1 Store, but which engine script that was isn't stated.
- A first-hand, start-to-finish success syncing a virginized MSS54 to a different car's EWS3. None found; the solved case used BDM-written data.
- Terra's original bimmerforums write-up and any INPA "ISN read/write" walkthrough for EWS3 (bimmerforums is behind Cloudflare).

## 3. Donor EWS route: using the M3's EWS and keys, SMG neutral coding, locks and keys

### Takeaway
Moving the donor's EWS and key with its DME, then re-aligning them in Tool32, cleared the EWS fault in one 325iT. But the car then needs the donor key's transponder to start, so unless lock cylinders are swapped, re-keyed or new keys made, you end up carrying two keys. The EWS coding has a `PARK/NEUTRAL_EINGANG` parameter (aktiv/nicht_aktiv), and EWS3 status shows whether the starter is blocked by the P/N input. Which value a US manual Touring needs wasn't documented.

### Cited Findings
- Case A, 2002 325iT: "I brought the EWS and key over from the donor vehicle and installed them in the swap vehicle. It still had an EWS error until I ran EWS synch jobs in Tool32 which worked to resynch the donor vehicle EWS and DME. This cleared the EWS error code" (read). — [e46fanatics 1318881](https://www.e46fanatics.com/threads/ews-synch-for-s54-swap-into-e46-touring.1318881/)
- Case B wagon with the donor EWS and DME fitted: "Started the wagon post swap with 2 keys - M3 key in the antenna, wagon key to turn the ignition switch - no problems, runs great." The owner had "Removed key ring antenna from the steering column but kept wired in" (read). — [e46fanatics 1300465](https://www.e46fanatics.com/threads/cant-sync-ews-dme-on-s54-swapped-e46-wagon.1300465/)
- BMW, EWS 3.3 start sequence: the transponder is powered through the ring antenna and returns the key ID and changing code. "The EWS III module also sends a new changing code to the key." Keys can be barred or released; the EWS is "codeable for only 10 keys (4 delivered with vehicle and 6 replacement)". "Replacement EWS III (3.3) Control Modules are ordered VIN specific… Once ZCS coded, the DISplus software 'resets' the current rolling code in the DME back to 'Rolling Code' #1" (read). — [BMW ST051, pp. 22–24](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- "The EWS is the tricky one to change, since the key transponders store the VIN and odometer reading" (read). Another member: "If you want to change the VIN on the EWS, you need to buy a AK90" (read). — [e46fanatics "Chassis VIN, DME/EWS VIN, LCM/IKE VIN all mismatched"](https://www.e46fanatics.com/threads/chassis-vin-dme-ews-vin-lcm-ike-vin-all-mismatched-help.1253491/)
- EWS3 SGBD `STATUS_LESEN` returns (read):
  - starter status: `STAT_ANLASSER_FREIGESCHALTET` (starter released), `STAT_ANLASSER_AUS_P_N` (starter off because of P/N), `STAT_P_N_EINGANG` (P/N input)
  - DME status: `STAT_DME_LEITUNG_FREI`, `STAT_EWS_JUNGFRAEULICH` (EWS virgin)
  - key status: `STAT_SCHLUESSEL_SENDET` (key sending), `STAT_SCHLUESSEL_GESPERRT` (key barred), `STAT_SCHLUESSEL_NIO_ID`, `STAT_SCHLUESSEL_NIO_PW`, `STAT_SCHLUESSEL_NIO_WC` (key ID, password or changing code not OK), `STAT_AKTUELLE_SCHLUESSELNUMMER` (current key number)

  The SGBD also has `FGNR_SCHREIBEN` ("Schreiben der 17-stelligen Fahrgestellnummer inkl. PZ") and `SCHL_SPERREN_FREIGEBEN`.
  — [SGBD doc EWS3](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/EWS3.md)
- Two real E46 EWS coding traces (NCS Expert `E46-EWS.C81-FSW_PSW.TRC`) show the parameter `PARK/NEUTRAL_EINGANG` set to `aktiv` in one car and `nicht_aktiv` in another. Both share `K_BUS_FREI_OHNE nicht_aktiv`, `ZEIT_BIS_AUTOM_SPERREN wert_01` and `EWS_3_SCHNITTSTELLE aktiv` (read). The cars' gearbox and market aren't stated. — [kd7iwp/BMW-Coding trace](https://raw.githubusercontent.com/kd7iwp/BMW-Coding/HEAD/E46/E46-EWS.C81-FSW_PSW.TRC); [Mael-Le-Garrec/E46 trace (323i)](https://raw.githubusercontent.com/Mael-Le-Garrec/E46/HEAD/E46_323i_backup/CODING/E46-EWS.C81-FSW_PSW.TRC)
- Owners who converted an E46 from auto to manual report recoding the EWS with NCS Expert as part of the job: "I have also coded the KMB, EWS, and DSC using NCS Expert (and cleared adaptations)" (read). — [e46fanatics "Manual Swap Rev Hang"](https://www.e46fanatics.com/threads/manual-swap-rev-hang.1315205/)

### Inferences
- **This route only makes sense as a test,** or if you accept the donor's keys. Two keys are needed: the donor transponder near the ring antenna for the EWS, and the Touring key for the mechanical ignition lock and doors. Making it one key would mean re-keying the ignition, door and tailgate cylinders to the donor key (a locksmith job; the Touring's tailgate and rear-glass locks have no M3 equivalent), or adding keys to the donor EWS with a key-programming tool. Neither was documented for this swap.
- **Coding a donor EWS** (if you do it):
  1. Before removing anything, read the Touring EWS's coding with NCS Expert and save `FSW_PSW.TRC`.
  2. Code the donor EWS to match, especially `PARK/NEUTRAL_EINGANG`.
  3. Verify in Tool32: `EWS3.prg` → `STATUS_LESEN` with the clutch pressed should show `STAT_ANLASSER_AUS_P_N = 0` and `STAT_ANLASSER_FREIGESCHALTET = 1` while cranking.
  4. Re-align the donor DME and EWS with the Tool32 sequence in Q2. BMW says alignment can be repeated without limit.
- **If the donor is an SMG M3,** its EWS takes start permission from the gearbox side rather than a clutch pedal. Check `PARK/NEUTRAL_EINGANG` and the P/N status bits before assuming it will accept the Touring's clutch switch on EWS pin 8. The exact SMG coding wasn't found.
- **The Touring's VIN-specific data won't follow** a donor EWS: its VIN and the key transponder data stay the donor's. The I/M test reads the DME's VIN, not the EWS's (Q4), so this matters less for inspection than for future key ordering, which goes by the donor VIN.

### Gaps
- The correct `PARK/NEUTRAL_EINGANG` value for a US manual E46 (clutch switch to EWS pin 8) versus an SMG M3. Not documented.
- Whether `FGNR_SCHREIBEN` can rewrite the VIN in a used EWS3 (a forum member says an AK90 is needed). Not verified.
- How the GM5/ZKE remote (central locking from the key fob) behaves with a donor EWS, and how to add keys to an EWS3 without a dealer. No E46-specific source found.

## 4. Writing the Touring's VIN into the DME

### Takeaway
State I/M testers read the VIN stored in an E46 DME (BMW SI B12 09 13). Write the Touring's full 17-character VIN into the donor MSS54's next free AIF slot with Tool32 and `12MSS54.PRG`:
1. `AIF_LESEN` with arguments 1, 2, 3… to find the first empty slot.
2. `SEED_KEY`.
3. `AIF_SCHREIBEN` with an 11-field semicolon string.
4. Confirm in INPA ("MS S54 for S54 M3" → Coding).

Or tick Kassel's "VIN Recode to Your VIN" ($20).

### Cited Findings
- BMW SI B12 09 13 (Nov 2013), "State Inspection and Emission (I/M) Test Fails Due To an Invalid VIN Number", models "E46… Produced to 12/2006": "The VIN read out and displayed on the state test printout does not match the actual VIN of the vehicle… If the DME was reprogrammed using the previously available BMW service equipment (e.g., Progman, GT1), it is possible that only the last 7 digits of the VIN were entered into the DME… The state I/M tester or OBD scan tool may read out WBAAA00000A123456 instead of the correct full 17-digit VIN." Its fix is to reprogram with ISTA/P, and "Using ISTA/D, the VIN correction can be verified by viewing the DME identification page." (read) — [BMW SI B12 09 13 via NHTSA](https://static.nhtsa.gov/odi/tsbs/2013/MC-10150160-9999.pdf)
- "Having a DME VIN that differs from the chassis VIN might be a problem for emissions testing. California's emissions check reads the VIN from the OBD2 port and uses that in the report sent to the state." (read) — [e46fanatics 1253491, DBecker](https://www.e46fanatics.com/threads/chassis-vin-dme-ews-vin-lcm-ike-vin-all-mismatched-help.1253491/)
- A NAM3 moderator: "VIN is super easy with Tool32" (read). — [NAM3 2052, heinzboehmer, 04-15-2020](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)
- **ECUWorx Tool32 procedure** for E46 M3 and E39 M5 (read):
  1. "Load up Tool32 (ToolSet 32). Click 'File' > 'Load SGBD, Group File' and browse to the 'C:\Ediabas\ECU\12MSS54.PRG' file and click 'Open'."
  2. "In the 'Jobs' list double click 'aif_lesen'. The results window should return a 'Job_Status' of 'OKAY' and the first VIN programmed into the DME will be displayed along with other AIF data."
  3. "In the 'Arguments' box type '2' and double click 'aif_lesen' again… repeat the process of incrementing the number in the 'Arguments' box until you reach a number with a blank 'AIF_FG_NR' field. Make a note of the 'AIF_ADRESSE_LOW' number… In my case, slot '3' was free and had an 'AIF_ADRESSE_LOW' of '7596'."
  4. Build the string in this order: "AIF_ADRESS_LOW; VIN; Today Date; AIF_AENDERUNGS_INDEX; Software Number; Authority Number; Assembly Number; Serial Number; Handler Number; AIF Programmed KM; AIF Program Number". The example is `7596;WBSBL12345JR12345;260216;DA;7837331;7834533;7834530;NFS01;240;0;000401`. "The software number, authority number and assembly numbers should be labeled on the outside case of the DME, the fields after those are fairly unimportant."
  5. "Double click 'seed_key' and then paste your newly constructed string into the 'Arguments' box."
  6. "Double click 'aif_schreiben' and ensure the 'JOB_STATUS' returns 'OKAY'. If the status returns 'Error' or 'Rejected' double click 'seed_key' and retry ensuring you don't click anything other than 'aif_schreiben'."
  7. Verify: "load up INPA, select 'E46' or 'E39' then 'Engine' then 'MS S54 for S54 M3' then select 'Coding'."
  — [ECUWorx "Adding / Updating your VIN & AIF with Tool32"](https://www.ecuworx.co.uk/2016/02/26/adding-updating-your-vin-uif-with-tool32/)
- The SGBD definitions match (read):
  - `12MSS54.PRG` `AIF_LESEN` takes `AIF_NUMMER` ("Nummer des zu lesenden AIF's >=1. 0 bedeutet aktuelles AIF, auf das ein freies AIF folgt") and returns `AIF_ADRESSE_LOW`, `AIF_ANZ_FREI` (number of free AIF entries remaining), `AIF_FG_NR` and others.
  - `AIF_SCHREIBEN` takes `AIF_ADRESSE, AIF_FG_NR, AIF_DATUM, AIF_AENDERUNGS_INDEX, AIF_SW_NR, AIF_BEHOERDEN_NR, AIF_ZB_NR, AIF_SERIEN_NR, AIF_HAENDLER_NR, AIF_KM, AIF_PROG_NR`.
  - `SEED_KEY` is the "Schutzmechanismus SEED_KEY".
  - `MSS54DS0.PRG`'s `AIF_LESEN` takes no argument, and MSS54DS0 has no AIF write job.
  — [SGBD doc 12MSS54](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/12MSS54.md); [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- `MSS54DS0` `IDENT` returns `ID_AIF_VORHANDEN` ("Ist ein AIF vorhanden") along with `ID_BMW_NR`, `ID_HW_NR` and `ID_SW_NR` (read). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- Kassel option "VIN Recode to Your VIN", $20 (read). — [Kassel](https://www.kasselperformance.com/product/bmw-e46-m3-s54-mss54-hp-tuning/)
- WinKFP comfort mode starts with "'Enter VIN'. Enter your complete VIN" before "Choose ZUSB" and "Program". This is ECUWorx's SMG-gearbox flash guide; the same front end is used for any ZUSB flash (read). — [ECUWorx SMG ECU guide](https://www.ecuworx.co.uk/how-to/updating-the-smg-ecu-to-run-csl-255-software/)
- In California, an MSS54-swapped sedan "coded to the chassis VIN and reflected as a 330i" passed the plug-in test with "All my monitors show as ready except EVAP". The poster mentions California's July 2021 Cal ID and CVN rules (read). Note that passing as a 330i hides an uncertified engine change. — [e46fanatics "S54 swaps and smog in california *update*"](https://www.e46fanatics.com/threads/s54-swaps-and-smog-in-california-update.1303447/)

### Inferences
- **Assembled VIN procedure:**
  1. Battery on a charger, ignition at position 2, engine off.
  2. Tool32 → `12MSS54.PRG`.
  3. Run `AIF_LESEN` with argument 1, then 2, 3… Record every slot's VIN, SW, BEHOERDEN and ZB numbers, and note `AIF_ANZ_FREI` and the first slot with a blank `AIF_FG_NR`, plus its `AIF_ADRESSE_LOW`.
  4. Build the string using the SW, authority and assembly numbers **from the latest filled slot** rather than the label, so later WinKFP updates match. ECUWorx's example date "260216" for 26 Feb 2016 implies DDMMYY.
  5. Run `SEED_KEY`, then immediately `AIF_SCHREIBEN` with the string, and check `JOB_STATUS = OKAY`.
  6. Read back with `AIF_LESEN 0` and confirm in INPA → MS S54 → Coding.
  7. Confirm with a generic OBD-II scanner that shows the Mode 09 VIN, if it supports that.
- Write all **17 characters**. The TSB shows testers flag a VIN with default characters. AIF slots are finite (`AIF_ANZ_FREI`), so don't write repeatedly.
- **A WinKFP ZUSB flash with the Touring's VIN** entered in comfort mode should also store the VIN, since that is how BMW tools write it. Combine it with the manual-variant flash if one is needed (Q5).
- The EWS's VIN doesn't need changing for inspection. Keeping the Touring's EWS keeps its own VIN anyway.

### Gaps
- Whether the US MSS54 reports the VIN in OBD Mode 09 to generic scanners, and which AIF slot it reports. The TSB implies it does for E46s generally, but I found no MSS54-specific test.
- Whether NCS Expert can write the VIN to the MSS54. Not found, and the SGBD has no coding jobs, so probably not.
- Whether Cal ID and CVN checks would flag M3 software in a 325i Touring. That is a certification question; see the guide's legal section.

## 5. Manual-gearbox settings: clutch-switch input, SMG versus manual software, and cruise control

### Takeaway
MSS54 hardware is identical for SMG and manual cars, but the software isn't. BMW released separate US "HS" (manual) and "SMG" data sets. An SMG donor DME needs either a reflash to the HS variant (WinKFP ZUSB, or a vendor) or a binary "Transmission Swap" (ECUWorx), which also disables the SMG DTCs. On the MSS54 the clutch switch and gearbox gear switch form a "power transmission" chain that cuts cruise and enables idle control. Cruise requests come from the MFL over one FGR wire, so cruise needs no coding on standard M3 software (CSL software needs "Enable Cruise").

### Cited Findings
- "Is there any hardware difference in DMEs between coupe, vert MT vs SMG?" Answer: "Nope. Hardware differences are only related to year (HP vs non-HP). Firmware is different though." (read) — [NAM3 2052, heinzboehmer, 04-06-2020](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)
- The NAM3 software table, "auto-parsed from flash files taken from the ISTA CDs", lists separate US releases (read). Examples:
  - "7.842.981 23-Apr-2009 MSS54HP E46-M3-USA-HS LEV A7843302.0DA JD39" and "MSS54HP E46-M3-USA-SMG LEV A7843304.0DA JD79"
  - "7.842.979 13-Mar-2009 MSS54HP E46-M3-USA-HS LEV A7842980.0DA J469"
  - "7.842.973 13-Mar-2009 MSS54 E46 M3 US HS USOBD A7842974.0DA J469"
  - "7.834.752 16-Dec-2002 MSS54 E46 USOBD A7834753.0DA JDF) (12.12.02) Serie E46M3SMG-USOBD from Prod. 9/2002" versus "7.834.746 … A7834747.0DA J4G9 (10.12.02) Serie E46M3-USOBD from Prod. 9/2002"

  The same post lists "Convert DME from SMG to 6MT & vice versa (VERIFIED)" among community-verified modifications.
  — [NAM3 2052](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)
- ECUWorx MSS5x tool: "Transmission Swap: If you have a chassis swapped car or want to change your transmission then you can swap between SMG and Manual. If you swap from SMG to Manual, the DTCs for SMG parts will be disabled automatically." Also: "Enable Cruise control (CSL / CSL Clones Only): This option will allow CSL converted ECUs to activate cruise control." (read) — [ECUWorx feature rundown](https://www.ecuworx.co.uk/how-to/a-run-down-of-features-of-the-mss5x-binary-modification-tool-and-what-they-do/)
- ECUWorx FAQ: "I suggest doing a 'ZUSB update' with WinKFP to flash your vehicle back to stock" (read). — [ECUWorx How To / FAQs](https://www.ecuworx.co.uk/how-to-faqs/)
- WinKFP comfort-mode flow from ECUWorx's SMG gearbox guide (read):
  1. Import the E46 SP-Daten ("'Import/Export' > 'Assembly line data'") and copy the `ECU` and `sgdat`/`gdaten` folders as described.
  2. "Click 'Comfort mode' and then 'Enter VIN'… Now click 'Choose ZUSB', change the 'ECU family' to … and the 'ZB-Number' to …"
  3. With the battery on a charger in supply mode, key at position 2: "press 'Program'. WinKFP will prompt you to alert you of the number of flashes remaining".

  That guide flashes the SMG gearbox unit (family GDSMG2, ZB 7843255), not the DME.
  — [ECUWorx SMG ECU guide](https://www.ecuworx.co.uk/how-to/updating-the-smg-ecu-to-run-csl-255-software/)
- "Just use MSS Flasher to reset the flash counter" (read). — [NAM3 2052, R3Z3N](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information)
- SMG-specific DTCs exist in the MSS54 SGBD (read): "0x06 Timeout SMG-CAN", "0x11 SMG Schaltablauf", "0x44 SMG Sicherheitskonzept", "0x7B Bus-Off lokaler SMG-CAN", and an environment text "MIL-Anforderung durch SMG". — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- BMW, MS S54 "Power Transmission Switch": "The power transmission switch (circuit) consists of two switches in series. The circuit includes a clutch switch and a gear selector switch on the transmission. The functions of the power transmission switch are as follows: • Cutout for cruise control operation • Enable condition for idle control. The switches provide a high signal for the MS S54 when the clutch is disengaged and the transmission is in gear. If either the clutch is engaged or the transmission is in neutral, the cruise control will be disengaged." (read) — [BMW ST055 "8 MS S54", p. 84](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- BMW, cruise: "the MS S54 ECM takes over the function of cruise control… All driver requested cruise control function requests are provided to the MS S54 from the MFL II control module in the steering wheel over a single FGR data lead." (read) — [BMW ST055, p. 85](https://archive.org/download/BMWTechnicalTrainingDocuments/ST055%20Engine%20Electronics%20%28Archive%201%29/8%20MS%20S54.pdf)
- BMW EWS 3.3: "On manual transmission vehicles clutch status is input directly into the DME." (read) — [BMW ST051, p. 22](https://archive.org/download/BMWTechnicalTrainingDocuments/ST051%20Body%20Electronics%20I%20%28Archive%201%29/05%20EWS.pdf)
- MSS54DS0 `STATUS_DIGITAL` includes `STAT_KUP_EIN` "Status Kupplungsschalter", `STAT_KRAFTSCHLUSS_EIN` "Status Kraftschlussschalterkette", `STAT_BLS_EIN` (brake light switch), `STAT_BLTS_EIN` (brake light test switch) and `STAT_FDYN_EIN` (sport button). `STATUS_ADAPTIONSBLOCK_06` includes `STAT_FGR_MFL_VERBAUT_WERT` "Status Fahrgeschwindigkeitsregler" (cruise) and `STAT_EKP_CFG_VERBAUT_WERT` "welche EKP wurde verbaut" (read). — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- MSS54 DTC "0x50 Schalterkette Kraftschluss" (power-transmission switch chain) can carry the fault types "0x1D Kraftschluss im Stillstand" (drive engaged while stationary) and "0x1E Kein Kraftschluss bei Fahrt" (no drive engaged while moving). Cruise DTCs: "0x8B Tempomatsystem", "0xC2 Sicherheitsabschaltung FGR" (read). — [SGBD doc MSS54DS0 (FORTTEXTE, FARTMATRIX)](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- Rev hang, from an M54 (323Ci) auto-to-manual swap (read):
  - The rev hang ended after a different tune: "We suppose RK Tunes' automatic tune has some rev hang… So to anyone with an ECU tuned for an auto in a manual-swapped car, now you know!"
  - "the most common rev hang is from improper clutch switch wiring"
  - "There is no 'manual software'. MS42 software for manual and auto are the same."
  - Another owner's rev hang: "the Auto ECU was still left connected. Disconnected and removed ECU plus reset the adaptations".

  — [e46fanatics "Manual Swap Rev Hang"](https://www.e46fanatics.com/threads/manual-swap-rev-hang.1315205/)

### Inferences
- **For a manual donor DME:** keep its software. Just confirm the clutch/gear switch chain in INPA or Tool32: `STATUS_DIGITAL` → `STAT_KUP_EIN` toggles with the pedal, and `STAT_KRAFTSCHLUSS_EIN` = 1 only in gear with the clutch released.
- **For an SMG donor DME,** choose one:
  - (a) Vendor: Kassel "Engine Swap Coding", or ask DUDMD or RPM for "SMG to 6MT" along with the delete.
  - (b) DIY binary: ECUWorx "Transmission Swap: SMG → Manual" plus the EWS delete, in one BMWFlash read and reflash.
  - (c) WinKFP ZUSB flash to a US "HS" data set matching the hardware (MSS54 vs MSS54HP, production date). The correct ZB number wasn't found; get it from a vendor or the SP-Daten. Entering the Touring VIN in comfort mode also writes the VIN.

  Options (b) and (c) reset or alter the flash counter, which MSS Flasher can reset.
- **Leaving SMG software in a manual car** will likely log SMG-CAN timeout and bus-off DTCs ("0x06", "0x7B"), and possibly an SMG MIL request, because the TCU is missing. That makes an inspection fail likely. This is inferred from the SGBD DTC list; I found no first-hand report.
- **The M54 rev-hang lesson carries over partly.** Unlike the MS42/43, the MSS54 *does* have distinct manual and SMG software. So rev hang or odd idle on clutch-in with an SMG variant is plausible, and the first checks are the variant and clutch-switch wiring (the chain also enables idle control).
- **Cruise** needs the MFL's FGR wire reaching the MSS54 pin and a working power-transmission chain. On standard (non-CSL) M3 software no enable is needed. `STAT_FGR_MFL_VERBAUT_WERT` appears to be a learned flag, so clear adaptations after wiring (Q6).

### Gaps
- The exact US HS ZB numbers for each MSS54/MSS54HP hardware number. Whether the "J4xx" Stand codes are manual and "JDxx" SMG (a pattern in the NAM3 table) is inferred, not confirmed.
- The MSS54 pin for the FGR (cruise) wire and the clutch-switch pins. That is wiring, covered by other researchers; the guide cites X60002 pin 20 for the gear-switch chain.
- First-hand reports of SMG-software MSS54s running in manual cars, and their symptoms.

## 6. Adaptations and setup after first start: resetting, throttle (EDR) and idle, VANOS checks, rev hang, status screens

### Takeaway
Clear the MSS54's adaptations once the swap is wired, using Tool32 `MSS54DS0` → `ADAPT_LOESCHEN` (or INPA's adaptation menu). Then let the DME relearn:
- **Throttle:** a pre-drive check at every ignition-on, and a post-drive full-load learn 10 s after key-off on a cold engine.
- **Idle and fuel trims:** by idling and driving.
- **Crank-wheel segments** (needed for full misfire sensitivity): by coasting in gear with the throttle closed.

Verify everything in `STATUS_ADAPTIONSBLOCK_06` and run the SGBD's VANOS timing and leak tests.

### Cited Findings
- Tool32 jobs in `MSS54DS0.prg` (read):
  - `ADAPT_LOESCHEN` "alle Adaptionen gleichzeitig loeschen" (no arguments; returns `JOB_STATUS`)
  - `ADAPT_SELEKTIV_LOESCHEN` "Adaptionen bitweise loeschen und Zustaende bitweise setzen" (argument `STATUS_ADAPT`, int)
  - `FS_LESEN`, `FS_LOESCHEN`, and `SG_RESET` ("Adaptionen/FS nicht gesichert!")

  `12MSS54.PRG` also has `ADAPTION_LOESCHEN`.
  — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md); [SGBD doc 12MSS54](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/12MSS54.md)
- `STATUS_ADAPTIONSBLOCK_06` returns (read):
  - throttle and pedal: `STAT_PWG1_A0_WERT`, `STAT_PWG2_A0_WERT` (pedal sensor zero positions), `STAT_WDK1_A0_WERT`, `STAT_WDK2_A0_WERT` (throttle zero positions), `STAT_WDK_ADAPT_WERT` "Zustand Drosselklappenadaption mit 0 = ok", `STAT_WDK_MAX_DIFF_ADAPT_WERT`, `STAT_PWG_MAX_DIFF_ADAPT_WERT`
  - idle: `STAT_MD_LLRA_WERT` (idle controller adaptation torque), `STAT_LFRA_MD_START_WERT`
  - fuel trims: `STAT_LAA_F1/F2_WERT` (lambda adaptation factors), `STAT_LAA_OFFSET1/2_WERT`
  - crank wheel: `STAT_LU_ADAPT1…8_WERT` (segment deviation, ppm) and `STAT_LU_ADAP_CNT_WERT`
  - VANOS: `STAT_EVAN1_ADAP_WERT`, `STAT_AVAN1_ADAP_WERT`, `STAT_VAN_ADAP_ST_WERT` ("Bit0 = Einlaß-Vanos Bank 1 adaptiert Bit1 = Auslaß-Vanos Bank 1 adaptiert")
  - installed-equipment flags: `STAT_KKOS_ST_VERBAUT_WERT` (A/C detected), `STAT_FGR_MFL_VERBAUT_WERT` (cruise), `STAT_EKP_CFG_VERBAUT_WERT` (fuel pump type), `STAT_LDPH_VERBAUT_WERT` (DMTL heater fitted)

  Other status jobs: `STATUS_LFR` (idle controller adaptation), `STATUS_LAMBDA_ADD_1/2`, `STATUS_LAMBDA_MUL_1/2`, `STATUS_GEBERRAD_ADAPTION`, `STATUS_DKP_WINKEL` and `STATUS_DKP_WINKEL_SOLL`.
  — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- VANOS service jobs (read):
  - `STEUERN_EVANOS1_VERSTELLZEIT`, `STEUERN_AVANOS1_VERSTELLZEIT` and the bank-2 equivalents, "Verstellzeitmessung… anstossen", returning `EVAN_VERSTELLZEIT_FRUEH` and `EVAN_VERSTELLZEIT_SPAET` with units
  - `STEUERN_EVANOS1_DICHTHEIT` and its siblings, "Dichtheitmessung…", returning `EVAN_ISTWERT`, `EVAN_SOLLWERT`, `EVAN_STATUS`
  - `STEUERN_EVANOS1_FRUEHANSCHLAG` and `SPAETANSCHLAG` (move to the advance or retard stop)
  - `STEUERN_LLS_TESTDREHZAHL`, "feste Leerlaufanhebung fuer VANOS-Test" (fixed idle raise for the VANOS test)
  - `STEUERN_TI_ABGLEICH_STARTEN`, "Anstossen der automatischen Einzeldrosselklappenkorrektur (Prueflauf)" (starts the automatic individual-throttle correction test run)

  — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- BMW, pedal sensor: "The potentiometers/Hall sensors are non-adjustable because the ECM 'learns' the throttle angle voltage at idle speed. If the throttle housing/accelerator pedal module is replaced, the ADAPTATIONS MUST BE CLEARED and ADAPTATION PROCEDURE MUST BE PERFORMED using the DISplus/MoDIC. If this is not performed, the vehicle will not start, or run in 'fail-safe' mode." (read) — [BMW ST041 Engine Electronics Part 1, p. 15](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%201%29.pdf)
- BMW, pre-drive check (read):
  - "This check is conducted every time KL15 is activated. The full load adaptation stop is learned in a new ECM the first time KL15 is recognized."
  - Phase 1 closes the throttles; phase 2 opens them 3%; phase 3 opens about 20% and lets the springs close them, when "a mechanical clicking sound can be heard".
  - "Post Drive Check: 10 seconds after KL15 is switched 'OFF' the EDR actuator is opened 102% in order to carry out renewed full load adaptation. Adaptation during the post drive check is only carried out when the engine is turned off before reaching the operating temperature."

  — [BMW ST041 Part 1, p. 17](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%201%29.pdf)
- BMW, crank-wheel adaptation: "an internal adaptation of the flywheel is made. The adaptation is made during periods of decel fuel cut-off… If the sensor wheel adaptation has not been completed the misfire thresholds are limited to engine speed dependent values only and misfire detection is less sensitive." (read) — [BMW ST041 Engine Electronics Part 3, p. 69](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)
- BMW, fuel trims: the ECM adapts "During idle and low load mid range engine speeds (Additive Adaptation)" and "under a normal to higher load… (Multiplicative Adaptation)". "If the adaptation value is greater than '0.0 ms' the ECM is trying to richen the mixture." (read) — [BMW ST041 Part 3, p. 74](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)
- INPA paths seen only in snippets:
  - Schwaben tool for an E46 M3: "Control Units → Drive → Engine-DME Motor Electronics MSS54 → Clear adaption values → Clear Vanos Adaptation", F3 to clear (snippet; the page returned HTTP 429). — [ECS Tuning blog](https://blog.ecstuning.com/schwaben-bmw-scan-tool-e46-m3-clear-valve-adaptions)
  - An M52TU owner's advice: delete adaptations "with the ignition on and the engine off, then pressing the throttle to wide open four times" (snippet). — [zroadster](https://zroadster.org/threads/clearing-adaptations-with-inpa-after-m54-engine-swap.19500)
  - One owner "soft-bricked" a DME after clearing adaptations in INPA (snippet). — [z4-forum](https://z4-forum.com/threads/e85-manual-swap-trouble-solved.152760/)
- An M54 owner also mentioned a separate throttle relearn: "I haven't tried resetting the throttle yet with the 'hold pedal for 10 seconds' reset" (read; M54 context). — [e46fanatics 1315205](https://www.e46fanatics.com/threads/manual-swap-rev-hang.1315205/)
- The guide's existing VANOS reference is Beisan Systems' S54 VANOS procedure (not re-read here). — [Beisan](https://beisansystems.com/s54-vanos-procedure-e46-m3/)

### Inferences
- **Assembled first-start sequence** (BMW's described behaviour plus the SGBD jobs):
  1. Charger on. Ignition on, engine off. Tool32 `MSS54DS0` → `IDENT` and `FS_LESEN`, and save the results.
  2. `ADAPT_LOESCHEN`, then `FS_LOESCHEN`.
  3. Key off and wait at least 15 s so the post-drive check runs (the engine is cold). Key on and listen for the phase-3 throttle click of the pre-drive check.
  4. `STATUS_ADAPTIONSBLOCK_06` → expect `STAT_WDK_ADAPT_WERT = 0`.
  5. Start without touching the pedal and idle to operating temperature. Watch `STATUS_LFR`, `STATUS_LAMBDA_ADD_1/2` and `STATUS_N_LL_SOLL`.
  6. Run the VANOS jobs warm: `STEUERN_LLS_TESTDREHZAHL`, then the `…_VERSTELLZEIT` and `…_DICHTHEIT` jobs per bank, comparing the results with the SGBD status and Beisan's reference.
  7. Drive, including several closed-throttle coast-downs in gear from 3,000–5,000 rpm (decel fuel cut-off) to complete crank-wheel adaptation (`STAT_LU_ADAP_CNT_WERT` rising).
  8. Re-check `STAT_VAN_ADAP_ST_WERT` bits and the fuel trims.
- **Clearing adaptations after any wiring change** also makes the DME relearn its "verbaut" flags: EKP type, A/C, cruise and DMTL heater. That is relevant after fuel-pump or cruise wiring changes.
- **Rev hang on clutch-in:** check the clutch and gear switch chain (`STAT_KUP_EIN`, `STAT_KRAFTSCHLUSS_EIN`, DTC 0x50), then the SMG versus HS software variant (Q5), then any third-party tune, before blaming adaptations.

### Gaps
- The verified INPA "MS S54 for S54 M3" menu key for "delete adaptations" and its screen texts. Not found first-hand.
- The meanings of the `ADAPT_SELEKTIV_LOESCHEN` bits, and the specification values for the VANOS `VERSTELLZEIT` and `DICHTHEIT` results.
- Whether `ADAPT_LOESCHEN` also resets readiness. It almost certainly isn't the same as clearing faults, but this wasn't documented.

## 7. Emissions readiness: MSS54 monitors, a drive cycle that sets them, and checking before inspection

### Takeaway
BMW documents the MSS54's catalyst, O2-sensor, O2-heater, secondary-air, EVAP (DMTL leak test plus purge check), fuel-system and misfire monitors, with their enabling conditions. The hardest is the DMTL leak test. It runs only with the engine off after at least 20 minutes of driving that followed a cold soak of at least 5 hours, with fuel at 15–85%, ambient −7 to 35 °C, and 11.5–14.5 V, and only every second time those criteria are met (about once a day). EVAP is the monitor reported "not ready" on an MSS54 swap. A non-M body harness needs its DMTL pins moved for it to work at all. New York fails a MY2001+ car with more than one monitor not ready. Check with a generic OBD-II scanner, or Tool32's `STATUS_ADAPTIONSBLOCK_26` readiness mask.

### Cited Findings
- **Catalyst monitoring** (read): "Conditions for Catalyst Monitoring: Closed loop operation YES • Engine coolant temperature Operating Temp. • Vehicle road speed 3 - 50 MPH (5 to 80 km/h) • Catalyst temperature (calculated)* 350°C to 650°C • Throttle angle deviation Steady throttle • Engine speed deviation Steady/stable engine speed • Average lambda value deviation Steady/stable load… The catalyst efficiency is monitored once per trip while the vehicle is in closed loop operation." — [BMW ST041 Part 3, p. 75](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)
- **O2 heater monitoring** (read): "The heater function is monitored continuously while the vehicle is in closed loop operation… If the power of the heater is not within a specified range, a fault will be set." — [BMW ST041 Part 3, p. 76](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)
- **Secondary air** (read): "Immediately following a cold engine start (-10 to 40°C) fresh air/oxygen is injected directly into the exhaust stream… The single speed pump runs for approximately 90 seconds after engine start up… Secondary Air Injection Monitoring is performed by the ECM via the use of the pre-catalyst oxygen sensors… If the oxygen sensor signals do not change within a predefined time a fault will be set." — [BMW ST041 Part 3, p. 77](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)
- **EVAP leak test via DMTL** (read): the test runs with "Engine OFF with ignition switched OFF", the "ECM still in active state… 'follow up mode'", and these conditions:
  - "Prior to Engine/Ignition switch OFF condition, vehicle must have been driven for a minimum of 20 minutes"
  - "Prior to minimum 20 minute drive, the vehicle must have been OFF for a minimum of 5 hours"
  - "Fuel Tank Capacity must be between 15 and 85%"
  - "Ambient Air Temperature between -7OC & 35OC (20OF & 95OF)"
  - "Altitude < 2500m"
  - "Battery Voltage between 11.5 and 14.5 Volts"

  "When these criteria are satisfied every second time, the ECM will start the Fuel System Leak Diagnosis Test. The test will typically be carried out once a day." "The time duration varies between 45 & 270 seconds." The DMTL detects "leaks as small as 1.0 mm (.040")".
  — [BMW ST041 Part 3, pp. 64–72](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)
- **Purge** (read): "The 'purging' process takes place when: Oxygen Sensor Control is active • Engine Coolant Temperature is >60º C • Engine Load is present." The flow check looks for a rich or lean shift; failing that, "a second step is performed when the vehicle is stationary and the engine is at idle speed". — [BMW ST041 Part 3, p. 73](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)
- **Misfire** (read): counted over 1,000-revolution (emissions) and 200-revolution (catalyst damage) windows. Crank-wheel adaptation during decel fuel cut-off is needed for full sensitivity (see Q6). — [BMW ST041 Part 3, pp. 69, 78](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)
- **New York rules** (read): "Since the three continuous monitors are constantly evaluating, they will be reported as Ready all of the time… New York has adopted the federal Environmental Protection Agency (EPA) guidance concerning readiness during OBD II inspections… model year 2001 and newer vehicles will fail when more than 1 monitor is reported as Not Ready." Readiness resets on "Disconnecting the battery" and "Erasing stored codes with a scan tool". "Removing the catalyst converter… is emissions tampering and is illegal for street-driven vehicles." — [NYVIP3 Ready vs Not Ready](https://www.nyvip3.com/OBDII/ReadyVSNotReady)
- **NYVIP3 universal drive cycle** (read):
  1. "The universal OBD-II drive cycle begins with a cold start (coolant temperature below 122 F, and the coolant and air temperature sensors within 11 degrees of one another)… The ignition key must not be left on prior to the cold start."
  2. "idle the engine in drive for two and half minutes, with the A/C and rear defroster on"
  3. "accelerate to 55 mph under moderate, constant acceleration. Hold at a steady speed for three minutes."
  4. "Decelerate (coast down) to 20 mph without braking or depressing the clutch"
  5. "Accelerate back to 55-60 mph at 3/4 throttle. Hold at a steady speed for five minutes."
  6. "Decelerate (coast down) to a stop without braking."

  The tips page adds: make sure "the check engine light is not commanded on", and "Some monitors, for instance the EVAP monitor, may require the fuel level to be between 35% and 85%".
  — [NYVIP3 Universal Drive Cycle](https://www.nyvip3.com/OBDII/UniversalDriveCycle); [NYVIP3 Helping set Monitors](https://www.nyvip3.com/OBDII/HelpingSetMonitors)
- **Readiness in Tool32** (read): `MSS54DS0` → `STATUS_ADAPTIONSBLOCK_26` returns `STAT_FF_FF_RDY_WERT` "Readinessmaske", `STAT_FF_FF_DCY_CNT_WERT` "Anzahl Driving-Cycles seit Ruecksetzen", `STAT_FF_FF_WUC_CNT_WERT` (warm-up cycles), `STAT_FF_FF_DCY_CLR_WERT` (driving cycles since fault memory cleared), and `STAT_FF_FF_RDY_CNT0…15_WERT` "Anzahl Readiness erreicht fuer Diagnostic Function n". — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- **Service function tests in the same SGBD** (read):
  - secondary air: `START_SYSTEMCHECK_SEK_LUFT` then `LESEN_SYSTEMCHECK_SEK_LUFT` (status value and text), and `STEUERN_SLS_CHECK`
  - leak pump: `START_SYSTEMCHECK_DMTL` then `LESEN_SYSTEMCHECK_DMTL`, and `STATUS_TANK_DICHTHEIT`
  - purge valve: `STEUERN_TEV_CHECK` (returns `TEV_STATUS`)
  - actuators: `STEUERN_SLP`, `STEUERN_SLV`, `STEUERN_LSHV1/2`, `STEUERN_LSHN1/2` (O2 heaters)
  - status tables `SLSSTATUS`, `LDPSTATUS`, `TEVSTATUS`

  — [SGBD doc MSS54DS0](https://github.com/emdzej/ediabasx-docs-sgbd/blob/main/docs/sgbd/MSS54DS0.md)
- **Swap evidence** (read): an MSS54-swapped E46 sedan had "All my monitors show as ready except EVAP. No CEL." — [e46fanatics 1303447](https://www.e46fanatics.com/threads/s54-swaps-and-smog-in-california-update.1303447/)
- **DMTL wiring in a non-M body harness** (read): "WDS for MSS54 and MS45 show I need to change the 330i body harness for X60004 connector and move pin 2 to 18 for DMTLH as the other 2 DMTL's are already at pins 20 and 30." Later: "no PINS need to be changed on X60003 harness… Just need to swap the DMTL plugs on X60004 plug to get charcoal canister to work." A reply: "pin 2 on my 325i is empty." That car's EVAP had been "coded out" by a previous owner. — [e46fanatics "E46 S54 sedan swap, EVAP pin outs"](https://www.e46fanatics.com/threads/e46-s54-sedan-swap-evap-pin-outs.1291729/)
- The guide's claim that "lazy pre-cat O2 sensors can stop the secondary-air monitor completing" comes from a thread I couldn't open (HTTP 406), so it remains unverified. BMW's description, that SAI is judged by the pre-cat O2 sensors' lean shift within a set time, is consistent with it (read). — [e46fanatics "E46 emission readiness monitor issues"](https://www.e46fanatics.com/threads/e46-emission-readiness-monitor-issues.1244521/); [BMW ST041 Part 3, p. 77](https://archive.org/download/BMWTechnicalTrainingDocuments/ST041%20M3%20Complete%20Vehicle/3%20EngineElectronics%20%28Part%203%29.pdf)
- **Emissions deletes exist but must not be used on a road car** (read):
  - ECUWorx lists "Disable SAP / Cat Heating Sequence", "Disable Cat Efficiency DTCs" and "Disable Rear O2 DTCs".
  - Kassel lists "SAP Delete" ($20) and "Disable Post Cat O2 Sensors" ($20).
  - Hack Engineering lists secondary-air and secondary-lambda removal coding.
  - NAM3 lists "Post-Cat O2 SES delete" and "Secondary Air Pump delete".

  All of these are illegal on a road car.
  — [ECUWorx](https://www.ecuworx.co.uk/how-to/a-run-down-of-features-of-the-mss5x-binary-modification-tool-and-what-they-do/); [Kassel](https://www.kasselperformance.com/product/bmw-e46-m3-s54-mss54-hp-tuning/); [Hack Engineering](https://www.hackengineering.co.uk/?p=49060); [NAM3 2052](https://nam3forum.com/forums/forum/special-interests/coding-tuning/2052-comprehensive-mss54-mss54hp-dme-information); [NYVIP3](https://www.nyvip3.com/OBDII/ReadyVSNotReady)

### Inferences
- **An MSS54-specific readiness plan** (merges BMW's enabling conditions with NYVIP3's cycle; not a BMW-published drive cycle):
  0. **Before you start:**
     - Fix every DTC and make sure the MIL is off. A leftover 130 (0x82) is a question mark (Q1 gap).
     - Fuel between 1/4 and 3/4 (35–85% satisfies both sources).
     - Battery healthy (11.5–14.5 V).
     - Confirm the hardware with the SGBD tests while parked: `STEUERN_SLS_CHECK` or `START/LESEN_SYSTEMCHECK_SEK_LUFT`, `START/LESEN_SYSTEMCHECK_DMTL`, `STEUERN_TEV_CHECK`.
  1. **Evening:** park and leave the car at least 5 h (overnight). Don't switch the ignition on.
  2. **Morning cold start** between 14 and 104 °F (−10 to 40 °C) for secondary air. Let it idle about 2.5 min so the roughly 90 s pump run and the O2 check complete.
  3. **Drive at least 20 minutes:**
     - steady 30–50 mph stretches for the catalyst monitor (it only runs between 3 and 50 mph, closed loop, steady throttle)
     - 55 mph steady segments per NYVIP3
     - several in-gear coast-downs without the clutch for decel fuel cut-off (misfire crank-wheel adaptation)
     - some warm idle for the purge check
  4. **Park, switch off, and leave it alone for at least 5 minutes** so the DMTL test can run in follow-up mode (45–270 s; you may hear the pump). Don't lock-and-unlock or restart during this time.
  5. **Repeat steps 1–4 the next day.** The DMTL runs only every second time its criteria are met.
  6. **Check readiness** with a generic OBD-II scanner (Mode 01 monitor status) or Tool32 `STATUS_ADAPTIONSBLOCK_26` (readiness mask and per-function counters). Go for inspection only when no more than one monitor is not ready (NY, MY2001+), and ideally none.
- **If EVAP never completes:**
  - check the DMTL (leak pump), its heater and change-over-valve wiring to the MSS54 (X60004 pin moves in a non-M harness), and its hoses and filler cap
  - check that `STAT_LDPH_VERBAUT_WERT` shows the heater detected after an adaptation reset
  - the ambient-temperature window (−7 to 35 °C) means winter or summer testing can stall it
- **If secondary air never completes,** check the pump relay and valve with `STEUERN_SLP`/`STEUERN_SLV`, the pre-cat O2 response, and that the cold-start temperature is inside −10 to 40 °C.
- **Don't clear codes or disconnect the battery within the weeks before the test.** Both reset readiness (NYVIP3).

### Gaps
- BMW's official E46 M3 OBD drive cycle (from TIS/ISTA). Not found online; the plan above is assembled from BMW's enabling conditions.
- Which monitors the US MSS54 reports as supported in Mode 01 (count and list). No source found.
- Whether the SGBD system-check jobs mark a monitor "ready" or only test the hardware.
- The content of the e46fanatics readiness thread (HTTP 406 every time; the Wayback Machine was unreachable from this environment).
- The 8-page billswebspace S54 training PDF the guide cites is a mechanical excerpt. It has no monitor content, so all monitor facts here come from ST041 Part 3.
