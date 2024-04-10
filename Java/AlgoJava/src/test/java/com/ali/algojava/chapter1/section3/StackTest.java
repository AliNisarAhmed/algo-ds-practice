package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class StackTest {

  @Test
  public void test_copy() {
    Stack<Integer> s1 = new Stack<Integer>();
    s1.push(1);
    s1.push(2);
    s1.push(3);

    Stack<Integer> s2 = new Stack<>(s1);
    assertEquals(3, s1.size());
    assertEquals(3, s2.size());

    int three = s1.pop();
    assertEquals(three, 3);
    assertEquals(2, s1.size());
    assertEquals(3, s2.size());

    s2.push(4);
    assertEquals(4, s2.size());
    assertEquals(2, s1.size());
    assertEquals(4, s2.peek());
    assertEquals(2, s1.peek());
  }

  @Test
  public void test_concat() {
    Stack<Integer> s1 = new Stack<Integer>();
    s1.push(1);
    s1.push(2);
    s1.push(3);

    Stack<Integer> s2 = new Stack<Integer>();
    s2.push(4);
    s2.push(5);
    s2.push(6);

    s1.concat(s2);
    assertEquals(6, s1.size());
    assertEquals(6, s1.peek());
  }
}
