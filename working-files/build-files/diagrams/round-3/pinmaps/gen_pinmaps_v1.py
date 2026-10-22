#!/usr/bin/env python3
"""Generate the two connector pin maps (landscape, 800 wide):

    17-pinmap-ms43.svg   MS43 Touring (09/2001 to 02/2003)
    18-pinmap-ms45.svg   MS45.1 Touring (from 03/2003)

Both share one layout (same scale, positions, legend and card grid) so a reader can compare them.
Data: scratchpad/foldin/wiring-canonical.md sections 2-4 (= the WIRING-AND-CODING.md move tables).
Text in backticks is set in t-mono (pins, wire codes, connector names, part numbers).
"""
import re
import sys

sys.dont_write_bytecode = True
from pmkit import Canvas, marker, write  # noqa: E402

W, H = 800, 640

# ---------------------------------------------------------------- geometry
P, CW, CH = 30, 26, 22          # cavity pitch, width, height
G = 16                          # gap between the two rows of a block
CHAN = 56                       # channel between the upper and lower block (two lanes run in it)
YT = 98                         # top of X60004's top row (31-40)
XC = 372                        # left edge of X60004 column 1
ROWS = {                        # X60004 row tops: pin 1 at the bottom left, rows run left to right
    "U1": YT, "U2": YT + CH + G,                      # upper block: 31-40 over 21-30
    "L1": YT + 2 * CH + G + CHAN, "L2": YT + 3 * CH + 2 * G + CHAN,  # lower block: 11-20 over 1-10
}
XX = 44                         # left edge of X6011 column 1
XGAP = 20                       # gap between X6011's rows
YX = ROWS["L1"] + CH / 2 - CH - XGAP / 2   # X6011's row gap lines up with X60004 row 11-20


def x4(pin):
    """Left edge and top of an X60004 cavity."""
    r, col = (pin - 1) // 10, (pin - 1) % 10
    return XC + P * col, ROWS[["L2", "L1", "U2", "U1"][r]]


def x11(pin):
    """Left edge and top of an X6011 cavity (5 6 7 8 over 1 2 3 4)."""
    if pin <= 4:
        return XX + P * (pin - 1), YX + CH + XGAP
    return XX + P * (pin - 5), YX


def mid4(pin):
    x, y = x4(pin)
    return x + CW / 2, y + CH / 2


def mid11(pin):
    x, y = x11(pin)
    return x + CW / 2, y + CH / 2


# ---------------------------------------------------------------- text with `mono` runs
def segs(s, base_mono="t-mono"):
    """'empty → `0.35 BL` from ...' -> list of str / (str, 't-mono') for Canvas.text."""
    out = []
    for i, part in enumerate(s.split("`")):
        if not part:
            continue
        out.append((part, base_mono) if i % 2 else part)
    return out


# ---------------------------------------------------------------- cavity styles
class _NoText:
    def __init__(self, c):
        self.c = c

    def rect(self, *a, **k):
        self.c.rect(*a, **k)

    def text(self, *a, **k):
        pass


def cavity(c, x, y, num, state, w=CW, h=CH):
    """state: keep | empty | moved | new | emptied | outnew. num '' draws a legend chip."""
    if not num:
        c = _NoText(c)
    big = "t t-b t-mono"
    if state == "keep":
        c.rect(x, y, w, h, "keep", rx=3, sw=1.5)
        c.text(x + w / 2, y + h / 2 + 4, num, "t-sm t-mono", "middle")
    elif state == "empty":
        c.rect(x, y, w, h, "fill-bg", rx=3)
        c.rect(x, y, w, h, "ln-thin", rx=3)
        c.text(x + w / 2, y + h / 2 + 4, num, "t-sm t-mono", "middle")
    elif state == "moved":
        c.rect(x, y, w, h, "fab", rx=3, sw=1.5)
        c.text(x + w / 2, y + h / 2 + 4.5, num, big, "middle")
    elif state == "new":
        c.rect(x, y, w, h, "new", rx=3, sw=1.5)
        c.text(x + w / 2, y + h / 2 + 4.5, num, big, "middle")
    elif state == "emptied":
        c.rect(x, y, w, h, "fill-bg", rx=3)
        c.rect(x, y, w, h, "fab-s dash", rx=3, sw=1.5)
        c.text(x + w / 2, y + h / 2 + 4.5, num, big, "middle")
    elif state == "outnew":
        c.rect(x - 3, y - 3, w + 6, h + 6, "fab-s dash", rx=4, sw=1.5)
        c.rect(x, y, w, h, "new", rx=3, sw=1.5)
        c.text(x + w / 2, y + h / 2 + 4.5, num, big, "middle")
    else:
        raise ValueError(state)


