package com.ali.algojava.chapter1.section5;

import com.ali.algojava.chapter1.section3.RandomBag;

import edu.princeton.cs.algs4.StdOut;

public class RandomGrid {
  public class Connection {
    int p;
    int q;

    public Connection(int p, int q) {
      this.p = p;
      this.q = q;
    }
  }

  public static void main(String[] args) {
    int numberOfSites = Integer.parseInt(args[0]);
    StdOut.println("number of sites: " + numberOfSites);
    Connection[] connections = new RandomGrid().generate(numberOfSites);

    StdOut.print("Connections");
    for (Connection connection : connections) {
      StdOut.println(connection.p + " - " + connection.q);
    }
  }

  public Connection[] generate(int numberOfSites) {
    RandomBag<Connection> bag = new RandomBag<>();

    for (int i = 0; i < numberOfSites; i++) {
      for (int j = 0; j < numberOfSites; j++) {
        if (i != j) {
          Connection connection = new Connection(i, j);
          bag.add(connection);
        }
      }
    }

    Connection[] connections = new Connection[bag.size()];
    int i = 0;
    for (Connection connection : connections) {
      connections[i] = connection;
      i++;
    }

    return connections;
  }
}
