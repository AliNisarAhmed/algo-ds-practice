package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;
import java.util.Arrays;
import java.util.Iterator;

// 1.3.35 && 1.3.36
public class RandomQueue<Item> implements Iterable<Item> {
  private Item[] items;
  private int size;

  private static String[] cards = new String[] {
      "sA", "sK", "sQ", "sJ", "s10", "s9", "s8", "s7", "s6", "s5", "s4",
      "s3", "s2", "hA", "hK", "hQ", "hJ", "h10", "h9", "h8", "h7", "h6",
      "h5", "h4", "h3", "h2", "dA", "dK", "dQ", "dJ", "d10", "d9", "d8",
      "d7", "d6", "d5", "d4", "d3", "d2", "cA", "cK", "cQ", "cJ", "c10",
      "c9", "c8", "c7", "c6", "c5", "c4", "c3", "c2" };

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

  @Override
  public Iterator<Item> iterator() {
    return new RandomQueueIterator();
  }

  private class RandomQueueIterator implements Iterator<Item> {
    private int index = 0;
    private Item[] arr;

    public RandomQueueIterator() {
      arr = (Item[]) new Object[size];
      for (int i = 0; i < size; i++) {
        arr[i] = items[i];
      }
      StdRandom.shuffle(arr);
    }

    @Override
    public Item next() {
      Item result = arr[index];
      index++;
      return result;
    }

    @Override
    public boolean hasNext() {
      return index < size;
    }
  }

  // 1.3.37
  public static void main(String[] args) {
    RandomQueue<String> q = new RandomQueue<>();
    for (String card : cards) {
      q.enqueue(card);
    }

    String[] hand1 = new String[13];
    String[] hand2 = new String[13];
    String[] hand3 = new String[13];
    String[] hand4 = new String[13];

    for (int i = 1; i < 53; i++) {
      if (i <= 13) {
        hand1[i - 1] = q.dequeue();
      } else if (i > 13 && i <= 26) {
        hand2[(i - 1) % 13] = q.dequeue();
      } else if (i > 26 && i <= 39) {
        hand3[(i - 1) % 13] = q.dequeue();
      } else {
        hand4[(i - 1) % 13] = q.dequeue();
      }
    }

    StdOut.println("hand1: " + Arrays.toString(hand1));
    StdOut.println("hand2: " + Arrays.toString(hand2));
    StdOut.println("hand3: " + Arrays.toString(hand3));
    StdOut.println("hand4: " + Arrays.toString(hand4));
  }
}
