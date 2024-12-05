package com.ali.algojava.chapter2.section4;

import edu.princeton.cs.algs4.StdOut;

public class HeapSort {
  public static void sort(Comparable[] a) {
    int N = a.length;

    for (int k = N; k >= 0; k--) {
      StdOut.printf("k: %d\n", k);
      sink(a, k, N);
    }

    while (N > 1) {
      exch(a, 1, N--);
      sink(a, 1, N);
    }
  }

  private static void sink(Comparable[] a, int k, int N) {
    while ((2 * k + 1) <= N) {
      int j = 2 * k + 1;
      // choose the next child if it's less than j
      if (j < N && less(a, j, j + 1)) {
        j++;
      }

      if (!less(a, k, j)) {
        break;
      }

      exch(a, k, j);
      k = j;
    }
  }

  private static boolean less(Comparable[] a, int i, int j) {
    if (i >= a.length || j >= a.length) {
      return true;
    }
    return a[i].compareTo(a[j]) < 0;
  }

  private static void exch(Comparable[] a, int i, int j) {
    if (i >= a.length || j >= a.length) {
      return;
    }
    Comparable t = a[i];
    a[i] = a[j];
    a[j] = t;
  }
}
