package com.ali.algojava.chapter3.section1;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

import org.junit.jupiter.api.Test;

import edu.princeton.cs.algs4.StdOut;

public class OrderedSequentialSearchSTTest {

  @Test
  public void test_orderedSequentialSearchST() {
    OrderedSequentialSearchST<String, Integer> st = new OrderedSequentialSearchST<>();
    st.put("a", 1);
    st.put("c", 3);
    st.put("b", 2);

    Integer b = st.get("b");
    assertEquals(2, b);

    String c = st.max();
    assertEquals("c", c);

    String a = st.min();
    assertEquals("a", a);

    String b2 = st.ceiling("a");
    assertEquals("b", b2);

    String b3 = st.floor("c");
    assertEquals("b", b3);

    b = st.delete("b");
    assertEquals(2, b);
  }
}
