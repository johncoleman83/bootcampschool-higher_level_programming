#!/usr/bin/node
/* 0-readme.js */

const fs = require('fs');
let file;
if (process.argv.length > 2) {
  file = process.argv[2];
} else {
  file = '';
}
fs.readFile(file, 'utf8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data.slice(0, data.length - 1));
  }
});
