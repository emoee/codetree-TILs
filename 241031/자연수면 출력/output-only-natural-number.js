const fs = require("fs");
let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let i = 0;
let result = "";

while (i < b) {
    result += a;
    i++;
}

console.log((a <= 0) ? 0 : result);