#!/usr/bin/node
/* comment */
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
