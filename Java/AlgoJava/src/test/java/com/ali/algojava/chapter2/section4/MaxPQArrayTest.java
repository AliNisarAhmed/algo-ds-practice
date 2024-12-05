package com.ali.algojava.chapter2.section4;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class MaxPQArrayTest {
  @Test
  public void test_MaxPQArray() {
    MaxPQArray<Integer> pq = new MaxPQArray<>(100);
    pq.insert(3);
    pq.insert(1);
    pq.insert(2);
    assertEquals((int)pq.delMax(), 3);
    assertEquals((int)pq.delMax(), 2);
    assertEquals((int)pq.delMax(), 1);
  }
}
