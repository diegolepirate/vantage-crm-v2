"""Convert chromatic-template.html to JS string and inject as TPL_ECOM_HTML['6']"""

with open('chromatic-template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Escape for JS string
def esc(s):
    return s.replace('\\', '\\\\').replace("'", "\\'").replace('\n', '\\n').replace('\r', '').replace('</script>', '\\x3c/script>')

js_str = esc(html)

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find insertion point - right before TPL_ECOM_HTML['9']
marker = "TPL_ECOM_HTML['9']"
pos = content.index(marker)

# Build the new function
new_tpl = f"TPL_ECOM_HTML['6'] = function () {{\n  return '{js_str}'\n}};\n\n"

# Insert before TPL 9
content = content[:pos] + new_tpl + content[pos:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Injected TPL_ECOM_HTML['6'] ({len(js_str)} chars)")
print("Done!")
