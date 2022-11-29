#!/usr/bin/node

const Rectangle = require('./4-rectanglee');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
