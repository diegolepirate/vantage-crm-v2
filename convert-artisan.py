with open('artisan-goods-template.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('\\', '\\\\')
html = html.replace("'", "\\'")
html = html.replace('<script>', '\\x3cscript>')
html = html.replace('</script>', '\\x3c/script>')
html = html.replace('<script ', '\\x3cscript ')
html = html.replace('</style>', '<\\/style>')
html = html.replace('\n', '\\n')
while html.endswith('\\n'):
    html = html[:-2]

with open('artisan-jsstring.txt', 'w', encoding='utf-8') as f:
    f.write(html)
print(f'Done: {len(html)} chars')
