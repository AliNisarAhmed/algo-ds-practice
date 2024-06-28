package com.ali.algojava.chapter1.section4;

import com.ali.algojava.chapter1.section3.Stack;

// 1.4.31
public class DequeWithThreeStacks<T> {
  Stack<T> left = new Stack<>();
  Stack<T> mid = new Stack<>();
  Stack<T> right = new Stack<>();

  public int size() {
    return left.size() + mid.size() + right.size();
  }

  public boolean isEmpty() {
    return left.isEmpty() && right.isEmpty() && mid.isEmpty();
  }

  public void pushLeft(T item) {
    left.push(item);
  }

  public void pushRight(T item) {
    right.push(item);
  }

  public T popLeft() {
    if (left.isEmpty()) {
      if (!mid.isEmpty()) {
        return mid.pop();
      }
      moveHalfFromRightToLeftAndMid();
    }

    return left.pop();
  }

  public T popRight() {
    if (right.isEmpty()) {
      if (!mid.isEmpty()) {
        moveMidToRight();
      } else {
        moveHalfFromLeftToRightAndMid();
      }
    }

    return right.pop();
  }

  private void moveHalfFromLeftToRightAndMid() {
    int halfSize = left.size() / 2;
    int remainingSize = left.size() - halfSize;

    for (int i = 0; i < halfSize; i++) {
      mid.push(left.pop());
    }

    for (int i = 0; i < remainingSize; i++) {
      right.push(left.pop());
    }
  }

  private void moveMidToRight() {
    while (!mid.isEmpty()) {
      right.push(mid.pop());
    }
  }

  private void moveHalfFromRightToLeftAndMid() {
    int halfSize = right.size() / 2;
    int remainingSize = right.size() - halfSize;

    for (int i = 0; i < halfSize; i++) {
      mid.push(right.pop());
    }

    for (int i = 0; i < remainingSize; i++) {
      left.push(right.pop());
    }
  }

}
