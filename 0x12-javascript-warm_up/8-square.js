#!/usr/bin/node
/* comment */
if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  const size = parseInt(process.argv[2]);
  for (let i = 0; i < size; i++) {
    console.log(Array(size + 1).join('X'));
  }
}
