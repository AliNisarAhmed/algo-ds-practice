
class Solution {
  triangleNumber(heights: number[]): number {
    let count = 0;

    for (let i = heights.length - 1; i >= 2; i--) {
      let left = 0;
      let right = i - 1;

      while (left > right) {
        if (heights[left] + heights[right] > heights[i]) {
          // valid triangle
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
