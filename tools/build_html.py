#!/usr/bin/env python3
"""Build the phone-friendly HTML version of the guide from its Markdown source.

    python3 tools/build_html.py OUT.html               # page fragment (for the Artifact viewer)
    python3 tools/build_html.py --standalone OUT.html  # full HTML document to open locally
    --photos=inline|link|omit  embed photos as data URIs (default), keep photos/ paths, or drop them

That one-file version holds the whole guide. The website, built by tools/build_site.py, splits the
guide into a home page and one page per chapter (build_guide() below) and adds a search box.
Needs pandoc (GitHub-flavoured Markdown -> HTML) and BeautifulSoup.
Diagrams referenced as ![...](diagrams/*.svg) are inlined so they follow the page theme.
"""
import base64
import html
import json
import pathlib
import re
import subprocess
import sys

from bs4 import BeautifulSoup, NavigableString

ROOT = pathlib.Path(__file__).resolve().parent.parent
TOOLS = ROOT / "tools"

GUIDE_TITLE = "E46 M3 Touring Conversion"
GUIDE_EYEBROW = "Build guide &middot; US 325i Touring, manual &middot; home garage with welding"

# Short labels for the sticky chapter bar, keyed by the H2 id pandoc generates.
NAV_LABELS = {
    "overview": "Overview",
    "plan-and-budget": "Plan",
    "parts-list": "Parts",
    "step-by-step-build": "Steps",
    "deep-dive-chassis-and-drivetrain": "Chassis",
    "deep-dive-electronics-and-coding": "Electronics",
    "deep-dive-bodywork-and-fitment": "Body",
    "registration-and-legal-us": "Legal",
    "sources": "Sources",
    "appendix": "Appendix",
    # Wiring and coding manual
    "engine-harness-and-dme": "Engine harness",
    "body-side-wiring": "Body wiring",
    "fuel-pump-control": "Fuel pump",
    "checks-before-first-power-up": "Power-up checks",
    "coding-step-by-step": "Coding",
    "readiness-and-inspection": "Readiness",
}
# Sidebar labels for headings that are whole sentences (the research notes), by how they start.
NAV_TEXT_LABELS = [
    ("A fourth round in October 2026", "Round 4: what changed"),
    ("Five jobs on X60004", "Wiring: five jobs on X60004"),
    ("The 325i's own pump relay", "Fuel pump and lines"),
    ("BMW's documents settle the torque", "Torque values"),
    ("The Touring floor is sedan steel", "The Touring floor"),
    ("A convertible's quarter", "Convertible quarter panels"),
    ("Coding follows a fixed order", "Coding order"),
    ("Only five openly licensed photos", "Photos"),
    ("YouTube shows the metalwork", "YouTube"),
]
CHAPTER_KEYS = {"parts-list": "parts", "step-by-step-build": "steps"}

# Every page of the site, in site-navigation order. A page is built when its Markdown file exists.
# "fill" pages turn empty table cells and task lists into fields saved in the browser.
PAGES = [
    {"key": "guide", "md": "README.md", "html": "index.html", "label": "Guide",
     "eyebrow": GUIDE_EYEBROW},
    {"key": "wiring", "md": "WIRING-AND-CODING.md", "html": "wiring-and-coding.html",
     "label": "Wiring and coding", "eyebrow": "Wiring and coding manual &middot; companion to the build guide"},
    {"key": "cards", "md": "JOB-CARDS.md", "html": "job-cards.html", "label": "Job cards",
     "eyebrow": "Job cards &middot; one printable page per phase", "fill": True},
    {"key": "sheets", "md": "WORKSHEETS.md", "html": "worksheets.html", "label": "Worksheets",
     "eyebrow": "Worksheets &middot; print them, or fill them in here", "fill": True},
    {"key": "calc", "md": "CALCULATORS.md", "html": "calculators.html", "label": "Calculators",
     "eyebrow": "Calculators &middot; gearing, tires and wheel fitment",
     "css": "calculators.css", "js": "calculators.js"},
    {"key": "research", "md": "research.md", "html": "research.html", "label": "Research notes",
     "eyebrow": "Research notes &middot; companion to the build guide"},
]

