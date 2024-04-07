package com.ali.algojava.chapter1.section2;

import edu.princeton.cs.algs4.StdOut;

// 1.2.6

public class CircularRotationString {
  public static void main(String[] args) {
    String s1 = "ACTGACG";
    String s2 = "TGACGAC";

    StdOut.print(isContained(s1, s2));
  }

  private static boolean isContained(String s1, String s2) {
    return (s1.length() == s2.length()) && (s1 + s1).contains(s2);
  }
}
