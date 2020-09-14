using System;
using System.Collections.Generic;
using System.Text;
using Xunit;
using CSharp.InterviewCake.BinarySearchFolder;

namespace Tests_CSharp
{
    public class FindRotationPointTest
    {
        [Fact]
        public void SmallArrayTest()
        {
            var actual = BinarySearch.FindRotationPoint(new string[] { "cape", "cake" });
            var expected = 1;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void MediumArrayTest()
        {
            var actual = BinarySearch.FindRotationPoint(new string[] { "grape", "orange", "plum", "radish",
            "apple" });
            var expected = 4;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void LargeArrayTest()
        {
            var actual = BinarySearch.FindRotationPoint(
                new string[] { "ptolemaic", "retrograde", "supplant", "undulate", "xenoepist",
            "asymptote", "babka", "banoffee", "engender", "karpatka", "othellolagkage" });
            var expected = 5;
            Assert.Equal(expected, actual);
        }
    }
}
