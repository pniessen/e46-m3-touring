# Round-4 fold-in: shared brief for writers

Paths below use `$R` for `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold` and `$G` for `/home/user/archeyon/e46-m3-touring-conversion`.

## The project

- **The guide** lives in `$G`: `README.md` (the build guide, about 530 KB), `WIRING-AND-CODING.md` (the wiring and coding manual), `JOB-CARDS.md` (one printable card per job), `WORKSHEETS.md` (fill-in records), `CALCULATORS.md` and `research.md`. It is published as a website at https://pniessen.github.io/e46-m3-touring/.
- **The car:** the owner's 2003 US BMW E46 325i Touring (M54, 5-speed manual, rear-wheel drive), registered in Massachusetts. If it was built before 03/2003 it has an MS43 DME; from 03/2003 it has an MS45.1. The owner hasn't sent the build month yet, so the guide covers both.
- **The donor:** a 2003–06 US E46 M3 with a manual gearbox: S54, MSS54 or MSS54HP DME, and Teves MK60 DSC from 09/2002.
- **Round-4 research notes**, one per topic, are in `/home/user/archeyon/research_notes/E46 M3 Touring coding, body and chassis/`. Each has:
  - a Takeaway
  - cited findings, inferences and gaps for each question
  - a Guide-ready section (parts tables, procedures, pass values)
  - diagram data
  - a numbered list, "Guide statements this research corrects": quotes of the guide's current text, each with its correction
- The notes mark how each claim was read:
  - [read]: the page itself was read
  - [snippet]: only a search engine's summary was seen
  - [image]: a diagram image was read
  - [captions]: video captions were read
- Older research notes in `/home/user/archeyon/research_notes/` are background only.

## How the edit works: fragments

The four pages are split into section files under `$R/frags/<PAGE>/NNNN__slug.md`. The folders are README, WIRING-AND-CODING, JOB-CARDS and WORKSHEETS. Joining a page's files in file-name order recreates the page exactly. `$R/frags/owners.tsv` lists every fragment and its owner (columns: page, file, heading, owner). Several writers work at once, one per topic: coding-body, coding-power, arches, floor, susp, fuel, front and cool. An integrator handles every fragment marked `integrator` after all writers finish.

**Rules**

1. Edit only fragments whose owner is you: `awk -F'\t' '$4=="<you>"' $R/frags/owners.tsv`.
   - You may read anything.
   - The pages in `$G` stay unchanged until the integrator joins the fragments, so read them for context.
   - Don't read README.md whole (it is large). Grep it, or read the fragments you need.
2. Never edit the `.md` pages in `$G`, another writer's fragment, or another writer's request file. Don't commit, don't build the site, and don't run git commands that change anything.
3. Keep each fragment's first line, its heading, exactly as it is. Headings anchor links across the site.
   - You may add new headings inside your fragment, one level below the fragment's own heading or deeper.
   - First grep the page to confirm the new heading text appears nowhere else on it. Pandoc numbers duplicate headings, which breaks existing links.
4. Some new sections belong between fragments. For those, create a new fragment file named with the preceding fragment's number plus your digit:

   | Writer | Digit |
   |---|---|
   | coding-body | 1 |
   | coding-power | 2 |
   | arches | 3 |
   | floor | 4 |
   | susp | 5 |
   | fuel | 6 |
   | front | 7 |
   | cool | 8 |

   For example, after `0670__x.md` the floor writer creates `0674__new-slug.md`. Start it with a heading at the level of its neighbours (`##` for job cards). List it in your final report.
5. Changes to fragments you don't own go in your request file, `$R/requests/<you>.md`. Format each request like this:

   ```
   ### R<n>: <PAGE> <fragment file>: <short title>
   - **Change:** replace | insert after | add row | delete
   - **Find (exact current text, for replace, delete or insert after):**
     > ...
   - **New text:**
     > ...
   - **Why:** one line, plus the notes section it comes from
   ```

   - Make each request complete enough to apply without opening your notes: the exact new wording, with its links.
   - Put any conflict you notice between your notes and another topic's notes at the top of the file, under `## Conflicts`.

**Shared sections.** These are owned by the integrator. Always send requests for them; never edit them yourself.

- **README:**
  - The preamble ("At a glance") and the Overview sections
  - Plan and budget, except "Factory documentation and coding kit"
  - From the Parts list: Gearbox and driveline, Body, Consumables and single-use parts
  - Phases 0, 1, 2, 3, 4, 9, 12 and 13
  - Deep-dive sections: Driveline and rear axle, S54 refresh on the stand, Troubleshooting (the README one), Front end on a 4-door body
  - Registration and legal (all of it) and Sources
  - From the Appendix: Torque values, Fluids and capacities, Key numbers, Glossary, Open questions to verify, Photo credits, About this research
