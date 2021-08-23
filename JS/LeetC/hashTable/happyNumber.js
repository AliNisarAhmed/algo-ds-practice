

function isHappy(n) {
  // using floyd's cycle finding algorithm in a linked list 

  let slowRunner = n; 
  let fastRunner = sumOfDigitsSquared(n); 

  while (fastRunner !== 1 && slowRunner !== fastRunner) {
    slowRunner = sumOfDigitsSquared(slowRunner);
    fastRunner = sumOfDigitsSquared(sumOfDigitsSquared(fastRunner));
  }

  return fastRunner === 1;

}

// T = O(n), space compexity O(log(n))
function isHappy(n) {
  let set = new Set();

  let res = sumOfDigitsSquared(n);

  while (res !== 1) {
    if (!set.has(res)) {
      set.add(res);
    } else {
      return false;
    }

    res = sumOfDigitsSquared(res);
  }

  return true;
}

function sumOfDigitsSquared(n) {
  let digits = getDigits(n);
  return digits.reduce((acc, x) => acc + x * x, 0);
}

function getDigits(n) {
  let res = [];

  while (n > 0) {
    let d = n % 10;
    res.push(d);
    n = Math.floor(n / 10);
  }

  return res;
}
