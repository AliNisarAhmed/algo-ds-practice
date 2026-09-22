// 1,3  6,9 (2,5)
class Solution {
  insertIntervals(intervals: number[][], newInterval: number[]): number[][] {
    const merged: number[][] = [];

    let i = 0;
    const n = intervals.length;

    while (i < n && intervals[i][1] < newInterval[0]) {
      merged.push(intervals[i]);
      i++;
    }

    while (i < n && intervals[i][0] <= newInterval[1]) {
      newInterval[0] = Math.min(intervals[i][0], newInterval[0]);
      newInterval[1] = Math.max(intervals[i][1], newInterval[1]);
      i++;
    }

    merged.push(newInterval);

    while (i < n) {
      merged.push(intervals[i]);
      i++;
    }
    return merged;
  }

}
