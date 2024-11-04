const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let numbers = input[1].split(" ").map(Number);
let index = -1;
let count = 0;

for (let i=0; i < numbers.length; i++) {
    if (numbers[i] === 2) {
        index = i+1;
        count += 1;
    }
    if (count === 3)
        break;
}

console.log(index)