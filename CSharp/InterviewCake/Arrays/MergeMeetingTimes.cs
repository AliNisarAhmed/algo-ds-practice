using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CSharp.InterviewCake.Arrays
{
    public static class MergeMeetingTimes
    {
        public static List<Meeting> MergeRanges(List<Meeting> meetings)
        {
            var sorted = meetings.Select(c => c).OrderBy(m => m.StartTime).ToList();

            var results = new List<Meeting> { sorted[0] };

            foreach (var m in sorted)
            {
                var last = sorted.Last();

                if (m.StartTime <= last.EndTime)
                {
                    last.EndTime =
                        Math.Max(m.EndTime, last.EndTime);
                }
                else
                {
                    // meetings dont merge, just push the current one into results
                    results.Add(m);
                }
            }

            return results;
        }
    }

    public class Meeting
    {
        public int StartTime { get; set; }

        public int EndTime { get; set; }

        public Meeting(int startTime, int endTime)
        {
            // Number of 30 min blocks past 9:00 am e.g. 9:30 is 1, 10 is 2
            StartTime = startTime;
            EndTime = endTime;
        }

        public override bool Equals(object obj)
        {
            if (obj == null || GetType() != obj.GetType())
            {
                return false;
            }

            if (ReferenceEquals(obj, this))
            {
                return true;
            }

            var meeting = (Meeting)obj;
            return StartTime == meeting.StartTime && EndTime == meeting.EndTime;
        }

        public override int GetHashCode()
        {
            var result = 17;
            result = result * 31 + StartTime;
            result = result * 31 + EndTime;
            return result;
        }

        public override string ToString()
        {
            return $"({StartTime}, {EndTime})";
        }
    }
}
