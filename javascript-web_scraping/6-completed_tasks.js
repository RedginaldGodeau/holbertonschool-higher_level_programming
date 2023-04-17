#!/usr/bin/node
const argv = process.argv.splice(2);
const request = require('request');

request(`${argv[0]}?completed=true`, function (err, rep, body) {
  if (err) {
    console.log(err);
    return;
  }
  const data = JSON.parse(body);
  console.log(data);
});