# On the website the guide (README.md) is a home page plus one page per chapter, in reading order.
# "h2" lists the H2 sections a page holds. "h3" instead moves H3 sections, each with everything under
# it, out of their chapter onto a page of their own; with "promote", a single moved H3 becomes the
# page title and its H4s the page's sections.
GUIDE_CHAPTERS = [
    {"key": "overview", "html": "overview.html", "title": "Overview", "short": "Overview",
     "h2": ["overview"],
     "blurb": "What you're building, the recipe documented builds follow, how hard each job is, "
              "what to decide before you spend money, and the builds compared."},
    {"key": "plan", "html": "plan-and-budget.html", "title": "Plan and budget", "short": "Plan",
     "h2": ["plan-and-budget"],
     "blurb": "Check your own Touring, choose the donor, then budget and time, factory documents and "
              "coding kit, tools, space, shop briefs and safety."},
    {"key": "parts", "html": "parts-list.html", "title": "Parts list", "short": "Parts",
     "h2": ["parts-list"],
     "blurb": "Every part by system: from the donor, buy new, fabricate or keep. "
              "Tick them off as you go; the ticks stay in your browser."},
    {"key": "steps", "html": "step-by-step-build.html", "title": "Step-by-step build", "short": "Steps",
     "h2": ["step-by-step-build"],
     "blurb": "The build in 14 phases, from paperwork and the donor to first start, shakedown and "
              "inspection, with the checks that prove each step."},
    {"key": "chassis", "html": "chassis-and-drivetrain.html", "title": "Chassis and drivetrain",
     "short": "Chassis", "h2": ["deep-dive-chassis-and-drivetrain"], "kind": "deep dive",
     "blurb": "Subframe mounts, trunk floor and exhaust, welding, the S54 refresh, front and rear axles, "
              "suspension, brakes and bleeding."},
    {"key": "fuel", "html": "fuel-cooling-and-ac.html", "title": "Fuel, cooling and A/C",
     "short": "Fuel & cooling", "h3": ["fuel-system", "cooling-and-oil-cooler", "air-conditioning"],
     "kind": "deep dive",
     "blurb": "The M3 fuel system from tank to rail, then cooling, fans and the oil cooler, "
              "and the air conditioning."},
    {"key": "xi", "html": "325xi.html", "title": "325xi: rear drive or all-wheel drive", "short": "325xi",
     "h3": ["325xi-rear-drive-or-all-wheel-drive"], "promote": True, "kind": "deep dive",
     "blurb": "Only if your car is a 325xi: converting it to rear drive, which we recommend, "
              "or keeping all-wheel drive.",
     "tag": "Only for a 325xi"},
    {"key": "electronics", "html": "electronics-and-coding.html", "title": "Electronics and coding",
     "short": "Electronics", "h2": ["deep-dive-electronics-and-coding"], "kind": "deep dive",
     "blurb": "Harness re-pinning, fuel-pump control, the immobilizer, cluster and mileage, DSC, "
              "inspection readiness and troubleshooting."},
    {"key": "body", "html": "bodywork-and-fitment.html", "title": "Bodywork and fitment", "short": "Body",
     "h2": ["deep-dive-bodywork-and-fitment"], "kind": "deep dive",
     "blurb": "The M3 front end, the rear-arch graft step by step, rear doors, wheels and offsets, "
              "bumper and trim."},
    {"key": "legal", "html": "registration-and-legal.html", "title": "Registration and legal (US)",
     "short": "Legal", "h2": ["registration-and-legal-us"],
     "blurb": "What Massachusetts and California require of an engine swap, plus A/C, odometer, "
              "title and insurance."},
    {"key": "reference", "html": "sources-and-appendix.html", "title": "Sources and appendix",
     "short": "Sources", "h2": ["sources", "appendix"],
     "blurb": "Where the guide's claims come from, then torques, fluids, alignment, key numbers, "
              "glossary and open questions."},
]


def page_links(guide_href: str = "index.html") -> dict:
    """Map each page's Markdown file name to the HTML file that links should point at."""
    links = {pg["md"]: pg["html"] for pg in PAGES}
    links["README.md"] = guide_href
    return links

ALERTS = {
    "NOTE": ("note", "Note"),
    "TIP": ("tip", "Tip"),
    "IMPORTANT": ("key", "Key point"),
    "WARNING": ("warn", "Warning"),
    "CAUTION": ("crit", "Safety"),
}

COLOPHON = """  <p>Compiled from enthusiast forums, build logs, vendor DIYs and videos (see Sources). Specs and part numbers vary by build date and market: confirm against your VIN on RealOEM and BMW TIS before ordering or torquing.</p>
  <p>This is a planning guide, not a substitute for the factory repair manual, a qualified welder or local legal advice. Work safely: support the car on stands, disconnect the battery, and never weld near fuel.</p>
  <p>An independent enthusiast project, not affiliated with or endorsed by BMW AG. BMW and M3 are trademarks of BMW AG.</p>"""

SEARCH_ICON = ('<svg viewBox="0 0 20 20" aria-hidden="true" focusable="false"><circle cx="8.5" cy="8.5" r="5.5" '
               'fill="none" stroke="currentColor" stroke-width="2"/><path d="M12.6 12.6l4.6 4.6" '
               'stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>')
SEARCH_BUTTON = (f'<li class="search-item"><button type="button" class="search-open" aria-label="Search the site">'
                 f'{SEARCH_ICON}<span class="lbl-full">Search</span></button></li>')
SEARCH_PANEL = """<div class="search-panel" role="dialog" aria-modal="true" aria-label="Search" hidden>
  <div class="wrap">
    <form class="search-form" role="search">
      <input type="search" class="search-q" placeholder="Search the guide, manual, cards and sheets" autocomplete="off" spellcheck="false" aria-label="Search the site">
      <button type="button" class="search-close">Close</button>
    </form>
    <p class="search-status" aria-live="polite"></p>
    <ol class="search-results"></ol>
  </div>
</div>"""