def halo(c, x, y, w=CW, h=CH):
    c.rect(x - 6, y - 6, w + 12, h + 12, "warn-f", rx=6, sw=1.5)


def dot(c, x, y, cls="fab-f"):
    c.circle(x, y, 2.5, cls)


# ---------------------------------------------------------------- data
X4_KEEP = {p: "keep" for p in range(1, 41)}

MS43 = {
    "key": "ms43",
    "file": "17-pinmap-ms43.svg",
    "title": "MS43 TOURING: X60004 AND BODY X6011",
    "sub": "For a Touring built 09/2001 to 02/2003, with an M3 donor built from 09/2001.",
    "x60004": {**X4_KEEP,
               **{p: "moved" for p in (1, 2, 11, 18, 21, 34)},
               **{p: "new" for p in (5, 15, 16)},
               **{p: "emptied" for p in (23, 28)},
               **{p: "empty" for p in (6, 19, 25, 31, 35, 40)}},
    "x6011": {1: "keep", 2: "keep", 3: "emptied", 4: "emptied", 5: "emptied", 6: "emptied", 7: "moved", 8: "empty"},
    "x6011_note": "`1` and `2` stay; `8` stays empty",
    "halos": (),
    # cards: (chips, title, move, line 2); chips are (pin, state); 6 per column, by cavity number
    "cards": [
        ([(1, "moved")], "Charge lamp", "move 4", "empty → `0.35 BL` from body `X6011` pin `4`"),
        ([(2, "moved")], "Start feedback (terminal 30h)", "move 6", "empty → `0.35 SW/GN` from body `X6011` pin `6`"),
        ([(5, "new")], "DME ground, recommended", "move 8", "empty → new `0.35 BR/SW` to ground point `X1108`"),
        ([(6, "empty")], "Stays empty", "", "older charts put the start feedback here; it goes in `2`"),
        ([(11, "moved")], "Oil-pressure lamp", "move 3", "empty → `0.35 BR/GN` from body `X6011` pin `3`"),
        ([(15, "new")], "Sport button, optional", "move 9", "empty → new `0.35 SW/RT/GE` from `X1869` pin `17`"),
        ([(16, "new")], "Sport LED, optional", "move 9", "empty → new `0.35 SW/GR/GE` to `X1869` pin `18`"),
        ([(18, "moved")], "Leak-test heater", "move 1", "empty → `0.75 SW/RT` from body `X6011` pin `7`"),
        ([(21, "moved")], "Oil level", "move 5", "empty → `0.5 WS/GN` from body `X6011` pin `5`"),
        ([(23, "emptied")], "Clutch", "move 2", "`0.35 BL/BR` → empty: the wire goes to body `X6011` pin `7`"),
        ([(28, "emptied"), (34, "moved")], "Brake test contact", "move 7", "`0.35 BR/GR` moves from `28` to `34`"),
    ],
    "notes": [
        ("t-sm t-b fab-t", "Order: move 1 takes the heater wire out of body `X6011` pin `7` before move 2 puts the clutch wire in."),
        ("t-sm", "Every wire that moves between `X6011` and `X60004` needs a new terminal of the target's type, or a BMW repair lead."),
        ("t-sm", "No change: `10` (pump relay `K96`), `20` and `30` (leak-test pump: test before you swap). Move 10: fit the M3 clutch module `61319122700`."),
        ("t-sm", "`X60001`, `X60002`, `X60003` and `X60005` number the other way: right to left, with pin `1` at the bottom right."),
        ("t-sm", "Built before 09/2001? Body `X6011` pin `7` is empty and the leak-test module has no heater: see “Earlier MS43 Tourings” in the manual."),
    ],
    "aria": ("Pin map for an MS43 Touring built 09/2001 to 02/2003: connector views of the DME plug X60004, two blocks of "
             "two rows of ten with pin 1 at the bottom left, and the body side of the E-box plug X6011, two rows of four with "
             "5 above 1. Five wires move from X6011 into X60004: the oil-pressure lamp from 3 to 11, the charge lamp from 4 to 1, "
             "the oil level from 5 to 21, the start feedback from 6 to 2 and the leak-test heater from 7 to 18. Once the heater "
             "wire is out, the clutch wire moves from X60004 pin 23 into X6011 pin 7, and the brake test contact moves from 28 "
             "to 34. New wires go into 5, a ground to X1108 (recommended), and into 15 and 16 for the optional Sport button. "
             "X60004 pin 6 stays empty. Every moved wire needs a new terminal of the target's type."),
}

