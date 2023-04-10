#!/usr/bin/node
import { argv } from 'node:process';

const intArg = parseInt(argv[0]);

if (intArg) { console.log(`My number: ${intArg}`); } else { console.log('Not a number'); }
