package com.ali.algojava.chapter1.section4;

import com.ali.algojava.chapter1.section3.Queue;

public class StackWithQueue<T> {
  Queue<T> q = new Queue<T>();

  public void push(T item) {
    q.enqueue(item);
  }

  public T pop() {
    for (int i = size() - 1; i > 0; i--) {
      q.enqueue(q.dequeue());
    }

    return q.dequeue();
  }

  public int size() {
    return q.size();
  }

  public boolean isEmpty() {
    return q.isEmpty();
  }
}
