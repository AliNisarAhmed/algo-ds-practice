package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class BufferTest {

  @Test
  public void test_buffer() {
    Buffer b = new Buffer();
    assertEquals(0, b.size());

    b.insert('a');
    assertEquals(1, b.size());
    assertEquals('a', b.get());

    b.insert('b');
    b.insert('c');
    // a b c
    assertEquals(3, b.size());
    assertEquals('c', b.get());

    b.left(1);
    // a <b> c
    assertEquals('b', b.get());

    b.insert('d');
    b.insert('e');
    b.insert('f');
    b.insert('g');
    // a b d e f <g> c
    assertEquals('g', b.get());

    b.right(1);
    // a b d e f g <c>
    assertEquals('c', b.get());

    b.right(100);
    // a b d e f g <c>
    assertEquals('c', b.get());

    b.left(3);
    // a b d <e> f g c
    assertEquals('e', b.delete());
    assertEquals('d', b.get());
    assertEquals(6, b.size());
  }
}
