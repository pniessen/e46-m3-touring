"""Per PDF: page count, and for each card the page of its heading and of its last line ('Stop and ask')."""
import re, subprocess, sys
for pdf in sys.argv[1:]:
    n = int(re.search(r'Pages:\s+(\d+)', subprocess.run(['pdfinfo', pdf], capture_output=True, text=True).stdout).group(1))
    pages = [subprocess.run(['pdftotext', '-layout', '-f', str(i), '-l', str(i), pdf, '-'], capture_output=True, text=True).stdout for i in range(1, n + 1)]
    heads = {}
    for i, t in enumerate(pages, 1):
        for m in re.finditer(r'CARD (\d+[A-F]?):', t):
            heads.setdefault(m.group(1), []).append(i)
    bad = []
    for card, pg in heads.items():
        if len(pg) != 1:
            bad.append(f'{card} heading on pages {pg}')
            continue
        # The card's last block is "Stop and ask"; it must be on the heading's page, before any later card.
        t = pages[pg[0] - 1]
        if 'Stop and ask' not in t:
            bad.append(f'{card}: no "Stop and ask" on page {pg[0]}')
    multi = [i for i, t in enumerate(pages, 1) if len(re.findall(r'CARD \d+[A-F]?:', t)) > 1]
    spill = [i for i, t in enumerate(pages, 1) if i > 1 and not re.search(r'CARD \d+[A-F]?:', t)]
    print(f'{pdf}: {n} pages, {len(heads)} cards; pages with two cards: {multi}; pages without a card heading (after page 1): {spill}; problems: {bad or "none"}')
    print('   page 1 starts:', ' '.join(pages[0].split())[:120])
    print('   last page ends:', ' '.join(pages[-1].split())[-160:])
