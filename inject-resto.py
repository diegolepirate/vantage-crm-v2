#!/usr/bin/env python3
"""Inject vantage-resto-index.html into index.html as TPL_ECOM_HTML['33'].

Relative paths (./vantage-resto-hero.mp4 etc.) resolve to the parent
page's origin when the iframe is loaded via srcdoc — so the videos
served from Netlify root continue to work.
"""
import re, sys

with open('vantage-resto-index.html', 'r', encoding='utf-8') as f:
    html = f.read()

js = html
js = js.replace('\\', '\\\\')
js = js.replace("'", "\\'")
js = js.replace('\r\n', '\n')
js = js.replace('\n', '\\n\\\n')
js = js.replace('</script>', '\\x3c/script>')
js = js.replace('</style>',  '\\x3c/style>')
out = []
for ch in js:
    if ord(ch) > 127:
        out.append('\\u{:04X}'.format(ord(ch)))
    else:
        out.append(ch)
js = ''.join(out)

block = "TPL_ECOM_HTML['33'] = function () {\nreturn '" + js + "'\n};\n"
print('Template size:', len(block), 'chars')

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

pat = r"TPL_ECOM_HTML\['33'\]\s*=\s*function\s*\(\)\s*\{[\s\S]*?\n\};\s*\n"
m = re.search(pat, idx)
if m:
    idx = idx[:m.start()] + block + idx[m.end():]
    print("TPL_ECOM_HTML['33'] REPLACED!")
else:
    # Insert after TPL17 (Apex) or after TPL_FOOD_HTML['32']
    pat17 = r"(TPL_ECOM_HTML\['17'\]\s*=\s*function\s*\(\)\s*\{[\s\S]*?\n\};\s*\n)"
    m = re.search(pat17, idx)
    if m:
        idx = idx[:m.end()] + '\n' + block + idx[m.end():]
        print("TPL_ECOM_HTML['33'] INSERTED after TPL17!")
    else:
        print("ERROR: could not find insertion point")
        sys.exit(1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)
print('Done.')
