#!/usr/bin/env python3
"""Regenerate diagrams/06-electronics.svg to match the new Figure 6 caption (same layout and size)."""
import sys
sys.dont_write_bytecode = True
from svgkit import svg_open, write

ARIA = ("Electronics after the swap. In the engine bay the M3 engine harness plugs into your body harness once a "
        "few body-side pins are moved; the DME is EWS-deleted with your VIN written in, or virginized and synced "
        "to your EWS; and the DSC unit, your own MK60 or the M3's, is coded and initialised. The DME, DSC, M3 "
        "cluster and steering-angle sensor share the CAN bus. In the cabin your EWS and keys stay and still "
        "control starting through the clutch interlock, the M3 cluster gets your VIN and takes your true mileage "
        "from the light module, and the steering-angle sensor is calibrated after the wheel alignment.")

BODY = """
<!-- Key -->
<rect class="donor" x="8" y="6" width="12" height="12" rx="2"/>
<text class="t-sm" x="25" y="16.5">From donor M3</text>
<rect class="keep" x="130" y="6" width="12" height="12" rx="2"/>
<text class="t-sm" x="147" y="16.5">Keep</text>
<text class="t-sm fab-t t-b" x="200" y="16.5">Orange text: what you do</text>

<!-- Zones -->
<rect class="panel" x="6" y="28" width="388" height="214" rx="8"/>
<text class="t-xs t-b" x="16" y="46">ENGINE BAY</text>
<rect class="panel" x="6" y="290" width="388" height="222" rx="8"/>
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
<text class="t-sm" x="28" y="192">or virginized and synced</text>
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
<path class="ln" d="M382,476 H390 V266"/>

<!-- EWS to DME rolling code, skipped after a delete -->
<line class="crit-s dash" x1="60" y1="320" x2="60" y2="198" stroke-width="2"/>

<!-- Cabin -->
<rect class="keep" x="18" y="320" width="140" height="50" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="28" y="340">EWS3 + keys</text>
<text class="t-sm" x="28" y="358">still controls starting</text>

<rect class="keep" x="18" y="404" width="140" height="50" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="28" y="424">Clutch switch</text>
<text class="t-sm" x="28" y="442">to EWS and DME</text>
<line class="ln" x1="88" y1="404" x2="88" y2="371" marker-end="url(#ah)"/>
<text class="t-xs" x="94" y="391">US start interlock</text>

<rect class="donor" x="210" y="316" width="172" height="56" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="220" y="335">M3 cluster</text>
<text class="t fab-t" x="220" y="352">gets your VIN</text>
<text class="t-sm" x="220" y="367">via a service or new chip</text>

<rect class="keep" x="210" y="396" width="172" height="46" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="220" y="415">Light module (LCM)</text>
<text class="t-sm" x="220" y="432">holds VIN + true mileage</text>
<line class="ln" x1="260" y1="395" x2="260" y2="373" marker-end="url(#ah)"/>
<text class="t-xs" x="266" y="387.5">true mileage</text>

<rect class="keep" x="210" y="450" width="172" height="54" rx="5" stroke-width="1.5"/>
<text class="t t-b" x="220" y="468">Steering-angle sensor</text>
<text class="t fab-t" x="220" y="484">calibrate it after the</text>
<text class="t fab-t" x="220" y="499">wheel alignment</text>
"""

svg = svg_open(516, ARIA) + BODY.lstrip("\n") + "</svg>"
print(write("06-electronics.svg", svg))
