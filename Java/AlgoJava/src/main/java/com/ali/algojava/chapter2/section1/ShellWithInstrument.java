package com.ali.algojava.chapter2.section1;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class ShellWithInstrument {
  public static void sort(Comparable[] a) {
    int N = a.length;
    int h = 1;
    while (h < N / 3) {
      h = 3 * h + 1; // 1, 4, 13, 40, 121, 364, 1093
    }

    int numCompares = 0;

    while (h >= 1) {
      for (int i = h; i < N; i++) {
        // insert a[i] among a[i - h], a[i - 2h], a[i - 3h]
        for (int j = i; j >= h && less(a[j], a[j - h]); j -= h) {
          numCompares++;
          exch(a, j, j - h);
        }
      }
      StdOut.println("numCompares: " + numCompares);
      StdOut.println("array size: " + a.length);
      StdOut.println("numCompares / array size: " + numCompares / (a.length * 1.0));
      StdOut.println("---- ----");
      numCompares = 0;
      h = h / 3;
    }

  }

  private static boolean less(Comparable v, Comparable w) {
    return v.compareTo(w) < 0;
  }

  private static void exch(Comparable[] a, int i, int j) {
    Comparable temp = a[i];
    a[i] = a[j];
    a[j] = temp;
  }

  private static void show(Comparable[] a) {
    for (int i = 0; i < a.length; i++) {
      StdOut.print(a[i] + " ");
    }
    StdOut.println();
  }

  private static boolean isSorted(Comparable[] a) {
    for (int i = 1; i < a.length; i++) {
      if (less(a[i], a[i - 1])) {
        return false;
      }
    }
    return true;
  }

  public static void main(String[] args) {
    int arraySize = 10;
    for (arraySize = 10; arraySize < 100_000_000; arraySize *= 10) {
      Double[] arr = generateRandomArray(arraySize);
      sort(arr);
      assert isSorted(arr);
    }
  }

  private static Double[] generateRandomArray(int arraySize) {
    Double[] result = new Double[arraySize];
    for (int i = 0; i < arraySize; i++) {
      result[i] = StdRandom.uniform(0.0, arraySize);
    }
    return result;
  }
}
