package com.ali.algojava.chapter2.section3;

import com.ali.algojava.utils.ArrayGenerator;

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

// 2.3.6

public class QuickCountCompares {
  static int numCompares = 0;

  public static void main(String[] args) {
    int[] arraySizes = { 100, 1000, 10000 };

    for (int size : arraySizes) {
      Comparable[] array = ArrayGenerator.generateRandomArray(size);
      sort(array);

      double lnN = Math.log(size);
      double numberOfExpectedCompares = 2 * size * lnN;
      StdOut.printf("%10d %12d %20.0f\n", size, numCompares, numberOfExpectedCompares);
      numCompares = 0;
    }
  }

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
        numCompares++;
      }

      while (less(v, a[--j])) {
        // keep traversing till we find a smaller item OR condition below reaches
        if (j == lo) {
          break;
        }
        numCompares++;
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
