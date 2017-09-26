#!/usr/bin/node
/* 10-converter.js */
exports.converter = function (base) {
  return function (num) {
    return num.toString(base);
  };
};
