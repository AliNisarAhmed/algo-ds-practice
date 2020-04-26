using CSharp.Sorting;
using System;
using System.Collections.Generic;

namespace CSharp
{
    class Program
    {
        static void Main(string[] args)
        {
            //Console.WriteLine(BinarySearch.NaiveStringSearch("hahaomghahaomg", "ha"));

            //LinqQueries.Run();
            int[] arr = { 7, 6, 5, 4, 3, 2};
            SelectionSort.Sort(arr);

            foreach(var b in arr)
            {
                Console.Write(b);
            }
        }
    }
}