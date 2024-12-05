package com.ali.algojava.chapter3.section2;

import static org.junit.jupiter.api.Assertions.assertEquals;

import org.junit.jupiter.api.Test;

public class BSTTest {

  @Test
  public void test_height_rec() {
    BST<Integer, Integer> bst = new BST<>();
    assertEquals(0, bst.height_rec());

    bst.put(1, 0);
    bst.put(2, 0);
    bst.put(3, 0);
    bst.put(4, 0);
    bst.put(5, 0);
    bst.put(6, 0);
    bst.put(7, 0);

    assertEquals(7, bst.height_rec());

    bst = new BST<>();
    bst.put(4, 0);
    bst.put(6, 0);
    bst.put(7, 0);
    bst.put(5, 0);
    bst.put(2, 0);
    bst.put(3, 0);
    bst.put(1, 0);

    assertEquals(3, bst.height_rec());
  }

  @Test
  public void test_height() {
    BST<Integer, Integer> bst = new BST<>();
    assertEquals(0, bst.height());

    bst.put(1, 0);
    bst.put(2, 0);
    bst.put(3, 0);
    bst.put(4, 0);
    bst.put(5, 0);
    bst.put(6, 0);
    bst.put(7, 0);

    assertEquals(7, bst.height());

    bst = new BST<>();
    bst.put(4, 0);
    bst.put(6, 0);
    bst.put(7, 0);
    bst.put(5, 0);
    bst.put(2, 0);
    bst.put(3, 0);
    bst.put(1, 0);

    assertEquals(3, bst.height());
  }

  @Test
  public void test_put_iter() {
    BST<Integer, Integer> bst = new BST<>();
    assertEquals(0, bst.size());

    bst.put_iter(1, 0);
    bst.put_iter(2, 0);
    bst.put_iter(3, 0);
    bst.put_iter(4, 0);
    bst.put_iter(5, 0);
    bst.put_iter(6, 0);
    bst.put_iter(7, 0);

    assertEquals(7, bst.size());

    bst = new BST<>();
    bst.put_iter(4, 0);
    bst.put_iter(6, 0);
    bst.put_iter(7, 0);
    bst.put_iter(5, 0);
    bst.put_iter(2, 0);
    bst.put_iter(3, 0);
    bst.put_iter(1, 0);

    assertEquals(7, bst.size());
  }

  @Test 
  public void test_misc() {
    BST<Integer, Integer> bst = new BST<>();

    assertEquals(null, bst.min());
    assertEquals(null, bst.min_iter());

    bst.put_iter(1, 0);
    bst.put_iter(2, 0);
    bst.put_iter(3, 0);
    bst.put_iter(4, 0);
    bst.put_iter(5, 0);
    bst.put_iter(6, 0);
    bst.put_iter(7, 0);

    assertEquals(1, bst.min());
    assertEquals(1, bst.min_iter());
    assertEquals(7, bst.floor(8));
    assertEquals(7, bst.floor_iter(8));
    assertEquals(2, bst.rank(3));
    assertEquals(2, bst.rank_iter(3));

    bst = new BST<>();
    bst.put_iter(4, 0);
    bst.put_iter(6, 0);
    bst.put_iter(7, 0);
    bst.put_iter(5, 0);
    bst.put_iter(2, 0);
    bst.put_iter(3, 0);
    bst.put_iter(1, 0);

    assertEquals(1, bst.min());
    assertEquals(1, bst.min_iter());
    assertEquals(7, bst.floor(8));
    assertEquals(7, bst.floor_iter(8));
    assertEquals(3, bst.rank(4));
    assertEquals(3, bst.rank_iter(4));
  }
}
