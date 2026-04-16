#!/usr/bin/env python3
"""Inject pixel-forge-template.html into index.html as TPL_ECOM_HTML['8']"""
import re, sys

with open('pixel-forge-template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Escape for JS string
js = html
js = js.replace('\\', '\\\\')
js = js.replace("'", "\\'")
js = js.replace('\r\n', '\n')
js = js.replace('\n', '\\n\\\n')
js = js.replace('</script>', '\\x3c/script>')
# Encode non-ASCII
out = []
for ch in js:
    if ord(ch) > 127:
        out.append('\\u{:04X}'.format(ord(ch)))
    else:
        out.append(ch)
js = ''.join(out)

block = "TPL_ECOM_HTML['8'] = function () {\nreturn '" + js + "'\n};\n"
print('Template size:', len(block), 'chars')

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

# Check if TPL8 already exists
pat = r"TPL_ECOM_HTML\['8'\]\s*=\s*function\s*\(\)\s*\{[\s\S]*?\n\};\s*\n"
if re.search(pat, idx):
    m8 = re.search(pat, idx)
    idx = idx[:m8.start()] + block + idx[m8.end():]
    print("TPL_ECOM_HTML['8'] REPLACED!")
else:
    # Insert after TPL7 block or at end of script
    pat7 = r"(TPL_ECOM_HTML\['7'\]\s*=\s*function\s*\(\)\s*\{[\s\S]*?\n\};\s*\n)"
    m = re.search(pat7, idx)
    if m:
        idx = idx[:m.end()] + '\n' + block + idx[m.end():]
        print("TPL_ECOM_HTML['8'] INSERTED after TPL7!")
    else:
        print("ERROR: Could not find insertion point")
        sys.exit(1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)
print('Done!')
