#!/usr/bin/node
const fa = parseInt(process.argv[2]);
const sa = parseInt(process.argv[3]);
function add (a, b) {
    if (isNaN(a) || isNaN(b)) {
	return NaN;
    }
    return a + b;
}
console.log(add(fa, sa));