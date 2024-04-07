package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class LinkedListTest {

  @Test
  public void testGet() {
    LinkedList<String> l = new LinkedList<String>().append("a").append("b").append("c").append(
        "d");
    assertEquals("a", l.get(0).item);
    assertEquals("b", l.get(1).item);
    assertEquals("c", l.get(2).item);
    assertEquals("d", l.get(3).item);
    assertEquals(4, l.size());
  }

  @Test
  public void testDelete() {
    LinkedList<String> l = new LinkedList<String>().append("a").append("b").append("c").append(
        "d");
    assertEquals("a", l.delete(1));
    assertEquals(3, l.size());
    assertEquals("d", l.delete(3));
    assertEquals(2, l.size());
    assertEquals("b", l.delete(1));
    assertEquals(1, l.size());
    assertEquals("c", l.delete(1));
    assertEquals(0, l.size());
    assertTrue(l.isEmpty());
  }

  @Test
  public void testFind() {
    LinkedList<String> l = new LinkedList<String>().append("a").append("b").append("c").append(
        "d");
    assertTrue(l.find("a"));
    assertTrue(l.find("b"));
    assertTrue(l.find("c"));
    assertTrue(l.find("d"));
    assertFalse(l.find("e"));
  }

  @Test
  public void testRemoveAfter() {
    LinkedList<String> l = new LinkedList<String>().append("a").append("b").append("c").append(
        "d");
    LinkedList<String>.Node node = l.get(0);
    l.removeAfter(node);
    assertEquals(3, l.size());
    assertEquals("a", l.get(0).item);
    assertEquals("c", l.get(1).item);
    assertEquals("d", l.get(2).item);

    LinkedList<String>.Node d = l.get(2);
    l.removeAfter(d);
    assertEquals(3, l.size());
    assertEquals("a", l.get(0).item);
    assertEquals("c", l.get(1).item);
    assertEquals("d", l.get(2).item);

    LinkedList<String>.Node c = l.get(1);
    l.removeAfter(c);
    assertEquals(2, l.size());
    assertEquals("a", l.get(0).item);
    assertEquals("c", l.get(1).item);
    assertNull(l.get(2));

    LinkedList<String>.Node a = l.get(0);
    l.removeAfter(a);
    assertEquals(1, l.size());
    assertEquals("a", l.get(0).item);
    assertNull(l.get(1));
  }

  @Test
  public void testRemove() {
    LinkedList<String> l = new LinkedList<String>()
        .append("a")
        .append("b")
        .append("c")
        .append("a")
        .append("d")
        .append("a");
    LinkedList.remove(l, "a");
    assertEquals(3, l.size());
    assertEquals("b", l.get(0).item);
    assertEquals("c", l.get(1).item);
    assertEquals("d", l.get(2).item);
  }

  @Test
  public void testInsertAfter() {
    LinkedList<String> l = new LinkedList<String>().append("a").append("b").append("c").append(
        "d");
    LinkedList<String>.Node a = l.get(0);
    LinkedList<String>.Node c = l.get(2);
    LinkedList<String>.Node d = l.get(3);
    l.insertAfter(a, l.new Node("1", null));
    assertEquals(5, l.size());
    assertEquals("1", l.get(1).item);

    l.insertAfter(c, l.new Node("2", null));
    assertEquals(6, l.size());
    assertEquals("2", l.get(4).item);

    l.insertAfter(d, l.new Node("3", null));
    assertEquals(7, l.size());
    assertEquals("3", l.get(6).item);
  }

  @Test 
  public void testMax() {
    LinkedList<Integer> l = new LinkedList<Integer>().append(1).append(2).append(3).append(4);
    LinkedList<Integer>.Node first = l.get(0);
    int max = LinkedList.max(first);
    assertEquals(4, max);

    LinkedList<Integer>.Node last = l.get(3);
    max = LinkedList.max(last);
    assertEquals(4, max);
  }

  @Test 
  public void testMaxRecursive() {
    LinkedList<Integer> l = new LinkedList<Integer>().append(1).append(2).append(3).append(4);
    LinkedList<Integer>.Node first = l.get(0);
    int max = LinkedList.maxRecursive(first);
    assertEquals(4, max);

    LinkedList<Integer>.Node last = l.get(3);
    max = LinkedList.maxRecursive(last);
    assertEquals(4, max);
  }
}
