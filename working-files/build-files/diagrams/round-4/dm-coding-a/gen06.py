#!/usr/bin/env python3
"""Redraw diagrams/06-electronics.svg (README Figure 8).

Same layout as last round's gen06.py. Round-4 changes, all in the cabin:
- the M3 cluster box says it carries the donor's vehicle order (coordinator's correction from BMW's coding
  data: the cluster keeps the donor's order for good);
- the light-module box says it also holds the car's own vehicle order;
- both boxes grow, so the light module, the steering-angle sensor, its CAN drop and the cabin panel move down.
- Review fix F7: the DME line reads "or matched to your EWS" (a vendor's match or your own sync).
Run:  python3 -I gen06.py
"""
import os
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(__file__))
from ckit import Doc, run, width  # noqa: E402

ARIA = ("Electronics after the swap. In the engine bay the M3 engine harness plugs into your body harness once a "
        "few body-side pins are moved; the DME is EWS-deleted with your VIN written in, or matched to your EWS by "
        "a vendor or by your own sync; and the DSC unit, your own MK60 or the M3's, is coded and initialised. The DME, DSC, M3 "
        "cluster and steering-angle sensor share the CAN bus. In the cabin your EWS and keys stay and still "
        "control starting through the clutch interlock. The M3 cluster gets your VIN through a service or a new "
        "chip, takes your true mileage from the light module and keeps the donor's vehicle order. The light "
        "module holds your VIN, your true mileage and the car's own vehicle order. The steering-angle sensor is "
        "calibrated after the wheel alignment.")

ENGINE_BAY = """
<!-- Key -->
<rect class="donor" x="8" y="6" width="12" height="12" rx="2"/>
<text class="t-sm" x="25" y="16.5">From donor M3</text>
<rect class="keep" x="130" y="6" width="12" height="12" rx="2"/>
<text class="t-sm" x="147" y="16.5">Keep</text>
<text class="t-sm fab-t t-b" x="200" y="16.5">Orange text: what you do</text>

<!-- Zones -->
<rect class="panel" x="6" y="28" width="388" height="214" rx="8"/>
<text class="t-xs t-b" x="16" y="46">ENGINE BAY</text>
<rect class="panel" x="6" y="290" width="388" height="{cabin_h}" rx="8"/>
<text class="t-xs t-b" x="16" y="308">CABIN</text>

<!-- Engine bay -->
<rect class="donor" x="18" y="56" width="172" height="58" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="28" y="75">M3 engine harness</text>
<text class="t fab-t" x="28" y="92">move a few pins in</text>
<text class="t fab-t" x="28" y="108">your body-side plugs</text>
<rect class="keep" x="210" y="56" width="172" height="58" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="220" y="75">Your body harness</text>
<text class="t-sm" x="220" y="92">meets the DME plugs</text>
<text class="t-sm" x="220" y="108">in the E-box</text>
<path class="fab-s" d="M190,85 H210" stroke-width="5"/>

<rect class="donor" x="18" y="140" width="172" height="58" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="28" y="159">DME (MSS54 / HP)</text>
<text class="t fab-t" x="28" y="176">EWS-deleted, your VIN</text>
<text class="t-sm" x="28" y="192">or matched to your EWS</text>
<line class="ln" x1="104" y1="114" x2="104" y2="139" marker-end="url(#ah)"/>

<rect class="keep" x="210" y="140" width="172" height="58" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="220" y="159">DSC unit (MK60)</text>
<text class="t-sm" x="220" y="176">yours, or the M3's</text>
<text class="t fab-t" x="220" y="192">code and initialise</text>

<text class="t-xs crit-t" x="68" y="222">rolling-code check</text>
<text class="t-xs crit-t" x="68" y="235">off after a delete</text>

<!-- CAN bus -->
<line class="ln" x1="28" y1="266" x2="390" y2="266" style="stroke-width:3"/>
<text class="t-xs t-b" x="12" y="262">CAN</text>
<line class="ln" x1="172" y1="198" x2="172" y2="266"/>
<line class="ln" x1="296" y1="198" x2="296" y2="266"/>
<line class="ln" x1="330" y1="266" x2="330" y2="316"/>
<path class="ln" d="M382,{sas_mid} H390 V266"/>

<!-- EWS to DME rolling code, skipped after a delete -->
<line class="crit-s dash" x1="60" y1="320" x2="60" y2="198" stroke-width="2"/>

<!-- Cabin, left: EWS and the clutch interlock (unchanged) -->
<rect class="keep" x="18" y="320" width="140" height="50" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="28" y="340">EWS3 + keys</text>
<text class="t-sm" x="28" y="358">still controls starting</text>

<rect class="keep" x="18" y="404" width="140" height="50" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="28" y="424">Clutch switch</text>
<text class="t-sm" x="28" y="442">to EWS and DME</text>
<line class="ln" x1="88" y1="404" x2="88" y2="371" marker-end="url(#ah)"/>
<text class="t-xs" x="94" y="391">US start interlock</text>
"""


def build(d: Doc):
    over = []
    # cabin, right column: cluster, light module, steering-angle sensor
    X, W = 210, 172
    cl_y, cl_h = 316, 88
    lcm_y, lcm_h = cl_y + cl_h + 24, 62
    sas_y, sas_h = lcm_y + lcm_h + 12, 54
    cabin_bottom = sas_y + sas_h + 8
    d.add(ENGINE_BAY.strip("\n").replace("{cabin_h}", str(cabin_bottom - 290))
          .replace("{sas_mid}", str(sas_y + sas_h // 2)))

    def box(cls, y, h, rows):
        d.add(f'<rect class="{cls}" x="{X}" y="{y}" width="{W}" height="{h}" rx="5" stroke-width="1.5"/>')
        for dy, c, s in rows:
            d.text(c, X + 10, y + dy, s)
            if X + 10 + width(c, s) > X + W - 3:
                over.append(s)

    d.comment("Cabin, right: the M3 cluster carries the donor's vehicle order; the light module holds the car's")
    box("donor", cl_y, cl_h, [(19, "t t-b", "M3 cluster"), (36, "t fab-t", "gets your VIN"),
                              (51, "t-sm", "via a service or new chip"),
                              (66, "t-sm", "keeps the donor's"), (80, "t-sm", "vehicle order")])
    box("keep", lcm_y, lcm_h, [(19, "t t-b", "Light module (LCM)"), (36, "t-sm", "holds VIN + true mileage"),
                               (51, "t-sm", "and the car's vehicle order")])
    a0, a1 = lcm_y - 1, cl_y + cl_h + 1
    d.add(f'<line class="ln" x1="260" y1="{a0}" x2="260" y2="{a1}" marker-end="url(#ah)"/>')
    d.text("t-xs", 266, (a0 + a1) / 2 + 3.5, "true mileage")
    box("keep", sas_y, sas_h, [(18, "t t-b", "Steering-angle sensor"), (34, "t fab-t", "calibrate it after the"),
                               (49, "t fab-t", "wheel alignment")])
    if over:
        print("DOES NOT FIT:", *over, sep="\n  ", flush=True)
    return cabin_bottom + 4, ARIA


if __name__ == "__main__":
    run(build, "06-electronics.svg")
