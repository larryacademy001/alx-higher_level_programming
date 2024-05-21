#!/usr/bin/node

const file_sys = require('fs');
const file_path = process.argv[2];

file_sys.readFile(file_path, 'utf-8', function (error, content) {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
