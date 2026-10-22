"""Figure 37: the fan layout, your manual Touring as built and the swapped car (portrait, 400 wide).

Data: README 0550 "Fans: what changes on a manual Touring" and its parts table, README 0200 rows,
README 0410 Phase 10, WIRING-AND-CODING 0190 "Fans and CAN", cooling_ac.md D2.
Run: python3 gen37.py (twice if it measured new text).
"""
from coolkit import Doc, svg_open, write, flush, report

D = Doc()
T = "t-xs"
XL = 216          # label column
XC = 120          # centre of the stack


def key():
    D.comment("Key")
    x = 8
    for cls, label in (("keep", "Keep"), ("donor", "From donor M3"), ("fab", "Extend or re-route"),
                       ("shape", "Comes out")):
        D.rect(cls, x, 6, 12, 12, rx=2, sw=1)
        w = D.text("t-sm", x + 17, 16.5, label)
        x += 17 + w + 14


def leader(x1, y, x2=XL - 6):
    D.line("ln-thin", x1, y, x2, y)


def stack(Q, after):
    """The cooling pack seen from above, front at the top; labels to the right. Q = top of row 1."""
    part = "donor" if after else "shape"
    # r1: pusher fan in front of the condenser
    if after:
        D.comment("Pusher fan 64546988914 in front of the condenser (donor)")
        D.rect("donor", 60, Q, 120, 16, rx=4, sw=1.5)
        D.circle("donor", XC, Q + 8, 4, sw=1.2)
        leader(181, Q + 8)
        D.rich("t-sm t-b", XL, Q + 6, [(None, "Pusher fan "), ("t-mono", "64546988914")], maxw=172)
        D.text(T, XL, Q + 19, "its power stage is on the fan", maxw=172)
    else:
        D.comment("Pusher fan: almost certainly none on a manual Touring")
        D.rect("ln-thin dash", 60, Q, 120, 18, rx=4)
        D.text("t-sm t-b", XC, Q + 13, "?", anchor="middle")
        leader(181, Q + 9)
        D.text("t-sm t-b", XL, Q + 6, "A pusher fan here too?", maxw=172)
        D.text(T, XL, Q + 19, "Almost certainly not: see below", maxw=172)
    # r2: condenser (keep)
    D.comment("Condenser (keep, same part)")
    D.rect("keep", 50, Q + 40, 140, 10, rx=2, sw=1.5)
    leader(191, Q + 45)
    D.text("t-sm t-b", XL, Q + 44, "Condenser", maxw=172)
    D.text(T, XL, Q + 57, "the same part on both cars", maxw=172)
    # r3: radiator
    D.comment("Radiator")
    D.rect(part, 46, Q + 70, 148, 18, rx=2, sw=1.5)
    leader(195, Q + 79)
    if after:
        D.rich("t-sm t-b", XL, Q + 83, [(None, "M3 radiator "), ("t-mono", "17102228941")], maxw=172)
    else:
        D.rich("t-sm t-b", XL, Q + 83, [(None, "Your radiator "), ("t-mono", "17119071518")], maxw=172)
    # r4: shroud and its fan
    D.comment("Shroud and its fan")
    D.path(part, f"M46,{Q + 90} H194 L158,{Q + 118} H82 Z", sw=1.5)
    D.rect(part, 86, Q + 109, 68, 6, rx=1, sw=1.2)
    leader(176, Q + 104)
    if after:
        D.rich("t-sm t-b", XL, Q + 107, [(None, "M3 shroud "), ("t-mono", "17112228943")], maxw=172)
        D.rich(T, XL, Q + 120, [(None, "with the viscous fan "), ("t-mono", "11521712058")], maxw=172)
    else:
        D.text("t-sm t-b", XL, Q + 107, "390 W electric fan", maxw=172)
        D.rich(T, XL, Q + 120, [("t-mono", "17117561757"), (None, ", in the radiator")], maxw=172)
        D.text(T, XL, Q + 132.5, "shroud; its power stage and plug", maxw=172)
        D.text(T, XL, Q + 145, "X82 sit on the shroud", maxw=172)
    # r5: the fan's drive, and the engine
    if after:
        D.comment("Viscous coupling 11527831619 on the S54's water pump (donor)")
        D.rect("donor", 111, Q + 115, 18, 15, rx=2, sw=1.5)
        D.rect("donor", 84, Q + 130, 72, 46, rx=4, sw=1.5)
        D.text("t-sm t-b", XC, Q + 157, "S54", anchor="middle")
        D.path("ln-thin", f"M130,{Q + 124} H198 L{XL - 6},{Q + 137}")
        D.rich("t-sm t-b", XL, Q + 141, [(None, "Coupling "), ("t-mono", "11527831619")], maxw=172)
        D.lines(T, XL, Q + 154, ["on the water pump, rated on at",
                                 "92 °C and off at 60 °C; no wiring.",
                                 "Left-hand thread, 40 Nm"], 12.5, maxw=172)
    else:
        D.comment("Electric fan motor on the shroud; M54 engine with no viscous fan")
        D.rect("shape", 111, Q + 115, 18, 12, rx=2, sw=1.5)
        D.rect("shape", 84, Q + 140, 72, 36, rx=4, sw=1.5)
        D.text("t-sm t-b", XC, Q + 162, "M54", anchor="middle")
        leader(157, Q + 158)
        D.text("t-sm t-b", XL, Q + 162, "No viscous fan", maxw=172)
        D.text(T, XL, Q + 175, "ETK lists it for automatics only", maxw=172)


