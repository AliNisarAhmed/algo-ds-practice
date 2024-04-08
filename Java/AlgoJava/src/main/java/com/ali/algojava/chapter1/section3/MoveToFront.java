package com.ali.algojava.chapter1.section3;

// 1.3.40
public class MoveToFront<Item> {

  private Node first;
  private int size;

  public class Node {
    public Item item;
    public Node next;
    public Node prev;

    public Node(Item item) {
      this.item = item;
    }
  }

  public int size() {
    return size;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public void insert(Item item) {
    Node newNode = new Node(item);
    if (!isEmpty()) {
      newNode.next = first;
      first.prev = newNode;
    }
    first = newNode;
    size++;
    if (size > 1) {
      removeOtherOccurences(item);
    }
  }

  public Item peek() {
    return first == null ? null : first.item;
  }

  private void removeOtherOccurences(Item item) {
    Node current = first.next;
    while (current != null) {
      if (current.item == item) {
        current.prev.next = current.next;
        if (current.next != null) {
          current.next.prev = current.prev;
        }
        size--;
      }
      current = current.next;
    }
  }
}
