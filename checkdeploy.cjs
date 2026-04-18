// checkdeploy.cjs — Diagnose TPL_ECOM_HTML['9'] escaping issues
const fs = require('fs');
const path = require('path');

const html = fs.readFileSync(path.join(__dirname, 'index.html'), 'utf8');

// Extract TPL_ECOM_HTML['9'] function body
const startMarker = "TPL_ECOM_HTML['9'] = function () {";
const startIdx = html.indexOf(startMarker);
if (startIdx === -1) { console.error('ERROR: Could not find TPL_ECOM_HTML[\'9\']'); process.exit(1); }

// Find the closing '};' for this function
let braceDepth = 0;
let funcStart = html.indexOf('{', startIdx);
let funcEnd = -1;
for (let i = funcStart; i < html.length; i++) {
  if (html[i] === '{') braceDepth++;
  if (html[i] === '}') { braceDepth--; if (braceDepth === 0) { funcEnd = i + 1; break; } }
}

const funcBody = html.substring(funcStart, funcEnd);

// Evaluate the function
let result;
try {
  const fn = new Function('return (' + 'function ()' + funcBody + ')()')
  result = fn();
  console.log('OK: Function evaluated successfully.');
  console.log('Output length:', result.length);
} catch (e) {
  console.error('ERROR evaluating function:', e.message);
  // Try to show problematic area
  const lines = funcBody.split('\n');
  console.log('Total lines in function:', lines.length);
  process.exit(1);
}

// Check tags
console.log('\n=== TAG ANALYSIS ===');

const checks = [
  { label: '<script>', pattern: /<script[\s>]/gi },
  { label: '</script>', pattern: /<\/script>/gi },
  { label: '<style>', pattern: /<style[\s>]/gi },
  { label: '</style>', pattern: /<\/style>/gi },
  { label: '<link', pattern: /<link[\s]/gi },
];

for (const c of checks) {
  const matches = result.match(c.pattern);
  console.log(`${c.label}: ${matches ? matches.length + ' found' : 'MISSING!'}`);
}

// Check for broken/escaped tags that should NOT appear in output HTML
const brokenChecks = [
  { label: '\\x3cscript (literal backslash-x3c)', pattern: /\\x3cscript/g },
  { label: '\\x3c/script (literal backslash-x3c)', pattern: /\\x3c\/script/g },
  { label: '<\\/style> (backslash in tag)', pattern: /<\\\/style>/g },
  { label: 'x3cscript (without backslash)', pattern: /(?<!\\)x3cscript/g },
];

console.log('\n=== BROKEN TAG CHECK (should all be 0) ===');
for (const c of brokenChecks) {
  const matches = result.match(c.pattern);
  console.log(`${c.label}: ${matches ? matches.length + ' FOUND — PROBLEM!' : '0 — OK'}`);
}

// Show first 500 chars
console.log('\n=== FIRST 500 CHARS OF OUTPUT ===');
console.log(result.substring(0, 500));

// Show around </style> area
const styleCloseIdx = result.indexOf('</style>');
if (styleCloseIdx === -1) {
  console.log('\n=== WARNING: No </style> found! Checking for broken variants ===');
  // Look for any "style>" pattern
  const idx = result.indexOf('style>');
  if (idx !== -1) {
    console.log('Found "style>" at index', idx);
    console.log('Context:', JSON.stringify(result.substring(Math.max(0, idx - 30), idx + 30)));
  }

  // Check for <\/style>
  const bsIdx = result.indexOf('<\\/style>');
  if (bsIdx !== -1) {
    console.log('Found "<\\/style>" (with backslash) at index', bsIdx, '— THIS IS THE BUG');
    console.log('Context:', JSON.stringify(result.substring(Math.max(0, bsIdx - 30), bsIdx + 30)));
  }
} else {
  console.log('\n</style> found at index', styleCloseIdx, '— OK');
}

// Check script tags vicinity
console.log('\n=== SCRIPT TAG LOCATIONS ===');
let pos = 0;
let scriptCount = 0;
while (true) {
  const idx = result.indexOf('<script', pos);
  if (idx === -1) break;
  scriptCount++;
  const end = result.indexOf('>', idx);
  console.log(`Script #${scriptCount} at index ${idx}: ${result.substring(idx, end + 1)}`);
  pos = end + 1;
}
if (scriptCount === 0) {
  console.log('NO <script> tags found in output!');
  // Check if \x3c was not interpreted
  const x3cIdx = result.indexOf('x3c');
  if (x3cIdx !== -1) {
    console.log('Found literal "x3c" at index', x3cIdx);
    console.log('Context:', JSON.stringify(result.substring(Math.max(0, x3cIdx - 10), x3cIdx + 30)));
  }
}

// Compare with standalone
console.log('\n=== STANDALONE COMPARISON ===');
const standalone = fs.readFileSync(path.join(__dirname, 'velvet-stone-template.html'), 'utf8');
const standaloneScripts = standalone.match(/<script[\s>]/gi);
const standaloneStyleClose = standalone.match(/<\/style>/gi);
console.log('Standalone <script> tags:', standaloneScripts ? standaloneScripts.length : 0);
console.log('Standalone </style> tags:', standaloneStyleClose ? standaloneStyleClose.length : 0);
console.log('CRM output <script> tags:', scriptCount);
console.log('CRM output </style> tags:', (result.match(/<\/style>/gi) || []).length);

// sandbox analysis
console.log('\n=== SANDBOX ANALYSIS ===');
console.log('iframe sandbox="allow-scripts" blocks:');
console.log('- allow-same-origin: BLOCKED (no cross-origin requests via fetch/XHR)');
console.log('- allow-popups: BLOCKED');
console.log('- allow-forms: BLOCKED');
console.log('- allow-top-navigation: BLOCKED');
console.log('NOTE: CDN script loading via <script src="..."> IS allowed with allow-scripts');
console.log('NOTE: Image loading via <img src="..."> IS allowed (not blocked by sandbox)');
console.log('NOTE: Three.js defer should work in srcdoc iframes — defer just means after parsing');
