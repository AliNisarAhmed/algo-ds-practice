
package com.ali.algojava.chapter2.section4;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class MaxPQSortedArrayTest {
  @Test
  public void test_MaxPQSortedArray() {
    MaxPQSortedArray<Integer> pq = new MaxPQSortedArray<>(100);
    pq.insert(29);
    pq.insert(12);
    pq.insert(3);
    pq.insert(100);
    assertEquals((int)pq.delMax(), 100);
    assertEquals((int)pq.delMax(), 29);
    assertEquals((int)pq.delMax(), 12);
    assertEquals((int)pq.delMax(), 3);
  }
}
