function zeroMatrix(matrix: number[][]) {
  let firstRowHasZero = false;
  let firstColHasZero = false;

  const M = matrix.length;
  const N = matrix[0].length;

  for (let j = 0; j < N; j++) {
    if (matrix[0][j] === 0) {
      firstRowHasZero = true;
      break;
    }
  }

  for (let i = 0; i < M; i++) {
    if (matrix[i][0] === 0) {
      firstColHasZero = true;
      break;
    }
  }

  for (let i = 1; i < M; i++) {
    for (let j = 1; j < N; j++) {
      if (matrix[i][j] === 0) {
        matrix[0][j] = 0;
        matrix[i][0] = 0;
      }
    }
  }

  for (let j = 0; j < N; j++) {
    if (matrix[0][j] === 0) {
      nullifyCol(matrix, j);
    }
  }

  for (let i = 0; i < M; i++) {
    if (matrix[i][0] === 0) {
      nullifyRow(matrix, i);
    }
  }

  if (firstRowHasZero) {
    nullifyRow(matrix, 0);
  }

  if (firstColHasZero) {
    nullifyCol(matrix, 0);
  }

  function nullifyRow(matrix: number[][], row: number) {
    for (let i = 0; i < matrix[0].length; i++) {
      matrix[row][i] = 0;
    }
  }

  function nullifyCol(matrix: number[][], col: number) {
    for (let i = 0; i < matrix.length; i++) {
      matrix[i][col] = 0;
    }
  }
}

const matrix = [
  [1, 0, 3],
  [4, 5, 6],
  [7, 0, 9],
];

zeroMatrix(matrix);
console.log(matrix);

// ----

function zeroMatrix2(matrix: number[][]) {
  const rows: boolean[] = [];
  const cols: boolean[] = [];

  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      if (matrix[i][j] === 0) {
        rows[i] = true;
        cols[j] = true;
      }
    }
  }

  for (let row = 0; row < rows.length; row++) {
    if (rows[row]) {
      nullifyRow(matrix, row);
    }
  }

  for (let col = 0; col < cols.length; col++) {
    if (cols[col]) {
      nullifyCol(matrix, col);
    }
  }

  function nullifyRow(matrix: number[][], row: number) {
    for (let i = 0; i < matrix[0].length; i++) {
      matrix[row][i] = 0;
    }
  }

  function nullifyCol(matrix: number[][], col: number) {
    for (let i = 0; i < matrix.length; i++) {
      matrix[i][col] = 0;
    }
  }
}
