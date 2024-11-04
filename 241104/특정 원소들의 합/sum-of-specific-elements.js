const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");

let board = input.map(b => b.trim().split(" ").map(Number));
let answer = 0;

for (let i=0; i < board.length; i++) {
    for (let j=0; j <= i; j++) {
        answer += board[i][j];
    }
}

console.log(answer);