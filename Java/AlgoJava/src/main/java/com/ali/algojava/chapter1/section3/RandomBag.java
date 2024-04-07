package com.ali.algojava.chapter1.section3;

import java.util.Iterator;

import edu.princeton.cs.algs4.StdRandom;

// 1.3.34
public class RandomBag<Item> implements Iterable<Item> {
  private Item[] items;
  private int size;
  private static final int DEFAULT_SIZE = 2;

  public RandomBag() {
    items = (Item[]) new Object[DEFAULT_SIZE];
    size = 0;
  }

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  public void add(Item item) {
    items[size] = item;
    size++;

    if (size >= items.length) {
      resize(items.length * 2);
    }
  }

  private void resize(int newSize) {
    Item[] newArray = (Item[]) new Object[newSize];
    System.arraycopy(items, 0, newArray, 0, size);
    items = newArray;
  }

  @Override
  public Iterator<Item> iterator() {
    return new RandomBagIterator();
  }

  private class RandomBagIterator implements Iterator<Item> {

    private int index = 0;
    private Item[] arr;

    public RandomBagIterator() {
      arr = (Item[]) new Object[size];
      System.arraycopy(items, 0, arr, 0, size);
      StdRandom.shuffle(arr);
    }

    @Override
    public boolean hasNext() {
      return index < size;
    }

    @Override
    public Item next() {
      Item item = arr[index];
      index++;
      return item;
    }

  }
}
