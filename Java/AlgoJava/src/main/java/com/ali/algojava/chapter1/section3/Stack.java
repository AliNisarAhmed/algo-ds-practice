package com.ali.algojava.chapter1.section3;

import java.util.ConcurrentModificationException;
import java.util.Iterator;

public class Stack<Item> implements Iterable<Item> {
  private Node first; // top of stack
  private int N; // size of stack
  private Node last;
  // 1.3.50
  private int operationCount;

  private class Node {
    Item item;
    Node next;
  }

  public Stack() {
    first = null;
    last = null;
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

  // 1.3.47
  public void concat(Stack<Item> stack2) {
    if (stack2.isEmpty()) {
      return;
    }
    stack2.last.next = first;
    N += stack2.size();
    first = stack2.first;
    stack2.N = 0;
    stack2.first = null;
    stack2.last = null;
  }

  public boolean isEmpty() {
    return N == 0;
  }

  public int size() {
    return N;
  }

  public void push(Item item) {
    Node oldFirst = first;
    first = new Node();
    first.item = item;
    first.next = oldFirst;
    if (first.next == null) {
      last = first;
    }
    N++;
    operationCount++;
  }

  public Item pop() {
    if (isEmpty()) {
      return null;
    }
    Item item = first.item;
    first = first.next;
    N--;
    if (isEmpty()) {
      last = null;
    }
    operationCount--;
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
    private int operationCountSnapshot = operationCount;

    @Override
    public boolean hasNext() {
      if (operationCountSnapshot != operationCount) {
        throw new ConcurrentModificationException(
            "stack modified during iteration");
      }
      return current != null;
    }

    @Override
    public Item next() {
      if (operationCountSnapshot != operationCount) {
        throw new ConcurrentModificationException(
            "stack modified during iteration");
      }
      Item item = current.item;
      current = current.next;
      return item;
    }
  }
}
