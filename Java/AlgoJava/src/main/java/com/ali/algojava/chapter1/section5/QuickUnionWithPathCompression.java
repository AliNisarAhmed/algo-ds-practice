package com.ali.algojava.chapter1.section5;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class QuickUnionWithPathCompression {
  private int[] id; // access to component id (site indexed)
  private int count; // number of components

  public QuickUnionWithPathCompression(int N) {
    count = N;
    id = new int[N];
    for (int i = 0; i < N; i++) {
      id[i] = i;
    }
  }

  public int count() {
    return count;
  }

  public boolean connected(int p, int q) {
    return find(p) == find(q);
  }

  // 1.5.12
  public int find(int p) {
    int root = p;
    while (id[root] != root) {
      root = id[root];
    }

    while (id[p] != p) {
      int nextParent = id[p];
      id[p] = root;
      p = nextParent;
    }
    return root;
  };

  public void union(int p, int q) {
    int i = find(p);
    int j = find(q);
    if (i == j) {
      return;
    }

    id[i] = j;

    count--;
  }

  public static void main(String[] args) {
    int N = StdIn.readInt();
    QuickUnionWithPathCompression uf = new QuickUnionWithPathCompression(N);

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
