using CSharp.InterviewCake.HashTables;
using System;
using System.Text;
using Xunit;
using CSharp.InterviewCake.Arrays;
using System.Collections.Generic;

namespace Tests_CSharp
{
    public class TopScoreSortTest
    {
        [Fact]
        public void NoScoresTest()
        {
            var scores = new int[] { };
            var expected = new int[] { };
            var actual = HashTableClass.SortScores(scores, 100);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void OneScoreTest()
        {
            var scores = new int[] { 55 };
            var expected = new int[] { 55 };
            var actual = HashTableClass.SortScores(scores, 100);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void TwoScoresTest()
        {
            var scores = new int[] { 30, 60 };
            var expected = new int[] { 60, 30 };
            var actual = HashTableClass.SortScores(scores, 100);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void ManyScoresTest()
        {
            var scores = new int[] { 37, 89, 41, 65, 91, 53 };
            var expected = new int[] { 91, 89, 65, 53, 41, 37 };
            var actual = HashTableClass.SortScores(scores, 100);
            Assert.Equal(expected, actual);
        }

        [Fact]
        public void RepeatedScoresTest()
        {
            var scores = new int[] { 20, 10, 30, 30, 10, 20 };
            var expected = new int[] { 30, 30, 20, 20, 10, 10 };
            var actual = HashTableClass.SortScores(scores, 100);
            Assert.Equal(expected, actual);
        }
    }
}
