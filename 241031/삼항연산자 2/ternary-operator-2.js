const fs = require("fs");

let a = Number(fs.readFileSync(0).toString().trim());

if (a == 1) {
    console.log("t");
} else {
    console.log("f");
}