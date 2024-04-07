package com.ali.algojava.chapter1.section3;

import java.util.Iterator;

// 1.3.33
public class Deque<Item> implements Iterable<Item> {
  private Node first;
  private Node last;
  private int size;

  public class Node {
    public Item item;
    public Node next;
    public Node prev;

    public Node(Item item) {
      this.item = item;
      this.next = null;
      this.prev = null;
    }
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  public void pushLeft(Item item) {
    Node newNode = new Node(item);
    if (isEmpty()) {
      first = newNode;
      last = newNode;
    } else {
      newNode.next = first;
      first.prev = newNode;
      first = newNode;
    }

    size++;
  }

  public void pushRight(Item item) {
    Node newNode = new Node(item);
    if (isEmpty()) {
      first = newNode;
      last = newNode;
    } else {
      newNode.prev = last;
      last.next = newNode;
      last = newNode;
    }
    size++;
  }

  public Item popLeft() {
    Item result = null;
    if (isEmpty()) {
      return result;
    }
    result = first.item;
    first = first.next;
    if (size == 1) {
      last = first;
    }
    size--;
    return result;
  }

  public Item popRight() {
    Item result = null;
    if (isEmpty()) {
      return result;
    }
    result = last.item;
    if (size == 1) {
      first = null;
      last = null;
    } else {
      last.prev.next = null;
      last = last.prev;
    }
    size--;
    return result;
  }

  @Override
  public Iterator<Item> iterator() {
    return new DequeIterator();
  }

  public class DequeIterator implements Iterator<Item> {
    private Node current = first;

    @Override
    public boolean hasNext() {
      return current != null;
    }

    @Override
    public Item next() {
      if (current == null) {
        return null;
      }
      Item result = current.item;
      current = current.next;
      return result;
    }
  }
}
