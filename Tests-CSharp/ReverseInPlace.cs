using CSharp.InterviewCake.Arrays;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Tests_CSharp
{
    public class ReverseInPlaceTest
    {
        [Fact]
        public void Test1()
        {
            char[] arr = { 'a', 'b', 'c', 'd' };

            var actual = ReverseInPlace.Reverse(arr);

            char[] expected = { 'd', 'c', 'b', 'a' };

            Assert.Equal(actual, expected);
        }
    }
}
