#!/usr/bin/node
/* 4-starwars_count.js */

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(0);
  }
  if (response && body) {
    findWedgeAntilles(response, body);
  }
});

function findWedgeAntilles (response, body) {
  const wedgeAntilles = '18';
  let count = 0;
  if (response.headers['content-type'] === 'application/json') {
    body = JSON.parse(body);
    let results = body.results;
    for (let result in results) {
      let characters = results[result].characters;
      if (characters) {
        for (let person in characters) {
          if (characters[person].includes(wedgeAntilles)) {
            count++;
          }
        }
      }
    }
  }
  console.log(count);
}
