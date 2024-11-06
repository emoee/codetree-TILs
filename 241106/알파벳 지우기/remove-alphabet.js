const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');
let a = input[0].toLowerCase().replace(/[a-z]/gi, '');
let b = input[1].toLowerCase().replace(/[a-z]/gi, '');

console.log(Number(a)+Number(b));