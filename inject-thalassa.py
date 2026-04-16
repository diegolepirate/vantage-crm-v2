"""Replace TPL_ECOM_HTML['6'] with THALASSA template"""

with open('thalassa-template.html', 'r', encoding='utf-8') as f:
    html = f.read()

def esc(s):
    s = s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n').replace('\r', '').replace('</script>', '\\x3c/script>')
    # Escape non-ASCII chars to \\uXXXX to avoid encoding issues
    out = []
    for ch in s:
        if ord(ch) > 127:
            out.append(f'\\u{ord(ch):04x}')
        else:
            out.append(ch)
    return ''.join(out)

js_str = esc(html)
print(f"Template size: {len(js_str)} chars")

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find existing TPL 6 — remove everything between TPL6 start and TPL9 start
tpl6_start = content.index("TPL_ECOM_HTML['6']")
tpl9_start = content.index("TPL_ECOM_HTML['9']")

# Find what comes after (TPL 9 onwards)
after = content[tpl9_start:]

new_tpl = f"TPL_ECOM_HTML['6'] = function () {{\n  return '{js_str}'\n}};\n\n"

content = content[:tpl6_start] + new_tpl + after

# Normalize line endings to match file
if '\r\n' in content[:1000]:
    new_tpl_normalized = new_tpl.replace('\n', '\r\n')
    content = content[:tpl6_start] + new_tpl_normalized + after

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("TPL_ECOM_HTML['6'] replaced with THALASSA!")
