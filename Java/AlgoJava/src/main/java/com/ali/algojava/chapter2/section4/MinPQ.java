package com.ali.algojava.chapter2.section4;

public class MinPQ<Key extends Comparable<Key>> {
  // heap-ordered complete binary tree
  // in pq[1..N] with pq[0] unused
  private Key[] pq;
  private int N = 0;

  public MinPQ(int maxN) {
    pq = (Key[]) new Comparable[maxN + 1];
  }

  public boolean isEmpty() {
    return N == 0;
  }

  public int size() {
    return N;
  }

  public void insert(Key v) {
    pq[++N] = v;
    swim(N);
  }

  public Key delMax() {
    Key max = pq[1];
    exch(1, N--);
    pq[N + 1] = null; // avoid loitering
    sink(1);
    return max;
  }

  private boolean less(int i, int j) {
    return pq[i].compareTo(pq[j]) > 0;
  }

  private void exch(int i, int j) {
    Key t = pq[i];
    pq[i] = pq[j];
    pq[j] = t;
  }

  private void swim(int k) {
    while (k > 1 && less(k / 2, k)) {
      exch(k / 2, k);
      k = k / 2;
    }
  }

  private void sink(int k) {
    while (2 * k <= N) {
      int j = 2 * k;
      // choose the next child if it's less than j
      if (j < N && less(j, j + 1)) {
        j++;
      }

      if (!less(k, j)) {
        break;
      }

      exch(k, j);
      k = j;
    }
  }
}
