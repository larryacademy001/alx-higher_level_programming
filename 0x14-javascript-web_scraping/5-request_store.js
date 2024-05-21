#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const apiURL = process.argv[2];
const filePath = process.argv[3];

request(apiURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(filePath, body, 'utf-8');
  }
});