def md_to_html(md_text: str) -> str:
    md_text = re.sub(r"<!-- toc -->.*?<!-- /toc -->", "", md_text, flags=re.S)
    # Notes meant only for readers of the Markdown on GitHub (e.g. "read it as a website").
    md_text = re.sub(r"<!-- github-only -->.*?<!-- /github-only -->", "", md_text, flags=re.S)
    # The Markdown escapes dollar signs (\$) so GitHub doesn't read prices as math.
    # Pandoc mishandles some of those escapes, so unescape them and turn its math parsing off.
    md_text = md_text.replace("\\$", "$")
    res = subprocess.run(
        ["pandoc", "-f", "gfm-tex_math_dollars", "-t", "html", "--wrap=none"],
        input=md_text, capture_output=True, text=True, check=True,
    )
    return res.stdout


def inline_svg(path: pathlib.Path, prefix: str) -> str:
    svg = path.read_text(encoding="utf-8")
    svg = re.sub(r"<\?xml[^>]*\?>", "", svg)
    svg = re.sub(r"<!--.*?-->", "", svg, flags=re.S)
    svg = re.sub(r"<style>.*?</style>", "", svg, flags=re.S)
    svg = re.sub(r'<rect class="bg"[^>]*/>', "", svg)
    svg = re.sub(r'\s(?:color|font-family)="[^"]*"', "", svg, count=0)
    svg = re.sub(r'\sxmlns:xlink="[^"]*"', "", svg)
    # Make ids unique per diagram so markers never collide across figures.
    ids = set(re.findall(r'\sid="([^"]+)"', svg))
    for i in ids:
        svg = svg.replace(f'id="{i}"', f'id="{prefix}-{i}"')
        svg = svg.replace(f"url(#{i})", f"url(#{prefix}-{i})")
        svg = svg.replace(f'href="#{i}"', f'href="#{prefix}-{i}"')
    return svg.strip()


def short_label(text: str, limit: int = 18) -> str:
    """A chapter-bar label for headings that have no entry in NAV_LABELS."""
    out = ""
    for word in text.split():
        if out and len(out) + 1 + len(word) > limit:
            break
        out = f"{out} {word}".strip()
    words = out.rstrip(":,;").split()
    while len(words) > 1 and words[-1].lower().rstrip(":,;") in {"and", "or", "of", "the", "to", "with", "for", "a"}:
        words.pop()
    return " ".join(words).rstrip(":,;") or text


def chapter_labels(sid: str, text: str) -> tuple:
    """(short, full): the short label for the phone chip bar, the full one for the desktop sidebar.

    The sidebar shows the heading itself unless it's a long sentence; job cards read
    "3a Rod bearings" in the chip bar.
    """
    plain = text.replace("’", "'")
    mapped = next((label for prefix, label in NAV_TEXT_LABELS if plain.startswith(prefix)), None)
    full = mapped or (text if len(text) <= 48 else short_label(text, 30))
    card = re.match(r"Card (\w+): (?:Bench work, )?(.+)", text)
    if sid in NAV_LABELS:
        short = NAV_LABELS[sid]
    elif card:
        short = card.group(1) + " " + card.group(2)[:1].upper() + card.group(2)[1:]
    else:
        short = short_label(mapped or text)
    return short, full


def guide_anchors(soup) -> dict:
    """Map every id in the rendered guide to the chapter page (GUIDE_CHAPTERS) that will hold it."""
    by_h2 = {sid: ch["html"] for ch in GUIDE_CHAPTERS for sid in ch.get("h2", [])}
    moves = {hid: ch["html"] for ch in GUIDE_CHAPTERS for hid in ch.get("h3", [])}
    anchors, page, moved = {}, None, None
    for el in soup.find_all(True):  # document order
        if el.name == "h2":
            page, moved = by_h2.get(el.get("id")), None
        elif el.name == "h3":
            moved = moves.get(el.get("id"))
        here = moved or page
        if here and el.get("id"):
            anchors[el["id"]] = here
    return anchors


def rewrite_links(soup, md_name: str, links: dict, anchors=None) -> None:
    """Point links at the right HTML page.

    Links to another page's Markdown file (WIRING-AND-CODING.md#x) go to its HTML. When the guide is
    split (anchors maps each guide id to its chapter page), links into the guide go straight to the
    chapter page that holds the target; other links within a page keep only their anchor.
    """
    for a in soup.find_all("a", href=True):
        path, _, frag = a["href"].partition("#")
        path = path[2:] if path.startswith("./") else path
        into_guide = path == "README.md" or (path == "" and md_name == "README.md")
        if anchors is not None and into_guide and frag in anchors:
            a["href"] = anchors[frag] + "#" + frag
        elif path == md_name:
            a["href"] = "#" + frag if frag else "#"
        elif path in links:
            a["href"] = links[path] + ("#" + frag if frag else "")


