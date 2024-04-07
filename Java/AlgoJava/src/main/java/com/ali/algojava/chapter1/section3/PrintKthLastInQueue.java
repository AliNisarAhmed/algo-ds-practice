package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;

// 1.3.15

public class PrintKthLastInQueue {
  public static void main(String[] args) {
    int k = Integer.parseInt(args[0]);
    String input = args[1];
    String[] strings = input.split(" ");

    Queue<String> q = new Queue<>();

    for (String string : strings) {
      q.enqueue(string);
    }

    printItems(q, k);
  }

  private static void printItems(Queue<String> q, int k) {
    int count = 0;

    for (String item : q) {
      count++;

      if (count == q.size() - (k - 1)) {
        StdOut.println(item);
        break;
      }
    }
  }
}
