with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()
with open('artisan-jsstring.txt', 'r', encoding='utf-8') as f:
    js_content = f.read().rstrip()

if "TPL_ECOM_HTML['12']" in content:
    start = content.find("TPL_ECOM_HTML['12'] = function")
    close = content.find("';\n};", start)
    end = close + len("';\n};")
    new_func = "TPL_ECOM_HTML['12'] = function () {\n  return '" + js_content + "';\n};"
    content = content[:start] + new_func + content[end:]
    print("Replaced existing TPL_ECOM_HTML['12']")
else:
    marker = "TPL_ECOM_HTML['11'] = function"
    idx = content.find(marker)
    if idx == -1:
        marker = "TPL_ECOM_HTML['10'] = function"
        idx = content.find(marker)
    close = content.find("';\n};", idx)
    end = close + len("';\n};")
    new_func = "\nTPL_ECOM_HTML['12'] = function () {\n  return '" + js_content + "';\n};"
    content = content[:end] + new_func + content[end:]
    print("Inserted new TPL_ECOM_HTML['12']")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Done! Injected {len(js_content)} chars")
