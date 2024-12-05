package com.ali.algojava.chapter2.section4;

import edu.princeton.cs.algs4.StdOut;

public class MaxPQSortedArray<Key extends Comparable<Key>> {
  private Key[] pq;
  private int N = 0;

  public MaxPQSortedArray(int maxN) {
    pq = (Key[]) new Comparable[maxN + 1];
  }

  public boolean isEmpty() {
    return N == 0;
  }

  public int size() {
    return N;
  }

  public void insert(Key v) {
    pq[N] = v;
    for (int i = N; i > 0; i--) {
      if (pq[i].compareTo(pq[i - 1]) < 0) {
        exch(i, i - 1);
      }
    }
    N++;
  }

  public Key delMax() {
    Key result = pq[N - 1];
    pq[N - 1] = null;
    N--;
    return result;
  }

  private void exch(int i, int j) {
    Key t = pq[i];
    pq[i] = pq[j];
    pq[j] = t;
  }

  public void print() {
    for (int i = 0; i < N; i++) {
      StdOut.printf("%d: %d\n", i, pq[i]);
    }
  }
}
