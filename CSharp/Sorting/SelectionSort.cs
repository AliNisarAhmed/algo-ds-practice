using System;
using System.Collections.Generic;
using System.Text;

namespace CSharp.Sorting
{
    public class SelectionSort
    {
        public static int[] Sort(int[] arr)
        {
            for (var i = 0; i < arr.Length; i++)
            {
                var min = i;

                for (var j = i + 1; j < arr.Length; j++)
                {
                    if (arr[j] < arr[min])
                    {
                        min = j;
                    }
                }

                if (min != i)
                {
                    var temp = arr[i];
                    arr[i] = arr[min];
                    arr[min] = temp;
                }
            }

            return arr;
        }
    }
}
