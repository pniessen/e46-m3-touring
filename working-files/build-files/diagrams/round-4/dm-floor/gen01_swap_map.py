#!/usr/bin/env python3
"""Figure 1 (diagrams/01-swap-map.svg): fix the floor wording only.

The original called the floor "fabricated or modified" (aria-label) and "rework floor" (visible
label). The guide now replaces the Touring's well with a new BMW M3 trunk floor (41127895619),
or the donor M3's floor. Nothing else changes. Re-run from the backed-up original in orig/.
"""
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "orig" / "01-swap-map.svg"
DST = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/diagrams/01-swap-map.svg")

EDITS = [
    ("the fuel filter-regulator is new; rear arches, subframe mounts, floor and rear bumper are "
     "fabricated or modified.",
     "the fuel filter-regulator is new; rear arches, subframe mounts and rear bumper are fabricated "
     "or modified, and the spare-wheel well is replaced by a new BMW M3 trunk floor, or the donor "
     "M3's floor, so the M3 muffler fits."),
    ('<text class="t crit-t" x="272" y="368">well: rework floor</text>',
     '<text class="t crit-t" x="272" y="368">well: fit M3 floor</text>'),
]

svg = SRC.read_text(encoding="utf-8")
for old, new in EDITS:
    assert svg.count(old) == 1, old
    svg = svg.replace(old, new)
DST.write_text(svg, encoding="utf-8")
print("wrote", DST)
