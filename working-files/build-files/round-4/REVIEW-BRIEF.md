# Round-4 review: brief for skeptic reviewers

## Paths

| Name | Path |
|---|---|
| `$R` | `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold` |
| `$G` | `/home/user/archeyon/e46-m3-touring-conversion` |
| `$N` | `/home/user/archeyon/research_notes/E46 M3 Touring coding, body and chassis/` |

## Background

- **The guide:** a home-garage plan to turn a 2003 US BMW E46 325i Touring (Massachusetts) into an E46 M3 Touring, using a 2003–06 US M3 donor.
- **This round:** research round 4 added coding, rear arches, floor and exhaust, suspension, fuel, front axle and brakes, cooling and A/C. A gap-filling pass followed, including BMW's own E46 TIS repair manual and coding data, plus a new 325xi subchapter.
- **How the text is stored:**
  - Writers and integrators folded the research into section fragments, `$R/frags/<PAGE>/NNNN__slug.md`. Joined in file-name order, the fragments make the four pages README, WIRING-AND-CODING, JOB-CARDS and WORKSHEETS.
  - New figures appear in the fragments as `<!-- figure: proposed-NAME -->` placeholders.
  - Their captions are in `$R/diagrams/proposed-NAME.caption.md`. Captions for redrawn figures are in `$R/diagrams/redraw-NN-name.caption.md`.
  - The SVGs are in `$G/diagrams/`.
- **Assembled preview:** `sh $R/assemble.sh <dir>` joins the fragments into a copy of the guide, places the figures and numbers them. A fresh preview is in `$R/preview/` (README.md etc.); read it to see the result in context. Never edit the preview; it's regenerated.
- **Sources:** the research notes in `$N`:
  - the eight topic notes
  - `gapfill_*.md`, which outrank the topic notes where they conflict: BMW TIS and BMW coding data beat forum posts
  - `xi_*.md`

## What changed

`sh $R/changed.sh <PAGE> <fragment file>` prints a unified diff of this round's changes to one section. A new fragment prints in full. Spend most of your time on the changed lines, but read enough around them to judge whether the section still reads correctly as a whole. The original sections are in `$R/frags-orig/`.

## Your job

You are a skeptic. You have three tasks.

1. **Check every new or changed fact in your area against the notes.**
   - Values: torques, capacities, dimensions, pressures, part numbers, prices with dates, fault codes, job names and pin numbers.
   - Rules, procedures and their order.
   - The source each claim cites, and that the claim says what the source says.

   Spot-check the most important new claims at their URLs with WebFetch: at least five per reviewer, prioritizing BMW documents. Don't use more than 10 WebSearch calls. Don't bypass bot checks or paywalls.
2. **Check that the guide reads correctly for an amateur in a home garage.**
   - Steps come in a workable order, and each check has a pass value.
   - Decisions sit where the builder meets them.
   - Nothing contradicts another part of the guide. Grep the other pages for each value you check, and the old value it replaced. Leftover old values are the most common bug.
   - Job cards cite the right phase steps.
   - The figures agree with the text: open the SVGs (the `aria-label` holds the full content) and compare every label and number.
3. **Check the hard limits:**
   - no EWS-delete patch bytes, addresses or hex
   - nothing that defeats or masks emissions or readiness
   - odometer set to the true mileage only
   - refrigerant never vented
   - safety notes not weakened

## What you may edit

- **Fragments you own.** Fix what's wrong directly, keeping the style rules in `$R/BRIEF.md`.
- **Caption files** of the figures in your area.

For everything else, write requests to `$R/review-requests/<you>.md`. Use the request format in `$R/BRIEF.md`, with a priority:
- P1: wrong, unsafe or contradicts something
- P2: unclear or missing a check
- P3: polish

Find what you own with:

```
awk -F'\t' '$4=="<you>"' $R/review-owners.tsv
```

**Figure drawing problems.** Don't edit SVGs. Report each one with:
- the figure file
- what is wrong
- the exact fix

The diagram makers will apply them.

## Report (under 400 words)

- the number of facts checked, and the number you spot-checked at a URL
- **P1 issues:** what was wrong, and the fix you made or requested
- P2 and P3 issues, counted, with the important ones
- figure fixes needed, per file
- anything you could not verify

Put the full list in `$R/review-requests/<you>.md` as well.
