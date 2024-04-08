package com.ali.algojava.chapter1.section3;

// 1.3.38
public class GeneralizedQueueArray<Item> {

  private Item[] items;
  private int first = 0;
  private int last = 0;
  private int size = 0;

  public GeneralizedQueueArray() {
    items = (Item[]) new Object[2];
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  public void insert(Item x) {
    if (last == size) {
      resize(items.length * 2);
    }

    items[last] = x;
    last++;
    size++;
  }

  public Item delete(int k) {

    int index = (first + k) % items.length;
    Item result = items[index];
    items[index] = null;

    size--;

    if (index != last) {
      for (int i = index; i < last; i++) {
        items[i] = items[i + 1];
      }
    }

    last--;
    if (size > 0 && size < items.length / 4) {
      resize(items.length / 2);
    }

    return result;
  }

  private void resize(int newSize) {
    Item[] copy = (Item[]) new Object[newSize];
    for (int i = 0; i < size; i++) {
      Item item = items[(first + i) % items.length];
      if (item == null) {
        continue;
      }
      copy[i] = item;
    }
    items = copy;
    first = 0;
    last = size;
  }
}
