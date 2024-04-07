package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;

// 1.3.11
public class EvaluatePostfix {

  public static void main(String[] args) {
    StdOut.print(evaluate("1 2 + 4 2 / *"));
  }

  public static Double evaluate(String input) {
    String[] tokens = input.split(" ");

    Stack<Double> stack = new Stack<>();

    for (String token : tokens) {
      if ("+-/*".contains(token)) {
        Double operand2 = stack.pop();
        Double operand1 = stack.pop();
        stack.push(evaluateExpression(operand1, operand2, token));
      } else {
        stack.push(Double.parseDouble(token));
      }
    }

    return stack.pop();
  }

  public static Double evaluateExpression(Double operand1, Double operand2,
      String token) {
    switch (token) {
      case "+":
        return operand1 + operand2;
      case "*":
        return operand1 * operand2;
      case "/":
        return operand1 / operand2;
      default:
        return operand1 - operand2;
    }
  }
}
