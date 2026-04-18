"""Find unescaped single quotes in TPL6 string"""
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start = content.index("TPL_ECOM_HTML['6']")
end = content.index('};', start) + 2
tpl = content[start:end]

rs = tpl.index("return '") + 8
re_end = tpl.rindex("'")
inner = tpl[rs:re_end]

count = 0
i = 0
while i < len(inner):
    ch = inner[i]
    if ch == '\\':
        i += 2  # skip escaped char
        continue
    if ch == "'":
        ctx = inner[max(0,i-30):i+30]
        print(f"UNESCAPED QUOTE at pos {i}: {repr(ctx)}")
        count += 1
        if count > 10:
            break
    i += 1

print(f"\nTotal unescaped quotes: {count}")
