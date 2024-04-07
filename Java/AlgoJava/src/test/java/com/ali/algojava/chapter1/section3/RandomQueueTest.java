package com.ali.algojava.chapter1.section3;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertTrue;

import edu.princeton.cs.algs4.StdOut;
import java.util.StringJoiner;
import org.junit.jupiter.api.Test;

public class RandomQueueTest {

  @Test
  public void test_randomQueue() {
    RandomQueue<Integer> q = new RandomQueue<>();
    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);
    assertEquals(5, q.size());
    StringJoiner sj = new StringJoiner(", ");
    int i1 = q.dequeue();
    int i2 = q.dequeue();
    int i3 = q.dequeue();
    int i4 = q.dequeue();
    int i5 = q.dequeue();
    sj.add(String.valueOf(i1));
    sj.add(String.valueOf(i2));
    sj.add(String.valueOf(i3));
    sj.add(String.valueOf(i4));
    sj.add(String.valueOf(i5));

    // StdOut.println(sj.toString());

    assertNotEquals("1, 2, 3, 4, 5", sj.toString());
    assertTrue(q.isEmpty());

    q.enqueue(1);
    q.enqueue(2);
    q.enqueue(3);
    q.enqueue(4);
    q.enqueue(5);

    sj = new StringJoiner(", ");
    sj.add(String.valueOf(q.sample()));
    sj.add(String.valueOf(q.sample()));
    sj.add(String.valueOf(q.sample()));
    sj.add(String.valueOf(q.sample()));
    sj.add(String.valueOf(q.sample()));

    // StdOut.println(sj.toString());
    assertNotEquals("1, 2, 3, 4, 5", sj.toString());
  }
}
