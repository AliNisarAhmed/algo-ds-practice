package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;

// 1.3.45
public class StackGenerability {

  public static boolean isStackUnderflow(String opString) {
    String[] operations = opString.split(" ");
    int count = 0;

    for (int i = 0; i < operations.length; i++) {
      String op = operations[i];

      if (op.equals("-")) {
        count--;
      } else {
        count++;
      }

      if (count < 0) {
        return true;
      }
    }

    return false;
  }

  public static boolean validPermutation(String numString) {
    // idea is that there cannot be a forbidden sequence:
    // a < b < c where c popped first, a second, b third
    // so cab cannot be 901 for example
    String[] numbers = numString.split(" ");
    int highestValue = -1;
    int upperLimit = -1;

    for (String valueString : numbers) {
      int value = Integer.parseInt(valueString);
      if (value > highestValue) {
        highestValue = value;
        upperLimit = value;
      } else {
        if (value >= upperLimit) {
          return false;
        } else {
          upperLimit = value;
        }
      }
    }

    return true;
  }

  public static void main(String[] args) {
    StdOut.println(isStackUnderflow("0 1 2 3 - - - - 4 - -"));
  }
}
