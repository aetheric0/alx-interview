#!/usr/bin/node
const request = require('request');
const argOne = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${argOne}/?format=json`;
request(url, function (error, response, body) {
  if (error) {
    console.error('External API Request Error: ', error);
    return;
  }
  try {
    const film = JSON.parse(body);
    const characters = film.characters;

    // Function to fetch character names in order
    const fetchCharacterName = (url, index) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
            return;
          }
          const characterName = JSON.parse(body).name;
          resolve({ index, characterName });
        });
      });
    };

    const characterPromises = characters.map((character, index) => fetchCharacterName(character, index));

    Promise.all(characterPromises)
      .then(results => {
        results.sort((a, b) => a.index - b.index); // Sort by original index
        results.forEach(result => console.log(result.characterName));
      })
      .catch(error => console.error(error));
  } catch (error) {
    console.error('Code Error: ', error);
  }
});
