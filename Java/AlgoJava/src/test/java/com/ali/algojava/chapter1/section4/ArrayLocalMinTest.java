package com.ali.algojava.chapter1.section4;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class ArrayLocalMinTest {
  @Test
  public void test_arrayLocalMin() {
    assertEquals(-9, ArrayLocalMin.localMin(
        new int[] { 10, -9, 20, 25, 21, 40, 50, -20 }));
  }
}
