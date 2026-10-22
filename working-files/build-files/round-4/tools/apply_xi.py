import sys, glob, os
sys.path.insert(0, os.path.dirname(__file__))
from parse_requests import parse
R = sys.argv[1]; only = set(sys.argv[2:])
B = parse(f"{R}/requests/xi.md")
def g(rid, i): return B[rid]['groups'][i][1]
def path(page, prefix):
    m = glob.glob(f"{R}/frags/{page}/{prefix}__*.md"); assert len(m) == 1, (page, prefix, m); return m[0]
def line_starting(text, start):
    ls = [l for l in text.split("\n") if l.startswith(start)]; assert len(ls) == 1, (start, len(ls)); return ls[0]
ops = {
 'R1': ('README','0080',[('rep',1,2)]), 'R2': ('README','0080',[('rep',1,2)]), 'R3': ('README','0080',[('rep',1,2)]),
 'R4': ('README','0080',[('row',1,2)]), 'R5': ('README','0080',[('rowstart','| Bry5on (',2)]),
 'R6': ('README','0810',[('rep',1,2)]), 'R7': ('README','0790',[('rep',1,2),('rep',3,4)]),
 'R8': ('README','0920',[('rep',1,2)]), 'R9': ('README','0120',[('para',1,2)]), 'R10': ('README','0130',[('rep',1,2)]),
 'R11': ('README','0310',[('rep',1,2)]), 'R12': ('README','0730',[('row',1,2),('rep',3,4)]), 'R13': ('README','0730',[('rep',1,2)]),
 'R14': ('README','0040',[('rep',1,2)]), 'R15': ('README','0100',[('rep',1,2)]), 'R17': ('README','0610',[('rep',1,2)]),
 'R18': ('README','0610',[('rep',1,2)]), 'R22': ('README','0870',[('row',1,2)]), 'R23': ('README','0880',[('rowstart','| Getrag 420G gearbox |',2)]),
 'R24': ('README','0190',[('rep',1,2)]),
 'R16': ('WIRING-AND-CODING','0090',[('rep',1,2)]), 'R19': ('WIRING-AND-CODING','0320',[('rep',1,2)]),
 'R20': ('WIRING-AND-CODING','0540',[('rep',1,2)]), 'R21': ('WIRING-AND-CODING','0240',[('sent',1,2)]),
}
for rid,(page,pre,steps) in ops.items():
    if only and rid not in only: continue
    p = path(page, pre); t = open(p, encoding='utf-8').read(); ok = True
    for kind,a,b in steps:
        new = g(rid,b)
        if kind == 'rowstart': find = line_starting(t, a); rep = find + "\n" + new
        else:
            find = g(rid,a)
            rep = {'rep': new, 'row': find + "\n" + new, 'para': find + "\n\n" + new, 'sent': find + " " + new}[kind]
        n = t.count(find)
        if n != 1: print(f"MISS {rid} {kind} count={n}: {find[:90]!r}"); ok = False; break
        if kind == 'para':
            after = t[t.index(find)+len(find):t.index(find)+len(find)+2]
            if after not in ("\n\n",) and not t.endswith(find+"\n"): print(f"MISS {rid} para not at paragraph end: {after!r}"); ok=False; break
        t = t.replace(find, rep)
    if ok: open(p,'w',encoding='utf-8').write(t); print(f"OK   {rid} {os.path.basename(p)}")
