const fs = require("fs");
let [b, a] = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let result = ""

for (let i = b; i >= a; i -= 2) {
    result += (i + " ")
}
console.log(result)