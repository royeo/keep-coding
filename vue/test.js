const BBPromise = require('bluebird');

async function func() {
  return await console.log(1);
}

async function funb() {
  return await console.log(2);
}

BBPromise.join(func(), funb())