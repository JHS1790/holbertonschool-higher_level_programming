#!/usr/bin/node
/* a script that prints My number: <first argument converted in integer> if the first argument can be converted to an integer */

const myArg = process.argv[2];
if (!(isNaN(myArg))) {
  console.log(parseInt(myArg));
} else {
  console.log('Not a number');
}
