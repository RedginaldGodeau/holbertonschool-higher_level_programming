#!/usr/bin/node
let save = 0;

exports.logMe = function (item) {
  console.log(`${save}: ${item}`);
  save++;
};
