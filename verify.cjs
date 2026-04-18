const fs = require('fs');
const h = fs.readFileSync('index.html', 'utf8');
const lines = h.split('\n');

let start = -1, end = -1;
for (let i = 0; i < lines.length; i++) {
  if (lines[i].includes("TPL_ECOM_HTML['9'] = function")) start = i;
  if (start > -1 && i > start && lines[i].trim() === '};') { end = i; break; }
}

if (start === -1 || end === -1) { console.log('NOT FOUND', start, end); process.exit(1); }

const block = lines.slice(start, end + 1).join('\n');
console.log('Block: lines', start+1, 'to', end+1, '(', block.length, 'chars)');

try {
  new Function(block);
  console.log('SYNTAX OK');
} catch(e) {
  console.log('SYNTAX ERROR:', e.message);
}
