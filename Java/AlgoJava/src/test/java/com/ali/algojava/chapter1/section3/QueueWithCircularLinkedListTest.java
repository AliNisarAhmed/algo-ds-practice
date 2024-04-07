package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class QueueWithCircularLinkedListTest {

  @Test
  public void testEnqueue() {
    QueueWithCircularLinkedList<String> q = new QueueWithCircularLinkedList<>();
    assertEquals(0, q.size()); 
    assertTrue(q.isEmpty());

    q.enqueue("a");
    assertEquals(1, q.size()); 
    assertFalse(q.isEmpty());

    q.enqueue("b").enqueue("c");
    assertEquals(3, q.size()); 
    assertFalse(q.isEmpty());
  }

  @Test 
  public void TestDequeue() {
    QueueWithCircularLinkedList<String> q = new QueueWithCircularLinkedList<>();
    q.enqueue("a").enqueue("b").enqueue("c").enqueue("d");

    assertEquals("a", q.dequeue());
    assertEquals(3, q.size());
    assertFalse(q.isEmpty());

    assertEquals("b", q.dequeue());
    assertEquals(2, q.size());
    assertFalse(q.isEmpty());

    assertEquals("c", q.dequeue());
    assertEquals(1, q.size());
    assertFalse(q.isEmpty());

    assertEquals("d", q.dequeue());
    assertEquals(0, q.size());
    assertTrue(q.isEmpty());

    assertEquals(null, q.dequeue());
    assertEquals(0, q.size());
    assertTrue(q.isEmpty());
  }
}
