package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class GeneralizedQueueArrayTest {

  @Test
  public void test_insert() {
    GeneralizedQueueArray<Integer> q = new GeneralizedQueueArray<>();
    assertTrue(q.isEmpty());
    q.insert(1);
    q.insert(2);
    q.insert(3);
    q.insert(4);
    q.insert(5);
    assertEquals(5, q.size());
  }

  @Test 
  public void test_delete() {
    GeneralizedQueueArray<Integer> q = new GeneralizedQueueArray<>();
    q.insert(1);
    q.insert(2);
    q.insert(3);
    q.insert(4);
    q.insert(5);
    
    assertEquals(1, q.delete(0));
    assertEquals(2, q.delete(0));
    assertEquals(3, q.delete(0));
    assertEquals(4, q.delete(0));
    assertEquals(5, q.delete(0));

    q.insert(1);
    q.insert(2);
    q.insert(3);
    q.insert(4);
    q.insert(5);
    
    assertEquals(2, q.delete(1));
    assertEquals(3, q.delete(1));
    assertEquals(4, q.delete(1));
    assertEquals(5, q.delete(1));
    assertEquals(1, q.delete(0));

    q.insert(1);
    q.insert(2);
    q.insert(3);
    q.insert(4);
    q.insert(5);

    assertEquals(5, q.delete(4));
    assertEquals(4, q.delete(3));
    assertEquals(3, q.delete(2));
    assertEquals(2, q.delete(1));
    assertEquals(1, q.delete(0));

    q.insert(1);
    q.insert(2);
    q.insert(3);
    q.insert(4);
    q.insert(5);

    assertEquals(2, q.delete(1)); // 1 3 4 5
    assertEquals(4, q.delete(2)); // 1 3 5
    assertEquals(1, q.delete(0)); // 3 5
    assertEquals(5, q.delete(1)); // 3
    assertEquals(3, q.delete(0));
  }
}
