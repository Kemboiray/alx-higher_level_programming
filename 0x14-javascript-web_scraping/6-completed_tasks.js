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
    print(completions);
  } else {
    console.error(error);
  }
});

function print (obj) {
  if (Object.keys(obj).length === 0) {
    console.log('{}');
  } else {
    console.log(`{ '${Object.keys(obj)[0]}': ${Object.values(obj)[0]},`);
    for (const key of Object.keys(obj).slice(1, -1)) {
      console.log(`  '${key}': ${obj[key]},`);
    }
    console.log(`  '${Object.keys(obj).slice(-1)}': ${Object.values(obj).slice(-1)} }`);
  }
}
