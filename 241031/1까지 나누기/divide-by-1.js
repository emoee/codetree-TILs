const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let i = 1;

while (1) {
    n = n/i;
    i++;

    if ((n/i) <= 1) 
        break  
}

console.log(i)