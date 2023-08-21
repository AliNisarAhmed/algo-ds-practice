function generatePerfectSquares(n) {
  const size = Math.floor(Math.sqrt(n));

  return new Set(Array.from(Array(size), (_x, i) => Math.pow(i + 1, 2)));
}

function numSquares(n) {
  const perfectSquares = generatePerfectSquares(n);

  let level = 0;
  let queue = new Set();
  queue.add(n);

  while (queue.size > 0) {
    level += 1;
    let nextQueue = new Set();

    for (let remainder of queue) {
      for (let square of perfectSquares) {
        if (remainder == square) {
          return level;
        }

        if (remainder < square) {
          break;
        }

        nextQueue.add(remainder - square);
      }
    }

    queue = nextQueue;
  }

  return level;
}

function numSquares_greedy(n) {
  const perfectSquares = generatePerfectSquares(n);

  for (let count = 1; count <= n; count++) {
    if (isDividedBy(n, count)) {
      return count;
    }
  }

  function isDividedBy(n, count) {
    if (count === 1) {
      return perfectSquares.has(n);
    }

    for (let square of perfectSquares) {
      if (isDividedBy(n - square, count - 1)) {
        return true;
      }
    }

    return false;
  }
}

function numSquares_dp(n) {
  const perfectSquares = generatePerfectSquares(n);

  const dp = Array.from({ length: n + 1 }, () => Number.POSITIVE_INFINITY);
  dp[0] = 0;

  for (let i = 1; i <= n; i++) {
    for (let square of perfectSquares) {
      if (i < square) {
        break;
      }

      dp[i] = Math.min(dp[i], dp[i - square] + 1);
    }
  }

  return dp[n];
}

function numSquares_brute_force(n) {
  const perfectSquares = generatePerfectSquares(n);

  return minNumSquares(n);

  function minNumSquares(k) {
    if (perfectSquares.includes(k)) {
      return 1;
    }

    let minNum = Number.POSITIVE_INFINITY;

    for (let square of perfectSquares) {
      if (k < square) {
        break;
      }

      let newNum = minNumSquares(k - square) + 1;
      minNum = Math.min(minNum, newNum);
    }

    return minNum;
  }
}
