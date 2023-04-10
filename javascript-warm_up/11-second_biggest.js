#!/usr/bin/node
import { argv } from 'node:process';

const args = argv.map(parseInt);
console.log(Math.max(args));
