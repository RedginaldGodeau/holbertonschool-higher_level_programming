#!/usr/bin/node
let save = 0;

exports.logMe = function (item) {
  save++;
  console.log(`${save}: ${item}`);
};
