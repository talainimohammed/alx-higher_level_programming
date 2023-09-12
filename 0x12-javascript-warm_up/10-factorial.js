#!/usr/bin/node
const process = require('process');

function factorial (number) {
  if (isNaN(number)) {
    return 1;
  }
  if (number < 0) {
    return -1;
  } else if (number === 0) {
    return 1;
  } else {
    return (number * factorial(number - 1));
  }
}

console.log(factorial(parseInt(process.argv[2])));
