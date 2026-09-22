package p_02_two_pointers.move_zeroes;

class Solution1 {
  public void moveZeroes(int[] nums) {
    int firstZero = 0;
    for (int i = 0; i < nums.length; i++) {
      if (nums[firstZero] != 0) {
        firstZero++;
      }
    }

    for (int i = firstZero + 1; i < nums.length; i++) {
      if (nums[i] != 0) {
        nums[firstZero] = nums[i];
        nums[i] = 0;
        firstZero++;
      }
    }

  }
}
