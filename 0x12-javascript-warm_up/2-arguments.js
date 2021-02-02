#!/usr/bin/node
/* a script that prints a message depending of the number of arguments passed */

const myArgs = process.argv.slice(2);
if (typeof myArgs[1] !== 'undefined') {
  console.log('Arguments found');
} else if (typeof myArgs[0] !== 'undefined') {
  console.log('Argument found');
} else {
  console.log('No argument');
}
