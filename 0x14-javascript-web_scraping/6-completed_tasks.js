#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./6-completed_tasks.js <API-URL>');
  process.exit(1);
}

const apiURL = process.argv[2];

request(apiURL, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    if (response.statusCode === 200) {
      const tasks = JSON.parse(body);
      const completedTasksByUser = {};

      tasks.forEach((task) => {
        if (task.completed) {
          if (completedTasksByUser[task.userId]) {
            completedTasksByUser[task.userId]++;
          } else {
            completedTasksByUser[task.userId] = 1;
          }
        }
      });

      console.log(completedTasksByUser);
    } else {
      console.error(`Error: Status code ${response.statusCode}`);
    }
  }
});
