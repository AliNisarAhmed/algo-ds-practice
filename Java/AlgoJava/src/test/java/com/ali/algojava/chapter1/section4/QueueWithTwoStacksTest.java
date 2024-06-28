package com.ali.algojava.chapter1.section4;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class QueueWithTwoStacksTest {

  @Test
  public void testQueueWithTwoStacks() {
    QueueWithTwoStacks<String> q = new QueueWithTwoStacks<String>();
    assertEquals(q.size(), 0);
    assertTrue(q.isEmpty());

    q.enqueue("a");
    assertEquals(q.size(), 1);
    assertFalse(q.isEmpty());

    q.enqueue("b");
    assertEquals(q.size(), 2);
    assertFalse(q.isEmpty());

    String a = q.dequeue();
    assertEquals("a", a);
    assertEquals(q.size(), 1);
    assertFalse(q.isEmpty());

    String b = q.dequeue();
    assertEquals("b", b);
    assertEquals(q.size(), 0);
    assertTrue(q.isEmpty());
  }
}