def wiring(Q, after):
    """X82 and its three wires: the same pins on both cars. Returns the y below the block."""
    y0 = Q + 200
    D.comment("X82 and its wires: no pin moves")
    shroud_y = Q + 104
    if after:
        # X82 now on the pusher fan; the lead from the harness's old end is extended or re-routed
        D.rect("shape", 22, Q + 1, 18, 14, rx=2, sw=1.5)
        D.text(T + " t-b t-mono", 31, Q - 4, "X82", anchor="middle")
        D.line("ln", 40, Q + 8, 59, Q + 8)
        D.line("fab-s", 31, Q + 16, 31, shroud_y, sw=3)
        D.line("keep-s", 31, shroud_y, 31, y0 + 52, sw=3)
    else:
        D.rect("shape", 22, shroud_y - 7, 18, 14, rx=2, sw=1.5)
        D.text(T + " t-b t-mono", 31, shroud_y - 12, "X82", anchor="middle")
        D.line("ln", 40, shroud_y, 63, shroud_y)
        D.line("keep-s", 31, shroud_y + 8, 31, y0 + 52, sw=3)
    for i, (pin, wire) in enumerate((("2", "0.5 SW/GN"), ("4", "6.0 RT/BL"), ("1", "6.0 BR"))):
        y = y0 + i * 26
        D.line("ln", 31, y, 214 if i < 2 else 196, y)
        D.rich(T, 42, y - 5, [(None, "pin "), ("t-mono t-b", pin), (None, " · "), ("t-mono", wire)], maxw=150)
    D.rect("donor" if after else "shape", 214, y0 - 11, 176, 22, rx=4, sw=1.5)
    D.rich("t-sm", 222, y0 + 4, [("t-b", "M3 DME" if after else "Your DME"), (None, ", "),
                                 ("t-mono", "X60004"), (None, " pin "), ("t-mono", "4")], maxw=162)
    D.rect("keep", 214, y0 + 15, 176, 22, rx=4, sw=1.5)
    D.rich("t-sm", 222, y0 + 30, [("t-b t-mono", "F37"), (None, ", 50 A feed")], maxw=162)
    D.ground(196, y0 + 52)
    D.text("t-sm", 214, y0 + 56, "ground", maxw=162)
    return y0 + 72


