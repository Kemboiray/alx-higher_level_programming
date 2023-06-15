#!/usr/bin/node

if (process.argv.length < 4) { console.log(0); } else {
  const array = process.argv.slice(2);
  array.forEach(parseInt);
  for (let i = 0; i < 2; i++) {
    for (let j = i + 1; j < array.length; j++) {
      if (array[j] > array[i]) {
        const tmp = array[j];
        array[j] = array[i];
        array[i] = tmp;
      }
    }
  }
  console.log(array[1]);
}
