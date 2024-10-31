const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let i = 1;

while ((n/i) >= 1) {
    n = n/i;
    i++;    
}

console.log(i)