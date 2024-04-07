package com.ali.algojava.chapter1.section2;

import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import java.util.Arrays;

// 1.2.1

public class PrintClosestDistance {

  public static void main(String[] args) {
    int N = Integer.parseInt(args[0]);

    Point2D[] points = generatePoints(N);

    printSmallestDistance(points);
  }

  private static Point2D[] generatePoints(int N) {
    StdDraw.setCanvasSize(1024, 512);
    StdDraw.setPenRadius(.015);
    StdDraw.setXscale(0, 1);
    StdDraw.setYscale(0, 1);

    Point2D[] points = new Point2D[N];

    for (int i = 0; i < N; i++) {
      points[i] = new Point2D(StdRandom.uniform(0.0, 1.0), StdRandom.uniform(0.0, 1.0));
      StdDraw.point(points[i].x(), points[i].y());
    }

    Arrays.sort(points, Point2D.X_ORDER);

    return points;
  }

  private static void printSmallestDistance(Point2D[] points) {
    double result = Double.MAX_VALUE;
    Point2D point1 = null;
    Point2D point2 = null;
    for (int i = 0; i < points.length - 1; i++) {
      Point2D p1 = points[i];
      Point2D p2 = points[i + 1];
      double d = p1.distanceTo(p2);
      if (d < result) {
        result = d;
        point1 = p1;
        point2 = p2;
      }
    }

    StdOut.println(point1);
    StdOut.println(point2);
    StdOut.println(result);
  }
}
