import pathlib, sys
ROOT = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion")
sys.path.insert(0, str(ROOT / "tools"))
import build_html
here = pathlib.Path(__file__).resolve().parent
md = (ROOT / "README.md").read_text(encoding="utf-8")
cap_dir = pathlib.Path("/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/foldin/diagrams")
for name in ["cargo-floor-plates", "build-timeline"]:
    insert, placeholder = (cap_dir / f"{name}.caption.md").read_text(encoding="utf-8").split("\n---\n")
    placeholder = placeholder.strip()
    assert md.count(placeholder) == 1, (name, md.count(placeholder))
    md = md.replace(placeholder, insert.strip())
(here / "e2e" / "README.md").write_text(md, encoding="utf-8")
html = build_html.build_page(here / "e2e" / "README.md", standalone=True, photo_mode="omit")
fonts = f'<link rel="stylesheet" href="{here / "fonts" / "fonts.css"}">\n'
html = html.replace("<title>", fonts + "<title>", 1)
(here / "e2e" / "page.html").write_text(html, encoding="utf-8")
print("ok", len(html))
