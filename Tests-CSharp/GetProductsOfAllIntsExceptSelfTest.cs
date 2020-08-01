using CSharp.InterviewCake.GreedyAlgorithms;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Tests_CSharp
{
    public class GetProductsOfAllIntsExceptSelfTest
    {
        [Fact]
        public void SmallArrayInputTest()
        {
            var expected = new int[] { 6, 3, 2 };
            var actual = Greedy.GetProductsOfAllIntsExceptAtIndex(new int[] { 1, 2, 3 });
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void LongArrayInputTest()
        {
            var expected = new int[] { 120, 480, 240, 320, 960, 192 };
            var actual = Greedy.GetProductsOfAllIntsExceptAtIndex(new int[] { 8, 2, 4, 3, 1, 5 });
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void InputHasOneZeroTest()
        {
            var expected = new int[] { 0, 0, 36, 0 };
            var actual = Greedy.GetProductsOfAllIntsExceptAtIndex(new int[] { 6, 2, 0, 3 });
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void InputHasTwoZerosTest()
        {
            var expected = new int[] { 0, 0, 0, 0, 0 };
            var actual = Greedy.GetProductsOfAllIntsExceptAtIndex(new int[] { 4, 0, 9, 1, 0 });
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void InputHasOneNegativeNumberTest()
        {
            var expected = new int[] { 32, -12, -24 };
            var actual = Greedy.GetProductsOfAllIntsExceptAtIndex(new int[] { -3, 8, 4 });
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void AllNegativesInputTest()
        {
            var expected = new int[] { -8, -56, -14, -28 };
            var actual = Greedy.GetProductsOfAllIntsExceptAtIndex(new int[] { -7, -1, -4, -2 });
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void ExceptionWithEmptyInputTest()
        {
            Assert.Throws<ArgumentException>(() => Greedy.GetProductsOfAllIntsExceptAtIndex(new int[] { }));
        }

        [Fact]
        public void ExceptionWithOneNumberInputTest()
        {
            Assert.Throws<ArgumentException>(() => Greedy.GetProductsOfAllIntsExceptAtIndex(new int[] { 1 }));
        }

        [Fact]
        public void MyArray1()
        {
            var expected = new int[] { 24, 30, 40, 60, 120 };
            var actual = Greedy.GetProductsOfAllIntsExceptAtIndex(new int[] { 5, 4, 3, 2, 1});
            Assert.Equal(expected, actual);
        }
    }
}
