package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;

import java.util.Arrays;
import java.util.Iterator;

// 1.3.14

public class ResizingArrayQueue<Item> implements Iterable<Item> {
  private Item[] values = (Item[]) new Object[2];
  private int size;
  private int first;
  private int last;

  public boolean isEmpty() {
    return size == 0;
  }

  public int size() {
    return size;
  }

  public boolean isFull() {
    return size == values.length;
  }

  public void enqueue(Item item) {
    StdOut.println("before enqueue: " + "last: " + last + " " + Arrays.toString(values));
    if (size == values.length) {
      resize(values.length * 2);
    }

    // if (last == values.length) {
    //   StdOut.println("setting last to 0");
    //   last = 0;
    // }

    values[last] = item;
    last++;
    size++;
    StdOut.println("after enqueue: " + "last: " + last + " " + Arrays.toString(values));
  }

  public Item dequeue() {
    StdOut.println("before dequeue: " + Arrays.toString(values));
    if (isEmpty()) {
      throw new RuntimeException("Queue is empty");
    }

    Item result = values[first];
    values[first] = null;
    first++;

    if (first == values.length) {
      first = 0;
    }
    size--;

    if (size > 0 && size == values.length / 4) {
      resize(values.length / 2);
    }

    StdOut.println("after dequeue: " + Arrays.toString(values));
    return result;
  }

  public void print() {
    for (int i = first; i <= last; i++) {
      StdOut.println(values[i]);
    }
  }

  private void resize(int capacity) {
    Item[] temp = (Item[]) new Object[capacity];

    for (int i = 0; i < size; i++) {
      temp[i] = values[(first + i) % values.length];
    }

    values = temp;
    first = 0;
    last = size;
  }

  // ---- ITERATOR ----

  public Iterator<Item> iterator() {
    return new ArrayIterator();
  }

  private class ArrayIterator implements Iterator<Item> {
    private int i = size;

    @Override
    public boolean hasNext() {
      return i > 0;
    }

    @Override
    public Item next() {
      return values[--i];
    }
  }

  // ---- MAIN ----

  public static void main(String[] args) {
    ResizingArrayQueue<Integer> q = new ResizingArrayQueue<>();
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    // q.print();
    StdOut.println(q.size());
    StdOut.println("deq result: " + q.dequeue());
    StdOut.println("deq result: " + q.dequeue());
    StdOut.println("deq result: " + q.dequeue());
    StdOut.println("deq result: " + q.dequeue());
    StdOut.println("deq result: " + q.dequeue());
    StdOut.println(q.isEmpty());
    // q.print();
  }
}
