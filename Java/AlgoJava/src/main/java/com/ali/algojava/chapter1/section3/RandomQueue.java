package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdRandom;

// 1.3.35
public class RandomQueue<Item> {
  private Item[] items;
  private int size;

  public RandomQueue() {
    items = (Item[]) new Object[10];
    size = 0;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  public void enqueue(Item item) {
    if (size == items.length) {
      resize(items.length * 2);
    }

    items[size] = item;
    size++;
  }

  public Item dequeue() {
    int random = StdRandom.uniform(0, size);
    Item result = items[random];
    items[random] = items[size - 1];
    items[size - 1] = null;
    size--;
    if (size > 0 && size == items.length / 4) {
      resize(items.length / 2);
    }
    return result;
  }

  public Item sample() {
    return items[StdRandom.uniform(0, size)];
  }

  private void resize(int newSize) {
    Item[] newArr = (Item[]) new Object[newSize];
    for (int i = 0; i < size; i++) {
      newArr[i] = items[i];
    }
    items = newArr;
  }
}
