#!/usr/bin/node
const process = require('process');
const request = require('request');
let order = [];
let resp = {};

function getCharName (charUrl) {
  let val;
  val = request(charUrl, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      let data = JSON.parse(body);
      val = data['name'];
      resp[charUrl] = val;
    }
  });
}

function doParse () {
  let movieID = process.argv[2];
  let apiURL = 'https://swapi.co/api/films/' + movieID;

  request(apiURL, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      let data = JSON.parse(body);
      data['characters'].forEach(function (charUrl) {
        order.push(charUrl);
        getCharName(charUrl);
      });
    }
  });
}

doParse();
setTimeout(function () {
  // some stuff
  order.forEach(function (apiURL) {
    console.log(resp[apiURL]);
  });
}, 5000);
