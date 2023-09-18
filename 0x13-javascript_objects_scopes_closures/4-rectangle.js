#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (printC = 'X') {
    let i;
    let j;
    let resp = '';
    for (i = 0; i < this.height; i++) {
      if (i > 0) {
        resp += '\n';
      }
      for (j = 0; j < this.width; j++) {
        resp += printC;
      }
    }
    console.log(resp);
  }

  rotate () {
    let tmp = this.width;
    this.width = this.height;
    this.height = tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
