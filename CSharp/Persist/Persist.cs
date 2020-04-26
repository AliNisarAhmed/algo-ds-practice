using System;

public class Persist
{
	public static int Persistence(long n)
	{
		var count = 0;
		while(n % 10 != n)
		{
			n = MultiplyDigits(n);
			count++;
		}
		return count;
	}

	public static long MultiplyDigits(long n)
	{
		long sum = 1;
		while (n != 0)
		{
			sum *= (n % 10);
			n /= 10;
		}
		return sum;
	}
}