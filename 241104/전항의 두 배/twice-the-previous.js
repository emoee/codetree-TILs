const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let [a1, a2] = [input[0], input[1]];
let result = [a1, a2];

for (let i = 2; i < 10; i++){
    result.push((2*result[i-2])+result[i-1]);
}

console.log(result.join(" "));