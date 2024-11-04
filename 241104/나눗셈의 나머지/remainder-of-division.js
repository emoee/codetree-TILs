const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split(" ").map(Number);
let [a, b] = [input[0], input[1]];
let count = Array(10).fill(0);

while (a/b > 0) {
    let num = Math.floor(a%b);
    count[num] += 1;
    a = Math.floor(a/b);
}

let answer = 0;
count.forEach((value) => {
    if (value > 0)
        answer += value**2;
})

console.log(answer);