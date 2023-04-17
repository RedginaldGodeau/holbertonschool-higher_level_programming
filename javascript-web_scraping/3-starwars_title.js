#!/usr/bin/node
const argv = process.argv.splice(2);
const request = require('request');

request(`https://swapi-api.hbtn.io/api/films/${argv[0]}`, function (err, rep, body) {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);

  console.log(data.title);
});
