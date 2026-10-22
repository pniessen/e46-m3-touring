"""Show what changed between two SVGs: visible text lines (as rendered strings) and the aria-label, word-diffed.
usage: python3 -I textdiff.py OLD.svg NEW.svg"""
import difflib, html, re, sys
def parts(p):
    s = open(p, encoding="utf-8").read()
    aria = html.unescape(re.search(r'aria-label="([^"]*)"', s).group(1))
    lines = [html.unescape(re.sub(r"<[^>]+>", "", m)) for m in re.findall(r"<text[^>]*>(.*?)</text>", s)]
    vb = re.search(r'viewBox="([^"]+)"', s).group(1)
    return aria, lines, vb
a0, l0, v0 = parts(sys.argv[1]); a1, l1, v1 = parts(sys.argv[2])
print("viewBox:", v0, "->", v1)
t0, t1 = " ".join(l0).split(), " ".join(l1).split()
def wd(x, y, name):
    sm = difflib.SequenceMatcher(None, x, y, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op != "equal":
            print(f"  {name} {op}: [{' '.join(x[i1:i2])}] -> [{' '.join(y[j1:j2])}]")
print("visible text changes:"); wd(t0, t1, "text")
print("aria changes:"); wd(a0.split(), a1.split(), "aria")
