import java.util;

public class Solution {
  public String decodeString(String s) {
    var stringStack = new Stack();
    var numStack = new Stack();
    var currString = "";
    var currNumber = 0;

    for (char c : s.toCharArray()) {
      if (c == '[') {
        stringStack.push(currString);
        numStack.push(currNumber);
        currString = "";
        currNumber = 0;
      } else if (c == ']') {
        int num = numStack.pop();
        String prevString = stringStack.pop();
        currString = prevString + currString.repeat(num);
      } else if (Character.isDigit(c)) {
        currNumber = currNumber * 10 + (c - '0');
      } else {
        currString += c;
      }
    }
    return currString;
  }
}
