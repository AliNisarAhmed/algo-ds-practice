import java.util.Arrays;

public class Solution {
  public Integer triangleNumber(int[] heights) {
    Arrays.sort(heights);

    int result = 0;

    for (int i = heights.length - 1; i >= 2; i--) {
      int left = 0;
      int right = i - 1;
      while (left < right) {
        if (heights[left] + heights[right] > heights[i]) {
          count += right - left;
          right--;
        } else {
          left++;
        }
      }
    }
    return count;
  }
}
