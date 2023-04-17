#!/usr/bin/node
const argv = process.argv.splice(2);
const request = require('request');
const fs = require('fs');

request(argv[0], function (err, rep, body) {
  if (err) {
    console.log(err);
    return;
  }
  const data = body;

  fs.writeFile(argv[1], data, { encoding: 'utf8' }, (err, data) => {
    if (err) {
      console.log(err);
    }
  });
});
