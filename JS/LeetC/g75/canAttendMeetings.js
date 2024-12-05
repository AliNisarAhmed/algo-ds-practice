function canAttendMeetings(intervals) {
  intervals.sort(([a1, b1], [a2, b2]) => a1- a2);

  for (let i = 0; i < intervals.length - 1; i++) {
    let current = intervals[i];
    let next = intervals[i + 1];

    if (next[0] < current[1] || current[0] > next[1]) {
      return false;
    }
  }

  return true;
}
