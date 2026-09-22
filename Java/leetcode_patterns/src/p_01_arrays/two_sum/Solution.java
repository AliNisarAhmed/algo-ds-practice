package p_01_arrays.two_sum;

import java.util.HashMap;

class Solution {
  public int[] twoSum(int[] nums, int target) {
    var sums = new HashMap<Integer, Integer>();

    for (int i = 0; i < nums.length; i++) {
      if (sums.containsKey(target - nums[i])) {
        return new int[] { sums.get(target - nums[i]), i };
      }
      sums.put(nums[i], i);
    }

    return null;
  }
}
