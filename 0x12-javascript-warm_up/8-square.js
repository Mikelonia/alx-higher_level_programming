#!/usr/bin/node
//By Okpako Michael
const argum = process.argv[2];
if (isNaN(argum)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < parseInt(argum); i++) {
    console.log('X'.repeat(parseInt(argum)));
  }
}
