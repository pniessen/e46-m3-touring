"""Compare the canonical file's copied sections with the manual's text, paragraph by paragraph."""
import pathlib, re, sys
CAN = pathlib.Path("/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/foldin/wiring-canonical.md").read_text()
MAN = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/WIRING-AND-CODING.md").read_text()

def norm_lines(s):
    out = []
    for l in s.splitlines():
        l = l.strip()
        if not l or l.startswith("<!-- figure"):
            continue
        l = re.sub(r"^#+\s*", "", l)
        out.append(l)
    return out

def can_section(n):
    m = re.search(rf"^## {n}\. .*?$(.*?)(?=^## \d+\. |\Z)", CAN, re.S | re.M)
    return m.group(1)

man_lines = set(norm_lines(MAN))
for n in (1, 7, 8, 9):
    lines = norm_lines(can_section(n))
    missing = [l for l in lines if l not in man_lines]
    print(f"§{n}: {len(lines)} lines, {len(missing)} not found verbatim in the manual")
    for l in missing:
        print("   ", l[:200])
