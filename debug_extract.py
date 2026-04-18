#!/usr/bin/env python3
"""Extract TPL_ECOM_HTML['5'] template, unescape it, write to _debug_tpl5.html, then validate."""

import re, sys, subprocess, os

INDEX = os.path.join(os.path.dirname(__file__), "index.html")
OUTPUT = os.path.join(os.path.dirname(__file__), "_debug_tpl5.html")

# 1. Read index.html
with open(INDEX, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 2. Find TPL_ECOM_HTML['5'] function
start = None
for i, line in enumerate(lines):
    if "TPL_ECOM_HTML['5']" in line and "function" in line:
        start = i
        break

if start is None:
    print("ERROR: TPL_ECOM_HTML['5'] not found")
    sys.exit(1)

# The return line is the next line
return_line = lines[start + 1]

# 3. Extract string between return ' and ';
m = re.match(r"\s*return\s*'(.*)'\s*;?\s*$", return_line, re.DOTALL)
if not m:
    print("ERROR: Could not find return '...' pattern on line", start + 2)
    print("Line starts with:", return_line[:100])
    sys.exit(1)

raw = m.group(1)
print(f"Extracted raw string: {len(raw)} characters")

# 4. Unescape
html = raw
html = html.replace("\\n", "\n")
html = html.replace("\\'", "'")
html = html.replace("\\\\", "\\")
# \x3c is < (used to avoid breaking outer script)
html = re.sub(r"\\x3c", "<", html, flags=re.IGNORECASE)
html = re.sub(r"\\x3e", ">", html, flags=re.IGNORECASE)
html = re.sub(r"\\x22", '"', html, flags=re.IGNORECASE)
# Also handle \x27 (single quote) just in case
html = re.sub(r"\\x27", "'", html, flags=re.IGNORECASE)

print(f"Unescaped HTML: {len(html)} characters")

# 5. Write output
with open(OUTPUT, "w", encoding="utf-8") as f:
    f.write(html)
print(f"Written to {OUTPUT}")

# === VALIDATION ===
print("\n" + "="*60)
print("VALIDATION")
print("="*60)

# Check script tag balance
open_scripts = len(re.findall(r"<script[^>]*>", html, re.IGNORECASE))
close_scripts = len(re.findall(r"</script\s*>", html, re.IGNORECASE))
print(f"\n<script> open tags:  {open_scripts}")
print(f"</script> close tags: {close_scripts}")
if open_scripts != close_scripts:
    print(">>> MISMATCH! Script tags are unbalanced!")
    # Find positions
    opens = [(m.start(), m.group()) for m in re.finditer(r"<script[^>]*>", html, re.IGNORECASE)]
    closes = [(m.start(), m.group()) for m in re.finditer(r"</script\s*>", html, re.IGNORECASE)]
    print(f"  Open positions: {[o[0] for o in opens]}")
    print(f"  Close positions: {[c[0] for c in closes]}")
else:
    print(">>> Script tags are balanced.")

# Check style tag balance
open_styles = len(re.findall(r"<style[^>]*>", html, re.IGNORECASE))
close_styles = len(re.findall(r"</style\s*>", html, re.IGNORECASE))
print(f"\n<style> open tags:  {open_styles}")
print(f"</style> close tags: {close_styles}")
if open_styles != close_styles:
    print(">>> MISMATCH! Style tags are unbalanced!")
else:
    print(">>> Style tags are balanced.")

# Check for remaining escape sequences that shouldn't be there
remaining_escapes = re.findall(r"\\x[0-9a-fA-F]{2}", html)
if remaining_escapes:
    print(f"\nWARNING: {len(remaining_escapes)} remaining \\xNN escapes found:")
    for esc in set(remaining_escapes):
        print(f"  {esc} (count: {remaining_escapes.count(esc)})")

# Check for unescaped backslashes that look wrong
bad_backslashes = re.findall(r"\\[^nrt\"'\\/ ]", html)
if bad_backslashes:
    unique = set(bad_backslashes)
    print(f"\nWARNING: {len(bad_backslashes)} suspicious backslash sequences:")
    for b in sorted(unique):
        print(f"  {b} (count: {bad_backslashes.count(b)})")

# Check basic HTML structure
if "<!DOCTYPE" not in html[:100]:
    print("\nWARNING: Missing DOCTYPE")
if "</html>" not in html[-200:]:
    print("\nWARNING: Missing closing </html> tag")

# Extract JS from script tags and check syntax with Node
print("\n" + "="*60)
print("JS SYNTAX CHECK (via Node.js)")
print("="*60)

script_blocks = re.findall(r"<script[^>]*>(.*?)</script>", html, re.DOTALL | re.IGNORECASE)
print(f"Found {len(script_blocks)} script blocks")

errors_found = 0
for i, block in enumerate(script_blocks):
    block = block.strip()
    if not block:
        continue
    # Skip external scripts (src=...)
    if len(block) < 5:
        continue

    # Write to temp file and check with node
    tmp = os.path.join(os.path.dirname(__file__), f"_tmp_js_{i}.js")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(block)

    result = subprocess.run(
        ["node", "--check", tmp],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        errors_found += 1
        print(f"\n>>> SYNTAX ERROR in script block #{i} ({len(block)} chars):")
        err = result.stderr.strip()
        print(f"    {err[:500]}")
        # Show context around the error
        line_match = re.search(r":(\d+)", err)
        if line_match:
            err_line = int(line_match.group(1))
            block_lines = block.split("\n")
            start_ctx = max(0, err_line - 3)
            end_ctx = min(len(block_lines), err_line + 3)
            print(f"    Context (lines {start_ctx+1}-{end_ctx}):")
            for li in range(start_ctx, end_ctx):
                marker = ">>>" if li == err_line - 1 else "   "
                print(f"    {marker} {li+1}: {block_lines[li][:120]}")

    os.remove(tmp)

if errors_found == 0:
    print("All script blocks pass syntax check.")
else:
    print(f"\n>>> {errors_found} script block(s) have syntax errors!")

# Check for the preloader specifically
print("\n" + "="*60)
print("PRELOADER ANALYSIS")
print("="*60)

if "preloader" in html.lower() or "loading" in html.lower():
    # Find preloader-related code
    preloader_matches = re.findall(r".*(?:preloader|loading-screen|loader).*", html, re.IGNORECASE)
    print(f"Found {len(preloader_matches)} lines mentioning preloader/loading/loader")

    # Check for window.onload or DOMContentLoaded
    if "window.onload" in html or "DOMContentLoaded" in html or "addEventListener" in html:
        print("Found load event listeners")

    # Check for setTimeout/setInterval related to preloader
    for pattern in [r"setTimeout.*(?:preload|load|opacity|display)", r"setInterval.*(?:progress|percent|width)"]:
        matches = re.findall(pattern, html, re.IGNORECASE)
        if matches:
            for m in matches[:3]:
                print(f"  Timer: {m[:150]}")

print("\nDone.")
