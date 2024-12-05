package com.ali.algojava.chapter1.section5;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class QuickFind {
  private int[] id; // access to component id (site indexed)
  private int count; // number of components

  public QuickFind(int N) {
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
    return id[p];
  };

  public void union(int p, int q) {
    int pId = find(p);
    int qId = find(q);
    if (pId == qId) {
      return;
    }

    for (int i = 0; i < id.length; i++) {
      if (id[i] == pId) {
        id[i] = qId;
      }
    }
    count--;
  }

  public static void main(String[] args) {
    int N = StdIn.readInt();
    QuickFind uf = new QuickFind(N);

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

// 1.5.1
// x-x [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 10 + 2 + 1 (2 for find, 1 for update)
// 9-0 [0, 1, 2, 3, 4, 5, 6, 7, 8, 0] 10 + 2 + 1
// 3-4 [0, 1, 2, 4, 4, 5, 6, 7, 8, 0] 10 + 2 + 1
// 5-8 [0, 1, 2, 4, 4, 8, 6, 7, 8, 0] 10 + 2 + 1
// 7-2 [0, 1, 2, 4, 4, 8, 6, 2, 8, 0] 10 + 2 + 1
// 2-1 [0, 1, 1, 4, 4, 8, 6, 1, 8, 0] 10 + 2 + 2
// 5-7 [0, 1, 1, 4, 4, 1, 6, 1, 1, 0] 10 + 2 + 2
// 0-3 [4, 1, 1, 4, 4, 1, 6, 1, 1, 4] 10 + 2 + 2
// 4-2 [1, 1, 1, 1, 1, 1, 6, 1, 1, 1] 10 + 2 + 4
