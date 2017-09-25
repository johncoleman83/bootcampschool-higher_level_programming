#!/usr/bin/node
/* 4-rectangle.js */

module.exports = {
  Rectangle: Rectangle
};

function Rectangle (w, h) {
  if (w > 0 && h > 0) {
    this.width = w;
    this.height = h;
  }

  this.print = function () {
    if (this.width && this.height) {
      for (let row = 0; row < this.height; row++) {
        console.log('X'.repeat(this.width));
      }
    }
  };

  this.rotate = function () {
    let temp = this.width;
    this.width = this.height;
    this.height = temp;
  };

  this.double = function () {
    this.width *= 2;
    this.height *= 2;
  };
}
