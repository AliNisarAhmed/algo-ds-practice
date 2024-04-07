package com.ali.algojava.chapter1.section3;

import java.util.Iterator;

public class ResizingArrayStack<T> implements Iterable<T> {
  private T[] a;
  private int N;

  public ResizingArrayStack(int cap) {
    a = (T[]) new Object[cap];
  }

  public boolean isEmpty() {
    return N == 0;
  }

  public int size() {
    return N;
  }

  private void resize(int max) {
    T[] temp = (T[]) new Object[max];
    for (int i = 0; i < N; i++) {
      temp[i] = a[i];
    }
    a = temp;
  }

  public void push(T item) {
    if (N == a.length) {
      resize(2 * a.length);
    }

    a[N++] = item;
  }

  public T pop() {
    T item = a[--N];
    a[N] = null; // avoid loitering
    if (N > 0 && N == a.length / 4) {
      resize(a.length / 2);
    }

    return item;
  }

  public Iterator<T> iterator() {
    return new ReverseArrayIterator();
  }

  private class ReverseArrayIterator implements Iterator<T> {
    private int i = N;

    @Override
    public boolean hasNext() {
      return i > 0;
    }

    @Override
    public T next() {
      return a[--i];
    }
  }
}
