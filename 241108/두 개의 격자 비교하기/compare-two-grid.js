const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');
const [n,m] = input.shift().split(' ').map(Number);

let a = input.slice(0,n).map(line=>line.split(' ').map(Number));
let b = input.slice(n,2*n).map(line=>line.split(' ').map(Number));

let result = a.map((row,i)=>
    row.map((val,j) => (val === b[i][j] ? 0 : 1))
);

result.forEach(row => console.log(row.join(' ')));