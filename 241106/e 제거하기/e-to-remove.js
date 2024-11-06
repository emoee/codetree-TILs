const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();
let result = input.replace('e', '');

console.log(result)