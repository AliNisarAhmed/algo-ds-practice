// run with
// mvn exec:java -Dexec.mainClass="com.ali.algojava.chapter2.section4.Multiway" -Dexec.args="./data/m1.txt ./data/m2.txt ./data/m3.txt"

package com.ali.algojava.chapter2.section4;

import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.IndexMinPQ;
import edu.princeton.cs.algs4.StdOut;

// merges together multiple SORTED streams
public class Multiway {

  public static void main(String[] args) {
    int n = args.length;
    In[] streams = new In[n];
    for (int i = 0; i < n; i++) {
      streams[i] = new In(args[i]);
    }
    merge(streams);
  }

  public static void merge(In[] streams) {
    int N = streams.length;
    IndexMinPQ<String> pq = new IndexMinPQ<>(N);

    for (int i = 0; i < N; i++) {
      if (!streams[i].isEmpty()) {
        String s = streams[i].readString();
        StdOut.printf("Inserting into pq from stream#%d: %s\n", i, s);
        pq.insert(i, s);
      }
    }

    while (!pq.isEmpty()) {
      StdOut.println(pq.minKey());
      int i = pq.delMin();
      if (!streams[i].isEmpty()) {
        String s = streams[i].readString();
        StdOut.printf("Stream %d is not empty: %s\n", i, s);
        pq.insert(i, s);
      }
    }
  }
}
