#!/usr/bin/node
/* 2-rectangle.js */

module.exports = {
  Rectangle: Rectangle
};

function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }
}
