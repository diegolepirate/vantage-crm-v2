const fs = require('fs');
const html = fs.readFileSync('index.html', 'utf8');

// Extract all inline script blocks
const regex = /<script(?![^>]*\bsrc\b)[^>]*>([\s\S]*?)<\/script>/gi;
let match;
let i = 0;
while ((match = regex.exec(html)) !== null) {
  i++;
  const content = match[1].trim();
  if (!content) continue;

  const lineNum = html.substring(0, match.index).split('\n').length;

  try {
    new Function(content);
    console.log(`Script #${i} (line ~${lineNum}): OK (${content.length} chars)`);
  } catch(e) {
    console.log(`Script #${i} (line ~${lineNum}): ERROR - ${e.message}`);
    // Show first 200 chars
    console.log('  Preview:', content.substring(0, 200));
  }
}
console.log(`\nTotal: ${i} scripts checked`);
