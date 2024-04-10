package com.ali.algojava.chapter1.section3;

import java.util.Iterator;

// 1.3.49
public class QueueWithTwoStacks<Item> implements Iterable<Item> {
  private Stack<Item> back;
  private Stack<Item> front;

  public int size() {
    return back.size() + front.size();
  }

  public boolean isEmpty() {
    return back.isEmpty() && front.isEmpty();
  }

  public void enqueue(Item item) {
    back.push(item);
  }

  public Item dequeue() {
    if (!front.isEmpty()) {
      return front.pop();
    }
    while (!back.isEmpty()) {
      front.push(back.pop());
    }
    return front.pop();
  }

  @Override
  public Iterator<Item> iterator() {
    return new QueueWithTwoStacksIterator();
  }

  private class QueueWithTwoStacksIterator implements Iterator<Item> {

    @Override
    public boolean hasNext() {
      return !front.isEmpty() || !back.isEmpty();
    }

    @Override
    public Item next() {
      if (!front.isEmpty()) {
        return front.pop();
      }

      while (!back.isEmpty()) {
        front.push(back.pop());
      }

      return front.pop();
    }
  }
}
