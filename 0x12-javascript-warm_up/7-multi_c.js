#!/usr/bin/node
/* a script that prints x times “C is fun” */

const myArg = process.argv[2];
let i;
if (!(isNaN(myArg))) {
  for (i = 0; i < parseInt(myArg); i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
