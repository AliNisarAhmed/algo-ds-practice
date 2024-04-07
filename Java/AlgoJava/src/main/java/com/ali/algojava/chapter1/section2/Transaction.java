package com.ali.algojava.chapter1.section2;

import edu.princeton.cs.algs4.Date;

// 1.2.13
// 1.2.14
// 1.2.19
public class Transaction {

  private String who;
  private Date when;
  private double amount;

  public Transaction(String who, Date when, double amount) {
    this.who = who;
    this.when = when;
    this.amount = amount;
  }

  public Transaction(String input) {
    String[] fields = input.split(" ");
    who = fields[0];
    when = new Date(fields[1]);
    amount = Double.parseDouble(fields[2]);
  }

  public String who() {
    return who;
  }

  public Date when() {
    return when;
  }

  public double amount() {
    return amount;
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    Transaction other = (Transaction) obj;
    if (who == null) {
      if (other.who != null)
        return false;
    } else if (!who.equals(other.who))
      return false;
    if (when == null) {
      if (other.when != null)
        return false;
    } else if (!when.equals(other.when))
      return false;
    if (Double.doubleToLongBits(amount) != Double.doubleToLongBits(other.amount))
      return false;
    return true;
  }
}
