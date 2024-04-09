#!/usr/bin/node
let sba = process.argv.slice(2).map((x) => {
    return parseInt(x);
});
if (sba.length <= 1) {
    console.log(0);
} else {
    console.log(sba.sort((a, b) => {
	return b - a;
    })[1]);
}
