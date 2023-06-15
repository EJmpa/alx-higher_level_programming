#!/usr/bin/node
/**
 * Check the parameters provided
 */
class Rectangle {
  constructor(w, h) {
    if (w <= 0 || h <= 0 || !Number.isInteger(w) || !Number.isInteger(h)) {
      return {}; // Return an empty object if the conditions are not met
    }

    this.width = w;
    this.height = h;
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

  rotate() {
    if (Object.keys(this).length === 0) {
      return; // Return if the object is empty
    }

    [this.width, this.height] = [this.height, this.width];
  }

  double() {
    if (Object.keys(this).length === 0) {
      return; // Return if the object is empty
    }

    this.width *= 2;
    this.height *= 2;
  }
}
module.exports = Rectangle;
