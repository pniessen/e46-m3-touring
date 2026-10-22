#!/usr/bin/env python3
"""Swap the captions of redrawn figures in the joined guide pages, and drop placeholders that were merged or cut.

usage: python3 apply_redraws.py GUIDE_DIR CAPTION_DIR
A caption file redraw-NN-name.caption.md holds: image line, blank line, "*Figure N. ...*", then "\n---\n" and notes.
The existing block for diagrams/NN-name.svg (image line + blank + "*Figure K. ...*") is replaced by the new block,
keeping K, so figures.py can still remap text references when it renumbers. A file whose block has no
"*Figure" line (caption unchanged) is skipped.
"""
import pathlib, re, sys

root, capdir = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2])
DROP = ["proposed-arch-section-axle", "proposed-booster-vacuum", "proposed-ncs-error-triage", "proposed-xenon-path"]
pages = {p: (root / p).read_text(encoding="utf-8") for p in ("README.md", "WIRING-AND-CODING.md")}
for cap in sorted(capdir.glob("redraw-*.caption.md")):
    block = cap.read_text(encoding="utf-8").split("\n---\n")[0].strip("\n")
    m = re.match(r"!\[[^\]]*\]\((diagrams/[^)]+\.svg)\)[^\n]*\n\n\*Figure N\. .+\*$", block, re.S)
    if not m:
        print(f"{cap.name}: no new caption block, skipped")
        continue
    svg = m.group(1)
    hits = 0
    for name, text in pages.items():
        pat = re.compile(r"!\[[^\]]*\]\(" + re.escape(svg) + r"\)[^\n]*\n\n\*Figure (\d+)\. [^\n]*\*")
        found = pat.findall(text)
        if not found:
            continue
        if len(found) > 1:
            sys.exit(f"{cap.name}: {svg} appears {len(found)} times in {name}")
        num = found[0]
        new = block.replace("*Figure N. ", f"*Figure {num}. ", 1)
        pages[name] = pat.sub(lambda _: new, text, count=1)
        hits += 1
        print(f"{cap.name}: replaced Figure {num} in {name}")
    if not hits:
        print(f"{cap.name}: WARNING {svg} not found in any page")
for name, text in pages.items():
    for ph in DROP:
        tag = f"<!-- figure: {ph} -->"
        if tag in text:
            text = re.sub(r"\n*" + re.escape(tag) + r"\n*", "\n\n", text)
            print(f"{name}: dropped placeholder {ph}")
    pages[name] = text
    (root / name).write_text(text, encoding="utf-8")
