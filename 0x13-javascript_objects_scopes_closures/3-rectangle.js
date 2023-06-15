#!/usr/bin/node
/**
 * Rectangle class
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    if (Object.keys(this).length === 0) {
      console.log("Empty object");
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log("X".repeat(this.width));
    }
  }
}
module.exports = Rectangle;
