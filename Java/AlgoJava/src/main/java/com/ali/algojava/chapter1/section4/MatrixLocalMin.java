package com.ali.algojava.chapter1.section4;

import edu.princeton.cs.algs4.StdOut;

// 1.4.19
public class MatrixLocalMin {

  public static void main(String[] args) {
    int matrix5[][] = {
        { 5, 90, 3, 10 }, { 4, 1, -7, 15 }, { 7, -1, -8, 19 }, { 12, 8, 13, 99 } };

    int min = localMinimumMatrix(matrix5);
    StdOut.println(min);
  }

  private static int localMinimumMatrix(int[][] matrix) {

    if (matrix.length != matrix[0].length) {
      throw new RuntimeException("must be a square matrix");
    }

    // N = 1 (1x1 matrix)
    if (matrix.length == 1) {
      return matrix[0][0];
    }

    // N = 2 (2x2 matrix)
    // for 2x2, check the corner elements and return any minimum
    if (matrix.length == 2) {
      if (matrix[0][0] < matrix[0][1] && matrix[0][0] < matrix[1][0]) {
        return matrix[0][0];
      }

      if (matrix[0][1] < matrix[0][0] && matrix[0][1] < matrix[1][1]) {
        return matrix[0][1];
      }

      if (matrix[1][0] < matrix[0][0] && matrix[1][0] < matrix[1][1]) {
        return matrix[1][0];
      }

      return matrix[1][1];
    }
    // for 3x3 or more
    return localMinimumMatrix(matrix, 0, matrix.length - 1, 0,
        matrix[0].length - 1);
  }

  private static int localMinimumMatrix(int[][] matrix, int firstRow,
      int endRow, int firstCol, int endCol) {
    if (firstRow == endRow && firstCol == endCol) {
      return matrix[firstRow][firstCol];
    }

    int currentMinElement = matrix[firstRow][firstCol];
    int currentMinElementRow = firstRow;
    int currentMinElementCol = firstCol;

    int centerRow = firstRow + (endRow - firstRow) / 2;
    int centerCol = firstCol + (endCol - firstCol) / 2;

    // Look at boundaries and center for the minimum element

    // Check rows
    for (int i = firstCol; i <= endCol; i++) {
      if (matrix[firstRow][i] < currentMinElement) {
        currentMinElement = matrix[firstRow][i];
        currentMinElementCol = i;
        currentMinElementRow = firstRow;
      }

      if (matrix[endRow][i] < currentMinElement) {
        currentMinElement = matrix[endRow][i];
        currentMinElementRow = endRow;
        currentMinElementCol = i;
      }
    }

    // Check columns
    for (int i = firstRow; i <= endRow; i++) {
      if (matrix[i][firstCol] < currentMinElement) {
        currentMinElement = matrix[i][firstCol];
        currentMinElementRow = i;
        currentMinElementCol = firstCol;
      }

      if (matrix[i][endCol] < currentMinElement) {
        currentMinElement = matrix[i][endCol];
        currentMinElementRow = i;
        currentMinElementCol = endCol;
      }
    }

    // Check center row
    for (int i = firstCol; i <= endCol; i++) {
      if (matrix[centerRow][i] < currentMinElement) {
        currentMinElement = matrix[centerRow][i];
        currentMinElementRow = centerRow;
        currentMinElementCol = i;
      }
    }

    // Check center col
    for (int i = firstRow; i <= endRow; i++) {
      if (matrix[i][centerCol] < currentMinElement) {
        currentMinElement = matrix[i][centerCol];
        currentMinElementCol = centerCol;
        currentMinElementRow = i;
      }
    }

    // Check if currentMinElement is a local min, else recurse

    if (currentMinElementRow - 1 >= 0 &&
        currentMinElement > matrix[currentMinElementRow - 1][currentMinElementCol - 1]) {
      // Element above is smaller
      if (currentMinElementRow - 1 <= centerRow) {
        endRow = centerRow;
      } else {
        firstRow = centerRow;
      }
      if (currentMinElementCol <= centerCol) {
        endCol = centerCol;
      } else {
        firstCol = centerCol;
      }

      return localMinimumMatrix(matrix, firstRow, endRow, firstCol, endCol);
    } else if (currentMinElementRow + 1 < matrix.length &&
        currentMinElement > matrix[currentMinElementRow + 1][currentMinElementCol]) {
      if (currentMinElementRow + 1 <= centerRow) {
        endRow = centerRow;
      } else {
        firstRow = centerRow;
      }

      if (currentMinElementCol <= centerCol) {
        endCol = centerCol;
      } else {
        firstCol = centerCol;
      }

      return localMinimumMatrix(matrix, firstRow, endRow, firstCol, endCol);
    } else if (currentMinElementCol - 1 >= 0 &&
        currentMinElement > matrix[currentMinElementRow][currentMinElementCol - 1]) {
      // Element to the left is smaller
      if (currentMinElementRow <= centerRow) {
        endRow = centerRow;
      } else {
        firstRow = centerRow;
      }

      if (currentMinElementCol - 1 <= centerCol) {
        endCol = centerCol;
      } else {
        firstCol = centerCol;
      }

      return localMinimumMatrix(matrix, firstRow, endRow, firstCol, endCol);
    } else if (currentMinElementCol + 1 < matrix[0].length &&
        currentMinElement > matrix[currentMinElementRow][currentMinElementCol + 1]) {
      // Element to the right is smaller
      if (currentMinElementRow <= centerRow) {
        endRow = centerRow;
      } else {
        firstRow = centerRow;
      }

      if (currentMinElementCol + 1 <= centerCol) {
        endCol = centerCol;
      } else {
        firstCol = centerCol;
      }

      return localMinimumMatrix(matrix, firstRow, endRow, firstCol, endCol);
    } else {
      // currentMinElement is a local minimum
      return currentMinElement;
    }
  }
}
