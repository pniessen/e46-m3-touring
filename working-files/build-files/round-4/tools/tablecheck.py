import sys, re
def cells(line):
    s = re.sub(r'`[^`]*`', 'X', line)          # ignore pipes in code
    s = s.replace('\\|', 'X')
    return s.count('|') - 1
bad = 0
for p in sys.argv[1:]:
    lines = open(p, encoding='utf-8').read().split("\n"); block = []
    for i, l in enumerate(lines + [""]):
        if l.startswith('|'): block.append((i+1, l))
        else:
            if block:
                n0 = cells(block[0][1])
                for ln, bl in block:
                    if cells(bl) != n0: print(f"{p.split('/')[-1]}:{ln}: {cells(bl)} cells, header {n0}"); bad += 1
            block = []
    # bare dollars outside code
    for i, l in enumerate(lines):
        s = re.sub(r'`[^`]*`', '', l)
        for m in re.finditer(r'(?<!\\)\$', s):
            print(f"{p.split('/')[-1]}:{i+1}: bare $ near {s[max(0,m.start()-20):m.start()+20]!r}"); bad += 1
print("issues:", bad)
