function canAttendMeetings(intervals: number[][]): boolean {
  intervals.sort(([a1, b1], [a2, b2]) => a1 - a2);

  for (let i = 1; i < intervals.length; i++) {
    let [a1, b1] = intervals[i - 1];
    let [a2, b2] = intervals[i];
    if (a2 < b1 || a1 > b2) {
      return false;
    }
  }
  return true;
}
