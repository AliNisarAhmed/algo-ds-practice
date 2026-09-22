public class Solution {
  public int maxSubArraySum(int[] nums, int k) {
    int result = 0;
    int start = 0;
    int windowSum = 0;

    for (int end = 0; end < nums.length; end++) {
      windowSum += nums[end];

      if (end - start + 1 == k) {
        // if window size equals target size
        result = Math.max(result, windowSum);

        // now prepare for next iteration
        windowSum -= nums[start];
        start++;
      }
    }

    return result;
  }
}
