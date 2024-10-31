const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let i = 0;

while (1) {
    i++;
    n = parseInt(n/i);

    if (n <= 1) 
        break  
}

console.log(i)