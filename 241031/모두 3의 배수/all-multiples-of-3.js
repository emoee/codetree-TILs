const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let result= 1;

for (let i = 0; i < 5; i++) {
    if (input[i]%3!==0){
        result = 0
        break
    }
}

console.log(result)