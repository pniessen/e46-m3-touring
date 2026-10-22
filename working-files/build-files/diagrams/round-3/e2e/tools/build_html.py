#!/usr/bin/env python3
"""Build the phone-friendly HTML version of the guide from its Markdown source.

    python3 tools/build_html.py OUT.html               # page fragment (for the Artifact viewer)
    python3 tools/build_html.py --standalone OUT.html  # full HTML document to open locally
    --photos=inline|link|omit  embed photos as data URIs (default), keep photos/ paths, or drop them

The GitHub Pages website is built by tools/build_site.py, which reuses build_page() below.
Needs pandoc (GitHub-flavoured Markdown -> HTML) and BeautifulSoup.
Diagrams referenced as ![...](diagrams/*.svg) are inlined so they follow the page theme.
"""
import base64
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
}
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


def md_to_html(md_text: str) -> str:
    md_text = re.sub(r"<!-- toc -->.*?<!-- /toc -->", "", md_text, flags=re.S)
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
    return out.rstrip(":,;") or text


def build_page(md_path: pathlib.Path, *, standalone: bool, title: str = GUIDE_TITLE,
               eyebrow: str = GUIDE_EYEBROW, spec_strip: bool = True, artifact_meta: bool = True,
               head_extra: str = "", site_nav=None, footer_extra: str = "",
               photo_mode: str = "inline", page_key: str = "guide", fill: bool = False,
               link_map=None, extra_css: str = "", extra_js: str = "") -> str:
    """Render one Markdown file as a themed page.

    site_nav is an optional list of (label, href, is_current) links shown above the title.
    photo_mode is "inline" (embed photos as data URIs), "link" (keep photos/ paths) or "omit".
    link_map rewrites links to other pages' Markdown files (e.g. WIRING-AND-CODING.md#x) to their HTML.
    fill marks the page so page.js turns empty table cells and task lists into saved fields.
    """
    md = md_path.read_text(encoding="utf-8")
    base = md_path.parent  # diagram paths resolve relative to the Markdown file
    portrait = {m.group(1) for m in
                re.finditer(r"!\[[^\]]*\]\((diagrams/[^)]+\.svg)\)\s*<!-- portrait -->", md)}
    soup = BeautifulSoup(md_to_html(md), "html.parser")

    # Links to other pages' Markdown files point at their HTML; a link to this page keeps only its anchor.
    links = page_links() if link_map is None else link_map
    for a in soup.find_all("a", href=True):
        path, _, frag = a["href"].partition("#")
        path = path[2:] if path.startswith("./") else path
        if path == md_path.name:
            a["href"] = "#" + frag if frag else "#"
        elif path in links:
            a["href"] = links[path] + ("#" + frag if frag else "")

    # Masthead pieces: H1, intro paragraphs and (for the guide) the first table ("at a glance").
    h1 = soup.find("h1")
    title_text = h1.get_text(" ", strip=True) if h1 else title
    intro, spec_rows = [], []
    node = h1.next_sibling if h1 else None
    while node is not None and not (getattr(node, "name", None) == "h2"):
        nxt = node.next_sibling
        name = getattr(node, "name", None)
        if name == "p" and not spec_rows:
            intro.append(node.extract())
        elif name == "table" and spec_strip and not spec_rows:
            for tr in node.find_all("tr"):
                cells = tr.find_all(["td", "th"])
                if len(cells) == 2 and tr.parent.name == "tbody":
                    spec_rows.append((cells[0].decode_contents(), cells[1].decode_contents()))
            node.extract()
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
            nav.append((sid, NAV_LABELS.get(sid) or short_label(el.get_text(" ", strip=True))))
        if section is None:
            if isinstance(el, NavigableString) and not el.strip():
                continue
            main.append(el.extract())
        else:
            section.append(el.extract())

    # Section links under each chapter, shown in the sidebar on wide screens.
    subs = {}
    for sec in main.find_all("section", recursive=False):
        subs[sec.get("id", "")] = [(h.get("id"), h.get_text(" ", strip=True))
                                   for h in sec.find_all("h3") if h.get("id")]

    body_html = str(main)
    for key, svg in placeholders.items():
        body_html = body_html.replace(key, svg)

    css = (TOOLS / "page.css").read_text(encoding="utf-8")
    js = (TOOLS / "page.js").read_text(encoding="utf-8")
    nav_html = ""
    for sid, label in nav:
        sub_html = "".join(f'<li><a href="#{hid}">{text}</a></li>' for hid, text in subs.get(sid, []))
        sub_html = f'<ol class="sub">{sub_html}</ol>' if sub_html else ""
        nav_html += f'<li><a href="#{sid}">{label}</a>{sub_html}</li>'
    intro_html = "".join(f'<p class="lede">{p.decode_contents()}</p>' for p in intro)
    spec_html = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in spec_rows)
    spec_block = f'<dl class="spec">{spec_html}</dl>' if spec_html else ""
    site_nav_html = ""
    if site_nav:
        links = ""
        for label, href, current in site_nav:
            cur = ' aria-current="page"' if current else ""
            links += f'<li><a href="{href}"{cur}>{label}</a></li>'
        site_nav_html = f'<nav class="sitenav" aria-label="Site"><ul>{links}</ul></nav>'
    meta = '<meta name="claude:viewport-fit-sides" content="cover">\n' if artifact_meta else ""

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
<nav class="chapters" aria-label="Chapters"><ol>{nav_html}</ol></nav>
<main data-page="{page_key}"{' data-fill' if fill else ''}>{body_html}</main>
<footer class="colophon"><div class="wrap">
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


def build(standalone: bool, photo_mode: str = "inline") -> str:
    """The guide page, as used for the Artifact and the local guide.html."""
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