MS45 = {
    "key": "ms45",
    "file": "18-pinmap-ms45.svg",
    "title": "MS45.1 TOURING: X60004 AND BODY X6011",
    "sub": "For a Touring built from 03/2003 with the M54 and a manual gearbox.",
    "x60004": {**X4_KEEP,
               **{p: "moved" for p in (18, 34)},
               **{p: "new" for p in (1, 11, 16, 21)},
               **{p: "outnew" for p in (5, 15)},
               **{p: "emptied" for p in (2, 19, 23, 28)},
               **{p: "empty" for p in (6, 25, 31, 35, 40)}},
    "x6011": {1: "keep", 2: "keep", 3: "empty", 4: "empty", 5: "empty", 6: "emptied", 7: "moved", 8: "empty"},
    "x6011_note": "`1`, `2` stay; `6`: check for a wire",
    "halos": (2, 15),
    "cards": [
        ([(1, "new")], "Charge lamp", "move 8", "empty → new `0.35 BL` to cluster `X11175` pin `2`"),
        ([(2, "emptied")], "Heater out; start feedback if present", "moves 1, 10",
         "`0.75 SW/RT` → `18`; `0.35 SW/GN` from `X6011` pin `6` if present"),
        ([(5, "outnew")], "Sensor wire out; ground recommended", "moves 2, 11",
         "`0.5 SW/GE` out → new `0.35 BR/SW` to ground point `X1108`"),
        ([(6, "empty")], "Stays empty", "", "older charts put the start feedback here"),
        ([(11, "new")], "Oil-pressure lamp", "move 7", "empty → new `0.35 BR/GN` to cluster `X11175` pin `13`"),
        ([(15, "outnew")], "Sensor wire out; Sport optional", "moves 3, 12",
         "`0.5 SW/RT` out → new `0.35 SW/RT/GE` from `X1869` pin `17`"),
        ([(16, "new")], "Sport LED, optional", "move 12", "empty → new `0.35 SW/GR/GE` to `X1869` pin `18`"),
        ([(18, "moved")], "Leak-test heater", "move 1", "empty (check it) → `0.75 SW/RT` from pin `2`"),
        ([(19, "emptied")], "E-box fan wire, if present", "move 4", "`0.5 BR/OR` → empty: out and insulated"),
        ([(21, "new")], "Oil level", "move 9", "empty → new `0.5 WS/GN` to cluster `X11175` pin `17`"),
        ([(23, "emptied")], "Clutch", "move 6", "`0.35 BL/BR` → empty: to body `X6011` pin `7`, new terminal"),
        ([(28, "emptied"), (34, "moved")], "Brake test contact", "move 5", "`0.35 BR/GR` moves from `28` to `34`"),
    ],
    "warning": "Tag `2` and `15` before you pull them: both are SW/RT (0.75 mm² in `2`, 0.5 mm² in `15`).",
    "notes": [
        ("t-sm t-b fab-t", "Order: take the wires out of `5`, `15` and `19` first and insulate them; the heater leaves `2` before anything else goes in."),
        ("t-sm", "A wire that moves between `X6011` and `X60004` needs a new terminal of the target's type; body `X6011` has only pins `1` and `2` today."),
        ("t-sm", "Code the cluster's `CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN` and `TOG_UEBER_CAN` to `nicht_aktiv`."),
        ("t-sm", "No change: `10` (pump relay `K96`), `20` and `30` (leak-test pump: test before you swap). Move 13: fit the M3 clutch module `61319122700`."),
        ("t-sm", "`X60001`, `X60002`, `X60003` and `X60005` number the other way: right to left, with pin `1` at the bottom right."),
    ],
    "aria": ("Pin map for an MS45.1 Touring built from 03/2003, laid out like the MS43 map: connector views of the DME plug "
             "X60004 and the body side of the E-box plug X6011. The leak-test heater moves from X60004 pin 2 to 18 and the brake "
             "test contact from 28 to 34. The secondary-air sensor wires come out of 5 and 15, and the E-box fan wire out of 19 "
             "if there is one, and are insulated; tag 2 and 15 first, because both are black with red. The clutch wire moves from "
             "23 to X6011 pin 7 with a new terminal. New wires run from 11, 1 and 21 to cluster pins 13, 2 and 17, a new ground "
             "goes into 5, and the optional Sport wires into 15 and 16. The start feedback moves from X6011 pin 6 to X60004 pin 2 "
             "only if pin 6 holds a wire. X60004 pin 6 stays empty."),
}


