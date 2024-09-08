#!/usr/bin/node
const argv = process.argv;
const request = require('request');

const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

function fetchMovieAndCharacters () {
  request(urlMovie, (error, response, body) => {
    if (!error && response.statusCode === 200) {
      const fbody = JSON.parse(body);
      const characters = fbody.characters;

      if (characters && characters.length > 0) {
        let index = 0;
        const fetchCharacter = () => {
          if (index < characters.length) {
            request(characters[index], (error, response, body) => {
              if (!error && response.statusCode === 200) {
                const character = JSON.parse(body);
                console.log(character.name);
                index++;
                fetchCharacter();
              }
            });
          }
        };
        fetchCharacter();
      }
    } else {
      console.error('error:', error || `Status Code: ${response.statusCode}`);
    }
  });
}

fetchMovieAndCharacters();
