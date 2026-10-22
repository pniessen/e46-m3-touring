# Round-4 diagrams: brief for diagram makers

## Paths

| Name | Path |
|---|---|
| `$R` | `/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold` |
| `$G` | `/home/user/archeyon/e46-m3-touring-conversion` (the guide; diagrams live in `$G/diagrams/`) |
| `$OLD` | `/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/diagrams-test` (last round's kits) |

## Context

- **The project:** a home-garage plan to turn a 2003 US BMW E46 325i Touring into an E46 M3 Touring, using a 2003–06 US M3 donor. It is published at https://pniessen.github.io/e46-m3-touring/.
- **Where the text is:** this round's research has just been folded into the guide. The new text is in section fragments under `$R/frags/<PAGE>/NNNN__slug.md`, with pages README, WIRING-AND-CODING, JOB-CARDS and WORKSHEETS.
  - Each new figure has a placeholder in a fragment: `<!-- figure: proposed-NAME -->`. Grep for it to see where the figure sits, and read the section around it. The figure must agree with that text.
  - The pages in `$G/*.md` are the old text. Use them only for existing figures' captions, which look like `*Figure N. …*` under each `![…](diagrams/…svg)` line.
- **Data sources:** the research notes in `/home/user/archeyon/research_notes/E46 M3 Touring coding, body and chassis/`, especially each one's "Diagram-ready data" section, plus the fragment text.
  - If the text and the notes disagree, follow the text and report the disagreement.
  - Never invent data. Where data is missing, draw that part generically and label it, e.g. "check on the car", or leave it out.

## Files you produce

1. **The SVG:** `$G/diagrams/NN-name.svg`, using the number and name in your prompt. A redraw overwrites the existing file and keeps its name.
2. **A generator:** one Python script per figure in your own folder, `$R/dgen/<you>/`, so the figure can be regenerated. Copy a kit into that folder; don't edit the originals.
   - Portrait, 400 wide: `$R/tools/svgkit.py`.
   - Landscape, 800 wide: `$OLD/circuits-a/kit.py` with `$OLD/circuits-a/measure_cache.js`. This kit measures text width in Chromium with the site's fonts, which helps layout.
3. **A caption file** in `$R/diagrams/`:
   - For a new figure: `proposed-NAME.caption.md`, named after its placeholder so the insert script matches it.
   - For a redraw: `redraw-NN-name.caption.md`.

   Use exactly this format:

   ```
   ![Short alt title](diagrams/NN-name.svg) <!-- portrait -->

   *Figure N. Caption text.*
   ---
   <!-- figure: proposed-NAME -->
   Where it goes: README.md, section "…", at the placeholder. (For a redraw: which existing caption it replaces, quoted.)
   ```

   - Keep `<!-- portrait -->` only for 400-wide figures.
   - Write "Figure N." literally. The insert script numbers every figure on the page.
   - A caption says what the figure shows and the one or two points the builder must take from it, in plain English. It doesn't repeat the aria-label.

## House style: match the 26 existing diagrams

- **Style block and classes:** the kit copies the `<style>` block verbatim. Use only its classes and never inline colours. The site strips the style block and re-themes the classes for light and dark mode.
- **Colour meanings:**

  | Class | Colour | Meaning |
  |---|---|---|
  | `keep` | grey | the Touring's own part, kept |
  | `donor` | blue | from the donor M3 |
  | `new` | green | buy new |
  | `fab` | orange | fabricate or modify |
  | `crit` | red | hazard or critical check |
  | `warn-f` | | caution-note fill |
  | `panel` | | background grouping |

  The same classes come in stroke (`-s`), text (`-t`) and fill (`-f`) versions. The landscape kit has arrowheads in each colour.
- **Text classes:**

  | Class | Use |
  |---|---|
  | `t` | 13 px body |
  | `t-sm` | 11.5 px |
  | `t-xs` | 10.5 px, the minimum; nothing smaller |
  | `t-b` | bold |
  | `t-h` | section heads |
  | `t-mono` | pins, part numbers, job names |

- **Width:**
  - Portrait (400 wide) is the default, since readers are often on phones.
  - Use landscape (800 wide, scrolls sideways on phones) only when the content needs width, such as a side view of a car body or a long circuit.
  - Height is whatever the content needs.
- **Key:** add one when you use more than one part colour.
- **Labels:** give units, and part numbers where they help the builder at the car.
- **aria-label:** the root element carries a full one, a few sentences saying what the figure shows with its key facts and numbers. The existing figures are good models.
- **Uncertain data:** approximate or inferred data says so on the figure, e.g. "approx.", "scaled from BMW drawings, ±10 mm" or "inferred".
- **Idioms to copy:**

  | Figure type | Existing examples in `$G/diagrams/` |
  |---|---|
  | Portrait options | `13-dsc-brake-options.svg` |
  | Portrait circuit | `11-fuel-pump-control.svg` |
  | Landscape circuit | `20-circuit-sport.svg` |
  | Flowcharts | `16-flow-which-dme.svg`, `25-flow-no-start.svg` |
  | Body | `08-rear-quarter.svg`, `09-arch-section.svg`, `14-cargo-floor-plates.svg` |
  | Layout | `05-exhaust-floor.svg`, `04-fuel-pressure.svg` |

## Test every figure

```
python3 -I $R/tools/make_pages.py $R/dtest/<you>/pages $G/diagrams/NN-name.svg
cd $R/tools && NODE_PATH=$(npm root -g) node shoot.js $R/dtest/<you>/shots $R/dtest/<you>/pages/NN-name.html
```

`shoot.js` renders the figure at 390 px phone width in light and dark, saves PNGs, and lists four kinds of issue:
- text outside the viewBox
- text overlapping text
- strokes crossing text
- text spilling out of its box

Fix the figure until it reports 0 issues, or justify each one that remains. Then open both PNGs with the Read tool and check:
- the text is legible
- the arrows point the right way
- nothing is clipped
- dark mode reads well

If Chromium is busy because other makers are testing at the same time, retry after a pause.

## Facts and limits

- Every number, part number and label on a figure matches the fragment text.
- No EWS patch content.
- Nothing that defeats emissions or readiness.
- Never vent refrigerant.
- Don't edit fragments, pages or other makers' files. Report any text problem you find instead.

## Report (250 words at most)

- the files you wrote (SVG, generator, caption)
- the shoot.js results
- the data gaps you labelled on the figure
- any place where the text and the notes disagree
- any text you think the guide should change to match the figure
