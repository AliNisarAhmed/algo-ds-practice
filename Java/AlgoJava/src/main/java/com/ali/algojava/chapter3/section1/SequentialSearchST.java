package com.ali.algojava.chapter3.section1;

// ST = symbol table
public class SequentialSearchST<Key, Value> {
  private Node first;
  private int size;

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

  public Value get(Key key) {
    for (Node x = first; x != null; x = x.next) {
      if (key.equals(x.key)) {
        return x.val;
      }
    }
    return null;
  }

  public void put(Key key, Value val) {
    for (Node x = first; x != null; x = x.next) {
      if (key.equals(x.key)) {
        x.val = val;
        return;
      }
    }
    first = new Node(key, val, first); // search miss, add new node
    size++;
  }

  public int size() {
    return size;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  // 3.1.5
  public Value delete(Key k) {
    Value result = null;
    Node prev = null;

    if (isEmpty()) {
      return result;
    }

    if (first.key.equals(k)) {
      result = first.val;
      first = first.next;
      size--;
      return result;
    }

    for (Node x = first; x != null; x = x.next) {
      if (k.equals(x.key)) {
        prev.next = x.next;
        size--;
        result = x.val;
        break;
      }
      prev = x;
    }
    return result;
  }

}
