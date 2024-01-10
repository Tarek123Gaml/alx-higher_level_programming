#!/usr/bin/node
// that prints a message depending of the number of arguments passed

if (process.argv.lenth === 2) {
  console.log('No argument');
} else if (process.argv.lenth === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
