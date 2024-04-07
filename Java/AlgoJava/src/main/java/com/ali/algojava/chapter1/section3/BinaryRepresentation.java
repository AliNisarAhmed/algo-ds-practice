package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;

// 1.3.5
public class BinaryRepresentation {

  public static void main(String[] args) {
    Stack<Integer> stack = new Stack<>();
    int N = 50;
    while (N > 0) {
      stack.push(N % 2);
      N = N / 2;
    }

    for (int d: stack) StdOut.print(d);
    StdOut.println();
  }
}
