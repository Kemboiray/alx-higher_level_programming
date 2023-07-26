#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

// Make a request to the specified URL
request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    const characterCount = countCharacterAppearances(data);
    console.log(characterCount);
  }
});

// Count the number of times the specified character appears in the data
function countCharacterAppearances (data) {
  let count = 0;
  const characterUrl = 'https://swapi-api.alx-tools.com/api/people/18/';
  const films = data.results;
  for (const film of films) {
    if (film.characters.includes(characterUrl)) {
      count += 1;
    }
  }
  return count;
}
