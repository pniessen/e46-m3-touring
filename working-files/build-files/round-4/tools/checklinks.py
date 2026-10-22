"""Check internal links, ids and dollar escapes across the guide's Markdown pages."""
import pathlib, re, subprocess, sys
from collections import Counter
from bs4 import BeautifulSoup
root = pathlib.Path(sys.argv[1])
pages = [p for p in ["README.md", "WIRING-AND-CODING.md", "JOB-CARDS.md", "WORKSHEETS.md", "CALCULATORS.md", "research.md"] if (root / p).exists()]
ids, links, problems = {}, [], []
for p in pages:
    md = (root / p).read_text(encoding="utf-8")
    # Unescaped $ (not preceded by backslash) outside code.
    for i, line in enumerate(md.splitlines(), 1):
        if re.search(r"(?<!\\)\$", re.sub(r"`[^`]*`", "", line)):
            problems.append(f"{p}:{i}: unescaped $")
    html = subprocess.run(["pandoc", "-f", "gfm-tex_math_dollars", "-t", "html", "--wrap=none"],
                          input=md.replace("\\$", "$"), capture_output=True, text=True, check=True).stdout
    if "\\$" in html:
        problems.append(f"{p}: literal \\$ in HTML x{html.count(chr(92) + '$')}")
    soup = BeautifulSoup(html, "html.parser")
    pid = [t["id"] for t in soup.find_all(id=True)]
    dup = [k for k, v in Counter(pid).items() if v > 1]
    if dup:
        problems.append(f"{p}: duplicate ids {dup}")
    ids[p] = set(pid)
    for a in soup.find_all("a", href=True):
        links.append((p, a["href"]))
for p, href in links:
    if href.startswith(("http://", "https://", "mailto:")):
        continue
    path, _, frag = href.partition("#")
    target = p if path == "" else path
    if target not in ids:
        if not (root / target).exists():
            problems.append(f"{p}: link to missing file {href}")
        continue
    if frag and frag not in ids[target]:
        problems.append(f"{p}: bad anchor {href}")
print("\n".join(problems) if problems else "all links, ids and dollar signs OK")
print(len(links), "links checked across", pages)
