using System;
using System.Collections.Generic;
using System.Text;

namespace CSharp
{
    public class BubbleSort
    {
        public static void Sort(int[] arr)
        {
            for (var i = arr.Length - 1; i >= 0; i--)
            {
                var swaps = false;
                for (var j = 0; j < i - 1; j++)
                {
                    if (arr[j] > arr[j = 1])
                    {
                        Swap(arr, j, j + 1);
                        swaps = true;
                    }
                }
                if (swaps) break;
            }
        }

        public static void Swap(int[] arr, int i, int j)
        {
            if (i == j) return;
            var temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }
}
