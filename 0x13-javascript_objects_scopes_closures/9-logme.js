#!/usr/bin/node
/* 9-logme.js */
exports.logMe = function (item) {
  if (this.count === undefined) {
    this.count = 0;
  }
  console.log(this.count + ':', item);
  this.count++;
};
