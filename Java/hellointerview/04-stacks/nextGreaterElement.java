import java.util.Arrays;
import java.util.Stack;

class Solution {
  public int[] nextGreaterElement(int[] nums) {
    int n = nums.length;
    int[] result = new int[n];
    Arrays.fill(result, -1);
    Stack<Integer> stack = new Stack<>();

    for (int i = 0; i < n; i++) {
      while (!stack.empty() && nums[i] > nums[stack.peek()]) {
        var index = stack.pop();
        result[index] = nums[i];
      }
      stack.push(i);
    }

    return result;
  }
}
