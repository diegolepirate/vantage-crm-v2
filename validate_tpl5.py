import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

start = c.index("TPL_ECOM_HTML['5']")
tpl9 = c.index("TPL_ECOM_HTML['9']")
tpl = c[start:tpl9]

ret_idx = tpl.index("return '")
end_idx = tpl.rindex("';")
s = tpl[ret_idx+8:end_idx]

# Unescape
html = []
i = 0
bs = chr(92)
while i < len(s):
    if s[i] == bs and i+1 < len(s):
        nxt = s[i+1]
        if nxt == 'n': html.append(chr(10))
        elif nxt == "'": html.append("'")
        elif nxt == bs: html.append(bs)
        elif nxt == 't': html.append(chr(9))
        elif nxt == 'x' and i+3 < len(s):
            # hex escape like \x3c
            hexval = s[i+2:i+4]
            try:
                html.append(chr(int(hexval, 16)))
            except:
                html.append(bs + nxt)
            i += 4
            continue
        else:
            html.append(bs + nxt)
        i += 2
    else:
        html.append(s[i])
        i += 1

html_str = ''.join(html)

with open('_temp_tpl5.html', 'w', encoding='utf-8') as f:
    f.write(html_str)

print(f'Wrote {len(html_str)} chars')

# Now extract all <script> content and validate with node
import re
scripts = re.findall(r'<script[^>]*>(.*?)</script>', html_str, re.DOTALL)
print(f'Found {len(scripts)} script blocks')

for idx, script in enumerate(scripts):
    if not script.strip():
        continue
    fname = f'_temp_script_{idx}.js'
    with open(fname, 'w', encoding='utf-8') as f:
        # Wrap in function to avoid execution
        f.write('(function(){\n' + script + '\n})()')
    print(f'Script {idx}: {len(script)} chars -> {fname}')
