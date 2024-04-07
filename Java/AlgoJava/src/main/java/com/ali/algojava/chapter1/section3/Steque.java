package com.ali.algojava.chapter1.section3;

// 1.3.32
public class Steque<Item> {
  // supports push, pop and enqueue

  private Node first;
  private Node last;
  private int size = 0;

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

  public Item peek() {
    if (isEmpty()) {
      return null;
    }

    return first.item;
  }

  public Steque<Item> push(Item item) {
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
    return this;
  }

  public Item pop() {
    Item result = null;
    if (isEmpty()) {
      return result;
    }
    result = first.item;
    first.prev = null;
    first = first.next;
    size--;
    return result;
  }

  public Steque<Item> enqueue(Item item) {
    Node newNode = new Node(item);
    if (isEmpty()) {
      first = newNode;
      last = newNode;
    } else {
      last.next = newNode;
      newNode.prev = last;
      last = newNode;
    }
    size++;
    return this;
  }
}
