import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Solution {
  public int[][] mergeIntervals(int[][] intervals) {
    Arrays.sort(intervals, (a, b) -> a[0] - b[0]);
    List<int[]> merged = new ArrayList<>();

    for (int[] interval : intervals) {
      if (merged.isEmpty() || interval[0] > merged.get(merged.size() - 1)[1]) {
        // intervals don't overlap
        merged.add(interval);
      } else {
        // intervals overlap
        merged.get(merged.size() - 1)[1] = Math.max(interval[1], merged.get(merged.size() - 1)[1]);
      }
    }

    return merged.toArray(new int[merged.size()]);
  }
}
