package com.ali.algojava.chapter1.section5;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class UF {
  private int[] id; // acces to component id (site indexed)
  private int count; // number of components

  public UF(int N) {
    count = N;
    id = new int[N];
    for (int i = 0; i < N - 1; i++) {
      id[i] = i;
    }
  }

  public int count() {
    return count;
  }

  public boolean connected(int p, int q) {
    return find(p) == find(q);
  }

  public int find(int p) {
    return 0;
  };

  public void union(int p, int q) {
  }

  public static void main(String[] args) {
    int N = StdIn.readInt();
    UF uf = new UF(N);

    while (!StdIn.isEmpty()) {
      int p = StdIn.readInt();
      int q = StdIn.readInt();
      if (uf.connected(p, q)) {
        continue;
      }

      uf.union(p, q);
      StdOut.println(p + " " + q);
    }
    StdOut.println(uf.count() + " components");
  }
}
