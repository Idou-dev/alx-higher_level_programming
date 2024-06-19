#!/usr/bin/node
let x = 0;
const args = process.argv;
if (isNaN(args[2])) {
  console.log('Missing number of occurrences');
} else {
  while (x < parseInt(args[2])) {
    console.log('C is fun');
    x++;
  }
}
