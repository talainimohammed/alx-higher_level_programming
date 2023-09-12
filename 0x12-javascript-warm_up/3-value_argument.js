#!/usr/bin/node
const process = require('process');
let args = process.argv[2];
if (args === undefined) {
  console.log('No argument');
} else {
  console.log(args);
}
