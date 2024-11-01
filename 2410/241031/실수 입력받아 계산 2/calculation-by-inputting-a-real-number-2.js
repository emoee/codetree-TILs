const fs = require("fs");
let a = Number(fs.readFileSync(0).toString())+1.5;

console.log(a.toFixed(2))