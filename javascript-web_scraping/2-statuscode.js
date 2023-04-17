#!/usr/bin/node
const argv = process.argv.splice(2);
const request = require('request');

request(argv[0], function (error, response, body) {
  console.log('code:', response && response.statusCode);
});
