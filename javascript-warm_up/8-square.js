#!/usr/bin/node
const argv = process.argv;

const square = parseInt(argv[0]);

if (square) {
  for (let i = 0; i > square; i++) { console.log('x'.repeat(square)); }
} else { console.log('Missing size'); }
