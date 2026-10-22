# Round-4 fold-in: brief for the integrators

Read `BRIEF.md` in this folder first. It holds:
- the project
- the fragment system
- style, units and sourcing
- the hard limits, all of which bind you too

Paths: `$R` = `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold` and `$G` = `/home/user/archeyon/e46-m3-touring-conversion`.

## Where things stand

Eight topic writers worked in parallel:
- coding-body
- coding-power
- arches
- floor
- susp
- fuel
- front
- cool

Each one:
- edited the fragments it owned
- wrote everything else it needed into `$R/requests/<writer>.md`, as requests to change fragments it didn't own
- listed cross-topic disagreements under `## Conflicts` at the top of that file

All writers have finished, so every fragment is free to edit, with two exceptions:

- **The 325xi fragment is reserved.** `README/0050__if-your-car-is-a-325xi.md` belongs to a separate xi writer who is still researching. Send changes for it to your own request file instead.
- **Figure placeholders stay.** Never remove or move a `<!-- figure: … -->` line. I handle those.

Four integrators now work in parallel, each on its own set of fragments:

| Integrator | Fragments |
|---|---|
| **readme-plan** | README `0000__preamble.md` through `0290__consumables-and-single-use-parts.md`: preamble, Overview, Plan and budget, Parts list (except the reserved 325xi fragment) |
| **readme-build** | README `0300__step-by-step-build.md` through `0710__rear-bumper-skirts-and-trim.md`: the phases and all three deep dives |
| **readme-back** | README `0720__…` to the end: Registration and legal, Sources, Appendix |
| **others** | every fragment of WIRING-AND-CODING, JOB-CARDS and WORKSHEETS |

Edit only the fragments in your own set. A change needed in another integrator's set goes into `$R/requests/integrator-<you>.md`, in the same request format; I'll apply those afterwards. Keep them rare.

**Read `$R/LOG.md` before you start.** It records each writer's hand-off:
- requests that a writer has **already applied** in its own fragments, which you must skip, though you should still check the result reads right
- overlapping requests, and which one to apply
- the conflicts each writer flagged, and the decisions writers already made

**Gap-fill addenda come later.** Gap-filling researchers are still running. When they finish, I'll send you their findings (files named `gapfill_*.md` in the notes folder) as more requests for your set. Finish the writer requests first.

## Your job

1. **Read every request file** in `$R/requests/`. Collect each request that targets a fragment in your set, whatever its owner was in Phase A, and apply it.
   - Requests are proposals, not orders. Before you apply one, check it against the writer's notes when it changes a fact (a value, a part number, a rule) and isn't self-evidently right. The notes are in `/home/user/archeyon/research_notes/E46 M3 Touring coding, body and chassis/`.
   - Fix wording to the style rules.
   - Merge requests that overlap, for example two writers adding rows to the same torque table or the same open question.
   - Skip a request when the target text has already changed in a way that makes it moot. Say so in your report.
2. **Resolve the Conflicts sections** that touch your set. Decide from the sources the notes cite:
   - BMW documents beat the parts catalog.
   - The parts catalog beats forum posts.
   - Read beats snippet.

   Where a conflict can't be decided, give both values with their sources and add an open question. List every decision in your report.
3. **Keep values in step within your set.** The same torque, fluid, part number, price or rule must read the same everywhere in your set. Grep your fragments for each changed value and the old value it replaced. Old values left behind are the most common bug.
   - **readme-back** owns the Appendix tables, which are the reference.
   - **readme-plan**, **readme-build** and **others** use the same values from the same requests.

   If you find a mismatch with another integrator's set, put it in your request file.
4. **Update the text that frames the guide** (readme-plan):
   - the preamble's description of the research rounds: add the October 2026 fourth round on coding, body and chassis
   - "At a glance" if the budget, time or hardest jobs change
   - "Decide these before you spend money", "How hard each job is", Budget and Time, where round 4 changes a decision or a cost. Examples:
     - new BMW trunk floor and quarter panels, which mean no donor steel
     - the in-tank fuel set
     - springs and coilovers
     - fans
     - A/C hose

   **readme-back** updates "About this research" and the Sources section's lists. Add any source the writers used heavily that the lists lack.
5. **Open questions to verify** (readme-back):
   - Remove the questions round 4 answered, or mark them answered with the answer and a link to where the guide now uses it.
   - Add the new gaps the writers raised. Keep each question one or two lines, with what would settle it.

## Finish

1. Re-read every fragment you changed. Check:
   - table cell counts
   - links
   - `\$` escapes
   - that no heading duplicates another on its page
   - that no heading line changed, unless a request said so and every link to it was updated
2. Don't join, build, commit or run git.
3. Report in about 300 words:
   - requests applied, merged and skipped (with reasons)
   - conflicts decided and how
   - value mismatches found
   - anything left for me
