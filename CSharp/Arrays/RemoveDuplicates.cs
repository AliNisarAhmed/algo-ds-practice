using System;
using System.Linq;

namespace Arrays
{
	public class RemoveDuplicates
	{
		public int Solution(int[] nums)
		{
			if (nums.Length < 2)
			{
				return nums.Length;
			}

			int j = 1;

			for (int i = 1; i < nums.Length; i++)
			{
				if (nums[i] != nums[i - 1])
				{
					nums[j] = nums[i];
					j++;
				}
			}

			Array.Resize(ref nums, j);
			return nums.Length;
		}

		public int Solution2(int[] nums)
		{
			if (nums.Length == 0)
				return 0;
			// keep track of the last position we swapped the value with.

			int lastPosition = 0;

			for (int i = 0; i < nums.Length; i++)
			{

				if (nums[i] != nums[lastPosition])
					nums[++lastPosition] = nums[i];

			}

			return lastPosition + 1;
		}
	}
}