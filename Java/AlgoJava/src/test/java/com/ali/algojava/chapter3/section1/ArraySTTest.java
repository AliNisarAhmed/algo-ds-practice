package com.ali.algojava.chapter3.section1;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

import org.junit.jupiter.api.Test;

import edu.princeton.cs.algs4.StdOut;

public class ArraySTTest {

  @Test
  public void test_ArrayST() {
    ArrayST<String, Integer> st = new ArrayST<>(100);
    st.put("c", 2);
    st.put("a", 0);
    st.put("b", 1);

    Integer result = st.get("a");
    assertEquals(result, 0);

    result = st.get("b");
    assertEquals(result, 1);

    result = st.get("d");
    assertNull(result);

    String m = st.min();
    assertEquals(m, "a");

    m = st.max();
    assertEquals(m, "c");

    String b = st.ceiling("a");
    assertEquals("b", b);

    b = st.floor("c");
    assertEquals("b", b);

    b = st.delete("b");
    assertEquals("b", b);
  }
}
