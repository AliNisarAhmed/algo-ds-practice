package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertFalse;
import static org.junit.jupiter.api.Assertions.assertNull;
import static org.junit.jupiter.api.Assertions.assertTrue;

import org.junit.jupiter.api.Test;

public class DoublyLinkedListTest {

  @Test
  public void test_insertAtBeginning() {
    DoublyLinkedList<String> l = new DoublyLinkedList<>();
    assertEquals(0, l.size());
    assertTrue(l.isEmpty());

    l.insertAtBeginning("c");
    assertEquals(1, l.size());
    assertFalse(l.isEmpty());
    assertEquals("c", l.get(0).item);
    assertNull(l.get(1));
    assertNull(l.get(2));

    l.insertAtBeginning("b");
    assertEquals(2, l.size());
    assertFalse(l.isEmpty());
    assertEquals("b", l.get(0).item);
    assertEquals("c", l.get(1).item);
    assertNull(l.get(2));

    l.insertAtBeginning("a");
    assertEquals(3, l.size());
    assertFalse(l.isEmpty());
    assertEquals("a", l.get(0).item);
    assertEquals("b", l.get(1).item);
    assertEquals("c", l.get(2).item);
  }

  @Test 
  public void test_insertAtEnd() {
    DoublyLinkedList<String> l = new DoublyLinkedList<>();
    assertEquals(0, l.size());
    assertTrue(l.isEmpty());

    l.insertAtEnd("c");
    assertEquals(1, l.size());
    assertFalse(l.isEmpty());
    assertEquals("c", l.get(0).item);
    assertNull(l.get(1));
    assertNull(l.get(2));

    l.insertAtEnd("b");
    assertEquals(2, l.size());
    assertFalse(l.isEmpty());
    assertEquals("c", l.get(0).item);
    assertEquals("b", l.get(1).item);
    assertNull(l.get(2));

    l.insertAtEnd("a");
    assertEquals(3, l.size());
    assertFalse(l.isEmpty());
    assertEquals("c", l.get(0).item);
    assertEquals("b", l.get(1).item);
    assertEquals("a", l.get(2).item);
  }

  @Test 
  public void test_removeFromBeginning() {
    DoublyLinkedList<String> l = new DoublyLinkedList<>();
    l.insertAtEnd("a").insertAtEnd("b").insertAtEnd("c");

    assertEquals(3, l.size());
    assertFalse(l.isEmpty());

    String a = l.removeFromBeginning();
    assertEquals("a", a);
    assertEquals(2, l.size());
    assertFalse(l.isEmpty());
    assertEquals("b", l.get(0).item);
    assertEquals("c", l.get(1).item);
    assertNull(l.get(2));

    String b = l.removeFromBeginning();
    assertEquals("b", b);
    assertEquals(1, l.size());
    assertFalse(l.isEmpty());
    assertEquals("c", l.get(0).item);
    assertNull(l.get(1));

    String c = l.removeFromBeginning();
    assertEquals("c", c);
    assertEquals(0, l.size());
    assertTrue(l.isEmpty());
    assertNull(l.get(1));

    assertNull(l.removeFromBeginning());
  }

  @Test 
  public void test_removeFromEnd() {
    DoublyLinkedList<String> l = new DoublyLinkedList<>();
    l.insertAtEnd("a").insertAtEnd("b").insertAtEnd("c");

    assertEquals(3, l.size());
    assertFalse(l.isEmpty());

    String c = l.removeFromEnd();
    assertEquals("c", c);
    assertEquals(2, l.size());
    assertFalse(l.isEmpty());
    assertEquals("a", l.get(0).item);
    assertEquals("b", l.get(1).item);
    assertNull(l.get(2));

    String b = l.removeFromEnd();
    assertEquals("b", b);
    assertEquals(1, l.size());
    assertFalse(l.isEmpty());
    assertEquals("a", l.get(0).item);
    assertNull(l.get(1));

    String a = l.removeFromEnd();
    assertEquals("a", a);
    assertEquals(0, l.size());
    assertTrue(l.isEmpty());
    assertNull(l.get(1));

    assertNull(l.removeFromEnd());
  }

