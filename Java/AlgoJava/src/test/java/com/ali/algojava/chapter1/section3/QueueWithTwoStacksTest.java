package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class QueueWithTwoStacksTest {

  @Test
  public void test_queueCopy() {
    Queue<String> q1 = new Queue<String>();
    q1.enqueue("a");
    q1.enqueue("b");
    q1.enqueue("c");
    assertEquals(3, q1.size());
    assertEquals("a", q1.dequeue());
    assertEquals("b", q1.dequeue());
    assertEquals("c", q1.dequeue());
    assertTrue(q1.isEmpty());
  }
}
