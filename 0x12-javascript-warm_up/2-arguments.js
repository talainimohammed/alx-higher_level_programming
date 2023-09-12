#!/usr/bin/node
const proces = require('process');
let response;
if (proces.argv.length === 3) {
  response = 'Argument found';
} else if (proces.argv.length < 3) {
  response = 'No argument';
} else {
  response = 'Arguments found';
}
console.log(resp);
