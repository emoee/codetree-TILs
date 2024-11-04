const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let [n, m] = input[0].split(" ").map(Number);
let board1 = input.slice(1,n+1).map(b => b.trim().split(" ").map(Number));
let board2 = input.slice(n+1).map(b => b.trim().split(" ").map(Number));

let answer = Array(n).fill(0).map(() => Array(m).fill(0));
for (let i=0; i<n; i++) {
    for (let j=0; j<n; j++) {
        if (board1[i][j] != board2[i][j]) {
            answer[i][j] = 1;
        }
    }
}

for (let a of answer) {
    console.log(a.join(" "));
}