#!/usr/bin/node

const request = require('request');
const fs = require('fs');

request(process.argv[2], function (_error, _res, bd) {
  fs.writeFile(process.argv[3], bd, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
