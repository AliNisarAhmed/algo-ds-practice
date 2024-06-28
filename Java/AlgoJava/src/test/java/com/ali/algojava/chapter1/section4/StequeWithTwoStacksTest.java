package com.ali.algojava.chapter1.section4;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class StequeWithTwoStacksTest {

  @Test
  public void test_push() {
    StequeWithTwoStacks<Integer> s = new StequeWithTwoStacks<>();
    assertEquals(0, s.size());
    assertTrue(s.isEmpty());

    s.push(1);
    assertEquals(1, s.size());
    assertFalse(s.isEmpty());
    assertEquals(1, s.peek());

    s.push(2);
    assertEquals(2, s.size());
    assertEquals(2, s.peek());
  }

  @Test
  public void test_pop() {
    StequeWithTwoStacks<Integer> s = new StequeWithTwoStacks<>();
    s.push(1).push(2).push(3);

    int three = s.pop();
    assertEquals(3, three);
    assertEquals(2, s.peek());
    assertEquals(2, s.size());

    int two = s.pop();
    assertEquals(2, two);
    assertEquals(1, s.peek());
    assertEquals(1, s.size());

    int one = s.pop();
    assertEquals(1, one);
    assertEquals(0, s.size());
    assertNull(s.peek());
    assertTrue(s.isEmpty());
  }

  @Test
  public void test_enqueue() {
    StequeWithTwoStacks<Integer> s = new StequeWithTwoStacks<>();
    assertEquals(0, s.size());
    assertTrue(s.isEmpty());

    s.enqueue(1);
    assertEquals(1, s.size());
    assertFalse(s.isEmpty());
    assertEquals(1, s.peek());

    s.enqueue(2);
    assertEquals(2, s.size());
    assertEquals(1, s.peek());

    s.enqueue(3);
    assertEquals(3, s.size());
    assertEquals(1, s.peek());
  }
}
