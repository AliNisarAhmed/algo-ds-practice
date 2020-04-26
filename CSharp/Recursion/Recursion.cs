using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;

namespace CSharp
{
    public class Recursion
    {
        public static bool IsPalindrome(string str)
        {
            if (str.Length <= 1) return true;
            if (str[0] != str[str.Length - 1]) return false;

            return IsPalindrome(str.Substring(1, str.Length - 2));
        }

        public static bool SomeRecursive<T>(IEnumerable<T> arr, Func<T, bool> f)
        {
            if (arr.Count() == 0) return false;

            if (f(arr.First())) return true;

            return SomeRecursive(arr.Skip(1), f);
        }


        public static int Power(int b, int exp)
        {
            if (exp == 1) return 1;
            return b * Power(b, exp - 1);
        }

        public static int Factorial(int n) =>
            n <= 1 ? 1 : n * Factorial(n - 1);

        public static int ProductOfArray(IEnumerable<int> arr) =>
            arr.Count() == 0 ? 1 : arr.First() * ProductOfArray(arr.Skip(1));

        public static int RecursiveRange(int n) =>
            n == 0 ? 0 : n + RecursiveRange(n - 1);

        public static int Fib(int n)
        {
            if (n == 1 || n == 2) return 1;
            var first = 1;
            var second = 1;
            n -= 2;
            while(n > 0)
            {
                var temp = first;
                first = second;
                second += temp;
                n--;
            }
            return second;
        }

        public static string Reverse(string str) =>
            str == "" ? "" : Reverse(str.Substring(1)) + str[0];
        
    }
}