  @Test 
  public void test_insertBefore() {
    DoublyLinkedList<String> l = new DoublyLinkedList<>();
    l.insertAtEnd("a").insertAtEnd("b").insertAtEnd("c");

    DoublyLinkedList<String>.DoubleNode a = l.get(0);
    DoublyLinkedList<String>.DoubleNode b = l.get(1);
    DoublyLinkedList<String>.DoubleNode c = l.get(2);

    l.insertBefore(a, "1");
    assertEquals("1", l.get(0).item);
    assertEquals(4, l.size());
    assertFalse(l.isEmpty());
    assertEquals("a", l.get(1).item);
    assertEquals("b", l.get(2).item);
    assertEquals("c", l.get(3).item);

    l.insertBefore(b, "2");
    assertEquals("1", l.get(0).item);
    assertEquals("2", l.get(2).item);
    assertEquals(5, l.size());
    assertFalse(l.isEmpty());
    assertEquals("a", l.get(1).item);
    assertEquals("b", l.get(3).item);
    assertEquals("c", l.get(4).item);

    l.insertBefore(c, "3");
    assertEquals("1", l.get(0).item);
    assertEquals("2", l.get(2).item);
    assertEquals("3", l.get(4).item);
    assertEquals(6, l.size());
    assertFalse(l.isEmpty());
    assertEquals("a", l.get(1).item);
    assertEquals("b", l.get(3).item);
    assertEquals("c", l.get(5).item);
  }

  @Test 
  public void test_insertAfter() {
    DoublyLinkedList<String> l = new DoublyLinkedList<>();
    l.insertAtEnd("a").insertAtEnd("b").insertAtEnd("c");

    DoublyLinkedList<String>.DoubleNode a = l.get(0);
    DoublyLinkedList<String>.DoubleNode b = l.get(1);
    DoublyLinkedList<String>.DoubleNode c = l.get(2);

    l.insertAfter(a, "1");
    assertEquals("1", l.get(1).item);
    assertEquals(4, l.size());
    assertFalse(l.isEmpty());
    assertEquals("a", l.get(0).item);
    assertEquals("b", l.get(2).item);
    assertEquals("c", l.get(3).item);

    l.insertAfter(b, "2");
    assertEquals("1", l.get(1).item);
    assertEquals("2", l.get(3).item);
    assertEquals(5, l.size());
    assertFalse(l.isEmpty());
    assertEquals("a", l.get(0).item);
    assertEquals("b", l.get(2).item);
    assertEquals("c", l.get(4).item);

    l.insertAfter(c, "3");
    assertEquals("1", l.get(1).item);
    assertEquals("2", l.get(3).item);
    assertEquals("3", l.get(5).item);
    assertEquals(6, l.size());
    assertFalse(l.isEmpty());
    assertEquals("a", l.get(0).item);
    assertEquals("b", l.get(2).item);
    assertEquals("c", l.get(4).item);
  }

  @Test 
  public void test_remove() {
    DoublyLinkedList<String> l = new DoublyLinkedList<>();
    l.insertAtEnd("a").insertAtEnd("b").insertAtEnd("c").insertAtEnd("d").insertAtEnd("e");

    DoublyLinkedList<String>.DoubleNode a = l.get(0);
    DoublyLinkedList<String>.DoubleNode b = l.get(1);
    DoublyLinkedList<String>.DoubleNode c = l.get(2);
    DoublyLinkedList<String>.DoubleNode d = l.get(3);
    DoublyLinkedList<String>.DoubleNode e = l.get(4);
    
    l.removeNode(a);
    assertEquals(4, l.size());
    assertEquals("b", l.get(0).item);
    assertEquals("c", l.get(1).item);
    assertEquals("d", l.get(2).item);
    assertEquals("e", l.get(3).item);

    l.removeNode(c);
    assertEquals(3, l.size());
    assertEquals("b", l.get(0).item);
    assertEquals("d", l.get(1).item);
    assertEquals("e", l.get(2).item);

    l.removeNode(e);
    assertEquals(2, l.size());
    assertEquals("b", l.get(0).item);
    assertEquals("d", l.get(1).item);

    l.removeNode(b);
    assertEquals(1, l.size());
    assertEquals("d", l.get(0).item);
    assertNull(l.get(1));

    l.removeNode(d);
    assertTrue(l.isEmpty());
    assertNull(l.get(0));
  }
}
