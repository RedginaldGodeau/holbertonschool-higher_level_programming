#!/usr/bin/node
const argv = process.argv.splice(2);
const fs = require('fs');

fs.readFile(argv[0], 'utf8', (err, data) => {
  if (err) {
    console.log(err);
    return;
  }

  console.log(data);
});
