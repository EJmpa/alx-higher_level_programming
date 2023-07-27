#!/usr/bin/node

const request = require('request');

async function fetchCharacterData(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        const characterData = JSON.parse(body);
        resolve(characterData.name);
      }
    });
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./101-starwars_characters.js <Movie-ID>');
  process.exit(1);
}

const movieID = process.argv[2];
const url = `https://swapi.dev/api/films/${movieID}/`;

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const movie = JSON.parse(body);
      const characters = movie.characters;

      for (const characterUrl of characters) {
        try {
          const characterName = await fetchCharacterData(characterUrl);
          console.log(characterName);
        } catch (err) {
          console.error(err);
        }
      }
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  }
});
