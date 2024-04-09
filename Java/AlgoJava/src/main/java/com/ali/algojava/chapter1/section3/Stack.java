package com.ali.algojava.chapter1.section3;

import java.util.Iterator;

public class Stack<Item> implements Iterable<Item> {
  private Node first; // top of stack
  private int N; // size of stack

  private class Node {
    Item item;
    Node next;
  }

  public Stack() {
    first = null;
    N = 0;
  }

  // 1.3.42
  public Stack(Stack<Item> stack2) {
    int size = stack2.size();
    Item[] copy = (Item[]) new Object[size];
    for (int i = 0; i < size; i++) {
      copy[i] = stack2.pop();
    }

    for (int i = size - 1; i >= 0; i--) {
      Item item = copy[i];
      push(item);
      stack2.push(item);
    }
  }

  public boolean isEmpty() {
    return first == null;
  }

  public int size() {
    return N;
  }

  public void push(Item item) {
    Node oldFirst = first;
    first = new Node();
    first.item = item;
    first.next = oldFirst;
    N++;
  }

  public Item pop() {
    if (isEmpty()) {
      return null;
    }
    Item item = first.item;
    first = first.next;
    N--;
    return item;
  }

  // 1.3.7
  public Item peek() {
    if (isEmpty())
      return null;

    return first.item;
  }

  // ---- ITERATOR ----

  public Iterator<Item> iterator() {
    return new ListIterator();
  }

  private class ListIterator implements Iterator<Item> {
    private Node current = first;

    @Override
    public boolean hasNext() {
      return current != null;
    }

    @Override
    public Item next() {
      Item item = current.item;
      current = current.next;
      return item;
    }
  }
}
