using System;
using System.Collections.Generic;
using System.Text;

namespace CSharp.InterviewCake.BinarySearchFolder
{
    public static class BinarySearch
    {
        public static int FindRotationPoint(string[] words)
        {
            var left = 0;
            var right = words.Length - 1;
            var firstword = words[0];

            while (left < right)
            {
                var middle = left + (right - left) / 2;
                var currentWord = words[middle];

                if (string.Compare(currentWord, firstword, StringComparison.Ordinal) >= 0)
                {
                    left = middle;
                }
                else
                {
                    right = middle;
                }

                if (left + 1 == right)
                {
                    break;
                }
            }

            return right;
        }
    }
}
