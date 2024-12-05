package com.ali.algojava.chapter3.section1;

import edu.princeton.cs.algs4.StdOut;

// ST = symbol table
public class OrderedSequentialSearchST<Key extends Comparable<Key>, Value> {
  private Node first;
  private int size = 0;

  private class Node {
    Key key;
    Value val;
    Node next;

    public Node(Key key, Value val, Node next) {
      this.key = key;
      this.val = val;
      this.next = next;
    }
  }

  public int size() {
    return size;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public Value get(Key key) {
    for (Node x = first; x != null; x = x.next) {
      if (key.compareTo(x.key) == 0) {
        return x.val;
      } else if (key.compareTo(x.key) < 0) {
        break;
      }
    }
    return null;
  }

  public void put(Key key, Value val) {
    if (isEmpty()) {
      first = new Node(key, val, null);
      size++;
      return;
    }

    for (Node x = first; x != null; x = x.next) {
      if (x.next == null || x.next.key.compareTo(key) > 0) {
        x.next = new Node(key, val, x.next);
        size++;
        return;
      }

      if (key.equals(x.key)) {
        x.val = val;
        return;
      }

    }
  }

  public Key min() {
    if (isEmpty()) {
      return null;
    }

    return first.key;
  }

  public Key max() {
    if (isEmpty()) {
      return null;
    }

    Node result = null;
    for (Node x = first; x != null; x = x.next) {
      result = x;
    }

    return result.key;
  }

  public Key ceiling(Key k) {
    Key ceil = k;
    for (Node x = first; x != null; x = x.next) {
      if (k.compareTo(x.key) < 0) {
        return x.key;
      }
    }
    return ceil;
  }

  public Key floor(Key k) {
    Key floor = k;
    for (Node x = first; x != null; x = x.next) {
      if (x.next != null && k.compareTo(x.next.key) <= 0) {
        return x.key;
      }
    }
    return floor;
  }

  public Value delete(Key k) {
    Value result = null;
    for (Node x = first; x != null; x = x.next) {
      if (x.next != null && x.next.key.compareTo(k) == 0) {
        result = x.next.val;
        x.next = x.next.next;
        size--;
      }
    }
    return result;
  }

  public void print() {
    for (Node x = first; x != null; x = x.next) {
      StdOut.printf("key: %s, value: %d\n", x.key, x.val);
    }
  }
}
