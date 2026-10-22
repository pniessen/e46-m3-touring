#!/usr/bin/env python3
"""Figure 11 (README "Fuel-pump control"): 11-fuel-pump-control.svg, a round-4 tweak of the published figure.

Two changes, both from WIRING-AND-CODING 0360-0390 and README 0540/0580:
  1. A new row under the relay drawing: the test bypass, K96 pulled, a switch with a 15 A inline fuse across
     socket pins 6 (F54 supply) and 2 (out to the pump), for the fuel tests.
  2. The stored-fault box no longer says pin 11 "stores" the fault: "Expect a stored fault ... US software misses
     the pump module it expects; BMW's files don't say exactly what sets it."
Everything else is the published figure, kept verbatim (orig/11-fuel-pump-control.svg); the new row goes under
"Prove pin 10", and the parts below it move down. The new row's pin cells are outlines ("ln"), which look the same as the figure's white "shape"
cells on the plain background.

    python3 gen11.py        (exit 3 = new strings were measured: run it again)
"""
import re
import sys

from kit import Doc, width, flush_measurements, fmt, HERE, DIAGRAMS

NAME = "11-fuel-pump-control.svg"
SRC = (HERE / "orig" / NAME).read_text(encoding="utf-8")
H0 = 816
D1 = 94      # the bypass row
D2 = 12      # one more line in the stored-fault box


def shift(fragment: str, dy: float) -> str:
    """Move every element in an SVG fragment down by dy (y, y1, y2, cy and absolute path coordinates)."""
    def attr(m):
        return f'{m.group(1)}="{fmt(float(m.group(2)) + dy)}"'
    out = re.sub(r'\b(y|y1|y2|cy)="([-\d.]+)"', attr, fragment)

    def path_d(m):
        toks = re.findall(r'[MLHVZmlhvz]|[-\d.]+', m.group(1))
        res, cmd, i, nums = [], None, 0, []
        for t in toks:
            if t.isalpha():
                cmd = t
                res.append(t)
                nums = []
                continue
            nums.append(t)
            if cmd in "ML":
                if len(nums) == 2:
                    res.append(f"{nums[0]},{fmt(float(nums[1]) + dy)}")
                    nums = []
            elif cmd == "V":
                res.append(fmt(float(t) + dy))
                nums = []
            elif cmd in "ml":
                if len(nums) == 2:
                    res.append(f"{nums[0]},{nums[1]}")
                    nums = []
            else:          # H, h, v: no change
                res.append(t)
                nums = []
        s = ""
        for r in res:
            s += (r if r.isalpha() else (" " if s and not s[-1].isalpha() else "") + r)
        return f'd="{s}"'
    return re.sub(r'd="([^"]*)"', path_d, out)


# ---------------------------------------------------------------- split the published figure
i_prove = SRC.index("<!-- How to prove pin 10 -->")
i_fault = SRC.index("<!-- The stored fault -->")
i_never = SRC.index("<!-- Never -->")
i_end = SRC.rindex("</svg>")
head, prove, fault, rest = SRC[:i_prove], SRC[i_prove:i_fault], SRC[i_fault:i_never], SRC[i_never:i_end]

# ---------------------------------------------------------------- the new bypass row
d = Doc()
d.comment("Test bypass for the fuel tests, K96 pulled (WIRING-AND-CODING checks on the pump circuit, check 4)")
Y0 = 342                     # heading baseline of the new row
Y = Y0 + 24
d.text("t-sm t-b", 8, Y0, "Fuel tests: the bypass")
for i, s in enumerate(["Pull K96 and fit a switch with a", "15 A inline fuse across socket",
                       "pins 6 and 2. Check the pins on", "WDS for your VIN."]):
    d.text("t-xs", 8, Y0 + 16 + i * 12.5, s)
d.text("t-xs", 190, Y + 4, "F54")
d.line("ln", 211, Y, 223, Y, end="ah")
PX6, PX2 = 234, 336
for px, pn in ((PX6, "6"), (PX2, "2")):
    d.rect("ln", px - 10, Y - 9, 20, 18, rx=2, sw=1.2)
    d.text("t t-mono", px, Y + 4.5, pn, anchor="middle")
