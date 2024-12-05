package com.ali.algojava.chapter3.section1;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

import org.junit.jupiter.api.Test;

import edu.princeton.cs.algs4.StdOut;

public class SequentialSearchSTTest {

  @Test
  public void test_orderedSequentialSearchST() {
    SequentialSearchST<String, Integer> st = new SequentialSearchST<>();
    st.put("a", 1);
    st.put("c", 3);
    st.put("b", 2);

    assertEquals(3, st.size());

    Integer b = st.get("b");
    assertEquals(2, b);

    b = st.delete("b");
    assertEquals(2, b);

    assertEquals(2, st.size());
  }
}
