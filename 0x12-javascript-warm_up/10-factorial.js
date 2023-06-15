#!/usr/bin/node

function factorial (num) {
  return num ? num * factorial(num - 1) : 1;
}

const arg = parseInt(process.argv[2], 10);
console.log(arg ? factorial(arg) : 1);
