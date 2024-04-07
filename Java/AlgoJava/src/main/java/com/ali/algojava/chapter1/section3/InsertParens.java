package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;

// 1.3.9

public class InsertParens {

  public static void main(String[] args) {
    String input = "1 + 2 ) * 3 - 4 ) * 5 - 6 ) ) )";
    StdOut.println(insertParens(input));
  }

  public static String insertParens(String input) {
    Stack<String> stack = new Stack<>();
    String[] tokens = input.split(" ");

    for (String token : tokens) {
      if (")".equals(token)) {
        String last1 = stack.pop();
        String last2 = stack.pop();
        String last3 = stack.pop();
        stack.push("( " + last3 + last2 + last1 + " )");
      } else {
        stack.push(" " + token + " ");
      }
    }

    return stack.pop();
  }
}
