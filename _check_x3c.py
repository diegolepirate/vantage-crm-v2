import re
with open('index.html','r',encoding='utf-8') as f:
    c = f.read()
s = c.index("TPL_ECOM_HTML['5']")
e = c.index("TPL_ECOM_HTML['9']")
t = c[s:e]
bad = 0
for m in re.finditer(r'x3c', t):
    p = m.start()
    pre = t[max(0,p-3):p]
    if '\\' in pre:
        continue
    print(f'BAD @{p}: {repr(t[max(0,p-5):p+15])}')
    bad += 1
if bad == 0:
    print('All x3c tags OK')
else:
    print(f'{bad} broken x3c tags found!')
