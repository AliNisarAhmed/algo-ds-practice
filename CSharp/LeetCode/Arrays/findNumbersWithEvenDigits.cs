using System;
using System.Linq;

public class Solution
{
	public int FindNumbers(int[] nums)
	{
		return nums.Select(n => this.numDigit(n)).Where(n => n > 2).Count();
	}

	private int numDigit(int n)
	{
		var count = 0;
		while (n > 0)
		{
			n /= 10;
			count++;
		}
		return count;
	}
}

var s = new Solution();
s.FindNumbers([555,901,482,1771]);