#!/usr/bin/node
const argv = process.argv.splice(2);

if (argv.length) { console.log(argv[0]); } else { console.log('No argument'); }
