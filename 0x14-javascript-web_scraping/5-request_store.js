#!/usr/bin/node
/* 5-request_store.js */

const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const file = process.argv[3];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    writeBody(body);
  }
});

function writeBody (body) {
  fs.writeFile(file, body, 'utf8', function (err) {
    if (err) {
      console.log(err);
    }
  });
}
