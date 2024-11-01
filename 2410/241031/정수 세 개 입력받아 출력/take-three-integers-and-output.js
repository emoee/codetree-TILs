const fs = require("fs");
let values = fs.readFileSync(0).toString().split("\n");
let [a, b] = values[0].split(" ").map(Number);
let c = values[1]

console.log(a, b, c)