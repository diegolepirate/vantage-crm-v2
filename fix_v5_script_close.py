"""Fix the broken x3c/script> tag in V5 code inside TPL5"""

filepath = r"C:\vantage-clean\crm-v2-push\index.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Locate TPL5 boundaries
tpl5_start = content.index("TPL_ECOM_HTML['5']")
tpl9_start = content.index("TPL_ECOM_HTML['9']")

tpl = content[tpl5_start:tpl9_start]

# The bug: the V5 patch inserted JS before what it thought was
# the last \x3c/script> but the regex found "x3c/script>"
# (with only the escape sequence chars, not the backslash).
# The patch's esc() function then double-escaped it.
# Result in the raw file: the closing tag is "x3c/script>"
# instead of "\\x3c/script>"

# Find the broken occurrence - it's the one WITHOUT the \\ prefix
# The good ones look like: \\x3c/script>
# The bad one looks like: x3c/script> (preceded by \\n\\n, not \\)

broken = 'initLiveActivityFeed();\\n\\nx3c/script>'
fixed  = 'initLiveActivityFeed();\\n\\n\\x3c/script>'

idx = tpl.index(broken)
print(f"Found broken tag at TPL offset {idx}")

tpl = tpl[:idx] + fixed + tpl[idx+len(broken):]

# Verify all x3c patterns now have proper prefix
import re
for m in re.finditer(r'x3c', tpl):
    pos = m.start()
    prefix = tpl[pos-2:pos]
    tag = tpl[pos:pos+15]
    ok = prefix.endswith('\\')
    print(f"  @{pos}: prefix={repr(prefix)} tag={repr(tag)} {'OK' if ok else 'BROKEN!'}")

content = content[:tpl5_start] + tpl + content[tpl9_start:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("\nFixed!")