# ---------------------------------------------------------------- lanes
# Levels (y) where lanes cross the space between the plugs. X60004 entry levels are fixed by the rows.
A_IN = ROWS["U2"] + CH / 2          # into 21 (left edge)
B_CH = ROWS["U2"] + CH + 17         # channel, upper lane (23 out)
C_CH = ROWS["L1"] - 17              # channel, lower lane (into 18)
D_IN = ROWS["L1"] + CH / 2          # into 11 (left edge) = X6011 row-gap level
E_IN = ROWS["L2"] + CH / 2          # into 1 (left edge)
GAP_L = ROWS["L1"] + CH + G / 2     # inside the lower block, between its rows
GAP_U = ROWS["U1"] + CH + G / 2     # inside the upper block, between its rows
YA, YB, YC = YX - 61, YX - 41, YX - 21      # lanes above X6011 (MS43)
XJ_C, XJ_B, XJ_A, XJ_E = 318, 334, 350, 342  # jog columns near X60004 (lower lanes jog first)
YF = ROWS["L2"] + CH + 40           # start-feedback lane under both plugs
XF = XX - 20                        # ... and down the left side of X6011
X7_IN, X7_OUT = x11(7)[0] + 6, x11(7)[0] + 20   # two wires at X6011 pin 7's face
LANE_X = XX + P * 3 + CW + 14       # where lane labels start (right of X6011)


def lanes_ms43(c):
    c.comment("Wires that move between body X6011 and X60004 (orange): no two cross")
    # 5 -> 21: oil level
    x5, _ = mid11(5)
    dot(c, x5, YX)
    c.path([(x5, YX), (x5, YA), (XJ_A, YA), (XJ_A, A_IN), (XC, A_IN)], "fab-s", end="ahf", sw=1.5)
    # 23 -> X6011 7: clutch
    x23, _ = mid4(23)
    dot(c, x23, ROWS["U2"] + CH)
    c.path([(x23, ROWS["U2"] + CH), (x23, B_CH), (XJ_B, B_CH), (XJ_B, YB), (X7_IN, YB), (X7_IN, YX)],
           "fab-s", end="ahf", sw=1.5)
    # X6011 7 -> 18: leak-test heater
    x18, _ = mid4(18)
    dot(c, X7_OUT, YX)
    c.path([(X7_OUT, YX), (X7_OUT, YC), (XJ_C, YC), (XJ_C, C_CH), (x18, C_CH), (x18, ROWS["L1"])],
           "fab-s", end="ahf", sw=1.5)
    # 3 -> 11: oil-pressure lamp (rises into X6011's row gap, then straight across)
    x3, y3 = x11(3)
    dot(c, x3 + CW / 2, y3)
    c.path([(x3 + CW / 2, y3), (x3 + CW / 2, D_IN), (XC, D_IN)], "fab-s", end="ahf", sw=1.5)
    # 4 -> 1: charge lamp (leaves X6011 pin 4's outer face)
    x4_, y4_ = x11(4)
    dot(c, x4_ + CW, y4_ + CH / 2)
    c.path([(x4_ + CW, y4_ + CH / 2), (XJ_E, y4_ + CH / 2), (XJ_E, E_IN), (XC, E_IN)], "fab-s", end="ahf", sw=1.5)
    # 6 -> 2: start feedback (round the left of X6011, under both plugs)
    lanes_start_feedback(c, dashed=False)
    c.text(LANE_X, YA - 5, "oil level · move 5", "t-sm")
    c.text(LANE_X, YB - 5, "clutch · move 2", "t-sm")
    c.text(LANE_X, YC - 5, "leak-test heater · move 1", "t-sm")
    c.text(LANE_X, D_IN - 5, "oil-pressure lamp · move 3", "t-sm")
    c.text(LANE_X, x11(4)[1] + CH / 2 - 5, "charge lamp · move 4", "t-sm")


