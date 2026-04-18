"""Find exact position of syntax error in TPL6"""
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.index("TPL_ECOM_HTML['6']")
end = content.index('};', start) + 2
tpl = content[start:end]

# Get the string value
rs = tpl.index("return '") + 8
re_end = tpl.rindex("'")
inner = tpl[rs:re_end]

# Look for problematic patterns
# 1. Unescaped backslashes that aren't valid escape sequences
import re
i = 0
problems = []
while i < len(inner):
    if inner[i] == '\\':
        if i + 1 < len(inner):
            next_ch = inner[i+1]
            if next_ch not in ('n', 'r', 't', '\\', "'", '"', 'x', 'u', '0', 'b', 'f', 'v'):
                ctx = inner[max(0,i-20):i+20]
                problems.append((i, next_ch, ctx))
            i += 2
        else:
            problems.append((i, 'EOF', ''))
            i += 1
    else:
        i += 1

print(f"Suspicious escapes: {len(problems)}")
for pos, ch, ctx in problems[:20]:
    print(f"  pos {pos}: \\{ch} -> {repr(ctx)}")
