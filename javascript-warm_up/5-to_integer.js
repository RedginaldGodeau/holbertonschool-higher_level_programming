#!/usr/bin/node
import { argv } from 'node:process'

let intArg = parseInt(argv[0]);

if (intArg)
    console.log(`My number: ${intArg}`)
else
    console.log("Not a number")