package com.ali.algojava.chapter1.section5;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class WeightedQuickUnion {
  private int[] id; // access to component id (site indexed)
  private int[] sz; // keeps track of size of each component
  private int count; // number of components

  public WeightedQuickUnion(int N) {
    count = N;
    id = new int[N];
    for (int i = 0; i < N; i++) {
      id[i] = i;
    }
    sz = new int[N];
    for (int i = 0; i < N; i++) {
      sz[i] = 1;
    }
  }

  public int count() {
    return count;
  }

  public boolean connected(int p, int q) {
    return find(p) == find(q);
  }

  public int find(int p) {
    while (id[p] != p) {
      p = id[p];
    }
    return p;
  };

  public void union(int p, int q) {
    int i = find(p);
    int j = find(q);
    if (i == j) {
      return;
    }

    // Make smaller root point to larger one
    if (sz[i] < sz[j]) {
      id[i] = j;
      sz[j] += sz[i];
    } else {
      id[j] = i;
      sz[i] += sz[j];
    }

    count--;
  }

  public static void main(String[] args) {
    int N = StdIn.readInt();
    WeightedQuickUnion uf = new WeightedQuickUnion(N);

    while (!StdIn.isEmpty()) {
      int p = StdIn.readInt();
      int q = StdIn.readInt();
      if (uf.connected(p, q)) {
        continue;
      }

      uf.union(p, q);
    }
    StdOut.println(uf.count() + " components");
  }
}
