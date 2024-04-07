package com.ali.algojava.chapter1.section3;

public class LinkedList<Item> {

  private Node first;
  private int size;

  public class Node {
    Item item;
    Node next;

    public Node(Item item, Node next) {
      this.item = item;
      this.next = next;
    }
  }

  public LinkedList<Item> append(Item item) {
    Node newNode = new Node(item, null);
    if (isEmpty()) {
      first = newNode;
    } else {
      Node last = get(size - 1);
      last.next = newNode;
    }
    size++;
    return this;
  }

  public Node get(int index) {
    if (isEmpty()) {
      return null;
    }

    Node current;

    for (current = first; current != null; current = current.next) {
      if (index == 0) {
        return current;
      }
      index--;
    }

    return null;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  // 1.3.20
  // k is the kth element, not index
  public Item delete(int k) {
    if (k > size || isEmpty()) {
      return null;
    }

    Item result = null;
    if (k == 1) {
      result = first.item;
      first = first.next;
    } else {
      Node current;
      int count = 1;
      for (current = first; current != null; current = current.next) {
        if (count == k - 1 && current.next != null) {
          result = current.next.item;
          current.next = current.next.next;
          break;
        }
        count++;
      }
    }
    size--;
    return result;
  }

  // 1.3.21
  public boolean find(String key) {
    Node current = first;

    while (current != null) {
      if (current.item.equals(key)) {
        return true;
      }
      current = current.next;
    }

    return false;
  }

  // 1.3.24
  public void removeAfter(Node node) {
    if (node == null || node.next == null) {
      return;
    }

    node.next = node.next.next;
    size--;
  }

  // 1.3.25
  public void insertAfter(Node node1, Node node2) {
    if (isEmpty() || node1 == null || node2 == null) {
      return;
    }

    node2.next = node1.next;
    node1.next = node2;
    size++;
  }

  // 1.3.26
  public static <T> void remove(LinkedList<T> list, T key) {
    if (list.isEmpty() || key == null) {
      return;
    }

    LinkedList<T>.Node prev = null;
    LinkedList<T>.Node current = list.first;

    while (current != null) {
      if (current.item.equals(key)) {
        if (prev == null) {
          current = current.next;
          list.delete(1);
        } else {
          list.removeAfter(prev);
          current = prev.next;
        }
      } else {
        prev = current;
        current = current.next;
      }
    }
  }

  // 1.3.27
  public static int max(LinkedList<Integer>.Node node) {
    if (node == null) {
      return 0;
    }

    int max = node.item;

    LinkedList<Integer>.Node current = node;
    while (current != null) {
      if (current.item > max) {
        max = current.item;
      }
      current = current.next;
    }

    return max;
  }

  // 1.3.28
  public static int maxRecursive(LinkedList<Integer>.Node node) {
    if (node == null) {
      return 0;
    }

    return Math.max(node.item, maxRecursive(node.next));
  }

  public static <T> LinkedList<T>.Node reverse(LinkedList<T>.Node node) {
    if (node == null || node.next == null) {
      return node;
    }

    LinkedList<T>.Node second = node.next;
    LinkedList<T>.Node rest = LinkedList.reverse(second);
    second.next = node;
    node.next = null;
    return rest;
  }

  public static <T> LinkedList<T>.Node reverseIter(LinkedList<T>.Node node) {
    LinkedList<T>.Node first = node;
    LinkedList<T>.Node reverse = null;
    while (first != null) {
      LinkedList<T>.Node second = first.next;
      first.next = reverse;
      reverse = first;
      first = second;
    }
    return reverse;
  }
}
