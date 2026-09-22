package p_01_arrays.contains_dup;

import java.util.HashSet;

class Solution {
  public boolean containsDuplicate(int[] nums) {
    var seen = new HashSet<Integer>();

    for (int i = 0; i < nums.length; i++) {
      if (seen.contains(nums[i])) {
        return true;
      }
      seen.add(nums[i]);
    }

    return false;
  }
}
