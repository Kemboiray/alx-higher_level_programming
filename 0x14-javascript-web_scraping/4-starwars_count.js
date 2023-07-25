#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18';

request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const films = data.results.filter(film => film.characters.includes(characterUrl));
    console.log(films.length);
  }
});
