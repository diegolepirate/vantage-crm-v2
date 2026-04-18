with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

with open('velvet-stone-jsstring.txt', 'r', encoding='utf-8') as f:
    js_content = f.read().rstrip()

# Find the start line (TPL_ECOM_HTML['9'] = function)
start_idx = None
end_idx = None
for i, line in enumerate(lines):
    if "TPL_ECOM_HTML['9'] = function" in line:
        start_idx = i
    if start_idx is not None and i > start_idx and line.strip() == '};':
        end_idx = i
        break

if start_idx is None or end_idx is None:
    print(f"ERROR: start={start_idx}, end={end_idx}")
    exit(1)

print(f"Replacing lines {start_idx+1} to {end_idx+1}")

# Build new function - the js_content already has \ continuations on each line
# Last line of js_content has no \, so we just close with ';
new_func = "TPL_ECOM_HTML['9'] = function () {\n  return '" + js_content + "';\n};\n"

# Replace
new_lines = lines[:start_idx] + [new_func] + lines[end_idx+1:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Done! Injected {len(js_content)} chars")
