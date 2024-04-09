#!/usr/bin/node
const ss = parseInt(process.argv[2]);
if (isNaN(ss)) {
    console.log('Missing size');
} else {
    for (let i = 0; i < ss; i++) {
	console.log('X'.repeat(ss));
    }
}
