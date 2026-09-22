import java.util;

public class Solution {
  public Long maxSum(int[] nums, Integer k) {

    var seen = new HashMap<Integer, Integer>();
    Long windowSum = 0;
    Long result = 0;
    int start = 0;

    for (int end = 0; end < nums.length; end++) {
      windowSum += nums[end];

      if (end - start + 1 == k) {
        if (seen.size() == k) {
          result = Math.max(result, windowSum);
        }

        windowSum -= nums[start];
        seen.put(nums[start], seen.get(nums[start]) - 1);
        if (seen.get(nums[start]) == 0) {
          seen.remove(nums[start]);
        }
        start++;
      }
    }
    return result;
  }
}