d.line("ln", PX6 + 10, Y, 254, Y)
d.rect("shape", 254, Y - 5, 26, 10, rx=1.5, sw=1.2)            # fuse
d.line("ln", 254, Y, 280, Y, sw=1)
d.line("ln", 280, Y, 292, Y)
d.dot("fill-fg", 292, Y, 2.4)                                   # switch
d.line("ln", 292, Y, 312, Y - 10, sw=1.5)
d.dot("fill-fg", 314, Y, 2.4)
d.line("ln", 314, Y, PX2 - 10, Y)
d.line("ln", PX2 + 10, Y, PX2 + 23, Y, end="ah")
d.text("t-xs", PX2 + 28, Y + 4, "pump")
d.text("t-xs", 267, Y + 22, "15 A fuse", anchor="middle")
# README 0540 "How to run the pump": leave pin 8 alone, WDS calls it "Terminal 87" but it's the coil supply from F3
d.rich("t-xs", 8, Y0 + 66, [("t-b", "Not pin 8:"), (None, " WDS's \"Terminal 87\" is the coil supply.")])
bypass = d.body() + "\n\n"

# ---------------------------------------------------------------- the stored-fault box, softened
f = Doc()
f.comment("The stored fault")
y0 = 330 + D1
f.rect("warn-f", 8, y0, 384, 78 + D2, rx=5, sw=1.5)
f.rich("t-sm t-b", 18, y0 + 17, [(None, "Expect a stored fault: "), ("t-mono", "1 (0x01)")])
rows = [
    [(None, "\"Relais Kraftstoffpumpe\": US software misses the pump module it")],
    [(None, "expects; BMW's files don't say exactly what sets it. It shows in INPA")],
    [(None, "(as 1), ISTA and PA-Soft, not on a generic scanner, and doesn't light")],
    [(None, "the check-engine lamp. Not "), ("t-mono", "130 (0x82)"), (None, ", the immobilizer fault. Don't")],
    [(None, "flash Euro software to clear it: that drops the DM-TL leak test.")],
]
for i, r in enumerate(rows):
    f.rich("t-xs", 18, y0 + 32 + i * 12.5, r)
fault_new = f.body() + "\n\n"

# ---------------------------------------------------------------- the root: height and aria-label
H = H0 + D1 + D2
head = head.replace(f'viewBox="0 0 400 {H0}"', f'viewBox="0 0 400 {fmt(H)}"')
head = head.replace(f'width="400" height="{H0}" fill="#ffffff"', f'width="400" height="{fmt(H)}" fill="#ffffff"')
old_crash = "Whether US software drops the pin-10 output after a crash isn't documented. "
new_crash = (old_crash + "For the fuel tests, pull K96 and bridge its socket's pins 6 (the F54 supply) and 2 (out to "
             "the pump) through a switch with a 15 A inline fuse, but not pin 8: WDS calls it Terminal 87, but it's "
             "the coil supply. Check the pins on WDS for your VIN. ")
old_fault = ("Expect stored fault location 1 (0x01), Relais Kraftstoffpumpe, which INPA shows as 1; it shows in INPA, "
             "ISTA and PA-Soft but not on a generic scanner, and doesn't light the check-engine lamp; it is not 130 "
             "(0x82), the immobilizer fault; don't flash Euro software to clear it.")
new_fault = ("Expect a stored fault, location 1 (0x01), Relais Kraftstoffpumpe, because US software misses the pump "
             "module it expects; BMW's files don't say exactly what sets it. INPA shows it as 1; it shows in INPA, "
             "ISTA and PA-Soft but not on a generic scanner, and doesn't light the check-engine lamp; it is not 130 "
             "(0x82), the immobilizer fault; don't flash Euro software to clear it.")
for a, b in ((old_crash, new_crash), (old_fault, new_fault)):
    assert a in head, a[:50]
    head = head.replace(a, b)

out = head + prove + bypass + fault_new + shift(rest, D1 + D2) + "</svg>\n"
(DIAGRAMS / NAME).write_text(out, encoding="utf-8")
if flush_measurements():
    print("measured new strings: run again")
    sys.exit(3)
print("wrote", DIAGRAMS / NAME)
