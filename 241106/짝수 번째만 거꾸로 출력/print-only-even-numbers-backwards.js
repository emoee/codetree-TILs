const fs = require('fs');
let input = fs.readFileSync(0).toString().trim()
let total = [];

for (let i=0; i<input.length; i++) {
    if (i%2 != 0) {
        total.push(input[i])
    }
}

console.log(total.reverse().join(""))