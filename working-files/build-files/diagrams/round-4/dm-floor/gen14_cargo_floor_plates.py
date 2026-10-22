#!/usr/bin/env python3
"""Redraw of Figure 5 (diagrams/14-cargo-floor-plates.svg).

Panel A (underside) is copied verbatim from the original (orig/14-cargo-floor-plates.svg).
Panel B (cargo side) is regenerated: the "no flame-cutting or grinding within about 120 mm of the
rails" bands and labels are gone. Now the floor behind the RACP seam, well included, is drilled
out along its spot welds at the RACP seam, both rails and the rear panel, so those flanges
stay; CMP's 120 mm (5 in) is shown as the strip CMP cuts away to reach the rear-mount tops
(README fragments 0460 step 8 and 0470 "Cut rules").
"""
import pathlib
import re

from floorkit import Fig, build, write, shift_markup

HERE = pathlib.Path(__file__).resolve().parent
ORIG = (HERE / "orig" / "14-cargo-floor-plates.svg").read_text(encoding="utf-8")

ARIA = (
    "Two plan views of the Touring's rear floor around the rear subframe mounts, front of the car at "
    "the top, schematic and not to scale. From below, with the fuel tank, exhaust and subframe out: one "
    "reinforcement plate is plug-welded under each of the four subframe mounts, a V-brace mounting box "
    "is welded in on each side where the Touring has a grommet, the M3 push rod and V-brace bolt on "
    "later, and both diagonals between the mounts are measured before welding and after each session. "
    "From the cargo side, with the seat and trim out: the front-mount top welds are reached by cutting "
    "in under the rear seat and patching; the Touring has no partition wall behind the seat, so some kit "
    "parts won't fit; failed spot welds along the rail flanges are stitched and rail plates fitted. The "
    "floor behind the RACP seam, spare-wheel well included, is separated by drilling out its spot welds "
    "along the RACP seam, both rails and the rear panel, so those flanges stay whole, and it drops out "
    "downward; the three rosette welds on each rear mount are then welded through the opening. CMP's "
    "120 mm (5 in) is the strip of the well beside each rail that CMP cuts away to reach the mount "
    "tops, so it comes out with the well; it is not a zone to avoid. No kit maker publishes "
    "Touring-specific cargo-side plates, so sedan-pattern plates are dry-fitted and traced before cutting."
)

H = 742


def closing_g(src: str, start: int) -> int:
    """Index of the </g> that closes the <g ...> opening at start (nested groups counted)."""
    import re
    depth = 0
    for m in re.finditer(r"<g[\s>]|</g>", src[start:]):
        depth += -1 if m.group(0) == "</g>" else 1
        if depth == 0:
            return start + m.start()
    raise ValueError("unclosed <g>")


def panel_b():
    """Cargo side, seen from above, in the group's own coordinates (translate(8,354))."""
    d = Fig()
    # floor between the rails; the part behind the seam comes out
    d.rect("panel", 14, 0, 168, 236)
    d.rect("fab dash", 14, 118, 168, 118, sw=1.5)
    # CMP's access strips: within 120 mm of each rail, at the front of the well
    for x0 in (14, 152):
        d.rect("fab-f", x0, 118, 30, 44, extra=' opacity="0.16"')
        d.hatch("fab-s", x0, 118, x0 + 30, 162, step=6, sw=0.8)
    # rails, and the rear panel behind the floor
    d.rect("keep", 0, 0, 14, 244)
    d.rect("keep", 182, 0, 14, 244)
    d.rect("keep", 0, 236, 196, 8)

    # rear-seat base: front mounts below, cut-in openings (as before)
    d.text("t-xs", 98, 22, "rear-seat base", "middle")
    d.circle("ln-thin dash", 44, 48, 5.5)
    d.circle("ln-thin dash", 152, 48, 5.5)
    d.rect("fab-s dash", 33, 37, 22, 22, rx=2, sw=1.5)
    d.rect("fab-s dash", 141, 37, 22, 22, rx=2, sw=1.5)
    # no partition wall behind the seat on a Touring
    d.rect("warn-f dash", 14, 62, 168, 7)

    # RACP; rail-to-RACP flange spot welds and rail plates (as before)
    d.text("t-xs", 98, 98, "RACP", "middle")
    for y in (75, 82, 89, 96):
        d.dot("fill-fg", 17.5, y, 1.6)
        d.dot("fill-fg", 178.5, y, 1.6)
    d.rect("fab", 6, 100, 22, 15, rx=2, sw=1.5)
    d.rect("fab", 168, 100, 22, 15, rx=2, sw=1.5)
    for x in (11, 23, 173, 185):
        d.dot("fab-f", x, 107.5, 1.8)

    # the seam across the front of the well: a flange that stays
    d.line("ln", 14, 118, 182, 118)

    # the deep well, inside the floor that comes out
    d.rect("fab-s dash", 48, 124, 100, 106, rx=20, sw=1.5)
    d.text("t-xs fab-t", 98, 172, "floor and well", "middle")
    d.text("t-xs fab-t", 98, 185, "drop out below", "middle")

    # spot welds to drill from above: the seam, both rails, the rear panel
    x = 22.0
    while x <= 174.1:
        d.dot("fab-f", x, 118, 1.6)
        d.dot("fab-f", x, 240, 1.6)
        x += 8
    y = 126.0
    while y <= 230.1:
        d.dot("fab-f", 17.5, y, 1.6)
        d.dot("fab-f", 178.5, y, 1.6)
        y += 8

    # rear mounts below; the three rosette welds on top (as before)
    d.circle("ln-thin dash", 36, 133, 7)
    d.circle("ln-thin dash", 160, 133, 7)
    for cx in (36, 160):
        d.dot("fab-f", cx - 4, 130, 2.2)
        d.dot("fab-f", cx + 4, 130, 2.2)
        d.dot("fab-f", cx, 137, 2.2)

    # CMP's strip width
    d.line("ln-thin", 153, 155, 181, 155, start="ah", end="ah")

    # labels
    for dd in ("M204,33 L164,46", "M204,68 L180,65.5", "M204,99 L190,106", "M204,141 L171,121",
               "M204,187 L166,135", "M204,233 L176,158"):
        d.path("ln-thin", dd)
    d.text("t-sm fab-t", 206, 26, "Front mounts, under the seat:")
    d.text("t-sm fab-t", 206, 40, "cut in, weld the tops, patch")
    d.text("t-sm", 206, 62, "No partition wall behind the")
    d.text("t-sm", 206, 76, "seat: some kit parts won't fit")
    d.text("t-sm fab-t", 206, 98, "Rail flange: stitch failed spot")
    d.text("t-sm fab-t", 206, 112, "welds, then fit rail plates")
    d.text("t-sm crit-t", 206, 134, "Keep the flanges: drill out the")
    d.text("t-sm crit-t", 206, 148, "spot welds along the seam,")
    d.text("t-sm crit-t", 206, 162, "both rails and the rear panel")
    d.text("t-sm fab-t", 206, 180, "Rear mounts: through the")
    d.text("t-sm fab-t", 206, 194, "opening, weld the three")
    d.text("t-sm fab-t", 206, 208, "rosette welds on top")
    d.text("t-sm", 206, 226, "CMP's 120 mm (5 in): the strip")
    d.text("t-sm", 206, 240, "CMP cuts away to reach the")
    d.text("t-sm", 206, 254, "mount tops. It comes out too")
    return d


