using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CSharp
{
    public static class BinarySearch
    {
        public static int Search<T>(IEnumerable<T> arr, T target) where T: IComparable
        {
            var left = 0;
            var right = arr.Count() - 1;

            int mid;

            while (left <= right)
            {
                mid = (left + right) / 2;
                var current = arr.ElementAt(mid);

                if (current.Equals(target))
                {
                    return mid;
                }
                else if (current.CompareTo(target) < 0)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                }
            }

            return -1;

        }
    
        // check how many times the smaller string m appears inside the bigger one s
        public static int NaiveStringSearch(string s, string m)
        {
            var count = 0;
            for (var i = 0; i < s.Length; i++)
            {
                if (s[i] == m[0])
                {
                    for (var j = 0; j < m.Length; j++)
                    {
                        if (s[i + j] != m[j])
                            break;
                    }
                    count++;
                }
            }
            return count;
        }
    }
}
