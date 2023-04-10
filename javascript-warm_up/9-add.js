#!/usr/bin/node
const argv = process.argv.splice(2);
const add = (a, b) => console.log(a + b);

add(parseInt(argv[0]), parseInt(argv[1]));
