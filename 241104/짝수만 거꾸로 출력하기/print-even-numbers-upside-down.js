const fs = require("fs");
let input = fs.readFileSync(0).toString().trim().split("\n");
let n = Number(input[0]);
let arr = input[1].split(" ");
let resultArr = [];

arr.forEach((value) => {
    if (Number(value)%2 === 0)
        resultArr.push(value);
})

resultArr.reverse();
console.log(resultArr.join(" "));