#!/usr/bin/node

const file_sys = require('fs');
const file_path = process.argv[2];
const string = process.argv[3];

file_sys.writeFile(file_path, string, 'utf-8', function (error) {
  if (error) console.log(error);
});
