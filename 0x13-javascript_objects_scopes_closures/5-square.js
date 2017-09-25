#!/usr/bin/node
/* 5-square.js */

module.exports = {
  Square: Square
};

const Rectangle = require('./4-rectangle').Rectangle;

function Square (size) {
  Rectangle.call(this, size, size);
}
