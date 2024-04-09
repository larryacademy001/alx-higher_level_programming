#!/usr/bin/node
const fa = process.argv[2];
if (fa === undefined) {
    console.log('No argument');
} else {
    console.log(fa);
}