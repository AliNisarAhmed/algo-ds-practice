package com.ali.algojava.chapter1.section5;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class QuickUnion {
  private int[] id; // access to component id (site indexed)
  private int count; // number of components

  public QuickUnion(int N) {
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

  public int find(int p) {
    // find the root
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

    id[i] = j;

    count--;
  }

  public static void main(String[] args) {
    int N = StdIn.readInt();
    QuickUnion uf = new QuickUnion(N);

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

// 1.5.2
// x-x [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
// 9-0 [0, 1, 2, 3, 4, 5, 6, 7, 8, 0] 1 + 1 + 1
// 3-4 [0, 1, 2, 4, 4, 5, 6, 7, 8, 0] 1 + 1 + 1
// 5-8 [0, 1, 2, 4, 4, 8, 6, 7, 8, 0] 1 + 1 + 1
// 7-2 [0, 1, 2, 4, 4, 8, 6, 2, 8, 0] 1 + 1 + 1
// 2-1 [0, 1, 1, 4, 4, 8, 6, 2, 8, 0]
// 5-7 [0, 1, 1, 4, 4, 2, 6, 2, 8, 0]
// 0-3 [4, 1, 1, 4, 4, 2, 6, 2, 8, 0]
// 4-2 [4, 1, 1, 4, 1, 2, 6, 2, 8, 0]
