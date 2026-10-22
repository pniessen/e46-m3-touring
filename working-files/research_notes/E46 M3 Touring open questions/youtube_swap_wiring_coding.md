# YouTube evidence: S54 swaps into non-M E46s, and E46 M3 electronics (wiring, EWS, cluster, DSC, steering angle, coding)

Method, 22 Oct 2026: video metadata (title, channel, upload date, description, chapters) and English captions were pulled with yt-dlp (`--skip-download`, captions and info JSON only, no media). Captions are YouTube's auto-generated track unless marked "creator subtitles"; one French video was read through YouTube's auto-translation. Chapter lists that don't appear in a video's description are probably YouTube's auto-generated "key moments". Every citation gives the source as [captions], [chapters], [description] or [title only]. YouTube rate-limited the session (HTTP 429 on the subtitle endpoint, and several "confirm you're not a bot" checks). I didn't try to get around these: affected videos were retried once at a slower pace, then read from their description only, or listed under Gaps. Quotes are kept short. Where a video shows emissions-equipment removal or odometer changes, I note only that it exists. Upload dates are YYYY-MM-DD.

## Q1. Which videos show S54 swaps into non-M E46s with useful wiring or first-start detail?

### Takeaway
Six E46 swap series show wiring or first-start detail on camera:
- **Tenza Motorsports:** a 2004 US Touring that started as an M56 SULEV car, the closest match to this project. It used a Kassel EWS-delete DME and a Kassel-programmed cluster.
- **ShopLifeTV:** a 2001 330i converted from automatic. Its first start was blocked by the EWS clutch/park-neutral input.
- **M3projekts:** a Euro 318d Touring wired by a specialist.
- **M346 Projects:** a base automatic Touring receiving an M3 SMG driveline and the M3 body harness's switch-centre wiring.
- **Import Modify:** a 328Ci race car. It applies Kassel's MS42 column on camera and runs into the EWS starter interlock.
- **ThaChileanDude:** a Touring converted to manual. The clutch switch was wired to the EWS; an ABS light, the tamper dot and a check-engine light stayed on afterwards.

UNRIVALED's sedan video is advice rather than a build log. It covers an SMG-donor DME left in limp mode after a shop's "coding", the S54's second auxiliary water pump wiring, and the coolant-level sensor extension.

No video films the MS43/MS45-to-MSS54 cluster-lamp, brake-switch, DM-TL-heater or clutch moves that the written harness notes list. DBO's 330Ci and Project BMW's 325i Touring show mechanical work only, and DBO's car had a complete M3 body harness fitted rather than re-pinned connectors. BackyardWrenchin's series ends before any wiring.

### Cited Findings

#### Inventory (all read 22 Oct 2026)

| Channel and series | Base car | Engine management and immobiliser route | Electrical content on camera | First start on camera |
|---|---|---|---|---|
| Tenza Motorsports, "S54 wagon" (2021; 2025 follow-up) | 2004 US E46 Touring, originally M56B25 SULEV; S54 + 6-speed from a donor M3 | Kassel Performance DME (EWS delete, tune, VIN) and Kassel-programmed M3 cluster | Sport button, switch-panel power, wheel-speed sensors, E-box fan plug, M56 fuel-tank connector | Yes |
| ShopLifeTV, "S54 swap sedan" (2015–16) | 2001 330i sedan, automatic → 6-speed | Donor's matched DME/EWS/key/tumbler/cluster; EWS recoded with NCS Expert | Clutch-switch/EWS start interlock, coolant-level sensor extension, reverse light | Yes |
| M3projekts, "E46 M3 Touring build" (2023, Hungarian with creator subtitles) | Euro E46 318d Touring (M47 diesel) | Not stated; started before coding | Harness-planning list; specialist's view of which harness section must change | Yes |
| M346 Projects, "E46 M3 SMG Touring Build" (2023–24) | Base-model E46 Touring, automatic | Donor 2003.5 M3 convertible SMG; whole M3 body harness harvested | Switch centre, PDC and SMG wiring extracted from the M3 body harness | Yes (Pt 13, 2024) |
| Import Modify, "E46 S54 Swap/Build" (2018) | 328Ci race car (MS42, cable throttle) | eBay vendor's EWS-delete DME | Kassel MS42 X60004 moves; E-box connector mismatch; EWS starter jumper | Yes |
| DBO, "Full M3 Swap Into A 330ci!" (2019–21) | 2001 330Ci, manual | Complete M3 body harness fitted before filming | DM-TL module plug only | Only "it runs" (2021) |
| ThaChileanDude, "Building an e46 m3 Wagon in 10 days !!" (2024) | E46 Touring (original engine not stated), converted to manual with M3 pedals | M3 DME ("it is tuned"); no EWS work mentioned; clutch switch wired to the EWS | Clutch-switch wiring to the EWS and brake-pedal switch | Yes; ABS light, tamper dot and CEL left on |
| UNRIVALED, "WATCH THIS BEFORE YOU S54 SWAP YOUR BMW" (2021) | E46 sedan; S54 from an SMG car, converted to manual | SMG-donor DME "coded" by a local shop, still in limp mode | Coolant-level sensor extension; second auxiliary water pump; Sport button (talked about, not shown) | No (car finished but not running reliably) |
| Project BMW, S54 E46 Touring (2021) | E46 325i Touring (M54) | Not shown | None shown | Result only |
| BackyardWrenchin, "E46 S54 SWAP" parts 1–4 (2017) | 1999 328i sedan (MS42) | MSS54 from a 2003 M3 SMG | SMG-to-manual harness strip | No; series ends at part 4 |

