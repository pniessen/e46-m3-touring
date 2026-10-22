"""Check that identifiers, fault codes, connectors, part numbers and quoted names in the SVGs appear in the
manual or the canonical file."""
import html, pathlib, re, sys
MAN = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/WIRING-AND-CODING.md").read_text()
CAN = pathlib.Path("/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/foldin/wiring-canonical.md").read_text()
SRC = MAN + "\n" + CAN
def svg_text(p):
    s = pathlib.Path(p).read_text()
    lines = [html.unescape(re.sub(r"<[^>]+>", "", m)) for m in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]
    aria = html.unescape(re.search(r'aria-label="([^"]*)"', s).group(1))
    return " ".join(lines).replace(" ", " "), aria
pats = {
    "ident": r"\b[A-Z][A-Z0-9]*(?:_[A-Z0-9]+)+\b|\b[A-Z0-9]+\.PRG\b",
    "fault": r"\b\d+(?:[–-]\d+)? \(0x[0-9A-F]{2}(?:[–-]0x[0-9A-F]{2})?(?:, 0x[0-9A-F]{2}(?:[–-]0x[0-9A-F]{2})?)*\)",
    "hex": r"0x[0-9A-F]{2}",
    "conn": r"\bX\d{4,6}\b|\bK\d{2,4}\b|\bF\d{1,3}\b",
    "part": r"\b\d{11}\b",
    "quoted": r'"[^"]{3,60}"',
}
bad = 0
for p in sys.argv[1:]:
    text, aria = svg_text(p)
    missing = []
    for kind, rx in pats.items():
        for tok in sorted(set(re.findall(rx, text + " " + aria))):
            t = tok.strip('"') if kind == "quoted" else tok
            if t not in SRC:
                missing.append((kind, tok))
    print(f"{pathlib.Path(p).name}: {len(missing)} token(s) not found verbatim")
    for k, t in missing:
        print(f"   {k:7s} {t}")
    bad += len(missing)
