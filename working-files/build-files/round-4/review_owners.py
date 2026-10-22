"""Write review-owners.tsv: every fragment mapped to a reviewer. Run after all writers and integrators finish."""
import csv, pathlib, re
R = pathlib.Path("/tmp/claude-0/-home-user/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/r4fold")
writer = {}
for row in csv.reader((R / "frags/owners.tsv").read_text().splitlines()[1:], delimiter="\t"):
    writer[(row[0], row[1])] = row[3]
DIGIT = {"1": "coding-body", "2": "coding-power", "3": "arches", "4": "floor", "5": "susp", "6": "fuel", "7": "front", "8": "cool", "9": "xi"}
TOPIC = {"susp": "rv-chassis", "front": "rv-chassis", "fuel": "rv-fluids", "cool": "rv-fluids", "arches": "rv-body",
         "floor": "rv-body", "coding-power": "rv-coding", "coding-body": "rv-coding", "xi": "rv-plan"}
rows = ["page\tfile\theading\treviewer"]
for page in ("README", "WIRING-AND-CODING", "JOB-CARDS", "WORKSHEETS"):
    for f in sorted((R / "frags" / page).glob("[0-9][0-9][0-9][0-9]__*.md")):
        first = f.read_text(encoding="utf-8").split("\n", 1)[0]
        num = int(f.name[:4])
        key = (page, f.name)
        w = writer[key] if key in writer else DIGIT.get(f.name[3], "integrator")
        if page == "README" and f.name.startswith("0050__"):
            w = "xi"
        if w != "integrator":
            rv = TOPIC[w]
        elif page == "README":
            rv = "rv-plan" if num < 870 else "rv-ref"     # Appendix (torque 0870 onward) and back matter go to rv-ref
            if 770 <= num < 870:                          # Sources
                rv = "rv-ref"
        else:
            rv = "rv-ref"                                 # shared cards, worksheet logs, WIRING preamble and power-up checks
        rows.append(f"{page}\t{f.name}\t{first if first.startswith('#') else '(preamble)'}\t{rv}")
(R / "review-owners.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
from collections import Counter
print(Counter(r.split("\t")[3] for r in rows[1:]))
