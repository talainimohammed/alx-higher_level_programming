#!/usr/bin/node
const process = require('process');
let resp = '';
let fail = 'Missing size';
let number;
let i;
let j;

if (process.argv.length > 2) {
  number = parseInt(process.argv[2]);
  if (isNaN(number)) {
    resp = fail;
  } else {
    for (i = 0; i < number; i++) {
      if (i > 0) {
        resp += '\n';
      }
      for (j = 0; j < number; j++) {
        resp += 'X';
      }
    }
  }
} else {
  resp = fail;
}
if (resp !== '') {
  console.log(resp);
}
