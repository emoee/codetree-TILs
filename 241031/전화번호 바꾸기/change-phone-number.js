const fs = require("fs");
let [head, body, tail] = fs.readFileSync(0).toString().trim().split("-")

console.log(`${head}-${tail}-${body}`)