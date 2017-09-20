#!/usr/bin/node
/* comment */
if (process.argv.length <= 3) {
  console.log('0');
} else {
  let argv = process.argv.slice(2);
  console.log(argv.sort()[argv.length - 2]);
}
