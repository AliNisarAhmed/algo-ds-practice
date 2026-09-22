
class Solution {
  trappingRainWater(heights: number[]): number {
    if (heights.length === 0) {
      return 0;
    }

    let left = 0;
    let leftMax = heights[left];
    let right = heights.length - 1;
    let rightMax = heights[right];
    let count = 0;

    while (left < right) {

      if (leftMax < rightMax) {
        left++;
        if (heights[left] >= heights[leftMax]) {
          leftMax = heights[left];
        } else {
          count += leftMax - heights[left];
        }
      } else {
        right++;
        if (heights[right] >= heights[rightMax]) {
          rightMax = heights[right];
        } else {
          count += rightMax - heights[right]
        }
      }
    }
    return count;
  }
}
