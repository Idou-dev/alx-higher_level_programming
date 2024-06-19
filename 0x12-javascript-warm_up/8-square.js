#!/usr/bin/node
let i = 0;
const args = process.argv;
if (isNaN(args[2])) console.log('Missing size');
else {
  while (i < parseInt(args[2])) {
    let j = 0;
    while (j < parseInt(args[2])) {
      process.stdout.write('X');
      if (j === args[2] - 1) process.stdout.write('\n');
      j++;
    }
    i++;
  }
}
