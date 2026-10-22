#!/usr/bin/env python3
"""Mirror the guide folder into a clone of pniessen/e46-m3-touring and build the site into docs/.

    python3 sync_repo.py /path/to/e46-m3-touring-clone

Copies every tracked-worthy file from /home/user/archeyon/e46-m3-touring-conversion (no caches),
removes files in the clone that no longer exist in the source (except .git, docs/ and working-files/,
which lives only in the public repository), then rebuilds docs/ from scratch with tools/build_site.py.
"""
import pathlib
import shutil
import subprocess
import sys

SRC = pathlib.Path("/home/user/archeyon/e46-m3-touring-conversion")
SKIP_DIRS = {".git", "docs", "__pycache__", "working-files"}

dst = pathlib.Path(sys.argv[1]).resolve()
assert (dst / ".git").is_dir(), f"{dst} is not a git clone"


def wanted(rel: pathlib.Path) -> bool:
    return not any(part in SKIP_DIRS for part in rel.parts)


src_files = {p.relative_to(SRC) for p in SRC.rglob("*") if p.is_file() and wanted(p.relative_to(SRC))}
for rel in sorted(src_files):
    (dst / rel).parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(SRC / rel, dst / rel)
removed = []
for p in sorted(dst.rglob("*")):
    rel = p.relative_to(dst)
    if p.is_file() and wanted(rel) and rel not in src_files:
        p.unlink()
        removed.append(str(rel))
if (dst / "docs").exists():
    shutil.rmtree(dst / "docs")
subprocess.run([sys.executable, "-B", "tools/build_site.py", "docs"], cwd=dst, check=True)
print(f"copied {len(src_files)} files; removed {removed or 'nothing'}; docs/ rebuilt")
