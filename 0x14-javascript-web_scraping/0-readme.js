#!/usr/bin/node
/* a script that reads and prints the content of a file. */

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (err, data) {
  if (data) {
    console.log(data);
  } else {
    return console.log(err);
  }
});