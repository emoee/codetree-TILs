const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let [p1A, p1S] = input[0].split(" ");
let [p2A, p2S] = input[1].split(" ");

if (p1A >= 19 && p1S == "M") {
    console.log(1)
} else if (p2A >= 19 && p2S == "M") {
    console.log(1)
} else {
    console.log(0)
}