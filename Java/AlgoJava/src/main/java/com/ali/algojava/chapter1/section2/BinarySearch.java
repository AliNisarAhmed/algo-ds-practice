package com.ali.algojava.chapter1.section2;

import edu.princeton.cs.algs4.Counter;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import java.util.Arrays;

// 1.2.9

public class BinarySearch {
  public static void main(String[] args) {
    Counter counter = new Counter("keys");
    int[] whitelist = In.readInts(args[0]);
    Arrays.sort(whitelist);
    while (!StdIn.isEmpty()) {
      int key = StdIn.readInt();
      if (rank(key, whitelist, counter) == -1) {
        StdOut.println(key);
      }
    }
    StdOut.println(counter);
  }

  public static int rank(int key, int[] a, Counter counter) {
    int lo = 0;
    int hi = a.length - 1;
    while (lo <= hi) {
      int mid = lo + (hi - lo) / 2;
      counter.increment();
      if (key < a[mid]) {
        hi = mid - 1;
      } else if (key > a[mid]) {
        lo = mid + 1;
      } else {
        return mid;
      }
    }

    return -1;
  }
}
