#!/usr/bin/node
/* 6-completed_tasks.js */

const request = require('request');
const url = process.argv[2];
request.get(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    computeTasks(body);
  }
});

function computeTasks (body) {
  const usersObj = Object();
  const tasksByUser = JSON.parse(body);
  for (let userTask in tasksByUser) {
    let userId = tasksByUser[userTask].userId.toString();
    if (tasksByUser[userTask].completed) {
      if (usersObj[userId] === undefined) {
        usersObj[userId] = 1;
      } else {
        usersObj[userId]++;
      }
    }
  }
  console.log(usersObj);
}
