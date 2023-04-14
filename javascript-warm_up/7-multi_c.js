#!/usr/bin/node
const argv = process.argv.splice(2);

if (parseInt(argv[0])) {
  for (let i = 0; i < parseInt(argv[0]); i++) { console.log('C is fun'); }
} else { console.log('Missing number of occurrences'); }
