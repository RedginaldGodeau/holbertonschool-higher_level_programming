#!/usr/bin/node
const argv = process.argv;

const fact = (max = 1, n = 1) => {
  if (n >= max) { return n; }

  return fact(max, n * (n + 1));
};

console.log(fact(parseInt(argv[0])));
