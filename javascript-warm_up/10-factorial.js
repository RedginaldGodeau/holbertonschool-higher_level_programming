#!/usr/bin/node
const argv = process.argv.splice(2);

if (!argv.length)
{
	console.log(1)
	return;
}

function fact (max = 1, n = 1, i = 1) {
	if (i >= max) { return n; }

  return fact(max, n * (i + 1), i+1);
};

console.log(fact(parseInt(argv[0])));
