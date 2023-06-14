#!/usr/bin/node
const args = process.argv.slice(2).map(arg => parseInt(arg));
if (args.length <= 1) {
  console.log(0);
} else {
  const max = Math.max(...args);
  const secondMax = Math.max(...args.filter(arg => arg !== max));
  console.log(secondMax);
}
