#!/usr/bin/node
const argv = process.argv.splice(2);

const square = parseInt(argv[0]);

if (square) {
  for (let i = 0; i > square; i++) { console.log('x'.repeat(square)); }
} else { console.log('Missing size'); }
