package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import java.util.Iterator;

import org.junit.jupiter.api.Test;

public class DequeTest {

  @Test
  public void test_pushLeft() {
    Deque<String> d = new Deque<>();
    assertEquals(0, d.size());
    assertTrue(d.isEmpty());

    d.pushLeft("a");
    assertEquals(1, d.size());

    d.pushLeft("b");
    assertEquals(2, d.size());
  }

  @Test
  public void test_pushRight() {
    Deque<String> d = new Deque<>();
    assertEquals(0, d.size());
    assertTrue(d.isEmpty());

    d.pushRight("a");
    assertEquals(1, d.size());

    d.pushRight("b");
    assertEquals(2, d.size());
  }

  @Test 
  public void test_popLeft() {
    Deque<String> d = new Deque<>();
    d.pushRight("a");
    d.pushRight("b");
    d.pushRight("c");

    String a = d.popLeft();
    assertEquals("a", a);
    assertEquals(2, d.size());

    String b = d.popLeft();
    assertEquals("b", b);
    assertEquals(1, d.size());

    String c = d.popLeft();
    assertEquals("c", c);
    assertEquals(0, d.size());

    d.pushRight("a");
    d.pushRight("b");
    d.pushRight("c");

    a = d.popLeft();
    assertEquals("a", a);
    assertEquals(2, d.size());

    b = d.popLeft();
    assertEquals("b", b);
    assertEquals(1, d.size());

    c = d.popLeft();
    assertEquals("c", c);
    assertEquals(0, d.size());
  }

  @Test 
  public void test_popRight() {
    Deque<String> d = new Deque<>();
    d.pushRight("a");
    d.pushRight("b");
    d.pushRight("c");

    String c = d.popRight();
    assertEquals("c", c);
    assertEquals(2, d.size());

    String b = d.popRight();
    assertEquals("b", b);
    assertEquals(1, d.size());

    String a = d.popLeft();
    assertEquals("a", a);
    assertEquals(0, d.size());

    d.pushRight("a");
    d.pushRight("b");
    d.pushRight("c");

    c = d.popRight();
    assertEquals("c", c);
    assertEquals(2, d.size());

    b = d.popRight();
    assertEquals("b", b);
    assertEquals(1, d.size());

    a = d.popRight();
    assertEquals("a", a);
    assertEquals(0, d.size());
  }

  @Test 
  public void test_iterator() {
    Deque<String> d = new Deque<>();
    d.pushRight("a");
    d.pushRight("b");
    d.pushRight("c");

    Iterator<String> it = d.iterator();

    assertTrue(it.hasNext());
    assertEquals("a", it.next());
    assertTrue(it.hasNext());
    assertEquals("b", it.next());
    assertTrue(it.hasNext());
    assertEquals("c", it.next());
    assertFalse(it.hasNext());
    assertNull(it.next()); 
  }

}
