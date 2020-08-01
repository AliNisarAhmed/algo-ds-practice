using CSharp.LeetCode;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Tests_CSharp
{
    public class RomanToIntTest
    {
        [Fact]
        public void NoScoresTest()
        {
            var input = "IV";
            var expected = 4;
            var actual = RomanToInt.Solution(input);
            Assert.Equal(expected, actual);
        }
        
        [Fact]
        public void LVIII()
        {
            var input = "LVIII";
            var expected = 58;
            var actual = RomanToInt.Solution(input);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void MDCCCLXXXIV()
        {
            var input = "MDCCCLXXXIV";
            var expected = 1884;
            var actual = RomanToInt.Solution(input);
            Assert.Equal(expected, actual);
        }
    }
}
