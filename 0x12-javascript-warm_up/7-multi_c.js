#!/usr/bin/node
const proces = require('process');
let b = '';
let fail = 'Missing number of occurrences';
let number;
let i;

if (proces.argv.length > 2) {
  number = parseInt(proces.argv[2]);
  if (isNaN(number)) {
    b = fail;
  } else {
    for (i = 0; i < number; i++) {
      if (i > 0) {
        b += '\n';
      }
      b += 'C is fun';
    }
  }
} else {
  b = fail;
}
if (b !== '') {
  console.log(b);
}
