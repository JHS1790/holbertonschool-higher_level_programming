#!/usr/bin/node
/* a script that prints a square */

const myArg = process.argv[2];
let i, j;
if (!(isNaN(myArg))) {
  let row = '';
  for (i = 0; i < parseInt(myArg); i++) {
    row = row + 'X';
  }
  for (j = 0; j < parseInt(myArg); j++) {
    console.log(row);
  }
} else {
  console.log('Missing size');
}
