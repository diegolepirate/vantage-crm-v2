import sys

with open('velvet-stone-template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Escape backslashes first, then single quotes
html = html.replace('\\', '\\\\')
html = html.replace("'", "\\'")
html = html.replace('<script>', '\\x3cscript>')
html = html.replace('</script>', '\\x3c/script>')
html = html.replace('<script ', '\\x3cscript ')
html = html.replace('</style>', '<\\/style>')

# Replace real newlines with \n so they survive as newlines in the final HTML
# This is CRITICAL: without this, // comments in JS break everything
html = html.replace('\n', '\\n')

# Remove trailing empty \\n
while html.endswith('\\n'):
    html = html[:-2]

result = html

with open('velvet-stone-jsstring.txt', 'w', encoding='utf-8') as f:
    f.write(result)

print(f'Done: {len(result)} chars')
