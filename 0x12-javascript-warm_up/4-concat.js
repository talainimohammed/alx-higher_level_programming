#!/usr/bin/node
const proces = require('process');

let value1;
let value2;
if (proces.argv.length > 2) {
  if (proces.argv.length > 3) {
    value2 = proces.argv[3];
  }
  value1 = proces.argv[2];
}
console.log(value1 + ' is ' + value2);
