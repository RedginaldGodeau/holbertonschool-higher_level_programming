#!/usr/bin/node
const argv = process.argv;

const args = argv.map(parseInt);
console.log(Math.max(args));
