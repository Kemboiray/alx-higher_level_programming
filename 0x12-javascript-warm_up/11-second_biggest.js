#!/usr/bin/node

if (process.argv.length < 4) {
  console.log(0);
} else {
  const array = process.argv.slice(2);
  const len = array.length;
  for (let i = 0; i < len; i++) {
    array[i] = parseInt(array[i], 10);
  }
  for (let i = 0; i < 2; i++) {
    for (let j = i + 1; j < len; j++) {
      if (array[j] > array[i]) {
        const temp = array[j];
        array[j] = array[i];
        array[i] = temp;
      }
    }
  }
  console.log(array[1]);
}
