function isValidSudoku(board) {
  const N = 9;

  const rows = Array.from({ length: 9 }, _ => 0);
  const cols = Array.from({ length: 9 }, _ => 0);
  const boxes = Array.from({ length: 9 }, _ => 0);

  for (let r = 0; r < N; r++) {
    for (let c = 0; c < N; c++) {
      
      if (board[r][c] === '.') {
        continue;
      }

      let val = Number(board[r][c]);
      let pos = 1 << (val - 1);

      if ((rows[r] & pos) > 0) {
        return false;
      }

      rows[r] = rows[r] | pos;
      

      // Check the column
      if ((cols[c] & pos) > 0) {
        return false;
      }

      cols[c] = cols[c] | pos;

      // Check the box 
      let idx = Math.floor(r / 3) * 3 + Math.floor(c / 3);
      if ((boxes[idx] & pos) > 0) {
        return false;
      }

      boxes[idx] = boxes[idx] | pos;
    }
  }

  return true;
}
