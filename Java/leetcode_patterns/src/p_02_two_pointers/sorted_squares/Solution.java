package p_02_two_pointers.sorted_squares;

class Solution {
  public int[] sortedSquares(int[] nums) {
    var left = 0;
    var right = nums.length - 1;
    int[] result = new int[nums.length];

    for (int i = nums.length - 1; i >= 0; i--) {
      if (Math.abs(nums[left]) > Math.abs(nums[right])) {
        result[i] = nums[left] * nums[left];
        left++;
      } else {
        result[i] = nums[right] * nums[right];
        right--;
      }
    }

    return result;
  }

  public static void main(String[] args) {
    var s = new Solution();
    int[] nums = { -4, -1, 0, 3, 10 };
    var result = s.sortedSquares(nums);
  }
}

// 4, _, _, _, _, 16
// 1, _, _, _, 4, 16
// 1, _, _, 1, 4, 16
// 1, 1, _, 9, 4, 16
//
// while left < right
// if @left^2 > @right^2
// swap
// right--
// else
// left++

// -2 -1 1 2 3 4
// 4 16
// 1
//
// -4,
//
// -4, -1, 0, 2, 3
// 9, _, _, _, 16
// 4, _, _, 9, 16
// 0, _, 4, 9, 16
// 0, 1, 4, 9, 16
