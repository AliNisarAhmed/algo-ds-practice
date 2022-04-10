function exist(board, word) {
  const ROW_SIZE = board.length;
  const COL_SIZE = board[0].length;
  const WORD_SIZE = word.length;

  for (let row = 0; row < ROW_SIZE; row++) {
    for (let col = 0; col < COL_SIZE; col++) {
      if (search(row, col, 0)) {
        return true;
      }
    }
  }

  return false;

  function search(row, col, count) {
    if (count >= WORD_SIZE) {
      return true;
    }

    if (row < 0 || row === ROW_SIZE || col <  0 || col === COL_SIZE || board[row][col] !== word[count]) {
      return false;
    }

    board[row][col] = '#';

    let res = false;
    for (let [r, c] of getNeighbCoords(row, col)) {
        res = search(r, c, count + 1);
        if (res) {
          break
        }
      }

    board[row][col] = word[count];
    return res
  }

  function getNeighbCoords(r, c) {
    return [
      [r - 1, c],
      [r + 1, c],
      [r, c - 1],
      [r, c + 1],
    ];
  }
}

console.log(
  exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"))