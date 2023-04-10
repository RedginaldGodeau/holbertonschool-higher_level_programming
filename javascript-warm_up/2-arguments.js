#!/usr/bin/node
const argv = process.argv.splice(2);

if (argv.length > 0) { console.log('Argument found'); } else { console.log('No argument'); }
