const fs = require("fs");
let ages = fs.readFileSync(0).toString().trim().split("\n");
let i = 0;
let avg = 0;

while (1) {
    avg += Number(ages[i])
    i++;
    
    if (Number(ages[i]) > 29 || Number(ages[i]) < 20) {
        console.log((avg/i).toFixed(2))
        break
    }
    if (i === ages.length)
        break
}