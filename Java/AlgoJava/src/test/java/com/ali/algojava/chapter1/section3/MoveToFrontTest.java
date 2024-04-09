package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class MoveToFrontTest {

  @Test
  public void test_moveToFront() {
    MoveToFront<String> m = new MoveToFront<>();
    assertEquals(0, m.size());

    m.insert("a");
    assertEquals(1, m.size());
    assertEquals("a", m.peek());

    m.insert("b");
    assertEquals(2, m.size());
    assertEquals("b", m.peek());

    m.insert("a");
    assertEquals(2, m.size());
    assertEquals("a", m.peek());

    m.insert("c");
    m.insert("d");
    m.insert("e");
    assertEquals(5, m.size());
    assertEquals("e", m.peek());

    m.insert("a");
    assertEquals(5, m.size());
    assertEquals("a", m.peek());
  }
}
