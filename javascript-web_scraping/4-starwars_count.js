#!/usr/bin/node
const argv = process.argv.splice(2);
const request = require('request');

request(`https://swapi-api.hbtn.io/api/people/18`, function (err, rep, body) {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data.length);
});
