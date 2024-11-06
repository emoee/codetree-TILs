const fs =require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');
let string = input[0];
let code = input[1];

for (let c of code) {
    if (c === 'L') {
        string = string.slice(1) + string.slice(0,1);
    } else {
        string = string.slice(-1) + string.slice(0, -1);
    }
}
console.log(string);