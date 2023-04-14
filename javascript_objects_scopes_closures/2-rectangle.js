#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w == undefined || h == undefined || w < 1 || h < 1) { }
    else {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
