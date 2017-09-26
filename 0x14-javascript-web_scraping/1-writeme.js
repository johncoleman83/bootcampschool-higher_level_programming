#!/usr/bin/node
/* 1-writeme.js */

const fs = require('fs');
let file;
let data;
if (process.argv.length > 3) {
  file = process.argv[2];
  data = process.argv[3];
} else {
  file = '';
  data = '';
}
fs.writeFile(file, data, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
