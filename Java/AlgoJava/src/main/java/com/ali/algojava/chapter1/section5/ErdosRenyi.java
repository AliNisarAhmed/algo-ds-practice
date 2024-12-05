package com.ali.algojava.chapter1.section5;

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

// 1.5.17
public class ErdosRenyi {

  public static int count(int N) {
    WeightedQuickUnion wq = new WeightedQuickUnion(N);
    int num_connections = 0;

    while (wq.count() > 1) {
      int first = StdRandom.uniform(0, N);
      int second = StdRandom.uniform(0, N);

      if (!wq.connected(first, second)) {
        wq.union(first, second);
        num_connections++;
      }
    }

    return num_connections;
  }

  public static void main(String[] args) {
    int conn = count(10);
    StdOut.println("Number of connections: " + conn);
  }
}
