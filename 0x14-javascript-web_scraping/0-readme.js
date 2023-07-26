#!/usr/bin/node

const fs = require('fs');

function printFileContent(filePath) {
  fs.readFile(filePath, 'utf-8', (error, data) => {
    if (error) {
      console.log(error);
    } else {
      console.log(data);
    }
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: ./0-readme.js <file-path>');
  process.exit(1);
}

const filePath = process.argv[2];
printFileContent(filePath);
