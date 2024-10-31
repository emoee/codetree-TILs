const fs = require("fs");
let n = Number(fs.readFileSync(0).toString().trim());
let cnt = 0;
let avg = 0;

while (1) {
    cnt++;
    if (n%2 === 0){
        n = (n*3)+1;
    } else {
        n = (n*2)+2;
    }

    if (n > 1000)
        break;
}
console.log(cnt);