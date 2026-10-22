"""Shared bits for the diagram generators: the house <style> block (copied verbatim from
diagrams/04-fuel-pressure.svg), the root element, defs and background."""
import pathlib
import re
from xml.sax.saxutils import escape

DIAGRAMS = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion/diagrams")
_src = (pathlib.Path(__file__).resolve().parent / "orig" / "04-fuel-pressure.svg").read_text(encoding="utf-8")
STYLE = re.search(r"<style>.*?</style>", _src, re.S).group(0)

AH = ('  <marker id="ah" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" '
      'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="fill-fg"/></marker>')


def marker(mid: str, cls: str) -> str:
    return (f'  <marker id="{mid}" viewBox="0 0 8 8" refX="7.5" refY="4" markerWidth="7" markerHeight="7" '
            f'orient="auto-start-reverse"><path d="M0,0 L8,4 L0,8 Z" class="{cls}"/></marker>')


def svg_open(height: int, aria: str, extra_markers=()) -> str:
    defs = "\n".join([AH, *extra_markers])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 {height}" role="img" '
            f'aria-label="{escape(aria, {chr(34): "&quot;"})}" color="#1b2128">\n{STYLE}\n<defs>\n{defs}\n</defs>\n'
            f'<rect class="bg" x="0" y="0" width="400" height="{height}" fill="#ffffff"/>\n')


def t(cls: str, x, y, s: str, anchor: str = None) -> str:
    a = f' text-anchor="{anchor}"' if anchor else ""
    return f'<text class="{cls}" x="{fmt(x)}" y="{fmt(y)}"{a}>{escape(s)}</text>'


def fmt(v) -> str:
    return (f"{v:.1f}".rstrip("0").rstrip(".")) if isinstance(v, float) else str(v)


def write(name: str, body: str) -> pathlib.Path:
    p = DIAGRAMS / name
    p.write_text(body if body.endswith("\n") else body + "\n", encoding="utf-8")
    return p
