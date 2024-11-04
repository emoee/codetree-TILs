const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let [n, m] = input[0].split(" ").map(Number);
let board = Array(n).fill(0).map(()=> Array(n).fill(0));

for (let i=1; i<=m; i++){
    let [r, c] = input[i].split(" ").map(Number);
    board[r-1][c-1] = r*c;
}

for (let b of board) {
    console.log(b.join(" "));
}