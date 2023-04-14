#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w == undefined || h == undefined || w < 1 || h < 1) { }
    else {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < h; i++) { console.log('X'.repeat(w)); }
  }
}

module.exports = Rectangle;
