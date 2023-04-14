#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  return list.slice(searchElement).length - 1;
};
