with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

start = None
end = None
for i, line in enumerate(lines):
    if "TPL_ECOM_HTML['9'] = function" in line:
        start = i
    if start is not None and i > start and line.strip() == '};':
        end = i
        break

print(f'Start: {start+1}, End: {end+1}')

bslash = chr(92)  # backslash

for i in range(start + 2, end):
    curr = lines[i].rstrip('\n')
    # Empty or doesn't end with backslash (except the final '; line)
    if curr.strip() == '':
        print(f'EMPTY LINE at {i+1}')
    if not curr.endswith(' ' + bslash) and curr.strip() not in ["';", '']:
        print(f'NO CONTINUATION at line {i+1}: {repr(curr[:120])}')
