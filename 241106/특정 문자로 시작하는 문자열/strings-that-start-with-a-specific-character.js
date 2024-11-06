const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');
let n = Number(input[0]);
let strings = input.slice(1,n);
let char = input[n+1];
let total = 0;
let count = 0;

for (let string of strings) {
    if (char === string[0]) {
        total += string.length;
        count++;
    }
}

console.log(count, (total/count).toFixed(2));