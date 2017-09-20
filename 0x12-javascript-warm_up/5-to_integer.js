#!/usr/bin/node
/* comment */
if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number is: ' + parseInt(process.argv[2]));
}
