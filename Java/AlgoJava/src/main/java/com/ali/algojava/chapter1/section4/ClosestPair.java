package com.ali.algojava.chapter1.section4;

import edu.princeton.cs.algs4.StdOut;
import java.util.Arrays;

public class ClosestPair {

  public static double[] closestPair(double[] arr) {
    double[] result = new double[2];

    Arrays.sort(arr);

    double diff = Double.MAX_VALUE;

    for (int i = 0; i < arr.length - 1; i++) {
      if (Math.abs(arr[i] - arr[i + 1]) < diff) {
        result[0] = arr[i];
        result[1] = arr[i + 1];
        diff = Math.abs(arr[i] - arr[i + 1]);
      }
    }

    return result;
  }

  public static void main(String[] args) {
    double[] array1 = { -5.2, 9.4, 20, -10, 21.1, 40, 50, -20 };
    double[] result = closestPair(array1);
    StdOut.println(Double.toString(result[0]) + ": " +
        Double.toString(result[1]));
  }
}
