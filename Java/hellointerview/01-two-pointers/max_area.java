public class Solution {
  public Integer max_area(int[] heights) {
    var left = 0;
    var right = heights.length - 1;
    int maxArea = 0;

    while (left < right) {
      var current = (right - left) * (Math.min(heights[left], heights[right]));
      if (maxArea < current) {
        maxArea = current;
      }

      if (heights[left] < heights[right]) {
        left++;
      } else {
        right--;
      }
    }
    return maxArea;
  }
}
