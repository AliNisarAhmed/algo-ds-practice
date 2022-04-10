const EMPTY = 2147483647;
const GATE = 0;
const WALL = -1;
const DIRECTIONS = [
  [1, 0],
  [-1, 0],
  [0, 1],
  [0, -1],
];

function wallsAndGates(rooms) {
  if (rooms.length === 0) return;

  const M = rooms.length;
  const N = rooms[0].length;

  let queue = [];

  for (let row = 0; row < M; row++) {
    for (let col = 0; col < N; col++) {
      if (rooms[row][col] === GATE) {
        queue.unshift([row, col]);
      }
    }
  }

  while (queue.length > 0) {
    let [row, col] = queue.pop();

    for (let [rowOffset, colOffset] of DIRECTIONS) {
      let r = row + rowOffset;
      let c = col + colOffset;

      if (r < 0 || c < 0 || r >= M || c >= N || rooms[r][c] !== EMPTY) {
        continue;
      }

      rooms[r][c] = rooms[r][c] + 1;
      queue.unshift([r, c])
    }
  }
}
