package com.ali.algojava.chapter2.section3;

import edu.princeton.cs.algs4.StdRandom;

public class Quick3Way {
  public static void sort(Comparable[] a) {
    StdRandom.shuffle(a);
    sort(a, 0, a.length - 1);
  }

  private static void sort(Comparable[] a, int lo, int hi) {
    if (hi <= lo) {
      return;
    }

    int lt = lo;
    int i = lo + 1;
    int gt = hi;

    Comparable v = a[lo];

    while (i <= gt) {

      int cmp = a[i].compareTo(v);
      if (cmp < 0) {
        exch(a, lt++, i++);
      } else if (cmp > 0) {
        exch(a, i, gt--);
      } else {
        i++;
      }
    }

    // now: a[lo..lt-1] < v = a[lt..gt] < a[gt+1..hi]
    sort(a, lo, lt - 1);
    sort(a, gt + 1, hi);
  }

  private static void exch(Comparable[] a, int i, int j) {
    Comparable temp = a[i];
    a[i] = a[j];
    a[j] = temp;
  }
}
