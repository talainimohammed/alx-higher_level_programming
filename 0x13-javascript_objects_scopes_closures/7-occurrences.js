#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let j = 0;
  list.forEach(function (obj) {
    if (obj === searchElement) {
      j++;
    }
  });
  return j;
};
