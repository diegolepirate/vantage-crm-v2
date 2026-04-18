import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the template function body
m = re.search(r"TPL_ECOM_HTML\['9'\]\s*=\s*function\s*\(\)\s*\{\s*return\s*'", content)
if not m:
    print("NOT FOUND")
    exit(1)

start = m.end()
# Find closing '; };
end = content.find("';\n};", start)
if end == -1:
    end = content.find("'; };", start)
tpl_escaped = content[start:end]

# Join line continuations
tpl_joined = tpl_escaped.replace('\\\n', '')

# Unescape JS string
tpl = tpl_joined
tpl = tpl.replace('\\n', '\n')
tpl = tpl.replace('\\x3cscript', '<script')
tpl = tpl.replace('\\x3c/script', '</script')
tpl = tpl.replace('<\\/style>', '</style>')
tpl = tpl.replace("\\'", "'")
tpl = tpl.replace('\\\\', '\\')

with open('extracted-template.html', 'w', encoding='utf-8') as f:
    f.write(tpl)

print(f"Extracted {len(tpl)} chars")

# Compare with original
with open('velvet-stone-template.html', 'r', encoding='utf-8') as f:
    original = f.read()

if tpl.strip() == original.strip():
    print("MATCH: extracted == original")
else:
    print(f"MISMATCH: extracted={len(tpl.strip())} original={len(original.strip())}")
    # Find first difference
    for i, (a, b) in enumerate(zip(tpl.strip(), original.strip())):
        if a != b:
            print(f"First diff at char {i}: extracted='{a}' ({ord(a)}) original='{b}' ({ord(b)})")
            print(f"Context extracted: ...{repr(tpl[max(0,i-30):i+30])}...")
            print(f"Context original:  ...{repr(original[max(0,i-30):i+30])}...")
            break
    else:
        print("One is longer than the other")
