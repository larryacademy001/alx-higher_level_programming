#!/usr/bin/node
//  prints all characters of a Star Wars movie.

const request = require('request');
const filmID = process.argv[2];
const apiURL = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

request.get(apiURL, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const result = JSON.parse(body);
    const characters = result.characters;
    // console.log(characters);
    for (const character of characters) {
      request.get(character, (error, response, body) => {
        if (error) {
          console.log(error);
        } else {
          const names = JSON.parse(body);
          console.log(names.name);
        }
      });
    }
  }
});
