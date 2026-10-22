"""Reverse check: every line of the manual's sections should appear in the canonical file."""
import pathlib, re
CAN = pathlib.Path("/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/foldin/wiring-canonical.md").read_text()
MAN = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/WIRING-AND-CODING.md").read_text()
def norm(s):
    out = []
    for l in s.splitlines():
        l = l.strip()
        if not l or l.startswith("<!-- figure"): continue
        out.append(re.sub(r"^#+\s*", "", l))
    return out
can = set(norm(CAN))
def man_span(start_heading, end_heading):
    a = MAN.index(start_heading); b = MAN.index(end_heading, a + 1)
    return MAN[a:b]
spans = {
  "§1 Which DME": ("### Which DME your Touring has", "### The five DME plugs"),
  "§7 Power-up": ("## Checks before first power-up", "## Coding step by step"),
  "§8 Troubleshooting/Won't start": ("## Troubleshooting", "### Warning lights"),
  "§9 Warning lights": ("### Warning lights", "### DSC, ABS and steering angle"),
}
for name, (a, b) in spans.items():
    lines = norm(man_span(a, b))
    miss = [l for l in lines if l not in can]
    print(f"{name}: {len(lines)} lines, {len(miss)} missing from canonical")
    for l in miss: print("   ", l[:160])
