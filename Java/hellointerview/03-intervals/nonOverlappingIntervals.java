import java.util;

class Solution {
  public int nonOverlappingIntervals(int[][] intervals) {
    if (intervals.length == 0) {
      return 0;
    }

    Arrays.sort(intervals, (a, b) -> a[1] - b[1]);

    int end = intervals[0][1];
    int count = 1;

    for (int i = 1; i < intervals.length; i++) {
      if (intervals[i][0] >= end) {
        end = intervals[i][1];
        count++;
      }
    }

    return intervals.length - count;
  }
}
