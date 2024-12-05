package com.ali.algojava.chapter2.section1;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public class Selection {
  public static void sort(Comparable[] a) {
    int N = a.length;

    for (int i = 0; i < N; i++) {
      int min = i;

      for (int j = i + 1; j < N; j++) {
        if (less(a[j], a[min])) {
          min = j;
        }
        exch(a, i, min);
      }
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
    String[] a = In.readStrings();
    sort(a);
    assert isSorted(a);
    show(a);
  }
}

// 2.1.1
// 0 -> E A S Y Q U E S T I O N
// 1 -> A E S Y Q U E S T I O N
// 2 -> A E E Y Q U S S T I O N
// 3 -> A E E I Q U S S T Y O N
// 4 -> A E E I N U S S T Y O Q
// 5 -> A E E I N O S S T Y U Q
// 6 -> A E E I N O S S T Y U Q
// 7 -> A E E I N O S S T Y U Q
// 8 -> A E E I N O S S T Y U Q
// 9 -> A E E I N O S S T U Y Q
// 10-> A E E I N O S S T U Q Y
