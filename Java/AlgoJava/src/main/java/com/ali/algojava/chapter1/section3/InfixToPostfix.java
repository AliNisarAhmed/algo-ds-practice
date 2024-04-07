package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;

public class InfixToPostfix {

  public static void main(String[] args) {
    String input = "( ( 1 + 2 ) * ( 4 / 2 ) )";
    StdOut.println(convert(input));
  }

  public static String convert(String input) {
    String[] tokens = input.split("\\s");

    Stack<String> operands = new Stack<>();
    Stack<String> operators = new Stack<>();

    for (String token : tokens) {
      if ("(".equals(token)) {
        // do nothing
      } else if ("+-/*".contains(token)) {
        operators.push(token);
      } else if (")".equals(token)) {
        String operand1 = operands.pop();
        String operand2 = operands.pop();
        String op = operators.pop();

        operands.push(operand2 + " " + operand1 + " " + op);
      } else {
        operands.push(token);
      }
    }

    return operands.pop();
  }
}
