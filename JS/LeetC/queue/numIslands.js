const DIRECTIONS = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

function numIslands(grid) {
  const M = grid.length;
  const N = grid[0].length;

  let count = 0;

  for (let row = 0; row < M; row++) {
    for (let col = 0; col < N; col++) {
      if (grid[row][col] === "1") {
        count++;
        dfs(row, col);
      }
    }
  }

  return count;

  function dfs(row, col) {
    let queue = [];
    queue.unshift([row, col]);

    while (queue.length > 0) {
      let [currentRow, currentCol] = queue.pop();

      for (let [rowOffset, colOffset] of DIRECTIONS) {
        let r = currentRow + rowOffset;
        let c = currentCol + colOffset;

        if (r < 0 || c < 0 || r >= M || c >= N || grid[r][c] === "0") {
          continue;
        }

        grid[r][c] = "0";
        queue.unshift([r, c]);
      }
    }
  }
}
