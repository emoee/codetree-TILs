const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();
let result = '';

for (let i=0; i<input.length; i++) {
    if (input[i].charCodeAt(0) > 96) {
        result += input[i].toUpperCase();
    } else {
        result += input[i].toLowerCase();
    }
}
console.log(result);