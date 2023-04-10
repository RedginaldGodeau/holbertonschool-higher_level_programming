#!/usr/bin/node
const argv = process.argv;

const intArg = parseInt(argv[0]);

if (intArg) { console.log(`My number: ${intArg}`); } else { console.log('Not a number'); }
