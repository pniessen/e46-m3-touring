# Working files

Everything behind the guide that the website doesn't show. GitHub Pages publishes only `docs/`, so nothing in this folder appears on [the website](https://pniessen.github.io/e46-m3-touring/), though anyone can read it here.

| Folder | What it holds |
|---|---|
| `research_notes/E46 M3 Touring open questions/` | The research that re-checked the first draft's sources and answered its open questions: harness and body circuits, DME and EWS coding, fuel-pump control, torques, subframe reinforcement, convertible arch steel, photos and videos |
| `reports/` | The report written from those notes, which became the guide's [research page](../research.md) |
| `research_notes/E46 S54 Touring wiring details/` | The third round: factory wiring diagrams, body and network circuits, re-pinning practice, test values and Massachusetts rules |
| `research_notes/E46 M3 Touring coding, body and chassis/` | The fourth round: coding, rear arches, floor and exhaust, suspension, fuel, front axle and brakes, cooling and A/C, then a gap-filling pass (`gapfill_*.md`) and the two 325xi studies (`xi_*.md`) |
| `build-files/` | The scripts that drew the diagrams, the fourth round's log, change requests and reviews, the website checks and the publish script. Its [README](build-files/README.md) says what each part does |

The notes say how each claim was read: [read] means the page itself was read, [snippet] only a search engine's summary, [image] a diagram image and [captions] a video's captions. They quote their sources, including forum posts and BMW documents; follow the links for the originals.

The guide itself (`README.md`, `WIRING-AND-CODING.md`, `JOB-CARDS.md`, `WORKSHEETS.md`, `CALCULATORS.md`, `research.md`, `diagrams/`, `photos/`) is at the top of this repository, and `tools/build_site.py docs` rebuilds the website from it.
