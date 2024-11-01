const fs = require("fs");
let [s, t] = fs.readFileSync(0).toString().trim().split("\n").map(String);

console.log(`${t}\n${s}`)