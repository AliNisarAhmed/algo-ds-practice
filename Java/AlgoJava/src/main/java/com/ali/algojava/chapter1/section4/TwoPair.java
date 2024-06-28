package com.ali.algojava.chapter1.section4;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import java.util.Arrays;

// 1.4.8
public class TwoPair {

  public static void main(String[] args) {
    int[] a = In.readInts(args[0]);
    int count = countEqualPairs(a);
    StdOut.println(count);
  }

  public static int countEqualPairs(int[] a) {
    Arrays.sort(a);
    int i = 0;
    int j = 1;

    int result = 0;

    while (j < a.length) {
      if (a[i] == a[j]) {
        result++;
      }
      i++;
      j++;
    }

    return result;
  }
}
