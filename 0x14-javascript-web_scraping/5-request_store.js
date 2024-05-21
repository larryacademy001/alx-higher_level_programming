#!/usr/bin/node

const request = require('request');
const fs = require('fs');
const api_url = process.argv[2];
const file_path = process.argv[3];

request(api_url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file_path, body, 'utf-8');
  }
});
