const fs = require("fs");
let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let result = "";

while (a <= b) {
    result += (a + " ")
    a += 2;
}
console.log(result);