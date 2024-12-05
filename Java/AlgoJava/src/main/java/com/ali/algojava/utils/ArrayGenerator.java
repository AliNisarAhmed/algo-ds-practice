package com.ali.algojava.utils;

import edu.princeton.cs.algs4.StdRandom;

public class ArrayGenerator {

  public static Comparable[] generateRandomArray(int length) {
    Comparable[] array = new Comparable[length];
    for (int i = 0; i < length; i++) {
      array[i] = StdRandom.uniform();
    }
    return array;
  }
}
