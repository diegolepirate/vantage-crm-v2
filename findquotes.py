with open('velvet-stone-jsstring.txt', 'r', encoding='utf-8') as f:
    content = f.read()

# Manual search for unescaped single quotes
i = 0
count = 0
while i < len(content):
    if content[i] == "'":
        # Check if preceded by backslash
        if i == 0 or content[i-1] != '\\':
            line_num = content[:i].count('\n') + 1
            start = max(0, i - 30)
            end = min(len(content), i + 30)
            ctx = content[start:end].replace('\n', '\\n')
            print(f'UNESCAPED QUOTE line {line_num}: ...{ctx}...')
            count += 1
            if count > 10:
                print('... (stopping at 10)')
                break
    i += 1

if count == 0:
    print('No unescaped single quotes found')
