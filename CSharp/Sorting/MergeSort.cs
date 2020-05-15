using System;
using System.Collections.Generic;
using System.Text;

namespace CSharp.Sorting
{
    public static class MergeSort
    {
        public static int[] Sort(int[] arrayToSort)
        {
            // BASE CASE: arrays with fewer than 2 elements are sorted
            if (arrayToSort.Length < 2)
            {
                return arrayToSort;
            }

            // STEP 1: divide the array in half
            // We use integer division, so we'll never get a "half index"
            int midIndex = arrayToSort.Length / 2;

            int[] left = MakeSubarray(arrayToSort, 0, midIndex);
            int[] right = MakeSubarray(arrayToSort, midIndex, arrayToSort.Length);

            // STEP 2: sort each half
            int[] sortedLeft = Sort(left);
            int[] sortedRight = Sort(right);

            // STEP 3: merge the sorted halves
            int[] sortedArray = new int[arrayToSort.Length];

            int currentLeftIndex = 0;
            int currentRightIndex = 0;

            for (int currentSortedIndex = 0; currentSortedIndex < arrayToSort.Length;
                    currentSortedIndex++)
            {
                // sortedLeft's first element comes next
                // if it's less than sortedRight's first
                // element or if sortedRight is exhausted
                if (currentLeftIndex < sortedLeft.Length
                        && (currentRightIndex >= sortedRight.Length  // means right array is empty
                        || sortedLeft[currentLeftIndex] < sortedRight[currentRightIndex]))
                {
                    sortedArray[currentSortedIndex] = sortedLeft[currentLeftIndex];
                    currentLeftIndex++;
                }
                else
                {
                    sortedArray[currentSortedIndex] = sortedRight[currentRightIndex];
                    currentRightIndex++;
                }
            }

            return sortedArray;
        }

        public static T[] MakeSubarray<T>(T[] source, int begin, int end)
        {
            if (source == null)
            {
                throw new ArgumentNullException(nameof(source), "Source array is null");
            }

            if (begin > source.Length)
            {
                throw new ArgumentOutOfRangeException(nameof(begin),
                    "Begin index is too big");
            }

            if (end > source.Length)
            {
                throw new ArgumentOutOfRangeException(nameof(end),
                    "End index is too big");
            }

            if (begin > end)
            {
                throw new ArgumentOutOfRangeException(nameof(begin),
                    "Begin index is larger than end index");
            }

            T[] destination = new T[end - begin];
            if (destination.Length > 0)
            {
                Array.Copy(source, begin, destination, 0, destination.Length);
            }

            return destination;
        }
    }
}
