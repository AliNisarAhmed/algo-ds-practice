package com.ali.algojava.chapter1.section3;

public class FixedCapacityStackOfStrings {
  private String[] a;
  private int N;

  public FixedCapacityStackOfStrings(int cap) {
    a = new String[cap];
  }

  public boolean isEmpty() {
    return N == 0;
  }

  // 1.3.1
  public boolean isFull() {
    return N == a.length;
  }

  public int size() {
    return N;
  }

  public void push(String item) {
    a[N++] = item;
  }

  public String pop() {
    return a[--N];
  }
}

// 1.3.3
// b, f, g
