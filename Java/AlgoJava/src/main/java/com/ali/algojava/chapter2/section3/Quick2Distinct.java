package com.ali.algojava.chapter2.section3;

public class Quick2Distinct {
  public static void sort(Comparable[] a) {
    sort(a, 0, a.length - 1);
  }

  private static void sort(Comparable[] a, int lo, int hi) {
    if (hi <= lo) {
      return;
    }

    Comparable v = a[lo];
    int left = lo;
    int right = lo + 1;

    while (right < a.length) {
      int cmp = a[right].compareTo(v);
      if (cmp >= 0) {
        right++;
      } else {
        exch(a, left++, right++);
      }
    }

    sort(a, lo, left - 1);
    sort(a, left + 1, hi);

  }

  private static void exch(Comparable[] a, int i, int j) {
    Comparable temp = a[i];
    a[i] = a[j];
    a[j] = temp;
  }
}
