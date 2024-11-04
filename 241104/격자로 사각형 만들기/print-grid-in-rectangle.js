const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let board = Array(n).fill(0).map(()=> Array(n).fill(1));

for (let i=1; i<n; i++) {
    for (let j=1; j<n; j++) {
        board[i][j] = board[i-1][j-1] + board[i][j-1] + board[i-1][j];
    }
} 

for (let b of board){
    console.log(b.join(" "));
}