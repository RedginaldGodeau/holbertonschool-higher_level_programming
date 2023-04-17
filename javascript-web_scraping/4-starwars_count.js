#!/usr/bin/node
const argv = process.argv.splice(2);
const request = require('request');

request(`${argv[0]}/18`, function (err, rep, body) {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);

  console.log(data.films.length);
});
