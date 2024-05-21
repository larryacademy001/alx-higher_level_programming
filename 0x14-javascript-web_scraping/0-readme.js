#!/usr/bin/node

const fileSys = require('fs');
const filePath = process.argv[2];

fileSys.readFile(filePath, 'utf-8', function (error, content) {
  if (error) {
    console.log(error);
  } else {
    console.log(content);
  }
});
