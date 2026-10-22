"""Swap figure placeholders for their diagram blocks, then number each page's figures in order.

usage: python3 figures.py GUIDE_DIR [CAPTION_DIR ...]
Caption files: scratchpad/foldin/diagrams/NAME.caption.md = image line, blank, "*Figure N. ...*", then
"---" and notes. A placeholder <!-- figure: NAME --> in README.md or WIRING-AND-CODING.md is replaced by
the block. Figures are numbered per page; text references like "Figure 6" follow their figure.
"""
import pathlib, re, sys
root = pathlib.Path(sys.argv[1])
capdirs = [pathlib.Path(p) for p in sys.argv[2:]] or [pathlib.Path("/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/foldin/diagrams")]
blocks = {cap.name[: -len(".caption.md")]: cap.read_text(encoding="utf-8").split("\n---\n")[0].strip("\n")
          for capdir in capdirs for cap in capdir.glob("*.caption.md")}
pat = re.compile(r"(!\[[^\]]*\]\((diagrams/[^)]+\.svg)\)[^\n]*\n\n\*Figure )(\d+|N)(\.)")

for page in ("README.md", "WIRING-AND-CODING.md"):
    f = root / page
    if not f.exists():
        continue
    s = f.read_text(encoding="utf-8")
    for name, block in blocks.items():
        ph = f"<!-- figure: {name} -->"
        if ph in s:
            s = s.replace(ph, block)
            print(page, "inserted", name)
    found = list(pat.finditer(s))
    old_to_new = {m.group(3): str(i) for i, m in enumerate(found, 1) if m.group(3) != "N"}
    counter = iter(range(1, len(found) + 1))
    s = pat.sub(lambda m: f"{m.group(1)}{next(counter)}{m.group(4)}", s)
    lines = s.split("\n")
    for i, line in enumerate(lines):
        if line.startswith("*Figure "):
            head, sep, rest = line.partition(". ")
            rest = re.sub(r"\bFigures? (\d+)\b", lambda m: m.group(0).replace(m.group(1), "@@" + old_to_new.get(m.group(1), m.group(1))), rest)
            lines[i] = head + sep + rest
        else:
            lines[i] = re.sub(r"\bFigure (\d+)\b", lambda m: "Figure @@" + old_to_new.get(m.group(1), m.group(1)), line)
    s = "\n".join(lines).replace("@@", "")
    f.write_text(s, encoding="utf-8")
    left = re.findall(r"<!-- figure: [^>]+ -->", s)
    print(page, "numbered", len(found), "figures; renumbered", {k: v for k, v in old_to_new.items() if k != v}, "placeholders left:", left)
