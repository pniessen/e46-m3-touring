# YouTube DIY videos for the S54 / E46 M3 swap: mechanical and chassis jobs

Research date: 22 October 2026. I read captions (manual where they exist, otherwise YouTube's auto-generated English track), chapters and descriptions through yt-dlp. No video or audio was downloaded, and raw caption files stay in the session scratchpad, not the repository.

How to read the citations:
- Each citation gives "Channel – Title (upload date), mm:ss" and links to that moment with `&t=`. Later timestamps from the same video in the same bullet are bare links.
- The tag after a citation says what I read: **[captions]**, **[chapters]**, **[description]**, or a title tag such as **[title only]**, **[search listing title]** or **[oEmbed title]** (only the title, from a YouTube search listing or oEmbed, was available).
- A timestamp marks the caption cue or chapter where the statement starts.
- Auto-captions mishear numbers, so I report only figures that are unambiguous in context and flag garbled ones.
- Quotes are short; everything else is summarised. ft-lb to Nm conversions are mine (1 ft-lb = 1.356 Nm).
- The BMW-sourced values I compare against are in `torque_specs.md` in this folder (mainly BMW SI B11 04 04 and the TIS-cited compilations it reviews).

**What I could and couldn't read.**
- **Captions read for eight videos:** FCP Euro's rod-bearing and valve-adjustment videos (manual captions), plus auto captions for The Bimmer Barn's rod bearings, Paul Vo, ECS Tuning's VANOS/valve video, M5x Mechanix, 50sKid's rack video and Throttle House's clutch-delay-valve video.
- **Then YouTube blocked further downloads.** Caption downloads from this session's shared egress were rate-limited (HTTP 429) for over 30 minutes while several researchers were fetching. After that, YouTube began answering with "Sign in to confirm you're not a bot".
- **What I did about it:** as instructed, I didn't try to get around either block. I stopped fetching and covered the rest from chapters, descriptions and titles.
- **No caption track at all:** six videos have none (FCP Euro's control-arm video, both FCP Euro clutch videos, Condor's diff-bushing video, Adam's INPA bleed video, and E46ISTHEBEST's fuel-test clip).

## Q1. Which videos are best for each job (channel, title, date, URL, length, captions)?

### Takeaway
The engine jobs have strong readable videos:
- FCP Euro's rod-bearing and valve-lash videos, with manual captions and nearly every step and torque on camera. The valve video was filmed on an S54-swapped E46 sedan.
- ECS Tuning's 2025 combined VANOS-and-valves video.

The chassis jobs are thin:
- FCP's M3 control-arm and M3 clutch videos have no captions, so only their chapters could be used.
- 50sKid's rack video is a non-M car and gives no torques.
- Every subframe-reinforcement, trailing-arm-bushing (RTAB), fuel-test and DSC-bleed video could be judged only from chapters and descriptions, because YouTube blocked the captions.

Three of the guide's links should change:
- the M5x valve video (weak);
- FCP's non-M clutch video (an M3-specific FCP video exists);
- the Treats On The Streets playlist (all E36).

### Cited Findings
| Job | Pick | Channel – title (upload date) | Length | Captions read | Why / caveats |
|---|---|---|---|---|---|
| S54 rod bearings | 1 | [FCP Euro – BMW S54 Rod Bearing Replacement DIY (2001-2006 BMW E46 M3) (2022-10-12)](https://www.youtube.com/watch?v=Emjw22o_V8c) | 51:43 | Manual English captions, 33 chapters | Most complete: every step and most torques on camera, M10 three-cycle procedure, Plastigauge, pan sealing. In-car (subframe lowered), so the removal half differs from stand work. Guide link, keep |
| | 2 | [Paul Vo – BMW E46 M3 Rod Bearing Installation & Torque Procedure (2017-05-30)](https://www.youtube.com/watch?v=O345BKC8EkM) | 14:34 | Auto captions (barely usable), 10 chapters, detailed description | Only video that shows the M10 back-off-and-repeat cycles being done at home on jack stands; description has part numbers and pitfalls. Guide link, keep |
| | 3 | [The Bimmer Barn – How to: Replace S54 Rod Bearings! (+ Checking Clearance w/Plastigauge) (2022-06-09)](https://www.youtube.com/watch?v=kb7PO3CtERE) | 17:28 | Auto captions, 7 chapters | Early M11 car, Plastigauge reading and angle-gauge technique; contains a spoken spec slip for M10 bolts (see Q3). Part 1 (pan removal) is a separate video. Guide link, keep with a warning |
| Valve adjustment | 1 | [FCP Euro – BMW E46 M3 Valve Adjustment DIY (BMW S54 Engine Valve Lash Adjustment) (2022-12-10)](https://www.youtube.com/watch?v=6xtAIiKbKmM) | 48:32 | Manual captions, 15 chapters | Filmed on an S54-swapped E46 sedan; full access, measurement, shim maths and reassembly torques. **Replace** the guide's M5x link with this |
| | 2 | [ECS Tuning – BMW S54 Valve Adjustment & VANOS Rebuild \| ECS DIY (2025-10-31)](https://www.youtube.com/watch?v=vhsxb5IRa8s) | 1:14:43 | Auto captions, 13 chapters | Valve section 12:41–17:29; useful because it does valves and VANOS in one teardown. Its plug and cover torques differ from FCP's |
| | — | [M5x Mechanix – BMW E46 M3 Valve Adjustment How To (Full easy walkthrough) (2025-07-09)](https://www.youtube.com/watch?v=mTcIK8Ryc04) | 23:28 | Auto captions, no chapters | Guide's current link. Only a few valves shown on camera, no shim arithmetic, and one misspoken spec. Keep only as a secondary clip |
| VANOS | 1 | [ECS Tuning – BMW S54 Valve Adjustment & VANOS Rebuild \| ECS DIY (2025-10-31)](https://www.youtube.com/watch?v=vhsxb5IRa8s) | 1:14:43 | Auto captions (machine-translated feel) | Newest and most complete: seals, solenoid test, anti-rattle preload, S62 springs, sprocket bolts, guide and tensioner, "magic tooth", diaphragm preload, torques. **Add** |
| | — | [Parker Repp – S54 VANOS REBUILD (Everything you need)](https://www.youtube.com/watch?v=rbhWLdmnp4U) | 14:54 (search listing) | **Not read**: YouTube "confirm you're not a bot" check; oEmbed gave only title and channel | Guide's current link; contents unverified |
| Tie rods and rack | 1 | [50sKid – BMW E46 Steering Rack Replacement DIY (2018-04-08)](https://www.youtube.com/watch?v=iwCoomDpICI) | 39:21 | Auto captions, 14 chapters | Non-M car but same rack mounting; good on lines, coupler and toe by eye; no torques; doesn't support the guide's "one spline off gives bump steer" sentence |
| Front control arms | 1 | [FCP Euro – How to Replace the Control Arms, Bushings, Ball Joints, Tie Rods, & End Links On A BMW E46 M3 (2020-06-05)](https://www.youtube.com/watch?v=usfbSLE_1aI) | 29:17 | **No caption track exists**; chapters and description only | M3-specific; step order only from chapters |
| Clutch, flywheel, RMS | 1 | [FCP Euro – BMW E46 M3 Clutch Replacement DIY (2001-2006 BMW M3) (2022-10-01)](https://www.youtube.com/watch?v=NmEOFBqreX8) | 36:33 | **No caption track**; 19 chapters, parts list | The M3-specific version, with RMS. **Replace** the guide's link, which is a non-M race car |
| | — | [FCP Euro – BMW E46 Clutch, Flywheel & Rear Main Seal Replacement DIY (330i, 325i, 330ci, 323i, 325ci, & More) (2020-07-24)](https://www.youtube.com/watch?v=5S7-gNEgJoM) | 45:15 | **No caption track**; 23 chapters | Guide's current link; Spec E46 race car with aluminium flywheel and E36 M3 clutch |
| Clutch delay valve | 1 | [Throttle House – BMW E46 Clutch Delay Valve delete DIY and REVIEW (2016-05-12)](https://www.youtube.com/watch?v=LDEty2tnZLQ) | 7:32 | Auto captions, 5 chapters | Short, clear removal with the hose-clamp trick; presenter is not a mechanic. Guide link, keep |
| Diff bushings | 1 | [Condor Speed Shop – E46 M3 Differential Bushing Install - E46 Coupe - Condor Speed Shop (2019-06-19)](https://www.youtube.com/watch?v=fcOohpFKZZE) | 2:15 | **No caption track** (music); 19 chapters carry the text | Quick order of work; its two torque figures conflict with the BMW-based values (Q3) |
| Rear subframe (whole) | — | [FCP Euro – BMW E46 M3 Rear Subframe Refresh DIY (Trailing Arm Bushings, Camber Arms, Differential Mounts)](https://www.youtube.com/watch?v=mKNPI5KTUK8) | 1:11:50 (search listing) | **Not read**: bot check; oEmbed title only | Likely the best single video for the M3 rear axle (≈298,000 views), but contents unverified here |
| Subframe reinforcement | — | [ECS Tuning – BMW E46 Subframe Reinforcement \| ECS DIY](https://www.youtube.com/watch?v=CL9L5MQbjpA) | 22:33 (search listing) | **Not read**: bot check; oEmbed title only | — |
| | — | [Treats On The Streets subframe playlist](https://www.youtube.com/playlist?list=PLd8QLEWWC1G1i5y7Eu4WLRFpttcEk4JxO) | 4 videos | Titles only | All four are **E36 M3**; the guide calls it "E36/E46" |
| Brake/DSC bleed | — | [Adam – ABS/DSC brake system bleeding with INPA BMW (2018-05-27)](https://www.youtube.com/watch?v=ZOPhh7dAbHA) | 5:17 | **No caption track**; step list in description | Generic INPA routine; car not named |
| VANOS on the stand | (lead) | [OnlyyDans – BMW S54 - Engine Build / Vanos Rebuild, Timing Procedure, and Valve Adjustment - Build Series Pt. 4 (2024-06-27)](https://www.youtube.com/watch?v=iDQEaRzFoTg); [CRANK – BMW S54 Timing Chain Procedure (2023-04-10)](https://www.youtube.com/watch?v=FTgMMSVow84) | 43:21; 55:24 | Auto captions exist but **not read** (rate limit); chapters only | The only engine-out (stand) sequences found for cams, VANOS and timing; worth watching for the guide's "on the stand" framing |
| VANOS (more) | (lead) | [The Bimmer Barn – BMW S54 Vanos Rebuild: Seals + Exhaust Sprocket UPGRADE! (2022-04-30)](https://www.youtube.com/watch?v=_1GnFql4G_E); [ShopLifeTV – E46 M3 S54 VANOS UPGRADED OIL PUMP DISK (S54 VANOS: PART 2) (2019-03-04)](https://www.youtube.com/watch?v=QjB-pDLadXk) | 27:03; 20:02 | **Not read** (bot check / rate limit); chapters and descriptions | ShopLifeTV's description is the only one found that explicitly covers the Beisan oil-pump disc swap the guide recommends (Geno Foster's Beisan video may too) |
| Subframe reinforcement | (lead) | [O'LearysGenuineBMW – BMW E46 Chassis/Subframe Reinforcement Done Right - Rear Bushings & Reinforcement Job (2024-06-26)](https://www.youtube.com/watch?v=leftkCgDfK0); [Tedward – BMW E46 M3 - How To INSPECT for Cracks and REINFORCE your Rear Subframe (2020-03-19)](https://www.youtube.com/watch?v=Ww5WNopJshk) | 21:55; 13:56 | **Not read** (bot check / rate limit); chapters only | O'Leary's is the guide's link and the newest; Tedward adds crack inspection and a trunk-floor step. Condor's plate video is music-only with a useful kit description |
| RTAB | (lead) | [SeanS54 – BimmerWorld Rear Trailing Arm Bearing (RTAB) Install - BMW E46 M3 (2017-10-27)](https://www.youtube.com/watch?v=_A6SqbMowgE) | 6:59 | **Not read** (rate limit); no chapters, one-line description | Guide's link; contents unverified |
| Fuel-pump test | (lead) | [LaRosa Drift – How to Check Fuel Pressure - E46 BMW (2022-11-17)](https://www.youtube.com/watch?v=t_JkzUQQ7Hs) | 7:06 | **Not read** (rate limit); chapters and description | An E46 drift-car project, model not stated; nothing indicates an S54, so don't expect the S54's 5 bar |
| DSC bleed | (lead) | [50sKid – BMW 330i 325i E46 Brake Bleeding Using INPA (2015-08-01)](https://www.youtube.com/watch?v=uKk0uc0Dnf4) | 7:47 | **Not read** (rate limit); short description | Non-M E46 |
| Engine removal | 1 | [DBO – How To Pull a BMW e46 Engine! (M3) (2019-04-28)](https://www.youtube.com/watch?v=SH-J8ngKerk) | 32:10 | Auto captions **not read** (rate limit); 12 chapters | Already in the guide; M3-specific |

Notes on the guide's current links:
- The guide's clutch link is a non-M race car. Its description says it is "a SPEC E46 race car" with a "Fidanza billet aluminum flywheel (11.8lbs)… along with an E36 M3 clutch" — [FCP Euro – BMW E46 Clutch, Flywheel & Rear Main Seal Replacement DIY (330i, 325i, 330ci, 323i, 325ci, & More) (2020-07-24), description](https://www.youtube.com/watch?v=5S7-gNEgJoM) [description]. FCP's M3-specific clutch video is [NmEOFBqreX8](https://www.youtube.com/watch?v=NmEOFBqreX8) [chapters].
- The guide's valve-lash link has about 250 views and no chapters. It shows only a few valves on camera and misstates the intake range once — [M5x Mechanix – BMW E46 M3 Valve Adjustment How To (Full easy walkthrough) (2025-07-09), 11:08](https://www.youtube.com/watch?v=mTcIK8Ryc04&t=668s) [captions]. FCP Euro's version is filmed on "an E46 sedan, obviously therefore a swapped car" — [FCP Euro – BMW E46 M3 Valve Adjustment DIY (BMW S54 Engine Valve Lash Adjustment) (2022-12-10), 00:00](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=0s) [captions].
- The guide labels the Treats On The Streets playlist "E36/E46", but all four titles are E36 M3 — [playlist](https://www.youtube.com/playlist?list=PLd8QLEWWC1G1i5y7Eu4WLRFpttcEk4JxO) [titles].
- The guide cites 50sKid's rack video for "Being one spline off gives bump steer and an off-center wheel". The video never mentions spline indexing or bump steer. It centres the new rack by matching its position to the old one and takes up the difference with the tie rods — [50sKid – BMW E46 Steering Rack Replacement DIY (2018-04-08), 22:31](https://www.youtube.com/watch?v=iwCoomDpICI&t=1351s) [captions].
- Condor's plate kit lists fitment as "E46 coupe & sedan", with "minor modification" for the convertible; the Touring isn't mentioned — [Condor Speed Shop – Rear Subframe Reinforcement Plate Install - E46 Coupe - Condor Speed Shop (2019-05-14), description](https://www.youtube.com/watch?v=TVBHLFNL6k4) [description].
- Every rod-bearing, valve and VANOS video found is an in-car job except OnlyyDans' and CRANK's, whose chapters show an engine being assembled (rockers, cams, chain), i.e. out of the car — [OnlyyDans – BMW S54 - Engine Build / Vanos Rebuild, Timing Procedure, and Valve Adjustment - Build Series Pt. 4 (2024-06-27), 12:28](https://www.youtube.com/watch?v=iDQEaRzFoTg&t=748s), [CRANK – BMW S54 Timing Chain Procedure (2023-04-10), 01:24](https://www.youtube.com/watch?v=FTgMMSVow84&t=84s) [chapters].

### Inferences
- **Link changes for the guide:**
  - Replace the valve link with FCP Euro's 6xtAIiKbKmM, and the clutch link with FCP Euro's NmEOFBqreX8.
  - Keep FCP Euro, Paul Vo and The Bimmer Barn for rod bearings. The Bimmer Barn's video needs a warning about its spoken M10 spec.
  - Add ECS Tuning's vhsxb5IRa8s for VANOS.
  - Relabel or drop the Treats On The Streets playlist, because E36 subframe and diff hardware differ from the E46 M3's.
- **Still unverified:** Parker Repp's VANOS video (the guide's link) and FCP Euro's M3 rear-subframe refresh, probably the best single rear-axle video. Someone with normal browser access should watch both before the guide relies on them.
- **Which steps apply on a stand:** the guide does the S54 work on a stand. The in-car videos' removal steps (dropping the subframe, working the pan out past the rack) don't apply there, but their bearing, shim and VANOS steps do. From their chapters, OnlyyDans and CRANK look like the right companions for cams, VANOS and timing on a stand.
- **Most useful for an amateur:** FCP's rod-bearing video (specs and pitfalls) and ECS's VANOS video (tools, sequence and torques). Both were read in full.

### Gaps
- **Blocked by YouTube's bot check** (not retried):
  - Parker Repp – S54 VANOS REBUILD (rbhWLdmnp4U)
  - FCP Euro – BMW E46 M3 Rear Subframe Refresh DIY (mKNPI5KTUK8)
  - ECS Tuning – BMW E46 Subframe Reinforcement (CL9L5MQbjpA)
  - O'LearysGenuineBMW (leftkCgDfK0) and The Bimmer Barn VANOS (_1GnFql4G_E), after their metadata had already been read
  - M539 Restorations PT13/PT14 (6NbgUPsl8og, FzIDIqXD0AE): my queue was stopped before reaching them, and another researcher's saved copies of both watch pages are bot-check pages
- **Captions exist but were rate-limited (429) and never downloaded:**
  - Engine: DBO engine pull, ShopLifeTV's oil-pump disc and valve videos, OnlyyDans, CRANK timing, Geno Foster, Evolve, The Bimmer Barn's valve video
  - Chassis: Condor plates, SeanS54 RTAB, Tedward, YEVS BUILDS
  - Fuel and brakes: LaRosa Drift, Electrical Car Repair LIVE, 50sKid's INPA and pressure-bleed videos
- **Never fetched:** the leads listed at the end of Q2's findings; their titles and lengths come from YouTube search only.
- **No caption track exists:**
  - FCP Euro: control arms (usfbSLE_1aI), M3 clutch (NmEOFBqreX8), non-M clutch (5S7-gNEgJoM)
  - Condor diff bushings (fcOohpFKZZE)
  - Adam's INPA bleed (ZOPhh7dAbHA)
  - E46ISTHEBEST fuel test (I8mLZuhiTzs)
- **Comments:** the brief allowed for creator answers in comments, but I read only Condor's diff-bushing comments (12), which add no specs. The next comment request hit the bot check, so I stopped.
- **Not found:**
  - an E46 M3 video that measures the S54's 5-bar, vacuum-referenced fuel pressure on camera;
  - an M3-specific DSC bleed video with readable captions.

## Q2. What does each video show: steps, tools, on-camera specs, time and pitfalls?

### Takeaway
The readable engine videos give an amateur a complete sequence for three jobs.
- **Rod bearings:**
  - Identify the bolts by their heads. The 12-point M11 bolts are reused. The E12 Torx M10 bolts are replaced and get three full cycles of 5 Nm, 30 Nm and 105°.
  - The blue shell goes in the rod and the red in the cap; Plastigauge should read 0.03–0.07 mm.
  - Clean and oil the new bolts before torquing.
  - The hardest part is rod #1 behind the oil pump.
- **Valves:**
  - Work cold, with the lobe pointing up. Aim for 0.20 mm intake and 0.30 mm exhaust.
  - Measure the old shim and choose the next size.
  - Don't drop shims; early heads have no screen to catch them.
- **VANOS:**
  - Turn the hubs fully clockwise and find the "magic tooth".
  - Preload the diaphragm springs with a quarter turn.
  - Lubricate the Teflon seals heavily, and shim the transfer gears to a slight preload.
  - Replace the sprocket bolts and check the upper chain guide.

The chassis videos that could be read add practical rack and clutch-delay-valve technique but almost no torques. Condor's diff-bushing torques conflict with BMW's (see Q3). None of the readable videos states a total job time; Paul Vo's description says to plan 3–7 days for a first rod-bearing job.

### Cited Findings
#### Rod bearings (S54)

**FCP Euro – BMW S54 Rod Bearing Replacement DIY (2001-2006 BMW E46 M3) (2022-10-12)** [manual captions + 33 chapters]. In-car job on a lift: engine held from above, front subframe lowered, whole oil pan removed, oil pump left in.

- Tools named: engine support bar; E12 Torx socket for the late rod bolts; a torque-angle wrench or mechanical angle gauge; thin 32 mm fan-clutch wrench with counter-hold; BMW's crank-turning adapter that fits over the four E12 balancer bolts; Plastigauge PG-1 (green), "BMW recommends"; assembly lube, RTV, paint pen; denatured alcohol to clean the new rod bolts — [FCP Euro – BMW S54 Rod Bearing Replacement DIY (2001-2006 BMW E46 M3) (2022-10-12), 01:20](https://www.youtube.com/watch?v=Emjw22o_V8c&t=80s), [02:14](https://www.youtube.com/watch?v=Emjw22o_V8c&t=134s), [02:40](https://www.youtube.com/watch?v=Emjw22o_V8c&t=160s), [03:33](https://www.youtube.com/watch?v=Emjw22o_V8c&t=213s) [captions]
- Step order (chapters): drain oil → splash shield and reinforcement plate → control-arm brackets and steering-shaft bolt → fan shroud, fan, intake → crank pulley and belts → engine support → sway bar → lower front subframe → oil pan → pickup tube → rods → Plastigauge → install → pan → reverse — [chapters 04:11–50:58](https://www.youtube.com/watch?v=Emjw22o_V8c&t=251s) [chapters]
- Drain plug is a 6 mm Allen that strips easily: seat the key fully — [04:33](https://www.youtube.com/watch?v=Emjw22o_V8c&t=273s) [captions]
- Fan clutch is left-hand thread — [07:13](https://www.youtube.com/watch?v=Emjw22o_V8c&t=433s) [captions]
- Remove the six 13 mm screws of the cover over the balancer bolts; never turn the engine by that cover — [09:39](https://www.youtube.com/watch?v=Emjw22o_V8c&t=579s) [captions]
- Subframe: four 18 mm bolts and four 13 mm sway-bar link nuts; unplug the headlight-level sensor lead before lowering, because the sensor goes down with the subframe but its lead doesn't — [11:10](https://www.youtube.com/watch?v=Emjw22o_V8c&t=670s), [11:19](https://www.youtube.com/watch?v=Emjw22o_V8c&t=679s) [captions]
- Pan: 17 mm swivel oil-return fitting (counter-hold), two E10 bell-housing-to-pan bolts, oil-level sensor, dipstick tube nut, PCV connector; removing the power-steering pump from the filter housing exposes two hidden 10 mm pan screws — [12:36](https://www.youtube.com/watch?v=Emjw22o_V8c&t=756s), [14:10](https://www.youtube.com/watch?v=Emjw22o_V8c&t=850s) [captions]
- Pickup tube: two 10 mm nuts plus two 4 mm Allens at the pump — [16:15](https://www.youtube.com/watch?v=Emjw22o_V8c&t=975s) [captions]
- Bolts: late engines have single-use E12 Torx bolts; early 12-point bolts are reused. Rods are fracture-split, so each cap fits one way — [16:59](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1019s), [17:28](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1048s) [captions]
- The upper (rod-side) shell carries the load and wears first; FCP's #6 upper was through to copper — [18:24](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1104s) [captions]
- ACL bearings are the same in both halves; genuine BMW shells are red and blue and position-specific — [18:53](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1133s) [captions]
- Clean the new bolts in denatured alcohol, then oil them so torque is reached at the bolt seat; put the Plastigauge on a clean, dry journal — [20:27](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1227s) [captions]
- Torque on camera: "five newton meters as a joining torque, 30 newton meters as a set torque and then 105 degrees of rotation, loosen", repeated twice more; the Plastigauge check is done on the first pass — [20:51](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1251s), [22:41](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1361s) [captions]
- Clearance stated as BMW's: "between 30 000 and 70 000 of a mil" (i.e. 0.030–0.070 mm); FCP read about 0.050 mm — [21:43](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1303s) [captions]
- The factory rod bolts "can be torqued up to five times", but a new bolt already uses three, so FCP fits new ones — [24:52](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1492s) [captions]
- Reassembly specs: oil-pump strainer, sensor and other M6 screws 10 Nm; drain plug 25 Nm with a new crush washer (check the old one isn't stuck on: a double washer leaks); pan bolts 10 Nm (84 in-lb), done by hand with a ¼-in ratchet; power-steering pump bolts 23 Nm; crank-pulley bolts 23 Nm — [29:26](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1766s), [29:55](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1795s), [30:05](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1805s), [35:15](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2115s), [38:07](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2287s), [39:18](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2358s) [captions]
- Pan sealing: new O-ring on the pickup tube (oiled); the return tube flange has no gasket; zip-tie the new gasket to the pan to hold it; RTV bead where the timing cover and rear-main-seal cover meet the block; start every bolt by hand, then pull the pan back with the bell-housing bolts before tightening the pan bolts. There are three pan-bolt lengths — [27:41](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1661s), [32:01](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1921s), [33:19](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1999s), [34:43](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2083s), [36:00](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2160s) [captions]
- Subframe refit: steering wheel straight ahead and the notch in the steering shaft lined up with the coupler bolt hole; tighten the rear subframe bolts first, because their dowels centre the subframe; subframe bolts 110 Nm; new E10 steering-shaft bolt 22 Nm; engine-mount nuts 45 Nm; control-arm bracket bolts 59 Nm — [39:54](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2394s), [40:37](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2437s), [40:58](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2458s), [41:14](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2474s), [41:26](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2486s), [42:06](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2526s) [captions]
- Reinforcement plate: new bolts, which FCP describes as torque-to-yield (caption: "towards the yield"), 59 Nm + 90° — [50:07](https://www.youtube.com/watch?v=Emjw22o_V8c&t=3007s), [50:15](https://www.youtube.com/watch?v=Emjw22o_V8c&t=3015s) [captions]
- Oil fill on camera: 6 L of 10W-60 — [47:21](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2841s) [captions]
- Break-in on camera: about 1,000 miles of varied driving, "don't redline it", then change the oil and have it analysed — [49:07](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2947s) [captions]
- Hardest part: reaching rod #1 with the oil pump still fitted — [51:17](https://www.youtube.com/watch?v=Emjw22o_V8c&t=3077s) [captions]

**The Bimmer Barn – How to: Replace S54 Rod Bearings! (+ Checking Clearance w/Plastigauge) (2022-06-09)** [auto captions + 7 chapters]. Part 2 of a two-part in-car job on a 2001 (M11-bolt) M3 with 145,000 miles; part 1 is "How to: Remove E46 M3 Oil Pan!" (hEDzMrrgARE).

- Tools: torque-angle gauge, ⅜-in torque wrench covering 5–30 Nm, Plastigauge ("ballpark" only), assembly lube — [01:03](https://www.youtube.com/watch?v=kb7PO3CtERE&t=63s), [01:38](https://www.youtube.com/watch?v=kb7PO3CtERE&t=98s) [captions]
- Bolt types: pre-2003 engines have the larger-headed M11 bolt, 2003-on the Torx M10; the rods differ, so the bolts don't interchange. Early bolts are "100% reusable according to BMW", late ones must be replaced — [The Bimmer Barn – How to: Replace S54 Rod Bearings! (+ Checking Clearance w/Plastigauge) (2022-06-09), 02:08](https://www.youtube.com/watch?v=kb7PO3CtERE&t=128s), [02:38](https://www.youtube.com/watch?v=kb7PO3CtERE&t=158s) [captions]
- Shells: blue in the rod (top), red in the cap (bottom), marked on the shell edge and the box; mixing them up risks "catastrophic engine failure" — [03:03](https://www.youtube.com/watch?v=kb7PO3CtERE&t=183s) [captions]
- Torque as spoken: "5, 30 and 70 degrees" for early cars, and "5, 30 and 105 newton meters" for post-2003 cars — [03:36](https://www.youtube.com/watch?v=kb7PO3CtERE&t=216s) [captions]. The second phrase is a slip (105 is degrees) and the three-cycle M10 procedure is never mentioned.
- Oil pump: he couldn't remove it because a 6 mm Allen bolt was already rounded, so he left it in and turned the engine to reach each rod pair (1/6, then the others) — [05:43](https://www.youtube.com/watch?v=kb7PO3CtERE&t=343s), [06:47](https://www.youtube.com/watch?v=kb7PO3CtERE&t=407s) [captions]
- Removal: crack the bolts, break the cap free, then remove; push the piston up and lift the upper shell out with a pick; mark M11 bolts to their caps — [06:53](https://www.youtube.com/watch?v=kb7PO3CtERE&t=413s), [07:26](https://www.youtube.com/watch?v=kb7PO3CtERE&t=446s), [07:48](https://www.youtube.com/watch?v=kb7PO3CtERE&t=468s) [captions]
- He lubes the upper shell before the Plastigauge check (it can't be reached afterwards) and puts the Plastigauge on the cap side — [10:08](https://www.youtube.com/watch?v=kb7PO3CtERE&t=608s) [captions]
- Clearance: "factory specs" 0.03–0.07 (mm); his strip was "a little bit skinnier than the 0.03 mark", which he called good (on Plastigauge a narrower strip means more clearance — my note) — [10:50](https://www.youtube.com/watch?v=kb7PO3CtERE&t=650s) [captions]
- Angle technique: two ways to use a dial angle gauge, with its reference arm braced against the bell housing; 70° on his M11 bolts — [11:56](https://www.youtube.com/watch?v=kb7PO3CtERE&t=716s), [12:16](https://www.youtube.com/watch?v=kb7PO3CtERE&t=736s) [captions]
- Break-in: "the first 1200 miles under 5,500 rpm" — [17:00](https://www.youtube.com/watch?v=kb7PO3CtERE&t=1020s) [captions]

**Paul Vo – BMW E46 M3 Rod Bearing Installation & Torque Procedure (2017-05-30)** [auto captions (very poor: music and mumbling) + 10 chapters + detailed description]. A 2004 M3 on jack stands, done alone over a weekend with the front subframe dropped.

- Front subframe dropped onto a jack as one assembly with the knuckles and rotors; the description lists what to undo first: strut bolts, sway-bar end links, ABS lines, calipers and the subframe bolts, with an engine support bar holding the engine — [Paul Vo – BMW E46 M3 Rod Bearing Installation & Torque Procedure (2017-05-30), 01:25](https://www.youtube.com/watch?v=O345BKC8EkM&t=85s) [chapters/captions], [description](https://www.youtube.com/watch?v=O345BKC8EkM) [description]
- Paper laid over the crank pin while pushing out shells, to avoid scratching the journal — [03:34](https://www.youtube.com/watch?v=O345BKC8EkM&t=214s) [captions]
- "Red cap": red shell to the cap (three letters each) — [04:19](https://www.youtube.com/watch?v=O345BKC8EkM&t=259s) [captions]
- The numbered side of the cap faces the passenger side — [06:17](https://www.youtube.com/watch?v=O345BKC8EkM&t=377s) [captions]
- Tools: E12 socket; a small torque wrench for 5 Nm ("you can hardly feel the click"); Snap-on ⅜ TechAngle wrench — [05:14](https://www.youtube.com/watch?v=O345BKC8EkM&t=314s), [06:46](https://www.youtube.com/watch?v=O345BKC8EkM&t=406s) [captions]
- Sequence shown: 5 Nm, 30 Nm, 105° (his wrench read 108°), back off 360°, two more cycles, final cycle left tight — [08:00](https://www.youtube.com/watch?v=O345BKC8EkM&t=480s), [10:55](https://www.youtube.com/watch?v=O345BKC8EkM&t=655s), [11:35](https://www.youtube.com/watch?v=O345BKC8EkM&t=695s) [captions]; the description spells out the same three cycles for "post 12/2002" cars, "Do not loosen rod bolts on the final torque" — [description](https://www.youtube.com/watch?v=O345BKC8EkM) [description]
- Description tips: his first attempt with the subframe in place rounded off most rod bolts, so drop the subframe and buy spare bolts; the oil-pump return line has a cone that must seat or the oil-pan cover bolts won't line up, so test-fit before bolting; push the power-steering lines rearward so they don't touch the sway bar or pan (his wore a mark in the pan); allow 3–7 days the first time. Parts list includes 6 red 11247835439, 6 blue 11247835440, 12 × 11247834310 M10 bolts, pan-cover gasket 11137832023 (before 04/2003) or 11137834886 (after), and 7 L of 10W-60 — [description](https://www.youtube.com/watch?v=O345BKC8EkM) [description]

#### Valve adjustment

**FCP Euro – BMW E46 M3 Valve Adjustment DIY (BMW S54 Engine Valve Lash Adjustment) (2022-12-10)** [manual captions + 15 chapters]. Filmed on an S54-swapped E46 sedan, so directly relevant to a swap.

- Car is "an E46 sedan, obviously therefore a swapped car"; the S54 has a solid valvetrain (rocker arms with shims, no hydraulic lifters); interval "every 25 to 30 000 miles" — [FCP Euro – BMW E46 M3 Valve Adjustment DIY (BMW S54 Engine Valve Lash Adjustment) (2022-12-10), 00:00](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=0s), [00:31](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=31s), [01:01](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=61s) [captions]
- Tools: 8/10/13/16/17 mm sockets, T25/T30/T50, BMW crank-turning socket, BMW feeler set, magnetic shim pick-up tool, a micrometer for shims, fan-clutch wrench set, spark-plug socket and thread-starter, a magnetic pick "just in case you drop a shim… it's pretty common" — [01:32](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=92s), [02:15](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=135s) [captions]
- Access order (chapters): splash shield → fan and shroud → cabin-filter cowl → belts → crank pulley/cover → valve cover → intake side → exhaust side → reassembly — [chapters](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=153s) [chapters]
- Pitfalls on the way in: the longest T25 shroud screw goes top right; mark belt direction if reusing belts; the crank-pulley cover has a 32 mm hex but it is stamped steel, so turn the engine on the four balancer bolts with BMW's adapter and inspect the balancer ("S54s are known for destroying harmonic balancers"); blow oil out of the plug tubes before pulling plugs (hydrolock risk); bolt the 13 mm coil-harness ground back finger-tight as a reminder — [05:35](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=335s), [08:09](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=489s), [09:42](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=582s), [12:29](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=749s), [13:42](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=822s) [captions]
- Later S54s have a plastic screen in the head's oil drain gallery to catch dropped shims; earlier ones don't — [16:34](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=994s) [captions]
- Method: plugs out, turn the engine clockwise, intake side first; lobe pointing straight up (base circle on the follower) for the valve being measured — [17:19](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1039s), [17:49](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1069s) [captions]
- Intake spec 0.18–0.23 mm, target 0.20 with light drag; 0.25 mm must not enter, 0.15 mm enters freely — [18:06](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1086s), [19:11](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1151s), [19:23](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1163s) [captions]
- Shim swap: unclip the rocker retainer, slide the rocker aside, lift the shim with BMW's magnet tool, measure it (2.28 mm), fit a thinner one to open a tight valve (2.24 mm, −0.04 mm), number side down; re-clip until it bottoms — [20:22](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1222s), [21:09](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1269s), [21:45](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1305s), [22:09](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1329s), [22:23](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1343s), [23:03](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1383s) [captions]
- Temperature: BMW requires coolant below 35 °C; he measured after the car sat over a day — [24:11](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1451s) [captions]
- Exhaust spec 0.28–0.33 mm, target 0.30, 0.35 mm must not enter; exhaust shims fall out easily because of the valve angle, so seat them carefully; used shims can be reused — [25:31](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1531s), [26:44](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1604s), [28:16](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1696s) [captions]
- Reassembly specs: spark plugs M12×1.25, dry (no anti-seize), 23 Nm; thin RTV at the VANOS-to-head joint and at the rear half-moons; the three front cap nuts take the thinner grommets; valve-cover cap nuts 10 Nm in a cross pattern; PCV return banjo 19 Nm with new washers; push coil connectors fully home by hand before closing the lock, or you get a misfire — [30:21](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1821s), [31:23](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1883s), [32:25](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1945s), [34:27](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=2067s), [34:58](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=2098s), [36:06](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=2166s), [38:43](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=2323s) [captions]

**ECS Tuning – BMW S54 Valve Adjustment & VANOS Rebuild | ECS DIY (2025-10-31)**, valve section [auto captions; the narration reads like a machine translation, e.g. "puck"/"washer" for shim].

- Turns the engine with a 32 mm socket on the crank bolt; intake 0.18–0.23 mm checked with 0.15/0.20/0.25 feelers; exhaust 0.28–0.33 mm with 0.25/0.30/0.35 — [ECS Tuning – BMW S54 Valve Adjustment & VANOS Rebuild | ECS DIY (2025-10-31), 12:50](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=770s), [16:58](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1018s) [captions]
- Example: a loose intake valve (0.25 felt right) went from a 2.24 mm to a 2.28 mm shim; shims measured with a caliper; refitting the shim needs patience and you hear a click when it seats in the spring retainer — [14:21](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=861s), [14:53](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=893s), [15:23](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=923s) [captions]
- Reassembly specs that differ from FCP's: plugs "18 ft-lbs or 25 Nm"; valve-cover cap nuts "6 foot-pounds or 8 newton-meters"; check the gasket's rear half-moons with a mirror, as unseated ones are "guaranteed to leak" — [1:11:04](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4264s), [1:12:08](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4328s), [1:13:45](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4425s) [captions]

**M5x Mechanix – BMW E46 M3 Valve Adjustment How To (Full easy walkthrough) (2025-07-09)** [auto captions, no chapters, about 250 views]. A 2003 M3; shows only a few valves on each side, the rest done off camera.

- Uses go/no-go feelers: 0.20 for intake (should drag), 0.254 must not enter; exhaust 0.30, with 0.35 as no-go — [M5x Mechanix – BMW E46 M3 Valve Adjustment How To (Full easy walkthrough) (2025-07-09), 01:19](https://www.youtube.com/watch?v=mTcIK8Ryc04&t=79s), [14:55](https://www.youtube.com/watch?v=mTcIK8Ryc04&t=895s) [captions]
- Early M3s lack the drain-gallery screens, so pack the valley with rags; his 2003 car had them — [09:00](https://www.youtube.com/watch?v=mTcIK8Ryc04&t=540s), [09:26](https://www.youtube.com/watch?v=mTcIK8Ryc04&t=566s) [captions]
- The engine is canted, so hold the feeler square to the valve, not vertical — [16:13](https://www.youtube.com/watch?v=mTcIK8Ryc04&t=973s) [captions]
- Mis-statement: "the spec is from 0.18 to 0.19" — [11:08](https://www.youtube.com/watch?v=mTcIK8Ryc04&t=668s) [captions]; he gave 0.18–0.23 earlier.

**Other valve-adjustment videos (chapters and descriptions only):**

- **ShopLifeTV – Do E46 M3 need Valve Adjustment? How To: BMW M3 S54 Valve Adjustment! (2021-12-02)**, 23:13. Description gives intake 0.18–0.23 mm (0.007–0.009 in) and exhaust 0.28–0.33 mm (0.011–0.013 in), and corrects the video's interval: first adjustment at 15–20k miles, then every 20–30k. Chapters include measuring 09:49, removing shims 13:30, measuring the shim with a caliper 15:00, rechecking 20:13 — [ShopLifeTV – Do E46 M3 need Valve Adjustment? How To: BMW M3 S54 Valve Adjustment! (2021-12-02), 13:30](https://www.youtube.com/watch?v=2jPRb34JSKg&t=810s), [15:00](https://www.youtube.com/watch?v=2jPRb34JSKg&t=900s) [chapters], [description](https://www.youtube.com/watch?v=2jPRb34JSKg) [description]
- **The Bimmer Barn – How to: S54 Valve Adjustment (+Valve Cover DIY) (2022-04-26)**, 16:06: description says "every 30-40k miles"; chapters intake 07:05–11:58, exhaust 11:58 — [The Bimmer Barn – How to: S54 Valve Adjustment (+Valve Cover DIY) (2022-04-26), 07:05](https://www.youtube.com/watch?v=eLskvIMDOIs&t=425s) [chapters], [description](https://www.youtube.com/watch?v=eLskvIMDOIs) [description]

#### VANOS

**ECS Tuning – BMW S54 Valve Adjustment & VANOS Rebuild | ECS DIY (2025-10-31)** [auto captions + 13 chapters]. Full in-car job: seals, solenoid pack, anti-rattle shims, hub diaphragm springs, sprocket bolts, upper guide and tensioner, timing check. Says it also applies to Z3 M and Z4 M S54s.

- Special tools: S54 timing set (cam bridge, two locking pins, crank pin); transfer-gear holder and socket; crank socket — "a four-turn head or a 32-turn head" depending on S54 year (garbled; probably the four-bolt adapter or a 32 mm socket); 32 mm deep socket for the chain tensioner; fan-clutch wrench and counter-hold — [ECS Tuning – BMW S54 Valve Adjustment & VANOS Rebuild | ECS DIY (2025-10-31), 01:30](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=90s), [02:01](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=121s), [02:31](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=151s) [captions]
- Access: battery off; xenon control unit and airbox out; fan clutch is reverse-thread (loosen clockwise); cowl and microfilter housing out; the crankcase-vent hose clips crack easily, so buy a new hose; 17 mm banjo on the valve-cover drain tube; 15 cap nuts, no sequence — [02:31](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=151s), [05:36](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=336s), [08:19](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=499s), [11:00](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=660s), [11:31](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=691s) [captions]
- Removal: unplug the solenoid, crack the pressure-relief valve, rag over the oil-cooler hose, remove the solenoid block (five 5 mm hex screws, support it, keep the gasket) — [17:30](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1050s), [18:01](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1081s) [captions]
- TDC: cylinder 1 lobes facing each other, the two holes pointing up, then insert the crank pin (use a mirror) — [18:31](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1111s), [19:01](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1141s) [captions]
- Turn each cam to the retard position with a 24 mm wrench on the cam hex (counter-clockwise); remove the upper chain guide (two 5 mm hex), the 14 mm oil-line banjo (keep the washer), the line brackets including a hidden 10 mm bolt under the lower radiator hose, and the three lower 5 mm VANOS bolts; hang the unit on two long solenoid bolts to reach the transfer-gear nuts (7 mm and 10 mm open-ends, reverse thread) — [19:31](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1171s), [20:01](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1201s), [20:33](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1233s), [21:04](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1264s), [21:34](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1294s), [22:09](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1329s) [captions]
- Solenoid pack: four E5 Torx; test each plunger with a strong magnet (a faint click each), flush with brake cleaner; new Teflon and rubber rings and filter on the pressure-relief valve; coil screws 4 Nm — [23:11](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1391s), [24:11](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1451s), [24:45](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1485s), [27:02](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1622s) [captions]
- Oil-pressure regulator: two new O-rings, check the piston springs back, refit with its holes at 9 and 3 o'clock — [27:32](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1652s), [28:35](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1715s) [captions]
- Piston seals: cut old rings without scratching the piston; Viton ring first, then the Teflon ring, warmed in warm water or the hand so it stretches without twisting; tuck the inner bore seal in with round-nose pliers; oil heavily and park the piston in the bore for a minute to size the Teflon. ECS admits an earlier under-lubricated seal was damaged and had to be replaced. A worn Teflon ring sitting flush with the piston no longer seals. Cover screws 7 ft-lb (10 Nm) — [29:35](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1775s), [30:19](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1819s), [31:50](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1910s), [33:26](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2006s), [36:20](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2180s), [39:52](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2392s) [captions]
- Rattle cure: "VANOS knock" is axial play in the transfer-gear bearings; fit the new race and end washers, torque the gear cover to 55 Nm (40.5 ft-lb), then aim for no axial play and slight rotating preload (adjustment window about 0.005–0.015 mm) by lapping the race (to tighten) or end washers (to loosen) on 400-grit paper, 30–40 strokes, rotating 90° each set — [42:13](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2533s), [42:43](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2563s), [45:01](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2701s), [45:31](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2731s), [46:32](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2792s) [captions]
- Hubs: rags into the timing cover; replace the diaphragm spring and pressure plate with the S62 parts (spring convex side down, plate "B" side up in its groove) — [47:02](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2822s), [48:21](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2901s) [captions]
- Exhaust sprocket bolts: BMW's updated Torx bolts replace the old hex ones, which shear and let the sprocket move on the hub; blue thread-locker, 12 Nm — [48:51](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2931s), [49:52](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2992s) [captions]
- Upper guide and tensioner: tensioner out with a 32 mm deep socket; the upper guide was broken (common on high-mileage S54s), fish out the pieces; guide bolt 24 Nm; new tensioner washer, snug plus half a turn — [50:31](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3031s), [51:34](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3094s), [52:40](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3160s), [53:10](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3190s) [captions]
- Timing: new M6×25 hub bolts finger-tight, hub tabs horizontal with the hole up; crank pin still in; cam bridge between cylinders 2 and 3 (E = intake, A = exhaust), the pin must slide in freely and the bridge sit flat — [53:40](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3220s), [54:41](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3281s), [55:11](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3311s) [captions]
- "Magic tooth": with the hub turned fully clockwise, find the one transfer-gear tooth position whose straight splines enter with no hub rotation; mark gear and hub — [56:13](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3373s), [58:47](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3527s) [captions]
- Refit: gasket flange toward the VANOS, tabs under it; hubs fully clockwise ("very important"); align the oil-pump disc lugs; stop with about 5 mm gap to the head, snug four opposing hub bolts then back each off exactly a quarter turn (diaphragm-spring preload); draw the unit in evenly with the two upper bolts while watching that the cams don't move and the gasket stays on its dowels; lower VANOS bolts 10 Nm; snug the reachable hub bolts, then pull the bridge and crank pin, turn the engine 360°, re-pin and do the next set, aiming for about 14 Nm (10.5 ft-lb) by feel because there's no room for a torque wrench; finally turn the cams to retard with the 24 mm and recheck with the bridge — [59:52](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3592s), [1:00:22](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3622s), [1:02:10](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3730s), [1:02:40](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3760s), [1:04:18](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3858s), [1:04:52](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3892s), [1:06:17](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3977s), [1:07:21](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4041s) [captions]
- Finish: braided VANOS oil line routed round the AC compressor; new plate gasket under the solenoid block, screws 10 Nm; pressure-relief valve (22 mm) tightened until it bottoms on its O-ring — [1:07:51](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4071s), [1:09:53](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4193s), [1:10:27](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4227s) [captions]

**Other VANOS videos (captions could not be read; chapters and descriptions only):**

- **The Bimmer Barn – BMW S54 Vanos Rebuild: Seals + Exhaust Sprocket UPGRADE! (2022-04-30)**, 27:03. Chapters: unit removal 01:20, disassembly 04:26, internal seals 06:18, "manifold" cleaning 14:00, exhaust sprocket upgrade 17:00, reinstallation 19:19, start and test 25:15 — [The Bimmer Barn – BMW S54 Vanos Rebuild: Seals + Exhaust Sprocket UPGRADE! (2022-04-30), 01:20](https://www.youtube.com/watch?v=_1GnFql4G_E&t=80s), [17:00](https://www.youtube.com/watch?v=_1GnFql4G_E&t=1020s), [19:19](https://www.youtube.com/watch?v=_1GnFql4G_E&t=1159s) [chapters]. Description: new seals plus "an upgrade exhaust sprocket" — [description](https://www.youtube.com/watch?v=_1GnFql4G_E) [description]
- **ShopLifeTV – E46 M3 S54 VANOS UPGRADED OIL PUMP DISK (S54 VANOS: PART 2) (2019-03-04)**, 20:02. Chapters: engine disassembly 02:13, timing and locking 05:05, unit removal 06:47, disassembly 09:30, oil-pump disc 12:54, pump reassembly 16:46 — [ShopLifeTV – E46 M3 S54 VANOS UPGRADED OIL PUMP DISK (S54 VANOS: PART 2) (2019-03-04), 05:05](https://www.youtube.com/watch?v=QjB-pDLadXk&t=305s), [12:54](https://www.youtube.com/watch?v=QjB-pDLadXk&t=774s) [chapters]. The description lists the series' scope: a re-drilled Beisan oil-pump disc, all VANOS seals, hub sprocket bolts, spring diaphragms, O-rings and gaskets, the anti-rattle kit, and a timing check; tools listed are an S54 timing tool and a flywheel locking pin — [description](https://www.youtube.com/watch?v=QjB-pDLadXk) [description]
- **OnlyyDans – BMW S54 - Engine Build / Vanos Rebuild, Timing Procedure, and Valve Adjustment - Build Series Pt. 4 (2024-06-27)**, 43:21. With CRANK's, the only VANOS videos found whose chapters show an engine being assembled rather than an in-car job: VANOS seals 02:22–10:57, rocker arms 12:28, camshafts 17:23, valve shims 22:10, timing bridge 26:40, hubs and sprockets 29:19, chain 31:05, setting timing 34:04, VANOS install 37:13, final timing check 39:33, final torquing 41:45 — [OnlyyDans – BMW S54 - Engine Build / Vanos Rebuild, Timing Procedure, and Valve Adjustment - Build Series Pt. 4 (2024-06-27), 12:28](https://www.youtube.com/watch?v=iDQEaRzFoTg&t=748s), [22:10](https://www.youtube.com/watch?v=iDQEaRzFoTg&t=1330s), [34:04](https://www.youtube.com/watch?v=iDQEaRzFoTg&t=2044s), [41:45](https://www.youtube.com/watch?v=iDQEaRzFoTg&t=2505s) [chapters]. The description is empty.
- **CRANK – BMW S54 Timing Chain Procedure (2023-04-10)**, 55:24, part 7 of an engine-build series, so the engine is apart: timing cover 01:24, crank timing 05:45, crank-bolt torque 09:34, cam locking 13:34, chain 22:35, VANOS spline-gear setup 26:59, VANOS install 34:03, final torque 41:32, timing correction 46:33, "Oil pump and safety wire" 50:20 — [CRANK – BMW S54 Timing Chain Procedure (2023-04-10), 09:34](https://www.youtube.com/watch?v=FTgMMSVow84&t=574s), [46:33](https://www.youtube.com/watch?v=FTgMMSVow84&t=2793s), [50:20](https://www.youtube.com/watch?v=FTgMMSVow84&t=3020s) [chapters]. The description says it compares OEM and "Chinese" timing tools (crank pin and cam bridge) — [description](https://www.youtube.com/watch?v=FTgMMSVow84) [description]
- **Evolve Automotive – E46 M3 VANOS Failure - Why it happens + how to fix it with Mr VANOS - M3 CSL + Z3 M Coupe S54 (2022-07-23)**, 23:24: a specialist (Mr VANOS) explains failures; the description lists the symptoms "noisy, rattle, lazy actuation, broken bolts and leaking oil" — [Evolve Automotive – E46 M3 VANOS Failure - Why it happens + how to fix it with Mr VANOS - M3 CSL + Z3 M Coupe S54 (2022-07-23), 05:26](https://www.youtube.com/watch?v=_jzNPBuySDs&t=326s) [chapters], [description](https://www.youtube.com/watch?v=_jzNPBuySDs) [description]
- **Geno Foster – High Mileage E46 M3 Vanos Bulletproofing! - Beisan Systems (2020-10-17)**, 9:32: description says the job at 200k miles showed "pretty surprising results as far as the condition of the sprocket tabs" and cured a P0014 code — [Geno Foster – High Mileage E46 M3 Vanos Bulletproofing! - Beisan Systems (2020-10-17), description](https://www.youtube.com/watch?v=YID3BgKGNyg) [description]
- Beisan Systems' own channel (GetVanosParts) has only short clips, e.g. "S54 Vanos Issues & Solutions" (4:17) and "S54 Vanos Solenoid Pack Rebuild" (12:52); I found no full Beisan procedure video — [GetVanosParts – S54 Vanos Issues & Solutions](https://www.youtube.com/watch?v=MqV55hUXb58), [GetVanosParts – S54 Vanos Solenoid Pack Rebuild](https://www.youtube.com/watch?v=V-jQNTEc8B8) [search listing titles]

#### Rear subframe mount reinforcement

No reinforcement video's captions could be read: O'Leary's and the ECS video hit YouTube's bot check, and the others were caught by the rate limit. What the metadata shows:

- **O'LearysGenuineBMW – BMW E46 Chassis/Subframe Reinforcement Done Right - Rear Bushings & Reinforcement Job (2024-06-26)**, 21:55. Chapters: subframe removal 01:12, surface preparation 03:21, applying primer 06:34, "Drilling for reinforcement" 08:07, "Subframe modification" 12:30, "Welding and coating" 16:09, final assembly 18:38 — [O'LearysGenuineBMW – BMW E46 Chassis/Subframe Reinforcement Done Right - Rear Bushings & Reinforcement Job (2024-06-26), 03:21](https://www.youtube.com/watch?v=leftkCgDfK0&t=201s), [08:07](https://www.youtube.com/watch?v=leftkCgDfK0&t=487s), [12:30](https://www.youtube.com/watch?v=leftkCgDfK0&t=750s), [16:09](https://www.youtube.com/watch?v=leftkCgDfK0&t=969s) [chapters]. Description: "the usual process I do… for a BMW E46"; the body style isn't stated — [description](https://www.youtube.com/watch?v=leftkCgDfK0) [description]
- **Tedward – BMW E46 M3 - How To INSPECT for Cracks and REINFORCE your Rear Subframe (2020-03-19)**, 13:56, filmed at Wile Motorsport. Chapters: identifying cracks 01:03, removing the subframe 03:07, detailed inspection 04:50, welding and reinforcement 06:53, protecting the repairs 09:08, trunk-floor reinforcement 10:57, severe cases 12:04; the description adds a floor so far gone it "required a full replacement" — [Tedward – BMW E46 M3 - How To INSPECT for Cracks and REINFORCE your Rear Subframe (2020-03-19), 04:50](https://www.youtube.com/watch?v=Ww5WNopJshk&t=290s), [09:08](https://www.youtube.com/watch?v=Ww5WNopJshk&t=548s), [10:57](https://www.youtube.com/watch?v=Ww5WNopJshk&t=657s) [chapters], [description](https://www.youtube.com/watch?v=Ww5WNopJshk) [description]
- **YEVS BUILDS – BMW E46 M3 | Rear Subframe Reinforcement DIY - Removing the Subframe Pt 1 (2021-08-31)**, 12:54. Chapters: exhaust and driveline 01:06, interior and brakes 01:51, subframe 03:29, fuel tank 04:57, cleaning the mounts 06:08, weld prep 07:53, trunk prep 10:26 — [YEVS BUILDS – BMW E46 M3 | Rear Subframe Reinforcement DIY - Removing the Subframe Pt 1 (2021-08-31), 03:29](https://www.youtube.com/watch?v=R2k5cd7Lor4&t=209s), [04:57](https://www.youtube.com/watch?v=R2k5cd7Lor4&t=297s) [chapters]
- **Condor Speed Shop – Rear Subframe Reinforcement Plate Install - E46 Coupe - Condor Speed Shop (2019-05-14)**, 4:15 (the guide's link; music video). Description: 14-gauge steel plates; kit has two M12×1.5 bolts, two front-mount plates, one right and one left rear-mount plate, two crossmember spacers and two square trunk block-off plates; fitment "E46 coupe & sedan", convertible "requires minor modification"; "professional installation is recommended". The Touring isn't listed — [Condor Speed Shop – Rear Subframe Reinforcement Plate Install - E46 Coupe - Condor Speed Shop (2019-05-14), description](https://www.youtube.com/watch?v=TVBHLFNL6k4) [description]
- **M539 Restorations, Project Cologne**: "Fixing & Reinforcing Factory Weak Points - BMW E46 330i - Project Cologne: PT13" (40:41) and "BMW E46 M3 Rear-End Restoration - Project Cologne: PT 14" (1:06:25). Other episodes call the car a "BMW E46 325i Touring" (Parts 3 and 6), so PT13's "330i" label is inconsistent. My queue was stopped before reaching them, and another researcher's saved copies of both watch pages are YouTube bot-check pages, so only the titles are known — [M539 Restorations – PT13](https://www.youtube.com/watch?v=6NbgUPsl8og), [PT14](https://www.youtube.com/watch?v=FzIDIqXD0AE), [Part 3](https://www.youtube.com/watch?v=dQyzcomasIE) [search listing titles]
- **ECS Tuning – BMW E46 Subframe Reinforcement | ECS DIY** (22:33): bot check; title from oEmbed only — [ECS Tuning – BMW E46 Subframe Reinforcement | ECS DIY](https://www.youtube.com/watch?v=CL9L5MQbjpA) [oEmbed title]

#### Rear subframe, trailing-arm and diff bushings

**Condor Speed Shop – E46 M3 Differential Bushing Install - E46 Coupe - Condor Speed Shop (2019-06-19)** [19 chapters (on-screen text); no caption track; music only]. Condor's UHMW solid diff bushings; fitment E46 M3 and Z4 M.

- Order: the diff can come out with the subframe on or off the car → disconnect end links and remove the sway bar → disconnect the half-shafts → support the diff and remove the two rear E12 Torx bolts → remove the 21 mm front bolt → lower the diff → press out the old bushing → install the new one (no grease needed; mallet or press) → refit — [Condor Speed Shop – E46 M3 Differential Bushing Install - E46 Coupe - Condor Speed Shop (2019-06-19), 00:16](https://www.youtube.com/watch?v=fcOohpFKZZE&t=16s), [00:33](https://www.youtube.com/watch?v=fcOohpFKZZE&t=33s), [00:42](https://www.youtube.com/watch?v=fcOohpFKZZE&t=42s), [00:54](https://www.youtube.com/watch?v=fcOohpFKZZE&t=54s), [01:05](https://www.youtube.com/watch?v=fcOohpFKZZE&t=65s) [chapters]
- Torque in the chapter titles: "Insert Torx bolts and torque to 70 ft-lbs" (≈95 Nm, rear) and "Insert 21mm bolt and torque to 128 ft-lbs" (≈174 Nm, front); then refit axles and sway bar "and torque to spec", and get an alignment — [01:32](https://www.youtube.com/watch?v=fcOohpFKZZE&t=92s), [01:42](https://www.youtube.com/watch?v=fcOohpFKZZE&t=102s), [01:50](https://www.youtube.com/watch?v=fcOohpFKZZE&t=110s), [01:58](https://www.youtube.com/watch?v=fcOohpFKZZE&t=118s) [chapters]

**Treats On The Streets subframe playlist** (PLd8QLEWWC1G1i5y7Eu4WLRFpttcEk4JxO) [titles only]: its four videos are "E36 M3 Subframe Removal for a FULL REBUILD! *Step by step DIY*", "E36 M3 Subframe & LSD get OVERHAULED", "E36 M3 GETS NEW DIFF AND SUBFRAME BUSHINGS!" and "ARE POLYURETHANE BUSHINGS WORTH IT? (Subframe & differential bushings review)" — [playlist](https://www.youtube.com/playlist?list=PLd8QLEWWC1G1i5y7Eu4WLRFpttcEk4JxO) [titles]. It is E36 M3 content, not E46.

**Other rear-bushing videos (titles or descriptions only):**

- **SeanS54 – BimmerWorld Rear Trailing Arm Bearing (RTAB) Install - BMW E46 M3 (2017-10-27)**, 6:59, the guide's RTAB link: no chapters; the description only says it installs BimmerWorld's spherical RTAB kit; captions blocked — [SeanS54 – BimmerWorld Rear Trailing Arm Bearing (RTAB) Install - BMW E46 M3 (2017-10-27), description](https://www.youtube.com/watch?v=_A6SqbMowgE) [description]
- **FCP Euro – BMW E46 M3 Rear Subframe Refresh DIY (Trailing Arm Bushings, Camber Arms, Differential Mounts)**, 1:11:50, about 298,000 views: bot check, title only — [FCP Euro – BMW E46 M3 Rear Subframe Refresh DIY](https://www.youtube.com/watch?v=mKNPI5KTUK8) [oEmbed title; length and views from search listing]
- **The Bimmer Barn – Must Have E46 Mods: RTAB + Diff Bushings! Powerflex DIY Upgrade** (16:58) and **Geno Foster – Change Out These Bushings ASAP! | BMW E46 M3** (9:24): titles only — [The Bimmer Barn](https://www.youtube.com/watch?v=1ybK4HgwIf0), [Geno Foster](https://www.youtube.com/watch?v=q-cr3s91ON4) [search listing titles]

#### Front control arms

**FCP Euro – How to Replace the Control Arms, Bushings, Ball Joints, Tie Rods, & End Links On A BMW E46 M3 (2020-06-05)** [chapters + description only; the video has no caption track of any kind]. 29:17, M3-specific (fitment 2001–06 M3), Lemförder arms.

- Step order from the chapters: tools (01:37) → remove reinforcement plate (03:00) → outer ball joint (04:32) → inner ball joint (06:54) → tie rod (08:37) → replace bushings (12:23) → reinstall control arms (15:58) → outer ball joint (19:05) → tie rods (19:49) — [FCP Euro – How to Replace the Control Arms, Bushings, Ball Joints, Tie Rods, & End Links On A BMW E46 M3 (2020-06-05), 03:00](https://www.youtube.com/watch?v=usfbSLE_1aI&t=180s), [06:54](https://www.youtube.com/watch?v=usfbSLE_1aI&t=414s), [12:23](https://www.youtube.com/watch?v=usfbSLE_1aI&t=743s), [15:58](https://www.youtube.com/watch?v=usfbSLE_1aI&t=958s), [19:49](https://www.youtube.com/watch?v=usfbSLE_1aI&t=1189s) [chapters]
- The description says the job includes "pressing in new bushings" and points to a written version on FCP's blog — [description](https://www.youtube.com/watch?v=usfbSLE_1aI) [description]

#### Tie rods and steering rack

**50sKid – BMW E46 Steering Rack Replacement DIY (2018-04-08)** [auto captions + 14 chapters]. 50sKid's own non-M E46 (his pressure-bleed video's description calls it a 2002 330i); the rack-to-subframe mounting and steering coupler are laid out the same way as the M3's, but it is not M3 footage.

- Break the tie-rod lock nut (22 mm, 19 mm on the other flat) while the tie-rod end is still in the knuckle, so the rod is braced — [50sKid – BMW E46 Steering Rack Replacement DIY (2018-04-08), 03:56](https://www.youtube.com/watch?v=iwCoomDpICI&t=236s), [04:13](https://www.youtube.com/watch?v=iwCoomDpICI&t=253s) [captions]
- Pop the tie-rod end with a hammer on the knuckle or a puller; keep fingers clear as it "pops pretty violently" — [04:20](https://www.youtube.com/watch?v=iwCoomDpICI&t=260s), [05:19](https://www.youtube.com/watch?v=iwCoomDpICI&t=319s) [captions]
- Count the turns as you unscrew the outer end (18½ here) so toe is close when it goes on the new rack; "you absolutely need to get an alignment" — [06:22](https://www.youtube.com/watch?v=iwCoomDpICI&t=382s), [06:39](https://www.youtube.com/watch?v=iwCoomDpICI&t=399s) [captions]
- Lines: 19 mm and 22 mm fittings on the rack, 17 mm at the pump (use a line wrench); aluminium sealing washers on each side of the banjo-type fittings can drop onto the pan, so catch them and preferably replace them — [07:54](https://www.youtube.com/watch?v=iwCoomDpICI&t=474s), [08:28](https://www.youtube.com/watch?v=iwCoomDpICI&t=508s), [08:53](https://www.youtube.com/watch?v=iwCoomDpICI&t=533s), [10:58](https://www.youtube.com/watch?v=iwCoomDpICI&t=658s) [captions]
- Rack mounting: two bolts to the subframe, 16 mm nuts on top and 15 mm heads below; on his car the rack came out forward without lowering the subframe — [03:01](https://www.youtube.com/watch?v=iwCoomDpICI&t=181s), [11:35](https://www.youtube.com/watch?v=iwCoomDpICI&t=695s) [captions]
- Coupler: E10 external-Torx pinch bolts; lock the steering column first so it can't turn; loosen both coupler bolts while the rack is still bolted in; the coupler collar's indent must line up with the pinch bolt — [12:35](https://www.youtube.com/watch?v=iwCoomDpICI&t=755s), [13:20](https://www.youtube.com/watch?v=iwCoomDpICI&t=800s), [14:51](https://www.youtube.com/watch?v=iwCoomDpICI&t=891s), [21:43](https://www.youtube.com/watch?v=iwCoomDpICI&t=1303s) [captions]
- Centring: he centres the new rack by matching its input position (bolt hole) to the old rack's and takes up small differences on the tie rods — [22:31](https://www.youtube.com/watch?v=iwCoomDpICI&t=1351s) [captions]. Nothing in the video concerns spline indexing or bump steer.
- Parts lesson: an eBay aftermarket rack's hard lines hit the subframe and it was unusable; a remanufactured ZF unit fitted; the pressure line he bought had the wrong bend — [23:35](https://www.youtube.com/watch?v=iwCoomDpICI&t=1415s), [25:23](https://www.youtube.com/watch?v=iwCoomDpICI&t=1523s), [26:06](https://www.youtube.com/watch?v=iwCoomDpICI&t=1566s), [27:35](https://www.youtube.com/watch?v=iwCoomDpICI&t=1655s), [30:08](https://www.youtube.com/watch?v=iwCoomDpICI&t=1808s) [captions]
- The two rack lines are different sizes (bigger one at the bottom); fitting the lower line first is easier — [29:50](https://www.youtube.com/watch?v=iwCoomDpICI&t=1790s), [31:08](https://www.youtube.com/watch?v=iwCoomDpICI&t=1868s) [captions]
- Toe by eye: 13 mm on the tie-rod flats, release the boot clamp so the boot doesn't twist; a string line between jack stands "doesn't substitute for an alignment"; he reused the tie-rod lock nuts though "I'm sure we're supposed to replace it" — [32:58](https://www.youtube.com/watch?v=iwCoomDpICI&t=1978s), [34:15](https://www.youtube.com/watch?v=iwCoomDpICI&t=2055s), [34:31](https://www.youtube.com/watch?v=iwCoomDpICI&t=2071s), [35:24](https://www.youtube.com/watch?v=iwCoomDpICI&t=2124s), [37:25](https://www.youtube.com/watch?v=iwCoomDpICI&t=2245s) [captions]
- No torque values are given anywhere in the video.

#### Clutch, flywheel and rear main seal

**FCP Euro – BMW E46 M3 Clutch Replacement DIY (2001-2006 BMW M3) (2022-10-01)** [19 chapters + description; no caption track]. 36:33, M3-specific, presented by Gareth Foley.

- Order from chapters: tools (01:25) → reinforcement plate (02:28) → exhaust (02:58) → driveshaft (04:27) → shift linkage (06:40) → transmission (08:06) → clutch and flywheel off (11:14) → rear main seal removal (11:54), swap (13:33), install (15:05) → clutch and flywheel install (17:19) → transmission prep (23:10) → transmission install (26:34) → linkage (28:55) → driveshaft (29:39) → exhaust (32:16) → reinforcement plate (34:56) — [FCP Euro – BMW E46 M3 Clutch Replacement DIY (2001-2006 BMW M3) (2022-10-01), 11:14](https://www.youtube.com/watch?v=NmEOFBqreX8&t=674s), [11:54](https://www.youtube.com/watch?v=NmEOFBqreX8&t=714s), [17:19](https://www.youtube.com/watch?v=NmEOFBqreX8&t=1039s), [23:10](https://www.youtube.com/watch?v=NmEOFBqreX8&t=1390s) [chapters]
- Parts listed in the description: an FCP "MA" clutch kit with flywheel (tagged "lightweight flywheel"), rear-main-seal kit 11142247867, a steel clutch-fork pivot pin 21511223281, clutch fork 21511223302 and release-bearing guide tube 23117512866 — [description](https://www.youtube.com/watch?v=NmEOFBqreX8) [description]

**FCP Euro – BMW E46 Clutch, Flywheel & Rear Main Seal Replacement DIY (330i, 325i, 330ci, 323i, 325ci, & More) (2020-07-24)** [23 chapters + description; no caption track]. The one the guide links. It is a Spec E46 race car (non-M) with a Fidanza 11.8 lb billet flywheel, an E36 M3 clutch and an unsprung disc.

- Chapters include "Rear Main Seal Removal" (20:00), "Swapping Rear Main Seal" (21:25), "Install Rear Main Seal" (23:59), "Pilot Bearing Install" (26:48), "Flywheel Install" (30:28), "Pressure Plate Install" (34:22) — [FCP Euro – BMW E46 Clutch, Flywheel & Rear Main Seal Replacement DIY (330i, 325i, 330ci, 323i, 325ci, & More) (2020-07-24), 20:00](https://www.youtube.com/watch?v=5S7-gNEgJoM&t=1200s), [26:48](https://www.youtube.com/watch?v=5S7-gNEgJoM&t=1608s), [30:28](https://www.youtube.com/watch?v=5S7-gNEgJoM&t=1828s) [chapters]; description — [description](https://www.youtube.com/watch?v=5S7-gNEgJoM) [description]

#### Clutch delay valve

**Throttle House – BMW E46 Clutch Delay Valve delete DIY and REVIEW (2016-05-12)** [auto captions + 5 chapters]. An E46 whose model isn't stated; the presenter's description says "I am not a mechanic" and credits impee.co.uk's written DIY.

- Slave cylinder comes off with two fasteners and "just pops out"; his was leaking after a failed reseal — [Throttle House – BMW E46 Clutch Delay Valve delete DIY and REVIEW (2016-05-12), 00:00](https://www.youtube.com/watch?v=LDEty2tnZLQ&t=0s), [00:26](https://www.youtube.com/watch?v=LDEty2tnZLQ&t=26s) [captions]
- Clamp the flexible clutch hose first "cuz you don't want to have to bleed more than you have to" — [00:26](https://www.youtube.com/watch?v=LDEty2tnZLQ&t=26s) [captions]
- 17 mm on the delay valve, 15 mm and 17 mm wrenches to split it from the line; have a catch can ready; shows the valve's tiny orifice — [00:53](https://www.youtube.com/watch?v=LDEty2tnZLQ&t=53s), [01:53](https://www.youtube.com/watch?v=LDEty2tnZLQ&t=113s), [02:38](https://www.youtube.com/watch?v=LDEty2tnZLQ&t=158s) [captions]
- Line screwed straight into the slave; with the hose clamped he barely needed to bleed ("maybe bleed it a little bit") — [03:09](https://www.youtube.com/watch?v=LDEty2tnZLQ&t=189s), [06:37](https://www.youtube.com/watch?v=LDEty2tnZLQ&t=397s) [captions]
- Time is not stated; the whole DIY occupies about 3½ minutes of the video — [chapters 00:00–03:36](https://www.youtube.com/watch?v=LDEty2tnZLQ&t=0s) [chapters]

#### Fuel-pump testing

- **LaRosa Drift – How to Check Fuel Pressure - E46 BMW (2022-11-17)**, 7:06, an E46 drift-car project (model not stated): chapters diagnosing 01:08, preparing the test 01:30, testing 03:41, results 04:57; description lists low-pressure symptoms as "sluggish power, no start, start and shut-off" — [LaRosa Drift – How to Check Fuel Pressure - E46 BMW (2022-11-17), 01:30](https://www.youtube.com/watch?v=t_JkzUQQ7Hs&t=90s), [03:41](https://www.youtube.com/watch?v=t_JkzUQQ7Hs&t=221s) [chapters], [description](https://www.youtube.com/watch?v=t_JkzUQQ7Hs) [description]
- **Electrical Car Repair LIVE – HOW TO TEST FUEL PUMP ON BMW E46 E39 E60 E53 X3 X5 Z3 Z4 E83 E85 E90 (2019-08-27)**, 4:26: description says it checks whether the pump runs on a no-start car, shown on an E46 — [Electrical Car Repair LIVE, description](https://www.youtube.com/watch?v=nPNse7EDv-4) [description]
- **E46ISTHEBEST – E46 m3 fuel pressure test results (2021-08-26)**, 1:13: no captions, no description — [title](https://www.youtube.com/watch?v=I8mLZuhiTzs) [title only]

#### Brake and DSC bleeding

**Adam – ABS/DSC brake system bleeding with INPA BMW (2018-05-27)** [description only; no captions]. Car not identified in the metadata.

- Steps: start INPA with the ignition on → select the car → select the DSC or ABS module → "Activate" → run the DSC bleeding menus in the order listed; for each wheel, top up the reservoir, open the bleeder, and pump and release the pedal as INPA's coloured screen instructs; close the bleeder; repeat at every wheel. The "pre-bleeding" item (Shift+F2) only tells you to bleed conventionally first. INPA bleeding "MIGHT be needed if you introduced air into the ABS/DSC module", e.g. after a master-cylinder or DSC-unit change — [Adam – ABS/DSC brake system bleeding with INPA BMW (2018-05-27), description](https://www.youtube.com/watch?v=ZOPhh7dAbHA) [description]

**Other bleeding videos (descriptions or titles only):**

- **50sKid – BMW 330i 325i E46 Brake Bleeding Using INPA (2015-08-01)**, 7:47: description only says INPA comes with an eBay K+DCAN cable; captions blocked — [50sKid – BMW 330i 325i E46 Brake Bleeding Using INPA (2015-08-01), description](https://www.youtube.com/watch?v=uKk0uc0Dnf4) [description]
- **50sKid – BMW 330i 325i E46 Brake Pressure Bleeding DIY (and Fix for Endless Bubbles) (2015-02-28)**, 28:33: description says a home-made pressure bleeder needs an airtight reservoir cap (his is a modified Dorman 42035), suggests a wire wheel for rusty bleed nipples, and covers "endless bubbles" — [50sKid – BMW 330i 325i E46 Brake Pressure Bleeding DIY (and Fix for Endless Bubbles) (2015-02-28), description](https://www.youtube.com/watch?v=_LLJXUbQkdA) [description]
- **Level Up Classics – How To Flush BMW E46 M3 Brakes With Motive Power Bleeder** (9:45): the only M3-specific bleed video found; title only — [Level Up Classics](https://www.youtube.com/watch?v=e-wP5Z37Zvs) [search listing title]

#### Engine removal (supporting job)

**DBO – How To Pull a BMW e46 Engine! (M3) (2019-04-28)** [12 chapters; auto captions exist but were not read (rate limit)]. An E46 M3; the driveline and gearbox come off before the engine work, per the chapter order.

- Order: exhaust (00:00) → driveshaft (01:32) → transmission (04:06) → engine bay prep (07:05) → electrical (10:30) → ECU and vacuum lines (13:44) → cooling (19:47) → fuel (22:13) → subframe prep (23:24) → sway bar and AC lines (24:52) → extraction (27:01–30:23) — [DBO – How To Pull a BMW e46 Engine! (M3) (2019-04-28), 01:32](https://www.youtube.com/watch?v=SH-J8ngKerk&t=92s), [13:44](https://www.youtube.com/watch?v=SH-J8ngKerk&t=824s), [23:24](https://www.youtube.com/watch?v=SH-J8ngKerk&t=1404s), [27:01](https://www.youtube.com/watch?v=SH-J8ngKerk&t=1621s) [chapters]

#### Leads not read

**Other leads found but not read (titles from search listings):** "How to: Remove E46 M3 Oil Pan!" (The Bimmer Barn, part 1 of its rod-bearing pair, 11:56); "Z3 Steering Rack Install in the E46 M3" (Right Foot Down, 25:16); "Clutch, Flywheel and Rear Main Seal Replacement - E46 M3 build pt 9" (Motorsport Inspired, 25:24); "BMW E46 M3 - Clutch DIY" (SeanS54, 16:21); "CDV Delete & Stainless Clutch Line Replacement DIY - BMW E46 M3 - Bimmerworld" (Redline360, 7:08); "BMW E46 Manual Swap Project: Clutch Delay Valve Install/Remove DIY" (50sKid, 7:49); "E46 Front Lower Control Arm Bushing Replacement with Tool Sizes and Torque Specs" (Endless Money Pits, 12:43); "Original vs Meyle HD, Poly & Z4m LCA Bushings - Install & Review E46" (OEMplusResto, 23:23); "BMW S54 Main and Conrod Bearings Inspection" (CRANK, 18:48); "PART 1: E46 M3 TOURING S54 ENGINE GETS ROD BEARINGS DONE" (solspeeds, 13:31) — [Bimmer Barn oil pan](https://www.youtube.com/watch?v=hEDzMrrgARE), [Right Foot Down](https://www.youtube.com/watch?v=sTvLwq6KmGQ), [Motorsport Inspired](https://www.youtube.com/watch?v=Usi3h-hXmNo), [SeanS54 clutch](https://www.youtube.com/watch?v=8YPgO4lzQXc), [Redline360](https://www.youtube.com/watch?v=hLb3LZaKq6s), [50sKid CDV](https://www.youtube.com/watch?v=t-QIQPNRzuI), [Endless Money Pits](https://www.youtube.com/watch?v=YX5g-XPZPWY), [OEMplusResto](https://www.youtube.com/watch?v=oTUR6MOgU_E), [CRANK bearings](https://www.youtube.com/watch?v=hAEiNuiw5MA), [solspeeds](https://www.youtube.com/watch?v=VQTtPpeMXcs) [search listing titles]

### Inferences
- **Order on the stand:**
  - Do the rod bearings with the pan off. FCP calls rod #1 the hardest part with the oil pump fitted, so on a stand it's reasonable to take the pump off — [FCP Euro – BMW S54 Rod Bearing Replacement DIY (2001-2006 BMW E46 M3) (2022-10-12), 51:17](https://www.youtube.com/watch?v=Emjw22o_V8c&t=3077s) [captions]. The pump sprocket nut is 25 Nm, left-hand thread (BMW SI, in `torque_specs.md`).
  - OnlyyDans' chapters put valve shims after the camshafts and before timing and VANOS. That is the logical order when building on a stand.
  - In the car, ECS sets the valves first and then removes the VANOS.
- **Plastigauge and M10 bolts:** in FCP's method the Plastigauge check is the first of the three M10 cycles. If the clearance is wrong, that bolt has already used one of its tightenings. Doing the check with old bolts first, as `torque_specs.md` suggests, avoids this.
- **Oiling the new bolts:** FCP cleans the new M10 bolts in alcohol, then oils them. `torque_specs.md` found no BMW statement on oiling them, so this is vendor practice, not BMW's.
- **Choosing shims:**
  - A tight valve needs a thinner shim and a loose one a thicker shim. FCP and ECS both moved one size, 0.04 mm.
  - The usual arithmetic is new shim = old shim + (measured clearance − target). That is standard practice; neither video states the formula.
- **Correction to the guide's valve paragraph:** the spring clip holds the rocker (finger follower) on its shaft. The shim sits loose in a pocket on the valve-spring retainer and comes out once the rocker is slid aside ([FCP Euro valve adjustment, 20:22](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1222s), [21:24](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1284s); [ECS, 14:21](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=861s), [15:23](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=923s) [captions]). No video states the shim diameter.
- **VANOS additions to the guide's Beisan-based list:**
  - S62 diaphragm springs and pressure plates
  - BMW's Torx exhaust-sprocket bolts (12 Nm with blue thread-locker)
  - inspecting the upper chain guide (broken on ECS's car) and the tensioner
  - the anti-rattle preload method
  - the "magic tooth" and quarter-turn preload steps
- **Fitting the M3 front axle (Phase 8):** FCP's subframe-refit pitfalls apply here. Unplug the headlight-level sensor lead before lowering, line up the steering-shaft notch with the wheel straight, tighten the rear bolts first and fit a new steering-shaft bolt. FCP's 110 Nm is unverified.
- **Rack:**
  - Centre the rack with the wheel straight ahead and line up the coupler indent before fitting the pinch bolt, then get a proper alignment.
  - Before fitting, check that a replacement rack's hard lines clear the subframe; 50sKid's aftermarket rack failed this.
- **Clutch delay valve:** it matters only if the Touring's own clutch line is kept; the guide plans to fit the M3 line, which has no delay valve. Clamping the flexible hose cuts the bleeding, but bleed anyway.
- **Rear axle:** no readable video exists for it. Use the BMW-based values in `torque_specs.md`, not Condor's chapter torques.
- **Brake and DSC bleeding:** INPA's DSC bleed routine (from Adam's description) is for when air has entered the hydraulic unit. A conventional or pressure bleed comes first, and a pressure bleeder needs an airtight cap (50sKid).

### Gaps
- **Job time:** none of the videos read states total hours. The only time data:
  - Paul Vo's description: one weekend working alone, and 3–7 days for a first-timer.
  - FCP's car sat about a day with the pan off.
  - The guide's VANOS estimate (5 h for a mechanic, 7+ h for a DIYer) comes from Beisan's written procedure, not a video.
- **No readable video** for:
  - welding in rear subframe reinforcement, or RTAB and rear bushing work;
  - front control-arm, clutch and flywheel torques;
  - an S54 5-bar fuel-pressure test;
  - an M3 DSC bleed.
- **Unreliable auto-captions:**
  - Paul Vo's captions are largely unintelligible.
  - ECS's narration reads like a machine translation: "transmission gear" for transfer gear, "graduation" for exhaust, "tranquilizer" and "silencer" for the chain guide. One remark about the crank socket ("a four-turn head or a 32-turn head") is garbled; it probably means the four-bolt adapter or a 32 mm socket.
  - I reported only the figures that are clear in context.

## Q3. Do the on-camera specs agree with the BMW-sourced values in torque_specs.md?

### Takeaway
Where a video gives a value that `torque_specs.md` also has, most agree with BMW's SI B11 04 04:
- the rod-bolt procedures (three cycles for M10, a single 70° for M11)
- the shell colours
- the oil-pan screws (10 Nm)
- the steering-shaft bolt (22 Nm)
- the reinforcement plate (59 Nm + 90°)

Disagreements:
- Condor's diff-mount torques (70 ft-lb rear Torx, 128 ft-lb front bolt) against the M3's 20 Nm + 90° and 200 Nm.
- The Bimmer Barn's spoken "105 newton meters" with no repeat cycles.
- FCP's looser break-in and 6 L oil fill.

Many other on-camera values, such as the front subframe (110 Nm), the VANOS fasteners, the plugs and the valve cover, have no BMW reference in `torque_specs.md`. FCP and ECS disagree on two of them.

### Cited Findings
| Fastener or spec | What the video says (source) | BMW-sourced value in torque_specs.md | Verdict |
|---|---|---|---|
| S54 M10 E-Torx rod bolts | 5 Nm, 30 Nm, 105°, loosen, repeat twice more ([FCP Euro rod bearings, 20:51](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1251s) [captions]); same, backing off 360° between cycles ([Paul Vo, 11:35](https://www.youtube.com/watch?v=O345BKC8EkM&t=695s) [captions], [description](https://www.youtube.com/watch?v=O345BKC8EkM) [description]) | SI B11 04 04: 5 Nm, 30 Nm, 105° in one stroke, back off about one turn, three cycles, third is final | **Agree** |
| M10 rod bolts as spoken by The Bimmer Barn | "5, 30 and 105 newton meters" for post-2003 cars, no repeat cycles ([The Bimmer Barn rod bearings, 03:39](https://www.youtube.com/watch?v=kb7PO3CtERE&t=219s) [captions]) | 105° (angle, not Nm), three cycles | **Disagree** — a slip; don't follow it |
| Re-tightening limit for M10 bolts | "can be torqued up to five times" ([FCP Euro rod bearings, 24:52](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1492s) [captions]) | Only an e46fanatics snippet ("no more than five"); not in the SI text read | **Unverified**, but now two independent mentions |
| S54 M11 rod bolts | 5 Nm, 30 Nm, 70°; reuse, each in its own location ([The Bimmer Barn rod bearings, 03:36](https://www.youtube.com/watch?v=kb7PO3CtERE&t=216s), [07:48](https://www.youtube.com/watch?v=kb7PO3CtERE&t=468s) [captions]) | 5 Nm, 30 Nm, 70° in one stroke; reuse in the same holes | **Agree** |
| M10/M11 change-over | "pre-2003" vs "2003 forward" ([The Bimmer Barn, 02:08](https://www.youtube.com/watch?v=kb7PO3CtERE&t=128s) [captions]); "post 12/2002" ([Paul Vo, description](https://www.youtube.com/watch?v=O345BKC8EkM) [description]) | SI: 12/12–13/2002 production | Paul Vo **agrees**; Bimmer Barn is approximate |
| Shell colours | Blue in the rod, red in the cap ([The Bimmer Barn, 03:03](https://www.youtube.com/watch?v=kb7PO3CtERE&t=183s); [Paul Vo, 04:19](https://www.youtube.com/watch?v=O345BKC8EkM&t=259s) [captions]) | Blue rod side, red cap side | **Agree** |
| Oil-pan M6 screws | 10 Nm ([FCP Euro rod bearings, 29:26](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1766s), [35:15](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2115s) [captions]) | 10 Nm | **Agree** |
| Sealant at timing-cover and rear-cover joints | RTV (Corteco) bead ([FCP Euro rod bearings, 33:19](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1999s) [captions]) | Hylomar at those joints | Same joints, **different product** |
| Steering-shaft clamp bolt | New E10 bolt, 22 Nm ([FCP Euro rod bearings, 41:14](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2474s) [captions]) | New M8×33, 22 Nm | **Agree** |
| Front reinforcement plate | New bolts, 59 Nm + 90° ([FCP Euro rod bearings, 50:15](https://www.youtube.com/watch?v=Emjw22o_V8c&t=3015s) [captions]) | New M10 screws, 59 Nm then 90° | **Agree** |
| Oil after a rod-bearing job | 6 L of 10W-60 ([FCP Euro rod bearings, 47:21](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2841s) [captions]); 7 L bought ([Paul Vo, description](https://www.youtube.com/watch?v=O345BKC8EkM) [description]) | 6.5 L of 10W-60 | **Minor difference**; fill to the SI figure and check |
| Bearing break-in | 1,200 miles under 5,500 rpm ([The Bimmer Barn, 17:00](https://www.youtube.com/watch?v=kb7PO3CtERE&t=1020s) [captions]); about 1,000 miles, "don't redline it" ([FCP Euro, 49:07](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2947s) [captions]) | 1,200 miles below 5,500 rpm | Bimmer Barn **agrees**; FCP is **looser** than BMW |
| Diff rear mount bolts (M3) | "torque to 70 ft-lbs" (≈95 Nm) ([Condor diff bushings, 01:32](https://www.youtube.com/watch?v=fcOohpFKZZE&t=92s) [chapters]) | 20 Nm + 90° (Department 69, Flow PDF, NAM3; compilations, TIS not read directly) | **Disagree** |
| Diff front bolt (M3, 21 mm head) | "torque to 128 ft-lbs" (≈174 Nm) ([Condor diff bushings, 01:42](https://www.youtube.com/watch?v=fcOohpFKZZE&t=102s) [chapters]) | 200 Nm (compilations); torque_specs already flags a 128 ft-lb vendor snippet | **Disagree** |

Values stated on camera that `torque_specs.md` doesn't cover (no BMW value to compare):

| Fastener or spec | Value on camera (source) | In torque_specs.md? |
|---|---|---|
| Front subframe to body | 110 Nm, rear bolts first ([FCP Euro rod bearings, 40:58](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2458s) [captions]) | No |
| Engine-mount nuts | 45 Nm ([FCP Euro rod bearings, 41:26](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2486s) [captions]) | No |
| Front control-arm bracket bolts | 59 Nm ([FCP Euro rod bearings, 42:06](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2526s) [captions]) | No |
| Power-steering pump bolts; crank-pulley bolts | 23 Nm each ([FCP Euro rod bearings, 38:07](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2287s), [39:18](https://www.youtube.com/watch?v=Emjw22o_V8c&t=2358s) [captions]) | No |
| Oil drain plug | 25 Nm, new crush washer ([FCP Euro rod bearings, 30:05](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1805s) [captions]) | No |
| Spark plugs (M12×1.25) | 23 Nm, dry ([FCP Euro valve adjustment, 31:23](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1883s) [captions]) vs 25 Nm ([ECS, 1:11:04](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4264s) [captions]) | No — **the videos disagree** |
| Valve-cover cap nuts | 10 Nm ([FCP Euro valve adjustment, 34:58](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=2098s) [captions]) vs 8 Nm ([ECS, 1:13:45](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4425s) [captions]) | No — **the videos disagree** |
| PCV return banjo (17 mm) | 19 Nm, new washers ([FCP Euro valve adjustment, 36:06](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=2166s) [captions]) | No |
| VANOS solenoid coil screws | 4 Nm ([ECS, 27:02](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=1622s) [captions]) | No |
| VANOS piston covers; lower VANOS bolts; solenoid block screws | 10 Nm (7 ft-lb) each ([ECS, 39:52](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2392s), [1:04:52](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3892s), [1:09:53](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=4193s) [captions]) | No |
| VANOS transfer-gear cover | 55 Nm (40.5 ft-lb) ([ECS, 45:01](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2701s) [captions]) | No |
| Exhaust sprocket Torx bolts | 12 Nm with blue thread-locker ([ECS, 49:52](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=2992s) [captions]) | No |
| Upper chain guide bolt; chain tensioner | 24 Nm; snug + ½ turn with a new washer ([ECS, 52:40](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3160s), [53:10](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3190s) [captions]) | No |
| VANOS hub bolts (new M6×25) | About 14 Nm, by feel ([ECS, 1:06:17](https://www.youtube.com/watch?v=vhsxb5IRa8s&t=3977s) [captions]) | No |
| S54 rod-bearing clearance | 0.03–0.07 mm, called BMW's/"factory" spec by both ([FCP Euro rod bearings, 21:43](https://www.youtube.com/watch?v=Emjw22o_V8c&t=1303s); [The Bimmer Barn, 10:50](https://www.youtube.com/watch?v=kb7PO3CtERE&t=650s) [captions]) | No |
| Valve clearance, cold | Intake 0.18–0.23 mm, exhaust 0.28–0.33 mm, coolant below 35 °C ([FCP Euro valve adjustment, 18:06](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1086s), [24:11](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1451s), [25:31](https://www.youtube.com/watch?v=6xtAIiKbKmM&t=1531s) [captions]) | No (the guide's BMW S54 module gives the same values) |

### Inferences
- **Condor's figures:** its two numbers equal Department 69's non-M diff figures, but swapped between the mounts. 70 ft-lb ≈ 95 Nm is the non-M front figure, and 128 ft-lb ≈ 174 Nm is the non-M rear figure. My inference is that Condor took non-M data. The same 128 ft-lb is the ECS/Rogue snippet `torque_specs.md` already flagged. For an M3 diff, use 200 Nm front and 20 Nm + 90° rear, and treat Condor's chapter torques as wrong for OEM-type mounts.
- **M10 bolt reuse limit:** FCP's "up to five times" is a second, independent mention of a five-tightening limit. It is still not in any BMW text read.
- **Break-in and oil:** follow BMW's 1,200 miles below 5,500 rpm, not FCP's looser advice. Fill to the SI's 6.5 L and check the dipstick.
- **Plugs and valve cover:** where FCP and ECS disagree (plugs 23 vs 25 Nm; valve-cover nuts 10 vs 8 Nm), the guide needs a TIS value. Neither video's figure is BMW-sourced.
- **Other FCP figures:** the front-subframe 110 Nm, engine-mount 45 Nm and control-arm bracket 59 Nm are unverified. They belong in the guide's open questions until checked against TIS, not in its torque table.

### Gaps
- `torque_specs.md` has no BMW value for:
  - the front subframe, engine mounts and control-arm brackets
  - the spark plugs and valve cover
  - the VANOS fasteners
  - rod-bearing clearance
  - valve clearance; the guide already cites the BMW S54 training module for this, and the videos match it.
- I couldn't find where Condor's figures come from: the video has no captions and its 12 comments are silent on them.
- The M3 diff-mount values rest on compilations that cite TIS (Department 69, the Flow PDF), not on TIS itself (see `torque_specs.md`).
