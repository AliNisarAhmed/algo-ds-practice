package com.ali.algojava.chapter1.section3;

// 1.3.38
public class GeneralizedQueueLinkedList<Item> {

  private Node first;
  private int size;

  public class Node {
    public Item item;
    public Node next;

    public Node(Item item) {
      this.item = item;
    }
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  public void insert(Item x) {
    Node newNode = new Node(x);
    if (isEmpty()) {
      first = newNode;
    } else {
      newNode.next = first;
      first = newNode;
    }
    size++;
  }

  public Item delete(int k) {
    if (isEmpty()) {
      throw new RuntimeException("queue is empty");
    }

    if (k >= size) {
      throw new RuntimeException("not enough items");
    }

    Item result = null;
    int target = size - k - 1;
    if (size == 1 || target == 0) {
      result = first.item;
      first = first.next;
    } else {
      int index = 0;
      Node current = first;

      while (index < target - 1) {
        current = current.next;
        index++;
      }

      result = current.next.item;
      current.next = current.next.next;
    }

    size--;
    return result;
  }
}
