#!/usr/bin/node

const request = require('request');

// Function to make a request and return a promise
function makeRequest (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else if (response.statusCode !== 200) {
        reject(new Error(`Status: ${response.statusCode}`));
      } else {
        resolve(body);
      }
    });
  });
}

// Function to fetch and print characters for a given movie ID
async function fetchCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  try {
    const filmData = await makeRequest(url);
    const characters = JSON.parse(filmData).characters;

    // Fetching and printing character names sequentially
    for (const characterUrl of characters) {
      const characterData = await makeRequest(characterUrl);
      console.log(JSON.parse(characterData).name);
    }
  } catch (error) {
    console.error('Error:', error.message);
  }
}

// Main script
if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <movieId>');
  process.exit(1);
}

const movieId = process.argv[2];
fetchCharacters(movieId);