- **Job cards:** 0, 1, 2a, 3a–3e, 4, 9a, 9b, 12a, 12b, 12c and 13.
- **WIRING-AND-CODING:** the preamble and all of "Checks before first power-up".
- **Worksheets:**
  - Touring baseline record and Mileage
  - Donor M3 record and tests
  - S54 refresh measurements
  - Torque log intro, and its Phase 3, 9 and 12 tables
  - Fluids log, Power-up checks, First start, Shakedown log intro, Break-in log
  - Inspection day, Results and paperwork

**Keeping values in step.** Every torque, fluid, part number, price, open question or Massachusetts rule you change or add must appear consistently everywhere it is used.

- Torques belong in the README Appendix torque table and in the matching job card and worksheet torque log.
- Fluids belong in the Appendix fluids table and the worksheet fluids log.
- Parts and prices belong in the Parts list and the Budget.
- Answered or new open questions belong in "Open questions to verify".

Edit the places you own. Send requests for the rest.

## What to write

- **Corrections first.** Work through your notes' "Guide statements this research corrects" list. Apply each correction where it lands: in your fragments, or as a request.
- **Then the Guide-ready material:** parts tables, procedures and decision points. The guide is a plan for an amateur in a home garage.
  - Say what to do, in order.
  - Give the check that proves each step, and the value it must hit.
  - Put decisions where the builder meets them, with a recommendation.
- **Sources.** Cite inline with Markdown links, as the guide already does:
  - `[Name – title (year), mm:ss](url)` for a video timestamp
  - `[ETK](url)` for a parts-catalog page
  - `[BMW ST041](url)` for a BMW document

  Rules for sourcing:
  - Use the URLs in the notes; invent none, and don't cite the research notes themselves.
  - Label estimates and inferences in the text, for example "our estimate" or "we infer".
  - A claim that rests only on a search summary ([snippet]) or on a page nobody could open gets "(unverified)".
  - Don't do new web research. Work from the notes. If a fact looks shaky, hedge it or leave it out.
- **Units:**
  - Metric first, US units in brackets: 59 Nm (44 ft-lb), 587 mm (23.1 in), 9.3 L (9.8 US qt).
  - Prices carry their source and date ("\$763.61 at BMWPartsDeal, October 2026"). Give non-US prices in their own currency.
  - Write every dollar sign as `\$`. The site's checker fails on a bare `$` outside code.
- **BMW part numbers:** 11 digits, no spaces (41127895619).
- **Fault codes:**
  - Write them decimal first, as INPA prints them, with hex in brackets: 130 (0x82).
  - DSC fault codes that BMW and the sources print in hex, like 5EF1, stay as printed, with a word on what they mean.
- **Voice:**
  - Plain English, second person, short sentences, active verbs. Lead with the action or the answer.
  - No filler: "genuine", "honest", "actually" or "real" used as intensifiers, "it's worth noting", "importantly".
  - Prefer a table or numbered steps to a long paragraph.
  - Match the formatting already in your fragments:
    - bold lead-ins
    - `> [!WARNING]`, `> [!CAUTION]` and `> [!NOTE]` callouts
    - tables
    - in job cards, task lines written as `- [ ] <span>…</span>`, and Done-when tables with an empty Reading column
- **Size:**
  - **Deep dives** can grow as far as the material earns.
  - **Job cards** must stay printable on one or two pages each. Add only what the builder needs at the car, link to the guide for the rest, and don't let a card grow by more than about 40%.
  - **Worksheets:** add rows or fields for new measurements and pass values. The empty last columns become fillable fields on the site, so copy the existing tables' shape.
- **Diagrams** are drawn after this step, so don't draw any.
  - **New diagrams.** Where one would help a reader, put a placeholder on its own line between paragraphs, such as `<!-- figure: proposed-brake-hydraulics -->`. Say in your final report what it should show.
  - **Existing figures.** Don't remove or renumber them. If one's caption or drawing is now wrong, say so in your report; the diagram makers fix both the SVG and the caption.

## Hard limits (unchanged from earlier rounds)

- **EWS delete:** no patch bytes, addresses or hex patches, and no step-by-step EEPROM edits. The delete appears only as a service you buy or a tool function you run.
- **Emissions and readiness:** nothing that removes, disables, masks or defeats an emissions function or a readiness monitor. Moving an emissions part into BMW's own M3 arrangement is fine, and the text must say it has to keep working.
- **Odometer:** a replacement cluster is only ever set to the car's true mileage (49 U.S.C. §32704).
- **Refrigerant:** never vent it. A/C work starts with recovery by a licensed shop (EPA Section 609).
- **Safety notes:** don't weaken them (welding fumes and fire, fuel vapour, jacking and stands, airbags, brake fluid).

## When you finish

Re-read every fragment you changed from top to bottom. Check that:

- tables still have the same number of cells in every row
- links are well formed
- every `$` is escaped
- no heading you added duplicates one elsewhere on its page

Then reply with a report of about 300 words:

- fragments changed and fragments created
- the number of requests, with the important ones
- conflicts with other notes
- proposed figures: placeholder name and what each should show
- existing figures that are now wrong
- corrections from your notes you didn't apply, and why
