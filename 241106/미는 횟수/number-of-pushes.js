const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');
let [a, b] = [input[0], input[1]];
let count = 0;

while (a != b) {
    count++;
    a = a.slice(-1) + a.slice(0,-1);

    if (count > (2*a.length)+1) {
        count = -1;
        break
    }
}
console.log(count)