#!/usr/bin/env python3
"""Generate diagrams/11-fuel-pump-control.svg: relay K96 (recommended) vs the US M3's EKP module."""
import sys
sys.dont_write_bytecode = True
from svgkit import svg_open, t, write

out = []
add = out.append


def box(cls, x, y, w, h, sw="1.5"):
    add(f'<rect class="{cls}" x="{x}" y="{y}" width="{w}" height="{h}" rx="5" stroke-width="{sw}"/>')


def dme(y0):
    """M3 DME with its two pump outputs; returns the y of the pin-10 and pin-11 stubs."""
    box("donor", 8, y0, 116, 108)
    add(t("t t-b", 16, y0 + 19, "M3 DME"))
    add(t("t-sm", 16, y0 + 35, "MSS54 / HP"))
    add(t("t-sm t-b", 16, y0 + 58, "X60004 pin 10"))
    add(t("t-xs", 16, y0 + 71, '"not USA"'))
    add(t("t-sm t-b", 16, y0 + 88, "X60002 pin 11"))
    add(t("t-xs", 16, y0 + 101, '"USA only"'))
    p10, p11 = y0 + 54, y0 + 84
    add(f'<line class="ln" x1="98" y1="{p10}" x2="124" y2="{p10}"/>')
    add(f'<line class="ln" x1="98" y1="{p11}" x2="124" y2="{p11}"/>')
    return p10, p11


def pump(y0):
    box("keep", 334, y0, 58, 56)
    add(t("t t-b", 363, y0 + 24, "Pump", "middle"))
    add(t("t-xs", 363, y0 + 39, "in the tank", "middle"))


# Key
add("<!-- Key -->")
box("donor", 8, 6, 12, 12, "1")
add(t("t-sm", 25, 16.5, "From donor M3"))
box("keep", 130, 6, 12, 12, "1")
add(t("t-sm", 147, 16.5, "Keep"))

# ------------------------------------------------------------ recommended: the relay
add("\n<!-- Recommended: the MSS54's relay output drives your K96 -->")
add(t("t-h", 8, 44, "RECOMMENDED: KEEP THE RELAY"))
p10, p11 = dme(56)
add(t("t-xs", 142, 70, "Confirm in your VIN's diagrams that pin 10"))
add(t("t-xs", 142, 83, "reaches K96's coil wire, first on an MS45 car"))
box("keep", 214, 94, 96, 56)
add(t("t t-b", 262, 116, "Relay K96", "middle"))
add(t("t-xs", 262, 130, "behind the", "middle"))
add(t("t-xs", 262, 142, "glovebox", "middle"))
add(f'<line class="ln" x1="124" y1="{p10}" x2="213" y2="{p10}" marker-end="url(#ah)"/>')
add(t("t-xs", 166, p10 - 5, "SW/VI wire", "middle"))
add('<line class="ln" x1="310" y1="122" x2="333" y2="122" marker-end="url(#ah)"/>')
add(t("t-xs", 321.5, 113, "F54", "middle"))
pump(94)

add("\n<!-- Pin 11, the PWM output: connected to nothing, never to K96 -->")
add(f'<line class="ln" x1="124" y1="{p11}" x2="152" y2="{p11}"/>')
add(f'<circle class="shape" cx="156" cy="{p11}" r="3.5"/>')
add(f'<line class="crit-s dash" x1="160" y1="{p11}" x2="213" y2="{p11}" stroke-width="1.5"/>')
add(f'<path class="crit-s" d="M181,{p11 - 5} l10,10 M181,{p11 + 5} l10,-10" stroke-width="2"/>')
add(t("t-xs crit-t t-b", 186, p11 - 9, "never", "middle"))
add(f'<line class="ln-thin" x1="156" y1="{p11 + 3.5}" x2="156" y2="179"/>')