def make():
    """Both panels are flattened to absolute coordinates (no group transforms), so the layout
    checker, which ignores transforms, sees them where they render."""
    body = Fig()
    pa = ORIG.index("<!-- ============ Panel A")
    ga = ORIG.index('<g transform="translate(8,50)">')
    ga_end = closing_g(ORIG, ga)
    gb = ORIG.index('<g transform="translate(8,354)">')
    body.add(ORIG[pa:ga].rstrip() + "\n")           # panel A heading: verbatim
    inner_a = ORIG[ga + len('<g transform="translate(8,50)">'):ga_end]
    body.add("<!-- panel A drawing (was translate(8,50)), flattened -->")
    body.add(shift_markup(inner_a, 8, 50).strip("\n"))
    body.add(ORIG[ga_end + len("</g>"):gb].rstrip() + "\n")   # separator and panel B heading: verbatim
    b = panel_b()
    body.add("<!-- panel B drawing (translate(8,354)), flattened -->")
    body.add(shift_markup(b.body(), 8, 354))

    # Touring note (moved down) and key
    ny = 636
    body.add(f'\n<!-- Touring note -->\n<rect class="warn-f" x="8" y="{ny}" width="384" height="58" rx="5"/>')
    body.text("t-sm fill-fg", 18, ny + 19, "No kit maker publishes Touring-specific cargo-side plates.")
    body.text("t-sm fill-fg", 18, ny + 34, "The steel is the sedan's, so sedan-pattern plates should")
    body.text("t-sm fill-fg", 18, ny + 49, "land in the same places: dry-fit and trace before you cut.")
    ky = 706
    body.comment("Key")
    body.rect("fab", 8, ky, 12, 12, rx=2)
    body.text("t-sm", 26, ky + 10.5, "Phase 5: cut, weld, fit")
    body.line("donor-s dash", 206, ky + 6, 222, ky + 6, sw=2.5)
    body.text("t-sm", 228, ky + 10.5, "M3 part, bolted on in Phase 7")
    ky += 18
    body.rect("keep", 8, ky, 12, 12, rx=2)
    body.text("t-sm", 26, ky + 10.5, "Your Touring's floor and rails")
    for x in (208, 214, 220):
        body.dot("fab-f", x, ky + 6, 1.6)
    body.text("t-sm", 228, ky + 10.5, "Spot welds to drill out")
    return body


def main():
    body = build(make)
    style = re.search(r"<style>.*?</style>", ORIG, re.S).group(0)
    defs = re.search(r"<defs>.*?</defs>", ORIG, re.S).group(0)
    from xml.sax.saxutils import escape
    head = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 {H}" role="img" '
            f'aria-label="{escape(ARIA, {chr(34): "&quot;"})}" color="#1b2128">\n{style}\n{defs}\n'
            f'<rect class="bg" x="0" y="0" width="400" height="{H}" fill="#ffffff"/>\n\n')
    p = write("14-cargo-floor-plates.svg", head, body.body())
    print("wrote", p)


if __name__ == "__main__":
    main()
