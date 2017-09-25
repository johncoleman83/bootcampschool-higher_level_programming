#!/usr/bin/node
/* 6-square.js */

module.exports = {
  Square: Square
};

const ParentSquare = require('./5-square').Square;

function Square (size) {
  ParentSquare.call(this, size, size);
  this.charPrint = function (c) {
    if (c === undefined) {
      c = 'X';
    }
    for (let col = 0; col < this.height; col++) {
      console.log(c.repeat(this.width));
    }
  };
}
