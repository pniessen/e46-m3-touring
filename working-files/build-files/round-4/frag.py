#!/usr/bin/env python3
"""Split the guide's Markdown pages into section fragments, or join them back.

usage:
  frag.py split GUIDE_DIR FRAG_DIR      one folder per page, one file per H2/H3 section (H2 only for JOB-CARDS)
  frag.py join  FRAG_DIR GUIDE_DIR      concatenate each page's fragments in file-name order
  frag.py check FRAG_DIR GUIDE_DIR      report which pages differ from their joined fragments
  frag.py owners FRAG_DIR               print the ownership manifest (FRAG_DIR/owners.tsv)
Fragment names: NNNN__slug.md. NNNN steps by 10, so a section added later can slot in between.
"""
import pathlib, re, sys

PAGES = {"README.md": 3, "WIRING-AND-CODING.md": 3, "JOB-CARDS.md": 2, "WORKSHEETS.md": 3}

def chunks(text, maxlevel):
    out, cur, fence = [], [], False
    head = re.compile(r"#{2,%d} \S" % maxlevel)
    for line in text.splitlines(keepends=True):
        if line.lstrip().startswith(("```", "~~~")):
            fence = not fence
        if not fence and head.match(line) and cur:
            out.append("".join(cur)); cur = []
        cur.append(line)
    if cur:
        out.append("".join(cur))
    return out

def slug(chunk):
    first = chunk.split("\n", 1)[0]
    if not first.startswith("##"):
        return "preamble"
    s = re.sub(r"[^a-z0-9]+", "-", first.lstrip("#").strip().lower()).strip("-")
    return s[:60].rstrip("-")

def joined(folder):
    return "".join(f.read_text(encoding="utf-8") for f in sorted(folder.glob("[0-9][0-9][0-9][0-9]__*.md")))

def main():
    cmd = sys.argv[1]
    if cmd == "split":
        guide, frag = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
        for page, level in PAGES.items():
            folder = frag / page[:-3]
            if folder.exists():
                sys.exit(f"{folder} exists; refusing to overwrite")
            folder.mkdir(parents=True)
            text = (guide / page).read_text(encoding="utf-8")
            parts = chunks(text, level)
            for i, c in enumerate(parts):
                (folder / f"{i*10:04d}__{slug(c)}.md").write_text(c, encoding="utf-8")
            assert joined(folder) == text, page
            print(page, len(parts), "fragments")
    elif cmd in ("join", "check"):
        frag, guide = pathlib.Path(sys.argv[2]), pathlib.Path(sys.argv[3])
        for page in PAGES:
            new = joined(frag / page[:-3])
            old = (guide / page).read_text(encoding="utf-8")
            if cmd == "join":
                if new != old:
                    (guide / page).write_text(new, encoding="utf-8")
                print(page, "written" if new != old else "unchanged")
            else:
                print(page, "same" if new == old else "differs")
    elif cmd == "owners":
        print((pathlib.Path(sys.argv[2]) / "owners.tsv").read_text(encoding="utf-8"))

if __name__ == "__main__":
    main()
