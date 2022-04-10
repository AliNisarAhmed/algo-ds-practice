function uniquePaths(m, n) {
  if (m === 0) return 1;
  if (n === 0) return 1;
  return uniquePaths(m - 1, n) + uniquePaths(m, n - 1);
}

// iterative - Dynamic Programming

function uniquePaths(m, n) {
  let d = Array.from({ length: m }, () => Array.from({ length: n }, () => 1));

  for (let col = 1; col < m; col++) {
    for (let row = 1; row < n; row++) {
      d[col][row] = d[col - 1][row] + d[col][row - 1];
    }
  }

  return d[m - 1][n - 1];
}
