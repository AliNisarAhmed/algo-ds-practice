using System;
using System.Collections.Generic;
using System.Linq;

namespace CSharp.LeetCode
{
    public class RemoveVowel
    {
		private static readonly char[] vowels = { 'a', 'e', 'i', 'o', 'u' };
        public string Method(string S) {
            return String.Concat(S.Where(c => !vowels.Contains(c)));
        }
    }
}