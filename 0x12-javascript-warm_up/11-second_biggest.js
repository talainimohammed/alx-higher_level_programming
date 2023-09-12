#!/usr/bin/node
const process = require('process');
let max1;
let max2;

process.argv.forEach(function (value, index) {
  value = parseInt(value);
  if (index > 1) {
    if (max1 === undefined) {
      max1 = value;
    } else if (max2 === undefined && value <= max1) {
      max2 = value;
    } else if (value >= max1) {
      max2 = max1;
      max1 = value;
    }
  }
});
if (max2 === undefined) {
  console.log(0);
} else {
  console.log(max2);
}
