package com.ali.algojava.chapter1.section3;

public class FixedCapacityStack<T> {
  private T[] a;
  private int N;

  public FixedCapacityStack(int cap) {
    a = (T[]) new Object[cap];
  }

  public boolean isEmpty() {
    return N == 0;
  }

  public int size() {
    return N;
  }

  public void push(T item) {
    a[N++] = item;
  }

  public T pop() {
    return a[--N];
  }
}
