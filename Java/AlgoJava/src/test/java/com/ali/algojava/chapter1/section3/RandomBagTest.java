package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;

import java.util.StringJoiner;

import org.junit.jupiter.api.Test;

import edu.princeton.cs.algs4.StdOut;

public class RandomBagTest {

  @Test
  public void test_add() {
    RandomBag<String> bag = new RandomBag<>();
    bag.add("a");
    bag.add("b");
    bag.add("c");
    bag.add("d");
    bag.add("e");
    assertEquals(5, bag.size());
  }

  @Test 
  public void test_iter() {
    RandomBag<Integer> b = new RandomBag<>();
    b.add(1);
    b.add(2);
    b.add(3);
    b.add(4);
    b.add(5);
    b.add(6);

    StringJoiner items = new StringJoiner(" ");
    for (int item: b) {
      items.add(String.valueOf(item));
    }
    // StdOut.println(items.toString());
  }
}
