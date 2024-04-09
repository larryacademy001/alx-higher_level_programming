#!/usr/bin/node
const ca = parseInt(process.argv[2]);
if (isNaN(ca)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + ca);
}
