using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace CSharp.InterviewCake.Arrays
{
    public static class ReverseInPlace
    {
        public static char[] Reverse(char[] arr)
        {
            var i = 0;
            var j = arr.Length - 1;

            while (i < j)
            {
                var temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                i++;
                j--;
            }

            return arr;
        }
    
        public static char[] ReverseWords(char[] arr)
        {
            // ['I', ' ', 'a', 'm', ' ', 'A', 'l', 'i'];
            ReverseCharacters(arr, 0, arr.Length - 1); // reverse the whole array in place

            var currentStartIndex = 0;

            for (var i = 0; i <= arr.Length; i++)
            {
                if (i == arr.Length || arr[i] == ' ')
                {
                    ReverseCharacters(arr, currentStartIndex, i - 1);
                    currentStartIndex = i + 1;
                }
            }

            return arr;
        }

        public static void ReverseCharacters(char[] arr, int start, int end)
        {
            while (start < end)
            {
                var temp = arr[start];
                arr[start] = arr[end];
                arr[end] = temp;
                start++;
                end--;
            }
        }
    }
}
