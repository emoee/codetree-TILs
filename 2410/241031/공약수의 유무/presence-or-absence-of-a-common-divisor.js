const fs = require("fs");
let [a,b] = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let result = 0;

for (let i=a; i <= b; i++){
    if (1920%i===0 && 2880%i===0) {
        result = 1;
        break
    }
}

console.log(result)