#### Tenza Motorsports (US 2004 Touring, ex-M56 SULEV)
- The car is described as "our 2004 s54 swapped six-speed manual e46 wagon" — [Tenza Motorsports – Building an E46 M3 wagon is far more complicated than previously thought (2021-10-20), 00:03](https://www.youtube.com/watch?v=O63Y52j-4PY&t=3s) [captions]. The build started as "Saying goodbye to the M56B25" — [Tenza Motorsports – Project S54 wagon has officially started! (title)](https://www.youtube.com/watch?v=Jsk-8VLRFKc) [title only].
- **What Kassel's flash and cluster did, as Tenza describes them:**
  - EWS: the DME "can take any signal and it'll start", i.e. an EWS delete.
  - A performance tune; the Sport button "will still work".
  - The M3 cluster's mileage was changed "to reflect the mileage of the actual wagon, the chassis mileage".
  - The RPM (warm-up and shift) lights work.
  — [Tenza Motorsports – M3 touring build finally runs! - Kassel performance M3 tune (2021-04-25), 01:52–02:44](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=112s) [captions]
- **First start:**
  - The first attempt failed on a flat battery — [same video, 03:55](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=235s) [captions].
  - Next day it ran. The check-engine and oil lights went out after about 10–15 s. Other lamps (airbag/seat belt with the seat out, washer fluid, headlights) were expected — [same video, 05:38](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=338s) [captions].
  - "All the VINs match. All of the mileage matches." The Sport button worked but its LED did not ("this is on me") — [same video, 06:28](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=388s) [captions].
- **Pin moves and instructions:**
  - "there's really not much of that", which he credits to Kassel's software — [same video, 06:53](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=413s) [captions].
  - Kassel sent written instructions telling him to "move pins around". He only understood them after tracing the circuits on the donor M3: "If I didn't have this donor car here… I'd have gotten hung up" — [same video, 08:36–09:27](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=516s) [captions].
- **ABS light after first start.** "the body side is non-M, but the hubs are M", so non-M wheel-speed sensors sat in M3 hubs. His fallback was to splice in the donor's M3 sensor pigtails — [same video, 07:18–07:44](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=438s) [captions].
- **"5 things they don't tell you" part 2** — [Tenza Motorsports – 5 things they DON'T tell you about S54 swaps (part 2) (2021-07-19)](https://www.youtube.com/watch?v=mDBiRn30fEs) [chapters: 01:05 washer tank, 02:05 ECU fan plug, 03:15 wheel speed sensors, 05:32 Kassel tuning, 08:45 sport button wiring]:
  - **E-box fan plug (02:05–03:05):**
    - The M3 engine harness carries a male plug for the E-box fan. On the M3 one half comes from the engine harness and one from the body.
    - On the wagon "the plug is already filled" from the body side, so the M3 engine-harness plug was "just left disconnected".
    - [02:05](https://www.youtube.com/watch?v=mDBiRn30fEs&t=125s) [captions]
  - **Wheel-speed sensors (03:15–05:15):**
    - The M3 and non-M sensors' body-side connectors "are different, they will not plug into each other" ("only two wires").
    - He fitted non-M sensors into the M3 hubs and had driven only about 0.3–0.4 mile.
    - His warning: wrong sensors "will cause your traction control to be weird… ABS to go nuts… affect your speedometer".
    - [03:15](https://www.youtube.com/watch?v=mDBiRn30fEs&t=195s), [05:15](https://www.youtube.com/watch?v=mDBiRn30fEs&t=315s) [captions]
  - **What Kassel asked for (05:42–06:33):**
    - Inputs: the car's mileage, tune or no tune, which buttons are in the centre switch panel, the year, and wagon vs sedan.
    - Kassel also "physically pull[s] apart" the cluster "so that they can add rear door lights".
    - Budget: "plan for around a thousand dollars", including shipping and options.
    - [05:42](https://www.youtube.com/watch?v=mDBiRn30fEs&t=342s), [06:07](https://www.youtube.com/watch?v=mDBiRn30fEs&t=367s) [captions]
  - **Sport button (08:45–11:13):**
    - The wagon had only a DSC button. The single plug shared by both cars has four wires.
    - "17 and 18" on the M3 switch-panel plug run "out to the ECU box which is 6004" pins 15 and 16 ("15 and 17 and 16 and 18").
    - Switch-panel power: constants "red with the purple stripe" and "white with the red stripe"; "purple with the blue" is accessory.
    - Things worked only intermittently until he fed all of them from a constant 12 V spliced at the cigarette lighter.
    - Result: DSC, Sport and the Sport LED work; the speaker (Hi-Fi) button lights but does nothing; TPMS doesn't work.
    - [08:45](https://www.youtube.com/watch?v=mDBiRn30fEs&t=525s), [09:31](https://www.youtube.com/watch?v=mDBiRn30fEs&t=571s), [10:22](https://www.youtube.com/watch?v=mDBiRn30fEs&t=622s) [captions]
- **M56 SULEV fuel tank (legal flag).** The video swaps the M56 SULEV car's sealed tank and evaporative parts for an M54/S54-type tank and the M3 charcoal canister ("the tank used in the s54b32 M3 is the same tank used in all M54Bxx models") — [Tenza Motorsports – No more SULEV! … S54 wagon build (pt16) (2021-05-09)](https://www.youtube.com/watch?v=PgW1oWs7cfk) [description; chapters 02:46 charcoal canister, 07:29 wiring, 09:35 final setup]. Electrical points only:
  - The M56 tank has one plug with six wires. The normal tank has two plugs: four wires on the pump side (heavy power and ground plus a small pair for one level sender) and two on the other side.
  - The small pairs are identified by yellow-dot (passenger side) and white-dot (driver side) wires. He extended the driver-side pair.
  - [07:17–08:49](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=437s) [captions]
  - "the car runs". He was unsure about "that second fuel line" because "I don't necessarily know exactly how the m56 works" — [10:23](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=623s), [11:24](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=684s) [captions].
  - Whether replacing a SULEV car's certified evaporative system is legal is for the guide's legal section; I haven't documented the hose work.
- **Cost context (no Kassel price in this video):**
  - Both cars cost $8,700: a $6,500 M3 donor (plus $1,000 to collect it) and a $2,200 wagon — [Tenza Motorsports – S54 swap costs-What you should expect to pay building an s54 wagon (2021-11-25), 02:05](https://www.youtube.com/watch?v=urkCbJGGPhs&t=125s).
  - "a bare minimum… I would expect to spend 15 000" once mounts, bearings, bushings and fluids are included — [04:38](https://www.youtube.com/watch?v=urkCbJGGPhs&t=278s) [captions].
  - The Kassel/coding budget of about $1,000 comes from the "5 things" part 2 video above.

#### ShopLifeTV (2001 330i sedan, automatic → S54 6-speed)
- **Background:**
  - The first swap went into a 2002 330i 5-speed about a year earlier — [ShopLifeTV – Introduction: My BMW E46 S54 Build (2015-04-13), 00:35](https://www.youtube.com/watch?v=-LxxIZKRE_A&t=35s) [captions].
  - The description links the creator's write-up of that first swap: tinyurl.com/s54swap, which resolves to e46fanatics showthread.php?t=1027628 (not read) [description].
- **Parts video, description:** "Matching set of DME/EWS/Key/Ignition Tumbler/Guage Cluster", "MK60 DSC (Recommended)", "Code DSC from Auto to Manual using NCS Expert", "Realign LCM and DSC using INPA and NCS Expert", "add a few wires or move them around in the DME connectors" — [ShopLifeTV – What Parts Are Needed For S54 Engine Swap (2016-02-11)](https://www.youtube.com/watch?v=hnaZqKbvwT4) [description].
- **Parts video, captions:**
  - With the matching set "you don't have to worry about doing any code at first" — [01:51](https://www.youtube.com/watch?v=hnaZqKbvwT4&t=111s).
  - "realign the LCM… get the VIN numbers to match up in the mileage" — [03:14](https://www.youtube.com/watch?v=hnaZqKbvwT4&t=194s).
  - The MK60 is "for the most part plug-and-play" — [03:35](https://www.youtube.com/watch?v=hnaZqKbvwT4&t=215s).
  - Keeping the old cluster takes "a little bit more coding and some moving around wires", and wires must be added "for extra stuff like the sport button". He promised a separate wiring video — [04:15](https://www.youtube.com/watch?v=hnaZqKbvwT4&t=255s) [captions].
  - That video was never posted: his channel's 299 uploads, listed 22 Oct 2026, contain no S54 wiring episode.
- **Teardown:** he reused the manual pedal box from his first swap car and expected to "run one [wire] for the clutch switch" — [ShopLifeTV – Taking Out EVERYTHING! BMW S54 Swap Sedan- Part 1 (2015-06-22), 02:19](https://www.youtube.com/watch?v=xGmzbehhNrU&t=139s) [captions].
- **First start** — [ShopLifeTV – STARTING THE S54 SWAP CAR ON FOR THE FIRST TIME! (2015-08-19)](https://www.youtube.com/watch?v=BV1yvGP7sCM) [chapters: 01:05 clutch switch coding, 05:41 first engine start]:
  - The car wouldn't start. He had done "the clutch switch wiring… twice and still" no start, suspected "the brake wires", and had cut some harness wires by accident while removing the carpet — [00:38](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=38s) [captions].
  - Cause, in his words: "EWS checks if the clutch is… engaged… that's what was holding it back from starting". He recoded the EWS (procedure in Q2) — [01:08](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=68s) [captions].
  - It started; the dash lit up "like a Christmas tree" — [05:45–06:31](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=345s) [captions].
  - Other wiring needed (07:34–08:05):
    - The coolant-level sensor lead had to be extended because the expansion tank moves to the passenger side; temporarily taped.
    - Reverse lights, because the automatic car "had a separate way to set the reverse light".
    - The clutch switch still had to be made to work for cruise control.
    - [07:34](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=454s), [08:05](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=485s) [captions]
- **Seven years later:** "the check engine light is on and the traction control light came on" — [ShopLifeTV – Time to move on. The End Of The E46 S54 Swapped Sedan. (2022-05-29), 05:19](https://www.youtube.com/watch?v=WAiAHoTgfYw&t=319s) [captions; the video also has creator subtitles].

#### M3projekts (Euro 318d Touring → S54; wiring by "Imi", @dmxpowa)
- Options planned in the description: heated seats, four power windows, sunroof, power-folding M3 mirrors, PDC, rain/light sensor, xenons, roof rails — [M3projekts – BMW E46 M3 TOURING BUILD | Ep6 | S54 and body wiring (2023-09-25)](https://www.youtube.com/watch?v=YfJyE9DU5OE) [description].
- **Planning list (creator subtitles):**
  - No speed-sensor extension was needed, because the M3 MK60 uses "the same connector" as the car's ABS block: "only the number of the ABS block is different" — [01:43](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=103s).
  - The ignition switch stays because the car goes manual to manual — [02:13](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=133s).
  - "since the car is German so there is no need to delete the DMTL either" (a Euro car has no DM-TL) — [02:48](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=168s).
  - The expansion-tank level sensor moves from the left side to the right; the circulation (auxiliary water) pump "has both connectors" — [03:22](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=202s).
  - "Body harness M3 upgrade" and then "the remaining is coding" — [03:53](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=233s).
- **Specialist's rule for the engine-bay part of the body harness:** "It is good from any 6-cylinder… you have to add the wires for the Sport button - if not M3". A section from an M52 car would also lack the electronic-pedal wiring — [08:35](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=515s) [creator subtitles]
- **Other wiring steps:**
  - Expansion-tank and secondary-air-pump wires taken from a spare harness (an addition, since the diesel had no secondary air) — [05:24](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=324s).
  - The radiator-outlet temperature sensor wire may need extending — [07:31](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=451s).
  - The interior harness was "converted… from four to six cylinders" and the Sport button added — [09:38–10:10](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=578s).
  - The secondary-air relay was connected — [10:42](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=642s).
- **First start:** "only the coding is remaining and then we can start" — [17:02](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=1022s). The engine started after a few cranks, run briefly with no coolant and the belts off — [17:32–19:16](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=1052s) [creator subtitles].

#### M346 Projects (base automatic E46 Touring → M3 SMG; donor 2003.5 M3 convertible SMG)
- **Approach:** "go through all the connectors and pull exactly what I need… compare that to the tis" — [M346 Projects – E46 M3 SMG Touring Build Part 2 M3 wiring harness dissection (2023-07-30), 01:37](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=97s) [captions; chapters 02:25 body harness, 06:50 wiring diagram, 18:05 wagon wiring].
- **SMG wiring:** he de-pinned the SMG-related wires from the M3 body harness into one custom harness ending at the SMG connector in the DME box — [08:26](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=506s).
  - The Touring's automatic-gearbox fuse feeds can probably be re-pinned for the SMG unit: "blue connectors but they're the same size" — [08:56–09:26](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=536s).
  - The DSC, yaw sensor and SMG share data "on the can bus" rather than dedicated wires — [09:56](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=596s) [captions].
- **PDC:** BMW built separate body-harness versions for cars with and without PDC — [11:30](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=690s). PDC is fuse 24 — [16:37](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=997s) [captions].
- **Switch centre on a base Touring:**
  - The wagon "doesn't even have a main switch Center panel… only has one button for DSC" — [18:05–18:38](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=1085s).
  - "in those cars there's no wiring to the K bus for the switch panel or the fuse box" — [20:45](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=1245s).
  - The M3 switch-panel plug carries a red/purple feed routed to the fuse box, green/yellow and green/purple seat-heater wires, K-bus, a seat-heater temperature signal, and seat-heater grounds to the sill grounding blocks — [19:14–19:45](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=1154s).
  - "the tricky ones were getting the wiring going to the DME connector and to the DSC connector" — [22:49](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=1369s) [captions].
- **First start** — [M346 Projects – e46 M3 SMG Touring build Pt 13 Engine Start! (2024-06-04)](https://www.youtube.com/watch?v=4Q3PxGuJyxI) [captions]:
  - **Expansion tank:** the M3 expansion-tank brackets for the Touring came "from Atilla over in Hungary". They are made to be welded; he fitted them with rivnuts so they can be removed — [00:05–00:35](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=5s).
  - **Before cranking:** "SMG system… was working and functioning, DME is all connected" — [00:35](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=35s).
  - **Oil priming:** he cranked to prime oil, then "put the fuel pump fuse in" before the start attempt — [03:27–04:35](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=207s).
  - **First attempt:** a fuel-pressure-regulator leak. A replacement regulator fixed it ("I think the O-rings were bad") — [05:57](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=357s).
  - **Running:** choppy at first after the VANOS refresh, then settles — [07:32](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=452s).

#### Import Modify (328Ci race car, MS42 → MSS54)
- **Base car:** "this is for the 328CI chassis" — [Import Modify – Ep.36 S54 Swap! Transmission & Wiring (part 10) (2018-09-14), 12:51](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=771s) [captions; chapters 10:21 brake system and wiring, 14:09 electronic throttle wiring].
- **E-box connector mismatch:** the manual names the two plugs "X60541, and the other is X60531… that one is 3-pin. This is a 4-pin. So, I'm missing a wire" — [01:05–01:35](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=65s) [captions].
- **Kassel's chart applied:**
  - He followed "this nice article from Kessle Performance" for X60004, after releasing the connector's two end latches; the pin numbers are on the bottom — [13:57–14:27](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=837s).
  - "I moved pin 28 to pin 30… And then moved pin 30 to pin 20", removed pin 1 (blue) and pin 2 and heat-shrank them, then added the e-pedal wires — [15:28](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=928s).
  - The new circuits used terminals salvaged from another engine harness, soldered to the pedal pigtail. Pin 9 was purple — [15:58–19:41](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=958s).
  - The pedal loom was rerouted through the existing bulkhead gap so the DME box could stay sealed — [20:43](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=1243s) [captions].
- **Other wiring:** the coolant-level sensor "needs to be rewired somewhere" — [13:22](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=802s) [captions]. He also blanked the secondary-air pump; noted only — [03:06](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=186s).
- **First start** — [Import Modify – Ep.41 S54 Swap, First Start! (part 15) (2018-10-08)](https://www.youtube.com/watch?v=gSeB5NYZ8qc) [captions]:
  - The DME came from an eBay vendor with EWS deleted and Sport defaulted; the same flash also removed emissions-related functions, which I haven't documented — [01:49–02:19](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=109s).
  - First attempt: no crank, no fuel-pump prime, and the coolant gauge "all the way tagged out" — [11:20](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=680s).
  - The vendor told him that with this delete "you still have to have the EWS matching the key", otherwise jumper the EWS starter circuit — [11:50–12:53](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=710s).
  - His home-made jumper was first on the wrong pair of terminals; once corrected the engine cranked, and it started after the battery was charged — [14:24–15:25](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=864s). I have deliberately not recorded which terminals, since this bypasses an immobiliser.
  - Throttle wiring works and the alternator charges — [16:37](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=997s), [17:40](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=1060s) [captions].

#### DBO (2001 330Ci, full M3 body harness)
- **Approach:** a shop owner (Eurogarage303) "has already stripped the hellrot e46 and installed the body harness" — [DBO – Full M3 Swap Into A 330ci! Mechanical Swap Part 1! (2019-12-22)](https://www.youtube.com/watch?v=td8MgQ_3KGs) [description]. "the entire harness is already in the car" — [05:34](https://www.youtube.com/watch?v=td8MgQ_3KGs&t=334s) [captions].
- **DM-TL plug mismatch:**
  - The 330Ci's DM-TL was still fitted next to the M3 harness plug: "one has four wires one has three wires" — [22:22–22:48](https://www.youtube.com/watch?v=td8MgQ_3KGs&t=1342s) [captions].
  - "this one is a 3-wire the m3 DMT L is a four wire". The M3 module "bolted right in"; they would only know whether it worked once a check-engine light did or didn't appear — [DBO – Full M3 Swap Into A 330ci! Final Mechanical Touches Part 2! (2020-01-02), 03:41–04:33](https://www.youtube.com/watch?v=cEAIugEHkRQ&t=221s) [captions].
- **Fuel pressure, a mistake on camera:** they guessed the M3 filter/regulator "runs at four bar… somebody correct me" — [part 1, 16:40](https://www.youtube.com/watch?v=td8MgQ_3KGs&t=1000s) [captions].
- **Mechanical gotchas:** the M3 brake-booster holes didn't line up with the 330Ci firewall and had to be slotted — [part 1, 08:44–10:17](https://www.youtube.com/watch?v=td8MgQ_3KGs&t=524s); the heater-valve bracket was trimmed — [part 2, 02:43](https://www.youtube.com/watch?v=cEAIugEHkRQ&t=163s) [captions].
- **Result:** "we have re-shelled an e46 m3 into a non-m car… it runs". No electrical or coding episode was published; the channel lists only parts 1, 2 and this update — [DBO – The Engine Swap 6 Years in The Making! (2021-10-20), 12:08–12:58](https://www.youtube.com/watch?v=pokku8YU3BU&t=728s) [captions; description: "wiring harness, body harness, engine, subframe, all of it M3"].

#### ThaChileanDude (E46 Touring → S54, converted to manual)
- **Scope:** the build was "basically like a M3 conversion without the body kit" — [ThaChileanDude – Building an e46 m3 Wagon in 10 days !! (2024-05-07), 00:55](https://www.youtube.com/watch?v=iSgClonTiQg&t=55s) [captions; description credits a shop, Miracle Motorwerks].
- **Fuel:** "s54 has different fuel pumps and different fuel lines", so the tank and lines were replaced with M3 parts — [01:56](https://www.youtube.com/watch?v=iSgClonTiQg&t=116s) [captions].
- **Clutch switch (auto → manual):**
  - The clutch-switch information he found "all refers to the clutch pedals" and the manual pedal-box harness, which he no longer had — [05:58–06:29](https://www.youtube.com/watch?v=iSgClonTiQg&t=358s).
  - The wiring: "you add an extra pin… grab that harness out of a parts car". Then "you go to the ews module", and "you also tap into the brake pedal switch" — [19:56–20:26](https://www.youtube.com/watch?v=iSgClonTiQg&t=1196s) [captions].
- **First start:** wiring was plugged in the day after the engine went in — [23:49](https://www.youtube.com/watch?v=iSgClonTiQg&t=1429s). "it is tuned but it does take a little bit to start and it also needs gas" — [29:34](https://www.youtube.com/watch?v=iSgClonTiQg&t=1774s) [captions].
- **After the swap (daily-driven):**
  - "the ABS light is on I'm not sure why"; he had ordered a K+DCAN cable to check with INPA — [34:48–35:19](https://www.youtube.com/watch?v=iSgClonTiQg&t=2088s).
  - "The Temper light on and then check engine light on".
  - He blamed the check-engine light partly on a CSL airbox run without the HP/CSL DME and MAP sensor, and noted a CSL DME would need re-tuning "for the manual swap… because all csls were actually SMGs" — [35:19–35:49](https://www.youtube.com/watch?v=iSgClonTiQg&t=2119s) [captions].

#### UNRIVALED (E46 sedan with an S54 from an SMG car, converted to manual)
- **Overall:** "plug and play… true in a sense but there are some things that can get… overlooked" — [UNRIVALED – WATCH THIS BEFORE YOU S54 SWAP YOUR BMW (2021-02-05), 00:32](https://www.youtube.com/watch?v=eddLff8yba0&t=32s) [captions; the description says it was recorded in a hurry and some part names may be wrong].
- **Coolant-level sensor:** the expansion tank moves to the passenger side, so the level-sensor wire had to be cut, soldered and extended. He routed it over the radiator — [01:02–01:32](https://www.youtube.com/watch?v=eddLff8yba0&t=62s).
- **SMG-donor DME:**
  - It must be recoded or flashed. A local shop "got the cog light to disappear but the car still thinks it's an smg". It was "still in limp mode even after they coded it".
  - He recommends ECUWorx (UK) for the conversion.
  - [02:02–02:32](https://www.youtube.com/watch?v=eddLff8yba0&t=122s)
- **Auxiliary water pumps:**
  - "the s54 uses two auxiliary water pumps… two wire… and the non-m's only have one". The extra pump needs its connector and wires extended "inside the cabin to the hvac module".
  - Without it the cooling system was hard to bleed (an air pocket).
  - [02:32–03:33](https://www.youtube.com/watch?v=eddLff8yba0&t=152s)
- **Harness and Sport button:** "make sure you swap over all harnesses including the oxygen sensor harness, the smg harness" — [04:39](https://www.youtube.com/watch?v=eddLff8yba0&t=279s). "the sport button needs wiring" — [06:47](https://www.youtube.com/watch?v=eddLff8yba0&t=407s) [captions].

#### Project BMW (E46 325i Touring, M54 → S54)
- The 325i fuel line "is not going to work with this motor", so the lines were swapped from the M3 — [Project BMW – S54 Engine Swap Wagon RUNS.. ALMOST COMPLETE!! (2021-12-07), 00:34](https://www.youtube.com/watch?v=t9S0iXJj2GI&t=34s) [captions].
- Wiring is only mentioned, never shown: "got all the wiring sorted out which wasn't too bad"; "everything's either factory bmw crimps or… solder some wires but… very few" — [Project BMW – THIS S54 SWAP WAGON PULLS HARD!!! (2021-12-27), 00:38](https://www.youtube.com/watch?v=8ItILfnYuuY&t=38s), [03:13](https://www.youtube.com/watch?v=8ItILfnYuuY&t=193s) [captions]. The other episodes are mechanical.

#### BackyardWrenchin (1999 328i sedan, MS42; 2003 M3 SMG engine)
- **Plan:** use the MSS54 and do "converting my car's ms42 to ms43" wiring — [BackyardWrenchin – E46 S54 SWAP (PART 1)- Disassembly, SMG to Manual Harness (2017-03-26), 00:02](https://www.youtube.com/watch?v=3i3oCJJbh88&t=2s) [captions; chapters 05:22 wiring harness conversion, 10:45 SMG wire deletion].
- **SMG-to-manual strip, done by trial and error** ("I really don't know exactly what I'm doing"):
  - Identified the grey connectors as the SMG ECU's, cut them off, and pulled the wires back through the harness by matching colours — [09:53–10:47](https://www.youtube.com/watch?v=3i3oCJJbh88&t=593s), [12:32](https://www.youtube.com/watch?v=3i3oCJJbh88&t=752s).
  - Removed what he believed is the SMG relay and taped off wires that also ran to the engine DME connectors. Two connectors from that relay were left over, purpose unknown — [14:28–15:43](https://www.youtube.com/watch?v=3i3oCJJbh88&t=868s).
  - One gearbox connector remained (two green, one blue/yellow, one green/white), "may be for the… reverse light" — [16:09](https://www.youtube.com/watch?v=3i3oCJJbh88&t=969s) [captions].
- **Unknown extra wire:** the M3 has "this extra wire going into the exhaust manifold" that non-M cars lack. He didn't know what it was — [09:03](https://www.youtube.com/watch?v=3i3oCJJbh88&t=543s) [captions].
- He also removed secondary-air parts and planned to drop the post-cat sensors; noted only.
- The channel has only parts 1–4 (to part 4, cleaning and reassembly). No wiring or first-start episode exists.

#### Other E46 S54 clips found by search (short; titles only, not opened)
- The BMW Wagon Guy, "S54 swapped E46 touring/wagon - first start" (16 s), [EcGHTYG5I_U](https://www.youtube.com/watch?v=EcGHTYG5I_U).
- M346 Projects, "Starting S54 for first time in E46 ZHP" (22 s), [rS1uaWsxcFE](https://www.youtube.com/watch?v=rS1uaWsxcFE).
- Jared Wise, "Bmw E46 S54 swap - start attempt and failure" (30 s), [6UxYoCjpSpY](https://www.youtube.com/watch?v=6UxYoCjpSpY).
- cyberkaa, "S54 Sedan Swap - First Start", [IBwvpcC5ABE](https://www.youtube.com/watch?v=IBwvpcC5ABE).
- Silwer666, "E46 M3 s54b32 engine and sMg swap to facelift e46 330ci body - first start", [1KNppKr8hbI](https://www.youtube.com/watch?v=1KNppKr8hbI).
- FekzenSE, "StandAlone BMW M3 S54B32 engine swap in an E46 Touring" (standalone ECU, not MSS54), [4qwYa-cnxN4](https://www.youtube.com/watch?v=4qwYa-cnxN4).

### Inferences
- **The two US-relevant Touring builds both started from base-spec cars with only a DSC button** (Tenza, M346). A US 325i Touring may be the same. If so, the Sport button needs the M3 switch centre plus its power, K-bus and DME wiring, not just X60004 pins 15/16. Check the Touring's centre console before buying parts.
- **A Kassel-style vendor flash (EWS delete, VIN, cluster mileage) left Tenza with few pin moves,** but three body-side jobs remained even so:
  - the Sport LED;
  - wheel-speed-sensor plug compatibility, with an ABS light at first start;
  - the E-box fan plug.
  Kassel's written instructions were not self-explanatory without a donor car to trace.
- **The M3projekts specialist's rule fits the notes' X60004 table.** On a car that is already a six-cylinder with an electronic pedal, the engine-bay section of the body harness can stay, plus Sport wires. He doesn't mention the cluster-lamp, brake-switch and DM-TL differences the notes list. On an MS43/MS45 Touring those are still needed.
- **DM-TL:** DBO's 2001 330Ci (MS43) had a three-wire DM-TL, against four wires on the M3. The notes generalise that MS43 cars carry a DM-TL heater on X6011-7. Check the Touring's DM-TL plug before planning the pin-18 heater move (inference from one car; the 330Ci's exact build date isn't given).
- **E-box sub-connectors:** Import Modify's 3-pin vs 4-pin mismatch at X60541/X60531 supports the notes' warning that the X6053/X60531 family differs between M3 and non-M harnesses. Compare each E-box plug pin by pin before first start.
- **An ABS/DSC light after first start is the most common leftover:** Tenza and ThaChileanDude both had one, and ShopLifeTV's car later showed the traction light. Plan wheel-speed-sensor plug compatibility, DSC coding and VIN/steering-angle initialisation as part of the swap, not as an afterthought (Q2–Q3).
- **Starting order seen across these builds:**
  1. Charged battery (Tenza's first no-start).
  2. EWS solved: matched set or delete, and the EWS's own clutch/park-neutral input satisfied (ShopLifeTV, Import Modify).
  3. Fluids.
  4. Expect a "Christmas tree" of lamps until the cluster, LCM and DSC are coded (ShopLifeTV, Tenza).

### Gaps
- **No video films the MS43/MS45 → MSS54 body-side moves:**
  - X6011 → X60004 pins 1, 6, 11 and 21 for the cluster lamps;
  - 28 → 34 brake;
  - DM-TL heater to 18;
  - clutch via the gear-recognition switch to X60002-20.
  Kassel's written instructions to Tenza are not shown on camera.
- ShopLifeTV's promised S54 wiring video was never posted. BackyardWrenchin's series stops before wiring. DBO never posted an electrical episode.
- **Not read (YouTube rate limits during this session):**
  - captions for Tenza's "5 things… (part 1)" ([-TXzg2Z8d7w](https://www.youtube.com/watch?v=-TXzg2Z8d7w)), whose part 2 says it covered the expansion tank, washer tank and brake-booster lines;
  - Tenza's build part 1 ([Jsk-8VLRFKc](https://www.youtube.com/watch?v=Jsk-8VLRFKc));
  - M3projekts Ep5 "S54 install" ([Ipbjt8S2c2g](https://www.youtube.com/watch?v=Ipbjt8S2c2g));
  - Project BMW "The S54 ENGINE SWAP Begins!" and "…NOW INSTALLED IN THIS E46 TOURING" (titles only);
  - M346 Projects "e46 M3 SMG Touring Build pt 8 SMG WIRING" ([ua4AAA5sWOw](https://www.youtube.com/watch?v=ua4AAA5sWOw)), the most promising unread wiring episode, plus its other parts (12, 17, 26);
  - Dr_Wrench "S54 Swapped E46 Sedan: The Ultimate Street Build Full M3 conversion" ([LboNDJrVZ2M](https://www.youtube.com/watch?v=LboNDJrVZ2M));
  - Import Modify part 23 "Harness and Dash Panel" ([EJK2yHRhIEM](https://www.youtube.com/watch?v=EJK2yHRhIEM));
  - M3projekts Ep1/Ep7 and the "goodbye" video;
  - Tenza's front-end reassembly and total-cost episodes.
  
  I stopped fetching after repeated "confirm you're not a bot" checks rather than work around them.
- Tenza's 12-minute build summary ([-JDZ-UCllEI](https://www.youtube.com/watch?v=-JDZ-UCllEI)) has no captions; the description adds nothing electrical.
- **Comments** (creator replies) were not read, to avoid further rate-limit hits.

## Q2. Which videos show the coding: tools, NCS Expert, PA-Soft, M3 cluster in a non-M E46, MK60 DSC, steering angle, EWS sync, DME VIN, adaptations?

### Takeaway
The generic E46 coding steps in the written notes are all shown on camera, and they match:
- Standard Tools and K+DCAN install and settings;
- NCS Expert vehicle-order (FA/ZCS) read, edit and write;
- `FSW_PSW.MAN` edits followed by `SG_CODIEREN`;
- MK60 coding from the vehicle order;
- INPA MK60 Shift+F4 → F1 VIN/steering-angle initialisation;
- INPA adaptation erase.

Nothing MSS54-specific is shown with narration:
- Kassel's only EWS-sync video is a 40-second MS43 clip; the INPA keys are in its description.
- A French MS43 tutorial adds the key-off step.
- Mss Tuning's "Tool32 AIF writing VIN MSS54" has no captions and no description beyond its title.

No video found runs the Tool32 steering-angle jobs or an MSS54 EWS sync. The PA-Soft cluster VIN/mileage videos found all involve changing mileage, so they are only noted. Two useful additions: PA-Soft can write a VIN into a used MK60 ("Write FGSTNR", 14 characters), and the EWS's clutch/park-neutral input can be recoded in NCS Expert. The second is a workaround with a safety cost.

### Cited Findings

#### Tool setup: Standard Tools, K+DCAN cable, EDIABAS settings
- **ShopLifeTV (2016, 344k views)** — [ShopLifeTV – How To Setup INPA/NCSEXPERT (2016-04-20)](https://www.youtube.com/watch?v=9GS21wpt7l4) [chapters: 01:00 software and file prep, 07:11 configuring the cable driver, 09:50 testing]:
  - It installs the older XP-era package. He recommends a Windows XP Professional laptop: on Windows 7/8 or 64-bit "you're not going to be able to have full… usability", mainly INPA only — [00:40–01:11](https://www.youtube.com/watch?v=9GS21wpt7l4&t=40s).
  - Steps 1–3 from a forum package: EC-APPS copied to C:\, then `NFS\ENTPACKT\DISK1\setup.exe` with Windows XP, user mode and OBD selected; later steps "update under INPA 5.0.1 and complete under NCS Expert 3.0.8" — [02:43–06:27](https://www.youtube.com/watch?v=9GS21wpt7l4&t=163s).
  - Cable driver: Device Manager → USB Serial Port → Port Settings → Advanced, set "comm port number one" and change "the latency timer from 16 to 1", then run OBD setup — [09:06–09:40](https://www.youtube.com/watch?v=9GS21wpt7l4&t=546s).
  - Connection order: adapter into the same USB port, then cable into the car, then open INPA, then ignition on — [10:42](https://www.youtube.com/watch?v=9GS21wpt7l4&t=642s).
  - [captions]
- **50sKid (2016):** "I couldn't get NCS expert to run on" Windows 7 64-bit; "it has to run on a 32-bit system" — [50sKid – BMW E46 DSC… Unit Replacement & Coding! DIY (2016-07-31), 30:43](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=1843s) [captions].
- **Nick Goonan (2025), Windows 10/11** — [Nick Goonan – Install INPA, NCS Expert, WinKFP, Tool32 on Win10/11 Easily! (2025-03-29)](https://www.youtube.com/watch?v=62pyWB4x03w) [captions; chapters]:
  - Run the Standard Tools installer in Windows 7 compatibility mode and choose complete install — [00:32–01:03](https://www.youtube.com/watch?v=62pyWB4x03w&t=32s).
  - Turn off the data-backup options and select OBD and COM1 — [01:33–02:06](https://www.youtube.com/watch?v=62pyWB4x03w&t=93s).
  - Delete the installed C:\ folders and extract the pre-populated package to C:\ — [02:41–03:15](https://www.youtube.com/watch?v=62pyWB4x03w&t=161s).
  - In Device Manager change "com three to com one" — [05:53–06:23](https://www.youtube.com/watch?v=62pyWB4x03w&t=353s).
  - The MS4x Flasher/TunerPro part of the video is for MS42/MS43, not the MSS54.
- **BMW Doctor (2024)** — [BMW Doctor – BMW HOW TO SETUP K DCAN CABLE SETTINGS FOR INPA & ISTA THE CORRECT WAY!! (2024-12-31)](https://www.youtube.com/watch?v=2Oebra7Kbn0) [captions; chapters 01:25 configuring EDIABAS settings, 02:08 OBD]:
  - `EDIABAS.INI` interface must be "STD OBD", not "remote" or "enet" — [01:35](https://www.youtube.com/watch?v=2Oebra7Kbn0&t=95s).
  - The `OBD.ini` COM port must match the Device Manager port; he always uses COM1 — [02:06–03:06](https://www.youtube.com/watch?v=2Oebra7Kbn0&t=126s).
  - Latency must be 1. At the default 16, "the impa the battery and ignition lights are going to go crazy", and ISTA reads little more than the VIN — [03:36](https://www.youtube.com/watch?v=2Oebra7Kbn0&t=216s).
- **Cable pins:** "make sure pin 7 and 8 are bridged on your cable" before INPA on an E46 — [Evan Goyuk – How to calibrate the Steering Angle Sensor on any BMW // ABS FIX (2020-09-15), 02:17](https://www.youtube.com/watch?v=lseY6SRXWks&t=137s) [captions].

#### NCS Expert: the vehicle order and `FSW_PSW.MAN` edits
- **Vehicle order, 50sKid (2017)** — [50sKid – BMW E46 Manual Swap Project: How To Code the Vehicle Order DIY (2017-10-15)](https://www.youtube.com/watch?v=FiBr1h9j0bU) [captions; chapters 02:37 pre-facelift data, 05:51 post-facelift data, 08:36 coding the new vehicle order, 23:19 clearing engine adaptations]. Car: a post-facelift (FA) E46 converted from automatic.
  - **Where the order is stored:** two modules. He first says KMB and LCM for pre-facelift cars, then corrects himself: "it's not LCM it's EWS". Post-facelift cars use AKMB and ALSZ — [01:38–02:40](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=98s), [09:26](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=566s).
  - **ZCS edit:** erase the checksum digit, tick recalculate, subtract 8 from the last SA digit — [02:40–04:45](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=160s). His on-screen example is wrong: hex B minus 8 is 3, not "4" — [04:45](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=285s). He gives the correct table later: "8 becomes 0, 9 becomes 1, A becomes 2, B becomes 3" — [30:12](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1812s).
  - **Read the FA:** Load profile → Expert mode → VIN/ZCS/FA → ZCS/FA f. ECU → E46. The list offers EWS, KMB, AKMB and ALSZ; EWS fails on his facelift car and AKMB works — [08:52–09:26](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=532s).
  - **Edit the FA:** Enter FA, leave the VIN alone, then delete option "205" (automatic). 205 is looked up in `NCSEXPER\DATEN\E46` `E46ZST` — [09:59–11:31](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=599s).
  - **Write the FA:** don't use Process Car at this point. Use Process ECU → AKMB, job `FA_WRITE` (pre-facelift: `ZCS_SCHREIBEN`) → Execute, then change ECU → ALSZ → Execute — [12:31–15:10](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=751s).
  - **Verify:** restart NCS Expert and re-read from AKMB and ALSZ — [15:40](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=940s).
  - **Code the car:** Process Car → `SG_CODIEREN` stopped at the first module that failed (airbag "ABG"). He then coded modules one by one, skipping the airbag and the absent factory radio — [17:15–22:27](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1035s).
  - **Adaptations:** INPA → E46 → Engine → F4 → F7 "erasing adaptations", run each sub-item — [23:59–24:31](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1439s).
  - **Lesson:** the gearbox icon stayed until he default-coded AKMB and ALSZ themselves: "remember to recode all of your modules even the AKMB and ALSZ" — [26:05–28:08](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1565s).
- **EWS parameter edit, ShopLifeTV (2015)** — [ShopLifeTV – STARTING THE S54 SWAP CAR ON FOR THE FIRST TIME! (2015-08-19)](https://www.youtube.com/watch?v=BV1yvGP7sCM) [captions; chapter 01:05 clutch switch coding]:
  1. Start INPA and run the E46 chassis scan (it showed "about six errors" for brake-light switching). This starts the EDIABAS server. Close INPA — [01:40–02:12](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=100s).
  2. Open NCS Expert with Expert mode → F1 → F3 → E46. Pick the module pair for the car's age: KMB/EWS before 09/2001, AKMB/ALSZ after — [02:42](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=162s).
  3. Process ECU → EWS, change the job to `CODIERDATEN_LESEN` and execute. This writes `FSW_PSW.TRC` in `C:\NCSEXPER\WORK` — [03:13–03:43](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=193s).
  4. In the file, the parameter is "Park neutral eingang" (`PARK/NEUTRAL_EINGANG`). The captions are garbled on the value: "put active which means not… won't check it". This most likely means `nicht_aktiv`.
  5. Keep a backup and save the file as `FSW_PSW.MAN` — [04:13–04:44](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=253s).
  6. Reopen NCS Expert with a manipulation ("god mode", Revtor or Fister) profile and repeat F1 → F3 → E46. Process ECU → EWS → `SG_CODIEREN` → execute until "job ended" — [04:44–05:15](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=284s).
  7. Before the first crank he warns to check neutral "especially since you took off that [clutch] switch" check — [05:45](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=345s).
- **Cluster option, Motorsport Inspired (2022)** — [Motorsport Inspired – How to code and enable CSL OIL Level display readout on your E46 M3 (2022-01-19)](https://www.youtube.com/watch?v=SISvhcoWmYE) [captions; chapters]:
  - Key to position 2, NCS Expert with a "Revtor" profile, read from AKMB, Process ECU → AKMB, job `CODIERDATEN_LESEN` — [00:35–01:35](https://www.youtube.com/watch?v=SISvhcoWmYE&t=35s).
  - Back up the TRC, rename to `FSW_PSW.MAN`, find `OELNIVEAU_M3` and change "nicht active to just active" — [02:05–02:35](https://www.youtube.com/watch?v=SISvhcoWmYE&t=125s).
  - Change the job to `SG_CODIEREN` and execute — [03:05](https://www.youtube.com/watch?v=SISvhcoWmYE&t=185s).
  - "you will have to run a csl engine management", otherwise the display won't appear — [04:09](https://www.youtube.com/watch?v=SISvhcoWmYE&t=249s).
  - Readings: static at ignition on; dynamic needs a warm engine, about two minutes' idling on level ground and a button held for a couple of seconds (the captions don't make clear which button) — [06:44–08:15](https://www.youtube.com/watch?v=SISvhcoWmYE&t=404s).
- Pawel SWI – "NCS EXPERT ADD AND REMOVE VO/FA" (2016-11-28, 1:15) has no captions; the description repeats the title — [qWN_BRZSKDU](https://www.youtube.com/watch?v=qWN_BRZSKDU&t=0s) [description].

#### M3 cluster in a non-M E46
- **Tenza (Kassel-prepared cluster):**
  - Kassel set the M3 cluster to "the mileage of the actual wagon, the chassis mileage" and enabled the RPM lights — [8uwpzS_-uDs, 02:17–02:44](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=137s).
  - Kassel added rear-door lights to the cluster — [mDBiRn30fEs, 06:07](https://www.youtube.com/watch?v=mDBiRn30fEs&t=367s).
  - After the swap "All the VINs match. All of the mileage matches" — [8uwpzS_-uDs, 06:28](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=388s).
  - [captions]
- **flipfinish (2003 330Ci, 5-speed, M3 cluster)** — [flipfinish – Non M E46 with M3 cluster mod (2024-03-08)](https://www.youtube.com/watch?v=NuW1TWE_GBc) [captions]:
  - Traction control worked only after they "use[d] my friend's scanner… to recalibrate some stuff"; "I think he did change the light control module too" — [00:34](https://www.youtube.com/watch?v=NuW1TWE_GBc&t=34s).
  - Warm-up lights "start at 4,000 RPM and work their way around as the oil temp goes up"; the oil-temperature and coolant gauges and shift lights work — [01:04](https://www.youtube.com/watch?v=NuW1TWE_GBc&t=64s).
  - The same video describes setting the cluster to a lower mileage than the car's and coding out the tamper dot — [02:05](https://www.youtube.com/watch?v=NuW1TWE_GBc&t=125s). That is an odometer rollback; not documented here.
- **TerraPhantm (330i, 2016):** "Fully functional including warmup lights" — [TerraPhantm – M3 Cluster on 330i (2016-06-12)](https://www.youtube.com/watch?v=M7q7xC0wyIY&t=0s) [description; 23-second clip, no captions].
- **Tenza (2025), non-S54 race cars:**
  - "the M3 instrument cluster is a direct plug and play" — [Tenza Motorsports – E46 cruise control stalk wiring… M3 instrument cluster custom… (2025-05-05), 14:47](https://www.youtube.com/watch?v=8uRGM-OzqWs&t=887s).
  - Lamps on afterwards included the SMG warning, which the tuner (Rev Match) would code out — [16:19](https://www.youtube.com/watch?v=8uRGM-OzqWs&t=979s).
  - In the second car, cruise wouldn't engage; a scan showed "plausibility signal brake light switch" — [14:15](https://www.youtube.com/watch?v=8uRGM-OzqWs&t=855s).
  - [captions]
- **Add-on modules for non-S54 cars:** drukhadze's M3-cluster videos ("Oil temperature, RPM Lights and displayng of current gear realised with additional module") and PeterisGG's 330ti ("Module made by user drukhadze") use a third-party module so non-S54 cars can drive the M3 cluster's extra functions — [drukhadze – E46 328Ci MT with M3 SMG cluster (2018-05-07)](https://www.youtube.com/watch?v=km9v4GXo05M&t=0s), [drukhadze – E46 M3 Cluster in 330iA… (2019-03-18)](https://www.youtube.com/watch?v=aSAUeLIYJ7c&t=0s), [PeterisGG – E46 M3 cluster swap in 330ti… (2019-08-06)](https://www.youtube.com/watch?v=eZEUnrrJOQI&t=0s) [descriptions; no captions].
- **Mileage and tamper-dot videos (titles only, steps not documented):** Zero To 60 "BMW Milage Tamper Dot Removal E46 E39 E53: LCM Programming DIY" ([XRbUdOpYVUo](https://www.youtube.com/watch?v=XRbUdOpYVUo)), BimmerZen "E46 Odometer Tamper Dot Fix: Light switch module VIN and mileage coding" ([G5-0LvOcg4I](https://www.youtube.com/watch?v=G5-0LvOcg4I)), and M346 Projects "E46 M3 Cluster Mileage adjustment" ([pneZmknX858](https://www.youtube.com/watch?v=pneZmknX858)) [title only].
- **PDC after an SMG-to-manual conversion on an M3:**
  - One added wire runs from an empty slot beside the "yellow and blue wires" in the junction block behind the glove box ("Do not cut them. Do not tap into them") to pin 7 of the cluster's white connector — [WERKSTATTE - BMW ONLY – How to make PDC work on a BMW e46 M3 after SMG to Manual swap (2021-04-10), 02:57–03:58](https://www.youtube.com/watch?v=8pMdqlfaxpU&t=177s), [07:29](https://www.youtube.com/watch?v=8pMdqlfaxpU&t=449s) [captions].
  - Description part numbers: cluster-end wire 61130005197; glove-box terminal 61131387140/142/144 [description].

#### MK60 DSC: coding and VIN
- **50sKid (2016), non-M 2002+ MK60:**
  - NCS: File → Load profile → Expert mode → F1 → F3 → E46. "ews did not work", so he "chose… AKMB". Then F6 back → F4 → MK60, check the job is `SG_CODIEREN`, F3 execute: "coding active… coding ended" — [31:14–32:17](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=1874s).
  - INPA: F3 E46 → Chassis → DSC MK60 → F1 error memory showed "Vin not initialized execute lws calibration" — [32:47–33:47](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=1967s).
  - From the DSC screen: Shift+F4 → F1 with the wheel straight → "initialization completed". Then F4 → F2 clear and F1 read: no errors — [33:47–34:18](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=2027s).
  - [captions]
  - Description: "You don't need both cables, you only need a K+DCAN cable and INPA to recode a module" [description].
- **Warp Drive M (2023), filmed on an E53, "will work for E53… E39 or E46"** — [Warp Drive M – How to code your ABS module on your BMW E39/E46/E53 after replacement! (2023-04-27)](https://www.youtube.com/watch?v=S79WHnlpSuM) [captions; chapters]:
  - Replacing only the hydraulic block while keeping your own control module needs bleeding but no coding — [00:32](https://www.youtube.com/watch?v=S79WHnlpSuM&t=32s).
  - NCS: Expert mode → F1 → F3 → read from EWS (on that car) → F6 → F4 → DSC → `SG_CODIEREN` (F2 to change job) → F3 — [02:32–04:09](https://www.youtube.com/watch?v=S79WHnlpSuM&t=152s).
  - Steering-angle fault: try lock to lock "a few times till the lights go off"; otherwise a scan tool's chassis → ABS → sensor adjustments → steering angle — [05:11–06:13](https://www.youtube.com/watch?v=S79WHnlpSuM&t=311s).
- **LM Auto Repairs (2016), used same-part-number MK60 on a 2003 E46 diesel** — [LM Auto Repairs – BMW E46 Replacement ABS/DSC MK60 coding/programming. (2016-06-15)](https://www.youtube.com/watch?v=1dn4c3g6dsA) [captions; chapters 02:42 steering angle, 04:52 correct the VIN]:
  - PA-Soft showed "PT can chassis number wrong", "ECU not initialized" — [03:39](https://www.youtube.com/watch?v=1dn4c3g6dsA&t=219s).
  - Fix in PA-Soft: ABS module → reprogramming → "write FGSTNR". It asks for "the last 14" characters of the VIN, starting after "WBA" (unlike modules that take the last seven), and records "straight into" the unit — [04:47–05:50](https://www.youtube.com/watch?v=1dn4c3g6dsA&t=287s).
  - Steering angle: PA-Soft couldn't calibrate, and his INPA "would fail connection to the ECU every single time". A generic scan tool did it "straightway" with the wheel dead straight — [06:23–07:26](https://www.youtube.com/watch?v=1dn4c3g6dsA&t=383s).
- **EvzenBimmer (2020):** after fitting an MK60, bleed in order "rear right, rear left, front right, front left"; install "Mike's Easy BMW Tools" — [EvzenBimmer – BMW DSC Unit MK60 Replace + Coding VIN (2020-06-17)](https://www.youtube.com/watch?v=chlaonE3CGU&t=0s) [description; no captions].
- **Swap-specific remarks:**
  - ShopLifeTV calls the MK60 "for the most part plug-and-play" — [hnaZqKbvwT4, 03:35](https://www.youtube.com/watch?v=hnaZqKbvwT4&t=215s) [captions].
  - M3projekts fitted the M3 MK60 on the car's own connector — [YfJyE9DU5OE, 01:43](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=103s) [creator subtitles].
  - DBO's team noted the later M3 DSC allows M Track — [td8MgQ_3KGs, 12:35](https://www.youtube.com/watch?v=td8MgQ_3KGs&t=755s) [captions].
  - None of these shows an M3 MK60 coded to a non-M FA.

#### Steering-angle calibration
- **Evan Goyuk (2020, 379k views):**
  - Lock-to-lock three times didn't clear his lights — [01:16](https://www.youtube.com/watch?v=lseY6SRXWks&t=76s).
  - INPA: E46 → Chassis → MK60 → "routines… shift and then F4" → F1 with the wheel centred → "initialization complete" — [02:48–03:19](https://www.youtube.com/watch?v=lseY6SRXWks&t=168s).
  - Check: E46 → Chassis → MK60 → F5 status → "read analog" → F2 "read DSC sensor". The steering angle should read zero with the wheel straight; "if it says like two or three then you know that it's not calibrated" — [03:19–04:19](https://www.youtube.com/watch?v=lseY6SRXWks&t=199s).
  - [captions]
- **Earl Moorhead (2023), ZHP with 5E43 "steering angle sensor internal":**
  - A recalibration "said successful but the code was still there" — [03:00](https://www.youtube.com/watch?v=2mqz14tWpMI&t=180s).
  - The new sensor (32 36 6 792 …) sits "at the base of the steering column" — [04:05](https://www.youtube.com/watch?v=2mqz14tWpMI&t=245s).
  - With the new sensor the code cleared, but the lamps came back on the test drive: "it does need to be calibrated" — [26:24](https://www.youtube.com/watch?v=2mqz14tWpMI&t=1584s).
  - [Earl Moorhead – 1999-2006 BMW E46 Code 5E43 DSC won't calibrate steering Angle Sensor Repair (2023-02-19)](https://www.youtube.com/watch?v=2mqz14tWpMI) [captions]
- **Unusable for steps:** Pedro Canales "E46 STEERING WHEEL ANGLE FIX WITH INPA" (2021-09-05) has no captions; the description says only it was his first INPA use — [7JedR_UiIO8](https://www.youtube.com/watch?v=7JedR_UiIO8&t=0s) [description]. BMW Programming & Encoding "BMW E46 LWS STEERING ANGLE SENSOR MATCHING" (2019) has unintelligible captions — [s8AIz5IsEMc](https://www.youtube.com/watch?v=s8AIz5IsEMc) [captions unusable].
- **Tool32:** no video found uses `DSC_MK60.PRG` / `lenkwinkel_dsc_abgleichen` / `test_lenkwinkel`.

#### EWS: sync, delete, starter interlock
- **Kassel Performance, MS43 not MSS54:** the description reads "Initial EWS sync of a Virginized Kassel Performance MS43 ECU", done in INPA. It warns "Used DME's must be sent in for reset service". The keys given are "Select E46, Engine M54 MS43, Shift + F6, F1" — [KasselPerformance – BMW M54 Siemens MS43 325 330 EWS Sync - INPA (2015-08-27)](https://www.youtube.com/watch?v=HPoaKPqLpgE&t=0s) [description; 40-second clip, no captions; it is the channel's only upload].
- **Theo BiTurbo, M54/MS43 (French; captions are YouTube's auto-translation):**
  - He had run the car temporarily on "my two-key system" after fitting a "Phase 2 ECU on my Phase 1" car, then refitted the original EWS — [00:05](https://www.youtube.com/watch?v=Czg63KkIRZw&t=5s).
  - An unsynchronised EWS/DME "will just crank; it won't start" — [00:35](https://www.youtube.com/watch?v=Czg63KkIRZw&t=35s).
  - In INPA "you press Shift + F6", then turn the key off for 5 seconds — [01:40](https://www.youtube.com/watch?v=Czg63KkIRZw&t=100s).
  - [Theo BiTurbo – TUTO synchronisation EWS e46 e39 M54 INPA (2022-12-22)](https://www.youtube.com/watch?v=Czg63KkIRZw) [auto-translated captions]
- **EWS delete in practice:**
  - Tenza's Kassel-flashed DME started first time once the battery was charged — [8uwpzS_-uDs, 05:38](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=338s).
  - Import Modify's eBay-vendor delete still needed "the EWS matching the key", or the EWS starter circuit jumpered — [gSeB5NYZ8qc, 11:50–12:53](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=710s) [captions].
- **Clutch/park-neutral start interlock:**
  - ShopLifeTV recoded the EWS parameter instead of fixing the wiring — [BV1yvGP7sCM, 01:08–05:15](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=68s).
  - ThaChileanDude wired the clutch switch to the EWS module — [iSgClonTiQg, 19:56–20:26](https://www.youtube.com/watch?v=iSgClonTiQg&t=1196s) [captions].
- No video found shows an MSS54 EWS sync (INPA or Tool32 `EWS3_*` jobs).

#### DME VIN (AIF) writing and flashing
- Mss Tuning – "Tool32 AIF writing VIN MSS54 BMW" (2015-03-31, 2:17, 47k views): no captions; the description repeats the title — [NQkKzv5NvW4](https://www.youtube.com/watch?v=NQkKzv5NvW4&t=0s) [description]. It exists, but its steps couldn't be read.
- Mss Tuning – "MSS Flasher" (2015-01-05): "Flashing of MSS54HP-CSL using MSSFlasher" — [odtFf9lEp0o](https://www.youtube.com/watch?v=odtFf9lEp0o&t=0s) [description].
- Tenza's Kassel DME arrived with the VIN done ("All the VINs match") — [8uwpzS_-uDs, 06:28](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=388s) [captions].

#### Adaptation reset
- INPA → E46 → Engine (M54 in his car) → F4 → F7 "erasing adaptations", run each entry — [FiBr1h9j0bU, 23:59–24:31](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1439s) [captions]. No MSS54-specific adaptation video was read (see Gaps).

### Inferences
- **The NCS/INPA mechanics are not where these builds got stuck.** Where they struggled, it came down to:
  - which module to read the FA from (AKMB vs EWS: 50sKid and Warp Drive M, depending on car age);
  - Code Car stopping at the first failure;
  - an INPA build that couldn't reach the MK60 (LM Auto);
  - which value an EWS parameter needs.
- **For the Touring:**
  - Prove the tool chain on the unmodified car first: STD:OBD, COM1, latency 1, pins 7+8 bridged.
  - Keep a second way to calibrate steering angle (Tool32 per the notes, or a scan tool, as LM Auto and Warp Drive M fell back on).
  - Don't rely on an INPA 5.0.x package of the kind ShopLifeTV installs for the MK60 page.
- **PA-Soft's MK60 "Write FGSTNR" is a documented, low-risk way** to put the Touring's VIN into a used DSC unit before the INPA initialisation (LM Auto). It does not replace NCS coding of the unit's parameters.
- **No video supports a DIY MSS54 EWS sync.** The only sync videos are MS43, and Kassel's says used DMEs must first be "reset" by them. That agrees with the notes: virginise or delete.
- **The safe route for an ex-automatic or SMG-donor EWS is wiring, not coding:** wire the clutch switch to the EWS, as ThaChileanDude did. Coding the park/neutral input off (ShopLifeTV) removes a start interlock. ShopLifeTV himself warned the car could lurch if started in gear.

### Gaps
- **Not readable:**
  - Mss Tuning's MSS54 AIF/VIN video (no captions or description) and Pedro Canales' INPA steering-angle video (no captions);
  - BMW Doctor's "How to REMOVE Your EWS / IMMOBILISER" ([rHjXWBOdA0E](https://www.youtube.com/watch?v=rHjXWBOdA0E)), bimmermerchant's "M54 Engine DME EWS Master Key Tumbler Swap Part 1" ([T0HKsNfjhio](https://www.youtube.com/watch?v=T0HKsNfjhio)), Burak Saylav's "BMW INPA Guide: How to Reset Engine Adaptations?" ([18WdML4pCYM](https://www.youtube.com/watch?v=18WdML4pCYM)), 50sKid's "BMW E46 DIY How To Code Module Options" ([4PuVjeUYpZE](https://www.youtube.com/watch?v=4PuVjeUYpZE)) and Bimmer Shed NI's install tutorial ([Vh0mbi2yA18](https://www.youtube.com/watch?v=Vh0mbi2yA18)): bot checks or HTTP 429.
- **Not found:**
  - a video of the INPA "MS S54 for S54 M3" script (EWS page, adaptations, VANOS tests);
  - an MSS54 `ADAPT_LOESCHEN` run;
  - a Tool32 `12MSS54.PRG` AIF write with narration;
  - an M3 MK60 coded into a non-M Touring;
  - PA-Soft M3-cluster EEPROM work that sets the true VIN and mileage without altering mileage.
- The labels of INPA's other two MK60 compensation routines, beyond F1, are not shown in any video read.

## Q3. Steps, pin moves, job names and gotchas as shown, and where the videos contradict or add to the written notes

### Takeaway
On the points they cover, the videos mostly confirm the written notes. They add practical detail the notes lack:
- switch-centre power and K-bus wiring for the Sport button on a base Touring;
- incompatible wheel-speed-sensor plugs;
- the EWS clutch/park-neutral input as a first-start blocker;
- PA-Soft writing a VIN into a used MK60;
- an INPA check of the steering-angle reading;
- Kassel's INPA keys for an MS43 sync;
- the M56 SULEV tank connector.

They contradict the notes in five places:
- ShopLifeTV's advice to realign the LCM to a donor cluster, and his recoding of the EWS park/neutral input;
- DBO's "four bar" fuel-pressure guess;
- 2015–16 claims that the tools need 32-bit Windows XP;
- a hex-arithmetic slip in 50sKid's ZCS example, which he corrects later in the same video.

The notes' biggest open items are not settled by any video:
- the cluster-lamp pin moves on MS43/MS45 cars;
- an MSS54 EWS sync;
- MSS54 AIF writing;
- an M3 MK60 coded into a Touring;
- the Tool32 steering-angle job.

### Cited Findings

#### Harness and pins
- **Sport button: agrees, and adds the power and K-bus wiring.**
  - *Notes:* switch-centre pins 17/18 → X60004-15/16; the M3 switch unit is needed.
  - *Video:* Tenza wired exactly that ("17 and 18… 6004… pins 15 and 16") — [mDBiRn30fEs, 09:31](https://www.youtube.com/watch?v=mDBiRn30fEs&t=571s) [captions].
  - *Addition:* on a base Touring with only a DSC button, the M3 panel's power and K-bus feeds are missing:
    - "no wiring to the K bus for the switch panel or the fuse box" — [VHCrVhVuFzY, 20:45](https://www.youtube.com/watch?v=VHCrVhVuFzY&t=1245s);
    - Tenza's panel misbehaved until all its feeds had constant 12 V — [mDBiRn30fEs, 10:22–10:48](https://www.youtube.com/watch?v=mDBiRn30fEs&t=622s) [captions].
  - Tenza's Sport LED initially didn't work at all — [8uwpzS_-uDs, 06:28](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=388s).
- **Kassel's MS42 column: confirms the chart.**
  - *Notes:* they question its "remove pin 1 (charge lamp)" line.
  - *Video:* Import Modify moved 28→30 and 30→20, removed pins 1 and 2, and added the pedal wires — [9ErSBXkH7S0, 15:28](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=928s).
  - The charge-lamp outcome isn't shown; he only says "alternators charging" — [gSeB5NYZ8qc, 17:40](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=1060s) [captions]. The MS42 column doesn't apply to a 2001–05 Touring anyway.
- **E-box sub-connectors: supports the notes.**
  - *Notes:* X6053/X60531 differ between harnesses (injector-circuit-low case).
  - *Video:* Import Modify found X60541/X60531 as 3-pin vs 4-pin ("I'm missing a wire") — [9ErSBXkH7S0, 01:05](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=65s) [captions].
- **E-box fan: adds.**
  - *Notes:* the E-box blower exists only on automatic, SMG or hot-climate cars, and the MSS54 drives it from X60002-12.
  - *Video:* on Tenza's wagon the M3 engine-harness fan plug had no mate and was "left disconnected", because the wagon's fan plug is fed from the body side — [mDBiRn30fEs, 02:05–03:05](https://www.youtube.com/watch?v=mDBiRn30fEs&t=125s) [captions].
  - *Open:* he didn't check whether the body-side feed still runs the fan under the MSS54. Kassel's MS45 column removes X60004-19, the MS45 fan output, per the notes.
- **DM-TL: adds a question.**
  - *Notes:* DM-TL heater on X60004-18; MS43 cars carry it on X6011-7.
  - *Video:* DBO's 2001 330Ci DM-TL was "a 3-wire", the M3's "a four wire", and the M3 module "bolted right in" — [cEAIugEHkRQ, 03:41](https://www.youtube.com/watch?v=cEAIugEHkRQ&t=221s) [captions].
  - That car had a full M3 body harness, so its plug matched the M3 unit. A Touring keeping its own harness needs its DM-TL plug and wire count checked before planning the heater move.
- **Wheel-speed sensors: adds.**
  - *Notes:* only MK20→MK60 plug differences.
  - *Video:* M3 and non-M wheel-speed-sensor plugs "will not plug into each other". Tenza fitted non-M sensors in M3 hubs and had an ABS light at first start — [mDBiRn30fEs, 03:15–05:15](https://www.youtube.com/watch?v=mDBiRn30fEs&t=195s), [8uwpzS_-uDs, 07:18](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=438s) [captions].
  - M3projekts needed no wheel-speed-sensor extension with the M3 MK60 on the car's connector — [YfJyE9DU5OE, 01:43](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=103s) [creator subtitles].
- **Coolant-level sensor and expansion tank: agrees with the notes' remark that builders extended the coolant-level lead.**
  - ShopLifeTV extended it temporarily — [BV1yvGP7sCM, 07:34](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=454s).
  - Import Modify had to rewire it — [9ErSBXkH7S0, 13:22](https://www.youtube.com/watch?v=9ErSBXkH7S0&t=802s).
  - M3projekts moved it from left to right — [YfJyE9DU5OE, 03:22](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=202s).
  - M346 used Hungarian-made M3 expansion-tank brackets on the Touring — [4Q3PxGuJyxI, 00:05](https://www.youtube.com/watch?v=4Q3PxGuJyxI&t=5s).
  - [captions / creator subtitles]
- **Second auxiliary water pump (M3 heater-valve pump): agrees and adds.**
  - *Notes:* the M3 heater valve has a pump needing "2 wires not present on non m" (harness_engine_side.md, Q3).
  - *Video:* UNRIVALED says the extra two-wire pump must be wired back "inside the cabin to the hvac module". Without it his cooling system was hard to bleed — [eddLff8yba0, 02:32–03:33](https://www.youtube.com/watch?v=eddLff8yba0&t=152s) [captions].
- **Reverse light on ex-automatic cars: adds.** ShopLifeTV still had to wire the reverse light because the automatic "had a separate way" — [BV1yvGP7sCM, 08:05](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=485s) [captions]. This matters only if the Touring was automatic.
- **Engine-bay body-harness section: adds a rule of thumb that fits the notes.** "It is good from any 6-cylinder… add the wires for the Sport button - if not M3"; an M52-era section would also lack the electronic-pedal wiring — [YfJyE9DU5OE, 08:35](https://www.youtube.com/watch?v=YfJyE9DU5OE&t=515s) [creator subtitles]. The notes' list of MS43/MS45 lamp, brake and DM-TL moves still applies on top of this.
- **SMG-to-manual harness: a gap the video doesn't close.**
  - *Video:* BackyardWrenchin removed the SMG ECU connectors and relay by trial and error — [3i3oCJJbh88, 10:47–15:43](https://www.youtube.com/watch?v=3i3oCJJbh88&t=647s) [captions].
  - *Notes:* an SMG engine harness lacks X60002-20 (gear recognition, used for cruise). The video never mentions adding it.
  - ShopLifeTV's and ThaChileanDude's clutch-switch work was on the body side, for the EWS start interlock — [BV1yvGP7sCM, 00:38](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=38s), [iSgClonTiQg, 19:56](https://www.youtube.com/watch?v=iSgClonTiQg&t=1196s) [captions].

#### Fuel
- **Fuel pressure: contradiction (video wrong).** DBO guessed the M3 filter/regulator runs "four bar… somebody correct me" — [td8MgQ_3KGs, 16:40](https://www.youtube.com/watch?v=td8MgQ_3KGs&t=1000s) [captions]. The fuel-pump notes give 5 bar (BMW) and 5.0 ± 0.2 bar (Bentley).
- **Lines: agrees.** Project BMW: "this is the 325 line and it's not going to work with this motor" — [t9S0iXJj2GI, 00:34](https://www.youtube.com/watch?v=t9S0iXJj2GI&t=34s). ThaChileanDude: "different fuel pumps and different fuel lines" — [iSgClonTiQg, 01:56](https://www.youtube.com/watch?v=iSgClonTiQg&t=116s) [captions]. This matches the notes' M3 fittings point.
- **M56 SULEV Touring: adds first-hand evidence for the fuel-pump notes' finding that only M56 SULEV 325is had the EKP controller and a returnless tank.**
  - The M56 tank's one 6-wire plug vs two plugs on the M54/S54 tank — [PgW1oWs7cfk, 07:17–08:49](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=437s) [captions].
  - The video doesn't say how the pump is switched afterwards (M56 EKP module kept or bypassed). It does run, with a Kassel DME — [PgW1oWs7cfk, 10:23](https://www.youtube.com/watch?v=PgW1oWs7cfk&t=623s).

#### EWS and starting
- **DME-side delete leaves the car's EWS in charge of the starter: agrees.** Import Modify's vendor: "you still have to have the EWS matching the key" — [gSeB5NYZ8qc, 12:23](https://www.youtube.com/watch?v=gSeB5NYZ8qc&t=743s) [captions].
- **Park/neutral input: fills a gap, and contradicts the notes' preferred setting.**
  - *Notes:* the correct `PARK/NEUTRAL_EINGANG` value for a US manual car is undocumented; their inference is to keep it `aktiv`.
  - *Video:* ShopLifeTV's ex-automatic 330i would not start until he recoded the EWS so it "won't check" the clutch/park-neutral input (most likely `nicht_aktiv`; captions garbled) — [BV1yvGP7sCM, 01:08–04:44](https://www.youtube.com/watch?v=BV1yvGP7sCM&t=68s).
  - *Alternative shown:* ThaChileanDude kept the interlock and wired the clutch switch to the EWS module instead — [iSgClonTiQg, 20:26](https://www.youtube.com/watch?v=iSgClonTiQg&t=1226s) [captions].
- **INPA EWS sync keys (MS43 only): add.**
  - Kassel's description gives "Shift + F6, F1" for a Kassel-virginised MS43 — [HPoaKPqLpgE](https://www.youtube.com/watch?v=HPoaKPqLpgE&t=0s) [description].
  - The notes' failed Touring case A used Shift+F6, then F2 (reset) and F1 (store).
  - Theo BiTurbo adds key-off for about 5 seconds after Shift+F6 — [Czg63KkIRZw, 01:40](https://www.youtube.com/watch?v=Czg63KkIRZw&t=100s) [auto-translated captions].
  - None of this has been shown to work on an MSS54.
- **Two-key interim: agrees with the notes' case B.** Theo BiTurbo also ran a "two-key system" while his EWS and DME didn't match — [Czg63KkIRZw, 00:05](https://www.youtube.com/watch?v=Czg63KkIRZw&t=5s).

- **SMG-donor DME software: agrees.**
  - *Notes:* an SMG donor DME needs the HS (manual) variant or ECUWorx's "Transmission Swap".
  - *Video:* UNRIVALED's local shop "coded" it, which cleared the gear icon, but the car "still thinks it's an smg and it's still in limp mode". He turned to ECUWorx — [eddLff8yba0, 02:02](https://www.youtube.com/watch?v=eddLff8yba0&t=122s) [captions].
  - So NCS-style coding is not enough; the DME software has to change.

#### Cluster, LCM and mileage
- **LCM is the master record: contradicted by ShopLifeTV, consistent with Tenza and Kassel.**
  - *Notes:* make the cluster match the LCM, never the reverse (49 U.S.C. §32704).
  - *Contradiction:* ShopLifeTV advises "realign the LCM… get the VIN numbers to match up in the mileage" to a matched donor set — [hnaZqKbvwT4, 03:14](https://www.youtube.com/watch?v=hnaZqKbvwT4&t=194s) [captions]. Following that with a donor cluster would change the car's recorded mileage.
  - *Consistent:* Kassel set Tenza's M3 cluster to the wagon's own mileage — [8uwpzS_-uDs, 02:17](https://www.youtube.com/watch?v=8uwpzS_-uDs&t=137s).
- **The tamper dot appears when this is skipped.** ThaChileanDude's swapped Touring shows "The Temper light on" — [iSgClonTiQg, 35:19](https://www.youtube.com/watch?v=iSgClonTiQg&t=2119s) [captions]. This supports the notes' EEPROM/VIN step.
- **Rear-door LEDs: agrees.** The notes say sedan/Touring owners must add rear-door LEDs to an M3 cluster; Kassel does this as part of its cluster service — [mDBiRn30fEs, 06:07](https://www.youtube.com/watch?v=mDBiRn30fEs&t=367s) [captions].
- **Warm-up and shift lights: agrees, and adds.** They work on non-M cars with an M3 cluster (flipfinish 330Ci, TerraPhantm 330i) — [NuW1TWE_GBc, 01:04](https://www.youtube.com/watch?v=NuW1TWE_GBc&t=64s) [captions], [M7q7xC0wyIY](https://www.youtube.com/watch?v=M7q7xC0wyIY&t=0s) [description]. An SMG warning lamp may need coding out on a non-SMG car — [8uRGM-OzqWs, 16:19](https://www.youtube.com/watch?v=8uRGM-OzqWs&t=979s) [captions].
- **CSL oil-level display needs CSL DME software: agrees** — [SISvhcoWmYE, 04:09](https://www.youtube.com/watch?v=SISvhcoWmYE&t=249s) [captions].

#### DSC and steering angle
- **"MK60 is mostly plug-and-play": partly in tension with the notes.**
  - *Notes:* the DSC is "the least predictable part".
  - *Video:* ShopLifeTV recommends the MK60 as "for the most part plug-and-play" — [hnaZqKbvwT4, 03:35](https://www.youtube.com/watch?v=hnaZqKbvwT4&t=215s).
  - No video shows an M3 MK60 coded to a non-M FA. The ABS lights in Tenza's and ThaChileanDude's Tourings were not diagnosed on camera.
- **DSC VIN: adds and verifies.**
  - *Notes:* the PA-Soft MK60 VIN route was "unverified by the poster", and Bali says "You don't directly code the VIN".
  - *Video:* LM Auto writes it with PA-Soft "write FGSTNR", 14 characters — [1dn4c3g6dsA, 04:47–05:50](https://www.youtube.com/watch?v=1dn4c3g6dsA&t=287s) [captions].
  - Both can be true: NCS coding doesn't write the VIN, but a dedicated PA-Soft job does.
- **NCS module to read the vehicle order: agrees** with the notes' madstig sequence (AKMB, "If AKMB does not work try EWS"). "ews did not work" on a 2002+ car and AKMB did — [CvyVCwCAx1Q, 31:14](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=1874s), [FiBr1h9j0bU, 09:26](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=566s). EWS worked on an E53 — [S79WHnlpSuM, 03:03](https://www.youtube.com/watch?v=S79WHnlpSuM&t=183s) [captions].
- **INPA MK60 initialisation: agrees.** Shift+F4 → F1 — [CvyVCwCAx1Q, 33:47](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=2027s), [lseY6SRXWks, 02:48](https://www.youtube.com/watch?v=lseY6SRXWks&t=168s).
  - *Addition:* the F5 → read analog → F2 check of the steering-angle reading — [lseY6SRXWks, 03:19–04:19](https://www.youtube.com/watch?v=lseY6SRXWks&t=199s) [captions].
  - *Addition:* lock-to-lock sometimes clears the fault and sometimes doesn't — [S79WHnlpSuM, 05:11](https://www.youtube.com/watch?v=S79WHnlpSuM&t=311s), [lseY6SRXWks, 01:16](https://www.youtube.com/watch?v=lseY6SRXWks&t=76s).
  - *Addition:* an INPA build that can't reach the unit is worked around with a generic scan tool — [1dn4c3g6dsA, 06:54](https://www.youtube.com/watch?v=1dn4c3g6dsA&t=414s).
- **Sensor location: agrees with the notes' inference.** On an E46 ZHP the steering-angle sensor is "at the base of the steering column", and a new sensor still needs calibrating — [2mqz14tWpMI, 04:05](https://www.youtube.com/watch?v=2mqz14tWpMI&t=245s), [26:24](https://www.youtube.com/watch?v=2mqz14tWpMI&t=1584s) [captions].
- **Bleed order: agrees** — RR, RL, FR, FL [chlaonE3CGU](https://www.youtube.com/watch?v=chlaonE3CGU&t=0s) [description].

#### Tools and coding order
- **Windows version: dated contradiction.** 2015–16 videos say XP/32-bit only — [9GS21wpt7l4, 00:40–01:11](https://www.youtube.com/watch?v=9GS21wpt7l4&t=40s), [CvyVCwCAx1Q, 30:43](https://www.youtube.com/watch?v=CvyVCwCAx1Q&t=1843s). The notes (Standard Tools 2.12 on Windows 7–11, 64-bit) are confirmed by a 2025 Windows 10/11 install — [62pyWB4x03w, 00:32–06:23](https://www.youtube.com/watch?v=62pyWB4x03w&t=32s) [captions].
- **INPA 5.0.x: adds a caution.** ShopLifeTV's package installs "INPA 5.0.1" — [9GS21wpt7l4, 06:27](https://www.youtube.com/watch?v=9GS21wpt7l4&t=387s). The notes report owners on INPA 5.00/5.0.2 finding no MK60 steering-angle entry.
- **Cable settings: agrees, with on-screen support.** COM1 + latency 1 — [9GS21wpt7l4, 09:06](https://www.youtube.com/watch?v=9GS21wpt7l4&t=546s), [2Oebra7Kbn0, 03:36](https://www.youtube.com/watch?v=2Oebra7Kbn0&t=216s). `STD:OBD` — [2Oebra7Kbn0, 01:35](https://www.youtube.com/watch?v=2Oebra7Kbn0&t=95s). Pins 7/8 bridged — [lseY6SRXWks, 02:17](https://www.youtube.com/watch?v=lseY6SRXWks&t=137s). The notes rested `STD:OBD` on secondary sources; the video shows it on screen.
- **Code Car: agrees, and adds.** It fails at the first module, so code modules singly — [FiBr1h9j0bU, 17:15–22:27](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1035s), matching the notes' Bali text.
  - *Addition:* after an FA change, re-code AKMB and ALSZ themselves; the gearbox icon stayed until he did — [FiBr1h9j0bU, 26:05–28:08](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1565s).
  - *Addition:* reset DME adaptations afterwards (INPA F4 → F7) — [FiBr1h9j0bU, 23:59](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1439s) [captions].
- **ZCS bit arithmetic: video slip.** The notes' "subtract 8" is right. 50sKid's whiteboard example gives "B → 4" at 04:45 and is corrected to "B becomes 3" at 30:12 — [FiBr1h9j0bU, 04:45](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=285s), [30:12](https://www.youtube.com/watch?v=FiBr1h9j0bU&t=1812s) [captions].
- **PDC after SMG→manual: adds** (only relevant if the M3 body harness or SMG parts are kept). One wire from the glove-box junction block to cluster connector pin 7 — [8pMdqlfaxpU, 03:28–07:29](https://www.youtube.com/watch?v=8pMdqlfaxpU&t=208s) [captions].

### Inferences
**Changes worth making to the guide and the written notes:**
1. Add the switch-centre feed (constant/accessory power, K-bus, seat-heater lines) to the Sport-button item, and a check for whether the Touring has a switch centre at all.
2. Add "M3 and non-M wheel-speed-sensor plugs differ" to the subframe/hub transfer step. Either keep the Touring's own sensors in the M3 hubs or move the M3 pigtails, then verify with INPA status before driving.
3. In the EWS section, state that an EWS-deleted DME still needs the Touring's EWS to see the key and the clutch input. Recommend wiring the clutch switch to EWS pin 8 rather than coding `PARK/NEUTRAL_EINGANG` off. Cite ShopLifeTV as the counter-example.
4. Add PA-Soft "Write FGSTNR" as the documented way to put the Touring's VIN into a used MK60, before INPA initialisation.
5. Correct any "four bar" claim (DBO), drop XP-only advice, and warn against INPA 5.0.x packages for MK60 work.
6. Keep the "make the cluster match the LCM" rule. ShopLifeTV's LCM-realign advice is the main video source to warn readers about. Tenza/Kassel show the legal way (cluster set to the car's true mileage).

**Typical order, as the builds that got furthest did it:**
1. Vendor or virgin DME (or a matched set).
2. Battery charged and oil primed (fuel-pump fuse out).
3. Clutch switch to EWS.
4. First start.
5. Cluster VIN/mileage.
6. DSC coding and VIN, then steering-angle initialisation.
7. Clear faults and reset adaptations.
8. Fix Sport, wheel-speed and lamp leftovers.

### Gaps
- **No video settles the notes' main open items:**
  - MS43/MS45 cluster-lamp moves (X6011 → X60004 1/6/11/21; oil-pressure lamp to cluster pin 13 vs 14);
  - brake 28→34 symptoms if missed;
  - DM-TL heater routing on a Touring;
  - the clutch/gear-recognition crossing point;
  - MSS54 EWS sync, MSS54 AIF write and MSS54 adaptation jobs;
  - an M3 MK60 coded to a Touring FA;
  - the Tool32 steering-angle job name.
- Tenza's ABS light and ThaChileanDude's ABS light, tamper dot and check-engine light were never diagnosed on camera, and no follow-up videos were found.
- Videos with "first start" in the title but under a minute long (Wagon Guy, M346 ZHP, Jared Wise, cyberkaa) and other short clips were read from titles and descriptions only, if at all (see Q1).
- Creator replies in comments were not read.
