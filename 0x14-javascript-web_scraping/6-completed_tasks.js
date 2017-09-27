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
  for (let i = 1; i < 11; i++) {
    usersObj[i.toString(10)] = 0;
  }
  const tasksByUser = JSON.parse(body);
  for (let userTask in tasksByUser) {
    let userId = tasksByUser[userTask].userId.toString();
    if (tasksByUser[userTask].completed) {
      usersObj[userId]++;
    }
  }
  console.log(usersObj);
}
