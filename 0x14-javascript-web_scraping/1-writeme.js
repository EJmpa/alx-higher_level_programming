#!/usr/bin/node

const fs = require('fs');

function writeFileContent(filePath, content) {
  fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
      console.error(err);
    }
  });
}

if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file-path> <content>');
  process.exit(1);
}

const filePath = process.argv[2];
const content = process.argv[3];

writeFileContent(filePath, content);
