const fs = require('fs');
let a = Number(fs.readFileSync(0).toString().trim());

if (a % 2 === 1) {
  a += 3
}

let result = 0
if (a % 3 === 0) {
  result = parseInt(a/3)
}

console.log(result);