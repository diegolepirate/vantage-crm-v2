const fs = require('fs');
const content = fs.readFileSync('index.html', 'utf8');
const start = content.indexOf("TPL_ECOM_HTML['6']");
const tpl9 = content.indexOf("TPL_ECOM_HTML['9']");

const tpl6block = content.substring(start, tpl9).trim();
console.log('TPL6 block length:', tpl6block.length);
console.log('Ends with:', JSON.stringify(tpl6block.slice(-20)));

try {
  const TPL_ECOM_HTML = {};
  eval(tpl6block);
  const result = TPL_ECOM_HTML['6']();
  console.log('SUCCESS! HTML length:', result.length);
} catch(e) {
  console.log('ERROR:', e.message);

  const retStart = tpl6block.indexOf("return '") + 8;
  const retEnd = tpl6block.lastIndexOf("'");
  const str = tpl6block.substring(retStart, retEnd);
  console.log('String length:', str.length);

  let lo = 0, hi = str.length;
  while (hi - lo > 50) {
    const mid = Math.floor((lo + hi) / 2);
    try {
      new Function("return '" + str.substring(0, mid) + "'");
      lo = mid;
    } catch(e2) {
      hi = mid;
    }
  }
  console.log('Error around pos:', lo, '-', hi);
  console.log('Context:', JSON.stringify(str.substring(Math.max(0, lo-10), hi+10)));
}
