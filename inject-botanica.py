with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
with open('botanica-jsstring.txt', 'r', encoding='utf-8') as f:
    js_content = f.read().rstrip()

if "TPL_ECOM_HTML['13']" in content:
    start = content.find("TPL_ECOM_HTML['13'] = function")
    close = content.find("';\n};", start)
    end = close + len("';\n};")
    new_func = "TPL_ECOM_HTML['13'] = function () {\n  return '" + js_content + "';\n};"
    content = content[:start] + new_func + content[end:]
    print("Replaced existing TPL_ECOM_HTML['13']")
else:
    marker = "TPL_ECOM_HTML['12'] = function"
    idx = content.find(marker)
    close = content.find("';\n};", idx)
    end = close + len("';\n};")
    new_func = "\nTPL_ECOM_HTML['13'] = function () {\n  return '" + js_content + "';\n};"
    content = content[:end] + new_func + content[end:]
    print("Inserted new TPL_ECOM_HTML['13']")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Done! Injected {len(js_content)} chars")
