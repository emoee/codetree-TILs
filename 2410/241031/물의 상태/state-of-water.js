const fs = require("fs");

let water = Number(fs.readFileSync(0).toString().trim());

if (water >= 100) {
    console.log("vapor");
} else if (water < 0 ){
    console.log("ice");
} else {
    console.log("water")
}