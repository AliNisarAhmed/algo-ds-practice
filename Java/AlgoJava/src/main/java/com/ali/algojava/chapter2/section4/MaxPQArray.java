package com.ali.algojava.chapter2.section4;

public class MaxPQArray<Key extends Comparable<Key>> {
  private Key[] pq;
  private int N = 0;

  public MaxPQArray(int maxN) {
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
    N++;
  }

  public Key delMax() {
    int max = 0;
    for (int i = 0; i < N; i++) {
      if (pq[i].compareTo(pq[max]) > 0) {
        max = i;
      }
    }
    Key result = pq[max];
    exch(max, N - 1);
    pq[N - 1] = null;
    N--;
    return result;
  }

  private void exch(int i, int j) {
    Key t = pq[i];
    pq[i] = pq[j];
    pq[j] = t;
  }
}
