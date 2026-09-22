public class Solution {
  public Boolean twoSum(int[] nums, Integer target) {
    int left = 0;
    int right = nums.length - 1;

    while (left < right) {
      var current = nums[left] + nums[right];
      if (current == target) {
        return true;
      } else if (current < target) {
        left++;
      } else {
        right--;
      }
    }
    return false;
  }

  public static void main(String[] args) {
    int[] nums = { 1, 3, 4, 6, 8, 10, 13 };
    var target = 13;
    var result = new Solution().twoSum(nums, target);
    System.out.println("result: " + result.toString());
  }

}
