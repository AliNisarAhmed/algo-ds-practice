package com.ali.algojava.chapter2.section3;

import static org.junit.jupiter.api.Assertions.assertArrayEquals;

import org.junit.jupiter.api.Test;

public class Quick2DistinctTest {

  @Test
  public void test() {
    Integer[] a = { 5, 2, 5, 2, 5, 2, 2, 5, 5, 5 };
    Integer[] b = { 2, 5, 5, 2, 5, 2, 2, 5, 5, 5 };
    Quick2Distinct.sort(a);
    Quick2Distinct.sort(b);
    Integer[] expected = { 2, 2, 2, 2, 5, 5, 5, 5, 5, 5 };
    assertArrayEquals(expected, a);
    assertArrayEquals(expected, b);
  }

}
