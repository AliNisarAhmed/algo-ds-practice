package com.ali.algojava.chapter1.section3;

import com.ali.algojava.chapter1.section2.SmartDate;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;
import java.util.Arrays;

public class ReadDates {
  public static void main(String[] args) {
    StdOut.println(Arrays.toString(readDates("data/dates.txt")));
  }

  public static SmartDate[] readDates(String name) {
    In in = new In(name);
    Queue<SmartDate> q = new Queue<>();

    while (!in.isEmpty()) {
      q.enqueue(new SmartDate(in.readLine()));
    }

    SmartDate[] result = new SmartDate[q.size()];
    int size = q.size();
    for (int i = 0; i < size; i++) {
      result[i] = q.dequeue();
    }

    return result;
  }
}
