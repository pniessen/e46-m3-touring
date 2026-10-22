"""Check every internal link in a built site: the target page exists and holds the anchor."""
import re, sys, pathlib, html as H
site = pathlib.Path(sys.argv[1])
pages = {p.name: re.sub(r"<script>.*?</script>", "", p.read_text(encoding="utf-8"), flags=re.S) for p in site.glob("*.html")}
ids = {n: set(re.findall(r'\sid="([^"]+)"', t)) for n, t in pages.items()}
bad, total, cross = [], 0, 0
for n, t in pages.items():
    for href in re.findall(r'\shref="([^"]+)"', t):
        href = H.unescape(href)
        if re.match(r'^(https?:|mailto:|data:)', href) or href.startswith("//"):
            continue
        if href.startswith(("diagrams/", "photos/", "favicon", "og-image")):
            if not (site / href.split("#")[0]).exists(): bad.append((n, href, "missing file"))
            continue
        total += 1
        path, _, frag = href.partition("#")
        target = n if path == "" else ("index.html" if path in ("./", "index.html") else path)
        if target != n: cross += 1
        if target not in pages:
            bad.append((n, href, "no such page")); continue
        if frag and frag not in ids[target]:
            bad.append((n, href, "no such anchor"))
print(f"{total} internal links ({cross} to another page); {len(bad)} broken")
for b in bad[:25]: print("  ", b)
dups = {n: [i for i in set(re.findall(r'\sid="([^"]+)"', t)) if len(re.findall(r'\sid="' + re.escape(i) + '"', t)) > 1] for n, t in pages.items()}
print("duplicate ids:", {n: d[:5] for n, d in dups.items() if d})
