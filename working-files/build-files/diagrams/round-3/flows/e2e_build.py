"""Build the wiring manual with my figures folded in (a scratch copy), the way the site builds it."""
import pathlib, re, shutil, sys
sys.dont_write_bytecode = True
ROOT = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion")
CAP = pathlib.Path("/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/foldin/diagrams")
OUT = pathlib.Path(__file__).resolve().parent / "e2e"
sys.path.insert(0, str(ROOT / "tools"))
from build_html import build_page  # noqa: E402

def snippet(name):
    head = CAP.joinpath(name + ".caption.md").read_text().split("\n---\n")[0].strip()
    return head

md = (ROOT / "WIRING-AND-CODING.md").read_text()
for name in ("flow-which-dme", "flow-power-up", "flow-no-start", "flow-no-start-2", "flow-warning-lights"):
    ph = f"<!-- figure: {name} -->"
    assert md.count(ph) == 1, name
    md = md.replace(ph, snippet(name))
anchor = "**Step 19.** Disconnect the battery again."
assert md.count(anchor) == 1
md = md.replace(anchor, snippet("flow-power-up-2") + "\n\n" + anchor)
(OUT / "WIRING-AND-CODING.md").write_text(md)
d = OUT / "diagrams"
if d.exists():
    shutil.rmtree(d)
shutil.copytree(ROOT / "diagrams", d)
page = build_page(OUT / "WIRING-AND-CODING.md", standalone=True, title="Wiring and coding manual", photo_mode="omit",
                  page_key="wiring")
(OUT / "wiring.html").write_text(page)
print("built", OUT / "wiring.html", len(page))
