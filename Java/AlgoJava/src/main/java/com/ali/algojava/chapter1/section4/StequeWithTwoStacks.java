package com.ali.algojava.chapter1.section4;

import com.ali.algojava.chapter1.section3.Stack;

// 1.4.29
public class StequeWithTwoStacks<T> {
  Stack<T> front = new Stack<>();
  Stack<T> back = new Stack<>();

  public int size() {
    return front.size() + back.size();
  }

  public boolean isEmpty() {
    return front.isEmpty() && back.isEmpty();
  }

  public StequeWithTwoStacks<T> push(T item) {
    front.push(item);
    return this;
  }

  public T pop() {
    if (front.isEmpty()) {
      while (!back.isEmpty()) {
        front.push(back.pop());
      }
    }
    return front.pop();
  }

  public void enqueue(T item) {
    back.push(item);
  }

  public T peek() {
    if (front.isEmpty()) {
      while (!back.isEmpty()) {
        front.push(back.pop());
      }
    }
    return front.peek();
  }
}
