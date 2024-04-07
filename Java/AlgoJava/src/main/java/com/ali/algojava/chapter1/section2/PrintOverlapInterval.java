package com.ali.algojava.chapter1.section2;

import edu.princeton.cs.algs4.Interval1D;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import java.util.Arrays;

// 1.2.2

public class PrintOverlapInterval {

  public static void main(String[] args) {
    int N = Integer.parseInt(args[0]);

    Interval1D[] intervals = new Interval1D[N];

    for (int i = 0; i < N; i++) {
      StdOut.print("Enter min: ");
      double min = StdIn.readDouble();

      StdOut.print("Enter max: ");
      double max = StdIn.readDouble();

      intervals[i] = new Interval1D(min, max);
    }

    Arrays.sort(intervals, Interval1D.MIN_ENDPOINT_ORDER);

    for (int i = 0; i < intervals.length - 1; i++) {
      Interval1D interval1 = intervals[i];
      Interval1D interval2 = intervals[i + 1];

      if (interval1.intersects(interval2)) {
        StdOut.print(interval1);
        StdOut.print(" intersects with: ");
        StdOut.print(interval2);
      }
    }
  }
}
