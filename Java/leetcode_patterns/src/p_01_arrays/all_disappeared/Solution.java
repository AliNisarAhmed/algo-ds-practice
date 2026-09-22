package p_01_arrays.all_disappeared;

import java.util.ArrayList;
import java.util.List;

class Solution {
  public List<Integer> findDisappearedNumbers(int[] nums) {
    for (int i = 0; i < nums.length; i++) {
      var index = Math.abs(nums[i]) - 1;
      if (nums[index] > 0) {
        nums[index] *= -1;
      }
    }

    List<Integer> result = new ArrayList<>();

    for (int i = 0; i < nums.length; i++) {
      if (nums[i] > 0) {
        result.add(i + 1);
      }
    }

    return result;
  }
}
