package com.ali.algojava.chapter1.section3;

// 1.3.44
public class Buffer {
  private Stack<Character> cursorStack;
  private Stack<Character> otherStack;

  public Buffer() {
    cursorStack = new Stack<>();
    otherStack = new Stack<>();
  }

  public void insert(char c) {
    cursorStack.push(c);
  }

  public char get() {
    return cursorStack.peek();
  }

  public char delete() {
    return cursorStack.pop();
  }

  public void left(int k) {
    while (!cursorStack.isEmpty() && k > 0) {
      otherStack.push(cursorStack.pop());
      k--;
    }
  }

  public void right(int k) {
    while (!otherStack.isEmpty() && k > 0) {
      cursorStack.push(otherStack.pop());
      k--;
    }
  }

  public int size() {
    return cursorStack.size() + otherStack.size();
  }
}
