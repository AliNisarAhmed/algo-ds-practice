package com.ali.algojava.chapter1.section3;

import java.util.Iterator;

// 1.3.29
public class QueueWithCircularLinkedList<Item> implements Iterable<Item> {

  private Node last = null;
  private int size = 0;

  public class Node {
    public Item item;
    public Node next;

    public Node(Item item, Node next) {
      this.item = item;
      this.next = next;
    }
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  public QueueWithCircularLinkedList<Item> enqueue(Item item) {
    Node newNode = new Node(item, null);
    if (isEmpty()) {
      last = newNode;
      last.next = last;
    } else {
      Node first = last.next;
      newNode.next = first;
      last.next = newNode;
      last = newNode;
    }
    size++;
    return this;
  }

  public Item dequeue() {
    Node result;
    if (isEmpty()) {
      return null;
    } else if (size == 1) {
      result = last;
      last = null;
    } else {
      result = last.next;
      last.next = last.next.next;
    }
    size--;
    return result.item;
  }

  // ---- ITERATOR ----

  @Override
  public Iterator<Item> iterator() {
    return new QueueIterator();
  }

  public class QueueIterator implements Iterator<Item> {
    private Node current;
    int count = 0;

    public QueueIterator() {
      if (last != null && size > 1) {
        current = last.next;
      } else {
        current = last;
      }
    }

    @Override
    public Item next() {
      count++;
      Item item = current.item;
      current = current.next;
      return item;
    }

    @Override
    public boolean hasNext() {
      return count < size;
    }
  }
}
