#!/usr/bin/node
/* 8-esrever.js */
exports.esrever = function (list) {
  let end = list.length - 1;
  for (let i = 0; i < list.length / 2; i++, end--) {
    [list[i], list[end]] = [list[end], list[i]];
  }
  return list;
};
