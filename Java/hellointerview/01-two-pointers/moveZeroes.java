public class Solution {
  public void moveZeroes(int[] nums) {
    int currentNonZeroSpot = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[i] != 0) {
        var temp = nums[i];
        nums[i] = nums[currentNonZeroSpot];
        nums[currentNonZeroSpot] = temp;
        currentNonZeroSpot++;
      }
    }
  }
}
