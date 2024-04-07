package com.ali.algojava.chapter1.section2;

import edu.princeton.cs.algs4.Interval1D;
import edu.princeton.cs.algs4.Interval2D;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import java.util.stream.IntStream;

public class PrintOverlap2DInterval {
  public static void main(String[] args) {
    int N = Integer.parseInt(args[0]);
    double min = Double.parseDouble(args[1]);
    double max = Double.parseDouble(args[2]);

    Interval2D[] intervals = generateIntervals(N, min, max);

    drawIntervals(intervals, min, max);
    printOverlappingOrContaining(intervals);
  }

  private static Interval2D[] generateIntervals(int N, double min, double max) {
    return IntStream.range(0, N)
        .mapToObj(i -> new Interval2D(generate1DInterval(min, max),
            generate1DInterval(min, max)))
        .toArray(Interval2D[]::new);
  }

  private static Interval1D generate1DInterval(double min, double max) {
    double d1 = StdRandom.uniform(min, max);
    double d2 = StdRandom.uniform(min, max);
    if (d1 > d2) {
      return new Interval1D(d2, d1);
    }
    return new Interval1D(d1, d2);
  }

  private static void drawIntervals(Interval2D[] intervals, double min,
      double max) {
    StdDraw.setCanvasSize(1024, 512);
    StdDraw.setPenRadius(.015);
    StdDraw.setXscale(min, max);
    StdDraw.setYscale(min, max);
    for (Interval2D interval : intervals) {
      interval.draw();
    }
  }

  private static void printOverlappingOrContaining(Interval2D[] intervals) {
    for (int i = 0; i < intervals.length - 1; i++) {
      if (intervals[i].intersects(intervals[i + 1])) {
        StdOut.print(intervals[i]);
        StdOut.print(" intersects with ");
        StdOut.println(intervals[i + 1]);
      }
    }
  }
}
