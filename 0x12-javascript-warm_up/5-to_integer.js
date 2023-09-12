#!/usr/bin/node
const proces = require('process');
let response;
let number;
response = 'Not a number';
if (proces.argv.length > 2) {
  number = parseInt(proces.argv[2]);
  if (!isNaN(number)) {
    response = 'My number: ' + String(number);
  }
}
console.log(response);
