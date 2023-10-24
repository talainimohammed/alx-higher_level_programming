#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, _res, bd) {
  if (error) {
    console.log(error);
  } else {
    const completedTasksByUsers = {};
    bd = JSON.parse(bd);

    for (let i = 0; i < bd.length; ++i) {
      const userId = bd[i].userId;
      const completed = bd[i].completed;

      if (completed && !completedTasksByUsers[userId]) {
        completedTasksByUsers[userId] = 0;
      }

      if (completed) ++completedTasksByUsers[userId];
    }

    console.log(completedTasksByUsers);
  }
});
