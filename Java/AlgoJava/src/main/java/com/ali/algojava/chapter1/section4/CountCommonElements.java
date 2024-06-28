package com.ali.algojava.chapter1.section4;

import edu.princeton.cs.algs4.StdOut;

// 1.4.12
public class CountCommonElements {

  public static void main(String[] args) {
    int[] a1 = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int[] a2 = new int[] { 1, 3, 5, 7, 9, 11, 12, 13, 14, 15 };

    int count = countCommonElements(a1, a2);
    StdOut.println(count);
  }

  public static int countCommonElements(int[] a1, int[] a2) {
    int result = 0;

    int i = 0;
    int j = 0;

    while (i < a1.length && j < a2.length) {
      if (a1[i] == a2[j]) {
        StdOut.println(a1[i]);
        result++;
        i++;
        j++;
      } else if (a1[i] > a2[j]) {
        j++;
      } else {
        i++;
      }
    }

    return result;
  }
}

