package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;
import java.util.Arrays;

// 1.3.37
// eliminate every Mth person from a circle of N persons
public class Josephus {
  public static void main(String[] args) {
    int M = 2;
    int N = 7;
    if (args.length == 2) {
      M = Integer.parseInt(args[0]);
      N = Integer.parseInt(args[1]);
    }
    int[] output = josephus(M, N);
    StdOut.println(Arrays.toString(output));
  }

  private static int[] josephus(int M, int N) {
    int[] result = new int[N];
    Queue<Integer> q = new Queue<>();
    for (int i = 1; i <= N; i++) {
      q.enqueue(i);
    }

    for (int i = 0; i < N; i++) {

      for (int j = 1; j < M; j++) {
        q.enqueue(q.dequeue());
      }

      result[i] = q.dequeue();
    }

    return result;
  }
}
