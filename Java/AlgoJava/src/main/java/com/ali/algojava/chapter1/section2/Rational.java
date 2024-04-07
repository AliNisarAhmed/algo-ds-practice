package com.ali.algojava.chapter1.section2;

import edu.princeton.cs.algs4.StdOut;

public class Rational {

  private long numerator;
  private long denominator;

  public Rational(long numerator, long denominator) {
    if (denominator == 0) {
      throw new RuntimeException("denominator cannot be 0");
    }

    long gcd = gcd(numerator, denominator);

    this.numerator = numerator / gcd;
    this.denominator = denominator / gcd;

    if (this.denominator < 0) {
      this.denominator = -1 * this.denominator;
      this.numerator = -1 * this.numerator;
    }
  }

  @Override
  public boolean equals(Object obj) {
    if (this == obj)
      return true;
    if (obj == null)
      return false;
    if (getClass() != obj.getClass())
      return false;
    Rational other = (Rational) obj;
    if (numerator != other.numerator)
      return false;
    if (denominator != other.denominator)
      return false;
    return true;
  }

  private long gcd(long numerator, long denominator) {
    if (denominator == 0)
      return numerator;

    return gcd(denominator, numerator % denominator);
  }

  public Rational plus(Rational b) {
    return new Rational(this.numerator * b.denominator +
        this.denominator * b.numerator,
        this.denominator * b.denominator);
  }

  public Rational minus(Rational b) {
    return new Rational(this.numerator * b.denominator - this.denominator *
        b.numerator,
        this.denominator * b.denominator);
  }

  public Rational times(Rational b) {
    return new Rational(this.numerator * b.numerator,
        this.denominator * b.denominator);
  }

  public Rational reciprocal(Rational b) {
    return new Rational(b.denominator, b.numerator);
  }

  public Rational dividedBy(Rational b) {
    return times(reciprocal(b));
  }

  @Override
  public String toString() {
    return "Rational [numerator=" + numerator + ", denominator=" + denominator +
        "]";
  }

  public static void main(String[] args) {
    Rational r1 = new Rational(1, 4);
    Rational r2 = new Rational(2, 3);

    StdOut.println(r1.plus(r2));
    StdOut.println(r1.minus(r2));
    StdOut.println(r1.times(r2));
    StdOut.println(r1.dividedBy(r2));
  }
}