def render(md_path: pathlib.Path, *, photo_mode: str, link_map: dict, spec_strip: bool,
           anchors=None, split: bool = False) -> dict:
    """Markdown -> the page body as soup, sectioned on H2, plus the masthead pieces.

    split=True (the guide on the website) works out which chapter page holds each id first, so that
    every link, including those in the masthead, points at the right page.
    """
    md = md_path.read_text(encoding="utf-8")
    base = md_path.parent  # diagram paths resolve relative to the Markdown file
    portrait = {m.group(1) for m in
                re.finditer(r"!\[[^\]]*\]\((diagrams/[^)]+\.svg)\)\s*<!-- portrait -->", md)}
    soup = BeautifulSoup(md_to_html(md), "html.parser")
    if split:
        anchors = guide_anchors(soup)
    rewrite_links(soup, md_path.name, link_map, anchors)

    # Masthead pieces: H1, intro paragraphs and (for the guide) the first table ("at a glance").
    h1 = soup.find("h1")
    title_text = h1.get_text(" ", strip=True) if h1 else GUIDE_TITLE
    intro, spec_rows = [], []
    in_intro = True  # only the paragraphs right under the H1 go in the masthead
    node = h1.next_sibling if h1 else None
    while node is not None and not (getattr(node, "name", None) == "h2"):
        nxt = node.next_sibling
        name = getattr(node, "name", None)
        if name == "p" and in_intro and not spec_rows:
            intro.append(node.extract())
        elif name == "table" and spec_strip and not spec_rows:
            for tr in node.find_all("tr"):
                cells = tr.find_all(["td", "th"])
                if len(cells) == 2 and tr.parent.name == "tbody":
                    spec_rows.append((cells[0].decode_contents(), cells[1].decode_contents()))
            node.extract()
        elif name is not None:
            in_intro = False
        node = nxt
    if h1:
        h1.extract()

    # Callouts from GitHub alert syntax.
    for bq in soup.find_all("blockquote"):
        p = bq.find("p")
        if not p:
            continue
        first = p.contents[0] if p.contents else None
        if not isinstance(first, NavigableString):
            continue
        m = re.match(r"\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*", str(first))
        if not m:
            continue
        kind, label = ALERTS[m.group(1)]
        first.replace_with(NavigableString(str(first)[m.end():]))
        if not p.get_text(strip=True) and not p.find(True):
            p.decompose()
        bq.name = "aside"
        bq["class"] = ["callout", f"callout-{kind}"]
        tag = soup.new_tag("span", attrs={"class": "callout-label"})
        tag.string = label
        bq.insert(0, tag)

    # Diagrams: replace <img> with inline SVG figures (placeholders swapped in after serialising).
    placeholders = {}
    for n, img in enumerate(soup.find_all("img")):
        src = img.get("src", "")
        if not (src.startswith("diagrams/") and src.endswith(".svg")):
            continue
        key = f"@@SVG{n}@@"
        placeholders[key] = inline_svg(base / src, "d" + pathlib.Path(src).stem)
        container = img.parent if img.parent and img.parent.name in ("p", "figure") else img
        caption_html = None
        nxt = container.find_next_sibling()
        if nxt is not None and nxt.name == "p" and nxt.get_text(strip=True).startswith("Figure"):
            em = nxt.find("em")
            caption_html = (em.decode_contents() if em and len(nxt.contents) == 1 else nxt.decode_contents())
            nxt.decompose()
        fig = soup.new_tag("figure", attrs={"class": "diagram"})
        scroll_cls = "diagram-scroll portrait" if src in portrait else "diagram-scroll"
        scroll = soup.new_tag("div", attrs={"class": scroll_cls})
        scroll.append(NavigableString(key))
        fig.append(scroll)
        if src not in portrait:
            hint = soup.new_tag("p", attrs={"class": "scroll-hint"})
            hint.string = "Swipe sideways to see the whole diagram"
            fig.append(hint)
        cap = soup.new_tag("figcaption")
        cap.append(BeautifulSoup(caption_html or img.get("alt", ""), "html.parser"))
        fig.append(cap)
        container.replace_with(fig)

    # Photos: ![alt](photos/name.jpg) followed by a "*Photo: ... credit ...*" paragraph.
    # "link" keeps the file reference (website), "inline" embeds it (self-contained page), "omit" drops it.
    for img in soup.find_all("img"):
        src = img.get("src", "")
        if not src.startswith("photos/"):
            continue
        container = img.parent if img.parent and img.parent.name == "p" else img
        caption_html = None
        nxt = container.find_next_sibling()
        if nxt is not None and nxt.name == "p" and nxt.get_text(strip=True).startswith("Photo"):
            em = nxt.find("em")
            caption_html = (em.decode_contents() if em and len(nxt.contents) == 1 else nxt.decode_contents())
            nxt.decompose()
        if photo_mode == "omit":
            container.decompose()
            continue
        path = base / src
        attrs = {"src": src, "alt": img.get("alt", ""), "loading": "lazy", "decoding": "async"}
        try:
            from PIL import Image
            with Image.open(path) as im:
                attrs["width"], attrs["height"] = str(im.width), str(im.height)
        except Exception:
            pass
        if photo_mode == "inline":
            mime = {".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
                    ".webp": "image/webp"}.get(path.suffix.lower(), "image/jpeg")
            attrs["src"] = f"data:{mime};base64," + base64.b64encode(path.read_bytes()).decode("ascii")
        fig = soup.new_tag("figure", attrs={"class": "photo"})
        fig.append(soup.new_tag("img", attrs=attrs))
        if caption_html:
            cap = soup.new_tag("figcaption")
            cap.append(BeautifulSoup(caption_html, "html.parser"))
            fig.append(cap)
        container.replace_with(fig)

    # Two photos in a row sit side by side on wider screens.
    for fig in soup.find_all("figure", class_="photo"):
        if "photo-pair" in (fig.parent.get("class") or []):
            continue
        nxt = fig.find_next_sibling()
        if nxt is not None and nxt.name == "figure" and "photo" in (nxt.get("class") or []):
            pair = soup.new_tag("div", attrs={"class": "photo-pair"})
            fig.insert_before(pair)
            pair.append(fig.extract())
            pair.append(nxt.extract())
            # A much taller photo is cropped to 3:2 beside its partner, so the pair lines up.
            for img in pair.find_all("img"):
                w, h = int(img.get("width") or 0), int(img.get("height") or 0)
                if w and h / w > 0.8:
                    img["class"] = "crop-tall"

    # Tables scroll inside their own box.
    for table in soup.find_all("table"):
        wrap = soup.new_tag("div", attrs={"class": "table-wrap"})
        table.wrap(wrap)

    # Remove "Back to top" style links used in the Markdown version.
    for a in soup.find_all("a", href="#contents"):
        parent = a.parent
        a.decompose()
        if parent and parent.name == "p" and not parent.get_text(strip=True):
            parent.decompose()

    # Sectionise on H2.
    main = soup.new_tag("div", attrs={"class": "wrap"})
    section = None
    nav = []
    for el in list(soup.contents):
        if getattr(el, "name", None) == "h2":
            sid = el.get("id", "")
            section = soup.new_tag("section", attrs={"id": sid})
            if sid in CHAPTER_KEYS:
                section["data-chapter"] = CHAPTER_KEYS[sid]
            del el["id"]
            main.append(section)
            nav.append((sid, *chapter_labels(sid, el.get_text(" ", strip=True))))
        if section is None:
            if isinstance(el, NavigableString) and not el.strip():
                continue
            main.append(el.extract())
        else:
            section.append(el.extract())

    return {"soup": soup, "main": main, "nav": nav, "title_text": title_text, "intro": intro,
            "spec_rows": spec_rows, "placeholders": placeholders, "anchors": anchors}


