"""Print the text lines of an SVG (one <text> per line), joining tspans, for proofreading."""
import re, sys, html
for path in sys.argv[1:]:
    s = open(path, encoding="utf-8").read()
    print("=" * 10, path.split("/")[-1], re.search(r'viewBox="([^"]+)"', s).group(1))
    for m in re.finditer(r"<text[^>]*>(.*?)</text>", s, re.S):
        t = re.sub(r"<[^>]+>", "", m.group(1))
        print("  " + html.unescape(t).replace(" ", " "))