def lanes_start_feedback(c, dashed):
    x6, y6 = x11(6)
    x2, _ = mid4(2)
    ys = y6 + CH + 5
    dot(c, x6 + CW / 2, y6 + CH)
    cls = "fab-s dash" if dashed else "fab-s"
    c.path([(x6 + CW / 2, y6 + CH), (x6 + CW / 2, ys), (XF, ys), (XF, YF), (x2, YF), (x2, ROWS["L2"] + CH)],
           cls, end="ahf", sw=1.5)
    label = "start feedback, if present · move 10" if dashed else "start feedback · move 6"
    c.text(LANE_X + 40, YF - 5, label, "t-sm")


def lanes_ms45(c):
    c.comment("Wires between body X6011 and X60004 (orange; dashed = only if your X6011 pin 6 holds a wire)")
    x23, _ = mid4(23)
    dot(c, x23, ROWS["U2"] + CH)
    c.path([(x23, ROWS["U2"] + CH), (x23, B_CH), (X7_IN + 7, B_CH), (X7_IN + 7, YX)], "fab-s", end="ahf", sw=1.5)
    c.text(LANE_X + 30, B_CH - 5, "clutch, new terminal · move 6", "t-sm")
    lanes_start_feedback(c, dashed=True)
    c.comment("New wires from X60004 to the cluster plug X11175 (green)")
    tip = 300
    for pin, y, lab, mv in ((21, A_IN, "cluster `X11175` pin `17`", "move 9"),
                            (11, D_IN, "cluster `X11175` pin `13`", "move 7"),
                            (1, E_IN, "cluster `X11175` pin `2`", "move 8")):
        dot(c, XC, y, "new-f")
        c.path([(XC, y), (tip, y)], "new-s", end="ahn", sw=1.5)
        c.text(tip - 5, y + 4, segs(lab), "t-sm", "end")
        c.text((tip + XC) / 2 + 2, y - 5, mv, "t-sm", "middle")


def internal_moves(c, ms45):
    c.comment("Moves inside X60004 (small arrowheads)")
    # 28 -> 34 through the upper block's row gap
    x28, _ = mid4(28)
    x34, _ = mid4(34)
    dot(c, x28, ROWS["U2"])
    c.path([(x28, ROWS["U2"]), (x28, GAP_U), (x34, GAP_U), (x34, ROWS["U1"] + CH)], "fab-s", end="ahs", sw=1.5)
    if ms45:
        # 2 -> 18 through the lower block's row gap
        x2, _ = mid4(2)
        x18, _ = mid4(18)
        dot(c, x2 - 6, ROWS["L2"])
        c.path([(x2 - 6, ROWS["L2"]), (x2 - 6, GAP_L), (x18, GAP_L), (x18, ROWS["L1"] + CH)], "fab-s", end="ahs", sw=1.5)


# ---------------------------------------------------------------- whole figure
CARD_PITCH = 32


