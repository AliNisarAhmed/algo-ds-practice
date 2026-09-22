import java.util;

class Solution {
  public boolean validParens(string s) {
    var stack = new Stack<Character>();
    var parenMap = new HashMap<Character, Character>();
    parenMap.put('}', '{');
    parenMap.put(']', '[');
    parenMap.put(')', '(');

    for (char c : s) {
      if (parenMap.containsKey(c)) {
        if (stack.isEmpty() || stack.peek() != mapping.get(c)) {
          return false;
        }
        stack.pop();
      } else {
        stack.push(c);
      }
    }
    return stack.isEmpty();
  }
}
