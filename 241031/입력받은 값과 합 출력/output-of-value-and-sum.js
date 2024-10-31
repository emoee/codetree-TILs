const fs = require("fs")

let values = fs.readFileSync(0).toString().split(" ")
let a = Number(values[0])
let b = Number(values[1])

console.log(a, b, a+b)