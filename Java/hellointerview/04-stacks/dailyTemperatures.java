import java.util.Stack;

public class Solution {
  public int[] dailyTemperatures(int[] temps) {
    int n = temps.length;
    int[] result = new int[n];
    var stack = new Stack<Integer>();

    for (int i = 0; i < n; i++) {
      while (!stack.empty() && temps[i] > temps[stack.peek()]) {
        int index = stack.pop();
        result[index] = i - index;
      }
      stack.push(i);
    }

    return result;
  }
}
