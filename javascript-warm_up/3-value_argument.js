#!/usr/bin/node
import { argv } from 'node:process';

if (argv) { console.log(argv[0]); } else { console.log('No argument'); }
