import java.util;

class Solution {
  public int[][] insertIntervals(int[][] intervals, int[] newInterval) {
    List<int[]> result = new ArrayList<>();

    int i = 0;
    int n = intervals.length;

    while (i < n && intervals[i][0] < newInterval[0]) {
      result.add(intervals[i]);
      i++;
    }

    while (i < n && intervals[i][0] <= newInterval[1]) {
      newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
      newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
      i++;
    }

    result.add(newInterval);

    for (int j = i; j < n; j++) {
      results.add(intervals[j]);
    }

    return result.toArray(new int[result.size()][]);
  }
}
