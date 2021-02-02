#!/usr/bin/node
/* a script that computes and prints a factorial */

const myArg = process.argv[2];
function factorial (a) {
  a = parseInt(a);
  if (isNaN(a) || a === 1) {
    return 1;
  } else {
    return factorial(a - 1) * a;
  }
}
console.log(factorial(myArg));