key()
# ---------------------------------------------------------------- panel 1
P1 = 28
H1 = 408
D.comment("Panel 1: your manual Touring as built")
D.rect("panel", 6, P1, 388, H1, rx=8, sw=1)
D.text("t-h", 16, P1 + 22, "YOUR TOURING AS BUILT (MANUAL)")
D.text(T, 16, P1 + 37, "Seen from above, front at the top")
stack(P1 + 58, after=False)
y = wiring(P1 + 58, after=False)
D.comment("The pusher fan on a manual Touring: almost certainly none")
D.rect("warn-f", 14, y + 4, 372, 66, rx=5, sw=1.5)
D.text("t-sm t-b", 24, y + 21, "A manual Touring almost certainly has no pusher fan:", maxw=356)
D.lines(T, 24, y + 36, ["ETK lists one (64546988913) with no gearbox note, but the DME has only",
                        "one fan output and owners call it the automatic's part. Check your car",
                        "in Phase 0."], 12.5, maxw=356)
assert y + 70 <= P1 + H1 - 6, y

# ---------------------------------------------------------------- panel 2
P2 = P1 + H1 + 10
H2 = 448
D.comment("Panel 2: after the swap")
D.rect("panel", 6, P2, 388, H2, rx=8, sw=1)
D.text("t-h", 16, P2 + 22, "AFTER THE SWAP")
D.text(T, 16, P2 + 37, "Fit both M3 fans, as BMW did")
stack(P2 + 58, after=True)
y = wiring(P2 + 58, after=True)
D.lines(T, 16, y + 8, ["No pin moves. The orange lead: extend or re-route X82 only if it doesn't",
                       "reach the pusher (one manual-Touring swap plugged straight in), keeping",
                       "the pins; extend pins 1 and 4 in 6.0 mm², pin 2 in 0.5 mm²."],
        12.5, maxw=368)
D.rect("warn-f", 14, y + 44, 372, 66, rx=5, sw=1.5)
D.text("t-sm t-b", 24, y + 61, "Compare the plugs before you cut anything", maxw=356)
D.lines(T, 24, y + 76, ["WDS calls X82 a 4-pin plug with pins 1, 2 and 4 used. ETK lists a",
                        "3-pole housing (61138380380, terminal 61138380385) for both cars'",
                        "pusher fans, and no plug for the shroud fan."], 12.5, maxw=356)
assert y + 110 <= P2 + H2 - 6, y

H = P2 + H2 + 6
ARIA = ("The electric fan before and after the swap, seen from above with the front at the top. Your "
        "manual 325i Touring as built has no viscous fan, since ETK lists it for automatics only; its fan is a "
        "390 W electric fan, 17117561757, inside the radiator shroud, with its power stage and plug X82 on the "
        "shroud. A manual Touring almost certainly has no pusher fan in front of the condenser: ETK lists one, "
        "64546988913, with no gearbox note, but the DME has only one fan output and owners call it the "
        "automatic's part; check your car in Phase 0. After the swap the car has "
        "both M3 fans: the electric pusher fan 64546988914 in front of the condenser, with its power stage on "
        "the fan, and the viscous fan 11521712058 in the M3 shroud on coupling 11527831619 on the water pump, "
        "rated on at 92 °C and off at 60 °C, with no wiring and a left-hand thread at 40 Nm. The condenser is "
        "the same part on both cars. In both cars the DME drives the fan from X60004 pin 4 over the 0.5 SW/GN "
        "wire to X82 pin 2, F37 (50 A) feeds pin 4 over 6.0 RT/BL, and pin 1 is ground over 6.0 BR, so no pin "
        "moves; X82's lead is extended or re-routed only if it doesn't reach the pusher fan (one manual-Touring "
        "swap plugged straight in), keeping the pins, with pins 1 and 4 in 6.0 square millimetres and pin 2 in "
        "0.5. Compare the plugs first: WDS calls X82 a 4-pin plug with pins 1, 2 and 4 "
        "used, while ETK lists a 3-pole housing, 61138380380, for both cars' pusher fans.")
p = write("37-fan-layout.svg", svg_open(H, ARIA), D.body())
print("wrote", p)
report()
if flush():
    print("measured new strings: run again")
