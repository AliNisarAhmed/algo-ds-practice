package com.ali.algojava.chapter2.section3;

import edu.princeton.cs.algs4.StdRandom;

public class Quick {
  public static void sort(Comparable[] a) {
    StdRandom.shuffle(a);
    sort(a, 0, a.length - 1);
  }

  private static void sort(Comparable[] a, int lo, int hi) {
    if (hi <= lo) {
      return;
    }
    int j = partition(a, lo, hi);
    sort(a, lo, j);
    sort(a, j + 1, hi);
  }

  private static int partition(Comparable[] a, int lo, int hi) {
    int i = lo;
    int j = hi + 1;
    Comparable v = a[lo]; // the partitioning item

    while (true) {
      while (less(a[++i], v)) {
        // keep traversing till we find a bigger item OR condition below reaches
        if (i == hi) {
          break;
        }
      }

      while (less(v, a[--j])) {
        // keep traversing till we find a smaller item OR condition below reaches
        if (j == lo) {
          break;
        }
      }

      if (i >= j) {
        break;
      }

      exch(a, i, j);
    }

    exch(a, lo, j); // exchange partitioning item with the rightmost entry of the left subArray
    return j;
  }

  private static boolean less(Comparable v, Comparable w) {
    return v.compareTo(w) < 0;
  }

  private static void exch(Comparable[] a, int i, int j) {
    Comparable temp = a[i];
    a[i] = a[j];
    a[j] = temp;
  }
}

// 2.3.1
// E A S Y Q U E S T I O N
// i  || j  || EASYQUESTION
// 0  || 12 || EASYQUESTION
// 2  || 6  || EAEYQUSSTION


// 2.3.2
// EASYQUESTION
// EAE YQUSSTION
// AE E QUSSTION Y
// A E E UION Q SST Y
// A E E ION U Q S ST Y
// A E E I ON U Q S S T Y 
// A E E I N O U Q S S T Y

// 2.3.3
// https://stackoverflow.com/questions/43263249/number-of-largest-element-exchanges-for-quicksort

// 2.3.4
// [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
// [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
