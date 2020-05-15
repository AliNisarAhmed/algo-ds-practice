using System;
using System.Collections.Generic;
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
    }
}
