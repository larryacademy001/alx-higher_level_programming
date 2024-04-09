#!/usr/bin/node
const na = process.argv.length - 2;
if (na === 0) {
    console.log('No argument');
} else if (na === 1) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
