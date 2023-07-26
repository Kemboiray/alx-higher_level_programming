#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    console.log(filter(data));
  }
});

function filter (obj) {
  let count = 0;
  const key = 'https://swapi-api.alx-tools.com/api/people/18/';
  const catalog = obj.results;
  for (const film of catalog) {
    if (film.characters.includes(key)) {
      count += 1;
    }
  }
  return count;
}
