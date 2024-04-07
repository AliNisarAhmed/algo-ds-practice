package com.ali.algojava.chapter1.section3;

// 1.3.31
public class DoublyLinkedList<Item> {

  private DoubleNode first;
  private int size = 0;

  public class DoubleNode {
    public Item item;
    public DoubleNode next;
    public DoubleNode prev;

    public DoubleNode(Item item) {
      this.item = item;
      this.prev = null;
      this.next = null;
    }

    public DoubleNode(Item item, DoubleNode next, DoubleNode prev) {
      this.item = item;
      this.next = next;
      this.prev = prev;
    }
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  public DoubleNode get(int index) {
    if (index >= size) {
      return null;
    }

    DoubleNode current = first;
    while (current != null) {
      if (index == 0) {
        return current;
      }
      index--;
      current = current.next;
    }
    return null;
  }

  public DoublyLinkedList<Item> insertAtBeginning(Item item) {
    DoubleNode newNode = new DoubleNode(item);
    if (isEmpty()) {
      first = newNode;
    } else {
      newNode.next = first;
      first.prev = newNode;
      first = newNode;
    }
    size++;
    return this;
  }

  public DoublyLinkedList<Item> insertAtEnd(Item item) {
    DoubleNode newNode = new DoubleNode(item);
    if (isEmpty()) {
      first = newNode;
    } else {
      DoubleNode last = get(size - 1);
      last.next = newNode;
      newNode.prev = last;
    }
    size++;
    return this;
  }

  public Item removeFromBeginning() {
    Item result = null;
    if (isEmpty()) {
      return result;
    }

    result = first.item;
    if (size > 1) {
      first.next.prev = null;
    }
    first = first.next;

    size--;
    return result;
  }

  public Item removeFromEnd() {
    Item result = null;
    if (isEmpty()) {
      return result;
    }

    DoubleNode last = get(size - 1);
    result = last.item;
    if (size > 1) {
      last.prev.next = null;
    }
    last.prev = null;

    size--;
    return result;
  }

  public DoubleNode insertBefore(DoubleNode node, Item item) {
    if (isEmpty()) {
      throw new RuntimeException("List is empty");
    }
    DoubleNode newNode = new DoubleNode(item);
    DoubleNode prev = node.prev;
    if (prev != null) {
      prev.next = newNode;
      newNode.prev = prev;
    }
    newNode.next = node;
    node.prev = newNode;
    if (prev == null) {
      first = newNode;
    }
    size++;
    return newNode;
  }

  public DoubleNode insertAfter(DoubleNode node, Item item) {
    if (isEmpty()) {
      throw new RuntimeException("List is empty");
    }
    DoubleNode newNode = new DoubleNode(item);
    DoubleNode next = node.next;

    if (next != null) {
      next.prev = newNode;
      newNode.next = next;
    }
    node.next = newNode;
    newNode.prev = node;
    size++;
    return newNode;
  }

  public void removeNode(DoubleNode node) {
    if (isEmpty()) {
      throw new RuntimeException("list is empty");
    }
    DoubleNode prev = node.prev;
    DoubleNode next = node.next;

    if (prev != null) {
      prev.next = next;
    }

    if (next != null) {
      next.prev = prev;
    }

    node = null;
    if (prev == null) {
      first = next;
    }

    size--;
  }
}
