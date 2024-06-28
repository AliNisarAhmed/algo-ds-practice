package com.ali.algojava.chapter1.section4;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class StackWithQueueTest {

  @Test
  public void testStackWithQueue() {
    StackWithQueue<String> s = new StackWithQueue<>();

    s.push("A");
    s.push("B");

    String one = s.pop();
    assertEquals("B", one);

    String two = s.pop();
    assertEquals("A", two);
  }
}
