#!/usr/bin/node
/* 3-starwars_title.js */

const request = require('request');
let episode = process.argv[2];
let url = 'http://swapi.co/api/films/' + episode;
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (body) {
    body = JSON.parse(body);
    console.log(body.title);
  }
});
