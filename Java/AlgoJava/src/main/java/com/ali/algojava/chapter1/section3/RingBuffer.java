package com.ali.algojava.chapter1.section3;

// 1.3.39
public class RingBuffer<Item> {
  private Item[] items;
  private int writer;
  private int reader;
  private final int CAPACITY = 10;

  public RingBuffer() {
    items = (Item[]) new Object[CAPACITY];
    writer = -1;
    reader = 0;
  }

  public boolean isEmpty() {
    return writer < reader;
  }

  public boolean isFull() {
    return (writer - reader) + 1 == CAPACITY;
  }

  public boolean write(Item e) {
    if (!isFull()) {
      int nextWriter = writer + 1;
      items[nextWriter % CAPACITY] = e;
      writer++;
      return true;
    }
    return false;
  }

  public Item read() {
    if (!isEmpty()) {
      Item nextVal = items[reader % CAPACITY];
      reader++;
      return nextVal;
    }

    return null;
  }
}
