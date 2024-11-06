const fs = require('fs');
let input = fs.readFileSync(0).toString().trim().split('\n');

let a = input[0];
let b = input[1];

let ab = a+b;
let ba = b+a;

if (ab === ba) {
    console.log(true);
} else {
    console.log(false);
}