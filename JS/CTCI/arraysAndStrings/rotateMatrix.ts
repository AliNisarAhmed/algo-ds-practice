function rotateMatrix(matrix: any[][]) {
  const edge = matrix.length - 1;

  for (let i = 0; i < matrix.length / 2; i++) {
    for (let j = i; j < edge - i; j++) {
      movePixels(i, j);
    }
  }

  function movePixels(row: number, col: number) {
    let fromRow;
    let fromCol;
    let fromPixel;

    let toRow = row;
    let toCol = col;
    let toPixel = matrix[row][col];

    for (let i = 0; i < 4; i++) {
      fromRow = toRow;
      fromCol = toCol;
      toRow = fromCol;
      toCol = edge - fromRow;

      fromPixel = toPixel;
      toPixel = matrix[toRow][toCol];
      matrix[toRow][toCol] = fromPixel;
    }
  }
}

console.log();

const testMatrix = [
  [1, 2, 3, 4],
  [0, 1, 2, 3],
  [0, 0, 1, 2],
  [1, 0, 0, 1],
];

console.log("before:");
console.log(testMatrix[0]);
console.log(testMatrix[1]);
console.log(testMatrix[2]);
console.log(testMatrix[3]);

rotateMatrix(testMatrix);

console.log("after:");
console.log(testMatrix[0]);
console.log(testMatrix[1]);
console.log(testMatrix[2]);
console.log(testMatrix[3]);
