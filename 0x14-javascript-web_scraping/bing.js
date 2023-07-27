#!/usr/bin/node

const request = require('request');
const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
  if (error) throw error;
  const todos = JSON.parse(body);
  const completedTasks = {};
  todos.forEach((todo) => {
    if (todo.completed) {
      if (completedTasks[todo.userId]) {
        completedTasks[todo.userId] += 1;
      } else {
        completedTasks[todo.userId] = 1;
      }
    }
  });
  //  for (const userId in completedTasks) {
  //    console.log(`User ${userId}: ${completedTasks[userId]}`);
  //  }
  console.log(completedTasks);
});
