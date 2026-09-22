class Solution {
  public void sortColors(int[] nums) {
    int left = 0, right = nums.length - 1;
    int i = 0;

    while (i <= right) {
      if (nums[i] == 0) {
        int temp = nums[i];
        nums[i] = nums[left];
        nums[left] = temp;
        left++;
        i++;
      } else if (nums[i] == 2) {
        int temp = nums[i];
        nums[i] = nums[right];
        nums[right] = temp;
        right--;
      } else {
        i++;
      }
    }
  }
}
