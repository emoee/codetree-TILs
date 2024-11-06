const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();

let result = input.replaceAll(input[1], input[0]);
console.log(result)