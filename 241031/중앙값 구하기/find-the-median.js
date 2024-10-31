const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);

input.sort()
console.log(input[1])