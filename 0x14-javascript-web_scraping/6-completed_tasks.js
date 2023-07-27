#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error) {
    const users = JSON.parse(body);
    const completions = {};
    for (const user of users) {
      const userId = String(user.userId);
      if (userId in completions) {
        if (user.completed === true) {
          completions[userId] += 1;
        }
      } else if (user.completed === true) {
        completions[userId] = 1;
      }
    }
    console.log(completions);
  } else {
    console.error(error);
  }
});
