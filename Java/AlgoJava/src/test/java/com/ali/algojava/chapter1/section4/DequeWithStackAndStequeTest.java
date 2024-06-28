package com.ali.algojava.chapter1.section4;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class DequeWithStackAndStequeTest {

  @Test
  public void test_pushLeft() {
    DequeWithStackAndSteque<String> d = new DequeWithStackAndSteque<>();
    assertEquals(0, d.size());
    assertTrue(d.isEmpty());

    d.pushLeft("a");
    assertEquals(1, d.size());

    d.pushLeft("b");
    assertEquals(2, d.size());
  }

  @Test
  public void test_pushRight() {
    DequeWithStackAndSteque<String> d = new DequeWithStackAndSteque<>();
    assertEquals(0, d.size());
    assertTrue(d.isEmpty());

    d.pushRight("a");
    assertEquals(1, d.size());

    d.pushRight("b");
    assertEquals(2, d.size());
  }

  @Test
  public void test_popLeft() {
    DequeWithStackAndSteque<String> d = new DequeWithStackAndSteque<>();
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
    DequeWithStackAndSteque<String> d = new DequeWithStackAndSteque<>();
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
}