def sub_links(sections) -> list:
    """(id, text) for the H3 headings of the given sections: the sidebar's section links."""
    return [(h.get("id"), h.get_text(" ", strip=True)) for sec in sections for h in sec.find_all("h3") if h.get("id")]


def fill_svgs(body_html: str, placeholders: dict) -> str:
    for key, svg in placeholders.items():
        body_html = body_html.replace(key, svg)
    return body_html


def assemble(*, title: str, eyebrow: str, title_text: str, body_html: str, nav_html: str,
             intro_html: str = "", spec_block: str = "", site_nav=None, page_key: str = "guide",
             fill: bool = False, artifact_meta: bool = True, head_extra: str = "", footer_extra: str = "",
             extra_css: str = "", extra_js: str = "", standalone: bool = True, search: bool = False) -> str:
    """Wrap a page body in the site's masthead, navigation, footer, styles and scripts."""
    css = (TOOLS / "page.css").read_text(encoding="utf-8")
    js = (TOOLS / "page.js").read_text(encoding="utf-8")
    site_nav_html = ""
    if site_nav:
        links = ""
        for label, href, current in site_nav:
            cur = ' aria-current="page"' if current else ""
            links += f'<li><a href="{href}"{cur}>{label}</a></li>'
        site_nav_html = f'<nav class="sitenav" aria-label="Site"><ul>{links}</ul></nav>'
    meta = '<meta name="claude:viewport-fit-sides" content="cover">\n' if artifact_meta else ""
    search_btn = SEARCH_BUTTON if search else ""
    search_panel = SEARCH_PANEL + "\n" if search else ""

    page = f"""<title>{title}</title>
{meta}{head_extra}<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:ital,wght@0,400;0,500;0,600;1,400&family=Saira+Condensed:wght@600;700&display=swap">
<style>
{css}{extra_css}
</style>
<header class="masthead">
  <div class="wrap">
    {site_nav_html}
    <p class="eyebrow">{eyebrow}</p>
    <h1>{title_text}</h1>
    {intro_html}
    {spec_block}
  </div>
</header>
<nav class="chapters" aria-label="Chapters"><ol>{search_btn}{nav_html}</ol></nav>
<main data-page="{page_key}"{' data-fill' if fill else ''}>{body_html}</main>
{search_panel}<footer class="colophon"><div class="wrap">
{COLOPHON}
{footer_extra}</div></footer>
<script>
{js}{extra_js}
</script>
"""
    if standalone:
        page = ("<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
                "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1, viewport-fit=cover\">\n"
                + page.replace("<header", "</head>\n<body>\n<header", 1) + "</body>\n</html>\n")
    return page


