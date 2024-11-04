const fs = require("fs");
const INTMAX = Number.MAX_SAFE_INTEGER;

let input = fs.readFileSync(0).toString().trim().split("\n");
let numbers = input[1].split(" ").map(Number);
let answer = INTMAX;

for (let i=1; i<numbers.length; i++) {
    answer = Math.min(answer, numbers[i]-numbers[i-1])
}

console.log(answer)