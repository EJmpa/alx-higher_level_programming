#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./100-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

const movieID = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characters = movie.characters;

      function printCharacters(characters) {
        if (characters.length === 0) {
          return;
        }

        const characterUrl = characters.shift();
        request(characterUrl, (error, response, body) => {
          if (error) {
            console.error(error);
          } else {
            if (response.statusCode === 200) {
              const character = JSON.parse(body);
              console.log(character.name);
              printCharacters(characters);
            } else {
              console.error(`Error: Status code ${response.statusCode}`);
            }
          }
        });
      }

      printCharacters(characters);
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  }
});
