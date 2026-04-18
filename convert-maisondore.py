with open('maison-dore-template.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace relative video path with absolute Netlify URL
html = html.replace('src="maison-dore-bg.mp4"', 'src="https://vantagebookdesign.netlify.app/maison-dore-bg.mp4"')

html = html.replace('\\', '\\\\')
html = html.replace("'", "\\'")
html = html.replace('<script>', '\\x3cscript>')
html = html.replace('</script>', '\\x3c/script>')
html = html.replace('<script ', '\\x3cscript ')
html = html.replace('</style>', '<\\/style>')
html = html.replace('\n', '\\n')

while html.endswith('\\n'):
    html = html[:-2]

with open('maisondore-jsstring.txt', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'Done: {len(html)} chars')
