package com.ali.algojava.chapter1.section3;

// 1.3.48
public class TwoStacks<Item> {
  private Deque<Item> deque;
  private int rightStackSize;
  private int leftStackSize;

  public boolean isRightStackEmpty() {
    return rightStackSize == 0;
  }

  public boolean isLeftStackEmpty() {
    return leftStackSize == 0;
  }

  public int rightStackSize() {
    return rightStackSize;
  }

  public int leftStackSize() {
    return leftStackSize;
  }

  public void pushRight(Item item) {
    deque.pushRight(item);
    rightStackSize++;
  }

  public Item popRight() {
    if (isRightStackEmpty()) {
      return null;
    }
    Item result = deque.popRight();
    rightStackSize--;
    return result;
  }

  public void pushLeft(Item item) {
    deque.pushLeft(item);
    leftStackSize++;
  }

  public Item pushLeft() {
    if (isLeftStackEmpty()) {
      return null;
    }
    Item result = deque.popLeft();
    leftStackSize--;
    return result;
  }
}
