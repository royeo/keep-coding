const Promise = require('bluebird');

let a = {
  b() {
    console.log(2);
  }
}

Promise.resolve([a]).each((i) => {
  console.log(i);
})