add("\n<!-- Where the stored fault comes from -->")
add('<rect class="warn-f" x="8" y="179" width="384" height="48" rx="5" stroke-width="1.5"/>')
add(t("t-sm t-b", 18, 196, "Pin 11 connected to nothing: expect a stored pump-module fault"))
add(t("t-xs", 18, 210, "It shows in INPA, ISTA and PA-Soft but doesn't light the check-engine"))
add(t("t-xs", 18, 222, "lamp. Don't flash Euro software to clear it: that drops the DM-TL leak test."))

add("\n<!-- Warning -->")
add('<rect class="crit-s" x="8" y="235" width="384" height="61" rx="5" stroke-width="1.5"/>')
add(t("t-sm t-b crit-t", 18, 252, "Never connect the PWM pump output to K96"))
add(t("t-xs", 18, 266, "A relay coil can't follow a 0–120 Hz signal and would likely chatter."))
add(t("t-xs", 18, 279, "The wire leaves the M3 harness in the black 4-pin E-box plug: if it"))
add(t("t-xs", 18, 291, "would reach K96, de-pin it and insulate it."))

add('\n<line class="ln-faint" x1="8" y1="310" x2="392" y2="310"/>')

# ------------------------------------------------------------ optional: the EKP module
add("\n<!-- Optional: the US M3's pump module, driven by pin 11 -->")
add(t("t-h", 8, 334, "OPTIONAL: THE M3 PUMP MODULE (EKP)"))
q10, q11 = dme(346)
add(f'<line class="ln" x1="124" y1="{q10}" x2="152" y2="{q10}"/>')
add(f'<circle class="shape" cx="156" cy="{q10}" r="3.5"/>')
add(t("t-xs", 164, q10 + 3.7, "not used"))
box("donor", 214, q11 - 28, 96, 56)
add(t("t t-b", 262, q11 - 8, "EKP module", "middle"))
add(t("t-xs", 262, q11 + 6, "slows the pump at", "middle"))
add(t("t-xs", 262, q11 + 18, "idle and part load", "middle"))
add(f'<line class="ln" x1="124" y1="{q11}" x2="213" y2="{q11}" marker-end="url(#ah)"/>')
add(t("t-xs", 164, q11 - 6, "0–120 Hz PWM", "middle"))
add(f'<line class="ln" x1="310" y1="{q11}" x2="333" y2="{q11}" marker-end="url(#ah)"/>')
pump(q11 - 28)

add("\n<!-- Crash cut-off -->")
box("keep", 8, 480, 116, 34)
add(t("t t-b", 66, 501.5, "Airbag unit", "middle"))
add('<line class="ln" x1="66" y1="479" x2="66" y2="455" marker-end="url(#ah)"/>')
add(t("t-xs", 73, 471, "crash signal"))
add(t("t-xs", 214, 487, "After a crash, the DME"))
add(t("t-xs", 214, 500, "cuts the module's power"))

add("\n<!-- When to fit it -->")
add(t("t-xs", 8, 535, "Fit it only if your state won't accept the stored fault, or you want the"))
add(t("t-xs", 8, 548, "slow-running pump and crash cut-off back. It needs five wires to the"))
add(t("t-xs", 8, 561, "relay's four, and nobody has documented it in a Touring."))

H = 571
ARIA = ("Fuel-pump control, two ways. Recommended: keep the relay. The M3 DME's X60004 pin 10 output, marked "
        "not USA, drives your relay K96 behind the glovebox through the SW/VI wire, and K96 switches the pump "
        "through fuse F54. The DME's PWM pump output, X60002 pin 11, marked USA only, is connected to nothing, "
        "so the DME stores a pump-module fault that shows in INPA, ISTA and PA-Soft but doesn't light the "
        "check-engine lamp. Never connect that 0–120 Hz PWM output to K96: a relay coil can't follow it and "
        "would likely chatter. Optional: the US M3's EKP pump module, driven by pin 11, slows the pump at idle "
        "and part load, and the DME cuts its power when the airbag unit signals a crash; pin 10 is then unused. "
        "Fit it only if your state won't accept the stored fault or you want those functions back.")
svg = svg_open(H, ARIA) + "\n".join(out) + "\n</svg>"
print(write("11-fuel-pump-control.svg", svg))
