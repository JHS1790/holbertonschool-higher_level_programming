#!/usr/bin/node
/*
  class Square that defines a square and
  inherits from Square of 5-square.js
*/

const square = require('./5-square.js');

class Square extends square {
  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.width));
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
