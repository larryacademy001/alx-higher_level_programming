#!/usr/bin/node

const fileSys = require('fs');
const filePath = process.argv[2];
const string = process.argv[3];

fileSys.writeFile(filePath, string, 'utf-8', function (error) {
  if (error) console.log(error);
});
