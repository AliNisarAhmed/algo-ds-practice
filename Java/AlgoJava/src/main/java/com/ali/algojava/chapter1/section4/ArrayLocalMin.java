package com.ali.algojava.chapter1.section4;

// 5 4 3 1 7

// 1.4.18
public class ArrayLocalMin {

  public static final int NOT_FOUND = -9999;

  public static void main(String[] args) {
  }

  public static int localMin(int[] array) {
    int low = 0;
    int high = array.length - 1;

    if (array.length == 1) {
      return array[0];
    }

    if (array.length == 2) {
      if (array[0] < array[1]) {
        return array[0];
      } else {
        return array[1];
      }
    }

    while (low <= high) {
      int mid = low + (high - low) / 2;

      if (mid == 0) {
        if (array[mid] < array[mid + 1]) {
          return array[mid];
        } else {
          return NOT_FOUND;
        }
      }

      if (mid == array.length - 1) {
        if (array[mid] > array[mid - 1]) {
          return array[mid];
        } else {
          return NOT_FOUND;
        }
      }

      if (array[mid - 1] > array[mid] && array[mid] < array[mid + 1]) {
        return array[mid];
      }

      if (array[mid - 1] < array[mid]) {
        high = mid - 1;
      } else if (array[mid] > array[mid + 1]) {
        low = mid + 1;
      }
    }

    return NOT_FOUND;
  }
}
