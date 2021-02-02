#!/usr/bin/node
/* a script that searches the second biggest integer in the list of arguments */

const myArgs = process.argv.slice(2);
if (myArgs === undefined || myArgs.length === 0 || myArgs.length === 1) {
  console.log(0);
} else {
  let bigger = 1;
  let big = 0;
  let i;
  let w;
  for (i = 0; i < myArgs.length; i++) {
    w = parseInt(myArgs[i]);
    if (w > bigger) {
      big = bigger;
      bigger = w;
    } else if (w > big) {
      big = w;
    }
  }
  console.log(big);
}
