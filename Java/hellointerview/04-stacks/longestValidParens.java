import java.util;

class Solution {
  public int longestValidParentheses(String s) {
    int maxLen = 0;
    int current = 0;
    var stack = new Stack<Character>();

    for (char c : s.toCharArray()) {
      if (c == '(') {
        stack.push(c);
        current = 0;
      } else if (!stack.isEmpty()) {
        current += stack.pop() + 2;
        maxLen = Math.max(current, maxLen);
      } else {
        current = 0;
      }
    }

    return maxLen;
  }
}
