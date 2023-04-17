#!/usr/bin/node
const argv = process.argv.splice(2);
const fs = require('fs');
const path = require('path');

const url = path.resolve(argv[0]);

fs.writeFile(url, argv[1], { encoding: 'utf8' }, (err, data) => {
  if (err) {
    console.log(err);
  }
});
