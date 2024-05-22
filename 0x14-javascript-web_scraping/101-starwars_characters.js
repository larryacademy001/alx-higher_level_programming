#!/usr/bin/node
const process = require('process');
const request = require('request');
const order = [];
const resp = {};

function getCharName (charUrl) {
  let val;
  val = request(charUrl, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
      val = data['name'];
      resp[charUrl] = val;
    }
  });
}

function doParse () {
  const movieID = process.argv[2];
  const apiURL = 'https://swapi.co/api/films/' + movieID;

  request(apiURL, function (error, response, body) {
    if (error != null) {
      console.log(error);
    } else {
      const data = JSON.parse(body);
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
