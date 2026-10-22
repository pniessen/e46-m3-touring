#!/usr/bin/env python3
"""Generate the two connector pin maps (landscape, 800 wide):

    17-pinmap-ms43.svg   MS43 Touring (09/2001 to 02/2003)
    18-pinmap-ms45.svg   MS45.1 Touring (from 03/2003)

Both share one layout (same scale, positions, legend and card grid) so a reader can compare them.
Data: scratchpad/foldin/wiring-canonical.md sections 2-4 and WIRING-AND-CODING.md (the move tables).
Text in backticks is set in t-mono (pins, wire codes, connector names, part numbers, coding names).
Move numbers are written "#n", as in the manual's tables, so they can't be read as cavity numbers.
"""
import sys

sys.dont_write_bytecode = True
from pmkit import Canvas, marker, write  # noqa: E402

W = 800

# ---------------------------------------------------------------- geometry
P, CW, CH = 30, 26, 22          # cavity pitch, width, height
G = 20                          # gap between the two rows of a block (in-plug moves run here)
CHAN = 56                       # channel between the upper and lower block (two lanes run in it)
YT = 116                        # top of X60004's top row (31-40)
XC = 372                        # left edge of X60004 column 1
ROWS = {                        # X60004 row tops, as WDS draws it: 1-10 at the bottom, left to right
    "U1": YT, "U2": YT + CH + G,                                     # upper block: 31-40 over 21-30
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


def segs(s):
    """'empty → `0.35 BL` from ...' -> list of str / (str, 't-mono') for Canvas.text."""
    out = []
    for i, part in enumerate(s.split("`")):
        if part:
            out.append((part, "t-mono") if i % 2 else part)
    return out


# ---------------------------------------------------------------- cavity styles
# keep      unchanged (gray)            empty      never used (white, thin outline)
# moved     a moved wire goes in        new        a new wire goes in (required)
# newrec    new wire, recommended       newopt     new wire, optional
# emptied   its wire leaves             ifpresent  its wire leaves, only if there is one (dotted)
# outrec / outopt   the old wire comes out first (dashed ring), then a recommended / optional new one
# tag=True  amber fill inside the outline: tag this wire before you pull it
class _NoText:
    def __init__(self, c):
        self.c = c

    def rect(self, *a, **k):
        self.c.rect(*a, **k)

    def text(self, *a, **k):
        pass


def cavity(c, x, y, num, state, w=CW, h=CH, tag=False):
    if not num:
        c = _NoText(c)
    big, small = "t t-b t-mono", "t-sm t-mono"
    ty = y + h / 2 + 4.5
    if state in ("outrec", "outopt"):
        c.rect(x - 3, y - 3, w + 6, h + 6, "fab-s dash", rx=4, sw=1.5)
        state = "newrec" if state == "outrec" else "newopt"
    if tag:
        c.rect(x, y, w, h, "warn-f", rx=3, sw=1.5)
    if state == "keep":
        c.rect(x, y, w, h, "keep", rx=3, sw=1.5)
        c.text(x + w / 2, y + h / 2 + 4, num, small, "middle")
    elif state == "empty":
        c.rect(x, y, w, h, "fill-bg", rx=3)
        c.rect(x, y, w, h, "ln-thin", rx=3)
        c.text(x + w / 2, y + h / 2 + 4, num, small, "middle")
    elif state == "moved":
        c.rect(x, y, w, h, "fab", rx=3, sw=1.5)
        c.text(x + w / 2, ty, num, big, "middle")
    elif state == "new":
        c.rect(x, y, w, h, "new", rx=3, sw=1.5)
        c.text(x + w / 2, ty, num, big, "middle")
    elif state == "newrec":
        c.rect(x, y, w, h, "new dash", rx=3, sw=1.5)
        c.text(x + w / 2, ty, num, big, "middle")
    elif state == "newopt":
        if not tag:
            c.rect(x, y, w, h, "fill-bg", rx=3)
        c.rect(x, y, w, h, "new-s dash", rx=3, sw=1.5)
        c.text(x + w / 2, ty, num, big, "middle")
    elif state == "emptied":
        if not tag:
            c.rect(x, y, w, h, "fill-bg", rx=3)
        c.rect(x, y, w, h, "fab-s dash", rx=3, sw=1.5)
        c.text(x + w / 2, ty, num, big, "middle")
    elif state == "ifpresent":
        c.rect(x, y, w, h, "fill-bg", rx=3)
        c.rect(x, y, w, h, "fab-s", rx=3, sw=1.8, dots=True)
        c.text(x + w / 2, ty, num, big, "middle")
    else:
        raise ValueError(state)


def dot(c, x, y, cls="fab-f"):
    c.circle(x, y, 2.5, cls)


def tag_on_line(c, xm, y, label):
    """A small label sitting on an in-plug move line, on a surface-colored patch."""
    wpx = 5.6 * len(label) + 8
    c.rect(xm - wpx / 2, y - 7, wpx, 14, "fill-bg", rx=3)
    c.text(xm, y + 4, segs(label), "t-sm", "middle")


# ---------------------------------------------------------------- data
X4_KEEP = {p: "keep" for p in range(1, 41)}
VIEW_NOTE = ["Layout as WDS draws it. WDS doesn't say which face that is,",
             "so your plug may look mirrored: find each cavity by the number",
             "moulded on the housing, never by counting positions in this",
             "drawing."]
KEY = ["Wire colors: SW black, WS white, RT red, GN green, BL blue, BR brown, GE yellow, GR gray, VI violet, OR orange.",
       "0.35 BR/GR = 0.35 mm², brown with a gray tracer."]
CODING = "Code the cluster's `CAN_OELDRUCKSCHALTER`, `GENERATOR_UEBER_CAN` and `TOG_UEBER_CAN` to `nicht_aktiv`."
NO_CHANGE = "No change: pin `10` (pump relay `K96`); pins `20` and `30` (leak-test pump: test before your Touring's DME comes out)."

MS43 = {
    "key": "ms43",
    "file": "17-pinmap-ms43.svg",
    "title": "MS43 TOURING: X60004 AND BODY X6011",
    "sub": ["For a Touring built 09/2001 to 02/2003, with an M3 donor built from 09/2001."],
    "x60004": {**X4_KEEP,
               **{p: "moved" for p in (1, 2, 11, 18, 21, 34)},
               5: "newrec", 15: "newopt", 16: "newopt",
               **{p: "emptied" for p in (23, 28)},
               **{p: "empty" for p in (6, 19, 25, 31, 35, 40)}},
    "x6011": {1: "keep", 2: "keep", 3: "emptied", 4: "emptied", 5: "emptied", 6: "emptied", 7: "moved", 8: "empty"},
    "x6011_note": ["`1` and `2` stay; `8` stays empty", "`7`: heater out, then clutch in"],
    "tags": (),
    # cards: (chips, title, move, line 2); chips are (pin, state); 6 per column, by cavity number
    "cards": [
        ([(1, "moved")], "Charge lamp", "#4", "empty → `0.35 BL` from body `X6011` pin `4`"),
        ([(2, "moved")], "Start feedback (terminal 30h)", "#6", "empty → `0.35 SW/GN` from body `X6011` pin `6`"),
        ([(5, "newrec")], "DME ground, recommended", "#8", "empty → new `0.35 BR/SW` to ground point `X1108`"),
        ([(6, "empty")], "Stays empty", "", "a forum mapping put the start feedback here; it goes in `2`"),
        ([(11, "moved")], "Oil-pressure lamp", "#3", "empty → `0.35 BR/GN` from body `X6011` pin `3`"),
        ([(15, "newopt")], "Sport button, optional", "#9", "empty → new `0.35 SW/RT/GE` from `X1869` pin `17`"),
        ([(16, "newopt")], "Sport LED, optional", "#9", "empty → new `0.35 SW/GR/GE` to `X1869` pin `18`"),
        ([(18, "moved")], "Leak-test heater", "#1", "empty → `0.75 SW/RT` from body `X6011` pin `7`"),
        ([(21, "moved")], "Oil level", "#5", "empty → `0.5 WS/GN` from body `X6011` pin `5`"),
        ([(23, "emptied")], "Clutch", "#2", "`0.35 BL/BR` → empty: the wire goes to body `X6011` pin `7`"),
        ([(28, "emptied"), (34, "moved")], "Brake test contact", "#7", "`0.35 BR/GR` moves from `28` to `34`"),
        ([], "Clutch module", "#10", "fit the M3's `61319122700` in place of `61319231129`"),
    ],
    "notes": [
        ("t-sm t-b fab-t", "Order: move #1 takes the heater wire out of body `X6011` pin `7` before move #2 puts the clutch wire in."),
        ("t-sm", "Every wire that moves between `X6011` and `X60004` needs a new terminal of the target's type, or a BMW repair lead."),
        ("t-sm", CODING),
        ("t-sm", NO_CHANGE),
        ("t-sm", "Built before 09/2001? Body `X6011` pin `7` is empty and the leak-test module has no heater: see “Earlier MS43 Tourings” in the manual."),
    ],
    "aria": ("Pin map for an MS43 Touring built 09/2001 to 02/2003, with an M3 donor built from 09/2001: the DME plug "
             "X60004, two blocks of two rows of ten, and the body side of the E-box plug X6011, two rows of four, laid out "
             "as WDS draws them. WDS doesn't say which face that is, so your plug may look mirrored: find each cavity by "
             "the number moulded on the housing, never by counting positions in the drawing. Five wires move from X6011 "
             "into X60004: the oil-pressure lamp from 3 to 11, the charge lamp from 4 to 1, the oil level from 5 to 21, "
             "the start feedback from 6 to 2 and the leak-test heater from 7 to 18. Once the heater wire is out, the clutch "
             "wire moves from X60004 pin 23 into X6011 pin 7, and the brake test contact moves from 28 to 34. New wires go "
             "into 5, a ground to X1108 (recommended), and into 15 and 16 for the optional Sport button. X60004 pin 6 stays "
             "empty. Every wire that moves between X6011 and X60004 needs a new terminal of the target's type, or a BMW "
             "repair lead, and the cluster's three lamp switches are coded to nicht_aktiv."),
}

MS45 = {
    "key": "ms45",
    "file": "18-pinmap-ms45.svg",
    "title": "MS45.1 TOURING: X60004 AND BODY X6011",
    "sub": ["For a Touring built from 03/2003 with the M54 and a manual gearbox,", "with an M3 donor built from 09/2001."],
    "x60004": {**X4_KEEP,
               **{p: "moved" for p in (18, 34)},
               **{p: "new" for p in (1, 11, 21)},
               16: "newopt", 5: "outrec", 15: "outopt", 19: "ifpresent",
               **{p: "emptied" for p in (2, 23, 28)},
               **{p: "empty" for p in (6, 25, 31, 35, 40)}},
    "x6011": {1: "keep", 2: "keep", 3: "empty", 4: "empty", 5: "empty", 6: "ifpresent", 7: "moved", 8: "empty"},
    "x6011_note": ["`1` and `2` stay; `8` stays empty", "`6`: check for a wire"],
    "tags": (2, 15),
    "cards": [
        ([(1, "new")], "Charge lamp", "#8", "empty → new `0.35 BL` to cluster `X11175` pin `2`"),
        ([(2, "emptied")], "Heater out; start feedback only if present", "#1, #10",
         "`0.75 SW/RT` → `18`, then `0.35 SW/GN` from body `X6011` pin `6`"),
        ([(5, "outrec")], "Sensor wire out; ground recommended", "#2, #11",
         "`0.5 SW/GE` out → new `0.35 BR/SW` to ground point `X1108`"),
        ([(6, "empty")], "Stays empty", "", "a forum mapping put the start feedback here; it goes in `2`"),
        ([(11, "new")], "Oil-pressure lamp", "#7", "empty → new `0.35 BR/GN` to cluster `X11175` pin `13`"),
        ([(15, "outopt")], "Sensor wire out; Sport optional", "#3, #12",
         "`0.5 SW/RT` out → new `0.35 SW/RT/GE` from `X1869` pin `17`"),
        ([(16, "newopt")], "Sport LED, optional", "#12", "empty → new `0.35 SW/GR/GE` to `X1869` pin `18`"),
        ([(18, "moved")], "Leak-test heater", "#1", "empty (check it) → `0.75 SW/RT` from pin `2`"),
        ([(19, "ifpresent")], "E-box fan wire, if fitted", "#4", "`0.5 BR/OR` → empty: out and insulated"),
        ([(21, "new")], "Oil level", "#9", "empty → new `0.5 WS/GN` to cluster `X11175` pin `17`"),
        ([(23, "emptied")], "Clutch", "#6", "`0.35 BL/BR` → empty: to body `X6011` pin `7`, new terminal"),
        ([(28, "emptied"), (34, "moved")], "Brake test contact", "#5", "`0.35 BR/GR` moves from `28` to `34`"),
    ],
    "warning": "Tag `2` and `15` before you pull them: both are SW/RT (0.75 mm² in `2`, 0.5 mm² in `15`).",
    "notes": [
        ("t-sm t-b fab-t", "Order: take the wires out of `5`, `15` and (if fitted) `19` first and insulate them; the heater leaves `2` before anything else goes in."),
        ("t-sm", "A wire that moves between `X6011` and `X60004` needs a new terminal of the target's type; body `X6011` pin `7` is empty today."),
        ("t-sm", CODING),
        ("t-sm", NO_CHANGE),
        ("t-sm", "Move #13: fit the M3 clutch module `61319122700` in place of `61319231129`."),
    ],
    "aria": ("Pin map for an MS45.1 Touring built from 03/2003 with the M54 and a manual gearbox, with an M3 donor built "
             "from 09/2001, laid out like the MS43 map: the DME plug X60004 and the body side of the E-box plug X6011 as "
             "WDS draws them. WDS doesn't say which face that is, so your plug may look mirrored: find each cavity by the "
             "number moulded on the housing, never by counting positions in the drawing. The secondary-air sensor wires "
             "come out of 5 and 15, and the E-box fan wire out of 19 if there is one, and are insulated; tag 2 and 15 "
             "first, because both are black with red. The leak-test heater moves from X60004 pin 2 to 18 and the brake test "
             "contact from 28 to 34. The clutch wire moves from 23 to X6011 pin 7 with a new terminal. New wires run from "
             "11, 1 and 21 to cluster pins 13, 2 and 17, a new ground (recommended) goes into 5, and the optional Sport "
             "wires into 15 and 16. The start feedback moves from X6011 pin 6 to X60004 pin 2, with a new terminal, only "
             "if pin 6 holds a wire. X60004 pin 6 stays empty, and the cluster's three lamp switches are coded to "
             "nicht_aktiv."),
}


# ---------------------------------------------------------------- lanes
A_IN = ROWS["U2"] + CH / 2          # into 21 (left edge)
B_CH = ROWS["U2"] + CH + 17         # channel, upper lane (23 out)
C_CH = ROWS["L1"] - 17              # channel, lower lane (into 18)
D_IN = ROWS["L1"] + CH / 2          # into 11 (left edge) = X6011 row-gap level
E_IN = ROWS["L2"] + CH / 2          # into 1 (left edge)
GAP_L = ROWS["L1"] + CH + G / 2     # inside the lower block, between its rows
GAP_U = ROWS["U1"] + CH + G / 2     # inside the upper block, between its rows
YA, YB, YC = YX - 61, YX - 41, YX - 21      # lanes above X6011 (MS43)
XJ_C, XJ_B, XJ_A, XJ_E = 318, 334, 350, 342  # jog columns near X60004 (lower lanes jog first)
X6011_BOTTOM = YX + 2 * CH + XGAP + 8
YF = X6011_BOTTOM + 62              # start-feedback lane under both plugs
XF = XX - 20                        # ... and down the left side of X6011
X7_IN, X7_OUT = x11(7)[0] + 6, x11(7)[0] + 20   # two wires at X6011 pin 7's face
LANE_X = XX + P * 3 + CW + 14       # where lane labels start (right of X6011)
STUB_TIP = 318                      # MS45.1: where the new cluster wires end


def lanes_ms43(c):
    c.comment("Wires that move between body X6011 and X60004 (orange): no two cross")
    x5, _ = mid11(5)
    dot(c, x5, YX)
    c.path([(x5, YX), (x5, YA), (XJ_A, YA), (XJ_A, A_IN), (XC, A_IN)], "fab-s", end="ahf", sw=1.5)
    x23, _ = mid4(23)
    dot(c, x23, ROWS["U2"] + CH)
    c.path([(x23, ROWS["U2"] + CH), (x23, B_CH), (XJ_B, B_CH), (XJ_B, YB), (X7_IN, YB), (X7_IN, YX)],
           "fab-s", end="ahf", sw=1.5)
    x18, _ = mid4(18)
    dot(c, X7_OUT, YX)
    c.path([(X7_OUT, YX), (X7_OUT, YC), (XJ_C, YC), (XJ_C, C_CH), (x18, C_CH), (x18, ROWS["L1"])],
           "fab-s", end="ahf", sw=1.5)
    x3, y3 = x11(3)
    dot(c, x3 + CW / 2, y3)
    c.path([(x3 + CW / 2, y3), (x3 + CW / 2, D_IN), (XC, D_IN)], "fab-s", end="ahf", sw=1.5)
    x4_, y4_ = x11(4)
    dot(c, x4_ + CW, y4_ + CH / 2)
    c.path([(x4_ + CW, y4_ + CH / 2), (XJ_E, y4_ + CH / 2), (XJ_E, E_IN), (XC, E_IN)], "fab-s", end="ahf", sw=1.5)
    start_feedback(c, conditional=False)
    c.text(LANE_X, YA - 5, "oil level · #5", "t-sm")
    c.text(LANE_X, YB - 5, "clutch · #2", "t-sm")
    c.text(LANE_X, YC - 5, "leak-test heater · #1", "t-sm")
    c.text(LANE_X, D_IN - 5, "oil-pressure lamp · #3", "t-sm")
    c.text(LANE_X, x11(4)[1] + CH / 2 - 5, "charge lamp · #4", "t-sm")


def start_feedback(c, conditional):
    x6, y6 = x11(6)
    x2, _ = mid4(2)
    ys = y6 + CH + 5
    dot(c, x6 + CW / 2, y6 + CH)
    c.path([(x6 + CW / 2, y6 + CH), (x6 + CW / 2, ys), (XF, ys), (XF, YF), (x2, YF), (x2, ROWS["L2"] + CH)],
           "fab-s", end="ahf", sw=1.5 if not conditional else 1.8, dots=conditional)
    if conditional:
        c.text(LANE_X + 40, YF - 19, "start feedback, only if present:", "t-sm")
        c.text(LANE_X + 40, YF - 5, "new terminal · #10", "t-sm")
    else:
        c.text(LANE_X + 40, YF - 5, "start feedback · #6", "t-sm")


def lanes_ms45(c):
    c.comment("Wires between body X6011 and X60004 (orange; dotted = only if your X6011 pin 6 holds a wire)")
    x23, _ = mid4(23)
    dot(c, x23, ROWS["U2"] + CH)
    c.path([(x23, ROWS["U2"] + CH), (x23, B_CH), (X7_IN + 7, B_CH), (X7_IN + 7, YX)], "fab-s", end="ahf", sw=1.5)
    c.text(LANE_X + 40, B_CH - 5, "clutch, new terminal · #6", "t-sm")
    start_feedback(c, conditional=True)
    c.comment("New wires from X60004 to the cluster plug X11175 (green)")
    for pin, y, lab, mv in ((21, A_IN, "cluster `X11175` pin `17`", "#9"),
                            (11, D_IN, "cluster `X11175` pin `13`", "#7"),
                            (1, E_IN, "cluster `X11175` pin `2`", "#8")):
        dot(c, XC, y, "new-f")
        c.path([(XC, y), (STUB_TIP, y)], "new-s", end="ahn", sw=1.5)
        c.text(STUB_TIP - 5, y + 4, segs(lab), "t-sm", "end")
        c.text((STUB_TIP + XC) / 2 + 3, y - 5, mv, "t-sm", "middle")


def internal_moves(c, ms45):
    c.comment("Moves inside X60004 (small arrowheads), labelled on the line")
    x28, _ = mid4(28)
    x34, _ = mid4(34)
    dot(c, x28, ROWS["U2"])
    c.path([(x28, ROWS["U2"]), (x28, GAP_U), (x34, GAP_U), (x34, ROWS["U1"] + CH)], "fab-s", end="ahs", sw=1.5)
    tag_on_line(c, (x28 + x34) / 2, GAP_U, "brake · #5" if ms45 else "brake · #7")
    if ms45:
        x2, _ = mid4(2)
        x18, _ = mid4(18)
        dot(c, x2 - 6, ROWS["L2"])
        c.path([(x2 - 6, ROWS["L2"]), (x2 - 6, GAP_L), (x18, GAP_L), (x18, ROWS["L1"] + CH)], "fab-s", end="ahs", sw=1.5)
        tag_on_line(c, (x2 - 6 + x4(15)[0] - 3) / 2 + 1, GAP_L, "heater · #1")


# ---------------------------------------------------------------- whole figure
CARD_PITCH = 32
LEGEND_X = (439, 580, 688)


def legend(c, ms43):
    c.comment("Legend")
    items = {  # (col, row): (state or special, label); shared entries sit in the same place on both maps
        (0, 0): ("moved", "moved here"), (1, 0): ("new", "new wire"), (2, 0): ("emptied", "emptied"),
        (0, 1): ("newrec", "new, recommended"), (1, 1): ("newopt", "new, optional"),
        (0, 2): ("keep", "unchanged"), (1, 2): ("empty", "empty"),
        (1, 3): ("arrow", "a wire moves"),
    }
    if not ms43:
        items.update({(2, 1): ("ifpresent", "only if present"), (2, 2): ("tag", "tag it first"),
                      (0, 3): ("outring", "out, then rec./opt.")})
    for (col, row), (st, lab) in items.items():
        x, y = LEGEND_X[col], 4 + row * 20
        if st == "arrow":
            dot(c, x + 4, y + 10)
            c.line(x + 4, y + 10, x + 25, y + 10, "fab-s", sw=1.5, end="ahf")
        elif st == "outring":
            c.rect(x + 2 - 2.5, y + 3 - 2.5, 27, 19, "fab-s dash", rx=4, sw=1.5)
            c.rect(x + 2, y + 3, 22, 14, "fill-bg", rx=3)
            c.rect(x + 2, y + 3, 22, 14, "new-s dash", rx=3, sw=1.5)
        elif st == "tag":
            c.rect(x + 2, y + 3, 22, 14, "warn-f", rx=3, sw=1.5)
        else:
            cavity(c, x + 2, y + 3, "", st, w=22, h=14)
        c.text(x + 31, y + 14, lab, "t-sm")


def build(d):
    c = Canvas()
    ms43 = d["key"] == "ms43"

    c.comment("Title, scope and the viewing-side caution")
    c.text(12, 22, d["title"], "t-h")
    for i, line in enumerate(d["sub"]):
        c.text(12, 40 + 14 * i, line, "t-sm")
    by = 40 + 14 * (len(d["sub"]) - 1) + 9
    c.rect(8, by, 348, 14 * len(VIEW_NOTE) + 8, "warn-f", rx=4, sw=1.5)
    for i, line in enumerate(VIEW_NOTE):
        lead = "Layout as WDS draws it."
        content = [(lead, "t-b"), line[len(lead):]] if line.startswith(lead) else line
        c.text(14, by + 15 + 14 * i, content, "t-sm")
    legend(c, ms43)

    c.comment("X60004: two blocks of two rows of ten, as WDS draws them")
    c.text(XC - 8, YT - 16, [("X60004", "t-mono"), " DME plug (body harness)"], "t t-b")
    for top, bot, name in ((ROWS["U1"], ROWS["U2"] + CH, "upper block"), (ROWS["L1"], ROWS["L2"] + CH, "lower block")):
        c.rect(XC - 8, top - 8, P * 9 + CW + 16, bot - top + 16, "panel", rx=6)
        c.text(XC + P * 9 + CW + 18, (top + bot) / 2 + 4, name, "t-sm")
    for pin in range(1, 41):
        cavity(c, *x4(pin), str(pin), d["x60004"][pin], tag=pin in d["tags"])
    # X60001/2/3/5 note, under the lower block
    nx, ny0 = mid4(6)[0] + 13, ROWS["L2"] + CH + 26
    c.text(nx, ny0, segs("In WDS, `X60001`/`2`/`3`/`5` run the other way:"), "t-sm")
    c.text(nx, ny0 + 14, segs("pin `1` at the bottom right."), "t-sm")

    c.comment("Body X6011: two rows of four, 5 next to 1")
    c.rect(XX - 8, YX - 8, P * 3 + CW + 16, CH * 2 + XGAP + 16, "panel", rx=6)
    for pin in range(1, 9):
        cavity(c, *x11(pin), str(pin), d["x6011"][pin])
    c.text(XX - 8, X6011_BOTTOM + 16, [("X6011", "t-mono"), " body side (E-box)"], "t t-b")
    for i, line in enumerate(d["x6011_note"]):
        c.text(XX - 8, X6011_BOTTOM + 31 + 14 * i, segs(line), "t-sm")

    if ms43:
        lanes_ms43(c)
    else:
        lanes_ms45(c)
    internal_moves(c, not ms43)

    c.comment("X60004 pin 6 stays empty")
    x6, y6 = x4(6)
    c.path([(x6 + CW / 2, y6 + CH), (x6 + CW / 2, y6 + CH + 22)], "crit-s", sw=1.5)
    c.text(x6 + CW / 2 - 5, y6 + CH + 26, segs("`6` stays empty"), "t-sm t-b crit-t", "end")

    c.comment("Change cards: every X60004 cavity that changes, before -> after, with its move number")
    cy0 = YF + 18
    c.line(12, cy0 - 8, W - 12, cy0 - 8, "ln-faint")
    for i, (chips, title, move, l2) in enumerate(d["cards"]):
        col, row = i // 6, i % 6
        x, y = 12 + col * 394, cy0 + row * CARD_PITCH
        for j, (pin, st) in enumerate(chips):
            cavity(c, x + j * 30, y, str(pin), st, tag=pin in d["tags"])
        tx = x + 30 * max(1, len(chips)) + 8
        crit = title == "Stays empty"
        head = [title] + ([("  " + move, "t-sm")] if move else [])
        c.text(tx, y + 11, head, "t t-b crit-t" if crit else "t t-b")
        c.text(tx, y + 25, segs(l2), "t-sm")

    c.comment("Notes and the wire-color key")
    ny = cy0 + 6 * CARD_PITCH + 14
    c.line(12, ny - 16, W - 12, ny - 16, "ln-faint")
    if not ms43:
        c.rect(8, ny - 8, W - 16, 19, "warn-f", rx=4, sw=1.5)
        c.text(14, ny + 6, segs(d["warning"]), "t-sm t-b")
        ny += 22
    lines = d["notes"] + [("t-sm", k) for k in KEY]
    for k, (cls, s_) in enumerate(lines):
        c.text(12, ny + 6 + k * 15, segs(s_), cls)
    d["height"] = int(ny + 6 + (len(lines) - 1) * 15 + 14)

    markers = [marker("ahf", "fab-f"), marker("ahn", "new-f"), marker("ahs", "fab-f", 4.5)]
    return c, markers


def main():
    for d in (MS43, MS45):
        c, markers = build(d)
        print(write(d["file"], c.svg(W, d["height"], d["aria"], markers)), d["height"])


if __name__ == "__main__":
    main()
