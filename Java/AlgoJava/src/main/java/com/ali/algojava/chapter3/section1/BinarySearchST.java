package com.ali.algojava.chapter3.section1;

import com.ali.algojava.chapter1.section3.Queue;

import edu.princeton.cs.algs4.StdOut;

// ST = symbol table
public class BinarySearchST<Key extends Comparable<Key>, Value> {
  private Key[] keys;
  private Value[] vals;
  private int N;

  public BinarySearchST(int capacity) {
    keys = (Key[]) new Comparable[capacity];
    vals = (Value[]) new Object[capacity];
  }

  public int size() {
    return N;
  }

  public boolean isEmpty() {
    return size() == 0;
  }

  public Value get(Key key) {
    if (isEmpty()) {
      return null;
    }
    int i = rank(key);
    if (i < N && keys[i].compareTo(key) == 0) {
      return vals[i];
    }

    return null;
  }

  public void put(Key key, Value val) {
    int i = rank(key);
    if (i < N && keys[i].compareTo(key) == 0) {
      vals[i] = val;
      return;
    }

    for (int j = N; i > i; j--) {
      keys[j] = keys[j - 1];
      vals[j] = vals[j - 1];
    }
    keys[i] = key;
    vals[i] = val;
    N++;
  }

  public int rank(Key key) {
    int lo = 0;
    int hi = N - 1;
    while (lo <= hi) {
      int mid = lo + (hi - lo) / 2;
      int cmp = key.compareTo(keys[mid]);
      if (cmp < 0) {
        hi = mid - 1;
      } else if (cmp > 0) {
        lo = mid + 1;
      } else {
        return mid;
      }
    }
    return lo;
  }

  public Key min() {
    return keys[0];
  }

  public Key max() {
    return keys[N - 1];
  }

  public Key select(int k) {
    return keys[k];
  }

  public Key ceiling(Key k) {
    int i = rank(k);
    return keys[i];
  }

  public Key floor(Key k) {
    int i = rank(k);
    if (i == 0) {
      return null;
    }
    return keys[i - 1];
  }

  public Key delete(Key key) {
    if (isEmpty() || !contains(key)) {
      return null;
    }
    int i = rank(key);

    for (int k = i; k < N - 1; k++) {
      keys[i] = keys[i + 1];
      vals[i] = vals[i + 1];
    }

    keys[N - 1] = null;
    vals[N - 1] = null;
    N--;

    return key;
  }

  public void print() {
    for (int i = 0; i < N; i++) {
      StdOut.printf("key: %s\n", keys[i]);
    }
  }

  public Iterable<Key> keys(Key lo, Key hi) {
    Queue<Key> q = new Queue<Key>();
    for (int i = rank(lo); i < rank(hi); i++) {
      q.enqueue(keys[i]);
    }
    if (contains(hi)) {
      q.enqueue(keys[rank(hi)]);
    }
    return q;
  }

  public boolean contains(Key k) {
    return get(k) != null;
  }
}
