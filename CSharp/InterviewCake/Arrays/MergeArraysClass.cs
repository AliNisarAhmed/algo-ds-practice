using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace CSharp.InterviewCake.Arrays
{
    public static class MergeArraysClass
    {
        public static int[] MergeArrays(int[] first, int[] second)
        {
            var total = first.Length + second.Length;
            var result = new int[total];

            var i = 0;
            var j = 0;

            for (var k = 0; k < total; k++)
            {
                if (i == first.Length)
                {
                    // means we have exhausted first
                    if (j < second.Length)
                    {
                        result[k] = second[j];
                        j++;
                    }
                }
                else if (j == second.Length)
                {
                    if (i < first.Length)
                    {
                        result[k] = first[i];
                        i++;
                    }
                }
                else if (first[i] < second[j])
                {
                    result[k] = first[i];
                    i++;
                }
                else
                {
                    result[k] = second[j];
                    j++;
                }
            }

            return result;
        }
    
        public static int[] MergeMultipleArrays(int[][] arrays)
        {
            var dict = new Dictionary<int, int>();
            var total = 0;

            // declare individual counters
            for (var i = 0; i < arrays.Length; i++)
            {
                dict[i] = 0;
                total += arrays[i].Length;
            }

            var result = new int[total];

            for (var k = 0; k < total; k++)
            {
                var min = int.MaxValue;
                int minIndex = 0;

                foreach(var kvp in dict)
                {
                    if (kvp.Value < arrays[kvp.Key].Length && arrays[kvp.Key][kvp.Value] < min)
                    {
                        min = arrays[kvp.Key][kvp.Value];
                        minIndex = kvp.Key;
                    }
                }

                result[k] = min;
                dict[minIndex]++;
            }

            return result;
        }
    }
}
