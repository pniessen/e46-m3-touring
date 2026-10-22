#!/usr/bin/env python3
"""Cross-check code-like tokens in the SVGs against wiring-canonical.md and the manual."""
import re, sys, xml.etree.ElementTree as ET
sys.dont_write_bytecode = True
canon = open('/tmp/claude-0/-home-user-archeyon/fd84ab71-04a6-5529-8e78-c4db518f2c79/scratchpad/foldin/wiring-canonical.md').read()
manual = open('/home/user/archeyon/e46-m3-touring-conversion/WIRING-AND-CODING.md').read()
src = canon + "\n" + manual
NS = '{http://www.w3.org/2000/svg}'
pats = {
    'connector': r'\bX\d{3,6}\b',
    'wire': r'\b\d\.\d{1,2} [A-Z]{2}(?:/[A-Z]{2}){0,2}\b',
    'colors': r'\b(?:SW|WS|RT|GN|BL|BR|GE|GR|VI|OR)(?:/(?:SW|WS|RT|GN|BL|BR|GE|GR|VI|OR)){1,2}\b',
    'part': r'\b\d{11}\b',
    'job': r'\b(?:STEUERN|START|LESEN|STATUS|STAT|FS)_[A-Z0-9_]+\b|(?<![A-Z])_[A-Z]{1,8}\b',
    'fault': r'\b\d{1,3} \(0x[0-9A-F]{2}\)',
    'fuse': r'\bF\d{1,3}\b',
    'relay': r'\bK\d{2,4}\b',
    'ohm': r'\d+ Ω',
}
for f in sys.argv[1:]:
    root = ET.parse(f).getroot()
    texts = [''.join(el.itertext()) for el in root.iter(NS + 'text')]
    texts.append(root.get('aria-label'))
    allt = '\n'.join(texts)
    print(f'== {f.split("/")[-1]}')
    for kind, p in pats.items():
        toks = sorted(set(re.findall(p, allt)))
        missing = [x for x in toks if x not in src]
        print(f'  {kind:9s} {len(toks):3d} found; not in sources: {missing}')
