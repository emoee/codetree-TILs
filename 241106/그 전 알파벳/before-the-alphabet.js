const fs = require('fs');
let input = fs.readFileSync(0).toString().trim();
let char = input.charCodeAt(0);

if (char === 97) {
    result = 'z';
} else {
    result = String.fromCharCode(char - 1);
}
console.log(result)