const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let answer = '';

for (let str of input) {
    for (let char of str.split(" ")) {
        answer += char
    }
}

console.log(answer)