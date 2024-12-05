def canAttendMeetings(intervals):
    intervals.sort()
    for i in range(len(intervals) - 1):
        current = intervals[i]
        next = intervals[i + 1]

        if current[1] > next[0]:
            return False

    return True
