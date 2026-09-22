class Solution {
  public static int trappingWater(int[] heights) {
    if (heights.length == 0) {
      return 0;
    }
    int left = 0;
    int right = heights.length - 1;
    int leftMax = heights[left];
    int rightMax = heights[right];
    int result = 0;

    while (left < right) {
      if (leftMax < rightMax) {
        left++;
        if (heights[left] > leftMax) {
          leftMax = heights[left];
        } else {
          count += leftMax - heights[left];
        }
      } else {
        right--;
        if (heights[right] >= rightMax) {
          rightMax = heights[right];
        } else {
          count += rightMax - heights[right];
        }
      }
    }
  }
}