def in_page_nav(nav: list, subs: dict) -> str:
    """Chapter navigation for a page whose chapters are its own H2 sections."""
    out = ""
    for sid, short, full in nav:
        sub_html = "".join(f'<li><a href="#{hid}">{text}</a></li>' for hid, text in subs.get(sid, []))
        sub_html = f'<ol class="sub">{sub_html}</ol>' if sub_html else ""
        label = short if short == full else f'<span class="lbl-short">{short}</span><span class="lbl-full">{full}</span>'
        out += f'<li><a href="#{sid}">{label}</a>{sub_html}</li>'
    return out


def build_page(md_path: pathlib.Path, *, standalone: bool, title: str = GUIDE_TITLE,
               eyebrow: str = GUIDE_EYEBROW, spec_strip: bool = True, artifact_meta: bool = True,
               head_extra: str = "", site_nav=None, footer_extra: str = "",
               photo_mode: str = "inline", page_key: str = "guide", fill: bool = False,
               link_map=None, extra_css: str = "", extra_js: str = "", anchors=None,
               search: bool = False, index=None) -> str:
    """Render one Markdown file as a themed page.

    site_nav is an optional list of (label, href, is_current) links shown above the title.
    photo_mode is "inline" (embed photos as data URIs), "link" (keep photos/ paths) or "omit".
    link_map rewrites links to other pages' Markdown files (e.g. WIRING-AND-CODING.md#x) to their HTML;
    anchors (from build_guide) sends links into the guide to the chapter page that holds the target.
    fill marks the page so page.js turns empty table cells and task lists into saved fields.
    search adds the search button and panel; index, a list, collects the page's search entries.
    """
    r = render(md_path, photo_mode=photo_mode, link_map=page_links() if link_map is None else link_map,
               spec_strip=spec_strip, anchors=anchors)
    main = r["main"]
    subs = {sec.get("id", ""): sub_links([sec]) for sec in main.find_all("section", recursive=False)}
    if index is not None:
        lead = " ".join(t for t in (_text(el) for el in main.children
                                     if getattr(el, "name", None) not in (None, "section")) if t)
        if lead:
            index.append(["", r["title_text"], lead])
        index.extend(search_entries(main.find_all("section", recursive=False), "", None))
    body_html = fill_svgs(str(main), r["placeholders"])
    intro_html = "".join(f'<p class="lede">{p.decode_contents()}</p>' for p in r["intro"])
    spec_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in r["spec_rows"])
    return assemble(
        title=title, eyebrow=eyebrow, title_text=r["title_text"], body_html=body_html,
        nav_html=in_page_nav(r["nav"], subs), intro_html=intro_html,
        spec_block=f'<dl class="spec">{spec_html}</dl>' if spec_html else "", site_nav=site_nav,
        page_key=page_key, fill=fill, artifact_meta=artifact_meta, head_extra=head_extra,
        footer_extra=footer_extra, extra_css=extra_css, extra_js=extra_js, standalone=standalone,
        search=search)


# --- Search -------------------------------------------------------------------------------------

def _text(el) -> str:
    """Readable text of an element for the search index (diagram placeholders dropped)."""
    if isinstance(el, NavigableString):
        s = str(el)
    else:
        s = el.get_text(" ", strip=True)
    s = re.sub(r"@@SVG\d+@@", " ", s)
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([,.;:!?)\]])", r"\1", s)  # get_text's separator also lands before punctuation
    return re.sub(r"([(\[])\s+", r"\1", s).strip()


def search_entries(sections, page_href: str, page_title) -> list:
    """Search entries for a page: one per H2 section intro and per H3 or H4, as [anchor, heading, text].

    page_title, when given, names a section whose own H2 was moved into the masthead.
    """
    out = []
    for sec in sections:
        sid = sec.get("id", "")
        h2 = sec.find("h2", recursive=False)
        cur = [sid, h2.get_text(" ", strip=True) if h2 else (page_title or sid), []]
        out.append(cur)
        for el in sec.children:
            name = getattr(el, "name", None)
            if name in ("h3", "h4") and el.get("id"):
                cur = [el["id"], el.get_text(" ", strip=True), []]
                out.append(cur)
            elif name == "h2":
                continue
            else:
                t = _text(el)
                if t:
                    cur[2].append(t)
    return [[a, h, " ".join(t)] for a, h, t in out if t]


def search_index_js(groups: list) -> str:
    """groups: [(href, page label, entries)] -> search-index.js, loaded by page.js on first search."""
    pages, items = [], []
    for i, (href, label, entries) in enumerate(groups):
        pages.append([href, label])
        for anchor, head, text in entries:
            items.append([i, anchor, head, text])
    data = json.dumps({"pages": pages, "items": items}, ensure_ascii=False, separators=(",", ":"))
    return "window.E46_SEARCH=" + data + ";\n"


# --- The guide as a home page plus chapter pages ------------------------------------------------

