package com.ali.algojava.chapter1.section3;

public class ResizingArrayDeque<Item> {

  private Item[] items;
  private int first;
  private int size;
  private static final int DEFAULT_SIZE = 10;

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

  public ResizingArrayDeque() {
    items = (Item[]) new Object[DEFAULT_SIZE];
    first = DEFAULT_SIZE / 2;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  public void pushLeft(Item item) {
    items[first] = item;
    first--;
    size++;

    if (first < 0) {
      if (size > items.length / 2) {
        resize(items.length * 2);
      } else {
        resize(items.length); // shift items to center
      }
    }
  }

  public void pushRight(Item item) {
    int endIndex = first + size + 1;
    items[endIndex] = item;
    size++;

    if (endIndex == items.length - 1) {
      if (size > items.length / 2) {
        resize(items.length * 2);
      } else {
        resize(items.length);
      }
    }
  }

  public Item popLeft() {
    if (isEmpty()) {
      throw new RuntimeException("Deque empty");
    }

    Item item = items[first + 1];
    items[first + 1] = null;
    first++;
    size--;

    if (size == items.length / 4) {
      resize(items.length / 2);
    }
    return item;
  }

  public Item popRight() {
    if (isEmpty()) {
      throw new RuntimeException("deque empty");
    }

    int endIndex = first + size;
    Item item = items[endIndex];
    items[endIndex] = null;
    size--;
    if (size == items.length / 4) {
      resize(items.length / 2);
    }
    return item;
  }

  public void resize(int newSize) {
    int startPosition = (newSize / 2) - (size / 2);
    Item[] newArray = (Item[]) new Object[newSize];
    System.arraycopy(items, first + 1, newArray, startPosition, size);
    items = newArray;
    first = startPosition - 1;
  }
}
