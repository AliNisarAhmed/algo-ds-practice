package p_01_arrays.majority_element;

class Solution {
  public int majorityElement(int[] nums) {
    var candidate = nums[0];
    var count = 1;

    for (int i = 1; i < nums.length; i++) {
      if (nums[i] != candidate) {
        if (count == 0) {
          candidate = nums[i];
          count = 1;
        } else {
          count--;
        }
      } else {
        count++;
      }
    }

    return candidate;
  }
}