def build_guide(md_path: pathlib.Path, *, link_map: dict, home_href: str, site_nav, standalone_home: bool,
                artifact_meta: bool, head_extra_for, footer_extra: str, photo_mode: str = "link",
                companions=()) -> dict:
    """Split the guide into index.html (home) and one page per chapter.

    head_extra_for(key, title, html_name) gives each page's <head> extras (website meta tags).
    companions: [(label, href, description)] for the home page's list of the other pages.
    Returns {"pages": {html name: page}, "anchors": {id: html name}, "index": [(href, label, entries)]}.
    """
    r = render(md_path, photo_mode=photo_mode, link_map=link_map, spec_strip=True, split=True)
    soup, main, anchors = r["soup"], r["main"], r["anchors"]
    sections = {sec.get("id", ""): sec for sec in main.find_all("section", recursive=False)}

    # Pull each moved H3 section out of its chapter, with everything up to the next H3 or H2.
    page_sections = {}
    for ch in GUIDE_CHAPTERS:
        if ch.get("h3"):
            promote = ch.get("promote") and len(ch["h3"]) == 1
            sec = soup.new_tag("section", attrs={"id": ch["h3"][0] if promote else ch["html"][:-len(".html")]})
            for hid in ch["h3"]:
                h3 = main.find("h3", id=hid)
                node = h3.next_sibling
                if promote:
                    h3.decompose()  # the masthead carries it
                else:
                    sec.append(h3.extract())
                while node is not None and getattr(node, "name", None) not in ("h2", "h3"):
                    nxt = node.next_sibling
                    sec.append(node.extract())
                    node = nxt
            if promote:
                for h in sec.find_all(["h4", "h5", "h6"]):  # its H4s are the new page's sections
                    h.name = "h" + str(int(h.name[1]) - 1)
            page_sections[ch["key"]] = [sec]
        else:
            page_sections[ch["key"]] = [sections[sid] for sid in ch["h2"]]
    for ch in GUIDE_CHAPTERS:
        secs = page_sections[ch["key"]]
        if len(secs) == 1 and not ch.get("h3"):
            h2 = secs[0].find("h2", recursive=False)
            if h2:
                h2.decompose()  # the masthead carries the chapter title

    n = len(GUIDE_CHAPTERS)
    out_pages, index = {}, []

    def nav_item(href: str, label: str, current: bool, subs_html: str) -> str:
        li = '<li class="open">' if current else "<li>"
        cur = ' aria-current="page"' if current else ""
        return f'{li}<a href="{href}"{cur}>{label}</a>{subs_html if current else ""}</li>'

    def chapter_nav(current_key, subs_html: str) -> str:
        items = [nav_item(home_href, '<span class="lbl-short">Home</span><span class="lbl-full">Guide home</span>',
                          current_key is None, subs_html)]
        for ch in GUIDE_CHAPTERS:
            label = (ch["short"] if ch["short"] == ch["title"] else
                     f'<span class="lbl-short">{ch["short"]}</span><span class="lbl-full">{ch["title"]}</span>')
            items.append(nav_item(ch["html"], label, ch["key"] == current_key, subs_html))
        return "".join(items)

    for i, ch in enumerate(GUIDE_CHAPTERS):
        secs = page_sections[ch["key"]]
        wrap = soup.new_tag("div", attrs={"class": "wrap"})
        for sec in secs:
            wrap.append(sec.extract() if sec.parent is not None else sec)
        # Links to this page keep only their anchor, so they scroll instead of reloading.
        for a in wrap.find_all("a", href=True):
            if a["href"].startswith(ch["html"] + "#"):
                a["href"] = a["href"][len(ch["html"]):]
        # Section links for the sidebar: H3s, and on a two-chapter page the H2s as well.
        sub = []
        for sec in secs:
            h2 = sec.find("h2", recursive=False)
            if h2 is not None and len(secs) > 1:
                sub.append(f'<li class="sub-h2"><a href="#{sec.get("id")}">{h2.get_text(" ", strip=True)}</a></li>')
            sub += [f'<li><a href="#{hid}">{text}</a></li>' for hid, text in sub_links([sec])]
        subs_html = f'<ol class="sub">{"".join(sub)}</ol>' if sub else ""
        prev_ch = GUIDE_CHAPTERS[i - 1] if i > 0 else None
        next_ch = GUIDE_CHAPTERS[i + 1] if i + 1 < n else None
        prev_html = (f'<a class="prev" href="{prev_ch["html"]}"><span>Previous</span>{prev_ch["title"]}</a>'
                     if prev_ch else f'<a class="prev" href="{home_href}"><span>Previous</span>Guide home</a>')
        next_html = (f'<a class="next" href="{next_ch["html"]}"><span>Next</span>{next_ch["title"]}</a>'
                     if next_ch else f'<a class="next" href="{home_href}"><span>Back to</span>Guide home</a>')
        pager = BeautifulSoup(f'<nav class="pager" aria-label="Guide chapters">{prev_html}{next_html}</nav>',
                              "html.parser")
        wrap.append(pager)
        index.append((ch["html"], ch["title"], search_entries(secs, ch["html"], ch["title"])))
        kind = f' &middot; {ch["kind"]}' if ch.get("kind") else ""
        eyebrow = f'Build guide{kind} &middot; part {i + 1} of {n}'
        title = f'{ch["title"]} · {GUIDE_TITLE}'
        out_pages[ch["html"]] = assemble(
            title=title, eyebrow=eyebrow, title_text=html.escape(ch["title"]),
            body_html=fill_svgs(str(wrap), r["placeholders"]), nav_html=chapter_nav(ch["key"], subs_html),
            site_nav=site_nav, page_key="guide", artifact_meta=artifact_meta,
            head_extra=head_extra_for(ch["key"], title, ch["html"]), footer_extra=footer_extra,
            standalone=True, search=True)

    # Home: the masthead (title, intro, "at a glance"), a search field, where to start, the chapters.
    def chapter_link(ch, i):
        tag = f'<span class="tag">{ch["tag"]}</span>' if ch.get("tag") else ""
        return (f'<li><a href="{ch["html"]}"><span class="n">Part {i + 1}</span><strong>{ch["title"]}</strong>'
                f'{tag}<span class="d">{ch["blurb"]}</span></a></li>')

    by_key = {ch["key"]: ch for ch in GUIDE_CHAPTERS}
    hrefs = {k: by_key[k]["html"] for k in by_key}
    comp = {label: href for label, href, _ in companions}
    cards = comp.get("Job cards", "job-cards.html")
    sheets = comp.get("Worksheets", "worksheets.html")
    start = f"""<section id="home-start"><h2>Where to start</h2>
<ol class="start">
<li><strong>New to the project?</strong> Read the <a href="{hrefs['overview']}">Overview</a>, then <a href="{hrefs['plan']}">Plan and budget</a>. Together they show what the build involves and what to decide first.</li>
<li><strong>Is your car a 325xi?</strong> Read <a href="{hrefs['xi']}">the 325xi chapter</a> before you buy a donor: it changes which donor you want.</li>
<li><strong>Ready to build?</strong> Work through the <a href="{hrefs['steps']}">Step-by-step build</a> phase by phase. Each phase links to the deep dives for detail, and to its printable <a href="{cards}">job card</a> and <a href="{sheets}">worksheet</a>.</li>
<li><strong>Registering the car?</strong> <a href="{hrefs['legal']}">Registration and legal</a> covers what Massachusetts and California require of an engine swap.</li>
</ol>
</section>"""
    chapters = "".join(chapter_link(ch, i) for i, ch in enumerate(GUIDE_CHAPTERS))
    comp_html = "".join(f'<li><a href="{href}"><strong>{label}</strong><span class="d">{desc}</span></a></li>'
                        for label, href, desc in companions)
    home_body = f"""<div class="wrap">
<button type="button" class="search-open home-search">{SEARCH_ICON}<span>Search the guide, manual, cards and sheets</span></button>
{start}
<section id="home-chapters"><h2>The guide, part by part</h2>
<ol class="chapter-list">{chapters}</ol>
</section>
{'<section id="home-companions"><h2>Companion pages</h2><ul class="chapter-list companions">' + comp_html + '</ul></section>' if comp_html else ''}
</div>"""
    intro_html = "".join(f'<p class="lede">{p.decode_contents()}</p>' for p in r["intro"])
    spec_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in r["spec_rows"])
    # Old links to the one-page guide (index.html#phase-7-...) forward to the chapter page.
    order = [ch["html"] for ch in GUIDE_CHAPTERS]
    ids = {k: order.index(v) for k, v in anchors.items()}
    forward = ("\n(function () {\n  var pages = " + json.dumps(order) + ", ids = "
               + json.dumps(ids, separators=(",", ":")) + ";\n"
               "  var h = location.hash ? decodeURIComponent(location.hash.slice(1)) : \"\";\n"
               "  if (h && !document.getElementById(h) && Object.prototype.hasOwnProperty.call(ids, h)) {\n"
               "    location.replace(pages[ids[h]] + \"#\" + encodeURIComponent(h));\n  }\n})();\n")
    out_pages["index.html"] = assemble(
        title=GUIDE_TITLE, eyebrow=GUIDE_EYEBROW, title_text=r["title_text"], body_html=home_body,
        nav_html=chapter_nav(None, ""), intro_html=intro_html,
        spec_block=f'<dl class="spec">{spec_html}</dl>' if spec_html else "", site_nav=site_nav,
        page_key="guide", artifact_meta=artifact_meta, head_extra=head_extra_for("guide", GUIDE_TITLE, ""),
        footer_extra=footer_extra, extra_js=forward, standalone=standalone_home, search=True)
    return {"pages": out_pages, "anchors": anchors, "index": index}


def build(standalone: bool, photo_mode: str = "inline") -> str:
    """The whole guide as one page, as used for a local guide.html."""
    return build_page(ROOT / "README.md", standalone=standalone, photo_mode=photo_mode)


if __name__ == "__main__":
    args = sys.argv[1:]
    standalone = "--standalone" in args
    photo_mode = "inline"
    for a in list(args):
        if a.startswith("--photos="):
            photo_mode = a.split("=", 1)[1]
            if photo_mode not in ("inline", "link", "omit"):
                sys.exit("--photos must be inline, link or omit")
    args = [a for a in args if a != "--standalone" and not a.startswith("--photos=")]
    out = pathlib.Path(args[0]) if args else ROOT / "guide.html"
    out.write_text(build(standalone, photo_mode), encoding="utf-8")
    print(f"wrote {out} ({out.stat().st_size // 1024} KB)")
