// Run with:
// cat data/tinyBatch.txt  | mvn exec:java -Dexec.mainClass="com.ali.algojava.chapter2.section4.TopM" -Dexec.args="5"

package com.ali.algojava.chapter2.section4;

import edu.princeton.cs.algs4.MinPQ;
import edu.princeton.cs.algs4.Stack;
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Transaction;

public class TopM {
  public static void main(String[] args) {
    int M = Integer.parseInt(args[0]);
    MinPQ<Transaction> pq = new MinPQ<Transaction>(M + 1);

    while (StdIn.hasNextLine()) {
      pq.insert(new Transaction(StdIn.readLine()));

      if (pq.size() > M) {
        pq.delMin();
      }
    }

    Stack<Transaction> stack = new Stack<Transaction>();
    while (!pq.isEmpty()) {
      stack.push(pq.delMin());
    }

    for (Transaction tr : stack) {
      StdOut.println(tr);
    }
  }
}
