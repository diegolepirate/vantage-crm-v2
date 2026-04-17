#!/usr/bin/env python3
"""Inject apex-consulting-template.html into index.html as TPL_ECOM_HTML['17']"""
import re, sys

with open('apex-consulting-template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Escape for JS string
js = html
js = js.replace('\\', '\\\\')
js = js.replace("'", "\\'")
js = js.replace('\r\n', '\n')
js = js.replace('\n', '\\n\\\n')
js = js.replace('</script>', '\\x3c/script>')
js = js.replace('</style>',  '\\x3c/style>')
# Encode non-ASCII
out = []
for ch in js:
    if ord(ch) > 127:
        out.append('\\u{:04X}'.format(ord(ch)))
    else:
        out.append(ch)
js = ''.join(out)

block = "TPL_ECOM_HTML['17'] = function () {\nreturn '" + js + "'\n};\n"
print('Template size:', len(block), 'chars')

with open('index.html', 'r', encoding='utf-8') as f:
    idx = f.read()

pat = r"TPL_ECOM_HTML\['17'\]\s*=\s*function\s*\(\)\s*\{[\s\S]*?\n\};\s*\n"
m = re.search(pat, idx)
if m:
    idx = idx[:m.start()] + block + idx[m.end():]
    print("TPL_ECOM_HTML['17'] REPLACED!")
else:
    # Insert after TPL8 block
    pat8 = r"(TPL_ECOM_HTML\['8'\]\s*=\s*function\s*\(\)\s*\{[\s\S]*?\n\};\s*\n)"
    m = re.search(pat8, idx)
    if m:
        idx = idx[:m.end()] + '\n' + block + idx[m.end():]
        print("TPL_ECOM_HTML['17'] INSERTED after TPL8!")
    else:
        print("ERROR: Could not find insertion point")
        sys.exit(1)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx)
print('Done!')
