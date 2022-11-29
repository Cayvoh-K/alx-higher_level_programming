#!/usr/bin/node
// Executes the function 'x' times
exports.callMeMoby = function (x, theFunction) {
  while (x-- > 0) {
    theFunction();
  }
};
