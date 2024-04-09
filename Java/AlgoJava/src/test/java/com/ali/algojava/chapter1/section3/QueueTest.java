package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class QueueTest {

  @Test
  public void test_queueCopy() {
    Queue<String> q1 = new Queue<String>();
    q1.enqueue("a");
    q1.enqueue("b");
    q1.enqueue("c");
    assertEquals(3, q1.size());

    Queue<String> q2 = new Queue<String>(q1);
    assertEquals(3, q2.size());

    q1.enqueue("d");
    assertEquals(4, q1.size());
    assertEquals(3, q2.size());

    String a = q2.dequeue();
    assertEquals("a", a);
    assertEquals(2, q2.size());
    assertEquals(4, q1.size());
  }
}
