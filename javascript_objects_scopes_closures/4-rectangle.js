#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < h; i++) { console.log('X'.repeat(w)); }
  }

  double () {
    for (let i = 0; i < h * 2; i++) { console.log('X'.repeat(w * 2)); }
  }

  rotate () {
    for (let i = 0; i < w * 2; i++) { console.log('X'.repeat(h * 2)); }
  }
}

module.exports = Rectangle;
