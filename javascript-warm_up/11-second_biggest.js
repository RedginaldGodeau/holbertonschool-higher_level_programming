#!/usr/bin/node
const argv = process.argv.splice(2);

const args = argv.map(parseInt);
console.log(Math.max(args));
