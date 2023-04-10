#!/usr/bin/node
const argv = process.argv.splice(2);
const args = argv.map(Number);

console.log(Math.max.apply(null, args));
