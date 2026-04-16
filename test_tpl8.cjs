// Test TPL_ECOM_HTML['8'] — Pixel Forge
const fs = require('fs');
const src = fs.readFileSync('index.html', 'utf8');

const m = src.match(/TPL_ECOM_HTML\['8'\]\s*=\s*function\s*\(\)\s*\{[\s\S]*?\n\};\s*\n/);
if (!m) { console.error('TPL8 block NOT FOUND'); process.exit(1); }

console.log('TPL8 block length:', m[0].length);

try {
  const fn = new Function("var TPL_ECOM_HTML = {};\n" + m[0] + "\nreturn TPL_ECOM_HTML['8']();");
  const html = fn();
  if (html.length < 100) throw new Error('HTML too short: ' + html.length);
  if (!html.includes('<!DOCTYPE html>')) throw new Error('Missing DOCTYPE');
  if (!html.includes('PIXEL FORGE')) throw new Error('Missing PIXEL FORGE text');
  if (!html.includes('class="hero"')) throw new Error('Missing hero class');
  console.log('SUCCESS! HTML length:', html.length);
} catch (e) {
  console.error('EVAL FAILED:', e.message);
  process.exit(1);
}
