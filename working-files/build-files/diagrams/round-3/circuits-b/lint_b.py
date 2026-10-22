#!/usr/bin/env python3
"""Static checks for the house rules.  python3 lint_b.py a.svg [b.svg ...]"""
import re
import sys
import xml.etree.ElementTree as ET

sys.dont_write_bytecode = True
from ckit import STYLE  # verbatim style block from 04-fuel-pressure.svg

ALLOWED = set("""t t-sm t-xs t-b t-h t-mono ln ln-thin ln-faint dash fill-fg fill-bg shape panel donor new fab keep
donor-s new-s fab-s keep-s crit-s donor-t new-t fab-t crit-t donor-f new-f fab-f crit-f keep-f warn-f bg""".split())
NS = "{http://www.w3.org/2000/svg}"

for f in sys.argv[1:]:
    src = open(f, encoding="utf-8").read()
    probs = []
    root = ET.fromstring(src)
    vb = [float(v) for v in root.get("viewBox").split()]
    landscape = vb[2] > 400
    if root.get("role") != "img":
        probs.append("root role is not img")
    if root.get("color") != "#1b2128":
        probs.append("root color attribute missing")
    al = root.get("aria-label") or ""
    if len(al) < 40 or not al.rstrip().endswith("."):
        probs.append("aria-label missing or not a full sentence")
    m = re.search(r"<style>.*?</style>", src, re.S)
    if not m or m.group(0) != STYLE:
        probs.append("style block differs from 04-fuel-pressure.svg")
    if not re.search(r'<rect class="bg" x="0" y="0" width="%g" height="%g" fill="#ffffff"/>' % (vb[2], vb[3]), src):
        probs.append("bg rect missing or wrong size")
    for el in root.iter():
        tag = el.tag.replace(NS, "")
        cls = (el.get("class") or "").split()
        for c in cls:
            if c not in ALLOWED:
                probs.append(f"unknown class {c!r} on <{tag}>")
        if "bg" in cls:
            continue
        for a in ("fill", "stroke", "style"):
            if el.get(a) is not None:
                probs.append(f"hard-coded {a}={el.get(a)!r} on <{tag} class={' '.join(cls)!r}>")
        if tag == "text" and landscape and "t-xs" in cls:
            probs.append(f"t-xs text in a landscape figure: {''.join(el.itertext())!r}")
        if tag == "text" and not ({"t", "t-sm", "t-xs", "t-h"} & set(cls)):
            probs.append(f"text without a size class: {''.join(el.itertext())!r}")
    print(f"== {f}: viewBox {vb[2]:g}x{vb[3]:g}, {'landscape' if landscape else 'portrait'}, {len(probs)} problem(s)")
    for p in probs:
        print("   " + p)
