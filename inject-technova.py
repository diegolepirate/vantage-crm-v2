with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

with open('technova-jsstring.txt', 'r', encoding='utf-8') as f:
    js_content = f.read().rstrip()

# Find where to insert - after TPL_ECOM_HTML['9'] closing };
marker = "TPL_ECOM_HTML['9'] = function"
idx = content.find(marker)
if idx == -1:
    print("ERROR: TPL_ECOM_HTML['9'] not found")
    exit(1)

# Find the closing }; of template 9
close = content.find("';\n};", idx)
if close == -1:
    print("ERROR: closing }; not found")
    exit(1)
end_of_9 = close + len("';\n};")

# Check if TPL_ECOM_HTML['10'] already exists
if "TPL_ECOM_HTML['10']" in content:
    # Replace existing
    start10 = content.find("TPL_ECOM_HTML['10'] = function")
    close10 = content.find("';\n};", start10)
    end10 = close10 + len("';\n};")
    new_func = "TPL_ECOM_HTML['10'] = function () {\n  return '" + js_content + "';\n};"
    content = content[:start10] + new_func + content[end10:]
    print(f"Replaced existing TPL_ECOM_HTML['10']")
else:
    # Insert after template 9
    new_func = "\nTPL_ECOM_HTML['10'] = function () {\n  return '" + js_content + "';\n};"
    content = content[:end_of_9] + new_func + content[end_of_9:]
    print(f"Inserted new TPL_ECOM_HTML['10']")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Done! Injected {len(js_content)} chars")
