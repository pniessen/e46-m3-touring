#!/usr/bin/env python3
"""Build the static website for GitHub Pages, or the Claude artifact bundle, from the Markdown pages.

    python3 tools/build_site.py OUT_DIR [--base-url URL] [--repo-url URL]
    python3 tools/build_site.py OUT_DIR --artifact

Each page in build_html.PAGES is built when its Markdown file sits next to tools/ (README.md is the
build guide and becomes index.html; WIRING-AND-CODING.md, JOB-CARDS.md, WORKSHEETS.md,
CALCULATORS.md and research.md become their own pages). Every page links to the others.

Website mode also writes 404.html, favicon.svg, og-image.png and .nojekyll, and copies diagrams/
and photos/. Artifact mode writes index.html as a page fragment (the artifact host adds the
document skeleton), the other pages as full documents, and files.json: the supporting files to
publish next to index.html, as {published path: source path}.
"""
import argparse
import html
import json
import pathlib
import shutil

from build_html import GUIDE_TITLE, PAGES, ROOT, TOOLS, build_page, page_links

ASSETS = TOOLS / "assets"
DEFAULT_BASE = "https://pniessen.github.io/e46-m3-touring/"
DEFAULT_REPO = "https://github.com/pniessen/e46-m3-touring"
DESCRIPTIONS = {
    "guide": ("A home-garage plan for converting a US E46 325i Touring into an M3 Touring: S54 engine, "
              "six-speed, M3 axles, brakes and arches. Parts list, step-by-step build, wiring, "
              "diagrams and sources."),
    "wiring": ("Wiring and coding manual for an S54 swap into a US E46 325i Touring: connector-by-connector "
               "re-pinning, fuel-pump control, checks before power-up and coding step by step."),
    "cards": "One printable job card per build phase: parts, tools, torques, fluids, steps and checks.",
    "sheets": ("Printable and fillable worksheets for the E46 M3 Touring build: baseline records, donor tests, "
               "coding backups, re-pin and continuity log, body measurements and shakedown log."),
    "calc": ("Calculators for the E46 M3 Touring build: gearing and road speed, tire size and speedometer, "
             "wheel fitment and offsets, and a tire load check."),
    "research": ("Research notes behind the E46 M3 Touring conversion guide: wiring, fuel-pump control, "
                 "torque specs, subframe reinforcement, arch steel, coding, photos and videos."),
}


def head_tags(title: str, description: str, url: str, image: str) -> str:
    t, d = html.escape(title, quote=True), html.escape(description, quote=True)
    return f"""<meta name="description" content="{d}">
<link rel="canonical" href="{url}">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<meta name="theme-color" content="#f2f4f6" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0e1114" media="(prefers-color-scheme: dark)">
<meta property="og:type" content="article">
<meta property="og:site_name" content="{html.escape(GUIDE_TITLE)}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image">
"""


def not_found_page(base: str) -> str:
    css = (TOOLS / "page.css").read_text(encoding="utf-8")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Page not found</title>
<link rel="icon" href="{base}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;600&family=Saira+Condensed:wght@700&display=swap">
<style>
{css}
</style>
</head>
<body>
<header class="masthead">
  <div class="wrap">
    <p class="eyebrow">404 &middot; {html.escape(GUIDE_TITLE)}</p>
    <h1>Page not found</h1>
    <p class="lede">There's nothing at this address. The build guide is at <a href="{base}">{base}</a>.</p>
  </div>
</header>
</body>
</html>
"""


def h1_of(md_path: pathlib.Path) -> str:
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return GUIDE_TITLE


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("out", type=pathlib.Path)
    ap.add_argument("--src", type=pathlib.Path, default=ROOT, help="folder holding the Markdown pages")
    ap.add_argument("--base-url", default=DEFAULT_BASE)
    ap.add_argument("--repo-url", default=DEFAULT_REPO)
    ap.add_argument("--artifact", action="store_true",
                    help="build the Claude artifact bundle instead of the website")
    ap.add_argument("--repo-link", action="store_true",
                    help="in artifact mode, also link the GitHub repository (once it exists)")
    a = ap.parse_args()
    base = a.base_url if a.base_url.endswith("/") else a.base_url + "/"
    out = a.out
    out.mkdir(parents=True, exist_ok=True)
    image = base + "og-image.png"
    pages = [pg for pg in PAGES if (a.src / pg["md"]).exists()]
    guide_href = "index.html" if a.artifact else "./"
    links = page_links(guide_href)

    def nav(current: str):
        items = [(pg["label"], guide_href if pg["key"] == "guide" else pg["html"], pg["key"] == current)
                 for pg in pages]
        if a.repo_link or not a.artifact:
            items.append(("Source on GitHub", a.repo_url, False))
        return items

    source = (f'Source, history and diagrams: <a href="{a.repo_url}">{a.repo_url.replace("https://", "")}</a>. '
              if a.repo_link or not a.artifact else "")
    footer = f'  <p>{source}Anything you tick or type on these pages is saved in your browser only.</p>\n'
    written = []
    for pg in pages:
        md = a.src / pg["md"]
        is_guide = pg["key"] == "guide"
        title = GUIDE_TITLE if is_guide else f"{h1_of(md)} · {GUIDE_TITLE}"
        url = base if is_guide else base + pg["html"]
        extra_css = (TOOLS / pg["css"]).read_text(encoding="utf-8") if pg.get("css") else ""
        extra_js = (TOOLS / pg["js"]).read_text(encoding="utf-8") if pg.get("js") else ""
        fragment = a.artifact and is_guide
        page = build_page(
            md, standalone=not fragment, title=title, eyebrow=pg["eyebrow"], spec_strip=is_guide,
            artifact_meta=a.artifact, photo_mode="link", page_key=pg["key"], fill=pg.get("fill", False),
            link_map=links, extra_css=extra_css, extra_js=extra_js, site_nav=nav(pg["key"]),
            head_extra="" if a.artifact else head_tags(title, DESCRIPTIONS[pg["key"]], url, image),
            footer_extra=footer)
        (out / pg["html"]).write_text(page, encoding="utf-8")
        written.append(pg["html"])

    if a.artifact:
        files = {pg["html"]: str((out / pg["html"]).resolve()) for pg in pages if pg["key"] != "guide"}
        photos = a.src / "photos"
        for f in sorted(photos.glob("*.jpg")) if photos.is_dir() else []:
            files[f"photos/{f.name}"] = str(f.resolve())
        (out / "files.json").write_text(json.dumps(files, indent=1), encoding="utf-8")
        print(f"artifact bundle in {out}: " + ", ".join(written) + f"; files.json lists {len(files)} files")
        return

    (out / "404.html").write_text(not_found_page(base), encoding="utf-8")
    (out / ".nojekyll").write_text("", encoding="utf-8")
    for name in ("favicon.svg", "og-image.png"):
        if (ASSETS / name).exists():
            shutil.copyfile(ASSETS / name, out / name)
            written.append(name)
    for folder in ("diagrams", "photos"):
        src = a.src / folder
        if src.is_dir() and src.resolve() != (out / folder).resolve():
            shutil.copytree(src, out / folder, dirs_exist_ok=True)
            written.append(folder + "/")
    written += ["404.html", ".nojekyll"]
    print(f"site written to {out}: " + ", ".join(written))


if __name__ == "__main__":
    main()
