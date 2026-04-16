"""Replace/Insert TPL_ECOM_HTML['7'] with SUMMIT STRATEGY template"""

with open('summit-template.html', 'r', encoding='utf-8') as f:
    html = f.read()

def esc(s):
    s = s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n').replace('\r', '').replace('</script>', '\\x3c/script>')
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

new_tpl = f"TPL_ECOM_HTML['7'] = function () {{\n  return '{js_str}'\n}};\n\n"

# Check if TPL7 already exists
if "TPL_ECOM_HTML['7']" in content:
    # Replace existing TPL7 — find boundary to TPL8 or TPL9
    tpl7_start = content.index("TPL_ECOM_HTML['7']")
    # Find next TPL declaration after TPL7
    rest = content[tpl7_start + 20:]
    for marker in ["TPL_ECOM_HTML['8']", "TPL_ECOM_HTML['9']", "TPL_ECOM_HTML['10']"]:
        if marker in content[tpl7_start + 20:]:
            next_tpl_start = content.index(marker, tpl7_start + 20)
            break
    after = content[next_tpl_start:]
    content = content[:tpl7_start] + new_tpl + after
    print("TPL_ECOM_HTML['7'] REPLACED with SUMMIT!")
else:
    # Insert new TPL7 before TPL9
    tpl9_start = content.index("TPL_ECOM_HTML['9']")
    before = content[:tpl9_start]
    after = content[tpl9_start:]
    content = before + new_tpl + after
    print("TPL_ECOM_HTML['7'] INSERTED before TPL9!")

# Normalize line endings
if '\r\n' in content[:1000]:
    new_tpl_normalized = new_tpl.replace('\n', '\r\n')
    if "TPL_ECOM_HTML['7']" in content:
        tpl7_pos = content.index("TPL_ECOM_HTML['7']")
        # Re-find next TPL after our insertion
        for marker in ["TPL_ECOM_HTML['8']", "TPL_ECOM_HTML['9']", "TPL_ECOM_HTML['10']"]:
            if marker in content[tpl7_pos + 20:]:
                next_pos = content.index(marker, tpl7_pos + 20)
                break
        content = content[:tpl7_pos] + new_tpl_normalized + content[next_pos:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done!")
