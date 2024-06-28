package com.ali.algojava.chapter1.section4;

import com.ali.algojava.chapter1.section3.Stack;
import com.ali.algojava.chapter1.section3.Steque;

// 1.4.29
public class DequeWithStackAndSteque<T> {
  // support pushLeft, pushRight, popLeft, popRight

  // Stack will handle left operations
  Stack<T> stack = new Stack<>();
  // Steque will handle right operations
  Steque<T> steq = new Steque<T>();

  public int size() {
    return stack.size() + steq.size();
  }

  public boolean isEmpty() {
    return stack.isEmpty() && steq.isEmpty();
  }

  public void pushLeft(T item) {
    stack.push(item);
  }

  public void pushRight(T item) {
    steq.push(item);
  }

  // By moving half items from steq to stack, this becomes amortized O(1)
  public T popLeft() {
    if (isEmpty()) {
      throw new RuntimeException("Deque underflow");
    }

    if (stack.isEmpty()) {
      moveHalfItemsFromStequeToStack();
    }

    return stack.pop();
  }

  private void moveHalfItemsFromStequeToStack() {
    int halfSize = steq.size() / 2;
    int remainingSize = steq.size() - halfSize;

    for (int i = 0; i < halfSize; i++) {
      steq.enqueue(steq.pop());
    }

    for (int i = 0; i < remainingSize; i++) {
      stack.push(steq.pop());
    }
  }

  public T popRight() {
    if (steq.isEmpty()) {
      while (!stack.isEmpty()) {
        steq.push(stack.pop());
      }
    }
    return steq.pop();
  }

}
