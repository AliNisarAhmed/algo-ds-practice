package com.ali.algojava.chapter1.section4;

import edu.princeton.cs.algs4.StdOut;

// 1.4.10
public class BinarySearch {

  public static void main(String[] args) {
    int[] test = { 3, 4, 4, 5, 6, 10, 15, 20, 20, 20, 20, 21 };
    StdOut.println(binarySearchIterative(test, 4, 0, test.length));
  }

  public static int binarySearchIterative(int[] array, int element, int low,
      int high) {
    int lowestIndex = -1;
    while (low <= high) {
      int mid = low + (high - low) / 2;

      if (array[mid] < element) {
        low = mid + 1;
      } else if (array[mid] > element) {
        high = mid - 1;
      } else {
        lowestIndex = mid;
        high = mid - 1;
      }
    }

    return lowestIndex;
  }
}
