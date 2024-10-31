const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());

let i = 0; 
while (i < 5) {
    console.log("*");
    i++;
}