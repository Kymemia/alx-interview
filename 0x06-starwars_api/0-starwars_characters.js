#!/usr/bin/node
const argv = process.argv;
const axios = require('axios');

const urlFilm = 'https://swapi-api.hbtn.io/api/films/';
const urlMovie = `${urlFilm}${argv[2]}/`;

async function fetchMovieAndCharacters () {
  try {
    const { data: fbody } = await axios.get(urlMovie);
    const characters = fbody.characters;

    if (characters && characters.length > 0) {
      const characterPromises = characters.map((url) => axios.get(url));
      const responses = await Promise.all(characterPromises);

      responses.forEach((response) => {
        console.log(response.data.name);
      });
    }
  } catch (error) {
    console.error('error:', error);
  }
}

fetchMovieAndCharacters();
