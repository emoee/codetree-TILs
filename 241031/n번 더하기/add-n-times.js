const fs = require("fs");
let [a, n] = fs.readFileSync(0).toString().trim().split(" ").map(Number);

let i = 0;
while (i < n) {
    a += n;
    console.log(a);
    i++;
}