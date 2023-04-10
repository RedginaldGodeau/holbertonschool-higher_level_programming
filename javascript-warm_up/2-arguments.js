#!/usr/bin/node
const argv = process.argv.splice(2);

if (argv.length) {
  console.log(argv.length > 1 ? "Arguments found" : "Argument found");
} else {
  console.log("No argument");
}
