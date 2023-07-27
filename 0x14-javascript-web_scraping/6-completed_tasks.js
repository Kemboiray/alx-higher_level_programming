#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (!error && response.statusCode === 200) {
    const users = JSON.parse(body);
    const completions = {};
    for (const user of users) {
      const userId = JSON.stringify(user.userId);
      if (userId in completions) {
        if (user.completed === true) {
          completions[userId] += 1;
        }
      } else {
        if (user.completed === true) {
          completions[userId] = 1;
        } else {
          completions[userId] = 0;
        }
      }
    }
    console.log(completions);
  } else {
    console.error(error);
  }
});
