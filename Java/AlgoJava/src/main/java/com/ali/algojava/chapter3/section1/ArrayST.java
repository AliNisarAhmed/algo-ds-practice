package com.ali.algojava.chapter3.section1;

import java.util.Arrays;

import edu.princeton.cs.algs4.StdOut;

public class ArrayST<Key extends Comparable<Key>, Value> {
  private Key[] keys;
  private Value[] vals;
  private int N;

  public ArrayST(int capacity) {
    keys = (Key[]) new Comparable[capacity];
    vals = (Value[]) new Object[capacity];
    N = 0;
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

    for (int i = 0; i < N; i++) {
      if (keys[i].equals(key)) {
        return vals[i];
      }
    }

    return null;
  }

  public void put(Key key, Value val) {
    keys[N] = key;
    vals[N] = val;
    N++;
  }

  public Key min() {
    if (isEmpty()) {
      return null;
    }
    Key k = keys[0];
    for (int i = 0; i < N; i++) {
      if (keys[i].compareTo(k) < 0) {
        k = keys[i];
      }
    }
    return k;
  }

  public Key max() {
    if (isEmpty()) {
      return null;
    }
    Key k = keys[0];
    for (int i = 0; i < N; i++) {
      if (keys[i].compareTo(k) > 0) {
        k = keys[i];
      }
    }
    return k;
  }

  public Key select(int k) {
    // TODO:
    return keys[k];
  }

  public Key ceiling(Key k) {
    Key ceil = k;
    boolean found = false;
    for (int i = 0; i < N; i++) {
      int cmp = keys[i].compareTo(k);
      if (cmp > 0) {
        if (!found) {
          ceil = keys[i];
          found = true;
        } else {
          if (keys[i].compareTo(ceil) < 0) {
            ceil = keys[i];
          }

        }
      }
    }
    return ceil;
  }

  public Key floor(Key k) {
    Key ceil = k;
    boolean found = false;
    for (int i = 0; i < N; i++) {
      int cmp = keys[i].compareTo(k);
      if (cmp < 0) {
        if (!found) {
          ceil = keys[i];
          found = true;
        } else {
          if (keys[i].compareTo(ceil) > 0) {
            ceil = keys[i];
          }

        }
      }
    }
    return ceil;
  }

  public Key delete(Key key) {
    for (int i = 0; i < N; i++) {
      if (keys[i].equals(key)) {
        keys[i] = keys[N - 1];
        vals[i] = vals[N - 1];

        keys[N - 1] = null;
        vals[N - 1] = null;
        N--;
        break;
      }
    }
    return key;
  }

  public Iterable<Key> keys(Key lo, Key hi) {
    // TODO:
    return null;
  }

  public boolean contains(Key k) {
    return get(k) != null;
  }
}
