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
}
module.exports = Rectangle;
