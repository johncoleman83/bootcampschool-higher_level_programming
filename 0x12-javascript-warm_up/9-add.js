#!/usr/bin/node
/* comment */
function add (a, b) {
  return a + b;
}
if (!isNaN(process.argv[2]) && !isNaN(process.argv[3])) {
  const one = parseInt(process.argv[2]);
  const two = parseInt(process.argv[3]);
  let sum = add(one, two);
  console.log(sum);
} else {
  console.log(NaN);
}
