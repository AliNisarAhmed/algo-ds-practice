package com.ali.algojava.chapter1.section4;

// 1.3.20
// An array is bitonic if it is comprised of an increasing sequence
// of integers followed immediately by a decreasing sequence of integers.
// In our case below we assume all integest are distinct
// 1 3 4 5 7 6 4 2

public class BitonicSearch {

  private int isPresentInBitonicArray(int[] array, int target) {
    if (array == null || array.length == 0) {
      return -1;
    }

    int tippingPoint = findTippingPoint(array, 0, array.length - 1);

    int ascendingSearchResult = ascendingBinarySearch(array, target, 0, tippingPoint);

    if (ascendingSearchResult != -1) {
      return ascendingSearchResult;
    }

    return descendingBinarySearch(array, target, tippingPoint + 1, array.length - 1);
  }

  private static int ascendingBinarySearch(int[] array, int target, int low,
      int high) {

    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (target == array[mid]) {
        return mid;
      } else if (target > array[mid]) {
        low = mid + 1;
      } else {
        high = mid - 1;
      }
    }

    return -1;
  }

  private static int descendingBinarySearch(int[] array, int target, int low, int high) {
    while (low <= high) {
      int mid = low + (high - low) / 2;
      if (target == array[mid]) {
        return mid;
      } else if (target > array[mid]) {
        // search left subarray
        high = mid - 1;
      } else {
        low = mid + 1;
      }
    }

    return -1;
  }

  private static int findTippingPoint(int[] array, int low, int high) {
    if (low > high) {
      // tipping point must be at the end of the array, the array has only
      // increasing elements
      return array.length - 1;
    }

    if (low == high) {
      return high;
    }

    int mid = low + (high - low) / 2;
    if (mid == 0) {
      if (array[mid] < array[mid + 1]) {
        return findTippingPoint(array, mid + 1, high);
      } else {
        return mid;
      }
    } else if (mid == array.length - 1) {
      return array.length - 1;
    }

    if (array[mid - 1] > array[mid] && array[mid] > array[mid + 1]) {
      // we are in descending part
      // search left subarray from mid
      return findTippingPoint(array, low, mid - 1);
    } else if (array[mid - 1] < array[mid] && array[mid] < array[mid + 1]) {
      // we are in ascending part
      // search right subarray from mid
      return findTippingPoint(array, mid + 1, high);
    } else {
      return mid;
    }
  }
}
