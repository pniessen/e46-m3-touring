"""Parse a request file into blocks: {rid: {'title':..., 'groups':[(label, text), ...]}}."""
import re, sys
def parse(path):
    blocks, cur, label, buf = {}, None, None, None
    def flush():
        if cur is not None and label is not None:
            blocks[cur]['groups'].append((label, "\n".join(buf)))
    for line in open(path, encoding='utf-8').read().split("\n"):
        m = re.match(r'^### (R\d+): (.*)$', line)
        if m:
            flush(); cur, label, buf = m.group(1), None, []
            blocks[cur] = {'title': m.group(2), 'groups': []}
            continue
        if cur is None: continue
        if line.startswith('- **') or line.startswith('---'):
            flush(); label, buf = line, []
            continue
        q = re.match(r'^  >( ?)(.*)$', line)
        if q and label is not None:
            buf.append(q.group(2))
    flush()
    return blocks
if __name__ == '__main__':
    b = parse(sys.argv[1])
    for k, v in b.items():
        print(k, v['title'][:70], [ (l[:30], len(t)) for l, t in v['groups']])
