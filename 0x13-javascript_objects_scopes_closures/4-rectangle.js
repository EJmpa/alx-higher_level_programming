#!/usr/bin/node
/**
 * Check the parameters provided
 */
class Rectangle {
  constructor (w, h) {
    if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (Object.keys(this).length === 0) {
      console.log("Empty object");
      return;
    }

    for (let i = 0; i < this.height; i++) {
      console.log("X".repeat(this.width));
    }
  }

  rotate () {
    if (Object.keys(this).length === 0) {
      return; // Return if the object is empty
    }

    [this.width, this.height] = [this.height, this.width];
  }

  double () {
    if (Object.keys(this).length === 0) {
      return; // Return if the object is empty
    }

    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
