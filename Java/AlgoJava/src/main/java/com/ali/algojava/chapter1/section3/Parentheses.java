package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;

// 1.3.4
public class Parentheses {

  public static void main(String[] args) {
    String brackets = args[0];
    StdOut.println(isBalanced(brackets));
  }

  private static boolean isBalanced(String input) {
    char[] brackets = input.toCharArray();
    Stack<Character> stack = new Stack<>();

    for (char bracket : brackets) {
      if (isOpeningBracket(bracket)) {
        stack.push(bracket);
      } else {
        if (stack.isEmpty()) {
          return false;
        }
        char openingBracket = stack.pop();
        if (!matchingBracket(openingBracket, bracket)) {
          return false;
        }
      }
    }

    return stack.isEmpty();
  }

  private static boolean isOpeningBracket(char c) {
    return c == '{' || c == '[' || c == '(';
  }

  private static boolean matchingBracket(char opening, char closing) {
    return (opening == '[' && closing == ']') ||
        (opening == '{' && closing == '}') ||
        (opening == '(' && closing == ')');
  }
}
