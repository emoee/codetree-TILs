const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');
let n = Number(input[0]);
let numbers = input.slice(1).map(Number);
let result = 0;

for (let num of numbers) {
    result += num;
}
let string = result.toString();
console.log(string.slice(1)+string[0]);