#!/usr/bin/node
/* 4-starwars_count.js */

const request = require('request');
const wedgeAntilles = 'https://swapi.co/api/people/18/';
let count = 0;
let url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (body) {
    body = JSON.parse(body);
    let films = body.results;
    for (let film = 0; film < films.length; film++) {
      let characters = films[film].characters;
      if (characters.indexOf(wedgeAntilles) > -1) {
        count++;
      }
    }
    console.log(count);
  }
});
