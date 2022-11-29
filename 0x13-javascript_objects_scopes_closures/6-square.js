#!/usr/bin/node

const SquareB = require('./5-square');
module.exports = class Square extends Squares {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    process.stdout.write((c.repeat(this.width) + '\n').repeat(this.height));
  }
};
