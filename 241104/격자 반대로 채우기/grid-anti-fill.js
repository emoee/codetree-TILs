const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let board = Array(n).fill(0).map(()=> Array(n).fill(0));
let count = 0;

for (let i=0; i<n; i++){
    if (i%2 === 0) {
        for (let j=n-1; j>=0; j--){
            count += 1;
            board[i][j] = count;
        }
    } else {
        for (let j=0; j<n; j++){
            count += 1;
            board[i][j] = count;
        }
    }
}

for (let i=0; i<n; i++){
    let answer = "";
    for (let j=n-1; j>=0; j--){ 
        answer += board[j][i]+" ";
    }
    console.log(answer);
}