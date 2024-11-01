const fs = require("fs");
let [a, b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let sumVal = 0

for (let i = a; i<=b; i++) {
    if (i%6===0 && i%8!=0)
        sumVal += i
}

console.log(sumVal)