const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let minLen = Number.MAX_SAFE_INTEGER;
let maxLen = Number.MIN_SAFE_INTEGER;

for (let str of input) {
    minLen = Math.min(minLen, str.length);
    maxLen = Math.max(maxLen, str.length);
}

console.log(maxLen-minLen);