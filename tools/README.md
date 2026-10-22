# Building the website

The Markdown files one folder up are the source: `README.md` (the build guide), `WIRING-AND-CODING.md`, `JOB-CARDS.md`, `WORKSHEETS.md`, `CALCULATORS.md` and `research.md`. The scripts here turn them into the static site that GitHub Pages serves from `docs/`.

## Rebuild

You need Python 3, [pandoc](https://pandoc.org/) and BeautifulSoup (`pip install beautifulsoup4`). From the repository root:

```sh
python3 tools/build_site.py docs
```

That rewrites every page in `docs/`, plus `404.html`, the icon, the link-preview image and copies of `diagrams/` and `photos/`. Commit `docs/` with your Markdown changes and GitHub Pages republishes within a minute or two.

## What's here

- `build_site.py`: builds the whole site (or, with `--artifact`, a bundle for a claude.ai page).
- `build_html.py`: renders one Markdown page into the site's layout: chapter sidebar, inline diagrams, callouts, fillable fields.
- `page.css`, `page.js`: the shared look and behavior, including light and dark themes, print styles, the parts checklist and the worksheet fields (saved in the reader's browser only).
- `calculators.css`, `calculators.js`: the calculators page.
- `assets/`: the icon and the link-preview card; `render_card.sh` re-renders the card as `og-image.png`.

Diagrams are SVG files in `diagrams/`. Each page inlines them, so they follow the reader's light or dark theme.
