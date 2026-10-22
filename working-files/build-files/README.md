# E46 M3 Touring guide: build files

Scripts and working records behind the guide at the top of this repository. The website doesn't use them.

| Folder | What it holds |
|---|---|
| `diagrams/round-3/`, `diagrams/round-3-extra/` | The scripts that drew the third round's figures: wiring pin maps, circuits, flowcharts and body figures (diagrams 01–26) |
| `diagrams/round-4/` | The scripts that drew diagrams 27–42 and redrew or fixed earlier ones, one folder per drawing session (`dm-arches`, `dm-floor`, `dm-chassis`, `dm-fuel`, `dm-cool`, `dm-coding-a`, `dm-coding-b`, `dm-xi`). Most `genNN.py` scripts write straight to `diagrams/NN-name.svg` |
| `round-4/` | How the fourth research round was folded in and reviewed: the briefs, the running log (`LOG.md`), each writer's change requests (`requests/`), the six reviewers' findings (`review-requests/`), and the scripts that split the pages into sections, joined them again and placed the figures (`frag.py`, `assemble.sh`, `tools/`) |
| `checks/` | Checks for the built website: every page at phone width, links between pages, old links forwarding to chapter pages, search, and screenshots |
| `job-cards/` | The scripts used to lay out and test the job cards page |
| `publish/sync_repo.py` | Copies the guide from the archeyon working copy into a clone of `pniessen/e46-m3-touring` and rebuilds its `docs/` folder. It leaves `working-files/` alone |

## Before you run anything

- The scripts ran in a temporary workspace, so many contain absolute paths to it (`/tmp/claude-0/…`) and to `/home/user/…`. Point those at your own copies first.
- They need Python 3 with BeautifulSoup (`pip install beautifulsoup4`), and Node with [Playwright](https://playwright.dev/) and Chromium for anything that measures text or takes screenshots. Some import the guide's own `tools/build_html.py`.
- The drawing scripts overwrite the SVG files in the guide's `diagrams/` folder. Commit or copy those first, and check the result in both light and dark themes before you keep it.
