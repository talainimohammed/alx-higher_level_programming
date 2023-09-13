#!/usr/bin/node
exports.esrever = function (list) {
  let newList = [];
  let j;
  for (j = list.length - 1; j >= 0; j--) {
    newList.push(list[j]);
  }
  return newList;
};
