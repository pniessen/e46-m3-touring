#!/usr/bin/env python3
"""Generate diagrams/15-build-timeline.svg.

Model (stated in the figure): a typical 24-month build. Paint-shop time is the guide's "about four
months" at one shop; the rest of the 24 months is shared out in proportion to the guide's weekend
estimates (midpoints of the Time table's ranges). Phases that share one estimate split it evenly.
Phase 0 has no estimate in the guide; it gets a short, unlabeled bar.
"""
import pathlib

OUT = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/diagrams/15-build-timeline.svg")

TOTAL_MONTHS = 24.0
PAINT_SHOP = 4.0
# Midpoints of the Time table (weekends), split per phase where one estimate covers several.
work = {0: 3, 1: 3, 2: 3, 4: 3, 5: 6, 6: 12, 7: 2.5, 8: 2.5, 9: 2.5, 10: 2.5, 11: 3, 12: 3, 13: 6}
per_weekend = (TOTAL_MONTHS - PAINT_SHOP) / sum(work.values())

# Serial chain on your Touring; Phase 3 runs alongside 4-8.
t = 0.0
span = {}
for p in [0, 1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
    span[p] = (t, t + work[p] * per_weekend)
    t = span[p][1]
p13_own = work[13] * per_weekend
span[13] = (t, t + p13_own + PAINT_SHOP)
span[3] = (span[4][0], span[8][1])

X0, PX = 56.0, 10.8          # chart origin and px per month (30 months -> x=380)
def x(m):
    return X0 + PX * m

ROW0, ROWH = 50.0, 32.0
def top(i):
    return ROW0 + ROWH * i

def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")

for p in sorted(span):
    a, b = span[p]
    print(p, f"{a:5.2f}-{b:5.2f} mo", f"x {x(a):6.1f}-{x(b):6.1f}")
print("months per weekend", round(per_weekend, 3))

ARIA = "A typical 24-month build on a calendar, with a mark every six months and a typical finish between 18 and 30 months. Phases 0 to 2, paperwork and baseline, buying and inspecting the donor, and stripping the donor, fill roughly the first three and a half months; the donor is bought and tested at the end of Phase 1. Phase 3, bench work on the S54, 420G, axles, DME and fenders, runs alongside Phases 4 to 8. After stripping your Touring, Phase 5 welds the subframe mounts and floor, and the first cut into your floor there is the point of no return; Phase 6, the rear arches, is the longest phase of your own work. Phases 7 to 10 fit the rear axle and fuel system, front suspension and steering, the S54 and 420G, and cooling, intake and exhaust; Phase 11 is wiring, immobilizer and coding; Phase 12 fits the front end and includes the first start, shakedown and alignment. Phase 13 includes about four months at the paint shop and ends with inspection at about 24 months. Bar lengths follow the guide's weekend estimates for each phase: typical, and your times will vary."

STYLE = open("/home/user/archeyon/e46-m3-touring-conversion/diagrams/03-subframe-mount.svg").read()
STYLE = STYLE[STYLE.index("<style>"):STYLE.index("</style>") + len("</style>")]

KIND = {0: "shape", 1: "donor", 2: "donor", 3: "donor", 4: "shape", 5: "fab", 6: "fab",
        7: "shape", 8: "shape", 9: "shape", 10: "shape", 11: "shape", 12: "shape"}
TITLES = {
    0: ["Paperwork and baseline"],
    1: ["Buy and inspect the donor"],
    2: ["Strip the donor"],
    3: ["Bench work, alongside 4–8"],
    4: ["Strip your Touring"],
    5: ["Metalwork 1, subframe mounts and floor"],
    6: ["Metalwork 2, rear arches"],
    7: ["Fit the M3 rear axle and", "fuel system"],
    8: ["Fit the M3 front suspension", "and steering"],
    9: ["Install the S54 and 420G"],
    10: ["Cooling, intake and", "exhaust"],
    11: ["Wiring, immobilizer and", "coding"],
    12: ["Front end, first start", "and shakedown"],
    13: ["Paint, trim and paperwork"],
}
LEFT = {12, 13}            # titles that sit left of their bar
NOTE2 = {0: "before you buy the donor", 3: "S54, 420G, axles, DME, fenders"}

def diamond(cx, cy, cls, r=4.5):
    return (f'<path class="{cls}" d="M{f(cx)},{f(cy - r)} L{f(cx + r)},{f(cy)} '
            f'L{f(cx)},{f(cy + r)} L{f(cx - r)},{f(cy)} Z"/>')

L = []
add = L.append
H = 618
add('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 %d" role="img" aria-label="ARIA" color="#1b2128">' % H)
add(STYLE)
add('<defs>\n  <marker id="ah" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="fill-fg"/></marker>\n</defs>')
add(f'<rect class="bg" x="0" y="0" width="400" height="{H}" fill="#ffffff"/>')
add('')
add('<text class="t-h" x="8" y="20">BUILD CALENDAR</text>')
add('<text class="t-xs" x="390" y="20" text-anchor="end">Typical; your times will vary</text>')
add('<text class="t-xs t-b" x="8" y="42">weekends</text>')
add('')
bottom = top(14) + 4
add('<!-- Typical finish window and month grid -->')
add(f'<rect class="panel" x="{f(x(18))}" y="46" width="{f(x(30) - x(18))}" height="{f(bottom - 46)}" opacity="0.6"/>')
add('<g class="ln-faint">')
for m in range(0, 31, 6):
    add(f'  <line x1="{f(x(m))}" y1="46" x2="{f(x(m))}" y2="{f(bottom)}"/>')
add('</g>')
add('')
add('<!-- Weekend estimates from the Time table; brackets join phases that share one -->')
def bracket(r0, r1, label):
    y0, y1 = top(r0) + 7, top(r1) + 17
    add(f'<path class="ln-thin" d="M43,{f(y0)} H47 V{f(y1)} H43"/>')
    add(f'<text class="t-sm" x="40" y="{f((y0 + y1) / 2 + 4)}" text-anchor="end">{label}</text>')
def single(r, label):
    add(f'<text class="t-sm" x="40" y="{f(top(r) + 16)}" text-anchor="end">{label}</text>')
bracket(1, 2, "4–8")
single(3, "6–10")
single(4, "2–4")
single(5, "4–8")
single(6, "8–16")
bracket(7, 10, "8–12")
bracket(11, 12, "4–8")
single(13, "4–8")
add(f'<text class="t-xs" x="40" y="{f(top(13) + 30)}" text-anchor="end">+ shop</text>')
add('')
add('<!-- Phase bars -->')
for p in range(13):
    a, b = span[p]
    add(f'<rect class="{KIND[p]}" x="{f(x(a))}" y="{f(top(p) + 7.5)}" width="{f(x(b) - x(a))}" height="9" rx="1.5" stroke-width="1.5"/>')
a13, b13 = span[13]
own = p13_own / 2
add(f'<rect class="shape" x="{f(x(a13))}" y="{f(top(13) + 7.5)}" width="{f(x(a13 + own) - x(a13))}" height="9" rx="1.5"/>')
add(f'<rect class="keep dash" x="{f(x(a13 + own))}" y="{f(top(13) + 7.5)}" width="{f(x(b13 - own) - x(a13 + own))}" height="9" rx="1.5" stroke-width="1.5"/>')
add(f'<rect class="shape" x="{f(x(b13 - own))}" y="{f(top(13) + 7.5)}" width="{f(x(b13) - x(b13 - own))}" height="9" rx="1.5"/>')
add('')
add('<!-- Phase titles -->')
for p in range(14):
    a, b = span[p]
    lines = TITLES[p]
    if p in LEFT:
        tx, anchor = x(a) - 6, ' text-anchor="end"'
    else:
        tx, anchor = x(b) + 6, ''
    for k, line in enumerate(lines):
        y = top(p) + 16 + 14 * k
        if k == 0:
            add(f'<text class="t-sm fill-fg" x="{f(tx)}" y="{f(y)}"{anchor}><tspan class="t-b">{p} </tspan>{line}</text>')
        else:
            pad = 0 if anchor else (16.5 if p >= 10 else 10)
            add(f'<text class="t-sm fill-fg" x="{f(tx + pad)}" y="{f(y)}"{anchor}>{line}</text>')
    if p in NOTE2:
        add(f'<text class="t-xs" x="{f(tx + (16.5 if p >= 10 else 10))}" y="{f(top(p) + 30)}">{NOTE2[p]}</text>')
add('')
add('<!-- Milestones -->')
cy = lambda r: top(r) + 12
add(diamond(x(span[1][1]), cy(1), "fill-fg"))
add(f'<text class="t-xs t-b fill-fg" x="{f(x(span[1][1]) + 16)}" y="{f(top(1) + 30)}">Donor bought and tested</text>')
first_cut = span[5][0] + 0.4 * (span[5][1] - span[5][0])
add(diamond(x(first_cut), cy(5), "crit-f"))
add(f'<text class="t-xs t-b crit-t" x="{f(x(span[5][1]) + 16)}" y="{f(top(5) + 30)}">First cut into your floor: point of no return</text>')
fs = span[12][0] + 0.15 * (span[12][1] - span[12][0])
al = span[12][1]
add(diamond(x(fs), cy(12), "fill-fg", 3.6))
add(diamond(x(al), cy(12), "fill-fg", 3.6))
add(f'<text class="t-xs t-b fill-fg" x="{f(x(span[12][1]) + 8)}" y="{f(top(12) + 16)}">First start</text>')
add(f'<text class="t-xs t-b fill-fg" x="{f(x(span[12][1]) + 8)}" y="{f(top(12) + 30)}">Alignment</text>')
add(diamond(x(span[13][1]), cy(13), "fill-fg"))
add(f'<text class="t-xs t-b fill-fg" x="{f(x(span[13][1]) + 7)}" y="{f(top(13) + 16)}">Inspection</text>')
add(f'<text class="t-xs" x="{f((x(a13 + own) + x(b13 - own)) / 2)}" y="{f(top(13) + 30)}" text-anchor="middle">at the paint shop, about 4 months</text>')
add('')
add('<!-- Month axis -->')
for m in range(0, 31, 6):
    add(f'<text class="t-xs" x="{f(x(m))}" y="{f(bottom + 13)}" text-anchor="middle">{m}</text>')
add(f'<text class="t-xs" x="56" y="{f(bottom + 27)}">months from the start</text>')
add(f'<line class="ln-thin" x1="163" y1="{f(bottom + 23.5)}" x2="181" y2="{f(bottom + 23.5)}" marker-end="url(#ah)"/>')
add(f'<text class="t-xs t-b" x="{f((x(18) + x(30)) / 2)}" y="{f(bottom + 27)}" text-anchor="middle">typical finish: 18–30 months</text>')
add('')
ky = bottom + 44
add('<!-- Key -->')
add(f'<rect class="shape" x="8" y="{f(ky)}" width="12" height="12" rx="2"/>')
add(f'<text class="t-sm" x="26" y="{f(ky + 10.5)}">Your Touring</text>')
add(f'<rect class="donor" x="132" y="{f(ky)}" width="12" height="12" rx="2" stroke-width="1.5"/>')
add(f'<text class="t-sm" x="150" y="{f(ky + 10.5)}">Donor and bench</text>')
add(f'<rect class="fab" x="270" y="{f(ky)}" width="12" height="12" rx="2" stroke-width="1.5"/>')
add(f'<text class="t-sm" x="288" y="{f(ky + 10.5)}">Welding</text>')
add(f'<rect class="keep dash" x="8" y="{f(ky + 18)}" width="12" height="12" rx="2" stroke-width="1.5"/>')
add(f'<text class="t-sm" x="26" y="{f(ky + 28.5)}">At a shop</text>')
add(diamond(138, ky + 24, "fill-fg"))
add(f'<text class="t-sm" x="150" y="{f(ky + 28.5)}">Milestone</text>')
add('')
ny = ky + 52
add(f'<text class="t-xs" x="8" y="{f(ny)}">Bar lengths follow the guide\'s weekend estimates, spread over a</text>')
add(f'<text class="t-xs" x="8" y="{f(ny + 13)}">24-month build with about four months at the paint shop.</text>')
add('</svg>')

svg = ("\n".join(L) + "\n").replace('aria-label="ARIA"', 'aria-label="' + ARIA + '"')
print("bottom", bottom, "key", ky, "note", ny, "H", H)
OUT.write_text(svg, encoding="utf-8")
