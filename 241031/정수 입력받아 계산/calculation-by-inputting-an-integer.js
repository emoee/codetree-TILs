const fs = require("fs");

let a = fs.readFileSync(0).toString();
a = Number(a)*2+3

console.log(a)