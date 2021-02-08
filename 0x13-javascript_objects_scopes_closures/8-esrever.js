#!/usr/bin/node
/* a function that returns the reversed version of a list: */

exports.esrever = function (list) {
  const copyList = [];
  let i;
  for (i = list.length - 1; i >= 0; i--) {
    copyList.push(list[i]);
  }
  return (copyList);
};
