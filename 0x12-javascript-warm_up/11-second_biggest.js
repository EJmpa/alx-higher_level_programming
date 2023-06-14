#!/usr/bin/node
const args = process.argv.slice(2);
const numbers = args.map(arg => parseInt(arg));

if (numbers.length === 0) {
  console.log(0);
} else if (numbers.length === 1) {
  console.log(0);
} else {
  numbers.sort((a, b) => b - a);
  console.log(numbers[1]);
}