def build(d):
    c = Canvas()
    ms43 = d["key"] == "ms43"

    c.comment("Title, scope, viewing-side caveat and the wire-color key")
    c.text(12, 22, d["title"], "t-h")
    c.text(12, 40, d["sub"], "t-sm")
    c.text(12, 56, "Cavity numbers as moulded on the housing; WDS doesn't state the viewing side.", "t-sm")
    c.text(12, 76, "Wire colors: SW black, WS white, RT red, GN green, BL blue,", "t-sm")
    c.text(12, 91, "BR brown, GE yellow, GR gray, VI violet, OR orange.", "t-sm")
    c.text(12, 106, "0.35 BR/GR = 0.35 mm², brown with a gray tracer.", "t-sm")

    c.comment("Legend")
    lx, ly = 470, 4
    items = [("moved", "moved here"), ("new", "new wire"), ("emptied", "emptied"),
             ("keep", "unchanged"), ("empty", "empty")]
    if not ms43:
        items.append(("outnew", "out, then new"))
    for i, (st, lab) in enumerate(items):
        col, row = i % 3, i // 3
        x, y = lx + col * 108, ly + row * 20
        cavity(c, x + 2, y + 3, "", st, w=22, h=14)
        c.text(x + 31, y + 14, lab, "t-sm")
    y = ly + 40
    dot(c, lx + 4, y + 10)
    c.line(lx + 4, y + 10, lx + 25, y + 10, "fab-s", sw=1.5, end="ahf")
    c.text(lx + 31, y + 14, "a wire moves", "t-sm")
    if not ms43:
        c.rect(lx + 108 + 2, y + 3, 22, 14, "warn-f", rx=4, sw=1.5)
        c.text(lx + 108 + 31, y + 14, "tag it first", "t-sm")

    c.comment("X60004: two blocks of two rows of ten; pin 1 at the bottom left, rows run left to right")
    c.text(XC - 8, YT - 16, [("X60004", "t-mono"), " DME plug (body harness)"], "t t-b")
    for top, bot, name in ((ROWS["U1"], ROWS["U2"] + CH, "upper block"), (ROWS["L1"], ROWS["L2"] + CH, "lower block")):
        c.rect(XC - 8, top - 8, P * 9 + CW + 16, bot - top + 16, "panel", rx=6)
        c.text(XC + P * 9 + CW + 18, (top + bot) / 2 + 4, name, "t-sm")
    for h in d["halos"]:
        halo(c, *x4(h))
    for pin in range(1, 41):
        cavity(c, *x4(pin), str(pin), d["x60004"][pin])

    c.comment("Body X6011: two rows of four, 5 next to 1")
    c.rect(XX - 8, YX - 8, P * 3 + CW + 16, CH * 2 + XGAP + 16, "panel", rx=6)
    for pin in range(1, 9):
        cavity(c, *x11(pin), str(pin), d["x6011"][pin])
    by = YX + 2 * CH + XGAP + 8
    c.text(XX - 8, by + 16, [("X6011", "t-mono"), " body side (E-box)"], "t t-b")
    c.text(XX - 8, by + 31, segs(d["x6011_note"]), "t-sm")

    if ms43:
        lanes_ms43(c)
    else:
        lanes_ms45(c)
    internal_moves(c, not ms43)

    c.comment("Pin 6 stays empty")
    x6, y6 = x4(6)
    c.path([(x6 + CW / 2, y6 + CH), (x6 + CW / 2, y6 + CH + 20)], "crit-s", sw=1.5)
    c.text(x6 + CW / 2 + 6, y6 + CH + 21, segs("`6` stays empty"), "t-sm t-b crit-t")

    c.comment("Change cards: every X60004 cavity that changes, before -> after")
    cy0 = YF + 18
    c.line(12, cy0 - 8, W - 12, cy0 - 8, "ln-faint")
    for i, (chips, title, move, l2) in enumerate(d["cards"]):
        col, row = i // 6, i % 6
        x, y = 12 + col * 394, cy0 + row * CARD_PITCH
        for j, (pin, st) in enumerate(chips):
            if pin in d["halos"]:
                halo(c, x + j * 30, y)
            cavity(c, x + j * 30, y, str(pin), st)
        tx = x + 30 * len(chips) + 8
        crit = title == "Stays empty"
        head = [title] + ([("  " + move, "t-sm")] if move else [])
        c.text(tx, y + 11, head, "t t-b crit-t" if crit else "t t-b")
        c.text(tx, y + 25, segs(l2), "t-sm")

    c.comment("Notes")
    ny = cy0 + 6 * CARD_PITCH + 14
    c.line(12, ny - 16, W - 12, ny - 16, "ln-faint")
    if not ms43:
        c.rect(8, ny - 8, W - 16, 19, "warn-f", rx=4, sw=1.5)
        c.text(14, ny + 6, segs(d["warning"]), "t-sm t-b")
        ny += 22
    for k, (cls, s_) in enumerate(d["notes"]):
        c.text(12, ny + 6 + k * 15, segs(s_), cls)
    d["height"] = int(ny + 6 + (len(d["notes"]) - 1) * 15 + 14)

    markers = [marker("ahf", "fab-f"), marker("ahn", "new-f"), marker("ahs", "fab-f", 4.5)]
    return c, markers


def main():
    for d in (MS43, MS45):
        c, markers = build(d)
        print(write(d["file"], c.svg(W, d["height"], d["aria"], markers)), d["height"])


if __name__ == "__main__":
    main()
