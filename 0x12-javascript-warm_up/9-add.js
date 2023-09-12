#!/usr/bin/node
const process = require('process');
let responce;
let number;
let number2;
responce = 'NaN';

if (process.argv.length > 3) {
  number = parseInt(process.argv[2]);
  number2 = parseInt(process.argv[3]);
  if (!isNaN(number) && !isNaN(number2)) {
    responce = String((number + number2));
  }
}
console.log(responce);
