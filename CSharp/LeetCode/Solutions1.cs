using System;
using System.Collections.Generic;
using System.Linq;

namespace CSharp.LeetCode
{
    public static class Solutions1
    {
        public static int[] RunningSum(int[] nums)
        {
            var result = new int[nums.Length];
            for (var i = 0; i < nums.Length; i++)
            {
                if (i == 0)
                {
                    result[i] = nums[i];
                }
                else
                {
                    result[i] = result[i - 1] + nums[i];

                }

            }

            return result;
        }

        public static IList<bool> KidsWithCandies(int[] candies, int extraCandies)
        {
            var max = candies.Max();
            return candies.Select(c => c + extraCandies >= max).ToList();
        }
    }
}