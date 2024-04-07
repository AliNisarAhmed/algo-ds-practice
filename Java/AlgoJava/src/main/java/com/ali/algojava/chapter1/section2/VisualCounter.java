package com.ali.algojava.chapter1.section2;

import edu.princeton.cs.algs4.StdDraw;

// 1.2.10
public class VisualCounter {

  private int N;
  private int max;
  private int count;
  private int operations;
  private String name;

  public VisualCounter(String name, int N, int max) {
    this.N = N;
    this.max = max;
    this.count = 0;
    this.operations = 0;

    StdDraw.setPenRadius(.015);
    StdDraw.setXscale(0, 20);
    StdDraw.setYscale(-max - 3, max + 3);
  }

  public void increment() {
    if (operations < N) {
      count = Math.max(count + 1, max);
    }
    operations++;
    plotCounter();
  }

  public void decrement() {
    if (operations < N) {
      count--;
    }
    operations++;
    plotCounter();
  }

  public int tally() {
    return count;
  }

  public String toString() {
    return name + ": " + count;
  }

  public void plotCounter() {
    StdDraw.point(operations, count);
  }

  public static void main(String[] args) {
    VisualCounter counter = new VisualCounter("VisualCounter", 6, 4);
    counter.increment();
    counter.decrement();
    counter.decrement();
    counter.decrement();
    counter.decrement();
    counter.decrement();
    counter.increment();
    counter.increment();
    counter.increment();
    counter.increment();
    counter.increment();
    counter.increment();
  }
}
