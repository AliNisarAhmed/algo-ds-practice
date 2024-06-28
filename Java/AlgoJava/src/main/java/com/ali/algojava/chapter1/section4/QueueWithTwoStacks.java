package com.ali.algojava.chapter1.section4;

import com.ali.algojava.chapter1.section3.Stack;

// 1.4.27
public class QueueWithTwoStacks<T> {
  Stack<T> front = new Stack<>();
  Stack<T> back = new Stack<>();

  public boolean isEmpty() {
    return front.isEmpty() && back.isEmpty();
  }

  public int size() {
    return front.size() + back.size();
  }

  public void enqueue(T item) {
    back.push(item);
  }

  public T dequeue() {
    if (front.isEmpty()) {
      while (!back.isEmpty()) {
        front.push(back.pop());
      }
    }

    return front.pop();
  }
}
