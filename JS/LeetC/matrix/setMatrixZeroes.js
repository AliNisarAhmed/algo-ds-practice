// using additional memory to store the location of zeroes
function setZeroes(matrix) {
  const rows = {};
  const cols = {};

  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      if (matrix[row][col] === 0) {
        rows[row] = true;
        cols[col] = true;
      }
    }
  }

  for (let row = 0; row < matrix.length; row++) {
    for (let col = 0; col < matrix[0].length; col++) {
      if (rows[row] || cols[col]) {
        matrix[row][col] = 0;
      }
    }
  }
}

// O(1) space 

function setZeroes(matrix) {
  const ROW_SIZE = matrix.length;
  const COL_SIZE = matrix[0].length;

  let firstColHasZero;

  for (let row = 0; row < ROW_SIZE; row++) {
    if (matrix[row][0] === 0) {
      firstColHasZero = true;
    }

    for (let col = 0; col < COL_SIZE; col++) {
      if (matrix[row][col] === 0) {
        matrix[row][0] = 0;
        matrix[0][col] = 0;
      }
    }
  }

  for (let row = 1; row < ROW_SIZE; row++) {
    for (let col = 1; col < COL_SIZE; col++) {
      if (matrix[0][col] === 0 || matrix[row][0] === 0) {
        matrix[row][col] = 0;
      }
    }
  }

  if (matrix[0][0] === 0) {
    for (let col = 0; col < COL_SIZE; col++) {
      matrix[0][col] = 0;
    }
  }

  if (firstColHasZero) {
    for (let row = 0; row < ROW_SIZE; row++) {
      matrix[row][0] = 0;
    }
  }
}
