#!/usr/bin/node
const argv = process.argv.splice(2);

if (argv.length) { console.log('Argument found'); } else { console.log('No argument'); }
