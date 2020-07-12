using CSharp.InterviewCake.Arrays;
using System;
using System.Collections.Generic;
using System.Text;
using Xunit;

namespace Tests_CSharp
{
    public class MergeArraysTest
    {
        [Fact]
        public void BothArraysAreEmptyTest()
        {
            var myArray = new int[] { };
            var alicesArray = new int[] { };
            var expected = new int[] { };
            var actual = MergeArraysClass.MergeArrays(myArray, alicesArray);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void FirstArrayIsEmptyTest()
        {
            var myArray = new int[] { };
            var alicesArray = new int[] { 1, 2, 3 };
            var expected = new int[] { 1, 2, 3 };
            var actual = MergeArraysClass.MergeArrays(myArray, alicesArray);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void SecondArrayIsEmptyTest()
        {
            var myArray = new int[] { 5, 6, 7 };
            var alicesArray = new int[] { };
            var expected = new int[] { 5, 6, 7 };
            var actual = MergeArraysClass.MergeArrays(myArray, alicesArray);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void BothArraysHaveSomeNumbersTest()
        {
            var myArray = new int[] { 2, 4, 6 };
            var alicesArray = new int[] { 1, 3, 7 };
            var expected = new int[] { 1, 2, 3, 4, 6, 7 };
            var actual = MergeArraysClass.MergeArrays(myArray, alicesArray);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void ArraysAreDifferentLengthsTest()
        {
            var myArray = new int[] { 2, 4, 6, 8 };
            var alicesArray = new int[] { 1, 7 };
            var expected = new int[] { 1, 2, 4, 6, 7, 8 };
            var actual = MergeArraysClass.MergeArrays(myArray, alicesArray);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void TEST_MERGE_MULTIPLE()
        {
            int[][] myArray = {
                new int[] { 1, 2, 3},
                new int[] {4, 5, 6},
                new int[] {7, 8, 9, 10}
            };

            var actual = MergeArraysClass.MergeMultipleArrays(myArray);
            var expected = new int[] { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10};

            Assert.Equal(expected, actual);
        }
    }
}
