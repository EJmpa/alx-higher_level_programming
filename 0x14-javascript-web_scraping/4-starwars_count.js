#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./4-starwars_count.js <API-URL>');
  process.exit(1);
}

const apiURL = process.argv[2];

request(apiURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const films = JSON.parse(body).results;
      const wedgeAntillesMovies = films.filter(movie => movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/'));
      console.log(wedgeAntillesMovies.length);
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  }
});
