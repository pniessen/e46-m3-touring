"""Build job-cards.html from a JOB-CARDS.md the same way build_site.py does (website mode)."""
import sys, pathlib
sys.path.insert(0, '/home/user/archeyon/e46-m3-touring-conversion/tools')
from build_html import build_page, page_links
src = pathlib.Path(sys.argv[1]); out = pathlib.Path(sys.argv[2])
html = build_page(src, standalone=True, title='Job cards', eyebrow='Job cards &middot; one printable page per phase',
                  spec_strip=False, artifact_meta=False, photo_mode='link', page_key='cards', fill=True,
                  link_map=page_links('./'))
out.write_text(html, encoding='utf-8'); print('built', out)
