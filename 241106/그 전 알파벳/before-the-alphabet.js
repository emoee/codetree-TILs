const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();
let char = input.charCodeAt(0);

console.log(String.fromCharCode(char-1));