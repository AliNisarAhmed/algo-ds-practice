using CSharp.InterviewCake.GreedyAlgorithms;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Tests_CSharp
{
    public class HighestProductOf3Tests
    {
        [Fact]
        public void ShortArrayTest()
        {
            var actual = Greedy.HighestProductOf3(new int[] { 1, 2, 3, 4 });
            var expected = 24;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void LongerArrayTest()
        {
            var actual = Greedy.HighestProductOf3(new int[] { 6, 1, 3, 5, 7, 8, 2 });
            var expected = 336;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void ArrayHasOneNegativeTest()
        {
            var actual = Greedy.HighestProductOf3(new int[] { -5, 4, 8, 2, 3 });
            var expected = 96;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void ArrayHasTwoNegativesTest()
        {
            var actual = Greedy.HighestProductOf3(new int[] { -10, 1, 3, 2, -10 });
            var expected = 300;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void ArrayHasAllNegativesTest()
        {
            var actual = Greedy.HighestProductOf3(new int[] { -5, -1, -3, -2 });
            var expected = -6;
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void ExceptionWithEmptyArrayTest()
        {
            Assert.Throws<ArgumentException>(() => Greedy.HighestProductOf3(new int[] { }));
        }

        [Fact]
        public void ExceptionWithOneNumberTest()
        {
            Assert.Throws<ArgumentException>(() => Greedy.HighestProductOf3(new int[] { 1 }));
        }

        [Fact]
        public void ExceptionWithTwoNumbersTest()
        {
            Assert.Throws<ArgumentException>(() => Greedy.HighestProductOf3(new int[] { 1, 1 }));
        }

    }
}
