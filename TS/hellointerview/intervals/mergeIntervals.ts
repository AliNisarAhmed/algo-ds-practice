class Solution {
  mergeIntervals(intervals: number[][]): number[][] {
    const merged: number[][] = [];
    // check 0 or 1 length edge case

    intervals.sort((a, b) => a[0] - b[0]);
    const n = intervals.length;

    for (const interval of intervals) {
      if (merged.length === 0 || interval[0] > merged[merged.length - 1][1]) {
        merged.push(interval);
      } else {
        merged[merged.length - 1][1] = Math.max(merged[merged.length - 1][1], interval[1]);
      }
    }

    return merged;
  }
}
