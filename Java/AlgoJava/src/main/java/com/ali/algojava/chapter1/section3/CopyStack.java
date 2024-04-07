package com.ali.algojava.chapter1.section3;

import edu.princeton.cs.algs4.StdOut;

// 1.3.12
public class CopyStack {
  
  public static void main(String[] args) {
    Stack<String> stack = new Stack<>();
    stack.push("a");
    stack.push("b");
    stack.push("c");

    for (String s: stack) {
      StdOut.print(s);
    }
    StdOut.println();
    StdOut.println("After copy");

    Stack<String> copy = copy(stack);

    for (String s: stack) {
      StdOut.print(s);
    }

    StdOut.println();

    for (String s: copy) {
      StdOut.print(s);
    }

  }

  public static Stack<String> copy(Stack<String> input) {
    Stack<String> temp = new Stack<>();
    Stack<String> stack = new Stack<>();

    for (String s : input) {
      temp.push(s);
    }

    for (String s: temp) {
      stack.push(s);
    }

    return stack;
  }
}
