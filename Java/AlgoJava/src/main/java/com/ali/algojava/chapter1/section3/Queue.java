package com.ali.algojava.chapter1.section3;

import java.util.Iterator;

public class Queue<Item> implements Iterable<Item> {
  private Node first;
  private Node last;
  private int N;

  private class Node {
    Item item;
    Node next;
  }

  public boolean isEmpty() {
    return N == 0;
  }

  public int size() {
    return N;
  }

  public Queue() {
    first = null;
    last = null;
    N = 0;
  }

  // 1.3.41
  public Queue(Queue<Item> q) {
    int size = q.size();

    while (size > 0) {
      Item item = q.dequeue();
      enqueue(item);
      q.enqueue(item);
      size--;
    }
  }

  public void enqueue(Item item) {
    Node oldLast = last;
    last = new Node();
    last.item = item;
    last.next = null;
    if (isEmpty()) {
      first = last;
    } else {
      oldLast.next = last;
    }
    N++;
  }

  public Item dequeue() {
    if (isEmpty()) {
      throw new RuntimeException("Queue is empty");
    }

    Item item = first.item;
    first = first.next;
    N--;
    if (isEmpty()) {
      last = null;
    }
    return item;
  }

  public Iterator<Item> iterator() {
    return new ListIterator();
  }

  private class ListIterator implements Iterator<Item> {
    private Node current = first;

    @Override
    public boolean hasNext() {
      return current != null;
    }

    @Override
    public Item next() {
      Item item = current.item;
      current = current.next;
      return item;
    }
  }
}

// 1.3.13
// B, C, D cannot occur
