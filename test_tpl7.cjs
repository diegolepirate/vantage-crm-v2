// Test TPL_ECOM_HTML['7'] — Summit Strategy
const fs = require('fs');
const src = fs.readFileSync('index.html', 'utf8');

const m = src.match(/TPL_ECOM_HTML\['7'\]\s*=\s*function\s*\(\)\s*\{[\s\S]*?\n\};\s*\n/);
if (!m) { console.error('TPL7 block NOT FOUND'); process.exit(1); }

console.log('TPL7 block length:', m[0].length);
console.log('Ends with:', JSON.stringify(m[0].slice(-30)));

try {
  const fn = new Function("var TPL_ECOM_HTML = {};\n" + m[0] + "\nreturn TPL_ECOM_HTML['7']();");
  const html = fn();
  if (html.length < 100) throw new Error('HTML too short: ' + html.length);
  if (!html.includes('<!DOCTYPE html>')) throw new Error('Missing DOCTYPE');
  if (!html.includes('SUMMIT')) throw new Error('Missing SUMMIT text');
  console.log('SUCCESS! HTML length:', html.length);
} catch (e) {
  console.error('EVAL FAILED:', e.message);
  process.exit(1);
}
