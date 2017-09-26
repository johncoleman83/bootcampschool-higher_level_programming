#!/usr/bin/node
/* 2-statuscode.js */

const request = require('request');
let url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  if (response) {
    let code = response.statusCode;
    console.log('code:', code);
  }
});
