#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) { console.log('X'.repeat(this.width)); }
  }

  double () {
    for (let i = 0; i < this.height * 2; i++) { console.log('X'.repeat(this.width * 2)); }
  }

  rotate () {
    for (let i = 0; i < w * 2; i++) { console.log('X'.repeat(this.height * 2)); }
  }
}

class Square extends Rectangle {
  constructor (w) {
    super().width = w;
    super().height = w;
  }

  charPrint (c) {
    if (c == undefined) { c = 'X'; }

    for (let i = 0; i < this.height; i++) { console.log(c.repeat(this.width)); }
  }
}

module.exports = { Rectangle, Square };
